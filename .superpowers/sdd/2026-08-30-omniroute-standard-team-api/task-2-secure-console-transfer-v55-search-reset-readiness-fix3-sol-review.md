# OmniRoute V55 search-reset readiness fix-3 Sol High implementation/security re-review

Date: 2026-09-03 (Asia/Bangkok)
Reviewer: Codex, independent `gpt-5.6-sol` High implementation/security re-review
Reviewed fix commit: `237b73ed0b0ae924c7be9d573976b11842de4992`
Parent / fix-2 review: `cf6fc3c4bf2c3e37b1f1a79f189cc585bcae6d5f`
Approved V55 design / design PASS: `3d2caf86b2b3314e5f531c243c74c714640f42fa` / `045bd275b39bf70dc1cbfb41e81ec396ac61593b`

## Verdict

`FAIL`

`fix_may_proceed=true`

`capacity_proof_may_proceed=false`

`classification_may_begin=false`

`authorizes_live_execution=false`

The remaining semantic sentinel-residue finding is closed: a candidate-derived
case reaches exact reset URL convergence while the filtered table/sentinel stays
visible, stops at `resetSentinelWait 1/0`, keeps every later counter `0/0`, and
proves full cleanup. One Minor evidence-accounting defect remains: the fixture
still reports 208 behavioral executions although its executable control flow
now performs 212.

## Direct committed-byte and lineage evidence

`237b73ed0` is the direct child of the fix-2 review commit `cf6fc3c4b` and
modifies exactly the V55 pure fixture and review package. Direct Git-object
reads produced:

| Artifact | Git blob | Bytes | SHA-256 | ASCII |
| --- | --- | ---: | --- | --- |
| Source | `7fbcdeb98312cb021c4d3dbf44c7ec665c4601cf` | 46758 | `ABFE257FCD6EEA7F128621ACEC40F1773B5EF54DE20C394334B193EF8CB4F889` | yes |
| Executable | `4614b61ce3e0a26a8d2e5ad1c77ef9ba220b82b9` | 26597 | `A9692FFBB688DB244566FCE68D84C08686A7B1D0D4D0FAA587187D8135FB286A` | yes |
| Pure fixture | `889be0b785b3430ceec406a7ed8ade1c1765c677` | 33256 | `4DCB11F11620575C9EF12B26FCC728ED82385ACA1752052222304F2DF6AC5B51` | yes |
| Review package | `3a0757bd1a3fa02385060f532dce4f2a3ceead64` | 3792 | `991B87AC57CF694F1AF0974A2EB24EB77C60E1625BCF25C3D700A79FC33A4993` | yes |

The source and executable blob IDs, byte lengths, and SHA-256 values are
identical to `dfaee613f` and `c22158bff`; fix-3 changes no runtime or candidate
byte. The parent fix-2 review is blob
`ec2fbbbd7c35990572e5e4db7d4272c9b2fd6c9d`, 6456 bytes, SHA-256
`2BC3E3F832CA374E3ACA03A43A5EF8B2FB72F37420DC6FDB881AA80C1AF2DD1F`.

## Scoped offline result

Fresh syntax checks of source, executable, and fixture plus the full pure
fixture returned:

```json
{"result":"PASS","executableBytes":26597,"executableSha256":"A9692FFBB688DB244566FCE68D84C08686A7B1D0D4D0FAA587187D8135FB286A","sourceBytes":46758,"sourceSha256":"ABFE257FCD6EEA7F128621ACEC40F1773B5EF54DE20C394334B193EF8CB4F889","fixtureBytes":33256,"predecessorContaminations":132,"behavioralExecutions":208,"terminalOutputCleanup":true,"completeCounterVector":true}
```

Syntax, source-to-executable exact derivation, ASCII, 132 contamination runs,
all assertions, and cleanup passed. The `behavioralExecutions` field itself is
the Minor finding below. No capacity, CUA, browser/provider, network, DNS, VM,
clipboard, credential, secret, or live action ran.

## Closed semantic finding

The new `visibleSentinel` run is generated from the instrumented V55 source and
therefore exercises candidate-derived behavior. It independently seeds the
stale nonempty input, stale query URL, and filtered table, then records that the
empty fill changes only the input. The reset URL wait settles to the exact base
URL while deliberately retaining `resetSettledTableFiltered:true`.

The actual hidden-state locator double consequently rejects the still-visible
sentinel. Assertions prove `resetUrlWait 1/1`, `resetUrlRead 1/1`,
`resetSentinelWait 1/0`, `resetSentinelRead 0/0`, and final-input, baseline,
target fill, filtered read, Create, name, and row counters all `0/0`.
Persistent state is null/ineligible with the reviewed failure state; attachment,
runtime, agent, chrome, and setup bindings are cleared; failure cleanup is true.

The separate successful three-state convergence, timeout, wrong-settled-URL,
reset-read, sentinel throw/read, ordinary failure, documentation-output, final-
output, 132 predecessor, and retained current-table matrix cases remain and pass.

## Finding

### V55-MIN-001 — Minor — behavioral execution count is stale

The fixture emits:

```js
behavioralExecutions: 3 + failureCases.length + throwStages.length +
  predecessorNames.length + 2
```

That formula counts the original three success variants, the retained failure/
throw/contamination loops, and two output-failure runs. It omits four executed
runs now present before `failureCases`: stale success, the two-entry
`resetFailure` loop, and `visibleSentinel`. Therefore the emitted value remains
208 while the fixture actually performs 212 behavioral executions.

Required fix: include those four executions in the formula (or increment an
execution counter inside `run` and assert the final count), update the package
only if it cites the number, and rerun the scoped suite. No runtime or executable
change is required.

## Capacity and classification

The candidate remains 26597 bytes; the prior 25351-byte inert proof remains
insufficient. Per the existing zero-finding gate, a new capacity proof and
classification may proceed only after the evidence count is corrected and a
zero-finding re-review confirms the final package. This report does not
authorize any live execution.

## Severity counts

- Critical: 0
- HIGH: 0
- IMPORTANT: 0
- Minor: 1
