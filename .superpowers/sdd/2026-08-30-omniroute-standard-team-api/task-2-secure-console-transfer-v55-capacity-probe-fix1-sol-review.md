# OmniRoute V55 inert capacity-probe fix-1 Sol High re-review

Date: 2026-09-03 (Asia/Bangkok)
Reviewer: Codex, independent `gpt-5.6-sol` High implementation/security re-review
Reviewed fix commit: `c357dc849d3046473d34593ae3ae6e52328196e4`
Parent / prior FAIL review: `fe65021b650992349c3767511af0211247b91e35`
Final V55 implementation PASS: `c6f4a1edd7a1a30104f697de2782073f2837de53`

## Verdict

`PASS`

`capacity_probe_may_execute=true`

`authorizes_live_execution=false`

No unresolved Critical, HIGH, IMPORTANT, or Minor findings remain. The exact
committed 27200-byte inert cell now returns the exact fields required by its
single-send contract. This review permits only the separately owned inert
capacity probe in a disposable realm; it does not authorize V55 candidate or
provider execution.

## Direct committed-byte evidence

`c357dc849` is the direct child of the prior capacity-review commit and modifies
exactly the probe and its review package. Direct Git-object reads produced:

| Artifact | Git blob | Bytes | SHA-256 | ASCII |
| --- | --- | ---: | --- | --- |
| 27200-byte probe | `6f9b4c88d0fa577c176125e6e9921d1dc6fd37d2` | 27200 | `FA4F4A6295A4E4A124A706541C30D55A5BBD2EF09A395223161A90F67E2735C1` | yes |
| Review package | `5e7987697c6e7b24fec177851449567ae70ca45a` | 1385 | `C77D64D9D1127D789B237190D8897DC71D2ED6F5AEF55A044BFC4B596DA99C3E` | yes |

The prior FAIL review is blob `695c6e9e1401cb8e50c48507f2a2940dea00ccfd`,
4062 bytes, SHA-256
`0816AC55378091720E293BAAB55D06CC60D81594705DE6222DB6F2ED19CAB6B0`.
The final implementation PASS is blob
`f73f18be24a7bbb2ce80decc5228d36a76e8a144`, 4667 bytes, SHA-256
`6A6FC3E807D4D34FD8850B270D7A2F76A8A982812CB37E430992A6CBC5B4A798`.
The reviewed V55 candidate remains 26597 bytes, so the inert cell exceeds it by
603 bytes.

Fresh `node --check` on the committed probe passed. Direct-byte inspection also
found zero non-ASCII bytes and zero NUL bytes.

## Exact inert behavior

The probe has one expression and exactly one output call. Its literal structure
is:

```js
await nodeRepl.write({result:"V55_CAPACITY_PASS",cellBytes:27200,literalBytes:"AAA...".length});
```

The padding literal is exactly 27109 ASCII `A` characters. Static evaluation of
the object therefore yields the exact required fields:

```json
{"result":"V55_CAPACITY_PASS","cellBytes":27200,"literalBytes":27109}
```

The probe contains zero imports and zero browser, openTabs, claimTab,
playwright, navigation, click, URL/network, clipboard, storage/cookie,
credential/secret/token, DNS, or VM references. Its only effect is the intended
sanitized `nodeRepl.write` result. The probe itself was not evaluated or sent.

## One-shot disposable-realm contract

The package requires a fresh disposable CUA realm, reset before use; the
mandatory first initialization call `await cua.getState();`; one exact send of
the committed probe; acceptance only for the exact three-field result above;
fail-closed handling of any mismatch, failure, or uncertainty; and immediate
realm reset after the result. Those requirements are internally consistent with
the committed probe. No retry, fallback, continuation, or result relaxation is
authorized.

Successful execution can establish only that the literal cell accepts at least
27200 bytes, which is larger than the 26597-byte candidate. It cannot establish
candidate-byte fidelity, replace the later exact UTF-8/SHA-256 comparison,
authorize V55 live execution, or grant browser/tab/UI/provider/secret authority.

## Severity counts

- Critical: 0
- HIGH: 0
- IMPORTANT: 0
- Minor: 0
