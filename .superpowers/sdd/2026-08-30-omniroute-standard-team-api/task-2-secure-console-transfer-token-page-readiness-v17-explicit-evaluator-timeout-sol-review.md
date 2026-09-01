# OmniRoute V17 explicit evaluator-timeout readiness — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only commit
`df60f78c2d5aaa354b2d2cfe5e4224307add1e38` and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-token-page-readiness-v17-explicit-evaluator-timeout-brief.md`.
Its direct parent is the consumed-failed-clean V16 incident commit
`eab7c640add2e0ed5fd5bc22376cd93b5cb2b138`.

I independently reviewed the raw committed bytes, syntax, V16 incident and
predecessor binding, the evaluator timeout diagnosis boundary, normalized V16
semantic equivalence, causal/stable terminal proof, visible query echo,
cross-realm fixed-key validation, output safety, call cardinality, exact-handle
ownership and cleanup, no-retry/no-provider-mutation limits, secret exclusions,
and downstream manual confirmations.

I performed no Chrome, browser, provider, clipboard, credential, process,
network, DNS, routing, Prox-01, or VM action and did not evaluate the V17 cell.
The only workspace write is this assigned review artifact. No inherited dirty
baseline source path was modified or staged.

## Final verdict

**PASS** — no Critical, HIGH, or IMPORTANT finding remains unresolved.

`authorizes_live_execution=false`

## Direct-byte, syntax, and Git evidence

- Reviewed commit: `df60f78c2d5aaa354b2d2cfe5e4224307add1e38`.
- Direct parent: `eab7c640add2e0ed5fd5bc22376cd93b5cb2b138`.
- The reviewed commit adds exactly the assigned V17 brief path.
- V17 brief: `36379` bytes, SHA-256
  `9F1B7B7C4F26EF8DEF2210E1BD39B8A662CBDBF90FB3D59525E8E46196C343AC`,
  Git blob `727e624800a8f2e779f34d5b01daada9c8f4c8b7`.
- Encoding is UTF-8 without BOM and LF-only with zero CR bytes. There is
  exactly one `javascript` fence.
- The executable payload ending at `})();` is exactly `31261` bytes at
  SHA-256
  `6D21204A07C427585C3DE5D8F43F9592A11F2C7E79ECC9DC901F31034AB3EC0E`.
  The Markdown fence separator contributes one additional LF outside the
  executable payload.
- Non-evaluating top-level-awaited JavaScript parse: **PASS**. There is exactly
  one awaited outer IIFE.
- Index before this review write: zero paths. The inherited dirty baseline was
  exactly twelve paths and remained unstaged.

## Diagnosis and timeout boundary

The direct-parent V16 incident records one exact consumed execution: terminal
evaluation was attempted once but did not fulfill; all later query/Create/name/
row reads were skipped; the exact created handle closed once; residue
converged; persistent V16 state became null, ineligible, failed-clean, and
consumed; and no provider or secret action occurred. It explicitly prohibits
retry, continuation, reinterpretation, or use of V16 as PASS evidence.

The incident's sanitized `Error` class does not prove that an omitted transport
timeout was the unique root cause. V17 does not overclaim that proof: it says
the observation is *consistent with* the transport rejecting before the page
loop's longer deadline, then makes one narrowly scoped replacement change.
That is an accurate fail-closed diagnosis boundary.

The pinned installed Chrome API is `58477` bytes at SHA-256
`4BFEB97E958025DB37D52AEA11B75BC70BCA417B4995B0F711C0F07F3DDCCB08`.
Its locator signature accepts
`evaluate(pageFunction, arg?, options?: PlaywrightEvaluateOptions)`, and that
options type contains `timeoutMs?: number` as the maximum setup-and-script
execution time. V17 supplies exactly one third-argument
`{ timeoutMs: 25000 }`, only on the asynchronous terminal evaluator.

The page-local loop retains one exact `20000 ms` deadline, leaving a fixed
`5000 ms` transport settlement margin inside the `25000 ms` evaluator budget.
The outer one-shot execution envelope remains explicitly fixed at `60000 ms`
in the contract, so the documented nesting is `20000 < 25000 < 60000`. The
outer envelope is an action-time controller pin rather than a second page-side
timer; classification and the post-commit tuple must preserve it exactly.

## Exact V16 equivalence and predecessor chain

I extracted both executable payloads and normalized reviewed V16's own `V16`
identifiers/states to `V17`. The normalized diff contains only:

1. the required V16 consumed declaration check;
2. the exact seven-field failed-clean V16 predecessor tuple;
3. the single terminal-evaluator `{ timeoutMs: 25000 }`; and
4. three fixed-equality V16 predecessor booleans in terminal output.

No baseline evaluator, terminal evaluator body, semantic predicate, row
variant, query-echo locator, Create/name/row read, projection helper, success
retention, cleanup branch, counter, or inherited V4 predicate otherwise
changed.

V17 sets its consumed flag before predecessor validation. Before its sole
creation attempt it requires:

- fresh V17 declarations with null/ineligible/uncreated state and both V17
  detach flags and the V17 Cloudflare-read flag false;
- V16 consumed true, exact retained binding null, eligibility false, state
  `V16_READINESS_FAILED_CLEAN`, both detach flags false, and Cloudflare-read
  flag false;
- V15 through V9 consumed with every diagnostic/readiness retained handle
  null; and
- V4 consumed true, binding null, eligibility false, exact state
  `V9_OWNED_TAB_READINESS_FAILED_CLEAN`, both detach flags false, and
  Cloudflare-read flag false.

There is no call, reset, retry, continuation, reinterpretation, reacquisition,
alternate-tab selection, reconnect, or fallback path for V16 or any earlier
gate.

## Inherited semantic completeness and temporal proof

V17 retains the exact public navigation target
`https://dash.cloudflare.com/profile/api-tokens` and the sole fixed non-secret
filter value `OmniRoute secure console R5 20260901`.

