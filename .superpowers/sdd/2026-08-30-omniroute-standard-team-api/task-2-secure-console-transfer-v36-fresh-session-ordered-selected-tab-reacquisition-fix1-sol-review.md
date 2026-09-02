# OmniRoute V36 ordered selected-tab reacquisition fix round 1 — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This fix-round review covers only corrected brief commit
`0282071506d3876a96905f7013b63f1b2bd1fb4a`, its direct parent original FAIL
review `36460bd2f7ead55d945a8b86b3d81d88b718f1fe`, and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v36-fresh-session-ordered-selected-tab-reacquisition-brief.md`.
The corrected commit modifies exactly that path.

I independently verified the fixes for `V36-001` and `V36-002`, then rechecked
the inherited current-runtime/API, failed-clean predecessor, one-cell
consumption and completeness, ordered rank-zero selection, account-home
signature, untrusted-data projection, method/counter cardinality, failure and
terminal-output cleanup, no-retry/no-fallback/no-close, secret exclusion,
residue, and mandatory later-confirmation boundaries.

I performed no Chrome, browser-binding, provider, clipboard, credential,
network, DNS, routing, process-start, Prox-01, or VM action and did not evaluate
the V36 cell. The supplied syntax and `V36_FIX1_PURE_FIXTURES_PASS` suites were
not rerun. Direct inspection exposed one uncovered output-boundary doubt, so I
ran one standalone pure-JavaScript Proxy probe with no import or browser
binding. The only workspace write is this assigned review artifact.

## Final verdict

**FAIL** — `V36-001` and `V36-002` are closed, but one new IMPORTANT finding
remains unresolved. V36 must not be executed.

`authorizes_live_execution=false`

## Direct-byte and Git evidence

- Reviewed commit: `0282071506d3876a96905f7013b63f1b2bd1fb4a`.
- Direct parent: `36460bd2f7ead55d945a8b86b3d81d88b718f1fe`.
- The commit modifies exactly the assigned V36 brief path.
- Brief: `24952` bytes, SHA-256
  `44984C6331E7B313CF5029CE0677A3BA2DB46E124F0A3B46544A0184A9CDF34B`,
  Git blob `3b00803bc39324ce5adeb9a255f689ca04668eaa`.
- One JavaScript cell: `15005` normalized UTF-8 LF bytes, SHA-256
  `DC954CEB50C79777E424C18BE2586DB86A6288F71350CBBB6ED134E9B2A78422`.
- The brief is UTF-8 without BOM and LF-only, contains exactly one JavaScript
  fence, and `git diff-tree --check` reports no whitespace error.
- The supplied AsyncFunction syntax result is `PASS`; the supplied focused
  fixture result is `V36_FIX1_PURE_FIXTURES_PASS`. Static source inspection
  agrees with the stated fix coverage but identified the additional raw-length
  output path below.
- Before review creation, the index was empty and the inherited exact
  twelve-path dirty product baseline was present and unstaged.

## Current API and predecessor evidence

The installed reviewed pair still reproduces the brief's pins:

- `browser-client.mjs`: `149771` bytes, SHA-256
  `A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`;
- `api.json`: `58480` bytes, SHA-256
  `A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.

The pinned API declares `openTabs()` returning `BrowserUserTabInfo[]` ordered
by `lastOpened` descending and `claimTab(string | BrowserUserTabInfo)`. Its
current six-field record shape and the browser get, complete documentation,
session naming, navigation, URL, one-argument wait, locator, and read-only
evaluate methods remain consistent with the corrected cell.

The V35 incident remains the exact failed-clean predecessor: Call 1 was
consumed/PASS; Call 2 consumed once, returned eight valid records, and stopped
at cardinality with zero claim/navigation/page actions; retained ownership was
null, eligibility false, bindings cleared, and the realm reset. The corrected
V36 contract still requires a fresh realm and never authorizes reuse or
reinterpretation of V35 or any earlier gate.

## Fix verification

### V36-001 — closed

The corrected `trustedListing` now requires `Array.isArray(value)`, exact
`Array.prototype`, and zero own symbols. It obtains one own `length` data
descriptor, requires a non-enumerable safe integer in `1..1000`, caches that
value, and requires the array's complete own string-name set to be exactly
`length` plus numeric names `0..length-1`.

It then obtains each numeric index through exactly one own descriptor and
requires an enumerable data descriptor before projecting the cached descriptor
value as a record. There is no `for...of`, iterator access, or indexed property
read. Own iterators/symbols, holes, accessors, Array subclasses, and unexpected
names fail before record selection or claim. The projected count must equal the
cached descriptor length, and rank zero comes only from the cached descriptor
for own index `0`. The supplied fixtures exercise these cases, and direct source
inspection confirms the closure.

### V36-002 — closed

The record projector now retains only primitive cached `id` and `url` strings;
it never stores the original record. `claimTab(candidate.id)` receives the
cached validated ID directly, and the source contains no `candidate.record` or
`record: item` path. A Proxy can disagree between descriptor and property-get
results without affecting the claim because the untrusted record is never read
after projection. The supplied disagreement fixture and direct source
inspection agree that only the cached primitive ID reaches the one-call claim.

## Finding

### V36-003 — IMPORTANT — raw untrusted `length` property bypasses projection and enters terminal evidence

