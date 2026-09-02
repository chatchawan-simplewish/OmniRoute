# OmniRoute V38 listing-shape diagnostic — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only brief commit
`5dbc5bb6cae06261aa73f17abd3c524445216d86`, its direct parent and fixed V37
incident commit `2389694b7043adcb6ac31a74376f695ad8800d7f`, exact brief path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v38-fresh-session-listing-shape-diagnostic-brief.md`,
the incident path named by that brief, and the pinned runtime/docs files needed
to verify the declared API boundary.

I independently reviewed committed bytes and extraction, JavaScript syntax,
fresh-realm and one-shot semantics, runtime/API validity, complete documentation,
fixed-schema privacy, diagnostic predicate fidelity, method/counter cardinality,
failure and terminal-output cleanup, no-retry/no-claim/no-navigation boundaries,
secret exclusion, action-time pins, and both mandatory later confirmations.

I performed no Chrome, browser-binding, provider, clipboard, credential,
network, DNS, routing, process-start, Prox-01, or VM action and did not evaluate
the V38 cell. One offline `AsyncFunction` construction verified syntax without
execution. One standalone pure-JavaScript descriptor probe confirmed an
identified boolean mismatch without importing the browser runtime. I also
assessed the coordinator-supplied inert foreign-realm Array evidence; it was not
a Chrome or live-listing observation. The only workspace write is this assigned
review artifact.

## Final verdict

**FAIL** — three IMPORTANT findings remain unresolved. V38 must not be executed.

`authorizes_live_execution=false`

## Direct-byte, syntax, and Git evidence

- Reviewed commit: `5dbc5bb6cae06261aa73f17abd3c524445216d86`.
- Direct parent: `2389694b7043adcb6ac31a74376f695ad8800d7f`.
- The commit adds exactly the assigned V38 brief path.
- Brief: `21626` bytes, SHA-256
  `D4267CCB30E1A368E023820AAB5FDEA0B0008AC5C8D942829A6BE6B1948680C9`,
  Git blob `42ca61d28b2661d54da7226b6fd9823080b52621`.
- Exactly one JavaScript cell was extracted at `14894` normalized UTF-8 LF
  bytes, SHA-256
  `F4B95AF411FD16B189916F67BE6AB9DCD33E722B03AD177B3B5E26ACA591B71A`.
- Constructing an `AsyncFunction` from those exact normalized bytes without
  invoking it returned `ASYNC_FUNCTION_SYNTAX=PASS`.
- The brief is UTF-8 without BOM and LF-only, contains exactly one JavaScript
  fence, and `git diff-tree --check` reports no whitespace error.
- Before review creation, the index was empty and the inherited exact
  twelve-path dirty product baseline was present and unstaged.

## Predecessor and intended diagnostic boundary

The direct-parent incident proves V37 consumed once and failed cleanly after
complete fresh attachment, documentation, session naming, and one fulfilled
`openTabs`. Structural listing validation returned null before producing either
a bounded offered count or target-candidate count. Claim, navigation, wait, URL,
and snapshot counts remained zero; retained ownership was null, eligibility
false, runtime bindings cleared, and the realm reset.

The incident correctly classifies the exact rejecting structural subpredicate
as NOT PROVEN. It permits no inference from the private listing and requires a
new no-claim/no-navigation fixed-schema diagnostic. V38's intended scope matches
that requirement: one fresh attachment and enumeration, fixed predicate
booleans and one bounded count only, then permanent ineligibility and realm
disposal. V37 and every earlier gate remain spent and cannot be retried,
continued, relaxed, or reused.

## Current runtime and API evidence

The installed reviewed pair reproduces the brief's pins:

- `browser-client.mjs`: `149771` bytes, SHA-256
  `A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`;
- `api.json`: `58480` bytes, SHA-256
  `A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.

The API supports browser get, complete documentation, session naming, browser
user access, and `openTabs()` returning the declared six-field
`BrowserUserTabInfo[]`. The pinned module's actual export tail is equivalent to:

```javascript
export { setupBrowserRuntime };
```

Static search found zero `BROWSER_CLIENT_ID` occurrences in the pinned module.
That mismatch is terminal for the current V38 source, as described below.

## Foreign-realm evidence boundary

The coordinator supplied an inert, non-browser observation from a freshly reset
Node realm: an Array constructed in `vm.runInNewContext` produced
`Array.isArray=true` and `Object.getPrototypeOf(value) === Array.prototype`
false. The realm was reset immediately afterward.

