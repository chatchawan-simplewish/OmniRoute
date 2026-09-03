# V57 in-memory VM-module replacement design

`authorizes_live_execution=false`

## Replacement and incident lineage

V56 was sent exactly once and failed safely before candidate parsing or
execution because the CUA `node_repl` rejects `data:` import specifiers. V56 is
permanently spent and may not be retried, continued, reused, or used as a
fallback. Its cleanup passed and its retained namespace was null.

A later disposable-realm diagnostic proved `node:vm.SourceTextModule` and
`SyntheticModule` are available and can perform one in-memory module evaluation
with one allowlisted bridged dynamic import. That check was diagnostic only.
V57 is the new offline replacement and authorizes no live action.

## Candidate

The V57 source is mechanically derived from final V56 by renaming V56 globals
and result labels to V57, then adding freshness guards for the seven V56
exported global names plus `secureConsoleV56Module`. The predecessor block has
exactly 140 names: the inherited 132 V35-V54 names plus these eight V56 names.

The generated ASCII ESM exports the seven V57 continuation bindings: owned tab,
eligible flag, state, pre-Create and post-native detach-consumed flags,
Cloudflare-reads-consumed flag, and V57-consumed flag. All V56 readiness,
counter, output, and cleanup behavior is retained under V57 labels.

## Loader

The ASCII loader reads the exact V57 executable path once with `node:fs` and
requires its pinned byte count, SHA-256, and ASCII bytes. It creates one
`SourceTextModule` directly from that verified Buffer decoded as UTF-8; there is
no file reopen or `data:` URL.

The source module rejects every static import at link time. Its dynamic-import
callback accepts only the exact pinned browser-client file URL and only once.
The callback imports that host module once, validates only
`setupBrowserRuntime`, and returns one linked/evaluated `SyntheticModule` that
exports only that function into the isolated context. The V57 source module is
evaluated once and must consume exactly one bridge. Only then is its namespace
retained at `globalThis.secureConsoleV57Module`.

The namespace starts null and is reset to null on read, shape, hash, ASCII,
parse, link, bridge, evaluation, or count failure. There is no retry, fallback,
alternate specifier, second candidate read, path import, or continuation after
failure.

## Offline fixtures

Pure fixtures run with Node's VM-modules flag. They derive source and executable
bytes mechanically, prove ASCII/ESM syntax, exactly 140 predecessor names,
seven exports, the inherited 212 behaviors plus eight new contamination stops,
and all prior counter/output/cleanup cases.

The loader fixture uses real `SourceTextModule`, `SyntheticModule`, and
`createContext` while replacing file and browser-client effects with in-memory
doubles. It proves the exact candidate success path has one read, one source
module evaluation, one exact allowlisted host import, one synthetic bridge, and
global namespace retention. Failure cases cover read, VM shape, size, hash,
ASCII, parse, static import, wrong and duplicate dynamic import, bridge import,
evaluation/count, and cleanup. No fixture uses CUA, browser, provider, network,
clipboard, credential, secret, DNS, VM host, or live-resource access.

Independent review and classification remain mandatory before any future V57
execution or token action.
