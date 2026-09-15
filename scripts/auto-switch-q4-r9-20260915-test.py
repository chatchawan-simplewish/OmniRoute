import hashlib
import importlib.util
import json
import os
import pathlib
import tempfile
import unittest
from unittest import mock


ROOT = pathlib.Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "scripts" / "auto-switch-q4-r9-20260915.py"
HELPER = ROOT / "scripts" / "auto-switch-q4-r9-20260915-helper.py"


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PROGRAM = r'''import json,sys
def frames(raw):
 out=[]
 while raw:
  size=int.from_bytes(raw[:8],"big");raw=raw[8:]
  out.append(raw[:size]);raw=raw[size:]
 return out
action_raw,command_raw=frames(sys.stdin.buffer.read())
command=json.loads(command_raw)
with open(command["marker"],"a",encoding="ascii") as handle:handle.write(sys.argv[1]+"\n")
if sys.argv[1]=="start" and command["fail_start"]:raise SystemExit(7)
'''.encode()


COLLECTOR = r'''import json,sys
def frames(raw):
 out=[]
 while raw:
  size=int.from_bytes(raw[:8],"big");raw=raw[8:]
  out.append(raw[:size]);raw=raw[size:]
 return out
action_raw,request_raw,secret=frames(sys.stdin.buffer.read())
action=json.loads(action_raw);request=json.loads(request_raw)
assert secret==b"fixture-secret" and request=={"schema":"q4-request/v1","prompt":"reply one byte"}
r=action["runtime"]
value={"schema":"auto-switch-q4-r9-evidence/v1","runtime":r,
 "health":{"status":200,"candidate_id":r["candidate_id"]},
 "models":{"status":200,"candidate_id":r["candidate_id"],"model":r["model"]},
 "completion":{"status":200,"candidate_id":r["candidate_id"],"model":r["model"],
 "connection_id":r["connection_id"],"request_count":1,
 "request_id":"11111111-1111-4111-8111-111111111111","content_bytes":1}}
sys.stdout.buffer.write(json.dumps(value,sort_keys=True,separators=(",",":")).encode())
'''.encode()


