"""Read-only auth metadata diagnosis for the pinned VM1205 OmniRoute runtime."""
import hashlib
import json
import os
import pathlib
import shlex
import subprocess
import sys
import tomllib
from urllib.parse import urlsplit


SSH = pathlib.Path(r"C:\WINDOWS\System32\OpenSSH\ssh.exe")
IDENTITY = pathlib.Path(r"C:\Users\chatc\.ssh\codex-prox01-vms-ed25519")
KNOWN_HOSTS = pathlib.Path(r"C:\Users\chatc\.ssh\known_hosts")
EXPECTED_ENV = "OMNIROUTE_ADMIN_TOKEN"

REMOTE_SCRIPT = r'''
import datetime
import json
import pathlib
import sqlite3
import subprocess

EXPECTED_CONTAINER_ID = "7b20ca195e3c9e875d0a1ce98832ca469c2a114886335b8466b1467b3ed139bc"
EXPECTED_IMAGE_ID = "sha256:60ab56311d1c9873416dc53683148d314465370312547b8ce87c442ce084c6a5"
EXPECTED_VOLUME = "omniroute-data-mcp-audit-20260910-r3"


def command(args):
    result = subprocess.run(args, capture_output=True, text=True, timeout=20)
    if result.returncode:
        raise RuntimeError("COMMAND_FAILED")
    return result.stdout


def enum_json_boolean(value):
    if value is None:
        return "missing"
    try:
        parsed = json.loads(value)
    except (TypeError, ValueError):
        return "invalid"
    if parsed is True:
        return "true"
    if parsed is False:
        return "false"
    return "invalid"


def enum_flag(value):
    if value is None:
        return "missing"
    if value in ("true", "1", "yes"):
        return "true"
    if value in ("false", "0", "no"):
        return "false"
    return "invalid"


def parse_scopes(value):
    if not isinstance(value, str) or not value.strip():
        return []
    try:
        parsed = json.loads(value)
    except (TypeError, ValueError):
        return []
    return [item for item in parsed if isinstance(item, str)] if isinstance(parsed, list) else []


def timestamp_expired(value, now):
    if not isinstance(value, str) or not value.strip():
        return False
    try:
        parsed = datetime.datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=datetime.timezone.utc)
        return parsed <= now
    except ValueError:
        # Node Date.parse treats an invalid timestamp as not expired.
        return False


def api_key_valid(row, now):
    is_active, is_banned, revoked_at, expires_at, _scopes = row
    active = is_active not in (0, "0", False)
    banned = is_banned in (1, "1", True)
    revoked = isinstance(revoked_at, str) and bool(revoked_at.strip())
    return active and not banned and not revoked and not timestamp_expired(expires_at, now)


def remote_main(digest):
    if not isinstance(digest, str) or len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
        raise ValueError("DIGEST_INVALID")

    ids = command(["docker", "ps", "--filter", "publish=20128", "--format", "{{.ID}}"] ).split()
    if len(ids) != 1:
        raise RuntimeError("PRIMARY_COUNT_NOT_ONE")
    item = json.loads(command(["docker", "inspect", ids[0]]))[0]
    if item.get("Id") != EXPECTED_CONTAINER_ID or item.get("Image") != EXPECTED_IMAGE_ID:
        raise RuntimeError("RUNTIME_PIN_MISMATCH")
    if item.get("Name", "").lstrip("/") != "omniroute" or item.get("State", {}).get("Running") is not True:
        raise RuntimeError("RUNTIME_PIN_MISMATCH")

    mounts = item.get("Mounts", [])
    data = [m for m in mounts if m.get("Destination") == "/app/data"]
    if len(data) != 1 or data[0].get("Type") != "volume" or data[0].get("Name") != EXPECTED_VOLUME:
        raise RuntimeError("VOLUME_PIN_MISMATCH")
    path = pathlib.Path(data[0]["Source"]) / "storage.sqlite"
    if not path.is_file():
        raise RuntimeError("DATABASE_MISSING")

    db = sqlite3.connect(path.as_uri() + "?mode=ro", uri=True)
    try:
        db.execute("PRAGMA query_only=ON")
        tables = {row[0] for row in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        if not {"api_keys", "key_value"}.issubset(tables):
            raise RuntimeError("SCHEMA_MISMATCH")

        api_columns = {row[1] for row in db.execute("PRAGMA table_info(api_keys)")}
        required_api = {"key_hash", "is_active", "is_banned", "revoked_at", "expires_at", "scopes"}
        api_hash_supported = required_api.issubset(api_columns)
        api_unhashed_count = None
        api_rows = []
        if api_hash_supported:
            api_unhashed_count = db.execute(
                "SELECT count(*) FROM api_keys WHERE key_hash IS NULL OR length(key_hash) <> 64 OR key_hash GLOB '*[^0-9a-f]*'"
            ).fetchone()[0]
            api_rows = db.execute(
                "SELECT is_active, is_banned, revoked_at, expires_at, scopes FROM api_keys WHERE key_hash = ?",
                (digest,),
            ).fetchall()

        now = datetime.datetime.now(datetime.timezone.utc)
        api_lifecycle_valid = None
        api_manage_or_admin = None
        api_mcp_connect = None
        if api_hash_supported and api_unhashed_count == 0:
            api_lifecycle_valid = len(api_rows) == 1 and api_key_valid(api_rows[0], now)
            scopes = parse_scopes(api_rows[0][4]) if len(api_rows) == 1 else []
            api_manage_or_admin = any(scope in ("manage", "admin") for scope in scopes) if len(api_rows) == 1 else False
            api_mcp_connect = "mcp:connect" in scopes if len(api_rows) == 1 else False

        cli_present = "cli_access_tokens" in tables
        cli_hash_coverage_complete = None
        cli_rows = []
        if cli_present:
            cli_columns = {row[1] for row in db.execute("PRAGMA table_info(cli_access_tokens)")}
            required_cli = {"token_hash", "scope", "revoked_at", "expires_at"}
            if not required_cli.issubset(cli_columns):
                raise RuntimeError("SCHEMA_MISMATCH")
            malformed = db.execute(
                "SELECT count(*) FROM cli_access_tokens WHERE token_hash IS NULL OR length(token_hash) <> 64 OR token_hash GLOB '*[^0-9a-f]*'"
            ).fetchone()[0]
            cli_hash_coverage_complete = malformed == 0
            cli_rows = db.execute(
                "SELECT scope, revoked_at, expires_at FROM cli_access_tokens WHERE token_hash = ?", (digest,)
            ).fetchall()

        cli_lifecycle_valid = None
        cli_scope = "not_proven"
        if cli_present and cli_hash_coverage_complete:
            if len(cli_rows) == 0:
                cli_lifecycle_valid = False
                cli_scope = "none"
            elif len(cli_rows) == 1:
                scope, revoked_at, expires_at = cli_rows[0]
                revoked = isinstance(revoked_at, str) and bool(revoked_at.strip())
                cli_lifecycle_valid = not revoked and not timestamp_expired(expires_at, now)
                cli_scope = scope if scope in ("read", "write", "admin") else "invalid"
            else:
                cli_lifecycle_valid = False
                cli_scope = "ambiguous"

        require_login_row = db.execute(
            "SELECT value FROM key_value WHERE namespace='settings' AND key='requireLogin'"
        ).fetchone()
        require_key_row = db.execute(
            "SELECT value FROM key_value WHERE namespace='feature_flags' AND key='REQUIRE_API_KEY'"
        ).fetchone()
        result = {
            "require_login": enum_json_boolean(require_login_row[0] if require_login_row else None),
            "require_api_key_db_override": enum_flag(require_key_row[0] if require_key_row else None),
            "token_starts_oma": False,
            "api_key_hash_supported": api_hash_supported,
            "api_key_unhashed_count": api_unhashed_count,
            "api_key_match_count": len(api_rows) if api_hash_supported else None,
            "api_key_lifecycle_valid": api_lifecycle_valid,
            "api_key_manage_or_admin_scope": api_manage_or_admin,
            "api_key_mcp_connect_scope": api_mcp_connect,
            "cli_token_table_present": cli_present,
            "cli_token_hash_coverage_complete": cli_hash_coverage_complete,
            "cli_token_match_count": len(cli_rows) if cli_present else None,
            "cli_token_lifecycle_valid": cli_lifecycle_valid,
            "cli_token_scope": cli_scope,
        }
        print(json.dumps(result, sort_keys=True))
    finally:
        db.close()
'''

