"""Prepare one exact candidate-only Codex connection deactivation."""
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
COORDINATOR_ROOT = pathlib.Path(r"C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-auto-switch-20260912")
ROLLOUT_ROOT = pathlib.Path(r"C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-live-rollout-20260913")
R5 = ROOT / "scripts/auto-switch-candidate-key-r5-20260913.py"
TRANSPORT = COORDINATOR_ROOT / "scripts/auto-switch-image-transfer-r3-20260913.py"
R3_RECEIPT = ROOT / "docs/auto-switch-candidate-key-r5-preflight-result-r3-20260913.json"
R3_EVIDENCE = ROLLOUT_ROOT / "docs/auto-switch-candidate-key-r5-preflight-r3-evidence-review-20260913.md"
CONTRACT = ROOT / "docs/auto-switch-candidate-codex-deactivate-r1-contract-20260913.md"
TEST = ROOT / "scripts/test-auto-switch-candidate-codex-deactivate-r1-20260913.py"
RESULT = ROOT / "docs/auto-switch-candidate-codex-deactivate-r1-result-20260913.json"

R5_SHA256 = "191913463849c7c42ae2e52126f73825b21bc661b6e88bfe6a799ed656f19273"
TRANSPORT_SHA256 = "78bb97e57d6229aae84c2f0d0caaf68eeb71ba6b92e69415d83af2a869b8224a"
R3_RECEIPT_SHA256 = "d34341199d8b832b449884a943f6dd6d780c2d3be0afcac17c59afa5b9fa4695"
R3_EVIDENCE_SHA256 = "de9a9aa6dccf3522998682443a6f81a55f3461beddd8a0839c2d888f485f499f"
CANDIDATE_ID = "9468859edcdb483c53900edde14d301a162cccc791079154677e913f39bf26a3"
CODEX_CONNECTION = "8f92f200-d280-47b3-b380-2d94be0a4b75"
VM1205 = "192.168.1.68"
SCHEMA = "auto-switch-candidate-codex-deactivate-r1-result/v1"
REVIEW_SCHEMA = "auto-switch-candidate-codex-deactivate-r1-review/v1"
EXECUTION_READY = True
RESULT_LIMIT = 32768
PRECONDITIONS = ("candidate_identity", "live_identity", "image_identity", "volume_identity",
                 "cloud_false", "migration_170", "migration_171", "schema_columns",
                 "credential_shape", "server_env_exact", "store_absent")
FIELDS = {"status", "stage", "candidate_id", "connection_id", "checks", "before_active",
          "patch_dispatched", "patch_http_status", "readback_http_status", "inactive_readback",
          "failure_category"}


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
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