The prefill evaluator still requires one connected, visible, empty placeholder
search input in its unique depth-three section; exactly two page tables; zero
page grids, pagination, or busy markers; one section table, search input, and
`tbody`; five physical and visible rows; and zero section status, empty-status,
busy, and Create-like action. Its private fingerprint covers normalized row and
recognized-status text plus visibility and is accepted only as a bounded
unsigned safe integer. It is retained privately and excluded from output.

After the one fixed fill, the terminal evaluator receives the exact prefill
fingerprint. It can set `terminalObserved=true` only when all of the following
hold together:

- the post-fill fingerprint differs from the exact prefill fingerprint;
- one of three exact row variants holds: zero rows; five prefill rows all
  hidden; or one recognized empty-state row with no visible candidate;
- every exact page/section/input/query/table/status/body/busy/matching-row
  predicate is satisfied;
- at least `2000 ms` has elapsed; and
- at least `1000 ms` has elapsed since the latest scoped section mutation or
  fingerprint change.

One section-scoped `MutationObserver` covers attributes, child-list,
character-data, and subtree changes. Fingerprint polling catches visibility or
text changes not represented by a useful callback. Section replacement
disconnects/rebinds observation and resets the quiet clock. `finally` always
disconnects the observer on evaluator return or throw. The initial snapshot
cannot PASS merely because its row shape is transiently acceptable: causal
transition, minimum elapsed time, and quiet time must all become true.

The controller validates and requires the transition, minimum-elapsed, and
quiet-window booleans in terminal semantics, `filterComplete`, and the final
signature. It then separately waits for one exact visible query echo, requires
one exact global actionable `Create Token` button/link, and requires zero exact
token-name text, zero exact matching role-row, and zero normalized evaluator
matching row. This preserves the inherited V4 completeness/query-echo/
token-name/matching-row/Create protections.

## Cross-realm validation and fixed safe output

