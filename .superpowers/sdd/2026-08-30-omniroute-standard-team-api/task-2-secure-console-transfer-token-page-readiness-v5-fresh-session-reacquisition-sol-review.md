# OmniRoute V5 fresh-session reacquisition — independent Sol High review

Date: `2026-09-01` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only the committed V5 offline contract at
`8aaa90a22720d7f59928939959fc3ebf82bb39e7`. V3 remains consumed and failed;
V4 remains static evidence only. I performed no Chrome, tab, provider,
clipboard, credential, process, network, routing, Prox-01, or VM1205 action.
The mocked checks used local JavaScript objects only and never loaded the
installed browser runtime.

This PASS is a static security-contract verdict. It does not classify V5 for
execution, consume either V5 call, or authorize any live action.

## Git and byte pins

- Reviewed HEAD: `8aaa90a22720d7f59928939959fc3ebf82bb39e7`.
- Direct parent: `a32c53c2d5fba3940e44af691bcd8feae75d1681`.
- The reviewed commit adds only the V5 brief path.
- Index before review: `0` paths.
- Inherited dirty baseline: exactly the expected 12 porcelain records:
  five modified paths (`open-sse/services/codexQuotaFetcher.ts`,
  `src/app/api/v1/models/catalog.ts`, `src/lib/localDb.ts`,
  `tests/unit/api/models-agent-route-aliases.test.ts`, and
  `tests/unit/services/agent-route.test.ts`) and seven untracked paths
  (`open-sse/services/agentRoute.ts`,
  `open-sse/services/agentRouteObjectives.ts`,
  `src/app/api/v1/agent-routes/`, `src/lib/db/agentRouteRuns.ts`,
  `src/lib/db/migrations/134_agent_route_runs.sql`,
  `tests/unit/api/agent-route-events.test.ts`, and
  `tests/unit/db/agent-route-runs.test.ts`).

The exact committed inputs reproduce:

| Input | Commit | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| V3 title incident | `172da50d2b841398c6e4c1d55942e3f6a75d38eb` | `5104` | `E57C82BA099832C4FFD2EB096CE7439288F8688E75C19D1A0F29AA1BA6FD1CFD` |
| V4 replacement brief | `82971f2d7165325b616dab293e275cb7287d1914` | `54334` | `89E52D8157677821FC44E84CFCABFC4AEB01A1F9CF23D0DDBCD31E56085B8EE8` |
| V4 Sol High review | `7e2bf2341d88113536507298b3df8f1f25e8f417` | `7813` | `547449928E647AE5E229A4ECAEEF4BFD9473410F494BE1B88E0197F9FD7ACADB` |
| Inherited live brief | `7af3ab75ec87d81d75811ff8f2e9b4fa9d0c3e3b` | `62054` | `995CA4D59E564EAF53417B9F577808F9C307C5CDEE93FB8E91DC73A5211F52CC` |

## Direct-byte checks

The V5 brief is exactly `25818` bytes, SHA-256
`1C1F75635538E87B0FDE6D7F853A77A1405456C2FFF53D7D30B5F56DC121E3CC`,
and Git blob `44d4606f22b4fbd630f275ba39d82b93d94ca54b`. It is strict UTF-8 without
BOM, contains zero CR bytes, uses LF-only line endings, and has exactly one
trailing LF. It contains exactly two `javascript` fences:

| Cell | Bytes | SHA-256 | Parse |
| --- | ---: | --- | --- |
| Call 1 | `2654` | `652634636A35305170906233FD5DF953F51D2527CAE22273CAE493A7AD3A67C3` | PASS |
| Call 2 | `11823` | `971471ADD6EF543B7C0D68E1ACC76B851EF9A34A4E39D676C9A82028E8547912` | PASS |

Both direct extracted cells parse through Node.js as async JavaScript without
executing the installed runtime.

## JavaScript syntax and mocked scenarios

The bounded harness replaced only Call 1's pinned dynamic-import statement
with an in-memory setup function. Call 2 ran unchanged after that shimmed Call
1 in the same async lexical session. No browser or external API was loaded.

- Call 1 success: exact PASS, consumed true, connect `1/1`, documentation
  `1/1`, connected shape true, error `NONE`.
- Call 1 attachment failure: exact STOP, consumed true, connect `1/0`,
  documentation `0/0`, fixed redacted failure class.
- Call 1 documentation failure: exact STOP, consumed true, connect `1/1`,
  documentation `1/0`, fixed redacted failure class.
- Call 2 success: exact PASS; selection/navigation/URL/Create/name/row `1/1`;
  readiness `3/3`; fill `1/1`; write `1`; zero name/row matches; binding
  eligible and non-null in `TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE`.
- Call 2 no-selected-tab and malformed-tab: non-PASS, consumed true,
  selection `1/1`, no navigation, binding null/ineligible in the exact failure
  state.
- Call 2 navigation failure: non-PASS, navigation `1/0`, binding
  null/ineligible.
