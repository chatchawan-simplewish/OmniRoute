# OmniRoute V48 fresh-realm listing-shape diagnostic design

Date: 2026-09-02
Status: approved under the project standing unattended design authority

## Purpose and predecessor

V47 is consumed and failed cleanly. Its fixed incident is commit
`28a77a3fed0816709d390129552fc5d3bed17957`. V47 must never be retried,
continued, reinterpreted, relaxed, or reused.

V47 proved that attachment setup and pinned API documentation validation passed,
and that its sole `openTabs()` call fulfilled. It failed before trusted-listing
validation completed. The exact rejecting structural subpredicate remains **NOT
PROVEN**. The presence of other tabs or another Codex task is not a proven cause.

V48 is the smallest new one-shot, read-only structural diagnostic. It determines
which existing trusted-listing predicate rejects the current `openTabs()` result
without revealing any tab identifier, title, URL, group value, provider data, or
secret. It does not select or claim a tab and cannot authorize later adoption.

## Ownership and concurrency boundary

- This task remains sole owner of the OmniRoute provider and authority-gate lane.
- Another Codex task may control different tabs in the same Chrome profile or
  window only while its live-resource lane is disjoint.
- V48 may use only the freshly confirmed Cloudflare API Tokens task tab surface.
- Any observed overlap on the same tab or Cloudflare object is a fail-closed stop.
- V48 does not require other disjoint-tab tasks to stop and must not inspect,
  identify, claim, navigate, or close their tabs.

## Immutable runtime and API boundary

V48 reuses the exact pinned CUA Node runtime, browser-client module, and complete
API documentation bytes already required by V47. No alternate runtime, browser
API, extension path, direct DevTools connection, HTTP client, shell browser
automation, retry, fallback, or manual integration is allowed.

The executable must:

1. run in a freshly reset persistent Node realm;
2. validate the fixed declaration audit before execution;
3. load the pinned browser client once;
4. obtain only the named `chrome` browser surface;
5. read and validate the complete pinned documentation once;
6. set the reviewed session name once; and
7. call `openTabs()` exactly once.

All calls after `openTabs()` are forbidden. V48 performs no claim, navigation,
wait, page URL read, snapshot, DOM action, clipboard action, provider mutation,
DNS action, VM action, secret-store action, or network request.

## Diagnostic data flow

The `openTabs()` result is treated as untrusted. Inspection uses only cached
standard built-ins and own-property descriptors. No untrusted iterator, getter,
setter, proxy-dependent callback enumerator, direct indexed read, spread,
destructuring, `for...of`, `map`, `filter`, or `reduce` is allowed.

The diagnostic emits a fixed result object containing only:

- a fixed V48 result literal;
- fixed state and single-use booleans;
- one bounded `offeredCount`, otherwise `-1`;
- aggregate array-structure booleans;
- aggregate rank-zero record-structure booleans;
- fixed per-documented-key descriptor/type booleans;
- fixed URL-classification booleans derived in memory; and
- fixed zero counters proving forbidden operations were not attempted.

It must never emit or stringify an exception, object, key value, tab record,
identifier, title, URL, group value, provider response, page content, clipboard
content, or secret.

## Fixed array predicates

V48 reports these predicates independently so the rejecting rule is identifiable:

- result is an array;
- own symbol count is zero;
- own `length` descriptor exists;
- `length` is a data descriptor, non-enumerable, and has no getter or setter;
- `length` value is a safe integer in `[1,1000]`;
- own string names are exactly `length` plus canonical indices `0..length-1`;
- every index has an own enumerable data descriptor with no getter or setter;
- every index descriptor contains a non-null object value; and
- descriptor-derived index count equals the bounded length.

`offeredCount` is populated only from the cached own `length` data descriptor
after the bounded-length predicate passes. Otherwise it stays `-1`.

## Fixed rank-zero record predicates

Only the value cached from index `0`'s own data descriptor may be inspected. V48
reports independently:

