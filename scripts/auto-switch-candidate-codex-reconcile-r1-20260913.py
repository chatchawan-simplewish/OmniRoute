"""Prepare a read-only reconciliation of the R4 candidate and Codex row."""
import argparse
import ast
import base64
import hashlib
import importlib.util
import inspect
import json
import os
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parents[1]
COORDINATOR = pathlib.Path(r"C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-auto-switch-20260912")
RECONCILE_ROOT = pathlib.Path(r"C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-candidate-reconcile-20260913")
ROLLOUT_ROOT = pathlib.Path(r"C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-live-rollout-20260913")
TRANSPORT = COORDINATOR / "scripts/auto-switch-image-transfer-r3-20260913.py"
RECONCILE = RECONCILE_ROOT / "scripts/auto-switch-candidate-reconcile-r2-20260913.py"
RECONCILE_RESULT = RECONCILE_ROOT / "docs/auto-switch-candidate-reconcile-r2-result-20260913.md"
DEACTIVATION = ROOT / "scripts/auto-switch-candidate-codex-deactivate-r1-20260913.py"
DEACTIVATION_RESULT = ROOT / "docs/auto-switch-candidate-codex-deactivate-r1-result-20260913.json"
DEACTIVATION_EVIDENCE = ROLLOUT_ROOT / "docs/auto-switch-candidate-codex-deactivate-r1-evidence-review-20260913.md"
DIAGNOSIS = ROOT / "docs/auto-switch-candidate-codex-deactivate-r1-stop-diagnosis-20260913.md"
TEST = ROOT / "scripts/test-auto-switch-candidate-codex-reconcile-r1-20260913.py"
CONTRACT = ROOT / "docs/auto-switch-candidate-codex-reconcile-r1-contract-20260913.md"
RESULT = ROOT / "docs/auto-switch-candidate-codex-reconcile-r1-result-20260913.json"

TRANSPORT_SHA256 = "78bb97e57d6229aae84c2f0d0caaf68eeb71ba6b92e69415d83af2a869b8224a"
RECONCILE_SHA256 = "5bf842eba4b12da90acc6ede36b1db62fc8b2df23d1343b2879038df7d17a779"
RECONCILE_RESULT_SHA256 = "7efe1cb83cc1c5c6cf85199b919338bb2a6143054d9a6cd315e0c3270fc213cf"
DEACTIVATION_SHA256 = "5a5b80f62a04255addd0e2ac9598de48efe0cc12500e80a899b576cfb4f6be8d"
DEACTIVATION_RESULT_SHA256 = "e85e339b88c36da8c2fdf41b569f96ecec1895a75041d3cb122ce9e93a33dd80"
DEACTIVATION_EVIDENCE_SHA256 = "e999da23ab2651b134b36237eb210232e1627b0bf696fcd7397a9df512f10ab9"
DIAGNOSIS_SHA256 = "ba93655e44a15b09cf661245a53edcd518ec993880cf702c8857f2f77a0489b2"

SOURCE = "e53d895e9a5e38a7f06ce59de254835f10e829c1"
IMAGE = "sha256:8211e1071a3b68eac01673d76129150eb0c0fea329dd222bc8bf0394b13fc844"
TAG = "omniroute-auto-switch-r3:" + SOURCE
CANDIDATE = "omniroute-auto-switch-candidate-r4-20260913"
CANDIDATE_ID = "9468859edcdb483c53900edde14d301a162cccc791079154677e913f39bf26a3"
VOLUME = "omniroute-auto-switch-candidate-data-r4-20260913"
CODEX = "8f92f200-d280-47b3-b380-2d94be0a4b75"
VM1205 = "192.168.1.68"
SCHEMA = "auto-switch-candidate-codex-reconcile-r1-result/v1"
REVIEW_SCHEMA = "auto-switch-candidate-codex-reconcile-r1-review/v1"
REMOTE_FIELDS = {"status", "stage", "candidate_id", "candidate_running", "candidate_healthy",
                 "network_none", "isolation_verified", "live_unchanged", "retained_unchanged",
                 "connection_id", "provider", "is_active", "get_http_status", "failure_category"}
PRECONDITION_STAGES = ("candidate_discovery", "candidate_revalidation", "candidate_identity",
                       "candidate_state", "candidate_isolation", "live_identity", "retained_identity",
                       "image_identity", "candidate_volume")
