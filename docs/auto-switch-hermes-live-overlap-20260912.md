# Hermes live source overlap

Read-only checks on 2026-09-12 around 08:00 UTC used strict existing SSH trust for `hermes@192.168.1.141` and `git --no-optional-locks -C /home/hermes/.hermes/hermes-agent diff --numstat HEAD` scoped to the candidate's runtime paths. No file content, credentials, configuration, service state or working-tree bytes were modified.

| Path                              | Added | Removed |
| --------------------------------- | ----: | ------: |
| agent/chat_completion_helpers.py  |   482 |     180 |
| agent/conversation_compression.py |    10 |      28 |
| agent/conversation_loop.py        |    30 |     107 |
| agent/turn_facade.py              |     1 |       5 |
| hermes_state.py                   |    45 |     219 |
| run_agent.py                      |    20 |      18 |

These are substantive tracked changes against the previously discovered `04dd80a977f40b05e5b2054111747af07a61886a` HEAD, not a clean deployment target. The HEAD was not re-read during the numstat call, so these counts establish overlap at observation time rather than a fresh full release pin. Earlier broad name-only output reported 98 lines within the agent scope and was truncated; the exact scoped numstat above is the retained evidence.

The completed task `Check VM104 Hermes status` (`01a08719-c395-7e31-aa64-a36b902d6bd4`) recorded an updater HTTP 429 failure on September 9/10 and no modifications/retry by that task. This historical finding does not establish the origin or ownership of today's tracked edits.

Continue offline port qualification, then establish live dirty-source provenance and reconcile these exact paths before preparing a deployment. Do not reset, overwrite, infer ownership transfer, or claim the offline clean-base port matches the live installation.

## Later provenance observation

At 09:30:56 UTC, live HEAD was re-read as `04dd80a977f40b05e5b2054111747af07a61886a`. At 09:32:24 UTC, all 12 inspected candidate runtime paths matched recorded commit `693641aa8b4359c602283bdbbc14041e03bc47bc`; eight differed from HEAD and four also matched HEAD. HEAD and hashes were stable before and after observation. Only Git blob hashes were compared; no live source contents were exported or changed.

Paths: `run_agent.py`, `hermes_state_compression.py`, and `agent/{anthropic_adapter,chat_completion_helpers,conversation_compression,conversation_loop,stream_delivery,turn_facade,turn_final_response,turn_response_check,turn_response_intake,turn_tool_round}.py`.

Commit 693641 is available in the local `hermes-routing-live-compatible` repository and is titled `fix(chat-completions): strip name from tool-result messages for strict providers`. This provides a concrete offline reconciliation base for these paths. It does not establish full-tree parity, the origin of every live modification, or live deployment ownership.

At 09:51 UTC a broader strict-SSH read, `git --no-optional-locks diff --shortstat 693641aa8b4359c602283bdbbc14041e03bc47bc -- agent run_agent.py hermes_state.py hermes_state_compression.py`, returned exit 0 and empty output on VM104. Thus the tracked working-tree bytes across that scope match 693641. Untracked files and paths outside the scope are not covered; HEAD remains a separate deployment pin. The two recorded bases differ across 99 files in this scope, so replacing the live installation with the accepted 04dd-based candidate would introduce unrelated changes.