- Call 2 initial-filter failure and baseline-incomplete failure: non-PASS at
  readiness `1/1`, fill `0/0`, binding null/ineligible.
- Call 2 query-echo failure: non-PASS at readiness `2/1`, fill `1/1`, binding
  null/ineligible.
- Call 2 semantic mismatch: non-PASS after readiness `3/3` and fill `1/1`,
  binding null/ineligible.
- Invalid exception-name fixture: non-PASS with only the fixed safe class
  `TokenPageSemanticReadinessError` emitted.

Every completed Call 2 failure emitted write `1`, consumed true,
`bindingEligible=false`, `bindingNull=true`, and exact state
`V5_REACQUISITION_OR_READINESS_FAILED`.

## Forbidden and required surface counts

Direct executable-code cardinality is:

- pinned runtime import `1`; setup call `1`;
  `secureConsoleAgentV5.browsers.get("chrome")` `1`;
  `secureConsoleChromeV5.tabs.selected()` `1`; fixed navigation `1`;
- `browsers.list`, `getDefault`, `getForUrl`, extension get, `tabs.list`,
  `openTabs`, `claimTab`, `tabs.get`, `tabs.new`, reconnect, close,
  `markHandoff`, screenshot, clipboard, and keyboard surfaces: `0` each;
- `MutationObserver`, event listener, interval, timer, `localStorage`,
  `sessionStorage`, `indexedDB`, `document.cookie`, and async evaluate callback:
  `0` each;
- placeholders: `0`; secret-like Bearer values, Cloudflare token forms,
  OpenAI-style keys, and JWT forms: `0`.

The only evaluation callbacks are bounded synchronous semantic snapshots.
There is no page-resident observer, persistence, helper, timer, or event hook.

## V4 semantic equivalence and retained pins

I extracted both adoption/readiness blocks from direct bytes. For each, the
downstream semantic body begins at the first
`counters.navigationAttempted++;` and ends after the PASS result assignment.
After changing only V5's PASS result label to V4's reviewed result label, the
two bodies are byte-identical: `6798` bytes and SHA-256
`FCA4B89585E2E34115A432EB3348A8A5175292653AE062EE5AC180742DAF6609`.

The retained V4 executable blocks also reproduce directly:

| Retained V4 block | Bytes | SHA-256 |
| --- | ---: | --- |
| Fresh Cloudflare prestart reads | `20437` | `FAB457F36F3AEA9EFF89716DD28C30751B2F7607683E31CCCBA4D7F9C4A6AEBB` |
| Pre-Create detach | `2309` | `60692947118FCD2CA765B8C7C850490B79B9ED3C0D3942D14CB5F429F924746D` |
| Post-native detach | `2305` | `5ABC144ABA9866294EC4A7746906E3D3132ADAE993B93969C426295085FE102D` |

V5 pins these unchanged bytes and forbids downstream source adaptation.

## Constraint preservation

- Semantic page signature: exact public token URL, unique search textbox,
  validated `aria-controls` region, unique paginator, authoritative complete
  baseline, exact query echo/value, terminal empty state, one Create semantic
  control, and zero exact name/row matches all survive byte-for-byte.
- Completeness: initial zero or complete nonempty pagination and final exact
  zero terminal remain required; busy, malformed, partial, or ambiguous state
  fails closed.
- Minimal reacquisition: Call 1 has one pinned bootstrap/get/documentation
  path; Call 2 has one selected-tab acquisition and one navigation/readiness
  path. There is no list, claim, retained-ID get, new tab, fallback, retry, or
  alternate route.
- No residue: no tab is created; every completed Call 2 non-PASS nulls and
  disqualifies the V4-compatible binding. Missing or uncertain output is not
  cleanup evidence and permits no follow-up call.
- No retry: both calls are separately one-shot and consumed by any completed
  failure; timeout, truncation, malformed output, or uncertainty stops the
  contract with no reacquisition, cleanup reuse, handoff, or relaxation.
- Secrets: outputs are fixed redacted metadata; no tab/browser ID, private
  URL, page content, selector content, credential, clipboard bytes, response,
  or exception message is emitted.
- Confirmations and cleanup: the combined final Create/user-native semantic
  Copy/user-native masked Paste confirmation remains mandatory. The later
  exact-row deletion confirmation remains separate and mandatory. Agent page
  or clipboard inspection after Create remains forbidden. Revocation hold,
  invalid-token proof, retained-owner disposition, proxy cleanup, local
  cleanup, and redacted evidence terminals remain inherited without change.

## Findings by severity

- BLOCKING: none.
- HIGH: none.
- IMPORTANT: none.
- LOW: none.

## Residual limits

This review proves only the committed static contract and offline fixtures. It
does not prove current Chrome/profile/tab selection, installed-runtime bytes,
provider state, VM availability, DNS, credentials, or action-time Git state.
Execution remains blocked pending the separately committed non-self-referential
classification, post-commit coordinator tuple, and every action-time pin and
manual confirmation required by V5.

## Final verdict

PASS

`authorizes_live_execution=false`
