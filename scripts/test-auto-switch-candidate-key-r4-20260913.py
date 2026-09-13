"""Focused offline boundaries for the unbound R4 native qualification-key source."""
import copy
import ast
import importlib.util
import inspect
import json
import os
import pathlib
import sqlite3
import subprocess
import tempfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "scripts/auto-switch-candidate-key-r4-20260913.py"

assert LAUNCHER.is_file(), "R4 qualification-key launcher missing"
spec = importlib.util.spec_from_file_location("candidate_key_r4", LAUNCHER)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.EXECUTION_READY is True
assert module.SOURCE == "e53d895e9a5e38a7f06ce59de254835f10e829c1"
assert module.IMAGE == "sha256:8211e1071a3b68eac01673d76129150eb0c0fea329dd222bc8bf0394b13fc844"
assert module.CANDIDATE_NAME == "omniroute-auto-switch-candidate-r4-20260913"
assert module.CANDIDATE_VOLUME == "omniroute-auto-switch-candidate-data-r4-20260913"
assert module.CANDIDATE_ID == "9468859edcdb483c53900edde14d301a162cccc791079154677e913f39bf26a3"
assert module.RECONCILIATION_RESULT_SHA256 == "7efe1cb83cc1c5c6cf85199b919338bb2a6143054d9a6cd315e0c3270fc213cf"
assert module.require_bound() == []

runtime = ROOT.parent / "omniroute-auto-switch-matrix-20260913"
native = subprocess.run(["node", "--import", "tsx", "-e", module.native_roundtrip_probe()],
                        cwd=runtime, capture_output=True, timeout=90)
assert native.returncode == 0 and len(native.stdout) <= module.RESULT_LIMIT and len(native.stderr) <= module.RESULT_LIMIT, (len(native.stdout), len(native.stderr))
native_result = json.loads(native.stdout.decode("utf-8").strip().splitlines()[-1])
assert native_result == {"create_status": 201, "patch_status": 200, "get_status": 200,
                         "missing_fields": [], "extra_fields": [], "mismatch_fields": [],
                         "db_ip_allowlist_is_null": True}

rendered = module.render_remote("oma_fixture_secret", module.CANDIDATE_ID)
compiled = ast.parse(rendered)
imports = {alias.name for node in compiled.body if isinstance(node, ast.Import) for alias in node.names}
assert {"subprocess", "threading", "time"}.issubset(imports)
assert b"oma_fixture_secret" not in rendered
assert rendered.count(b"if not key_id or rollback_attempted:return") == 1


