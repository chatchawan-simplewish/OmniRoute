# Task 11 v6 native clipboard contract — independent Sol High static review

Review timestamp: `20260831 232331` (Asia/Bangkok)  
Reviewed commit: `7e7aae4833d0f710a635a8a16e23cbd0901d6b6e`  
Base: `86f51e3d04fb070fa6c5bf2444bc1861e84cfc53`  
Scope: direct-byte/static review only; no browser, clipboard, listener, process, credential, or routing action was executed.  
`authorizes_live_execution=false`

## Verdict

- Specification verdict: **FAIL**.
- Security/quality verdict: **FAIL**.
- Findings: **1 HIGH, 1 MEDIUM**.
- This static result grants no execution authority. The contract must be corrected and independently re-reviewed before any standing-authority gate can be consumed.

## Findings

### HIGH — the persistent challenge lifecycle does not match the required success boundaries

The required contract permits the retained challenge binding only after exact browser success and requires it to be nulled only after the terminal child success boundary. The implementation instead assigns the global `nativeClipboardPreflightV6ExpectedChallenge` at `task-11-v6-native-clipboard-brief.md:131`, before `tabs.new()` (`:136`), the native clipboard write (`:146`), exact-tab close (`:151`), counter validation (`:155`), and the browser-success result (`:157`). Thus the supposedly retained-after-success binding already exists throughout every browser uncertainty window.

Call 3 then clears that global in the `spawnSync` `finally` at `task-11-v6-native-clipboard-brief.md:270-272`, before child error/status/output/schema/exact-success validation at `:273-291`; it also clears it on import failure at `:209-215`. This is not “null only after terminal success.” A timeout, signal, malformed output, nonzero exit, comparison failure, or cleanup failure loses the binding before the terminal verdict is known.

Because challenge retention and destruction are explicit one-shot state-machine boundaries, this is load-bearing rather than documentary. Keep the generated challenge lexical during Call 2; assign the persistent binding only in the exact browser-success branch immediately before setting Call 3 eligibility. In Call 3, implement the specified terminal-success transition explicitly (and separately define the terminal-failure disposition without making it look like success). Preserve consumed-before-child and no-retry semantics.

### MEDIUM — a rejected session-naming mutation is reported with `browserUncertain=false`

Call 2 sets `result = "SESSION_NAME_UNCERTAIN"` before awaiting `residualV5Chrome.nameSession()` at `task-11-v6-native-clipboard-brief.md:125-127`, but the catch computes uncertainty only from `tabState.endsWith("_UNCERTAIN")` at `:161-164`. At that point `tabState` remains `NOT_ATTEMPTED`, so a rejected or uncertain session-name promise is emitted as `PRECONDITION_OR_RUNTIME_UNCERTAIN` with `browserUncertain=false`; the purpose-built `SESSION_NAME_UNCERTAIN` value is overwritten. The gate still stops and Call 3 remains ineligible, so this is fail-closed, but the redacted evidence understates a browser-session mutation uncertainty. Make browser uncertainty monotonic from immediately before the name call through fulfillment, or track session-name uncertainty separately and require it false for exact success.

## Verified static properties

- Commit scope is one new 321-line brief; the reviewed HEAD equals the pinned commit. The Git index is empty. The pre-existing dirty baseline count is exactly 12 paths; no path was staged or modified by this review except this requested untracked scratch artifact.
- Brief bytes are UTF-8 without BOM, LF-only (`321` LF bytes, zero CR bytes), with no replacement character.
- Installed API bytes match the pinned `58477`-byte SHA-256 `4BFEB97E958025DB37D52AEA11B75BC70BCA417B4995B0F711C0F07F3DDCCB08`. They declare `nameSession(name: string): Promise<void>`, `Tabs.new(): Promise<Tab>`, `TabClipboardAPI.writeText(text: string): Promise<void>`, and `Tab.close(): Promise<void>`.
- Installed module bytes match the pinned `149210`-byte SHA-256 `C52BA09202F0E82CAA6F6D2A6463A8635C1B1316567975D9B91C1A05FB5AF501`.
- Non-evaluating syntax checks passed: the standalone PowerShell block and embedded child script each have zero parser errors; both JavaScript cells pass `node --check --input-type=module`. No reviewed JavaScript or PowerShell block was evaluated.
- Apart from the findings, the text provides strict serial stop-on-first-failure, a fresh 50-character uppercase-hex non-secret challenge, one documented native clipboard write on the exact new tab, one exact-tab close, consumed-before-child eligibility, one `spawnSync` child with `shell:false`, stdin-only handoff, 30000 ms timeout, exact comparison, one final clear/read, bounded ordered redacted output, and no retry/fallback.
- Static cardinality and prohibited-action inspection found no navigation, URL, DOM/locator, keyboard, server/listener, reconnect, enumeration, credential, key, token, or routing action. Old v3/v5 listener/process residuals remain untouched and `NOT PROVEN`.
- The project standing-authority text allows a newly reviewed one-shot gate only after independent PASS and action-time pins; failed, uncertain, or consumed gates remain spent. This review is FAIL, so that permission cannot attach to this candidate.

## Required disposition

Do not execute Task 11 v6. Correct both state-reporting issues, regenerate the direct-byte package, and obtain a fresh independent static PASS. `authorizes_live_execution=false`.
