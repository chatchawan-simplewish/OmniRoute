# Candidate qualification key R5 contract — 20260913

**Status: SOURCE PREPARATION ONLY; `execution_ready=false`.** This revision is a fresh successor to spent R4. It authorizes no SSH, Docker, credential, API, key, provider, inference, container, network, or cleanup action. Independent Sol High review is required before the repeatable read-only preflight. A preflight PASS must then be saved, hashed, bound into a new reviewed source revision and reviewed pins before one explicit coordinator dispatch may create R5.

## Frozen target and evidence

The only target is R4 candidate `omniroute-auto-switch-candidate-r4-20260913`, historical reconciled ID `9468859edcdb483c53900edde14d301a162cccc791079154677e913f39bf26a3`, image `sha256:8211e1071a3b68eac01673d76129150eb0c0fea329dd222bc8bf0394b13fc844`, source `e53d895e9a5e38a7f06ce59de254835f10e829c1`, and volume `omniroute-auto-switch-candidate-data-r4-20260913`. The accepted reconciliation R2 receipt SHA-256 is `7efe1cb83cc1c5c6cf85199b919338bb2a6143054d9a6cd315e0c3270fc213cf`; it is historical evidence and does not replace current preflight. Spent startup, reconciliation R1 and key R4 bytes/results remain immutable and are never invoked.

The fresh key name is `auto-switch-candidate-qualification-r5-20260913`; the only store is `/root/.omniroute-qualification/auto-switch-candidate-qualification-r5-20260913.key`. The result is `docs/auto-switch-candidate-key-r5-result-20260913.md`. All remain absent during source preparation.

## Repeatable read-only preflight

`--preflight` revalidates the exact candidate twice by name and ID, exact image/tag/source, running and healthy state, network-none isolation, zero ports, sole local volume, hardened user/root/tmpfs/capability/security/restart settings, exact live-container identity, canonical volume mountpoint and regular database. It performs SQLite URI `mode=ro`, `query_only`, `quick_check`, exact route-table columns, `cloudEnabled=false`, and aggregate credential classification `encrypted=18`, `plain=0`, `empty=34`.

Migration rows must use the native loader representation: `('170','agent_route_runs')` and `('171','agent_route_deferred_metrics')`. The source regression reads these rows from the accepted `e53d895` runtime migration loader; fixtures may not substitute filename-prefixed names.

The preflight reads the bounded stable no-follow `server.env` only to require exact nonempty names `STORAGE_ENCRYPTION_KEY`, `JWT_SECRET`, `API_KEY_SECRET`, plus optional `STORAGE_ENCRYPTION_KEY_VERSION`, with owner/group `1000:1000` and mode `0600`. It verifies the protected parent through a held no-follow directory descriptor and requires the R5 store absent. Using the existing management token only in memory and SSH stdin, it performs GET-only native schema checks for `/api/keys`, `/api/combos`, and the exact Codex connection; it requires R5 key-name and sentinel absence, exact response shapes, no token fields, and Codex inactive. It emits only the candidate ID and fixed named booleans. It never POSTs, PATCHes, creates a file, or changes candidate state. Transport failure is an observation failure and makes no mutation claim.

## One-shot creation, still unbound

After a separately accepted preflight is bound, the future reviewed execution must repeat the same identity, database, environment, store and native GET predicates before mutation. It creates exactly one R5 key, PATCHes exactly once, and exhaustively GETs the exact 14 models, five connections, sentinel no-combo, empty quotas, `noLog=true`, `autoResolve=false`, scope `agent:route`, endpoints `chat,models`, SQL-null IP allowlist and all fixed restrictive defaults. It requires the exact native field sets, patch echo, masked key, prefix/hash metadata, inactive Codex connection and native migration rows.

The secret exists only in the candidate native process, remote root memory and the designated store. Store publication uses one held root-owned `0700` parent descriptor, `O_EXCL|O_NOFOLLOW`, owner `0:0`, mode `0600`, stable inode checks and leaf/parent fsync. No secret value, response body, environment list, or raw stderr is emitted.

## Failure and evidence

An authoritative native failure after a returned key ID may perform one compensating PATCH to deactivate that exact R5 key and one GET readback. The enclosing process never repeats rollback. Child timeout, bounded-output failure, stderr, malformed envelope, or unvalidated response after dispatch is terminal `UNKNOWN`: candidate, key, store and rollback fields remain null, with no retry or cleanup. A stable store is removed only after authoritative failure and exact inode verification through the held parent descriptor, then the parent is fsynced. Every attempted creation is spent.

Preparation verification is limited to the focused R5 test, launcher `--self-check`, Python compilation and diff-check. The test runs the accepted runtime's native migration loader and disposable key roundtrip, the complete rendered remote PASS path with native migration rows, the same rendered read-only preflight path, and post-create timeout/output/malformed UNKNOWN cases. It uses no live resource. A future PASS proves only key policy/storage on the isolated candidate; it does not prove provider generation, Q4/Q6 hardware behavior, client routing, DNS, gateway cutover, or live migration.
