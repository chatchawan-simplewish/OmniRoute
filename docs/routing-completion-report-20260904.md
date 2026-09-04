# OmniRoute routing completion candidate

Updated 20260904 180745 Asia/Bangkok. Product owner: routing_completion_specialist
(fresh Sol High following the prior implementer's explicit release). Checkout:
`C:/ChatGPT Projects/SW-Selfhosted-Network/.worktrees/omniroute-routing-completion`.
Starting commit: `914b3e8d1ae6cc794e080e9ec90c782ea3f730db`.

## Scoped residual-finding correction — F1-F3

Following independent review of `90f439b30a7196d1d8dc1642b0694ef98a3e8ec4`,
only the following residual fixes and directly affected regressions were added:

- F1: the absolute monotonic deadline is checked after authorization and before
  claiming/entering admission, around slot acquisition, at actual slot/generation
  prefetch, at submission, and when accepting either a callback or a returned
  response. An expired callback cannot clear a queued timer and gain acceptance.
  The timer remains the asynchronous cancellation mechanism; synchronous budget
  checks do not depend on timer scheduling. Cancellation and settlement precede
  fallback, and unaccepted expiry costs zero attempts.
- F2: supported Responses JSON and terminal SSE must explicitly report
  `status=completed`, with no error or incomplete details. Missing, incomplete,
  failed, queued, cancelled and in-progress states fail closed. Completed
  Responses text/tool envelopes and legitimate Chat envelopes remain accepted.
- F3: normal/high final Chinese stages scan the existing ordered cheap/strong
  pools past pre-admission ineligible entries. The first admitted Chinese
  candidate consumes the entire final-stage candidate allowance; HTTP failure
  or reviewer REVISE does not cause another Chinese producer call. Reviewer
  selection remains independent and ordered. No-eligible-candidate still blocks.

Exactly three added regression tests were first run against the rejected bytes:
**0 passed, 3 failed**, reproducing each finding. After the fixes, the bounded
command below ran those three tests plus five directly related controller/native
checks: **8 passed, 0 failed**, exit0, 12.678 seconds at 20260904 180723 Bangkok.
The real native five-second case completed in5.428 seconds, with cancellation,
zero Q6 charge and settled-before-Bell behavior preserved. Unrelated catalog,
event, DB and logging suites were not rerun for this residual-fix round.

```powershell
& 'C:/Users/chatc/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe' --import file:///C:/ChatGPT%20Projects/SW-Selfhosted-Network/.worktrees/omniroute-routing-completion/node_modules/tsx/dist/loader.mjs --import ./tests/_setup/isolateDataDir.ts --test --test-name-pattern='review F[123]|admission cancellation|semantic Chat|real Chat and Responses|public streaming endpoints|native five-second' tests/unit/services/agent-route.test.ts tests/integration/agent-route-api.test.ts
```

The independent reviewer also checked the preceding candidate against pristine
pre-feature base `6449695dd985045a0120e3246402296e62a967c6`:730 baseline,728 current,
0 introduced diagnostics, exit0. This strengthens the historical attribution
below but is not a clean build claim. Event wire, key permissions, role bindings,
client ownership and all live/build/deployment gates remain unchanged. Return
this descendant for **re-review of F1-F3 only** before B1; no broad re-review or
live action is implied.

Residual-round native-root type comparison against
`90f439b30a7196d1d8dc1642b0694ef98a3e8ec4` also completed with exit0:
**728 baseline,728 current,0 introduced diagnostics**. The exact command was:

```powershell
& 'C:/Users/chatc/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe' scripts/check-agent-route-type-delta.mjs 90f439b30a7196d1d8dc1642b0694ef98a3e8ec4
```

## Status and authority

Corrected offline candidate ready for the coordinator's one independent scoped
R1-R10 re-review. This is not deployment, live acceptance, or independent PASS.
No dependency install, provider request, credential access/change, VM action,
image build, live database access, or deployment was performed by this lane.
Network responses in native integration tests are in-memory synthetic fixtures.

The earlier report and partial migration were preserved as history in Git and
superseded here. Earlier claims of 29 tests and a clean broad TypeScript check
must not be used: those claims were not reliable acceptance evidence.

## Findings addressed

| Finding | Production correction and direct evidence |
| --- | --- |
| R1 | Behavioral controller cases replace placeholders; both actual public Chat and Responses endpoint modules dispatch through `handleChat`, credential selection, native executor, core response conversion, and SQLite. Tests assert outputs, exact upstream identities, counts, state, errors, and absence of retained payload. |
| R2 | Bell is inserted only after normal Q6 full/offline admission. Technical/objective/reviewer REVISE allows one feedback-bearing free repair; repaired output receives a new independent review. BLOCKED stops. Technical/malformed reviewer output tries the next eligible independent reviewer. Counters charge admitted attempts, not selections. |
| R3 | One monotonic five-second local admission deadline spans authorization/precheck/native dispatch. A two-slot, zero-queue semaphore and fresh same-origin `/slots` check precede generation. Native HTTP uses the same abort signal; upstream local SSE exposes acceptance before generation completion. Full/deadline before acceptance costs zero attempts; submission failures after dispatch remain charged. Cancellation and complete response consumption settle before releasing the dispatch claim or selecting another target. A real-handler five-second fixture proves cancellation, zero charge, then Bell after settlement. Physical overlap remains a live gate. |
| R4 | Private request-scoped controlled dispatch retains native key/quota/circuit checks but pins model and connection. It disables enclosing cooldown retries, account rotation, emergency/family/context/empty-content fallback, proxy-executor substitution, model mutation, cache substitution, plugins, hosted tools, background redirects, and memory/skill injection. Native executor and actual HTTP-fetch guards reject second execution/fetch and identity drift. Ordinary callers retain their existing paths. Native HTTP402 fixture proves one generation and no hidden reroute. |
| R5 | The routing adapter validates raw weekly values without display-parser zero defaults, rejects missing/malformed/nonweekly/reached-limit evidence, returns a distinct evidence ID and exact connection ID, and bypasses cache. Every provider=`codex` target (including another pool object) is gated; reused IDs, mismatched account, >=80%, stale/future and missing evidence fail closed. The exact active connection is authorized/resolved before token refresh/evidence, and freshness/account is checked again immediately before HTTP dispatch. Existing native session-quota enforcement remains. |
| R6 | Explicit `agent:route` harness scope plus no-log, alias permission, concrete provider/model permission and connection/quota allowlists are required. Exact hard pin bypasses affinity substitution, not permission checks. Synthetic no-auth selection is rejected. Native tests cover a restricted key, missing reviewer permission, conflicting affinity, and synthetic no-auth. |
| R7 | Strict validated objective extension is stripped upstream. Chat JSON/SSE and Responses JSON/SSE are decoded semantically; incomplete/malformed envelopes cannot pass as nonempty wire bytes. Supported JSON types/enums/additional-properties, exact tool names, evidence hashes, duplicate/unknown checks are validated. Unimplemented policy IDs fail closed at request validation. Review uses isolated fresh Chat messages without original tools/input; only strict structured verdict/findings are accepted, never a PASS substring. |
| R8 | Exact HTTP409 `error.code=agent_route_resume_required`. Canonical `(key,task)` owns one stable run; child turns have independently unique turn and idempotency IDs. New tuple after terminal prior turn is accepted; every exact/reused tuple is rejected. Run risk is monotonic. Binding/reviewer readiness validation precedes creation. Public keepalive wrappers do not convert controlled failures to HTTP200. |
| R9 | Run/turn admission, dispatch claims, lifecycle events+latches, and output release are transactional with a SQLite write reservation before state reads. Full key/task/run/turn/idempotency ownership is checked. One active/stopping child turn per run; late events strengthen only their old turn. Latches cancel in-flight I/O and prohibit further attempts; dispatch claim clears only after I/O settles. Output latch commits before response release; terminal state is set on body consumption/cancel/failure. Orphaned active claims remain fail-closed; there is no timer-based unsafe reclaim. Tests include rollback on interrupted latch update. |
| R10 | Fixed metadata columns receive actual dispatch/admission/busy-slot/processing/latency/token/objective/reviewer/subscription decisions and counters. Responses include task/run/turn/virtual route/resolved provider+model/candidate-attempt/reviewer-verdict/fallback headers. Private logger suppression, disabled content hooks/caches, no-log attempt bodies/errors/warnings, and sanitized provider error persistence prevent candidate/reviewer payload retention. Native tests inspect every SQLite table and captured console sinks; provider-error echo fixture also checks every table. |

## Explicit binding and permission contract delta

`OMNIROUTE_AGENT_ROUTE_BINDINGS_JSON` keeps `vm1201`, `bellPc`, ordered
three-entry `free`, ordered `cheapChineseReviewers`, and ordered
`strongChineseReviewers`. It now requires two explicit Codex role objects:

```json
{
  "codexNormal": { "provider": "codex", "model": "gpt-5.6-terra", "reasoningEffort": "medium", "connectionId": "REVIEWED_ACCOUNT_ID" },
  "codex": { "provider": "codex", "model": "gpt-5.6-sol", "reasoningEffort": "high", "connectionId": "REVIEWED_ACCOUNT_ID" }
}
```

This is a partial illustration, not a complete runnable binding. Missing or
ambiguous single-Codex configurations fail closed; they are not silently
flattened. Both roles must use the same explicitly approved account. This
implements the accepted binding-selection review; no actual model inventory or
live binding was inferred or changed here. Normal candidate uses Terra-medium;
high candidate and high-risk reviewer use Sol-high. A normal alias with a stored
high-risk floor also receives Sol-high review, else ordered strong Chinese;
Terra is never an automatic high-risk reviewer. Independence uses concrete
model identity across provider/account/effort aliases. Every Codex dispatch has
its own fresh exact-account evidence.

The dedicated harness key must have `noLog=true`, scope `agent:route`, both slash
aliases as appropriate, exact permitted resolved provider/model names, and the
reviewed connection allowlist (plus any intended quota restrictions). Existing
hyphen aliases and a no-log flag alone do not grant policy/paid access. Public
team keys must not receive this scope or paid permissions by implication.

Controlled Codex transport is HTTP/SSE; an explicitly configured Codex WebSocket
connection is ineligible rather than silently entering an unguarded transport.
Provider proxy-executor substitution is not part of the controlled ladder.

Migration134 is rewritten before deployment to create canonical runs, child
turns and metadata events. Coordinator evidence says live schema is133 with no
agent_route tables. An installation that already applied a different134 must
not use this migration as an in-place upgrade; it needs separately reviewed
schema reconciliation. No destructive or automatic repair is included.

## Lifecycle wire and client compatibility

`POST /v1/agent-routes/events`: bearer same owning no-log key; four matching
`x-omniroute-{task-id,run-id,turn-id,idempotency-key}` headers; strict body:
`event_id`, `task_id`, `run_id`, `turn_id`, `idempotency_key` (UUID strings),
`kind` (`output_started` or `tool_started`), and `occurred_at` (ISO UTC datetime).
Acknowledgement is HTTP202 with `{"accepted":true}`. Identical event replay is
idempotent; event-ID conflict is409; foreign identity is403. No query or
secondary credentials are accepted. Clients await the authenticated ack before
side effects. Old terminal events cannot latch a newer child turn.

The approved original Hermes client reused one tuple across its internal tool
loop. That is not compatible with the corrected replay guard. The separate
client lane is implementing fresh persisted per-logical-step turn+idempotency
IDs after prior accepted response and committed tool results, keeping stable
run/task/risk and frozen IDs across retries. No server replay relaxation was
made. Combined live/native harness workflow acceptance is still required.

## Reproducible verification

Run in PowerShell from the assigned checkout; existing bundled Node and tsx only:

```powershell
& 'C:/Users/chatc/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe' --import file:///C:/ChatGPT%20Projects/SW-Selfhosted-Network/.worktrees/omniroute-routing-completion/node_modules/tsx/dist/loader.mjs --import ./tests/_setup/isolateDataDir.ts --test tests/unit/services/agent-route.test.ts tests/unit/db/agent-route-runs.test.ts tests/unit/api/agent-route-events.test.ts tests/unit/api/models-agent-route-aliases.test.ts tests/integration/agent-route-api.test.ts tests/unit/chatcore-attempt-logging.test.ts
```

Latest corrected candidate result at 20260904 175135 Bangkok: exit0, **32 passed,
0 failed, 0 cancelled/skipped**, 16.018 seconds. Native deadline case took
5.445 seconds and verified the cancelled Q6 consumed no candidate before Bell.
The four ordinary attempt-logging cases pass unchanged. Earlier intermediate
failures led to native deadline/fixture-account-state corrections; only this
final candidate result is the acceptance receipt.

```powershell
& 'C:/Users/chatc/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe' scripts/check-agent-route-type-delta.mjs 914b3e8d1ae6cc794e080e9ec90c782ea3f730db
```

Result exit0: **731 baseline diagnostics, 728 current diagnostics, 0 introduced
diagnostics**. This read-only script compiles all19 named changed/native/test
roots and their dependency graph from `tsconfig.typecheck-agent-route.json`,
then repeats with exact starting-commit bytes in an in-memory compiler host.
It compares complete messages, source expressions, error codes and counts;
only two equivalent displayed union-order variations are canonicalized.
It does not suppress newly introduced diagnostics or mutate the worktree.

This is a passing diagnostic-delta check, **not a clean TypeScript build**.
The expanded native graph still has728 attributable baseline errors; direct
`tsc -p tsconfig.typecheck-agent-route.json` is not green. Earlier broad `tsc`
also failed; its entire repository-wide error set was not independently
classified. The narrower pre-existing core check alone is not claimed to cover
native seams. Production image build remains the separate build owner's gate.
`git diff --check` exits0.

## Remaining gates

- One independent scoped code/security/specification re-review of this candidate.
- Corrected client commits and exact deployed/imported runtime identity receipts.
- Reviewed real bindings and least-privilege harness permission configuration.
- Actual private connectivity/authentication, exact-account live quota evidence,
  VM1201 three-overlap admission with correlated busy/deferred/token-rate/latency
  metrics, Bell current health, and normal/high multi-step workflows per harness.
- Separate reviewed image build, migration/restore/rollback and deployment gates.

No server-side timeout unlock, synthetic quota evidence, paid test dispatch,
permission broadening, or fallback outside the reviewed ladder was used to
remove those gates. Keep this feature disabled until the coordinator accepts
the independent review and subsequent live/deployment contracts.
