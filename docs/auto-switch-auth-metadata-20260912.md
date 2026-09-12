# Read-only authentication metadata diagnosis

Owner: task `01a09361-8143-73d3-adb7-15043355276b`, source branch `codex/omniroute-auto-switch-20260912`. Status: PREPARED; independent Sol High review is required before execution. This is a new read-only diagnostic and does not reuse or relax any earlier gate.

## Purpose and authority boundary

The reviewed direct `GET /v1/models` returned 401 when sent the existing `OMNIROUTE_ADMIN_TOKEN`, while the management MCP transport accepts that configured credential. Current source has separate authentication branches: client API routes validate deployment or persisted API keys; management routes can also accept scoped CLI access tokens or bypass ordinary login when `requireLogin=false`. This diagnostic distinguishes those persisted metadata branches without inference, credential creation, key rotation, settings changes or service changes.

The Windows wrapper reads the exact configured environment reference and bearer locally. It computes SHA-256 over the token's UTF-8 bytes, matching `src/lib/db/apiKeys.ts::hashKey` and `src/lib/db/accessTokens.ts::hashAccessToken`. The bearer never enters argv, SSH command text, files, stdout or stderr. Only its one-way digest is placed in a JSON frame on strict-known-host SSH stdin to VM1205. The digest is used only as a bound SQLite equality parameter and is never emitted or stored. No HTTP request or token transmission occurs in this step.

## Exact live target and read boundary

Before opening the database, the remote payload requires the sole running container publishing port 20128 and revalidates all accepted discovery pins:

- container name `omniroute` and ID `7b20ca195e3c9e875d0a1ce98832ca469c2a114886335b8466b1467b3ed139bc`;
- image ID `sha256:60ab56311d1c9873416dc53683148d314465370312547b8ce87c442ce084c6a5`;
- running state true; and
- exactly one `/app/data` named-volume mount, `omniroute-data-mcp-audit-20260910-r3`.

It opens only that volume's `storage.sqlite` using SQLite URI `mode=ro`, immediately enables `PRAGMA query_only=ON`, and issues fixed schema/count/equality reads. It never imports application code, selects `api_keys.key`, emits a stored hash, ID, name, prefix, timestamp or scopes array, or reads configuration files, logs, usage, provider credentials or routing rows. Missing `api_keys.key_hash` support or any missing/malformed API-key hash is fail-closed as NOT PROVEN; it is never treated as proof that the current bearer is absent. Missing or malformed CLI-token schema is also not treated as a valid credential.

Allowed success fields are exactly:

- `require_login`: `true`, `false`, `missing` or `invalid`;
- `require_api_key_db_override`: `true`, `false`, `missing` or `invalid`;
- `token_starts_oma`, `api_key_hash_supported`, and `cli_token_table_present`: booleans;
- `api_key_unhashed_count`, `api_key_match_count`, and `cli_token_match_count`: nonnegative integers or null;
- `api_key_lifecycle_valid`, `api_key_manage_or_admin_scope`, `api_key_mcp_connect_scope`, `cli_token_hash_coverage_complete`, and `cli_token_lifecycle_valid`: booleans or null; and
- `cli_token_scope`: `read`, `write`, `admin`, `none`, `invalid`, `ambiguous` or `not_proven`.

No row metadata beyond these reductions is evidence-authorized. The local wrapper accepts exactly one JSON output line with exactly these keys and suppresses remote stderr and arbitrary exception text.

## Interpretation limits

A lifecycle-valid `api_keys.key_hash` match explains client API validity; its management-scope booleans show whether it could also authorize MCP under the applicable peer/path branch. A lifecycle-valid CLI-token hash match plus local `token_starts_oma=true` explains management-only acceptance and the `/v1/models` rejection. `require_login=false` establishes the ordinary management login bypass is enabled, but does not by itself prove which branch served an earlier request. Nulls, malformed hash coverage, multiple matches, pin drift or schema drift are NOT PROVEN. The DB override is not the complete effective `REQUIRE_API_KEY` value when absent because environment/default precedence remains outside this SQLite read. No result proves inference, upstream provider health, routing-marker deployment or client cutover readiness.

## Fail-closed behavior and rollback

Stop on configuration mismatch, absent/malformed local bearer, missing local SSH files, host-key mismatch, unavailable passwordless sudo, timeout, container/image/volume drift, zero or multiple port-20128 containers, database/schema mismatch, unexpected output fields or any nonzero SSH status. Do not repair, retry, fall back to an old gate or broaden selected columns. This diagnostic has no deliberate mutation, so no rollback is required; normal filesystem access metadata or SQLite read-side implementation activity is not claimed as application-state mutation.

An offline self-check is available as `python scripts/auto-switch-auth-metadata-20260912.py --self-check`. It performs no SSH/network action and checks target/config pin rejection plus strict output-field exclusion using a secret sentinel. The independent reviewer may inspect or run only this offline mode before reviewing exact source and contract hashes. The live default mode must remain unexecuted until that review returns PASS.

## Exact invocation after independent review

Run from this coordinator worktree in PowerShell using the currently resolved local Python interpreter:

```powershell
python scripts/auto-switch-auth-metadata-20260912.py
```

The wrapper itself invokes exact Windows OpenSSH `C:\WINDOWS\System32\OpenSSH\ssh.exe` with `-F none -T`, identity `C:\Users\chatc\.ssh\codex-prox01-vms-ed25519`, `IdentitiesOnly=yes`, `BatchMode=yes`, `StrictHostKeyChecking=yes`, `UserKnownHostsFile=C:/Users/chatc/.ssh/known_hosts`, `GlobalKnownHostsFile=none`, `HostKeyAlias=192.168.1.68`, bounded connection/server-alive settings, and fixed target `belladmin@192.168.1.68`. The fixed remote command is `sudo -n python3 -c <reviewed launcher>`; source and digest travel only in the framed stdin payload. Evidence is the sanitized single-line stdout, exit status, and reviewed hashes. Never capture or publish the stdin frame.
