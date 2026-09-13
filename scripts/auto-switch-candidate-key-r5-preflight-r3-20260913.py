"""Prepare one evidence-preserving successor to the frozen R5 read-only preflight."""
import argparse
import ast
import base64
import hashlib
import importlib.util
import json
import os
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parents[1]
COORDINATOR_ROOT = pathlib.Path(r"C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-auto-switch-20260912")
MATRIX_ROOT = pathlib.Path(r"C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-auto-switch-matrix-20260913")
R5 = ROOT / "scripts/auto-switch-candidate-key-r5-20260913.py"
TRANSPORT = COORDINATOR_ROOT / "scripts/auto-switch-image-transfer-r3-20260913.py"
KEYS_ROUTE = MATRIX_ROOT / "src/app/api/keys/route.ts"
COMBOS_ROUTE = MATRIX_ROOT / "src/app/api/combos/route.ts"
PROVIDER_ROUTE = MATRIX_ROOT / "src/app/api/providers/[id]/route.ts"
CONTRACT = ROOT / "docs/auto-switch-candidate-key-r5-preflight-r3-contract-20260913.md"
TEST = ROOT / "scripts/test-auto-switch-candidate-key-r5-preflight-r3-20260913.py"
RESULT = ROOT / "docs/auto-switch-candidate-key-r5-preflight-result-r3-20260913.json"

R5_SHA256 = "191913463849c7c42ae2e52126f73825b21bc661b6e88bfe6a799ed656f19273"
TRANSPORT_SHA256 = "78bb97e57d6229aae84c2f0d0caaf68eeb71ba6b92e69415d83af2a869b8224a"
KEYS_ROUTE_SHA256 = "7dfe03fa78ad4e1acb468632968fc5ca994f3c5206e8924cd8cc2760b5ea07b3"
COMBOS_ROUTE_SHA256 = "e0b18b802dc00de1b4fef2798b6d627ab84dfd0c5c339f6b858e730bc34c0fba"
PROVIDER_ROUTE_SHA256 = "fff5ce6cb8bc6fd3126b44584cebb1b22d11ea2ef1879acaba7f2f8d29a65ef8"
CANDIDATE_ID = "9468859edcdb483c53900edde14d301a162cccc791079154677e913f39bf26a3"
VM1205 = "192.168.1.68"
SCHEMA = "auto-switch-candidate-key-r5-preflight-r3-result/v1"
REVIEW_SCHEMA = "auto-switch-candidate-key-r5-preflight-r3-review/v1"
NATIVE_CHECKS = ("key_api_schema", "key_name_absent", "combo_api_schema",
                 "combo_sentinel_absent", "codex_schema", "codex_inactive")
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
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


