# Automatic model switching completion

Owner: Codex task `01a09361-8143-73d3-adb7-15043355276b`.
Source worktree: `.worktrees/omniroute-auto-switch-20260912`.
Baseline: `066a32e9fcb5aa47f73aade21d1a0fbba73cfe4e`.
User instruction: "start implement Full automatic model switching unattended".

## Scope and authority

Reuse the approved `docs/superpowers/specs/2026-08-29-omniroute-agent-routing-design.md` in the project root and subsequent reviewed routing/client corrections. Explicit `agent/normal` and `agent/high` remain the interface. Automatic difficulty classification is not included.

This new source worktree is exclusively owned by the current task. All prior source and rollout worktrees remain read-only; no ownership or spent authority gate is inherited. Independent read-only agents may inspect them. Live-resource ownership, exact targets, preconditions, rollback and sanitized evidence must be documented and independently reviewed before changes. No old D/B/V gate may be consumed or retried. A fresh consuming gate requires its sole Sol High owner. Do not print credentials or read provider credential columns for discovery.

## Global constraints

- Normal: local Q6, then Q4 only for capacity/offline, then three distinct free models with one repair each, eligible subscription, explicit cheap Chinese fallback.
- High: one accepted Q6 xhigh attempt, eligible subscription, explicit strong Chinese fallback; no Q4/free ladder.
- Local admission is at most five seconds; admission failure does not consume a candidate attempt.
- Subscription candidate/reviewer dispatch requires separate fresh provider-live weekly usage evidence, age 0–30000 ms and usage strictly below 80%; unknown evidence skips subscription.
- Independent review and objective checks remain mandatory as specified. No replay after released output or acknowledged side effects; preserve durable run/turn/idempotency lifecycle.
- Authorize every resolved model and connection. No generic auto alias as proof of Chinese selection or reviewer independence.
- Preserve current working provider fixes, client defaults until acceptance, rollback assets and unrelated changes.
- Focused tests only, expanding for a concrete security/integration concern. No artificial Chinese-model capability or spend limits.

## Phase 1 — recover and pin (three tasks)

- [x] Create isolated source worktree from accepted routing baseline.
- [x] Reconcile latest server/client acceptance and spent-gate ownership records.
- [x] Independently review fresh discovery scope and pin live runtime/authentication metadata.

## Phase 2 — complete candidate (three tasks)

- [x] Trace and repair the shared inference authentication path if current evidence confirms a defect.
- [ ] Reconcile accepted controller/client code with the current provider/audit repair runtime; implement only proven gaps.
- [x] Run focused acceptance checks and independent source/security review.

## Phase 3 — qualify and bind (three tasks)

- [x] Prepare/review exact connection/model bindings and fail-closed quota evidence.
- [ ] Qualify eligible providers through the intended inference path under a fresh reviewed contract.
- [ ] Prove the routing matrix on an isolated candidate, including authorization and replay boundaries.

## Phase 4 — activate and finish (three tasks)

- [ ] Review and execute bounded live rollout with rollback under sole Sol High gate ownership.
- [ ] Verify both clients through explicit aliases before changing their defaults.
- [ ] Complete independent final audit and durable evidence/publication handoff.

## Current state

Phase 1: 3/3. Phase 2: 2/3. Phase 3: 1/3. Phase 4: 0/3.
Live switching is NOT PROVEN; no live mutation or inference probe has occurred in this implementation run.
Next: close the Codex app-server attempt-accounting finding, preserve Gemini behavior, and finish the scoped caller credential diagnosis. Live client deployment remains subject to the ownership boundary in `auto-switch-client-ownership-20260912.md`.

## Recovered evidence and current ownership

