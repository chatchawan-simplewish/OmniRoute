# Task 8 v4 retained-tab direct-close independent Sol High static review

Observed at: `2026-08-31 22:19:25` (`Asia/Bangkok`)

## Verdict

**PASS — STATIC DIRECT-BINDING TAB-DISPOSITION CONTRACT ONLY.** The candidate at `7cbb93be68786c20c48f92650bacf8baf9f39585` is narrowly scoped to one possible directly awaited close of the exact existing `loopbackPreflightV4RetainedTab` binding. No blocking specification, security, ownership, lifecycle, redaction, authority, or quality finding was found.

**Findings: 0.** `authorizes_live_execution=false`.

## Scope and method

Reviewed the implementation report and the direct-byte package for the single committed brief. Review was static only. No code was executed, and Chrome, clipboard, listener, port, process, credential, provider, routing, or other live state was not inspected or mutated.

The implementation report's passing strict-byte, non-evaluating JavaScript syntax, operation-cardinality, ordering, prohibited-action, installed-API, hash, Git-scope, index, and 12-path-baseline checks were not rerun because the direct bytes raised no concrete doubt about them.

## Evidence-bound review

### Exact retained binding and cleanup-only scope

The brief defines Task 8 as a fresh cleanup-only gate, not a v4 retry or continuation, and limits it to the exact existing `loopbackPreflightV4RetainedTab` binding with no discovery, reacquisition, alternate handle, or other live action (`task-8-v4-retained-tab-close-brief.md:1-8`). It pins the v4 live evidence/classification, installed browser module/API document, standing-authority file, and the documented `Tab.close(): Promise<void>` declaration (`:10-32`).

**PASS:** the contract neither searches for a tab nor substitutes a different handle; ownership is the retained exact binding only.

### Standing-authority and one-shot gate boundary

Consumption is allowed only after separately pinned independent Sol High PASS and action-time verification of all brief/review/evidence/API/module/authority hashes, empty index, exact 12-path baseline, the same persistent Node session, undeclared fresh Task 8 eligibility, and absence of an earlier/uncertain Task 8 invocation (`task-8-v4-retained-tab-close-brief.md:34-48`).

Standing authority permits only this reviewed one-shot after those pins; missing/mismatched state stops before the cell. Invocation permanently spends Task 8 on success, failure, rejection, timeout, malformed/missing output, or tool uncertainty, and explicitly permits no retry, fallback, continuation, or replacement call under that authority (`:50-55`).

**PASS:** standing unattended authority supplies no broader browser, clipboard, listener/process, credential, or routing authority and does not revive any spent v4/preflight gate. This static review does not perform the later action-time verification or consume Task 8.

### Consumed-before-call semantics

The cell declares a fresh Task 8 eligibility binding, snapshots it, and sets it false before inspecting or calling the retained binding (`task-8-v4-retained-tab-close-brief.md:65-82`). Missing, null, or non-callable retained state returns `RETAINED_TAB_BINDING_INVALID` without a browser call (`:80-87`).

**PASS:** every path is non-retryable before the sole possible browser mutation; precondition failure cannot trigger discovery, reacquisition, or an alternate close.

### Exact close cardinality and binding-null ordering

Only after consumed eligibility and strict declared/non-null/callable checks does the cell increment `closeAttempted`, directly await exactly one `loopbackPreflightV4RetainedTab.close()`, increment `closeFulfilled`, set the retained binding to null, then report success (`task-8-v4-retained-tab-close-brief.md:84-93`).

The catch path reports a bounded safe error class, retains the binding unless it is already null, and never infers closure from the attempt (`:94-98`). The single `finally` emits exactly one result object (`:98-101`). PASS requires error `NONE`, close `1 / 1`, exact success result, and retained binding absent (`:104-119`).

**PASS:** the retained binding is nulled only after fulfilled close. Rejected/uncertain close preserves exact ownership for evidence, while the new gate remains spent.

### Redaction and fail-closed result handling

The only output fields are bounded result, safe error class, close attempted/fulfilled counters, and retained-binding presence (`task-8-v4-retained-tab-close-brief.md:67-79,104-114`). No tab handle, ID, title, URL, content, metadata, exception message, or stack is emitted. Missing, extra, malformed, rejected, timed-out, or transport-uncertain output is `NOT PROVEN`; no close or null assignment may be inferred (`:116-119`).

**PASS:** the result is bounded and redacted, and every uncertain tool/result state fails closed without retry.

### Prohibited operations and residual boundaries

The cell has one direct exact-binding close and one result write, with zero tabs list/get/new, discovery, reacquisition, navigation, keyboard, clipboard, listener/server/process/child, retry/fallback, credential, permission, deletion, provider, Cloudflare, VM, proxy, key, token, OmniRoute, or routing action (`task-8-v4-retained-tab-close-brief.md:121-127`). It does not touch the proven-closed v4 listener or the unrelated old v3 listener/process, which remains `NOT PROVEN` (`:126-127`).

**PASS:** no prohibited action or authority expansion exists.

## Final disposition

**PASS with 0 findings.** Task 8 is a valid static candidate for one later direct close of the exact retained v4 tab only, after the sole owner revalidates all action-time pins under the standing authority. Any invocation spends Task 8 permanently. No live action is authorized by this review: `authorizes_live_execution=false`.
