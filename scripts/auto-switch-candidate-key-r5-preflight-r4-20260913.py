"""Fresh receipt owner for the frozen ordered R5 read-only preflight."""
import argparse
import hashlib
import importlib.util
import json
import os
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parents[1]
ROLLOUT_ROOT = pathlib.Path(r"C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-live-rollout-20260913")
COORDINATOR_ROOT = pathlib.Path(r"C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-auto-switch-20260912")
R3 = ROOT / "scripts/auto-switch-candidate-key-r5-preflight-r3-20260913.py"
R3_TEST = ROOT / "scripts/test-auto-switch-candidate-key-r5-preflight-r3-20260913.py"
R3_CONTRACT = ROOT / "docs/auto-switch-candidate-key-r5-preflight-r3-contract-20260913.md"
R3_RESULT = ROOT / "docs/auto-switch-candidate-key-r5-preflight-result-r3-20260913.json"
R3_EVIDENCE = ROLLOUT_ROOT / "docs/auto-switch-candidate-key-r5-preflight-r3-evidence-review-20260913.md"
RECONCILE = ROOT / "scripts/auto-switch-candidate-codex-reconcile-r1-20260913.py"
RECONCILE_TEST = ROOT / "scripts/test-auto-switch-candidate-codex-reconcile-r1-20260913.py"
RECONCILE_CONTRACT = ROOT / "docs/auto-switch-candidate-codex-reconcile-r1-contract-20260913.md"
RECONCILE_REVIEW = ROLLOUT_ROOT / "docs/auto-switch-candidate-codex-reconcile-r1-review-20260913.md"
RECONCILE_PINS = ROLLOUT_ROOT / "docs/auto-switch-candidate-codex-reconcile-r1-reviewed-pins-20260913.json"
RECONCILE_RESULT = ROOT / "docs/auto-switch-candidate-codex-reconcile-r1-result-20260913.json"
RECONCILE_EVIDENCE = ROLLOUT_ROOT / "docs/auto-switch-candidate-codex-reconcile-r1-evidence-review-20260913.md"
TRANSPORT = COORDINATOR_ROOT / "scripts/auto-switch-image-transfer-r3-20260913.py"
TEST = ROOT / "scripts/test-auto-switch-candidate-key-r5-preflight-r4-20260913.py"
CONTRACT = ROOT / "docs/auto-switch-candidate-key-r5-preflight-r4-contract-20260913.md"
RESULT = ROOT / "docs/auto-switch-candidate-key-r5-preflight-result-r4-20260913.json"

R3_SHA256 = "988aef23a7ff17fb2c5e7706c1635151b76efc0700e5e7a55c4dd83356eeb813"
R3_TEST_SHA256 = "e48c77c904e09f5052eb7c2dc124bd046fc63a6dfe82d2c129090bfb6d45994d"
R3_CONTRACT_SHA256 = "2034bdf77c9f87ce02b4dfce4930e9cce0fa7fd5ef8e8c682ee13d695fdde753"
R3_RESULT_SHA256 = "d34341199d8b832b449884a943f6dd6d780c2d3be0afcac17c59afa5b9fa4695"
R3_EVIDENCE_SHA256 = "de9a9aa6dccf3522998682443a6f81a55f3461beddd8a0839c2d888f485f499f"
RECONCILE_SHA256 = "f614b5f2c91cbe083bb76d8344781bea3600fcbf1a3bc8a298137c84d56f161f"
RECONCILE_TEST_SHA256 = "3a1207d86192599ee4cf57736481e92c854892cc80d025ae274f1d413e716c58"
RECONCILE_CONTRACT_SHA256 = "58312a9b74e0b96bbc0b47e7a00f88a84b36dc1ae399570819767a246059db2a"
RECONCILE_REVIEW_SHA256 = "e4ab53fa77a66dd397b0ba4be1db10aa05f2d2bb2f6bc0a9a767780388933141"
RECONCILE_PINS_SHA256 = "77f514b08ea698c841ee6818a663a7d42f06d1af4cf729a931d17ac3f86811ae"
RECONCILE_RESULT_SHA256 = "fdcbc3cb1a050870d0643cd9df444fdbdb7b5f836046fb910b70492fb6ea0157"
RECONCILE_EVIDENCE_SHA256 = "ad73e14a71402b456f4d1ec28fd5c24c87ab759000f3b75e45c897ff0ef64cd3"
TRANSPORT_SHA256 = "78bb97e57d6229aae84c2f0d0caaf68eeb71ba6b92e69415d83af2a869b8224a"
CANDIDATE_ID = "9468859edcdb483c53900edde14d301a162cccc791079154677e913f39bf26a3"
VM1205 = "192.168.1.68"
SCHEMA = "auto-switch-candidate-key-r5-preflight-r4-result/v1"
REVIEW_SCHEMA = "auto-switch-candidate-key-r5-preflight-r4-review/v1"
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
        (R3, R3_SHA256), (R3_TEST, R3_TEST_SHA256), (R3_CONTRACT, R3_CONTRACT_SHA256),
        (R3_RESULT, R3_RESULT_SHA256), (R3_EVIDENCE, R3_EVIDENCE_SHA256),
        (RECONCILE, RECONCILE_SHA256), (RECONCILE_TEST, RECONCILE_TEST_SHA256),
        (RECONCILE_CONTRACT, RECONCILE_CONTRACT_SHA256), (RECONCILE_REVIEW, RECONCILE_REVIEW_SHA256),
        (RECONCILE_PINS, RECONCILE_PINS_SHA256), (RECONCILE_RESULT, RECONCILE_RESULT_SHA256),
        (RECONCILE_EVIDENCE, RECONCILE_EVIDENCE_SHA256), (TRANSPORT, TRANSPORT_SHA256),
    )