def run_rendered_remote(mode):
    with tempfile.TemporaryDirectory() as temporary:
        root = pathlib.Path(temporary)
        volume = root / "volume"
        store_parent = root / "qualification"
        volume.mkdir()
        store_parent.mkdir()
        os.chmod(volume, 0o700)
        os.chmod(store_parent, 0o700)
        (volume / "server.env").write_text(
            "STORAGE_ENCRYPTION_KEY='storage-secret'\nJWT_SECRET='jwt-secret'\nAPI_KEY_SECRET='api-secret'\n",
            encoding="utf-8",
        )
        os.chmod(volume / "server.env", 0o600)
        database = volume / "storage.sqlite"
        db = sqlite3.connect(database)
        db.executescript("""
          CREATE TABLE key_value(namespace TEXT,key TEXT,value TEXT);
          INSERT INTO key_value VALUES('settings','cloudEnabled','false');
          CREATE TABLE _omniroute_migrations(version TEXT,name TEXT);
          INSERT INTO _omniroute_migrations VALUES('170','170_agent_route_runs');
          INSERT INTO _omniroute_migrations VALUES('171','171_agent_route_deferred_metrics');
          CREATE TABLE agent_route_runs(run_id TEXT,api_key_id TEXT,task_id TEXT,effective_review_class TEXT,created_at TEXT,updated_at TEXT);
          CREATE TABLE agent_route_turns(run_id TEXT,turn_id TEXT,idempotency_key TEXT,virtual_route TEXT,state TEXT,output_started INTEGER,tool_started INTEGER,dispatch_claimed INTEGER,created_at TEXT,updated_at TEXT);
          CREATE TABLE agent_route_events(event_id TEXT,run_id TEXT,turn_id TEXT,idempotency_key TEXT,kind TEXT,provider TEXT,model TEXT,connection_id TEXT,candidate_attempt INTEGER,repair_attempt INTEGER,reviewer_attempt INTEGER,admission_state TEXT,fallback_reason TEXT,latency_ms INTEGER,busy_slots INTEGER,processing_requests INTEGER,prompt_tokens INTEGER,completion_tokens INTEGER,objective_outcome TEXT,reviewer_class TEXT,reviewer_model TEXT,reviewer_verdict TEXT,subscription_percent REAL,subscription_evidence_id TEXT,subscription_evidence_at TEXT,subscription_decision TEXT,occurred_at TEXT,deferred_requests INTEGER);
          CREATE TABLE provider_connections(api_key TEXT,access_token TEXT,refresh_token TEXT,id_token TEXT);
          CREATE TABLE api_keys(id TEXT,ip_allowlist TEXT);
        """)
        cells = ["enc:v1:fixture"] * 18 + [""] * 34
        db.executemany("INSERT INTO provider_connections VALUES(?,?,?,?)",
                       [cells[index:index + 4] for index in range(0, 52, 4)])
        db.commit()
        db.close()

        key_id = "11111111-1111-4111-8111-111111111111"
        candidate = {
            "id": module.CANDIDATE_ID, "name": "/" + module.CANDIDATE_NAME,
            "image": module.IMAGE, "config_image": module.TAG, "source": module.SOURCE,
            "user": "node", "running": True, "status": "running", "health": "healthy",
            "network": "none", "readonly": True, "restart": "no", "caps": ["ALL"],
            "security": ["no-new-privileges"], "ports": {}, "network_ports": {},
            "tmpfs": {"/tmp": "rw,noexec,nosuid,nodev,size=67108864,mode=1777"},
            "mounts": [{"Type": "volume", "Name": module.CANDIDATE_VOLUME,
                        "Destination": "/app/data", "RW": True}],
        }
        live = {"id": module.LIVE_ID, "image": module.LIVE_IMAGE, "running": True,
                "mounts": [{"Type": "volume", "Name": module.LIVE_VOLUME,
                            "Destination": "/app/data"}]}
        capture = f'''def bounded_capture(args,payload=None,timeout=1800):
 mode={mode!r};database={str(database)!r};candidate={candidate!r};live={live!r}
 if args[:3]==['docker','container','inspect']:
  value=candidate if args[-1] in ({module.CANDIDATE_ID!r},{module.CANDIDATE_NAME!r}) else live
 elif args[:3]==['docker','image','inspect']:
  value={{'id':{module.IMAGE!r},'tags':[{module.TAG!r}]}}
 elif args[:3]==['docker','volume','inspect']:
  value={{'name':{module.CANDIDATE_VOLUME!r},'driver':'local','scope':'local','root':{str(volume)!r}}}
 elif args[:3]==['docker','container','exec']:
  db=sqlite3.connect(database);db.execute('INSERT INTO api_keys VALUES(?,NULL)',({key_id!r},));db.commit();db.close()
  if mode=='timeout':raise RuntimeError('COMMAND_TIMEOUT')
  if mode=='overflow':raise RuntimeError('OUTPUT_LIMIT')
  if mode=='malformed':return 0,b'{{',b''
  value={{'status':'KEY_NATIVE_R4_PASS','key_id':{key_id!r},'secret':'sk-1111111111111111-111111-11111111','codex_inactive_readback':True}}
 else:raise RuntimeError('FIXTURE_UNEXPECTED')
 return 0,json.dumps(value,separators=(',',':')).encode(),b''
'''
        source = module.render_remote("oma_fixture_secret", module.CANDIDATE_ID).decode("utf-8")
        original_capture = inspect.getsource(module.load_transport().bounded_capture)
        source = source.replace(original_capture, capture)
        store = store_parent / pathlib.Path(module.OPERATOR_STORE).name
        source = source.replace(repr(module.OPERATOR_STORE), repr(str(store)))
        source = source.replace("parent!=pathlib.Path('/root/.omniroute-qualification')",
                                "parent!=pathlib.Path(" + repr(str(store_parent)) + ")")
        source = source.replace("read_regular(root/'server.env',65536,1000,1000,0o600)",
                                "read_regular(root/'server.env',65536,0,0,0o600)")
        fake_os = r'''
import os as _real_os
class _FixtureOS:
 path=_real_os.path;O_RDONLY=_real_os.O_RDONLY;O_WRONLY=_real_os.O_WRONLY;O_CREAT=_real_os.O_CREAT;O_EXCL=_real_os.O_EXCL;O_NOFOLLOW=0;O_DIRECTORY=0
 def __init__(self):self.paths={}
 def _path(self,path,dir_fd=None):
  path=str(path)
  return str(pathlib.Path(self.paths[dir_fd])/path) if dir_fd is not None else path
 def open(self,path,flags,mode=0o777,dir_fd=None):
  resolved=self._path(path,dir_fd);flags|=getattr(_real_os,'O_BINARY',0)
  target=str(pathlib.Path(resolved)/'.fixture-dirfd') if pathlib.Path(resolved).is_dir() else resolved
  if target!=resolved:flags=_real_os.O_RDWR|_real_os.O_CREAT|getattr(_real_os,'O_BINARY',0)
  fd=_real_os.open(target,flags,mode);self.paths[fd]=resolved;return fd
 def close(self,fd):self.paths.pop(fd,None);return _real_os.close(fd)
 def _fixed(self,value):
  mode=(value.st_mode&~0o777)|(0o700 if stat.S_ISDIR(value.st_mode) else 0o600)
  return _real_os.stat_result((mode,*tuple(value)[1:]))
 def stat(self,path,dir_fd=None,follow_symlinks=True):return self._fixed(_real_os.stat(self._path(path,dir_fd),follow_symlinks=follow_symlinks))
 def lstat(self,path):return self._fixed(_real_os.lstat(path))
 def fstat(self,fd):
  mapped=self.paths.get(fd)
  return self._fixed(_real_os.stat(mapped) if mapped and pathlib.Path(mapped).is_dir() else _real_os.fstat(fd))
 def unlink(self,path,dir_fd=None):return _real_os.unlink(self._path(path,dir_fd))
 def fchown(self,fd,uid,gid):return None
 def fchmod(self,fd,mode):return None
 def __getattr__(self,name):return getattr(_real_os,name)
os=_FixtureOS()
'''
        source = source.replace("import json,os,pathlib,re,sqlite3,stat,subprocess,threading,time,urllib.parse",
                                "import json,pathlib,re,sqlite3,stat,subprocess,threading,time,urllib.parse" + fake_os)
        returncode, stdout, stderr = module.load_transport().bounded_capture(
            ["python", "-B", "-c", source], timeout=30)
        assert len(stdout) <= module.RESULT_LIMIT and len(stderr) <= module.RESULT_LIMIT
        db = sqlite3.connect(database)
        committed = db.execute("SELECT count(*) FROM api_keys").fetchone()[0]
        db.close()
        return returncode, json.loads(stdout), store.exists(), committed


