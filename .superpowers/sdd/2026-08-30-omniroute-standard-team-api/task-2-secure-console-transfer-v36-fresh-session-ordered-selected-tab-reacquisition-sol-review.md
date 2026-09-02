# OmniRoute V36 ordered selected-tab reacquisition — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only brief commit
`7760a74cf299ab1bafeaa25c3f6dedde73c10d83`, its direct parent V35 incident
commit `1d9adba04a8d432865b2b28e1e4eb06a5945169a`, and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v36-fresh-session-ordered-selected-tab-reacquisition-brief.md`.
The reviewed commit adds exactly that path.

I reviewed the one-cell consumption and completeness contract, current runtime
and API, V35 failed-clean predecessor, complete listing projection, ordered
rank-zero selection under the owner's external selection pin, exact claim
target, account-home signature, counters, output and secret boundary, failure
cleanup, no-retry/no-fallback/no-close requirements, and both mandatory later
confirmations.

I performed no Chrome, browser-binding, provider, clipboard, credential,
network, DNS, routing, process-start, Prox-01, or VM action and did not evaluate
the V36 cell. I did not rerun the supplied passing syntax or fixture suites.
After direct inspection exposed two uncovered trust-boundary doubts, I ran two
standalone pure-JavaScript adversarial projections with no import or browser
binding. Those probes are described below. The only workspace write is this
assigned review artifact.

## Final verdict

**FAIL** — two IMPORTANT findings remain unresolved. V36 must not be executed.

`authorizes_live_execution=false`

## Direct-byte and Git evidence

- Reviewed commit: `7760a74cf299ab1bafeaa25c3f6dedde73c10d83`.
- Direct parent: `1d9adba04a8d432865b2b28e1e4eb06a5945169a`.
- The commit adds exactly the assigned V36 brief path.
- Brief: `22581` bytes, SHA-256
  `D94AE1BC808A245F55F27BED85B7B76D5A6DE59CA3B001E6B28FC1568B26A083`,
  Git blob `605e1017442aa3facec7335b7ef299f751d277af`.
- One JavaScript cell: `13929` normalized UTF-8 LF bytes, SHA-256
  `035DA9B16658C3A8F1CCDCDADE735E53DE3271B9CC065D130CB2C1F214E1050D`.
- The brief is UTF-8 without BOM and LF-only, contains exactly one JavaScript
  fence, and `git diff-tree --check` reports no whitespace error.
- Source inspection found no syntax contradiction. The supplied syntax result
  remains `PASS`, and the supplied fixture result remains
  `V36_PURE_FIXTURES_PASS`; neither suite covers the two adversarial cases below.
- Before review creation, the index was empty and the inherited exact
  twelve-path dirty product baseline was present and unstaged.

## Current runtime, API, and predecessor evidence

The installed reviewed runtime pair reproduces the contract pins:

- `browser-client.mjs`: `149771` bytes, SHA-256
  `A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`;
- `api.json`: `58480` bytes, SHA-256
  `A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.

The API declares `BrowserUser.openTabs():
Promise<Array<BrowserUserTabInfo>>`, ordered by `lastOpened` descending, and
`BrowserUser.claimTab(tab: string | BrowserUserTabInfo): Promise<Tab>`.
`BrowserUserTabInfo` requires string `id` and permits optional string
`lastOpened`, `providerTabId`, `tabGroup`, `title`, and `url`. Browser get,
complete documentation, session naming, navigation, URL, one-argument wait,
locator, and read-only evaluate methods also match the cell.

The pinned implementation is relevant to the exact claim boundary. Its
`claimTab(record)` path calls a helper equivalent to:

```javascript
if (record && typeof record === "object" &&
    typeof record.id === "string") return record.id;
```

Thus an object argument's `id` is read twice before the claim command is sent.
The same API permits the already validated string ID directly.

The direct parent records V35 Call 1 consumed/PASS and Call 2
consumed/failed-clean at the exact-one cardinality gate with eight records,
one fulfilled `openTabs`, zero claim/navigation/page actions, null retained tab,
false eligibility, cleared runtime bindings, and a reset realm. V35 and every
earlier gate remain spent; V36 correctly requires a fresh realm and does not
claim continuity with any prior controller.

## Findings

### V36-001 — IMPORTANT — iterator-controlled traversal does not prove the documented rank-zero array element

`trustedListing` bounds `value.length`, but then traverses the untrusted array
with `for (const item of value)`. It validates record symbols and descriptors,
but it never validates the array's own symbols, iterator, own string names, or
indexed descriptors. Its selected `projected[0]` is therefore the iterator's
first yield, not necessarily the API array's own rank-zero element `value[0]`.

A genuine Array can have length `1`, own index zero pointing to a non-target
record, and an own `Symbol.iterator` that yields a different shape-valid
Cloudflare record. The current projector accepts the yielded record, reports
count `1`, and returns that injected object as `candidate.record`. A standalone
probe using the cell's exact projector produced `ITERATOR_REDIRECT=true` and
proved `candidate.record !== listing[0]`.

This breaks the security premise that the documented `lastOpened` ordering and
owner's exact selection pin identify the sole claim target. The cell can claim
and navigate a record that was never the returned array's rank-zero indexed
record. Validating every yielded record does not restore array-order fidelity.

**Required fix:** project the array structurally without invoking its iterator.
Cache and validate one bounded length descriptor, reject own symbols and
unexpected own string names, require exactly the own numeric indices
`0..length-1` plus the standard length property, and read each index through one
data descriptor. Use the cached descriptor value for index zero and prove the
projected record count equals the cached length. Add a fixture with an own
iterator that yields a different record and require rejection before claim.