NODE = r'''
const http=require('node:http');
const ADMIN=Buffer.from('__ADMIN_B64__','base64').toString('utf8'),CODEX=__CODEX__;
let stage='get_before',beforeActive=null,patchDispatched=false,patchStatus=null,readbackStatus=null;
function fail(category){const e=new Error(category);e.category=category;throw e}
function category(status){return status>=400&&status<=499?'http_4xx':status>=500&&status<=599?'http_5xx':'http_other'}
function request(method,path,body){return new Promise((resolve,reject)=>{const raw=body?Buffer.from(JSON.stringify(body)):null;const headers={Authorization:'Bearer '+ADMIN,Accept:'application/json'};if(raw){headers['Content-Type']='application/json';headers['Content-Length']=String(raw.length)}const q=http.request({host:'127.0.0.1',port:20128,method,path,headers},r=>{let n=0,a=[];r.on('data',c=>{n+=c.length;if(n>1048576)q.destroy(Object.assign(new Error('output_limit'),{category:'output_limit'}));else a.push(c)});r.on('end',()=>resolve({status:r.statusCode,body:Buffer.concat(a)}))});q.setTimeout(8000,()=>q.destroy(Object.assign(new Error('timeout'),{category:'timeout'})));q.on('error',e=>{if(!e.category)e.category='connection';reject(e)});if(raw)q.write(raw);q.end()})}
function decode(response){if(response.status!==200)fail(category(response.status));let value;try{value=JSON.parse(response.body.toString('utf8'))}catch{fail('parse_error')}if(!value||typeof value!=='object'||Array.isArray(value)||JSON.stringify(Object.keys(value))!==JSON.stringify(['connection']))fail('schema_mismatch');const row=value.connection;if(!row||typeof row!=='object'||Array.isArray(row)||row.id!==CODEX||row.provider!=='codex'||typeof row.isActive!=='boolean'||'accessToken'in row||'refreshToken'in row||'idToken'in row)fail('schema_mismatch');return row}
(async()=>{let response=await request('GET','/api/providers/'+CODEX);readbackStatus=response.status;let row=decode(response);beforeActive=row.isActive;if(beforeActive){stage='patch';patchDispatched=true;response=await request('PATCH','/api/providers/'+CODEX,{isActive:false});patchStatus=response.status;row=decode(response);if(row.isActive!==false)fail('predicate_failed')}stage='readback';response=await request('GET','/api/providers/'+CODEX);readbackStatus=response.status;row=decode(response);if(row.isActive!==false)fail('predicate_failed');process.stdout.write(JSON.stringify({status:'CODEX_DEACTIVATE_PASS',stage:'complete',connection_id:CODEX,before_active:beforeActive,patch_dispatched:patchDispatched,patch_http_status:patchStatus,readback_http_status:readbackStatus,inactive_readback:true,failure_category:null}))})().catch(e=>{const unknown=patchDispatched;process.stdout.write(JSON.stringify({status:unknown?'CODEX_DEACTIVATE_UNKNOWN':'CODEX_DEACTIVATE_STOP',stage,connection_id:CODEX,before_active:beforeActive,patch_dispatched:patchDispatched,patch_http_status:patchStatus,readback_http_status:readbackStatus,inactive_readback:false,failure_category:e&&e.category||'connection'}));process.exitCode=unknown?2:1});
'''


BRANCH = r''' if MODE=='preflight':
  failed=next((name for name in PRECONDITIONS if checks[name] is not True),None)
  if failed:stage=failed;raise Stop()
  stage='native_dispatch'
  try:rc,out,err=bounded_capture(['docker','container','exec','-i','--user','node','--workdir','/app',CANDIDATE,'node','-'],DEACTIVATE_NODE.encode(),60)
  except RuntimeError:
   print(json.dumps({'status':'CANDIDATE_CODEX_DEACTIVATE_R1_UNKNOWN','stage':'native_dispatch','candidate_id':CANDIDATE_ID,'connection_id':None,'checks':{name:checks[name] for name in PRECONDITIONS},'before_active':None,'patch_dispatched':None,'patch_http_status':None,'readback_http_status':None,'inactive_readback':None,'failure_category':'child_timeout_or_output'},sort_keys=True,separators=(',',':')));raise SystemExit(2)
  if err:
   print(json.dumps({'status':'CANDIDATE_CODEX_DEACTIVATE_R1_UNKNOWN','stage':'native_dispatch','candidate_id':CANDIDATE_ID,'connection_id':None,'checks':{name:checks[name] for name in PRECONDITIONS},'before_active':None,'patch_dispatched':None,'patch_http_status':None,'readback_http_status':None,'inactive_readback':None,'failure_category':'child_stderr'},sort_keys=True,separators=(',',':')));raise SystemExit(2)
  try:native=json.loads(out)
  except Exception:
   print(json.dumps({'status':'CANDIDATE_CODEX_DEACTIVATE_R1_UNKNOWN','stage':'native_dispatch','candidate_id':CANDIDATE_ID,'connection_id':None,'checks':{name:checks[name] for name in PRECONDITIONS},'before_active':None,'patch_dispatched':None,'patch_http_status':None,'readback_http_status':None,'inactive_readback':None,'failure_category':'remote_envelope'},sort_keys=True,separators=(',',':')));raise SystemExit(2)
  try:native=validate_native_child(native,rc,CODEX)
  except Exception:
   print(json.dumps({'status':'CANDIDATE_CODEX_DEACTIVATE_R1_UNKNOWN','stage':'native_dispatch','candidate_id':CANDIDATE_ID,'connection_id':None,'checks':{name:checks[name] for name in PRECONDITIONS},'before_active':None,'patch_dispatched':None,'patch_http_status':None,'readback_http_status':None,'inactive_readback':None,'failure_category':'remote_envelope'},sort_keys=True,separators=(',',':')));raise SystemExit(2)
  outer_status={'CODEX_DEACTIVATE_PASS':'CANDIDATE_CODEX_DEACTIVATE_R1_PASS','CODEX_DEACTIVATE_STOP':'CANDIDATE_CODEX_DEACTIVATE_R1_STOP','CODEX_DEACTIVATE_UNKNOWN':'CANDIDATE_CODEX_DEACTIVATE_R1_UNKNOWN'}[native['status']]
  outer={'status':outer_status,'stage':native['stage'],'candidate_id':CANDIDATE_ID,'connection_id':native['connection_id'],'checks':{name:checks[name] for name in PRECONDITIONS},'before_active':native['before_active'],'patch_dispatched':native['patch_dispatched'],'patch_http_status':native['patch_http_status'],'readback_http_status':native['readback_http_status'],'inactive_readback':native['inactive_readback'],'failure_category':native['failure_category']}
  print(json.dumps(outer,sort_keys=True,separators=(',',':')));raise SystemExit(rc if rc in (0,1,2) else 2)
'''


