"""Prepare the minimum actual-hardware OmniRoute concurrency qualification.

The launcher is deliberately not executable until a reviewed R4 startup result,
exact R4 container ID, and a fresh candidate-only qualification key are bound.
"""
import argparse
import ast
import base64
import concurrent.futures
import hashlib
import importlib.util
import inspect
import json
import os
import pathlib
import re
import time
import uuid


ROOT = pathlib.Path(__file__).resolve().parents[1]
COORDINATOR_ROOT = pathlib.Path(r"C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-auto-switch-20260912")
CANDIDATE_ROOT = pathlib.Path(r"C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-candidate-r4-20260913")
RECONCILIATION_ROOT = pathlib.Path(r"C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-candidate-reconcile-20260913")
MATRIX_ROOT = pathlib.Path(r"C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-auto-switch-matrix-20260913")
CONTRACT = ROOT / "docs/auto-switch-hardware-qualification-r1-contract-20260913.md"
RESULT = ROOT / "docs/auto-switch-hardware-qualification-r1-result-20260913.json"
PLAN = COORDINATOR_ROOT / "docs/auto-switch-final-candidate-proof-plan-20260913.md"
BINDINGS = COORDINATOR_ROOT / "docs/auto-switch-bindings-candidate-20260912.json"
R6 = COORDINATOR_ROOT / "scripts/auto-switch-provider-qualification-r6-20260913.py"
METRICS = COORDINATOR_ROOT / "scripts/auto-switch-q6-authenticated-metrics-r2-20260913.py"
TRANSPORT = COORDINATOR_ROOT / "scripts/auto-switch-image-transfer-r3-20260913.py"
CANDIDATE_LAUNCHER = CANDIDATE_ROOT / "scripts/auto-switch-candidate-start-r4-20260913.py"
CANDIDATE_START_RESULT = CANDIDATE_ROOT / "docs/auto-switch-candidate-start-r4-result-20260913.md"
RECONCILIATION_RESULT = RECONCILIATION_ROOT / "docs/auto-switch-candidate-reconcile-r1-result-20260913.md"
CANDIDATE_KEY_RESULT = COORDINATOR_ROOT / "docs/auto-switch-candidate-key-r4-result-20260913.md"

PLAN_SHA256 = "c8d6710b74f61e453e61a84c2af7836a500f3425a7252be2d816ed37d5a4d3bc"
BINDINGS_SHA256 = "c30aa56eba04d15a50c766a20ba44e88792c60bcddbdf25670fafd5955286e58"
R6_SHA256 = "da1b1114d9273d95499604afff8e1a3de27750f174ff65a6593b219758278868"
METRICS_SHA256 = "4fb6a77ef4ace419d4ab5094bbd6bfbdb276adfac2f0fe064332fb86923e343a"
TRANSPORT_SHA256 = "78bb97e57d6229aae84c2f0d0caaf68eeb71ba6b92e69415d83af2a869b8224a"
CANDIDATE_LAUNCHER_SHA256 = "8dce8544eac30a163a520956a7ed6ee042f52bf00e769554c7d3e72d4fb33fab"
SOURCE = "e53d895e9a5e38a7f06ce59de254835f10e829c1"
IMAGE = "sha256:8211e1071a3b68eac01673d76129150eb0c0fea329dd222bc8bf0394b13fc844"
TAG = "omniroute-auto-switch-r3:" + SOURCE
CANDIDATE_NAME = "omniroute-auto-switch-candidate-r4-20260913"
CANDIDATE_VOLUME = "omniroute-auto-switch-candidate-data-r4-20260913"
CANDIDATE_ID = "UNBOUND"
CANDIDATE_START_RESULT_SHA256 = "cbbd08cfd678021d67bc6f8a799743cfd00d72cff1ce0bbc73960d945e1348bf"
RECONCILIATION_RESULT_SHA256 = "UNBOUND"
KEY_ID = "UNBOUND"
CANDIDATE_KEY_RESULT_SHA256 = "UNBOUND"
CANDIDATE_KEY_STORE = "UNBOUND"
EXECUTION_READY = False

Q6_CONNECTION = "eb57393b-f559-4acf-aac6-3eb4612e6d1f"
Q4_CONNECTION = "da74225c-0fc0-45ce-ad22-ded85edb34b8"
CODEX_CONNECTION = "8f92f200-d280-47b3-b380-2d94be0a4b75"
OPENROUTER_FREE = "441b80a8-0dd8-4d6b-af31-f0e829f500d8"
OPENROUTER_PAID = "c9cf9beb-d5bf-4d47-b65e-e219ea4206b9"
ALL_CONNECTIONS = [Q6_CONNECTION, Q4_CONNECTION, OPENROUTER_FREE, CODEX_CONNECTION, OPENROUTER_PAID]
Q6_MODEL = "llama-cpp/qwen3.8-27b"
Q4_MODEL = "lm-studio/qwen3.8-27b-unsloth-ud-q4ks"
ALLOWED_MODELS = [
    "agent/normal", "agent/high", Q6_MODEL, Q4_MODEL,
    "openrouter/cohere/north-mini-code:free", "openrouter/nex-agi/nex-n2.5-pro:free",
    "openrouter/nvidia/nemotron-3-super-120b-a12b:free", "codex/gpt-5.6-terra",
    "codex/gpt-5.6-sol", "openrouter/deepseek/deepseek-v4-flash-0731",
    "openrouter/z-ai/glm-5.3-flash", "openrouter/moonshotai/kimi-k3",
    "openrouter/z-ai/glm-5.3", "openrouter/qwen/qwen3.8-2.4t-a95b",
]
COMPANION_NAME = "omniroute-auto-switch-hardware-r1-20260913"
NETWORK_NAME = "omniroute-internal"
NETWORK_ID = "baf515e5b9c139e2233df62323a46b50ddc97b99f4c3d427b3ae9b460df9de1c"
NETWORK_SUBNET = "172.18.0.0/16"
NETWORK_GATEWAY = "172.18.0.1"
LIVE_ID = "7b20ca195e3c9e875d0a1ce98832ca469c2a114886335b8466b1467b3ed139bc"
Q4_PROXY_ID = "fc422155a923ea5acee184130110469edf2f9caa97284fa0ec259b9710093756"
TEAM_PROXY_ID = "b979b42dc79015ed70139a7494e2d0b0f47e783752801a2633e6043d967e1203"
VM1205 = "192.168.1.68"
VM1201 = "192.168.1.143"
SATURATION_DEADLINE_SECONDS = 120
DISPATCH_LIMIT_MS = 5000
REQUEST_TIMEOUT_SECONDS = 900
RESULT_LIMIT = 65536
FIXTURE_CANDIDATE_ID = "f" * 64
PREP_FIELDS = {"status", "stage", "candidate_id", "candidate_stopped", "companion_id",
               "detail_baseline", "network_private", "published_ports", "cloud_false",
               "codex_inactive", "migration_170", "migration_171", "key_policy", "health_counters"}
PREP_STOP_FIELDS = {"status", "stage", "candidate_id", "candidate_stopped", "companion_id",
                    "companion_stopped"}


class Stop(Exception):
    pass


def digest(path):
    with pathlib.Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def regular(path):
    path = pathlib.Path(path)
    return path.is_file() and not path.is_symlink()


def require_bound():
    missing = []
    if not re.fullmatch(r"[0-9a-f]{64}", CANDIDATE_ID): missing.append("candidate_id")
    if not re.fullmatch(r"[0-9a-f]{64}", RECONCILIATION_RESULT_SHA256): missing.append("candidate_reconciliation_result_sha256")
    if not re.fullmatch(r"[0-9a-f-]{36}", KEY_ID): missing.append("candidate_key_id")
    if not re.fullmatch(r"[0-9a-f]{64}", CANDIDATE_KEY_RESULT_SHA256): missing.append("candidate_key_result_sha256")
    if not (isinstance(CANDIDATE_KEY_STORE, str) and re.fullmatch(r"/root/\.omniroute-qualification/[a-z0-9._-]+\.key", CANDIDATE_KEY_STORE)):
        missing.append("candidate_key_store")
    return missing


