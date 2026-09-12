"""Reviewed-only transfer of the retained candidate archive; never run by preparation."""
import argparse
import ast
import hashlib
import json
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE = "dc53bcfed67b3bbea7d2fbf82468342e573dadb3"
IID = "sha256:a91994bf883698d4520ff048d16be999d4614331a528c76c0b95bc6dc8bec803"
TAG = "omniroute-auto-switch-r2:" + SOURCE
BUILDER_ARCHIVE = "/var/tmp/omniroute-auto-switch-image-transfer-20260912/image.tar"
ARCHIVE_BYTES = 1117870592
ARCHIVE_SHA256 = "ef45e7734e64280cbe9ca9bbbd8a950f350c028c50e9b02c55ab0e48801abb15"
TARGET_ROOT = "/var/tmp/omniroute-auto-switch-image-transfer-r4-20260912"
LOCAL = ROOT / "scripts/auto-switch-image-transfer-r4-20260912"
CONTRACT = ROOT / "docs/auto-switch-image-transfer-contract-r4-20260912.md"
HELPER = ROOT / "scripts/auto-switch-oci-identity-20260912.py"
HELPER_SHA256 = "7f822582a2ef5ce6c515ba002c7523b787cc3703e255ce5ec1cd0dca6bfc662a"
ROOT_DIAGNOSIS = ROOT / "scripts/auto-switch-containerd-root-diagnosis-20260912.py"
ROOT_DIAGNOSIS_SHA256 = "8e34792fa2a91297e5154589fca519c38f71123470aeaedc2cf50eb0b016ae2e"
ROOT_RESULT = ROOT / "docs/auto-switch-containerd-root-diagnosis-result-20260912.md"
ROOT_RESULT_SHA256 = "10310a6939409723af636e4088378443dc3ac423d02fd2f02ecbaf8e10cb43ca"
OLD_SPENT_LAUNCHER_SHA256 = "7776a680ade8940ece3a47dc5feb154e0ef27209a07897674d309ea6f7822279"
SSH = r"C:\WINDOWS\System32\OpenSSH\ssh.exe"
SCP = r"C:\WINDOWS\System32\OpenSSH\scp.exe"


class Stop(Exception):
    pass


