# OmniRoute V57 in-memory VM-module implementation review package

`authorizes_live_execution=false`

## Scope and incident lineage

This package covers only the six new V57 artifacts. The candidate is derived
mechanically from final V56, with V56 labels renamed to V57 and freshness
guards added for all seven V56 exported globals plus
`secureConsoleV56Module`. No inherited product, V56, provider, or live-resource
file changed.

V56 was sent exactly once and failed before candidate parsing or evaluation
because the CUA `node_repl` rejected its `data:` import. Its cleanup passed,
its namespace was null, and V56 remains permanently spent: it is not retried,
continued, reused, or available as a fallback. A later disposable-realm
diagnostic proved that `node:vm.SourceTextModule` and `SyntheticModule` can
perform one in-memory evaluation with one bridged dynamic import. That
diagnostic consumed no provider or token authority. V57 is a new offline
replacement and this package authorizes no live action.

## Direct-byte facts

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| V57 design | 3370 | `C6DC6629880B074EA3B5875A9D238BCAFB9997485C7E232109EE032A92B0E649` |
| V57 source | 47611 | `0920D1D410C8109446B565340777D14190A0850222A0970E63CDF653B537A290` |
| V57 ESM executable | 27336 | `48DD581AE424042D42002AA8D32D017B7156A65CEE729A983BFB878200051A38` |
| V57 loader cell | 2553 | `23477C4DC06262AD25CE28D270B767A804DF55A7598D379EB74A560F55AC06D7` |
| V57 pure fixture | 45054 | `45C4918DA62D810D984244E94CC67043CCDB642503F0A178794C7C4E0CDC3900` |

All five files are ASCII. The fixture mechanically regenerates the executable
with the inherited Terser settings and requires exact bytes. The executable
exports exactly seven V57 live bindings. The predecessor block contains the
inherited 132 V35-V54 names followed by the exact eight V56 names, for 140
freshness guards total.

## One-read VM loader contract

The loader reads the pinned absolute executable path exactly once with
`node:fs`, verifies 27,336 bytes, the pinned SHA-256, and ASCII, and passes that
same verified Buffer's UTF-8 text to one `SourceTextModule`. It never constructs
a `data:` URL, reopens the path, path-imports the candidate, retries, or falls
back.

Every static import is rejected. The dynamic-import callback accepts exactly
one request for the pinned browser-client file URL, imports that host module
once, validates `setupBrowserRuntime`, and bridges only that binding through
one linked and evaluated `SyntheticModule`. The source module evaluates once,
requires exactly one bridge, and only then retains its namespace at
`globalThis.secureConsoleV57Module`. Every loader read, VM-shape, fidelity,
parse, link, import, bridge, evaluation, or count failure clears the namespace
and rethrows.

## Offline evidence

Run from the worktree:

```powershell
node --check .superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v57-vm-module-source.js
node --check .superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v57-vm-module-executable.mjs
node --check .superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v57-vm-module-loader-cell.js
node --check .superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v57-vm-module-pure-fixtures.mjs
node --experimental-vm-modules .superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v57-vm-module-pure-fixtures.mjs
```

Fresh result:

```json
{"result":"PASS","executableBytes":27336,"executableSha256":"48DD581AE424042D42002AA8D32D017B7156A65CEE729A983BFB878200051A38","sourceBytes":47611,"sourceSha256":"0920D1D410C8109446B565340777D14190A0850222A0970E63CDF653B537A290","fixtureBytes":45054,"fixtureSha256":"45C4918DA62D810D984244E94CC67043CCDB642503F0A178794C7C4E0CDC3900","loaderBytes":2553,"loaderSha256":"23477C4DC06262AD25CE28D270B767A804DF55A7598D379EB74A560F55AC06D7","moduleExports":7,"moduleExecutions":1,"syntheticBridges":1,"allowlistedBrowserImports":1,"loaderCases":14,"predecessorContaminations":140,"inheritedBehavioralExecutions":212,"behavioralExecutions":220,"terminalOutputCleanup":true,"completeCounterVector":true}
```

The fixture uses real VM modules under Node's experimental VM-modules flag. It
proves one successful source evaluation, one synthetic bridge, one exact host
import, seven retained exports, 212 inherited behaviors, eight new
contamination stops, and thirteen failure paths plus success. Failure coverage
includes size, hash, ASCII, read, VM shape, parse, static import, wrong and
duplicate dynamic imports, host import, bridge shape, evaluation, bridge count,
and namespace cleanup. It performs no CUA, browser, provider, network,
clipboard, credential, secret, DNS, VM-host, or live-resource action.

## Later gate

Independent review and classification are required before any V57 loader or
candidate execution. A future sole owner must revalidate exact bytes, path,
runtime capability, browser/profile/tab, provider object, exclusive control,
and the governing one-shot contract. This package does not authorize import,
browser effect, token creation, copy/paste, deletion, or any V56 action.
