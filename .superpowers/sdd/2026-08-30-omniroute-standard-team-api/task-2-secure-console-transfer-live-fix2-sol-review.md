# Task 2 secure-console transfer live brief — fix-round-2 Sol High review

## Verdict

**PASS — zero blocking, HIGH, IMPORTANT, or new-breakage findings.** Both
fix-round-1 IMPORTANT findings are fully corrected. All previously resolved
HIGH/IMPORTANT findings remain resolved, and the exact transfer, confirmation,
redaction, no-retry, cleanup, and excluded-scope boundaries remain intact.

This is an independent static/direct-byte review only. No embedded block was
evaluated or invoked, and no browser, clipboard, token, credential,
Cloudflare, VM, proxy, process, registry, evidence, or routing action occurred.

`authorizes_live_execution=false`

## Evidence integrity and static checks

- Fix-round-1 brief: `4b0f3d8c5116fce5a07a57595eb594d79b089154`.
- Fix-round-1 FAIL review:
  `be3bd4f17032d7332a62b0bfdb9f598eede9d8f7`.
- Fix-round-2 brief commit:
  `7af3ab75ec87d81d75811ff8f2e9b4fa9d0c3e3b`; its direct parent is the
  fix-round-1 FAIL review commit.
- The fixed commit changes exactly
  `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-live-brief.md`.
- Fixed brief: `62054` bytes, SHA-256
  `995CA4D59E564EAF53417B9F577808F9C307C5CDEE93FB8E91DC73A5211F52CC`.
- Fix-round-2 package: `17526` bytes, SHA-256
  `578C39CAC4524B4D78198F6FFA2757514C3748F78318FA59F0E862104617C7BA`.
- Before this artifact was created, the Git index was empty and the unrelated
  worktree baseline remained exactly 12 status entries.
- The brief is strict UTF-8, no BOM, LF-only, with one trailing LF.
- All five PowerShell fences parse with zero parser errors without evaluation.
- Extracted owner: exactly `22118` bytes, SHA-256
  `347FCD60A41DF780CE4A94E4FC14C87E5059112068C689EF73636ABC5B0F0B6C`.
- Extracted deterministic R5 remains exactly `10890` bytes, SHA-256
  `DB75253CD851075C1D612A54EC4B02C8016C034C8BC192A3DB9D02DB9890AD41`.
- Full executable text contains zero parameterless `WaitForExit()` calls and
  zero synchronous `ReadToEnd()` calls. Stream capture uses async drains.

No passing live suite was rerun. Review checks were direct-byte, Git,
non-evaluating parser/AST, reachability, cardinality, deadline arithmetic,
redaction, and authority-flow checks only.

## Fix-round-2 finding resolution

### IMPORTANT 1 — exactly one reachable R5 exit proof: RESOLVED

The R5 child still has two syntactic exit-proof sites because they cover two
mutually exclusive failure classes, but at most one is reachable in any run:

1. If the `180000 ms` wall wait times out, the timeout branch increments
   `$r5ExitProofAttempted` once and performs the sole `10000 ms` proof wait.
2. If that proof fails, the counter remains one and the child `finally` guard
   `if ($r5ExitProofAttempted -eq 0)` is false. It cannot wait again.
3. If a different post-start exception occurs before any exit proof, the
   counter remains zero and the `finally` performs the sole proof wait.
4. If either proof succeeds, `$r5ChildExited` becomes one, independently
   preventing another proof branch.

The sole termination cardinality is also preserved. The timeout branch attempts
one exact-retained-handle `Kill()`. The `finally` can attempt termination only
when `$r5TerminationAttempted -eq 0`; thus a timeout-path kill is never repeated.
There is no PID/name lookup, tree kill, process reacquisition, second exit-proof
observation, or retry.

A failed timeout proof now leaves exact fixed residual
`EXACT_CHILD_EXIT_NOT_PROVEN`, retains the exact handle, clears the two
start-info private environment entries, classifies R5 uncertain, and proceeds
to the universal revocation hold without another wait. Exact success still
requires R5 wait `1/1`, timeout `0`, termination/exit proof `0/0`, stream
capture `1/1`, private environment clear `2/2`, child exit proven, and residual
`NONE`.

### IMPORTANT 2 — owner lifetime bound from retained launch: RESOLVED

The retained parent starts `$ownerClock = [Diagnostics.Stopwatch]::StartNew()`
immediately before `Start-Process`. The monotonic clock remains in the same
parent process with the exact owner handle and expected PID throughout both
human checkpoints and native actions.

Coordination is explicitly nonblocking: it may inspect only safe log data and
`$owner.HasExited`, and it must not call a blocking process wait while observing
the revocation tuple or requesting either chat confirmation. Before a further
consuming step it must stop if the monotonic budget is exhausted.

The final block computes exactly:

`ownerRemainingMs = 1800000 - ownerClock.ElapsedMilliseconds`

- If the remainder is nonpositive, timeout disposition is immediate.
- If positive, the parent performs one wait for only that remainder.
- If the owner is still present after expiry, it permits one `Kill()` on the
  retained exact handle and one bounded `10000 ms` exit proof.
