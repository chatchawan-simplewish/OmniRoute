import hashlib
import importlib.util
import inspect
import json
import os
import pathlib
import sqlite3
import tempfile
import unittest
from unittest import mock


ROOT = pathlib.Path(__file__).resolve().parents[1]
PREFLIGHT = ROOT / "scripts" / "auto-switch-q4-r9-preflight-20260915.py"
RUNTIME = ROOT / "scripts" / "auto-switch-q4-r9-runtime-template-20260915.py"
COLLECTOR = ROOT / "scripts" / "auto-switch-q4-r9-collector-template-20260915.py"


class Q4R9PreflightTest(unittest.TestCase):
    def test_one_contact_receipt_and_exact_action_render(self):
        self.assertTrue(PREFLIGHT.is_file(), "preflight renderer is missing")
        spec = importlib.util.spec_from_file_location("q4_r9_preflight", PREFLIGHT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        now_ns = 1_789_445_000_000_000_000
        retained_bootstrap = module.read_once(module.BOOTSTRAP)
        retained_known_hosts = b"reviewed-host-key-bytes\n"
        calls = []
        used_known_hosts = []

        def transport(command, payload, timeout):
            calls.append((command, timeout))
            known_hosts_arg = next(item for item in command if item.startswith("UserKnownHostsFile="))
            known_hosts_path = pathlib.Path(known_hosts_arg.split("=", 1)[1])
            used_known_hosts.append(known_hosts_path)
            self.assertNotEqual(known_hosts_path, module.KNOWN_HOSTS)
            self.assertEqual(known_hosts_path.read_bytes(), retained_known_hosts)
            replacement = known_hosts_path.with_name("replacement")
            replacement.write_bytes(b"different-host-key\n")
            with self.assertRaises(PermissionError):
                os.replace(replacement, known_hosts_path)
            replacement.unlink()
            size = int.from_bytes(payload[:8], "big")
            bootstrap, raw_config = payload[8:8 + size], payload[8 + size:]
            self.assertEqual(bootstrap, retained_bootstrap)
            self.assertNotIn(b"fixture-secret", payload)
            config = json.loads(raw_config)
            credential = {
                "schema": "auto-switch-q4-r9-credential/v1",
                "parent_device": 1, "parent_inode": 2, "parent_uid": 0, "parent_gid": 0,
                "parent_mode": 0o700, "secret_device": 3, "secret_inode": 4,
                "secret_uid": 0, "secret_gid": 0, "secret_mode": 0o600,
                "secret_size": 32, "secret_mtime_ns": 5, "secret_leaf": config["secret_leaf"],
            }
            response = {
                "schema": "auto-switch-q4-r9-descriptor-preflight/v1",
                "status": "PASS", "host": config["host"], "nonce": config["nonce"],
                "observed_unix_ns": now_ns, "secret_parent": config["secret_parent"],
                "credential": credential, "state_leaf": config["state_leaf"],
                "terminal_leaf": config["terminal_leaf"], "state_absent": True,
                "terminal_absent": True,
                "bootstrap_sha256": hashlib.sha256(bootstrap).hexdigest(),
            }
            return 0, module.canonical(response), b""

        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            receipt_path = root / "receipt.json"
            self.assertIn("bootstrap", inspect.signature(module.run_preflight).parameters,
                          "approved retained bootstrap cannot be supplied")
            self.assertIn("known_hosts", inspect.signature(module.run_preflight).parameters,
                          "approved known-host bytes cannot be supplied")
            with mock.patch.object(module, "read_once", side_effect=AssertionError("bootstrap reopened")):
                receipt_raw = module.run_preflight(receipt_path, transport, now_ns=now_ns,
                                                   bootstrap=retained_bootstrap,
                                                   known_hosts=retained_known_hosts)
            self.assertEqual(len(calls), 1)
            self.assertFalse(used_known_hosts[0].exists())
            self.assertEqual(receipt_path.read_bytes(), receipt_raw)
            with self.assertRaises(FileExistsError):
                module.run_preflight(receipt_path, transport, now_ns=now_ns)
            self.assertEqual(len(calls), 1)

            uncertain_path = root / "uncertain.json"
            with self.assertRaises(RuntimeError):
                module.run_preflight(uncertain_path, lambda *_: (_ for _ in ()).throw(RuntimeError("lost")),
                                     now_ns=now_ns, bootstrap=retained_bootstrap,
                                     known_hosts=retained_known_hosts)
            self.assertEqual(json.loads(uncertain_path.read_bytes())["status"], "UNKNOWN")
            self.assertEqual(module.failure_envelope(uncertain_path), {
                "schema": "auto-switch-q4-r9-preflight-error/v1", "status": "UNKNOWN",
                "preflight_spent": True,
            })
            uncertain_path.unlink()
            self.assertEqual(module.failure_envelope(uncertain_path)["status"], "UNKNOWN")

            request_id = "11111111-1111-4111-8111-111111111111"
            action_raw = module.render_action(receipt_raw, "172.18.0.9", request_id, root / "action", now_ns=now_ns)
            action = json.loads(action_raw)
            self.assertEqual(action_raw, module.canonical(action))
            self.assertEqual(action["credential"], json.loads(receipt_raw)["credential"])
            self.assertEqual(action["runtime"]["endpoint"], "http://172.18.0.9:20129/v1")

            runtime_spec = importlib.util.spec_from_file_location("q4_r9_runtime", RUNTIME)
            runtime_module = importlib.util.module_from_spec(runtime_spec)
            runtime_spec.loader.exec_module(runtime_module)
            runtime_config = json.loads((ROOT / "scripts" / "auto-switch-q4-r9-command-template-20260915.json").read_bytes())
            candidate = {
                "Id": runtime_config["candidate_id"], "Name": "/" + runtime_config["candidate_name"],
                "Image": "sha256:" + runtime_config["image_sha256"],
                "NetworkSettings": {"Networks": {
                    runtime_config["network_name"]: {"IPAddress": "172.18.0.9"}}},
            }
            self.assertEqual(runtime_module.validate_candidate_endpoint(candidate, runtime_config, action["runtime"]),
                             "172.18.0.9")
            candidate["NetworkSettings"]["Networks"][runtime_config["network_name"]]["IPAddress"] = "172.18.0.10"
            with self.assertRaises(ValueError):
                runtime_module.validate_candidate_endpoint(candidate, runtime_config, action["runtime"])

            collector_spec = importlib.util.spec_from_file_location("q4_r9_collector", COLLECTOR)
            collector_module = importlib.util.module_from_spec(collector_spec)
            collector_spec.loader.exec_module(collector_module)
            selection_db = root / "selection.sqlite"
            observed_log_id = "1789445000000-abc123"
            connection = sqlite3.connect(selection_db)
            connection.execute("CREATE TABLE call_logs(id TEXT,status INTEGER,model TEXT,provider TEXT,connection_id TEXT)")
            connection.execute("INSERT INTO call_logs VALUES(?,?,?,?,?)", (
                observed_log_id, 200, action["runtime"]["model"], "lm-studio", action["runtime"]["connection_id"]))
            connection.commit(); connection.close()
            self.assertEqual(collector_module.observed_connection(selection_db, observed_log_id, action["runtime"]),
                             action["runtime"]["connection_id"])
            mismatched_runtime = dict(action["runtime"])
            mismatched_runtime["connection_id"] = "22222222-2222-4222-8222-222222222222"
            with self.assertRaises(ValueError):
                collector_module.observed_connection(selection_db, observed_log_id, mismatched_runtime)
            review_package_path = root / "action" / "review-package.json"
            self.assertTrue(review_package_path.is_file(), "exact-action review package is missing")
            review_package = json.loads(review_package_path.read_bytes())
            self.assertEqual(review_package["schema"], "auto-switch-q4-r9-exact-action-review-package/v1")
            self.assertEqual(review_package["receipt_sha256"], hashlib.sha256(receipt_raw).hexdigest())
            self.assertEqual(review_package["action_sha256"], hashlib.sha256(action_raw).hexdigest())
            self.assertEqual(review_package["host"], module.HOST)
            self.assertEqual(review_package["secret_parent"], module.SECRET_PARENT)
            for name in ("runtime", "command", "collector", "request"):
                raw = (root / "action" / (name + (".py" if name in {"runtime", "collector"} else ".json"))).read_bytes()
                self.assertEqual(hashlib.sha256(raw).hexdigest(), action["source_manifest"][name + "_sha256"])
            current_launcher = module.R9_SOURCES["launcher"]
            current_helper = module.R9_SOURCES["helper"]
            launcher_spec = importlib.util.spec_from_file_location("q4_r9_launcher", current_launcher)
            launcher = importlib.util.module_from_spec(launcher_spec); launcher_spec.loader.exec_module(launcher)
            helper_spec = importlib.util.spec_from_file_location("q4_r9_helper", current_helper)
            helper = importlib.util.module_from_spec(helper_spec); helper_spec.loader.exec_module(helper)
            sources = {name: module.read_once(path) for name, path in module.R9_SOURCES.items()}
            operations = {name: (root / "action" / (name + (".py" if name in {"runtime", "collector"} else ".json"))).read_bytes()
                          for name in ("runtime", "command", "collector", "request")}
            approval = {"schema": "auto-switch-q4-r9-approval/v2", "verdict": "PASS",
                        "model": "gpt-5.6-sol", "effort": "high",
                        "reviewed_payload_sha256": hashlib.sha256(action_raw).hexdigest(),
                        **{field: action["source_manifest"][field] for field in launcher.APPROVAL_HASH_FIELDS}}
            retained = launcher.approved_request_bytes(action_raw, launcher.canonical(approval), sources, operations)
            self.assertEqual(helper._validate(retained), action)

            unsafe = json.loads(receipt_raw)
            unsafe["secret_sha256"] = "0" * 64
            with self.assertRaises(ValueError):
                module.render_action(module.canonical(unsafe), "172.18.0.9", request_id, root / "unsafe", now_ns=now_ns)


if __name__ == "__main__":
    unittest.main()
