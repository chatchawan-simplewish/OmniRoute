# Q4 R9 independent source rereview

Verdict: **BLOCK**

Fix commit reviewed: `9d93f96b0b2313582cb0199eb925cb4b5a93a605`

Prior BLOCK review: `485699abfdc48813477717baec314d59ca677172`

Scope was limited to the exact fix diff and current committed bytes of the contract, launcher, helper, and focused test. No live resource was contacted and no consuming mode was executed.

## Current source package

| File | SHA-256 |
| --- | --- |
| `docs/auto-switch-q4-r9-20260915-contract.md` | `4eae793445b848c8c71e955c2894b4c474b7fc2785c52a9a6588ea460ac258ec` |
| `scripts/auto-switch-q4-r9-20260915.py` | `4e2a638305e96789c61be2779e66195abec0b940925841debfdbb30b835d8cd9` |
| `scripts/auto-switch-q4-r9-20260915-helper.py` | `8326e4a3f14a923333260aefcc6cfa6af5ae524990bdd6ce702365c15b0f911d` |
| `scripts/auto-switch-q4-r9-20260915-test.py` | `315704e4eae7a982d6053c689a7e031892522f68269545de3125ee21c3952a38` |

## Prior finding disposition

1. **Runtime/action binding: OPEN — BLOCK.** The action now contains exact runtime metadata and digest fields, but the helper asks the out-of-band `runtime` object to attest both with `runtime.snapshot()` and `runtime.source_bytes()`. A different implementation can return the approved dictionary and approved source bytes while its `start`, `authenticate`, or `stop` methods execute different behavior. Likewise, `command_sha256`, `collector_sha256`, and `request_sha256` are compared only as self-reported strings; the helper never hashes the command, collector, or request bytes actually used. The retained `source_bundle` is rehashed but is not tied to the Python code actually executing the launcher/helper. These are claims about approved bytes, not execution from those retained bytes. In addition, `secret_path` and therefore the state/terminal root remain out-of-band and unpinned, allowing an approved action to read a different credential source and reserve a different leaf location. Exact runtime, source-at-execution, credential-source, leaf-target, and action-time pins therefore remain unproved (`helper` lines 50-66; contract lines 7 and 11).

2. **Authenticated readiness/direct Q4 proof: OPEN — BLOCK.** Evidence is still a dictionary returned by the same out-of-band runtime. The helper validates its shape and equality to approved claims, but receives no authenticated response bytes, collector-produced canonical evidence bytes/hash, or independently derived proof that one request reached the pinned candidate/model/connection. A runtime can return the accepted dictionary without contacting anything. The contract also says caller booleans are not evidence, but Python accepts `True` as both `request_count == 1` and `isinstance(content_bytes, int) and content_bytes > 0`; those two proof fields therefore still accept booleans (`helper` lines 66-73; contract line 13).

3. **Start transport uncertainty: CLOSED.** `runtime.start()` is now inside the `try/finally`; an exception after a possibly applied start causes one stop attempt, leaves the pre-reserved UNKNOWN/SPENT state in place, and cannot publish PASS (`helper` lines 61-81). The focused test adds the corresponding synthetic lost-acknowledgement case.

4. **Canonical/exact schemas: PARTIALLY CLOSED; execution-byte binding remains OPEN.** Canonical action/approval bytes, exact manifest/action/approval/request/runtime keys, approval schema, retained-bundle hashes, and distinct safe leaf names are now checked. However, rehashing bytes supplied inside the request does not prove that the executing launcher, helper, runtime, command, collector, or request uses those bytes. This residual defect overlaps finding 1 and contradicts the contract's direct-byte/action-time claim (`launcher` lines 35-55; `helper` lines 34-52; contract line 7).

## Preserved properties

- R9 remains isolated to fresh, distinct `q4-r9-*` leaves with no R8 invocation, receipt lookup, retry, fallback, or reinterpretation of the historic missing R8 invocation.
- State reservation still uses exclusive creation, mode `0600`, file/directory fsync, and occurs before the secret read; any failure remains UNKNOWN/SPENT and PASS uses a separate exclusive leaf.
- The reviewed code does not itself log, hash, emit, or place secret bytes in argv/environment. End-to-end secret safety is not established while the runtime and credential source remain unbound.

## Checks and required disposition

- Reviewed the exact `485699ab..9d93f96b` diff and the four current committed files; recorded their SHA-256 values above.
- Focused offline test not run: the remaining defects follow directly from the accepted interfaces and Python boolean semantics; its synthetic cases do not bind live executable bytes or prove direct authenticated generation.
- Do not issue source approval, exact-action approval, execution authority, or remote contact. Replace the self-attestation boundary with execution from retained reviewed bytes (or independent hashing of the actual executable inputs), pin the credential/leaf target without exposing the secret, require direct canonical evidence bound to the pinned collector request/response, reject booleans for integer proof fields, then obtain a fresh independent review.
