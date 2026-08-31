# Task 13 v7 native clipboard — independent Sol High static review

Review timestamp: `20260901 001455` (Asia/Bangkok)  
Brief commit: `f2529b8193bbfc8bed2ede5aa4d45b9f04683182`  
Base / Task 12 PASS classification: `ce26c909a259b17ce02768b813d3563c872c580e`  
Scope: direct-byte review and non-evaluating compatibility checks only. No contract cell, clipboard, browser, tab, listener, server, credential, or routing action was executed. The pinned executable parsed text and ran one inert encoded-command stream probe; neither operation evaluated the embedded clipboard child.  
`authorizes_live_execution=false`

## Verdict

- Specification verdict: **FAIL**.
- Security/quality verdict: **FAIL**.
- Findings: **1 HIGH**.
- The contract remains fail-closed, but its exact success tuple is unreachable under the pinned child launch shape observed on this host. Do not execute it.

## Finding

### HIGH — pinned Windows PowerShell emits startup progress on stderr, making exact Call 3 success unreachable

Call 3 launches the pinned Windows PowerShell executable with `-EncodedCommand`, redirected streams, and an environment containing only `SystemRoot` and `WINDIR` (`task-13-v7-native-clipboard-brief.md:286-289`). Its ordered schema is valid only when `stderr.length === 0` (`:301-306`), and exact success requires that schema (`:314`).

The requested exact-executable static compatibility check disproved that assumption:

- exact executable: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`;
- exact process switches: `-NoLogo -NoProfile -NonInteractive -EncodedCommand`;
- exact restricted environment: only `SystemRoot=C:\Windows` and `WINDIR=C:\Windows`;
- inert encoded command: one safe redacted output line and exit 0; no clipboard/browser/listener/process-management code;
- observed exit: `0`;
- observed stdout: the single intended safe line;
- observed stderr: `392` characters beginning with `#< CLIXML`, containing a PowerShell progress record whose activity is `Preparing modules for first use.`

The same non-evaluating parser harness, run twice through the exact pinned executable, returned parser error count zero but also produced non-empty stderr each time. This is therefore not caused by the embedded clipboard script. It is an observable property of the selected executable/encoded-command/restricted-environment pipe shape on the pinned host.

Consequently, even if the actual child reads and compares the challenge, clears the clipboard, proves it empty, emits the exact 13 stdout lines, and exits 0, line 306 forces `schema=false`. Call 3 then reports `HANDOFF_OR_COMPARISON_UNCERTAIN_RETAINED_BINDING`, retains the challenge, spends the one-shot gate, and cannot produce the required `EXACT_MATCH_AND_FINAL_EMPTY`. The root-cause correction replaces `ENOENT` with a child that starts, but does not provide a viable exact-success transport.

Required correction: retain strict rejection of unexpected stderr, but change and directly verify the child launch/script environment so the exact pinned executable produces zero stderr under the actual spawn shape. Do not merely ignore arbitrary stderr or relax the verdict. Regenerate the package and obtain a fresh independent static review before any action.

## Other static results

- Reviewed HEAD equals `f2529b8193bbfc8bed2ede5aa4d45b9f04683182`; the commit adds only the 359-line v7 brief. Before creating this requested scratch report, Git index count was `0` and the unchanged dirty baseline count was exactly `12`.
- Brief bytes are UTF-8 without BOM, LF-only (`359` LF bytes, zero CR bytes), with no replacement character.
- Pinned executable exists as a regular file and matches every pin: `495616` bytes; SHA-256 `8BB6FA8C283B4D92120B1EF249A9B311B0F804D4CABBE9981159976C8BE76A5E`; file version `10.0.26100.8972 (WinBuild.160101.0800)`; product version `10.0.26100.8972`.
- Exact pinned Windows PowerShell parser returned zero errors for Call 1 and for the embedded child without evaluating either script. Both JavaScript cells passed `node --check --input-type=module`.
- Installed browser API/module bytes match the pins: API `58477` bytes / `4BFEB97E958025DB37D52AEA11B75BC70BCA417B4995B0F711C0F07F3DDCCB08`; module `149210` bytes / `C52BA09202F0E82CAA6F6D2A6463A8635C1B1316567975D9B91C1A05FB5AF501`. API declarations confirm `nameSession`, `Tabs.new`, `TabClipboardAPI.writeText`, and `Tab.close` signatures.
- Apart from the finding, v7 correctly preserves the fixed v6 state machine: fresh bindings; lexical challenge until exact browser success; monotonic session/browser uncertainty; exact-tab retention on uncertainty and clear-on-fulfilled-close; eligibility consumed before the sole child; failure-retained and success-only-cleared challenge; no retry/fallback/continuation.
- Static cardinality is one `nameSession`, one `tabs.new`, one native `clipboard.writeText`, one exact-tab `close`, and one `spawnSync`; baseline and child together contain two clears and three reads in their intended separate calls.
- No navigation, URL, DOM/locator, keyboard, server/listener, reconnect, enumeration, credential, key, token, or routing action exists. Output remains value-redacted. Old v3/v5 listener/process residuals remain untouched and `NOT PROVEN`.
- Standing authority is stated narrowly and cannot attach because this independent review is FAIL. Action-time pins do not rehabilitate a statically disproven success condition.

## Disposition

Do not consume Task 13 v7. Correct the stderr incompatibility without weakening the strict schema or redaction boundary, then obtain a fresh independent direct-byte PASS.  
`authorizes_live_execution=false`
