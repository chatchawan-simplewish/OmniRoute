# OmniRoute V33 zone-route outer-locator signature diagnostic — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only commit
`7ccc364e0beb2d1b78dccc2a65733722b364abfd` and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-zone-route-v33-outer-locator-signature-brief.md`.
Its sole direct parent is the V32 consumed failed-clean incident commit
`7563e19717d5bf6a8b7ba09f4290167cdf554e53`.

I independently reviewed the direct committed bytes, V32 predecessor evidence,
one-shot consumption, exact method and counter cardinality, route and locator
semantics, untrusted page-returned data handling, fixed output, exact-handle
cleanup, no-residue/no-retry rules, secret exclusions, and the mandatory later
confirmation boundaries.

I performed no Node, Chrome, browser-binding, provider, clipboard, credential,
network, DNS, routing, process, Prox-01, or VM action and did not evaluate the
V33 cell. The only workspace write is this assigned review artifact.

## Final verdict

**FAIL** — one HIGH and two IMPORTANT findings remain unresolved. V33 must not
be executed.

`authorizes_live_execution=false`

## Direct-byte and Git evidence

- Reviewed commit: `7ccc364e0beb2d1b78dccc2a65733722b364abfd`.
- Direct parent: `7563e19717d5bf6a8b7ba09f4290167cdf554e53`.
- The reviewed commit adds exactly the assigned V33 brief path.
- Brief: `23862` bytes, SHA-256
  `CD9C383BBD06FD81FC4C150D1C38DA057FF1E5DC726DF26626DA3094EE5EB5FD`,
  Git blob `1e8a8e8dfbf486542b4d2ca4d1b66c402ba862ec`.
- Normalized executable: `19704` UTF-8 LF bytes, SHA-256
  `09596785000C6F0BBD01269D46420452BAAA7FA3FAE98849A7E728C83955C500`.
- The brief is UTF-8 without BOM and LF-only. The exact executable bytes match
  the supplied pin. Source-level static inspection found no syntax
  contradiction; no Node parse or execution command was run.
- Before review creation, the index held zero paths and the inherited exact
  twelve-path dirty product baseline was present and unstaged.
- `git diff-tree --check` reports one trailing blank line at EOF in the new
  brief; this is recorded as Minor finding `V33-004` below.

## Exact predecessor and inherited boundaries

The parent incident proves that V32 was consumed exactly once, opened and
closed one exact tab, validated and navigated the unique private same-account
`mysw.me` href, then rejected at its first post-navigation evaluator. Its
terminal state is `V32_DIAGNOSTIC_FAILED_CLEAN`, close is `1 / 1`, residue is
converged, and no handle remains. It proves no API-token/profile/manage-account
signature and permanently forbids V32 retry or reinterpretation.

V33 preserves the predecessor tuple and consumes its fresh gate before its
first precondition. It does not reset or continue V32. The sole new-tab handle
is chained into the durable and local bindings before later awaits. Exact close
fulfillment is required to clear the durable handle; close rejection retains
it, forces non-PASS, and reports unconverged residue. Rejected or malformed
creation cannot be classified clean after a creation attempt.

The code contains no click, press, fill, Create, Copy, Paste, fetch, clipboard,
provider mutation, tab listing/discovery/reacquisition, retry, fallback, manual
integration, or verdict relaxation. Terminal output contains only fixed
strings, booleans, bounded counters, validated count projections, and a
sanitized error class. It emits no raw href, URL, path, account identifier,
page text, DOM, attribute, screenshot, credential, token, secret, or exception
message. The later final Create/native Copy/native masked Paste confirmation
and separate exact-row deletion confirmation remain unreached and mandatory.

## Findings

### V33-001 — HIGH — locator counts are attributed to a stale pre-count route

Lines 343-357 read and validate `settledZoneUrl` once. Lines 359-433 then make
eleven separately awaited locator-count calls. Lines 435-472 nevertheless
derive `hostExact`, `zonePathExact`, `zonePathPrefix`, and `accountHomePath`
from the old `settledZoneParsed` object rather than from the page after those
calls.

A navigation or redirect after line 357 can therefore move the tab before or
during the outer probes. V33 can collect some or all counts from another route
and still report a clean expected-zone route because the final route booleans
are computed from stale data. The final busy count does not prove route
continuity. This breaks the claimed evidence boundary that a clean PASS proves
the fixed route/locator signature counts.

The initial settled check is also weaker than the observed-href check: it does
not require empty port, username, or password. Exact-origin continuity is not
established even at the initial read.

**Required fix:** bracket the outer-probe sequence with explicit attempted /
fulfilled URL reads, validate exact `https://dash.cloudflare.com` origin,
empty username/password, and the original account/zone prefix at both ends,
and require route continuity. Derive the terminal post-route booleans from the
fresh post-probe URL, not the stale pre-probe object. Preserve the no-URL-output
rule and fail closed on any mismatch. If the design intends to prove one
coherent page state rather than only route-bounded sequential counts, add a
bounded stability rule that actually establishes that stronger claim.

