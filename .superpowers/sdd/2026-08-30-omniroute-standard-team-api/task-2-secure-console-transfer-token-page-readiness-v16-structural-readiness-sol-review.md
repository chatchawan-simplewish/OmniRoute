# OmniRoute V16 structural token-page readiness — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only commit
`4f985c80cd4b3793702caf7836b790d9b4fe6716` and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-token-page-readiness-v16-structural-readiness-brief.md`.
Its direct parent is immutable V15 live-report commit
`c0127cc5340a44958853cb3bc871527632edb72a`.

I independently reviewed raw committed bytes, syntax, the V15/V14 consumed
predecessor chain, inherited V4 token-page semantics, the two evaluators,
bounded observation, row variants, cross-realm validation, fixed-output
boundary, call cardinality, success retention, every cleanup branch, secret
exclusions, no-provider-mutation limits, and downstream confirmations.

I performed no Chrome, browser, provider, clipboard, credential, process,
network, DNS, routing, Prox-01, or VM action and did not evaluate the V16 cell.
The only workspace write is this assigned review artifact. No inherited
baseline source path was modified or staged.

## Final verdict

**FAIL** — two HIGH and one IMPORTANT finding remain unresolved.

`authorizes_live_execution=false`

## Findings

### HIGH V16-001 — terminal readiness can accept a transient post-fill state

The page-local `terminalShape` at brief lines 412–445 accepts its first
post-fill snapshot immediately whenever one of the three row shapes is already
true. The `20000 ms` deadline is only a maximum: there is no minimum elapsed
time, repeated-identical-snapshot requirement, mutation observation, causal
table transition, content fingerprint change, or quiet interval. The loop is
skipped completely if the first snapshot matches.

In particular, this exact first snapshot passes the committed predicate:

- input exact and query-input exact count `1`;
- exact section/page tuple, no busy/pagination/status marker;
- the five baseline rows still present but temporarily hidden;
- visible-candidate, empty-row, and matching-row counts all `0`.

An offline reproduction of the committed predicate returned
`immediate_hidden_baseline_shape_pass=true`. This is a plausible intermediate
state after the one fill has hidden current rows but before a debounced,
asynchronous, or rendered result transition has settled. Because the code can
return on that first snapshot, the subsequent zero name/row counts can be
sampled during the same transient and V16 can retain the tab as eligible even
though filtered completeness has not been proved.

The controller-side query-echo check at line 497 is also only `count()`. Unlike
the V4 contract, it has no visible `waitFor` or equivalent visibility proof, so
a hidden query echo can satisfy the inherited `1` count. V4 explicitly waited
for the exact query echo and exact empty result state to become visible before
claiming terminal completeness. The current async evaluator therefore does not
preserve V4's completeness/query-binding protection merely by being bounded.

Impact: a false no-existing-token readiness PASS can authorize the later
prestart chain against an incompletely filtered page. That is a fail-closed
security boundary, so severity is HIGH.

Required correction: add a bounded causal and stable terminal proof. Because
the proved baseline is nonempty, this must at minimum exclude the first
transient hide by demonstrating a post-fill exact-table/section transition and
a settled final state (for example, a private fingerprint change plus minimum
elapsed and mutation-quiet windows or an equivalently strong bounded proof),
and restore an exact visible query-echo requirement. The corrected predicate
must be independently reviewed; V16 must not be executed as written.

### HIGH V16-002 — `undefined` fulfillment escapes the no-handle cleanup branch

After a fulfilled `tabs.new()`, V16 permits any value to be assigned durably to
`tab` before checking `createdHandleCaptured`. If fulfillment returns
`undefined`, the capture check throws and reaches post-catch cleanup. At brief
line 539, however, `tab !== null` is true for `undefined`, so line 540 evaluates
`typeof tab.close`. Property access on `undefined` throws `TypeError` outside
the main `try/catch` and before the explicit fulfilled-without-handle branch at
lines 569–572.

The offline language-level reproduction returned:

```text
undefined_not_null=true
undefined_close_guard_throws=TypeError
```

Consequences are a missing terminal write, consumed V16 with its durable
binding left `undefined`, state still `UNCREATED`, and no explicit
`NEW_FULFILLED_WITHOUT_HANDLE_RESIDUE_UNPROVEN` disposition. This contradicts
the contract that every malformed/no-handle result is classified fail-closed
and that missing output cannot hide residue.

Impact: an uncertain creation result can bypass the reviewed residue state and
cleanup evidence. Severity is HIGH.

Required correction: test the fulfilled-without-handle condition before any
handle property access, or require `tab !== null && tab !== undefined` before
the close-shape branch and use property access that cannot throw for a nullish
value. Preserve the durable returned value/status and classify residue as
unproven without claiming a clean close.

### IMPORTANT V16-003 — validated objects are re-enumerated by untrusted spread

The controller correctly checks cross-realm plain-record shape, exact keys,
types, and ranges. It then copies the two untrusted results using:

```javascript
baseline = { ...untrustedBaseline };
terminal = { ...untrustedTerminal };
```

at brief lines 337 and 466. These spreads perform a second untrusted key
enumeration and a new set of property reads after validation. The accepted
cross-realm plain-record predicate does not exclude an accessor object or
Proxy. Such an object can expose the exact expected keys/safe values during
validation and then expose an additional raw key or changed value during the
spread. That additional key/value is retained inside `baseline` or `terminal`
and emitted by the fixed terminal object without another allowlist check.

This regresses the established safe-projection boundary used by the V15 chain:
validated output must be projected by the fixed expected-key allowlist, never
by re-spreading the untrusted record. The committed page callbacks themselves
construct safe literals, which limits current practical reach, but the code
explicitly treats the bridge result as untrusted and claims fixed output under
malformed return values. The implementation does not fully enforce that claim.

Required correction: construct fresh trusted objects by assigning only the
fixed expected keys, with each value accepted/copied under the same type/range
check; do not enumerate or spread the untrusted object after validation.

## Verified direct-byte and Git evidence

- V16 commit: `4f985c80cd4b3793702caf7836b790d9b4fe6716`.
- Direct parent: `c0127cc5340a44958853cb3bc871527632edb72a`.
- The V16 commit adds exactly the assigned brief path.
- V16 brief: `32161` bytes, SHA-256
  `D0E74B275AC38F0AD586520B418E4A0F4F88CA4CA8CC2E168D231667E2BD9B86`,
  Git blob `7c09297796eaa8914852324c5f569b18ef6ffb02`.
- Encoding is UTF-8 without BOM, LF-only with zero CR bytes and one final LF.
  There is exactly one `javascript` fence. Parent-to-target
  `git diff --check` passes.
- Executable including its final LF: `25837` bytes, SHA-256
  `BDA416FDCA5D4943CDCA9FC225C07973C2A660AB5D90993C4F0339122748EF37`.
- Non-evaluating top-level-awaited JavaScript parse: **PASS**. The outer IIFE
  is awaited exactly once.
- V15 live report: `4381` bytes, SHA-256
  `0123216F0C2E042128BA04574D3B14BB3DA952BF0732D7D1D7B3785C3AF25725`,
  Git blob `8dc8c73e9397b4c0ce9039fae27b1a0e2bfbc1e4`.
- Index before review: zero paths. Exact inherited dirty baseline: twelve
  records, preserved and not staged.

## Verified predecessor and no-retry chain

The exact linear chain is intact:

1. V15 brief `1704a3a80237b829b81cf1cc0ba69faaf81b7448`;
2. independent V15 PASS review
   `7982d986190f68c9cfb6e2c6d477e69355891963`;
3. V15 classification `3ad8f1c89981fc2c7b79e896023626c327671f51`;
4. V15 live report `c0127cc5340a44958853cb3bc871527632edb72a`;
5. V16 brief `4f985c80cd4b3793702caf7836b790d9b4fe6716`.

Each commit has the preceding commit as its direct parent and changes exactly
its named artifact. The V15 report records one exact PASS, exact close,
converged residue, null retained V15 binding, no provider mutation, and the
unchanged V4 null/ineligible/state tuple.

V16 sets its consumed flag before checking the predecessor. Its precondition
requires consumed V15 through V9 with every retained handle null, consumed V4
with exact null/ineligible/failure-clean state, both V4 detach gates false, the
V4 Cloudflare-read gate false, and fresh exact V16 declarations. No V15/V14/V4
invocation, reset, continuation, alternate-tab path, retry, or fallback exists.

## Verified structural and semantic controls not implicated by findings

- The fixed navigation URL and fixed non-secret filter name are exact.
- The unique visible search input and exact depth-3 section are required before
  the one fill.
- Baseline semantics exactly require the V15-proved tuple: two page tables;
  zero grid, pagination, and busy marker; one section table/search/body; five
  visible rows; and zero status, empty-status, busy, and Create-in-section
  marker.
- The terminal evaluator uses only three explicit row variants: zero rows;
  five rows all hidden; or one allowlisted empty-state row with no visible
  candidate. It also requires no page/section busy state, zero matching rows,
  exact section/page tuple, query input exact, and zero or one recognized
  status marker. Finding V16-001 concerns temporal completeness, not the static
  boolean composition of these variants.
- Global exact Create Token semantics require exactly one button/link; exact
  token-name and role-row queries are scoped to the structural section/table
  and require zero matches.
- The baseline schema has exactly `18` keys in its empty, evaluator, and
  expected-key sets. The terminal schema has exactly `22`; neither set has a
  missing, extra, or duplicate declared key.
- The cross-realm helper exactly implements the installed bridge rule:
  non-null object with direct prototype null or direct-prototype parent null.
  The installed bridge remains `149210` bytes at SHA-256
  `C52BA09202F0E82CAA6F6D2A6463A8635C1B1316567975D9B91C1A05FB5AF501`;
  its `135`-byte predicate remains SHA-256
  `CE3E29DA20DBE7CEA1C14DB761B4CB45AC14328DB37722E98BF013669ADBC295`.
- Integer values are required to be safe integers in the bounded range
  `-1..1000000`; semantic PASS narrows the relevant values to exact tuples.

## Call cardinality and mutation boundary

Static AST call counts are:

- one each: `tabs.new`, fixed `goto`, URL read, visible `waitFor`, placeholder
  count, section count, fill, close, terminal write, and page timer call site;
- two evaluator call sites: one synchronous baseline and one bounded async
  terminal evaluator;
- seven total locator count call sites: placeholder, section, query echo, two
  Create roles, token-name, and matching-row;
- two `Object.getPrototypeOf` call sites implementing the exact bridge rule;
- zero click, press, selected/list/get, connect/reconnect, detach, screenshot,
  clipboard read/write, title, Create/edit/delete, retry, or fallback call site.

The fill is the sole page-local mutation and uses only the fixed non-secret
token name. No provider-persistent mutation or secret sink is present.
Executable scans find no Bearer value, JWT form, or 40-hex secret. Raw URL,
ID, title, href, DOM, page text, cookie/storage/session value, screenshot,
clipboard content, and raw prototype are not terminal fields.

## Success retention and remaining cleanup branches

The exact result of `tabs.new()` is assigned simultaneously to local and V16
durable state before every later await. The success path retains only that
exact value, sets eligibility true and exact state
`TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE_V16`, and never calls close. It can reach
the fixed PASS only after all sequential baseline/fill/terminal/query/Create/
name/row checks have completed.

Apart from V16-002's nullish-guard defect, the cleanup branches are fail-closed:

- new rejection reports residue unproven;
- null fulfillment reaches the explicit fulfilled-without-handle residue-
  unproven branch;
- a non-null malformed value without a close function is retained and marked
  ineligible;
- a non-PASS exact handle is closed once; bindings clear only after close
  settles successfully;
- close rejection retains the exact value and marks residue unconverged; and
- precondition failure before creation records a clean no-tab failure.

No failure branch is authorized for retry, fallback, provider action, manual
integration, or verdict relaxation.

## Downstream confirmations and limits

The exact token name, secret exclusions, V4 prestart/detach ordering, final
Create/native Copy/native masked Paste confirmation, and later separate
exact-row deletion confirmation remain explicitly mandatory. Neither manual
checkpoint was reached or bypassed.

This review proves only static committed bytes and current installed bridge
bytes. It does not prove current browser, controller, provider, credential,
process, VM, DNS, routing, or persistent-REPL state. Because the verdict is
FAIL, no classification or action-time tuple may authorize this V16 cell.

## Finding totals and final verdict

- Critical: `0`.
- HIGH: `2` unresolved.
- IMPORTANT: `1` unresolved.
- Minor: `0`.

**FAIL**

`authorizes_live_execution=false`
