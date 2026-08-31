# Task 3 v3 independent Sol High static review

Observed at: `2026-08-31 17:29:16` (`Asia/Bangkok`)

## Verdict

- **Specification verdict: FAIL / NOT PROVEN.** The committed brief does not mechanically enforce Call 3 eligibility or one-shot child use after a failed/uncertain Call 2, and late server uncertainty can be overwritten by a successful server close.
- **Security and quality verdict: FAIL.** Two HIGH findings affect load-bearing fail-closed state transitions. They must be corrected and independently reviewed before any execution approval is requested.
- **Execution authority: FALSE.** This static review authorizes no execution, credential action, browser action, clipboard action, child process, or live-resource mutation.

## Scope and method

Static direct-byte review only of pinned range `abef54ac26e63e523b7bf760b4c916911a178fdc..a4091379290b5b64689d5b49551036e87164550d`, using only the requirements brief, implementer report, and supplied direct-byte review package. No embedded code or live action was executed. The implementer's passing syntax/byte/Git checks were not rerun because the diff raised no concrete doubt about those reported checks.

## Findings

### HIGH 1 — Call 3 eligibility and one-shot child use are advisory, not fail-closed

The Call 2 cell stores the challenge in the persistent binding before server/browser success at `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-loopback-clipboard-preflight-v3-live-brief.md:151`. It sets the exact Call 2 success result only later at line 280, but persists no success/eligibility state. Call 3 checks only that the challenge binding is a shaped string at line 336, then attempts the child at line 416. Therefore the exact same Call 3 cell remains executable after any Call 2 server/browser failure or uncertainty that occurred after challenge creation. That contradicts the binding rule that any rejected/uncertain browser promise forbids later clipboard mutation and that Call 3 is eligible only after exact Call 2 success with the tab and server closed.

The binding is cleared only on exact Call 3 success at line 487. On child spawn/stdin/timeout/status/parse/schema/comparison/cleanup failure, it remains populated, so rerunning the cell can start a second child and deliver the challenge again. This violates the exact-one-child/no-retry contract even though the prose tells the operator to stop.

Required correction: persist a private Call 2 eligibility state initialized false and set true only inside the exact Call 2 success branch; require both that state and the shaped challenge in Call 3; atomically consume eligibility and detach/clear the persistent challenge before the sole spawn attempt so every failure path is non-retryable. Preserve the challenge only in a Call 3 local binding long enough for that one synchronous stdin handoff.

### HIGH 2 — Late server uncertainty is erased by successful listener close

Response error, client error, and server error handlers write uncertainty/error states at `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-loopback-clipboard-preflight-v3-live-brief.md:174-176` and `:185-191`. The `finally` close callback then unconditionally replaces the current server state with `CLOSED` when close fulfills at lines `267-268`. The exact-success predicate at line 279 checks only the final overwritten state and counters; it has no sticky server-uncertainty flag.

Consequently, an error event arriving after the last in-flow server-state check but before/during close can be masked by the successful close and produce `COPY_SETTLED_TAB_AND_SERVER_CLOSED`. This violates the requirement that any request/response/server uncertainty fail closed and is a race in a load-bearing acceptance state.

Required correction: record server/request/response uncertainty in a monotonic boolean or terminal error state that close cannot clear, set it in every relevant error/client-error/invalid-lifecycle handler, and require it to remain false in the exact Call 2 success predicate. Closing the listener may prove cleanup, but must not rehabilitate an uncertain exchange.

## Requirements otherwise satisfied by the reviewed bytes

The diff otherwise pins the exact deliverable only; a CSPRNG challenge and separate request path; a Node standard-library listener on explicit `127.0.0.1:0`; exact method/path one-use serving with the required no-store/security headers; directly awaited serial browser mutations; exact-tab binding retention; local-only server cleanup; redacted bounded objects; one synchronous no-shell PowerShell 7 child using stdin; one comparison read; one `finally` clear and empty read; strict counters/schema; no retry/fallback/`Promise.race`/data navigation/helper/background action; and the stated static-only authority boundary.

## Final disposition

**FAIL / NOT PROVEN — 2 HIGH findings.** Do not request or consume execution approval. After a narrow fix, produce a new direct-byte package pinned to the corrected head and obtain a fresh independent Sol High static review.

---

# Fix round 1 scoped Sol High re-review

Observed at: `2026-08-31 17:56:21` (`Asia/Bangkok`)

## Scope

