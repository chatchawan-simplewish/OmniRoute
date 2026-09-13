import importlib.util
import json
import pathlib
import subprocess


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


def rejected(value, returncode):
    try:
        module.validate_native(value, returncode)
    except module.Stop:
        return
    raise AssertionError("contradictory native evidence accepted")


bad_pass = json.loads(json.dumps(passed)); bad_pass["evidence"]["http_status"]["keys"] = 401
bad_pass["evidence"]["http_category"]["keys"] = "auth_401"; bad_pass["evidence"]["schema"]["keys"] = "mismatch"
rejected(bad_pass, 0)

# A later combo failure must retain the two successful key predicates and key evidence.
partial = {name: name in {"key_api_schema", "key_name_absent"} for name in module.NATIVE_CHECKS}
stopped = native(partial, {"keys": 200, "combos": 500, "codex": None},
                 {"keys": "ok", "combos": "server_5xx", "codex": None},
                 {"keys": "expected", "combos": None, "codex": None},
                 ["keys"], "KEY_NATIVE_R5_PREFLIGHT_R3_STOP", "combo_api_schema", "server_5xx", "http_error")
module.validate_native(stopped, 1)
broken = {**stopped, "evidence": {**stopped["evidence"], "completed_steps": []}}
rejected(broken, 1)
wrong_stage = json.loads(json.dumps(stopped)); wrong_stage["stage"] = "codex_schema"; rejected(wrong_stage, 1)
later = json.loads(json.dumps(stopped)); later["evidence"]["http_status"]["codex"] = 200; later["evidence"]["http_category"]["codex"] = "ok"; later["evidence"]["schema"]["codex"] = "expected"; rejected(later, 1)

outer_checks = {name: (passed["checks"][name] if name in module.NATIVE_CHECKS else True)
                for name in sorted(r5.PREFLIGHT_CHECKS)}
module.validate_remote({"status": "CANDIDATE_KEY_R5_PREFLIGHT_R3_PASS", "stage": "complete",
                        "candidate_id": module.CANDIDATE_ID, "checks": outer_checks, "native": passed}, 0, r5)


def run_rendered(responses):
    source = module.render_node("oma_fixture_preflight_r3_secret", r5)
    stub = """const __responses=__ROWS__;const http={request:(opts,cb)=>{const handlers={};const q={setTimeout(){},on(name,fn){handlers[name]=fn},end(){queueMicrotask(()=>{const item=__responses.shift();if(item.error){const e=new Error(item.error);handlers.error(e);return}const rh={};const r={statusCode:item.status,on(name,fn){rh[name]=fn}};cb(r);if(item.body!==null)rh.data(Buffer.from(item.body));rh.end()})}};return q}};""".replace("__ROWS__", json.dumps(responses, separators=(",", ":")))
    source = source.replace("const http=require('node:http');", stub)
    child = subprocess.run(["node", "-"], input=source.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10)
    assert not child.stderr
    return json.loads(child.stdout), child.returncode


success_rows = [
    {"status": 200, "body": json.dumps({"keys": [], "total": 0, "allowKeyReveal": False})},
    {"status": 200, "body": json.dumps({"combos": [], "total": 0})},
    {"status": 200, "body": json.dumps({"connection": {"id": r5.CODEX_CONNECTION, "provider": "codex", "isActive": False}})},
]
whole_pass, rc = run_rendered(success_rows); module.validate_native(whole_pass, rc)
whole_stop, rc = run_rendered([success_rows[0], {"status": 500, "body": json.dumps({"error": "fixed"})}])
module.validate_native(whole_stop, rc)
assert whole_stop["checks"]["key_name_absent"] is True and whole_stop["evidence"]["completed_steps"] == ["keys"]

print("CANDIDATE_KEY_R5_PREFLIGHT_R3_TEST_PASS")
