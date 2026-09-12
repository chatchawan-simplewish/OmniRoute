"""Reviewed-only transfer of the retained candidate archive; never run by preparation."""
import argparse
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
TARGET_ROOT = "/var/tmp/omniroute-auto-switch-image-transfer-r2-20260912"
LOCAL = ROOT / "scripts/auto-switch-image-transfer-r2-20260912"
CONTRACT = ROOT / "docs/auto-switch-image-transfer-contract-r2-20260912.md"
HELPER = ROOT / "scripts/auto-switch-oci-identity-20260912.py"
HELPER_SHA256 = "6bf5248b2859b87bc422784342751aa7b91ae95ed530039e7da6f11b6c7eca01"
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
        raise Stop(stage + ":command_failed:" + str(result.returncode))
    return result.stdout


REMOTE = r'''
import hashlib,json,os,pathlib,re,shutil,subprocess,sys
role,archive,expected_size,expected_sha,iid,tag,target=sys.argv[1:]
def cmd(args, timeout=120):
 r=subprocess.run(args,capture_output=True,timeout=timeout)
 if r.returncode: raise AssertionError('command')
 return r.stdout.decode()
def docker(args): return cmd((['sudo','-n'] if role=='target' else [])+['docker']+args)
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
def derived_containerd_root():
 # Docker documents that the containerd store is separate.  Its path must come
 # from the running daemon metadata, never a default literal.
 status=docker(['info','--format','{{json .DriverStatus}}'])
 rows=json.loads(status)
 if not any(x[0]=='driver-type' and x[1]=='io.containerd.snapshotter.v1' for x in rows): return None
 ps=cmd(['sudo','-n','ps','-eo','args='],20).splitlines()
 matches=[x for x in ps if re.search(r'(^|/)containerd( |$)',x) and '--config ' in x]
 assert len(matches)==1
 config=re.search(r'--config\\s+([^\\s]+)',matches[0]).group(1)
 assert config.startswith('/') and pathlib.Path(config).is_file()
 root=None
 for line in pathlib.Path(config).read_text(encoding='utf-8').splitlines():
  hit=re.fullmatch(r'\\s*root\\s*=\\s*"([^"]+)"\\s*',line)
  if hit: root=hit.group(1); break
 assert root and root.startswith('/')
 return root
def capacity(size):
 assert size>0
 paths=['/var/tmp',docker(['info','--format','{{.DockerRootDir}}']).strip()]
 containerd=derived_containerd_root()
 if containerd: paths.append(containerd)
 for p in paths:
  assert pathlib.Path(p).is_absolute()
  line=cmd(['sudo','-n','df','-Pk','--',p],20).splitlines()
  assert len(line)==2 and int(line[1].split()[3])*1024>=size*2+1073741824
 return bool(containerd)
def absent():
 rows=docker(['image','ls','--all','--no-trunc','--format','{{.ID}} {{.Repository}}:{{.Tag}}']).splitlines()
 assert all(not r.startswith(iid+' ') and not r.endswith(' '+tag) for r in rows)
 for ref in [iid,tag]:
  r=subprocess.run((['sudo','-n'] if role=='target' else [])+['docker','image','inspect',ref],capture_output=True,timeout=20)
  assert r.returncode==1 and r.stdout==b'[]\\n'
def live():
 row=json.loads(docker(['inspect','omniroute']))[0]
 assert row['Id']=='7b20ca195e3c9e875d0a1ce98832ca469c2a114886335b8466b1467b3ed139bc'
 assert row['Image']=='sha256:60ab56311d1c9873416dc53683148d314465370312547b8ce87c442ce084c6a5'
 assert row['State']['Running'] is True
def image():
 row=json.loads(docker(['image','inspect',tag]))[0]
 assert row['Id']==iid and row['RepoTags']==[tag]
if role=='builder':
 p=pathlib.Path(archive); assert p.is_file() and not p.is_symlink()
 size=p.stat().st_size; assert size>0
 print(json.dumps({'size':size,'sha256':file_hash(p),'containerd_path_proven':capacity(size)}))
elif role=='target-preflight':
 require_private(target,False); absent(); live(); print(json.dumps({'containerd_path_proven':capacity(int(expected_size))}))
elif role=='target-load':
 p=require_private(target,True)/'image.tar'; assert p.is_file() and not p.is_symlink()
 assert p.stat().st_size==int(expected_size) and file_hash(p)==expected_sha
 absent(); live(); assert capacity(int(expected_size))
 docker(['load','--input',str(p)]); image(); live(); print(json.dumps({'image':iid,'tag':tag}))
else: raise AssertionError('role')
'''


