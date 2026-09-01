# OmniRoute V16 structural token-page readiness — independent Sol High re-review

Date: `2026-09-02` (`Asia/Bangkok`)

Review round: `fix round 1`

`authorizes_live_execution=false`

## Scope and authority

This re-review covers only fix commit
`3f625370ed49b3cb3aa7185bfc1d934edb01a98d` and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-token-page-readiness-v16-structural-readiness-brief.md`.
Its direct parent is the original FAIL review commit
`4429b770fba3a9de13dc266e18bbad50efd8ddf8`.

I independently rechecked raw committed bytes, syntax, all three prior
findings, exact V15/V14/V4 predecessor and no-retry semantics, V4 semantic
page completeness, both page evaluators, bounded temporal proof, row variants,
cross-realm validation, fixed safe output, call cardinality, success retention,
all cleanup dispositions, secret exclusions, no-provider-mutation limits, and
downstream mandatory confirmations.

I performed no Chrome, browser, provider, clipboard, credential, process,
network, DNS, routing, Prox-01, or VM action and did not evaluate the V16 cell.
The only workspace write is this assigned review artifact. No inherited
baseline source path was modified or staged.

## Final verdict

**PASS** — fix round 1 closes V16-001, V16-002, and V16-003. No Critical,
HIGH, or IMPORTANT finding remains unresolved.

`authorizes_live_execution=false`

## Direct-byte, syntax, and Git evidence

- Fix commit: `3f625370ed49b3cb3aa7185bfc1d934edb01a98d`.
- Direct parent: `4429b770fba3a9de13dc266e18bbad50efd8ddf8`.
- The fix commit modifies exactly the assigned V16 brief path.
- V16 fixed brief: `37213` bytes, SHA-256
  `E969D49A46350365600786F63C2A4272F0C652E3FA5FB707750CF207BA52FFA6`,
  Git blob `d827c537903c701528d5672d4e351272a8a57f07`.
- Encoding is UTF-8 without BOM, LF-only with zero CR bytes and one final LF.
  There is exactly one `javascript` fence. Parent-to-fix
  `git diff --check` passes.
- The exact executable payload ending at `})();` is `30509` bytes, SHA-256
  `CCE8C4592E3F17DCC9580A1A4E84B72AAF881E899E945CC0498C95E2BBA14FCA`.
  The fenced byte slice additionally contains the single Markdown-separating
  LF and is `30510` bytes at SHA-256
  `8DC177A7E24F6B0812E0345F07D10B3F881219A6024493DBCE941E61F4CCD150`.
- Non-evaluating top-level-awaited JavaScript parse: **PASS**. The outer IIFE
  is awaited exactly once.
- Index before review update: zero paths. Exact inherited dirty baseline:
  twelve records, preserved and not staged.

## Prior finding closure

### V16-001 — CLOSED: causal, stable terminal proof and visible query echo

The fixed baseline evaluator derives a private `sectionFingerprint` from row
visibility/text and recognized status visibility/text. The controller accepts
that fingerprint only as an unsigned safe integer bounded to `0xffffffff`,
retains it in a private local, and omits it from public baseline and terminal
output.

After the one fixed fill, the terminal evaluator receives that private
prefill fingerprint and requires all of the following before it can set
`terminalObserved=true`:

- the post-fill fingerprint differs from the exact prefill fingerprint;
- one of the three exact terminal row shapes and every semantic field is true;
- at least `2000 ms` has elapsed inside the evaluator;
- at least `1000 ms` has elapsed since the latest private fingerprint change
  or scoped section DOM mutation; and
- the observation remains within the fixed `20000 ms` deadline.

One scoped `MutationObserver` covers attributes, child-list, character-data,
and subtree changes. Fingerprint polling also catches row visibility/text
changes that do not produce a useful scoped observer record. Section identity
replacement disconnects and rebinds the observer while resetting the quiet
clock. The observer is disconnected in `finally` on every evaluator return or
throw.

The original first-snapshot transient cannot PASS: even when its row predicate
is already true, minimum elapsed and quiet booleans are false and the loop
continues. A transition completed between the fill and evaluator start is
still causally distinguished from the exact nonempty prefill fingerprint, then
must remain terminal for the minimum and quiet windows.

The separate exact query-echo locator is shape-checked, awaited with
`state: "visible"` and `timeoutMs: 10000`, then required to have exact count
`1`. The same section retains the exact input-value/count proof, and the later
exact token-name and matching-row counts remain zero. This restores V4's
visible query-binding protection without repeating the fill or any provider
action.

The controller validates and requires all three fixed stability booleans:
`transitionObserved`, `minimumElapsedSatisfied`, and
`quietWindowSatisfied`. `filterComplete` and the final token semantic signature
also require them, so a malformed or truncated evaluator result cannot bypass
the temporal proof.

### V16-002 — CLOSED: nullish/no-handle cleanup is ordered before handle access

Post-catch cleanup now evaluates these mutually ordered dispositions:

1. attempted-but-rejected new-tab creation;
2. fulfilled creation with `createdHandleCaptured === false`;
3. only then a non-null, non-undefined value eligible for close-shape access;
4. otherwise no tab created.

Thus `null`, `undefined`, and every non-object primitive fulfillment reaches
`NEW_FULFILLED_WITHOUT_HANDLE_RESIDUE_UNPROVEN` before any `.close` property
access. V16 remains consumed, eligibility remains false, and the state becomes
`V16_READINESS_FAILED_RESIDUE_UNPROVEN`; the previous outside-cleanup
`TypeError` path is removed.

An object without a callable close remains retained and ineligible. A callable
exact handle is closed once on non-PASS; local and durable bindings clear only
after awaited close settlement. Close rejection retains the exact value and
marks residue unconverged. No rejected, malformed, nullish, or uncertain
creation path claims clean residue or PASS.

### V16-003 — CLOSED: fixed-key trusted projection replaces untrusted spread

Both controller-side results now pass through `trustedProjection`. The helper:

- requires the pinned cross-realm plain-record rule;
- requires the exact fixed key set;
- reads only fixed boolean/integer/wide-integer allowlists;
- validates and copies each value from the same local read; and
- returns a new controller-local object.

There is no `...untrustedBaseline` or `...untrustedTerminal` spread. The public
baseline is constructed with `Object.fromEntries` over the fixed public
baseline key list; the private fingerprint cannot be emitted. The terminal
object is the fixed projected record. Re-enumeration cannot add a raw key, and
a changed getter value cannot escape without being type/range checked on the
same read that is copied.

## Exact predecessor and no-retry chain

The immutable chain remains linear and exact:

1. V15 brief `1704a3a80237b829b81cf1cc0ba69faaf81b7448`;
2. V15 independent PASS review
   `7982d986190f68c9cfb6e2c6d477e69355891963`;
3. V15 classification `3ad8f1c89981fc2c7b79e896023626c327671f51`;
4. V15 live report `c0127cc5340a44958853cb3bc871527632edb72a`;
5. original V16 brief `4f985c80cd4b3793702caf7836b790d9b4fe6716`;
6. V16 FAIL review `4429b770fba3a9de13dc266e18bbad50efd8ddf8`;
7. V16 fix round 1 `3f625370ed49b3cb3aa7185bfc1d934edb01a98d`.

V15's immutable report remains `4381` bytes at SHA-256
`0123216F0C2E042128BA04574D3B14BB3DA952BF0732D7D1D7B3785C3AF25725`,
Git blob `8dc8c73e9397b4c0ce9039fae27b1a0e2bfbc1e4`. It records one exact V15 PASS,
exact close, converged residue, null retained V15 binding, no provider
mutation, and the unchanged V4 null/ineligible/state tuple.

V16 sets its consumed flag before checking predecessor state. Before its sole
creation attempt it requires consumed V15 through V9 with every retained
handle null; consumed V4 with exact null/ineligible/failure-clean state; both
V4 detach gates false; the V4 Cloudflare-read gate false; and exact fresh V16
declarations. No V15, V14, or V4 call/reset/continuation/reinterpretation, tab
reacquisition, retry, fallback, reconnect, or alternate-tab path exists.

## V4 semantic page signature and completeness

The fixed V16 retains the exact public navigation target and the sole fixed
non-secret filter value `OmniRoute secure console R5 20260901`.

The prefill proof requires:

- one connected, visible, empty placeholder search input;
- its unique nearest depth-3 section;
- exactly two page tables, zero page grid/pagination/busy marker;
- exactly one section table, search input, and `tbody`;
- exactly five physical and visible section rows; and
- zero section status, empty-status, busy, and Create-like action.

The post-fill terminal proof retains exactly three allowlisted complete
representations: zero rows; the five prefill rows all hidden; or one recognized
empty-state row with no visible candidate. Every branch additionally requires
the exact page/section tuple, unique exact query input, zero visible candidate,
zero matching row, zero busy/pagination/grid, one `tbody`, and zero or one
status where every status is recognized. The private causal/stability proof
closes the transient-hide gap without adding a second fill.

The exact visible query echo count is `1`. Global exact `Create Token`
button/link semantics sum to `1`. Exact token-name text under the section table
body and exact role-row matching both remain `0`; the evaluator's normalized
all-row matching count is also `0`. No title, broad page text, raw fingerprint,
or paginator assumption can produce PASS.

## Cross-realm schema and fixed safe output

The installed pinned bridge still independently reproduces:

- `149210` bytes, SHA-256
  `C52BA09202F0E82CAA6F6D2A6463A8635C1B1316567975D9B91C1A05FB5AF501`;
- `isPlainObject` fragment `135` bytes, SHA-256
  `CE3E29DA20DBE7CEA1C14DB761B4CB45AC14328DB37722E98BF013669ADBC295`.

V16's `plainRecord` exactly accepts a non-null object whose direct prototype
is null or whose direct prototype's parent is null. There is no broader
prototype-chain walk.

The baseline evaluator returns exactly `19` keys: `18` fixed public
boolean/integer fields plus the one private unsigned fingerprint. The public
empty/output baseline remains exactly the `18` public keys. The terminal empty,
evaluator, expected, projected, and output records have the same exact `25`
keys: eight booleans and seventeen bounded safe integers. There are no missing,
extra, or duplicate schema keys.

Terminal output is restricted to fixed result/cleanup strings, sanitized
bounded error class, booleans, safe integer counts/depths, the trusted public
baseline/terminal records, and locally initialized/incremented counters. It
does not reference the untrusted records, private fingerprint, raw prototype,
URL, ID, title, href, attribute, DOM, page text, cookie/storage/session value,
screenshot, token value, credential, or clipboard content.

## Call cardinality, ownership, and cleanup

Static AST call-site counts are:

- one each: `tabs.new`, fixed `goto`, URL read, fill, exact-handle close,
  terminal write, `MutationObserver` construction, and page timer call site;
- two visible `waitFor` call sites: initial search input and exact query echo;
- two evaluator call sites: synchronous prefill and bounded async terminal;
- seven locator count call sites: input, section, query echo, two Create roles,
  token name, and matching row;
- two `Object.getPrototypeOf` calls implementing the pinned bridge predicate;
- zero click, press, selected/list/get, connect/reconnect, detach, screenshot,
  clipboard read/write, title, Create/edit/delete, retry, or fallback call site.

The exact `tabs.new()` result is assigned simultaneously to the local and
durable V16 binding before every later await. Controller/tab shape is checked
before use. The fixed success path retains only that exact value, sets
eligibility true and exact state `TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE_V16`, and
never calls close. It reaches fixed PASS only after all baseline, fill,
terminal, visible-echo, Create, name, and row checks complete.

All non-PASS creation/handle dispositions are explicit and fail-closed:
rejection and no-handle fulfillment report residue unproven; malformed object
is retained and ineligible; exact-close success clears only after settlement;
close rejection retains the exact value and marks residue unconverged; and
precondition failure before creation records a clean no-tab failure. Missing,
truncated, timed-out, or uncertain output remains consumed and cannot be
reclassified, retried, or manually integrated.

## Mutation, secrets, and downstream confirmations

The sole page-local mutation is one fill of the fixed non-secret token name.
Repeated observation performs no second fill and no provider action. The code
contains no click, press, Create, edit, delete, provider-persistent mutation,
clipboard operation, secret/credential read, cookie/storage/session operation,
process, DNS, VM, or routing action.

Executable scans find no Bearer value, JWT form, or 40-hex secret. The exact
token name, V4 prestart/read/detach ordering, secret exclusions, final
Create/native Copy/native masked Paste confirmation, and later separate
exact-row deletion confirmation remain mandatory and unchanged. Neither manual
checkpoint is bypassed or reached by V16.

## Findings and residual limits

- Critical: none.
- HIGH: none unresolved.
- IMPORTANT: none unresolved.
- Minor: none.

This PASS proves only fixed committed bytes and current installed bridge bytes.
It does not prove current browser, controller, provider, credential, process,
VM, DNS, routing, or persistent-REPL state. It does not authorize live
execution: non-self-referential classification, a post-commit tuple, and all
fresh action-time pins remain mandatory.

## Final verdict

**PASS**

Unresolved findings: Critical `0`, HIGH `0`, IMPORTANT `0`, Minor `0`.

`authorizes_live_execution=false`
