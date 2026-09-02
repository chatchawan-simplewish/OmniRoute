# OmniRoute V36 ordered selected-tab reacquisition fix round 2 — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This fix-round review covers only corrected brief commit
`8905b23e81df28eb283614d96cba0ba1fa5c9957`, its direct parent fix-round-1
FAIL review `a0f15ddde6432d5c586bf64902a75ed6eb2d7b78`, and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v36-fresh-session-ordered-selected-tab-reacquisition-brief.md`.
The corrected commit modifies exactly that path.

I independently verified the closure of `V36-003`, reconfirmed `V36-001` and
`V36-002`, and rechecked the inherited current-runtime/API, failed-clean
predecessor, one-cell consumption and completeness, ordered rank-zero
selection, account-home signature, untrusted-data projection, method/counter
cardinality, failure and terminal-output cleanup, no-retry/no-fallback/no-close,
secret exclusion, residue, and mandatory later-confirmation boundaries.

I performed no Chrome, browser-binding, provider, clipboard, credential,
network, DNS, routing, process-start, Prox-01, or VM action and did not evaluate
the V36 cell. The supplied AsyncFunction syntax and
`V36_FIX2_PURE_FIXTURES_PASS` suites were not rerun because direct source
inspection raised no concrete unresolved doubt. The only workspace write is
this assigned review artifact.

## Final verdict

**PASS** — `V36-001`, `V36-002`, and `V36-003` are closed, with zero unresolved
Critical, HIGH, IMPORTANT, or Minor findings.

This review does not itself authorize live execution. The required
non-self-referential classification, separate post-commit coordinator tuple,
action-time drift and residue pins, owner selection confirmation, fresh-realm
proof, and later mandatory confirmations remain unreached and mandatory.

`authorizes_live_execution=false`

## Direct-byte and Git evidence

- Reviewed commit: `8905b23e81df28eb283614d96cba0ba1fa5c9957`.
- Direct parent: `a0f15ddde6432d5c586bf64902a75ed6eb2d7b78`.
- The commit modifies exactly the assigned V36 brief path.
- Brief: `25410` bytes, SHA-256
  `73F88B050EEA1604ECC771B0CB9866C8B2FE5844D70D04597775D842A675EFDE`,
  Git blob `cad341e6d719b8004bf0d196c3487c9da7a1a165`.
- One JavaScript cell: `15000` normalized UTF-8 LF bytes, SHA-256
  `5395EAC07AEC15AB63BC78AA9DB1E89AE909DC00EE74991F6CEDF0BCB32834B0`.
- The brief is UTF-8 without BOM and LF-only, contains exactly one JavaScript
  fence, and `git diff-tree --check` reports no whitespace error.
- The supplied AsyncFunction syntax result is `PASS`; the supplied focused
  fixture result is `V36_FIX2_PURE_FIXTURES_PASS`. Direct source inspection
  agrees with both results.
- Before review creation, the index was empty and the inherited exact
  twelve-path dirty product baseline was present and unstaged.

## Current API and predecessor evidence

The installed reviewed pair still reproduces the brief's pins:

- `browser-client.mjs`: `149771` bytes, SHA-256
  `A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`;
- `api.json`: `58480` bytes, SHA-256
  `A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.

The pinned API continues to declare `openTabs()` returning
`BrowserUserTabInfo[]` ordered by `lastOpened` descending and
`claimTab(string | BrowserUserTabInfo)`. Its current six-field record shape and
the browser get, complete documentation, session naming, navigation, URL,
one-argument wait, locator, and read-only evaluate methods remain consistent
with the corrected cell.

The V35 incident remains the exact failed-clean predecessor: Call 1 was
consumed/PASS; Call 2 consumed once, returned eight valid records, and stopped
at cardinality with zero claim/navigation/page actions; retained ownership was
null, eligibility false, bindings cleared, and the realm reset. V35 and every
earlier gate remain spent. V36 still requires a fresh realm and authorizes no
reuse, continuation, or reinterpretation of predecessor state.

## Fix verification

### V36-003 — closed

The corrected cell no longer reads `offered.length` through ordinary property
access. `offeredCount` begins at the fixed numeric sentinel `-1` and remains
that sentinel when `trustedListing` rejects the value. Only after the projector
returns a non-null local candidate does the cell assign:

```javascript
offeredCount = listingValidated ? candidate.count : -1;
```

`candidate.count` comes exclusively from the projector's one cached own
`length` data descriptor, already required to be a safe integer in `1..1000`.
The candidate is a fresh local record, so this assignment performs no read from
the untrusted listing. Static inspection found zero `offered.length` sites and
exactly one `candidate.count` site. The supplied Proxy-array fixture proves zero
property-get reads and a fixed bounded evidence count. Terminal output can now
contain only the validated bounded count or `-1`, closing both the no-secret and
evidence-cardinality defects.

