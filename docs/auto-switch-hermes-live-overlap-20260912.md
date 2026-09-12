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
