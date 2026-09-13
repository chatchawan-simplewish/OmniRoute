"""Capture one frozen candidate-key R5 read-only preflight into a fresh receipt."""
import argparse
import hashlib
import importlib.util
import json
import os
import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
COORDINATOR_ROOT = pathlib.Path(r"C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-auto-switch-20260912")
ROLLOUT_ROOT = pathlib.Path(r"C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-live-rollout-20260913")
R5 = ROOT / "scripts/auto-switch-candidate-key-r5-20260913.py"
R5_TEST = ROOT / "scripts/test-auto-switch-candidate-key-r5-20260913.py"
R5_CONTRACT = ROOT / "docs/auto-switch-candidate-key-r5-contract-20260913.md"
TRANSPORT = COORDINATOR_ROOT / "scripts/auto-switch-image-transfer-r3-20260913.py"
OLD_PREFLIGHT = ROOT / "docs/auto-switch-candidate-key-r5-preflight-result-20260913.json"
DIAGNOSTIC = ROOT / "docs/auto-switch-candidate-key-r5-get-diagnosis-result-20260913.json"
EVIDENCE_REVIEW = ROLLOUT_ROOT / "docs/auto-switch-candidate-key-r5-get-diagnosis-evidence-review-20260913.md"
CONTRACT = ROOT / "docs/auto-switch-candidate-key-r5-preflight-capture-contract-20260913.md"
TEST = ROOT / "scripts/test-auto-switch-candidate-key-r5-preflight-capture-20260913.py"
RESULT = ROOT / "docs/auto-switch-candidate-key-r5-preflight-result-r2-20260913.json"

R5_SHA256 = "191913463849c7c42ae2e52126f73825b21bc661b6e88bfe6a799ed656f19273"
R5_TEST_SHA256 = "656ee0a395393d08bf1a3fcf798fcf4a6c13611a3dccc251d38d1ba934a04fbe"
R5_CONTRACT_SHA256 = "5bb65014f5fb43065275206de455872fc77720084106d6b625be8db03195a7c0"
TRANSPORT_SHA256 = "78bb97e57d6229aae84c2f0d0caaf68eeb71ba6b92e69415d83af2a869b8224a"
OLD_PREFLIGHT_SHA256 = "54287dda6512affc813a87306c13e82996290487659b4ac61bd4bd09b81970b9"
DIAGNOSTIC_SHA256 = "551e9238a46e71715327a60483f8e0b8cf37c66f19708377c8c3529993863539"
EVIDENCE_REVIEW_SHA256 = "5fa91ff613a27b2a1ef425fc6a2ca15ba5a096bd0e22ec538f62e311d529055e"
CANDIDATE_ID = "9468859edcdb483c53900edde14d301a162cccc791079154677e913f39bf26a3"
SCHEMA = "auto-switch-candidate-key-r5-preflight-capture-r2/v1"
RESULT_LIMIT = 16384


class Stop(Exception):
    pass


def digest(path):
    with pathlib.Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def regular(path):
    path = pathlib.Path(path)
    return path.is_file() and not path.is_symlink()


def load(path, expected, name):
    if not regular(path) or digest(path) != expected:
        raise Stop("local_validation")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def dependencies():
    return (
        (R5, R5_SHA256), (R5_TEST, R5_TEST_SHA256), (R5_CONTRACT, R5_CONTRACT_SHA256),
        (TRANSPORT, TRANSPORT_SHA256), (OLD_PREFLIGHT, OLD_PREFLIGHT_SHA256),
        (DIAGNOSTIC, DIAGNOSTIC_SHA256), (EVIDENCE_REVIEW, EVIDENCE_REVIEW_SHA256),
    )


def review_payload():
    return {
        "schema": SCHEMA,
        "candidate_id": CANDIDATE_ID,
        "request_method": "GET",
        "request_paths": ["/api/keys", "/api/combos", "/api/providers/8f92f200-d280-47b3-b380-2d94be0a4b75"],
        "r5_sha256": digest(R5),
        "r5_test_sha256": digest(R5_TEST),
        "r5_contract_sha256": digest(R5_CONTRACT),
        "transport_sha256": digest(TRANSPORT),
        "old_preflight_sha256": digest(OLD_PREFLIGHT),
        "diagnostic_sha256": digest(DIAGNOSTIC),
        "evidence_review_sha256": digest(EVIDENCE_REVIEW),
        "launcher_sha256": digest(__file__),
        "test_sha256": digest(TEST),
        "contract_sha256": digest(CONTRACT),
        "result": str(RESULT),
    }


def classify_child(stdout, stderr, returncode, r5):
    if stderr or len(stdout) > RESULT_LIMIT or returncode not in (0, 1):
        raise Stop("child_envelope")
    try:
        outer = json.loads(stdout)
    except Exception as error:
        raise Stop("child_envelope") from error
    if not isinstance(outer, dict) or set(outer) != {"schema", "remote"} or outer["schema"] != r5.PREFLIGHT_SCHEMA:
        raise Stop("child_envelope")
    try:
        remote = r5.validate_preflight(outer["remote"], returncode)
    except Exception as error:
        raise Stop("child_envelope") from error
    all_pass = all(remote["checks"].values())
    if (returncode == 0) != all_pass:
        raise Stop("child_envelope")
    status = "PASS" if returncode == 0 else "STOP"
    stage = "complete" if status == "PASS" else remote["stage"]
    return {"schema": SCHEMA, "status": status, "stage": stage,
            "child_returncode": returncode, "all_17_pass": all_pass, "remote": remote}


