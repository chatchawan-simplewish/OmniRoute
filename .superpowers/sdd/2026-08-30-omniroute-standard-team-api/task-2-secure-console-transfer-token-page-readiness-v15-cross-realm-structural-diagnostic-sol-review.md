# OmniRoute V15 cross-realm structural diagnostic — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only commit
`1704a3a80237b829b81cf1cc0ba69faaf81b7448` and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-token-page-readiness-v15-cross-realm-structural-diagnostic-brief.md`.
Its direct parent is immutable V14 cross-realm-boundary incident commit
`1e8405d21d73af692b3aaa1ac196e6c0fe0b22a2`.

I independently reviewed raw committed bytes, the installed pinned bridge and
its exported plain-object predicate, exact V14 consumption/predecessor state,
the visible selector and bounded wait, the page evaluator and 60-field schema,
the cross-realm acceptance rule, all remaining validation, bounded output,
call cardinality, durable exact-handle retention, cleanup/residue behavior,
no-retry/no-mutation constraints, secret exclusions, and downstream mandatory
confirmations.

I performed no Chrome, browser, provider, clipboard, credential, process,
network, routing, Prox-01, or VM action and did not execute the V15 cell. The
only workspace write is this assigned review artifact. No inherited baseline
source path was modified or staged.

## Final verdict

**PASS** — no Critical, HIGH, or IMPORTANT finding remains unresolved.

## Git and direct-byte pins

- V15 commit: `1704a3a80237b829b81cf1cc0ba69faaf81b7448`.
- Direct parent: `1e8405d21d73af692b3aaa1ac196e6c0fe0b22a2`.
- The V15 commit adds exactly the assigned V15 brief path; reviewed HEAD was
  exactly that commit before this review commit.
- Index before review: zero paths. Exact inherited dirty baseline: twelve
  records, preserved and not staged.
- V15 brief: `27474` bytes, SHA-256
  `10B06179F1A8F731E8F93E2F8BC6B61F15F56D633ED409F40D326A68CF240FE3`,
  Git blob `72052983c87260d54a9eea99d7834ff2afcdf78a`.
- The brief is UTF-8 without BOM, LF-only with zero CR bytes and exactly one
  trailing LF. The target-parent-to-target `git diff --check` passes.
- Immutable V14 incident: `3289` bytes, SHA-256
  `349AD41F6F544626957EA6D25DBBFEB65677831F2261BFA61DE870D0236A72ED`,
  Git blob `676b6e6be5ff9ee3ead1baf7322f653185a9a032`.

## Executable fence and syntax

The brief contains exactly one `javascript` fence. Including its mandatory
final LF, the executable independently reproduces:

- bytes: `21107`;
- SHA-256:
  `24A2AB0390136F3F1360779C190D17DDDEEAA8A864B4B7155B122D42C13A1000`;
- top-level-awaited asynchronous JavaScript syntax: **PASS**.

The syntax check parsed the committed source without evaluating the V15 cell
or loading any live resource. The outer IIFE is awaited exactly once, with no
fire-and-forget `void` form.

## Pinned bridge predicate and exact acceptance

The installed pinned bridge at
`C:\Users\chatc\.codex\plugins\cache\openai-bundled\chrome\26.825.51511\scripts\browser-client.mjs`
independently reproduces:

- `149210` bytes;
- SHA-256
  `C52BA09202F0E82CAA6F6D2A6463A8635C1B1316567975D9B91C1A05FB5AF501`;
- exported minified `isPlainObject` fragment: `135` bytes, SHA-256
  `CE3E29DA20DBE7CEA1C14DB761B4CB45AC14328DB37722E98BF013669ADBC295`.

The pinned predicate is exactly:

```javascript
function to(t){if(t==null||typeof t!="object")return!1;let e=Object.getPrototypeOf(t);return e===null||Object.getPrototypeOf(e)===null}
```

V15 first requires a non-null object, obtains its direct prototype, and accepts
exactly these two mutually exclusive branches:

```javascript
resultPrototypeNullExact =
  resultObjectNonNull && resultPrototype === null;
resultPrototypeParentNullExact =
  resultObjectNonNull &&
  resultPrototype !== null &&
  Object.getPrototypeOf(resultPrototype) === null;
resultPlainRecordExact =
  resultPrototypeNullExact || resultPrototypeParentNullExact;