NODE = r'''
const http=require('node:http');
const ADMIN=Buffer.from('__ADMIN_B64__','base64').toString('utf8'),NAME=__NAME__,CODEX=__CODEX__,SENTINEL=__SENTINEL__;
const checks={key_api_schema:false,key_name_absent:false,combo_api_schema:false,combo_sentinel_absent:false,codex_schema:false,codex_inactive:false};
const evidence={http_status:{keys:null,combos:null,codex:null},http_category:{keys:null,combos:null,codex:null},schema:{keys:null,combos:null,codex:null},completed_steps:[],failure_category:null,child_outcome:null};let stage='key_api_schema';
function category(s){return s===200?'ok':s===401?'auth_401':s===403?'auth_403':s>=500&&s<=599?'server_5xx':s>=100&&s<=599?'other_http':'none'}
function exact(v,w){return !!v&&typeof v==='object'&&!Array.isArray(v)&&JSON.stringify(Object.keys(v).sort())===JSON.stringify([...w].sort())}
function fail(kind,outcome){const e=new Error(kind);e.kind=kind;e.outcome=outcome;throw e}
function request(path){return new Promise((resolve,reject)=>{const q=http.request({host:'127.0.0.1',port:20128,method:'GET',path,headers:{Authorization:'Bearer '+ADMIN,Accept:'application/json'}},r=>{let n=0,a=[];r.on('data',c=>{n+=c.length;if(n>1048576)q.destroy(Object.assign(new Error('output_limit'),{kind:'output_limit',outcome:'output_limit'}));else a.push(c)});r.on('end',()=>resolve({status:r.statusCode,body:Buffer.concat(a)}))});q.setTimeout(8000,()=>q.destroy(Object.assign(new Error('timeout'),{kind:'timeout',outcome:'timeout'})));q.on('error',e=>{if(!e.kind){e.kind='connection';e.outcome='connection'}reject(e)});q.end()})}
async function read(label,path,expected){const r=await request(path);evidence.http_status[label]=r.status;evidence.http_category[label]=category(r.status);if(r.status!==200)fail(evidence.http_category[label],'http_error');let value;try{value=JSON.parse(r.body.toString('utf8'))}catch{fail('parse_error','parse_error')}const got=value&&typeof value==='object'&&!Array.isArray(value)?Object.keys(value).sort():null;evidence.schema[label]=got&&JSON.stringify(got)===JSON.stringify([...expected].sort())?'expected':got?'mismatch':'not_object';if(!exact(value,expected))fail('schema_mismatch','schema_error');return value}
(async()=>{let value=await read('keys','/api/keys',['keys','total','allowKeyReveal']);if(!Array.isArray(value.keys))fail('schema_mismatch','schema_error');checks.key_api_schema=true;stage='key_name_absent';if(value.keys.some(x=>x&&x.name===NAME))fail('predicate_failed','predicate_error');checks.key_name_absent=true;evidence.completed_steps.push('keys');
stage='combo_api_schema';value=await read('combos','/api/combos',['combos','total']);if(!Array.isArray(value.combos))fail('schema_mismatch','schema_error');checks.combo_api_schema=true;stage='combo_sentinel_absent';if(value.combos.some(x=>x&&(x.name===SENTINEL||x.name==='combo/'+SENTINEL)))fail('predicate_failed','predicate_error');checks.combo_sentinel_absent=true;evidence.completed_steps.push('combos');
stage='codex_schema';value=await read('codex','/api/providers/'+CODEX,['connection']);if(!value.connection||typeof value.connection!=='object'||Array.isArray(value.connection))fail('schema_mismatch','schema_error');checks.codex_schema=true;stage='codex_inactive';if(value.connection.id!==CODEX||value.connection.provider!=='codex'||value.connection.isActive!==false||'accessToken'in value.connection||'refreshToken'in value.connection||'idToken'in value.connection)fail('predicate_failed','predicate_error');checks.codex_inactive=true;evidence.completed_steps.push('codex');evidence.child_outcome='complete';process.stdout.write(JSON.stringify({status:'KEY_NATIVE_R5_PREFLIGHT_R3_PASS',stage:'complete',checks,evidence}))})().catch(e=>{evidence.failure_category=e&&e.kind||'connection';evidence.child_outcome=e&&e.outcome||'connection';process.stdout.write(JSON.stringify({status:'KEY_NATIVE_R5_PREFLIGHT_R3_STOP',stage,checks,evidence}));process.exitCode=1});
'''

BRANCH = r''' if MODE=='preflight':
  stage='native_preflight';rc,out,err=run(['docker','container','exec','-i','--user','node','--workdir','/app',CANDIDATE,'node','-'],PREFLIGHT_NODE.encode(),60)
  if err or rc not in (0,1):raise Stop()
  native=json.loads(out)
  fields={'status','stage','checks','evidence'}
  if not isinstance(native,dict) or set(native)!=fields or not isinstance(native.get('checks'),dict):raise Stop()
  for name in ('key_api_schema','key_name_absent','combo_api_schema','combo_sentinel_absent','codex_schema','codex_inactive'):
   if native['checks'].get(name) is True:checks[name]=True
  ok=rc==0 and native.get('status')=='KEY_NATIVE_R5_PREFLIGHT_R3_PASS' and native.get('stage')=='complete' and all(native['checks'].values())
  stopped=rc==1 and native.get('status')=='KEY_NATIVE_R5_PREFLIGHT_R3_STOP' and not all(native['checks'].values())
  if not (ok or stopped):raise Stop()
  print(json.dumps({'status':'CANDIDATE_KEY_R5_PREFLIGHT_R3_PASS' if ok else 'CANDIDATE_KEY_R5_PREFLIGHT_R3_STOP','stage':'complete' if ok else native['stage'],'candidate_id':CANDIDATE_ID,'checks':checks,'native':native},sort_keys=True,separators=(',',':')));raise SystemExit(0 if ok else 1)
'''


