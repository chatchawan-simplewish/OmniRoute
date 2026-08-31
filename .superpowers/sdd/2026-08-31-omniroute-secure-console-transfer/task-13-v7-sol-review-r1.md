# Task 13 v7 native clipboard — Sol High fix-round 1 static re-review

Review timestamp: `20260901 003245` (Asia/Bangkok)  
Corrected brief commit: `a2b887bb4fad01343b5d2957a27363ee877c7c72`  
Fix base / prior failed review: `7f0b1708c`  
Original v7 brief: `f2529b8193bbfc8bed2ede5aa4d45b9f04683182`  
Scope: fix-round diff and new-breakage risk, direct bytes and non-evaluating compatibility checks only. No contract cell, clipboard, browser, tab, listener, server, credential, or routing action was executed.  
`authorizes_live_execution=false`

## Verdict

- Specification verdict: **PASS**.
- Security/quality verdict: **PASS**.
- Prior HIGH finding: **RESOLVED**.
- New findings: **none**.
- This static PASS grants no live-execution authority; exact action-time pins remain mandatory for the sole Sol High gate owner.

## Prior-finding resolution

The corrected contract replaces incompatible Windows PowerShell with the bundled PowerShell runtime at:

`C:\Users\chatc\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\powershell\pwsh.exe`

Direct filesystem evidence matches every pin:

- regular file exists;
- size `301368` bytes;
- SHA-256 `DB6DD81183FE57D22E03B911EC9A30A2FD7C40542E97743615355A6FB44F458F`;
- file version `7.6.4.500`.

The independent review reproduced the exact inert compatibility tuple using Node `spawnSync`, the exact pinned path, `-NoLogo -NoProfile -NonInteractive -EncodedCommand`, `shell:false`, `windowsHide:true`, UTF-8 capture, 30000 ms timeout, SIGKILL, 16384-byte buffer, and an environment containing only `SystemRoot=C:\Windows` and `WINDIR=C:\Windows`:

- status `0`;
- signal `null`;
- error `null`;
- stdout line count `1`;
- stdout exactly `V7_CHILD_COMPAT=PASS`;
- stderr length `0`.

This resolves the prior startup-progress CLIXML incompatibility while retaining the strict `stderr.length === 0` schema condition. No stderr is ignored, parsed away, or verdict-relaxed.

## Syntax and runtime compatibility

- The exact pinned bundled `pwsh` parser returned zero errors for Call 1 and for the embedded comparison child, with stderr length zero in both parse-only invocations. Neither script was evaluated.
- Both JavaScript cells passed `node --check --input-type=module`.
- The corrected spawn line uses the same exact pinned bundled path and otherwise preserves the reviewed arguments, restricted environment, stdin-only challenge handoff, 30000 ms deadline, buffer bound, and stream capture.

## Preserved one-shot/security invariants

- V7 bindings remain fresh and separate from v6; only the existing connected `residualV5Chrome` binding is reused.
- Call 1 retains exactly one baseline clipboard clear and one empty read with value-redacted counters.
- Call 2 retains one awaited `nameSession`, one `tabs.new`, one exact-tab native `clipboard.writeText`, and one exact-tab `close`, in strict serial order.
- The challenge remains lexical until exact browser success; the persistent binding is published only immediately before Call 3 eligibility. Session-name uncertainty remains monotonic and is folded into browser uncertainty and exact-success gating.
- Call 3 consumes eligibility before its sole child attempt, passes the challenge only through stdin, performs one comparison read and one final clear/read in the child, retains the challenge on every failure, and nulls it only after the fully validated exact success tuple.
- The strict ordered stdout schema, zero-stderr condition, child status/signal/error validation, exact counters, exact comparison, and final-empty proof remain unchanged.
- Static cardinality remains one `nameSession`, one `tabs.new`, one native write, one exact-tab close, one `spawnSync`; across Call 1 and the child there are exactly two clear sites and three read sites in their separate phases.
- Static prohibited-action inspection found no navigation, URL, DOM/locator, keyboard, server/listener, reconnect, enumeration, credential, key, token, or routing action. Old v3/v5 listener/process residuals remain untouched and `NOT PROVEN`.
- Output remains redacted: no challenge, clipboard value, tab handle/ID/title/URL, content/metadata, exception message/stack, credential, key, or token is emitted.

## Pins and repository boundary

- Reviewed HEAD equals `a2b887bb4fad01343b5d2957a27363ee877c7c72`; the fix commit changes only the v7 brief.
- Before creating this requested scratch report, Git index count was `0` and the unchanged dirty baseline count was exactly `12`.
- Corrected brief is UTF-8 without BOM and LF-only (`385` LF bytes, zero CR bytes), with no replacement character.
- Installed API/module bytes remain pinned: API `58477` bytes / `4BFEB97E958025DB37D52AEA11B75BC70BCA417B4995B0F711C0F07F3DDCCB08`; module `149210` bytes / `C52BA09202F0E82CAA6F6D2A6463A8635C1B1316567975D9B91C1A05FB5AF501`. Direct API declarations confirm `nameSession`, `Tabs.new`, `TabClipboardAPI.writeText`, and `Tab.close`.
- Project authority bytes remain `6051` / `AD0EA394F694C7795870C2B66D745EDC1FCA8997E7D7041A21E5659B0C349DDC`. Standing authority does not permit retry and requires exact brief/review/evidence/runtime/API/module/authority pins, empty index, exact baseline, same connected browser binding, zero intervening action, and never-declared fresh v7 bindings at action time.

## Disposition

Fix-round 1 static review is complete and **PASS**. Any later execution remains a separate one-shot gate consumption by the sole Sol High owner after all action-time pins pass. `authorizes_live_execution=false`.
