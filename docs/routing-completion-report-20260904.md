# OmniRoute routing completion report

## Changed paths

- `open-sse/services/agentRoute.ts`: deterministic alias ladder, strict fresh
  subscription evidence validation, buffered candidate handling, objective gates,
  reviewer independence, repair dispatch, and native dispatch boundary.
- `src/sse/handlers/chat.ts`: intercepts only `agent/normal` and `agent/high`
  after existing authentication, policy, guardrails, hooks, and session checks;
  each dispatch uses the existing `handleSingleModelChat` pipeline with a forced
  binding connection and `skipUpstreamRetry: true`.
- Existing baseline paths retain the no-log event route, metadata-only SQLite
  ledger, migration, model discovery, and provider-live Codex evidence adapter.

## Verified offline

`C:\Users\chatc\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe --import file:///C:/ChatGPT%20Projects/SW-Selfhosted-Network/.worktrees/omniroute-routing-completion/node_modules/tsx/dist/loader.mjs --import ./tests/_setup/isolateDataDir.ts --test tests/unit/services/agent-route.test.ts tests/unit/db/agent-route-runs.test.ts tests/unit/api/agent-route-events.test.ts tests/unit/api/models-agent-route-aliases.test.ts`

Result: 29 passed, 0 failed. Coverage includes slash alias catalog authorization,
no-log lifecycle authorization and payload rejection, idempotent/latching run
storage, objective checks, fresh 79/80 boundary validation, and native-controller
dispatch ordering. `node node_modules/typescript/bin/tsc --noEmit --pretty false
--incremental false` also completed successfully.

## Remaining live requirements

No provider, credential, VM, deployment, or live paid request was made. Live
enablement still requires reviewed bindings, provider-live Codex evidence for
each routing/reviewer decision, physical local admission evidence, and the
separate deployment/acceptance owner gate. The feature remains inert unless the
exact bindings environment setting is supplied and callers use authorized no-log
keys with the UUID protocol.

## Review round 1 status

R1 placeholder tests were removed and replaced with behavioral controller/objective
tests. R2 capacity-versus-quality Bell-PC routing, R5 strict raw weekly evidence,
R7 objective enforcement and strict reviewer verdict decoding, R8 machine-readable
resume errors, R9 transactional event latching/identity verification, and Docker
context exclusion were corrected. R3/R4/R6/R10 still need a second implementation
round for native admission cancellation, controlled-handler no-fallback mode, exact
pre-dispatch account authorization, and persistent per-attempt metadata. This branch
is not ready for deployment or enablement.
