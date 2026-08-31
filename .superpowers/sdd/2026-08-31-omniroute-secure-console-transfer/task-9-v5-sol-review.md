# Task 9 v5 independent Sol High static review

Observed at: `2026-08-31 22:42:50` (`Asia/Bangkok`)

## Verdict

**PASS — FRESH NON-SECRET V5 STATIC CONTRACT ONLY.** The candidate at `f31cbc18b10d132e14909b09acb4047a18248fff` implements the reviewed one-shot state machine, separates the unique challenge request from an optional single favicon request, and preserves fail-closed browser/server/child ownership. No HIGH issue, blocking defect, or new breakage was found.

**Findings: 0.** `authorizes_live_execution=false`.

## Scope and direct checks

Reviewed the direct-byte package and committed brief without evaluating embedded code or performing any live/browser/clipboard/listener/process/credential/routing action.

Direct read-only verification established:

- HEAD exactly `f31cbc18b10d132e14909b09acb4047a18248fff`;
- commit scope exactly one path, `task-9-v5-brief.md`;
- Git index paths `0`;
- dirty source baseline exactly `12` paths;
- pinned `api.json`, `browser-client.mjs`, and project-root `AGENTS.md` sizes/hashes match the brief;
- installed API declarations for `Tabs.new`, `Tab.goto`, `Tab.close`, and the surrounding tab interfaces are present; and
- both fenced JavaScript cells passed Node syntax checking through standard input with `--check --input-type=module`, without evaluation (`JS_SYNTAX_ONLY_PASS=2`).

## Evidence-bound review

### Fresh v5 and immutable authority boundary

The brief declares v5 fresh, not a retry/continuation/fallback/override of v4, and creates fresh v5 challenge, eligibility, and retained-tab bindings plus a fresh ephemeral loopback listener and new tab (`task-9-v5-brief.md:1-11,105-108`). The old v3 listener/server/process remains `NOT PROVEN` and untouched (`:9-11`).

Standing authority permits later consumption only after separately pinned independent PASS and action-time verification of the exact brief/review/API/module/authority pins, empty index, exact 12-path baseline, the existing connected `residualV3Chrome` binding, and never-declared fresh v5 bindings (`task-9-v5-brief.md:42-52`). The actual pinned standing-authority text likewise requires a documented independently reviewed gate and action-time revalidation, and states that failed/uncertain/consumed gates remain spent. Any invocation or uncertainty spends v5 and forbids retry, fallback, override, continuation, alternate tab, reconnect, discovery, or verdict relaxation (`:49-52`).

**PASS:** standing authority does not broaden v5 or revive any spent gate. This static PASS does not itself perform action-time verification or authorize/consume execution.

### Three-call envelope and timeouts

The calls are strictly serial. Call 2 is invoked once with exact orchestrator `timeout_ms=120000`; Call 3 retains only its internal 30000-millisecond child deadline (`task-9-v5-brief.md:54-59`). Call 2 requires exact Call 1 PASS, and Call 3 requires the exact Call 2 success object. No in-cell timer, `Promise.race`, retry, fallback, or second invocation exists.

**PASS:** control and child timeouts are exact and separate; any timeout is terminal and spends the gate.

### Call 1 clipboard baseline

Call 1 clears once, reads once, proves empty, emits bounded v5 counters/error state, clears its local read binding, and exits nonzero on every mismatch (`task-9-v5-brief.md:61-96`).

**PASS:** Call 2 cannot start without exact clear/read `1 / 1`, empty `TRUE`, and error `NONE`; no clipboard value is emitted.

### Existing Chrome binding and fresh server/tab

Call 2 reuses only `residualV3Chrome`, performs no reconnect/documentation/enumeration, and rejects a missing/null/non-callable `tabs.new` binding before resource creation (`task-9-v5-brief.md:98-144`). It then creates a fresh CSPRNG v5 challenge, a separate random exact path, one Node standard-library HTTP server bound to explicit `127.0.0.1:0`, validates the returned address, and opens one new controllable tab (`:145-153,207-236`).

**PASS:** no v4 handle/challenge/server is reused and no browser discovery or alternate tab path exists.

### Main challenge and favicon routing state machine

The page embeds a data favicon (`<link rel="icon" href="data:,">`) so the browser does not need a network favicon, while the server tolerates at most one exact optional `GET /favicon.ico` (`task-9-v5-brief.md:147-154,182-195`).

The unique random main path:

- increments its own attempted counter;
- requires exactly the first occurrence;
- serves the challenge only on that first exact `GET`;
- owns distinct request/response attempted/fulfilled counters; and
- marks every duplicate main request sticky-uncertain and returns a challenge-free 409 (`task-9-v5-brief.md:167-181`).

The optional favicon path:

