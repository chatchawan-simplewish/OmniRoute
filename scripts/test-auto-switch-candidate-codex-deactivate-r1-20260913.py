"""Focused offline checks for the candidate-only Codex deactivation gate."""
import ast
import copy
import pathlib
import runpy


ROOT = pathlib.Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "scripts/auto-switch-candidate-codex-deactivate-r1-20260913.py"
module = runpy.run_path(str(LAUNCHER), run_name="candidate_codex_deactivate_r1_test")

assert module["EXECUTION_READY"] is True
assert module["CANDIDATE_ID"] == "9468859edcdb483c53900edde14d301a162cccc791079154677e913f39bf26a3"
assert module["CODEX_CONNECTION"] == "8f92f200-d280-47b3-b380-2d94be0a4b75"

for before, patched in ((True, True), (False, False)):
    value = module["fixture_result"](before, patched)
    assert module["validate_remote"](value, 0) == value

unknown = module["fixture_unknown"]("patch")
assert module["validate_remote"](unknown, 2) == unknown
for mutator in (
    lambda v: v.update(status="CANDIDATE_CODEX_DEACTIVATE_R1_PASS"),
    lambda v: v.update(connection_id=None),
    lambda v: v.update(stage="readback"),
):
    bad = copy.deepcopy(unknown); mutator(bad)
    try: module["validate_remote"](bad, 2)
    except module["Stop"]: pass
    else: raise AssertionError("contradictory UNKNOWN accepted")

skipped_readback_stop = module["fixture_result"](False, False)
skipped_readback_stop.update(status="CANDIDATE_CODEX_DEACTIVATE_R1_STOP", stage="readback",
                             readback_http_status=500, inactive_readback=False,
                             failure_category="http_5xx")
assert module["validate_remote"](skipped_readback_stop, 1) == skipped_readback_stop

native = module["fixture_native"]()
assert module["validate_native_child"](native, 0, module["CODEX_CONNECTION"]) == native
native_negatives = (
    ({"connection_id": "wrong-target"}, 0),
    ({"status": "CODEX_DEACTIVATE_STOP", "stage": "get_before", "before_active": None,
      "patch_dispatched": False, "patch_http_status": None,
      "readback_http_status": 401, "inactive_readback": False,
      "failure_category": "http_4xx"}, 0),
    ({"status": "CODEX_DEACTIVATE_UNKNOWN", "stage": "patch",
      "patch_dispatched": False, "patch_http_status": None,
      "readback_http_status": 200, "inactive_readback": False,
      "failure_category": "timeout"}, 2),
)
for mutation, rc in native_negatives:
    bad = copy.deepcopy(native); bad.update(mutation)
    try: module["validate_native_child"](bad, rc, module["CODEX_CONNECTION"])
    except ValueError: pass
    else: raise AssertionError("contradictory native child envelope accepted")

native_dispatch = module["fixture_unknown"]("patch")
native_dispatch.update(stage="native_dispatch", connection_id=None, before_active=None,
                       patch_dispatched=None, patch_http_status=None,
                       readback_http_status=None, inactive_readback=None,
                       failure_category="remote_envelope")
assert module["validate_remote"](native_dispatch, 2) == native_dispatch

payload = module["render_remote"]("oma_fixture_codex_deactivation_secret")
rendered = payload.decode("utf-8")
rendered_tree = ast.parse(rendered)
rendered_validator = next(node for node in ast.walk(rendered_tree)
                          if isinstance(node, ast.FunctionDef) and node.name == "validate_native_child")
rendered_namespace = {}
exec(compile(ast.fix_missing_locations(ast.Module(body=[rendered_validator], type_ignores=[])),
             "<rendered-validator>", "exec"), rendered_namespace)
for mutation, rc in native_negatives:
    bad = copy.deepcopy(native); bad.update(mutation)
    try: rendered_namespace["validate_native_child"](bad, rc, module["CODEX_CONNECTION"])
    except ValueError: pass
    else: raise AssertionError("rendered native child contradiction accepted")
text = module["NODE"]
assert b"oma_fixture_codex_deactivation_secret" not in payload
assert text.count("request('GET','/api/providers/'+CODEX)") == 2
assert text.count("request('PATCH','/api/providers/'+CODEX,{isActive:false})") == 1
assert "/v1/chat" not in text and "container','start" not in text and "container','stop" not in text
assert rendered.index("def validate_native_child") < rendered.index("native=validate_native_child") < rendered.index("outer_status=")
assert "'connection_id':None" in rendered
module["offline_check"]()
print("PASS: candidate-only Codex deactivate skip/PATCH/readback/UNKNOWN boundaries")
