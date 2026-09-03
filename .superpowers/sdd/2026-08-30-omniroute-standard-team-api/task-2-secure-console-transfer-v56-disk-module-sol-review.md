# OmniRoute V56 disk-module Sol High implementation/security review

Date: 2026-09-03 (Asia/Bangkok)
Reviewer: Codex, independent `gpt-5.6-sol` High implementation/security review
Reviewed implementation commit: `25c3eb2c309302b6d9866c9d25b90010c4e5d1bc`
Parent / V55 capacity-probe PASS: `5701c57c214edfb7f3f41d29e196c62c0a26fe02`

## Verdict

`FAIL`

`fix_may_proceed=true`

`live_execution_classification_may_begin=false`

`authorizes_live_execution=false`

The V56 ESM candidate mechanically retains the reviewed V55 readiness behavior,
exports the seven required continuation bindings, and passes its offline matrix.
The loader is not hash-pinned at the execution boundary, however: it hashes one
read of the path and then asks Node's file-URL importer to reopen that same path.
A replacement between those operations can execute bytes that were never
hashed. This unresolved HIGH TOCTOU finding blocks classification and execution.

## Direct committed-byte evidence

`25c3eb2c3` is the direct child of `5701c57c2` and adds exactly the six assigned
V56 disk-module artifacts. Direct Git-object reads produced:

| Artifact | Git blob | Bytes | SHA-256 | ASCII |
| --- | --- | ---: | --- | --- |
| Design | `3dfbd0b84507b78a96b16338a15efe68ccaa2e7d` | 2905 | `7EC9D1DEE393E3077CEFBB8979C7C4B6D193468C25C7CC3C47FB2C148AB386F8` | yes |
| Source | `64e880102ef29b139abc249dff7f0793dd5b868b` | 47062 | `8E25FEB99014A2E85DF77F2A10AE9A19D4EA51C00E584317D3942104F774A3BD` | yes |
| ESM executable | `53c3ceff0ffdc566c149b13b5c24d7b26153f587` | 26875 | `932A9A06331C5683AB68471E7DA6E9AB9277819722323405B7711CFFB1B25CAA` | yes |
| Loader cell | `d248667532febeb9202f79f244354fd935cc5c07` | 1244 | `2BAC3384451CE9097111B5718612D50E0C28F9B360CAE531E33C6D8F4776A1D0` | yes |
| Pure fixture | `5f84befe45cebdcbd7d50495046e423b3e010dbb` | 40048 | `BFAFDFAA84E4A46FEF0FEE98CF118D9CBEC0B229457DFE00CE3CFAFAB5A3D3B2` | yes |
| Review package | `4c56cec88f3f66666bc66aca6155b4dafbd6189e` | 4614 | `714E56C0CB7811E7552938E366D3F35FB1A3F94C104029D4CEB111BA4A5836BE` | yes |

All six blobs contain zero non-ASCII and zero NUL bytes. Fresh syntax checks of
source, executable, loader, and fixture passed. The full scoped fixture returned:

```json
{"result":"PASS","executableBytes":26875,"executableSha256":"932A9A06331C5683AB68471E7DA6E9AB9277819722323405B7711CFFB1B25CAA","sourceBytes":47062,"sourceSha256":"8E25FEB99014A2E85DF77F2A10AE9A19D4EA51C00E584317D3942104F774A3BD","fixtureBytes":40048,"fixtureSha256":"BFAFDFAA84E4A46FEF0FEE98CF118D9CBEC0B229457DFE00CE3CFAFAB5A3D3B2","loaderBytes":1244,"loaderSha256":"2BAC3384451CE9097111B5718612D50E0C28F9B360CAE531E33C6D8F4776A1D0","moduleExports":7,"moduleExecutions":1,"loaderCases":6,"loaderTargetImports":1,"predecessorContaminations":132,"behavioralExecutions":212,"terminalOutputCleanup":true,"completeCounterVector":true}
```

This rerun was justified by the named loader-integrity doubt. It was purely
offline and performed no CUA, provider, network, DNS, VM, clipboard, credential,
secret, or live action.

## Finding

### V56-DISK-HIGH-001 — HIGH — verified bytes are not the imported bytes

The loader performs these distinct operations:

1. `readFileSync(modulePath)` returns bytes which are checked for exact length,
   SHA-256, and ASCII.
2. `import(moduleUrl + "?sha256=" + moduleSha256)` tells Node's ESM loader to
   open and compile the file at `moduleUrl`.

The query string is only a module-cache key. It does not bind Node's later file
read to `moduleBytes`, lock the path, or cause the importer to verify the query's
hash. Another local writer can replace or rewrite the executable after step 1
and before step 2. Node can then execute different bytes while the URL still
carries the hash of the earlier verified buffer. Because module execution owns
the one-shot browser/readiness gate, post-import detection cannot undo effects.

The transformed loader fixture does not test this boundary. Its `__load` double
accepts only the URL and returns a fixed namespace; it never reopens the path or
selects code from current disk contents. Thus its size/hash/ASCII cases prove
pre-import validation and cleanup, but its success case cannot prove that the
validated bytes equal the executed bytes.

Required fix: import the already verified `moduleBytes` through a content-bound
ESM representation, such as an exact data URL constructed from that buffer, and
pin/assert that representation and its single import. Alternatively provide an
equivalent mechanism that cryptographically binds execution to the verified
buffer without reopening a mutable path. Add a fixture case that mutates the
path's backing content after verification and proves the executed module still
comes only from the verified bytes (or fails before execution). Retain all
cleanup, one-shot, path, size, hash, ASCII, and no-fallback assertions.

## Retained properties without findings

The source is exactly the final V55 source with `V55` renamed to `V56` plus the
seven-name export list. Exact regeneration proves executable derivation and
ASCII syntax. The module namespace exposes exactly these live bindings:

- `secureConsoleOwnedTaskTabV56`
- `secureConsoleOwnedTaskTabV56Eligible`
- `secureConsoleOwnedTaskTabV56State`
- `secureConsoleOwnedTaskTabV56PreCreateDetachConsumed`
- `secureConsoleOwnedTaskTabV56PostNativeDetachConsumed`
- `secureConsoleCloudflareReadsV56Consumed`
- `secureConsoleV56Consumed`

The candidate-derived matrix retains one successful module execution, 132
fresh-realm predecessor guards/contaminations, 212 V55-equivalent readiness and
failure behaviors, exact counters, output/ordinary cleanup, and sanitized
results. No retry, fallback, alternate provider path, token creation, click,
copy/paste, secret access, persistent provider mutation, DNS, or VM action was
introduced beyond the inherited read-only token-page readiness flow.

The loader otherwise pins the exact absolute path, expected 26875-byte length,
expected executable SHA-256, ASCII constraint, one `node:fs` import, one
`node:crypto` import, one target-import expression, namespace-null prestate, and
namespace cleanup/rethrow on read, validation, parse/execution, or import
failure. These retained properties do not close the gap between the verified
buffer and Node's separate file import.

## Severity counts

- Critical: 0
- HIGH: 1
- IMPORTANT: 0
- Minor: 0