- Failure to prove exit retains the handle, emits only fixed safe uncertainty,
  and makes no cleanup, token, or revocation success inference.
- No name/PID reacquisition, process enumeration, tree kill, retry, fallback,
  or session handoff occurs.

The numeric lifetime is sufficient: the fixed phase budget is
`600 + 20 + 20 + 180 + 600 + 20 = 1440` seconds. The `1800`-second outer
budget leaves 360 seconds for bounded R5 exit/stream proof and local cleanup.
The final positive remainder fits a signed 32-bit millisecond argument.

## Regression review of all earlier findings

### Universal post-accept revocation hold — remains resolved

Every path after `$maskedAccepted = $true` is inside the post-accept operation
scope whose `finally` owns the one revocation hold. Clipboard cleanup, BSTR
conversion, token verification, zone lookup, spawn-time validation, R5 start,
R5 timeout/output/error, and unexpected operation failures all reach the hold
before named-token/BSTR/SecureString cleanup. Conversion without a usable token
still permits separately confirmed exact-row deletion while classifying HTTP
401 NOT PROVEN.

### Revocation trigger — remains independent of R5

Every post-accept result uses the exact safe tuple
`REVOCATION_REQUIRED=PASS`, fixed `REVOCATION_ROW_NAME`, and
`REVOCATION_AUTHORITY=WAITING`. Zero R5 starts, R5 pin drift, failure, timeout,
uncertain exit, and PASS all use the same separate confirmation trigger. The
confirmation remains limited to one exact-row deletion plus refreshed exact
name/row counts `0 / 0`; only then may the user natively signal `G`.

### Exact R5 executable and process lifetime — remain resolved

Immediately before the sole child start, the owner requires the exact bundled
pwsh path, length `301368`, SHA-256
`DB6DD81183FE57D22E03B911EC9A30A2FD7C40542E97743615355A6FB44F458F`,
and version `7.6.4.500`. The child has async stdout/stderr drains, one fixed wall
wait, one reachable termination/exit-proof disposition, bounded stream drain,
fixed residual state, and private start-info cleanup. No blocking read or
unbounded wait was reintroduced.

### SSH retained processes — remain resolved

START, PROOF, and ROLLBACK each use connection/liveness settings, one
`60000 ms` wall wait, async drains, at most one exact-handle termination, and
one `10000 ms` exit proof. Timeout stops without retry or later-stage inference;
unproven exit retains the exact handle and uncertainty.

## Full security/quality recheck

- **Target and permissions:** exact zone `mysw.me`, fixed token name, specific
  zone resource, and exactly Zone WAF Edit plus Zone Read remain unchanged.
  Refreshed exact-name and matching-row prestate remains `0 / 0`.
- **Mandatory human gates:** final Create + native semantic Copy + one masked
  Paste require one action-time confirmation. Exact-row deletion requires a
  separate confirmation. Static PASS and standing authority waive neither.
- **Browser boundary:** after Create there is no agent DOM/page/attribute read,
  snapshot, screenshot, evaluation, browser Clipboard API, keyboard injection,
  CUA, or token-page inspection. V10 equivalence remains explicitly unclaimed.
- **Clipboard:** executable cardinality remains one `Set-Clipboard` and one
  `Get-Clipboard`, guarded against retry and used only for current-clear/empty
  proof. No history-erasure claim is made.
- **Masked input:** one same-process 600-second monotonic secret prompt, no
  `Read-Host`, no second secret prompt, no emitted value or length, and
  per-iteration key/reference clearing.
- **Same-process API:** active verify, exact `mysw.me` zone lookup, and invalid
  check remain serial and each has `TimeoutSec 20`. Zone success requires one
  result, total count one, case-exact name, and lowercase 32-hex ID without
  emitting the ID.
- **Credential holders:** the token appears only in the fixed owner and sole
  exact child; never arguments, parent environment, file, safe log, tool
  result, or report. The R5 child receives only the two authorized private
  entries and those start-info entries are cleared on every path.
- **Cleanup/redaction:** BSTR zero-free, SecureString disposal, managed/header/
  response/reference clearing, exact-hash script deletion, parent exit/absence
  proof, safe-log scan/hash/delete, and GUID-root guard remain fail-closed.
  Failed exit proof never claims cleanup success.
- **One-shot scope:** no retry, fallback, second token/prompt/child/POST, session
  handoff, alternate bridge, permission expansion, secret output, or broader
  delete/process action was introduced.
- **Excluded rollout:** Tunnel, DNS/public hostname, Access, rollout key, model
  request, OmniRoute/Bell changes, VM power, routing, and evidence mutation
  remain outside this gate.

## Findings

None.

## Disposition

The fix-round-2 candidate is statically review-clean. This PASS authorizes no
live action and does not itself consume any gate. Any later preparation or
action-time eligibility decision must pin this exact brief and review, preserve
the sole Sol High owner lane, revalidate all fresh state, obtain both mandatory
human confirmations at their exact checkpoints, and treat the first consuming
failure or uncertainty as spent with no retry.
