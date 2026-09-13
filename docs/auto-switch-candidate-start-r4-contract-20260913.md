# Offline OmniRoute candidate clone/start R4 contract — 2026-09-13

**Status: PREPARATION ONLY; NOT EXECUTABLE.** Exact launcher, contract, dependency and result-schema bytes require fresh independent Sol High review and a new reviewed-pins file before one explicit coordinator dispatch. This source task has no live-resource or consuming-gate authority.

## Exact candidate and evidence pins

Use accepted source `e53d895e9a5e38a7f06ce59de254835f10e829c1`, image IID `sha256:8211e1071a3b68eac01673d76129150eb0c0fea329dd222bc8bf0394b13fc844`, and singleton tag `omniroute-auto-switch-r3:e53d895e9a5e38a7f06ce59de254835f10e829c1`. Require completed transfer receipt `docs/auto-switch-image-transfer-r3-result-20260913.md`, SHA-256 `1146ddb26372878193223babc726db9764f367d41604660760b0640f6003261f`, including the exact IID/tag and `IMAGE_TRANSFER_PASS`.

The launcher lives in the isolated source worktree but may read only these hash-pinned coordinator dependencies: bindings `c30aa56eba04d15a50c766a20ba44e88792c60bcddbdf25670fafd5955286e58`; bounded strict-SSH helper `scripts/auto-switch-image-transfer-r3-20260913.py` SHA-256 `78bb97e57d6229aae84c2f0d0caaf68eeb71ba6b92e69415d83af2a869b8224a`; R1 start result `cd9dcb70213a9280859e15e1ef06054623ef1cd9559eb5b276773227018ecf48`; R1 diagnosis result `0cf8c9052fc90a9f3e3613bd96cce0c6c71c50b72ebb075a1f63a3ce462481f0`; R2 start result `5a3a134390414f34f8670c39361926c6463aa46f6d5b60781099020c70ef2535`; R3 start result `be622186c4f63a901d626f0ca7e7e5442ebc418e0babc3458874189d37c72aad`; and startup root-cause evidence `4332de225d868dc78b382c604f678d3b2c5a7d07c3d6af6ee287b70892b195a5`. Action-time pins must equal the exact launcher, contract and every dependency hash before SSH.

Before any mutation, require the live `omniroute` container ID `7b20ca195e3c9e875d0a1ce98832ca469c2a114886335b8466b1467b3ed139bc`, image `sha256:60ab56311d1c9873416dc53683148d314465370312547b8ce87c442ce084c6a5`, running state, and sole local read-write volume `omniroute-data-mcp-audit-20260910-r3` at `/app/data`. Require retained R1, R2 and R3 candidates to have their exact IDs, names, local volumes, old IID `sha256:a91994bf883698d4520ff048d16be999d4614331a528c76c0b95bc6dc8bec803`, stopped state and sole read-write `/app/data` mount. They are inspect-only and must never be started, stopped, removed, mounted or modified.

Create only fresh absent container `omniroute-auto-switch-candidate-r4-20260913` and local volume `omniroute-auto-switch-candidate-data-r4-20260913`. Never reuse, overwrite or clean an earlier candidate or result.

## Clone, secrets and migration

Validate the exact live volume Name, Driver `local`, Scope `local`, canonical mountpoint and regular non-symlink database/server.env before root reads. Use SQLite URI `mode=ro`, `query_only`, `quick_check`, and native SQLite backup into the fresh private candidate volume. Never mount the live volume into the candidate or modify it.

Read only the exact persisted `STORAGE_ENCRYPTION_KEY` and optional canonical version from bounded stable-FD `server.env`, plus exact live `JWT_SECRET` and `API_KEY_SECRET` from the already pinned Docker inspect response. Keep values only in the remote root process and candidate `server.env`; create it exclusive, no-follow, owner `1000:1000`, mode `0600`, and never put secrets in Docker arguments/environment, SSH arguments, Windows, stdout/stderr, tests, review artifacts or result evidence. Set clone-only `cloudEnabled` to JSON false before startup and preserve aggregate provider/credential/key-value counts.

The accepted image must apply exact migrations `170_agent_route_runs` and `171_agent_route_deferred_metrics`. After startup require the exact migration records, the three route tables and their required columns, and nullable `agent_route_events.deferred_requests`. Preserve the pre-start counts of `agent_route_runs`, `agent_route_turns`, and `agent_route_events`, along with provider rows, credential-field classes, key-value rows, and `PRAGMA user_version`. Emit only booleans and aggregate non-secret counts.

## Isolation, startup and bounded process handling

Create R4 as user `node`, network `none`, no published ports, read-only root, bounded hardened `/tmp`, all capabilities dropped, `no-new-privileges`, restart `no`, sole candidate-volume mount, exact bindings, and the accepted nonsecret disable allowlist. `OMNIROUTE_DISABLE_BACKGROUND_SERVICES` must be canonical `true`; keep the accepted credential-health disable value `1`. Do not call management, provider, inference, OAuth, routing, key, DNS, client or gateway endpoints.

Every local and nested remote child uses the exact hash-pinned helper's concurrent bounded collector: stdout at most 1 MiB, stderr at most 64 KiB, deadline including stdin delivery, terminate then kill, and bounded joins. The local SSH invocation inherits the normal Windows environment, including `PROGRAMDATA`; no minimal/custom environment is used. The total transport deadline is 480 seconds. Docker actions are bounded to 30 or 60 seconds; each native loopback health probe is bounded to 15 seconds inside one 180-second monotonic deadline, with the accepted 12-second timeout cooldown and two-second nonzero delay.

Start only R4 once. Require native health exit zero plus exact running and isolation reinspection, then read-only SQLite integrity, cloud-false, migration/schema, and aggregate-preservation checks. Success reports fixed status, exact candidate identity/volume, isolation booleans, migration booleans, health counters and aggregate database counts only.

## Failure and claim boundary

On a valid remote failure, stop and confirm only the exact R4 candidate once, retain its container and volume, and emit a fixed stage plus sanitized counters. A local timeout, output-bound failure, malformed response or rejected response reports candidate-stopped false because remote state is unknown; do not retry, probe, stop, clean up or fall back. Any attempted invocation is spent regardless of outcome and requires a new reviewed contract for further action.

A later PASS would prove only that the exact transferred image can migrate a private clone and start healthy under network-none isolation while preserving the checked aggregate state. It would not prove decryption, provider generation, Q4 availability, Q6 concurrency, client routing, automatic switching, live migration or gateway cutover.

Preparation checks are limited to `python -B scripts/test-auto-switch-candidate-start-r4-20260913.py`, `python -B scripts/auto-switch-candidate-start-r4-20260913.py --self-check`, and Python compilation. They perform no SSH, Docker, credential, provider or live action. No reviewed pins are created by this source task.
