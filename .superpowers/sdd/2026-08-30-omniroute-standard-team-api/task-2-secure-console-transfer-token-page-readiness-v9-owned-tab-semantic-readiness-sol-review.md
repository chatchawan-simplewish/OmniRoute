# OmniRoute V9 owned-tab semantic readiness — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only commit
`b2e0aadcc89d4ae0cda12222b6bc1b85147be163` and its exact added path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-token-page-readiness-v9-owned-tab-semantic-readiness-brief.md`.

The direct comparison point is immutable V8 live-report commit
`9f3343de6e6ab4ee8f60137f3f3e5bdc9502a2bb`, with the reviewed V8 chain
behind it. I reviewed V9 as the sole Sol High security/one-shot reviewer.

I performed no Chrome, browser, provider, clipboard, credential, process,
network, routing, Prox-01, or VM1205 action and did not execute the V9 cell.
The only workspace write before the requested exact-path commit is this
assigned review artifact. No baseline source file was modified or staged.

## Final verdict

**FAIL** — three unresolved **HIGH** findings and one unresolved
**IMPORTANT** finding block PASS and live eligibility.

## Git and direct-byte pins

- Reviewed commit: `b2e0aadcc89d4ae0cda12222b6bc1b85147be163`.
- Direct parent: exact V8 live-report commit
  `9f3343de6e6ab4ee8f60137f3f3e5bdc9502a2bb`.
- The reviewed commit adds exactly the one V9 brief path above.
- Reviewed HEAD equals the target commit before this review commit.
- Index before review: zero paths.
- Exact inherited dirty baseline: twelve source records, preserved.
- V9 brief: `15973` bytes, SHA-256
  `8C014E3BAA1F3DFC893A491D0031330B806CCCD71350D50D138047751F479104`,
  Git blob `c14ad9bcee523a28139994a876f084b2b3806e52`.
- V8 live report: `3214` bytes, SHA-256
  `4006F653859353DE59A8EECC7584A58AEBE4492E25FAE6DA9B65D3AD2AEB776A`,
  Git blob `ed342fe5658bc7414714942cd42231fb435a2c35`.
- V9 encoding is strict UTF-8 without BOM, LF-only, zero CR bytes, and exactly
  one trailing LF.
- `git diff --check` from the V8 report to V9 passes.

## Executable fence and static syntax

The brief contains exactly one `javascript` fence. Its executable content,
including the final LF, reproduces:

- bytes: `11825`;
- SHA-256:
  `3E5C0310A0419D859485E8FE4752848D8D5C40D19DB6603BA1C55173FF7951E7`;
- asynchronous JavaScript syntax: **PASS**.

The syntax check parsed an async wrapper without evaluating the V9 cell or
loading any live browser/runtime resource.

## Findings

### HIGH — the one-shot cell is launched fire-and-forget

The executable starts with:

```javascript
void (async () => {
```

and ends by invoking that async IIFE without awaiting its promise. V9 is the
only reviewed readiness artifact in this chain using this form; the preceding
one-shot cells await their outer IIFEs.

JavaScript evaluates through the first pending await, returns `undefined` from
the outer expression immediately, and leaves the rest of the browser work on a
detached promise. Consequently Node-tool completion is not coupled to fixed
navigation, the two settle intervals, V4 ownership transfer, failure close, or
the sole terminal write. A late rejection outside the internal protected
regions also cannot propagate through the evaluated result.

This permits the tool call to complete while the exact created tab and V4
binding are still being mutated in the background. It destroys the reviewed
one-shot distinction between completed, timed-out, truncated, and uncertain
execution and can leave cleanup/output arriving after the authority boundary.

Required correction: await the outer async IIFE and require the evaluated tool
call itself to remain pending through the terminal/cleanup outcome. Any outer
rejection must be surfaced as a consumed uncertain V9 result, never detached.

### HIGH — predecessor drift can erase an existing exact V4 handle

On every non-PASS, including a predecessor failure before `tabs.new()`, V9
unconditionally executes:

```javascript
secureConsoleOwnedTaskTabV4 = null;
secureConsoleOwnedTaskTabV4Eligible = false;
```

The exact predecessor requires the inherited V4 binding to be null, but drift
is precisely a reviewed failure case. If the inherited binding is unexpectedly
non-null, `predecessorStateExact` fails, the catch runs, and these assignments
discard that pre-existing exact handle without closing it, retaining it under
another durable alias, or reporting that residue.

Because V9 itself has no local tab in that branch, output remains
`cleanupState=NOT_REQUIRED_NO_HANDLE` and
`failureResidueConverged=true`. The cell therefore both creates hidden browser
residue and can falsely report convergence on a precondition failure.

Required correction: never mutate inherited V4 ownership state when the exact
predecessor did not pass. Preserve and report only fixed-equality booleans for
the drifted tuple. Failure handling may change V4 state only after the exact
predecessor is proven and must never erase an unknown or pre-existing handle.

### HIGH — the quiescence proof does not prove an unchanged complete result set

The `settle` helper re-discovers `root` and `table` on every snapshot and
compares only a JSON object of counts/booleans. It does not retain or compare
the exact root/table identity, test `table.isConnected`, observe DOM mutations,
or fingerprint row identity/content. A replaced table or changing rows with
the same row count therefore increments `stable` as though the scoped table
were unchanged.

The helper also returns after the first five equal 100 ms samples. Immediately
after `fill`, the input value is already exact, so a page with a debounce or
result update beginning after 500 ms can satisfy quiescence before the filter
has affected the result table. No filter-owned query echo, result-generation
marker, request completion, or transition proves causal application of the
query. The 40-iteration cap does not protect this branch because success exits
at the first five equal samples.

Finally, two page tables plus no pagination and stable DOM row counts do not by
themselves prove that the scoped table is non-virtualized or represents the
complete server-side token set. The zero-row and exact-name observations may
therefore be a transient or partial view.

This is a false-readiness path for the core no-existing-token gate and can
advance a later confirmed Create despite an unobserved existing exact row.

Required correction: bind the exact root and table once; continuously prove
their identity and connection; reset a mutation quiet-period on any relevant
table/result mutation; require a causal, filter-owned completion/query signal;
and prove the result surface represents the complete non-virtualized data set.
Any internal content fingerprint must remain local and only boolean/count
evidence may be emitted.

### IMPORTANT — the claimed V8-derived page signature is only partially enforced

The V8 live report establishes one placeholder-search input, zero ARIA
textboxes/search-name matches, no `aria-controls`, two tables, and no
pagination. V9 enforces the placeholder count, table count, and pagination
absence but never verifies the zero ARIA textbox/search-name result or absent
`aria-controls` relationship.

V9 can therefore run its replacement semantics on an unreviewed hybrid/drifted
page rather than the exact signature that justified replacing the V4/V7
controlled-paginator proof.

Required correction: before readiness evaluation, reproduce the relevant V8
signature as bounded counts/booleans, including zero ARIA textbox/search-name
matches and absent `aria-controls`, and fail closed on any drift.

## Passing security and specification checks

Subject to the blocking findings above, these reviewed mechanics pass:

- exact executable bytes/hash and static syntax match the brief;
- the V8 persistent predecessor predicate includes fresh V9, consumed V8, null
  V8 retained handle, consumed V4 adoption, null/ineligible V4 binding in exact
  V7-clean state, both detach cells unconsumed, and V4 reads unconsumed;
- exactly one `secureConsoleChromeV5.tabs.new()`, one fixed `tab.goto()`, one
  page-local `tokenFilter.fill()`, one failure-only exact-handle `tab.close()`,
  and one `nodeRepl.write()` call site;
- zero `tabs.selected`, `tabs.list`, `tabs.get`, connect/reconnect, retry,
  fallback, alternate-tab, click, press, screenshot, clipboard, and detach
  calls;
- the returned tab is assigned in one chained fulfillment assignment to local
  and durable V9 bindings before the following statement and every later await;
- on the ordinary exact-predecessor path, the durable V9 handle remains during
  every navigation/count/settle/fill await and while failure close is pending;
- ordinary success assigns the exact tab to V4, then eligibility and exact V4
  state, before clearing the V9 alias; there is no success interval after the
  alias clear without a complete V4 ownership tuple;
- close rejection and malformed returned handles retain the V9 exact value;
  creation rejection and unusable fulfillment remain explicitly residue-
  unproven rather than falsely clean;
- the only URL is the fixed public token page and only its equality boolean is
  output;
- the terminal emits local fixed statuses, sanitized error class, counts, and
  strict booleans; it does not emit the tab, ID, URL, title, page text, DOM,
  raw filter value, raw table content, token value, secret, cookie, storage,
  password, session, or clipboard data;
- no Bearer value, JWT form, or 40-hex secret appears in the executable;
- V9 performs no provider-persistent Create/edit/delete; its only page mutation
  is the expressly scoped search-input fill; and
- the fixed target name, V4 downstream bindings, no-generated-secret
  inspection rule, Create/native Copy/native masked Paste confirmation, later
  separate exact-row deletion confirmation, revocation hold, invalid-token
  proof, and cleanup requirements remain textually preserved.

## Findings by severity

- Critical: none.
- HIGH: `3` unresolved — detached async execution; predecessor-drift V4 handle
  erasure/false convergence; incomplete quiescence/completeness proof.
- IMPORTANT: `1` unresolved — incomplete enforcement of the V8-derived page
  signature.
- Minor: none.

## Residual limits

- This review proves only committed static bytes and does not prove current
  browser, controller, provider, credential, process, VM, DNS, routing, or
  persistent-REPL state.
- V9 must not be classified or consumed from this FAIL review. A corrected
  contract requires a fresh independent Sol High review.
- Static review grants no execution authority.

## Final verdict

**FAIL**

Unresolved findings: Critical `0`, HIGH `3`, IMPORTANT `1`, Minor `0`.

`authorizes_live_execution=false`
