# Task 2 secure-console scope replacement fix 2 — Sol High review

`authorizes_live_execution=false`

Review date: 2026-09-01 (Asia/Bangkok)  
Review mode: independent Sol High, direct-byte/static only  
Reviewed fix commit: `17c6c1c8c4dd687f9b73b34533da4e2a5ae5889e`  
Prior fix-1 FAIL review: `c6e6674cf508c2df11f3da15394007df030a7353`

## Verdict

**FAIL / NOT PROVEN — one HIGH and one IMPORTANT finding.**

Fix 2 closes most of the browser-authority finding and replaces the owner-cleanup prose with an executable, hash-pinned retained-handle state machine. The exact adoption call is now bounded, the owned alias becomes eligible only after explicit terminal write returns, `markHandoff` is removed, three no-browser lifecycle cells are present, and the launch wrapper pre-extracts/pins all start/disposition code before the start-capable operation.

Execution remains blocked. The newly introduced SSH proxy-cleanup process discards its bounded exit-proof result and loses its handle after a timeout, so residual process state is not safely retained or proven. Separately, the two alias-detachment cells do not verify their required prior declaration/eligibility/state, contain no one-shot consumption/counters, and can emit PASS repeatedly or in the wrong lifecycle state.

No browser, process, proxy, clipboard, credential, Cloudflare, VM, cleanup, or routing action is authorized by this review.

## Integrity and static parser evidence

- Replacement brief: `29276` bytes, SHA-256 `CE5B4F3A5D1F96F68E04C2348A8286C9B02DCA942F14BCB7162EC52AD71739D6`.
- `HEAD` is the exact fix-2 commit; its parent is the prior fix-1 FAIL review commit.
- The commit changes exactly the replacement-brief path.
- Git index is empty; unrelated dirty baseline remains exactly `12`.
- The brief is UTF-8 without BOM, LF-only, and ends with the expected trailing LF.

All three JavaScript fences parse as modules without evaluation:

| Fence | Bytes | SHA-256 | Parse result |
| --- | ---: | --- | --- |
| retained-tab adoption | `3350` | `10B7A77695A025A3EC06A11539577B1A096E93357A688B17A9FB8A0458DF43D2` | PASS |
| pre-Create alias detachment | `404` | `81BFA17E738694F13B17DBD8C4FD1FAE128EB79B7652C61D8D2A109A677CB55A` | PASS |
| post-native-close alias detachment | `419` | `8D39956A6AF71AA6DDCC07F05A7B8A4FA4B6E1CA28103694238ECBA63E3E06D0` | PASS |

All three PowerShell fences parse without evaluation and with zero errors:

| Fence | Bytes | SHA-256 | Parse result |
| --- | ---: | --- | --- |
| preparation wrapper | `2017` | `D438EFF617AA6983419D610A67FAC3DD01B4434E66300659A9A7821F1CE8C5D9` | PASS |
| guarded launch wrapper | `8548` | `E955B73987BF35A6D3753A8F74152C004CACEEE4DD07D79BD20BEB47BAE1021D` | PASS |
| post-launch/pre-accept disposition | `2190` | `53AF93C906957FB11124674512B28088870128529AC5D6944B7C880E21415094` | PASS |

The pinned live brief contains exactly two PowerShell fences after `## Launch and transfer sequence`: the `655`-byte launch block at SHA-256 `995185FA04790564F4CDCA967E87CAB82EB97731D8458EF85CEF942D4606A293` and the `2779`-byte final block at SHA-256 `9316DE2F7C84A89947E57C8563E9381E97D7C52F0DFFE56CA7E4DE616DD8F637`. Fix 2 extracts those exact blocks and the new disposition block before incrementing start attempted.

The installed Chrome-control API confirms compatibility for the sole adoption operations: `Tabs.get(id): Promise<Tab>`, safe `Tab.id`, `Tab.title()`, `getByRole`, and locator `count()`. The skill/API was used only as a static reference; no browser operation was executed.

## Prior HIGH 1 — browser adoption authority and lifecycle

### Closed portions

The adoption cell now has the required fixed `30000 ms` outer control deadline and explicitly forbids internal timers/races. Complete, untruncated terminal receipt and completed tool status are both required. No environment-dependent timeout can silently qualify the gate.

The exact controller-proven adoption remains narrow:

- one `secureConsoleChromeV1.tabs.get(retainedId)`;
- returned safe ID equals the candidate ID;
- one fixed title read;
- one exact-role textbox count;
- no list, new tab, reconnect, navigation, close, URL output, serialization, screenshot, clipboard, keyboard, or mutation; and
- no page/object/ID/title/marker/exception content in the fixed redacted terminal.

