# OmniRoute V35 fresh-session open-tabs claim reacquisition fix round 1 — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This fix-round review covers only corrected brief commit
`3504b9e87eacd1c8de6801df7256bd502ce7d37f`, its direct parent original FAIL
review `ebbe03b537d2ef8f373052b0831d5a862d13bf12`, and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v35-fresh-session-open-tabs-claim-reacquisition-brief.md`.
The corrected commit changes exactly that path.

I independently reviewed the fixes for `V35-001` and `V35-002`, then rechecked
the inherited current-runtime/API, failed-clean predecessor, fresh-realm,
two-call consumption, method/counter cardinality, exact ID continuity,
account-home signature, untrusted-data projection, terminal-output cleanup,
transport uncertainty, no-retry/no-close/no-fallback, secret exclusion, residue,
and mandatory later-confirmation boundaries.

I performed no Node, Chrome, browser-binding, provider, clipboard, credential,
network, DNS, routing, process, Prox-01, or VM action and did not evaluate either
V35 cell. The supplied AsyncFunction syntax and focused fixture PASS results
were not rerun because direct source inspection raised no concrete doubt. The
only workspace write is this assigned review artifact.

## Final verdict

**PASS** — `V35-001` and `V35-002` are closed, with zero unresolved Critical,
HIGH, or IMPORTANT findings.

This review does not itself authorize execution. The brief's independent
classification, post-commit coordinator tuple, action-time pins, exact external
profile/window/tab confirmation, fresh-realm proof, and all later confirmation
gates remain mandatory.

`authorizes_live_execution=false`

## Direct-byte and Git evidence

- Reviewed commit: `3504b9e87eacd1c8de6801df7256bd502ce7d37f`.
- Direct parent: `ebbe03b537d2ef8f373052b0831d5a862d13bf12`.
- The commit modifies exactly the assigned corrected V35 brief path.
- Brief: `22491` bytes, SHA-256
  `EF482474FF8A0E13637B92366DD911E157B989488628BAB33E465538D5DE71E9`,
  Git blob `e0aaf1dd69c76f4cb9e6aa66f8f72632a6181b83`.
- Call 1: `5456` normalized UTF-8 LF bytes, SHA-256
  `4F6F4A3F35D6BBCC3EFC5CA6A4B335788D14F38191C88B0D51D63539DA11A2F4`.
- Call 2: `9904` normalized UTF-8 LF bytes, SHA-256
  `6A387C46AA9A226649BA705F503037DCA0813678DDAEAD860060964069C0116F`.
- The brief is UTF-8 without BOM and LF-only, contains exactly two JavaScript
  fences, and `git diff-tree --check` reports no whitespace error.
- The correction is a one-path, 18-insertion/8-deletion change from the FAIL
  review parent. Before review creation, the index was empty and the inherited
  exact twelve-path dirty product baseline remained unstaged.

## Current API and predecessor evidence

The installed reviewed pair still reproduces the brief's current pins:

- `browser-client.mjs`: `149771` bytes, SHA-256
  `A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`;
- `api.json`: `58480` bytes, SHA-256
  `A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.

The pinned API declares `BrowserUser.openTabs():
Promise<Array<BrowserUserTabInfo>>` and `BrowserUser.claimTab(tab: string |
BrowserUserTabInfo): Promise<Tab>`. `BrowserUserTabInfo` requires string `id`
and permits only optional string `lastOpened`, `providerTabId`, `tabGroup`,
`title`, and `url`. The browser connection, complete documentation, fixed
navigation, URL, one-argument wait, locator, and read-only evaluate calls used
by the cells remain valid against the pinned API.

The V34 incident remains the precise failed-clean predecessor: Call 2 was
consumed before navigation when selected-tab ownership could not be proved;
the controller bindings were cleared, the external tab was not closed, and
V34 remains permanently spent. V35 correctly requires a fresh Node realm, and
its action-time gate requires proof that every V34/V35 declaration is absent
before Call 1, so V34 state cannot be reused or reinterpreted.

## Fix verification

### V35-001 — closed

The corrected `trustedCandidate` now requires exactly one array element and
applies the established cross-realm `plainRecord` predicate to that element.
It obtains every own symbol name and rejects any symbol. It obtains every own
string name with `Object.getOwnPropertyNames`, requires mandatory `id`, and
rejects every name outside the exact current six-field API set. This prevents
non-enumerable unexpected fields from hiding outside the allowed-name check.