def render_node(admin):
    if not re.fullmatch(r"oma_[A-Za-z0-9._~-]{16,512}", admin):
        raise Stop("local_validation")
    value = NODE.replace("__ADMIN_B64__", base64.b64encode(admin.encode()).decode()).replace("__CODEX__", json.dumps(CODEX_CONNECTION))
    if admin in value:
        raise Stop("local_validation")
    return value


def validate_native_child(value, returncode, expected_connection):
    fields = {"status", "stage", "connection_id", "before_active", "patch_dispatched",
              "patch_http_status", "readback_http_status", "inactive_readback", "failure_category"}
    if not isinstance(value, dict) or set(value) != fields or value["connection_id"] != expected_connection:
        raise ValueError("native_envelope")
    for field in ("patch_http_status", "readback_http_status"):
        if value[field] is not None and (type(value[field]) is not int or not 100 <= value[field] <= 599):
            raise ValueError("native_envelope")
    failures = {"http_4xx", "http_5xx", "http_other", "parse_error", "schema_mismatch",
                "predicate_failed", "timeout", "connection", "output_limit"}
    if returncode == 0:
        if (value["status"] != "CODEX_DEACTIVATE_PASS" or value["stage"] != "complete"
                or type(value["before_active"]) is not bool
                or value["patch_dispatched"] is not value["before_active"]
                or value["patch_http_status"] != (200 if value["before_active"] else None)
                or value["readback_http_status"] != 200 or value["inactive_readback"] is not True
                or value["failure_category"] is not None):
            raise ValueError("native_envelope")
    elif returncode == 1:
        if (value["status"] != "CODEX_DEACTIVATE_STOP" or value["stage"] not in {"get_before", "readback"}
                or value["patch_dispatched"] is not False or value["patch_http_status"] is not None
                or value["inactive_readback"] is not False or value["failure_category"] not in failures):
            raise ValueError("native_envelope")
        if value["stage"] == "get_before" and value["before_active"] is not None:
            raise ValueError("native_envelope")
        if value["stage"] == "readback" and value["before_active"] is not False:
            raise ValueError("native_envelope")
    elif returncode == 2:
        if (value["status"] != "CODEX_DEACTIVATE_UNKNOWN" or value["stage"] not in {"patch", "readback"}
                or value["before_active"] is not True or value["patch_dispatched"] is not True
                or value["inactive_readback"] is not False or value["failure_category"] not in failures):
            raise ValueError("native_envelope")
        if value["stage"] == "patch" and value["readback_http_status"] != 200:
            raise ValueError("native_envelope")
        if value["stage"] == "readback" and value["patch_http_status"] != 200:
            raise ValueError("native_envelope")
    else:
        raise ValueError("native_envelope")
    return value


