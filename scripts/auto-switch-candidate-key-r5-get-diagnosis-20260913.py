"""One bounded, read-only native /api/keys diagnosis for candidate-key R5."""
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
R5 = ROOT / "scripts/auto-switch-candidate-key-r5-20260913.py"
TRANSPORT = COORDINATOR / "scripts/auto-switch-image-transfer-r3-20260913.py"
CONTRACT = ROOT / "docs/auto-switch-candidate-key-r5-get-diagnosis-contract-20260913.md"
RESULT = ROOT / "docs/auto-switch-candidate-key-r5-get-diagnosis-result-20260913.json"
R5_SHA256 = "191913463849c7c42ae2e52126f73825b21bc661b6e88bfe6a799ed656f19273"
TRANSPORT_SHA256 = "78bb97e57d6229aae84c2f0d0caaf68eeb71ba6b92e69415d83af2a869b8224a"
CANDIDATE_ID = "9468859edcdb483c53900edde14d301a162cccc791079154677e913f39bf26a3"
KEY_NAME = "auto-switch-candidate-qualification-r5-20260913"
VM1205 = "192.168.1.68"
RESULT_LIMIT = 16384
RESULT_SCHEMA = "auto-switch-candidate-key-r5-get-diagnosis/v1"
REMOTE_FIELDS = {"status", "candidate_id", "preconditions_passed", "http_status",
                 "http_category", "json_parsed", "schema_category", "keys_is_array",
                 "key_name_present", "child_outcome"}


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


NODE = r'''
const http=require('node:http');
const ADMIN=Buffer.from('__ADMIN_B64__','base64').toString('utf8'),NAME=__NAME__;
const expected=['allowKeyReveal','keys','total'];
function category(s){return s===200?'ok':s===401?'auth_401':s===403?'auth_403':s>=500&&s<=599?'server_5xx':s>=100&&s<=599?'other_http':'none'}
function emit(v){process.stdout.write(JSON.stringify(v))}
const q=http.request({host:'127.0.0.1',port:20128,method:'GET',path:'/api/keys',headers:{Authorization:'Bearer '+ADMIN,Accept:'application/json'}},r=>{let n=0,a=[];r.on('data',c=>{n+=c.length;if(n>1048576)q.destroy(Object.assign(new Error('bound'),{kind:'output_limit'}));else a.push(c)});r.on('end',()=>{let v=null,parsed=false,shape='unparsed',array=null,present=null;try{v=JSON.parse(Buffer.concat(a).toString('utf8'));parsed=true;if(!v||typeof v!=='object'||Array.isArray(v))shape='not_object';else{const got=Object.keys(v).sort();shape=JSON.stringify(got)===JSON.stringify(expected)?'expected':expected.some(k=>!got.includes(k))?'missing':'extra';array=Array.isArray(v.keys);present=array?v.keys.some(x=>x&&typeof x==='object'&&x.name===NAME):null}}catch{}emit({http_status:r.statusCode,http_category:category(r.statusCode),json_parsed:parsed,schema_category:shape,keys_is_array:array,key_name_present:present,child_outcome:parsed?'complete':'parse_error'})})});
q.setTimeout(8000,()=>q.destroy(Object.assign(new Error('timeout'),{kind:'timeout'})));
q.on('error',e=>emit({http_status:null,http_category:'none',json_parsed:false,schema_category:'unparsed',keys_is_array:null,key_name_present:null,child_outcome:e.kind==='timeout'?'timeout':e.kind==='output_limit'?'output_limit':'connection'}));q.end();
'''


DIAG_BRANCH = r''' if MODE=='preflight':
  stage='native_preflight';rc,out,err=run(['docker','container','exec','-i','--user','node','--workdir','/app',CANDIDATE,'node','-'],PREFLIGHT_NODE.encode(),60)
  if rc or err:raise Stop()
  native=json.loads(out);fields={'http_status','http_category','json_parsed','schema_category','keys_is_array','key_name_present','child_outcome'}
  if not isinstance(native,dict) or set(native)!=fields:raise Stop()
  print(json.dumps({'status':'CANDIDATE_KEY_R5_GET_DIAG_PASS','candidate_id':CANDIDATE_ID,'preconditions_passed':True,**native},sort_keys=True,separators=(',',':')));raise SystemExit(0)
'''


def render_node(admin):
    if not re.fullmatch(r"oma_[A-Za-z0-9._~-]{16,512}", admin):
        raise Stop("local_validation")
    value = NODE.replace("__ADMIN_B64__", base64.b64encode(admin.encode()).decode()).replace("__NAME__", json.dumps(KEY_NAME))
    if admin in value or value.count("path:'/api/keys'") != 1:
        raise Stop("local_validation")
    return value


