"""Exact Docker lifecycle program for the later reviewed Q4 R9 action."""
import json
import subprocess
import sys
import time


def frames(raw):
    values = []
    while raw:
        if len(raw) < 8:
            raise ValueError("frame")
        size = int.from_bytes(raw[:8], "big")
        raw = raw[8:]
        if size > 1048576 or len(raw) < size:
            raise ValueError("frame")
        values.append(raw[:size])
        raw = raw[size:]
    return values


def command(argv, timeout):
    result = subprocess.run(argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, timeout=timeout, check=False)
    if result.returncode or len(result.stdout) > 1048576 or len(result.stderr) > 4096:
        raise RuntimeError("command")
    return result.stdout


def inspect(config):
    rows = json.loads(command([config["docker_path"], "container", "inspect", config["candidate_id"]], 20))
    if not isinstance(rows, list) or len(rows) != 1:
        raise ValueError("inspect")
    row = rows[0]
    if (row.get("Id") != config["candidate_id"] or row.get("Name") != "/" + config["candidate_name"]
            or row.get("Image") != "sha256:" + config["image_sha256"]):
        raise ValueError("identity")
    return row


def main():
    mode = sys.argv[1] if len(sys.argv) == 2 else ""
    action_raw, command_raw = frames(sys.stdin.buffer.read())
    action, config = json.loads(action_raw), json.loads(command_raw)
    keys = {"schema", "docker_path", "candidate_name", "candidate_id", "image_sha256",
            "health_attempts", "health_interval_ms"}
    runtime = action.get("runtime", {})
    if (mode not in {"start", "stop"} or set(config) != keys
            or config.get("schema") != "auto-switch-q4-r9-runtime-command/v1"
            or config["candidate_id"] != runtime.get("candidate_id")
            or config["image_sha256"] != runtime.get("image_sha256")
            or config["docker_path"] != "/usr/bin/docker"
            or type(config["health_attempts"]) is not int or not 1 <= config["health_attempts"] <= 60
            or type(config["health_interval_ms"]) is not int or not 100 <= config["health_interval_ms"] <= 5000):
        return 1
    row = inspect(config)
    if mode == "start":
        if row.get("State", {}).get("Running") is not False:
            return 1
        command([config["docker_path"], "container", "start", config["candidate_id"]], 60)
        for _ in range(config["health_attempts"]):
            state = inspect(config).get("State", {})
            if state.get("Running") is True and state.get("Health", {}).get("Status") == "healthy":
                return 0
            time.sleep(config["health_interval_ms"] / 1000)
        return 1
    if row.get("State", {}).get("Running") is True:
        command([config["docker_path"], "container", "stop", "--time", "10", config["candidate_id"]], 30)
    state = inspect(config).get("State", {})
    return 0 if state.get("Running") is False and state.get("OOMKilled") is False else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception:
        raise SystemExit(1)