passed_code, passed_remote, store_exists, committed = run_rendered_remote("pass")
assert passed_code == 0 and passed_remote["status"] == "CANDIDATE_KEY_R4_PASS" and store_exists and committed == 1
module.validate_result(passed_remote, passed_code)
for mode, category in (("timeout", "child_timeout"), ("overflow", "child_output"), ("malformed", "remote_envelope")):
    unknown_code, unknown_remote, unknown_store, committed = run_rendered_remote(mode)
    assert unknown_code == 2 and unknown_remote["status"] == "CANDIDATE_KEY_R4_UNKNOWN" and not unknown_store and committed == 1
    assert unknown_remote["failure_category"] == category
    assert all(unknown_remote[name] is None for name in ("candidate_id", "candidate_running", "key_id", "created", "stored", "store_removed", "http_status", "rollback_attempted", "key_inactive_readback"))
    module.validate_result(unknown_remote, unknown_code)

good = module.fixture_result()
assert module.validate_result(good, 0, module.FIXTURE_CANDIDATE_ID) == good

def rejected(mutator):
    value = copy.deepcopy(good)
    mutator(value)
    try:
        module.validate_result(value, 0, module.FIXTURE_CANDIDATE_ID)
    except module.Stop:
        return
    raise AssertionError("invalid R4 key result accepted")

rejected(lambda value: value.update(candidate_id="0" * 64))
rejected(lambda value: value.update(allowed_models=13))
rejected(lambda value: value.update(no_log=False))
rejected(lambda value: value.update(db_ip_allowlist_is_null=False))
rejected(lambda value: value.update(candidate_running=False))
rejected(lambda value: value.update(migration_171=False))

unknown = {"status": "CANDIDATE_KEY_R4_UNKNOWN", "stage": "native_dispatch",
           "candidate_id": None, "candidate_running": None, "key_id": None,
           "created": None, "stored": None, "store_removed": None,
           "failure_category": "child_timeout", "http_status": None,
           "rollback_attempted": None, "key_inactive_readback": None}
assert module.validate_result(unknown, 2, module.FIXTURE_CANDIDATE_ID) == unknown
bad_unknown = copy.deepcopy(unknown)
bad_unknown["created"] = False
try:
    module.validate_result(bad_unknown, 2, module.FIXTURE_CANDIDATE_ID)
except module.Stop:
    pass
else:
    raise AssertionError("false mutation state accepted as UNKNOWN")

receipt = module.parse_receipt(module.RECONCILIATION_RESULT)
assert module.validate_reconciliation(receipt, module.CANDIDATE_ID) == receipt
bad_receipt = copy.deepcopy(receipt)
bad_receipt["remote"]["native_health_checked"] = True
try:
    module.validate_reconciliation(bad_receipt, module.CANDIDATE_ID)
except module.Stop:
    pass
else:
    raise AssertionError("overclaimed reconciliation accepted")

module.offline_check()

with tempfile.TemporaryDirectory() as temporary:
    module.RESULT = pathlib.Path(temporary) / "result.md"
    descriptor = module.reserve_result()
    module.finish_result(descriptor, {"schema": module.RESULT_SCHEMA, "status": "UNKNOWN", "stage": "transport", "remote": None})
    assert json.loads(module.RESULT.read_text("utf-8"))["status"] == "UNKNOWN"
    try:
        module.reserve_result()
    except module.Stop as error:
        assert str(error) == "stale_result"
    else:
        raise AssertionError("existing result reservation accepted")

print("PASS: R4 key identity, reconciliation, native policy, protected store and terminal receipt")