def render_node(admin, r5):
    if not re.fullmatch(r"oma_[A-Za-z0-9._~-]{16,512}", admin):
        raise Stop("local_validation")
    value = NODE.replace("__ADMIN_B64__", base64.b64encode(admin.encode()).decode())
    value = value.replace("__NAME__", json.dumps(r5.KEY_NAME)).replace("__CODEX__", json.dumps(r5.CODEX_CONNECTION)).replace("__SENTINEL__", json.dumps(r5.COMBO_SENTINEL))
    if admin in value or value.count("'/api/keys'") != 1 or value.count("'/api/combos'") != 1 or value.count("'/api/providers/'") != 1:
        raise Stop("local_validation")
    return value


def render_remote(admin):
    r5 = load(R5, R5_SHA256, "candidate_key_r5_preflight_r3_source")
    source = r5.render_remote(admin, CANDIDATE_ID, "preflight").decode("utf-8")
    node = render_node(admin, r5); lines = source.splitlines()
    constants = next((i for i, line in enumerate(lines) if line.startswith("LIVE_ID=")), None)
    if constants is None: raise Stop("local_validation")
    lines[constants] = (f"LIVE_ID={r5.LIVE_ID!r};LIVE_IMAGE={r5.LIVE_IMAGE!r};LIVE_VOLUME={r5.LIVE_VOLUME!r};CANDIDATE={r5.CANDIDATE_NAME!r};"
                        f"CANDIDATE_ID={CANDIDATE_ID!r};VOLUME={r5.CANDIDATE_VOLUME!r};IMAGE={r5.IMAGE!r};TAG={r5.TAG!r};SOURCE={r5.SOURCE!r};"
                        f"KEY_NAME={r5.KEY_NAME!r};STORE=pathlib.Path({r5.OPERATOR_STORE!r});PREFLIGHT_NODE={node!r};MODE='preflight'")
    source = "\n".join(lines) + "\n"
    helpers = source.index("def rollback_key():"); body = source.index("try:\n candidate_format=", helpers)
    source = source[:helpers] + source[body:]
    start = source.index(" if MODE=='preflight':")
    suffix = r'''except SystemExit:raise
except Exception:
 print(json.dumps({'status':'CANDIDATE_KEY_R5_PREFLIGHT_R3_STOP','stage':stage if stage in CHECK_NAMES or stage in {'store_preflight','native_preflight'} else 'candidate_identity','candidate_id':CANDIDATE_ID,'checks':checks,'native':None},sort_keys=True,separators=(',',':')));raise SystemExit(1)
finally:
 if store_parent_fd is not None:os.close(store_parent_fd)
'''
    source = source[:start] + BRANCH + suffix
    ast.parse(source)
    if any(token in source for token in ("request('POST'", "request('PATCH'", "/v1/chat")):
        raise Stop("local_validation")
    return source.encode("utf-8")


