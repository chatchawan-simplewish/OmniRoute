"""Direct authenticated Q4 collector for the later reviewed Q4 R9 action."""
import http.client
import json
import pathlib
import sqlite3
import sys
import urllib.parse
import uuid


CALL_LOG_DB = pathlib.Path("/var/lib/docker/volumes/omniroute-auto-switch-candidate-data-r4-20260913/_data/storage.sqlite")


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


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


def request(origin, method, path, headers, body=None):
    connection = http.client.HTTPConnection(origin.hostname, origin.port, timeout=15)
    try:
        connection.request(method, path, body=body, headers=headers)
        response = connection.getresponse()
        raw = response.read(65537)
        if len(raw) > 65536:
            raise ValueError("response limit")
        return response.status, {name.lower(): value for name, value in response.getheaders()}, raw
    finally:
        connection.close()


def observed_connection(db_path, request_id, runtime):
    absolute = pathlib.Path(db_path).resolve(strict=True)
    uri = "file:" + urllib.parse.quote(str(absolute).replace("\\", "/"), safe="/:?") + "?mode=ro"
    database = sqlite3.connect(uri, uri=True, timeout=5)
    try:
        database.execute("PRAGMA query_only=ON")
        database.execute("BEGIN")
        rows = database.execute(
            "SELECT status,method,path,model,provider,connection_id FROM call_logs WHERE session_tag=?",
            (request_id,)).fetchall()
    finally:
        database.close()
    expected = (200, "POST", "/v1/chat/completions", runtime.get("model"),
                "lm-studio", runtime.get("connection_id"))
    if len(rows) != 1 or tuple(rows[0]) != expected:
        raise ValueError("selected connection")
    return rows[0][5]


def main():
    action_raw, request_raw, secret = frames(sys.stdin.buffer.read())
    action, spec = json.loads(action_raw), json.loads(request_raw)
    runtime = action.get("runtime", {})
    if (not 1 <= len(secret) <= 4096 or any(char in secret for char in (b"\0", b"\r", b"\n"))
            or set(spec) != {"schema", "headers", "body"}
            or spec.get("schema") != "auto-switch-q4-r9-q4-request/v1"
            or spec.get("body", {}).get("model") != runtime.get("model")
            or set(spec.get("headers", {})) != {"x-omniroute-session-id", "x-request-id"}):
        return 1
    request_id = spec["headers"]["x-request-id"]
    if spec["headers"]["x-omniroute-session-id"] != request_id or uuid.UUID(request_id).version != 4:
        return 1
    origin = urllib.parse.urlsplit(runtime.get("endpoint", ""))
    if (origin.scheme != "http" or origin.port != 20129 or origin.path.rstrip("/") != "/v1"
            or origin.username is not None or origin.password is not None or origin.query or origin.fragment):
        return 1
    token = secret.decode("utf-8")
    headers = {"Accept": "application/json", "Authorization": "Bearer " + token}
    health_status, _, _ = request(origin, "GET", "/api/health/ping", headers)
    models_status, _, models_raw = request(origin, "GET", "/v1/models", headers)
    models = json.loads(models_raw)
    if (health_status != 200 or models_status != 200 or not isinstance(models, dict)
            or runtime["model"] not in {row.get("id") for row in models.get("data", []) if isinstance(row, dict)}):
        return 1
    body_raw = canonical(spec["body"])
    completion_status, meta, completion_raw = request(
        origin, "POST", "/v1/chat/completions",
        {**headers, "Content-Type": "application/json", "X-OmniRoute-Session-Id": request_id,
         "X-Request-Id": request_id}, body_raw)
    completion = json.loads(completion_raw)
    choices = completion.get("choices") if isinstance(completion, dict) else None
    content = choices[0].get("message", {}).get("content") if isinstance(choices, list) and len(choices) == 1 and isinstance(choices[0], dict) else None
    if (completion_status != 200 or not isinstance(content, str) or not content
            or meta.get("x-omniroute-model") != runtime["model"]
            or meta.get("x-omniroute-provider") != "lm-studio"):
        return 1
    selected_connection = observed_connection(CALL_LOG_DB, request_id, runtime)
    evidence = {
        "schema": "auto-switch-q4-r9-evidence/v1", "runtime": runtime,
        "health": {"status": health_status, "candidate_id": runtime["candidate_id"]},
        "models": {"status": models_status, "candidate_id": runtime["candidate_id"], "model": runtime["model"]},
        "completion": {"status": completion_status, "candidate_id": runtime["candidate_id"],
            "model": runtime["model"], "connection_id": selected_connection, "request_count": 1,
            "request_id": request_id, "content_bytes": len(content.encode("utf-8"))},
    }
    secret = b""; token = ""
    sys.stdout.buffer.write(canonical(evidence))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception:
        raise SystemExit(1)