def remote(stage, host, role, archive, size=0, digest="none"):
    args = [SSH, "-T", *ssh_options(host), "belladmin@" + host, "python3", "-", role,
            archive, str(size), digest, IID, TAG, TARGET_ROOT]
    return json.loads(run(stage, args, REMOTE.encode("utf-8")))


def review_payload():
    return {"schema": "auto-switch-image-transfer-r2/v1", "source": SOURCE, "image": IID,
            "tag": TAG, "builder_archive": BUILDER_ARCHIVE, "target_root": TARGET_ROOT,
            "launcher_sha256": sha256(pathlib.Path(__file__)), "contract_sha256": sha256(CONTRACT),
            "oci_helper_sha256": sha256(HELPER), "old_spent_launcher_sha256": OLD_SPENT_LAUNCHER_SHA256}


def verify_review(path):
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload == review_payload() and payload["oci_helper_sha256"] == HELPER_SHA256


def verify_archive_with_helper(host, archive):
    harness = HELPER.read_bytes() + ("\nimport sys,tarfile\nwith tarfile.open(sys.argv[1],'r:') as b:\n print(validate_image_archive(b,sys.argv[2],sys.argv[3]))\n").encode()
    output = run("oci_graph", [SSH, "-T", *ssh_options(host), "belladmin@" + host,
                                "python3", "-", archive, IID, TAG], harness, 180)
    if output.strip() not in (b"config", b"oci_descriptor"):
        raise Stop("oci_graph:identity_failed")


def execute(reviewed):
    verify_review(reviewed)
    if sha256(HELPER) != HELPER_SHA256:
        raise Stop("pins:oci_helper_drift")
    info = remote("builder_read", "192.168.1.147", "builder", BUILDER_ARCHIVE)
    if not info["containerd_path_proven"]:
        raise Stop("builder_read:containerd_path_unproven")
    if not re.fullmatch(r"[0-9a-f]{64}", info["sha256"]): raise Stop("builder_read:hash_invalid")
    verify_archive_with_helper("192.168.1.147", BUILDER_ARCHIVE)
    if LOCAL.exists() or LOCAL.is_symlink(): raise Stop("local_prepare:path_not_absent")
    if shutil.disk_usage(ROOT).free < info["size"] * 2 + 1073741824: raise Stop("local_prepare:capacity")
    target = remote("target_preflight", "192.168.1.68", "target-preflight", "none", info["size"])
    if not target["containerd_path_proven"]: raise Stop("target_preflight:containerd_path_unproven")
    LOCAL.mkdir(mode=0o700)
    archive = LOCAL / "image.tar"
    run("download", [SCP, *ssh_options("192.168.1.147"), "belladmin@192.168.1.147:" + BUILDER_ARCHIVE, str(archive)])
    if archive.stat().st_size != info["size"] or sha256(archive) != info["sha256"]: raise Stop("download:hash_mismatch")
    run("target_prepare", [SSH, "-T", *ssh_options("192.168.1.68"), "belladmin@192.168.1.68", "mkdir", "-m", "700", TARGET_ROOT])
    run("upload", [SCP, *ssh_options("192.168.1.68"), str(archive), "belladmin@192.168.1.68:" + TARGET_ROOT + "/image.tar"])
    result = remote("target_load", "192.168.1.68", "target-load", "none", info["size"], info["sha256"])
    print(json.dumps({"status":"IMAGE_TRANSFER_R2_PASS","size":info["size"],"sha256":info["sha256"],**result},sort_keys=True))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--render-review-payload", action="store_true")
    parser.add_argument("--execute-reviewed", type=pathlib.Path)
    args = parser.parse_args()
    assert args.render_review_payload != bool(args.execute_reviewed)
    if args.render_review_payload:
        print(json.dumps(review_payload(), sort_keys=True, indent=2))
    else:
        execute(args.execute_reviewed)


if __name__ == "__main__":
    try: main()
    except Exception as error:
        stage = str(error).split(":", 1)[0] if isinstance(error, Stop) else "validation"
        print(json.dumps({"status":"IMAGE_TRANSFER_R2_STOP","stage":stage,"reason":type(error).__name__,"hint":"TIMEOUT" if isinstance(error,Stop) and "timeout" in str(error) else "CHECK_FAILED"}))
        sys.exit(1)
