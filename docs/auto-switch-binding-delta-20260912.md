# Binding refresh proposal — not applied

Reuse the reviewed September 4 finite pools, with one necessary replacement: `z-ai/glm-5.2:free` is absent from the current public OpenRouter models API. Proposed replacement `nex-agi/nex-n2.5-pro:free` is present and advertises tools plus structured_outputs with context 262144. This preserves three distinct concrete free models; it does not claim benchmark superiority or live generation qualification.

Public source read September 12: `https://openrouter.ai/api/v1/models`. Cohere North Mini Code Free is present and advertises tools but not structured_outputs; its required objective-format behavior must be qualified rather than assumed. Nvidia Nemotron free and all five explicit paid Chinese identities remain present and advertise tools/structured_outputs. Public catalog presence does not prove account credit, request eligibility or successful inference.

Connection IDs were observed in today's authenticated MCP quota inventory, but exact per-connection model access, caller authorization and fresh real weekly subscription evidence remain unproven. No new provider is connected and no live combo/model/key is changed by this proposal.

Candidate: `auto-switch-bindings-candidate-20260912.json`. Independent review and exact-path live qualification are required before activation. Keep unknown/stale Codex weekly quota fail-closed. No output/context/effort/spend caps are added. Exact key allowlists must use this same candidate's concrete identities, including the replacement free model, and must deny ordinary combos.
