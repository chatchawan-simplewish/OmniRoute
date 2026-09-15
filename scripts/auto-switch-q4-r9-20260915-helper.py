"""Remote-side, no-retry Q4 R9 state transition. Runtime is supplied by the sole executor."""
import hashlib
import json
import os
import pathlib


HASH_FIELDS = ("launcher_sha256", "helper_sha256", "contract_sha256", "test_sha256")


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


def _validate(request):
    action, approval, manifest = request.get("action"), request.get("approval"), request.get("source_manifest")
    if request.get("schema") != "auto-switch-q4-r9-request/v1" or not isinstance(action, dict): raise ValueError("bad request")
    if action.get("schema") != "auto-switch-q4-r9-action/v1" or action.get("source_manifest") != manifest: raise ValueError("action drift")
    if approval.get("verdict") != "PASS" or approval.get("model") != "gpt-5.6-sol" or approval.get("effort") != "high": raise ValueError("approval")
    if approval.get("reviewed_payload_sha256") != hashlib.sha256(json.dumps(action, sort_keys=True, separators=(",", ":")).encode()).hexdigest():
        raise ValueError("payload drift")
    if any(approval.get(field) != manifest.get(field) for field in HASH_FIELDS): raise ValueError("source drift")
    leaves = (action.get("state_leaf"), action.get("terminal_leaf"))
    if any(not isinstance(leaf, str) or pathlib.Path(leaf).name != leaf or not leaf.startswith("q4-r9-") for leaf in leaves): raise ValueError("unsafe leaf")
    return action


def execute(request, runtime, secret_path):
    action = _validate(request)
    root = pathlib.Path(secret_path).parent
    state, terminal = (root / action["state_leaf"], root / action["terminal_leaf"])
    if state.exists() or terminal.exists(): raise FileExistsError("spent or occupied")
    _write_new(state, {"schema": "auto-switch-q4-r9-state/v1", "status": "Q4_R9_UNKNOWN", "gate_spent": True})
    secret = pathlib.Path(secret_path).read_bytes().rstrip(b"\n")
    runtime.start()
    try:
        evidence = runtime.authenticate(secret)
        passed = all(evidence.get(field) == 200 for field in ("health_http_status", "models_http_status", "completion_http_status"))
        passed = passed and evidence.get("selected_q4") is True and evidence.get("content_valid") is True
    except Exception:
        return 1
    finally:
        stopped = runtime.stop()
    passed = passed and stopped is True
    if not passed: return 1
    _write_new(terminal, {"schema": "auto-switch-q4-r9-terminal/v1", "status": "Q4_R9_PASS", "gate_spent": True,
                          "request_id": evidence.get("request_id"), "candidate_stopped_retained": True})
    return 0
