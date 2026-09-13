"""Focused offline boundary checks for the R1 actual-hardware qualification source."""
import copy
import pathlib
import runpy


ROOT = pathlib.Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "scripts/auto-switch-hardware-qualification-r1-20260913.py"

assert LAUNCHER.is_file(), "hardware qualification launcher missing"
module = runpy.run_path(str(LAUNCHER), run_name="hardware_qualification_r1_test")
assert module["EXECUTION_READY"] is False
assert module["SOURCE"] == "e53d895e9a5e38a7f06ce59de254835f10e829c1"
assert module["IMAGE"] == "sha256:8211e1071a3b68eac01673d76129150eb0c0fea329dd222bc8bf0394b13fc844"
assert module["CANDIDATE_NAME"] == "omniroute-auto-switch-candidate-r4-20260913"
assert module["CANDIDATE_ID"] == "UNBOUND"
assert module["KEY_ID"] == "UNBOUND"
assert module["require_bound"]() == [
    "candidate_id", "candidate_reconciliation_result_sha256", "candidate_key_id",
    "candidate_key_result_sha256", "candidate_key_store",
]

good = module["fixture_result"]()
assert module["validate_result"](good, 0, module["FIXTURE_CANDIDATE_ID"]) == good
prep = {"status": "HARDWARE_PREP_PASS", "stage": "complete",
        "candidate_id": module["FIXTURE_CANDIDATE_ID"], "candidate_stopped": True,
        "companion_id": "e" * 64, "detail_baseline": 0, "network_private": True,
        "published_ports": 0, "cloud_false": True, "codex_inactive": True,
        "migration_170": True, "migration_171": True, "key_policy": True,
        "health_counters": {"attempts": 3, "timeouts": 1, "nonzero": 1, "successes": 1}}
assert module["validate_prep"](prep, 0, module["FIXTURE_CANDIDATE_ID"]) == prep
assert module["emitted_fields"](module["render_prep"]().decode("utf-8"), "HARDWARE_PREP_PASS") == set(prep)

remote = {name: False for name in (
    "environment_checked", "historical_startup_reconstructed", "database_checked", "native_health_checked")}
remote.update({name: True for name in (
    "candidate_present", "volume_present", "candidate_running", "can_enter_hardware_preflight_without_restart",
    "identity_verified", "image_verified", "volume_verified", "network_none", "published_ports_zero",
    "user_node", "mount_exact", "readonly_root", "cap_drop_all", "no_new_privileges", "restart_no",
    "tmpfs_hardened", "live_unchanged", "retained_candidates_unchanged")})
remote.update(status="CANDIDATE_RECONCILE_R1_PASS", candidate_id=module["FIXTURE_CANDIDATE_ID"],
              candidate_image=module["IMAGE"], candidate_volume=module["CANDIDATE_VOLUME"],
              source_revision=module["SOURCE"], state_status="running", docker_health_status="healthy")
reconciliation = {"schema": "auto-switch-candidate-reconcile-r1-result/v1", "status": "PASS",
                  "stage": "complete", "remote": remote}
validator_globals = module["validate_reconciliation_receipt"].__globals__
validator_globals["CANDIDATE_ID"] = module["FIXTURE_CANDIDATE_ID"]
assert module["validate_reconciliation_receipt"](reconciliation) == reconciliation
bad_reconciliation = copy.deepcopy(reconciliation)
bad_reconciliation["remote"]["database_checked"] = True
try:
    module["validate_reconciliation_receipt"](bad_reconciliation)
except module["Stop"]:
    pass
else:
    raise AssertionError("reconciliation overclaim accepted")
validator_globals["CANDIDATE_ID"] = "UNBOUND"

def rejected(mutator):
    value = copy.deepcopy(good)
    mutator(value)
    try:
        module["validate_result"](value, 0, module["FIXTURE_CANDIDATE_ID"])
    except module["Stop"]:
        return
    raise AssertionError("invalid hardware result accepted")

rejected(lambda value: value.update(candidate_id="0" * 64))
rejected(lambda value: value["requests"][2].update(q6_submissions=1))
rejected(lambda value: value["requests"][2].update(q4_http_status=530, content_valid=False))
rejected(lambda value: value["requests"][2].update(q4_selected_ms=5001))
rejected(lambda value: value["metrics_before_third"].update(processing=1))
rejected(lambda value: value["metrics_before_third"].update(deferred=1))
rejected(lambda value: value["health_counters"].update(attempts=99))
rejected(lambda value: value["correlation"].update(complete=False))
rejected(lambda value: value["final_metrics"].update(processing=1))

module["offline_check"]()
print("PASS: R1 hardware identity, Q6 saturation, Q4 completion, timing, metrics and correlation boundaries")
