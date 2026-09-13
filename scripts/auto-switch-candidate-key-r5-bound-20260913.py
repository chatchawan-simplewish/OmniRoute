"""Bind the unconsumed R5 key implementation to the accepted full preflight."""
import argparse
import hashlib
import importlib.util
import json
import os
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parents[1]
ROLLOUT_ROOT = pathlib.Path(r"C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-live-rollout-20260913")
R5 = ROOT / "scripts/auto-switch-candidate-key-r5-20260913.py"
R5_TEST = ROOT / "scripts/test-auto-switch-candidate-key-r5-20260913.py"
R5_CONTRACT = ROOT / "docs/auto-switch-candidate-key-r5-contract-20260913.md"
PREFLIGHT = ROOT / "scripts/auto-switch-candidate-key-r5-preflight-r4-20260913.py"
PREFLIGHT_TEST = ROOT / "scripts/test-auto-switch-candidate-key-r5-preflight-r4-20260913.py"
PREFLIGHT_CONTRACT = ROOT / "docs/auto-switch-candidate-key-r5-preflight-r4-contract-20260913.md"
PREFLIGHT_REVIEW = ROLLOUT_ROOT / "docs/auto-switch-candidate-key-r5-preflight-r4-review-20260913.md"
PREFLIGHT_PINS = ROLLOUT_ROOT / "docs/auto-switch-candidate-key-r5-preflight-r4-reviewed-pins-20260913.json"
PREFLIGHT_RESULT = ROOT / "docs/auto-switch-candidate-key-r5-preflight-result-r4-20260913.json"
PREFLIGHT_EVIDENCE = ROLLOUT_ROOT / "docs/auto-switch-candidate-key-r5-preflight-r4-evidence-review-20260913.md"
TEST = ROOT / "scripts/test-auto-switch-candidate-key-r5-bound-20260913.py"
CONTRACT = ROOT / "docs/auto-switch-candidate-key-r5-bound-contract-20260913.md"
RESULT = ROOT / "docs/auto-switch-candidate-key-r5-bound-result-20260913.json"

R5_SHA256 = "191913463849c7c42ae2e52126f73825b21bc661b6e88bfe6a799ed656f19273"
R5_TEST_SHA256 = "656ee0a395393d08bf1a3fcf798fcf4a6c13611a3dccc251d38d1ba934a04fbe"
R5_CONTRACT_SHA256 = "5bb65014f5fb43065275206de455872fc77720084106d6b625be8db03195a7c0"
PREFLIGHT_SHA256 = "53b55d5b751c8f0e231c8260baa3c286bc2eeeb083ff35ce05452a1eddead55e"
PREFLIGHT_TEST_SHA256 = "6c79d8a83483ccb13460473d12fffd42d2b0c44fa368db1627799e849a0444fc"
PREFLIGHT_CONTRACT_SHA256 = "80cbfa23c0cf385b1562b4f4e0faf4c805fd8841050b38854e36c3598f2293d1"
PREFLIGHT_REVIEW_SHA256 = "7036b2a2d51e40efe70a8faf53bd6a97815d40f8706157a50d134e347446276b"
PREFLIGHT_PINS_SHA256 = "2ad6136cbf093974a8385fa94589d63f7dae745b6a36012e0800c82ffb3c0846"
PREFLIGHT_RESULT_SHA256 = "8cdae537781844cc91174f810b2c5933ce1bd1c53a0fb175831a7cfaf6ca3b61"
PREFLIGHT_EVIDENCE_SHA256 = "006c053817d621864e3db61837408dd405eae1f79536c621f97fbd8878900fa1"
SCHEMA = "auto-switch-candidate-key-r5-bound-result/v1"
REVIEW_SCHEMA = "auto-switch-candidate-key-r5-bound-review/v1"
RESULT_LIMIT = 32768
EMPTY_SHA256 = hashlib.sha256(b"").hexdigest()


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
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


def fixed_dependencies():
    return (
        (R5, R5_SHA256), (R5_TEST, R5_TEST_SHA256), (R5_CONTRACT, R5_CONTRACT_SHA256),
        (PREFLIGHT, PREFLIGHT_SHA256), (PREFLIGHT_TEST, PREFLIGHT_TEST_SHA256),
        (PREFLIGHT_CONTRACT, PREFLIGHT_CONTRACT_SHA256), (PREFLIGHT_REVIEW, PREFLIGHT_REVIEW_SHA256),
        (PREFLIGHT_PINS, PREFLIGHT_PINS_SHA256), (PREFLIGHT_RESULT, PREFLIGHT_RESULT_SHA256),
        (PREFLIGHT_EVIDENCE, PREFLIGHT_EVIDENCE_SHA256),
    )


