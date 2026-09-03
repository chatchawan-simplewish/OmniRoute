# OmniRoute V54 current token-table readiness Sol High implementation/security review

Date: 2026-09-03 (Asia/Bangkok)
Reviewer: Codex, independent `gpt-5.6-sol` High implementation/security review
Reviewed implementation commit: `25a99b52d276d4c11ca954e43b5d729f7ef20e7f`
Direct parent / V54 design-review commit: `ccdc1a0d2acae2e76e13c09cee55965a9e5ff85d`
V53 live-incident commit: `52a9096db642322a64cf9edeedaa6822ed8359b4`

## Verdict

`FAIL`

`classification_may_begin=false`

`authorizes_live_execution=false`

The committed candidate is byte-consistent with its source and the runtime is
fail-closed on the reviewed paths, but the pure fixture does not establish the
required current-table semantics or assertion-derived cleanup/counter evidence.
Those evidence gaps must be fixed and independently re-reviewed before a
classification may begin.

## Direct committed-byte tuple

Commit `25a99b52d` is the direct child of `ccdc1a0d2` and changes exactly the five
assigned V54 files. Direct Git-object reads produced:

| Artifact | Git blob | Bytes | SHA-256 | ASCII |
| --- | --- | ---: | --- | --- |
| Design | `c20f4b47eeea2e177bdc2d141d93d5b035a8c346` | 5291 | `06E79FB51FA5F90D7F59812FB4CBCD5A6D3A105DEA3756A1FE4FA2FEF9E74B77` | yes |
| Executable | `62cc17088904ed4244ac398b3204452ff3d6200c` | 24311 | `B85D778166B7A58CB1494DCD89B54C7FD1C40440ACA6026854B5751DEB4AD79A` | yes |
| Pure fixture | `9670f5255283d8b385c4f9512c7a9e06cccbf2fb` | 13809 | `E05128A5AA05FD9CBA33D0BEA558A00242A51DE9D03F557177D141D10CFE458A` | yes |
| Review package | `e29ee9837210800ef31bf48420b85241ea895a7c` | 4352 | `55FFF7D2C75B1E9F5E80CD56E5186595AE01727B9D17EF6E21BE752A742E0BC8` | no |
| Normalized source | `b9ed2ed0d69af0d7253f3efe83a1b4d76797dc69` | 43245 | `54E006ECBD2496D8FC076D21394C03935D9F54349FB7F3FD91E8D06C782EAD33` | no |

The approved V54 design review is blob
`21262edb91bf0f714f9d698ab82fc4d1bb11a6dc` (4484 bytes, SHA-256
`B6F0E169578F9534CAF69F4012DE190282EBCECB1225FB5993E06822756A69B9`).
The V53 incident is blob `477327dff8927d58d9d845aaf2911db8fc6cc34b`
(3264 bytes, SHA-256
`3D3507CE19F6218E5A8B33386119F80FD1657556061064F54447F31D781D9BD2`).

## Verified implementation properties

A scoped offline direct-blob minification check, using the committed fixture's
exact Terser options, reproduced the executable byte-for-byte from the committed
normalized source: `24311 == 24311`. The candidate is ASCII and below the
reviewed 25,000-byte ceiling.

Static committed-source inspection found exactly 125 predecessor `typeof ... ===
"undefined"` guards, all unique: the retained 118 V35-V51 names plus all seven
V53 persistent names. The fixture executes candidate-derived bytes and iterates
all 125 names, requiring each contamination to stop before setup or tab listing.

The attachment logic preserves the V53 source projection, pinned import/API and
documentation signatures, bounded ordinary-array descriptor validation, unique
literal-URL selection, claimed-ID equality, account-home signature, exact
operation counters, success-only retention, and failure cleanup. The downstream
logic uses the exact search ID, one matching visible table, bounded/non-busy
baseline, exact target fill, exact filtered URL semantics, exact no-results row,
zero target/Actions residue, one Create control, exact counters, and full binding
cleanup on ordinary or final-output failure.

The committed source contains one import, one tab listing, one claim, the two
reviewed navigations, and one target fill. Static checks found zero occurrences
of the prohibited click/check/type/press/select/clipboard/close/new-tab/storage/
cookie/eval call strings. No live browser, provider, network, DNS, VM, clipboard,
credential, secret, or external action was performed during this review.

## Findings

### V54-IMP-001 — IMPORTANT — Current-table DOM semantics are not behaviorally tested

The fixture's table `evaluate` stub ignores the candidate-supplied callback and
returns precomputed `config.baseline` or `config.terminal` objects. Consequently,
the reported behavioral executions do not exercise the committed DOM logic that
derives header order, busy state, body-row bounds, exact target-cell count,
normalized terminal-row text, or Actions residue. A defect in those callbacks
can coexist with a green fixture.

The required matrix is also incomplete despite the broader claim in the review
package: there is no duplicate-search case (`searchCount: 2`), missing-table case
(`tableCount: 0`), non-empty busy-table case, or duplicate-Create case. The
fixture therefore does not prove the design's duplicate/missing/wrong input and
control requirements or its malformed/duplicate/busy/empty/oversized table
requirements.

Required fix: make the fixture invoke the exact candidate-supplied evaluation
callbacks against controlled table/input DOM doubles (or an equivalent pure DOM
harness), and add explicit distinct cases for every required current-table
variant, including duplicate and missing search/table/Create controls, wrong
input/control shape, header/order errors, busy non-empty data, row bounds,
pre-existing target, query variants, terminal-row variants, and target/Actions
residue.

### V54-IMP-002 — IMPORTANT — Cleanup and exact-counter claims are not assertion-derived

The success case asserts one complete counter vector, but failure cases assert
no attempted/fulfilled vector and the hostile-throw matrix omits count/read
operations after the waits, including search/table/no-results counts and Create,
name, and row reads. Thus the fixture does not prove earliest-stop behavior and
exact counters across the permitted stages.

For final-output failure, the fixture asserts only that an error was caught, the
mock write failed, and no object output was captured. It does not inspect the
seven persistent bindings or any cleanup evidence after that failure. The final
JSON nevertheless emits literal `terminalOutputCleanup: true` and
`completeCounterVector: true`; those fields are claims rather than results of
the missing assertions.

Required fix: instrument each candidate operation uniquely, add hostile throws
and exact attempted/fulfilled-vector assertions for every read/count stage, and
make both ordinary-failure and terminal-output cleanup proofs observe all
persistent/runtime/tab bindings after execution. Emit the two PASS fields only
after those assertions derive them.

## Severity counts

- Critical: 0
- HIGH: 0
- IMPORTANT: 2
- Minor: 0
