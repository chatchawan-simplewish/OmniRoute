# Task 2 secure-console transfer live brief — fix-round-1 Sol High review

## Verdict

**FAIL — zero blocking/HIGH findings; two IMPORTANT findings remain.** All
three original HIGH findings and original IMPORTANT 1 are corrected. The SSH
portion of original IMPORTANT 2 is corrected, but the owner “wall deadline” is
not measured from process start. A new R5 failure-path cardinality defect also
performs two exit-proof waits despite the contract requiring at most one.

This review does not overwrite or relax the original FAIL review. It is static
and non-executing; no browser, clipboard, token, credential, Cloudflare, VM,
proxy, process, registry, evidence, or routing action was performed.

`authorizes_live_execution=false`

## Direct-byte and parser evidence

- Original brief: `5026b28140ad2431c1a5b77903845d174e4ed606`.
- Original FAIL review: `646d42f40d5c217688252630ec91c2aff893a999`.
- Fixed brief commit: `4b0f3d8c5116fce5a07a57595eb594d79b089154`;
  direct parent is the original FAIL review commit.
- Fixed brief: `60073` bytes, SHA-256
  `19A99E2C8E7AB887E3EFDF00DF2E94BE322CB88D70396AF5755ACFACC47EB6F3`.
- Fix package: `52913` bytes, SHA-256
  `154C02906F4993905EDB315EEB14D28F572DBF92896EC0151C8260CD485050C9`.
- The fix commit changes exactly
  `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-live-brief.md`.
- Before this artifact was written, the Git index was empty and the unrelated
  worktree baseline remained exactly 12 status entries.
- The fixed brief is strict UTF-8 without BOM, LF-only, and has one trailing LF.
- All five PowerShell fences parse with zero errors without evaluation.
- The extracted owner is exactly `22013` bytes, SHA-256
  `27E4F7E447104BA6253682D082D54A0EBBE4AFBD843D7AA9806B82B6B8136BBB`.
- The unchanged R5 extraction remains exactly `10890` bytes, SHA-256
  `DB75253CD851075C1D612A54EC4B02C8016C034C8BC192A3DB9D02DB9890AD41`.
- Across executable fences there are zero parameterless `WaitForExit()` and
  zero synchronous `ReadToEnd()` calls. The owner uses two asynchronous stream
  drains and three timed process waits.

No passing live suite was rerun. Checks were limited to direct bytes, Git,
non-evaluating parser/AST, cardinality, control flow, and deadline arithmetic.

## Original finding resolution

### HIGH 1 — universal post-accept revocation hold: RESOLVED

After `$maskedAccepted = $true`, clipboard cleanup, BSTR conversion, active
verification, zone lookup, spawn-time pinning, R5 start/wait/output handling,
and their unexpected failures are inside an inner post-accept `try/catch` whose
`finally` contains the sole revocation hold (`brief:631-890`). Thus a failure
before obtaining a usable managed token still emits the exact safe hold tuple,
allows separately confirmed exact-row deletion, records HTTP 401 as NOT PROVEN,
and only then reaches outer reference/script cleanup.

`Write-Safe` no longer throws around the hold; it makes output uncertainty
sticky. The revocation prompt write is locally caught. Revocation denial,
timeout, console failure, invalidity failure, and success all converge on the
same post-hold terminal calculation and outer cleanup.

### HIGH 2 — bounded credential-bearing R5 child: RESOLVED for lifetime, with one new cardinality defect

The fixed owner starts async stdout/stderr drains, performs one `180000 ms`
wall wait, allows at most one exact-retained-handle `Kill()`, and uses bounded
`10000 ms` exit-proof waits plus a `5000 ms` stream-drain bound. It clears both
private `ProcessStartInfo` entries and routes every non-success state to the
universal revocation hold. A child whose exit is unproven is recorded as a
fixed residual and can never satisfy success.

This closes the indefinite credential-residency defect. The duplicate
exit-proof issue below is nevertheless an exact-contract failure requiring a
small correction.

### HIGH 3 — confirmation trigger independent of R5 terminal: RESOLVED

Authority and launch prose now trigger the separate exact-row deletion
confirmation on the exact safe tuple
`REVOCATION_REQUIRED=PASS` / fixed `REVOCATION_ROW_NAME` /
`REVOCATION_AUTHORITY=WAITING` for every post-accept outcome. Zero R5 starts,
pre-R5 failure, R5 failure/timeout, and R5 success all use the same trigger. The
fixed deletion, refreshed `0 / 0` proof, user-native `G`, and retained-token
HTTP 401 boundary remain unchanged.

### IMPORTANT 1 — immediate exact pwsh binding: RESOLVED

Immediately before the sole R5 `Start()`, the owner resolves the executable and
requires the exact path, file length `301368`, SHA-256
`DB6DD81183FE57D22E03B911EC9A30A2FD7C40542E97743615355A6FB44F458F`,
and file version `7.6.4.500` (`brief:692-702`). Drift starts no child, clears the
two start-info entries in the child-finally path, and enters revocation.

### IMPORTANT 2 — retained SSH/owner process bounds: PARTIALLY RESOLVED

SSH is corrected: every START/PROOF/ROLLBACK helper uses async drains,
`ConnectTimeout=10`, server-alive liveness, a `60000 ms` process wait, one
exact-handle termination attempt, and one `10000 ms` exit proof. It stops
without retry and preserves uncertainty if exit is not proven.

The owner portion is not yet a true from-launch wall clock; see IMPORTANT 2
below.

## Remaining findings

### IMPORTANT 1 — R5 timeout can perform two exit-proof waits

**Evidence:** fixed brief `:719-726` and `:760-778`; contract prose
`:984-992` and counters `:1105-1112`.

