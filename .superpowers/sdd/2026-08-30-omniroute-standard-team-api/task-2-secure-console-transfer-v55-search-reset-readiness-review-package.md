# OmniRoute V55 direct-byte implementation review package

`authorizes_live_execution=false`

## Scope and lineage

This package covers only the V55 source, generated ASCII executable, and pure
fixture. It implements the approved V55 design at `3d2caf86b` and final Sol
PASS classification at `045bd275b`, reusing the final-reviewed V54 trust
boundary as the minimum delta. V54 remains spent and is neither retried nor a
fallback.

## Candidate facts

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| V55 source | 46758 | `ABFE257FCD6EEA7F128621ACEC40F1773B5EF54DE20C394334B193EF8CB4F889` |
| V55 executable | 26597 | `A9692FFBB688DB244566FCE68D84C08686A7B1D0D4D0FAA587187D8135FB286A` |
| V55 pure fixture | 33256 | `4DCB11F11620575C9EF12B26FCC728ED82385ACA1752052222304F2DF6AC5B51` |

The executable is the Terser output of the V55 source with `evaluate:false`,
ASCII-only formatting, and all seven V55 persistent names reserved. It contains
the fixed source projection `10619` / `89D36435A31AE04E560A27D53D8A0953F19E837DF60837FADCF3DC174C0B9477`,
all 132 predecessor declaration guards (125 inherited plus the seven V54
globals), and `String.fromCodePoint(0x1F510)+" OmniRoute secure console"`.
It contains no literal emoji or `\\uXXXX` escape; control rejection uses ASCII
`\\x00` ranges. Reset convergence uses exact `waitForURL` with a 20-second
bound, then a separately counted URL read.

The only runtime delta is conditional one-time empty reset followed on both
branches by exact base-URL, hidden/detached sentinel, final-empty-input, and
full baseline convergence before the retained target selection. Reset failures
keep local binding `1/1` when reached, clear persistent state, and fail closed.

## Offline evidence

Run from the worktree:

```powershell
node --check .superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v55-search-reset-readiness-source.js
node --check .superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v55-search-reset-readiness-executable.js
node --check .superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v55-search-reset-readiness-pure-fixtures.mjs
node .superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v55-search-reset-readiness-pure-fixtures.mjs
```

The pure fixture regenerates and compares candidate bytes, checks syntax and
ASCII, exercises empty and stale-reset success, reset/retained earliest
failures, trusted-listing variants, 132 inert contaminations, counter vectors,
ordinary/documentation/final-output cleanup, sanitized output, and an
independently seeded stale input/query/table state. Its candidate-derived stale
case proves clear changes only input before `waitForURL`, then exact settlement
restores base URL, hidden/detached sentinel, and full rows. A separate exact
base-URL/filtered-table case proves visible sentinel residue stops at
`resetSentinelWait 1/0` before final input, baseline, target, Create, or
retention. Timeout, wrong settlement, reset-read, and sentinel throw/read stops
retain their exact counter and cleanup vectors. It also retains prohibited
effects. Its result is `PASS`; it performs no CUA, browser, provider, network,
DNS, VM, clipboard, credential, secret, or live action.

## Later gate

No literal-cell capacity proof is claimed here. Before any future send, the
coordinator must independently compare the literal cell UTF-8 bytes and
SHA-256 to the committed executable and satisfy the approved self-verification
gate. Mismatch, absence, ambiguity, or higher-priority policy stops before
import/browser effect. Independent Sol implementation review and classification
remain required; final Create/copy/paste and row deletion remain external
confirmations.
