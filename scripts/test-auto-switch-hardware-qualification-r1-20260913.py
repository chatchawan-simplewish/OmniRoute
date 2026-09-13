"""Focused offline boundaries for the R1 actual-hardware qualification source."""
import ast
import concurrent.futures
import base64
import copy
import json
import pathlib
import runpy
import subprocess


ROOT = pathlib.Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "scripts/auto-switch-hardware-qualification-r1-20260913.py"
module = runpy.run_path(str(LAUNCHER), run_name="hardware_qualification_r1_test")

assert module["EXECUTION_READY"] is False
assert module["SOURCE"] == "e53d895e9a5e38a7f06ce59de254835f10e829c1"
assert module["IMAGE"] == "sha256:8211e1071a3b68eac01673d76129150eb0c0fea329dd222bc8bf0394b13fc844"
assert module["CANDIDATE_ID"] == "9468859edcdb483c53900edde14d301a162cccc791079154677e913f39bf26a3"
assert module["KEY_ID"] == "a4ba1b25-64cf-4e1b-b694-a1b8bcb94f8a"
assert module["require_bound"]() == []

module["validate_spent_candidate_receipt"](module["parse_receipt"](module["CANDIDATE_START_RESULT"]))
module["validate_reconciliation_receipt"](module["parse_receipt"](module["RECONCILIATION_RESULT"]))
key = module["load_module"](module["CANDIDATE_KEY_LAUNCHER"], module["CANDIDATE_KEY_LAUNCHER_SHA256"], "hardware_test_key")
key_receipt = module["parse_receipt"](module["CANDIDATE_KEY_RESULT"])
assert module["validate_key_receipt"](key_receipt, key) == key_receipt
bad_key_receipt = copy.deepcopy(key_receipt)
bad_key_receipt["remote"]["key_id"] = "11111111-1111-4111-8111-111111111111"
try: module["validate_key_receipt"](bad_key_receipt, key)
except module["Stop"]: pass
else: raise AssertionError("wrong qualification key accepted")

prep = {"status": "HARDWARE_PREP_PASS", "stage": "complete",
        "candidate_id": module["FIXTURE_CANDIDATE_ID"], "candidate_stopped": True,
        "companion_id": "e" * 64, "detail_baseline": 0, "network_private": True,
        "published_ports": 0, "cloud_false": True, "codex_inactive": True,
        "migration_170": True, "migration_171": True, "key_policy": True,
        "environment_exact": True, "q4_reachable": True,
        "health_counters": {"attempts": 3, "timeouts": 1, "nonzero": 1, "successes": 1}}
assert module["validate_prep"](prep, 0, module["FIXTURE_CANDIDATE_ID"]) == prep
assert module["emitted_fields"](module["render_prep"]().decode(), "HARDWARE_PREP_PASS") == set(prep)

good = module["fixture_result"]()
assert module["validate_result"](good, 0, module["FIXTURE_CANDIDATE_ID"]) == good


def rejected(mutator):
    value = copy.deepcopy(good); mutator(value)
    try: module["validate_result"](value, 0, module["FIXTURE_CANDIDATE_ID"])
    except module["Stop"]: return
    raise AssertionError("invalid hardware result accepted")


rejected(lambda v: v["requests"][2].update(q6_submissions=1))
rejected(lambda v: v["requests"][2].update(q4_http_status=530, content_valid=False))
rejected(lambda v: v["requests"][2].update(q4_selected_ms=5001))
rejected(lambda v: v["requests"][2].update(q4_dispatch_at="2026-09-12T23:59:59.000Z"))
rejected(lambda v: v["requests"][0].update(candidate_attempt=2))
rejected(lambda v: v["requests"][0].update(reviewer_model="unexpected/model"))
rejected(lambda v: v["requests"][0].update(reviewer_attempt=3))
rejected(lambda v: v["requests"][0].update(event_order=False))
rejected(lambda v: v["requests"][2].update(request_started_ns=3_000_000_000))
rejected(lambda v: v["metrics_before_third"].update(processing=1))
rejected(lambda v: v["metrics_before_third"].update(deferred=1))
rejected(lambda v: v["health_counters"].update(attempts=99))
rejected(lambda v: v["correlation"].update(q4_after_full=False))

request_unknown = {name: None for name in ("http_status", "selected_connection_id", "resolved_provider",
                                             "resolved_model", "candidate_attempt", "reviewer_verdict",
                                             "fallback_reason", "request_id")}
