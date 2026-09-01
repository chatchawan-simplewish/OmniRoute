# Task 2 token-page readiness replacement — fix-round-1 Sol High review

## Verdict

**FAIL** — one HIGH and two IMPORTANT findings remain. The account binding,
unique click targeting, unique rate-table binding, and source working-projection
digest are materially improved, but the contract still has a reachable UI
false-PASS path and two actionability contradictions.

`authorizes_live_execution=false`.

This is a static review only. It authorizes no browser, clipboard, credential,
Cloudflare, VM, SSH, process, routing, or other live action.

## Reviewed source and integrity

- Fix-round-1 brief commit: `cbb2209a375b8f17b8745513f7e43bde3f0b377a`.
- Direct parent: `db8da1890e519997b2063cbf4c9bd947d9e43bd6`.
- Exact brief: `task-2-secure-console-transfer-token-page-readiness-replacement-brief.md`.
- Direct bytes: `42057`.
- SHA-256: `A901FAB22A750DB64ACBE38148EB67A961BCE5C600700C3FA33EF129B93474C4`.
- All four JavaScript fences match the supplied byte/SHA-256 pins exactly and
  pass non-evaluating `node --check` with empty stdout/stderr.
- The inherited PowerShell pins remain byte-identical to their already reviewed
  fences; no passing inherited parser suite was rerun because the fix raised no
  PowerShell syntax or identity doubt.
- The supplied source working-projection proof is
  `C4C9807FD5667E872BCBCFFD60FBF2AA71AEBC788AC744EFCD93FF18457C8E0F`
  over `10653` records, with index `0` and the exact filtered baseline of `12`.
  The finding below concerns the later attestation design, not that reproduced
  digest.

## Chrome API and mechanical cardinality

The installed Chrome control API version `26.825.51511` declares every method
used by the fix: `Tabs.get`, `Tab.goto`, `Tab.url`, `Tab.title`, locator
`count`, `fill`, `click`, `waitFor`, `getAttribute`, `filter`, and read-only
`evaluate`. The evaluate callbacks are syntactically read-only, and the dynamic
rate-panel selector is constrained before use.

The source mechanically contains the claimed one V3 get/navigation/readiness
sequence, four fresh-read navigations, nine unique-locator click helper calls,
and twenty-one readiness helper calls. Each click helper now rejects locator
counts other than one. Those counts are correct but do not prove that a visible
empty marker is fresh for the current filter value.

## Prior finding disposition

### Prior HIGH — wrong-account and unscoped rendered-list proof: partially corrected

The zone href now requires an exact 32-lowercase-hex segment and exact zone path.
The Zero Trust href and post-navigation URL require exact
`one.dash.cloudflare.com`, root-or-home path, and the same private account
segment; an in-page account marker is also required (brief lines 454-544).
Navigation clicks require count one. The rate proof binds one table to the exact
`aria-controls` panel instead of walking an incidental fixed parent depth
(lines 481-524). These changes close the prior wrong-account and ambiguous-click
subfindings.

The filtered-list completeness path still permits stale results to satisfy the
terminal; see HIGH finding 1.

### Prior IMPORTANT — source-head drift: partially corrected

The closed path allowlist, exact working-byte projection, index-zero condition,
and exact filtered dirty baseline now provide a stable source-state proof across
named artifact commits (lines 57-89). This closes the unbounded HEAD-drift
ambiguity. The required execution-classification self-attestation is impossible
as written; see IMPORTANT finding 2.

## Findings

### HIGH 1 — a stale already-visible empty marker can satisfy a later filter query

The `filteredZero` helper does not prove that the rendered result set corresponds
to the current query:

1. It clears the textbox and immediately samples the entire `main` element
   without waiting for the clear operation's result transition (lines 395-418).
   If the previous query's empty marker remains visible, the sampled baseline is
   accepted as `baselineCompleteEmpty`.
2. It fills the new query and waits for the same broad
   `/^(?:no results|no .* found)$/i` marker (lines 419-430). When that marker is
   already visible from the preceding query, `waitFor(visible)` can resolve
   immediately before the new filtered result is rendered.
3. Exact textbox value, zero current target locators, `aria-busy=0`, and no
   narrowly labelled `Next` control do not bind the result generation to that
   value. The UI need not expose network/debounce work through `aria-busy`, and
   the code does not require a marker disappearance/reappearance, result epoch,
   query echo, zero data-row count, authoritative result total, or exact
   pagination component.