This demonstrates the general cross-realm behavior but does **not** prove that
the live `openTabs()` listing is foreign-realm. V38's two fixed booleans are a
safe way to resolve that exact uncertainty if the diagnostic reaches the
listing: `Array.isArray` and `Object.getPrototypeOf` reveal only shape booleans,
invoke no iterator or indexed/property-value read, and emit no prototype or
metadata. A true/false result would distinguish a foreign-realm Array from a
current-realm exact-Array-prototype value without relaxing V37 retroactively.

## Findings

### V38-001 — IMPORTANT — nonexistent module export makes the diagnostic unreachable

After the one permitted import, V38 requires:

```javascript
moduleShape =
  typeof imported.setupBrowserRuntime === "function" &&
  imported.BROWSER_CLIENT_ID === "chrome";
```

The exact pinned module exports `setupBrowserRuntime` only. It contains no
`BROWSER_CLIENT_ID` declaration or export, so the second conjunct is always
false. The cell necessarily throws `BrowserModuleShapeError` immediately after
the import, before setup, browser get, documentation, session naming, or
`openTabs`.

V38 would therefore consume permanently while capturing no listing-shape
diagnostic at all. Its final fixed object would be a sanitized failure, but that
does not satisfy the sole purpose of this one-shot gate and cannot be retried.

**Required fix:** use the established pinned-module shape check: require the
module namespace to be non-null and `setupBrowserRuntime` to be a function,
without inventing an absent identity export. Call the reviewed runtime setup
without relying on the unrecognized `transport: "cdp"` option, or separately
prove and document an exact current setup option before using it. Add a static
fixture that imports or inspects only the pinned module export names without
starting the runtime and proves the corrected module predicate true.

### V38-002 — IMPORTANT — descriptor booleans do not independently reproduce V37 predicates

For each record field, V38 obtains the own descriptor safely. When the
descriptor is non-data, however, it sets the data/value booleans false and then
immediately `continue`s. It never evaluates that descriptor's enumerable flag
and never marks `allOptionalValuesStringOrUndefined` false for a present
optional accessor.

Consequently a non-enumerable accessor optional field produces the following
diagnostic combination:

```text
allRecordDescriptorsData=false
allRecordDescriptorsEnumerable=true
allOptionalValuesStringOrUndefined=true
```

The exact V37 predicate would reject that same descriptor both because it is
not a data descriptor and because `enumerable !== true`; an accessor is also not
the benign present-`undefined` optional representation V38 is intended to
distinguish. A standalone probe of the exact branch produced
`DIAGNOSTIC_MISMATCH=true` while never invoking the getter.

An unstable Proxy descriptor lookup that returns `undefined` has a related
problem: the code marks presence/data/value checks false but can still leave
`allOptionalValuesStringOrUndefined=true`. The emitted booleans therefore do not
faithfully distinguish every existing V37 structural predicate and can mislead
a separately reviewed successor about whether optional `undefined` is the sole
benign difference.

The non-plain-record branch also forces every later aggregate false without
evaluating those predicates. That is safe but should be represented as
not-evaluated rather than as independent observed failures if the output is
intended to classify each predicate precisely.

**Required fix:** compute descriptor presence, data-ness, and enumerability as
independent booleans before any branch or `continue`. For every present
descriptor, evaluate `descriptor.enumerable === true` without accessing its
value. Treat a missing or non-data optional descriptor as false (or explicitly
not evaluated) for `allOptionalValuesStringOrUndefined`; only a present data
descriptor whose cached value is string or `undefined` may satisfy that
diagnostic. Use `null` or explicit evaluated flags for predicates skipped after
a non-plain record rather than manufacturing false observations. Add fixtures
for enumerable and non-enumerable accessors, a missing descriptor from an
unstable Proxy, and a non-plain record; assert each output boolean independently
matches the corresponding V37 test without invoking a getter.

### V38-003 — IMPORTANT — no committed syntax or pure-fixture proof obligation covers the one-shot diagnostic matrix

The brief's action-time procedure requires byte-for-byte extraction, but it
does not require an `AsyncFunction` or parser syntax check of the extracted
cell. It also contains no offline fixture section or pinned fixture verdict for
the diagnostic itself.

That omission is material for a permanently consuming diagnostic whose sole
purpose is to classify individual private predicates. Required offline coverage
is absent for:

- ordinary current-realm and foreign-realm Arrays, including the demonstrated
  `Array.isArray=true` / `arrayPrototypeExact=false` case;
- own symbols, unsafe length descriptors, missing/unexpected names, holes,
  index accessors, and non-enumerable index descriptors;
- ordinary/null-prototype/non-plain records, record symbols, unexpected or
  missing keys, missing/unstable descriptors, enumerable and non-enumerable
  accessors, optional `undefined`, and empty/oversize/control-bearing values;
  and
