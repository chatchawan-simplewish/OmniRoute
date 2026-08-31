---
context: phase
phase: omniroute-standard-team-api
task: 6
total_tasks: 10
status: paused_review_blocked
last_updated: 2026-08-31T11:24:06+07:00
---

# OmniRoute standard team API — fresh-task handoff

# BLOCKING CONSTRAINTS — Read Before Anything Else

> These constraints were discovered through actual failures. The new owner must acknowledge each one before acting.

- [ ] **One task owns the live lane** — archive the superseded task before this task writes or consumes any authority gate. No parallel VM1205, Cloudflare, OmniRoute, browser, token, or evidence mutation.
- [ ] **The labeled gate is spent** — do not retry, resume, reinterpret, or repair it. Evidence commit: `80adaa7d5d63d1d2c7bfa63b236c6bee93b3b1d8`.
- [ ] **Browser and Windows clipboards are isolated** — browser automation clipboard operations did not reach the fixed PowerShell process. Never reuse that bridge.
- [ ] **The local data-page canary is rejected** — stale clipboard content could false-pass, and data-page keyboard copying does not prove Cloudflare's actual copy-control path. Contract review SHA-256: `1A03BA9DCD03AD5482DB550A63FEFB710A08E0A72270EE8A327494A2AE518A3C`.
- [ ] **No token-bearing page serialization** — after any future token creation, never use DOM snapshots, screenshots, page-text extraction, attribute reads, evaluation, or any output-producing inspection of the page.
- [ ] **One capture attempt means one** — the prior owner made repeated repair attempts after the first mismatch. Any future mismatch must immediately stop and clean up without another bridge, copy, process, or token.
- [ ] **Credential retention remains unresolved** — the revoked credential persists in private worker rollout `01a055c3-52e1-7692-9328-1fdaad80f279`. Do not open, copy, render, archive, move, edit, or manually delete it.
- [ ] **Invalid-token HTTP 401 is NOT PROVEN** — do not substitute dashboard absence, an unauthenticated request, or another token.
- [ ] **Dirty worktrees are user evidence** — preserve all unrelated modified and untracked files; exact-path staging only; never `git add .`.

**Do not proceed until all boxes are explicitly acknowledged.**

## Critical anti-patterns

| Pattern | Description | Severity | Prevention mechanism |
| --- | --- | --- | --- |
| Opaque compound proof | Earlier proof discarded the failing assertion. | blocking | Use individually labeled checks and preserve stdout/stderr. |
| Clipboard-domain assumption | Browser-side token shape was mistaken for host clipboard delivery. | blocking | Prove the exact end-to-end channel before creating a token. |
| Stale-value canary | Pre-existing expected clipboard text could produce a false PASS. | blocking | Clear both domains first and use freshness/challenge binding reviewed independently. |
| Surrogate-page proof | A local input does not establish Cloudflare copy-control behavior. | blocking | Exercise the same transfer semantics or use a separately reviewed secure input channel. |
| Capture repair after failure | Five browser writes and five host reads occurred after the first mismatch. | blocking | Structural one-attempt counters and unconditional cleanup on first mismatch. |
| Transcript exposure | Token-bearing DOM snapshots and a screenshot entered private retention. | blocking | Prohibit all page serialization after token creation; activate only the reviewed non-output action. |

<current_state>

The prior no-retry labeled proxy-proof/Rulesets correction gate failed before proxy start because the created Cloudflare token did not reach fixed PowerShell PID 31608. The exact token row was deleted once; refreshed row absence, clipboard/env/temp/PID cleanup, and VM safe state passed. Proxy/proof/restart/R5/POST/Rulesets DELETE counters remained zero. Invalid-token HTTP 401 remains NOT PROVEN.

Independent incident review is authoritative at `task-2-labeled-capture-incident-sol-review.md`, SHA-256 `A2558F9FBEC57A7FED2D0CA2DF2B3C9864716E23C0E07CC8F4DFD5851BEB93C4`.

The proposed follow-up `task-2-chrome-native-canary-live-brief.md` was independently rejected and must not execute. Review: `task-2-chrome-native-canary-contract-sol-review.md`, SHA-256 `1A03BA9DCD03AD5482DB550A63FEFB710A08E0A72270EE8A327494A2AE518A3C`.

No live gate or background process is active at handoff.

</current_state>

<completed_work>

