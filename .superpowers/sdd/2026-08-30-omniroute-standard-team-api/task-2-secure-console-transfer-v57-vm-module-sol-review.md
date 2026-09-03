# OmniRoute V57 in-memory VM-module Sol High implementation/security review

Date: 2026-09-03 (Asia/Bangkok)
Reviewer: Codex, independent `gpt-5.6-sol` High implementation/security review
Reviewed commit: `695aa10ad7c16544a0da9f9768bc82b8fa9f9095`
Parent: `12df94b3cd79e752ae51ecc2cbdd3aa0b81dd1b9`

## Verdict

`PASS`

`live_execution_classification_may_begin=true`

`authorizes_live_execution=false`

No unresolved Critical, HIGH, IMPORTANT, or Minor findings remain. The six-file
V57 package implements the reviewed replacement boundary without reopening or
retrying spent V56. This review permits a separate non-self-referential
execution-classification step; it does not authorize V57 execution or any live
browser/provider action.

## Direct committed-byte evidence

Direct Git-object inspection proves `695aa10ad` adds exactly the six named V57
artifacts and no other path:

| Artifact | Git blob | Bytes | SHA-256 | ASCII |
| --- | --- | ---: | --- | --- |
| Design | `47d06491ad9cb3fb70680174c1943c8b82a4c2f4` | 3370 | `C6DC6629880B074EA3B5875A9D238BCAFB9997485C7E232109EE032A92B0E649` | yes |
| Source | `5a07e532c75e1dd6da7b07c82460f5e97c4d27f5` | 47611 | `0920D1D410C8109446B565340777D14190A0850222A0970E63CDF653B537A290` | yes |
| ESM executable | `b3374909a13fa43bab349de7c342b8fe9afa69ea` | 27336 | `48DD581AE424042D42002AA8D32D017B7156A65CEE729A983BFB878200051A38` | yes |
| Loader cell | `78c4455ee3039ea5579f478d7ec467711d04375e` | 2553 | `23477C4DC06262AD25CE28D270B767A804DF55A7598D379EB74A560F55AC06D7` | yes |
| Pure fixture | `5f35202767961f24ce275dc7e6107bc04e394fc3` | 45054 | `45C4918DA62D810D984244E94CC67043CCDB642503F0A178794C7C4E0CDC3900` | yes |
| Review package | `b2a763834ded2163b7058d836c548961deafd093` | 5238 | `3507229D1DDFF242E7FE889E14E157E011CF7CF683E67DEA99D702E7935117AA` | yes |

The package's self-reported five-file tuple exactly matches the corresponding
committed blobs. Its omission of the review package's own tuple is a correct
non-self-reference boundary; the sixth row above supplies that independent
direct-byte evidence.

## Candidate derivation, guards, and exports

Direct source comparison proves V57 is exactly final V56 with all `V56` labels
renamed to `V57`, plus the sole prescribed extension of the predecessor guard:
the seven V56 continuation names and `secureConsoleV56Module`. The resulting
guard block contains exactly 140 unique ordered names: the inherited 132 V35-
V54 names followed by those exact eight V56 names.

The fixture applies the retained Terser module settings to the complete source
and requires exact executable bytes. The executable contains one export list
with exactly these seven retained live bindings: owned tab, eligible flag,
state, pre-Create detach-consumed flag, post-native detach-consumed flag,
Cloudflare-reads-consumed flag, and V57-consumed flag. All names remain
unmangled. The candidate has exactly one dynamic import, the fixed browser-
client URL, and retains the source-projection count/hash and inherited read-
only behavioral boundary.

## One-read VM-module loader

The loader initializes `globalThis.secureConsoleV57Module` to null, reads the
absolute executable path exactly once, and verifies the same Buffer's 27,336-
byte size, exact SHA-256, and ASCII-only bytes. It decodes that verified ASCII
Buffer directly into exactly one `SourceTextModule`; there is no `data:` URL,
path import, path reopen, second read, race, retry, alternate source, fallback,
or failure continuation.

The source module's static linker always throws, so every static import is
rejected before evaluation. Its dynamic-import callback accepts only the exact
allowlisted browser-client file URL and only while the bridge count is zero.
The callback performs at most one host import, validates
`setupBrowserRuntime` as a function, and creates one `SyntheticModule` whose
sole export is that function. The bridge is linked and evaluated exactly once;
the source module is evaluated exactly once and must finish with bridge count
exactly one before its seven-binding namespace is retained.

Every read, VM-shape, size, hash, ASCII, parse, static-link, dynamic-specifier,
duplicate-import, host-import, bridge-shape, evaluation, or bridge-count
failure reaches the outer cleanup, sets the retained namespace to null, and
rethrows. There is no retry or V56/V55 fallback surface.

## Fixture and security evidence

The pure fixture mechanically proves source-to-executable equality, 140 guard
contaminations, the inherited 212 behavior executions plus eight new V56
contaminations (220 total), complete counter vectors, terminal/documentation/
ordinary failure cleanup, and sanitized output. Its VM-loader harness uses
real `createContext`, `SourceTextModule`, and `SyntheticModule` lifecycle
objects while replacing only the file read and browser-client host import with
controlled in-memory doubles.

The success case executes the exact committed candidate-derived bytes and
asserts one exact-path read, one source construction/link/evaluation, zero
static-link requests, one exact allowlisted host import, one synthetic bridge
construction/link/evaluation, exact success output, and all seven namespace
values. Thirteen distinct negative cases cover size, hash, ASCII, read, VM
shape, parse, static import, wrong dynamic import, duplicate dynamic import,
browser import, bridge shape, evaluation, and missing bridge count. Together
with success this is exactly 14 loader cases; every negative asserts namespace
null, at most one read, and at most one host import, with stage-specific
evaluation/import counters.

The recorded scoped syntax and VM-module fixture result is PASS with
`moduleExports=7`, `moduleExecutions=1`, `syntheticBridges=1`,
`allowlistedBrowserImports=1`, `loaderCases=14`,
`predecessorContaminations=140`, and `behavioralExecutions=220`. It was not
rerun because direct-byte and source review identified no concrete unresolved
doubt.

The V56 incident is an exact single-path child of the V56 classification PASS:
V56 was sent once, failed before candidate parse/evaluation on the unsupported
`data:` specifier, cleaned its namespace to null, and is permanently spent.
V57 is a new offline replacement. Neither its implementation nor this review
performed CUA, browser/provider, network, DNS, VM-host, clipboard, credential,
secret, or token action.

## Severity counts

- Critical: 0
- HIGH: 0
- IMPORTANT: 0
- Minor: 0