- Server controller accepted at `d39ec5a4471d88d821576a3830fa55da4e2b027b`; original base `6449695dd985045a0120e3246402296e62a967c6`. Later completion tip `066a32e9f` adds build fixes.
- Hermes `.worktrees/hermes-routing-live-compatible` source `4fdcf6b...`; DeepSeek `.worktrees/deepseek-routing-completion` source `4d2f8dac...`. Both already implement per-step tuple rotation, ACK/redelivery and no hidden routed retries. Do not rewrite accepted client logic.
- Actual remaining integration: deployment, exact slash-alias/connection/key binding, side-by-side Hermes Linux compatibility stage and client normal/high acceptance.
- Old D1-D4 and D6-D8 are spent; D5 is blocked. D9 is obsolete after the host move. Old rollout lane remains read-only under its previous owner.
- Source port assigned to `/root/runtime_port` (Terra Medium) exclusively in `.worktrees/omniroute-auto-switch-runtime-20260912`, baseline `820ead300f0c03e17a87fbaa7e22e81d72faeeeb` (3.8.50 and accepted audit fix). This separate Git worktree is owned by the current task with the subagent as its sole source writer. The coordinator writes only this plan/discovery worktree while that implementation is active.
- No generic cherry-pick: the accepted routing delta conflicts with newer auth, handler and DB architecture. Port behavior without replacing newer files wholesale.
- Discovery review round 1 found excess API-key row metadata and incomplete SSH pins. Both were corrected; script `e53d0e0cd31af70fd6a9511cc8a7fe638ddfb2ffbaba4dc4d6c15ef5e54d8f03` passes the offline secret-exclusion/ambiguous-target check. Independent Sol High re-review PASS; exact pins checked and read executed successfully. See `auto-switch-live-discovery-result-20260912.md`.
- Live r3 remains healthy; no agent_route tables and no static inference-key env fallback. This proves no active controller persistence, not invalid upstream credentials.
- Public current catalog no longer lists GLM-5.2 Free. New candidate JSON proposes Nex N2.5 Pro Free as replacement, with independent review and live qualification pending. No live binding changed.
- Runtime port `c70211160bae5237be4dfd7c8bb9e2894d757492`, report-only HEAD `61665339353191db4b1e8321a27a63ed76183bdd`, passed six unit/API/DB cases and eight integration cases. Type comparison introduced zero diagnostics against the pinned baseline. Independent Sol High review found one P1: Codex app-server bypasses submitted-attempt hooks and can cause a post-send error to be treated as no attempt. Original implementer owns the fail-closed fix; other requested gates passed review. Acceptance remains pending.
- Reviewed direct metadata GET returned HTTP401; no forwarding defect is established. See `auto-switch-auth-result-20260912.md`. A separately reviewed hash-only metadata diagnosis is being prepared; no upstream credential rotation or authentication bypass is justified.
- Exact model binding candidate passed independent review as an offline proposal only. Provider generation, per-connection eligibility, tool behavior and subscription quota remain unproven.
- Phase 3 preparation is complete: exact candidate bindings are independently accepted, and unavailable/stale subscription evidence remains fail-closed. This checklist item records preparation only; the two following qualification/matrix tasks remain open and no live binding has changed.
- Caller authentication diagnosis is complete: the independently reviewed single hash-only diagnostic found exactly one valid admin CLI-token match and zero API-key matches with complete hash coverage. Stored requireLogin is true. Management-only authentication explains the 401; no server forwarding patch or upstream rotation is appropriate. Intended inference credentials still need a separate scoped reviewed contract before qualification. See `auto-switch-auth-metadata-result-20260912.md`.
- Gemini preservation is committed at `dc53bcfed67b3bbea7d2fbf82468342e573dadb3` with 28 focused tests and scoped lint passing; independent review is pending. Candidate source is frozen for that review.
- Independent Sol High Gemini review PASS closes candidate source review at `dc53bcfed67b3bbea7d2fbf82468342e573dadb3`; tests were not unnecessarily rerun. Candidate remains frozen. Exporter adaptation separately passed review and produced 5950 regular exact-Git-blob files, archive SHA256 `3cd078f0d025158248e710784c0499b51842d61f788f28e2a96fe589c4c9f440`, manifest SHA256 `c1179f5e5df5c42ec17f4c239e5ea077cd0416a608529b93e273ef0292782452`, with no credential-pattern matches. Image/runtime acceptance and current-client reconciliation remain open.
