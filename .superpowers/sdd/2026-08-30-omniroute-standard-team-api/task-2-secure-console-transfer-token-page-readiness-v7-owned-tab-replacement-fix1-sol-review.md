# OmniRoute V7 owned-tab replacement fix 1 — independent Sol High re-review

Date: `2026-09-01` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This re-review covers only fix commit
`398e9789a1fcf57b884b446c839bebb9f9e471ab` and its modification of exact
path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-token-page-readiness-v7-owned-tab-replacement-brief.md`.

The comparison points are original V7 commit
`6d2b30ab352dbe6f24d416ad4f79368469a1f62d` and its committed FAIL review
`73af6c57a0f5b0099897c1ead175c055e29c7ec7`. I rechecked the fixed exact-
handle lifecycle and all prior predecessor, API, one-shot, call-cardinality,
semantic, completeness, failure-disposition, secret, confirmation, counter,
and V4 detach constraints.

I performed no Chrome, browser, provider, clipboard, credential, process,
network, routing, Prox-01, or VM1205 action and did not execute the V7 cell
against a live runtime. This static review does not consume V7 or authorize
live execution.

## Final verdict

**PASS** — fix round 1 closes the sole prior HIGH finding. There is no
unresolved Critical, HIGH, or IMPORTANT finding.

## Git and direct-byte pins

- Fix commit: `398e9789a1fcf57b884b446c839bebb9f9e471ab`.
- Direct parent: prior FAIL review commit
  `73af6c57a0f5b0099897c1ead175c055e29c7ec7`.
- The fix commit changes exactly one path: the V7 brief named above.
- Prior FAIL review directly descends from original V7 and adds exactly its
  one review path.
- Current reviewed HEAD equals the fix commit.
- Index before review: `0` paths.
- Exact inherited dirty baseline: twelve source records, unchanged.
- Fixed V7 brief: `20371` bytes, SHA-256
  `45A7263EAB74980F35D41FF03488F94F67C3A72175203D4C569B0207C2FD0689`,
  Git blob `0c1cf6ddb8a1aa0326222fdf7e13c2d26d186099`.
- Fixed brief encoding: strict UTF-8 without BOM, zero CR bytes, LF-only, and
  exactly one trailing LF.
- Prior FAIL review: `11909` bytes, SHA-256
  `FFD182D005BA39E52DFE750210CF528D2B605E9C81BA226F27732EFEB15F69CC`,
  Git blob `5205b308c52681c56d420ac7ce32af5893b38142`.
- `git diff --check` from the prior FAIL review to the fix commit passes.

Pinned Chrome `api.json` remains exactly `58477` bytes, SHA-256
`4BFEB97E958025DB37D52AEA11B75BC70BCA417B4995B0F711C0F07F3DDCCB08`,
with direct declarations `new(): Promise<Tab>` and
`close(): Promise<void>`.

## Executable fence and syntax

The fixed brief contains exactly one `javascript` fence. Its executable
content, including the final LF, reproduces:

- bytes: `14216`;
- SHA-256:
  `315CC025B22734432F593A3BEBAA1AEAA173A36B509DC83658763408AD184BC0`;
- asynchronous JavaScript syntax: **PASS**.

The syntax check parsed an async wrapper without executing the cell, loading a
browser runtime, or contacting any live resource.

## Prior HIGH finding — CLOSED

### Durable capture before every later boundary

The returned object is now written by one chained fulfillment assignment:

```javascript
secureConsoleV7RetainedTab = adopted = await secureConsoleChromeV5.tabs.new();
```

The assignment appears exactly once. When the `await` fulfills, JavaScript
completes both lexical assignments in the same expression before advancing to
the next statement. The durable top-level retained binding therefore receives
the same exact object as local `adopted` before the fulfillment counter, shape
verdict, navigation, or any later await.

Direct source ordering reproduces:

- chained durable assignment before `counters.newFulfilled++`;
- chained durable assignment before local `createdHandleCaptured` and tab-
  shape evaluation;
- chained durable assignment before every later navigation, URL, locator,
  readiness, fill, semantic, and cleanup await;
- `21` post-assignment await expressions in total, all occurring before the
  first post-creation `secureConsoleV7RetainedTab = null`;
- the last such await is the sole `await adopted.close()` call.

Thus interruption, timeout, truncation, or uncertainty at any post-creation
asynchronous boundary leaves `secureConsoleV7RetainedTab` pointing to the exact
created object. The handle no longer exists only in IIFE-local state.

### Close settlement and failure retention

The cell has one exact-handle `adopted.close()` call site. The durable retained
binding remains populated while close is pending. Only after `close()` fulfills
does the cell increment cleanup fulfillment, null local `adopted`, and then
clear `secureConsoleV7RetainedTab` before declaring
`CREATED_TAB_CLOSED`/converged residue.

Normal close rejection keeps or reassigns the same exact object in the durable
binding and reports `CLOSE_FAILED_EXACT_HANDLE_RETAINED`. Close timeout,
interruption, or uncertain settlement cannot reach the clearing statement, so
the durable exact handle remains available for a new reviewed disposition.

### Success ownership transfer before alias clear

On semantic PASS, the synchronous success branch assigns the exact local
object to `secureConsoleOwnedTaskTabV4`, sets eligibility true, and sets exact
state `TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE` before clearing the V7 retained
alias. If interrupted before that clear, the retained alias still exposes the
handle. If interrupted after it, the complete V4 binding tuple already exposes
the same handle. There is no success-side interval with an existing tab and no
durable exact handle.

The original hidden-residue/partial-apply gap is therefore closed.

## Rechecked security and specification constraints

### Exact predecessor and one-shot state

The immutable V6 incident and retained predecessor checks are unchanged. V7
requires fresh V7 gate state; consumed V6; exact V5 attachment and connect/
documentation `1/1`; exact V5 attachment shape/error; V4 adoption consumed;
V4 binding null/ineligible in
`V6_LIST_REACQUISITION_OR_READINESS_FAILED`; and V4 prestart plus both detach
cells unconsumed.

V7 sets its consumed flag before declaration, predecessor, creation, shape, or
semantic failure can occur. `tabs.new()` rejection remains
`NEW_REJECTED_RESIDUE_UNPROVEN`; fulfillment without a usable handle remains
`NEW_FULFILLED_WITHOUT_TAB_HANDLE`. Neither case claims clean residue or
authorizes retry, inspection, fallback, or cleanup improvisation.

### Call cardinality and controller/tab shape

Direct executable-code cardinality remains:

- `secureConsoleChromeV5.tabs.new()`: exactly `1`;
- exact-handle `adopted.close()`: exactly `1` call site;
- `tabs.selected`, `tabs.list`, `tabs.get`, browser bootstrap/connect,
  reconnect, retry, alternate-browser logic, and fallback: `0` each;
- terminal `nodeRepl.write`: exactly `1`.

The returned object must be non-null with string controller ID and callable
`close`, `goto`, `url`, `playwright.getByRole`, and
`playwright.getByText`. A malformed non-null return remains durably retained
and explicitly unconverged. No alternate handle or tab is obtained.

### Completed failure and no-residue claims

The fixed normal-completion branches remain conservative:

- no creation attempt after predecessor failure: `NOT_NEEDED_NO_TAB`;
- `tabs.new()` rejection or unusable fulfillment: residue unproven;
- malformed object without close: exact returned value retained, residue
  unconverged;
- close rejection: exact handle retained, residue unconverged;
- only fulfilled exact-handle close: `CREATED_TAB_CLOSED`, retained alias
  cleared, residue converged;
- every completed non-PASS: V4 binding null/ineligible with clean versus
  retained-handle state selected from the durable alias.

No completed or interrupted post-creation path can falsely claim clean residue
while hiding the exact created handle.

### Semantic body, counters, and completeness

The V4, V5, and fixed V7 downstream semantic bodies, from the first navigation
counter through the PASS result assignment, remain byte-identical after
normalizing only the PASS label: `6798` bytes, SHA-256
`FCA4B89585E2E34115A432EB3348A8A5175292653AE062EE5AC180742DAF6609`.

The exact public URL, unique search/result binding, paginator/busy/row/total
completeness proof, initial-empty filter, exact query echo/value, terminal-zero
filtered result, one semantic Create control, zero token-name/row matches,
sanitized error class, and exact success counters are unchanged. The executable
counts the Create control but performs no click or provider-persistent
Create/edit/delete.

### Secrets, confirmations, and V4 detach ordering

The executable contains no Bearer value, OpenAI-style key, JWT form, 40-hex
secret, clipboard access, screenshot, click, press, or secret-output field. Its
single terminal does not emit the tab object/ID, URL, title, DOM/page content,
credential, exception message, or response body.

Exact semantic PASS completes the V4 binding before V4 prestart may run once.
A completed V7 non-PASS leaves the V4 binding null/ineligible and permits no V4
detach. A later prestart/pre-Create failure after PASS permits only the exact
V4 pre-Create zero-browser-call detach. The V4 post-native detach remains
reserved for the user's later native generated-page close report.

The mandatory combined final Create, user-native semantic Copy, and
user-native masked Paste confirmation remains withheld. Later deletion of the
exact created row retains its own separate mandatory confirmation. Standing
unattended authority waives neither checkpoint.

## Findings by severity

- Critical: none.
- HIGH: none.
- IMPORTANT: none.
- Minor: none.

## Residual limits

- This review proves only the committed static fix. It does not prove current
  browser/runtime/provider/VM/DNS/process/credential/action-time state or
  consume the V7 gate.
- A separately committed non-self-referential classification, post-commit
  coordinator tuple, and every action-time pin remain mandatory before any
  live call could be eligible.
- Static PASS is not live execution authority.

## Final verdict

**PASS**

The sole prior HIGH finding is closed. Unresolved findings: Critical `0`, HIGH
`0`, IMPORTANT `0`, Minor `0`.

`authorizes_live_execution=false`
