import importlib.util
import json
import pathlib
import subprocess
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "scripts/auto-switch-candidate-key-r5-preflight-capture-20260913.py"
spec = importlib.util.spec_from_file_location("capture", LAUNCHER)
capture = importlib.util.module_from_spec(spec); spec.loader.exec_module(capture)
r5 = capture.load(capture.R5, capture.R5_SHA256, "candidate_key_r5_capture_test")
transport = capture.load(capture.TRANSPORT, capture.TRANSPORT_SHA256, "candidate_key_r5_capture_test_transport")


def envelope(status, stage, checks):
    remote = {"status": status, "stage": stage, "candidate_id": capture.CANDIDATE_ID, "checks": checks}
    return json.dumps({"schema": r5.PREFLIGHT_SCHEMA, "remote": remote}, separators=(",", ":"), sort_keys=True).encode()


checks = {name: True for name in r5.PREFLIGHT_CHECKS}
code = "import sys;sys.stdout.buffer.write(" + repr(envelope("CANDIDATE_KEY_R5_PREFLIGHT_PASS", "complete", checks)) + ")"
rc, out, err = transport.bounded_capture([sys.executable, "-c", code], None, 10)
assert capture.classify_child(out, err, rc, r5)["all_17_pass"] is True

failed = dict(checks); failed["codex_inactive"] = False
value = capture.classify_child(envelope("CANDIDATE_KEY_R5_PREFLIGHT_STOP", "native_preflight", failed), b"", 1, r5)
assert value["status"] == "STOP" and value["all_17_pass"] is False and value["child_returncode"] == 1

for bad in (
    (envelope("CANDIDATE_KEY_R5_PREFLIGHT_PASS", "complete", failed), b"", 0),
    (envelope("CANDIDATE_KEY_R5_PREFLIGHT_STOP", "native_preflight", failed), b"warning", 1),
    (b"{}", b"", 1),
):
    try:
        capture.classify_child(*bad, r5)
    except capture.Stop:
        pass
    else:
        raise AssertionError("contradictory or invalid envelope accepted")

print("CANDIDATE_KEY_R5_PREFLIGHT_CAPTURE_TEST_PASS")