For each accepted own string name, it performs exactly one
`Object.getOwnPropertyDescriptor(item, key)` read. It rejects absent
descriptors, accessors, and non-enumerable fields before validating the
descriptor's value as a nonempty, bounded, control-free string. The `id` value
is cached from that same descriptor and returned only in a fresh local
`{ id: validatedId }` record. The candidate object is not read again after the
loop, and there is no second ID descriptor lookup.

Thus plain and null-prototype records can pass, while class instances,
non-enumerable extras or allowed fields, accessors, symbols, non-current names,
and zero/multiple candidates fail before `claimTab`. The supplied focused
fixtures confirm those cases and confirm exactly one ID-descriptor read. Direct
source inspection agrees with those results. Candidate metadata and the opaque
ID remain private, and the one claim receives only the cached validated ID.

### V35-002 — closed

The corrected `trustedSnapshot` now invokes the same cross-realm `plainRecord`
predicate before its exact-key, primitive-type, safe-integer, and bounded-count
checks. Plain and null-prototype page records remain admissible while class
instances are rejected before snapshot field access. The trusted projection
still returns only the fixed five fields, so the V34 account-home trust gate
and output boundary are restored without changing the semantic signature.

## Inherited security and one-shot boundaries

- Call 1 consumes before import, setup, browser connection, or documentation.
  It has one pinned import, one setup, one `browsers.get("chrome")`, one complete
  documentation read/write, one fixed terminal write, and no tab/page action.
- Call 2 separately consumes before precondition, discovery, or claim. Exact
  persistent Call-1 PASS is required. It has one `openTabs()` and one
  `claimTab()` source site; zero, multiple, or invalid candidates stop before
  claim or navigation. There is no alternate candidate or re-read fallback.
- The claimed controller must expose the same cached opaque ID and the required
  Tab methods before use. The route gate requires exact HTTPS Cloudflare host,
  32-hex account-home path, and the page signature requires exact host/path,
  one same-origin/empty-credential/empty-port zone href, positive anchors, and
  zero busy markers. Counts remain safe, nonnegative, and bounded.
- Ordinary Call-2 failure clears all owner/controller bindings and never closes
  the externally owned tab. JavaScript-visible final-output rejection performs
  the same fixed cleanup and rethrows without a second output. Unobservable
  transport failure requires disposal of the entire fresh realm.
- There is no browser/profile/window fallback, reconnect, retry, selected-tab
  call, tabs list/get/new/close, screenshot, DOM serialization, clipboard,
  click/press/fill, Create/edit/delete, provider mutation, process start, VM
  action, routing change, credential action, manual integration, or verdict
  relaxation.
- Terminal data remains limited to fixed strings, booleans, bounded counters,
  sanitized error class, and the fixed five-field snapshot. No candidate ID or
  metadata, page URL/path, account identifier, page text, DOM, attribute,
  exception message, credential, token, or secret can leave either cell.
- The owner's exact profile/window/tab confirmation remains required before
  Call 1. The final Create/native Copy/native masked Paste confirmation and the
  separate later exact-row deletion confirmation remain mandatory and are not
  delegated or implied by this PASS.

## Static method and counter cardinality

Call 1 contains exactly:

- dynamic import `1`; setup `1`; browser get `1`; documentation read `1`;
- awaited documentation write `1`; awaited terminal write `1`; terminal cleanup
  catch `1`;
- five attempted/fulfilled pairs, each with one increment site per member;
- browser/tab discovery, selection, claim, navigation, and page actions: `0`.

Call 2 contains exactly:

- `openTabs()` `1`; `claimTab()` `1`; fixed goto `1`; one-argument wait `1`;
- URL read `1`; locator evaluation `1`; awaited terminal write `1`; terminal
  cleanup catch `1`;
- six attempted/fulfilled pairs, each with one increment site per member;
- candidate own-name enumerations: string `1`, symbol `1`; candidate own
  descriptor reads: one loop site and exactly one read per enumerated string
  name, including one cached ID read;
- selected, tabs list/get/new/close, browser list/default/URL/extension,
  reconnect, title, screenshot, clipboard, click/press/fill, fetch, and provider
  actions: `0`.

Each cell retains one `writeAttempted` declaration and one increment. PASS
still requires each applicable attempted/fulfilled pair to be exactly `1/1`,
the complete fixed output, exact booleans and bounded values, and completed
tool status.

## Finding counts and limits

- Critical: `0`.
- HIGH: `0`.
- IMPORTANT: `0`.
- Minor: `0`.

No live or consuming action was authorized or performed. The passing syntax
and fixture evidence was accepted without rerun, and action-time drift checks
remain mandatory.

## Final verdict

**PASS**

Unresolved findings: Critical `0`, HIGH `0`, IMPORTANT `0`, Minor `0`.

`authorizes_live_execution=false`