def metric(value):
    if not isinstance(value, dict) or set(value) != {"processing", "deferred"}:
        raise Stop("result_validation")
    if any(type(value[k]) is not int or value[k] < 0 for k in value):
        raise Stop("result_validation")
    if value["processing"] > 2 or value["deferred"] > 1_000_000:
        raise Stop("result_validation")
    return value


def request_record(value, index):
    fields = {"index", "task_id", "run_id", "turn_id", "idempotency_key", "request_id",
              "selected_connection_id", "resolved_provider", "resolved_model", "candidate_attempt",
              "reviewer_verdict", "fallback_reason", "content_valid", "q6_submissions",
              "q4_submissions", "q4_http_status", "q4_selected_ms", "turn_completed"}
    if not isinstance(value, dict) or set(value) != fields or value["index"] != index:
        raise Stop("result_validation")
    for key in ("task_id", "run_id", "turn_id", "idempotency_key", "request_id"):
        if not isinstance(value[key], str) or not re.fullmatch(r"[0-9a-f-]{36}", value[key]):
            raise Stop("result_validation")
    if value["content_valid"] is not True or value["turn_completed"] is not True:
        raise Stop("result_validation")
    if value["reviewer_verdict"] != "PASS" or type(value["candidate_attempt"]) is not int or value["candidate_attempt"] < 1:
        raise Stop("result_validation")
    if any(not isinstance(value[k], str) or not value[k] for k in ("resolved_provider", "resolved_model", "fallback_reason")):
        raise Stop("result_validation")
    if index < 3:
        expected = {"selected_connection_id": Q6_CONNECTION, "q6_submissions": 1,
                    "q4_submissions": 0, "q4_http_status": None, "q4_selected_ms": None}
    else:
        expected = {"selected_connection_id": Q4_CONNECTION, "q6_submissions": 0,
                    "q4_submissions": 1, "q4_http_status": 200}
        if type(value["q4_selected_ms"]) is not int or not 0 <= value["q4_selected_ms"] <= DISPATCH_LIMIT_MS:
            raise Stop("result_validation")
        if value["fallback_reason"] not in {"capacity", "full"}:
            raise Stop("result_validation")
    if any(value[k] != want for k, want in expected.items()):
        raise Stop("result_validation")
    return value


def health_counters(value):
    fields = {"attempts", "timeouts", "nonzero", "successes"}
    if not isinstance(value, dict) or set(value) != fields:
        raise Stop("result_validation")
    if any(type(value[key]) is not int or value[key] < 0 for key in fields):
        raise Stop("result_validation")
    if value["successes"] != 1 or value["attempts"] != value["timeouts"] + value["nonzero"] + value["successes"]:
        raise Stop("result_validation")
    return value


def emitted_fields(source, status):
    matches = []
    for node in ast.walk(ast.parse(source)):
        if not isinstance(node, ast.Dict) or not all(isinstance(key, ast.Constant) and isinstance(key.value, str) for key in node.keys):
            continue
        keys = [key.value for key in node.keys]
        for key, value in zip(keys, node.values):
            if key == "status" and isinstance(value, ast.Constant) and value.value == status:
                matches.append(set(keys))
    if len(matches) != 1:
        raise Stop("local_validation")
    return matches[0]


def validate_result(value, returncode, expected_candidate_id=None):
    fields = {"status", "source", "image", "candidate_id", "candidate_stopped", "companion_id",
              "companion_stopped", "network_private", "published_ports", "metrics_baseline",
              "metrics_before_third", "final_metrics", "requests", "correlation", "no_log",
              "cloud_false", "codex_inactive", "migration_170", "migration_171", "key_id",
              "health_counters"}
    if returncode != 0 or not isinstance(value, dict) or set(value) != fields:
        raise Stop("result_validation")
    candidate_id = expected_candidate_id or CANDIDATE_ID
    if value["status"] != "HARDWARE_QUALIFICATION_R1_PASS" or value["source"] != SOURCE or value["image"] != IMAGE:
        raise Stop("result_validation")
    if value["candidate_id"] != candidate_id or not re.fullmatch(r"[0-9a-f]{64}", value["candidate_id"]):
        raise Stop("result_validation")
    if value["candidate_stopped"] is not True or value["companion_stopped"] is not True:
        raise Stop("result_validation")
    if not re.fullmatch(r"[0-9a-f]{64}", value["companion_id"]):
        raise Stop("result_validation")
    for key in ("network_private", "no_log", "cloud_false", "codex_inactive", "migration_170", "migration_171"):
        if value[key] is not True: raise Stop("result_validation")
    if value["published_ports"] != 0 or value["key_id"] != (KEY_ID if expected_candidate_id is None else "11111111-1111-4111-8111-111111111111"):
        raise Stop("result_validation")
    if metric(value["metrics_baseline"]) != {"processing": 0, "deferred": 0}:
        raise Stop("result_validation")
    if metric(value["metrics_before_third"]) != {"processing": 2, "deferred": 0}:
        raise Stop("result_validation")
    if metric(value["final_metrics"]) != {"processing": 0, "deferred": 0}:
        raise Stop("result_validation")
    health_counters(value["health_counters"])
    if not isinstance(value["requests"], list) or len(value["requests"]) != 3:
        raise Stop("result_validation")
    for index, row in enumerate(value["requests"], 1): request_record(row, index)
    correlation = value["correlation"]
    if not isinstance(correlation, dict) or set(correlation) != {"complete", "tuple_count", "q6_full_event",
                                                                  "processing_two_event", "deferred_zero_event",
                                                                  "q4_after_full", "payload_fields_retained"}:
        raise Stop("result_validation")
    if correlation != {"complete": True, "tuple_count": 3, "q6_full_event": True,
                       "processing_two_event": True, "deferred_zero_event": True,
                       "q4_after_full": True, "payload_fields_retained": False}:
        raise Stop("result_validation")
    return value


def fixture_result():
    def row(index, selected, q6, q4, q4_status=None, q4_ms=None, reason="initial"):
        return {"index": index, "task_id": str(uuid.uuid4()), "run_id": str(uuid.uuid4()),
                "turn_id": str(uuid.uuid4()), "idempotency_key": str(uuid.uuid4()),
                "request_id": str(uuid.uuid4()), "selected_connection_id": selected,
                "resolved_provider": "llama-cpp" if index < 3 else "lm-studio",
                "resolved_model": Q6_MODEL if index < 3 else Q4_MODEL,
                "candidate_attempt": 1, "reviewer_verdict": "PASS", "fallback_reason": reason,
                "content_valid": True, "q6_submissions": q6, "q4_submissions": q4,
                "q4_http_status": q4_status, "q4_selected_ms": q4_ms, "turn_completed": True}
    return {"status": "HARDWARE_QUALIFICATION_R1_PASS", "source": SOURCE, "image": IMAGE,
            "candidate_id": FIXTURE_CANDIDATE_ID, "candidate_stopped": True,
            "companion_id": "e" * 64, "companion_stopped": True, "network_private": True,
            "published_ports": 0, "metrics_baseline": {"processing": 0, "deferred": 0},
            "metrics_before_third": {"processing": 2, "deferred": 0},
            "final_metrics": {"processing": 0, "deferred": 0},
            "requests": [row(1, Q6_CONNECTION, 1, 0), row(2, Q6_CONNECTION, 1, 0),
                         row(3, Q4_CONNECTION, 0, 1, 200, 4999, "full")],
            "correlation": {"complete": True, "tuple_count": 3, "q6_full_event": True,
                            "processing_two_event": True, "deferred_zero_event": True,
                            "q4_after_full": True, "payload_fields_retained": False},
            "no_log": True, "cloud_false": True, "codex_inactive": True,
            "migration_170": True, "migration_171": True,
            "health_counters": {"attempts": 3, "timeouts": 1, "nonzero": 1, "successes": 1},
            "key_id": "11111111-1111-4111-8111-111111111111"}