EXECUTION_READY = True
RESULT_LIMIT = 32768


class Stop(Exception):
    pass


def digest(path):
    with pathlib.Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def regular(path):
    path = pathlib.Path(path)
    return path.is_file() and not path.is_symlink()


def load(path, expected, name):
    if not regular(path) or digest(path) != expected:
        raise Stop("local_validation")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def render_node(admin):
    template = r'''const http=require('node:http');const ID=__ID__;const ADMIN=Buffer.from('__ADMIN__','base64').toString();let done=false;let responseStatus=null;function emit(status,category,id=null,provider=null,active=null){if(done)return;done=true;process.stdout.write(JSON.stringify({status,stage:status==='CODEX_GET_PASS'?'complete':'get',connection_id:id,provider,is_active:active,get_http_status:responseStatus,failure_category:category}));if(status!=='CODEX_GET_PASS')process.exitCode=1}const req=http.request({host:'127.0.0.1',port:20128,path:'/api/providers/'+ID,method:'GET',headers:{Authorization:'Bearer '+ADMIN,Accept:'application/json'}},res=>{responseStatus=res.statusCode;let n=0;const chunks=[];res.on('data',chunk=>{n+=chunk.length;if(n>1048576){req.destroy(Object.assign(new Error('limit'),{category:'output_limit'}))}else chunks.push(chunk)});res.on('end',()=>{if(responseStatus!==200){emit('CODEX_GET_STOP',responseStatus>=400&&responseStatus<500?'http_4xx':responseStatus>=500?'http_5xx':'http_other');return}let value;try{value=JSON.parse(Buffer.concat(chunks).toString('utf8'))}catch{emit('CODEX_GET_STOP','parse_error');return}if(!value||typeof value!=='object'||Array.isArray(value)||Object.keys(value).length!==1||!value.connection||typeof value.connection!=='object'||Array.isArray(value.connection)){emit('CODEX_GET_STOP','schema_mismatch');return}const row=value.connection;if(row.id!==ID||row.provider!=='codex'||typeof row.isActive!=='boolean'||'apiKey'in row||'accessToken'in row||'refreshToken'in row||'idToken'in row){emit('CODEX_GET_STOP','schema_mismatch');return}emit('CODEX_GET_PASS',null,row.id,row.provider,row.isActive)})});req.setTimeout(8000,()=>req.destroy(Object.assign(new Error('timeout'),{category:'timeout'})));req.on('error',error=>emit('CODEX_GET_STOP',error&&error.category||'connection'));req.end();'''
    value = template.replace("__ID__", json.dumps(CODEX)).replace("__ADMIN__", base64.b64encode(admin.encode()).decode())
    if admin in value or value.count("method:'GET'") != 1 or "PATCH" in value or "POST" in value:
        raise Stop("local_validation")
    return value


def validate_native(value, returncode, expected=CODEX):
    fields = {"status", "stage", "connection_id", "provider", "is_active", "get_http_status", "failure_category"}
    if not isinstance(value, dict) or set(value) != fields:
        raise ValueError("native_envelope")
    status = value["get_http_status"]
    if status is not None and (type(status) is not int or not 100 <= status <= 599):
        raise ValueError("native_envelope")
    if returncode == 0:
        expected_value = {"status": "CODEX_GET_PASS", "stage": "complete", "connection_id": expected,
                          "provider": "codex", "is_active": value["is_active"], "get_http_status": 200,
                          "failure_category": None}
        if type(value["is_active"]) is not bool or value != expected_value:
            raise ValueError("native_envelope")
    elif returncode == 1:
        categories = {"http_4xx", "http_5xx", "http_other", "parse_error", "schema_mismatch",
                      "timeout", "connection", "output_limit"}
        if (value["status"] != "CODEX_GET_STOP" or value["stage"] != "get"
                or value["connection_id"] is not None or value["provider"] is not None
                or value["is_active"] is not None or value["failure_category"] not in categories):
            raise ValueError("native_envelope")
        category = value["failure_category"]
        if ((category == "http_4xx" and not (status is not None and 400 <= status <= 499))
                or (category == "http_5xx" and not (status is not None and 500 <= status <= 599))
                or (category == "http_other" and not (status is not None and 100 <= status <= 399))
                or (category in {"parse_error", "schema_mismatch"} and status != 200)):
            raise ValueError("native_envelope")
    else:
        raise ValueError("native_envelope")
    return value


