import hashlib
import importlib.util
import inspect
import json
import pathlib
import tempfile
import unittest
from unittest import mock


ROOT = pathlib.Path(__file__).resolve().parents[1]
PREFLIGHT = ROOT / "scripts" / "auto-switch-q4-r9-preflight-20260915.py"


class Q4R9PreflightTest(unittest.TestCase):
    def test_one_contact_receipt_and_exact_action_render(self):
        self.assertTrue(PREFLIGHT.is_file(), "preflight renderer is missing")
        spec = importlib.util.spec_from_file_location("q4_r9_preflight", PREFLIGHT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        now_ns = 1_789_445_000_000_000_000
        retained_bootstrap = module.read_once(module.BOOTSTRAP)
        calls = []

        def transport(command, payload, timeout):
            calls.append((command, timeout))
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
            with mock.patch.object(module, "read_once", side_effect=AssertionError("bootstrap reopened")):
                receipt_raw = module.run_preflight(receipt_path, transport, now_ns=now_ns,
                                                   bootstrap=retained_bootstrap)
            self.assertEqual(len(calls), 1)
            self.assertEqual(receipt_path.read_bytes(), receipt_raw)
            with self.assertRaises(FileExistsError):
                module.run_preflight(receipt_path, transport, now_ns=now_ns)
            self.assertEqual(len(calls), 1)

            request_id = "11111111-1111-4111-8111-111111111111"
            action_raw = module.render_action(receipt_raw, "172.18.0.9", request_id, root / "action", now_ns=now_ns)
            action = json.loads(action_raw)
            self.assertEqual(action_raw, module.canonical(action))
            self.assertEqual(action["credential"], json.loads(receipt_raw)["credential"])
            self.assertEqual(action["runtime"]["endpoint"], "http://172.18.0.9:20129/v1")
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