This is concretely reachable because the same Tunnel filter is called twice in
sequence (lines 552-558), as is the same Access filter (lines 568-574). The
second call can consume the first call's still-visible empty result while its
new query is pending. The initial token cell has the same broad `main` root and
unbound empty-marker assumption (lines 232-266). The rate panel also treats only
controls labelled exactly `Next` or `Next page` as pagination and has no exact
busy/total proof.

The terminal can therefore falsely report target counts `0` and completeness
true while a same-name token, DNS record, Tunnel/connector, Access application,
or rule exists in the current exact account. That would permit duplicate token
creation or later routing/security work, so this remains load-bearing HIGH.

#### Required correction

Bind every filter to its unique result region and to a query-specific freshness
signal. Before the next query on a reused filter, require the prior result state
to leave or establish a separately awaited, completed baseline; after filling,
require a state transition or UI-provided query/result generation marker that
proves the zero-result terminal was produced for the exact current value. Prove
zero result rows, no busy state, authoritative result total, and the exact
pagination component's terminal state inside that same result region. Do not
use a fixed delay, race, retry, broad `main` marker, or generic page-wide
`no .* found` text. Apply the same binding to the initial and final token proof
and to the unique rate-rule table.

### IMPORTANT 2 — the execution classification is required to pin its own unknowable commit and hash

Lines 91-103 require the execution-classification artifact to have the fix1
review as parent and to record the full commit, exact byte length, and SHA-256
“for itself.” A file cannot contain the final Git commit ID of the commit that
contains that file: inserting the commit ID changes the file blob and therefore
changes the commit ID. Requiring the file to contain its own SHA-256 has the
same cryptographic fixed-point problem. Repeated amend does not make this an
actionable one-shot condition.

This does not allow an unsafe PASS if interpreted literally; it makes the
required classification impossible to complete, so the replacement cannot
reach eligibility.

#### Required correction

Keep the classification's parent fixed to the review commit and have the
classification file pin only already-existing objects plus its expected path
and source-projection result. Pin the resulting classification commit and its
direct file bytes/hash in a separate, subsequent immutable authority record or
coordinator evidence item whose own identity is not self-referential. Define
that record's exact parent/ancestry rule and require it before browser use.

### IMPORTANT 3 — the V3 token filter is both executed and forbidden, and filter-fill cardinality is absent from terminals

The V3 cell performs `tokenFilter.fill(...)` at line 234, but its prohibition
list says the same cell permits no “form mutation” at lines 327-330. A page-local
search fill is a DOM/form mutation even though it is not a persistent provider
mutation. The contract therefore both requires and forbids the same action.

The one-shot terminals also count get, navigation, readiness, title, control,
name, row, click, and write operations but omit filter-fill attempted/fulfilled
counters. The V3 cell has one fill; the fresh-read cell invokes `filteredZero`
six times and performs a clear plus query fill per call, for twelve fills. A
strict redacted one-shot terminal cannot establish these browser mutation
cardinalities as written.

#### Required correction

State explicitly that no persistent/provider Create/edit mutation is permitted
while the exact page-local search-filter fills are authorized. Add truthful
fill attempted/fulfilled counters incremented immediately before and after each
awaited fill, require V3 `1/1` and fresh-read `12/12`, and include them in the
fixed redacted terminals and PASS tuples. Any rejected or uncertain fill must
stop without later browser action or retry.

## Preserved controls

- The V1/V2 predecessor tuple, sole V3 get, post-write V3 alias/eligibility
  assignment, and consumed/state transitions remain fail-closed.
- The two V3 detach cells remain mutually exclusive, zero-browser-call,
  redacted, and do not claim tab closure.
- Private hrefs, account/zone identifiers, titles, DOM/page content, exception
  messages, screenshots, clipboard bytes, and credentials remain excluded from
  output.
- Inherited PowerShell pins, mandatory final Create/native Copy/native masked
  Paste confirmation, later exact-row deletion confirmation, revocation hold,
  invalid-token proof, owner/proxy/local cleanup, no-retry, no-fallback, and
  no-handoff boundaries remain unchanged.

These controls do not compensate for the false-PASS filter freshness path or
the two actionability contradictions.

## Finding count

- Blocking: 0
- HIGH: 1
- IMPORTANT: 2
- Static verdict: **FAIL**
- `authorizes_live_execution=false`
