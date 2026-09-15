"""Direct-byte approval binding for the fresh Q4 R9 qualification gate."""
import hashlib
import json
import pathlib


ROOT = pathlib.Path(__file__).resolve().parents[1]
SELF = pathlib.Path(__file__).resolve()
HELPER = ROOT / "scripts" / "auto-switch-q4-r9-20260915-helper.py"
CONTRACT = ROOT / "docs" / "auto-switch-q4-r9-20260915-contract.md"
TEST = ROOT / "scripts" / "auto-switch-q4-r9-20260915-test.py"
APPROVAL_HASH_FIELDS = ("launcher_sha256", "helper_sha256", "contract_sha256", "test_sha256")


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def source_bytes():
    return {SELF: SELF.read_bytes(), HELPER: HELPER.read_bytes(), CONTRACT: CONTRACT.read_bytes(), TEST: TEST.read_bytes()}


def source_manifest(sources=None):
    sources = source_bytes() if sources is None else sources
    return {"schema": "auto-switch-q4-r9-source/v1",
            "launcher_sha256": hashlib.sha256(sources[SELF]).hexdigest(),
            "helper_sha256": hashlib.sha256(sources[HELPER]).hexdigest(),
            "contract_sha256": hashlib.sha256(sources[CONTRACT]).hexdigest(),
            "test_sha256": hashlib.sha256(sources[TEST]).hexdigest()}


def approved_request_bytes(payload_raw, approval_raw, sources):
    action, approval = json.loads(payload_raw), json.loads(approval_raw)
    manifest = source_manifest(sources)
    if action.get("schema") != "auto-switch-q4-r9-action/v1" or action.get("source_manifest") != manifest:
        raise ValueError("unbound action")
    if approval.get("schema") != "auto-switch-q4-r9-approval/v1" or approval.get("verdict") != "PASS":
        raise ValueError("unapproved action")
    if approval.get("model") != "gpt-5.6-sol" or approval.get("effort") != "high":
        raise ValueError("wrong reviewer")
    if approval.get("reviewed_payload_sha256") != hashlib.sha256(payload_raw).hexdigest():
        raise ValueError("payload drift")
    if any(approval.get(field) != manifest[field] for field in APPROVAL_HASH_FIELDS):
        raise ValueError("source drift")
    return {"schema": "auto-switch-q4-r9-request/v1", "action": action, "approval": approval,
            "source_manifest": manifest}


def approved_request(payload_path, approval_path, sources=None):
    sources = source_bytes() if sources is None else sources
    return approved_request_bytes(pathlib.Path(payload_path).read_bytes(), pathlib.Path(approval_path).read_bytes(), sources)
