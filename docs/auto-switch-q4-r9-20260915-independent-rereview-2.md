# Q4 R9 independent source rereview 2

Verdict: **BLOCK**

Fix-round-2 commit reviewed: `7a1fa6ba16c83641a027958fd0a905b8ec317ff8`

Prior rereview: `82e8c3445cad14abcdf61496540738f83d5a5c6d`

Scope was limited to the exact fix-round-2 diff and current committed bytes of the contract, launcher, helper, and focused test. No live resource was contacted and no consuming mode was executed.

## Current source package

| File | SHA-256 |
| --- | --- |
| `docs/auto-switch-q4-r9-20260915-contract.md` | `abdee7b93e832b42f7abbaec5b8972c422642f33b2f42f943eb5c708adff65a2` |
| `scripts/auto-switch-q4-r9-20260915.py` | `eb4cfd17ea48c59364d3a55aaecf1a2017e65ef719055a69db9693930093f131` |
| `scripts/auto-switch-q4-r9-20260915-helper.py` | `19e091fa35e4c4e41cc7774e4b155406e43170899c6b410a8113920780dd3881` |
| `scripts/auto-switch-q4-r9-20260915-test.py` | `4d1742f3201e81b229cc773af096c99f872f183443f871e71d7b237637264a87` |

## Blocking findings

1. **The runtime and operational bytes remain unbound, and the prior runtime check was removed.** `_validate()` no longer calls `runtime.snapshot()` or `runtime.source_bytes()`. It validates only that the action contains syntactically valid digest strings, then hands the approved runtime dictionary to the out-of-band object's `start()` method. That object may ignore the dictionary; the helper never hashes or otherwise derives the runtime, command, collector, or request bytes actually used, and `stop()` is not bound to the approved target. The `runtime_sha256`, `command_sha256`, `collector_sha256`, and `request_sha256` fields therefore remain inert claims. A different runtime can start a different target, fabricate accepted evidence bytes, and report a successful stop. This contradicts the contract statement that the helper compares native runtime/source bytes before reservation (`helper` lines 52-54 and 57-82; contract line 11).

2. **The credential source and leaf parent are still caller-controlled rather than action-pinned.** The approved action is required to contain only the generic strings `leaf_root="."` and `secret_path="key"`. During execution, the helper resolves the separately supplied `secret_path`, derives `root` from that path, and checks only that its basename is `key`; it never resolves or compares an approved absolute parent and never uses `action["leaf_root"]` to select or validate the root. Consequently, `/approved/key` and `/different/key` satisfy the same approved action while reading different credentials and creating different state/terminal leaves. This contradicts the claimed reviewed secret parent, credential-root pin, leaf-root pin, and parent-drift rejection (`helper` lines 49 and 57-65; contract line 7).

3. **Direct authenticated Q4 evidence remains self-reported and is not canonical.** `runtime.authenticate()` supplies all evidence bytes; because the runtime is unbound, it can return a passing document without an authenticated request or Q4 generation. The helper uses `json.loads()` but does not require `evidence_bytes` to equal a canonical encoding, despite the contract's canonical-evidence requirement. It does not independently hash/compare the collector and request bytes actually used or retain the reviewed evidence bytes/hash in the terminal leaf. Matching fields inside a runtime-produced document are not direct proof of the pinned collector request/response (`helper` lines 68-86; contract line 13).

4. **Executing-source binding remains incomplete.** Comparing `Path(__file__).read_bytes()` with the carried helper bytes detects ordinary helper-path drift, but does not execute the helper from those retained bytes and does not bind the already-running launcher to its retained launcher bytes. The current-path reread also cannot prove the loaded Python code came from that file. This does not repair the direct-byte execution gap identified in the prior rereview (`launcher` lines 22-55; `helper` lines 41-43; contract line 7).

## Closed and preserved properties

- Boolean values are now rejected for `request_count` and `content_bytes` by exact `type(...) is int` checks.
- The lost-start-acknowledgement path still attempts one stop in `finally`, retains UNKNOWN/SPENT, and cannot publish PASS.
- Canonical action/approval bytes, exact request/action/approval/manifest/runtime schemas, source-bundle hashes, distinct basename-only R9 leaves, exclusive/fsynced state reservation before secret read, and separate exclusive PASS publication remain enforced.
- The source contains no R8 invocation, receipt lookup, fallback, retry, or reinterpretation of the historic missing R8 invocation. It does not itself log, hash, emit, or put the secret in argv/environment; end-to-end secret safety remains blocked by findings 1 and 2.

## Checks and required disposition

- Reviewed the exact `82e8c344..7a1fa6ba` diff and the four current committed files; recorded their SHA-256 values above.
- Focused offline test not run: the remaining defects follow directly from the accepted interfaces and path logic, while the synthetic runtime is the same self-reporting boundary under review.
- Do not issue source approval, exact-action approval, execution authority, or remote contact. Bind execution to independently retained runtime/command/collector/request bytes, pin and compare the actual credential/leaf parent without exposing secret contents, require canonical direct evidence, and obtain another fresh independent review.