REMOTE = r'''
import json,re,subprocess,threading,time
__CAPTURE__
__CONSTANTS__
class Stop(Exception):pass
class Unknown(Exception):pass
__ASSESS__
__VALIDATE_NATIVE__
CANDIDATE_FORMAT='{"id":{{json .Id}},"name":{{json .Name}},"image":{{json .Image}},"config_image":{{json .Config.Image}},"source_revision":{{json (index .Config.Labels "org.opencontainers.image.revision")}},"user":{{json .Config.User}},"running":{{json .State.Running}},"state_status":{{json .State.Status}},"health_status":{{if .State.Health}}{{json .State.Health.Status}}{{else}}"none"{{end}},"network_mode":{{json .HostConfig.NetworkMode}},"readonly_root":{{json .HostConfig.ReadonlyRootfs}},"restart_name":{{json .HostConfig.RestartPolicy.Name}},"cap_drop":{{json .HostConfig.CapDrop}},"security_opt":{{json .HostConfig.SecurityOpt}},"port_bindings":{{json .HostConfig.PortBindings}},"ports":{{json .NetworkSettings.Ports}},"tmpfs":{{json .HostConfig.Tmpfs}},"mounts":{{json .Mounts}}}'
IDENTITY_FORMAT='{"id":{{json .Id}},"name":{{json .Name}},"image":{{json .Image}},"running":{{json .State.Running}},"mounts":{{json .Mounts}}}'
IMAGE_FORMAT='{"id":{{json .Id}},"repo_tags":{{json .RepoTags}},"os":{{json .Os}},"architecture":{{json .Architecture}},"user":{{json .Config.User}},"source_revision":{{json (index .Config.Labels "org.opencontainers.image.revision")}}}'
VOLUME_FORMAT='{"name":{{json .Name}},"driver":{{json .Driver}},"scope":{{json .Scope}}}'
stage='candidate_discovery'
def command(args,payload=None,timeout=30):
 try:rc,out,err=bounded_capture(args,payload,timeout)
 except RuntimeError as error:raise Unknown() from error
 if rc or err:raise Stop(stage)
 return out
def inspect_one(kind,fmt,identity):
 try:value=json.loads(command(['docker',kind,'inspect','--format',fmt,identity]))
 except Unknown:raise
 except Exception as error:raise Stop(stage) from error
 if not isinstance(value,dict):raise Stop(stage)
 return value
def full_state():
 global stage
 rows=command(['docker','container','ls','--all','--no-trunc','--filter','name=^/'+CANDIDATE_NAME+'$','--format','{{.ID}} {{.Names}}']).decode().splitlines()
 if rows!=[CANDIDATE_ID+' '+CANDIDATE_NAME]:raise Stop(stage)
 candidate=inspect_one('container',CANDIDATE_FORMAT,CANDIDATE_NAME)
 stage='candidate_revalidation'
 if inspect_one('container',CANDIDATE_FORMAT,CANDIDATE_ID)!=candidate:raise Stop(stage)
 stage='live_identity';live=inspect_one('container',IDENTITY_FORMAT,LIVE_ID)
 stage='retained_identity';retained=[inspect_one('container',IDENTITY_FORMAT,item[0]) for item in RETAINED]
 stage='image_identity';image=inspect_one('image',IMAGE_FORMAT,CANDIDATE_TAG)
 stage='candidate_volume';names=command(['docker','volume','ls','--filter','name=^'+CANDIDATE_VOLUME+'$','--format','{{.Name}}']).decode().splitlines()
 if names!=[CANDIDATE_VOLUME]:raise Stop(stage)
 volume=inspect_one('volume',VOLUME_FORMAT,CANDIDATE_VOLUME)
 state=assess_state(candidate,live,retained,image,volume)
 required=('candidate_present','volume_present','candidate_running','can_enter_hardware_preflight_without_restart','identity_verified','image_verified','volume_verified','network_none','published_ports_zero','user_node','mount_exact','readonly_root','cap_drop_all','no_new_privileges','restart_no','tmpfs_hardened','live_unchanged','retained_candidates_unchanged')
 if state.get('candidate_id')!=CANDIDATE_ID or any(state.get(name) is not True for name in required):raise Stop('candidate_state')
 return state
def outer(status,stage,state=None,native=None,category=None):
 return {'status':status,'stage':stage,'candidate_id':CANDIDATE_ID if state else None,'candidate_running':True if state else None,'candidate_healthy':True if state else None,'network_none':True if state else None,'isolation_verified':True if state else False,'live_unchanged':True if state else False,'retained_unchanged':True if state else False,'connection_id':native['connection_id'] if native else None,'provider':native['provider'] if native else None,'is_active':native['is_active'] if native else None,'get_http_status':native['get_http_status'] if native else None,'failure_category':native['failure_category'] if native else category}
try:
 state=full_state();stage='native_dispatch'
 try:rc,out,err=bounded_capture(['docker','container','exec','-i','--user','node','--workdir','/app',CANDIDATE_NAME,'node','-'],NODE.encode(),60)
 except RuntimeError:
  print(json.dumps(outer('CANDIDATE_CODEX_RECONCILE_R1_UNKNOWN','native_dispatch',state,category='child_timeout_or_output'),sort_keys=True,separators=(',',':')));raise SystemExit(2)
 if err:
  print(json.dumps(outer('CANDIDATE_CODEX_RECONCILE_R1_UNKNOWN','native_dispatch',state,category='child_stderr'),sort_keys=True,separators=(',',':')));raise SystemExit(2)
 try:native=validate_native(json.loads(out),rc,CODEX)
 except Exception:
  print(json.dumps(outer('CANDIDATE_CODEX_RECONCILE_R1_UNKNOWN','native_dispatch',state,category='remote_envelope'),sort_keys=True,separators=(',',':')));raise SystemExit(2)
 status='CANDIDATE_CODEX_RECONCILE_R1_PASS' if native['status']=='CODEX_GET_PASS' else 'CANDIDATE_CODEX_RECONCILE_R1_STOP'
 print(json.dumps(outer(status,native['stage'],state,native),sort_keys=True,separators=(',',':')));raise SystemExit(rc)
except SystemExit:raise
except Unknown:
 print(json.dumps(outer('CANDIDATE_CODEX_RECONCILE_R1_UNKNOWN',stage,category='child_timeout_or_output'),sort_keys=True,separators=(',',':')));raise SystemExit(2)
except Exception as error:
 named=str(error) if str(error) in PRECONDITION_STAGES else stage
 print(json.dumps(outer('CANDIDATE_CODEX_RECONCILE_R1_STOP',named if named in PRECONDITION_STAGES else 'candidate_discovery',category='precondition'),sort_keys=True,separators=(',',':')));raise SystemExit(1)
'''