def validate_current_reconcile(value, reconcile):
    if not isinstance(value, dict) or set(value) != {"schema", "status", "stage", "transport", "remote"}:
        raise Stop("local_validation")
    transport = value["transport"]
    if (value["schema"] != reconcile.SCHEMA or value["status"] != "PASS" or value["stage"] != "complete"
            or not isinstance(transport, dict) or set(transport) != {"category", "returncode", "stdout", "stderr"}
            or transport["category"] != "returned" or transport["returncode"] != 0):
        raise Stop("local_validation")
    for label, limit in (("stdout", RESULT_LIMIT), ("stderr", RESULT_LIMIT)):
        item = transport[label]
        if (not isinstance(item, dict) or set(item) != {"bytes", "sha256"}
                or type(item["bytes"]) is not int or not 0 <= item["bytes"] <= limit
                or not isinstance(item["sha256"], str) or not re.fullmatch(r"[0-9a-f]{64}", item["sha256"])):
            raise Stop("local_validation")
    if transport["stderr"] != {"bytes": 0, "sha256": EMPTY_SHA256} or transport["stdout"]["bytes"] == 0:
        raise Stop("local_validation")
    try:
        remote = reconcile.validate_remote(value["remote"], 0)
    except Exception as error:
        raise Stop("local_validation") from error
    if (remote["candidate_id"] != CANDIDATE_ID or remote["candidate_running"] is not True
            or remote["candidate_healthy"] is not True or remote["network_none"] is not True
            or remote["isolation_verified"] is not True or remote["live_unchanged"] is not True
            or remote["retained_unchanged"] is not True or remote["provider"] != "codex"
            or remote["is_active"] is not False or remote["get_http_status"] != 200):
        raise Stop("local_validation")
    return value


def review_payload():
    r3 = load(R3, R3_SHA256, "candidate_key_preflight_r4_review")
    return {
        "schema": REVIEW_SCHEMA, "execution_ready": True, "candidate_id": CANDIDATE_ID,
        "request_method": "GET", "request_paths": r3.review_payload()["request_paths"],
        "ordered_r3": r3.review_payload(), "r3_result_sha256": digest(R3_RESULT),
        "r3_evidence_sha256": digest(R3_EVIDENCE), "reconcile_sha256": digest(RECONCILE),
        "reconcile_test_sha256": digest(RECONCILE_TEST), "reconcile_contract_sha256": digest(RECONCILE_CONTRACT),
        "reconcile_review_sha256": digest(RECONCILE_REVIEW), "reconcile_pins_sha256": digest(RECONCILE_PINS),
        "reconcile_result_sha256": digest(RECONCILE_RESULT), "reconcile_evidence_sha256": digest(RECONCILE_EVIDENCE),
        "transport_sha256": digest(TRANSPORT), "launcher_sha256": digest(__file__),
        "test_sha256": digest(TEST), "contract_sha256": digest(CONTRACT), "result": str(RESULT),
    }


def transport_meta(returncode=None, stdout=None, stderr=None, category="bounded_capture_unknown"):
    def item(value):
        return None if value is None else {"bytes": len(value), "sha256": hashlib.sha256(value).hexdigest()}
    return {"category": category, "returncode": returncode, "stdout": item(stdout), "stderr": item(stderr)}