def validate_native(value, returncode):
    fields = {"status", "stage", "checks", "evidence"}
    if not isinstance(value, dict) or set(value) != fields or not isinstance(value["checks"], dict) or set(value["checks"]) != set(NATIVE_CHECKS):
        raise Stop("remote_validation")
    checks = value["checks"]
    if any(type(checks[name]) is not bool for name in NATIVE_CHECKS): raise Stop("remote_validation")
    true_count = sum(checks[name] for name in NATIVE_CHECKS)
    if list(checks[name] for name in NATIVE_CHECKS) != [True] * true_count + [False] * (6 - true_count): raise Stop("remote_validation")
    evidence = value["evidence"]
    ef = {"http_status", "http_category", "schema", "completed_steps", "failure_category", "child_outcome"}
    if not isinstance(evidence, dict) or set(evidence) != ef: raise Stop("remote_validation")
    labels = ("keys", "combos", "codex")
    if any(not isinstance(evidence[name], dict) or set(evidence[name]) != set(labels) for name in ("http_status", "http_category", "schema")): raise Stop("remote_validation")
    expected_steps = (["keys"] if true_count >= 2 else []) + (["combos"] if true_count >= 4 else []) + (["codex"] if true_count == 6 else [])
    if evidence["completed_steps"] != expected_steps: raise Stop("remote_validation")
    status_map = evidence["http_status"]; category_map = evidence["http_category"]; schema_map = evidence["schema"]
    for label in labels:
        status = status_map[label]; category = category_map[label]; schema = schema_map[label]
        if status is not None and (type(status) is not int or not 100 <= status <= 599): raise Stop("remote_validation")
        expected_category = "ok" if status == 200 else "auth_401" if status == 401 else "auth_403" if status == 403 else "server_5xx" if isinstance(status, int) and status >= 500 else "other_http" if isinstance(status, int) else None
        if category != expected_category or schema not in (None, "expected", "mismatch", "not_object"): raise Stop("remote_validation")
    if returncode == 0:
        if value["status"] != "KEY_NATIVE_R5_PREFLIGHT_R3_PASS" or value["stage"] != "complete" or true_count != 6 or evidence["failure_category"] is not None or evidence["child_outcome"] != "complete": raise Stop("remote_validation")
        if any((status_map[label], category_map[label], schema_map[label]) != (200, "ok", "expected") for label in labels): raise Stop("remote_validation")
    else:
        if returncode != 1 or value["status"] != "KEY_NATIVE_R5_PREFLIGHT_R3_STOP" or true_count == 6 or value["stage"] != NATIVE_CHECKS[true_count]: raise Stop("remote_validation")
        current = labels[true_count // 2]
        earlier = labels[:true_count // 2]; later = labels[true_count // 2 + 1:]
        if any((status_map[label], category_map[label], schema_map[label]) != (200, "ok", "expected") for label in earlier): raise Stop("remote_validation")
        if any((status_map[label], category_map[label], schema_map[label]) != (None, None, None) for label in later): raise Stop("remote_validation")
        current_value = (status_map[current], category_map[current], schema_map[current], evidence["failure_category"], evidence["child_outcome"])
        transport = {(None, None, None, name, name) for name in ("timeout", "connection", "output_limit")}
        http = {(code, category, None, category, "http_error") for code, category in ((401, "auth_401"), (403, "auth_403"))}
        if isinstance(status_map[current], int) and status_map[current] != 200:
            http.add((status_map[current], category_map[current], None, category_map[current], "http_error"))
        schema = {(200, "ok", None, "parse_error", "parse_error"),
                  (200, "ok", "mismatch", "schema_mismatch", "schema_error"),
                  (200, "ok", "not_object", "schema_mismatch", "schema_error"),
                  (200, "ok", "expected", "schema_mismatch", "schema_error")}
        predicate = {(200, "ok", "expected", "predicate_failed", "predicate_error")}
        allowed = transport | http | (predicate if true_count % 2 else schema)
        if current_value not in allowed: raise Stop("remote_validation")
    return value


def validate_remote(value, returncode, r5):
    fields = {"status", "stage", "candidate_id", "checks", "native"}
    if not isinstance(value, dict) or set(value) != fields or value["candidate_id"] != CANDIDATE_ID or not isinstance(value["checks"], dict) or tuple(value["checks"]) != tuple(sorted(r5.PREFLIGHT_CHECKS)): raise Stop("remote_validation")
    if value["native"] is None: raise Stop("remote_validation")
    native = validate_native(value["native"], returncode)
    for name in NATIVE_CHECKS:
        if value["checks"][name] is not native["checks"][name]: raise Stop("remote_validation")
    other = set(r5.PREFLIGHT_CHECKS) - set(NATIVE_CHECKS)
    if any(value["checks"][name] is not True for name in other): raise Stop("remote_validation")
    ok = returncode == 0
    if value["status"] != ("CANDIDATE_KEY_R5_PREFLIGHT_R3_PASS" if ok else "CANDIDATE_KEY_R5_PREFLIGHT_R3_STOP") or value["stage"] != ("complete" if ok else native["stage"]): raise Stop("remote_validation")
    return value


def review_payload():
    return {"schema": REVIEW_SCHEMA, "candidate_id": CANDIDATE_ID, "request_method": "GET",
            "request_paths": ["/api/keys", "/api/combos", "/api/providers/" + load(R5, R5_SHA256, "candidate_key_r5_preflight_r3_review").CODEX_CONNECTION],
            "r5_sha256": digest(R5), "transport_sha256": digest(TRANSPORT),
            "keys_route_sha256": digest(KEYS_ROUTE), "combos_route_sha256": digest(COMBOS_ROUTE),
            "provider_route_sha256": digest(PROVIDER_ROUTE), "launcher_sha256": digest(__file__),
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
            count = os.write(fd, raw[offset:]);
            if count <= 0: raise OSError("result_write")
            offset += count
        os.fsync(fd)
    finally: os.close(fd)


def execute(reviewed):
    fixed = ((R5, R5_SHA256), (TRANSPORT, TRANSPORT_SHA256), (KEYS_ROUTE, KEYS_ROUTE_SHA256), (COMBOS_ROUTE, COMBOS_ROUTE_SHA256), (PROVIDER_ROUTE, PROVIDER_ROUTE_SHA256))
    if not all(regular(path) and digest(path) == expected for path, expected in fixed) or not regular(reviewed) or json.loads(reviewed.read_text("utf-8")) != review_payload(): raise Stop("review_pin_mismatch")
    if not os.environ.get("PROGRAMDATA") or os.environ.get("PYTHONOPTIMIZE") is not None: raise Stop("local_validation")
    admin = os.environ.get("OMNIROUTE_ADMIN_TOKEN", "")
    if not re.fullmatch(r"oma_[A-Za-z0-9._~-]{16,512}", admin): raise Stop("local_validation")
    r5 = load(R5, R5_SHA256, "candidate_key_r5_preflight_r3_execute"); transport = load(TRANSPORT, TRANSPORT_SHA256, "candidate_key_r5_preflight_r3_transport")
    fd = reserve_result(); receipt = {"schema": SCHEMA, "status": "UNKNOWN", "stage": "transport", "remote": None}
    try:
        command = [transport.SSH, "-T", *transport.options(VM1205), "belladmin@" + VM1205, "sudo -n python3 -"]
        saved = os.environ.pop("OMNIROUTE_ADMIN_TOKEN", None)
        try: rc, out, err = transport.bounded_capture(command, render_remote(admin), 180)
        finally:
            if saved is not None: os.environ["OMNIROUTE_ADMIN_TOKEN"] = saved
        if err: return 2
        remote = validate_remote(json.loads(out), rc, r5); status = "PASS" if rc == 0 else "STOP"
        receipt = {"schema": SCHEMA, "status": status, "stage": "complete" if rc == 0 else remote["stage"], "remote": remote}
        return 0 if rc == 0 else 1
    except Exception:
        return 2
    finally: finish(fd, receipt)


def self_check():
    for path, expected in ((R5, R5_SHA256), (TRANSPORT, TRANSPORT_SHA256), (KEYS_ROUTE, KEYS_ROUTE_SHA256), (COMBOS_ROUTE, COMBOS_ROUTE_SHA256), (PROVIDER_ROUTE, PROVIDER_ROUTE_SHA256)):
        if not regular(path) or digest(path) != expected: raise Stop("local_validation")
    if RESULT.exists() or RESULT.is_symlink(): raise Stop("stale_result")
    fake = "oma_fixture_preflight_r3_secret"; payload = render_remote(fake)
    if fake.encode() in payload or payload.count(b"/api/keys") != 1 or payload.count(b"/api/combos") != 1 or payload.count(b"/api/providers/") != 1: raise Stop("local_validation")
    ast.parse(payload.decode()); print("CANDIDATE_KEY_R5_PREFLIGHT_R3_PREPARATION_PASS")


def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--self-check", action="store_true"); parser.add_argument("--render-review-payload", action="store_true"); parser.add_argument("--execute-reviewed", type=pathlib.Path); args = parser.parse_args()
    if sum((args.self_check, args.render_review_payload, bool(args.execute_reviewed))) != 1: raise Stop("local_validation")
    if args.self_check: self_check(); return 0
    if args.render_review_payload: print(json.dumps(review_payload(), indent=2, sort_keys=True)); return 0
    return execute(args.execute_reviewed)


if __name__ == "__main__":
    try: raise SystemExit(main())
    except Exception as error:
        stage = str(error) if str(error) in {"stale_result", "review_pin_mismatch"} else "local_validation"
        print(json.dumps({"status": "CANDIDATE_KEY_R5_PREFLIGHT_R3_NOT_EXECUTED", "stage": stage}, sort_keys=True)); raise SystemExit(1)
