# OmniRoute V38 listing-shape diagnostic fix round 1 — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only corrected brief commit
`0c37b62b5a30d298f3bff9dbc8e143fe6b09dd78`, its direct parent and original
FAIL review commit `d27ce23e9908827b3e125e483c0d837a05797e13`, and the two paths changed by
the corrected commit:

- `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v38-fresh-session-listing-shape-diagnostic-brief.md`;
- `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v38-pure-fixtures.mjs`.

I reviewed the exact committed diff and current files, the original three
findings, the fixed one-shot cell, the committed pure fixture, and the pinned
runtime export boundary. I ran the committed fixture exactly once. It imported
the pinned module only to inspect its namespace and did not call the real
runtime setup. I also ran one inert standalone JavaScript probe of the exact
`safeErrorClass` expression after identifying a concrete failure-path doubt.

I performed no Chrome setup, browser get, tab enumeration, provider, network,
DNS, routing, clipboard, credential, process-start, Prox-01, or VM action and
did not consume V38. The only workspace write is this assigned review artifact.

## Final verdict

**FAIL** — one HIGH finding remains unresolved. V38 must not be executed.

`authorizes_live_execution=false`

## Exact commit, bytes, and offline evidence

- Reviewed commit: `0c37b62b5a30d298f3bff9dbc8e143fe6b09dd78`.
- Direct parent: `d27ce23e9908827b3e125e483c0d837a05797e13`.
- The reviewed commit changes exactly the corrected brief and adds exactly the
  committed pure-fixture path listed above.
- Brief: `26063` bytes, SHA-256
  `FA76DC5DB60515286BE2E6396C20E8FC2B0191EC09774B7A3796ABE8D88090EC`,
  Git blob `9b83cd09499d02f51ad781a4d2ceed5f17853c95`.
- Fixture: `11265` bytes, SHA-256
  `002715CB46616C1340A9BDF0AC6C46794D7DB6C9F32BB323BF0EA16C711FFC2E`,
  Git blob `775d2302c156a6bc46a9986e4184c3ac7389698e`.
- The committed fixture extracted exactly one LF-normalized JavaScript cell at
  `17001` bytes, SHA-256
  `02F1CC4352E51B0DEA811C358D99C15F7B3FA4B09C46922EA7F8619828ED295E`,
  and constructed an `AsyncFunction` without invoking the real cell.
- Running the exact committed fixture returned:

```json
{"result":"V38_PURE_FIXTURES_PASS","briefBytes":26063,"briefSha256":"FA76DC5DB60515286BE2E6396C20E8FC2B0191EC09774B7A3796ABE8D88090EC","executableBytes":17001,"executableSha256":"02F1CC4352E51B0DEA811C358D99C15F7B3FA4B09C46922EA7F8619828ED295E","syntax":"PASS","moduleShape":true,"fixedSchema":true,"getterCalls":0}
```

- The fixture's transformed full-cell execution replaced only the dynamic
  import expression with inert setup/browser/documentation/listing/terminal
  stubs. It did not call the real `setupBrowserRuntime`, Chrome get, or
  `openTabs`.
- `git diff --check` for the corrected commit is clean. Before creating this
  review, the index was empty and the inherited exact twelve-path dirty product
  baseline remained unstaged.

## Original finding closure

### V38-001 — closed

The cell now requires a non-null module namespace and a function-valued
`setupBrowserRuntime`, without the nonexistent `BROWSER_CLIENT_ID` export. It
calls the reviewed setup function without the unproven `transport` option. The
fixture imports the pinned module without setup and proves the namespace shape,
the setup export, and absence of the invented identity export.

### V38-002 — closed

The exact marked `inspectListingV38` helper now computes descriptor presence,
data-ness, and enumerability independently before branching. Missing and
accessor optional descriptors make
`allOptionalValuesStringOrUndefined=false`; a present optional data descriptor
whose cached value is `undefined` keeps that diagnostic true while correctly
making `allRecordValuesV37Safe=false`. Predicates skipped after an unsafe length,
index descriptor, or non-plain record remain `null`, rather than being reported
as observed failures.

The helper uses descriptor-cached record values only and does not use an
iterator, direct array index, direct record field read, getter, or raw metadata
output. The fixture extracts this exact marked helper from the executable and
covers ordinary and foreign-realm arrays, symbols, bounded length, names,
holes, index descriptors, plain/null-prototype/non-plain records, symbols,
keys, unstable descriptors, accessors, optional `undefined`, string bounds and
controls, direct-read traps, and fixed success schema. The supplied
foreign-realm expectation remains correctly classified as synthetic evidence,
not proof of the live listing's realm.

### V38-003 — only partially closed