- traps proving no iterator, getter, direct indexed read, raw field output, or
  unbounded count occurs, plus exact fixed-schema and cleanup outcomes.

The missing matrix would have caught `V38-002`, and a pinned-module export
fixture would have caught `V38-001`. Review-time ad hoc checks are evidence for
this FAIL; they are not a substitute for a committed, reproducible pre-execution
obligation tied to the exact cell bytes.

**Required fix:** add an explicit offline-check section and action-time pins for
the exact extracted-cell byte count/SHA-256, syntax PASS, and a named pure-
fixture PASS covering every item above. The fixture must treat the foreign-realm
case as a diagnostic expectation only, not as proof of the live listing's realm,
and must assert every boolean independently without executing Chrome or the
browser runtime.

## Correctly preserved boundaries

- The declared gate consumes before import or attachment and remains permanently
  ineligible whether capture succeeds or fails. It cannot retain a tab binding.
- If the module predicate is corrected, the intended sequence contains one
  import, setup, browser get, complete documentation read/write, session name,
  `openTabs`, and fixed terminal write.
- The listing diagnostic contains no `claimTab`, goto, wait, URL read, locator,
  snapshot, tab creation/close, selected/list/get fallback, alternate browser,
  reconnect, or provider method source site.
- Array inspection uses `Array.isArray`, prototype/symbol reflection, one own
  length descriptor, own string names, and cached own index descriptors. It
  performs no `offered.length`, direct index read, iterator, `for...of`, spread,
  `map`, `filter`, `reduce`, or callback enumeration.
- The fixed `arrayIsArray` and `arrayPrototypeExact` booleans safely distinguish
  the supplied inert foreign-realm shape without exposing a prototype or tab
  metadata. They do not and must not classify the live listing before V38 runs.
- Record inspection begins only from cached index-descriptor values. Field names
  and values are never emitted; values are read only from own descriptors.
  `offeredCount` remains `-1` until a safe bounded own length data descriptor is
  proved, then receives only that safe integer in `1..1000`.
- Final evidence contains only fixed property names, booleans/nulls, bounded
  counts/sentinels, fixed states/results, and sanitized error class. It emits no
  property name, descriptor, ID, provider ID, URL, title, group, timestamp,
  account/zone data, raw listing, raw documentation body, raw exception,
  credential, token, or secret.
- All browser/runtime/owner bindings are nulled before the final evidence write.
  JavaScript-visible terminal-output failure repeats fixed cleanup and rethrows
  without a second output. Transport uncertainty is terminal and requires
  immediate realm disposal.
- The action-time package requires exact brief/review/classification ancestry,
  byte/hash extraction, stable source projection, empty index, exact twelve-path
  baseline, runtime/docs pins, clean evidence worktree, zero residue, VM1205
  checkpoint, public-DNS absence, exact owner profile/window/task-tab
  confirmation, no competing owner, and a fresh realm with every named
  V35/V36/V37/V38 declaration absent.
- The final Create/native Copy/native masked Paste confirmation and the later
  separate exact-row deletion confirmation remain mandatory and unreached.
  V38 authorizes neither one nor any credential/provider-persistent action.

## Static method and counter cardinality

The cell contains exactly:

- dynamic import `1`; setup invocation `1`; browser get `1`;
- documentation read `1`; awaited documentation write `1`;
- session naming `1`; `openTabs` `1`; awaited terminal write `1`;
- import/setup/connect/documentation/documentation-write/name/open-tabs
  attempted/fulfilled pairs, each with one increment site per member;
- one `writeAttempted` declaration and one increment;
- claim, navigation, URL, and snapshot attempted counters fixed at `0` and
  explicitly required at `0` by completeness;
- claim, goto, wait, tab URL, locator/evaluate, selected/list/get/new/close,
  browser list/default/URL/extension, reconnect, screenshot, clipboard,
  click/press/fill, fetch, provider mutation, and credential action sites: `0`.

The cardinalities and cleanup layout are otherwise correct but cannot make the
unreachable or semantically inaccurate diagnostic acceptable.

## Finding counts and limits

- Critical: `0`.
- HIGH: `0`.
- IMPORTANT: `3` (`V38-001`, `V38-002`, `V38-003`).
- Minor: `0`.

No live or consuming action was authorized or performed. V38 remains blocked
pending a corrected committed contract and fresh independent review.

## Final verdict

**FAIL**

Unresolved findings: Critical `0`, HIGH `0`, IMPORTANT `3`, Minor `0`.

`authorizes_live_execution=false`
