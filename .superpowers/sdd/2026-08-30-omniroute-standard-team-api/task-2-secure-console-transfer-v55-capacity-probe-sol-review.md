# OmniRoute V55 inert capacity-probe Sol High review

Date: 2026-09-03 (Asia/Bangkok)
Reviewer: Codex, independent `gpt-5.6-sol` High implementation/security review
Reviewed capacity-probe commit: `38f1fe2212120ecca076af4bef446bd01527795e`
Parent / final V55 implementation PASS: `c6f4a1edd7a1a30104f697de2782073f2837de53`

## Verdict

`FAIL`

`capacity_probe_may_execute=false`

`fix_may_proceed=true`

`authorizes_live_execution=false`

The committed cell is exactly 27200 inert ASCII bytes and exceeds the reviewed
26597-byte V55 candidate by 603 bytes. However, the probe's only result reports
the length of its embedded padding string, which is 27125, while the review
package requires the returned `payloadBytes` to equal 27200. Exact execution
would therefore deterministically fail the one-send acceptance contract and
spend the gate without accepted capacity evidence.

## Direct committed-byte evidence

`38f1fe221` is the direct child of the final V55 implementation PASS and adds
exactly the two assigned capacity-probe paths. Direct Git-object reads produced:

| Artifact | Git blob | Bytes | SHA-256 | ASCII |
| --- | --- | ---: | --- | --- |
| 27200-byte probe | `a1931b54373a9d1cc6f46fabe78ece0b926c5377` | 27200 | `6D4E928C1CB249893F97154372C1F60E1708B0909F7558CF1F56D35DB17818A1` | yes |
| Review package | `a57a0992b83b479c96c7fa09362e6291f29fa3d3` | 1335 | `7F2EE6E5A01F62C074B7F893FD06616F3E6C32FEA6323667B342466C7BAFDC20` | yes |

The final implementation PASS is blob
`f73f18be24a7bbb2ce80decc5228d36a76e8a144`, 4667 bytes, SHA-256
`6A6FC3E807D4D34FD8850B270D7A2F76A8A982812CB37E430992A6CBC5B4A798`.
The reviewed candidate remains blob
`4614b61ce3e0a26a8d2e5ad1c77ef9ba220b82b9`, 26597 bytes, SHA-256
`A9692FFBB688DB244566FCE68D84C08686A7B1D0D4D0FAA587187D8135FB286A`.

Fresh `node --check` on the probe passed. Direct-byte inspection confirms zero
non-ASCII bytes, zero NUL bytes, exactly one `await nodeRepl.write(`, and zero
imports or browser/openTabs/claimTab/playwright/navigation/click, URL/network,
clipboard/storage/cookie, credential/secret/token, DNS, or VM references. The
probe was not evaluated or sent; no CUA, disposable realm, reset, provider, or
live action occurred.

## Finding

### V55-CAP-HIGH-001 — HIGH — exact accepted result is impossible

The probe is structurally:

```js
await nodeRepl.write({result:"V55_CAPACITY_PASS",payloadBytes:"AAA...".length});
```

The complete committed cell is 27200 bytes, but the literal `A` string is
27125 characters. Its exact result is therefore
`{result:"V55_CAPACITY_PASS",payloadBytes:27125}`. The review package instead
requires acceptance only when `payloadBytes=27200`. Since this is an exact,
single-send/no-retry gate, that mismatch is not a harmless label: the reviewed
probe cannot produce its required success result.

Required fix: preserve an exact committed probe size of at least 26597 bytes,
but make its sole inert result report that exact full-cell byte count (for
example, a literal numeric full-cell value with padding adjusted to preserve the
chosen total). Update the committed byte/hash/package facts and retain the
single-send fail-closed contract. Re-review before any send.

## Retained capacity-only boundary

Apart from the result mismatch, the probe is inert: evaluation constructs one
ASCII string, reads its in-memory length, constructs one plain result object,
and writes only that result. It has no import, browser, tab, UI, provider,
secret, network, storage, clipboard, DNS, or VM side effect. The package
correctly requires a fresh disposable CUA realm, mandatory first
`await cua.getState();`, one exact send, exact result acceptance, immediate
realm reset, and fail-closed handling of uncertainty.

Even after correction and successful execution, this artifact can establish
only literal-cell input capacity. It cannot prove candidate-byte fidelity,
authorize V55 execution, relax the later exact UTF-8/SHA-256 comparison, or
grant any browser/provider authority.

## Severity counts

- Critical: 0
- HIGH: 1
- IMPORTANT: 0
- Minor: 0