def validate_preflight_receipt(value, preflight, r5):
    r3 = preflight.load(preflight.R3, preflight.R3_SHA256, "candidate_key_r5_bound_r3")
    try:
        value = preflight.validate_receipt(value, r3, r5)
    except Exception as error:
        raise Stop("local_validation") from error
    remote = value["remote"]
    if (value["status"] != "PASS" or value["stage"] != "complete" or remote["candidate_id"] != r5.CANDIDATE_ID
            or set(remote["checks"]) != set(r5.PREFLIGHT_CHECKS) or not all(remote["checks"].values())):
        raise Stop("local_validation")
    return value


def review_payload():
    r5 = load(R5, R5_SHA256, "candidate_key_r5_bound_review_r5")
    preflight = load(PREFLIGHT, PREFLIGHT_SHA256, "candidate_key_r5_bound_review_preflight")
    return {
        "schema": REVIEW_SCHEMA, "execution_ready": True, "operation": "candidate_key_r5_create",
        "candidate_id": r5.CANDIDATE_ID, "key_name": r5.KEY_NAME, "operator_store": r5.OPERATOR_STORE,
        "models": r5.MODELS, "connections": r5.CONNECTIONS, "r5_preparation": r5.review_payload(),
        "preflight_review": preflight.review_payload(), "preflight_result_sha256": digest(PREFLIGHT_RESULT),
        "preflight_evidence_sha256": digest(PREFLIGHT_EVIDENCE), "launcher_sha256": digest(__file__),
        "test_sha256": digest(TEST), "contract_sha256": digest(CONTRACT), "result": str(RESULT),
    }


def transport_meta(returncode=None, stdout=None, stderr=None, category="bounded_capture_unknown"):
    def item(value):
        return None if value is None else {"bytes": len(value), "sha256": hashlib.sha256(value).hexdigest()}
    return {"category": category, "returncode": returncode, "stdout": item(stdout), "stderr": item(stderr)}


def child_receipt(returncode, stdout, stderr, r5):
    meta = transport_meta(returncode, stdout, stderr, "returned")
    if stderr:
        meta["category"] = "child_stderr"
        return {"schema": SCHEMA, "status": "UNKNOWN", "stage": "transport", "transport": meta, "remote": None}
    try:
        remote = r5.validate_result(json.loads(stdout), returncode)
    except Exception:
        meta["category"] = "remote_envelope"
        return {"schema": SCHEMA, "status": "UNKNOWN", "stage": "remote_validation", "transport": meta, "remote": None}
    status = "PASS" if returncode == 0 else "UNKNOWN" if remote["status"] == "CANDIDATE_KEY_R5_UNKNOWN" else "STOP"
    return {"schema": SCHEMA, "status": status, "stage": "complete" if status == "PASS" else remote["stage"],
            "transport": meta, "remote": remote}


def validate_receipt(value, r5):
    if not isinstance(value, dict) or set(value) != {"schema", "status", "stage", "transport", "remote"} or value["schema"] != SCHEMA:
        raise Stop("result_validation")
    meta = value["transport"]
    if not isinstance(meta, dict) or set(meta) != {"category", "returncode", "stdout", "stderr"}:
        raise Stop("result_validation")
    if meta["category"] not in {"bounded_capture_unknown", "returned", "child_stderr", "remote_envelope"}:
        raise Stop("result_validation")
    for name, limit in (("stdout", 1048576), ("stderr", 65536)):
        item = meta[name]
        if item is not None and (not isinstance(item, dict) or set(item) != {"bytes", "sha256"}
                or type(item["bytes"]) is not int or not 0 <= item["bytes"] <= limit
                or not isinstance(item["sha256"], str) or not re.fullmatch(r"[0-9a-f]{64}", item["sha256"])):
            raise Stop("result_validation")
    if value["remote"] is not None:
        if (meta["category"] != "returned" or meta["returncode"] not in (0, 1, 2)
                or meta["stdout"] is None or meta["stdout"]["bytes"] == 0
                or meta["stderr"] != {"bytes": 0, "sha256": EMPTY_SHA256}):
            raise Stop("result_validation")
        try:
            remote = r5.validate_result(value["remote"], meta["returncode"])
        except Exception as error:
            raise Stop("result_validation") from error
        expected = "PASS" if meta["returncode"] == 0 else "UNKNOWN" if remote["status"] == "CANDIDATE_KEY_R5_UNKNOWN" else "STOP"
        if value["status"] != expected or value["stage"] != ("complete" if expected == "PASS" else remote["stage"]):
            raise Stop("result_validation")
    else:
        if value["status"] != "UNKNOWN" or value["stage"] not in {"transport", "remote_validation"}:
            raise Stop("result_validation")
        expected = {
            "bounded_capture_unknown": meta["returncode"] is None and meta["stdout"] is None and meta["stderr"] is None and value["stage"] == "transport",
            "child_stderr": isinstance(meta["returncode"], int) and meta["stdout"] is not None and meta["stderr"] is not None and meta["stderr"]["bytes"] > 0 and value["stage"] == "transport",
            "remote_envelope": isinstance(meta["returncode"], int) and meta["stdout"] is not None and meta["stderr"] == {"bytes": 0, "sha256": EMPTY_SHA256} and value["stage"] == "remote_validation",
        }.get(meta["category"], False)
        if not expected:
            raise Stop("result_validation")
    return value


