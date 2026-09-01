# OmniRoute V20 visible-candidate-settle readiness — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only commit
`a0c223231019a6abc27bb7fb4508b6476de416aa` and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-token-page-readiness-v20-visible-candidate-settle-brief.md`.
Its direct parent is consumed-failed-clean V19 incident commit
`291ac0a295df7d2d398e97bbf6a5c130c47e0544`.

I independently checked direct committed bytes, syntax, the V19 incident
boundary, dynamic visible-candidate locator semantics, exact prefill count,
`first().waitFor({ state: "hidden" })`, synchronous terminal validation, exact
V19/V18/V17/V16 and inherited predecessor state, V4/V15 page completeness,
fixed output/call cardinality, exact-handle cleanup/no-residue/no-retry,
secret/provider exclusions, and both mandatory confirmation boundaries.

I performed no Chrome, Node browser-binding, provider, clipboard, credential,
process, network, DNS, routing, Prox-01, or VM action and did not evaluate the
V20 cell. The only workspace write is this assigned review artifact.

## Final verdict

**PASS** — no Critical, HIGH, or IMPORTANT finding remains unresolved.

`authorizes_live_execution=false`

## Direct-byte, syntax, and Git evidence

- Reviewed commit: `a0c223231019a6abc27bb7fb4508b6476de416aa`.
- Direct parent: `291ac0a295df7d2d398e97bbf6a5c130c47e0544`.
- The reviewed commit adds exactly the assigned V20 brief path.
- V20 brief: `36543` bytes, SHA-256
  `FBD954D7750A0637E6324A0FFD928983F8C9220738B0ABF26CD9F6BBB32136F6`,
  Git blob `05737fa82ababe3500b6efff066ecad0fbff0f52`.
- The executable payload ending at `})();` is `32151` bytes at SHA-256
  `AE92E996BA324480F98C637BA8B90F2D73EEA2EEACF80BF75E222C90CE238604`.
- Encoding is UTF-8 without BOM and LF-only with zero CR bytes. There is
  exactly one `javascript` fence.
- Non-evaluating top-level-awaited JavaScript parse: **PASS**. The outer IIFE
  is awaited exactly once.
- Index before review creation: zero paths. The exact inherited twelve-path
  dirty baseline was present and remained unstaged.

## V19 incident and smallest replacement boundary

The direct-parent V19 incident reproduces its supplied pins: `3932` bytes,
SHA-256
`9A61D8BFAADE1EE23984D05A0731470DFFDAB53B3BAA520FC92AA654DD72A517`,
Git blob `8c7f6e95eb4a7eee30f93cabfecfe00af963abd0`.

That incident proves V19's exact prefill tuple, absent marker, one fixed fill,
and synchronous exact postfill input value/count. The next native union-marker
wait did not fulfill; terminal evaluation and all later Create/name/row reads
were skipped. The exact created tab closed once, residue converged, and V19 is
consumed, null, ineligible, and `V19_READINESS_FAILED_CLEAN`. No provider or
secret action occurred.

The incident cannot distinguish native union-wait rejection from a page that
settled without either V4 marker. V20 does not infer which occurred and does
not retry V19. It removes only the union-marker wait, retains the proven
synchronous input-value projection, and waits on the independently meaningful
visible candidate-row set before running the unchanged terminal snapshot.

## Dynamic visible-candidate locator semantics

V20 creates this section-scoped lazy locator before fill:

`tokenSection.locator("tbody tr").filter({ hasNotText: exactV4EmptyMarker, visible: true })`.

The installed Chrome API remains `58477` bytes at SHA-256
`4BFEB97E958025DB37D52AEA11B75BC70BCA417B4995B0F711C0F07F3DDCCB08`.
It explicitly documents `LocatorFilterOptions.hasNotText`,
`LocatorFilterOptions.visible`, `first(): PlaywrightLocator`, and
`waitFor` states including `hidden`.

The locator is dynamic rather than a captured element handle: each resolution
selects current `tbody tr` descendants in the same section, excludes rows whose
text is exactly `No API Tokens Found` or `No Tokens Found`, and retains only
currently visible rows. Therefore:

- prefill `visibleCandidateRows.count()` counts the current visible non-empty
  candidate set;
- `.first()` refers to the first currently matching row, not permanently to
  one original row; and
- `first().waitFor({ state: "hidden" })` cannot succeed while any visible
  candidate matches, because every match is constrained `visible: true`.
  It succeeds when the dynamic visible-candidate set becomes empty (no match),
  which is an accepted `hidden` state.

This avoids the unsafe interpretation “the originally first row hid while
others remained”: after that row stops matching, `.first()` reevaluates to the
next visible candidate. The exact empty row is excluded from the candidate set,
so an allowed V4 terminal empty row does not prevent settlement.

## Exact prefill and serial settle sequence

The inherited synchronous baseline first requires the current V15 tuple:

- one connected, visible, empty placeholder-search input in the unique nearest
  depth-three section;
- two page tables and zero page grid, pagination, or busy state;
- one section table, search input, and `tbody`;
- five physical and visible rows; and
- zero section status, empty status, busy marker, and Create-like action.

V20 then requires the derived exact target-valued input count `0`, exact V4
empty-marker union count `0`, and dynamic visible-candidate count exactly `5`.
These three checks are serial and occur before the sole fill.

After exactly one fixed non-secret fill, V20 synchronously proves the same
input is connected and visible, its normalized value is exact, and exactly one
search input in the section has that value. Only then does the single bounded
settle call wait for the dynamic candidate set to become empty. The synchronous
terminal evaluator follows immediately after that wait settles.

No native empty-marker wait remains. An absent/late marker cannot create a
false PASS: the terminal snapshot itself still requires exactly one visible
allowed V4 empty marker and the full row/page/section tuple. A transient or
unexpected state that lacks that complete tuple fails closed and consumes V20.

## Synchronous terminal and V4 completeness

The terminal evaluator is synchronous and read-only. It reproves the exact
query value/count and the depth-three/two-page-table/one-section-table/
one-search/one-`tbody` structure with zero grid, pagination, and page/section
busy state.

The three inherited V4 terminal representations remain exact:

- zero rows plus one visible exact empty status;
- five physical rows all hidden plus one visible exact empty status; or
- one visible exact empty row and zero visible candidate rows.

Every representation requires exactly one visible empty marker in total,
zero visible candidate rows, zero normalized target-matching rows, bounded
recognized status/empty-row counts, and the complete structural tuple. The
final controller checks also require one exact global actionable `Create Token`
button/link, zero exact target-name text in the table body, zero exact
matching role-row, and zero evaluator matching rows.

Thus candidate settlement is only a readiness trigger. It cannot by itself
produce PASS; the fixed-key synchronous terminal snapshot and all independent
Create/name/row completeness checks remain authoritative.

## Synchronous execution and fixed-key validation

The payload contains exactly three locator evaluator call sites: baseline,
postfill query state, and terminal. All callbacks are synchronous and read-only.
There is zero asynchronous evaluator callback, `MutationObserver`, page timer,
page `Promise`, performance clock, expando, polling loop, interval, concurrent
wait, or cross-evaluate page state.

The inherited cross-realm predicate accepts only a non-null object whose
direct prototype is null or whose direct prototype's parent is null.
`exactKeys` requires each exact schema. `trustedProjection` reads only fixed
allowlisted keys, validates and copies each same local read, and returns a new
controller-local object.

- Baseline: exactly 18 fields, four booleans and fourteen bounded integers.
- Postfill query state: exactly four fields, three booleans and one bounded
  integer.
- Terminal: exactly 25 fields, five booleans and twenty bounded integers.

There is no untrusted spread, raw-key/prototype emission, unchecked second
read, raw page object, or fingerprint output. Terminal output is restricted to
fixed result/cleanup strings, sanitized bounded error class, controller
booleans, bounded counts/depths, trusted fixed baseline/terminal projections,
local counters, and fixed-equality predecessor booleans.

No raw URL, ID, href, title, attribute, page/row text, DOM, HTML, screenshot,
token, credential, cookie/storage/session value, secret, or clipboard content
can be emitted.

## Exact predecessor and no-retry boundary

V20 sets its consumed flag before predecessor validation. Before its sole
new-tab attempt it requires V19, V18, V17, and V16 each consumed, retained
binding null, eligibility false, exact failed-clean state, both detach flags
false, and Cloudflare-read flag false. It also requires V15 through V9
consumed with all retained diagnostic handles null, and exact V4 consumed/
null/ineligible/failed-clean/no-detach/no-read state. Fresh V20 declarations
must remain null, ineligible, uncreated, and unused.

No prior gate is called, reset, continued, reinterpreted, reacquired, or
retried. Any missing, malformed, drifted, rejected, timed-out, truncated,
uncertain, or non-PASS state consumes V20 and stops.

## Call cardinality, ownership, and cleanup

Static call-site counts are:

- one each: `tabs.new`, fixed `goto`, URL read, fill, candidate `.first()`,
  exact-handle close, and terminal write;
- two serial `waitFor` calls: initial visible input and postfill dynamic
  candidate-set hidden;
- three synchronous locator evaluators;
- eight locator counts: input, section, prefill marker, prefill candidate set,
  two Create roles, target-name, and matching row; and
- zero click, press, selected/list/get, connect/reconnect, detach, screenshot,
  clipboard, title, Create/edit/delete, retry, or fallback call site.

The sole `tabs.new()` fulfillment is chained into the local and durable V20
bindings before every later statement or await. Controller ownership and full
tab shape are verified before use. PASS retains only that exact handle, marks
it eligible with exact V20 success state, and never calls close.

All non-PASS dispositions fail closed. Rejected creation and fulfilled
creation without an object handle report residue unproven. A malformed
non-null object remains retained and ineligible. A callable exact handle closes
once; bindings clear only after awaited close settlement. Close rejection
retains the exact handle and marks residue unconverged. Failure before creation
is clean with no tab. No non-PASS, missing, malformed, timed-out, truncated, or
uncertain result can claim clean residue incorrectly, be retried, or be
manually integrated.

## Secrets, provider mutation, and mandatory confirmations

The only page-local mutation is one fill of the fixed non-secret search query.
There is no provider-persistent action, click, press, Create/edit/delete,
clipboard, screenshot, credential, process, DNS, VM, or routing operation.

Executable scans find zero Bearer value, JWT form, or 40-plus-hex secret. The
V4 prestart/read/detach ordering and secret exclusions remain unchanged. The
mandatory final Create/native Copy/native masked Paste confirmation and the
later separate exact-row deletion confirmation remain explicit and mandatory;
V20 neither performs nor bypasses either checkpoint.

## Findings and residual limits

- Critical: none.
- HIGH: none.
- IMPORTANT: none.
- Minor: the committed Markdown contains one extra blank line at EOF;
  `git diff-tree --check` reports it at line 755. It is outside the pinned
  executable payload and has no semantic or security effect.

This PASS proves only the reviewed committed bytes and static installed API
contract. It does not prove current browser/controller/provider/credential/
process/VM/DNS/routing/persistent-REPL state. A non-self-referential
classification, separate post-commit coordinator tuple, and all fresh
action-time pins remain mandatory.

## Final verdict

**PASS**

Unresolved findings: Critical `0`, HIGH `0`, IMPORTANT `0`, Minor `1`.

`authorizes_live_execution=false`