REMOTE_PREP = r'''
import json,os,pathlib,re,sqlite3,stat,time,urllib.parse
__BOUNDED_CAPTURE__
LIVE_ID=__LIVE_ID__;CANDIDATE=__CANDIDATE__;CANDIDATE_ID=__CANDIDATE_ID__;VOLUME=__VOLUME__;IMAGE=__IMAGE__;TAG=__TAG__;SOURCE=__SOURCE__;KEY_ID=__KEY_ID__;STORE=pathlib.Path(__STORE__);COMPANION=__COMPANION__;NETWORK=__NETWORK__;NETWORK_ID=__NETWORK_ID__;Q4=__Q4__;TEAM=__TEAM__;ALLOWED_MODELS=__ALLOWED_MODELS__;ALL_CONNECTIONS=__ALL_CONNECTIONS__;CODEX=__CODEX__
stage='identity';companion_id=None;candidate_stopped=False;health={'attempts':0,'timeouts':0,'nonzero':0,'successes':0}
class Stop(Exception):pass
def run(a,p=None,t=60):
 rc,out,_=bounded_capture(a,p,t)
 if rc:raise Stop()
 return out
def docker(a,p=None,t=60):return run(['docker',*a],p,t)
def one(a):
 v=json.loads(docker(a))
 if not isinstance(v,list) or len(v)!=1 or not isinstance(v[0],dict):raise Stop()
 return v[0]
def envmap(v):
 out={}
 for row in v:
  if not isinstance(row,str) or '=' not in row:raise Stop()
  k,x=row.split('=',1)
  if not k or k in out:raise Stop()
  out[k]=x
 return out
def stop_companion():
 if not companion_id:return None
 try:
  row=one(['container','inspect',COMPANION])
  if row.get('Id')!=companion_id or row.get('Image')!=IMAGE:return None
  if row.get('State',{}).get('Running'):
   if docker(['container','stop','--timeout','10',COMPANION],t=25).decode().strip()!=COMPANION:return None
  row=one(['container','inspect',COMPANION])
  return row.get('Id')==companion_id and row.get('State',{}).get('Running') is False
 except:return None
try:
 live=one(['container','inspect','omniroute'])
 if live.get('Id')!=LIVE_ID or live.get('State',{}).get('Running') is not True:raise Stop()
 candidate=one(['container','inspect',CANDIDATE]);state=candidate.get('State',{});host=candidate.get('HostConfig',{});net=candidate.get('NetworkSettings',{})
 if candidate.get('Id')!=CANDIDATE_ID or candidate.get('Image')!=IMAGE or state.get('Running') is not True or state.get('Health',{}).get('Status')!='healthy' or candidate.get('RestartCount')!=0:raise Stop()
 if host.get('NetworkMode')!='none' or host.get('PortBindings') not in (None,{}) or any(v is not None for v in (net.get('Ports') or {}).values()):raise Stop()
 if len(candidate.get('Mounts',[]))!=1 or candidate['Mounts'][0].get('Name')!=VOLUME or candidate['Mounts'][0].get('Destination')!='/app/data':raise Stop()
 labels=one(['image','inspect',IMAGE]).get('Config',{}).get('Labels') or {}
 if labels.get('org.opencontainers.image.revision')!=SOURCE:raise Stop()
 vol=one(['volume','inspect',VOLUME]);root=pathlib.Path(vol.get('Mountpoint',''))
 if vol.get('Name')!=VOLUME or vol.get('Driver')!='local' or vol.get('Scope')!='local' or not root.is_dir() or root.is_symlink() or pathlib.Path(os.path.realpath(root))!=root:raise Stop()
 db=sqlite3.connect('file:'+urllib.parse.quote(str(root/'storage.sqlite'),safe='/')+'?mode=ro',uri=True,timeout=10)
 try:
  db.execute('PRAGMA query_only=ON');db.execute('BEGIN')
  if db.execute('PRAGMA quick_check').fetchall()!=[('ok',)]:raise Stop()
  cloud=db.execute("SELECT value FROM key_value WHERE namespace='settings' AND key='cloudEnabled'").fetchall()
  codex=db.execute('SELECT id,is_active FROM provider_connections WHERE id=?',(CODEX,)).fetchall()
  key=db.execute('SELECT id,no_log,is_active,allowed_models,allowed_connections,scopes,allowed_endpoints FROM api_keys WHERE id=?',(KEY_ID,)).fetchall()
  migrations=set(db.execute("SELECT version,name FROM _omniroute_migrations WHERE version IN ('170','171')"))
  cols={x[1] for x in db.execute('PRAGMA table_info(agent_route_events)')}
  detail=db.execute('SELECT count(*) FROM request_detail_logs').fetchone()[0]
  if cloud!=[('false',)] and not (len(cloud)==1 and json.loads(cloud[0][0]) is False):raise Stop()
  if codex!=[(CODEX,0)] or len(key)!=1 or key[0][1:3]!=(1,1):raise Stop()
  if json.loads(key[0][3])!=ALLOWED_MODELS or json.loads(key[0][4])!=ALL_CONNECTIONS or json.loads(key[0][5])!=['agent:route'] or set(json.loads(key[0][6]))!={'chat','models'}:raise Stop()
  if ('170','170_agent_route_runs') not in migrations or ('171','171_agent_route_deferred_metrics') not in migrations or 'deferred_requests' not in cols:raise Stop()
  db.execute('ROLLBACK')
 finally:db.close()
 before=os.lstat(STORE)
 if not stat.S_ISREG(before.st_mode) or stat.S_ISLNK(before.st_mode) or before.st_uid!=0 or before.st_gid!=0 or stat.S_IMODE(before.st_mode)!=0o600 or before.st_size>512 or pathlib.Path(os.path.realpath(STORE))!=STORE:raise Stop()
 network=one(['network','inspect',NETWORK]);cfg=network.get('IPAM',{}).get('Config')
 if network.get('Id')!=NETWORK_ID or network.get('Internal') is not False or len(cfg or [])!=1 or cfg[0].get('Subnet')!='172.18.0.0/16' or cfg[0].get('Gateway')!='172.18.0.1':raise Stop()
 members=network.get('Containers',{})
 if set(members)!={LIVE_ID,Q4,TEAM}:raise Stop()
 for expected in (Q4,TEAM):
  peer=one(['container','inspect',expected])
  if peer.get('Id')!=expected or peer.get('State',{}).get('Running') is not True or NETWORK not in (peer.get('NetworkSettings',{}).get('Networks') or {}):raise Stop()
 if COMPANION in docker(['container','ls','--all','--format','{{.Names}}']).decode().splitlines():raise Stop()
 stage='candidate_stop'
 if docker(['container','stop','--timeout','10',CANDIDATE],t=25).decode().strip()!=CANDIDATE:raise Stop()
 candidate=one(['container','inspect',CANDIDATE])
 if candidate.get('Id')!=CANDIDATE_ID or candidate.get('State',{}).get('Running') is not False or candidate.get('State',{}).get('OOMKilled') is not False:raise Stop()
 candidate_stopped=True
 stage='companion_create';env=envmap(candidate.get('Config',{}).get('Env',[]));fixed={'DATA_DIR':'/app/data','OMNIROUTE_AGENT_ROUTE_BINDINGS_JSON':env.get('OMNIROUTE_AGENT_ROUTE_BINDINGS_JSON'),'OMNIROUTE_DISABLE_BACKGROUND_SERVICES':'true','OMNIROUTE_DISABLE_CREDENTIAL_HEALTH_CHECK':'1','PROXY_HEALTH_ENABLED':'false','FREE_PROXY_AUTO_SYNC_ENABLED':'false','OMNIROUTE_ENABLE_LIVE_WS':'0','OMNIROUTE_DB_HEALTHCHECK_INTERVAL_MS':'0','OMNIROUTE_WAL_TRUNCATE_INTERVAL_MS':'0'}
 if not fixed['OMNIROUTE_AGENT_ROUTE_BINDINGS_JSON']:raise Stop()
 args=['container','create','--name',COMPANION,'--user','node','--network',NETWORK,'--read-only','--tmpfs','/tmp:rw,noexec,nosuid,nodev,size=67108864,mode=1777','--cap-drop','ALL','--security-opt','no-new-privileges','--restart','no','--mount','type=volume,src='+VOLUME+',dst=/app/data']
 for k in sorted(fixed):args.extend(['--env',k+'='+fixed[k]])
 companion_id=docker([*args,TAG],t=60).decode().strip()
 if not re.fullmatch(r'[0-9a-f]{64}',companion_id):raise Stop()
 stage='companion_start'
 if docker(['container','start',COMPANION],t=60).decode().strip()!=COMPANION:raise Stop()
 deadline=time.monotonic()+180
 while time.monotonic()+15<=deadline:
  health['attempts']+=1
  try:rc,_,_=bounded_capture(['docker','container','exec','--user','node',COMPANION,'node','healthcheck.mjs'],None,15)
  except RuntimeError as error:
   if str(error)!='COMMAND_TIMEOUT':raise
   health['timeouts']+=1;time.sleep(2);continue
  if rc==0:health['successes']+=1;break
  health['nonzero']+=1
  time.sleep(2)
 else:raise Stop()
 row=one(['container','inspect',COMPANION]);ports=row.get('NetworkSettings',{}).get('Ports') or {}
 if row.get('Id')!=companion_id or row.get('Image')!=IMAGE or row.get('State',{}).get('Running') is not True or row.get('HostConfig',{}).get('NetworkMode')!=NETWORK or any(v is not None for v in ports.values()):raise Stop()
 print(json.dumps({'status':'HARDWARE_PREP_PASS','stage':'complete','candidate_id':CANDIDATE_ID,'candidate_stopped':True,'companion_id':companion_id,'detail_baseline':detail,'network_private':True,'published_ports':0,'cloud_false':True,'codex_inactive':True,'migration_170':True,'migration_171':True,'key_policy':True,'health_counters':health},sort_keys=True))
except Exception:
 stopped=stop_companion()
 print(json.dumps({'status':'HARDWARE_PREP_STOP','stage':stage if stage in {'identity','candidate_stop','companion_create','companion_start'} else 'identity','candidate_id':CANDIDATE_ID,'candidate_stopped':candidate_stopped,'companion_id':companion_id,'companion_stopped':stopped},sort_keys=True));raise SystemExit(1)
'''


