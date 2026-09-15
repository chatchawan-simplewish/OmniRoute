"""Remote-side, no-retry Q4 R9 state transition. Runtime is supplied by the sole executor."""
import hashlib
import json
import os
import pathlib


HASH_FIELDS = ("launcher_sha256", "helper_sha256", "contract_sha256", "test_sha256")
MANIFEST_KEYS = {"schema", *HASH_FIELDS}
ACTION_KEYS = {"schema", "source_manifest", "runtime", "state_leaf", "terminal_leaf"}
APPROVAL_KEYS = {"schema", "verdict", "model", "effort", "reviewed_payload_sha256", *HASH_FIELDS}
REQUEST_KEYS = {"schema", "action", "approval", "source_manifest", "source_bundle", "action_bytes", "approval_bytes"}
RUNTIME_KEYS = {"schema", "host", "candidate_id", "image_sha256", "command_sha256", "collector_sha256", "endpoint", "model", "connection_id", "request_sha256", "runtime_sha256"}


def _digest(value):
    return isinstance(value, str) and len(value) == 64 and all(char in "0123456789abcdef" for char in value)


def _write_new(path, value):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(fd, "wb", closefd=False) as handle:
            handle.write(json.dumps(value, sort_keys=True, separators=(",", ":")).encode())
            handle.flush(); os.fsync(handle.fileno())
    finally:
        os.close(fd)
    if os.name != "nt":
        directory = os.open(path.parent, os.O_RDONLY)
        try: os.fsync(directory)
        finally: os.close(directory)


def _validate(request, runtime):
    action, approval, manifest = request.get("action"), request.get("approval"), request.get("source_manifest")
    bundle = request.get("source_bundle")
    if not isinstance(request, dict) or set(request) != REQUEST_KEYS or request.get("schema") != "auto-switch-q4-r9-request/v1": raise ValueError("bad request")
    if not all(isinstance(value, dict) for value in (action, approval, manifest)) or set(manifest) != MANIFEST_KEYS or set(action) != ACTION_KEYS or set(approval) != APPROVAL_KEYS:
        raise ValueError("schema drift")
    if request["action_bytes"] != json.dumps(action, sort_keys=True, separators=(",", ":")).encode() or request["approval_bytes"] != json.dumps(approval, sort_keys=True, separators=(",", ":")).encode(): raise ValueError("noncanonical input")
    if not isinstance(bundle, dict) or set(bundle) != {"launcher", "helper", "contract", "test"} or not all(isinstance(value, bytes) for value in bundle.values()): raise ValueError("source bundle")
    if any(hashlib.sha256(bundle[name]).hexdigest() != manifest[field] for name, field in zip(("launcher", "helper", "contract", "test"), HASH_FIELDS)): raise ValueError("source drift")
    if action.get("schema") != "auto-switch-q4-r9-action/v1" or action.get("source_manifest") != manifest: raise ValueError("action drift")
    if approval.get("schema") != "auto-switch-q4-r9-approval/v1" or approval.get("verdict") != "PASS" or approval.get("model") != "gpt-5.6-sol" or approval.get("effort") != "high": raise ValueError("approval")
    if approval.get("reviewed_payload_sha256") != hashlib.sha256(request["action_bytes"]).hexdigest():
        raise ValueError("payload drift")
    if any(approval.get(field) != manifest.get(field) for field in HASH_FIELDS): raise ValueError("source drift")
    leaves = (action.get("state_leaf"), action.get("terminal_leaf"))
    if leaves[0] == leaves[1] or any(not isinstance(leaf, str) or pathlib.Path(leaf).name != leaf or not leaf.startswith("q4-r9-") for leaf in leaves): raise ValueError("unsafe leaf")
    if not isinstance(action["runtime"], dict) or set(action["runtime"]) != RUNTIME_KEYS or action["runtime"].get("schema") != "auto-switch-q4-r9-runtime/v1": raise ValueError("runtime schema")
    if not all(isinstance(action["runtime"][field], str) and action["runtime"][field] for field in ("host", "endpoint", "model", "connection_id")) or not all(_digest(action["runtime"][field]) for field in ("candidate_id", "image_sha256", "command_sha256", "collector_sha256", "request_sha256", "runtime_sha256")): raise ValueError("runtime pins")
    if runtime.snapshot() != action["runtime"] or hashlib.sha256(runtime.source_bytes()).hexdigest() != action["runtime"]["runtime_sha256"]: raise ValueError("runtime drift")
    return action


def execute(request, runtime, secret_path):
    action = _validate(request, runtime)
    root = pathlib.Path(secret_path).parent
    state, terminal = (root / action["state_leaf"], root / action["terminal_leaf"])
    if state.exists() or terminal.exists(): raise FileExistsError("spent or occupied")
    _write_new(state, {"schema": "auto-switch-q4-r9-state/v1", "status": "Q4_R9_UNKNOWN", "gate_spent": True})
    secret = pathlib.Path(secret_path).read_bytes().rstrip(b"\n")
    evidence = None
    try:
        runtime.start()
        evidence = runtime.authenticate(secret, action)
        completion = evidence["completion"]
        passed = set(evidence) == {"schema", "runtime", "collector_sha256", "health", "models", "completion"}
        passed = passed and evidence["schema"] == "auto-switch-q4-r9-evidence/v1" and evidence["runtime"] == action["runtime"] and evidence["collector_sha256"] == action["runtime"]["collector_sha256"]
        passed = passed and evidence["health"] == {"status": 200, "candidate_id": action["runtime"]["candidate_id"]}
        passed = passed and evidence["models"] == {"status": 200, "candidate_id": action["runtime"]["candidate_id"], "model": action["runtime"]["model"]}
        passed = passed and set(completion) == {"status", "candidate_id", "model", "connection_id", "request_count", "request_id", "content_bytes"}
        passed = passed and completion["status"] == 200 and completion["candidate_id"] == action["runtime"]["candidate_id"] and completion["model"] == action["runtime"]["model"] and completion["connection_id"] == action["runtime"]["connection_id"] and completion["request_count"] == 1 and isinstance(completion["request_id"], str) and bool(completion["request_id"]) and isinstance(completion["content_bytes"], int) and completion["content_bytes"] > 0
    except Exception:
        return 1
    finally:
        stopped = runtime.stop()
    passed = passed and stopped is True
    if not passed: return 1
    _write_new(terminal, {"schema": "auto-switch-q4-r9-terminal/v1", "status": "Q4_R9_PASS", "gate_spent": True,
                          "request_id": evidence["completion"]["request_id"], "candidate_stopped_retained": True})
    return 0
