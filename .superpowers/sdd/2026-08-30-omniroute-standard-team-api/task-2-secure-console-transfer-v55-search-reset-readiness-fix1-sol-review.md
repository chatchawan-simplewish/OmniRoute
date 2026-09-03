# OmniRoute V55 search-reset readiness fix-1 Sol High implementation/security re-review

Date: 2026-09-03 (Asia/Bangkok)
Reviewer: Codex, independent `gpt-5.6-sol` High implementation/security re-review
Reviewed fix commit: `dfaee613ff6ccfe4a4463ca7774212adfd3bc3bf`
Parent / original implementation review: `8d8e7d3f24ccac7c5924ee45cf7dfe9de8fea435`
Approved V55 design / design PASS: `3d2caf86b2b3314e5f531c243c74c714640f42fa` / `045bd275b39bf70dc1cbfb41e81ec396ac61593b`

## Verdict

`FAIL`

`fix_may_proceed=true`

`capacity_proof_may_proceed=false`

`classification_may_begin=false`

`authorizes_live_execution=false`

`V55-HIGH-001` and `V55-IMP-001` are closed. `V55-IMP-002` is only
partially closed: reset wait/read operations and their earliest stops are now
distinct, but the fixture still does not instantiate the diagnosed state in
which the input is cleared while the URL and table remain stale. Fix that
candidate-derived coverage gap before running the new inert capacity proof.

## Direct committed-byte and lineage evidence

`dfaee613f` is the direct child of `8d8e7d3f2` and modifies exactly the four
V55 source, executable, pure-fixture, and review-package paths. Direct Git
object reads produced:

| Artifact | Git blob | Bytes | SHA-256 | ASCII |
| --- | --- | ---: | --- | --- |
| Source | `7fbcdeb98312cb021c4d3dbf44c7ec665c4601cf` | 46758 | `ABFE257FCD6EEA7F128621ACEC40F1773B5EF54DE20C394334B193EF8CB4F889` | yes |
| Executable | `4614b61ce3e0a26a8d2e5ad1c77ef9ba220b82b9` | 26597 | `A9692FFBB688DB244566FCE68D84C08686A7B1D0D4D0FAA587187D8135FB286A` | yes |
| Pure fixture | `0f5257763fc379a88a19056938a1d6e82038bf78` | 31113 | `1A49BF68D22A618075F996FD12ABAD500350DDB14F19FF7D46851BF4AD77604E` | yes |
| Review package | `c6ebe12e08caf49ece081242f138480822d6c2af` | 3343 | `6AE4AE39A6A9DCF1F7ECD573C7E5C2E057C9CF733904DA40E1974CAA11D4819E` | yes |

The pure fixture independently regenerates the executable with Terser
`evaluate:false`, ASCII-only output, and all seven V55 persistent names
reserved, then compares exact bytes. Scoped offline syntax checks and the pure
fixture passed:

```json
{"result":"PASS","executableBytes":26597,"executableSha256":"A9692FFBB688DB244566FCE68D84C08686A7B1D0D4D0FAA587187D8135FB286A","sourceBytes":46758,"sourceSha256":"ABFE257FCD6EEA7F128621ACEC40F1773B5EF54DE20C394334B193EF8CB4F889","fixtureBytes":31113,"predecessorContaminations":132,"behavioralExecutions":208,"terminalOutputCleanup":true,"completeCounterVector":true}
```

That result is valid for the cases the fixture runs; it does not cure the
missing stale-URL/stale-table state described below. No capacity, browser,
provider, network, DNS, VM, clipboard, credential, secret, or live action ran.

## Closed findings

### V55-HIGH-001 — closed

The committed executable is ASCII, contains zero `\\uXXXX` sequences and zero
non-ASCII code points, and contains exactly one
`String.fromCodePoint(128272)` construction. The source exact expression is
`String.fromCodePoint(0x1F510) + " OmniRoute secure console"`; the generated
candidate therefore names the exact `🔐 OmniRoute secure console` session
without literal emoji or Unicode escapes. All three identifier control guards
use ASCII `\\x00-\\x1f` / `\\x7f` ranges, so control rejection remains present.

### V55-IMP-001 — closed

The actual candidate requires `playwright.waitForURL` in the claimed-tab shape,
then invokes it exactly once with the exact base token URL and
`{timeoutMs:20000}`. Only fulfillment increments `resetUrlWaitFulfilled`; a
separately counted `adopted.url()` read follows, and its parsed `href` must equal
the exact base URL. Timeout or wrong settlement stops before reset URL read;
reset URL read failure stops before sentinel/final-input/baseline/target work.

The fixture now gives navigation URL read, reset URL wait, and reset URL read
unique instrumentation names. It exercises reset timeout, wrong settled URL,
and direct reset-read throw with assertion-derived counter vectors, ordinary
cleanup, and sanitized terminal output.

## Remaining finding

### V55-IMP-002 — IMPORTANT — fixture still does not model stale URL and stale table across clear

The V54 incident evidence requires the fixture to distinguish three states:
the filter input can become empty while the query URL and filtered/no-results
table remain stale, and only later converge. The revised fixture does separate
its variables, but it does not seed that state. On token-page navigation it
unconditionally sets `state.currentUrl = tokenUrl` and
`state.filtered = false`, even when `initialValue: "stale"`. The reset fill
then changes only `filterValue`; therefore its stale-reset success starts and
remains at the base URL with an unfiltered baseline table until `waitForURL`.

`resetConverges:false` likewise leaves the URL/table already at baseline. The
wrong-settlement case assigns a stale URL and filtered table inside the
`waitForURL` mock immediately before throwing, which tests wrong settlement but
not the incident transition or stale-then-converged success. No assertion
proves that, after the empty fill and before convergence, the URL is still the
stale query and the table/sentinel is still filtered/visible.

Required fix: give the input, URL, and table independent initial and settled
state controls; add a candidate-derived stale success that begins with all
three stale, proves the clear changes only the input, then allows exact URL and
table/sentinel convergence; retain independent timeout, wrong-settlement,
reset-read, sentinel, counter, and cleanup cases.

## Retained matrix and boundaries

The passing suite retains source-to-executable equality, syntax/ASCII checks,
the fixed `10619` / `89D36435...B9477` projection, 132 unique predecessor
contaminations, the empty and stale-field reset branches, counter vectors,
ordinary/documentation/final-output cleanup, and the missing/duplicate/wrong/
busy/bounds/query/terminal/Create matrix. Static checks retain the single
import/openTabs/claim/home navigation/token navigation/target fill calls and
absence of click, clipboard, storage, cookie, close, retry, provider mutation,
secret, DNS, and VM effects.

## Capacity classification

The stabilized candidate is `26597` bytes. The prior inert capacity evidence
was only `25351` bytes, so `25351 < 26597` and capacity remains
`INSUFFICIENT / NOT PASSED`. Per the requested gate, no capacity proof was run.
Because one implementation-review finding remains, a new proof may proceed
only after a zero-finding fix review stabilizes the final candidate bytes.

## Severity counts

- Critical: 0
- HIGH: 0
- IMPORTANT: 1
- Minor: 0