- accepts only exact `GET /favicon.ico`;
- allows at most one occurrence;
- has four separate favicon counters;
- returns 204 with no body and no challenge; and
- marks any duplicate sticky-uncertain (`task-9-v5-brief.md:182-195`).

Every other path or method increments `unexpectedRequestAttempted`, sets sticky uncertainty, and receives a challenge-free 404 (`:197-201`). Shared lifecycle handlers mark request abort/error, response error/incomplete close, client error, and server error sticky-uncertain (`:154-165,202-206`).

Final acceptance requires main/server/browser counters exactly one, all favicon counters either all zero or all one, unexpected requests zero, sticky uncertainty false, exact tab closed, and exact listener closed (`task-9-v5-brief.md:296-318`).

**PASS:** challenge delivery remains exactly once on the unique main path; optional favicon traffic is bounded, separately evidenced, content-free, and cannot mask a duplicate or unexpected request.

### Strict serial browser stop-first-failure

Browser mutations are directly awaited in exact order: one new tab, goto fresh loopback URL, exact labelled readonly-field click, `Control+A`, `Control+C`, and exact retained-tab close (`task-9-v5-brief.md:231-275`). Attempted counters and `_UNCERTAIN` states precede each promise; fulfilled counters and settled states follow only fulfillment. The exact tab binding is established immediately after new-tab fulfillment and nulled only after close fulfillment (`:235-274`).

Sticky server uncertainty is checked after the main exchange and after each focus/select/copy stage, stopping before the next mutation once observed (`:246-268`). A rejected/uncertain browser promise enters the catch path, retains the exact binding if obtained, and permits only local server cleanup (`:276-295`).

**PASS:** the state machine stops at the first observed failure/uncertainty, never infers remote closure, and performs no later browser or clipboard action after a rejected promise.

### Server cleanup and listener proof

The server start/listen transition is directly awaited and address-validated. Local server close is directly awaited in `finally`; its counter/state are separate from exchange validity. Sticky uncertainty is monotonic, a successful close becomes `CLOSED_AFTER_UNCERTAINTY` when necessary, and exact success requires `serverState=CLOSED`, `server.listening=false`, and `serverUncertain=false` (`task-9-v5-brief.md:209-230,281-318`).

**PASS:** close fulfillment/listening proof cannot rehabilitate a duplicate/unexpected/lifecycle error, and residual-listener ambiguity prevents Call 3.

### Call 2 redacted terminal object

The sole terminal object contains bounded result/error classes, challenge shape/length, fixed numeric counters, tab lifecycle/binding state, and server lifecycle/listening/uncertainty state (`task-9-v5-brief.md:318`). It emits no challenge, clipboard value, HTML, URL, port, request path, tab metadata/content/handle, exception message/stack, credential, key, or token (`:54-59`).

**PASS:** main and favicon evidence is complete without leaking exact values or browser metadata.

### Call 3 one-shot child, exact comparison, and final empty proof

Call 3 consumes eligibility and clears the persistent challenge before its first await or sole child attempt, retaining the challenge only in a local binding and child stdin (`task-9-v5-brief.md:333-363`). Invalid handoff/import state is terminal and non-retryable. The single synchronous no-shell PowerShell 7 child has a 30000-millisecond deadline, bounded buffer/output, hidden window, and fixed environment; the local challenge is nulled in `finally` (`:364-418`).

The child reads the handoff once, validates exact v5 shape/length, reads the clipboard once for exact equality, and always performs one final clear plus one read to prove empty (`:364-389`). The parent accepts only a fixed ordered bounded stdout schema, zero stderr, known exit 0, exact counters/equality/shape/length, both error labels `NONE`, and final empty proof (`:419-439`).

**PASS:** every spawn/stdin/timeout/status/schema/parse/comparison/cleanup uncertainty is terminal; no second child or later browser/clipboard mutation is possible.

### Prohibited authority lanes and reporting

The contract contains no tabs list/get, reconnect, retry/fallback/alternate tab, old-listener/process action, navigation outside the fresh loopback URL, keyboard action outside the exact labelled field, credential, permission, deletion, provider, Cloudflare, VM, proxy, API key, token, OmniRoute, or routing action (`task-9-v5-brief.md:463-471`). A future report is confined to the pinned redacted path and requires separate independent classification (`:13-40`).

**PASS:** no authority expansion or sensitive output path exists.

## Final disposition

**PASS with 0 findings and no HIGH issue.** V5 is a valid fresh static candidate for one later standing-authority consumption only after the sole Sol High owner completes every action-time pin/state check and uses exact `timeout_ms=120000`. Every failure/uncertainty spends v5 and forbids later calls. The old v3 listener/server/process remains `NOT PROVEN`. Static review authorizes no live execution: `authorizes_live_execution=false`.
