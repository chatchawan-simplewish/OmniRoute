# Q4 R9 independent source rereview 3

Verdict: **BLOCK**

High-risk fix commit reviewed: `e5fb6fdb61474ce608f51cd4d359f40297a8e253`

Prior rereview: `a130b890e164449c824da64892378e3d27a88895`

Scope was limited to the exact fix diff and current committed bytes of the contract, launcher, helper, and focused test. No live resource was contacted and no consuming mode was executed.

## Current source package

| File | SHA-256 |
| --- | --- |
| `docs/auto-switch-q4-r9-20260915-contract.md` | `fb2d49da63f05ee2f0904740b6b33db19a7bfa9267a23c6391dece6c40ca752b` |
| `scripts/auto-switch-q4-r9-20260915.py` | `71c7226818bf4b52b5b7ce4611fceb8b371bf2b6b41f958a2d3df3929ecf793c` |
| `scripts/auto-switch-q4-r9-20260915-helper.py` | `e72af98a5f5e9d5e3edc4c85fef4fde794eefd3cdacb5cdbcf19f8ee348535ad` |
| `scripts/auto-switch-q4-r9-20260915-test.py` | `6693de68852c979edcf07c9e6989e25ad2383a4dabc4e6217259e3e42ec3701f` |

## Blocking finding

1. **A short credential read is accepted and can consume the one-shot action with truncated secret bytes.** `_read_secret()` proves the opened file's approved identity, size, and mtime, then performs one `os.pread(secret_fd, 4097, 0)`. It rejects empty or oversized results and metadata drift, but never requires `len(secret) == before.st_size == expected["secret_size"]`. POSIX permits a successful read to return fewer bytes than requested. Any nonempty short read without a forbidden byte passes validation, after which the candidate is started and the truncated secret is sent to the collector. The UNKNOWN/SPENT and stop behavior remain fail-closed, but the exact reviewed credential was not used and the no-retry gate was needlessly consumed. Require exact length equality or a bounded loop that reads exactly the approved size before starting (`helper` lines 174-187 and 223-232).

## Verification blocker

2. **The only end-to-end POSIX/root gate test was skipped on this Windows review host, and no test drives the fail-start path through `execute()`.** The focused run reported `Ran 3 tests ... OK (skipped=1)`: retained runtime/collector and non-POSIX refusal checks passed, while `test_posix_gate_reserves_unknown_stops_once_and_publishes_only_direct_pass` was skipped by its POSIX-plus-root guard (`test` lines 158-179). Therefore the integrated openat identity, exclusive leaf reservation, held-descriptor secret read, retained operation execution, stop, and terminal publication have not run in this review environment. Moreover, the earlier fail-start check calls `_run_retained(..., "start")` and `_run_retained(..., "stop")` manually rather than calling `execute()`, so it does not prove that the production `finally` attempts exactly one stop while retaining state and withholding terminal PASS. After fixing finding 1, the exact package must pass offline as root on the matching POSIX execution platform, including a focused `execute()` fail-start assertion for one `start`, one `stop`, state present, and terminal absent.

## Prior findings now closed by static review

- **Retained-byte execution:** the canonical v2 action and Sol High approval pin launcher, helper, contract, test, runtime, command, collector, and request hashes. The launcher retains each bounded regular file once, executes helper bytes from memory, and the helper runs retained runtime/collector bytes through the fixed isolated stdin shim. Operation digests are no longer self-attested runtime fields.
- **Credential and leaf identity:** the action pins parent and secret device/inode/owner/mode/size/mtime plus the secret leaf. The helper opens the root-owned mode-0700 parent and mode-0600 regular secret with `O_NOFOLLOW`, validates `fstat` identities, and holds the parent descriptor for `openat` state/terminal publication. Caller path strings locate objects but cannot substitute identities.
- **Canonical direct evidence:** the exact retained collector and request are approved. Collector stdout must be duplicate-free canonical JSON with exact keys, empty stderr, bound runtime/candidate/Q4 model/connection, HTTP 200 readiness/completion, exact integer request count, positive integer content size, and UUIDv4 request ID. PASS retains its evidence SHA-256 and safe request ID only after a successful reviewed stop.
- **Fail-closed/no-retry:** UNKNOWN/SPENT is exclusively created and fsynced before secret use; existing state or terminal refuses replay. Start, collection, evidence validation, or stop uncertainty cannot publish PASS, and exactly one retained stop invocation is attempted in `finally`, including after failed/lost start acknowledgement. R8 remains untouched and unreferenced by executable paths.

## Checks and disposition

- Inspected the exact `a130b890..e5fb6fdb` diff and all four current committed files; recorded SHA-256 values above.
- Ran `python -B scripts/auto-switch-q4-r9-20260915-test.py -v` offline: two PASS, one SKIP (root-POSIX end-to-end test).
- Do not issue source approval, exact-action approval, execution authority, or remote contact until the exact-length credential read is fixed, freshly reviewed, and the root-POSIX focused test passes on the intended execution platform.