When the `180000 ms` R5 wall wait expires, the timeout branch increments
`$r5ExitProofAttempted` and calls
`WaitForExit($r5ExitProofDeadlineMs)`. If that returns false, it records the
residual and throws. The `finally` then sees a started but not-exited child. It
correctly avoids a second `Kill()` because `$r5TerminationAttempted` is already
one, but it increments `$r5ExitProofAttempted` again and calls the same timed
`WaitForExit` a second time.

Static cardinality is therefore:

- R5 termination attempts: maximum `1` — correct;
- exit-proof increment sites: `2`;
- exit-proof wait sites: `2`;
- reachable timeout tuple: `R5_EXIT_PROOF=2/0` or `2/1`.

That contradicts the claimed `0..1` exit-proof maximum and the explicit “no
second wait path” statement. It is also an observation retry under a contract
that requires a single bounded disposition.

**Required fix:** make the `finally` exit proof conditional on
`$r5ExitProofAttempted -eq 0`, not merely on child-start/exit state. After the
timeout branch's failed proof, retain the exact handle and fixed residual,
clear start-info private entries, enter revocation, and do not wait again. Keep
one termination and one exit-proof counter site reachable per invocation.

### IMPORTANT 2 — the owner timeout is relative to the final wait call, not process start

**Evidence:** owner launch at fixed brief `:999-1008`; prose `:1011-1021`;
final wait block `:1050-1072`.

The launch declares `$ownerWallDeadlineMs = 1800000` but records no launch-time
`Stopwatch`, timestamp, or absolute deadline. Later—explicitly “after the
visible owner exits”—the parent calls `WaitForExit($ownerWallDeadlineMs)`.
`WaitForExit(timeout)` measures from that call, not from process launch. Any
time already spent in masked-input, user coordination, R5, or revocation is not
subtracted. If the block is called only after visual exit as instructed, it
returns immediately and never enforced a wall deadline at all. If it is called
earlier, its blocking wait prevents the same coordinator from observing the
safe revocation tuple and obtaining the mandatory chat confirmation.

Consequently the claimed `1800000 ms` outer lifetime is not actually bound to
the retained owner's lifetime, and original IMPORTANT 2 is not fully resolved.

**Required fix:** start a monotonic owner stopwatch at the same time as the
retained process launch. During nonblocking coordination, preserve that clock.
At final wait, calculate the exact remaining budget as
`1800000 - ElapsedMilliseconds`; if nonpositive, take the one authorized
exact-handle timeout disposition immediately, otherwise wait only that
remaining duration. The coordinator must not block across the period in which
it must inspect the safe tuple and obtain the separate human confirmation.
Output fixed elapsed/remaining/termination counters without timestamps or
secret state.

## New-breakage and interruption-path audit

| Path | Result |
| --- | --- |
| Pre-accept guard, cancel, empty input, or 600-second timeout | PASS: no authenticated request/child; common clipboard/script cleanup. |
| Post-accept clipboard/BSTR/conversion failure | PASS: necessarily reaches universal hold before outer cleanup. |
| Verify/zone failure | PASS: zero R5 starts; same hold and independent confirmation trigger. |
| Pre-spawn pwsh drift | PASS: exact bytes/version checked immediately; zero child starts; hold reached. |
| R5 normal PASS/fixed terminal failure | PASS: async capture, bounded wait, exact safe status, hold reached. |
| R5 wall timeout with first exit proof success | PASS: one kill/one proof, conservative R5 failure, hold reached. |
| R5 wall timeout with first exit proof failure | **FAIL:** second proof wait occurs in finally (IMPORTANT 1). |
| Revocation deny/timeout/console uncertainty | PASS: fixed incident, no inferred revocation, bounded cleanup. |
| Grant with usable token and HTTP 401 | PASS: exact success/failure split retained. |
| Grant without usable token | PASS: exact-row deletion allowed, HTTP 401 explicitly NOT PROVEN. |
| Owner outer wall from launch | **FAIL:** relative final wait does not measure from launch (IMPORTANT 2). |
| Cleanup failure | PASS: fixed failure terminal, no retry or broader deletion. |

## Other contracts rechecked

- Exact target, token name, `mysw.me` resource scope, Zone WAF Edit plus Zone
  Read only, and refreshed token-name/matching-row counts `0 / 0` remain fixed.
- Final Create/native semantic Copy/masked Paste and exact-row deletion retain
  separate mandatory action-time confirmations. Standing authority does not
  waive either.
- No post-Create DOM/page read, screenshot, serialization, browser clipboard
  API, keyboard injection, CUA, or agent token-page inspection was added.
- Owner executable cardinality remains one `Set-Clipboard`, one
  `Get-Clipboard`, three same-process `Invoke-RestMethod` calls each with
  `TimeoutSec 20`, one R5 process start maximum, and no blocking stream read.
- Token and Zone ID remain absent from arguments and parent environment. The
  R5 child receives them only through its two private start-info entries, which
  are cleared on every start-info path.
- Exact Zone lookup still requires one result, total count one, case-exact
  `mysw.me`, and lowercase 32-hex ID without emission.
- BSTR, SecureString, managed token/header/response references, R5 private
  environment, exact script deletion, safe-log redaction, and residual claims
  remain conservative. Failed exit proof never claims cleanup success.
- No retry, fallback, session handoff, public rollout, Tunnel/DNS/Access,
  credential output, permission expansion, evidence mutation, or broader
  process/resource kill was introduced.

## Required disposition

Do not execute or consume the fixed candidate. Apply the two narrow lifecycle
corrections, repin the owner/brief/package bytes and hashes, and obtain a fresh
independent Sol High review. All original scope, confirmations, secret
boundaries, exact deletion, and no-retry rules must remain unchanged.
