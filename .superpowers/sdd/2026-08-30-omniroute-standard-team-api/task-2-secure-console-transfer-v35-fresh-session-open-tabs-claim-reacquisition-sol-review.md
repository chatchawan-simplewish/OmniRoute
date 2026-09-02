# OmniRoute V35 fresh-session open-tabs claim reacquisition — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only commit
`5fb89012252164d903487c0785aecf9240c47178` and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v35-fresh-session-open-tabs-claim-reacquisition-brief.md`.
Its direct parent is the V34 selected-tab ownership-shape incident commit
`0d6de7be7aea903bff24c82fb81db5ef25239f30`.

I independently reviewed both committed cells, current runtime/API pins, exact
V34 failed-clean predecessor, fresh-realm and two-call consumption, the sole
open-tabs/claim path, candidate trust projection and metadata exclusion, exact
ID continuity, account-home signature, final-output cleanup and transport
uncertainty, no-retry/no-close boundaries, counters, secret exclusions, and
both mandatory later confirmations.

I performed no Node, Chrome, browser-binding, provider, clipboard, credential,
network, DNS, routing, process, Prox-01, or VM action and did not evaluate either
V35 cell. The supplied AsyncFunction syntax PASS pins were not rerun. The only
workspace write is this assigned review artifact.

## Final verdict

**FAIL** — two IMPORTANT findings remain unresolved. V35 must not be executed.

`authorizes_live_execution=false`

## Direct-byte and Git evidence

- Reviewed commit: `5fb89012252164d903487c0785aecf9240c47178`.
- Direct parent: `0d6de7be7aea903bff24c82fb81db5ef25239f30`.
- The reviewed commit adds exactly the assigned V35 brief path.
- Brief: `21914` bytes, SHA-256
  `21378EED6E554E0E1217B2343D42A0B5FC3869425EA49E883A47FB5C865A2DB8`,
  Git blob `98bcb09632e7f342ac2b16a7e176f58866b80f00`.
- Call 1: `5456` normalized UTF-8 LF bytes, SHA-256
  `4F6F4A3F35D6BBCC3EFC5CA6A4B335788D14F38191C88B0D51D63539DA11A2F4`.
- Call 2: `9604` normalized UTF-8 LF bytes, SHA-256
  `194BC0D9EEB54F949C70D3F7756D6E613AAB7B5ACA27A43E53B2E5A4777740A5`.
- The brief is UTF-8 without BOM and LF-only, contains exactly two JavaScript
  fences, and `git diff-tree --check` reports no whitespace error.
- Source-level static inspection found no syntax contradiction. No Node parse
  or execution command was run.
- Before review creation, the index held zero paths and the inherited exact
  twelve-path dirty product baseline was present and unstaged.

## Predecessor and current API evidence

The parent incident proves V34 Call 1 passed exactly and Call 2 consumed once,
failed before navigation because the selected value did not expose the reviewed
controllable string-ID shape, emitted only sanitized fixed evidence, cleared
its controller/owner bindings, and left the external selected tab untouched.
V34 is permanently spent and V35 correctly requires a fresh Node realm rather
than reusing any V34 binding.

The current installed files reproduce:

- `browser-client.mjs`: `149771` bytes, SHA-256
  `A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`;
- `api.json`: `58480` bytes, SHA-256
  `A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.

The exact API declares `BrowserUser.openTabs():
Promise<Array<BrowserUserTabInfo>>` and `BrowserUser.claimTab(tab: string |
BrowserUserTabInfo): Promise<Tab>`. `BrowserUserTabInfo` requires string `id`
and permits optional string `lastOpened`, `providerTabId`, `tabGroup`, `title`,
and `url`. The navigation, URL, one-argument wait, locator, and read-only
evaluate method shapes used downstream also match the pinned API.

## Findings

### V35-001 — IMPORTANT — offered candidate is not an exact stable plain-record projection

`trustedCandidate` at lines 237-261 checks only that the sole array item is a
non-null object with no symbol properties. It then uses `Object.keys`, validates
the descriptors for those enumerable names, and re-reads the `id` descriptor
after the validation loop.

This does not establish the claimed exact current `BrowserUserTabInfo` shape:

- an Array instance or arbitrary class instance with an enumerable `id` can
  pass because no cross-realm plain-record rule is enforced;
- unexpected non-enumerable own string properties are invisible to
  `Object.keys` and therefore bypass the allowed-field check; and
- the `id` descriptor is obtained a second time after validation, so a Proxy
  or unstable reflection result can supply a different unvalidated value to
  the fresh `{ id }` projection that is then passed to the authority-bearing
  `claimTab` call.