REMOTE_EVIDENCE = r'''
import datetime,json,os,pathlib,re,sqlite3,urllib.parse
__BOUNDED_CAPTURE__
COMPANION=__COMPANION__;COMPANION_ID=__COMPANION_ID__;IMAGE=__IMAGE__;VOLUME=__VOLUME__;KEY_ID=__KEY_ID__;IDS=__IDS__;Q6=__Q6__;Q4=__Q4__;DETAIL=__DETAIL__
class Stop(Exception):pass
def docker(a,t=60):
 rc,out,_=bounded_capture(['docker',*a],None,t)
 if rc:raise Stop()
 return out
def one(a):
 v=json.loads(docker(a))
 if not isinstance(v,list) or len(v)!=1:return None
 return v[0]
try:
 row=one(['container','inspect',COMPANION])
 if not row or row.get('Id')!=COMPANION_ID or row.get('Image')!=IMAGE:raise Stop()
 if row.get('State',{}).get('Running'):
  if docker(['container','stop','--timeout','10',COMPANION],25).decode().strip()!=COMPANION:raise Stop()
 row=one(['container','inspect',COMPANION])
 if not row or row.get('Id')!=COMPANION_ID or row.get('State',{}).get('Running') is not False or row.get('State',{}).get('OOMKilled') is not False:raise Stop()
 vol=one(['volume','inspect',VOLUME]);root=pathlib.Path(vol.get('Mountpoint',''))
 if vol.get('Name')!=VOLUME or not root.is_dir() or root.is_symlink():raise Stop()
 db=sqlite3.connect('file:'+urllib.parse.quote(str(root/'storage.sqlite'),safe='/')+'?mode=ro',uri=True,timeout=10)
 try:
  db.execute('PRAGMA query_only=ON');db.execute('BEGIN')
  if db.execute('PRAGMA quick_check').fetchall()!=[('ok',)] or db.execute('SELECT count(*) FROM request_detail_logs').fetchone()[0]!=DETAIL:raise Stop()
  rows=[];complete=True;full=False;processing=False;deferred=False;q4after=False
  for index,ident in enumerate(IDS,1):
   turn=db.execute('SELECT state,created_at FROM agent_route_turns WHERE run_id=? AND turn_id=? AND idempotency_key=?',(ident['run_id'],ident['turn_id'],ident['idempotency_key'])).fetchall()
   run=db.execute('SELECT api_key_id,task_id FROM agent_route_runs WHERE run_id=?',(ident['run_id'],)).fetchall()
   events=db.execute('SELECT kind,connection_id,admission_state,fallback_reason,latency_ms,busy_slots,processing_requests,deferred_requests,objective_outcome,reviewer_verdict,occurred_at FROM agent_route_events WHERE run_id=? AND turn_id=? ORDER BY occurred_at,event_id',(ident['run_id'],ident['turn_id'])).fetchall()
   if len(turn)!=1 or turn[0][0]!='completed' or run!=[(KEY_ID,ident['task_id'])]:raise Stop()
   q6ad=sum(1 for x in events if x[1]==Q6 and x[2]=='admitted');q4ad=sum(1 for x in events if x[1]==Q4 and x[2]=='admitted')
   q4ms=None
   if index<3:
    if q6ad!=1 or q4ad!=0:raise Stop()
   else:
    fullrows=[x for x in events if x[1]==Q6 and x[2]=='full' and x[5]==2 and x[6]==2 and x[7]==0]
    q4rows=[x for x in events if x[1]==Q4 and x[0]=='dispatch' and x[3] in ('full','capacity')]
    if q6ad or q4ad!=1 or not fullrows or not q4rows:raise Stop()
    start=datetime.datetime.fromisoformat(turn[0][1].replace('Z','+00:00'));picked=datetime.datetime.fromisoformat(q4rows[0][10].replace('Z','+00:00'));q4ms=max(0,round((picked-start).total_seconds()*1000))
    if q4ms>5000:raise Stop()
    full=processing=deferred=q4after=True
   if not any(x[8]=='PASS' for x in events) or not any(x[9]=='PASS' for x in events):raise Stop()
   rows.append({'index':index,'q6_submissions':q6ad,'q4_submissions':q4ad,'q4_selected_ms':q4ms,'turn_completed':True})
  bad=db.execute('SELECT count(*) FROM call_logs WHERE api_key_id=? AND (has_request_body!=0 OR has_response_body!=0 OR has_pipeline_details!=0 OR artifact_relpath IS NOT NULL OR request_summary IS NOT NULL)',(KEY_ID,)).fetchone()[0]
  if bad:raise Stop()
  db.execute('ROLLBACK')
 finally:db.close()
 print(json.dumps({'status':'HARDWARE_EVIDENCE_PASS','companion_stopped':True,'rows':rows,'correlation':{'complete':complete,'tuple_count':3,'q6_full_event':full,'processing_two_event':processing,'deferred_zero_event':deferred,'q4_after_full':q4after,'payload_fields_retained':False},'no_log':True},sort_keys=True))
except Exception:
 print(json.dumps({'status':'HARDWARE_EVIDENCE_STOP','companion_stopped':None},sort_keys=True));raise SystemExit(1)
'''


