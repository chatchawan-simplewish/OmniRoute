"""One metadata GET using the existing MCP bearer; no inference or secret output."""
import http.client
import json
import os
import pathlib
import sys
import tomllib
from urllib.parse import urlsplit


def validate_entry(entry):
    url = urlsplit(entry.get("url", ""))
    if (url.scheme, url.hostname, url.port, url.path) != ("http", "192.168.1.68", 20128, "/api/mcp/stream") or url.username is not None or url.password is not None or url.query or url.fragment:
        raise ValueError("target mismatch")
    if entry.get("bearer_token_env_var") != "OMNIROUTE_ADMIN_TOKEN":
        raise ValueError("credential reference mismatch")


def main():
    config = tomllib.loads(pathlib.Path(r"C:\Users\chatc\.codex\config.toml").read_text(encoding="utf-8"))
    entry = config.get("mcp_servers", {}).get("omniroute-admin", {})
    validate_entry(entry)
    token = os.environ.get("OMNIROUTE_ADMIN_TOKEN", "")
    if not token or token.lower().startswith("bearer ") or "\r" in token or "\n" in token:
        raise ValueError("bearer unavailable")
    connection = http.client.HTTPConnection("192.168.1.68", 20128, timeout=10)
    try:
        connection.request("GET", "/v1/models", headers={"Authorization": "Bearer " + token, "Accept": "application/json"})
        response = connection.getresponse()
        # Never follow redirects, log headers/bodies, or retry the GET.
        body = response.read(8 * 1024 * 1024 + 1)
        result = {"http_status": response.status}
        if len(body) <= 8 * 1024 * 1024 and response.status == 200:
            data = json.loads(body).get("data", [])
            ids = {item.get("id") for item in data if isinstance(item, dict) and isinstance(item.get("id"), str)}
            result.update(model_count=len(ids), normal_alias_present="agent/normal" in ids, high_alias_present="agent/high" in ids)
        print(json.dumps(result, sort_keys=True))
    finally:
        connection.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(json.dumps({"status": "AUTH_READ_FAILED", "reason": type(exc).__name__}))
        sys.exit(1)
