# OmniRoute V54 current token-table readiness fix-1 Sol High re-review

Date: 2026-09-03 (Asia/Bangkok)
Reviewer: Codex, independent `gpt-5.6-sol` High implementation/security re-review
Reviewed fix commit: `9d6719fb5d3321f8e6a33b87a95bf5072b2133f9`
Direct parent / failed implementation package: `25a99b52d276d4c11ca954e43b5d729f7ef20e7f`
Approved V54 design-review commit: `ccdc1a0d2acae2e76e13c09cee55965a9e5ff85d`

## Verdict

`FAIL`

`classification_may_begin=false`

`authorizes_live_execution=false`

V54-IMP-001 is resolved. V54-IMP-002 is substantially improved but remains
open because ordinary-failure cleanup still lacks an independent probe of the
attachment/runtime/browser/tab locals. Classification must not begin until the
remaining evidence gap is fixed and re-reviewed.

## Direct committed-byte evidence

Commit `9d6719fb5` is the direct child of the failed package and changes only the
V54 source, executable, pure fixture, review package, and committed prior review.
Direct Git-object reads produced:

| Artifact | Git blob | Bytes | SHA-256 | ASCII |
| --- | --- | ---: | --- | --- |
| Source | `eb481cd0b7ab7326a9782d2691c42d937d4fe833` | 43477 | `29E41E2BCA86AC60C82AF5D360E0F9C1E17170ABAACF2124E21D08000AD379AD` | no |
| Executable | `c36c64d58d54e2d59d3a776e0fc725e723d93687` | 24436 | `794D23BD77254822FF02DA1EF9A66ACD2049DB6BEDBA2B8C46F7FCEFADA79DA6` | yes |
| Pure fixture | `3329119595fafe8be20f7679660ece5423145861` | 26654 | `638DBA5921210850C677221363C5187E7918CF998E7A36A5852FD9CF8CE23A9D` | yes |
| Review package | `b9915b276f137fb0cf8f616c80bdee216fa873e6` | 4976 | `C4B0C7A45EA9B3923A42C5329CB59FE1644B05B37B2F51882BF3F428188B9954` | no |
| Prior Sol review | `2f7ee7876fc7033c01de94dea37b808e650e2ded` | 6477 | `C6521833FF12AC4E02EE17B4C75A6282E187266915DC331AD42F9BE76FFB12A0` | no |

The V54 design remains blob `c20f4b47eeea2e177bdc2d141d93d5b035a8c346`,
5291 bytes, SHA-256
`06E79FB51FA5F90D7F59812FB4CBCD5A6D3A105DEA3756A1FE4FA2FEF9E74B77`.

A scoped offline `node --check` and exact pure fixture run completed with:

```json
{"result":"PASS","executableBytes":24436,"executableSha256":"794D23BD77254822FF02DA1EF9A66ACD2049DB6BEDBA2B8C46F7FCEFADA79DA6","sourceBytes":43477,"sourceSha256":"29E41E2BCA86AC60C82AF5D360E0F9C1E17170ABAACF2124E21D08000AD379AD","fixtureBytes":26654,"predecessorContaminations":125,"behavioralExecutions":195,"terminalOutputCleanup":true,"completeCounterVector":true}
```

This check is pure and mock-backed. No CUA, live browser/provider, network, DNS,
VM, clipboard, credential, secret, or external action occurred.

## Prior findings

### V54-IMP-001 — IMPORTANT — ADDRESSED

The fixture now passes the exact candidate-supplied input and table `evaluate`
callbacks controlled DOM doubles. It derives, rather than precomputes, header
order, busy state, body-row bounds, exact target counts, normalized terminal-row
text, and Actions residue.

The matrix now includes missing and duplicate search/table controls, wrong input
tag/type/disabled state, malformed header order, empty/oversized/busy/nonempty
tables, pre-existing target, absent/duplicate/wrong terminal rows, filtered busy/
target/Actions residue, complete wrong-host/path/fragment/extra/duplicate query
variants, missing/duplicate/mixed/hidden Create controls, and button-only and
link-only success. The source also makes the input tag/type/enabled check and
unique visible button-or-link Create locator explicit.

### V54-IMP-002 — IMPORTANT — PARTIALLY ADDRESSED

The fixture now uniquely instruments the candidate operations and compares
candidate attempted/fulfilled vectors with independent mock-effect vectors for
success, all ordinary failures, all 125 unique predecessor contaminations, and
hostile throws through search/table/no-results counts plus Create/name/row reads.
The seven persistent V54 bindings are independently probed on PASS and ordinary
failure. Candidate-derived injected probes also directly establish all
persistent, attachment, runtime/browser, and tab cleanup after documentation-
output and final-output failures.

One required proof remains absent. For every ordinary failure, `run()` selects
`executableWithProbe`, whose appended probe captures only the seven persistent
bindings. The attachment/runtime/browser/tab bindings are lexical locals inside
the candidate IIFE and are not included in that probe. The ordinary-failure loop
instead trusts the candidate's own `predecessorRuntimeCleared` and
`failureCleanupComplete` output booleans. Those booleans are useful internal
evidence but are not an independent post-cleanup observation of the locals, as
required by V54-IMP-002 and this fix-round scope.

Required fix: add one uniquely located candidate-derived ordinary-failure probe
at the post-cleanup/pre-output boundary that directly captures attachment tab,
attachment eligibility, runtime setup, agent, and browser nullness together with
all seven persistent bindings. Assert that probe for every ordinary and hostile
failure, and derive the cleanup PASS field only after those assertions.

## Retained implementation/security conclusions

The exact candidate remains ASCII and below the 25,000-byte direct-cell ceiling,
and the fixture proves exact source-to-candidate minimization. All 125 predecessor
guards/contaminations remain unique and stop before setup or tab listing. The
reviewed pins, one-shot/no-retry boundary, exact URL and table semantics, success-
only retention, sanitized output, and prohibited-effect absence remain intact.

## Severity counts

- Critical: 0
- HIGH: 0
- IMPORTANT: 1
- Minor: 0
