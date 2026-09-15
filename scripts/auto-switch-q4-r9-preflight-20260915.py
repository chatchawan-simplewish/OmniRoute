"""One-contact descriptor preflight and offline exact-action renderer."""
import argparse
import contextlib
import ctypes
import hashlib
import ipaddress
import json
import os
import pathlib
import re
import secrets
import stat
import subprocess
import sys
import tempfile
import threading
import time
import uuid


ROOT = pathlib.Path(__file__).resolve().parents[1]
SELF = ROOT / "scripts" / "auto-switch-q4-r9-preflight-20260915.py"
BOOTSTRAP = ROOT / "scripts" / "auto-switch-q4-r9-preflight-bootstrap-20260915.py"
TEST = ROOT / "scripts" / "auto-switch-q4-r9-preflight-20260915-test.py"
CONTRACT = ROOT / "docs" / "auto-switch-q4-r9-preflight-contract-20260915.md"
RUNTIME = ROOT / "scripts" / "auto-switch-q4-r9-runtime-template-20260915.py"
COMMAND = ROOT / "scripts" / "auto-switch-q4-r9-command-template-20260915.json"
COLLECTOR = ROOT / "scripts" / "auto-switch-q4-r9-collector-template-20260915.py"
REQUEST = ROOT / "scripts" / "auto-switch-q4-r9-request-template-20260915.json"
R9_SOURCES = {
    "launcher": ROOT / "scripts" / "auto-switch-q4-r9-20260915.py",
    "helper": ROOT / "scripts" / "auto-switch-q4-r9-20260915-helper.py",
    "contract": ROOT / "docs" / "auto-switch-q4-r9-20260915-contract.md",
    "test": ROOT / "scripts" / "auto-switch-q4-r9-20260915-test.py",
}
PACKAGE = {"preflight": SELF, "bootstrap": BOOTSTRAP, "test": TEST, "contract": CONTRACT,
           "runtime_template": RUNTIME, "command_template": COMMAND,
           "collector_template": COLLECTOR, "request_template": REQUEST}
HOST = "192.168.1.68"
SSH_USER = "belladmin"
SSH = pathlib.Path(r"C:\WINDOWS\System32\OpenSSH\ssh.exe")
IDENTITY = pathlib.Path(r"C:\Users\chatc\.ssh\codex-prox01-vms-ed25519")
KNOWN_HOSTS = pathlib.Path(r"C:\Users\chatc\.ssh\known_hosts")
SECRET_PARENT = "/root/.omniroute-qualification"
SECRET_LEAF = "auto-switch-candidate-qualification-r5-20260913.key"
STATE_LEAF = "q4-r9-state-20260915.json"
TERMINAL_LEAF = "q4-r9-terminal-20260915.json"
RECEIPT = ROOT / "docs" / "auto-switch-q4-r9-descriptor-preflight-result-20260915.json"
CANDIDATE_ID = "9468859edcdb483c53900edde14d301a162cccc791079154677e913f39bf26a3"
IMAGE_SHA256 = "8211e1071a3b68eac01673d76129150eb0c0fea329dd222bc8bf0394b13fc844"
MODEL = "lm-studio/qwen3.8-27b-unsloth-ud-q4ks"
CONNECTION_ID = "da74225c-0fc0-45ce-ad22-ded85edb34b8"
PREFLIGHT_SPENT = False
RECEIPT_KEYS = {"schema", "status", "host", "nonce", "observed_unix_ns", "secret_parent",
                "credential", "state_leaf", "terminal_leaf", "state_absent", "terminal_absent",
                "bootstrap_sha256"}
CREDENTIAL_KEYS = {"schema", "parent_device", "parent_inode", "parent_uid", "parent_gid",
                   "parent_mode", "secret_device", "secret_inode", "secret_uid", "secret_gid",
                   "secret_mode", "secret_size", "secret_mtime_ns", "secret_leaf"}