def reserve_result():
    if RESULT.exists() or RESULT.is_symlink():
        raise Stop("stale_result")
    return os.open(RESULT, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0), 0o600)


def finish_result(fd, value):
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
    if len(raw) > RESULT_LIMIT:
        raise Stop("result_validation")
    try:
        offset = 0
        while offset < len(raw):
            count = os.write(fd, raw[offset:])
            if count <= 0:
                raise OSError("result_write")
            offset += count
        os.fsync(fd)
    finally:
        os.close(fd)


def execute(reviewed):
    if not all(regular(path) and digest(path) == expected for path, expected in dependencies()):
        raise Stop("local_validation")
    if not regular(TEST) or not regular(CONTRACT) or not regular(reviewed):
        raise Stop("local_validation")
    if json.loads(reviewed.read_text(encoding="utf-8")) != review_payload():
        raise Stop("review_pin_mismatch")
    if not os.environ.get("PROGRAMDATA") or os.environ.get("PYTHONOPTIMIZE"):
        raise Stop("local_validation")
    token = os.environ.get("OMNIROUTE_ADMIN_TOKEN", "")
    if not re.fullmatch(r"oma_[A-Za-z0-9._~-]{16,512}", token):
        raise Stop("local_validation")
    r5 = load(R5, R5_SHA256, "candidate_key_r5_capture")
    if r5.CANDIDATE_ID != CANDIDATE_ID or len(r5.PREFLIGHT_CHECKS) != 17 or len(set(r5.PREFLIGHT_CHECKS)) != 17:
        raise Stop("local_validation")
    transport = load(TRANSPORT, TRANSPORT_SHA256, "candidate_key_r5_capture_transport")
    fd = reserve_result()
    receipt = {"schema": SCHEMA, "status": "UNKNOWN", "stage": "child_transport",
               "child_returncode": None, "all_17_pass": False, "remote": None}
    try:
        try:
            returncode, stdout, stderr = transport.bounded_capture(
                [sys.executable, "-B", str(R5), "--preflight"], None, 240)
            receipt = classify_child(stdout, stderr, returncode, r5)
        except Exception:
            returncode = 1
        return returncode
    finally:
        finish_result(fd, receipt)
        print(json.dumps({"status": receipt["status"], "stage": receipt["stage"],
                          "all_17_pass": receipt["all_17_pass"]}, sort_keys=True))


def self_check():
    if not all(regular(path) and digest(path) == expected for path, expected in dependencies()):
        raise Stop("local_validation")
    if RESULT.exists() or RESULT.is_symlink():
        raise Stop("stale_result")
    r5 = load(R5, R5_SHA256, "candidate_key_r5_capture_check")
    checks = {name: True for name in r5.PREFLIGHT_CHECKS}
    remote = {"status": "CANDIDATE_KEY_R5_PREFLIGHT_PASS", "stage": "complete",
              "candidate_id": CANDIDATE_ID, "checks": checks}
    if classify_child(json.dumps({"schema": r5.PREFLIGHT_SCHEMA, "remote": remote}, sort_keys=True).encode(), b"", 0, r5)["status"] != "PASS":
        raise Stop("local_validation")
    checks = dict(checks); checks["combo_api_schema"] = False
    remote = {"status": "CANDIDATE_KEY_R5_PREFLIGHT_STOP", "stage": "native_preflight",
              "candidate_id": CANDIDATE_ID, "checks": checks}
    stopped = classify_child(json.dumps({"schema": r5.PREFLIGHT_SCHEMA, "remote": remote}, sort_keys=True).encode(), b"", 1, r5)
    if stopped["status"] != "STOP" or stopped["all_17_pass"] is not False:
        raise Stop("local_validation")
    print("CANDIDATE_KEY_R5_PREFLIGHT_CAPTURE_PREPARATION_PASS")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--render-review-payload", action="store_true")
    parser.add_argument("--execute-reviewed", type=pathlib.Path)
    args = parser.parse_args()
    if sum((args.self_check, args.render_review_payload, bool(args.execute_reviewed))) != 1:
        raise Stop("local_validation")
    if args.self_check:
        self_check(); return 0
    if args.render_review_payload:
        print(json.dumps(review_payload(), indent=2, sort_keys=True)); return 0
    return execute(args.execute_reviewed)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        stage = str(error) if str(error) in {"stale_result", "review_pin_mismatch"} else "local_validation"
        print(json.dumps({"status": "CANDIDATE_KEY_R5_PREFLIGHT_CAPTURE_NOT_EXECUTED", "stage": stage}, sort_keys=True))
        raise SystemExit(1)