class Q4R9Test(unittest.TestCase):
    def setUp(self):
        self.launcher = load(LAUNCHER, "q4_r9_launcher")
        self.helper = load(HELPER, "q4_r9_helper")

    def build(self, root, fail_start=False):
        marker = root / "marker"
        operations = {
            "runtime": PROGRAM,
            "command": self.launcher.canonical({"schema": "q4-command/v1", "marker": str(marker), "fail_start": fail_start}),
            "collector": COLLECTOR,
            "request": self.launcher.canonical({"schema": "q4-request/v1", "prompt": "reply one byte"}),
        }
        sources = self.launcher.source_bytes()
        manifest = self.launcher.source_manifest(sources, operations)
        runtime = {
            "schema": "auto-switch-q4-r9-runtime/v2", "host": "192.0.2.9", "candidate_id": "a" * 64,
            "image_sha256": "b" * 64, "endpoint": "http://127.0.0.1:20129/v1",
            "model": "lm-studio/qwen3.8-27b-unsloth-ud-q4ks",
            "connection_id": "da74225c-0fc0-45ce-ad22-ded85edb34b8",
            **{name + "_sha256": hashlib.sha256(value).hexdigest() for name, value in operations.items()},
            "start_timeout_ms": 5000, "collect_timeout_ms": 5000, "stop_timeout_ms": 5000,
        }
        credential = {"schema": "auto-switch-q4-r9-credential/v1", "parent_device": 1, "parent_inode": 2,
                      "parent_uid": 0, "parent_gid": 0, "parent_mode": 0o700,
                      "secret_device": 3, "secret_inode": 4, "secret_uid": 0, "secret_gid": 0,
                      "secret_mode": 0o600, "secret_size": 14, "secret_mtime_ns": 5, "secret_leaf": "key"}
        action = {"schema": "auto-switch-q4-r9-action/v2", "source_manifest": manifest, "runtime": runtime,
                  "credential": credential, "state_leaf": "q4-r9-state.json", "terminal_leaf": "q4-r9-terminal.json"}
        action_raw = self.launcher.canonical(action)
        approval = {"schema": "auto-switch-q4-r9-approval/v2", "verdict": "PASS", "model": "gpt-5.6-sol",
                    "effort": "high", "reviewed_payload_sha256": hashlib.sha256(action_raw).hexdigest(),
                    **{field: manifest[field] for field in self.launcher.APPROVAL_HASH_FIELDS}}
        request = self.launcher.approved_request_bytes(action_raw, self.launcher.canonical(approval), sources, operations)
        return action, request, sources, operations, marker

    def test_retained_programs_and_direct_evidence_are_pinned_and_fail_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            action, request, sources, operations, marker = self.build(root)

            self.assertEqual(request["operation_bundle"], operations)
            self.assertEqual(self.helper._validate(request), action)
            start = self.helper._run_retained(operations["runtime"], "start",
                                              self.helper._pack(request["action_bytes"], operations["command"]), 5000, 0)
            self.assertEqual((start.returncode, start.stdout, start.stderr), (0, b"", b""))
            observed = self.helper._run_retained(operations["collector"], "collect",
                                                 self.helper._pack(request["action_bytes"], operations["request"], b"fixture-secret"), 5000, 65536)
            evidence = self.helper._validate_evidence(observed, action)
            self.assertEqual(evidence["completion"]["request_count"], 1)
            self.assertEqual(marker.read_text(encoding="ascii"), "start\n")

            runtime_path = root / "runtime.py"
            runtime_path.write_bytes(operations["runtime"])
            retained = self.launcher.retain_files({"runtime": runtime_path})
            runtime_path.write_text("raise SystemExit(99)\n", encoding="ascii")
            kept = self.helper._run_retained(retained["runtime"], "stop",
                                             self.helper._pack(request["action_bytes"], operations["command"]), 5000, 0)
            self.assertEqual(kept.returncode, 0)
            self.assertEqual(marker.read_text(encoding="ascii"), "start\nstop\n")

            noncanonical = observed.stdout + b"\n"
            with self.assertRaises(ValueError):
                self.helper._validate_evidence(type("Result", (), {"returncode": 0, "stdout": noncanonical, "stderr": b""})(), action)
            boolean_evidence = json.loads(observed.stdout)
            boolean_evidence["completion"]["request_count"] = True
            with self.assertRaises(ValueError):
                self.helper._validate_evidence(type("Result", (), {"returncode": 0,
                    "stdout": self.launcher.canonical(boolean_evidence), "stderr": b""})(), action)

            changed = dict(operations)
            changed["collector"] += b"\n"
            with self.assertRaises(ValueError):
                self.launcher.approved_request_bytes(request["action_bytes"], request["approval_bytes"], sources, changed)

            _, bad_request, _, bad_operations, bad_marker = self.build(root, fail_start=True)
            start = self.helper._run_retained(bad_operations["runtime"], "start",
                                              self.helper._pack(bad_request["action_bytes"], bad_operations["command"]), 5000, 0)
            stop = self.helper._run_retained(bad_operations["runtime"], "stop",
                                             self.helper._pack(bad_request["action_bytes"], bad_operations["command"]), 5000, 0)
            self.assertEqual(start.returncode, 7)
            self.assertEqual(stop.returncode, 0)
            self.assertTrue(bad_marker.read_text(encoding="ascii").endswith("start\nstop\n"))

    def test_secret_and_leaf_parent_pins_come_from_opened_objects(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            key = root / "key"
            key.write_bytes(b"fixture-secret")
            if os.name == "posix":
                os.chmod(root, 0o700); os.chmod(key, 0o600)
                parent_fd, secret_fd, identity = self.helper._open_credential(root, "key")
                try:
                    self.assertEqual(identity["parent_device"], os.fstat(parent_fd).st_dev)
                    self.assertEqual(identity["secret_inode"], os.fstat(secret_fd).st_ino)
                finally:
                    os.close(secret_fd); os.close(parent_fd)
            else:
                with self.assertRaises(OSError):
                    self.helper._open_credential(root, "key")

    def test_short_retained_secret_read_is_rejected_before_runtime(self):
        with tempfile.TemporaryDirectory() as tmp:
            key = pathlib.Path(tmp) / "key"
            key.write_bytes(b"fixture-secret")
            fd = os.open(key, os.O_RDONLY)
            try:
                opened = os.fstat(fd)
                expected = {"secret_device": opened.st_dev, "secret_inode": opened.st_ino,
                            "secret_uid": opened.st_uid, "secret_gid": opened.st_gid,
                            "secret_mode": opened.st_mode & 0o777, "secret_size": opened.st_size,
                            "secret_mtime_ns": opened.st_mtime_ns}
                with mock.patch.object(self.helper.os, "pread", return_value=b"fixture-secre", create=True):
                    with self.assertRaises(ValueError):
                        self.helper._read_secret(fd, {"expected": expected})
            finally:
                os.close(fd)

    def test_execute_fail_start_stops_once_retains_unknown_and_withholds_terminal(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            action, request, _, _, marker = self.build(root, fail_start=True)
            parent = os.open(root / "parent-handle", os.O_WRONLY | os.O_CREAT)
            secret = os.open(root / "secret-handle", os.O_WRONLY | os.O_CREAT)
            writes = []
            with mock.patch.object(self.helper, "_open_credential", return_value=(parent, secret, action["credential"])), \
                    mock.patch.object(self.helper, "_exists", return_value=False), \
                    mock.patch.object(self.helper, "_read_secret", return_value=b"fixture-secret"), \
                    mock.patch.object(self.helper, "_write_new", side_effect=lambda fd, leaf, value: writes.append((leaf, value))):
                self.assertEqual(self.helper.execute(request, root), 1)
            self.assertEqual(marker.read_text(encoding="ascii"), "start\nstop\n")
            self.assertEqual(writes, [(action["state_leaf"],
                {"schema": "auto-switch-q4-r9-state/v1", "status": "Q4_R9_UNKNOWN", "gate_spent": True})])

    @unittest.skipUnless(os.name == "posix" and getattr(os, "geteuid", lambda: 1)() == 0,
                         "live gate requires the reviewed root-owned POSIX store")
    def test_posix_gate_reserves_unknown_stops_once_and_publishes_only_direct_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            os.chmod(root, 0o700)
            key = root / "key"
            key.write_bytes(b"fixture-secret")
            os.chmod(key, 0o600)
            action, request, sources, operations, marker = self.build(root)
            parent_fd, secret_fd, action["credential"] = self.helper._open_credential(root, "key")
            os.close(secret_fd); os.close(parent_fd)
            action_raw = self.launcher.canonical(action)
            approval = {**request["approval"], "reviewed_payload_sha256": hashlib.sha256(action_raw).hexdigest()}
            request = self.launcher.approved_request_bytes(action_raw, self.launcher.canonical(approval), sources, operations)
            self.assertEqual(self.helper.execute(request, root), 0)
            self.assertEqual(json.loads((root / action["state_leaf"]).read_text()),
                             {"schema": "auto-switch-q4-r9-state/v1", "status": "Q4_R9_UNKNOWN", "gate_spent": True})
            self.assertEqual(json.loads((root / action["terminal_leaf"]).read_text())["status"], "Q4_R9_PASS")
            self.assertEqual(marker.read_text(encoding="ascii"), "start\nstop\n")
            with self.assertRaises(FileExistsError):
                self.helper.execute(request, root)


if __name__ == "__main__":
    unittest.main()