REMOTE_SHIM = 'import io,sys;r=sys.stdin.buffer.read();n=int.from_bytes(r[:8],"big");s=r[8:8+n];p=r[8+n:];sys.stdin=io.TextIOWrapper(io.BytesIO(p),encoding="utf-8");exec(compile(s,"<retained-q4-r9-preflight>","exec"),{"__name__":"__main__","__file__":"<retained-q4-r9-preflight>"})'


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def _object(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError("duplicate key")
        value[key] = item
    return value


def parse(raw):
    try:
        value = json.loads(raw, object_pairs_hook=_object)
    except Exception as error:
        raise ValueError("invalid json") from error
    if not isinstance(value, dict) or raw != canonical(value):
        raise ValueError("noncanonical json")
    return value


def read_once(path, limit=1048576):
    flags = os.O_RDONLY | getattr(os, "O_BINARY", 0) | getattr(os, "O_NOFOLLOW", 0)
    fd = os.open(path, flags)
    try:
        before = os.fstat(fd)
        if not stat.S_ISREG(before.st_mode) or before.st_size > limit:
            raise ValueError("unsafe file")
        raw = b""
        while len(raw) <= limit:
            chunk = os.read(fd, min(65536, limit + 1 - len(raw)))
            if not chunk:
                break
            raw += chunk
        after = os.fstat(fd)
        if len(raw) > limit or (before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns) != (
                after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns):
            raise ValueError("unstable file")
        return raw
    finally:
        os.close(fd)


def digest(path):
    return hashlib.sha256(read_once(path)).hexdigest()


def ssh_command(known_hosts_path):
    return [str(SSH), "-T", "-F", "none", "-i", str(IDENTITY),
            "-o", "IdentitiesOnly=yes", "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=yes",
            "-o", "UserKnownHostsFile=" + pathlib.Path(known_hosts_path).as_posix(), "-o", "GlobalKnownHostsFile=none",
            "-o", "HostKeyAlias=" + HOST, "-o", "ConnectTimeout=10", "-o", "ConnectionAttempts=1",
            "-o", "ServerAliveInterval=10", "-o", "ServerAliveCountMax=2", SSH_USER + "@" + HOST,
            "sudo -n /usr/bin/python3 -I -c '" + REMOTE_SHIM + "'"]


def retain_package():
    return {name: read_once(path) for name, path in PACKAGE.items()}


def review_payload(package=None, known_hosts=None):
    package = retain_package() if package is None else package
    known_hosts = read_once(KNOWN_HOSTS) if known_hosts is None else known_hosts
    if set(package) != set(PACKAGE) or not all(isinstance(raw, bytes) and raw for raw in package.values()):
        raise ValueError("package")
    return {
        "schema": "auto-switch-q4-r9-descriptor-preflight-review/v1",
        "base_source_commit": "e129b8dd7c3d2831198b6d675d459c6ba223f2ff",
        "source_review_commit": "b500e65e2386769ed38241ebb5cd9ee742a23eb0",
        "host": HOST, "ssh_user": SSH_USER, "ssh_path": str(SSH), "identity_path": str(IDENTITY),
        "known_hosts_path": str(KNOWN_HOSTS), "known_hosts_sha256": hashlib.sha256(known_hosts).hexdigest(),
        "secret_parent": SECRET_PARENT, "secret_leaf": SECRET_LEAF,
        "state_leaf": STATE_LEAF, "terminal_leaf": TERMINAL_LEAF, "receipt_path": str(RECEIPT),
        "package_sha256": {name: hashlib.sha256(package[name]).hexdigest() for name in PACKAGE},
    }


def validate_approval(raw):
    package = retain_package()
    known_hosts = read_once(KNOWN_HOSTS)
    approval = parse(raw)
    if set(approval) != {"schema", "verdict", "model", "effort", "reviewed_payload_sha256"}:
        raise ValueError("approval schema")
    if (approval["schema"], approval["verdict"], approval["model"], approval["effort"]) != (
            "auto-switch-q4-r9-descriptor-preflight-approval/v1", "PASS", "gpt-5.6-sol", "high"):
        raise ValueError("approval")
    if approval["reviewed_payload_sha256"] != hashlib.sha256(canonical(review_payload(package, known_hosts))).hexdigest():
        raise ValueError("review drift")
    return package["bootstrap"], known_hosts


def _bounded_capture(command, payload, timeout):
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, errors, failed = bytearray(), bytearray(), []
    def read(stream, target, limit):
        while len(target) <= limit:
            chunk = stream.read(min(65536, limit + 1 - len(target)))
            if not chunk:
                return
            target.extend(chunk)
        failed.append("overflow")
    def write():
        try:
            process.stdin.write(payload); process.stdin.close()
        except (BrokenPipeError, OSError):
            failed.append("pipe")
    threads = [threading.Thread(target=read, args=(process.stdout, output, 32768), daemon=True),
               threading.Thread(target=read, args=(process.stderr, errors, 4096), daemon=True),
               threading.Thread(target=write, daemon=True)]
    for thread in threads:
        thread.start()
    deadline = time.monotonic() + timeout
    while process.poll() is None and not failed and time.monotonic() < deadline:
        time.sleep(0.01)
    if process.poll() is None:
        process.kill(); process.wait(timeout=3); failed.append("timeout")
    for thread in threads:
        thread.join(timeout=3)
    if failed or any(thread.is_alive() for thread in threads):
        raise RuntimeError("bounded transport uncertainty")
    return process.returncode, bytes(output), bytes(errors)


def _config(bootstrap, nonce):
    return {"schema": "auto-switch-q4-r9-descriptor-preflight-config/v1", "host": HOST,
            "nonce": nonce, "secret_parent": SECRET_PARENT, "secret_leaf": SECRET_LEAF,
            "state_leaf": STATE_LEAF, "terminal_leaf": TERMINAL_LEAF,
            "bootstrap_sha256": hashlib.sha256(bootstrap).hexdigest()}


def validate_receipt(raw, nonce=None, now_ns=None, bootstrap_sha256=None):
    value = parse(raw)
    if set(value) != RECEIPT_KEYS or value["schema"] != "auto-switch-q4-r9-descriptor-preflight/v1" or value["status"] != "PASS":
        raise ValueError("receipt schema")
    if (value["host"], value["secret_parent"], value["state_leaf"], value["terminal_leaf"]) != (
            HOST, SECRET_PARENT, STATE_LEAF, TERMINAL_LEAF) or value["state_absent"] is not True or value["terminal_absent"] is not True:
        raise ValueError("receipt pins")
    if not re.fullmatch(r"[0-9a-f]{64}", value["nonce"]) or (nonce is not None and value["nonce"] != nonce):
        raise ValueError("nonce")
    bootstrap_sha256 = digest(BOOTSTRAP) if bootstrap_sha256 is None else bootstrap_sha256
    if value["bootstrap_sha256"] != bootstrap_sha256:
        raise ValueError("bootstrap drift")
    now_ns = time.time_ns() if now_ns is None else now_ns
    if type(value["observed_unix_ns"]) is not int or not 0 <= now_ns - value["observed_unix_ns"] <= 900_000_000_000:
        raise ValueError("stale receipt")
    credential = value["credential"]
    if not isinstance(credential, dict) or set(credential) != CREDENTIAL_KEYS or credential.get("schema") != "auto-switch-q4-r9-credential/v1":
        raise ValueError("credential schema")
    numeric = CREDENTIAL_KEYS - {"schema", "secret_leaf"}
    if any(type(credential[field]) is not int or credential[field] < 0 for field in numeric):
        raise ValueError("credential metadata")
    if ((credential["parent_uid"], credential["parent_gid"], credential["parent_mode"],
         credential["secret_uid"], credential["secret_gid"], credential["secret_mode"])
            != (0, 0, 0o700, 0, 0, 0o600) or not 1 <= credential["secret_size"] <= 4096
            or credential["secret_leaf"] != SECRET_LEAF):
        raise ValueError("unsafe credential metadata")
    return value


def _write_reserved(path, raw):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0), 0o600)
    try:
        offset = 0
        while offset < len(raw):
            written = os.write(fd, raw[offset:])
            if written <= 0:
                raise OSError("write")
            offset += written
        os.fsync(fd)
    finally:
        os.close(fd)