REMOTE_REQUEST = r'''
import base64,json,os,pathlib,re,stat
__BOUNDED_CAPTURE__
COMPANION=__COMPANION__;COMPANION_ID=__COMPANION_ID__;IMAGE=__IMAGE__;STORE=pathlib.Path(__STORE__)
IDS=__IDS__;INDEX=__INDEX__
def stop(): print(json.dumps({'status':'REQUEST_STOP','index':INDEX},sort_keys=True));raise SystemExit(1)
try:
 row=json.loads(bounded_capture(['docker','container','inspect',COMPANION],None,30)[1])[0]
 if row.get('Id')!=COMPANION_ID or row.get('Image')!=IMAGE or row.get('State',{}).get('Running') is not True:stop()
 before=os.lstat(STORE)
 if not stat.S_ISREG(before.st_mode) or stat.S_ISLNK(before.st_mode) or before.st_uid!=0 or before.st_gid!=0 or stat.S_IMODE(before.st_mode)!=0o600 or before.st_size>512 or pathlib.Path(os.path.realpath(STORE))!=STORE:stop()
 fd=os.open(STORE,os.O_RDONLY|os.O_NOFOLLOW)
 try:
  opened=os.fstat(fd);key=os.read(fd,513);after=os.fstat(fd)
  if (after.st_dev,after.st_ino,after.st_size,after.st_mtime_ns)!=(opened.st_dev,opened.st_ino,opened.st_size,opened.st_mtime_ns):stop()
 finally:os.close(fd)
 if not re.fullmatch(rb'sk-[0-9a-f]{16}-[0-9a-f]{6}-[0-9a-f]{8}',key):stop()
 node=r"""const http=require('node:http');const key=Buffer.from('__KEY__','base64').toString();const ids=__NODE_IDS__;const body=Buffer.from(JSON.stringify({model:'agent/normal',stream:false,messages:[{role:'user',content:'Produce a detailed complete technical explanation of safe concurrent queue admission without tools.'}],omniroute_route:{checks:[{kind:'nonempty'}]}}));const headers={authorization:'Bearer '+key,'content-type':'application/json','content-length':String(body.length),'x-request-id':ids.request_id,'x-omniroute-task-id':ids.task_id,'x-omniroute-run-id':ids.run_id,'x-omniroute-turn-id':ids.turn_id,'x-omniroute-idempotency-key':ids.idempotency_key,'x-omniroute-review-class':'standard'};const req=http.request({host:'127.0.0.1',port:20128,path:'/v1/chat/completions',method:'POST',headers},res=>{let n=0,a=[];res.on('data',c=>{n+=c.length;if(n>1048576)req.destroy();else a.push(c)});res.on('end',()=>{let v=null;try{v=JSON.parse(Buffer.concat(a).toString('utf8'))}catch{};const valid=res.statusCode===200&&v&&Array.isArray(v.choices)&&v.choices.length>0&&v.choices.every(x=>x&&x.message&&typeof x.message.content==='string'&&x.message.content.length>0);process.stdout.write(JSON.stringify({status:res.statusCode,content_valid:!!valid,selected_connection_id:res.headers['x-omniroute-selected-connection-id']||null,resolved_provider:res.headers['x-omniroute-resolved-provider']||null,resolved_model:res.headers['x-omniroute-resolved-model']||null,candidate_attempt:Number(res.headers['x-omniroute-candidate-attempt']),reviewer_verdict:res.headers['x-omniroute-reviewer-verdict']||null,fallback_reason:res.headers['x-omniroute-fallback-reason']||''}))})});req.setTimeout(840000,()=>req.destroy());req.on('error',()=>process.exit(1));req.write(body);req.end();"""
 node=node.replace('__KEY__',base64.b64encode(key).decode()).replace('__NODE_IDS__',json.dumps(IDS,separators=(',',':')))
 rc,out,_=bounded_capture(['docker','container','exec','-i','--user','node','--workdir','/app',COMPANION,'node','-'],node.encode(),900,1048576,65536)
 value=json.loads(out);key=b'';node=''
 safe={'status':'REQUEST_PASS' if rc==0 else 'REQUEST_STOP','index':INDEX,'http_status':value.get('status') if isinstance(value,dict) else None,'content_valid':value.get('content_valid') is True if isinstance(value,dict) else False,'selected_connection_id':value.get('selected_connection_id') if isinstance(value,dict) else None,'resolved_provider':value.get('resolved_provider') if isinstance(value,dict) else None,'resolved_model':value.get('resolved_model') if isinstance(value,dict) else None,'candidate_attempt':value.get('candidate_attempt') if isinstance(value,dict) else None,'reviewer_verdict':value.get('reviewer_verdict') if isinstance(value,dict) else None,'fallback_reason':value.get('fallback_reason') if isinstance(value,dict) else None}
 print(json.dumps(safe,sort_keys=True));raise SystemExit(0 if rc==0 else 1)
except SystemExit:raise
except Exception:stop()
'''


def load_module(path, expected, name):
    if not regular(path) or digest(path) != expected: raise Stop("local_validation")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


def render_request(index, ids, companion_id):
    if index not in {1, 2, 3} or set(ids) != {"task_id", "run_id", "turn_id", "idempotency_key", "request_id"}:
        raise Stop("local_validation")
    helper = load_module(TRANSPORT, TRANSPORT_SHA256, "hardware_transport_render")
    values = {"__BOUNDED_CAPTURE__": inspect.getsource(helper.bounded_capture),
              "__COMPANION__": repr(COMPANION_NAME), "__COMPANION_ID__": repr(companion_id),
              "__IMAGE__": repr(IMAGE), "__STORE__": repr(CANDIDATE_KEY_STORE),
              "__IDS__": repr(ids), "__INDEX__": repr(index)}
    value = REMOTE_REQUEST
    for key, item in values.items():
        if value.count(key) != 1: raise Stop("local_validation")
        value = value.replace(key, item)
    ast.parse(value)
    return value.encode("utf-8")


def render_script(template, values):
    helper = load_module(TRANSPORT, TRANSPORT_SHA256, "hardware_transport_render")
    replacements = {"__BOUNDED_CAPTURE__": inspect.getsource(helper.bounded_capture), **values}
    value = template
    for key, item in replacements.items():
        if value.count(key) != 1: raise Stop("local_validation")
        value = value.replace(key, item)
    ast.parse(value)
    return value.encode("utf-8")


def render_prep():
    return render_script(REMOTE_PREP, {
        "__LIVE_ID__": repr(LIVE_ID), "__CANDIDATE__": repr(CANDIDATE_NAME),
        "__CANDIDATE_ID__": repr(CANDIDATE_ID), "__VOLUME__": repr(CANDIDATE_VOLUME),
        "__IMAGE__": repr(IMAGE), "__TAG__": repr(TAG), "__SOURCE__": repr(SOURCE),
        "__KEY_ID__": repr(KEY_ID), "__STORE__": repr(CANDIDATE_KEY_STORE),
        "__COMPANION__": repr(COMPANION_NAME), "__NETWORK__": repr(NETWORK_NAME),
        "__NETWORK_ID__": repr(NETWORK_ID), "__Q4__": repr(Q4_PROXY_ID),
        "__TEAM__": repr(TEAM_PROXY_ID), "__ALLOWED_MODELS__": repr(ALLOWED_MODELS),
        "__ALL_CONNECTIONS__": repr(ALL_CONNECTIONS), "__CODEX__": repr(CODEX_CONNECTION),
    })


def render_evidence(ids, companion_id, detail_baseline):
    return render_script(REMOTE_EVIDENCE, {
        "__COMPANION__": repr(COMPANION_NAME), "__COMPANION_ID__": repr(companion_id),
        "__IMAGE__": repr(IMAGE), "__VOLUME__": repr(CANDIDATE_VOLUME),
        "__KEY_ID__": repr(KEY_ID), "__IDS__": repr(ids), "__Q6__": repr(Q6_CONNECTION),
        "__Q4__": repr(Q4_CONNECTION), "__DETAIL__": repr(detail_baseline),
    })


