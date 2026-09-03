# OmniRoute V55 search-reset readiness Sol High implementation/security review

Date: 2026-09-03 (Asia/Bangkok)
Reviewer: Codex, independent `gpt-5.6-sol` High implementation/security review
Reviewed implementation commit: `829801ccb71765b3488e84f23e78000614cde09a`
Direct parent / final V55 design PASS: `045bd275b39bf70dc1cbfb41e81ec396ac61593b`
Approved V55 design: `3d2caf86b2b3314e5f531c243c74c714640f42fa`

## Verdict

`FAIL`

`fix_may_proceed=true`

`capacity_proof_may_proceed=false`

`classification_may_begin=false`

`authorizes_live_execution=false`

The committed source and executable are mechanically consistent and retain the
V54 trust boundaries, but the reset does not implement bounded URL convergence,
the fixture does not exercise the diagnosed stale transition or reset-URL-read
earliest stop, and the executable violates the approved no-Unicode-escape
transport constraint. Fix the candidate and fixture first; only then measure a
new capacity payload against the final candidate size.

## Direct committed-byte evidence

Commit `829801ccb` is the direct child of the V55 design PASS and adds exactly
the four assigned source/executable/fixture/review-package paths. Direct Git-
object reads produced:

| Artifact | Git blob | Bytes | SHA-256 | ASCII |
| --- | --- | ---: | --- | --- |
| Source | `a31d64400107ef4bf38946e0c9e0b9e095565fc7` | 46630 | `A272F1B52D7841E10FFF7C31E0BCBA0DD1C9A64FE3457944A7E6B1D45A483DF8` | yes |
| Executable | `be83912e7b807e430ec5d28d84ba6d66ef03995d` | 26511 | `C528D16CE12F4BBEBF77925646663BF8BCA3C09CE4F7EAD6FC5045E325546A33` | yes |
| Pure fixture | `bc7516476b823463cbf7913132abff2bc14dff24` | 29676 | `CF69D25EB76D86CD3A714A45E077FAEC02F25AFC70FEF9AA4E1D1EB97A4B9B02` | yes |
| Review package | `99d961e71eadb236d039fc5fd4f958757b623342` | 3068 | `A0CA27C4C86DA01DAC99B739EFCC8DDABBF7E27ED5ABAD4237227BC8B69202B1` | yes |

The approved design is blob `da6c4e996faf9baaa91d95cf0798aab73f1ff675`,
5214 bytes, SHA-256
`90D04C01DDCCA2B6C05D228AA0BDA0A4B6A20EDD72B6C9891A8453922224FC7F`.
The design PASS is blob `2042fbee3e68d8a132cf7dd0adbd2c1233694fc6`,
2994 bytes, SHA-256
`DBA4078F4DFD6D11D01BD3AD5FBDB625E319DEE931A55E196D25378EA894F350`.

Fresh scoped offline syntax and pure-fixture checks reproduced:

```json
{"result":"PASS","executableBytes":26511,"executableSha256":"C528D16CE12F4BBEBF77925646663BF8BCA3C09CE4F7EAD6FC5045E325546A33","sourceBytes":46630,"sourceSha256":"A272F1B52D7841E10FFF7C31E0BCBA0DD1C9A64FE3457944A7E6B1D45A483DF8","fixtureBytes":29676,"predecessorContaminations":132,"behavioralExecutions":208,"terminalOutputCleanup":true,"completeCounterVector":true}
```

The passing regeneration proves source-to-executable derivation, syntax, and
ASCII. It does not overcome the semantic and coverage findings below. No CUA,
live browser/provider, network, DNS, VM, clipboard, credential, secret, or
external action was performed.

## Findings

### V55-HIGH-001 — HIGH — Executable contains forbidden Unicode escapes