The downstream equality check proves continuity only with whatever second ID
was projected; it does not repair the missing trust-boundary proof that this
was the one value validated from an exact current offered record.

**Required fix:** require the sole candidate to satisfy the established
cross-realm plain-record rule, enumerate all own string names with
`Object.getOwnPropertyNames`, reject symbols/accessors/non-current names and
non-enumerable record fields, and cache the validated `id` from the single
descriptor read used in the validation loop. Return only that cached string in
a fresh local record; never re-read the untrusted candidate before `claimTab`.

### V35-002 — IMPORTANT — account-home snapshot drops V34's plain-record trust gate

V35 says it applies the unchanged V34 private account-home semantic check, but
its `trustedSnapshot` at lines 263-287 accepts every non-null, non-Array object.
The corrected V34 predecessor explicitly required `plainRecord(value)` before
exact-key/type/range projection. That prototype gate is absent here.

Consequently a class instance or other non-plain object can reach repeated
direct property reads and be projected as trusted page evidence. This is a
semantic and trust-boundary regression from V34, not an unchanged copy of the
reviewed signature. Exact enumerable key names and primitive checks do not
substitute for the missing cross-realm record-shape rule.

**Required fix:** restore the exact V34 `plainRecord` gate before any snapshot
key/value access, or replace it with an equally strict one-read descriptor
projector. Preserve the exact five output fields and all existing boolean and
integer bounds.

## Correctly preserved boundaries

- Call 1 consumes before import, setup, connection, or documentation. It uses
  the exact pinned module once, attaches to `chrome` once, writes complete
  documentation once, and retains the controller only after exact completeness.
- Call 2 separately consumes before precondition, list, or claim. It contains
  exactly one `openTabs()` and one `claimTab()` source site. Non-array, zero,
  multiple, or rejected candidate shapes stop before claim or navigation.
- Candidate metadata is never included in terminal output. Only candidate
  count and validation status can leave the cell. The offered ID remains local,
  and a successful claim must return a controllable Tab with the exact projected
  ID before navigation.
- The account-home route and page-local semantic logic retain exact HTTPS host,
  32-hex account-home path, one exact same-origin/empty-credential zone href,
  positive anchors, zero busy markers, and bounded count projection. No title
  or raw page value is emitted.
- Ordinary failure clears the owner/controller bindings. JavaScript-visible
  terminal-output rejection performs fixed cleanup and rethrows without a
  second output. Unobservable transport uncertainty honestly requires disposal
  of the whole fresh realm.
- No tab is created or closed. There is no selected/list/get/new alternate,
  reconnect, fallback, retry, screenshot, DOM serialization, clipboard,
  click/press/fill, Create/edit/delete, provider mutation, process start, VM
  action, routing change, credential action, or verdict relaxation.
- Terminal data is limited to fixed strings, booleans, bounded counts, the
  five-field snapshot, and sanitized error class. It contains no candidate ID,
  provider ID, URL, title, group, timestamp, account, path, page text, DOM,
  attribute, exception message, credential, token, or secret.
- The final Create/native Copy/native masked Paste confirmation and the later
  separate exact-row deletion confirmation remain explicit, mandatory, and
  unreached.

## Static method and counter cardinality

Call 1 contains exactly:

- dynamic import `1`; setup `1`; browser get `1`; documentation read `1`;
- awaited documentation write `1`; awaited terminal write `1`; terminal cleanup
  catch `1`;
- five attempted/fulfilled pairs, each with one increment site per member;
- browser/tab discovery, claim, selection, navigation, and provider actions:
  `0`.

Call 2 contains exactly:

- `openTabs()` `1`; `claimTab()` `1`; fixed goto `1`; one-argument wait `1`;
- URL read `1`; locator evaluation `1`; awaited terminal write `1`; terminal
  cleanup catch `1`;
- six attempted/fulfilled pairs, each with one increment site per member;
- selected, tabs list/get/new/close, browser list/default/URL/extension,
  reconnect, title, screenshot, clipboard, click/press/fill, fetch, and provider
  actions: `0`.

Each cell has one `writeAttempted` declaration and one increment. These
cardinalities are correct but do not close `V35-001` or `V35-002`.

## Finding counts and limits

- Critical: `0`.
- HIGH: `0`.
- IMPORTANT: `2` (`V35-001`, `V35-002`).
- Minor: `0`.

## Final verdict

**FAIL**

Unresolved findings: Critical `0`, HIGH `0`, IMPORTANT `2`, Minor `0`.

`authorizes_live_execution=false`
