# Task 1: Port the accepted routing controller to the current source baseline

Ownership: implementer exclusively owns `.worktrees/omniroute-auto-switch-runtime-20260912`, branch `codex/omniroute-auto-switch-runtime-20260912`; baseline `820ead300f0c03e17a87fbaa7e22e81d72faeeeb` (3.8.50 plus audit fix). Other tasks/worktrees are active. Never modify another worktree or revert others' edits. No live service, database, provider, credential, SSH or browser action.

## Requirements

Reuse accepted source `.worktrees/omniroute-routing-completion`, original base `6449695dd985045a0120e3246402296e62a967c6`, accepted controller tip `d39ec5a4471d88d821576a3830fa55da4e2b027b`. Port its routing-only changes; do not import historical reports, build/TLS fixes, or old dashboard files. Root approved spec `docs/superpowers/specs/2026-08-29-omniroute-agent-routing-design.md` and corrections summarized in the coordinator worktree `docs/auto-switch-20260912-plan.md` control behavior. Read both before edits.

The controller, server API, auth/model/connection authorization, durable run/turn claims, objective checks, quota gate and tests were accepted together. Preserve all those guarantees. Map old localDb exports to current modular DB architecture; assign a non-colliding migration number using existing migration conventions. Keep the baseline audit fix and all newer provider/auth/retry code. Do not add new dependencies.

Known direct-patch conflicts: executors/base.ts, chatCore.ts, Chat/Responses routes, provider DB, chat handler, auth; localDb.ts and two old test paths no longer exist. Resolve semantically, not by replacing new files with old ones.

## Verification and evidence

Read current AGENTS.md and follow minimum focused test preference from project root. Establish focused RED/acceptance checks and run the ported routing tests (node --test and existing Vitest as applicable). Install locked dependencies only in assigned worktree if needed. Do not run the full suite or broad build. Existing accepted tests: tests/unit/services/agent-route.test.ts and tests/integration/agent-route-api.test.ts; discover related routing authorization/DB/API tests from the source delta. Report specific failures and fix them before completion.

Commit only exact intended paths with command-scoped Git identity. Write `docs/auto-switch-runtime-port-report-20260912.md` in your own worktree: baseline/tip, exact changed paths, preserved behavior, focused test results and remaining deployment limits. Return at most five lines: status, commit, test summary, report path, unresolved issues. Do not claim live acceptance.
