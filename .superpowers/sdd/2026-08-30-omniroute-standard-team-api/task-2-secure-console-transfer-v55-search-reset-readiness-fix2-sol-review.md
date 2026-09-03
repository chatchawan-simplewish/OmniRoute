# OmniRoute V55 search-reset readiness fix-2 Sol High implementation/security re-review

Date: 2026-09-03 (Asia/Bangkok)
Reviewer: Codex, independent `gpt-5.6-sol` High implementation/security re-review
Reviewed fix commit: `c22158bff28af7f4b4734e914a4bcc545ebb6746`
Parent / fix-1 review: `0cd7d08b3a07179b0f155aa10d693e1133a385aa`
Original implementation review: `8d8e7d3f24ccac7c5924ee45cf7dfe9de8fea435`
Approved V55 design / design PASS: `3d2caf86b2b3314e5f531c243c74c714640f42fa` / `045bd275b39bf70dc1cbfb41e81ec396ac61593b`

## Verdict

`FAIL`

`fix_may_proceed=true`

`capacity_proof_may_proceed=false`

`classification_may_begin=false`

`authorizes_live_execution=false`

The positive incident transition required by `V55-IMP-002` is now modeled:
the fixture independently seeds stale input, query URL, and filtered table;
captures the clear-only state; and later converges URL and table/sentinel before
full-baseline success. However, the approved design also requires a semantic
sentinel-residue negative. No executed case reaches the sentinel wait with the
exact base URL settled while the table remains filtered/visible. One IMPORTANT
fixture-coverage finding therefore remains.

## Direct committed-byte and lineage evidence

`c22158bff` is the direct child of the fix-1 review commit `0cd7d08b3` and
modifies exactly the V55 pure fixture and review package. Direct Git-object
reads produced:

| Artifact | Git blob | Bytes | SHA-256 | ASCII |
| --- | --- | ---: | --- | --- |
| Source | `7fbcdeb98312cb021c4d3dbf44c7ec665c4601cf` | 46758 | `ABFE257FCD6EEA7F128621ACEC40F1773B5EF54DE20C394334B193EF8CB4F889` | yes |
| Executable | `4614b61ce3e0a26a8d2e5ad1c77ef9ba220b82b9` | 26597 | `A9692FFBB688DB244566FCE68D84C08686A7B1D0D4D0FAA587187D8135FB286A` | yes |
| Pure fixture | `b61a72a1c31ae926298d92c16ed273e60d56729a` | 32289 | `3E1D9886F44960B44FC831AC0AD7B1C55770E91248134DE3FDC4C0122871F486` | yes |
| Review package | `7493b7713b70759e88a99dced2320d54b90260b1` | 3587 | `C53CE245DDD153319E060E8DF0F7C88685405E4D6F38C4AC272FE73E601CF304` | yes |

The source and executable Git blob IDs, byte sizes, and SHA-256 values are
identical to `dfaee613f`, so fix-2 makes no runtime/candidate-byte change. The
approved design is blob `da6c4e996faf9baaa91d95cf0798aab73f1ff675`,
5214 bytes, SHA-256
`90D04C01DDCCA2B6C05D228AA0BDA0A4B6A20EDD72B6C9891A8453922224FC7F`.
The committed fix-1 review is blob
`c7f92d9898155f03ec785fba8f24a57f38611d67`, 6641 bytes, SHA-256
`CEC3B147472F2EA0FFD4F4063D7A848EB75DF7AEB3645EB3A5BE682157429B48`.

## Scoped offline result

Fresh syntax checks of source, executable, and fixture plus the complete pure
fixture run returned:

```json
{"result":"PASS","executableBytes":26597,"executableSha256":"A9692FFBB688DB244566FCE68D84C08686A7B1D0D4D0FAA587187D8135FB286A","sourceBytes":46758,"sourceSha256":"ABFE257FCD6EEA7F128621ACEC40F1773B5EF54DE20C394334B193EF8CB4F889","fixtureBytes":32289,"predecessorContaminations":132,"behavioralExecutions":208,"terminalOutputCleanup":true,"completeCounterVector":true}
```

This proves source-to-executable exact derivation, syntax/ASCII, 132 predecessor
contaminations, and the executed matrix. It does not prove a semantic case that
is absent from that matrix. No capacity, CUA, browser/provider, network, DNS,
VM, clipboard, credential, secret, or live action ran.

## Closed portion of V55-IMP-002

The fixture now has independent `initialValue`, `initialUrl`, and
`initialTableFiltered` inputs. Its candidate-derived stale success returns the
exact base URL to the runtime's navigation read, then injects a stale query URL
and filtered table before initial filter evaluation. Clearing records the exact
intermediate snapshot `{input:"", url:"...api-tokens?search=stale",
filtered:true}` without changing URL/table. The later candidate call to
`waitForURL` settles the URL to the exact base and the table to unfiltered; the
hidden sentinel wait, final-empty read, nine-row baseline, target filter, exact
counters, retained binding, and cleanup then pass.

Reset timeout and wrong-URL settlement cases retain `resetUrlWait 1/0`,
`resetUrlRead 0/0`, and all later reads `0/0`. Unique throw instrumentation
includes reset URL read, sentinel wait/read, final input, baseline, and later
target operations; assertion-derived counters and persistent cleanup remain.
Documentation-output and final-output cleanup plus sanitized output remain
covered. The source/executable retain the already closed transport and bounded
URL-wait findings without byte drift.

## Remaining finding

### V55-IMP-002 — IMPORTANT — semantic sentinel-residue negative is not executed

The design explicitly requires fixture coverage for `sentinel residue` and a
visible sentinel to fail before final-input, baseline, target filter, Create,
name, and row operations. The fixture can model this state through
`resetSettledUrl: tokenUrl` with `resetSettledTableFiltered: true`, but no test
runs that combination.

The sole non-default `resetSettledTableFiltered:true` occurs in the wrong-URL
case, paired with `resetSettledUrl: tokenUrl + "?search=stale"`. That case stops
inside `waitForURL` before the sentinel locator exists. The generic
`throwAt:"resetSentinelWait"` case proves exception counter handling, not that
the controlled locator double rejects an actually visible sentinel after exact
URL convergence. Consequently the review package's broad claim that the reset
matrix proves sentinel convergence is only positive-path evidence.

Required fix: add a candidate-derived failure case with exact reset URL and
`resetSettledTableFiltered:true`; assert `resetUrlWait 1/1`, `resetUrlRead 1/1`,
`resetSentinelWait 1/0`, all later reset/target counters `0/0`, failed persistent
state, full runtime cleanup, and sanitized output. Retain the existing direct
sentinel throw/read cases separately.

## Retained boundaries and capacity classification

The full existing missing/duplicate/wrong/busy/bounds/query/terminal/Create
matrix, exact counter framework, 132 guards, ordinary/documentation/final-
output cleanup, no retry, and prohibited-effect/secret boundaries remain. The
candidate remains 26597 bytes; the only prior inert proof remains 25351 bytes,
so capacity is still `INSUFFICIENT / NOT PASSED`. No new inert proof may run
until a zero-finding review closes the required fixture matrix; classification
may not begin.

## Severity counts

- Critical: 0
- HIGH: 0
- IMPORTANT: 1
- Minor: 0
