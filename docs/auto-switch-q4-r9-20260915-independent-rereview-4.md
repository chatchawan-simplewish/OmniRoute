# Q4 R9 independent source rereview 4

Verdict: **PASS — SOURCE REVIEW ONLY / NOT EXECUTION AUTHORITY**

Final fix commit reviewed: `e129b8dd7c3d2831198b6d675d459c6ba223f2ff`

Prior BLOCK review: `2654b69803d532465d5aa5565f730e5cc6c99a93`

Scope was limited to the exact final-fix diff and current committed bytes of the contract, launcher, helper, and focused test. No live resource was contacted and no consuming mode was executed.

## Current source package

| File | SHA-256 |
| --- | --- |
| `docs/auto-switch-q4-r9-20260915-contract.md` | `7afad77dae2a21330f0f8d59afd587e8d110b8ad2716b6e77215a4585b57dc33` |
| `scripts/auto-switch-q4-r9-20260915.py` | `71c7226818bf4b52b5b7ce4611fceb8b371bf2b6b41f958a2d3df3929ecf793c` |
| `scripts/auto-switch-q4-r9-20260915-helper.py` | `0395ce2c3f3a6b7ad1287facb3c4fded4ff52ec131d3c758bf32ee0fadf4a020` |
| `scripts/auto-switch-q4-r9-20260915-test.py` | `7cd2c059c8c076f4332a0d48114bad647f3d6125695fb20c9b782784a019450c` |

## Residual closure

1. **Exact secret length: CLOSED.** `_read_secret()` still proves the held descriptor's approved identity, owner, mode, size, and mtime before reading, and now requires `len(secret) == expected["secret_size"]`. Empty, short, truncated, oversized, newline/NUL-bearing, or metadata-drifted bytes fail before any runtime start (`helper` lines 174-187). The focused test patches `pread` to return a one-byte-short value and verifies rejection.

2. **Production fail-start path: CLOSED.** The new test calls `helper.execute()` with the retained runtime's start mode returning nonzero. It verifies return code 1, exactly `start` then `stop`, one UNKNOWN/SPENT state write, and no terminal write. This directly covers the production `try/finally` stop path rather than manually invoking start and stop (`test` added `test_execute_fail_start_stops_once_retains_unknown_and_withholds_terminal`; `helper` lines 214-249).

## Complete source-review result

- The canonical v2 action and Sol High approval pin all eight source/operation byte strings. Launcher/helper/runtime/collector execution uses retained bytes rather than reopened operational paths.
- Credential and leaf publication are bound to reviewed opened-object identities and a held root-owned POSIX parent descriptor. State reservation is exclusive and durable before secret use; existing state or terminal refuses replay.
- Collector evidence is duplicate-free canonical JSON from the exact retained collector/request, with exact schema and runtime/candidate/Q4 model/connection bindings, authenticated readiness/completion status requirements, integer and UUIDv4 validation, and evidence hash retention only after a clean reviewed stop.
- Any start, collection, evidence, or stop failure/uncertainty leaves UNKNOWN/SPENT authoritative and cannot publish PASS. There is no retry, fallback, Q6 request, or executable reference to the historic missing R8 invocation.

## Checks, limit, and disposition

- Inspected the exact `2654b698..e129b8dd` diff and all four current committed files; recorded SHA-256 values above.
- Ran `python -B scripts/auto-switch-q4-r9-20260915-test.py -v` offline: four PASS, one SKIP. The exact-length and `execute()` fail-start cases passed.
- The skipped root-POSIX end-to-end test is an explicit remaining verification limit because this review host is Windows. It must pass offline as root on the matching intended POSIX execution platform before any consuming action. This source PASS permits only preparation of the separate exact-action review package; it does not prove absent leaves, approve live contact, authorize execution, or relax sole-owner/no-retry requirements.
