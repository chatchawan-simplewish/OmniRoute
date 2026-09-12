# Authentication metadata diagnostic result

Execution owner: `/root/authority_audit` (sole Sol High owner). Execution: 2026-09-12 Asia/Bangkok. Verdict: PASS for the single reviewed read-only diagnostic. No retry, fallback, old gate, inference or mutation was performed.

Immediately before execution, exact pins matched:

- script SHA-256 `ea0a986a83c318a224887d2280559ba67798751fd757dbd83c250bed7aeea6dc`;
- contract SHA-256 `527836c5b1bd60e8cf4d56042c029f2862cf05fe8a8aaf3f7adb7f29b893ae6b`.

Default invocation exit status: `0`. Sanitized result:

```json
{
  "api_key_hash_supported": true,
  "api_key_lifecycle_valid": false,
  "api_key_manage_or_admin_scope": false,
  "api_key_match_count": 0,
  "api_key_mcp_connect_scope": false,
  "api_key_unhashed_count": 0,
  "cli_token_hash_coverage_complete": true,
  "cli_token_lifecycle_valid": true,
  "cli_token_match_count": 1,
  "cli_token_scope": "admin",
  "cli_token_table_present": true,
  "require_api_key_db_override": "missing",
  "require_login": "true",
  "token_starts_oma": true
}
```

The configured MCP bearer is a lifecycle-valid persisted `oma_` CLI access token with `admin` scope. It is not a persisted inference API key: the current digest matched zero `api_keys.key_hash` rows, hash support is present, and there are zero unhashed/malformed API-key rows. `requireLogin` is stored true, so ordinary login-disabled management bypass does not explain MCP acceptance. This accounts for management MCP success and the reviewed `/v1/models` 401 under the separate client-API key validator.

The `REQUIRE_API_KEY` database override is absent; this read does not resolve its environment/default source independently. The result does not prove inference, provider health, routing deployment or client readiness, and it does not authorize reusing the admin CLI token as a client/inference credential.
