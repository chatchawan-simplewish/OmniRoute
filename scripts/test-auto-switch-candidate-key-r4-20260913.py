"""Focused offline boundaries for the unbound R4 native qualification-key source."""
import copy
import ast
import importlib.util
import json
import pathlib
import subprocess
import tempfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "scripts/auto-switch-candidate-key-r4-20260913.py"

assert LAUNCHER.is_file(), "R4 qualification-key launcher missing"
spec = importlib.util.spec_from_file_location("candidate_key_r4", LAUNCHER)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.EXECUTION_READY is True
assert module.SOURCE == "e53d895e9a5e38a7f06ce59de254835f10e829c1"
assert module.IMAGE == "sha256:8211e1071a3b68eac01673d76129150eb0c0fea329dd222bc8bf0394b13fc844"
assert module.CANDIDATE_NAME == "omniroute-auto-switch-candidate-r4-20260913"
assert module.CANDIDATE_VOLUME == "omniroute-auto-switch-candidate-data-r4-20260913"
assert module.CANDIDATE_ID == "9468859edcdb483c53900edde14d301a162cccc791079154677e913f39bf26a3"
assert module.RECONCILIATION_RESULT_SHA256 == "7efe1cb83cc1c5c6cf85199b919338bb2a6143054d9a6cd315e0c3270fc213cf"
assert module.require_bound() == []

runtime = ROOT.parent / "omniroute-auto-switch-matrix-20260913"
native = subprocess.run(["node", "--import", "tsx", "-e", module.native_roundtrip_probe()],
                        cwd=runtime, capture_output=True, timeout=90)
assert native.returncode == 0, (len(native.stdout), len(native.stderr))
native_result = json.loads(native.stdout.decode("utf-8").strip().splitlines()[-1])
assert native_result == {"create_status": 201, "patch_status": 200, "get_status": 200,
                         "missing_fields": [], "extra_fields": [], "mismatch_fields": [],
                         "db_ip_allowlist_is_null": True}

rendered = module.render_remote("oma_fixture_secret", module.CANDIDATE_ID)
compiled = ast.parse(rendered)
imports = {alias.name for node in compiled.body if isinstance(node, ast.Import) for alias in node.names}
assert {"subprocess", "threading", "time"}.issubset(imports)
assert b"oma_fixture_secret" not in rendered
assert rendered.count(b"if not key_id or rollback_attempted:return") == 1

good = module.fixture_result()
assert module.validate_result(good, 0, module.FIXTURE_CANDIDATE_ID) == good

def rejected(mutator):
    value = copy.deepcopy(good)
    mutator(value)
    try:
        module.validate_result(value, 0, module.FIXTURE_CANDIDATE_ID)
    except module.Stop:
        return
    raise AssertionError("invalid R4 key result accepted")

rejected(lambda value: value.update(candidate_id="0" * 64))
rejected(lambda value: value.update(allowed_models=13))
rejected(lambda value: value.update(no_log=False))
rejected(lambda value: value.update(db_ip_allowlist_is_null=False))
rejected(lambda value: value.update(candidate_running=False))
rejected(lambda value: value.update(migration_171=False))

receipt = module.parse_receipt(module.RECONCILIATION_RESULT)
assert module.validate_reconciliation(receipt, module.CANDIDATE_ID) == receipt
bad_receipt = copy.deepcopy(receipt)
bad_receipt["remote"]["native_health_checked"] = True
try:
    module.validate_reconciliation(bad_receipt, module.CANDIDATE_ID)
except module.Stop:
    pass
else:
    raise AssertionError("overclaimed reconciliation accepted")

module.offline_check()

with tempfile.TemporaryDirectory() as temporary:
    module.RESULT = pathlib.Path(temporary) / "result.md"
    descriptor = module.reserve_result()
    module.finish_result(descriptor, {"schema": module.RESULT_SCHEMA, "status": "UNKNOWN", "stage": "transport", "remote": None})
    assert json.loads(module.RESULT.read_text("utf-8"))["status"] == "UNKNOWN"
    try:
        module.reserve_result()
    except module.Stop as error:
        assert str(error) == "stale_result"
    else:
        raise AssertionError("existing result reservation accepted")

print("PASS: R4 key identity, reconciliation, native policy, protected store and terminal receipt")