The corrected brief now pins a committed syntax and pure-fixture obligation,
and the committed success-path matrix passes. The fixture also proves the
current pinned-module export predicate and an inert success-path terminal
schema, counters, permanent ineligibility, and retained-tab cleanup fields.

It does not exercise a thrown-value failure path. That omission leaves the
catch-handler defect below undetected and means the required failure cleanup,
fixed-value privacy, and no-getter boundary are not yet reproducibly proved.

## Finding

### V38-FIX1-001 — HIGH — untrusted thrown `name` can leak data or bypass cleanup

The outer catch passes an arbitrary caught value to:

```javascript
const safeErrorClass = (error) => {
  const name = typeof error?.name === "string" ? error.name : "Error";
  return /^[A-Za-z][A-Za-z0-9_]{0,63}$/.test(name) ? name : "Error";
};
```

The value caught here is not guaranteed to be a trusted `Error`. Any awaited
browser operation may reject with an arbitrary JavaScript value. More directly,
the listing is explicitly untrusted and the diagnostic invokes reflective
operations whose Proxy traps may throw any value.

The classifier performs an ordinary `name` property read twice. This violates
both hard boundaries the final schema is meant to preserve:

1. An arbitrary thrown object with an own data `name` matching the regular
   expression can place up to 64 attacker-controlled ASCII characters directly
   into `errorClass`. A token-like or credential-derived value can satisfy that
   syntax, so this is not a semantic secret sanitizer or a fixed output value.
2. A thrown object with a `name` getter can run that getter. If it throws, the
   catch handler itself escapes before the setup/agent/browser/tab bindings are
   nulled, before permanent-ineligibility state is set, and before the fixed
   terminal output is attempted.

An inert standalone probe of the exact classifier with a throwing `name`
getter returned:

```json
{"escaped":"name getter invoked","cleaned":false}
```

No getter was needed to demonstrate the output channel: a plain object such as
`{name: "ASecretLikeToken"}` would be accepted and emitted verbatim.

This is HIGH because the one-shot contract explicitly requires no secret or
untrusted-data output and deterministic cleanup on every thrown outcome. A
hostile or malformed listing can violate both before the operator reaches the
documented realm-disposal fallback.

**Required fix:** do not inspect, stringify, coerce, prototype-test, or read any
property from the caught value. Use a literal fixed class such as `"Error"`, or
derive a fixed enumerated failure phase solely from trusted code-owned state.
Add inert transformed-cell failure fixtures in which structural reflection
throws (a) a plain object whose data `name` is a token-like allowed string and
(b) an object whose `name` getter throws. Require zero getter calls, no thrown
value in any terminal field, exactly one fixed failure output, consumed and
permanently-ineligible state, exact failure counters, and cleanup of every
setup/agent/browser/tab binding. Pin this failure matrix in the brief and
action-time fixture verdict.

## Correctly preserved boundaries

- V38 consumes before import, remains permanently ineligible on success or
  failure, and authorizes no adoption or successor action.
- The live cell contains one setup, browser get, complete documentation read
  and write, session name, and `openTabs`; it contains no claim, navigation,
  wait, URL, snapshot, selected/list/get fallback, reconnect, new/close tab,
  provider, credential, clipboard, DNS, routing, or VM action.
- Array and record inspection is reflective and descriptor-cached. It emits
  only fixed keys, booleans/nulls, bounded counts/sentinels, fixed states and
  results, apart from the unsafe error value identified above.
- `offeredCount` remains `-1` until the own length data descriptor proves a safe
  integer in `1..1000`. No candidate filtering or derived identifying count is
  produced.
- The success path clears every runtime and ownership binding before the final
  write; terminal-write failure repeats cleanup, sets a fixed failed state, and
  rethrows. Transport uncertainty remains consumed and requires realm disposal.
- Action-time pins require exact brief/fixture hashes, extraction, syntax and
  fixture verdict, independent PASS ancestry, separate classification tuple,
  stable projection, empty index, exact twelve-path baseline, runtime/docs
  pins, clean evidence worktree, residue/DNS/VM checkpoint, exact owner profile,
  window and task-tab confirmation, and a fresh declaration-free realm.
- The final Create/native Copy/native masked Paste confirmation and separate
  exact-row deletion confirmation remain mandatory, external, and unreached.

## Finding counts and limits

- Critical: `0`.
- HIGH: `1` (`V38-FIX1-001`).
- IMPORTANT: `0`.
- Minor: `0`.

No live or consuming action was authorized or performed. V38 remains blocked
pending a corrected committed contract and fresh independent review.

## Final verdict

**FAIL**

Unresolved findings: Critical `0`, HIGH `1`, IMPORTANT `0`, Minor `0`.

`authorizes_live_execution=false`
