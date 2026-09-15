"""POSIX-only Q4 R9 execution from retained reviewed byte bundles."""
import hashlib
import json
import os
import pathlib
import stat
import subprocess
import sys
import uuid


HASH_FIELDS = ("launcher_sha256", "helper_sha256", "contract_sha256", "test_sha256",
               "runtime_sha256", "command_sha256", "collector_sha256", "request_sha256")
MANIFEST_KEYS = {"schema", *HASH_FIELDS}
ACTION_KEYS = {"schema", "source_manifest", "runtime", "credential", "state_leaf", "terminal_leaf"}
APPROVAL_KEYS = {"schema", "verdict", "model", "effort", "reviewed_payload_sha256", *HASH_FIELDS}
REQUEST_KEYS = {"schema", "action", "approval", "source_manifest", "source_bundle", "operation_bundle", "action_bytes", "approval_bytes"}
RUNTIME_KEYS = {"schema", "host", "candidate_id", "image_sha256", "endpoint", "model", "connection_id",
                "runtime_sha256", "command_sha256", "collector_sha256", "request_sha256",
                "start_timeout_ms", "collect_timeout_ms", "stop_timeout_ms"}
CREDENTIAL_KEYS = {"schema", "parent_device", "parent_inode", "parent_uid", "parent_gid", "parent_mode",
                   "secret_device", "secret_inode", "secret_uid", "secret_gid", "secret_mode", "secret_size",
                   "secret_mtime_ns", "secret_leaf"}
EXEC_SHIM = """import io,sys
raw=sys.stdin.buffer.read()
if len(raw)<8:raise SystemExit(125)
n=int.from_bytes(raw[:8],'big');source=raw[8:8+n];payload=raw[8+n:]
if len(source)!=n:raise SystemExit(125)
sys.stdin=io.TextIOWrapper(io.BytesIO(payload),encoding='utf-8')
exec(compile(source,'<retained-q4-r9-program>','exec'),{'__name__':'__main__','__file__':'<retained-q4-r9-program>'})
"""


def _digest(value):
    return isinstance(value, str) and len(value) == 64 and all(char in "0123456789abcdef" for char in value)


