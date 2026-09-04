# B1 pinned TLS native artifact source correction

Date: 2026-09-04 Asia/Bangkok. Source base: `d39ec5a4471d88d821576a3830fa55da4e2b027b`. Scope: source-only Docker/build helper/shared TLS options correction; no live builder, provider, credential, VM, deployment, or image-build action performed by this lane.

## Root cause and correction

The coordinator's B1 attempt 2 failed because locked `tls-client-node@0.2.0` resolves the latest GitHub release but expects `tls-client-linux-ubuntu-amd64-<version>.so`. Upstream v1.16.0 publishes `tls-client-xgo-1.16.0-linux-amd64.so` instead. Its postinstall warns and exits successfully without installing an asset; the Docker presence check then fails. Evidence: root `docs/handoffs/omniroute-b1-build-evidence-20260904.md`, generated `build-attempt-2.log`, SHA-256 `2e56112924384d56b4c822fe7946e6d485727b45eb75a3fa7b4cb830a3acaa7e`.

There is also a runtime path mismatch: all six native TLS services obtain `downloadDir` from the shared helper, pointing into writable `DATA_DIR/tls-client/bin`; a package-directory build artifact alone would not prevent a fresh unchecked runtime download. The Docker image now sets an explicit immutable native library path consumed by that same shared helper and therefore by chatgpt, claude, grok, lmarena, notion, and perplexity TLS clients. Non-Docker behavior with the new variable unset remains unchanged. Relative explicit paths fail closed.

The existing package lock is unchanged: `tls-client-node@0.2.0` and `koffi@2.16.1`. The installer asserts the exact TLS loader version before downloading. It fetches only the fixed v1.16.0 release URL, bounds download bytes, checks SHA-256, size, ELF class, endianness and machine before writing, refuses mismatched existing artifacts, and uses exclusive creation. Unsupported platforms fail explicitly. No dependency postinstall is enabled and no version is resolved from `latest`.

## Official artifact pins

