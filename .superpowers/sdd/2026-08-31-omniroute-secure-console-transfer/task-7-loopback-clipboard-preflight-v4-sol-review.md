# Task 7 loopback clipboard preflight v4 independent Sol High static review

Observed at: `2026-08-31 21:57:13` (`Asia/Bangkok`)

## Verdict

**PASS — FRESH NON-SECRET V4 STATIC CONTRACT ONLY.** The candidate at `04a75e8b61cfaaed73dc130687e9450a5b2d99c3` is a new one-shot contract, not a retry or continuation of the spent v3/residual gates. No HIGH issue, blocking specification/security/lifecycle defect, or new breakage was found in the direct committed bytes.

**Findings: 0.** The old lost listener/server/process remains `NOT_PROVEN` and outside v4. `authorizes_live_execution=false`.

## Scope and method

Reviewed the corrected v3 design evidence, v3 timeout report/classification, completed residual browser/clipboard disposition report/classification, candidate v4 brief, implementation report, and direct-byte review package. Review was static only. No code was executed, and Chrome, clipboard, listener, port, process, credential, provider, routing, or other live state was not inspected or mutated.

The implementation report's passing strict-byte, parser, non-evaluating JavaScript syntax, operation-cardinality, prohibited-action, installed-API, handoff-ordering, hash, Git-scope, index, and 12-path-baseline checks were not rerun because the direct bytes raised no concrete doubt about them.

## Evidence-bound review

### Fresh-contract and standing-authority boundary

The brief declares v4 fresh, assigns fresh v4 persistent bindings, and treats the completed residual disposition only as proof of the current zero-tab/empty-clipboard baseline; it neither reuses nor continues a spent v3 gate (`task-7-loopback-clipboard-preflight-v4-brief.md:1-9,104-108`). The old listener/server/process is expressly left `NOT_PROVEN` and untouched (`:6-9`).

Execution requires separately pinned independent PASS plus sole-owner action-time revalidation of exact brief/review bytes and hashes, the pinned standing-authority file, empty index, exact 12-path baseline, and existing non-null Chrome binding (`task-7-loopback-clipboard-preflight-v4-brief.md:39-48`). Any missing pin, mismatch, rejection, timeout, malformed result, or uncertainty spends the fresh gate and forbids retry, fallback, continuation, and later calls (`:47-54`).

**PASS:** standing authority can be consumed only after this static PASS and fresh action-time pin/state verification. Every earlier gate remains spent and non-retryable; v4 itself becomes spent on its sole invocation regardless of outcome. This review does not perform the later revalidation or consume authority.

### Orchestrator and timeout envelope

The sole orchestrator invocation of Call 2 is pinned to `timeout_ms=120000`; every other timeout and every second invocation are outside contract (`task-7-loopback-clipboard-preflight-v4-brief.md:50-52`). This directly addresses the recorded v3 45000-millisecond control timeout without adding an in-cell timer, `Promise.race`, retry, fallback, or second call. The PowerShell child deadline remains independently fixed at 30000 milliseconds (`:52`). Calls remain serial, with Call 2 gated by exact Call 1 PASS and Call 3 gated by the exact Call 2 success object (`:54-58`).

**PASS:** the tool-control deadline and child-process deadline are separated and exact. A control timeout still fails closed and spends v4; the longer envelope does not relax any result or cleanup requirement.

### Call 1 baseline clipboard state

Call 1 clears once, reads once, proves empty, emits only bounded v4 counters/state/error class, nulls its local value, and exits nonzero on any mismatch (`task-7-loopback-clipboard-preflight-v4-brief.md:60-95`).

**PASS:** exact `1 / 1` clear and read plus empty proof and error `NONE` are required before Call 2, with no clipboard value emitted.

### Strict existing Chrome precondition and fresh resources

Call 2 uses only the existing `residualV3Chrome` binding and performs no reconnect, documentation call, tab enumeration, or get (`task-7-loopback-clipboard-preflight-v4-brief.md:97-103`). Before importing Node modules or creating any resource, it requires a non-null object with callable `tabs.new` (`:139-142`). It then creates a fresh CSPRNG challenge and separate random path, one new Node standard-library HTTP server, and one fresh controllable tab (`:143-151,204-209`).

**PASS:** a missing/malformed binding fails before server or browser mutation; v4 does not reuse an old tab, challenge, listener, or server handle.

### Loopback server and one-use exchange