Immediately after `openTabs()`, the cell assigns:

```javascript
offeredCount = Array.isArray(offered) ? offered.length : -1;
```

This reads the untrusted array through ordinary property access before
`trustedListing` performs its descriptor-only projection. The projected safe
count is returned as `candidate.count`, but that value is never used. Instead,
the raw `offeredCount` is emitted in the final evidence object on both success
and failure.

A Proxy over an otherwise exact ordinary array can return an arbitrary string,
object, or sensitive metadata from its `get("length")` trap while exposing the
real bounded numeric length through `getOwnPropertyDescriptor("length")`. The
corrected structural projector then passes, the claim can proceed, and terminal
output emits the attacker-controlled raw property result despite the contract's
fixed bounded-count and no-metadata/no-secret promises.

A standalone probe using the corrected projector produced:

```text
LISTING_VALIDATED=true
CACHED_COUNT=1
RAW_OFFERED_COUNT=LEAKED_TAB_METADATA
RAW_LENGTH_READS=1
UNTRUSTED_OUTPUT_LEAK=true
```

This is not repaired by the descriptor checks because the leaking read occurs
outside them. It also makes the emitted evidence cardinality disagree with the
count that was actually validated.

**Required fix:** remove every ordinary `offered.length` read. Leave
`offeredCount` at the fixed sentinel until `trustedListing` succeeds, then set
`offeredCount = candidate.count` from the cached, bounded length descriptor.
On rejected listing output only the fixed sentinel. Add a Proxy fixture whose
`length` get trap throws or returns sensitive text while its length descriptor
is valid; prove the get trap is never invoked and terminal evidence contains
only the cached safe integer or sentinel.

## Correctly preserved inherited boundaries

- The single gate consumes before import, setup, browser attachment,
  documentation, naming, enumeration, or claim. The action-time package still
  requires every V35/V36 declaration absent in a reset fresh realm.
- The cell retains exactly one import, setup, browser get, complete
  documentation read/write, session name, `openTabs`, cached-ID `claimTab`,
  fixed navigation, 20000 ms wait, URL read, body evaluation, and terminal
  write. Every success-side attempted/fulfilled pair is required to be `1/1`.
- Once array fidelity and bounded output are established, the documented
  descending `lastOpened` order plus the immediate owner profile/window/task-tab
  confirmation and no-competing-owner pin is a coherent rank-zero rule. The
  first cached record URL remains privately restricted to exact HTTPS
  `dash.cloudflare.com` origin with empty credentials and port.
- Claimed ownership must match the cached ID and expose the required Tab methods
  before navigation. The page gate retains exact account-home URL, 32-lowercase
  hex account segment, exact HTTPS host/empty port, one same-account
  empty-credential `/mysw.me` href, positive anchors, zero busy markers, and the
  established plain five-field bounded snapshot.
- Ordinary failure nulls retained ownership and clears browser/agent/setup
  bindings. JavaScript-visible final-output failure performs fixed cleanup and
  rethrows without a second output. Any uncertainty remains terminal and
  requires disposal of the fresh realm; no tab is closed.
- There is no retry, second enumeration or claim, candidate-selection loop,
  selected-tab fallback, alternate browser/profile/window, reconnect,
  new/close tab, screenshot, DOM serialization, clipboard, click/press/fill,
  Create/edit/delete, provider mutation, manual integration, credential action,
  process start, VM action, routing change, or verdict relaxation.
- Apart from `V36-003`, terminal fields are fixed strings, booleans, bounded
  counts, sanitized error class, and the five-field snapshot. No tab/provider
  ID, title, URL/path, group, timestamp, account/zone ID, href, documentation
  body, raw exception, credential, token, or secret is otherwise emitted.
- The final Create/native Copy/native masked Paste confirmation and the later
  separate exact-row deletion confirmation remain mandatory and unreached.
  This review authorizes neither one nor any provider-persistent action.

## Static method and counter cardinality

The corrected cell contains exactly:

- dynamic import `1`; setup invocation `1`; browser get `1`;
- documentation read `1`; awaited documentation write `1`;
- session naming `1`; `openTabs` `1`; `claimTab(candidate.id)` `1`;
- fixed goto `1`; one-argument wait `1`; URL read `1`; locator evaluation `1`;
- awaited terminal write `1`; terminal-output cleanup catch `1`;
- twelve attempted/fulfilled pairs, each with one increment site per member;
- one `writeAttempted` declaration and one increment;
- iterator-based listing traversal, retained candidate record, alternate claim,
  selected/list/get/new/close, browser list/default/URL/extension, reconnect,
  title, screenshot, clipboard, click/press/fill, fetch, provider mutation: `0`;
- raw `offered.length` reads: `1`; safe `candidate.count` uses: `0`.

The method/counter cardinality is otherwise exact. `V36-003` prevents the
terminal schema and evidence count from being exact and bounded.

## Finding counts and limits

- Critical: `0`.
- HIGH: `0`.
- IMPORTANT: `1` (`V36-003`).
- Minor: `0`.

No live or consuming action was authorized or performed. V36 remains blocked
pending a corrected committed contract and fresh independent review.

## Final verdict

**FAIL**

Unresolved findings: Critical `0`, HIGH `0`, IMPORTANT `1`, Minor `0`.

`authorizes_live_execution=false`