Source: [official v1.16.0 release API](https://api.github.com/repos/bogdanfinn/tls-client/releases/tags/v1.16.0) and [release notes](https://github.com/bogdanfinn/tls-client/releases/tag/v1.16.0), retrieved 2026-09-04. Published 2026-09-02T15:06:10Z. v1.16.0 includes the non-SOCKS5 protocol-racing proxy IP-leak correction; this fix does not downgrade to the older legacy-named release.

| Docker / Node architecture | Official asset | Bytes | SHA-256 | ELF machine |
| --- | --- | ---: | --- | ---: |
| amd64 / x64 | `tls-client-xgo-1.16.0-linux-amd64.so` | 17412432 | `75f19133e3cb9b16ab3d2dfe3376c7590aab2fe6f2294debac661bfd63dca6a3` | 62 |
| arm64 / arm64 | `tls-client-xgo-1.16.0-linux-arm64.so` | 16398336 | `91f88d35fa64284c811373003d2a26caa3145eaeefd1c0e9576f10724a914332` | 183 |

Both use ELF64 little endian. URLs are exactly `https://github.com/bogdanfinn/tls-client/releases/download/v1.16.0/` plus the asset name above. The implementation received both actual upstream assets into memory only and independently matched the pinned size, SHA-256 and ELF machine; neither was persisted or loaded on this Windows host.

Builder filenames preserve compatibility with the actual locked loader:

- x64: `/app/node_modules/tls-client-node/bin/tls-client-linux-ubuntu-amd64-1.16.0.so`.
- arm64: `/app/node_modules/tls-client-node/bin/tls-client-linux-arm64-1.16.0.so`.
- Both runner architectures: explicit COPY to `/opt/omniroute/tls-client.so`, regular file mode 0644, root-owned and outside `/app`'s runtime-user ownership and the data volume.
- New image default: `OMNIROUTE_TLS_NATIVE_LIBRARY=/opt/omniroute/tls-client.so`. Shared options become `{runtimeMode: "native", nativeLibraryPath: <that path>}` without `downloadDir`; the package's native path branch bypasses cache discovery and release lookup.

The complete TLS loader and Koffi packages are explicitly copied into the runner so native tracing does not determine their availability. The original package-local copy remains present but is not the selected runtime artifact. No runtime checksum loop or network fallback is added: image construction verifies the artifact and the immutable image path is selected explicitly.

## Focused verification

The immutable-path regression was first run against the original helper and failed (0 pass / 1 fail: writable downloadDir returned instead of nativeLibraryPath). After the correction:

- `tests/unit/build/pinned-tls-client.test.ts`: 3/3 PASS. Covers the shared helper plus actual package native-path bypass with network prohibited; both legacy discovery names through actual Linux loader code; unsupported platforms; corrupt/size-preserving tampered bytes and unexpected loader version fail before artifact creation/download as applicable.
- Existing `tests/unit/tls-client-download-dir-8579.test.ts` behavior cases selected by `resolveTlsClientDownloadDir|buildNativeTlsClientOptions passes`: 2/2 PASS. The unrelated source-text Docker assertion was not rerun or changed.
- Both actual official release assets: size/SHA-256/ELF validation PASS, download to memory only. This proves integrity and architecture metadata, not Linux ABI loading.
- `node --check` on both new build helpers: PASS. `git diff --check`: PASS.
- No broad type-suite or routing-suite rerun: routing bytes are unchanged. No whole-project type-clean claim is made.

Commands used from this checkout in PowerShell (bundled Node; no installation):

```powershell
$tlsNode = 'C:/Users/chatc/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe'
$tlsLoader = 'file:///C:/ChatGPT%20Projects/SW-Selfhosted-Network/.worktrees/omniroute-routing-completion/node_modules/tsx/dist/loader.mjs'
& $tlsNode --import $tlsLoader --import ./tests/_setup/isolateDataDir.ts --test tests/unit/build/pinned-tls-client.test.ts
& $tlsNode --import $tlsLoader --import ./tests/_setup/isolateDataDir.ts --test --test-name-pattern='resolveTlsClientDownloadDir|buildNativeTlsClientOptions passes' tests/unit/tls-client-download-dir-8579.test.ts
& $tlsNode --check scripts/build/installPinnedTlsClient.mjs
& $tlsNode --check scripts/build/smokePinnedTlsClient.mjs
git diff --check
```

## Remaining B1 / B2 gates

Linux native compatibility is **NOT PROVEN** locally for either architecture. A newly authorized B1 image build must pass the added genuine native start/stop smoke twice: builder package-local artifact, then final runner artifact as `USER node`. Each Docker `RUN --network=none timeout 60 node scripts/build/smokePinnedTlsClient.mjs ...` verifies bytes before dlopen, loads the actual locked TLS/Koffi binding, resolves all five ABI symbols, calls native destroyAll on stop, and decodes/frees its response. No provider request is made. BuildKit networking is disabled for these steps, additionally to a JavaScript fetch prohibition. A mismatch, unresolved native dependency, ABI failure, network requirement, or timeout fails the build. The runner smoke also proves the explicit COPY and non-root path readability. An amd64 result does not constitute arm64 native proof.

B2's new-image-default mapping must explicitly permit the additional environment default above, retain that exact path and image file, and prohibit clearing/overriding it or mounting over that path under the current contract. An empty/unset variable intentionally restores existing non-Docker behavior; it must not be mistaken for the reviewed Docker configuration. Other live configuration/routing/event-wire settings are unchanged. This source report does not authorize a B1 retry or B2 execution; coordinator review and action-time pins remain required.

Changed files: `Dockerfile`; `scripts/build/installPinnedTlsClient.mjs`; `scripts/build/smokePinnedTlsClient.mjs`; `open-sse/services/tlsClientDownloadDir.ts`; `tests/unit/build/pinned-tls-client.test.ts`; this report. Next action: independent scoped source/security review, then the coordinator's separately authorized B1 native image proof.
