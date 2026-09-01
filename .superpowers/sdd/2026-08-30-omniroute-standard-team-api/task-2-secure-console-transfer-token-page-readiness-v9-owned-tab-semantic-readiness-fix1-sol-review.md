# OmniRoute V9 owned-tab semantic readiness fix 1 — independent Sol High re-review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This re-review covers only fix commit
`89078ba8bb81110df8a4bf9c97efc86b6c2b43ff` and its modification of exact
path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-token-page-readiness-v9-owned-tab-semantic-readiness-brief.md`.

The direct parent and comparison review is committed V9 FAIL review
`ee55bba5bf9a5e64c6f81e3d58b2a60a123c15b8`. I rechecked all four prior
findings and every predecessor, page-signature, completeness, one-shot,
call-cardinality, exact-handle, failure-residue, output, no-mutation, secret,
confirmation, and cleanup constraint.

I performed no Chrome, browser, provider, clipboard, credential, process,
network, routing, Prox-01, or VM1205 action and did not execute the V9 cell.
The only workspace write before the requested exact-path commit is this
assigned review artifact. No baseline source path was modified or staged.

## Final verdict

**FAIL** — the fix closes the four prior findings, but one new unresolved
**HIGH** completeness finding and one new unresolved **IMPORTANT** executable
finding block PASS.

## Git and direct-byte pins

- Fix commit: `89078ba8bb81110df8a4bf9c97efc86b6c2b43ff`.
- Direct parent: prior FAIL review commit
  `ee55bba5bf9a5e64c6f81e3d58b2a60a123c15b8`.
- The fix commit changes exactly the V9 brief path.
- Reviewed HEAD equals the fix commit before this review commit.
- Index before review: zero paths.
- Exact inherited dirty baseline: twelve source records, preserved.
- Fixed V9 brief: `26562` bytes, SHA-256
  `3E321B6DAF9B59E49F78CD55FD87F5DDAD7F6A15E00A2FC4A9E8D5EE33F5643D`,
  Git blob `318849f2383370c5e54131eae031dcf1f870d619`.
- Prior FAIL review: `10691` bytes, SHA-256
  `AADB6FDDBE8A6231BAE5E89D07A0C3459797CDB10B9CA2B8815F44D39B18B05B`,
  Git blob `1f48aa434924c2604fe01af867d5c197a0585c8c`.
- Fixed brief encoding is strict UTF-8 without BOM, LF-only, zero CR bytes,
  and exactly one trailing LF.
- `git diff --check` from the prior FAIL review to the fix commit passes.

## Executable fence and static syntax

The fixed brief contains exactly one `javascript` fence. Its executable
content, including the final LF, reproduces:

- bytes: `21505`;
- SHA-256:
  `27DED59F00F4176195625A42477B28536D3448B7214BD4F989E095E092040CAF`;
- top-level-awaited asynchronous JavaScript syntax: **PASS**.

The syntax check parsed an async wrapper without evaluating the V9 cell or
loading any live browser/runtime resource.

## Prior findings

### Prior HIGH — detached outer async execution: CLOSED

The executable now begins with exactly one awaited outer IIFE and has zero
fire-and-forget `void` outer IIFEs. The evaluated Node call is therefore
coupled to navigation, both settle calls, ownership transfer or failure close,
and the terminal write. Outer completion cannot precede the reviewed async
lifecycle.

### Prior HIGH — predecessor-drift V4 handle erasure: CLOSED

The cell captures only fixed-equality booleans for the inherited V4 tuple.
When `predecessorStateExact !== true`, it performs zero V4 binding/state
assignments, reports
`PREDECESSOR_REJECTED_INHERITED_BINDING_UNTOUCHED`, and proves only that V9
made no creation attempt and retained no V9 handle. All V4 writes are confined
to the exact-predecessor path.

Unexpected inherited handles or states are therefore preserved rather than
erased, and no raw inherited value is emitted.

### Prior HIGH — identity-free 500 ms quiescence: CLOSED as implemented

The fixed cell binds the exact result root and table once, retains their object
identity across the sole fill, and verifies root/table/input connection. An
active MutationObserver spans baseline through filtered terminal. Both settle
calls require at least `1200 ms` elapsed and `1000 ms` mutation quiet, one
physical `tbody`, exact physical-row consistency, no common virtualization
markers, no busy/progress marker, stable internal row-content fingerprint, and
unchanged exact identity.

The internal fingerprint is removed before return and never emitted. The input
listener is installed before fill and the filtered proof requires an observed
input event carrying the exact query. Observer/listener/global identity state
is disconnected and deleted on normal filtered completion; failure close
removes the page, while close rejection leaves the exact V9 handle retained and
residue explicitly unconverged.

The new HIGH finding below is narrower: association of the empty status and
the claimed causal mutation is still insufficiently scoped.

### Prior IMPORTANT — incomplete V8 page signature: CLOSED

Before readiness, V9 now verifies the relevant V8 signature with bounded
counts/booleans: zero exact and broad search-name textboxes, zero total ARIA
textboxes, one placeholder search input, absent `aria-controls`, two page
tables, zero grid, zero Create-token/Create-API-token buttons, and zero
pagination/next/previous controls during both completeness proofs.

V4's Create semantic is preserved by the simultaneous requirements of zero
exact Create button and exactly one exact Create link.

## New findings

### HIGH — empty-state and causal-mutation evidence is not tied to the exact table

The unique empty locator is created globally:

```javascript
const emptyStatus = tab.playwright.getByText(
  /^(no api tokens found|no tokens found|no results)$/i,
);
```

It is not scoped to the retained exact result root/table and does not require a
status role. The reviewed page has exactly two tables, so one global matching
text node can belong to the unrelated table or another page region while the
exact token result table has no empty-state evidence. Both baseline and
filtered `...EmptyStatusCount === 1` can therefore succeed on the wrong result
surface.

The claimed causal table mutation is also derived from the root-wide observer:

```javascript
retainedIdentity.mutationCount > 0 &&
retainedIdentity.lastMutation >= retainedIdentity.lastInputAt
```

The observer watches all subtree child, text, and attribute mutations on the
root and never records whether the mutation target belongs to `exactTable`.
An input/class/attribute mutation after the input event can satisfy
`causalMutationObserved`. Because the baseline fingerprint is not retained for
an explicit before/after table transition, a background table change between
baseline completion and the input event plus an unrelated later root mutation
can be misclassified as filter-caused.

Together these gaps allow the final zero-row table, the empty-state evidence,
and the causal filter evidence to describe different UI surfaces/events. That
is a false-completeness path for the exact no-existing-token gate.

Required correction: scope the recognized empty status to the retained exact
root (preferably an exact status-role locator), and separately track mutations
whose target is the exact table or its descendants. Retain a non-output
baseline table fingerprint/row state and require an exact-table transition
after the captured input event when the baseline is nonempty. Root-wide
unrelated mutations must not satisfy the causal predicate.

### IMPORTANT — `filtered.rootFound` is required but never produced

`settle` now returns fixed booleans including `rootIdentityExact`,
`tableIdentityExact`, `rootConnected`, and `tableConnected`; it has zero
`rootFound` property writes. Nevertheless `filteredComplete` still requires:

```javascript
filtered.rootFound === true
```

For every normal returned proof this value is `undefined`, so the equality is
always false. `filteredComplete`, `semanticSignature`, and exact V9 PASS are
therefore unreachable. A live attempt would consume V9 and close its newly
owned tab even when every intended readiness condition passed.

Required correction: remove the stale predicate in favor of the already
required root identity/connection booleans, or deliberately return and output
a fixed `rootFound` boolean. Recompute and repin executable bytes/hash after the
change.

## Rechecked passing constraints

Subject to the two blocking findings above, these mechanics pass:

- exact executable bytes/hash and static syntax match the committed brief;
- direct executable call cardinality is exactly one each for `tabs.new`, fixed
  `goto`, page-local `fill`, failure-only exact-handle `close`, and terminal
  `nodeRepl.write`;
- click, press, clipboard, selected, list, get, connect/reconnect, retry,
  fallback, alternate-tab, screenshot, and detach call cardinality is zero;
- the exact V8 persistent predecessor remains strict and occurs before the
  sole tab creation;
- one chained fulfillment assignment writes the returned tab to local and
  durable V9 bindings before every later await;
- `23` await expressions occur from exact-handle capture through the success
  transfer boundary; V4 binding, eligibility, and exact state are completed
  before clearing the V9 alias;
- on ordinary exact-predecessor failures the durable V9 handle remains through
  the failure-close await; close rejection and malformed handles retain it,
  while creation rejection/unusable fulfillment remain residue-unproven;
- predecessor rejection performs no tab creation and leaves inherited V4 state
  untouched;
- the only URL is the fixed public token page and only an equality boolean is
  emitted;
- output is limited to local fixed statuses, sanitized error class, counts,
  and strict booleans; the internal row-content fingerprint, page text, tab,
  ID, URL, title, DOM, raw attribute/query values, token, credential, cookie,
  storage, password, session, and clipboard content are not emitted;
- no Bearer value, JWT form, or 40-hex secret occurs in executable code;
- there is no provider-persistent Create/edit/delete; the sole page mutation is
  the reviewed local search-input fill plus non-persistent listener/observer
  instrumentation; and
- the no-generated-secret inspection rule, Create/native Copy/native masked
  Paste confirmation, later separate exact-row deletion confirmation,
  revocation hold, invalid-token proof, retained-owner disposition, and cleanup
  requirements remain preserved.

## Findings by severity

- Critical: none.
- HIGH: `1` unresolved — exact-table empty/causal-result association is not
  proven.
- IMPORTANT: `1` unresolved — stale `filtered.rootFound` makes PASS
  unreachable.
- Minor: none.

## Residual limits

- This review proves only committed static bytes and does not prove current
  browser, controller, provider, credential, process, VM, DNS, routing, or
  persistent-REPL state.
- V9 fix round 1 must not be classified or consumed from this FAIL review. A
  corrected contract requires a fresh independent Sol High review.
- Static review grants no execution authority.

## Final verdict

**FAIL**

Prior findings closed: HIGH `3`, IMPORTANT `1`. New unresolved findings:
Critical `0`, HIGH `1`, IMPORTANT `1`, Minor `0`.

`authorizes_live_execution=false`
