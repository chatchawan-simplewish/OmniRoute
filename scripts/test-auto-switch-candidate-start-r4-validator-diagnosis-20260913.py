"""Local-only reproduction of the spent R4 PASS-validator defect."""
import copy
import inspect
import pathlib
import runpy


CANDIDATE = pathlib.Path(r"C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-candidate-r4-20260913")
LAUNCHER = CANDIDATE / "scripts/auto-switch-candidate-start-r4-20260913.py"
module = runpy.run_path(str(LAUNCHER), run_name="candidate_r4_validator_diagnosis")

genuine = {
    "status": "CANDIDATE_START_R4_PASS", "candidate_id": "a" * 64,
    "candidate_image": module["CANDIDATE_IID"],
    "candidate_volume": "omniroute-auto-switch-candidate-data-r4-20260913",
    "network_none": True, "published_ports": 0, "health": True, "cloud_false": True,
    "db_bytes": 4096, "provider_rows": 5, "encrypted_fields": 18, "plain_fields": 0,
    "empty_fields": 2, "key_value_rows_before": 30, "key_value_rows_after": 30,
    "user_version_before": 171, "user_version_after": 171,
    "route_runs_before": 0, "route_runs_after": 0,
    "route_turns_before": 0, "route_turns_after": 0,
    "route_events_before": 0, "route_events_after": 0,
    "migration_170": True, "migration_171": True, "deferred_requests_column": True,
    "health_probe_attempts": 1, "health_probe_timeouts": 0, "health_probe_nonzero": 0,
    "health_probe_successes": 1, "health_deadline_expired": False,
    "health_container_stopped": False, "health_last_probe_category": "success",
}

try:
    module["validate_result"](genuine, 0)
    raise AssertionError("spent validator unexpectedly accepted a genuine PASS shape")
except KeyError as error:
    assert error.args == ("route_runsbefore",)

source = inspect.getsource(module["validate_result"])
source = source.replace('value[name + "before"]', 'value[name + "_before"]')
source = source.replace('value[name + "after"]', 'value[name + "_after"]')
namespace = {"re": module["re"], "CANDIDATE_IID": module["CANDIDATE_IID"]}
exec(source, namespace)
assert namespace["validate_result"](genuine, 0) == genuine

inconsistent = copy.deepcopy(genuine)
inconsistent["health_probe_attempts"] = 99
assert namespace["validate_result"](inconsistent, 0) == inconsistent
print("PASS: exact R4 PASS-validator KeyError reproduced; health-counter acceptance gap reproduced")
