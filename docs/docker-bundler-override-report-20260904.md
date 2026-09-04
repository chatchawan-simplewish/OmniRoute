# B1 Docker bundler override correction

Base: `3d4f0a9d0f77031c3662f7c13b1ee1c196847aa7`. Scope: expose the already documented Docker build argument; no Next configuration, runtime setting, memory framework, dependency, or host change.

Coordinator evidence in root `docs/handoffs/omniroute-b1-build-evidence-20260904.md`: the corrected TLS asset passed genuine network-none builder native start/stop. Next16.2.12 Turbopack then suffered a kernel-confirmed global OOM kill at 20260904 185342 Bangkok: node-MainThread PID36444, anon-RSS13,911,380KiB, file-RSS16,128KiB. Build log SHA-256 `dfe9e2ab8894435641299bfc3c30fae125a764dcccdb074f6a284f28358e8919`. No final image or runner native smoke resulted.

Existing `scripts/build/build-next-isolated.mjs` already selects `--webpack` for `OMNIROUTE_USE_TURBOPACK=0`, preserves existing `NODE_OPTIONS`, and explicitly warns that V8 heap limits do not constrain Turbopack's native Rust memory. Docker documented the build argument but hardcoded `ENV OMNIROUTE_USE_TURBOPACK=1`, so that argument could not reach the helper.

Correction: add `ARG OMNIROUTE_USE_TURBOPACK=1` immediately before `ENV OMNIROUTE_USE_TURBOPACK=${OMNIROUTE_USE_TURBOPACK}` in the builder stage. Default remains Turbopack. The existing `OMNIROUTE_BUILD_MEMORY_MB` argument remains unchanged (default4096). Independent runner stages/runtime defaults remain untouched.

One focused source-to-helper regression evaluates the relevant builder ARG/ENV assignments and calls the actual `resolveNextBuildEnv` and `resolveNextBuildBundlerFlag`. Before the fix it failed: expected webpack, received turbopack. After the fix it passed1/1, proving override0 selects webpack with the requested8192MiB heap preserved, and default settings still select Turbopack with4096MiB. This does not execute Docker or prove that a Linux image build avoids OOM.

Command from this checkout in PowerShell:

```powershell
& 'C:/Users/chatc/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe' --import 'file:///C:/ChatGPT%20Projects/SW-Selfhosted-Network/.worktrees/omniroute-routing-completion/node_modules/tsx/dist/loader.mjs' --import ./tests/_setup/isolateDataDir.ts --test tests/unit/build/docker-bundler-override.test.ts
```

Next: independent scoped review of this exact descendant. Only the coordinator's later reviewed B1 command may use `--build-arg OMNIROUTE_USE_TURBOPACK=0 --build-arg OMNIROUTE_BUILD_MEMORY_MB=8192` after heavy-builder ownership and capacity revalidation. No router image build was run here; the builder remains assigned elsewhere. No VM resize, swap, daemon change, runner-smoke omission, or acceptance relaxation is implied.
