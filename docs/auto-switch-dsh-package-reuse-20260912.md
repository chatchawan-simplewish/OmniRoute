# DSH package acceptance reuse

Read-only source assessment found that `.worktrees/deepseek-routing-completion` is at `e87dfc3576fac6021ecd330ba0ffa04dc7c176d7`, later than the earlier `4d2f8dac2a` routing pointer. Do not rebuild from the stale pointer or modify the accepted checkout.

Existing evidence to reuse in that worktree:

- `docs/handoffs/dsh-linux-pack-v6-raw-evidence-v1-20260907/logs/status.tsv`: all 13 build stages exited zero; the accepted family contains 237 packages.
- `docs/handoffs/dsh-consumer-v7-result-20260907.md`: consumer install and offline closure, four imports, and 133 plugins passed with retained source/package pins.
- Current tip records V7 PASS; its preceding commits include independent review and fixes. Source acceptance and package acceptance do not establish VM105 installed-byte parity, service startup, provider calls or end-to-end routing.

The VM105 owner's transfer at `d8a703cefde3ebe35092ed91c53b4ec2240033b9` grants retained package/client source assessment only. Its native supervisor block remains separate. No VM105 deployment/profile mutation, credential/provider action or spent-gate replay is authorized by this record.

Retained build source: `28551e5cc3e89e2866f547d5a4b4ac321d9e853c`. Package manifest SHA256: `661b44dfd42791ddaa1e2b39e5622f5c525267a1924b374c73dcaa078ba9d8d0`. Source manifest SHA256: `b95c4c730dbc285bcecce4a7c11aaff99f5009815de7fc1df40d515d664485a2`. V7 independent review SHA256: `aed2e00a10df0e28fe37888ca5f8f4acd71193d3025c9aabb485495e88a59165`.

Read-only comparison confirms `4d2f8dac2a` is an ancestor of the retained build source. The accepted no-recovery behavior (including HTTP 400/409), durable ACK and tuple/controller logic is preserved. Runtime differences use the session barrel export and add comments; they do not change the provider tuple/ACK transport behavior.

Next: bind these existing manifest and consumer acceptance pins into any separately reviewed client release proposal. Preserve existing packages; no replacement packaging is justified by this comparison.
