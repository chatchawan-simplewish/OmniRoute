# OmniRoute V37 unique task-tab reacquisition — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only brief commit
`9c4c167a4d49975b63a32ef5542ff73a82587042`, its direct parent V36 incident
commit `921326efd05daa44d946811080ca5209d79f503f`, and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v37-fresh-session-unique-task-tab-reacquisition-brief.md`.
The reviewed commit adds exactly that path.

I independently reviewed the one-cell consumption and completeness contract,
current runtime/API, V36 failed-clean predecessor, structural no-iterator list
projection, descriptor-cached record fields, private unique task-route filter,
bounded derived counts, cached-ID claim, account-home signature, output and
secret boundary, failure and terminal-output cleanup, no-retry/no-fallback/
no-close requirements, residue, and both mandatory later confirmations.

I performed no Chrome, browser-binding, provider, clipboard, credential,
network, DNS, routing, process-start, Prox-01, or VM action and did not evaluate
the V37 cell. The supplied AsyncFunction syntax and `V37_PURE_FIXTURES_PASS`
suites were not rerun because direct source inspection raised no concrete
unresolved doubt. The only workspace write is this assigned review artifact.

## Final verdict

**PASS** — zero unresolved Critical, HIGH, IMPORTANT, or Minor findings.

This review does not itself authorize live execution. The required
non-self-referential classification, separate post-commit coordinator tuple,
action-time drift and residue pins, owner profile/window/task-tab confirmation,
fresh-realm proof, and later mandatory confirmations remain unreached and
mandatory.

`authorizes_live_execution=false`

## Direct-byte and Git evidence

- Reviewed commit: `9c4c167a4d49975b63a32ef5542ff73a82587042`.
- Direct parent: `921326efd05daa44d946811080ca5209d79f503f`.
- The commit adds exactly the assigned V37 brief path.
- Brief: `25327` bytes, SHA-256
  `192417C7D078DA47CD5139A9BDEEEB0C43B276145195740AB985ECC60AA9B763`,
  Git blob `c6dffdd6d1351e770fc2fecd4a58b93d0e9deb15`.
- One JavaScript cell: `15826` normalized UTF-8 LF bytes, SHA-256
  `696C9D97AA0B5FB4510561DB0CB8D180643CB5FC43643717291D9D93FC8C8EBE`.
- The brief is UTF-8 without BOM and LF-only, contains exactly one JavaScript
  fence, and `git diff-tree --check` reports no whitespace error.
- The supplied AsyncFunction syntax result is `PASS`; the supplied focused
  fixture result is `V37_PURE_FIXTURES_PASS`. Direct source inspection agrees
  with both results.
- Before review creation, the index was empty and the inherited exact
  twelve-path dirty product baseline was present and unstaged.

## Current API and predecessor evidence

The installed reviewed pair reproduces the contract pins:

- `browser-client.mjs`: `149771` bytes, SHA-256
  `A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`;
- `api.json`: `58480` bytes, SHA-256
  `A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.

The pinned API declares `BrowserUser.openTabs():
Promise<Array<BrowserUserTabInfo>>` and `BrowserUser.claimTab(tab: string |
BrowserUserTabInfo): Promise<Tab>`. `BrowserUserTabInfo` requires string `id`
and permits optional string `lastOpened`, `providerTabId`, `tabGroup`, `title`,
and `url`. Browser get, complete documentation, session naming, navigation,
URL, one-argument wait, locator, and read-only evaluate methods also match the
cell.

The direct parent proves V36 consumed once and failed cleanly after complete
fresh attachment/session naming and one fulfilled `openTabs`. Its trusted
listing/rank-zero predicate returned no candidate, so claim/navigation/wait/
URL/snapshot counts remained zero. Retained ownership was null, eligibility
false, runtime bindings cleared, and the realm reset. The precise private
rejecting predicate remains correctly classified NOT PROVEN. V37 does not rely
on that inference: it retains the structural projection but replaces rank-zero
selection with a complete private unique-route filter. V36 and every earlier
gate remain spent and cannot be retried, continued, or reused.

## Structural listing and untrusted-data boundary

`trustedListing` accepts only a genuine Array with exact `Array.prototype`, no
own symbols, one bounded non-enumerable own length data descriptor, the exact
complete own-name set `length, 0..length-1`, and one enumerable own data
descriptor per numeric index. The cached length must be a safe integer in
`1..1000`, and projected count must equal it.

The projector invokes no array iterator and performs no indexed property read.
Own iterators/symbols, holes, accessors, subclasses, unexpected names, empty
arrays, and arrays above the bound stop before filtering or claim. Each cached
index value must then satisfy the established cross-realm plain-record rule,
zero-symbol rule, exact six-name allowlist, mandatory `id`, and enumerable data
descriptor checks. Every present field is projected from one descriptor read
as a nonempty, bounded, control-free string. Neither the untrusted array nor a
record is re-read after projection.

