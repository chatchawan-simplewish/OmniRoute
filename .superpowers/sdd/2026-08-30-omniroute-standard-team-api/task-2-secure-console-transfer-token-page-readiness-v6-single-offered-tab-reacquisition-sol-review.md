# OmniRoute V6 single-offered-tab reacquisition — independent Sol High review

Date: `2026-09-01` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only committed V6 brief
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-token-page-readiness-v6-single-offered-tab-reacquisition-brief.md`
at commit `7050edd5b3ca22b22a42a48efeb4db4ef79e1e1d` against the immutable V5
incident and the pinned V5/V4 static chain named below.

I performed direct-byte, Git ancestry, syntax, call-surface, predecessor-state,
semantic-equivalence, failure-state, secret-surface, confirmation, and detach-
ordering checks. I performed no Chrome, browser, provider, clipboard,
credential, process, network, routing, Prox-01, or VM1205 action and did not
execute the V6 cell against any live runtime.

This review is a static security/specification verdict. It does not classify
V6 for execution, consume V6, or authorize any live action.

## Git and direct-byte pins

- Reviewed commit: `7050edd5b3ca22b22a42a48efeb4db4ef79e1e1d`.
- Direct parent: immutable V5 incident commit
  `00ec3dc60c6ffa8aa27e2a161c52aee5fd52c031`.
- The reviewed commit adds exactly one path: the V6 brief named above.
- Current reviewed HEAD equals the V6 commit.
- Index before review: `0` paths.
- Inherited dirty baseline before review: exactly the expected twelve records,
  comprising five modified and seven untracked source paths.
- V6 brief: `18232` bytes, SHA-256
  `70A01F594B443EB003CD0F5FEDF233E99658773EABAECE41CAF132F6BBD7616B`,
  Git blob `13981e01e931fbaafbe6b1fba7f0ea5cdb38243c`.
- V6 brief encoding: strict UTF-8 without BOM, zero CR bytes, LF-only, and
  exactly one trailing LF.
- V5 incident: `1957` bytes, SHA-256
  `92060BED25210DBBCA085FF1870F5D2537E2B55592B690CC086F0BA288B6D4E9`,
  Git blob `305eb2d077a3e98857ae453665ae32d8aa82f1e7`.

The immutable predecessor chain and direct working bytes reproduce:

| Artifact | Commit | Bytes | SHA-256 | Git blob |
| --- | --- | ---: | --- | --- |
| V5 brief | `8aaa90a22720d7f59928939959fc3ebf82bb39e7` | `25818` | `1C1F75635538E87B0FDE6D7F853A77A1405456C2FFF53D7D30B5F56DC121E3CC` | `44d4606f22b4fbd630f275ba39d82b93d94ca54b` |
| V5 Sol High review | `50e0bfb350e294d089b6b9674628edb7ec63b5f1` | `8959` | `EF7ADB9C240B92E334972FC057BBB21A1C5C9242FAEC9E362D542512F972F7F8` | `5e0db7d8293662b906addc4c6e40fed8d5fcabf9` |
| V5 classification | `bbf67701b165940eed49e771ab29a258cd012c37` | `6773` | `2275EA1F6524A2192C960907907643DBE310796C389F7F862C0E41417577EAF9` | `34891f406f0b1ff337b57fb338be42d3d7c4811a` |
| V4 brief | `82971f2d7165325b616dab293e275cb7287d1914` | `54334` | `89E52D8157677821FC44E84CFCABFC4AEB01A1F9CF23D0DDBCD31E56085B8EE8` | `fdc290ab1d08b8a6a8bd22b440b6c0fd0e385364` |
| V4 Sol High review | `7e2bf2341d88113536507298b3df8f1f25e8f417` | `7813` | `547449928E647AE5E229A4ECAEEF4BFD9473410F494BE1B88E0197F9FD7ACADB` | `9fb318b385a5b2f8349c110631cdeeff37f2c63c` |

The V5 incident directly descends from the V5 classification, and V6 directly
descends from the incident. `git diff --check` for incident-to-V6 passes.

## Executable fence and syntax

The V6 brief contains exactly one `javascript` fence. Its executable content,
including the final LF, reproduces exactly:

- bytes: `12381`;
- SHA-256:
  `CEC306737C33AC561428579671AA44BDB766C45A41B6AAE1A43FAD884CD2693D`;
- asynchronous JavaScript syntax: **PASS**.

The syntax check parsed the cell inside an async wrapper without executing the
cell, importing a runtime, or contacting a browser.

## Acquisition surface and one-shot state

Direct executable-code cardinality is:

- `secureConsoleChromeV5.tabs.list()`: exactly `1` call;
- `secureConsoleChromeV5.tabs.selected()`: `0`;
- `secureConsoleAgentV5.browsers.get("chrome")`: `0`;
- browser bootstrap/setup: `0`;
- `browsers.list`, `getDefault`, `getForUrl`, `tabs.get`, `tabs.new`,
  `openTabs`, `claimTab`, reconnect, retry, and fallback surfaces: `0` each;
- click, press, close, screenshot, clipboard, keyboard, observer, listener,
  timer, storage, cookie, and persistence surfaces: `0` each.

V6 declares a fresh task-local gate and sets
`secureConsoleV6ListReacquisitionConsumed=true` before any declaration,
predecessor, list, cardinality, or semantic operation can fail. A timeout,
rejection, truncation, malformed output, or uncertainty therefore cannot leave
the reviewed V6 gate fresh. The contract explicitly forbids retry,
continuation, reinterpretation, fallback, or verdict relaxation.

## Exact V5 failure predecessor

The immutable incident records:

- V5 Call 1 exact attachment/documentation PASS, `1/1` for both operations;
- V5 Call 2 selected attempted/fulfilled `1/1`;
- controller ownership false and tab shape false;
- navigation, URL, readiness, fill, Create, token-name, and row calls all zero;
- consumed true;
- V4 binding null, ineligible, and state
  `V5_REACQUISITION_OR_READINESS_FAILED`;
- both V4 detach cells and V4 prestart unconsumed;
- no navigation, provider, credential, clipboard, process, routing, VM, or
  Cloudflare-persistent action.

Before the sole `tabs.list()` call, V6 requires the retained, observable
counter/state projection of that exact incident:

- fresh V6 gate;
- V5 attachment consumed and exact;
- V5 connect and complete-documentation counters each `1/1`;
- V5 connected shape true and attachment error `NONE`;
- V5 adoption consumed;
- V4 binding null/ineligible with exact V5 failure state;
- pre-Create detach, post-native detach, and V4 prestart all unconsumed.

Any mismatch throws before `list()` and still consumes V6. The immutable
incident supplies the terminal counters that were invocation-local in V5; the
V6 cell checks every retained predecessor value available in the same
persistent session. Action-time commit/state pins remain mandatory.

## Exact-one cardinality and controller/tab shape

The list result is accepted only when it is an array of length exactly one.
Non-array, zero, two, or more results fail before selecting or navigating any
element. The only accepted element is `offeredTabs[0]`; no code chooses among
multiple tabs.

That sole object must be non-null with a string controller ID and callable
`goto`, `url`, `playwright.getByRole`, and `playwright.getByText` members.
Malformed shape fails before navigation. No tab ID, URL, title, profile,
window, DOM, page content, or selector result is emitted.

## V5/V4 semantic equivalence and completeness

I extracted the V4, V5, and V6 downstream semantic bodies from the first
`counters.navigationAttempted++` through the respective PASS result
assignment. After normalizing only the result label, all three bodies are
byte-identical: `6798` bytes, SHA-256
`FCA4B89585E2E34115A432EB3348A8A5175292653AE062EE5AC180742DAF6609`.

Therefore V6 preserves the reviewed title-free signature and completeness
rules unchanged:

- exact public Cloudflare token URL;
- unique token-search textbox and validated `aria-controls` result region;
- unique paginator and visible readiness wait;
- initial filter empty;
- initial state either exact terminal zero or a complete nonempty page with
  consistent rows/total, status, busy state, and paginator controls;
- exact query echo/value and exact terminal-zero filtered result;
- exactly one semantic Create control, zero exact token-name matches, and zero
  matching rows;
- readiness `3/3`, fill `1/1`, and all fixed navigation/URL/Create/name/row
  counters exact in the required PASS terminal.

The executable counts the Create button/link only; it performs no click or
Create/edit/delete action.

## Failure, no-residue, and binding disposition

Every completed non-PASS leaves V6 consumed, writes one fixed redacted
terminal, and sets the V4-compatible binding to null, ineligible, and exact
state `V6_LIST_REACQUISITION_OR_READINESS_FAILED`. V6 creates no tab, so a V6
failure has no created-tab residue and permits no detach call or cleanup reuse.
Missing or uncertain output is not evidence of success or cleanup and cannot
be retried.

Exact success alone retains the offered tab under the V4-compatible binding
with state `TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE`. The unchanged V4 prestart cell
is then the sole permitted next browser cell, once, in the same session.

## Secrets, confirmations, and V4 detach ordering

The executable contains no Bearer value, OpenAI-style key, JWT form, 40-hex
secret, clipboard access, or secret-shaped literal. Its single output contains
only fixed labels, booleans, numeric counters/counts, sanitized error class,
and binding state. It does not emit the offered array, tab object/ID, URL,
title, page content, DOM, selector content, credential, exception message, or
response body.

The fixed downstream order preserves the reviewed boundaries:

1. exact V6 PASS permits the unchanged V4 prestart cell once;
2. a V6 non-PASS leaves no eligible binding and permits neither detach cell;
3. a proven V4 prestart/pre-Create failure after V6 PASS permits only the
   exact V4 pre-Create zero-browser-call detach once, then stop;
4. only after prestart and the inherited credential-free preparation path pass
   does the owner stop for the mandatory combined final Create, user-native
   semantic Copy, and user-native masked Paste confirmation;
5. only after the user's native generated-page close report may the exact V4
   post-native zero-browser-call detach run once;
6. later deletion of the exact created row retains its own separate mandatory
   confirmation.

The directly reproduced V4 prestart, pre-Create detach, and post-native detach
blocks remain `20437`, `2309`, and `2305` bytes with SHA-256 values
`FAB457F36F3AEA9EFF89716DD28C30751B2F7607683E31CCCBA4D7F9C4A6AEBB`,
`60692947118FCD2CA765B8C7C850490B79B9ED3C0D3942D14CB5F429F924746D`,
and `5ABC144ABA9866294EC4A7746906E3D3132ADAE993B93969C426295085FE102D`.
Standing unattended authority does not waive either manual confirmation.

## Findings by severity

- Critical: none.
- HIGH: none.
- IMPORTANT: none.
- Minor: none.

## Residual limits

- This review proves only the committed static V6 contract. It does not prove
  current Chrome/profile/window/tab isolation, current runtime bytes, offered-
  tab cardinality/shape, provider state, Prox-01/VM1205 state, DNS,
  credentials, process ownership, routing, or action-time Git/projection pins.
- The brief records a user visual-isolation confirmation, but execution still
  requires that confirmation and every other pin to revalidate at action time
  in the sole owner task.
- Static review and any later classification remain non-execution artifacts.
  V6 is not eligible until a committed non-self-referential classification,
  separate post-commit tuple, and all action-time conditions pass.

## Final verdict

**PASS**

The committed V6 single-offered-tab contract has no unresolved Critical,
HIGH, or IMPORTANT finding. It is a supported one-shot replacement for only
the failed V5 selected-tab reacquisition boundary while preserving the V5/V4
semantic, completeness, no-retry, no-residue, secret, confirmation, and detach
constraints.

`authorizes_live_execution=false`