def child_receipt(returncode, stdout, stderr, r3, r5):
    meta = transport_meta(returncode, stdout, stderr, "returned")
    if stderr:
        meta["category"] = "child_stderr"
        return {"schema": SCHEMA, "status": "UNKNOWN", "stage": "transport", "transport": meta, "remote": None}
    try:
        remote = json.loads(stdout)
        remote = r3.validate_remote(remote, returncode, r5)
    except Exception:
        meta["category"] = "remote_envelope"
        return {"schema": SCHEMA, "status": "UNKNOWN", "stage": "remote_validation", "transport": meta, "remote": None}
    status = "PASS" if returncode == 0 else "STOP"
    return {"schema": SCHEMA, "status": status, "stage": "complete" if status == "PASS" else remote["stage"],
            "transport": meta, "remote": remote}


def validate_receipt(value, r3, r5):
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
    if value["status"] in {"PASS", "STOP"}:
        if (meta["category"] != "returned" or meta["returncode"] not in (0, 1)
                or meta["stdout"] is None or meta["stdout"]["bytes"] == 0
                or meta["stderr"] != {"bytes": 0, "sha256": EMPTY_SHA256}
                or not isinstance(value["remote"], dict)):
            raise Stop("result_validation")
        try:
            remote = r3.validate_remote(value["remote"], meta["returncode"], r5)
        except Exception as error:
            raise Stop("result_validation") from error
        if value["status"] != ("PASS" if meta["returncode"] == 0 else "STOP") or value["stage"] != ("complete" if meta["returncode"] == 0 else remote["stage"]):
            raise Stop("result_validation")
    else:
        if value["status"] != "UNKNOWN" or value["remote"] is not None or value["stage"] not in {"transport", "remote_validation"}:
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
    reconcile = load(RECONCILE, RECONCILE_SHA256, "candidate_key_preflight_r4_reconcile")
    validate_current_reconcile(json.loads(RECONCILE_RESULT.read_text("utf-8")), reconcile)
    if not os.environ.get("PROGRAMDATA") or os.environ.get("PYTHONOPTIMIZE") is not None:
        raise Stop("local_validation")
    admin = os.environ.get("OMNIROUTE_ADMIN_TOKEN", "")
    if not re.fullmatch(r"oma_[A-Za-z0-9._~-]{16,512}", admin):
        raise Stop("local_validation")
    r3 = load(R3, R3_SHA256, "candidate_key_preflight_r4_execute")
    r5 = r3.load(r3.R5, r3.R5_SHA256, "candidate_key_preflight_r4_r5")
    transport = load(TRANSPORT, TRANSPORT_SHA256, "candidate_key_preflight_r4_transport")
    payload = r3.render_remote(admin)
    fd = reserve_result()
    receipt = {"schema": SCHEMA, "status": "UNKNOWN", "stage": "transport",
               "transport": transport_meta(), "remote": None}
    try:
        command = [transport.SSH, "-T", *transport.options(VM1205), "belladmin@" + VM1205, "sudo -n python3 -"]
        saved = os.environ.pop("OMNIROUTE_ADMIN_TOKEN", None)
        try:
            returncode, stdout, stderr = transport.bounded_capture(command, payload, 180)
        finally:
            payload = b""
            if saved is not None:
                os.environ["OMNIROUTE_ADMIN_TOKEN"] = saved
        receipt = child_receipt(returncode, stdout, stderr, r3, r5)
        validate_receipt(receipt, r3, r5)
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
    reconcile = load(RECONCILE, RECONCILE_SHA256, "candidate_key_preflight_r4_check_reconcile")
    validate_current_reconcile(json.loads(RECONCILE_RESULT.read_text("utf-8")), reconcile)
    r3 = load(R3, R3_SHA256, "candidate_key_preflight_r4_check")
    payload = r3.render_remote("oma_fixture_preflight_r4_secret")
    if b"oma_fixture_preflight_r4_secret" in payload or payload.count(b"/api/keys") != 1 or payload.count(b"/api/combos") != 1 or payload.count(b"/api/providers/") != 1:
        raise Stop("local_validation")
    print("CANDIDATE_KEY_R5_PREFLIGHT_R4_PREPARATION_PASS")


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
        print(json.dumps({"status": "CANDIDATE_KEY_R5_PREFLIGHT_R4_NOT_EXECUTED", "stage": stage}, sort_keys=True))
        raise SystemExit(1)
