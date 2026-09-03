# OmniRoute V57 VM-module execution classification

`authorizes_live_execution=false`

## Evidence classified

- V56 spent live incident: `12df94b3c`.
- V57 implementation: `695aa10ad`.
- Independent Sol High PASS: `4e5b5a05d`; Critical `0`, HIGH `0`,
  IMPORTANT `0`, Minor `0`.

The V56 candidate never executed. Its unsupported `data:` import failed before
browser/runtime activity, cleanup passed, and its realm was reset. V57 is a new
replacement and never retries or continues V56.

## Exact reviewed tuple

| Artifact | Bytes | SHA-256 | Git blob |
| --- | ---: | --- | --- |
| Design | 3370 | `C6DC6629880B074EA3B5875A9D238BCAFB9997485C7E232109EE032A92B0E649` | `47d06491ad9cb3fb70680174c1943c8b82a4c2f4` |
| Source | 47611 | `0920D1D410C8109446B565340777D14190A0850222A0970E63CDF653B537A290` | `5a07e532c75e1dd6da7b07c82460f5e97c4d27f5` |
| ESM executable | 27336 | `48DD581AE424042D42002AA8D32D017B7156A65CEE729A983BFB878200051A38` | `b3374909a13fa43bab349de7c342b8fe9afa69ea` |
| Loader cell | 2553 | `23477C4DC06262AD25CE28D270B767A804DF55A7598D379EB74A560F55AC06D7` | `78c4455ee3039ea5579f478d7ec467711d04375e` |
| Pure fixture | 45054 | `45C4918DA62D810D984244E94CC67043CCDB642503F0A178794C7C4E0CDC3900` | `5f35202767961f24ce275dc7e6107bc04e394fc3` |
| Review package | 5238 | `3507229D1DDFF242E7FE889E14E157E011CF7CF683E67DEA99D702E7935117AA` | `b2a763834ded2163b7058d836c548961deafd093` |
| Sol PASS | 6428 | `FE9A9E879CA7A1964C47EFA6D2088EAFB7811A7D6F132E6128AC2B075D1B2302` | `23514b95979ecff5f617471995067de092430123` |

The ASCII loader reads the executable once, validates exact bytes, SHA-256,
and ASCII, then evaluates that same verified string once with
`node:vm.SourceTextModule`. All static imports are rejected. Exactly one dynamic
import of the exact pinned browser-client URL is allowed and bridged through a
`SyntheticModule` exporting only `setupBrowserRuntime`. Every failure clears
`globalThis.secureConsoleV57Module` and rethrows; there is no retry, path reopen,
alternate import, transformation, or fallback.

## Classification

V57 is conditionally eligible for exactly one live loader execution by this
task as sole Sol High owner after all action-time checks pass. One loader send,
evaluation attempt, failure, uncertainty, malformed output, or cleanup doubt
spends V57 permanently.

The candidate retains the V55/V56 read-only Cloudflare attachment and current
token-table readiness logic, now with 140 predecessor guards, seven exported
continuation bindings, 212 inherited behavioral executions, 220 total fixture
executions, and 14 loader cases. It may navigate/read the signed-in dashboard
and fill only the fixed non-secret token-name search string. It counts but never
activates Create Token.

V57 authorizes no Create click, token creation, Copy, clipboard, secret or
credential access, storage/cookies, DNS/routing/VM/provider mutation, tab
creation/close, reconnect, retry, fallback, alternate selector/URL, override,
verdict relaxation, or manual continuation.

## Retained action-time pins

- Source projection: `10619` records at
  `89D36435A31AE04E560A27D53D8A0953F19E837DF60837FADCF3DC174C0B9477`.
- Browser client: `150611` bytes at
  `B9B9BC2319D5EE6AA0B1E481D63BB2130D28102FC7C9080803AB5552185D9037`.
- Documentation: `59294` bytes at
  `FC7966FFBC9010252AD3EA745E061068BEC3919EFFF860A87E6013A38A7E277F`.
- Empty index and exact inherited 12-path product baseline.
- Clean evidence worktree at `80adaa7d5d63d1d2c7bfa63b236c6bee93b3b1d8`.
- Zero Windows temporary-root/process residue and zero public A/CNAME results
  for `ai-api-omniroute.mysw.me` through `1.1.1.1` and `8.8.8.8`.
- VM1205 safe checkpoint: retained services running, target containers absent,
  network members `2`, Caddy SHA-256
  `a31c2010bb47767e25a826cebcd2469cb51d8af5c5ae089e46d2051edd69d9bb`,
  listener `20130` absent.

## Mandatory action-time conditions

Immediately before the one V57 send, prove:

1. a post-commit tuple shows this classification commit has sole parent
   `4e5b5a05d` and changes only this path, while reproducing the reviewed tuple;
2. syntax and fixture PASS, empty index, exact 12-path baseline, projection,
   runtime/docs, evidence worktree, DNS, residue, and VM pins;
3. a fresh CUA realm whose first call is exactly `await cua.getState();`, then
   a same-realm fixed capability check proving `createContext`,
   `SourceTextModule`, and `SyntheticModule` are functions, followed by a
   direct audit proving all 140 predecessors plus
   `secureConsoleV57Module` absent;
4. current state proves Chrome profile `Codex-Chrome-Bell-PC2`, exactly one API
   Tokens tab at the exact URL, and a disjoint provider/tab lane; and
5. loader bytes exactly match this tuple before the sole send.

Routine browser verification is tool-driven under the confirmed project rule.
Persistent API-token creation remains a later Computer Use action-time
confirmation; secret transmission, deletion, and other irreversible actions
remain separately gated.

## Non-self-reference boundary

This document classifies only prior committed evidence. Its own commit, blob,
bytes, and SHA-256 must be established by a later coordinator tuple.
