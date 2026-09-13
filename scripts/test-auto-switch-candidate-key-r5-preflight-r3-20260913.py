import importlib.util
import pathlib


ROOT = pathlib.Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "scripts/auto-switch-candidate-key-r5-preflight-r3-20260913.py"
spec = importlib.util.spec_from_file_location("preflight_r3", LAUNCHER)
module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
r5 = module.load(module.R5, module.R5_SHA256, "candidate_key_r5_preflight_r3_test")

# Pin the actual e53 handler envelopes used by the native validator.
keys_source = module.KEYS_ROUTE.read_text("utf-8")
combos_source = module.COMBOS_ROUTE.read_text("utf-8")
provider_source = module.PROVIDER_ROUTE.read_text("utf-8")
assert "keys: maskedKeys" in keys_source and "allowKeyReveal: isApiKeyRevealEnabled()" in keys_source and "total," in keys_source
assert "NextResponse.json({ combos, total })" in combos_source
assert "NextResponse.json({ connection: result })" in provider_source


def native(checks, statuses, categories, schemas, steps, status, stage, failure, outcome):
    return {"status": status, "stage": stage, "checks": checks,
            "evidence": {"http_status": statuses, "http_category": categories, "schema": schemas,
                         "completed_steps": steps, "failure_category": failure, "child_outcome": outcome}}


all_true = {name: True for name in module.NATIVE_CHECKS}
passed = native(all_true, {name: 200 for name in ("keys", "combos", "codex")},
                {name: "ok" for name in ("keys", "combos", "codex")},
                {name: "expected" for name in ("keys", "combos", "codex")},
                ["keys", "combos", "codex"], "KEY_NATIVE_R5_PREFLIGHT_R3_PASS", "complete", None, "complete")
module.validate_native(passed, 0)

# A later combo failure must retain the two successful key predicates and key evidence.
partial = {name: name in {"key_api_schema", "key_name_absent"} for name in module.NATIVE_CHECKS}
stopped = native(partial, {"keys": 200, "combos": 500, "codex": None},
                 {"keys": "ok", "combos": "server_5xx", "codex": None},
                 {"keys": "expected", "combos": None, "codex": None},
                 ["keys"], "KEY_NATIVE_R5_PREFLIGHT_R3_STOP", "combo_api_schema", "server_5xx", "http_error")
module.validate_native(stopped, 1)
broken = {**stopped, "evidence": {**stopped["evidence"], "completed_steps": []}}
try:
    module.validate_native(broken, 1)
except module.Stop:
    pass
else:
    raise AssertionError("lost accumulated evidence accepted")

outer_checks = {name: (passed["checks"][name] if name in module.NATIVE_CHECKS else True)
                for name in sorted(r5.PREFLIGHT_CHECKS)}
module.validate_remote({"status": "CANDIDATE_KEY_R5_PREFLIGHT_R3_PASS", "stage": "complete",
                        "candidate_id": module.CANDIDATE_ID, "checks": outer_checks, "native": passed}, 0, r5)

print("CANDIDATE_KEY_R5_PREFLIGHT_R3_TEST_PASS")