The write counter is now truthful: only `writeAttempted=1` is emitted, while terminal receipt plus completed tool status are the separate fulfillment proof. The owned alias and private eligibility flag are assigned only after `nodeRepl.write` returns, so the previously forecast fulfilled field is gone. Later use requires exact terminal receipt, completed cell status, and private eligibility true.

Output/completion uncertainty is conservatively `NOT_PROVEN` and cannot authorize later action or a detachment cell. `markHandoff` is expressly unauthorized. A proven pre-Create failure has a no-browser detachment path; a reported user-native generated-page close has a separate no-browser detachment path. Neither cell claims tab closure or performs a browser call.

The core controller-provenance, deadline, output-ordering, and browser-call authority defects from fix 1 are closed.

## Finding 1 — IMPORTANT: detachment cells do not enforce their lifecycle or one-shot state

The pre-Create detachment cell (brief lines 198–213) and post-native-close detachment cell (lines 215–230) immediately assign:

- `secureConsoleOwnedTaskTabV2Eligible=false`;
- `secureConsoleOwnedTaskTabV2=null`; and
- a terminal state label;

then emit PASS. Neither cell:

- uses `typeof` guards for the three retained bindings;
- requires the exact prior `ADOPTED_ELIGIBLE` state;
- requires the binding to be non-null and eligibility true;
- has its own eligibility/consumed flag;
- has attempted/fulfilled counters; or
- prevents the opposite detachment cell or the same cell from running later.

Therefore either cell can emit its exact PASS repeatedly, after the other cell, or in a wrong/reset JavaScript session. In a non-strict evaluation surface, assignment to absent identifiers can create new globals and falsely report a detach; in a strict surface it can fail before the fixed terminal. Neither behavior proves that the reviewed owned alias was detached from the exact adoption state. The problem is evidence/lifecycle integrity even though the cells make no browser call.

**Required correction:** make the two dispositions mutually exclusive one-shot state transitions:

1. Declare separate private `preCreateDetachEligible/Consumed` and `postNativeCloseDetachEligible/Consumed` state during successful adoption, or use one explicit finite-state transition gate.
2. Each cell must first use `typeof` guards for every retained name and compute an exact precondition without mutating anything.
3. Require `secureConsoleOwnedTaskTabV2State === "ADOPTED_ELIGIBLE"`, binding non-null, and eligibility true before either detach.
4. Consume the selected disposition eligibility before the null assignment; make the opposite transition permanently ineligible.
5. Increment attempted immediately before the single detach transition and fulfilled only after the alias is null, eligibility false, and final state exact.
6. On a mismatch, emit a fixed FAIL terminal with mutation counters `0/0` and leave bindings unchanged; no repair, second cell, or manual verdict.
7. Exact PASS must include declaration/precondition booleans, consumed state, detach attempted/fulfilled `1/1`, browser calls `0`, binding null, eligibility false, and the exact terminal state.
8. A rejected, missing, timed-out, truncated, or uncertain terminal spends that disposition with no retry. If mutation may have occurred, classify the alias state `NOT_PROVEN`; do not run the other cell as fallback.

The user-native close remains an external reported action, not a tab-closure proof. The post-close cell must preserve that wording.

## Prior HIGH 2 — owner retained-handle cleanup

### Closed portions

Fix 2 now supplies executable code rather than prose for the owner state machine:

- all owner start/handle/wait/file/root/proxy/residual counters and labels are initialized before launch;
- the inherited launch, inherited final block, and new disposition block are extracted and hash-pinned before the start-capable operation;
- start attempted increments immediately before the one dot-sourced launch;
- start fulfilled and handle retained are set only after the exact owner/PID/clock guard;
- prestart extraction failures use only direct-child/hash-guarded prepared-file cleanup;
- retained-handle failures dot-source the one exact final remaining-budget block;
- start-uncertain/no-handle state performs no lookup, reacquisition, kill, or destructive file cleanup;
- exit-unproven state retains artifacts and stops;
- file/root/proxy cleanup follows only successful inherited final disposition; and
- success/failure evidence is fixed counters, booleans, and residual labels without exception text or process metadata.

The original dot-sourcing correction remains sound: the exact preparation and launch bytes are unchanged, each is dot-sourced once in the same retained parent, and there is no `&` child-scope invocation. The retained `$owner`, `$expectedOwnerPid`, and `$ownerClock` remain available to nonblocking coordination and the sole final block.

This closes the original “matrix is prose-only” defect for the credential owner itself.

## Finding 2 — HIGH: new proxy-cleanup SSH child can remain live with its handle discarded