request_unknown.update(status="REQUEST_UNKNOWN", index=1, content_valid=False)
request_id = "11111111-1111-4111-8111-111111111111"
try: module["validate_request"](request_unknown, 2, 1, request_id)
except module["Stop"] as error: assert str(error) == "transport_unknown"
else: raise AssertionError("request uncertainty accepted")

request_pass = {"status": "REQUEST_PASS", "index": 1, "http_status": 200, "content_valid": True,
                "request_id": request_id,
                "selected_connection_id": module["Q6_CONNECTION"], "resolved_provider": "llama-cpp",
                "resolved_model": module["Q6_MODEL"], "candidate_attempt": 1,
                "reviewer_verdict": "PASS", "fallback_reason": "initial"}
assert module["validate_request"](request_pass, 0, 1, request_id) == request_pass
bad_request = copy.deepcopy(request_pass); bad_request["resolved_model"] = module["Q4_MODEL"]
try: module["validate_request"](bad_request, 0, 1, request_id)
except module["Stop"]: pass
else: raise AssertionError("wrong physical model accepted")
wrong_request_id = copy.deepcopy(request_pass); wrong_request_id["request_id"] = "22222222-2222-4222-8222-222222222222"
try: module["validate_request"](wrong_request_id, 0, 1, request_id)
except module["Stop"]: pass
else: raise AssertionError("unmatched runtime request ID accepted")

try: module["validate_evidence"]({"status": "HARDWARE_EVIDENCE_UNKNOWN", "companion_stopped": None}, 2)
except module["Stop"] as error: assert str(error) == "transport_unknown"
else: raise AssertionError("evidence uncertainty accepted")

future = concurrent.futures.Future(); future.set_exception(TimeoutError())
try: module["resolve_future"](future)
except module["Stop"] as error: assert str(error) == "transport_unknown"
else: raise AssertionError("future uncertainty accepted")

complete = concurrent.futures.Future(); complete.set_result(request_pass)
uncertain = concurrent.futures.Future(); uncertain.set_exception(module["Stop"]("transport_unknown"))
deterministic = concurrent.futures.Future(); deterministic.set_exception(module["Stop"]("request_validation"))
try: module["resolve_futures"]([complete, deterministic, uncertain], 0)
except module["Stop"] as error: assert str(error) == "transport_unknown"
else: raise AssertionError("concurrent uncertainty was hidden by deterministic failure")
pending = concurrent.futures.Future()
try: module["resolve_futures"]([complete, pending], 0)
except module["Stop"] as error: assert str(error) == "transport_unknown"
else: raise AssertionError("pending request accepted as deterministic stop")

prep_source = module["render_prep"]()
assert b"ipaddress.ip_interface(member_address)" in prep_source
assert b"HTTPConnection('172.18.0.3'" not in prep_source
assert b"Q4_PROXY_HOST='bell-cloudflare-proxy'" in prep_source
assert b"q4url.hostname!=Q4_PROXY_HOST" in prep_source
assert b"'Authorization':'Bearer '+token" in prep_source
assert b"Q4_MODEL='qwen3.8-27b-unsloth-ud-q4ks'" in prep_source

prep_tree = ast.parse(prep_source.decode())
one_nodes = [node for node in prep_tree.body if isinstance(node, (ast.ClassDef, ast.FunctionDef))
             and node.name in {"Stop", "Unknown", "one"}]
one_scope = {"docker": lambda _: b"{}", "stage": "candidate_stop"}
exec(compile(ast.Module(one_nodes, type_ignores=[]), "<hardware-prep-one>", "exec"), one_scope)
try: one_scope["one"](["container", "inspect", "candidate"])
except one_scope["Unknown"]: pass
else: raise AssertionError("post-mutation malformed Docker JSON was not UNKNOWN")
one_scope["stage"] = "identity"
try: one_scope["one"](["container", "inspect", "candidate"])
except one_scope["Stop"]: pass
else: raise AssertionError("pre-mutation malformed Docker JSON was not STOP")

safe_nodes = [node for node in prep_tree.body
              if (isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == "BINDINGS"
                                                       for target in node.targets))
              or (isinstance(node, ast.FunctionDef) and node.name == "safe_env")]