The fresh server binds explicitly to `127.0.0.1` on port `0`, validates the returned loopback address, and derives the exact URL locally (`task-7-loopback-clipboard-preflight-v4-brief.md:180-203`). Only the first exact `GET` and random path receives the challenge page; every extra/wrong request is rejected without challenge exposure and sets sticky uncertainty (`:152-174`). Required no-store/content-type/nosniff/no-referrer headers are present, and request abort/error, response error/incomplete close, client error, server error, start error, invalid address/lifecycle, residual listener, and close uncertainty all set the monotonic latch (`:152-180,211-221,254-268`).

Server close is directly awaited; fulfilled cleanup cannot erase earlier uncertainty and yields `CLOSED_AFTER_UNCERTAINTY` when applicable (`:254-268`). Exact success requires server state `CLOSED`, false listening, and false sticky uncertainty (`:269-285`).

**PASS:** one fresh loopback-only ephemeral listener, one exact challenge response, sticky lifecycle uncertainty, directly awaited cleanup, and no residual-listener inference meet the contract.

### Exact serial browser flow and retained ownership

The browser path directly awaits exactly one `tabs.new`, `goto`, labelled readonly-field `click`, `Control+A`, `Control+C`, and close in strict order (`task-7-loopback-clipboard-preflight-v4-brief.md:204-249`). Attempted counters and `_UNCERTAIN` states are set before each promise; fulfilled counters and settled states are set only afterward. The exact tab is retained immediately after creation and cleared only after its exact close fulfills (`:207-249`).

Any rejected/transport-uncertain browser promise enters the catch path, retains the exact binding if obtained, and permits only local server cleanup in `finally`; it performs no later browser or clipboard mutation (`:250-268`). Exact Call 2 success requires all 20 attempted/fulfilled counters exactly one, exact tab closed, retained binding false, server closed, and both browser/server uncertainty false (`:269-285`).

**PASS:** browser mutations are serial and directly awaited; closure is never inferred from an attempt; failure leaves bounded evidence and no prohibited follow-on action.

### Call 2 result redaction

The one result object contains only bounded result/error classes, challenge shape/length, numeric counters, tab closure/binding state, server lifecycle/listening state, and sticky uncertainty (`task-7-loopback-clipboard-preflight-v4-brief.md:276-285`). The contract forbids output of the challenge, clipboard value, URL, port, path, HTML, tab ID/title/URL/content/handle, exception message/stack, credentials, keys, or tokens (`:54-58`).

**PASS:** no exact value, browser metadata, or credential-like data crosses the result boundary.

### Call 3 one-shot handoff, exact comparison, and final cleanup

Call 3 first snapshots eligibility and the challenge to local state, then clears both persistent bindings before its first await or child attempt (`task-7-loopback-clipboard-preflight-v4-brief.md:298-307`). Invalid state and import failure are terminal and non-retryable (`:302-317`). The sole synchronous, no-shell PowerShell 7 child receives the challenge only through stdin, has a 30000-millisecond timeout, hidden window, bounded buffer, and restricted environment; the local challenge is nulled in `finally` (`:358-372`).

The child reads the handoff once, validates shape/length, reads the clipboard once for exact comparison, and always enters one final path that clears once and reads once to prove empty (`:318-357`). The parent accepts only a fixed ordered bounded schema, zero stderr, known exit status, exact counters/equality/shape/length, both error labels `NONE`, and final empty proof (`:373-392`). Every spawn, stdin, timeout, signal, status, parse, schema, comparison, or cleanup uncertainty is terminal and permits no second child or later browser/clipboard mutation (`:393-402`).

**PASS:** eligibility is consumed and challenge authority detached before the sole child; comparison and cleanup are exact, redacted, bounded, and non-retryable.

### Installed API and prohibited authority lanes

The pinned installed declarations cover `Tabs.new`, `Tab.goto`, `PlaywrightLocator.click`, `PlaywrightLocator.press`, and `Tab.close` (`task-7-loopback-clipboard-preflight-v4-brief.md:35-38,411-419`). The implementation uses those documented interfaces and contains no `.focus`, tabs list/get, reconnect, timer race, retry, fallback, alternate tab, old listener/process action, navigation outside the fresh loopback URL, keyboard action outside the exact labelled field, credential, permission, deletion, provider, Cloudflare, VM, proxy, API key, token, OmniRoute, or routing action (`:420-423`).

**PASS:** no authority expansion or undocumented browser operation was found.

## Final disposition

**PASS with 0 findings and no HIGH issue.** V4 is a valid fresh static candidate for one later standing-authority consumption only after the sole Sol High owner revalidates every action-time pin and precondition and uses the exact 120000-millisecond Call 2 control timeout. Every failure/uncertainty spends v4 and forbids continuation. The old listener/server/process remains `NOT_PROVEN`; no credential or routing work is authorized. Static review authorizes no live execution: `authorizes_live_execution=false`.