The new `Invoke-ExactScopeProxyCleanup` helper (brief lines 292–330) creates and starts a new `ssh.exe` process. Its timeout branch is:

```powershell
if (-not $process.WaitForExit(60000)) {
    try { $process.Kill() } catch {}
    $null = $process.WaitForExit(10000)
    throw 'SCOPE_PROXY_CLEANUP_TIMEOUT'
}
```

The `10000 ms` exit-proof result is explicitly discarded. Termination attempted/fulfilled and exit-proof attempted/fulfilled are not counted. If `Kill()` rejects or the second wait returns false, the function throws, unwinds, and loses the only `$process` handle. The outer disposition then reports only owner cleanup residual state; it cannot prove or retain the new SSH cleanup child's state. A still-running SSH process could continue the remote cleanup command after the gate is classified failed, while no exact handle remains for observation or bounded disposition.

The same helper also fails to dispose/retain its process object on start, wait, or stream-drain exceptions. A `WaitAll` timeout occurs after process exit but leaves stream tasks/handle cleanup unclassified. This is weaker than the inherited exact SSH child lifecycle and violates the replacement's own no residual process/handle ambiguity boundary.

**Required correction:** give the proxy-cleanup child the same exact retained-handle discipline as every inherited SSH child:

1. Store the cleanup `Process` in a parent-scope uniquely named binding before start; never lose it on exception.
2. Add start attempted/started, wait attempted/fulfilled, timeout, termination attempted/fulfilled, exit-proof attempted/fulfilled, stdout/stderr drain, dispose, and residual counters/labels.
3. Increment each attempted counter immediately before its individual call and each fulfilled counter only after fulfillment.
4. On the one `60000 ms` wait timeout, make at most one exact-handle `Kill()` attempt and exactly one checked `10000 ms` exit-proof wait.
5. If exit proof fails, retain the exact handle, set a fixed `PROXY_CLEANUP_CHILD_EXIT_NOT_PROVEN` residual, perform no second wait/kill/retry, and stop. Do not dispose or overwrite the retained handle.
6. After proven exit, perform one bounded `5000 ms` asynchronous stream drain. If drain is uncertain, classify output/proxy cleanup NOT PROVEN without retry; process exit remains separately proven.
7. Dispose and null the handle only after exit is proven and all required output/exit validation is complete; expose no stdout/stderr content except comparison to the exact safe terminal and empty stderr.
8. Include these child counters and residual state in the fixed redacted prestart/preaccept cleanup terminal. Outer owner cleanup success must require the proxy child exact terminal, proven exit, drain, dispose, proxy absence, network count `2`, and listener absence.

No process enumeration, PID/name reacquisition, alternate SSH process, second cleanup invocation, remote fallback, or tree kill may be added.

## Other authority and security boundaries

No additional defect was found in the preserved target/scope rules:

- the incident gate remains spent; fix 2 is a new no-retry replacement candidate;
- full original byte/hash, worktree, Windows identity/policy, VM, Cloudflare, token-row, DNS, and OmniRoute-key preconditions remain mandatory;
- the replacement-specific clipboard clear/read-empty proof is fresh and once-only;
- only one private proxy start and deterministic R5 POST maximum remain;
- exact token name, `mysw.me`, specific-zone scope, and only `Zone WAF Edit` plus `Zone Read` remain fixed;
- no account/token-management, DNS, Tunnel, Access, public rollout, OmniRoute rollout key, model request, alternate bridge, second start, second POST, dashboard Rulesets mutation, PATCH/edit, permission expansion, retry, fallback, owner handoff, or verdict relaxation is added;
- retained PID plus exact `OWNER_READY=PASS` and `SECRET_PROMPT_READY=PASS` remain required before final Create;
- final Create/native Copy/masked Paste and exact-row deletion retain separate mandatory action-time confirmations that standing authority cannot waive;
- no agent browser/token-page/clipboard inspection occurs after final Create;
- same-process token verification, private Zone-ID derivation, sole exact-hash bounded R5 child, universal revocation hold, invalidity proof, and guarded cleanup remain exact; and
- success remains only the inherited exact terminal tuple, proven owner exit, artifact cleanup, refreshed token counts `0 / 0`, and HTTP `401`.

## Disposition

Fix 2 is not safe and unambiguous enough for execution. Close the HIGH proxy-cleanup process lifecycle defect and the IMPORTANT one-shot detachment-state defect in a new committed revision, then obtain another independent Sol High review. Until then, all prior live gates remain spent, this replacement is blocked, and no browser, process, proxy, credential, Cloudflare, VM, cleanup, or routing action may be taken under it.

`authorizes_live_execution=false`
