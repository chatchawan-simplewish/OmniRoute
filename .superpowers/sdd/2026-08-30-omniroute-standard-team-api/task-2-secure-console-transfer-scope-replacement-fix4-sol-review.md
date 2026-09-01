# Task 2 secure-console scope replacement — fix-round-4 Sol High review

## Verdict

**PASS** — zero blocking, HIGH, or IMPORTANT findings. The fix-round-3
cleanup-child finding is corrected without relaxing the one-shot, cleanup,
confirmation, revocation, redaction, or no-retry boundaries.

`authorizes_live_execution=false`.

This is a static review only. It authorizes no browser, clipboard, credential,
Cloudflare, VM, SSH, process, routing, or other live action.

## Reviewed source and integrity

- Brief commit: `20cfaf30e57901b90126af973588bbb65601e7b2`.
- Exact brief: `task-2-secure-console-transfer-scope-replacement-brief.md`.
- Direct bytes: `41236`.
- SHA-256: `44D690E12123B29745442934A5C32C11B6914978768A974735C7404B87630962`.
- The three JavaScript fences matched the supplied byte/SHA-256 pins exactly
  and each passed non-evaluating `node --check` with empty stdout/stderr.
- The three PowerShell fences matched the supplied byte/SHA-256 pins exactly
  and each parsed with zero PowerShell parser errors.

## Fix-round-3 finding disposition

### IMPORTANT — cleanup-child exception classification and disposition: corrected

The guarded cleanup child now maintains truthful, monotonic state across all
reviewed branches:

- The exact process binding exists before the sole `Start()` attempt. Start
  exceptions, `Start() == false`, disposal-after-start-failure exceptions, and
  asynchronous stream-task creation exceptions each receive a fixed non-secret
  residual before failure (brief lines 400-428). The exact available process
  and task bindings are retained whenever safe disposal is not proven.
- The initial bounded wait, sole exact-handle termination, and sole bounded
  exit-proof wait each classify exceptions before failing (lines 429-459).
  Exit-not-proven stops with the exact handle/tasks retained; there is no lookup,
  reacquisition, second wait, or second termination.
- Every proven exit, including the timeout/kill path, reaches exactly one
  bounded drain attempt (lines 460-479). A thrown drain wait, drain timeout, or
  result/exit-code access failure receives a distinct non-`NONE` residual and
  retains the exact available bindings. Thus a faulted task can no longer fall
  through to a misleading `CHILD_RESIDUAL=NONE` terminal.
- Timeout-exit-proven, terminal mismatch, and exact terminal success are
  classified before the sole disposal attempt (lines 480-509). Disposal
  exceptions receive distinct contextual residuals; process/task bindings are
  nulled only after disposal is fulfilled. Timeout-exit-proven and terminal
  mismatch still fail after proven drain and disposal, while only the exact
  terminal returns success.

The fixed parent terminals expose only counters and controlled status labels.
They do not emit exception text, redirected child content, process metadata,
paths, identifiers, or secrets. A cleanup discrepancy therefore remains
fail-closed and spends the replacement gate without retry or continuation.

## Full actionability and preserved boundaries

- The retained-tab adoption and mutually exclusive detach fences are unchanged
  at their previously reviewed exact hashes. Their declaration, state,
  eligibility, consumed-flag, redacted-counter, and no-browser guards remain
  intact; neither detach path claims tab-closure proof.
- The guarded launch retains the exact owner process, PID, and stopwatch in the
  same PowerShell parent. All post-launch/pre-accept failures with an exact
  handle route to the single inherited remaining-budget final block before
  file/root/proxy cleanup. Start uncertainty without a handle remains
  `NOT PROVEN` and forbids lookup or cleanup.
- The proxy helper has fixed numeric waits and one exact-handle termination
  path. It performs no enumeration or alternate cleanup action. Any uncertain
  child state is retained and reported rather than rehabilitated.
- The original approved live contract remains inherited except for the reviewed
  scope/adoption mechanics. Mandatory final Create/native Copy/masked Paste and
  separate exact-row deletion confirmations remain mandatory. The universal
  post-accept revocation hold, invalid-token proof, cleanup, secret-redaction,
  and public-rollout exclusion remain unchanged.
- The predecessor and earlier replacement attempts remain spent. This PASS
  permits no retry, fallback, handoff, verdict relaxation, or authority
  expansion. Any later gate consumption still requires the contract's exact
  action-time pins and separate owner authority.

## Finding count

- Blocking: 0
- HIGH: 0
- IMPORTANT: 0
- Static verdict: **PASS**
- `authorizes_live_execution=false`
