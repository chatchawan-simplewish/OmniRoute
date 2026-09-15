"""Retained-byte approval and dispatch for the fresh Q4 R9 gate."""
import hashlib
import json
import os
import pathlib
import stat
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1] if not str(__file__).startswith("<retained-") else None
SELF = ROOT / "scripts" / "auto-switch-q4-r9-20260915.py" if ROOT else None
HELPER = ROOT / "scripts" / "auto-switch-q4-r9-20260915-helper.py" if ROOT else None
CONTRACT = ROOT / "docs" / "auto-switch-q4-r9-20260915-contract.md" if ROOT else None
TEST = ROOT / "scripts" / "auto-switch-q4-r9-20260915-test.py" if ROOT else None
SOURCE_NAMES = ("launcher", "helper", "contract", "test")
OPERATION_NAMES = ("runtime", "command", "collector", "request")
APPROVAL_HASH_FIELDS = tuple(name + "_sha256" for name in SOURCE_NAMES + OPERATION_NAMES)
MANIFEST_KEYS = {"schema", *APPROVAL_HASH_FIELDS}
ACTION_KEYS = {"schema", "source_manifest", "runtime", "credential", "state_leaf", "terminal_leaf"}
APPROVAL_KEYS = {"schema", "verdict", "model", "effort", "reviewed_payload_sha256", *APPROVAL_HASH_FIELDS}


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def _object(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError("duplicate key")
        value[key] = item
    return value


def _parse(raw):
    try:
        value = json.loads(raw, object_pairs_hook=_object)
    except Exception as error:
        raise ValueError("invalid json") from error
    if not isinstance(value, dict) or raw != canonical(value):
        raise ValueError("noncanonical input")
    return value


def _read_once(path, limit=1024 * 1024):
    flags = os.O_RDONLY | getattr(os, "O_BINARY", 0) | getattr(os, "O_NOFOLLOW", 0)
    fd = os.open(path, flags)
    try:
        before = os.fstat(fd)
        if not stat.S_ISREG(before.st_mode) or before.st_size > limit:
            raise ValueError("unsafe retained file")
        chunks, total = [], 0
        while True:
            chunk = os.read(fd, min(65536, limit + 1 - total))
            if not chunk:
                break
            chunks.append(chunk); total += len(chunk)
            if total > limit:
                raise ValueError("retained file too large")
        after = os.fstat(fd)
        if (before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns) != (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns):
            raise ValueError("retained file changed")
        return b"".join(chunks)
    finally:
        os.close(fd)


def retain_files(paths):
    return {name: _read_once(path) for name, path in paths.items()}


def source_bytes():
    if ROOT is None:
        raise ValueError("retained launcher needs supplied source bundle")
    return retain_files({"launcher": SELF, "helper": HELPER, "contract": CONTRACT, "test": TEST})


def source_manifest(sources, operations):
    if set(sources) != set(SOURCE_NAMES) or set(operations) != set(OPERATION_NAMES):
        raise ValueError("bundle schema")
    bundle = {**sources, **operations}
    if not all(isinstance(value, bytes) and value for value in bundle.values()):
        raise ValueError("empty bundle member")
    return {"schema": "auto-switch-q4-r9-source/v2",
            **{name + "_sha256": hashlib.sha256(bundle[name]).hexdigest() for name in SOURCE_NAMES + OPERATION_NAMES}}


def approved_request_bytes(action_raw, approval_raw, sources, operations):
    action, approval = _parse(action_raw), _parse(approval_raw)
    manifest = source_manifest(sources, operations)
    if set(action) != ACTION_KEYS or set(approval) != APPROVAL_KEYS:
        raise ValueError("schema drift")
    if action["schema"] != "auto-switch-q4-r9-action/v2" or action["source_manifest"] != manifest:
        raise ValueError("unbound action")
    if (approval["schema"], approval["verdict"], approval["model"], approval["effort"]) != ("auto-switch-q4-r9-approval/v2", "PASS", "gpt-5.6-sol", "high"):
        raise ValueError("unapproved action")
    if approval["reviewed_payload_sha256"] != hashlib.sha256(action_raw).hexdigest():
        raise ValueError("payload drift")
    if any(approval[field] != manifest[field] for field in APPROVAL_HASH_FIELDS):
        raise ValueError("source or operation drift")
    return {"schema": "auto-switch-q4-r9-request/v2", "action": action, "approval": approval,
            "source_manifest": manifest, "source_bundle": sources, "operation_bundle": operations,
            "action_bytes": action_raw, "approval_bytes": approval_raw}


def execute_retained_bytes(action_raw, approval_raw, sources, operations, secret_parent):
    request = approved_request_bytes(action_raw, approval_raw, sources, operations)
    namespace = {"__name__": "q4_r9_retained_helper", "__file__": "<retained-q4-r9-helper>"}
    exec(compile(sources["helper"], namespace["__file__"], "exec"), namespace)
    return namespace["execute"](request, secret_parent)


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if "__retained_launcher_bytes__" not in globals() or len(argv) != 10:
        return 2
    action_path, approval_path, runtime_path, command_path, collector_path, request_path, secret_parent, helper_path, contract_path, test_path = argv
    sources = retain_files({"helper": helper_path, "contract": contract_path, "test": test_path})
    sources["launcher"] = __retained_launcher_bytes__
    operations = retain_files({"runtime": runtime_path, "command": command_path, "collector": collector_path, "request": request_path})
    inputs = retain_files({"action": action_path, "approval": approval_path})
    return execute_retained_bytes(inputs["action"], inputs["approval"], sources, operations, secret_parent)


if __name__ == "__main__":
    raise SystemExit(main())