def _locked_read_fd(path):
    if os.name != "nt":
        raise OSError("Windows SSH boundary required")
    import msvcrt
    create_file = ctypes.windll.kernel32.CreateFileW
    create_file.argtypes = [ctypes.c_wchar_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p,
                            ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p]
    create_file.restype = ctypes.c_void_p
    handle = create_file(str(path), 0x80000000, 0x00000001, None, 3, 0x80, None)
    if handle == ctypes.c_void_p(-1).value:
        raise OSError(ctypes.get_last_error(), "known_hosts lock")
    try:
        return msvcrt.open_osfhandle(handle, os.O_RDONLY | getattr(os, "O_BINARY", 0))
    except Exception:
        ctypes.windll.kernel32.CloseHandle(ctypes.c_void_p(handle))
        raise


@contextlib.contextmanager
def retained_known_hosts(raw):
    if not isinstance(raw, bytes) or not raw or len(raw) > 1048576:
        raise ValueError("known_hosts bytes")
    parent = pathlib.Path(tempfile.mkdtemp(prefix="q4-r9-known-hosts-"))
    path = parent / "known_hosts"
    fd = None
    try:
        _write_reserved(path, raw)
        os.chmod(path, stat.S_IREAD)
        fd = _locked_read_fd(path)
        before = os.fstat(fd)
        os.lseek(fd, 0, os.SEEK_SET)
        if os.read(fd, len(raw) + 1) != raw:
            raise ValueError("known_hosts materialization")
        yield path
        after = os.fstat(fd)
        current = os.stat(path, follow_symlinks=False)
        os.lseek(fd, 0, os.SEEK_SET)
        if ((before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns) !=
                (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns)
                or (before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns) !=
                (current.st_dev, current.st_ino, current.st_size, current.st_mtime_ns)
                or os.read(fd, len(raw) + 1) != raw):
            raise RuntimeError("known_hosts uncertainty")
    finally:
        if fd is not None:
            os.close(fd)
        cleanup_error = None
        try:
            if path.exists():
                os.chmod(path, stat.S_IWRITE); path.unlink()
            parent.rmdir()
        except Exception as error:
            cleanup_error = error
        if cleanup_error is not None:
            raise RuntimeError("known_hosts cleanup uncertainty") from cleanup_error


