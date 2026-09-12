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
- [ ] Independently review fresh discovery scope and pin live runtime/authentication metadata.

## Phase 2 — complete candidate (three tasks)

- [ ] Trace and repair the shared inference authentication path if current evidence confirms a defect.
- [ ] Reconcile accepted controller/client code with the current provider/audit repair runtime; implement only proven gaps.
- [ ] Run focused acceptance checks and independent source/security review.

## Phase 3 — qualify and bind (three tasks)

- [ ] Prepare/review exact connection/model bindings and fail-closed quota evidence.
- [ ] Qualify eligible providers through the intended inference path under a fresh reviewed contract.
- [ ] Prove the routing matrix on an isolated candidate, including authorization and replay boundaries.

## Phase 4 — activate and finish (three tasks)

- [ ] Review and execute bounded live rollout with rollback under sole Sol High gate ownership.
- [ ] Verify both clients through explicit aliases before changing their defaults.
- [ ] Complete independent final audit and durable evidence/publication handoff.

## Current state

Phase 1: 2/3. Phase 2: 0/3. Phase 3: 0/3. Phase 4: 0/3.
Live switching is NOT PROVEN; no live mutation or inference probe has occurred in this implementation run.
Next: independently re-review and execute narrowed read-only discovery; complete the manual source port and review it.

## Recovered evidence and current ownership

- Server controller accepted at `d39ec5a4471d88d821576a3830fa55da4e2b027b`; original base `6449695dd985045a0120e3246402296e62a967c6`. Later completion tip `066a32e9f` adds build fixes.
- Hermes `.worktrees/hermes-routing-live-compatible` source `4fdcf6b...`; DeepSeek `.worktrees/deepseek-routing-completion` source `4d2f8dac...`. Both already implement per-step tuple rotation, ACK/redelivery and no hidden routed retries. Do not rewrite accepted client logic.
- Actual remaining integration: deployment, exact slash-alias/connection/key binding, side-by-side Hermes Linux compatibility stage and client normal/high acceptance.
- Old D1-D4 and D6-D8 are spent; D5 is blocked. D9 is obsolete after the host move. Old rollout lane remains read-only under its previous owner.
- Source port assigned to `/root/runtime_port` (Terra Medium) exclusively in `.worktrees/omniroute-auto-switch-runtime-20260912`, baseline `820ead300f0c03e17a87fbaa7e22e81d72faeeeb` (3.8.50 and accepted audit fix). This separate Git worktree is owned by the current task with the subagent as its sole source writer. The coordinator writes only this plan/discovery worktree while that implementation is active.
- No generic cherry-pick: the accepted routing delta conflicts with newer auth, handler and DB architecture. Port behavior without replacing newer files wholesale.
- Discovery review round 1 found excess API-key row metadata and incomplete SSH pins. Both were corrected; script `e53d0e0cd31af70fd6a9511cc8a7fe638ddfb2ffbaba4dc4d6c15ef5e54d8f03` passes the offline secret-exclusion/ambiguous-target check. Independent re-review pending.