```

This is semantically identical to the pinned predicate: direct-null objects
take the first branch; local- or cross-realm ordinary records whose direct
prototype has a null parent take the second. No grandparent or broader-chain
walk exists. The separate local-`Object.prototype` equality is retained only
as a safe boolean diagnostic and does not broaden or narrow acceptance.

Static AST inspection finds exactly two `Object.getPrototypeOf` calls: one for
the direct prototype and one, guarded by direct-prototype non-null, for its
parent. The complete prototype block SHA-256 is
`122DA12441A716A33B09C890C7BC38469D4B7E5DBD61043C30BCCE266E13A868`.

## Consumed-V14 predecessor

Immutable incident `1e8405d21d73af692b3aaa1ac196e6c0fe0b22a2`
records exactly one consumed V14 attempt. V14 returned a non-null exact
60-field object and passed every non-prototype validator, but both local-object
prototype identity and direct-null identity were false. V14 completed exact
close, converged residue, retained no tab, made no provider mutation, and left
V4 null/ineligible in exact state `V9_OWNED_TAB_READINESS_FAILED_CLEAN`.

Before its sole creation attempt, V15 requires:

- a fresh V15 gate;
- `secureConsoleV14StructuralDiagnosticConsumed === true` and
  `secureConsoleV14RetainedTab === null`;
- consumed V13, V12, V11, V10, and V9 with every retained handle null;
- consumed V4 adoption with V4 null/ineligible in exact state
  `V9_OWNED_TAB_READINESS_FAILED_CLEAN`; and
- both V4 detach gates and the V4 Cloudflare-read gate still false.

Every predecessor predicate occurs exactly once in the precondition. The V15
consumed flag is set before those checks. There is no V14 invocation,
continuation, reset, reinterpretation, reuse, retry, or fallback; V14 remains
spent.

## Unchanged selector, evaluator, and validation

Raw committed V14/V15 comparison proves:

- the visible placeholder locator plus its single
  `waitFor({ state: "visible", timeout: 10000 })`, count, and uniqueness check
  is byte-identical, segment SHA-256
  `E3F1C0E23A476A675ED9E80098AC4BEE5AC0741BA214EF26BB01915658B61AB3`;
- the page evaluator callback is byte-identical at `7678` bytes, SHA-256
  `812D84DE63708040580573F4D7048B18B4F0EB73607F0F5D65EFB3658B57D7A2`;
- `emptyStructure` is byte-identical, segment SHA-256
  `7F099D809B9C6EE9AFBEBAAD8EEF348825822B8B917D96EFE0806F63DA7C31C2`;
- all validation from `resultExactKeys` through count sentinels is
  byte-identical, SHA-256
  `3B75EBC13A3C572FB86111BB7C0D3165DD38AAE668E4ACC8A15642F823BE4C83`;
  and
- `emptyStructure` and the evaluator return each contain the same exact 60
  unique fields, with no missing, extra, or duplicate key.

Strict acceptance still requires the pinned plain-record predicate, exact keys,
exact boolean types, safe integer types and ranges, consistent found/missing
ancestor tuples, and nonnegative page/candidate count sentinels before copying
the exact expected-key allowlist into a fresh local structure or incrementing
`diagnosticFulfilled`.

Raw page text, hrefs, roles, attributes, URL components, DOM nodes, and
prototype objects remain local to fixed comparisons. The page evaluator and
wait/count operations are read-only.

## Safe stage output

The terminal object emits only fixed status strings, sanitized bounded error
class, booleans, capped/safe integer counts and depths, the validated 60-field
boolean/integer structure, fixed cleanup state, and integer counters.

Prototype output is limited to the fixed booleans
`resultPrototypeObjectExact`, `resultPrototypeNullExact`,
`resultPrototypeParentNullExact`, and `resultPlainRecordExact`. Static AST and
source checks find no terminal reference to `untrustedStructure`, `actualKeys`,
`expectedKeys`, or the raw `resultPrototype`, and no untrusted spread.
`...structure` occurs only after the full validation gate; `...counters`
contains integers initialized locally and changed only by unit increments.

Validation failure leaves the trusted structure empty, fixed false/`-1` stage
sentinels in place, and uses a fixed validation error. Error output is reduced
to a name matching the fixed bounded allowlist regex or the fixed fallback.
No raw key or untrusted raw value is emitted.

## Call cardinality, ownership, and residue

AST call-site counts are exactly one each for `tabs.new`, fixed `goto`, URL
read, bounded `waitFor`, visible-locator `count`, page-local locator `evaluate`,
exact-handle `close`, and terminal `nodeRepl.write`.

Call-site counts are zero for fill, click, press, selected/list/get,
connect/reconnect, detach, screenshot, clipboard read/write, retry, fallback,
alternate-tab selection, Create, edit, and delete operations.

The sole new-tab fulfillment uses one chained assignment:

```javascript
secureConsoleV15RetainedTab = tab = await secureConsoleChromeV5.tabs.new();
```

Thus the exact returned handle becomes both local and durable before any later
statement or await. Shape checks occur only after retention. Exact close is
awaited; local and durable bindings clear only after that close settles
successfully. PASS is promoted only after body completion, exact-close state,
converged residue, and a null retained V15 binding.

Close rejection retains the exact handle and reports unconverged residue.
Malformed fulfillment retains the returned value and reports unconverged
residue. New-tab rejection reports residue unproven. No uncertain or failed
creation/cleanup path can claim clean residue or PASS.

## Mutation, secret, and downstream constraints

- The only navigation target is the fixed public token page; only its exact
  equality boolean is output.
- The executable contains no fill, click, press, Create, edit, delete,
  provider-persistent action, clipboard operation, secret/credential read,
  cookie/storage/session operation, screenshot, or VM/routing action.
- Executable secret scans find no Bearer value, JWT form, or 40-hex secret.
- The exact token name, title-free authenticated semantics, complete-list and
  no-existing-token proofs, no-Create boundary, V4 detach ordering, final
  Create/native Copy/native masked Paste confirmation, later separate exact-row
  deletion confirmation, revocation hold, invalid-token proof, retained-owner
  disposition, and cleanup requirements remain mandatory and unchanged.

## Findings by severity

- Critical: none.
- HIGH: none unresolved.
- IMPORTANT: none unresolved.
- Minor: none.

## Residual limits

- This review proves committed static bytes and current installed bridge bytes
  only. It does not prove current browser, controller, provider, credential,
  process, VM, DNS, routing, or persistent-REPL state.
- This PASS does not authorize live execution. The brief still requires a
  non-self-referential classification, post-commit tuple, and fresh action-time
  pins before its separately owned one-shot gate can be considered.
- Static review grants no provider mutation authority.

## Final verdict

**PASS**

Unresolved findings: Critical `0`, HIGH `0`, IMPORTANT `0`, Minor `0`.

`authorizes_live_execution=false`
