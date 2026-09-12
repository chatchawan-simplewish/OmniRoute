# Live rollout outline — 2026-09-12

**Status: SOURCE-ONLY OUTLINE; NOT EXECUTABLE.** This describes the smallest final gateway cutover after candidate qualification and independent review. It authorizes no SSH, Docker, database/key/credential operation, provider request, client release, or default change.

## Reuse and non-promotion boundary

- Gateway source/image/binding inputs are `dc53bcfed67b3bbea7d2fbf82468342e573dadb3`, `sha256:a91994bf883698d4520ff048d16be999d4614331a528c76c0b95bc6dc8bec803`, and `docs/auto-switch-bindings-candidate-20260912.json` (SHA-256 `c30aa56eba04d15a50c766a20ba44e88792c60bcddbdf25670fafd5955286e58`). Use `docs/auto-switch-live-discovery-result-20260912.md` for the retained live r3 pins and `docs/auto-switch-provider-qualification-plan-20260912.md` for qualification boundaries.
- The qualification clone, its key, test ledger, and provider/OAuth state are never promoted. Its Codex token can be stale and must not be copied, refreshed, or used as live state. The final replacement starts from a fresh, consistent clone of the current live data only at a separately reviewed exclusive OAuth lifecycle boundary.
- Preserve the current `omniroute` container, image `sha256:60ab56311d1c9873416dc53683148d314465370312547b8ce87c442ce084c6a5`, and volume `omniroute-data-mcp-audit-20260910-r3` unchanged and recoverable. No prune, rename, overwrite, or volume reuse is allowed.

## Preconditions to an executable cutover

The later Sol-owned contract must pin and revalidate: qualified provider/routing evidence; accepted image/source/bindings; the exact live container/image/volume/ports/networks; replacement name/image/user/mounts/environment; effective cloud setting; native health endpoint; and a consistent clone method whose source snapshot identity is recorded without database contents. It must also establish an exclusive OAuth boundary before the clone: no concurrent live or candidate Codex generation/refresh, and a clear stop/resume order. Unknown OAuth freshness, clone consistency, bind conflicts, health, or pin drift is a stop.

The present live discovery found no `agent_route*` tables and no static inference-key environment fallback. Therefore the replacement must prove its migration/schema state before admitting aliases. Native key APIs must create and fully read back a **new final** restricted inference key: `noLog=true`, only `agent:route`, chat/models endpoints, exact final aliases/physical models/connections, no wildcards or quota-pool attachment. The `oma_` management token is not an inference key. Secret material is limited to the reviewed secure delivery path and never appears in argv, env dumps, logs, evidence, or client source.

## Minimal cutover and rollback shape

1. While the old container still runs, perform only action-time read/pin checks and stage the new private clone path; do not touch client defaults.
2. At the exclusive boundary, stop the exact old container once, make the pinned fresh consistent clone, then create the accepted-image replacement using only that clone. Preserve the old container/image/volume as rollback assets. The replacement gets the reviewed listener/network configuration; no qualification test volume or ledger enters this path.
3. Require native health, management authentication, final-key metadata readback, `/v1/models` permission surface, and the already-qualified physical/agent routing evidence against the replacement before any client configuration change. Evidence is sanitized identifiers, status/counters, selected/resolved connection metadata, and absence checks only.
4. On any failed pin, startup, health, authorization, schema, routing, or observed replay/side-effect boundary, stop the replacement and restart the untouched old container with its original volume/image/network/ports. Do not repair in place, retry automatically, or promote the clone. Retain the failed replacement and evidence for a fresh reviewed recovery contract.

## Client acceptance remains a separate live lane

- Hermes: only accepted source `9098efc055a186c862f189022417d9f553b2bee7` on base `693641aa8b4359c602283bdbbc14041e03bc47bc` may be staged after exact VM104 preimage/ownership transfer. Reuse `tests/agent/test_omniroute_protocol.py` and `tests/agent/test_omniroute_steps.py` as offline evidence only. Actual acceptance requires a bounded live `agent/normal` and `agent/high` receipt-correlated run proving caller authorization, durable event ACK, correct selected/resolved route metadata, and no replay-visible output or acknowledged side effect. No VM104 installer/rollback asset exists yet; `scripts/release.py` is GitHub publication only.
- DSH: reuse source/package evidence in `docs/auto-switch-dsh-package-reuse-20260912.md` (V7 source/package pins), but require VM105 owner transfer plus installed-byte, service, profile, key-delivery, and receipt-correlation evidence. The VM105 native bridge/supervisor block remains outside this outline.
- Keep both clients’ existing defaults until each exact-client acceptance passes under its own rollback-capable deployment contract. A successful gateway cutover alone does not authorize their installation, key delivery, or default selection.

## Genuinely unproved conditions

Restricted key R3 passed. Provider qualification R1 stopped before inference and is spent; its separately reviewed R2 replacement was dispatched once on 2026-09-13. No successful provider/routing-matrix result exists yet. The final live clone mechanism, exclusivity proof, listener/port replacement sequence, migration result, final-key secure destinations, and rollback commands remain unproved. VM104 exact-file overlay/rollback is drafted but unbound. VM105 has a separate conditional final-client draft whose native protocol compatibility remains under analysis; installed-runtime/native-bridge authority is excluded. These need concrete reviewed contracts within the standing authority.