def fixed_dependencies():
    return ((TRANSPORT, TRANSPORT_SHA256), (RECONCILE, RECONCILE_SHA256),
            (RECONCILE_RESULT, RECONCILE_RESULT_SHA256), (DEACTIVATION, DEACTIVATION_SHA256),
            (DEACTIVATION_RESULT, DEACTIVATION_RESULT_SHA256),
            (DEACTIVATION_EVIDENCE, DEACTIVATION_EVIDENCE_SHA256), (DIAGNOSIS, DIAGNOSIS_SHA256))


def render_remote(admin, capture_source=None):
    reconcile = load(RECONCILE, RECONCILE_SHA256, "codex_reconcile_r1_state")
    if capture_source is None:
        capture_source = inspect.getsource(load(TRANSPORT, TRANSPORT_SHA256, "codex_reconcile_r1_transport").bounded_capture)
    constants = (f"SOURCE={SOURCE!r};CANDIDATE_IID={IMAGE!r};CANDIDATE_TAG={TAG!r};"
                 f"CANDIDATE_NAME={CANDIDATE!r};CANDIDATE_ID={CANDIDATE_ID!r};CANDIDATE_VOLUME={VOLUME!r};LIVE_ID={reconcile.LIVE_ID!r};"
                 f"LIVE_IID={reconcile.LIVE_IID!r};LIVE_VOLUME={reconcile.LIVE_VOLUME!r};OLD_IID={reconcile.OLD_IID!r};"
                 f"RETAINED={reconcile.RETAINED!r};CODEX={CODEX!r};PRECONDITION_STAGES={PRECONDITION_STAGES!r};"
                 f"NODE={render_node(admin)!r}")
    value = REMOTE.replace("__CAPTURE__", capture_source).replace("__CONSTANTS__", constants)
    value = value.replace("__ASSESS__", inspect.getsource(reconcile.assess_state))
    value = value.replace("__VALIDATE_NATIVE__", inspect.getsource(validate_native))
    if any(token in value for token in ("method:'PATCH'", "method:'POST'", "/v1/chat", "container','start", "container','stop")):
        raise Stop("local_validation")
    ast.parse(value)
    if admin in value:
        raise Stop("local_validation")
    return value.encode()