### V33-002 — IMPORTANT — href selectors do not reproduce the claimed validated path shapes

The V32 evaluator parsed hrefs and counted only same-host URL pathnames against
bounded API-token patterns. V33 replaces those semantics with raw CSS attribute
tests:

- line 382 counts any href containing `/api-tokens`, including an external URL
  or an unrelated path/query value;
- lines 387-389 count only two literal relative profile href forms and miss an
  equivalent absolute same-host form; and
- lines 394-396 accept any relative account-prefixed href containing the
  substring later, including an unrelated route whose query contains
  `/api-tokens`.

These three values no longer have one consistent same-origin pathname meaning.
A positive or unique count can therefore be a false API-token route signature,
yet the evidence interpretation says such a signature may support a later
exact-locator navigation successor.

**Required fix:** either restore one explicitly same-origin, pathname-bounded
meaning for each advertised href count without emitting the href/account, or
rename and document the values as raw attribute-candidate counts and forbid
using them as validated route evidence. Any later navigation locator must be
separately bound to an exact validated destination; count coincidence is not
destination proof.

### V33-003 — IMPORTANT — unsafe count values do not stop at their probe boundary

Each outer `.count()` result is stored and the next locator call proceeds
immediately. The values are not type/range checked until the aggregate
`trustedRecord` call at lines 435-463. If, for example, `bodyCount` or an early
href count returns a non-safe, negative, or over-bound value, V33 continues the
remaining probes and eventually reports `postStage=PROJECT_RESULT` rather than
the originating count stage.

This contradicts both design claims that each outer count has an exact boundary
and that any unsafe count stops the lane. The aggregate projection prevents an
unsafe value from reaching terminal output, but it does not provide immediate
fail-closed control flow or accurate stage evidence.

**Required fix:** validate every returned count as a safe integer in
`0..1000000` immediately after its fulfillment counter and before advancing
`postStage` or starting the next probe. Keep the originating fixed stage on
failure, then retain the final exact-key aggregate projection as defense in
depth.

### V33-004 — Minor — committed brief has a blank line at EOF

`git diff-tree --check` reports `new blank line at EOF` for line 577.

**Required fix:** remove the extra blank line when repinning the corrected
brief.

## Static method and counter cardinality

Static source sites reproduce as:

- V33 persistent declarations: `3`;
- `tabs.new`: `1`; `goto`: `2`; URL reads: `2`;
- bounded network-idle waits: `2`; page evaluator: `1`;
- outer locator counts: `11`; exact-handle close: `1`; terminal write: `1`;
- click / press / fill: `0 / 0 / 0`;
- tab list / get / selected discovery: `0 / 0 / 0`;
- fetch / clipboard: `0 / 0`.

All twenty-one declared attempted/fulfilled pairs have exactly one increment
site for each member: new, home navigation/wait/URL, pre-snapshot, zone
navigation/wait/URL, aggregate post-snapshot, eleven individual counts, and
close. `writeAttempted` has one declaration and one increment. These static
cardinalities are structurally correct, but they do not close findings
`V33-001` through `V33-003`.

## Finding counts and limits

- Critical: `0`.
- HIGH: `1` (`V33-001`).
- IMPORTANT: `2` (`V33-002`, `V33-003`).
- Minor: `1` (`V33-004`).

## Final verdict

**FAIL**

Unresolved findings: Critical `0`, HIGH `1`, IMPORTANT `2`, Minor `1`.

`authorizes_live_execution=false`
