"""Offline credential-reference and destination pin checks; no network."""
import importlib.util
import pathlib

spec = importlib.util.spec_from_file_location("auth_read", pathlib.Path(__file__).with_name("auto-switch-auth-read-20260912.py"))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
good = {"url": "http://192.168.1.68:20128/api/mcp/stream", "bearer_token_env_var": "OMNIROUTE_ADMIN_TOKEN"}
module.validate_entry(good)
for changed in (
    {"bearer_token_env_var": "UNRELATED_SECRET"},
    {"url": "http://user@192.168.1.68:20128/api/mcp/stream"},
    {"url": good["url"] + "?token=fixture"},
    {"url": good["url"] + "#fixture"},
    {"url": "http://192.168.1.69:20128/api/mcp/stream"},
):
    try:
        module.validate_entry(good | changed)
    except ValueError:
        continue
    raise AssertionError("drift accepted")
print("PASS: credential reference and destination pins")