def _object(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError("duplicate key")
        value[key] = item
    return value


def _canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def _parse(raw):
    try:
        value = json.loads(raw, object_pairs_hook=_object)
    except Exception as error:
        raise ValueError("invalid json") from error
    if not isinstance(value, dict) or raw != _canonical(value):
        raise ValueError("noncanonical json")
    return value


def _pack(*values):
    return b"".join(len(value).to_bytes(8, "big") + value for value in values)


def _run_retained(source, mode, payload, timeout_ms, output_limit):
    if not isinstance(source, bytes) or not source or type(timeout_ms) is not int or not 1 <= timeout_ms <= 120000:
        raise ValueError("unsafe retained invocation")
    try:
        result = subprocess.run([sys.executable, "-I", "-c", EXEC_SHIM, mode], input=len(source).to_bytes(8, "big") + source + payload,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout_ms / 1000, check=False)
    except subprocess.TimeoutExpired as error:
        raise RuntimeError("bounded invocation uncertain") from error
    if len(result.stdout) > output_limit or len(result.stderr) > 4096:
        raise ValueError("bounded output exceeded")
    return result


def _validate(request):
    if not isinstance(request, dict) or set(request) != REQUEST_KEYS or request.get("schema") != "auto-switch-q4-r9-request/v2":
        raise ValueError("bad request")
    action, approval, manifest = request["action"], request["approval"], request["source_manifest"]
    sources, operations = request["source_bundle"], request["operation_bundle"]
    if not all(isinstance(value, dict) for value in (action, approval, manifest)) or set(manifest) != MANIFEST_KEYS or set(action) != ACTION_KEYS or set(approval) != APPROVAL_KEYS:
        raise ValueError("schema drift")
    if set(sources) != {"launcher", "helper", "contract", "test"} or set(operations) != {"runtime", "command", "collector", "request"}:
        raise ValueError("bundle schema")
    bundle = {**sources, **operations}
    if not all(isinstance(value, bytes) and value for value in bundle.values()):
        raise ValueError("bundle bytes")
    if manifest.get("schema") != "auto-switch-q4-r9-source/v2" or any(hashlib.sha256(bundle[field[:-7]]).hexdigest() != manifest[field] for field in HASH_FIELDS):
        raise ValueError("retained-byte drift")
    if request["action_bytes"] != _canonical(action) or request["approval_bytes"] != _canonical(approval):
        raise ValueError("noncanonical input")
    if action.get("schema") != "auto-switch-q4-r9-action/v2" or action.get("source_manifest") != manifest:
        raise ValueError("action drift")
    if (approval.get("schema"), approval.get("verdict"), approval.get("model"), approval.get("effort")) != ("auto-switch-q4-r9-approval/v2", "PASS", "gpt-5.6-sol", "high"):
        raise ValueError("approval")
    if approval.get("reviewed_payload_sha256") != hashlib.sha256(request["action_bytes"]).hexdigest() or any(approval.get(field) != manifest[field] for field in HASH_FIELDS):
        raise ValueError("approval drift")
    runtime, credential = action.get("runtime"), action.get("credential")
    if not isinstance(runtime, dict) or set(runtime) != RUNTIME_KEYS or runtime.get("schema") != "auto-switch-q4-r9-runtime/v2":
        raise ValueError("runtime schema")
    if not all(isinstance(runtime[field], str) and runtime[field] for field in ("host", "endpoint", "model", "connection_id")) or not all(_digest(runtime[field]) for field in ("candidate_id", "image_sha256", "runtime_sha256", "command_sha256", "collector_sha256", "request_sha256")):
        raise ValueError("runtime pins")
    if any(runtime[name + "_sha256"] != manifest[name + "_sha256"] for name in ("runtime", "command", "collector", "request")):
        raise ValueError("operation pins")
    if any(type(runtime[field]) is not int or not 1 <= runtime[field] <= 120000 for field in ("start_timeout_ms", "collect_timeout_ms", "stop_timeout_ms")):
        raise ValueError("timeout pins")
    if not isinstance(credential, dict) or set(credential) != CREDENTIAL_KEYS or credential.get("schema") != "auto-switch-q4-r9-credential/v1":
        raise ValueError("credential schema")
    if any(type(credential[field]) is not int or credential[field] < 0 for field in CREDENTIAL_KEYS - {"schema", "secret_leaf"}):
        raise ValueError("credential identity")
    if (credential["parent_uid"], credential["parent_gid"], credential["parent_mode"],
            credential["secret_uid"], credential["secret_gid"], credential["secret_mode"]) != (0, 0, 0o700, 0, 0, 0o600):
        raise ValueError("credential permissions")
    if not 1 <= credential["secret_size"] <= 4096:
        raise ValueError("credential size")
    leaves = (credential.get("secret_leaf"), action.get("state_leaf"), action.get("terminal_leaf"))
    if len(set(leaves)) != 3 or pathlib.Path(credential["secret_leaf"]).name != credential["secret_leaf"] or any(not isinstance(leaf, str) or pathlib.Path(leaf).name != leaf or not leaf.startswith("q4-r9-") for leaf in leaves[1:]):
        raise ValueError("unsafe leaf")
    return action


def _identity(parent, secret):
    return {"schema": "auto-switch-q4-r9-credential/v1",
            "parent_device": parent.st_dev, "parent_inode": parent.st_ino, "parent_uid": parent.st_uid,
            "parent_gid": parent.st_gid, "parent_mode": stat.S_IMODE(parent.st_mode),
            "secret_device": secret.st_dev, "secret_inode": secret.st_ino, "secret_uid": secret.st_uid,
            "secret_gid": secret.st_gid, "secret_mode": stat.S_IMODE(secret.st_mode), "secret_size": secret.st_size,
            "secret_mtime_ns": secret.st_mtime_ns}


def _open_credential(parent_path, secret_leaf):
    if os.name != "posix":
        raise OSError("Q4 R9 execution requires POSIX openat/O_NOFOLLOW semantics")
    parent_fd = os.open(parent_path, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC)
    secret_fd = None
    try:
        parent = os.fstat(parent_fd)
        secret_fd = os.open(secret_leaf, os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC, dir_fd=parent_fd)
        secret = os.fstat(secret_fd)
        if not stat.S_ISDIR(parent.st_mode) or not stat.S_ISREG(secret.st_mode):
            raise ValueError("unsafe credential objects")
        return parent_fd, secret_fd, {**_identity(parent, secret), "secret_leaf": secret_leaf}
    except Exception:
        if secret_fd is not None:
            os.close(secret_fd)
        os.close(parent_fd)
        raise


def _write_new(parent_fd, leaf, value):
    fd = os.open(leaf, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | os.O_CLOEXEC, 0o600, dir_fd=parent_fd)
    try:
        opened = os.fstat(fd)
        if not stat.S_ISREG(opened.st_mode) or opened.st_uid != 0 or opened.st_gid != 0 or stat.S_IMODE(opened.st_mode) != 0o600:
            raise ValueError("unsafe evidence leaf")
        raw = _canonical(value)
        with os.fdopen(fd, "wb", closefd=False) as handle:
            handle.write(raw); handle.flush(); os.fsync(fd)
    finally:
        os.close(fd)
    os.fsync(parent_fd)


def _exists(parent_fd, leaf):
    try:
        os.stat(leaf, dir_fd=parent_fd, follow_symlinks=False)
        return True
    except FileNotFoundError:
        return False


def _read_secret(secret_fd, credential):
    before = os.fstat(secret_fd)
    expected = credential["expected"]
    if (before.st_dev, before.st_ino, before.st_uid, before.st_gid, stat.S_IMODE(before.st_mode), before.st_size, before.st_mtime_ns) != (
            expected["secret_device"], expected["secret_inode"], expected["secret_uid"], expected["secret_gid"],
            expected["secret_mode"], expected["secret_size"], expected["secret_mtime_ns"]):
        raise ValueError("credential drift")
    secret = os.pread(secret_fd, 4097, 0)
    after = os.fstat(secret_fd)
    if len(secret) != expected["secret_size"] or any(char in secret for char in (b"\0", b"\r", b"\n")) or (
            before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns) != (
            after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns):
        raise ValueError("unsafe credential")
    return secret


def _validate_evidence(result, action):
    if result.returncode != 0 or result.stderr or not result.stdout:
        raise ValueError("collector failure")
    evidence = _parse(result.stdout)
    if set(evidence) != {"schema", "runtime", "health", "models", "completion"} or evidence["schema"] != "auto-switch-q4-r9-evidence/v1" or evidence["runtime"] != action["runtime"]:
        raise ValueError("evidence schema")
    runtime, completion = action["runtime"], evidence["completion"]
    if evidence["health"] != {"status": 200, "candidate_id": runtime["candidate_id"]} or evidence["models"] != {"status": 200, "candidate_id": runtime["candidate_id"], "model": runtime["model"]}:
        raise ValueError("readiness evidence")
    if not isinstance(completion, dict) or set(completion) != {"status", "candidate_id", "model", "connection_id", "request_count", "request_id", "content_bytes"}:
        raise ValueError("completion schema")
    expected = (200, runtime["candidate_id"], runtime["model"], runtime["connection_id"], 1)
    if (completion["status"], completion["candidate_id"], completion["model"], completion["connection_id"], completion["request_count"]) != expected:
        raise ValueError("completion drift")
    if type(completion["request_count"]) is not int or type(completion["content_bytes"]) is not int or completion["content_bytes"] <= 0 or not isinstance(completion["request_id"], str):
        raise ValueError("completion types")
    try:
        if uuid.UUID(completion["request_id"]).version != 4:
            raise ValueError("request id")
    except Exception as error:
        raise ValueError("request id") from error
    return evidence


def execute(request, secret_parent):
    action = _validate(request)
    parent_fd = secret_fd = None
    try:
        parent_fd, secret_fd, observed = _open_credential(secret_parent, action["credential"]["secret_leaf"])
        if observed != action["credential"]:
            raise ValueError("credential drift")
        if _exists(parent_fd, action["state_leaf"]) or _exists(parent_fd, action["terminal_leaf"]):
            raise FileExistsError("spent or occupied")
        _write_new(parent_fd, action["state_leaf"], {"schema": "auto-switch-q4-r9-state/v1", "status": "Q4_R9_UNKNOWN", "gate_spent": True})
        secret = _read_secret(secret_fd, {"expected": action["credential"]})
        operations, runtime = request["operation_bundle"], action["runtime"]
        passed = stopped = False
        evidence = evidence_raw = None
        try:
            start = _run_retained(operations["runtime"], "start", _pack(request["action_bytes"], operations["command"]), runtime["start_timeout_ms"], 0)
            if (start.returncode, start.stdout, start.stderr) != (0, b"", b""):
                return 1
            observed_result = _run_retained(operations["collector"], "collect", _pack(request["action_bytes"], operations["request"], secret), runtime["collect_timeout_ms"], 65536)
            evidence = _validate_evidence(observed_result, action); evidence_raw = observed_result.stdout
            passed = True
        except Exception:
            return 1
        finally:
            secret = b""
            try:
                stop = _run_retained(operations["runtime"], "stop", _pack(request["action_bytes"], operations["command"]), runtime["stop_timeout_ms"], 0)
                stopped = (stop.returncode, stop.stdout, stop.stderr) == (0, b"", b"")
            except Exception:
                stopped = False
        if not passed or not stopped:
            return 1
        _write_new(parent_fd, action["terminal_leaf"], {"schema": "auto-switch-q4-r9-terminal/v1", "status": "Q4_R9_PASS",
            "gate_spent": True, "request_id": evidence["completion"]["request_id"],
            "evidence_sha256": hashlib.sha256(evidence_raw).hexdigest(), "candidate_stopped_retained": True})
        return 0
    finally:
        if secret_fd is not None:
            os.close(secret_fd)
        if parent_fd is not None:
            os.close(parent_fd)