### V36-002 — IMPORTANT — passing the original record defeats the cached-ID trust boundary

The record projector correctly obtains each record field through one descriptor
read and caches the validated ID. It then retains the original untrusted object
as `record: item` and passes `candidate.record` to the authority-bearing
`claimTab` call.

The pinned runtime does not use object identity as an opaque capability. As
shown above, it reads the object's `id` twice and sends the second value. A Proxy
can expose a valid enumerable data descriptor with cached ID `A` during
projection, then return `A` for the runtime's type check and different string ID
`B` for its second read. A standalone probe using the cell projector and the
pinned runtime helper produced:

```text
CACHED_ID=cached
RUNTIME_CLAIM_ID=redirected
CLAIM_REREAD_REDIRECT=true
```

The later `adopted.id === candidate.id` check occurs only after the wrong ID has
already been submitted to the sole claim. It can stop navigation, but cannot
undo or reclassify that unauthorized claim as the exact rank-zero target. Realm
disposal releases the controller but does not make the claim exact.

**Required fix:** pass the cached validated primitive string as
`claimTab(candidate.id)`, which the pinned API explicitly supports, and remove
the original record from the trusted projection. Update the object-identity
fixture to require exact cached-ID continuity instead. Add a Proxy fixture whose
descriptor and property-get values disagree and prove there is no untrusted
candidate read after validation and only the cached ID reaches the one-call
claim stub.

## Correctly preserved boundaries

- The declared gate consumes before import, setup, browser attachment,
  documentation, session naming, enumeration, or claim. Its named V35 guard
  declarations and null V36 bindings are checked before the import, while the
  action-time gate separately requires every V35/V36 declaration absent.
- The cell contains one source site each for import, setup, browser get,
  documentation, documentation write, session naming, `openTabs`, `claimTab`,
  fixed navigation, 20000 ms wait, URL read, body evaluation, and final output.
- Every record reached by the current traversal is otherwise subjected to the
  established cross-realm plain-record gate, zero-symbol rule, complete own
  string-name allowlist, enumerable-data-descriptor requirement, mandatory
  cached ID, and bounded nonempty control-free string rules. The first projected
  URL is privately restricted to exact HTTPS `dash.cloudflare.com` origin with
  empty port and credentials. These record-level checks do not close the array
  traversal or post-projection re-read findings.
- Under an exact immutable array and cached-ID claim, the documented descending
  `lastOpened` order plus the immediate owner profile/window/task-tab selection
  pin is a coherent rank-zero selection rule. The action-time requirement to
  revalidate that pin, prove no competing owner, and stop on any drift remains
  essential.
- The post-navigation gate retains exact Cloudflare account-home URL, 32-lower
  hex account segment, HTTPS host/empty port, one same-account/empty-credential
  `/mysw.me` href, positive anchors, zero busy markers, and a plain five-field
  bounded snapshot.
- Ordinary failure nulls retained ownership and clears browser/agent/setup
  bindings. JavaScript-visible final-output failure performs the same cleanup
  and rethrows without a second output. Uncertainty remains terminal and
  requires whole-realm disposal; no tab is closed.
- No retry, candidate loop for selection, second enumeration or claim,
  selected-tab fallback, alternate browser/profile/window, reconnect, new/close
  tab, screenshot, DOM serialization, clipboard, click/press/fill,
  Create/edit/delete, provider mutation, manual integration, credential action,
  process start, VM action, routing change, or verdict relaxation is present.
- Terminal evidence is limited to fixed strings, booleans, bounded counts,
  sanitized error class, and the fixed five-field snapshot. It emits no tab or
  provider ID, tab metadata, URL/path, account/zone ID, href, documentation
  body, raw exception, credential, token, or secret.
- The final Create/native Copy/native masked Paste confirmation and the later
  exact-row deletion confirmation remain separate, mandatory, and unreached.
  V36 does not preapprove either one or any provider-persistent action.

## Static method and counter cardinality

The cell contains exactly:

- dynamic import `1`; setup invocation `1`; `browsers.get("chrome")` `1`;
- documentation read `1`; awaited documentation write `1`;
- `nameSession` `1`; `openTabs` `1`; `claimTab` `1`;
- fixed goto `1`; one-argument wait `1`; URL read `1`; locator evaluation `1`;
- awaited terminal write `1`; terminal-output cleanup catch `1`;
- twelve attempted/fulfilled pairs, each with one increment site per member;
- one `writeAttempted` declaration and one increment;
- browser/tabs list/default/URL/extension, selected/list/get/new/close,
  reconnect, title, screenshot, clipboard, click/press/fill, fetch, provider
  mutation, and alternate claim sites: `0`.

The success path explicitly requires all twelve attempted/fulfilled pairs to be
`1/1` before assigning the fixed PASS result. These cardinalities are correct
but do not prevent either pre-claim target substitution.

## Finding counts and limits

- Critical: `0`.
- HIGH: `0`.
- IMPORTANT: `2` (`V36-001`, `V36-002`).
- Minor: `0`.

No live or consuming action was authorized or performed. V36 remains blocked
pending a corrected committed contract and fresh independent review.

## Final verdict

**FAIL**

Unresolved findings: Critical `0`, HIGH `0`, IMPORTANT `2`, Minor `0`.

`authorizes_live_execution=false`