def render_remote(admin):
    r5 = load(R5, R5_SHA256, "codex_deactivate_r1_r5")
    source = r5.render_remote(admin, CANDIDATE_ID, "preflight").decode("utf-8")
    node = render_node(admin); lines = source.splitlines()
    constants = next((i for i, line in enumerate(lines) if line.startswith("LIVE_ID=")), None)
    if constants is None: raise Stop("local_validation")
    lines[constants] = (f"LIVE_ID={r5.LIVE_ID!r};LIVE_IMAGE={r5.LIVE_IMAGE!r};LIVE_VOLUME={r5.LIVE_VOLUME!r};"
                        f"CANDIDATE={r5.CANDIDATE_NAME!r};CANDIDATE_ID={CANDIDATE_ID!r};VOLUME={r5.CANDIDATE_VOLUME!r};"
                        f"IMAGE={r5.IMAGE!r};TAG={r5.TAG!r};SOURCE={r5.SOURCE!r};KEY_NAME={r5.KEY_NAME!r};"
                        f"STORE=pathlib.Path({r5.OPERATOR_STORE!r});MODE='preflight';DEACTIVATE_NODE={node!r};"
                        f"CODEX={CODEX_CONNECTION!r};PRECONDITIONS={PRECONDITIONS!r}")
    source = "\n".join(lines) + "\n"
    helpers = source.index("def rollback_key():"); body = source.index("try:\n candidate_format=", helpers)
    source = source[:helpers] + source[body:]
    start = source.index(" if MODE=='preflight':")
    validator = "\n".join(" " + line if line else line for line in inspect.getsource(validate_native_child).splitlines())
    suffix = r'''except SystemExit:raise
except Exception:
 print(json.dumps({'status':'CANDIDATE_CODEX_DEACTIVATE_R1_STOP','stage':stage if stage in PRECONDITIONS or stage=='store_preflight' else 'candidate_identity','candidate_id':CANDIDATE_ID,'connection_id':CODEX,'checks':{name:checks[name] for name in PRECONDITIONS},'before_active':None,'patch_dispatched':False,'patch_http_status':None,'readback_http_status':None,'inactive_readback':False,'failure_category':'precondition'},sort_keys=True,separators=(',',':')));raise SystemExit(1)
finally:
 if store_parent_fd is not None:os.close(store_parent_fd)
'''
    source = source[:start] + validator + "\n" + BRANCH + suffix
    ast.parse(source)
    if any(token in source for token in ("request('POST'", "/v1/chat", "container','start", "container','stop")):
        raise Stop("local_validation")
    return source.encode("utf-8")


def fixture_result(before_active=True, patched=True):
    return {"status": "CANDIDATE_CODEX_DEACTIVATE_R1_PASS", "stage": "complete",
            "candidate_id": CANDIDATE_ID, "connection_id": CODEX_CONNECTION,
            "checks": {name: True for name in PRECONDITIONS}, "before_active": before_active,
            "patch_dispatched": patched, "patch_http_status": 200 if patched else None,
            "readback_http_status": 200, "inactive_readback": True, "failure_category": None}


def fixture_unknown(stage="patch"):
    return {"status": "CANDIDATE_CODEX_DEACTIVATE_R1_UNKNOWN", "stage": stage,
            "candidate_id": CANDIDATE_ID, "connection_id": CODEX_CONNECTION,
            "checks": {name: True for name in PRECONDITIONS}, "before_active": True,
            "patch_dispatched": True, "patch_http_status": None,
            "readback_http_status": 200 if stage == "patch" else None,
            "inactive_readback": False, "failure_category": "timeout"}


def fixture_native(before_active=True, patched=True):
    return {"status": "CODEX_DEACTIVATE_PASS", "stage": "complete",
            "connection_id": CODEX_CONNECTION, "before_active": before_active,
            "patch_dispatched": patched, "patch_http_status": 200 if patched else None,
            "readback_http_status": 200, "inactive_readback": True, "failure_category": None}


