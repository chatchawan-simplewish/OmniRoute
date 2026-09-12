"""Read only fixed client identity/status fields; never opens client configuration."""
import json
import os
import pathlib
import subprocess
import sys


def read(args):
    result = subprocess.run(args, capture_output=True, text=True, timeout=10)
    return result.stdout.strip() if result.returncode == 0 else None


def discover(role):
    if role == "hermes":
        repository = "/home/hermes/.hermes/hermes-agent"
        service = ["systemctl", "--user", "show", "hermes-agent.service"]
    elif role == "deepseek":
        repository = "/opt/deepseek-harness"
        service = ["systemctl", "show", "deepseek-harness.service"]
    else:
        raise ValueError("invalid role")
    head = read(["git", "--no-optional-locks", "-C", repository, "rev-parse", "HEAD"])
    if head is not None and (len(head) != 40 or any(c not in "0123456789abcdef" for c in head)):
        head = None
    status = read(["git", "--no-optional-locks", "-C", repository, "status", "--porcelain", "--untracked-files=no"])
    result = {"role": role, "uid": os.getuid(), "repository_exists": pathlib.Path(repository).is_dir(),
              "head": head, "tracked_clean": status == "" if status is not None else None}
    for field in ("ActiveState", "SubState"):
        value = read(service + ["--property=" + field, "--value"])
        allowed = {"active", "inactive", "failed", "activating", "deactivating", "running", "dead", "exited", "auto-restart"}
        result[field] = value if value in allowed else "unknown"
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    try:
        discover(sys.argv[1])
    except Exception as exc:
        print(json.dumps({"status": "DISCOVERY_FAILED", "reason": type(exc).__name__}))
        sys.exit(1)