def run_preflight(receipt_path=RECEIPT, transport=_bounded_capture, now_ns=None, bootstrap=None,
                  known_hosts=None):
    global PREFLIGHT_SPENT
    receipt_path = pathlib.Path(receipt_path)
    fd = os.open(receipt_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0), 0o600)
    PREFLIGHT_SPENT = True
    raw = canonical({"schema": "auto-switch-q4-r9-descriptor-preflight-local/v1", "status": "UNKNOWN",
                     "host": HOST, "reason": "uncertain"})
    try:
        bootstrap = read_once(BOOTSTRAP) if bootstrap is None else bootstrap
        known_hosts = read_once(KNOWN_HOSTS) if known_hosts is None else known_hosts
        if not isinstance(bootstrap, bytes) or not bootstrap:
            raise ValueError("bootstrap")
        nonce = secrets.token_hex(32)
        payload = len(bootstrap).to_bytes(8, "big") + bootstrap + canonical(_config(bootstrap, nonce))
        with retained_known_hosts(known_hosts) as retained_path:
            code, output, errors = transport(ssh_command(retained_path), payload, 30)
        if code or errors or not output:
            raise RuntimeError("preflight transport")
        raw = canonical(validate_receipt(output, nonce, now_ns, hashlib.sha256(bootstrap).hexdigest()))
        return raw
    finally:
        try:
            offset = 0
            while offset < len(raw):
                written = os.write(fd, raw[offset:])
                if written <= 0:
                    raise OSError("write")
                offset += written
            os.fsync(fd)
        finally:
            os.close(fd)


def failure_envelope(receipt_path=RECEIPT):
    path = pathlib.Path(receipt_path)
    if PREFLIGHT_SPENT or (path.is_file() and not path.is_symlink()):
        return {"schema": "auto-switch-q4-r9-preflight-error/v1", "status": "UNKNOWN",
                "preflight_spent": True}
    return {"schema": "auto-switch-q4-r9-preflight-error/v1", "status": "NOT_EXECUTED",
            "preflight_spent": False}