REMOTE_STOP = r'''
import json
__BOUNDED_CAPTURE__
name=__COMPANION__;cid=__COMPANION_ID__;image=__IMAGE__;stopped=None;category=None
try:
 rc,out,_=bounded_capture(['docker','container','inspect',name],None,30)
 rows=json.loads(out) if rc==0 else []
 if len(rows)!=1 or rows[0].get('Id')!=cid or rows[0].get('Image')!=image:category='identity'
 else:
  if rows[0].get('State',{}).get('Running'):
   rc,out,_=bounded_capture(['docker','container','stop','--timeout','10',name],None,25)
   if rc or out.decode().strip()!=name:category='stop'
  if category is None:
   rc,out,_=bounded_capture(['docker','container','inspect',name],None,30);rows=json.loads(out) if rc==0 else []
   stopped=len(rows)==1 and rows[0].get('Id')==cid and rows[0].get('State',{}).get('Running') is False
   if not stopped:category='reinspection'
except:category='validation'
print(json.dumps({'status':'HARDWARE_STOP_PASS' if stopped else 'HARDWARE_STOP_STOP','companion_id':cid,'companion_stopped':stopped,'category':category},sort_keys=True));raise SystemExit(0 if stopped else 1)
'''


def render_stop(companion_id):
    return render_script(REMOTE_STOP, {"__COMPANION__": repr(COMPANION_NAME),
                                      "__COMPANION_ID__": repr(companion_id), "__IMAGE__": repr(IMAGE)})


def new_ids():
    return {name: str(uuid.uuid4()) for name in ("task_id", "run_id", "turn_id", "idempotency_key", "request_id")}


def validate_request(value, index):
    fields = {"status", "index", "http_status", "content_valid", "selected_connection_id",
              "resolved_provider", "resolved_model", "candidate_attempt", "reviewer_verdict", "fallback_reason"}
    if not isinstance(value, dict) or set(value) != fields or value["status"] != "REQUEST_PASS" or value["index"] != index:
        raise Stop("request_validation")
    if value["http_status"] != 200 or value["content_valid"] is not True:
        raise Stop("request_validation")
    if type(value["candidate_attempt"]) is not int or value["candidate_attempt"] < 1 or value["reviewer_verdict"] != "PASS":
        raise Stop("request_validation")
    if any(not isinstance(value[k], str) or not value[k] for k in ("selected_connection_id", "resolved_provider", "resolved_model", "fallback_reason")):
        raise Stop("request_validation")
    expected = Q6_CONNECTION if index < 3 else Q4_CONNECTION
    if value["selected_connection_id"] != expected: raise Stop("request_validation")
    return value


def command(transport, host, user="belladmin"):
    return [transport.SSH, "-T", *transport.options(host), user + "@" + host, "sudo -n python3 -"]


def invoke(transport, host, payload, timeout):
    try:
        returncode, stdout, stderr = transport.bounded_capture(command(transport, host), payload, timeout)
    except RuntimeError as error:
        raise Stop("transport_unknown") from error
    if stderr or len(stdout) > RESULT_LIMIT:
        raise Stop("transport_unknown")
    try:
        value = json.loads(stdout)
    except Exception as error:
        raise Stop("transport_unknown") from error
    return value, returncode


def validate_prep(value, returncode, expected_candidate_id=None):
    if returncode or not isinstance(value, dict) or set(value) != PREP_FIELDS or value["status"] != "HARDWARE_PREP_PASS":
        raise Stop("prep_stop")
    if value["stage"] != "complete" or value["candidate_id"] != (expected_candidate_id or CANDIDATE_ID) or value["candidate_stopped"] is not True:
        raise Stop("prep_validation")
    if not re.fullmatch(r"[0-9a-f]{64}", value["companion_id"]): raise Stop("prep_validation")
    if type(value["detail_baseline"]) is not int or value["detail_baseline"] < 0: raise Stop("prep_validation")
    if value["published_ports"] != 0 or any(value[k] is not True for k in ("network_private", "cloud_false", "codex_inactive", "migration_170", "migration_171", "key_policy")):
        raise Stop("prep_validation")
    health_counters(value["health_counters"])
    return value


def validate_prep_stop(value, returncode):
    if returncode == 0 or not isinstance(value, dict) or set(value) != PREP_STOP_FIELDS or value["status"] != "HARDWARE_PREP_STOP":
        raise Stop("transport_unknown")
    if value["stage"] not in {"identity", "candidate_stop", "companion_create", "companion_start"} or value["candidate_id"] != CANDIDATE_ID:
        raise Stop("transport_unknown")
    if type(value["candidate_stopped"]) is not bool:
        raise Stop("transport_unknown")
    if value["companion_id"] is not None and not re.fullmatch(r"[0-9a-f]{64}", value["companion_id"]):
        raise Stop("transport_unknown")
    if value["companion_stopped"] not in (None, True, False):
        raise Stop("transport_unknown")
    return value


def metric_sample(transport, metrics_module):
    payload = metrics_module.render_remote().encode("utf-8")
    value, returncode = invoke(transport, VM1201, payload, 60)
    try: value = metrics_module.validate_result(value, returncode)
    except Exception as error: raise Stop("metrics_validation") from error
    if value.get("status") != "Q6_AUTHENTICATED_METRICS_PASS": raise Stop("metrics_validation")
    return {"processing": value["requests_processing"], "deferred": value["requests_deferred"]}


def run_request(transport, index, ids, companion_id):
    value, returncode = invoke(transport, VM1205, render_request(index, ids, companion_id), REQUEST_TIMEOUT_SECONDS)
    return validate_request(value, index), returncode


def validate_evidence(value, returncode):
    if returncode or not isinstance(value, dict) or set(value) != {"status", "companion_stopped", "rows", "correlation", "no_log"}:
        raise Stop("evidence_validation")
    if value["status"] != "HARDWARE_EVIDENCE_PASS" or value["companion_stopped"] is not True or value["no_log"] is not True:
        raise Stop("evidence_validation")
    if not isinstance(value["rows"], list) or len(value["rows"]) != 3: raise Stop("evidence_validation")
    for index, row in enumerate(value["rows"], 1):
        if not isinstance(row, dict) or set(row) != {"index", "q6_submissions", "q4_submissions", "q4_selected_ms", "turn_completed"} or row["index"] != index or row["turn_completed"] is not True:
            raise Stop("evidence_validation")
        expected = (1, 0, None) if index < 3 else (0, 1, row["q4_selected_ms"])
        if (row["q6_submissions"], row["q4_submissions"], row["q4_selected_ms"]) != expected: raise Stop("evidence_validation")
        if index == 3 and (type(row["q4_selected_ms"]) is not int or not 0 <= row["q4_selected_ms"] <= DISPATCH_LIMIT_MS): raise Stop("evidence_validation")
    expected_correlation = {"complete": True, "tuple_count": 3, "q6_full_event": True,
                            "processing_two_event": True, "deferred_zero_event": True,
                            "q4_after_full": True, "payload_fields_retained": False}
    if value["correlation"] != expected_correlation: raise Stop("evidence_validation")
    return value


def parse_receipt(path):
    text = pathlib.Path(path).read_text(encoding="utf-8")
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        matches = re.findall(r"```json\s*(\{[^\r\n]+\})\s*```", text)
        if len(matches) != 1: raise Stop("local_validation")
        value = json.loads(matches[0])
    if not isinstance(value, dict): raise Stop("local_validation")
    return value


def validate_spent_candidate_receipt(value):
    fields = {"schema", "status", "stage", "candidate_stopped", "remote"}
    if set(value) != fields or value != {"schema": "auto-switch-candidate-start-r4-result/v1",
                                        "status": "UNKNOWN", "stage": "remote_validation",
                                        "candidate_stopped": None, "remote": None}:
        raise Stop("local_validation")
    return value


