# Hermes 693 reconciliation

This is offline source analysis only. No Hermes worktree, VM104 source, gateway, or runtime was modified.

## Evidence

Both `693641aa8b4359c602283bdbbc14041e03bc47bc` and `04dd80a977f40b05e5b2054111747af07a61886a` are readable local objects despite the shallow-root warning. The recorded twelve live candidate paths match 693; eight differ from 04dd. The broader `agent`, `run_agent.py`, and Hermes-state scope differs in 99 paths between the two bases. Accepted candidate `aa82b0fb468c4c16956051819d23d4f48d1ebc16` is based on 04dd, so its tested result does not establish direct applicability to 693.

The current-base candidate changes the protocol entry module plus the request/response, stream, loop, compression, and turn-facade seams. Its two final corrections place route-state creation after lease start immediately before the conversation call, and reject a setup failure before route admission. Those behaviors should be retained, but reimplemented against 693's current ownership boundaries after an interface map, not copied as a module bundle.

## Compatibility result

`4fdcf6bda33169e0059618b87c08ac176384e5ca` does not already fit 693. Neither commit is an ancestor of the other. Its own delta is narrow (the explicit-child/compression-lineage correction in `run_agent.py` and its focused test), but a three-way merge with 693 conflicts at `run_agent.py` and the routing seams `agent/anthropic_adapter.py`, `agent/chat_completion_helpers.py`, `agent/conversation_compression.py`, `agent/conversation_loop.py`, `agent/tool_executor.py`, and `hermes_state.py`. The large base divergence makes a clean cherry-pick or wholesale port unsafe.

## Minimal safe port

Start a fresh 693-based source worktree. First map the 693 call path from request admission through lease start, setup, conversation dispatch, streaming/finalization, and compression/session lineage. Then port only the accepted protocol state and hooks into the corresponding 693 owners, preserving 693's public interfaces and its live-matched behavior. Apply the two lease/setup fixes at the mapped 693 dispatch boundary, and translate the 4fd explicit-child correction only after confirming its session-store predicates exist there. Add focused tests for lease refusal, setup failure before route publication, no replay across stream/409 handling, compression lineage, and explicit child runs. Do not apply `aa82` or `4fd` directly, and do not claim VM parity until a separately reviewed 693-based candidate is compared to the recorded live scope.