def validate_remote(value, returncode):
    if not isinstance(value, dict) or set(value) != FIELDS or value["candidate_id"] != CANDIDATE_ID:
        raise Stop("remote_validation")
    expected_connection = None if returncode == 2 and value["stage"] == "native_dispatch" else CODEX_CONNECTION
    if value["connection_id"] != expected_connection:
        raise Stop("remote_validation")
    checks = value["checks"]
    if not isinstance(checks, dict) or tuple(checks) != tuple(PRECONDITIONS) or any(type(v) is not bool for v in checks.values()):
        raise Stop("remote_validation")
    for field in ("patch_http_status", "readback_http_status"):
        if value[field] is not None and (type(value[field]) is not int or not 100 <= value[field] <= 599): raise Stop("remote_validation")
    if returncode == 0:
        expected = fixture_result(value["before_active"], value["patch_dispatched"])
        if type(value["before_active"]) is not bool or value["patch_dispatched"] is not value["before_active"] or value != expected:
            raise Stop("remote_validation")
    elif returncode == 1:
        if value["status"] != "CANDIDATE_CODEX_DEACTIVATE_R1_STOP" or value["stage"] not in set(PRECONDITIONS) | {"store_preflight", "get_before", "readback"} or value["patch_dispatched"] is not False or value["inactive_readback"] is not False or value["failure_category"] not in {"precondition", "http_4xx", "http_5xx", "http_other", "parse_error", "schema_mismatch", "predicate_failed", "timeout", "connection", "output_limit"}:
            raise Stop("remote_validation")
        if value["stage"] in set(PRECONDITIONS) | {"store_preflight"}:
            index = PRECONDITIONS.index(value["stage"]) if value["stage"] in PRECONDITIONS else len(PRECONDITIONS) - 1
            if any(checks[name] is not True for name in PRECONDITIONS[:index]) or checks[PRECONDITIONS[index]] is not False or any(value[name] is not None for name in ("before_active", "patch_http_status", "readback_http_status")) or value["failure_category"] != "precondition": raise Stop("remote_validation")
        elif not all(checks.values()): raise Stop("remote_validation")
        if value["stage"] == "get_before" and value["before_active"] is not None: raise Stop("remote_validation")
        if value["stage"] == "readback" and (value["before_active"] is not False or value["patch_http_status"] is not None): raise Stop("remote_validation")
    elif returncode == 2:
        if value["status"] != "CANDIDATE_CODEX_DEACTIVATE_R1_UNKNOWN" or value["stage"] not in {"native_dispatch", "patch", "readback"} or value["inactive_readback"] not in (None, False) or value["failure_category"] not in {"child_timeout_or_output", "child_stderr", "remote_envelope", "http_4xx", "http_5xx", "http_other", "parse_error", "schema_mismatch", "predicate_failed", "timeout", "connection", "output_limit"}:
            raise Stop("remote_validation")
        if value["stage"] != "native_dispatch" and (value["before_active"] is not True or value["patch_dispatched"] is not True): raise Stop("remote_validation")
        if value["stage"] != "native_dispatch" and not all(checks.values()): raise Stop("remote_validation")
        if value["stage"] == "native_dispatch" and any(value[name] is not None for name in ("before_active", "patch_dispatched", "patch_http_status", "readback_http_status", "inactive_readback")): raise Stop("remote_validation")
        if value["stage"] == "patch" and value["readback_http_status"] != 200: raise Stop("remote_validation")
        if value["stage"] == "readback" and value["patch_http_status"] != 200: raise Stop("remote_validation")
    else:
        raise Stop("remote_validation")
    return value


def fixed_dependencies():
    return ((R5, R5_SHA256), (TRANSPORT, TRANSPORT_SHA256), (R3_RECEIPT, R3_RECEIPT_SHA256), (R3_EVIDENCE, R3_EVIDENCE_SHA256))


