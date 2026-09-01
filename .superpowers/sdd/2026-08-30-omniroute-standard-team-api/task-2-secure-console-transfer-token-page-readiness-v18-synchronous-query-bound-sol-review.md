# OmniRoute V18 synchronous query-bound readiness — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only commit
`913f324858fe1d67e163a174755768c8204439dc` and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-token-page-readiness-v18-synchronous-query-bound-brief.md`.
Its direct parent is the consumed-failed-clean V17 incident commit
`af89fd65c0dee91a98b2d780eae741e7982c809c`.

I independently checked committed bytes, syntax, the cited fix-round-2 and
fix-round-4 evidence, exact V17/V16/V15-through-V4 predecessor state,
synchronous evaluator and native-wait design, absent-before/present-after
query binding, current V15 structural tuple, V4 empty-marker semantics,
fixed-key output projection, call cardinality, ownership and cleanup, secret
exclusion, no-provider-mutation/no-retry limits, and mandatory confirmations.

I performed no Chrome, browser, provider, clipboard, credential, process,
network, DNS, routing, Prox-01, or VM action and did not evaluate the V18 cell.
The only workspace write is this assigned review artifact.

## Final verdict

**PASS** — no Critical, HIGH, or IMPORTANT finding remains unresolved.

`authorizes_live_execution=false`

## Direct-byte, syntax, and Git evidence

- Reviewed commit: `913f324858fe1d67e163a174755768c8204439dc`.
- Direct parent: `af89fd65c0dee91a98b2d780eae741e7982c809c`.
- The reviewed commit adds exactly the assigned V18 brief path.
- V18 brief: `33142` bytes, SHA-256
  `F0120B467799027CACFFD2428F9AB73555A46D2E371E736CDD5244125742CBA4`,
  Git blob `9c52064b198d050816429e288ab84dbb9f659457`.
- Encoding is UTF-8 without BOM, LF-only with zero CR bytes, exactly one
  final LF, and exactly one `javascript` fence. Commit diff-check is clean.
- The executable payload ending at `})();` is `28838` bytes at SHA-256
  `638074FCE6A7434D5ED0ECB137D57A0FCAB613A50916A9C05F517506C5E26A76`.
- Non-evaluating top-level-awaited JavaScript parse: **PASS**. There is one
  awaited outer IIFE.
- Index before review creation: zero paths. The exact twelve-path inherited
  dirty baseline was present and remained unstaged.

## Root-cause evidence and consumed predecessor boundary

The direct-parent V17 incident records the exact reviewed V17 payload as
consumed once and failed clean: baseline and the one fixed fill completed;
terminal evaluation was attempted once but did not fulfill; all later reads
were skipped; the exact created tab closed once; residue converged; and no
provider or secret action occurred. Its durable V17 binding is null,
ineligible, failed-clean, and consumed. It also records the exact failed-clean
V16 predecessor.

V17 reproduced V16's attempted/not-fulfilled boundary after adding a supported
`25000 ms` transport option around the unchanged asynchronous `20000 ms`
page-local loop. That falsifies the narrow claim that merely omitting that
option was sufficient to explain or fix the result. The sanitized `Error`
class alone does not prove a unique runtime cause, and V18 appropriately says
the repeated rejection is *consistent with* the independently established
asynchronous-evaluator violation rather than treating it as sole proof.

The cited fix-round-2 Sol High review
`080f9bec66a3b8f94b93e59e0c5e5463d9695401` specifically rejected persistent
page-resident `MutationObserver`, timer, Promise, expando, and cross-evaluate
state inside the documented read-only evaluator. The cited fix-round-4 PASS
`139c0b971d120647c319d3b5b5672aca67f94db9` accepted synchronous read-only
snapshots with directly and serially awaited native locator operations. V18
returns to that reviewed safe boundary instead of altering timeouts or retrying
V16/V17.

V18 consumes itself before predecessor validation and, before its sole tab
creation, requires both V17 and V16 consumed, exact retained binding null,
eligibility false, exact failed-clean state, both detach flags false, and
Cloudflare-read flag false. It also requires V15 through V9 consumed with all
retained diagnostic handles null and the exact V4 consumed/null/ineligible/
failed-clean/no-detach/no-read tuple. Fresh V18 declarations must still be
null, ineligible, uncreated, and unused. No earlier gate is called, reset,
continued, reinterpreted, reacquired, or retried.

## Synchronous browser boundary

Static inspection of the exact executable proves:

- exactly two locator `evaluate` call sites;
- both evaluator callbacks are synchronous read-only functions;
- zero asynchronous evaluator callback;
- zero `MutationObserver`, page timer, page `Promise`, performance clock,
  expando, interval, or cross-evaluate page state; and
- all native operations occur in direct serial `await` order.

The first evaluator takes one complete prefill snapshot. After it settles,
controller calls establish target/marker absence, perform the single fixed
fill, wait for the visible exact query echo, wait for the visible exact empty
marker, and only then invoke the second synchronous evaluator. There is no
concurrent wait, Promise race, repeated snapshot loop, post-rejection page
cleanup helper, or background page work capable of surviving the call.

The installed Chrome API remains `58477` bytes at SHA-256
`4BFEB97E958025DB37D52AEA11B75BC70BCA417B4995B0F711C0F07F3DDCCB08`.
It documents locator `evaluate` as read-only and exposes locator `or`, which
V18 uses only to union the exact empty-status and exact empty-row locators.

## Current V15 structural tuple and prefill completeness

V15's immutable live report records one unique visible empty search input,
two page tables, zero page grid/pagination/busy markers, and the unique nearest
depth-three section with one search input, one table, one `tbody`, five rows,
five visible rows, and zero busy/status/empty-status/Create-like marker.

V18 requires that exact current tuple before fill. It additionally requires
the input connected, visible, and empty, and validates the evaluator result as
an exact fixed-key record before using it. A changed or partial page cannot
advance to the fill.

Before the fill, V18 constructs the exact target-text locator and the union of
the two permitted V4 empty markers, then serially counts both. It requires
`prefillTargetTextCount === 0` and `prefillEmptyMarkerCount === 0`. Because the
baseline separately proves the input empty, neither a restored prior query nor
a stale hidden/visible empty-result marker can satisfy the precondition.

## Absent-before/present-after causal binding and V4 semantics

After exactly one fill of the fixed non-secret query, V18 serially requires:

1. the exact target text visible in the same unique section, then exact count
   one;
2. one visible exact empty marker, either `No API Tokens Found` or
   `No Tokens Found`, then exact union count one; and
3. a final synchronous snapshot from the same unique input and nearest section.

The terminal snapshot requires the input connected and visible with exact
normalized target value and exactly one target-valued search input. It retains
the exact depth-three/two-page-table/one-section-table/one-search/one-`tbody`
tuple and requires zero page/section busy, grid, or pagination marker.

The exact V4 terminal representations are preserved:

- zero rows plus one visible exact status marker;
- five physical rows all hidden plus one visible exact status marker; or
- one visible exact empty row and zero visible candidate row.

Every representation also requires exactly one visible empty marker in total,
zero visible candidate rows, zero normalized matching target rows, and bounded
recognized status/empty-row counts. The separate exact target-name count,
exact matching role-row count, and evaluator all-row matching count must all be
zero. One exact global actionable `Create Token` button/link is still required.

Thus the accepted transition is bound to a fresh known nonempty prefill state,
the one fixed query, a native visible echo, a native visible V4 empty marker,
and a complete synchronous terminal tuple. V18 does not relax completeness or
reuse the rejected time-based observer proof.

## Cross-realm validation and fixed safe output

The inherited cross-realm predicate accepts only a non-null object whose direct
prototype is null or whose direct prototype's parent is null. `exactKeys` then
requires the exact schema, and `trustedProjection` reads, type/range-checks,
and copies only fixed allowlisted boolean and integer keys into a new local
record.

The baseline evaluator/projection/output schema is exactly 18 keys: four
booleans and fourteen bounded integers. The terminal evaluator/projection/
output schema is exactly 25 keys: five booleans and twenty bounded integers.
There is no untrusted spread, untrusted key emission, raw prototype emission,
or unchecked second read.

Terminal output is limited to fixed result/cleanup strings, sanitized bounded
error class, controller booleans, bounded integer counts/depths, the two trusted
fixed records, locally owned counters, and fixed-equality V17/V16/V4 binding
booleans. It emits no raw URL, ID, href, title, attribute, page/row text, DOM,
HTML, screenshot, token, credential, cookie/storage/session value, secret, or
clipboard content.

## Call cardinality, ownership, and cleanup

Static call-site counts are:

- one each: `tabs.new`, fixed `goto`, URL read, fill, exact-handle close, and
  terminal write;
- three serial `waitFor` calls: initial visible input, post-fill visible exact
  query echo, and post-fill visible exact empty marker;
- exactly two synchronous locator evaluators;
- ten locator counts: input, section, two prefill counts, two post-fill counts,
  two Create-role counts, target-name count, and matching-row count; and
- zero click, press, selected/list/get, connect/reconnect, detach, screenshot,
  clipboard, title, Create/edit/delete, retry, or fallback call site.

The sole `tabs.new()` fulfillment is chained into the local and durable V18
bindings before every later statement or await. Controller ownership and full
tab shape are checked before use. PASS retains only that exact handle, marks it
eligible with exact V18 success state, and never calls close.

Every non-PASS disposition is fail-closed: rejected creation and fulfilled
creation without an object handle report residue unproven; a malformed
non-null object remains retained and ineligible; a callable exact handle closes
once; durable/local bindings clear only after awaited close settlement; close
rejection retains the exact handle and marks residue unconverged; and failure
before creation is clean with no tab. A rejected, timed-out, malformed,
truncated, uncertain, or non-PASS result consumes V18 and cannot be retried or
manually integrated.

## Mutation, secrets, and mandatory confirmations

The sole page-local mutation is one fill of the fixed non-secret search query.
The payload performs no provider-persistent action and contains no click,
press, Create/edit/delete, clipboard, screenshot, process, DNS, VM, routing,
or credential operation.

Executable scans find zero Bearer value, JWT form, or 40-plus-hex secret. The
V4 prestart/read/detach ordering and secret exclusions remain unchanged. The
mandatory final Create/native Copy/native masked Paste confirmation and the
later separate exact-row deletion confirmation remain explicit and mandatory;
V18 neither performs nor bypasses either checkpoint.

## Findings and residual limits

- Critical: none.
- HIGH: none.
- IMPORTANT: none.
- Minor: none.

This PASS proves only the reviewed committed bytes and installed API contract.
It does not prove current browser/controller/provider/credential/process/VM/
DNS/routing/persistent-REPL state or a unique historical root cause. A
non-self-referential classification, separate post-commit coordinator tuple,
and every fresh action-time pin remain mandatory.

## Final verdict

**PASS**

Unresolved findings: Critical `0`, HIGH `0`, IMPORTANT `0`, Minor `0`.

`authorizes_live_execution=false`
