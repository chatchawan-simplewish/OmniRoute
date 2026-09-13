"""Focused offline boundaries for the R1 actual-hardware qualification source."""
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
                                             "fallback_reason", "request_started_ns", "request_finished_ns")}
request_unknown.update(status="REQUEST_UNKNOWN", index=1, content_valid=False)
try: module["validate_request"](request_unknown, 2, 1)
except module["Stop"] as error: assert str(error) == "transport_unknown"
else: raise AssertionError("request uncertainty accepted")

request_pass = {"status": "REQUEST_PASS", "index": 1, "http_status": 200, "content_valid": True,
                "selected_connection_id": module["Q6_CONNECTION"], "resolved_provider": "llama-cpp",
                "resolved_model": module["Q6_MODEL"], "candidate_attempt": 1,
                "reviewer_verdict": "PASS", "fallback_reason": "initial",
                "request_started_ns": 1, "request_finished_ns": 2}
assert module["validate_request"](request_pass, 0, 1) == request_pass
bad_request = copy.deepcopy(request_pass); bad_request["resolved_model"] = module["Q4_MODEL"]
try: module["validate_request"](bad_request, 0, 1)
except module["Stop"]: pass
else: raise AssertionError("wrong physical model accepted")

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

credential_input = base64.b64encode(json.dumps({
    "storage_key": "fixture-storage-key",
    "api_key": "fixture-api-key",
    "access_token": "fixture-access-token",
}, separators=(",", ":")).encode()).decode()
credential_program = module["Q4_CREDENTIAL_NODE"].replace("__INPUT_B64__", credential_input)
credential_check = subprocess.run(
    ["node", "--input-type=module"], input=credential_program.encode(),
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10, check=False,
)
assert credential_check.returncode == 0 and credential_check.stderr == b""
assert json.loads(credential_check.stdout) == {
    "status": "Q4_CREDENTIAL_PASS", "source": "apiKey",
    "credential_b64": base64.b64encode(b"fixture-api-key").decode(),
}
for payload in (prep_source, module["render_request"](1, module["new_ids"](), "e" * 64),
                module["render_evidence"]([module["new_ids"]() for _ in range(3)], "e" * 64, 0),
                module["render_stop"]("e" * 64)):
    assert b"subprocess.run" not in payload and b"bounded_capture" in payload

module["offline_check"]()
print("PASS: R1 identity/key schema, uncertainty, authenticated Q4 readiness, timing and event evidence")
