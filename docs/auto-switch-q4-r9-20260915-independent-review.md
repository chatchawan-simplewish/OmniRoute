# Q4 R9 independent source review

Verdict: **BLOCK**

Reviewed commit: `ad8686ee2ec63de2ba8158ac3f723e9517e616a6`

Scope was limited to the committed contract, launcher, helper, and focused test. No live resource was contacted and no consuming mode was executed.

## Exact source package

| File | SHA-256 |
| --- | --- |
| `docs/auto-switch-q4-r9-20260915-contract.md` | `e80fa266ce52ac4bdd04ca15be8b04b589bb0605a9760f7710abaa86134891a6` |
| `scripts/auto-switch-q4-r9-20260915.py` | `3d0ad04905f0ae8381ac61a11816b755ce45396336fdd7883a674b73040da68d` |
| `scripts/auto-switch-q4-r9-20260915-helper.py` | `9a19637d3673c39c37f09eb6a06d6e0b429dab1e4aab8e231d22eb5eb3c79cef` |
| `scripts/auto-switch-q4-r9-20260915-test.py` | `a8d9fb4d3d494fb1c76a5fcc16294d51be8d3ce122c63f54966a6be20d064a12` |

## Blocking findings

1. **The approval does not bind the executable runtime or action-time target.** The launcher hashes the four source files and the action JSON, but `execute()` receives `runtime` out of band. The action schema contains only the source manifest and leaf names in the focused test; neither launcher nor helper requires a pinned host, isolated candidate identity, image/command/request bytes, endpoint, exact Q4 model identifier, or runtime implementation hash. `Runtime.snapshot()` exists only in the test and is never called. A reviewed payload can therefore be paired with materially different start/authenticate/stop behavior. This fails exact-action, source-at-execution, payload, and action-time pin requirements (`launcher` lines 32-46; `helper` lines 25-45; contract lines 7 and 11).

2. **Authenticated readiness and direct Q4 generation are not proven by the helper.** `runtime.authenticate()` returns a caller-controlled dictionary. The helper trusts three `200` values plus `selected_q4=True` and `content_valid=True`; it does not validate an authenticated collector identity, exact response schema, exact Q4 model ID, a nonempty completion body, one-and-only-one request count, or correlation of health/models/completion evidence to the reviewed candidate. `request_id` is accepted without type or nonempty validation. This cannot support the PASS claim in contract line 13 (`helper` lines 47-57).

3. **Transport uncertainty can leave a possibly started candidate without a stop attempt.** `runtime.start()` is outside the `try/finally`. If the start transport applies remotely and then raises because the response is lost, execution exits with the state correctly spent/UNKNOWN but never calls `runtime.stop()`. The package therefore does not enforce stopped retention under the exact uncertainty case the gate must contain (`helper` lines 43-53).

4. **The stated canonical/exact-schema checks are incomplete.** The launcher approves the SHA-256 of arbitrary raw JSON bytes without requiring those bytes to equal `canonical(action)`, while the helper later compares the approval to canonicalized action bytes. Noncanonical approved bytes pass the launcher and fail the helper. The helper also omits the approval schema check, exact-key checks for request/action/approval/manifest/evidence, actual-source-byte revalidation, and a requirement that state and terminal leaves differ. These gaps contradict the contract claim that launcher and helper reject schema, source, action, reviewer, and leaf drift (`launcher` lines 32-46; `helper` lines 25-35; contract line 7).

## Preserved properties

- The reviewed source is namespaced to fresh `q4-r9-*` leaves and contains no R8 invocation, receipt lookup, fallback, or retry path. It does not reinterpret or consume the historic missing R8 invocation.
- The state leaf is created with `O_EXCL`, mode `0600`, file fsync, and directory fsync before the secret is read. A pre-existing state or terminal leaf refuses execution, and PASS publication cannot remove or replace the spent UNKNOWN state.
- The reviewed launcher/helper do not log, hash, emit, or place the secret in argv/environment. They pass secret bytes directly to the unbound runtime, so end-to-end secret safety remains unproven until finding 1 is fixed.

## Checks

- Direct static review of the exact committed bytes and SHA-256 manifest above.
- Focused offline test not run: its single happy-path/replay test cannot resolve the static execution-boundary contradictions above, and project policy avoids redundant passing-suite reruns.
- Required disposition: do not issue source approval, exact-action approval, execution authority, or any remote contact from this package. Replace the package and obtain a fresh independent review; this review is not authority to retry or continue any historic gate.