- non-null object status;
- ordinary-object prototype status and bounded prototype depth;
- own symbol count zero;
- all own string names are documented keys;
- required identity-key presence;
- unexpected-key count, bounded and otherwise `-1`;
- for each documented key: own presence, data-descriptor status, enumerable
  status, and no getter/setter status;
- every present required value is a non-empty bounded control-free string;
- every present optional value is either `undefined` or a non-empty bounded
  control-free string; and
- the strict historical V47 all-values predicate, reported separately from the
  optional-string-or-undefined predicate.

The implementation plan must copy the documented key set and required/optional
classification exactly from the V47 committed executable and pinned API docs. It
must not invent a new accepted shape.

## Fixed URL predicates

If and only if the documented URL field has already passed its own cached data
descriptor and safe-string checks, V48 may parse that in-memory string with the
cached standard `URL` constructor. It reports only booleans for:

- URL field present;
- URL field safe string;
- URL parse success;
- HTTPS scheme;
- exact `dash.cloudflare.com` hostname; and
- exact intended API Tokens pathname.

The raw URL and all parsed components must be cleared before output and must
never be returned, logged, committed, or placed in evidence.

## Failure and cleanup semantics

- V48 is consumed at the start of its single live send.
- Any setup, documentation, listing, inspection, or cleanup uncertainty produces
  one fixed failure literal and permanent ineligibility.
- The outer catch reports only the fixed error class `Error`; it must not inspect
  or stringify the thrown value.
- Local browser, agent, documentation, listing, descriptor, record, and URL
  bindings are cleared before the result is returned.
- The result remains diagnostic-only and permanently ineligible even when every
  predicate passes.
- After the fixed output, one state-only query must prove consumed, ineligible,
  terminal state, cleared bindings, and zero forbidden-operation counters.
- The CUA realm is reset immediately after that cleanup proof.

V48 must not create a background process, proxy, listener, owner, route, token,
credential, DNS record, tunnel, VM process, temp file, or provider-persistent
state. A live result is documented as a single exact-path incident/evidence
artifact containing only the sanitized fixed fields.

## Verification and review plan

Before live execution, the implementation must provide:

1. one exact executable source and one smallest pure-fixture check;
2. syntax PASS plus a fixed `V48_PURE_FIXTURES_PASS` result covering ordinary,
   optional-undefined, accessor, symbol, sparse, extra-key, bad-prototype,
   malformed-length, malformed-URL, and throwing-object cases;
3. a committed byte/hash review package;
4. independent Sol High review with zero unresolved Critical, HIGH, or IMPORTANT
   findings and an exact PASS verdict;
5. a later non-self-referential execution-classification commit whose parent is
   the PASS review commit;
6. a separate post-commit coordinator tuple proving the exact classification
   commit, parent chain, path set, hashes, empty index, preserved exact 12-path
   dirty baseline, and stable projection;
7. the pinned runtime/docs, clean evidence worktree, Windows no-residue state,
   VM1205 safe checkpoint, and public DNS absence revalidated at action time;
8. a fresh realm, fixed declaration audit, and a new exact external confirmation
   that the intended Cloudflare task tab is selected; and
9. no evidence of a conflicting task acting on the same tab or Cloudflare object.

No live send is allowed before all nine items pass. A failure or uncertainty
spends V48 and forbids retry, continuation, fallback, reinterpretation, verdict
relaxation, or reuse. Any later attachment fix requires a newly reviewed V49
contract based only on V48's sanitized evidence.

## Approval record

The owner pre-approved the coordinator's safest routine design recommendation in
the project standing authority. This design selects the previously presented
recommended option: a new sanitized, structural, diagnostic-only one-shot. That
preapproval does not waive independent Sol High review, action-time pins,
single-use semantics, fresh external tab confirmation, secrets handling, or any
later mandatory Create/native Copy/native masked Paste and exact-row deletion
confirmations.
