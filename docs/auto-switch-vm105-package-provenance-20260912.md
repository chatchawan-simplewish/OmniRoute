# VM105 package provenance — read-only checkpoint

On 2026-09-12 around 11:11–11:19 UTC, strict known-host SSH reads inspected only package metadata and the expected source-file path under `/opt/deepseek-harness` on VM105. No package, configuration, service, credential or provider operation was changed.

- Installation root contains `node_modules`, `package.json`, `pnpm-lock.yaml` and `pnpm-workspace.yaml`; its only declared dependency is `@deepseek-ai/dsh`.
- Installed package: `@deepseek-ai/dsh`, version `0.1.1-rc.2`, binary `dsh` at `lib/bin.js`.
- Accepted source worktree `.worktrees/deepseek-routing-completion`, commit `4d2f8dac2a`, has the same CLI package name/version/bin mapping. Version agreement is not compiled-byte or routing-protocol parity.
- Expected source path `/opt/deepseek-harness/packages/core/agent-loop/src/agent.ts` is absent. The accepted local source file hashes to `6a9ce47b1f102fb242efa3c7b814738af07d9a5ad39b1bfa2d4e594c3e55495a`; no installed compiled-file equivalence is claimed.
- Its source report requires a fresh isolated official build/pack lane, not reuse of existing test junctions or stale `dist` artifacts. No packaging was performed by this observation.
- A fresh task snapshot confirms `Continue VM105 owner bridge preservation…` (`01a08307-591f-70b2-b6f0-651f8cd10455`) is not loaded and its latest turn records blocked progress 9/21 pending the supervisor architecture decision. Its ownership was not transferred. This implementation remains read-only on VM105.
