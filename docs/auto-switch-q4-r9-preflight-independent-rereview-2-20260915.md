# Q4 R9 descriptor preflight independent rereview 2

Verdict: **BLOCK — DO NOT AUTHORIZE THE PREFLIGHT**

Fix commit reviewed: `cf9ecaed16fb65df6fabab0a3cbb7e15f10319f3`

Prior BLOCK artifact commit: `fea27a0bfa47e87f72496b6fcfbc8669df6d4b54`

Scope was limited to the exact four-file fix diff and all eight current additive package files. Current OmniRoute source and schema were read only to verify the caller-session persistence contract. No live resource was contacted and no SSH, rendering, credential, Docker, HTTP, or consuming mode was executed.

## Current additive package

| File | SHA-256 |
| --- | --- |
| `docs/auto-switch-q4-r9-preflight-contract-20260915.md` | `b3b22069db48b094040d2280bb2f24cf285e9c3ad1bd62b263bae2bd3adc6601` |
| `scripts/auto-switch-q4-r9-collector-template-20260915.py` | `46fb9bdc20135d867f22a8a80adab4a6214b25580900c26415b6004744526365` |
| `scripts/auto-switch-q4-r9-command-template-20260915.json` | `be89ae6ec7711169f683ee95f5d1dfe25f1f96e180ba572986d13fe605dcf10b` |
| `scripts/auto-switch-q4-r9-preflight-20260915-test.py` | `644544eac29b53cd6d7c8468d87bc9bc37e80e63ced69558f09fee7515ef8891` |
| `scripts/auto-switch-q4-r9-preflight-20260915.py` | `d87603d4593c6e6c028ae0865686f1e0d0c97ec2db69962ce6a1ad5d2f82f16c` |
| `scripts/auto-switch-q4-r9-preflight-bootstrap-20260915.py` | `02713bc45a3fd636530de715f580478ee57220a0b4a6aff144daa629dc12fa7a` |
| `scripts/auto-switch-q4-r9-request-template-20260915.json` | `a464080c8bba3b2f2803ad28583580d96bae1803e53f855f300bf00389bddb76` |
| `scripts/auto-switch-q4-r9-runtime-template-20260915.py` | `bea23833c5732d716e5807b590a948a285381b6fc22e771aace473da02be102d` |

## Blocking finding

1. **The retained package contract contradicts the fixed collector.** The contract still states that the collector queries the exact server-returned OmniRoute log ID. The fixed collector no longer uses `x-omniroute-request-id`; it sends the caller UUID in `X-OmniRoute-Session-Id` and queries `call_logs WHERE session_tag=?`. Because the contract is one of the eight hashed review inputs, approving the current payload would attest to a false identifier and evidence-flow description. Update only that description to the caller-supplied UUID persisted in `session_tag`, regenerate the package hash, and obtain a fresh independent rereview.

## Prior blocking finding closure

1. **Request/log correlation: SOURCE CLOSED.** Current OmniRoute captures the explicit `x-omniroute-session-id` header separately from its internal `skillRequestId`, threads it into every `persistAttemptLogs` call, and passes it to `saveCallLog` as `sessionTag` (`open-sse/handlers/chatCore.ts` lines 860-910 and `open-sse/handlers/chatCore/attemptLogging.ts` lines 141-179, 234-279). `saveCallLog` inserts that value into `call_logs.session_tag`; migration 133 and the idempotent schema guard create the column and index (`src/lib/usage/callLogs.ts` lines 572-695, `src/lib/db/migrations/133_call_logs_session_tag.sql`, and `src/lib/db/schemaColumns.ts` lines 248-269).

2. **Exact one-row binding: CLOSED.** The renderer normalizes one supplied UUIDv4 into both request headers. The collector requires those values to be identical, sends the explicit session header, and performs an exact equality query. PASS requires exactly one row matching status `200`, method `POST`, path `/v1/chat/completions`, the pinned Q4 model, provider `lm-studio`, and the pinned connection. Zero rows, duplicates, or any field mismatch fail closed; the selected connection is taken from the matched database row, not copied into evidence from the action. The focused regression distinguishes pending, internal skill, and caller request IDs.

## Preserved closures

- **Retained `known_hosts`: CLOSED.** The fix does not change the retained-byte validation, temporary locked file, held-descriptor recheck, cleanup, or strict SSH command. The focused Windows test again proves replacement is denied during transport and the temporary leaf is removed.
- **Candidate endpoint binding: SOURCE CLOSED.** The fix does not change the exact candidate/image/network inspection or the requirement that the observed private IPv4 equal the reviewed endpoint before and through start/stop checks. Runtime-platform proof remains deferred to the later exact-action review/test.
- **UNKNOWN/SPENT: CLOSED.** Receipt reservation still precedes contact, every post-reservation exception retains canonical local `UNKNOWN`, and the consuming helper still reserves `Q4_R9_UNKNOWN` / `gate_spent=true` before secret read or candidate start. No retry, fallback, verdict relaxation, or historic-gate reuse was introduced.

## Checks and disposition

- Inspected the exact `fea27a0b..cf9ecaed` diff, all eight current additive files, the current OmniRoute header-to-attempt-log-to-SQL path, migration/self-heal schema, and the retained R9 launcher/helper contracts.
- `python -B scripts/auto-switch-q4-r9-preflight-20260915-test.py -v`: one test passed offline.
- `python -B scripts/auto-switch-q4-r9-20260915-test.py`: five tests passed, one platform-specific test skipped offline.
- `git diff --check fea27a0bfa47e87f72496b6fcfbc8669df6d4b54 cf9ecaed16fb65df6fabab0a3cbb7e15f10319f3`: passed.
- Do not issue a preflight approval or perform any contact/rendering/consuming action. Correct the stale contract sentence, preserve the now-sound implementation, and obtain another exact-package rereview.