def _operation_bytes(candidate_ipv4, request_id):
    address = ipaddress.ip_address(candidate_ipv4)
    if address.version != 4 or not address.is_private or address.is_loopback or address.is_multicast:
        raise ValueError("unsafe candidate address")
    request = parse(read_once(REQUEST).rstrip(b"\r\n"))
    if (request.get("headers") != {"x-omniroute-session-id": "__REQUEST_ID__", "x-request-id": "__REQUEST_ID__"}
            or uuid.UUID(request_id).version != 4):
        raise ValueError("request id")
    request["headers"] = {name: str(uuid.UUID(request_id)) for name in request["headers"]}
    command = parse(read_once(COMMAND).rstrip(b"\r\n"))
    if command.get("candidate_id") != CANDIDATE_ID or command.get("image_sha256") != IMAGE_SHA256:
        raise ValueError("command template")
    return {"runtime": read_once(RUNTIME), "command": canonical(command),
            "collector": read_once(COLLECTOR), "request": canonical(request)}, str(address)


def render_action(receipt_raw, candidate_ipv4, request_id, output_dir, now_ns=None):
    receipt = validate_receipt(receipt_raw, now_ns=now_ns)
    operations, address = _operation_bytes(candidate_ipv4, request_id)
    sources = {name: read_once(path) for name, path in R9_SOURCES.items()}
    manifest = {"schema": "auto-switch-q4-r9-source/v2",
                **{name + "_sha256": hashlib.sha256(raw).hexdigest() for name, raw in {**sources, **operations}.items()}}
    runtime = {
        "schema": "auto-switch-q4-r9-runtime/v2", "host": HOST, "candidate_id": CANDIDATE_ID,
        "image_sha256": IMAGE_SHA256, "endpoint": "http://" + address + ":20129/v1",
        "model": MODEL, "connection_id": CONNECTION_ID,
        **{name + "_sha256": hashlib.sha256(operations[name]).hexdigest() for name in operations},
        "start_timeout_ms": 120000, "collect_timeout_ms": 60000, "stop_timeout_ms": 60000,
    }
    action = {"schema": "auto-switch-q4-r9-action/v2", "source_manifest": manifest,
              "runtime": runtime, "credential": receipt["credential"],
              "state_leaf": STATE_LEAF, "terminal_leaf": TERMINAL_LEAF}
    action_raw = canonical(action)
    output_dir = pathlib.Path(output_dir)
    output_dir.mkdir(mode=0o700, parents=False, exist_ok=False)
    paths = {}
    for name, raw in operations.items():
        path = output_dir / (name + (".py" if name in {"runtime", "collector"} else ".json"))
        _write_reserved(path, raw); paths[name] = str(path.resolve())
    action_path = output_dir / "action.json"
    _write_reserved(action_path, action_raw); paths["action"] = str(action_path.resolve())
    review_package = {
        "schema": "auto-switch-q4-r9-exact-action-review-package/v1", "host": HOST,
        "secret_parent": SECRET_PARENT, "receipt_sha256": hashlib.sha256(receipt_raw).hexdigest(),
        "receipt_observed_unix_ns": receipt["observed_unix_ns"],
        "action_sha256": hashlib.sha256(action_raw).hexdigest(), "paths": paths,
        "source_manifest": manifest,
    }
    _write_reserved(output_dir / "review-package.json", canonical(review_package))
    return action_raw


def main():
    parser = argparse.ArgumentParser()
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--review-payload", action="store_true")
    modes.add_argument("--execute-approved", type=pathlib.Path)
    modes.add_argument("--render-action", type=pathlib.Path)
    parser.add_argument("--candidate-ipv4")
    parser.add_argument("--request-id")
    parser.add_argument("--output-dir", type=pathlib.Path)
    args = parser.parse_args()
    if args.review_payload:
        sys.stdout.buffer.write(canonical(review_payload())); return 0
    if args.execute_approved:
        bootstrap, known_hosts = validate_approval(read_once(args.execute_approved))
        run_preflight(bootstrap=bootstrap, known_hosts=known_hosts); return 0
    if not args.candidate_ipv4 or not args.request_id or not args.output_dir:
        return 2
    raw = render_action(read_once(args.render_action), args.candidate_ipv4, args.request_id, args.output_dir)
    sys.stdout.buffer.write(raw)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception:
        sys.stdout.buffer.write(canonical(failure_envelope()))
        raise SystemExit(1)