The inherited `plainRecord` rule accepts only a non-null object whose direct
prototype is null or whose direct prototype's parent is null. Both evaluator
results pass through `trustedProjection`, which requires an exact fixed key
set, reads only fixed boolean/integer/wide-integer allowlists, validates the
same local read that it copies, and returns a new controller-local object.

The baseline evaluator has exactly 19 accepted keys: 18 fixed public fields
plus the private fingerprint. Public baseline output contains only the 18
fixed fields. Terminal validation and output use the exact 25-field schema:
eight booleans and seventeen bounded safe integers. There is no untrusted
spread, untrusted key emission, raw prototype emission, or second read of an
untrusted value after validation.

Terminal output is limited to fixed result/cleanup strings, a sanitized bounded
error-class name, controller booleans, bounded integer counts/depths, trusted
fixed baseline/terminal projections, and locally initialized counters. The
three V16 output fields are fixed-equality booleans. No raw URL, ID, href,
title, attribute, page/row text, fingerprint, DOM, HTML, screenshot, token,
credential, cookie/storage/session value, or clipboard content can be emitted.

## Call cardinality, ownership, and cleanup

Static executable call-site counts are:

- one each: `tabs.new`, fixed `goto`, URL read, fill, exact-handle close,
  terminal write, `MutationObserver` construction, and page timer call site;
- two `waitFor` call sites: initial visible search input and exact visible
  query echo;
- two evaluator call sites: synchronous prefill and bounded asynchronous
  terminal, with exactly one `timeoutMs: 25000` option;
- seven locator count call sites: input, section, query echo, two Create roles,
  token name, and matching row; and
- zero click, press, selected/list/get, connect/reconnect, detach, screenshot,
  clipboard read/write, title, Create/edit/delete, retry, or fallback call
  site.

The sole `tabs.new()` fulfillment is chained into the local and durable V17
bindings before any later statement or await. Controller ownership and full
tab shape are verified before use. PASS retains only that exact handle, marks
it eligible with exact V17 success state, and does not call close.

Every non-PASS creation disposition is fail-closed: rejected creation and
fulfilled-without-object-handle report residue unproven; a malformed non-null
object remains retained and ineligible; a callable exact handle is closed once;
bindings clear only after awaited close settlement; close rejection retains
the exact handle and marks residue unconverged; and failure before creation is
clean with no tab. A missing, malformed, timed-out, truncated, uncertain, or
non-PASS V17 result remains consumed and cannot be retried or manually
integrated.

## Mutation, secrets, and mandatory confirmations

The only page-local mutation is one fill of the fixed non-secret filter value.
Observation performs no second fill and no provider-persistent mutation. The
payload has zero click, press, clipboard, screenshot, selected/list/get,
connect/reconnect, detach, Create/edit/delete, process, DNS, VM, or routing
action.

Executable scans find zero Bearer value, JWT form, or 40-plus-hex secret. The
V4 prestart/read/detach ordering and secret exclusions are unchanged. The final
Create/native Copy/native masked Paste confirmation and the later separate
exact-row deletion confirmation remain explicit and mandatory; V17 neither
performs nor bypasses either checkpoint.

## Findings and residual limits

- Critical: none.
- HIGH: none.
- IMPORTANT: none.
- Minor: the committed Markdown file contains one extra blank line at EOF;
  `git diff-tree --check` reports it at line 761. It is outside the pinned
  executable bytes and has no semantic, security, hash, or execution effect.

This PASS proves only the reviewed committed bytes and current installed API
contract. It does not prove current browser/controller/provider/credential/
process/VM/DNS/routing/persistent-REPL state, nor does it prove the timeout
hypothesis by live execution. A non-self-referential classification, separate
post-commit coordinator tuple, exact `60000 ms` action envelope, and all fresh
action-time pins remain mandatory.

## Final verdict

**PASS**

Unresolved findings: Critical `0`, HIGH `0`, IMPORTANT `0`, Minor `1`.

`authorizes_live_execution=false`