REMOTE_LAUNCHER = r'''import json,sys
p=json.load(sys.stdin)
if set(p) != {"source","digest"}: raise ValueError("FRAME_INVALID")
ns={"__name__":"auth_metadata_remote"}
exec(compile(p["source"],"<auth-metadata>","exec"),ns)
ns["remote_main"](p["digest"])
'''

RESULT_KEYS = {
    "require_login", "require_api_key_db_override", "token_starts_oma",
    "api_key_hash_supported", "api_key_unhashed_count", "api_key_match_count",
    "api_key_lifecycle_valid", "api_key_manage_or_admin_scope", "api_key_mcp_connect_scope",
    "cli_token_table_present", "cli_token_hash_coverage_complete", "cli_token_match_count",
    "cli_token_lifecycle_valid", "cli_token_scope",
}


def validate_entry(entry):
    if not isinstance(entry, dict):
        raise ValueError("entry mismatch")
    url = urlsplit(entry.get("url", ""))
    target = (url.scheme, url.hostname, url.port, url.path)
    if target != ("http", "192.168.1.68", 20128, "/api/mcp/stream"):
        raise ValueError("target mismatch")
    if url.username is not None or url.password is not None or url.query or url.fragment:
        raise ValueError("target mismatch")
    if entry.get("bearer_token_env_var") != EXPECTED_ENV:
        raise ValueError("credential reference mismatch")


