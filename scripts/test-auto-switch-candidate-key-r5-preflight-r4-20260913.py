"""Focused offline checks for the fresh ordered-preflight receipt owner."""
import copy
import importlib.util
import json
import pathlib
import subprocess


ROOT = pathlib.Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "scripts/auto-switch-candidate-key-r5-preflight-r4-20260913.py"
spec = importlib.util.spec_from_file_location("candidate_key_preflight_r4", LAUNCHER)
module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
r3 = module.load(module.R3, module.R3_SHA256, "candidate_key_preflight_r4_test_r3")
r5 = r3.load(r3.R5, r3.R5_SHA256, "candidate_key_preflight_r4_test_r5")
reconcile = module.load(module.RECONCILE, module.RECONCILE_SHA256, "candidate_key_preflight_r4_test_reconcile")
module.validate_current_reconcile(json.loads(module.RECONCILE_RESULT.read_text("utf-8")), reconcile)


def run_node(rows):
    source = r3.render_node("oma_fixture_preflight_r4_secret", r5)
    stub = """const __responses=__ROWS__;const http={request:(opts,cb)=>{const handlers={};const q={setTimeout(){},on(name,fn){handlers[name]=fn},end(){queueMicrotask(()=>{const item=__responses.shift();if(item.error){const e=new Error(item.error);handlers.error(e);return}const rh={};const res={statusCode:item.status,on(name,fn){rh[name]=fn}};cb(res);if(item.body!==null)rh.data(Buffer.from(item.body));rh.end()})}};return q}};""".replace("__ROWS__", json.dumps(rows, separators=(",", ":")))
    source = source.replace("const http=require('node:http');", stub)
    child = subprocess.run(["node", "-"], input=source.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10)
    assert not child.stderr
    return child.returncode, child.stdout


success = [
    {"status": 200, "body": json.dumps({"keys": [], "total": 0, "allowKeyReveal": False})},
    {"status": 200, "body": json.dumps({"combos": [], "total": 0})},
    {"status": 200, "body": json.dumps({"connection": {"id": r5.CODEX_CONNECTION, "provider": "codex", "isActive": False}})},
]
rc, output = run_node(success)
native = r3.validate_native(json.loads(output), rc)
checks = {name: (native["checks"][name] if name in r3.NATIVE_CHECKS else True) for name in sorted(r5.PREFLIGHT_CHECKS)}
remote = {"status": "CANDIDATE_KEY_R5_PREFLIGHT_R3_PASS", "stage": "complete",
          "candidate_id": module.CANDIDATE_ID, "checks": checks, "native": native}
receipt = module.child_receipt(0, json.dumps(remote, separators=(",", ":")).encode(), b"", r3, r5)
assert module.validate_receipt(receipt, r3, r5)["status"] == "PASS"

active = copy.deepcopy(success); active[2]["body"] = json.dumps({"connection": {"id": r5.CODEX_CONNECTION, "provider": "codex", "isActive": True}})
rc, output = run_node(active)
native = r3.validate_native(json.loads(output), rc)
checks = {name: (native["checks"][name] if name in r3.NATIVE_CHECKS else True) for name in sorted(r5.PREFLIGHT_CHECKS)}
remote = {"status": "CANDIDATE_KEY_R5_PREFLIGHT_R3_STOP", "stage": "codex_inactive",
          "candidate_id": module.CANDIDATE_ID, "checks": checks, "native": native}
receipt = module.child_receipt(1, json.dumps(remote, separators=(",", ":")).encode(), b"", r3, r5)
assert module.validate_receipt(receipt, r3, r5)["status"] == "STOP"
assert receipt["remote"]["native"]["evidence"]["completed_steps"] == ["keys", "combos"]

contradiction = copy.deepcopy(receipt); contradiction["transport"]["returncode"] = 0
try:
    module.validate_receipt(contradiction, r3, r5)
except module.Stop:
    pass
else:
    raise AssertionError("contradictory return code accepted")

unknown = module.child_receipt(0, b"not-json", b"", r3, r5)
assert unknown["status"] == "UNKNOWN" and unknown["remote"] is None and unknown["transport"]["category"] == "remote_envelope"
module.validate_receipt(unknown, r3, r5)
unknown = module.child_receipt(0, b"{}", b"warning", r3, r5)
assert unknown["status"] == "UNKNOWN" and unknown["remote"] is None and unknown["transport"]["category"] == "child_stderr"
module.validate_receipt(unknown, r3, r5)
bounded = {"schema": module.SCHEMA, "status": "UNKNOWN", "stage": "transport",
           "transport": module.transport_meta(), "remote": None}
module.validate_receipt(bounded, r3, r5)
broken = copy.deepcopy(bounded); broken["transport"]["stdout"] = {"bytes": 1, "sha256": "0" * 64}
try:
    module.validate_receipt(broken, r3, r5)
except module.Stop:
    pass
else:
    raise AssertionError("contradictory bounded-capture evidence accepted")

module.self_check()
print("CANDIDATE_KEY_R5_PREFLIGHT_R4_TEST_PASS")
