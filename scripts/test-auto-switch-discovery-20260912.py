"""Offline check: discovery excludes secrets and rejects ambiguous targets."""
import contextlib
import importlib.util
import io
import json
import pathlib
import sqlite3
import tempfile

spec = importlib.util.spec_from_file_location("discovery", pathlib.Path(__file__).with_name("auto-switch-discovery-20260912.py"))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
with tempfile.TemporaryDirectory() as directory:
    db = sqlite3.connect(pathlib.Path(directory) / "storage.sqlite")
    db.execute("CREATE TABLE api_keys (id TEXT, scopes TEXT, key TEXT)")
    db.execute("INSERT INTO api_keys VALUES ('fixture-id', '[]', 'DO_NOT_EMIT_FIXTURE_SECRET')")
    db.commit()
    db.close()
    fixture = {"Id": "fixture-container", "Name": "/fixture", "Image": "fixture-image",
               "Config": {"Env": ["OMNIROUTE_API_KEY=DO_NOT_EMIT_FIXTURE_SECRET"]},
               "State": {"Running": True}, "NetworkSettings": {"Networks": {}},
               "Mounts": [{"Destination": "/app/data", "Type": "volume", "Source": directory, "Name": "fixture-volume"}]}
    module.command = lambda args: "fixture-container" if args[1] == "ps" else json.dumps([fixture])
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        module.discover()
    value = json.loads(output.getvalue())
    assert "DO_NOT_EMIT" not in output.getvalue()
    assert value["inference_env_present"] is True
    assert value["api_key_count"] == 1
    assert "api_key_metadata" not in value
    module.command = lambda args: "first second"
    try:
        module.discover()
    except RuntimeError as exc:
        assert str(exc) == "PRIMARY_COUNT_NOT_ONE"
    else:
        raise AssertionError("ambiguous target accepted")
print("PASS: secret exclusion and ambiguous-target rejection")