- Offline Task 1 package approved at `d62d3207848810c3626a050193ae703d2f8369fe`.
- Approved Caddyfile SHA-256: `A31C2010BB47767E25A826CEBCD2469CB51D8AF5C5AE089E46D2051EDD69D9BB`.
- Approved verifier SHA-256: `2961687C8DB5D24DBFD81387F086206F448D63F419A69D2EB2225DD71C87632E`.
- Pinned Caddy image: `caddy@sha256:5f5c8640aae01df9654968d946d8f1a56c497f1dd5c5cda4cf95ab7c14d58648`.
- Multiple failed live attempts were rolled back and independently reviewed; latest exact evidence commit: `80adaa7d5d63d1d2c7bfa63b236c6bee93b3b1d8`.
- Exact revoked token row deleted; current retained credential risk is private rollout retention only.
- Redacted support request prepared and not submitted: `openai-support-targeted-rollout-deletion-request.md`, SHA-256 `F610AFF924A66C63732EED43F7F28D1E23B2DCC922E409A7B9F34BE88DA69BA5`.
- Owner approved unattended continuation for recommended bounded work. Mandatory action-time confirmations still apply to credentials, sensitive transmission, permissions, and deletion.

</completed_work>

<remaining_work>

1. Replace the rejected canary design with a faithful pre-token transfer proof or separately reviewed secure input channel.
2. Obtain fresh independent Sol High PASS on that design before any execution.
3. Execute one corrected token/proxy/19-label/R5/Rulesets gate with one attempt and immediate cleanup.
4. Separately authorize and complete public Cloudflare Tunnel, `ai-api-omniroute.mysw.me`, deterministic rate rule, temporary rollout key, bounded non-streaming/streaming verification, revocation, and evidence.
5. Configure and verify Hermes and DeepSeek Harness against the completed local/OmniRoute routing architecture.
6. Run final broad Sol High security and completion audit.

</remaining_work>

<decisions_made>

- High-difficulty requests first try one VM1201 Qwen Q6 xhigh attempt; Bell-PC Q4 is non-high work only; workload-tiered review and review-gated repair remain approved.
- Team access uses standard OpenAI-compatible API semantics.
- The credential-bearing private rollout remains unchanged pending supported OpenAI retention remediation; no manual task-store surgery.
- A fresh task should take ownership before unattended work continues because the current task is long and has consumed multiple one-shot gates.

</decisions_made>

<blockers>

- **Design blocker:** no review-clean exact transfer path exists. The data-page native-copy proposal is FAIL/REVISE/NOT AUTHORIZED.
- **Security residual:** revoked plaintext remains in private transcript retention; support request prepared, not submitted.
- **Verification residual:** invalid-token HTTP 401 remains NOT PROVEN.

</blockers>

## Required reading in order

1. `AGENTS.md` — ownership, timestamp, routing, and one-shot-gate rules.
2. `task-2-next-session-HANDOFF.json` — machine-readable state.
3. `progress.md` — full Task 1/Task 2 attempt ledger.
4. `task-2-labeled-capture-incident-sol-review.md` — authoritative credential/capture incident review.
5. `task-2-chrome-native-canary-contract-sol-review.md` — why the proposed canary is rejected.
6. `task-2-ps1-proxy-proof-incident-sol-review.md` — still-authoritative 19-label proxy/R5 contract portions.
7. `openai-support-targeted-rollout-deletion-request.md` — prepared retention request; do not submit without action-time confirmation.

## Infrastructure state at last verified checkpoint

- VM1205 existing OmniRoute and Bell proxy services were running.
- Target `team-api-proxy` and team Tunnel were absent.
- `omniroute-internal` had two expected members.
- No listener on host port `20130`.
- Target Cloudflare DNS record, Tunnel, rate rule, and rollout key were absent.
- Exact root-owned Caddy bytes were retained on VM1205.
- These facts are drift-prone and must be revalidated read-only before relying on them.

## Pre-execution critique required

- Rejected design: `task-2-chrome-native-canary-live-brief.md`
- Rejection review: `task-2-chrome-native-canary-contract-sol-review.md`
- Critique focus: faithful Cloudflare transfer semantics, freshness binding that cannot false-pass, atomic fixed-process ownership, abort/timeout cleanup, exact evidence mutation, and zero page serialization after token creation.
- Gate: **Do not begin execution until a replacement design receives a fresh independent Sol High PASS.**

<context>

The correct next move is design repair, not another live attempt. Favor the smallest channel that can be proven end to end without exposing a token. A user-assisted hidden PowerShell input may be considered only as a separately reviewed secure-input design; do not assume it is approved or equivalent.

</context>

<next_action>

Start with a read-only revalidation of the evidence worktree at `80adaa7d5d63d1d2c7bfa63b236c6bee93b3b1d8`, then produce a replacement transfer-channel design and send it to a fresh Sol High reviewer. Do not execute `task-2-chrome-native-canary-live-brief.md`.

</next_action>
