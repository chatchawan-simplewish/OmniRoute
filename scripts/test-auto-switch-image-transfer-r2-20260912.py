"""Offline regression checks for R2 remote role elevation and absence proof."""
import importlib.util
import pathlib
import subprocess
import sys
from unittest.mock import patch

script = pathlib.Path(__file__).with_name("auto-switch-image-transfer-r2-20260912.py")
spec = importlib.util.spec_from_file_location("transfer_r2", script)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Execute the generated helper definitions only, without any remote operation.
source = module.REMOTE.split("\nif role=='builder':", 1)[0]
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
print("IMAGE_TRANSFER_R2_LOCAL_CHECK_PASS")
