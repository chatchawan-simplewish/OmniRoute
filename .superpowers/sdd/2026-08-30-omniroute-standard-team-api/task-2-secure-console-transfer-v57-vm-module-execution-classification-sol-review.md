# OmniRoute V57 VM-module execution-classification Sol High review

Date: 2026-09-03 (Asia/Bangkok)
Reviewer: Codex, independent `gpt-5.6-sol` High security review
Reviewed commit: `6cdc043d59116c2184e1c660d4c1cd50f69b3d08`
Required parent: `4e5b5a05dbff89c58eb4f70d6e3329790ec5d527`

## Verdict

`FAIL`

`classification_may_execute=false`

`authorizes_live_execution=false`

The classification reproduces the committed V57 evidence and preserves its
security boundaries, but it omits one design-required action-time precondition:
fresh proof that the actual CUA execution realm still exposes the VM-module
capabilities on which this replacement depends. Executing as written could
irreversibly spend V57 on the same category of unpinned runtime-capability drift
that spent V56.

## Direct committed-byte and lineage evidence

Direct Git-object inspection proves `6cdc043d5` has exactly one parent,
`4e5b5a05d`, and exactly one changed path:
`task-2-secure-console-transfer-v57-vm-module-execution-classification.md`.
The classification is Git blob `b251fc3d58dca9820feaecf0fab697e936cf5bb0`,
5038 bytes, ASCII-only, with SHA-256
`235B5F44DC17AC7DF7335BA7072B11319D23FB213CED31AF1FCADB12C5350253`.

Its exact prior tuple is correct:

| Artifact | Git blob | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| Design | `47d06491ad9cb3fb70680174c1943c8b82a4c2f4` | 3370 | `C6DC6629880B074EA3B5875A9D238BCAFB9997485C7E232109EE032A92B0E649` |
| Source | `5a07e532c75e1dd6da7b07c82460f5e97c4d27f5` | 47611 | `0920D1D410C8109446B565340777D14190A0850222A0970E63CDF653B537A290` |
| ESM executable | `b3374909a13fa43bab349de7c342b8fe9afa69ea` | 27336 | `48DD581AE424042D42002AA8D32D017B7156A65CEE729A983BFB878200051A38` |
| Loader cell | `78c4455ee3039ea5579f478d7ec467711d04375e` | 2553 | `23477C4DC06262AD25CE28D270B767A804DF55A7598D379EB74A560F55AC06D7` |
| Pure fixture | `5f35202767961f24ce275dc7e6107bc04e394fc3` | 45054 | `45C4918DA62D810D984244E94CC67043CCDB642503F0A178794C7C4E0CDC3900` |
| Review package | `b2a763834ded2163b7058d836c548961deafd093` | 5238 | `3507229D1DDFF242E7FE889E14E157E011CF7CF683E67DEA99D702E7935117AA` |
| Sol PASS | `23514b95979ecff5f617471995067de092430123` | 6428 | `FE9A9E879CA7A1964C47EFA6D2088EAFB7811A7D6F132E6128AC2B075D1B2302` |

The PASS chain is exact: V56 spent incident `12df94b3c`, V57 implementation
`695aa10ad`, and sole-path Sol High review PASS `4e5b5a05d` with Critical `0`,
HIGH `0`, IMPORTANT `0`, Minor `0`. The V56 incident records one unsupported
`data:` import, no candidate parse/evaluation or browser/provider effect,
namespace-null cleanup, and permanent no-retry/no-fallback status.

## Retained correct boundaries

The classification accurately states the loader semantics: one executable
read; exact byte-count, SHA-256, and ASCII verification of that Buffer; one
`SourceTextModule` evaluation from the same decoded bytes; static imports
rejected; exactly one allowlisted browser-client dynamic import; one
`SyntheticModule` exporting only `setupBrowserRuntime`; exactly one bridge;
namespace retention only on complete success; namespace-null cleanup and
rethrow on every failure; and no path reopen, alternate import, transformation,
retry, continuation, or fallback.

It correctly scopes V57 to one send/evaluation attempt and read-only token-page
readiness. It permits navigation, reads, the fixed non-secret search fill, and
counts, but forbids Create activation, token creation, Copy, clipboard,
credential/secret access, storage/cookies, provider/DNS/routing/VM mutation,
tab creation/close/reconnect, retry, override, verdict relaxation, or manual
continuation.

The source-projection, browser-client, documentation, baseline/index,
evidence-worktree, residue, DNS, and VM pins are carried forward exactly. A
local offline read reproduced the browser-client 150611-byte/hash pin and the
documentation 59294-byte/hash pin. Browser/profile/tab and disjoint-lane facts
are correctly self-verified from current tool state under the project rule;
no redundant manual owner response is required for this routine read-only
selection. Persistent API-token creation remains a later, separate mandatory
Computer Use action-time confirmation.

## Finding

### V57-CLASS-IMP-001 — Missing action-time VM-module capability proof

Severity: IMPORTANT

The V57 design requires a future sole owner to revalidate “runtime capability”
before execution. V57 exists specifically because the prior loader's assumed
module-loading mechanism was unsupported in the CUA `node_repl`. The only
positive evidence for the replacement mechanism is an earlier disposable-realm
diagnostic plus the offline Node fixture.

The classification's retained runtime pin is only the browser-client file's
bytes/hash. Mandatory condition 2 requests “runtime/docs” pins but defines no
current CUA VM-module capability result, while condition 3 checks predecessor
globals and namespace freshness only. Neither condition proves, in the exact
fresh realm that would receive the one loader send, that `createContext`,
`SourceTextModule`, and `SyntheticModule` are still functions and usable under
the realm's active Node flags. The loader's own shape check is fail-closed, but
it happens after the consuming send; failure would permanently spend V57.

Required fix: amend the mandatory action-time conditions to require a
sanitized, non-mutating capability probe in the same freshly reset target realm,
after the required first `await cua.getState();` and before the loader send,
proving `node:vm.createContext`, `node:vm.SourceTextModule`, and
`node:vm.SyntheticModule` are functions. Bind that proof to the same realm and
stop before sending the loader on any unavailable, ambiguous, or malformed
result. Retain all existing 140-name freshness, exact-byte, one-shot, cleanup,
browser-lane, and separate token-confirmation gates. A corrected classification
requires independent fix review before execution.

No CUA, browser/provider, network, DNS, VM-host, clipboard, credential, secret,
or live action was performed. The previously passing implementation fixture was
not rerun because the finding is confined to the classification contract.

## Severity counts

- Critical: 0
- HIGH: 0
- IMPORTANT: 1
- Minor: 0
