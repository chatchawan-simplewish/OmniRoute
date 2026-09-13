"""Focused offline checks for the R5 key execution binding."""
import ast
import copy
import importlib.util
import json
import pathlib


ROOT = pathlib.Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "scripts/auto-switch-candidate-key-r5-bound-20260913.py"
spec = importlib.util.spec_from_file_location("candidate_key_r5_bound", LAUNCHER)
module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
r5 = module.load(module.R5, module.R5_SHA256, "candidate_key_r5_bound_test_r5")
preflight = module.load(module.PREFLIGHT, module.PREFLIGHT_SHA256, "candidate_key_r5_bound_test_preflight")
receipt = json.loads(module.PREFLIGHT_RESULT.read_text("utf-8"))
assert module.validate_preflight_receipt(receipt, preflight, r5) == receipt

payload = r5.render_remote("oma_fixture_candidate_key_r5_bound")
node = r5.render_node("oma_fixture_candidate_key_r5_bound")
ast.parse(payload.decode())
assert b"oma_fixture_candidate_key_r5_bound" not in payload
assert node.count("stage='create';r=await request('POST','/api/keys'") == 1
assert node.count("stage='patch';r=await request('PATCH','/api/keys/'+keyId,PATCH)") == 1
assert r5.OPERATOR_STORE.encode() in payload

remote = r5.fixture_result()
remote["candidate_id"] = r5.CANDIDATE_ID
result = module.child_receipt(0, json.dumps(remote, separators=(",", ":")).encode(), b"", r5)
assert module.validate_receipt(result, r5)["status"] == "PASS"
assert result["remote"]["allowed_models"] == 14 and result["remote"]["allowed_connections"] == 5

unknown_remote = {"status": "CANDIDATE_KEY_R5_UNKNOWN", "stage": "native_dispatch",
                  "candidate_id": None, "candidate_running": None, "key_id": None,
                  "created": None, "stored": None, "store_removed": None,
                  "failure_category": "child_timeout", "http_status": None,
                  "rollback_attempted": None, "key_inactive_readback": None}
result = module.child_receipt(2, json.dumps(unknown_remote, separators=(",", ":")).encode(), b"", r5)
assert module.validate_receipt(result, r5)["status"] == "UNKNOWN" and result["remote"] == unknown_remote
result = module.child_receipt(0, b"not-json", b"", r5)
assert module.validate_receipt(result, r5)["status"] == "UNKNOWN" and result["remote"] is None
result = module.child_receipt(0, b"{}", b"warning", r5)
assert module.validate_receipt(result, r5)["status"] == "UNKNOWN" and result["remote"] is None
bounded = {"schema": module.SCHEMA, "status": "UNKNOWN", "stage": "transport",
           "transport": module.transport_meta(), "remote": None}
module.validate_receipt(bounded, r5)
broken = copy.deepcopy(bounded); broken["transport"]["stdout"] = {"bytes": 1, "sha256": "0" * 64}
try:
    module.validate_receipt(broken, r5)
except module.Stop:
    pass
else:
    raise AssertionError("contradictory bounded-capture state accepted")

contradiction = module.child_receipt(0, json.dumps(remote, separators=(",", ":")).encode(), b"", r5)
contradiction["transport"]["returncode"] = 1
try:
    module.validate_receipt(contradiction, r5)
except module.Stop:
    pass
else:
    raise AssertionError("contradictory key result accepted")

module.self_check()
print("CANDIDATE_KEY_R5_BOUND_TEST_PASS")
