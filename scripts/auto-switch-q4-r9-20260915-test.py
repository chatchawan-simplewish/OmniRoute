import copy
import hashlib
import importlib.util
import json
import pathlib
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "scripts" / "auto-switch-q4-r9-20260915.py"
HELPER = ROOT / "scripts" / "auto-switch-q4-r9-20260915-helper.py"


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Runtime:
    def __init__(self):
        self.started = self.stopped = False

    def snapshot(self):
        return RUNTIME

    def source_bytes(self):
        return b"fixture-reviewed-runtime-v1"

    def start(self):
        self.started = True

    def authenticate(self, secret, action):
        assert secret == b"fixture-secret"
        return {"schema": "auto-switch-q4-r9-evidence/v1", "runtime": RUNTIME,
                "collector_sha256": RUNTIME["collector_sha256"],
                "health": {"status": 200, "candidate_id": RUNTIME["candidate_id"]},
                "models": {"status": 200, "candidate_id": RUNTIME["candidate_id"], "model": RUNTIME["model"]},
                "completion": {"status": 200, "candidate_id": RUNTIME["candidate_id"], "model": RUNTIME["model"],
                               "connection_id": RUNTIME["connection_id"], "request_count": 1,
                               "request_id": "11111111-1111-4111-8111-111111111111", "content_bytes": 1}}

    def stop(self):
        self.stopped = True
        return True


RUNTIME = {"schema": "auto-switch-q4-r9-runtime/v1", "host": "192.0.2.9", "candidate_id": "a" * 64,
           "image_sha256": "b" * 64, "command_sha256": "c" * 64, "collector_sha256": "d" * 64,
           "endpoint": "http://127.0.0.1:20129/v1", "model": "lm-studio/qwen3.8-27b-unsloth-ud-q4ks",
           "connection_id": "da74225c-0fc0-45ce-ad22-ded85edb34b8", "request_sha256": "e" * 64,
           "runtime_sha256": hashlib.sha256(b"fixture-reviewed-runtime-v1").hexdigest()}


class Q4R9Test(unittest.TestCase):
    def test_manifest_approval_and_single_spent_execution_are_bound_to_fresh_files(self):
        launcher = load(LAUNCHER, "q4_r9_launcher")
        helper = load(HELPER, "q4_r9_helper")
        sources = launcher.source_bytes()
        manifest = launcher.source_manifest(sources)
        self.assertEqual(manifest["schema"], "auto-switch-q4-r9-source/v1")
        self.assertEqual(manifest["helper_sha256"], hashlib.sha256(sources[launcher.HELPER]).hexdigest())
        action = {"schema": "auto-switch-q4-r9-action/v1", "source_manifest": manifest, "runtime": RUNTIME,
                  "state_leaf": "q4-r9-state.json", "terminal_leaf": "q4-r9-terminal.json"}
        raw = launcher.canonical(action)
        approval = {"schema": "auto-switch-q4-r9-approval/v1", "verdict": "PASS",
                    "model": "gpt-5.6-sol", "effort": "high",
                    "reviewed_payload_sha256": hashlib.sha256(raw).hexdigest(),
                    **{key: manifest[key] for key in launcher.APPROVAL_HASH_FIELDS}}
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            payload, review, key = root / "payload.json", root / "approval.json", root / "key"
            payload.write_bytes(raw)
            review.write_bytes(launcher.canonical(approval))
            key.write_bytes(b"fixture-secret\n")
            request = launcher.approved_request(payload, review, sources)
            self.assertEqual(request["action"], action)
            self.assertEqual(request["action_bytes"], raw)
            self.assertEqual(request["approval_bytes"], launcher.canonical(approval))
            self.assertEqual(request["source_bundle"]["launcher"], sources[launcher.SELF])
            runtime = Runtime()
            self.assertEqual(helper.execute(request, runtime, key), 0)
            state = json.loads((root / action["state_leaf"]).read_text())
            terminal = json.loads((root / action["terminal_leaf"]).read_text())
            self.assertEqual(state, {"schema": "auto-switch-q4-r9-state/v1", "status": "Q4_R9_UNKNOWN", "gate_spent": True})
            self.assertEqual(terminal["status"], "Q4_R9_PASS")
            self.assertTrue(runtime.started and runtime.stopped)
            with self.assertRaises(FileExistsError):
                helper.execute(request, Runtime(), key)
            altered = copy.deepcopy(request)
            altered["action"]["state_leaf"] = "q4-r9-altered-state.json"
            altered["action"]["terminal_leaf"] = "q4-r9-altered-terminal.json"
            with self.assertRaises(ValueError):
                helper.execute(altered, Runtime(), key)
            noncanonical = raw + b"\n"
            bad_approval = {**approval, "reviewed_payload_sha256": hashlib.sha256(noncanonical).hexdigest()}
            with self.assertRaises(ValueError):
                launcher.approved_request_bytes(noncanonical, launcher.canonical(bad_approval), sources)
            uncertain_action = {**action, "state_leaf": "q4-r9-uncertain-state.json", "terminal_leaf": "q4-r9-uncertain-terminal.json"}
            uncertain_raw = launcher.canonical(uncertain_action)
            uncertain_approval = {**approval, "reviewed_payload_sha256": hashlib.sha256(uncertain_raw).hexdigest()}
            class UncertainRuntime(Runtime):
                def start(self): raise OSError("lost start response")
            uncertain = UncertainRuntime()
            self.assertEqual(helper.execute(launcher.approved_request_bytes(uncertain_raw, launcher.canonical(uncertain_approval), sources), uncertain, key), 1)
            self.assertTrue(uncertain.stopped)
            self.assertTrue((root / uncertain_action["state_leaf"]).exists())
            self.assertFalse((root / uncertain_action["terminal_leaf"]).exists())
            bad_action = {**action, "state_leaf": "q4-r9-bad-state.json", "terminal_leaf": "q4-r9-bad-terminal.json"}
            bad_raw = launcher.canonical(bad_action)
            bad_approval = {**approval, "reviewed_payload_sha256": hashlib.sha256(bad_raw).hexdigest()}
            class BooleanProof(Runtime):
                def authenticate(self, secret, action): return {"health_http_status": 200, "selected_q4": True, "content_valid": True}
            self.assertEqual(helper.execute(launcher.approved_request_bytes(bad_raw, launcher.canonical(bad_approval), sources), BooleanProof(), key), 1)
            self.assertTrue((root / bad_action["state_leaf"]).exists())
            self.assertFalse((root / bad_action["terminal_leaf"]).exists())
        changed = dict(sources)
        changed[launcher.HELPER] += b"# changed\n"
        with self.assertRaises(ValueError):
            launcher.approved_request_bytes(raw, launcher.canonical(approval), changed)


if __name__ == "__main__":
    unittest.main()
