# OmniRoute V7 owned-tab replacement — independent Sol High review

Date: `2026-09-01` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only committed V7 brief
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-token-page-readiness-v7-owned-tab-replacement-brief.md`
at commit `6d2b30ab352dbe6f24d416ad4f79368469a1f62d` against the immutable V6
incident, V6 reviewed chain, pinned Chrome API documentation, and immutable
V5/V4 semantic contract.

I performed direct-byte, ancestry, syntax, API-signature, call-surface,
predecessor-state, exact-handle lifecycle, partial-apply, semantic-equivalence,
failure-disposition, secret-surface, confirmation, and V4 detach-ordering
checks. I performed no Chrome, browser, provider, clipboard, credential,
process, network, routing, Prox-01, or VM1205 action and did not execute the V7
cell against a live runtime.

This review does not classify V7 for execution, consume V7, or authorize any
live action.

## Final verdict

**FAIL** — one unresolved **HIGH** exact-handle retention and partial-apply
finding prevents a PASS. A created tab can become hidden from every durable
binding if the cell is interrupted after `tabs.new()` fulfills but before a
normally completed cleanup branch records the handle.

## Git, file, and API pins

- Reviewed commit: `6d2b30ab352dbe6f24d416ad4f79368469a1f62d`.
- Direct parent: immutable V6 incident commit
  `4acecd710db9a31eab2af7797df0ad8bd93e3073`.
- The reviewed commit adds exactly one path: the V7 brief named above.
- Reviewed HEAD equals the V7 commit; index before review is zero; the exact
  inherited twelve-path dirty source baseline is unchanged.
- V7 brief: `19734` bytes, SHA-256
  `88FD27429F756A87764E455DB262B2F16F77940FDD2A2CF74612EC44D7C6AEA9`,
  Git blob `cca2211ae0c07d5d4f25d8c831db94c2b3b04bd6`.
- V7 encoding: strict UTF-8 without BOM, zero CR bytes, LF-only, and exactly
  one trailing LF.
- V6 incident: `2466` bytes, SHA-256
  `116AF5437A985B78EE3269FAE378C406B61FFD2450152A42E8BB13286C4F63E1`,
  Git blob `4280efa565114bb6848e2d4a83eb6b502c5acc01`.
- Pinned Chrome `api.json`: `58477` bytes, SHA-256
  `4BFEB97E958025DB37D52AEA11B75BC70BCA417B4995B0F711C0F07F3DDCCB08`.
  Its direct declarations are `new(): Promise<Tab>` and
  `close(): Promise<void>`.
- `git diff --check` from the V6 incident through V7 passes.

The immutable V6 chain reproduces directly:

| Artifact | Commit | Bytes | SHA-256 | Git blob |
| --- | --- | ---: | --- | --- |
| V6 brief | `7050edd5b3ca22b22a42a48efeb4db4ef79e1e1d` | `18232` | `70A01F594B443EB003CD0F5FEDF233E99658773EABAECE41CAF132F6BBD7616B` | `13981e01e931fbaafbe6b1fba7f0ea5cdb38243c` |
| V6 Sol High review | `7d20afac35bcbe9f14937f9ec3444d059ccc759a` | `11152` | `0CD3FE83C64A8DA571634F0816C5BB688B8CE287CE8F3767CD06117FDC8FAD6B` | `fe2658519b2e3f4fd50d67e597a2c781cda7e431` |
| V6 classification | `4a144e120931fa23e50e1d09f94df477635e8d82` | `7093` | `83224CABF5431E23DCADF5D4114F7F852A26DB4A6136E2EF44CCFEBD48B9B794` | `ef3968f95dd712d51220e7772e39861c71e0f830` |

The V6 brief, review, classification, incident, and V7 brief form the required
linear parent chain.

## Executable fence and syntax

The brief contains exactly one `javascript` fence. Its executable content,
including the final LF, reproduces:

- bytes: `14103`;
- SHA-256:
  `1683849B04EE4638BDC8764C69EB0DAB6ABC27233357E6D68C3C4E86BC735B45`;
- asynchronous JavaScript syntax: **PASS**.

The syntax check parsed an async wrapper without executing the cell, importing
a runtime, or contacting a browser.

## Findings by severity

### HIGH — the created exact handle is not durably retained before later awaits

**Evidence:** In the executable fence, `secureConsoleV7RetainedTab` is declared
outside the IIFE and initialized to null at brief line 75. The owned tab is
created into the IIFE-local variable only at line 153:

```javascript
adopted = await secureConsoleChromeV5.tabs.new();
```

The code then records only a local boolean at line 155. It does not assign
`adopted` to the durable `secureConsoleV7RetainedTab` binding before awaiting
navigation, URL, paginator readiness, query-echo readiness, empty-state
readiness, or cleanup. The first possible assignment of the exact handle to
`secureConsoleV7RetainedTab` is at line 274, inside the normally caught
`adopted.close()` rejection branch; the other assignment is the malformed
no-close branch at line 280.

Direct executable ordering confirms:

- `tabs.new()` fulfillment/capture precedes the first later await;
- the first later await is `adopted.goto(...)`;
- `secureConsoleV7RetainedTab = adopted` occurs only after the cleanup
  `await adopted.close()` call site;
- there is no durable exact-handle assignment between `tabs.new()` fulfillment
  and the first later await.

**Impact:** If `tabs.new()` has fulfilled and created a tab, but the outer tool
times out, is interrupted, loses output, or becomes uncertain during any later
navigation/readiness await, the exact handle exists only in the inaccessible
IIFE-local `adopted` variable. The durable retained-handle variable still
reports null. The same gap exists while `adopted.close()` settlement is
uncertain: the global retained binding is populated only after a normal close
rejection reaches its catch block.

This creates the prohibited partial-apply state: a controller-owned tab may
exist while neither the V4 binding nor `secureConsoleV7RetainedTab` exposes its
exact handle to the required new offline disposition contract. The prose
correctly labels timeout/uncertainty as unproven, but the implementation loses
the only exact cleanup capability needed to converge that unproven residue.
It therefore does not satisfy “capture the exact created handle before any
verdict” under interruption semantics and can hide residue.

**Required remediation:** A replacement contract must publish the exact
returned object to the durable retained binding immediately after
`tabs.new()` fulfills and before shape evaluation or any later await. All
failure cleanup must operate on that durable exact binding. Clear it only
after `close()` has fulfilled, or after the exact same handle has been
synchronously transferred into the eligible V4 binding on semantic PASS.
Close rejection, close timeout, interruption, truncation, or uncertainty must
leave the durable exact handle retained rather than null. Re-review direct
bytes and bounded fixtures for interruption immediately after creation,
during navigation/readiness, and during close settlement.

### Critical

None.

### IMPORTANT

None beyond the blocking HIGH finding above.

### Minor

None.

## Verified non-finding areas

### Exact V6 predecessor

The immutable incident records V6 consumed exactly once with sole `tabs.list`
attempted/fulfilled `1/1`, offered-tab count zero, declaration/predecessor exact,
no controller/tab shape, zero navigation/readiness/fill/Create/name/row calls,
V4 binding null/ineligible in exact state
`V6_LIST_REACQUISITION_OR_READINESS_FAILED`, and no provider/credential/
process/routing/VM/DNS/Cloudflare-persistent action.

Before `tabs.new()`, V7 checks the fresh V7 gate plus every retained value
available from that exact terminal: V6 consumed; V5 attachment exact with
connect/documentation `1/1`; V5 connected shape and error `NONE`; V4 adoption
consumed; V4 binding null/ineligible in the exact V6 failure state; and V4
prestart plus both detach cells unconsumed. A predecessor mismatch consumes V7
before tab creation.

### Acquisition and close call surface

Direct executable cardinality is:

- `secureConsoleChromeV5.tabs.new()`: exactly `1` call site;
- exact-handle `adopted.close()`: exactly `1` call site;
- `tabs.selected`, `tabs.list`, `tabs.get`, browser connect/bootstrap,
  reconnect, retry, alternate-browser logic, and fallback: `0` each.

The returned object is captured in local `adopted` before its local shape
verdict. Controller/tab shape requires non-null object, string ID, and callable
`close`, `goto`, `url`, `playwright.getByRole`, and
`playwright.getByText`. These normal-path checks are sound; the HIGH finding is
that the exact object is not made durable before subsequent asynchronous
partial-apply points.

### Completed failure dispositions

For normally completed execution, the branches do not falsely claim clean
residue:

- `tabs.new()` rejection records `NEW_REJECTED_RESIDUE_UNPROVEN`;
- fulfillment without a usable object records
  `NEW_FULFILLED_WITHOUT_TAB_HANDLE` and residue unproven;
- a malformed non-null return without `close` is retained and marked
  `MALFORMED_EXACT_HANDLE_RETAINED`;
- a normal close rejection retains the exact local object and marks
  `CLOSE_FAILED_EXACT_HANDLE_RETAINED`;
- only a fulfilled `close()` records `CREATED_TAB_CLOSED` and converged
  residue;
- every completed non-PASS leaves the V4 binding null/ineligible.

These completed branches are correctly fail-closed. They do not repair the
interruption/uncertain-settlement gap identified above.

### V5/V4 semantic equivalence and completeness

The V4, V5, and V7 downstream semantic bodies, from the first navigation
counter through the PASS result assignment, are byte-identical after normalizing
only the result label: `6798` bytes, SHA-256
`FCA4B89585E2E34115A432EB3348A8A5175292653AE062EE5AC180742DAF6609`.

V7 therefore preserves the reviewed exact public URL, unique search/result
binding, paginator/busy/row/total completeness proof, exact filter query echo,
terminal zero state, one semantic Create control, zero name/row matches,
sanitized error class, and exact success counters. It counts the Create
control but performs no click or provider-persistent Create/edit/delete.

### V4 binding and detach ordering

Semantic PASS alone transfers the exact local handle into the V4-compatible
eligible binding and permits the unchanged V4 prestart cell once. A completed
V7 failure leaves the V4 binding null/ineligible and permits neither detach.
A later prestart/pre-Create failure after semantic PASS permits only the exact
V4 pre-Create zero-browser-call detach. The post-native detach remains
reserved until the user reports the native generated-page close.

The unchanged V4 prestart, pre-Create detach, and post-native detach blocks
retain their reviewed hashes:

- `20437` bytes,
  `FAB457F36F3AEA9EFF89716DD28C30751B2F7607683E31CCCBA4D7F9C4A6AEBB`;
- `2309` bytes,
  `60692947118FCD2CA765B8C7C850490B79B9ED3C0D3942D14CB5F429F924746D`;
- `2305` bytes,
  `5ABC144ABA9866294EC4A7746906E3D3132ADAE993B93969C426295085FE102D`.

### Secrets and mandatory confirmations

The executable contains no Bearer value, OpenAI-style key, JWT form, 40-hex
secret, clipboard operation, screenshot, click, press, or secret-output field.
Its terminal contains only fixed labels, booleans, counters, a sanitized error
class, cleanup state, and binding state; it does not emit the tab object/ID,
URL, title, page content, DOM, credential, exception message, or response body.

The mandatory combined final Create, user-native semantic Copy, and
user-native masked Paste confirmation remains withheld. Later deletion of the
exact created row retains its own separate mandatory confirmation. Standing
unattended authority waives neither checkpoint.

## Residual limits and required next state

- V7 must not be classified PASS or executed from this review.
- The committed V7 brief is immutable review input; remedy requires a new
  exact-path replacement/fix contract and fresh independent Sol High review.
- No Chrome inspection or cleanup call is authorized by this static review.
- Current runtime, browser, provider, VM1205, DNS, process, credential,
  projection, and action-time state remain outside this static verdict.

## Final verdict

**FAIL**

Unresolved findings: Critical `0`, HIGH `1`, IMPORTANT `0`, Minor `0`.

`authorizes_live_execution=false`