def reserve_result():
    if RESULT.exists() or RESULT.is_symlink():
        raise Stop("stale_result")
    return os.open(RESULT, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0), 0o600)


def finish(fd, value):
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()
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
    if not all(regular(path) and digest(path) == expected for path, expected in fixed_dependencies()):
        raise Stop("local_validation")
    if not regular(reviewed) or json.loads(reviewed.read_text("utf-8")) != review_payload():
        raise Stop("review_pin_mismatch")
    r5 = load(R5, R5_SHA256, "candidate_key_r5_bound_execute_r5")
    preflight = load(PREFLIGHT, PREFLIGHT_SHA256, "candidate_key_r5_bound_execute_preflight")
    validate_preflight_receipt(json.loads(PREFLIGHT_RESULT.read_text("utf-8")), preflight, r5)
    if not all(r5.regular(path) and r5.digest(path) == expected for path, expected in r5.fixed_dependencies()):
        raise Stop("local_validation")
    r5.validate_reconciliation(r5.parse_receipt(r5.RECONCILIATION_RESULT), r5.CANDIDATE_ID)
    if r5.RESULT.exists() or r5.RESULT.is_symlink() or not os.environ.get("PROGRAMDATA") or os.environ.get("PYTHONOPTIMIZE") is not None:
        raise Stop("local_validation")
    admin = os.environ.get("OMNIROUTE_ADMIN_TOKEN", "")
    if not re.fullmatch(r"oma_[A-Za-z0-9._~-]{16,512}", admin):
        raise Stop("local_validation")
    payload = r5.render_remote(admin)
    transport = r5.load_transport()
    fd = reserve_result()
    receipt = {"schema": SCHEMA, "status": "UNKNOWN", "stage": "transport",
               "transport": transport_meta(), "remote": None}
    try:
        command = [transport.SSH, "-T", *transport.options("192.168.1.68"), "belladmin@192.168.1.68", "sudo -n python3 -"]
        saved = os.environ.pop("OMNIROUTE_ADMIN_TOKEN", None)
        try:
            returncode, stdout, stderr = transport.bounded_capture(command, payload, 300)
        finally:
            payload = b""
            if saved is not None:
                os.environ["OMNIROUTE_ADMIN_TOKEN"] = saved
        receipt = child_receipt(returncode, stdout, stderr, r5)
        validate_receipt(receipt, r5)
        return 0 if receipt["status"] == "PASS" else 1 if receipt["status"] == "STOP" else 2
    except Exception:
        return 2
    finally:
        finish(fd, receipt)


def self_check():
    if not all(regular(path) and digest(path) == expected for path, expected in fixed_dependencies()):
        raise Stop("local_validation")
    if RESULT.exists() or RESULT.is_symlink():
        raise Stop("stale_result")
    r5 = load(R5, R5_SHA256, "candidate_key_r5_bound_check_r5")
    preflight = load(PREFLIGHT, PREFLIGHT_SHA256, "candidate_key_r5_bound_check_preflight")
    validate_preflight_receipt(json.loads(PREFLIGHT_RESULT.read_text("utf-8")), preflight, r5)
    secret = "oma_fixture_candidate_key_r5_bound"; node = r5.render_node(secret); payload = r5.render_remote(secret)
    if (secret.encode() in payload or node.count("stage='create';r=await request('POST','/api/keys'") != 1
            or node.count("stage='patch';r=await request('PATCH','/api/keys/'+keyId,PATCH)") != 1):
        raise Stop("local_validation")
    print("CANDIDATE_KEY_R5_BOUND_PREPARATION_PASS")


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
        print(json.dumps({"status": "CANDIDATE_KEY_R5_BOUND_NOT_EXECUTED", "stage": stage}, sort_keys=True))
        raise SystemExit(1)