def validate_reconciliation_receipt(value):
    if (not isinstance(value, dict) or set(value) != {"schema", "status", "stage", "remote"}
            or value["schema"] != "auto-switch-candidate-reconcile-r1-result/v1"
            or value["status"] != "PASS" or value["stage"] != "complete"):
        raise Stop("local_validation")
    remote = value["remote"]
    fields = {"status", "candidate_present", "volume_present", "candidate_id", "candidate_image",
              "candidate_volume", "source_revision", "candidate_running", "state_status",
              "docker_health_status", "can_enter_hardware_preflight_without_restart",
              "identity_verified", "image_verified", "volume_verified", "network_none",
              "published_ports_zero", "user_node", "mount_exact", "readonly_root", "cap_drop_all",
              "no_new_privileges", "restart_no", "tmpfs_hardened", "environment_checked",
              "live_unchanged", "retained_candidates_unchanged", "historical_startup_reconstructed",
              "database_checked", "native_health_checked"}
    if not isinstance(remote, dict) or set(remote) != fields or remote["status"] != "CANDIDATE_RECONCILE_R1_PASS":
        raise Stop("local_validation")
    if (remote["candidate_id"] != CANDIDATE_ID or remote["candidate_image"] != IMAGE
            or remote["candidate_volume"] != CANDIDATE_VOLUME or remote["source_revision"] != SOURCE
            or remote["state_status"] != "running" or remote["docker_health_status"] != "healthy"):
        raise Stop("local_validation")
    proven = ("candidate_present", "volume_present", "candidate_running",
              "can_enter_hardware_preflight_without_restart", "identity_verified", "image_verified",
              "volume_verified", "network_none", "published_ports_zero", "user_node", "mount_exact",
              "readonly_root", "cap_drop_all", "no_new_privileges", "restart_no", "tmpfs_hardened",
              "live_unchanged", "retained_candidates_unchanged")
    if any(remote[key] is not True for key in proven):
        raise Stop("local_validation")
    if any(remote[key] is not False for key in ("environment_checked", "historical_startup_reconstructed",
                                                 "database_checked", "native_health_checked")):
        raise Stop("local_validation")
    return value


def validate_key_receipt(value):
    required = {"status", "candidate_id", "candidate_running", "key_id", "key_store",
                "created", "patched", "readback", "stored", "no_log", "auto_resolve",
                "allowed_models", "allowed_connections", "scopes", "endpoints"}
    if set(value) != required or value["status"] != "CANDIDATE_KEY_R4_PASS" or value["candidate_id"] != CANDIDATE_ID or value["candidate_running"] is not True:
        raise Stop("local_validation")
    if value["key_id"] != KEY_ID or value["key_store"] != CANDIDATE_KEY_STORE:
        raise Stop("local_validation")
    if any(value[key] is not True for key in ("created", "patched", "readback", "stored", "no_log")) or value["auto_resolve"] is not False:
        raise Stop("local_validation")
    if (value["allowed_models"], value["allowed_connections"], value["scopes"], value["endpoints"]) != (14, 5, 1, 2):
        raise Stop("local_validation")
    return value


def reserve_result():
    if RESULT.exists() or RESULT.is_symlink(): raise Stop("stale_result")
    return os.open(RESULT, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0), 0o600)


def finish_result(fd, value):
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
    if len(raw) > RESULT_LIMIT: raise Stop("result_validation")
    offset = 0
    try:
        while offset < len(raw):
            written = os.write(fd, raw[offset:])
            if written <= 0: raise OSError("result_write")
            offset += written
        os.fsync(fd)
    finally:
        os.close(fd)


def stop_known_companion(transport, companion_id):
    value, returncode = invoke(transport, VM1205, render_stop(companion_id), 60)
    return (returncode == 0 and value == {"status": "HARDWARE_STOP_PASS", "companion_id": companion_id,
                                         "companion_stopped": True, "category": None})


def review_payload():
    return {"schema": "auto-switch-hardware-qualification-r1/v1", "execution_ready": EXECUTION_READY,
            "source": SOURCE, "image": IMAGE, "tag": TAG, "candidate_name": CANDIDATE_NAME,
            "candidate_id": CANDIDATE_ID, "candidate_volume": CANDIDATE_VOLUME,
            "spent_candidate_start_result_sha256": CANDIDATE_START_RESULT_SHA256,
            "candidate_reconciliation_result_sha256": RECONCILIATION_RESULT_SHA256,
            "candidate_key_id": KEY_ID, "candidate_key_result_sha256": CANDIDATE_KEY_RESULT_SHA256,
            "candidate_key_store": CANDIDATE_KEY_STORE, "companion_name": COMPANION_NAME,
            "q6_connection": Q6_CONNECTION, "q4_connection": Q4_CONNECTION,
            "allowed_connections": ALL_CONNECTIONS, "allowed_models": ALLOWED_MODELS,
            "plan_sha256": digest(PLAN), "bindings_sha256": digest(BINDINGS),
            "r6_sha256": digest(R6), "metrics_sha256": digest(METRICS),
            "transport_sha256": digest(TRANSPORT), "candidate_launcher_sha256": digest(CANDIDATE_LAUNCHER),
            "launcher_sha256": digest(__file__), "contract_sha256": digest(CONTRACT),
            "required_sequence": ["idle_0_0", "two_q6", "processing_2_deferred_0", "third_q4_within_5s",
                                  "three_valid_completions", "idle_0_0", "stop_retain"]}


def offline_check():
    fixed = ((PLAN, PLAN_SHA256), (BINDINGS, BINDINGS_SHA256), (R6, R6_SHA256),
             (METRICS, METRICS_SHA256), (TRANSPORT, TRANSPORT_SHA256),
             (CANDIDATE_LAUNCHER, CANDIDATE_LAUNCHER_SHA256))
    if not all(regular(path) and digest(path) == expected for path, expected in fixed):
        raise Stop("local_validation")
    if EXECUTION_READY or require_bound() != ["candidate_id", "candidate_reconciliation_result_sha256",
                                              "candidate_key_id", "candidate_key_result_sha256",
                                              "candidate_key_store"]:
        raise Stop("local_validation")
    if RESULT.exists() or RESULT.is_symlink(): raise Stop("stale_result")
    if len(ALLOWED_MODELS) != 14 or ALL_CONNECTIONS != [Q6_CONNECTION, Q4_CONNECTION, OPENROUTER_FREE, CODEX_CONNECTION, OPENROUTER_PAID]:
        raise Stop("local_validation")
    fixture = fixture_result(); validate_result(fixture, 0, FIXTURE_CANDIDATE_ID)
    rendered = render_request(1, new_ids(), "e" * 64).decode("utf-8")
    if "subprocess.run" in rendered or "bounded_capture" not in rendered or "REQUEST_PASS" not in rendered:
        raise Stop("local_validation")
    prep_payload = render_prep()
    if emitted_fields(prep_payload.decode("utf-8"), "HARDWARE_PREP_PASS") != PREP_FIELDS or emitted_fields(prep_payload.decode("utf-8"), "HARDWARE_PREP_STOP") != PREP_STOP_FIELDS:
        raise Stop("local_validation")
    for payload in (prep_payload, render_evidence([new_ids(), new_ids(), new_ids()], "e" * 64, 0), render_stop("e" * 64)):
        ast.parse(payload.decode("utf-8"))
        if b"subprocess.run" in payload or b"bounded_capture" not in payload: raise Stop("local_validation")
    metrics = load_module(METRICS, METRICS_SHA256, "hardware_metrics_render")
    remote = metrics.render_remote(); ast.parse(remote)
    print("HARDWARE_QUALIFICATION_R1_PREPARATION_PASS")