def validate_remote(value, returncode):
    if not isinstance(value, dict) or set(value) != REMOTE_FIELDS:
        raise Stop("remote_validation")
    status = value["get_http_status"]
    if status is not None and (type(status) is not int or not 100 <= status <= 599):
        raise Stop("remote_validation")
    full = (value["candidate_id"] == CANDIDATE_ID and value["candidate_running"] is True
            and value["candidate_healthy"] is True and value["network_none"] is True
            and value["isolation_verified"] is True and value["live_unchanged"] is True
            and value["retained_unchanged"] is True)
    if returncode == 0:
        if (value["status"] != "CANDIDATE_CODEX_RECONCILE_R1_PASS" or value["stage"] != "complete"
                or not full or value["connection_id"] != CODEX or value["provider"] != "codex"
                or type(value["is_active"]) is not bool or status != 200 or value["failure_category"] is not None):
            raise Stop("remote_validation")
    elif returncode == 1:
        if value["status"] != "CANDIDATE_CODEX_RECONCILE_R1_STOP":
            raise Stop("remote_validation")
        if value["stage"] in PRECONDITION_STAGES:
            if any(value[name] is not None for name in ("candidate_id", "candidate_running", "candidate_healthy", "network_none", "connection_id", "provider", "is_active", "get_http_status")) or value["isolation_verified"] is not False or value["live_unchanged"] is not False or value["retained_unchanged"] is not False or value["failure_category"] != "precondition":
                raise Stop("remote_validation")
        elif value["stage"] == "get":
            native = {name: value[name] for name in ("status", "stage", "connection_id", "provider", "is_active", "get_http_status", "failure_category")}
            native["status"] = "CODEX_GET_STOP"
            validate_native(native, 1)
            if not full: raise Stop("remote_validation")
        else:
            raise Stop("remote_validation")
    elif returncode == 2:
        if value["status"] != "CANDIDATE_CODEX_RECONCILE_R1_UNKNOWN" or any(value[name] is not None for name in ("connection_id", "provider", "is_active", "get_http_status")):
            raise Stop("remote_validation")
        if value["stage"] == "native_dispatch":
            if not full or value["failure_category"] not in {"child_timeout_or_output", "child_stderr", "remote_envelope"}:
                raise Stop("remote_validation")
        elif value["stage"] in PRECONDITION_STAGES:
            if (any(value[name] is not None for name in ("candidate_id", "candidate_running", "candidate_healthy", "network_none"))
                    or value["isolation_verified"] is not False or value["live_unchanged"] is not False
                    or value["retained_unchanged"] is not False or value["failure_category"] != "child_timeout_or_output"):
                raise Stop("remote_validation")
        else:
            raise Stop("remote_validation")
    else:
        raise Stop("remote_validation")
    return value


def transport_evidence(returncode=None, stdout=None, stderr=None, category=None):
    def evidence(raw):
        return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()} if raw is not None else None
    return {"returncode": returncode, "stdout": evidence(stdout), "stderr": evidence(stderr), "category": category}


def review_payload():
    if not all(regular(path) and digest(path) == expected for path, expected in fixed_dependencies()):
        raise Stop("local_validation")
    fixture = render_remote("oma_fixture_codex_reconcile_secret")
    return {"schema": REVIEW_SCHEMA, "execution_ready": EXECUTION_READY, "candidate_id": CANDIDATE_ID,
            "connection_id": CODEX, "operation": "GET", "transport_sha256": digest(TRANSPORT),
            "reconcile_sha256": digest(RECONCILE), "reconcile_result_sha256": digest(RECONCILE_RESULT),
            "deactivation_sha256": digest(DEACTIVATION), "deactivation_result_sha256": digest(DEACTIVATION_RESULT),
            "deactivation_evidence_sha256": digest(DEACTIVATION_EVIDENCE), "diagnosis_sha256": digest(DIAGNOSIS),
            "fixture_remote_sha256": hashlib.sha256(fixture).hexdigest(), "launcher_sha256": digest(__file__),
            "test_sha256": digest(TEST), "contract_sha256": digest(CONTRACT), "result": str(RESULT)}