def render_remote(admin):
    r5 = load(R5, R5_SHA256, "candidate_key_r5_diag_source")
    source = r5.render_remote(admin, CANDIDATE_ID, "preflight").decode("utf-8")
    new_node = render_node(admin)
    lines = source.splitlines()
    constants = next((index for index, line in enumerate(lines) if line.startswith("LIVE_ID=")), None)
    if constants is None:
        raise Stop("local_validation")
    lines[constants] = (f"LIVE_ID={r5.LIVE_ID!r};LIVE_IMAGE={r5.LIVE_IMAGE!r};LIVE_VOLUME={r5.LIVE_VOLUME!r};"
                        f"CANDIDATE={r5.CANDIDATE_NAME!r};CANDIDATE_ID={CANDIDATE_ID!r};VOLUME={r5.CANDIDATE_VOLUME!r};"
                        f"IMAGE={r5.IMAGE!r};TAG={r5.TAG!r};SOURCE={r5.SOURCE!r};KEY_NAME={KEY_NAME!r};"
                        f"STORE=pathlib.Path({r5.OPERATOR_STORE!r});PREFLIGHT_NODE={new_node!r};MODE='preflight'")
    source = "\n".join(lines) + "\n"
    helpers = source.index("def rollback_key():")
    body = source.index("try:\n candidate_format=", helpers)
    source = source[:helpers] + source[body:]
    start = source.index(" if MODE=='preflight':")
    suffix = r'''except SystemExit:raise
except Exception:
 print(json.dumps({'status':'CANDIDATE_KEY_R5_PREFLIGHT_STOP','stage':stage if stage in CHECK_NAMES or stage in {'store_preflight','native_preflight'} else 'candidate_identity','candidate_id':CANDIDATE_ID,'checks':checks},sort_keys=True,separators=(',',':')));raise SystemExit(1)
finally:
 if store_parent_fd is not None:os.close(store_parent_fd)
'''
    source = source[:start] + DIAG_BRANCH + suffix
    ast.parse(source)
    if source.count("/api/keys") != 1 or any(token in source for token in ("request('POST'", "request('PATCH'", "/v1/chat")):
        raise Stop("local_validation")
    return source.encode("utf-8")


def validate_remote(value, returncode):
    if returncode == 0:
        if not isinstance(value, dict) or set(value) != REMOTE_FIELDS:
            raise Stop("remote_validation")
        if value["status"] != "CANDIDATE_KEY_R5_GET_DIAG_PASS" or value["candidate_id"] != CANDIDATE_ID or value["preconditions_passed"] is not True:
            raise Stop("remote_validation")
        if value["http_status"] is not None and (type(value["http_status"]) is not int or not 100 <= value["http_status"] <= 599):
            raise Stop("remote_validation")
        if value["http_category"] not in {"ok", "auth_401", "auth_403", "server_5xx", "other_http", "none"}:
            raise Stop("remote_validation")
        if type(value["json_parsed"]) is not bool or value["schema_category"] not in {"expected", "missing", "extra", "not_object", "unparsed"}:
            raise Stop("remote_validation")
        if value["keys_is_array"] not in (None, True, False) or value["key_name_present"] not in (None, True, False):
            raise Stop("remote_validation")
        outcome = value["child_outcome"]
        if outcome not in {"complete", "parse_error", "timeout", "connection", "output_limit"}:
            raise Stop("remote_validation")
        expected_category = ("ok" if value["http_status"] == 200 else "auth_401" if value["http_status"] == 401
                             else "auth_403" if value["http_status"] == 403 else "server_5xx"
                             if isinstance(value["http_status"], int) and 500 <= value["http_status"] <= 599
                             else "other_http" if isinstance(value["http_status"], int) else "none")
        if value["http_category"] != expected_category:
            raise Stop("remote_validation")
        if outcome == "parse_error":
            if (value["http_status"] is None or value["json_parsed"] is not False
                    or value["schema_category"] != "unparsed"
                    or value["keys_is_array"] is not None or value["key_name_present"] is not None):
                raise Stop("remote_validation")
        elif outcome in {"timeout", "connection", "output_limit"}:
            if (value["http_status"] is not None or value["http_category"] != "none"
                    or value["json_parsed"] is not False or value["schema_category"] != "unparsed"
                    or value["keys_is_array"] is not None or value["key_name_present"] is not None):
                raise Stop("remote_validation")
        elif (value["http_status"] is None or value["json_parsed"] is not True
              or value["schema_category"] == "unparsed"):
            raise Stop("remote_validation")
        elif value["schema_category"] == "not_object":
            if value["keys_is_array"] is not None or value["key_name_present"] is not None:
                raise Stop("remote_validation")
        elif type(value["keys_is_array"]) is not bool:
            raise Stop("remote_validation")
        elif value["keys_is_array"] is True and type(value["key_name_present"]) is not bool:
            raise Stop("remote_validation")
        elif value["keys_is_array"] is False and value["key_name_present"] is not None:
            raise Stop("remote_validation")
        return value
    r5 = load(R5, R5_SHA256, "candidate_key_r5_diag_validator")
    return r5.validate_preflight(value, returncode)


