# OmniRoute V9 owned-tab semantic readiness fix 2 — independent Sol High re-review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This re-review covers only fix commit
`f60dd6da398f8817132490313bafa7073b89c80a` and its modification of exact
path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-token-page-readiness-v9-owned-tab-semantic-readiness-brief.md`.
Its direct parent is committed fix-1 FAIL review
`cc85e823b9ea9ada7391d3f5568493bd04f0d449`.

I rechecked the two fix-1 findings and the full predecessor, V8/V4 semantic,
quiescence/completeness, one-shot, call-cardinality, exact-handle,
failure-residue, output, no-provider-mutation, secret, downstream-confirmation,
and cleanup contract. I performed no Chrome, browser, provider, clipboard,
credential, process, network, routing, Prox-01, or VM action and did not execute
the V9 cell. The only workspace write is this assigned review artifact.

## Final verdict

**FAIL** — fix 2 closes both prior findings, but one new unresolved **HIGH**
temporal-causality finding blocks PASS.

## Git and direct-byte pins

- Fix commit: `f60dd6da398f8817132490313bafa7073b89c80a`.
- Direct parent: `cc85e823b9ea9ada7391d3f5568493bd04f0d449`.
- The fix commit changes exactly the V9 brief path; reviewed HEAD equaled the
  fix commit before this review commit.
- Index before review: zero paths. Exact inherited dirty baseline: twelve
  source records, preserved and not staged.
- Fixed brief: `27641` bytes, SHA-256
  `4514DEE42B39150A96EB31BBC05125D7E5412FAE87A36624FE1B7E2E05A2B30F`,
  Git blob `12de721d9b1d26401defac9e487156b6396f8b60`.
- Encoding is strict UTF-8 without BOM, LF-only, zero CR bytes, and exactly one
  trailing LF. `git diff --check` from parent to fix commit passes.

## Executable fence and syntax

The brief contains exactly one `javascript` fence. Including its mandatory
final LF, the executable reproduces the pinned `22483` bytes and SHA-256
`288B6070C8843F787305FF6D11E91CBD3BB59FB86E97E8024BD59BA015D9DD4E`.
An async-wrapper `node --check` parses successfully without evaluating the
cell or loading any live resource. The outer IIFE is awaited exactly once and
there is no fire-and-forget `void` outer IIFE.

## Prior findings

### Prior HIGH — root/table evidence association: CLOSED

The empty-state locator is now scoped beneath retained `tokenRoot`, requires a
status role, and accepts only the three anchored recognized empty strings. The
observer separately increments `tableMutationCount` only when a record target
is the retained exact table or its descendant. Root-wide mutations continue to
drive the conservative quiet period but cannot alone satisfy the table
predicate.

The private baseline fingerprint and row count are retained in the page
identity object and are never returned or emitted. A nonempty baseline now
requires a table mutation signal and a changed final fingerprint; a zero-row
baseline remains gated by the unique exact-root status marker.

### Prior IMPORTANT — stale `filtered.rootFound`: CLOSED

The nonexistent `filtered.rootFound` predicate is removed. Filtered
completeness uses the produced exact root/table identity and connection
booleans, so the intended PASS path is no longer unconditionally unreachable.

## New finding

### HIGH — observer callback time does not prove that the table mutation occurred after the input event

The executable records input time in the input listener:

```javascript
retainedIdentity.lastInputAt = performance.now();
```

but records table-mutation time only when the `MutationObserver` callback is
delivered:

```javascript
retainedIdentity.lastTableMutation = performance.now();
```

and accepts:

```javascript
retainedIdentity.lastTableMutation >= retainedIdentity.lastInputAt
```

Mutation records are delivered asynchronously at a microtask checkpoint. A
mutation of the exact table can therefore be queued before the captured input
event in the same task, while its callback runs after the input listener and
receives a later `performance.now()` value. The current code never calls
`observer.takeRecords()` or otherwise establishes/drains an event boundary.
That pre-input table mutation can satisfy `tableMutationCount > 0` and the
timestamp comparison. If the final fingerprint differs from the retained
baseline, V9 can report `causalTableTransitionObserved=true` without proving
the required exact-table mutation occurred after the captured input event.

This is a false-completeness path in the no-existing-token authorization gate,
so it is HIGH. Root scoping fixes spatial attribution but not this temporal
attribution.

Required correction: establish an unambiguous input-event boundary before
counting table records, for example by draining pre-event observer records at
the captured input event and arming a post-event table-mutation generation in
an ordering that precedes application input handling. Only records belonging
to that post-event generation may satisfy the causal predicate. Recompute and
repin executable bytes/hash after the change.

## Rechecked passing constraints

Subject to the blocking finding above:

- direct executable cardinality is exactly one each for `tabs.new`, fixed
  `goto`, page-local `fill`, failure-only exact-handle `close`, and terminal
  `nodeRepl.write`; click, press, clipboard, selected, list, get, connect,
  reconnect, retry, fallback, alternate-tab, screenshot, and detach call sites
  are zero;
- the exact V8 clean predecessor, consumed V4 adoption, null/ineligible V4
  tuple, unconsumed detach/read gates, and fixed predecessor state are required
  before creation; predecessor drift performs no creation and leaves inherited
  V4 fields untouched while emitting only fixed-equality booleans;
- one chained fulfillment assignment retains the returned handle in local and
  durable V9 state before every later await; success completes the exact V4
  binding/eligibility/state transfer before clearing the V9 alias;
- ordinary failures close only the exact created handle; close success clears
  it only after settlement, while close rejection and malformed fulfillment
  retain the exact handle and creation rejection remains residue-unproven;
- the relevant V8 signature and V4 semantics remain: fixed URL, one
  placeholder input, zero ARIA textbox/search-name matches, absent
  `aria-controls`, two page tables, no grid/pagination, zero Create buttons,
  exactly one exact Create link, stable connected physical table, exact query
  echo, zero filtered rows, unique scoped empty status, and zero exact-name and
  matching-row results;
- both settle phases require at least `1200 ms` elapsed, `1000 ms` mutation
  quiet, content stability, no busy marker, and nonvirtualized physical rows;
- output is restricted to fixed statuses, sanitized error class, counts, and
  strict booleans. No raw ID, URL, title, attribute value, page text, DOM,
  screenshot, secret, fingerprint, token, credential, cookie, storage,
  password, session, or clipboard content is emitted;
- no Bearer value, JWT form, or 40-hex secret occurs in the executable; and
- there is no provider-persistent Create/edit/delete action. The preserved
  contract still requires the final Create/native Copy/native masked Paste
  confirmation and the later separate exact-row deletion confirmation, plus
  the V4 detach ordering, revocation hold, invalid-token proof, retained-owner
  disposition, and cleanup terminals.

## Findings by severity

- Critical: none.
- HIGH: `1` unresolved — callback-delivery time can misclassify a pre-input
  table mutation as post-input.
- IMPORTANT: none unresolved.
- Minor: none.

## Residual limits

- This review proves only committed static bytes. It does not prove current
  browser, controller, provider, credential, process, VM, DNS, routing, or
  persistent-REPL state.
- V9 fix 2 must not be classified or consumed from this FAIL review. A corrected
  contract requires a fresh independent Sol High review.
- Static review grants no execution authority.

## Final verdict

**FAIL**

Prior findings closed: HIGH `1`, IMPORTANT `1`. New unresolved findings:
Critical `0`, HIGH `1`, IMPORTANT `0`, Minor `0`.

`authorizes_live_execution=false`