def execute(reviewed):
    missing = require_bound()
    if not EXECUTION_READY or missing:
        raise Stop("pending_bindings:" + ",".join(missing))
    fixed = ((PLAN, PLAN_SHA256), (BINDINGS, BINDINGS_SHA256), (R6, R6_SHA256),
             (METRICS, METRICS_SHA256), (TRANSPORT, TRANSPORT_SHA256),
             (CANDIDATE_LAUNCHER, CANDIDATE_LAUNCHER_SHA256),
             (CANDIDATE_START_RESULT, CANDIDATE_START_RESULT_SHA256),
             (RECONCILIATION_RESULT, RECONCILIATION_RESULT_SHA256),
             (CANDIDATE_KEY_RESULT, CANDIDATE_KEY_RESULT_SHA256), (CONTRACT, digest(CONTRACT)))
    if not all(regular(path) and digest(path) == expected for path, expected in fixed):
        raise Stop("local_validation")
    if not regular(reviewed) or json.loads(reviewed.read_text(encoding="utf-8")) != review_payload():
        raise Stop("review_pin_mismatch")
    validate_spent_candidate_receipt(parse_receipt(CANDIDATE_START_RESULT))
    validate_reconciliation_receipt(parse_receipt(RECONCILIATION_RESULT))
    validate_key_receipt(parse_receipt(CANDIDATE_KEY_RESULT))
    if "PROGRAMDATA" not in {key.upper() for key in os.environ}: raise Stop("local_validation")
    transport = load_module(TRANSPORT, TRANSPORT_SHA256, "hardware_transport_execute")
    metrics_module = load_module(METRICS, METRICS_SHA256, "hardware_metrics_execute")
    fd = reserve_result()
    companion_id = None; known_state = False; candidate_stopped = None; terminal_remote = None; stage = "prep"
    result = {"status": "HARDWARE_QUALIFICATION_R1_UNKNOWN", "stage": stage,
              "candidate_id": CANDIDATE_ID, "candidate_stopped": None,
              "companion_id": None, "companion_stopped": None}
    try:
        prep_value, prep_rc = invoke(transport, VM1205, render_prep(), 360)
        if prep_rc:
            stopped_prep = validate_prep_stop(prep_value, prep_rc)
            candidate_stopped = stopped_prep["candidate_stopped"]
            companion_id = stopped_prep["companion_id"]
            terminal_remote = {"status": "HARDWARE_QUALIFICATION_R1_STOP", "stage": stopped_prep["stage"],
                               "candidate_id": CANDIDATE_ID, "candidate_stopped": candidate_stopped,
                               "companion_id": companion_id, "companion_stopped": stopped_prep["companion_stopped"]}
            raise Stop("prep_stop")
        prep = validate_prep(prep_value, prep_rc); companion_id = prep["companion_id"]; known_state = True; candidate_stopped = True
        result.update(candidate_stopped=True, companion_id=companion_id, companion_stopped=False)
        stage = "baseline_metrics"; baseline = metric_sample(transport, metrics_module)
        if baseline != {"processing": 0, "deferred": 0}: raise Stop("baseline_not_idle")
        ids = [new_ids(), new_ids(), new_ids()]
        stage = "q6_parallel"
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            pending = [pool.submit(run_request, transport, index, ids[index - 1], companion_id) for index in (1, 2)]
            deadline = time.monotonic() + SATURATION_DEADLINE_SECONDS; occupied = None
            while time.monotonic() < deadline:
                if any(item.done() for item in pending): raise Stop("q6_not_occupied")
                sample = metric_sample(transport, metrics_module)
                if time.monotonic() >= deadline: raise Stop("q6_not_occupied")
                if sample == {"processing": 2, "deferred": 0}:
                    occupied = sample; break
                if sample["deferred"] != 0: raise Stop("metrics_invalid")
                time.sleep(0.25)
            if occupied is None: raise Stop("q6_not_occupied")
            stage = "q4_third"; third, _ = run_request(transport, 3, ids[2], companion_id)
            first = [future.result(timeout=REQUEST_TIMEOUT_SECONDS) for future in pending]
        responses = [first[0][0], first[1][0], third]
        stage = "final_metrics"; final = None; deadline = time.monotonic() + 60
        while time.monotonic() < deadline:
            sample = metric_sample(transport, metrics_module)
            if sample == {"processing": 0, "deferred": 0}: final = sample; break
            time.sleep(0.25)
        if final is None: raise Stop("metrics_not_idle")
        stage = "evidence"; known_state = False
        evidence_value, evidence_rc = invoke(transport, VM1205, render_evidence(ids, companion_id, prep["detail_baseline"]), 180)
        evidence = validate_evidence(evidence_value, evidence_rc)
        request_rows = []
        for index, (ident, response, dbrow) in enumerate(zip(ids, responses, evidence["rows"]), 1):
            request_rows.append({"index": index, **ident,
                                 "selected_connection_id": response["selected_connection_id"],
                                 "resolved_provider": response["resolved_provider"],
                                 "resolved_model": response["resolved_model"],
                                 "candidate_attempt": response["candidate_attempt"],
                                 "reviewer_verdict": response["reviewer_verdict"],
                                 "fallback_reason": response["fallback_reason"],
                                 "content_valid": response["content_valid"],
                                 "q6_submissions": dbrow["q6_submissions"], "q4_submissions": dbrow["q4_submissions"],
                                 "q4_http_status": response["http_status"] if index == 3 else None,
                                 "q4_selected_ms": dbrow["q4_selected_ms"], "turn_completed": dbrow["turn_completed"]})
        result = {"status": "HARDWARE_QUALIFICATION_R1_PASS", "source": SOURCE, "image": IMAGE,
                  "candidate_id": CANDIDATE_ID, "candidate_stopped": True, "companion_id": companion_id,
                  "companion_stopped": True, "network_private": prep["network_private"],
                  "published_ports": prep["published_ports"], "metrics_baseline": baseline,
                  "metrics_before_third": occupied, "final_metrics": final, "requests": request_rows,
                  "correlation": evidence["correlation"], "no_log": evidence["no_log"],
                  "cloud_false": prep["cloud_false"], "codex_inactive": prep["codex_inactive"],
                  "migration_170": prep["migration_170"], "migration_171": prep["migration_171"],
                  "health_counters": prep["health_counters"],
                  "key_id": KEY_ID}
        validate_result(result, 0); returncode = 0
    except Exception as error:
        unknown = str(error) == "transport_unknown"; stopped = None
        if terminal_remote is not None:
            result = terminal_remote
        elif known_state and not unknown:
            try: stopped = stop_known_companion(transport, companion_id)
            except Exception: stopped = None
        if terminal_remote is None:
            result = {"status": "HARDWARE_QUALIFICATION_R1_UNKNOWN" if unknown else "HARDWARE_QUALIFICATION_R1_STOP",
                      "stage": stage, "candidate_id": CANDIDATE_ID,
                      "candidate_stopped": candidate_stopped,
                      "companion_id": companion_id, "companion_stopped": stopped}
        returncode = 1
    finally:
        finish_result(fd, result)
    print(json.dumps(result, sort_keys=True)); return returncode


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--render-review-payload", action="store_true")
    parser.add_argument("--execute-reviewed", type=pathlib.Path)
    args = parser.parse_args()
    if sum((args.self_check, args.render_review_payload, bool(args.execute_reviewed))) != 1:
        raise Stop("local_validation")
    if args.self_check: offline_check(); return 0
    if args.render_review_payload: print(json.dumps(review_payload(), indent=2, sort_keys=True)); return 0
    return execute(args.execute_reviewed)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        stage = str(error).split(":", 1)[0]
        if stage not in {"pending_bindings", "independent_review_required", "local_validation", "stale_result"}:
            stage = "local_validation"
        print(json.dumps({"status": "HARDWARE_QUALIFICATION_R1_NOT_EXECUTABLE", "stage": stage,
                          "execution_ready": False}, sort_keys=True))
        raise SystemExit(1)