The approved design requires an ASCII candidate with no literal emoji and no
Unicode escape, specifically to avoid recurrence of V54's transformed
`\\ud83d\\udd10` payload. The executable has no literal emoji and correctly
constructs the session name as `String.fromCodePoint(128272)`, which is
semantically `String.fromCodePoint(0x1F510)`. However, direct-byte inspection
finds nine `\\uXXXX` sequences: three occurrences each of `\\u0000`,
`\\u001f`, and `\\u007f` in control-character guards.

Those bytes directly violate the reviewed transport constraint and remain
candidate-specific transformation surfaces. The fixture asserts only overall
ASCII and does not assert absence of Unicode escapes, despite the design's
explicit fixture requirement.

Required fix: express all control-character checks without `\\uXXXX` source
escapes, regenerate the executable, and assert on the committed candidate bytes
that literal emoji count and Unicode-escape count are both zero while the exact
session-name construction occurs once.

### V55-IMP-001 — IMPORTANT — Reset URL “wait” does not wait for convergence

The implementation increments `resetUrlWait`, calls only
`waitForTimeout(0)`, marks the wait fulfilled, then reads the URL once. A zero-
millisecond yield does not wait until the exact base URL is reached and cannot
implement the bounded convergence required by the design and the V54 diagnosis.
If clearing makes the input empty before the SPA updates the URL, the one-shot
gate can fail on the immediate stale read even though the approved state would
converge moments later.

Required fix: use a bounded, semantics-bearing wait that completes only when the
actual tab URL is exactly the base API Tokens URL, then perform the separately
counted exact URL read. A timeout or wrong settled URL must preserve its exact
earliest-stop vector and fail before sentinel/baseline/target operations.

### V55-IMP-002 — IMPORTANT — Fixture does not test the diagnosed stale transition or reset-URL-read stop

The fixture's reset fill immediately sets both `state.currentUrl` to the base URL
and `state.filtered` to false. Its zero-timeout mock then always fulfills. It
therefore cannot reproduce the required field-only-clear state with stale URL
and stale table, despite the review package claiming that case.

The initial post-navigation URL read and reset URL read also share the same
mock operation name, `tokenUrl`. `throwStages` lists that name twice, but both
entries throw at the first read; no case reaches and throws at the separately
counted reset URL read. Finally, the sentinel mock fulfills a `state:"hidden"`
wait while its configured sentinel count is one and modeled visible, so it does
not prove hidden/detached semantics.

Required fix: model input, URL, and table convergence as separate state changes;
give initial URL read, reset URL wait, and reset URL read unique operations; and
exercise stale-then-converged success plus field-only-clear/stale-URL,
stale-sentinel, timeout, wrong-settled-URL, and each exact earliest-stop vector.
The hidden/detached locator double must fail while visible and fulfill only when
hidden or absent.

## Capacity classification

The only prior inert direct-cell capacity proof is `25351` bytes. The committed
V55 executable is `26511` bytes, so `25351 < 26511` and capacity is
**INSUFFICIENT / NOT PASSED**. The implementation package correctly makes no
capacity-PASS claim.

A new inert capacity proof must not run yet because the required fixes will
change the final executable bytes and length. After a zero-finding fix review,
an inert payload whose measured literal length is at least the final candidate
length may establish capacity only; exact candidate UTF-8/SHA-256 fidelity
remains a separate action-time check.

## Retained properties without findings

The source-to-executable transformation, 132 unique predecessor guards and
contaminations, both conditional-reset branches, local binding `1/1` semantics,
unconditional execution of the reset URL/sentinel/final-input/baseline stages,
target-table matrix, exact counter framework, ordinary/documentation/final-
output cleanup, sanitized output, one-shot/no-retry boundary, and static absence
of Create click, token creation, clipboard, storage, secret, persistent provider,
DNS, VM, and tab mutation calls otherwise remain consistent with the approved
design and V54 baseline.

## Severity counts

- Critical: 0
- HIGH: 1
- IMPORTANT: 2
- Minor: 0