Only fresh local `{ id, url }` records survive. All emitted list/cardinality
values derive from the cached safe length or local candidate-array length; the
cell contains zero raw `offered.length` reads. Rejected listing output retains
fixed `-1` sentinels. This preserves V36's hardened bounded-output and
no-untrusted-property evidence boundary.

## Unique task-route selection and claim

Every non-null cached URL is privately parsed with `new URL`. A match requires:

- protocol exactly `https:`;
- hostname exactly `dash.cloudflare.com`;
- empty port, username, and password; and
- pathname matching
  `^/[0-9a-f]{32}/mysw\.me(?:/.*)?$`.

That accepts only the exact lower-hex account-scoped `/mysw.me` path, its
trailing-slash form, or descendants. It rejects other origins, credentials,
ports, accounts without 32 lowercase hex characters, sibling zones, prefix
collisions such as `mysw.me.evil`, and non-descendant paths. Query and fragment
data do not affect the pathname match and no parsed URL component is emitted.

The filter processes the complete local projection and derives a bounded local
`targetCount`. It returns a candidate only when that count is exactly one.
Zero or multiple matches set candidate null and stop before the sole claim.
The candidate retains only the descriptor-cached primitive ID. The authority-
bearing call is exactly `claimTab(candidate.id)`; no original record or cached
URL is passed or re-read. Claimed ownership must return that exact cached ID and
the required Tab method shape before navigation. These properties align with
the supplied unique/zero/multiple, iterator, Proxy, and one-call claim fixtures.

## Account-home semantics and cleanup

- After exact unique claim, the cell navigates only that tab to fixed
  `https://dash.cloudflare.com/`, waits once for 20000 ms, and obtains the final
  URL once.
- The final route must be exact HTTPS `dash.cloudflare.com`, a 32-lowercase-hex
  account segment, and `/home` with optional trailing slash.
- The page-local signature uses the same account segment and requires exact
  HTTPS host/empty port, exactly one same-origin empty-credential `/mysw.me`
  href, positive anchor count, and zero busy/progress markers.
- The untrusted page result must pass the established plain five-field snapshot
  projection with exact names, booleans, and safe nonnegative counts bounded by
  `1000000`. No raw page value, route, or account identifier is emitted.
- Ordinary failure nulls retained ownership and clears browser/agent/setup
  bindings. JavaScript-visible final-output failure performs the same cleanup
  and rethrows without a second output. Every uncertainty remains terminal and
  requires whole-realm disposal. No tab is closed.

## One-shot, secret, and confirmation boundaries

- The single gate consumes before import, setup, browser attachment,
  documentation, naming, enumeration, or claim. Action time separately requires
  a reset realm with every V35/V36/V37 declaration absent before consumption.
- Success requires exact method/counter completeness before assigning the fixed
  PASS result. Complete documentation is written once separately and only its
  bounded length/validation status enters the final evidence object.
- There is no retry, second enumeration or claim, alternate candidate,
  rank-zero/selected-tab fallback, alternate browser/profile/window, reconnect,
  new/close tab, screenshot, DOM serialization, clipboard, click/press/fill,
  Create/edit/delete, provider mutation, manual integration, credential action,
  process start, VM action, routing change, or verdict relaxation.
- Terminal evidence is limited to fixed strings, booleans, safe bounded derived
  counts or fixed sentinels, sanitized error class, and the fixed five-field
  snapshot. No tab/provider ID, title, URL/path, group, timestamp, account/zone
  ID, href, raw documentation, raw listing, raw exception, credential, token,
  secret, or untrusted property value can leave the cell.
- The final Create/native Copy/native masked Paste confirmation and the later
  separate exact-row deletion confirmation remain mandatory and unreached.
  This PASS authorizes neither one nor any provider-persistent action.

## Static method and counter cardinality

The cell contains exactly:

- dynamic import `1`; setup invocation `1`; browser get `1`;
- documentation read `1`; awaited documentation write `1`;
- session naming `1`; `openTabs` `1`; `claimTab(candidate.id)` `1`;
- fixed goto `1`; one-argument wait `1`; URL read `1`; locator evaluation `1`;
- awaited terminal write `1`; terminal-output cleanup catch `1`;
- twelve attempted/fulfilled pairs, each with one increment site per member;
- one `writeAttempted` declaration and one increment;
- raw `offered.length`, iterator-based untrusted traversal, retained candidate
  record, alternate claim, selected/list/get/new/close, browser
  list/default/URL/extension, reconnect, title, screenshot, clipboard,
  click/press/fill, fetch, and provider mutation sites: `0`;
- cached listing count use `1`; cached target-count use `1`; private cached-URL
  parse site `1`.

Each success-side attempted/fulfilled pair is explicitly required at `1/1`
before the fixed PASS result. Terminal write completion remains part of the
completed-tool-status requirement, with one visible-rejection cleanup path.

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