### V36-001 — remains closed

`trustedListing` still requires a genuine Array with exact `Array.prototype`,
zero own symbols, one bounded non-enumerable own length data descriptor, the
exact complete own numeric-name set, and one enumerable own data descriptor for
every index. It invokes no iterator and performs no indexed property read.
Own/custom iterators, symbols, holes, accessors, subclasses, unexpected names,
empty arrays, and arrays over the bound stop before candidate selection or
claim. The rank-zero value is the cached descriptor value for own index `0`,
and projected count must equal the cached length.

### V36-002 — remains closed

Each projected record retains only cached primitive `id` and `url` values after
the exact plain-record, own-name, zero-symbol, enumerable-data-descriptor, and
bounded control-free string checks. No original record is retained or re-read.
The sole authority-bearing call remains `claimTab(candidate.id)`, and the
claimed Tab ID must equal that same cached primitive before navigation. The
source contains no `candidate.record`, `record: item`, or post-projection
untrusted record read. The supplied disagreeing-Proxy fixture remains aligned
with the corrected source.

## Inherited security and one-shot boundaries

- The single gate consumes before import, setup, browser attachment,
  documentation, naming, enumeration, or claim. Action time separately requires
  a reset realm with every V35/V36 declaration absent before consumption.
- Exact persistent method cardinality is one import, setup, browser get,
  complete documentation read/write, session name, `openTabs`, cached-ID
  `claimTab`, fixed navigation, 20000 ms wait, URL read, body evaluation, and
  terminal write. Every success-side attempted/fulfilled pair must be `1/1`.
- The documented descending `lastOpened` order, exact structural rank-zero
  projection, immediate owner profile/window/task-tab confirmation, and
  no-competing-owner pin together establish the intended sole candidate. Its
  private cached URL must be exact HTTPS `dash.cloudflare.com` origin with empty
  credentials and port before claim.
- Claimed ownership must match the cached ID and expose the required Tab methods
  before navigation. The semantic gate retains exact Cloudflare account-home
  URL, 32-lowercase-hex account segment, exact HTTPS host/empty port, one
  same-account empty-credential `/mysw.me` href, positive anchors, zero busy
  markers, and the established plain five-field bounded snapshot.
- Ordinary failure nulls retained ownership and clears browser/agent/setup
  bindings. JavaScript-visible final-output failure performs fixed cleanup and
  rethrows without a second output. Every uncertainty remains terminal and
  requires disposal of the fresh realm; no tab is closed.
- There is no retry, second enumeration or claim, candidate-selection loop,
  selected-tab fallback, alternate browser/profile/window, reconnect,
  new/close tab, screenshot, DOM serialization, clipboard, click/press/fill,
  Create/edit/delete, provider mutation, manual integration, credential action,
  process start, VM action, routing change, or verdict relaxation.
- Terminal evidence is now limited to fixed strings, booleans, safe bounded
  counts or fixed sentinels, sanitized error class, and the fixed five-field
  snapshot. No tab/provider ID, title, URL/path, group, timestamp, account/zone
  ID, href, documentation body, raw exception, credential, token, secret, raw
  listing, or untrusted property value can leave the cell.
- The final Create/native Copy/native masked Paste confirmation and the later
  separate exact-row deletion confirmation remain mandatory and unreached.
  This PASS authorizes neither confirmation nor any provider-persistent action.

## Static method and counter cardinality

The corrected cell contains exactly:

- dynamic import `1`; setup invocation `1`; browser get `1`;
- documentation read `1`; awaited documentation write `1`;
- session naming `1`; `openTabs` `1`; `claimTab(candidate.id)` `1`;
- fixed goto `1`; one-argument wait `1`; URL read `1`; locator evaluation `1`;
- awaited terminal write `1`; terminal-output cleanup catch `1`;
- twelve attempted/fulfilled pairs, each with one increment site per member;
- one `writeAttempted` declaration and one increment;
- raw `offered.length`, iterator-based listing traversal, retained candidate
  record, alternate claim, selected/list/get/new/close, browser
  list/default/URL/extension, reconnect, title, screenshot, clipboard,
  click/press/fill, fetch, and provider mutation sites: `0`;
- safe `candidate.count` uses: `1`.

Each success-side pair is explicitly checked at `1/1` before the fixed PASS
result. Final terminal write completion remains required by completed tool
status, with its one visible-rejection cleanup path.

## Finding counts and limits

- Critical: `0`.
- HIGH: `0`.
- IMPORTANT: `0`.
- Minor: `0`.

No live or consuming action was authorized or performed. The passing syntax and
fixture evidence was accepted without rerun, and all classification/action-time
pins remain mandatory.

## Final verdict

**PASS**

Unresolved findings: Critical `0`, HIGH `0`, IMPORTANT `0`, Minor `0`.

`authorizes_live_execution=false`