def review_payload():
    return {"schema": "auto-switch-candidate-key-r5-get-diagnosis-review/v1",
            "launcher_sha256": digest(__file__), "contract_sha256": digest(CONTRACT),
            "r5_sha256": digest(R5), "transport_sha256": digest(TRANSPORT),
            "candidate_id": CANDIDATE_ID, "request_count": 1,
            "request_method": "GET", "request_path": "/api/keys", "result": str(RESULT)}


def reserve_result():
    if RESULT.exists() or RESULT.is_symlink():
        raise Stop("stale_result")
    return os.open(RESULT, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0), 0o600)


def finish_result(fd, value):
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()
    if len(raw) > RESULT_LIMIT:
        raise Stop("local_validation")
    try:
        offset = 0
        while offset < len(raw):
            count = os.write(fd, raw[offset:])
            if count <= 0:
                raise OSError("result_write")
            offset += count
        os.fsync(fd)
    finally:
        os.close(fd)


def execute(reviewed):
    if not regular(reviewed) or json.loads(reviewed.read_text("utf-8")) != review_payload():
        raise Stop("review_pin_mismatch")
    if not os.environ.get("PROGRAMDATA") or os.environ.get("PYTHONOPTIMIZE") is not None:
        raise Stop("local_validation")
    admin = os.environ.get("OMNIROUTE_ADMIN_TOKEN", "")
    if not re.fullmatch(r"oma_[A-Za-z0-9._~-]{16,512}", admin):
        raise Stop("local_validation")
    transport = load(TRANSPORT, TRANSPORT_SHA256, "candidate_key_r5_diag_transport")
    fd = reserve_result()
    receipt = {"schema": RESULT_SCHEMA, "status": "UNKNOWN", "stage": "transport", "remote": None}
    try:
        command = [transport.SSH, "-T", *transport.options(VM1205), "belladmin@" + VM1205, "sudo -n python3 -"]
        saved = os.environ.pop("OMNIROUTE_ADMIN_TOKEN", None)
        try:
            returncode, stdout, stderr = transport.bounded_capture(command, render_remote(admin), 180)
        finally:
            if saved is not None:
                os.environ["OMNIROUTE_ADMIN_TOKEN"] = saved
        if stderr:
            raise Stop("transport_unknown")
        remote = validate_remote(json.loads(stdout), returncode)
        status = "PASS" if returncode == 0 else "STOP"
        receipt = {"schema": RESULT_SCHEMA, "status": status,
                   "stage": "complete" if returncode == 0 else remote["stage"], "remote": remote}
        return 0 if returncode == 0 else 1
    except Stop as error:
        if str(error) != "transport_unknown":
            raise
        return 2
    finally:
        finish_result(fd, receipt)


def self_check():
    for path, expected in ((R5, R5_SHA256), (TRANSPORT, TRANSPORT_SHA256)):
        if not regular(path) or digest(path) != expected:
            raise Stop("local_validation")
    if RESULT.exists() or RESULT.is_symlink():
        raise Stop("stale_result")
    fake = "oma_fixture_diagnostic_secret"
    payload = render_remote(fake)
    if fake.encode() in payload or payload.count(b"/api/keys") != 1:
        raise Stop("local_validation")
    sample = {"status": "CANDIDATE_KEY_R5_GET_DIAG_PASS", "candidate_id": CANDIDATE_ID,
              "preconditions_passed": True, "http_status": 401, "http_category": "auth_401",
              "json_parsed": True, "schema_category": "missing", "keys_is_array": False,
              "key_name_present": None, "child_outcome": "complete"}
    validate_remote(sample, 0)
    print("CANDIDATE_KEY_R5_GET_DIAG_PREPARATION_PASS")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--render-review-payload", action="store_true")
    parser.add_argument("--execute-reviewed", type=pathlib.Path)
    args = parser.parse_args()
    if sum((args.self_check, args.render_review_payload, bool(args.execute_reviewed))) != 1:
        raise Stop("local_validation")
    if args.self_check:
        self_check(); return 0
    if args.render_review_payload:
        print(json.dumps(review_payload(), indent=2, sort_keys=True)); return 0
    return execute(args.execute_reviewed)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        category = str(error) if str(error) in {"stale_result", "review_pin_mismatch"} else "local_validation"
        print(json.dumps({"status": "CANDIDATE_KEY_R5_GET_DIAG_NOT_EXECUTABLE", "category": category}, sort_keys=True))
        raise SystemExit(1)