def validate_result(value):
    if not isinstance(value, dict) or set(value) != RESULT_KEYS:
        raise ValueError("result shape mismatch")
    if value["require_login"] not in {"true", "false", "missing", "invalid"}:
        raise ValueError("result value mismatch")
    if value["require_api_key_db_override"] not in {"true", "false", "missing", "invalid"}:
        raise ValueError("result value mismatch")
    if value["cli_token_scope"] not in {"read", "write", "admin", "none", "invalid", "ambiguous", "not_proven"}:
        raise ValueError("result value mismatch")
    boolean_or_none = {
        "api_key_lifecycle_valid", "api_key_manage_or_admin_scope", "api_key_mcp_connect_scope",
        "cli_token_hash_coverage_complete", "cli_token_lifecycle_valid",
    }
    boolean_only = {"token_starts_oma", "api_key_hash_supported", "cli_token_table_present"}
    count_or_none = {"api_key_unhashed_count", "api_key_match_count", "cli_token_match_count"}
    if any(type(value[key]) is not bool for key in boolean_only):
        raise ValueError("result value mismatch")
    if any(value[key] is not None and type(value[key]) is not bool for key in boolean_or_none):
        raise ValueError("result value mismatch")
    if any(value[key] is not None and (type(value[key]) is not int or value[key] < 0) for key in count_or_none):
        raise ValueError("result value mismatch")
    return value


def self_check():
    good = {"url": "http://192.168.1.68:20128/api/mcp/stream", "bearer_token_env_var": EXPECTED_ENV}
    validate_entry(good)
    for bad in (
        {**good, "url": "http://192.168.1.69:20128/api/mcp/stream"},
        {**good, "url": "http://user@192.168.1.68:20128/api/mcp/stream"},
        {**good, "bearer_token_env_var": "ANOTHER_SECRET"},
    ):
        try:
            validate_entry(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("pin mismatch accepted")
    fixture = {
        "require_login": "true", "require_api_key_db_override": "true", "token_starts_oma": False,
        "api_key_hash_supported": True, "api_key_unhashed_count": 0, "api_key_match_count": 0,
        "api_key_lifecycle_valid": False, "api_key_manage_or_admin_scope": False,
        "api_key_mcp_connect_scope": False, "cli_token_table_present": True,
        "cli_token_hash_coverage_complete": True, "cli_token_match_count": 0,
        "cli_token_lifecycle_valid": False, "cli_token_scope": "none",
    }
    sanitized = json.dumps(validate_result(fixture), sort_keys=True)
    if "DO_NOT_EMIT_FIXTURE_SECRET" in sanitized:
        raise AssertionError("secret emitted")
    try:
        validate_result({**fixture, "secret": "DO_NOT_EMIT_FIXTURE_SECRET"})
    except ValueError:
        pass
    else:
        raise AssertionError("unexpected field accepted")
    print(json.dumps({"status": "SELF_CHECK_PASS"}))


def main():
    config_path = pathlib.Path(r"C:\Users\chatc\.codex\config.toml")
    config = tomllib.loads(config_path.read_text(encoding="utf-8"))
    entry = config.get("mcp_servers", {}).get("omniroute-admin", {})
    validate_entry(entry)
    token = os.environ.get(EXPECTED_ENV, "")
    if not token or token.lower().startswith("bearer ") or "\r" in token or "\n" in token:
        raise ValueError("bearer unavailable")
    digest = hashlib.sha256(token.encode("utf-8")).hexdigest()

    for required in (SSH, IDENTITY, KNOWN_HOSTS):
        if not required.is_file():
            raise FileNotFoundError("required local file missing")
    remote_command = "sudo -n python3 -c " + shlex.quote(REMOTE_LAUNCHER)
    args = [
        str(SSH), "-F", "none", "-T", "-i", str(IDENTITY),
        "-o", "IdentitiesOnly=yes", "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=yes",
        "-o", "UserKnownHostsFile=C:/Users/chatc/.ssh/known_hosts", "-o", "GlobalKnownHostsFile=none",
        "-o", "HostKeyAlias=192.168.1.68", "-o", "ConnectTimeout=10", "-o", "ConnectionAttempts=1",
        "-o", "ServerAliveInterval=10", "-o", "ServerAliveCountMax=2",
        "belladmin@192.168.1.68", remote_command,
    ]
    frame = json.dumps({"source": REMOTE_SCRIPT, "digest": digest}, separators=(",", ":"))
    completed = subprocess.run(args, input=frame, capture_output=True, text=True, timeout=45)
    if completed.returncode != 0:
        raise RuntimeError("REMOTE_READ_FAILED")
    lines = completed.stdout.splitlines()
    if len(lines) != 1:
        raise ValueError("remote output mismatch")
    result = validate_result(json.loads(lines[0]))
    # This local-only classification is useful to interpret the management access-token branch.
    result["token_starts_oma"] = token.startswith("oma_")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    try:
        if sys.argv[1:] == ["--self-check"]:
            self_check()
        elif sys.argv[1:]:
            raise ValueError("unexpected argument")
        else:
            main()
    except Exception as exc:
        print(json.dumps({"status": "AUTH_METADATA_FAILED", "reason": type(exc).__name__}))
        sys.exit(1)
