"""Offline check: only approved metadata crosses the output boundary."""
import contextlib
import importlib.util
import io
import json
import pathlib

spec = importlib.util.spec_from_file_location("client_discovery", pathlib.Path(__file__).with_name("auto-switch-client-discovery-20260912.py"))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
module.os.getuid = lambda: 1000
calls = []
def fixture_read(args):
    calls.append(args)
    return "DO_NOT_EMIT_PRIVATE_TEXT"
module.read = fixture_read
output = io.StringIO()
with contextlib.redirect_stdout(output):
    module.discover("hermes")
value = json.loads(output.getvalue())
assert "DO_NOT_EMIT" not in output.getvalue()
assert value["head"] is None and value["tracked_clean"] is False
assert value["ActiveState"] == "unknown" and value["SubState"] == "unknown"
assert all(args[1] == "--no-optional-locks" for args in calls if args[0] == "git")
assert len([args for args in calls if args[0] == "git"]) == 2
try:
    module.discover("unapproved")
except ValueError:
    pass
else:
    raise AssertionError("unapproved role accepted")
print("PASS: client metadata output and role boundaries")
