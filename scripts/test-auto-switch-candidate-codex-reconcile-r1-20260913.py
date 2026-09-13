"""Focused whole-rendered-path checks for candidate/Codex reconciliation."""
import copy
import io
import json
import pathlib
import runpy
import subprocess
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "scripts/auto-switch-candidate-codex-reconcile-r1-20260913.py"
module = runpy.run_path(str(LAUNCHER), run_name="candidate_codex_reconcile_r1_test")
reconcile = module["load"](module["RECONCILE"], module["RECONCILE_SHA256"], "codex_reconcile_test_state")


def metadata():
    mount = lambda name: [{"Type": "volume", "Name": name, "Destination": "/app/data", "RW": True}]
    candidate = {"id": module["CANDIDATE_ID"], "name": "/" + module["CANDIDATE"], "image": module["IMAGE"],
                 "config_image": module["TAG"], "source_revision": module["SOURCE"], "user": "node",
                 "running": True, "state_status": "running", "health_status": "healthy", "network_mode": "none",
                 "readonly_root": True, "restart_name": "no", "cap_drop": ["ALL"],
                 "security_opt": ["no-new-privileges"], "port_bindings": {}, "ports": {},
                 "tmpfs": {"/tmp": "rw,noexec,nosuid,nodev,size=67108864,mode=1777"},
                 "mounts": mount(module["VOLUME"])}
    live = {"id": reconcile.LIVE_ID, "name": "/omniroute", "image": reconcile.LIVE_IID,
            "running": True, "mounts": mount(reconcile.LIVE_VOLUME)}
    retained = [{"id": row[0], "name": "/" + row[1], "image": reconcile.OLD_IID,
                 "running": False, "mounts": mount(row[2])} for row in reconcile.RETAINED]
    image = {"id": module["IMAGE"], "repo_tags": [module["TAG"]], "os": "linux", "architecture": "amd64",
             "user": "node", "source_revision": module["SOURCE"]}
    volume = {"name": module["VOLUME"], "driver": "local", "scope": "local"}
    return candidate, live, retained, image, volume


def fake_capture(native, native_rc=0, candidate_override=None):
    candidate, live, retained, image, volume = metadata()
    if candidate_override: candidate.update(candidate_override)
    mapping = {module["CANDIDATE"]: candidate, module["CANDIDATE_ID"]: candidate,
               reconcile.LIVE_ID: live, module["TAG"]: image, module["VOLUME"]: volume}
    mapping.update({row[0]: value for row, value in zip(reconcile.RETAINED, retained)})
    return f'''def bounded_capture(args,input_bytes=None,timeout=30,stdout_limit=1048576,stderr_limit=65536):
 if args[:3]==['docker','container','ls']:return 0,({module["CANDIDATE_ID"] + " " + module["CANDIDATE"] + chr(10)!r}).encode(),b''
 if args[:3]==['docker','volume','ls']:return 0,({module["VOLUME"] + chr(10)!r}).encode(),b''
 if len(args)>2 and args[1:3]==['container','exec']:return {native_rc},{json.dumps(native, separators=(",", ":"))!r}.encode(),b''
 if len(args)>5 and args[2]=='inspect' and args[3]=='--format':return 0,json.dumps({mapping!r}[args[-1]],separators=(',',':')).encode(),b''
 raise RuntimeError('unexpected_fixture_command')'''


def run_rendered(native, native_rc=0, candidate_override=None):
    payload = module["render_remote"]("oma_fixture_codex_reconcile_secret", fake_capture(native, native_rc, candidate_override))
    command = [sys.executable, "-I", "-B", "-c", "import sys;exec(compile(sys.stdin.buffer.read(),'<fixture>','exec'))"]
    completed = subprocess.run(command, input=payload, capture_output=True, timeout=10, check=False)
    assert completed.stderr == b""
    return completed.returncode, json.loads(completed.stdout)


native_pass = {"status": "CODEX_GET_PASS", "stage": "complete", "connection_id": module["CODEX"],
               "provider": "codex", "is_active": True, "get_http_status": 200, "failure_category": None}
rc, value = run_rendered(native_pass)
assert rc == 0 and module["validate_remote"](value, rc) == value and value["is_active"] is True

native_http = {"status": "CODEX_GET_STOP", "stage": "get", "connection_id": None, "provider": None,
               "is_active": None, "get_http_status": 401, "failure_category": "http_4xx"}
rc, value = run_rendered(native_http, 1)
assert rc == 1 and module["validate_remote"](value, rc) == value and value["get_http_status"] == 401

wrong = copy.deepcopy(native_pass); wrong["connection_id"] = "wrong-target"
rc, value = run_rendered(wrong)
assert rc == 2 and module["validate_remote"](value, rc) == value and value["stage"] == "native_dispatch"

rc, value = run_rendered(native_pass, candidate_override={"network_mode": "bridge"})
assert rc == 1 and module["validate_remote"](value, rc) == value and value["stage"] == "candidate_isolation"

module["offline_check"]()
print("PASS: whole rendered candidate identity, one-GET, sanitized STOP and contradiction paths")