def reserve_result():
    if RESULT.exists() or RESULT.is_symlink(): raise Stop("stale_result")
    return os.open(RESULT, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0), 0o600)


def finish(fd, value):
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()
    if len(raw) > RESULT_LIMIT: raise Stop("result_validation")
    try:
        offset = 0
        while offset < len(raw):
            written = os.write(fd, raw[offset:])
            if written <= 0: raise OSError("result_write")
            offset += written
        os.fsync(fd)
    finally:
        os.close(fd)


def execute(reviewed):
    if not EXECUTION_READY or not all(regular(path) and digest(path) == expected for path, expected in fixed_dependencies()):
        raise Stop("local_validation")
    if not regular(reviewed) or json.loads(reviewed.read_text("utf-8")) != review_payload():
        raise Stop("review_pin_mismatch")
    if not os.environ.get("PROGRAMDATA") or os.environ.get("PYTHONOPTIMIZE") is not None:
        raise Stop("local_validation")
    admin = os.environ.get("OMNIROUTE_ADMIN_TOKEN", "")
    if not re.fullmatch(r"oma_[A-Za-z0-9._~-]{16,512}", admin):
        raise Stop("local_validation")
    transport = load(TRANSPORT, TRANSPORT_SHA256, "codex_reconcile_r1_execute")
    fd = reserve_result()
    receipt = {"schema": SCHEMA, "status": "UNKNOWN", "stage": "transport",
               "transport": transport_evidence(category="not_started"), "remote": None}
    saved = os.environ.pop("OMNIROUTE_ADMIN_TOKEN", None)
    try:
        command = [transport.SSH, "-T", *transport.options(VM1205), "belladmin@" + VM1205, "sudo -n python3 -"]
        try:
            rc, out, err = transport.bounded_capture(command, render_remote(admin), 120)
        except RuntimeError:
            receipt["transport"] = transport_evidence(category="child_timeout_or_output")
            return 2
        receipt["transport"] = transport_evidence(rc, out, err, "child_stderr" if err else "returned")
        if err: return 2
        try: remote = validate_remote(json.loads(out), rc)
        except Exception:
            receipt["transport"]["category"] = "remote_envelope"
            return 2
        receipt = {"schema": SCHEMA, "status": "PASS" if rc == 0 else "STOP" if rc == 1 else "UNKNOWN",
                   "stage": remote["stage"], "transport": receipt["transport"], "remote": remote}
        return rc
    except Exception:
        receipt["transport"]["category"] = "local_exception"
        return 2
    finally:
        if saved is not None: os.environ["OMNIROUTE_ADMIN_TOKEN"] = saved
        finish(fd, receipt)


def offline_check():
    if not EXECUTION_READY or not all(regular(path) and digest(path) == expected for path, expected in fixed_dependencies()):
        raise Stop("local_validation")
    if RESULT.exists() or RESULT.is_symlink(): raise Stop("stale_result")
    payload = render_remote("oma_fixture_codex_reconcile_secret")
    if b"oma_fixture_codex_reconcile_secret" in payload or payload.count(b"method:\\'GET\\'") != 1:
        raise Stop("local_validation")
    ast.parse(payload.decode())
    print("CANDIDATE_CODEX_RECONCILE_R1_PREPARATION_PASS")


def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--self-check", action="store_true"); parser.add_argument("--render-review-payload", action="store_true"); parser.add_argument("--execute-reviewed", type=pathlib.Path); args = parser.parse_args()
    if sum((args.self_check, args.render_review_payload, bool(args.execute_reviewed))) != 1: raise Stop("local_validation")
    if args.self_check: offline_check(); return 0
    if args.render_review_payload: print(json.dumps(review_payload(), indent=2, sort_keys=True)); return 0
    return execute(args.execute_reviewed)


if __name__ == "__main__":
    try: raise SystemExit(main())
    except Exception as error:
        stage = str(error) if str(error) in {"stale_result", "review_pin_mismatch"} else "local_validation"
        print(json.dumps({"status": "CANDIDATE_CODEX_RECONCILE_R1_NOT_EXECUTED", "stage": stage}, sort_keys=True)); raise SystemExit(1)