safe_scope = {"json": json}
exec(compile(ast.Module(safe_nodes, type_ignores=[]), "<hardware-prep-env>", "exec"), safe_scope)
baseline_env = {"PATH": "/usr/local/bin:/usr/bin", "NODE_ENV": "production"}
expected_env = dict(baseline_env)
expected_env.update({
    "DATA_DIR": "/app/data",
    "OMNIROUTE_AGENT_ROUTE_BINDINGS_JSON": json.dumps(safe_scope["BINDINGS"], separators=(",", ":"), sort_keys=True),
    "OMNIROUTE_DISABLE_BACKGROUND_SERVICES": "true",
    "OMNIROUTE_DISABLE_CREDENTIAL_HEALTH_CHECK": "1",
    "PROXY_HEALTH_ENABLED": "false", "FREE_PROXY_AUTO_SYNC_ENABLED": "false",
    "OMNIROUTE_ENABLE_LIVE_WS": "0", "OMNIROUTE_DB_HEALTHCHECK_INTERVAL_MS": "0",
    "OMNIROUTE_WAL_TRUNCATE_INTERVAL_MS": "0",
})
assert safe_scope["safe_env"](expected_env, baseline_env)
assert not safe_scope["safe_env"]({**expected_env, "UNEXPECTED": "1"}, baseline_env)

credential_input = base64.b64encode(json.dumps({
    "storage_key": "fixture-storage-key",
    "api_key": "fixture-api-key",
    "access_token": None,
}, separators=(",", ":")).encode()).decode()
credential_program = module["Q4_CREDENTIAL_NODE"].replace("__INPUT_B64__", credential_input)
credential_check = subprocess.run(
    ["node", "--input-type=module"], input=credential_program.encode(),
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10, check=False,
)
assert credential_check.returncode == 0 and credential_check.stderr == b""
assert json.loads(credential_check.stdout) == {
    "status": "Q4_CREDENTIAL_PASS",
    "credential_b64": base64.b64encode(b"fixture-api-key").decode(),
}

encrypt_check = subprocess.run(
    ["node", "--input-type=module"],
    input=b"""import crypto from 'node:crypto';
const secret='fixture-storage-key',plain='fixture-api-key',iv=Buffer.alloc(16,7);
const key=crypto.scryptSync(secret,'omniroute-field-encryption-v1',32);
const cipher=crypto.createCipheriv('aes-256-gcm',key,iv);
const body=cipher.update(plain,'utf8','hex')+cipher.final('hex');
process.stdout.write('enc:v1:'+iv.toString('hex')+':'+body+':'+cipher.getAuthTag().toString('hex'));
""",
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10, check=False,
)
assert encrypt_check.returncode == 0 and encrypt_check.stderr == b""
encrypted_input = base64.b64encode(json.dumps({
    "storage_key": "fixture-storage-key", "api_key": encrypt_check.stdout.decode(),
}, separators=(",", ":")).encode()).decode()
encrypted_program = module["Q4_CREDENTIAL_NODE"].replace("__INPUT_B64__", encrypted_input)
encrypted_check = subprocess.run(
    ["node", "--input-type=module"], input=encrypted_program.encode(),
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10, check=False,
)
assert encrypted_check.returncode == 0 and encrypted_check.stderr == b""
assert json.loads(encrypted_check.stdout) == {
    "status": "Q4_CREDENTIAL_PASS",
    "credential_b64": base64.b64encode(b"fixture-api-key").decode(),
}

invoke_globals = module["run_request"].__globals__
old_invoke, old_render = invoke_globals["invoke"], invoke_globals["render_request"]
invoke_globals["invoke"] = lambda *_: (request_pass, 0)
invoke_globals["render_request"] = lambda *_: b"fixture"
before_request = module["time"].monotonic_ns()
timed_request = module["run_request"](object(), 1, {"request_id": request_id}, "e" * 64)
after_request = module["time"].monotonic_ns()
invoke_globals["invoke"], invoke_globals["render_request"] = old_invoke, old_render
assert before_request <= timed_request["request_started_ns"] <= timed_request["request_finished_ns"] <= after_request
rendered_request = module["render_request"](1, module["new_ids"](), "e" * 64)
assert b"monotonic_ns" not in rendered_request
assert b"'x-correlation-id':ids.request_id" in rendered_request
assert b"request_id:res.headers['x-correlation-id']||null" in rendered_request
assert '"request_id": response["request_id"]' in LAUNCHER.read_text(encoding="utf-8")
for payload in (prep_source, module["render_request"](1, module["new_ids"](), "e" * 64),
                module["render_evidence"]([module["new_ids"]() for _ in range(3)], "e" * 64, 0),
                module["render_stop"]("e" * 64)):
    assert b"subprocess.run" not in payload and b"bounded_capture" in payload

module["offline_check"]()
print("PASS: R1 identity/key schema, uncertainty, authenticated Q4 readiness, timing and event evidence")