def review_payload():
    if not all(regular(path) and digest(path) == expected for path, expected in fixed_dependencies()): raise Stop("local_validation")
    return {"schema": REVIEW_SCHEMA, "execution_ready": EXECUTION_READY, "candidate_id": CANDIDATE_ID,
            "connection_id": CODEX_CONNECTION, "method": "PATCH", "body": {"isActive": False},
            "r5_sha256": digest(R5), "transport_sha256": digest(TRANSPORT),
            "r3_receipt_sha256": digest(R3_RECEIPT), "r3_evidence_sha256": digest(R3_EVIDENCE),
            "launcher_sha256": digest(__file__), "test_sha256": digest(TEST),
            "contract_sha256": digest(CONTRACT), "result": str(RESULT)}


def reserve_result():
    if RESULT.exists() or RESULT.is_symlink(): raise Stop("stale_result")
    return os.open(RESULT, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0), 0o600)


def finish(fd, value):
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()
    if len(raw) > RESULT_LIMIT: raise Stop("result_validation")
    try:
        offset = 0
        while offset < len(raw):
            count = os.write(fd, raw[offset:])
            if count <= 0: raise OSError("result_write")
            offset += count
        os.fsync(fd)
    finally: os.close(fd)


def execute(reviewed):
    if not EXECUTION_READY or not all(regular(path) and digest(path) == expected for path, expected in fixed_dependencies()): raise Stop("local_validation")
    if not regular(reviewed) or json.loads(reviewed.read_text("utf-8")) != review_payload(): raise Stop("review_pin_mismatch")
    if not os.environ.get("PROGRAMDATA") or os.environ.get("PYTHONOPTIMIZE") is not None: raise Stop("local_validation")
    admin = os.environ.get("OMNIROUTE_ADMIN_TOKEN", "")
    if not re.fullmatch(r"oma_[A-Za-z0-9._~-]{16,512}", admin): raise Stop("local_validation")
    transport = load(TRANSPORT, TRANSPORT_SHA256, "codex_deactivate_r1_transport")
    fd = reserve_result(); receipt = {"schema": SCHEMA, "status": "UNKNOWN", "stage": "transport", "remote": None}
    try:
        command = [transport.SSH, "-T", *transport.options(VM1205), "belladmin@" + VM1205, "sudo -n python3 -"]
        saved = os.environ.pop("OMNIROUTE_ADMIN_TOKEN", None)
        try: rc, out, err = transport.bounded_capture(command, render_remote(admin), 180)
        finally:
            if saved is not None: os.environ["OMNIROUTE_ADMIN_TOKEN"] = saved
        if err: return 2
        try: remote = validate_remote(json.loads(out), rc)
        except Exception: return 2
        status = "PASS" if rc == 0 else "STOP" if rc == 1 else "UNKNOWN"
        receipt = {"schema": SCHEMA, "status": status, "stage": remote["stage"], "remote": remote}
        return rc
    except Exception:
        return 2
    finally: finish(fd, receipt)


def offline_check():
    if not EXECUTION_READY or not all(regular(path) and digest(path) == expected for path, expected in fixed_dependencies()): raise Stop("local_validation")
    if RESULT.exists() or RESULT.is_symlink(): raise Stop("stale_result")
    receipt = json.loads(R3_RECEIPT.read_text("utf-8"))
    if receipt.get("status") != "STOP" or receipt.get("stage") != "codex_inactive" or receipt.get("remote", {}).get("checks", {}).get("codex_inactive") is not False: raise Stop("local_validation")
    payload = render_remote("oma_fixture_codex_deactivation_secret")
    if b"oma_fixture_codex_deactivation_secret" in payload: raise Stop("local_validation")
    ast.parse(payload.decode()); validate_remote(fixture_result(True, True), 0); validate_remote(fixture_result(False, False), 0); validate_remote(fixture_unknown(), 2)
    print("CANDIDATE_CODEX_DEACTIVATE_R1_PREPARATION_PASS")


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
        print(json.dumps({"status": "CANDIDATE_CODEX_DEACTIVATE_R1_NOT_EXECUTED", "stage": stage}, sort_keys=True)); raise SystemExit(1)
