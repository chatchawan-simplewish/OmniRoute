# OmniRoute V12 visible structural diagnostic — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only commit
`6062100e6d5893980419dd5edc377777806f7032` and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-token-page-readiness-v12-visible-structural-diagnostic-brief.md`.
Its direct parent is immutable V11 clean ambiguity incident commit
`612aff1c272407983b6b0cadb01a79e8bb948ae4`.

I reviewed exact V11 consumption/predecessor state, the sole reviewed CSS
`:visible` narrowing and bounded wait, unchanged 60-field evaluator/validation,
call cardinality, durable exact-handle retention, exact-close acceptance,
failure residue, safe output, no-retry/no-provider-mutation boundaries,
secrets, and preserved downstream confirmations.

I performed no Chrome, browser, provider, clipboard, credential, process,
network, routing, Prox-01, or VM action and did not execute the V12 cell. The
only workspace write is this assigned review artifact. No baseline source path
was modified or staged.

## Final verdict

**PASS** — no Critical, HIGH, or IMPORTANT finding remains unresolved.

## Git and direct-byte pins

- V12 commit: `6062100e6d5893980419dd5edc377777806f7032`.
- Direct parent: `612aff1c272407983b6b0cadb01a79e8bb948ae4`.
- The V12 commit adds exactly the V12 brief path; reviewed HEAD equaled that
  commit before this review commit.
- Index before review: zero paths. Exact inherited dirty baseline: twelve
  source records, preserved and not staged.
- V12 brief: `23426` bytes, SHA-256
  `C94D6AEC6680A704DABF9275242D9583ED191AC83955498B1E5F0F80140CE8B2`,
  Git blob `cc1a4aebeeaf352c0ed0fc69a2df25d4cb05dd28`.
- Encoding is strict UTF-8 without BOM, LF-only, zero CR bytes, and exactly one
  trailing LF. `git diff --check` from the V11 incident parent to V12 passes.

## Executable fence and syntax

The brief contains exactly one `javascript` fence. Including its mandatory
final LF, the executable independently reproduces:

- bytes: `18502`;
- SHA-256:
  `18C66B1B29B1A547EC381211669589FE8F9BBA2F3682C9F7F50F51BD0A877BA4`;
- top-level-awaited asynchronous JavaScript syntax: **PASS**.

The syntax check parsed an async wrapper without evaluating the V12 cell or
loading any live resource. The outer IIFE is awaited exactly once and has no
fire-and-forget `void` form.

## Exact predecessor and replacement boundary

Immutable V11 incident
`612aff1c272407983b6b0cadb01a79e8bb948ae4` records one consumed V11 attempt,
one fulfilled bounded visible wait, two matches from the unfiltered placeholder
locator, zero evaluator calls, exact created-tab close, converged residue, null
V11 retained handle, and unchanged null/ineligible V4 state.

V12 requires, before its sole creation attempt:

- fresh V12 consumption state;
- `secureConsoleV11StructuralDiagnosticConsumed === true` and
  `secureConsoleV11RetainedTab === null`;
- consumed V10 and V9 with both retained handles null;
- consumed V4 adoption with V4 null/ineligible in exact state
  `V9_OWNED_TAB_READINESS_FAILED_CLEAN`; and
- both V4 detach gates and the V4 Cloudflare-read gate still false.

The V12 consumed flag is set before those checks. There is no V11 invocation,
continuation, reset, reinterpretation, or reuse. V11 remains spent.

## Reviewed visible narrowing and bounded wait

After one fixed navigation and fixed-URL equality check, V12 changes only the
candidate selector from V11's unfiltered placeholder predicate to:

```javascript
input[placeholder*="search" i]:visible
```

The executable contains exactly one `:visible` occurrence. It verifies the
resulting locator's `waitFor` shape and makes exactly one bounded call:

```javascript
await tokenFilter.waitFor({ state: "visible", timeout: 10000 });
```

The same narrowed locator is then counted exactly once and must equal one
before its sole evaluation. There is no alternate selector, second wait, loop,
retry, fallback, or manual continuation. If visibility/cardinality changes
before evaluation, the locator operation fails closed rather than selecting an
unreviewed fallback.

## Unchanged evaluator and strict output validation

Static AST comparison against V11 commit
`3dc06bb377bc701b54c1c04875f123466ca17d8e` proves:

- V11 and V12 evaluator callback text is byte-identical, SHA-256
  `812D84DE63708040580573F4D7048B18B4F0EB73607F0F5D65EFB3658B57D7A2`;
- V11 and V12 validation/projection text from `expectedKeys` through the
  pre-fulfillment boundary is byte-identical, SHA-256
  `953936A7AB55258F7C32834D9E3BB30E98D644ECB2DB4916368F14796838F418`;
- `emptyStructure` and the evaluator return each have exactly 60 unique keys,
  with no missing, extra, or duplicate key; and
- the seven unique boolean keys are all members of that exact set.

The controller still requires a non-null plain object, exact sorted 60-key
equality, exact boolean types, safe integer/range checks, consistent
found/missing ancestor tuples, and nonnegative page/global candidate counts.
Mismatch throws before diagnostic fulfillment or body completion. Accepted
data is copied key-by-key into a fresh allowlisted object; the terminal has
zero untrusted spreads.

The visible input is the evaluator subject. Its candidate metrics deliberately
retain the unchanged raw placeholder descendant counts, so the structural
diagnostic can report the hidden duplicate without selecting or acting on it.
All raw page text, href, role, attribute, URL, and DOM values remain confined
to evaluator-local comparisons.

## Call cardinality, ownership, and residue

- Exact direct call cardinality is one each for `tabs.new`, fixed `goto`, URL
  read, bounded `waitFor`, narrowed-locator `count`, page-local locator
  `evaluate`, exact-handle `close`, and terminal `nodeRepl.write`.
- Fill, click, press, clipboard, selected, list, get, connect/reconnect, retry,
  fallback, alternate-tab, screenshot, and detach call cardinality is zero.
- One chained fulfillment assignment retains the returned handle in local and
  durable V12 state before every later await.
- Exact PASS is possible only after the exact close settles, local and V12
  bindings are cleared, cleanup is `CREATED_TAB_CLOSED`, and residue is
  converged.
- Close rejection and malformed handle fulfillment retain the exact returned
  value; creation rejection remains residue-unproven. No failure path falsely
  claims clean residue.
- The only URL is the fixed public token page and output contains only its
  equality boolean. The wait, count, and evaluator are read-only; no
  provider-persistent or page-form mutation is present.

## Output, secret, and downstream constraints

- Terminal output is restricted to fixed statuses, sanitized error class,
  booleans, and safe integer counts/depths.
- No raw ID, URL, href, title, attribute value, page text, DOM, HTML,
  screenshot, fingerprint, token, secret, credential, cookie, storage,
  session, or clipboard content is emitted.
- No Bearer value, JWT form, or 40-hex secret occurs in executable code.
- V12 performs no fill, click, press, Create, edit, delete, clipboard, secret,
  credential, cookie, storage, or session action.
- The exact token name, title-free authenticated semantics, complete-list and
  no-existing-token proofs, no-Create rule, V4 detach ordering, final
  Create/native Copy/native masked Paste confirmation, later separate exact-row
  deletion confirmation, revocation hold, invalid-token proof, retained-owner
  disposition, and cleanup requirements remain preserved.

## Findings by severity

- Critical: none.
- HIGH: none unresolved.
- IMPORTANT: none unresolved.
- Minor: none.

## Residual limits

- This review proves only committed static bytes. It does not prove current
  browser, controller, provider, credential, process, VM, DNS, routing, or
  persistent-REPL state.
- This PASS does not itself authorize live execution. The brief still requires
  non-self-referential classification, a post-commit tuple, and fresh
  action-time pins before its separately owned one-shot gate can be considered.
- Static review grants no provider mutation authority.

## Final verdict

**PASS**

Unresolved findings: Critical `0`, HIGH `0`, IMPORTANT `0`, Minor `0`.

`authorizes_live_execution=false`