def sha256(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def ssh_options(host):
    return ["-F", "none", "-i", r"C:\Users\chatc\.ssh\codex-prox01-vms-ed25519",
            "-o", "IdentitiesOnly=yes", "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=yes",
            "-o", "UserKnownHostsFile=C:/Users/chatc/.ssh/known_hosts", "-o", "GlobalKnownHostsFile=none",
            "-o", "HostKeyAlias=" + host, "-o", "ConnectTimeout=10", "-o", "ConnectionAttempts=1",
            "-o", "ServerAliveInterval=10", "-o", "ServerAliveCountMax=2"]


def run(stage, args, payload=None, timeout=1800):
    try:
        result = subprocess.run(args, input=payload, capture_output=True, timeout=timeout)
    except subprocess.TimeoutExpired as error:
        raise Stop(stage + ":timeout") from error
    if result.returncode:
        try:
            value = json.loads(result.stdout)
            if set(value) == {"stop"} and isinstance(value["stop"], str) and re.fullmatch(r"[a-z_]{1,64}", value["stop"]):
                raise Stop(stage + ":" + value["stop"])
        except (ValueError, TypeError):
            pass
        raise Stop(stage + ":command_failed:" + str(result.returncode))
    return result.stdout


REMOTE = r'''
import hashlib,json,os,pathlib,re,shutil,subprocess,sys
role,archive,expected_size,expected_sha,iid,tag,target=sys.argv[1:]
TARGET_ROLES=('target-preflight','target-load')
assert role in ('builder',)+TARGET_ROLES
check='initial'
def cmd(args, timeout=120):
 r=subprocess.run(args,capture_output=True,timeout=timeout)
 if r.returncode: raise AssertionError('command')
 return r.stdout.decode()
def docker(args, timeout=120): return cmd((['sudo','-n'] if role in TARGET_ROLES else [])+['docker']+args,timeout)
def file_hash(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1048576),b''): h.update(b)
 return h.hexdigest()
def require_private(p, present):
 q=pathlib.Path(p)
 assert q.exists() is present and not q.is_symlink()
 if present:
  s=q.stat(); assert s.st_uid==os.getuid() and s.st_mode&0o777==0o700
 return q
def verify_containerd_capacity():
 global check
 check='containerd_probe'
 r=subprocess.run(['sudo','-n','python3','-'],input=root_script.encode('utf-8'),capture_output=True,timeout=60)
 assert r.returncode==0
 value=json.loads(r.stdout)
 names=('process_identity','argv_parse','native_config_dump','runtime_fd_root','source_runtime_match','all_root_capacity')
 assert set(value)=={'driver','daemon_count','root_source','checks','returncodes'}
 assert value['driver']=='containerd_snapshotter' and type(value['daemon_count']) is int and 1<=value['daemon_count']<=8
 assert value['root_source'] in ('config_dump','explicit_override','mixed')
 assert set(value['checks'])==set(names)
 for name in names:
  check='containerd_'+name
  assert value['checks'][name]=='PASS'
 codes=value['returncodes']; check='containerd_returncodes'
 assert set(codes)=={'docker_driver','config_dump','capacity'} and type(codes['docker_driver']) is int and codes['docker_driver']==0
 assert len(codes['config_dump'])==value['daemon_count'] and 1<=len(codes['capacity'])<=value['daemon_count']
 assert all(type(x) is int and x==0 for x in codes['config_dump']+codes['capacity'])
def capacity(size):
 global check
 assert size==1117870592
 verify_containerd_capacity()
 check='docker_root_metadata'
 paths=['/var/tmp',docker(['info','--format','{{.DockerRootDir}}']).strip()]
 for p in paths:
  check='var_tmp_capacity' if p=='/var/tmp' else 'docker_root_capacity'
  assert pathlib.Path(p).is_absolute()
  line=cmd(['sudo','-n','df','-Pk','--',p],20).splitlines()
  assert len(line)==2 and int(line[1].split()[3])*1024>=size*2+1073741824
 return True
def absent():
 rows=docker(['image','ls','--all','--no-trunc','--format','{{.ID}} {{.Repository}}:{{.Tag}}']).splitlines()
 assert all(not r.startswith(iid+' ') and not r.endswith(' '+tag) for r in rows)
 for ref in [iid,tag]:
  r=subprocess.run((['sudo','-n'] if role in TARGET_ROLES else [])+['docker','image','inspect',ref],capture_output=True,timeout=20)
  allowed=(b'Error response from daemon: No such image: '+ref.encode(),b'Error: No such image: '+ref.encode())
  assert r.returncode==1 and r.stdout==b'[]\n' and r.stderr.strip() in allowed
def live():
 row=json.loads(docker(['inspect','omniroute']))[0]
 assert row['Id']=='7b20ca195e3c9e875d0a1ce98832ca469c2a114886335b8466b1467b3ed139bc'
 assert row['Image']=='sha256:60ab56311d1c9873416dc53683148d314465370312547b8ce87c442ce084c6a5'
 assert row['State']['Running'] is True
def image():
 row=json.loads(docker(['image','inspect',tag]))[0]
 assert row['Id']==iid and row['RepoTags']==[tag]
try:
 if role=='builder':
  check='builder_archive'
  p=pathlib.Path(archive); assert p.is_file() and not p.is_symlink()
  size=p.stat().st_size; assert size>0
  sha=file_hash(p); assert size==int(expected_size) and sha==expected_sha
  print(json.dumps({'size':size,'sha256':sha}))
 elif role=='target-preflight':
  check='target_path'; require_private(target,False)
  check='image_absence'; absent()
  check='live_container'; live()
  print(json.dumps({'containerd_path_proven':capacity(int(expected_size))}))
 elif role=='target-load':
  check='target_archive'
  p=require_private(target,True)/'image.tar'; assert p.is_file() and not p.is_symlink()
  assert p.stat().st_size==int(expected_size) and file_hash(p)==expected_sha
  check='image_absence'; absent()
  check='live_container'; live()
  assert capacity(int(expected_size))
  check='image_load'; docker(['load','--input',str(p)],1800)
  check='postload_identity'; image()
  check='live_container'; live()
  print(json.dumps({'image':iid,'tag':tag}))
 else: raise AssertionError('role')
except Exception:
 print(json.dumps({'stop':check})); raise SystemExit(1)
'''


def root_script_bytes():
    assert ROOT_DIAGNOSIS.is_file() and not ROOT_DIAGNOSIS.is_symlink()
    assert sha256(ROOT_DIAGNOSIS) == ROOT_DIAGNOSIS_SHA256
    tree = ast.parse(ROOT_DIAGNOSIS.read_text(encoding="utf-8"))
    values = [ast.literal_eval(node.value) for node in tree.body if isinstance(node, ast.Assign)
              and any(isinstance(target, ast.Name) and target.id == "REMOTE" for target in node.targets)]
    assert len(values) == 1 and isinstance(values[0], str)
    return values[0]


def remote(stage, host, role, archive, size=0, digest="none"):
    args = [SSH, "-T", *ssh_options(host), "belladmin@" + host, "python3", "-", role,
            archive, str(size), digest, IID, TAG, TARGET_ROOT]
    payload = ("root_script=" + repr(root_script_bytes()) + "\n" + REMOTE).encode("utf-8")
    return json.loads(run(stage, args, payload, 2400 if role == "target-load" else 1800))


def review_payload():
    return {"schema": "auto-switch-image-transfer-r4/v1", "source": SOURCE, "image": IID,
            "tag": TAG, "builder_archive": BUILDER_ARCHIVE, "archive_bytes": ARCHIVE_BYTES,
            "archive_sha256": ARCHIVE_SHA256, "target_root": TARGET_ROOT,
            "launcher_sha256": sha256(pathlib.Path(__file__)), "contract_sha256": sha256(CONTRACT),
            "oci_helper_sha256": sha256(HELPER), "root_diagnosis_sha256": sha256(ROOT_DIAGNOSIS),
            "root_result_sha256": sha256(ROOT_RESULT), "old_spent_launcher_sha256": OLD_SPENT_LAUNCHER_SHA256}


def verify_review(path):
    assert all(p.is_file() and not p.is_symlink() for p in (HELPER, ROOT_DIAGNOSIS, ROOT_RESULT, CONTRACT))
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload == review_payload() and payload["oci_helper_sha256"] == HELPER_SHA256
    assert payload["root_diagnosis_sha256"] == ROOT_DIAGNOSIS_SHA256
    assert payload["root_result_sha256"] == ROOT_RESULT_SHA256


def verify_archive_with_helper(host, archive):
    harness = HELPER.read_bytes() + ("\nimport sys,tarfile\nwith tarfile.open(sys.argv[1],'r:') as b:\n print(validate_image_archive(b,sys.argv[2],sys.argv[3]))\n").encode()
    output = run("oci_graph", [SSH, "-T", *ssh_options(host), "belladmin@" + host,
                                "python3", "-", archive, IID, TAG], harness, 180)
    if output.strip() not in (b"config", b"oci_descriptor"):
        raise Stop("oci_graph:identity_failed")


def execute(reviewed, preflight_only=False):
    verify_review(reviewed)
    if sha256(HELPER) != HELPER_SHA256:
        raise Stop("pins:oci_helper_drift")
    info = remote("builder_archive_pin", "192.168.1.147", "builder", BUILDER_ARCHIVE,
                  ARCHIVE_BYTES, ARCHIVE_SHA256)
    if set(info) != {"size", "sha256"} or type(info["size"]) is not int or info["size"] <= 0:
        raise Stop("builder_archive_metadata:invalid")
    if info != {"size": ARCHIVE_BYTES, "sha256": ARCHIVE_SHA256}:
        raise Stop("builder_archive_pin:mismatch")
    verify_archive_with_helper("192.168.1.147", BUILDER_ARCHIVE)
    if LOCAL.exists() or LOCAL.is_symlink(): raise Stop("local_path_absence:failed")
    if shutil.disk_usage(ROOT).free < info["size"] * 2 + 1073741824: raise Stop("local_capacity:failed")
    target = remote("target_preflight", "192.168.1.68", "target-preflight", "none", info["size"])
    if target != {"containerd_path_proven": True}: raise Stop("target_containerd_metadata:unproven")
    if preflight_only:
        print(json.dumps({"status":"IMAGE_TRANSFER_R4_PREFLIGHT_PASS","image":IID,"size":ARCHIVE_BYTES,"sha256":ARCHIVE_SHA256},sort_keys=True))
        return
    LOCAL.mkdir(mode=0o700)
    archive = LOCAL / "image.tar"
    run("download", [SCP, *ssh_options("192.168.1.147"), "belladmin@192.168.1.147:" + BUILDER_ARCHIVE, str(archive)])
    if archive.stat().st_size != info["size"] or sha256(archive) != info["sha256"]: raise Stop("download_hash:failed")
    run("target_prepare", [SSH, "-T", *ssh_options("192.168.1.68"), "belladmin@192.168.1.68", "mkdir", "-m", "700", TARGET_ROOT])
    run("upload", [SCP, *ssh_options("192.168.1.68"), str(archive), "belladmin@192.168.1.68:" + TARGET_ROOT + "/image.tar"])
    result = remote("target_load", "192.168.1.68", "target-load", "none", info["size"], info["sha256"])
    if result != {"image": IID, "tag": TAG}: raise Stop("postload_identity:failed")
    print(json.dumps({"status":"IMAGE_TRANSFER_R4_PASS","size":info["size"],"sha256":info["sha256"],**result},sort_keys=True))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--render-review-payload", action="store_true")
    parser.add_argument("--execute-reviewed", type=pathlib.Path)
    parser.add_argument("--preflight-reviewed", type=pathlib.Path)
    args = parser.parse_args()
    assert sum((args.render_review_payload, bool(args.execute_reviewed), bool(args.preflight_reviewed))) == 1
    if args.render_review_payload:
        print(json.dumps(review_payload(), sort_keys=True, indent=2))
    elif args.preflight_reviewed:
        execute(args.preflight_reviewed, preflight_only=True)
    else:
        execute(args.execute_reviewed)


if __name__ == "__main__":
    try: main()
    except Exception as error:
        stage = str(error).split(":", 1)[0] if isinstance(error, Stop) else "validation"
        detail = str(error).split(":", 1)[1] if isinstance(error, Stop) and ":" in str(error) else "unexpected"
        print(json.dumps({"status":"IMAGE_TRANSFER_R4_STOP","stage":stage,"reason":type(error).__name__,"detail":detail,"hint":"TIMEOUT" if isinstance(error,Stop) and "timeout" in str(error) else "STAGE_FAILED"}))
        sys.exit(1)
