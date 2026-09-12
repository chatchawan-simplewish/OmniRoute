"""Read-only VM1205 metadata. Never emits environment or credential values."""
import json
import pathlib
import sqlite3
import subprocess
import sys


def command(args):
    result = subprocess.run(args, capture_output=True, text=True, timeout=20)
    if result.returncode:
        raise RuntimeError("COMMAND_FAILED")
    return result.stdout


def discover():
    ids = command(["docker", "ps", "--filter", "publish=20128", "--format", "{{.ID}}"] ).split()
    if len(ids) != 1:
        raise RuntimeError("PRIMARY_COUNT_NOT_ONE")
    item = json.loads(command(["docker", "inspect", ids[0]]))[0]
    env = {entry.partition("=")[0]: bool(entry.partition("=")[2])
           for entry in item.get("Config", {}).get("Env", [])}
    mounts = item.get("Mounts", [])
    data = [m for m in mounts if m.get("Destination") == "/app/data"]
    if len(data) != 1 or data[0].get("Type") != "volume":
        raise RuntimeError("DATA_VOLUME_NOT_ONE")
    path = pathlib.Path(data[0]["Source"]) / "storage.sqlite"
    if not path.is_file():
        raise RuntimeError("DATABASE_MISSING")
    # URI read-only mode; no credential-bearing column is selected.
    db = sqlite3.connect(path.as_uri() + "?mode=ro", uri=True)
    try:
        db.execute("PRAGMA query_only=ON")
        tables = {row[0] for row in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        result = {
            "container_id": item["Id"], "container_name": item["Name"].lstrip("/"),
            "image_id": item["Image"], "running": item["State"]["Running"],
            "health": item["State"].get("Health", {}).get("Status", "unknown"),
            "data_volume": data[0]["Name"],
            "networks": sorted(item["NetworkSettings"]["Networks"]),
            "inference_env_present": env.get("OMNIROUTE_API_KEY", False),
            "router_env_present": env.get("ROUTER_API_KEY", False),
            "agent_route_tables": sorted(t for t in tables if t.startswith("agent_route")),
            "credential_table_names": sorted(t for t in tables if t in ("api_keys", "access_tokens", "management_tokens")),
        }
        if "api_keys" in tables:
            result["api_key_count"] = db.execute("SELECT count(*) FROM api_keys").fetchone()[0]
        print(json.dumps(result, sort_keys=True))
    finally:
        db.close()


if __name__ == "__main__":
    try:
        discover()
    except Exception as exc:
        # Do not emit subprocess stderr, SQL values, or arbitrary exception text.
        allowed = {"COMMAND_FAILED", "PRIMARY_COUNT_NOT_ONE", "DATA_VOLUME_NOT_ONE", "DATABASE_MISSING"}
        reason = str(exc) if type(exc) is RuntimeError and str(exc) in allowed else type(exc).__name__
        print(json.dumps({"status": "DISCOVERY_FAILED", "reason": reason}))
        sys.exit(1)