Static review only of fix range `a4091379290b5b64689d5b49551036e87164550d..9057575ef3e59e0789042656ef76df3f8304196f`, limited to the two prior HIGH findings and new breakage introduced by their fix. Inputs were the requirements brief, appended implementer report, and supplied direct-byte fix package. No embedded or live code was executed. The implementer's passing checks were not rerun because the fix diff raised no concrete doubt about those reported checks.

## Finding 1 re-verdict — PASS

The private eligibility binding is initialized false in `review-a40913792..9057575ef.diff:89-92` and is set true only inside the exact Call 2 success predicate, which also requires clean browser/server state and a false sticky uncertainty latch, at `:287-293`. Call 3 synchronously copies the challenge to a local binding, consumes eligibility, and clears the persistent challenge before its first await or child attempt at `:355-359`. Invalid eligibility/shape exits without a child at `:359-364`; import uncertainty is non-retryable at `:365-374`; and the sole `spawnSync` attempt uses only the detached local challenge and clears it in `finally` at `:395-431`.

This closes both prior paths: failed/uncertain Call 2 cannot enable Call 3, and every Call 3 path consumes the persistent authority before the sole child attempt, so failure cannot make a second child eligible.

## Finding 2 re-verdict — PASS

The fix introduces one monotonic `serverUncertain` latch and shared marker at `review-a40913792..9057575ef.diff:113-117`. Rejected/extra requests, request abort/error, response error/incomplete close, client error, server error, start error, invalid listener/exchange/lifecycle state, residual listener, and close uncertainty all set the latch at `:128-200`, `:209-253`, and `:267-286`. Successful listener close reports `CLOSED_AFTER_UNCERTAINTY` rather than clearing the latch at `:274-277`, and exact Call 2 success explicitly requires `!serverUncertain` at `:287-293`.

The prior race is closed: listener cleanup can prove cleanup but cannot rehabilitate an uncertain request/response/server lifecycle.

## New-breakage review

**No new security, specification, lifecycle, redaction, authority, or cleanup breakage found in the scoped fix diff.** The changes remain within the single brief and preserve direct serial browser awaits, exact-tab binding, local server cleanup, bounded redacted output, one synchronous no-shell child, stdin-only challenge handoff, strict comparison/final clipboard cleanup, and no retry/fallback/helper/background action.

## Scoped disposition

**PASS for both prior HIGH findings; 0 new findings.** This is a static fix-round verdict only. `authorizes_live_execution=false`; any future one-shot execution still requires the coordinator's remaining review/approval gates and fresh exact user authority.

---

# Fix round 2 scoped Sol High re-review

Observed at: `2026-08-31 19:24:58` (`Asia/Bangkok`)

## Scope

Static review only of fix range `d451d002d588f772795bed4e9991c890a57e1b36..f7fd70caeae9c0b0caa6b2f87d894efcb32f25f7`, limited to replacing the unsupported locator focus action and identifying new breakage introduced by that fix. Inputs were the requirements brief, appended implementer report, and supplied direct-byte fix-round-2 review package. No embedded or live code was executed; Chrome and the clipboard were not touched. The implementer's passing checks were not rerun because the one-line diff raised no concrete doubt about them.

## Required-correction verdict — PASS

The sole executable locator call changes from `await field.focus()` to the documented, directly awaited `await field.click()` at `task-3-v3-fix-round-2-review-package.md:23-28`. The fix package contains zero added executable `.focus(` calls and exactly one `field.click()` call. Clicking the same exact labelled readonly input is a direct browser mutation that focuses that selectable control without changing its challenge value.

The surrounding load-bearing sequence is unchanged: `FOCUS_UNCERTAIN` and `browserFocusAttempted` are set before the awaited mutation, `browserFocusFulfilled` and `FOCUSED` are set only after fulfillment, then server state is revalidated before the serial `Control+A` and `Control+C` operations (`task-3-v3-fix-round-2-review-package.md:19-37`). A rejected or transport-uncertain click therefore remains fail-closed and forbids later browser/clipboard mutation under the existing catch path.

## New-breakage review

**No new breakage found; 0 findings.** The direct-byte package changes one line in the exact deliverable only (`task-3-v3-fix-round-2-review-package.md:1-14`). It does not alter counters, serial ordering, exact-tab ownership, sticky server uncertainty, one-shot Call 3 eligibility, challenge handling, redaction, server cleanup, child lifecycle, clipboard comparison/cleanup, retry/fallback boundaries, or authority scope.

## Scoped disposition

**PASS — fix round 2 satisfies the documented-locator correction with no new findings.** This static verdict authorizes no execution. `authorizes_live_execution=false`; any future one-shot run still requires every remaining coordinator review/approval gate and fresh exact user authority.
