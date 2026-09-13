"""Focused local sanitization checks for the R5 native GET diagnosis."""
import copy
import pathlib
import runpy


ROOT = pathlib.Path(__file__).resolve().parents[1]
module = runpy.run_path(str(ROOT / "scripts/auto-switch-candidate-key-r5-get-diagnosis-20260913.py"), run_name="r5_get_diag_test")
fake = "oma_fixture_diagnostic_secret"
payload = module["render_remote"](fake)
assert fake.encode() not in payload
assert payload.count(b"/api/keys") == 1
for forbidden in (b"request('POST'", b"request('PATCH'", b"/v1/chat", b"/v1/models"):
    assert forbidden not in payload

good = {"status": "CANDIDATE_KEY_R5_GET_DIAG_PASS", "candidate_id": module["CANDIDATE_ID"],
        "preconditions_passed": True, "http_status": 200, "http_category": "ok",
        "json_parsed": True, "schema_category": "expected", "keys_is_array": True,
        "key_name_present": False, "child_outcome": "complete"}
assert module["validate_remote"](good, 0) == good

parse_error = copy.deepcopy(good)
parse_error.update(http_status=503, http_category="server_5xx", json_parsed=False,
                   schema_category="unparsed", keys_is_array=None, key_name_present=None,
                   child_outcome="parse_error")
assert module["validate_remote"](parse_error, 0) == parse_error

transport_error = copy.deepcopy(good)
transport_error.update(http_status=None, http_category="none", json_parsed=False,
                       schema_category="unparsed", keys_is_array=None, key_name_present=None,
                       child_outcome="timeout")
assert module["validate_remote"](transport_error, 0) == transport_error

for change in (
    lambda v: v.update(raw_body="secret-like-value"),
    lambda v: v.update(http_category="arbitrary"),
    lambda v: v.update(schema_category="keys,keyHash"),
    lambda v: v.update(child_outcome="raw error"),
    lambda v: v.update(http_status=999),
    lambda v: v.update(child_outcome="parse_error", http_status=None, json_parsed=False,
                       schema_category="unparsed", keys_is_array=None, key_name_present=None),
    lambda v: v.update(child_outcome="timeout", http_status=None, json_parsed=False,
                       schema_category="unparsed", keys_is_array=None, key_name_present=None),
    lambda v: v.update(schema_category="not_object", keys_is_array=True, key_name_present=False),
    lambda v: v.update(keys_is_array=False, key_name_present=False),
):
    bad = copy.deepcopy(good); change(bad)
    try:
        module["validate_remote"](bad, 0)
    except module["Stop"]:
        pass
    else:
        raise AssertionError("unsafe diagnostic result accepted")

module["self_check"]()
print("PASS: one-GET rendering and fixed secret-free result classification")
