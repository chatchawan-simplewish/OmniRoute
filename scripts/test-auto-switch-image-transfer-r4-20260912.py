"""Offline regression checks for R4 remote role elevation and absence proof."""
import importlib.util
import pathlib
import subprocess
import sys
import contextlib
import io
import json
from types import SimpleNamespace
from unittest.mock import patch

script = pathlib.Path(__file__).with_name("auto-switch-image-transfer-r4-20260912.py")
spec = importlib.util.spec_from_file_location("transfer_R4", script)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Execute the generated helper definitions only, without any remote operation.
source = module.REMOTE.split("\ntry:\n", 1)[0]
namespace = {}
with patch.object(sys, "argv", ["remote", "target-preflight", "none", "0", "none", module.IID, module.TAG, "/tmp/r2"]):
    exec(compile(source, "remote", "exec"), namespace)

for role, expected in (("builder", ["docker"]), ("target-preflight", ["sudo", "-n", "docker"]),
                       ("target-load", ["sudo", "-n", "docker"])):
    namespace["role"] = role
    calls = []
    namespace["cmd"] = lambda args, timeout=120: calls.append(args) or ""
    namespace["docker"](["info"])
    assert calls == [expected + ["info"]]

namespace["role"] = "target-preflight"
namespace["cmd"] = lambda args, timeout=120: ""
missing = lambda args, **kwargs: subprocess.CompletedProcess(args, 1, b"[]\n", b"Error response from daemon: No such image: " + args[-1].encode())
with patch.object(namespace["subprocess"], "run", missing):
    namespace["absent"]()
unexpected = lambda args, **kwargs: subprocess.CompletedProcess(args, 1, b"[]\n", b"permission denied")
with patch.object(namespace["subprocess"], "run", unexpected):
    try:
        namespace["absent"]()
    except AssertionError:
        pass
    else:
        raise AssertionError("unexpected Docker inspect error must stop")
assert "assert size==int(expected_size) and sha==expected_sha" in module.REMOTE
assert "capacity(size)" not in module.REMOTE.split("if role=='builder':", 1)[1].split("elif role=='target-preflight':", 1)[0]
assert module.ARCHIVE_BYTES == 1117870592
assert module.ARCHIVE_SHA256 == "ef45e7734e64280cbe9ca9bbbd8a950f350c028c50e9b02c55ab0e48801abb15"
assert 'assert size==int(expected_size) and sha==expected_sha' in module.REMOTE
assert module.review_payload()["archive_sha256"] == module.ARCHIVE_SHA256
assert module.review_payload()["root_result_sha256"] == module.ROOT_RESULT_SHA256
compile(module.root_script_bytes(), "root_probe", "exec")
compile("root_script=" + repr(module.root_script_bytes()) + "\n" + module.REMOTE, "payload", "exec")

# Any accidental transition from read-only preflight to a mutation fails here.
local = SimpleNamespace(exists=lambda: False, is_symlink=lambda: False,
                        mkdir=lambda **kwargs: (_ for _ in ()).throw(AssertionError("mkdir reached")))
for target_ok in (True, False):
    responses = [{"size": module.ARCHIVE_BYTES, "sha256": module.ARCHIVE_SHA256},
                 {"containerd_path_proven": target_ok}]
    output = io.StringIO()
    with patch.object(module, "verify_review"), patch.object(module, "LOCAL", local), \
         patch.object(module, "remote", side_effect=responses) as remote_mock, \
         patch.object(module, "verify_archive_with_helper") as archive_mock, \
         patch.object(module.shutil, "disk_usage", return_value=SimpleNamespace(free=1 << 40)), \
         patch.object(module, "run", side_effect=AssertionError("copy/load reached")), \
         contextlib.redirect_stdout(output):
        try:
            module.execute(pathlib.Path("unused-pins"), preflight_only=True)
        except module.Stop:
            assert not target_ok
        else:
            assert target_ok
            assert json.loads(output.getvalue())["status"] == "IMAGE_TRANSFER_R4_PREFLIGHT_PASS"
        assert remote_mock.call_count == 2 and archive_mock.call_count == 1

with patch.object(module.subprocess, "run", return_value=subprocess.CompletedProcess([], 1,
                  b'{"stop":"containerd_source_runtime_match"}', b'not for output')):
    try:
        module.run("target_preflight", [])
    except module.Stop as error:
        assert str(error) == "target_preflight:containerd_source_runtime_match"
    else:
        raise AssertionError("remote failure was ignored")
print("IMAGE_TRANSFER_R4_LOCAL_CHECK_PASS")
