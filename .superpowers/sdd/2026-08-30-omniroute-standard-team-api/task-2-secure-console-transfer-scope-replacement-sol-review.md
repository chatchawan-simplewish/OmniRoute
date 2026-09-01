# Task 2 secure-console retained-scope replacement — Sol High review

Review date: 2026-09-01 (Asia/Bangkok)  
Review mode: independent Sol High, direct-byte/static only  
Reviewed replacement commit: `1441e3908da44e7aa403794d586b8d17c9339201`  
Pinned incident commit: `029cf42275d2d61b6f69f38b7d94a1478702f135`  
Fixed live brief / PASS: `7af3ab75ec87d81d75811ff8f2e9b4fa9d0c3e3b` / `ce47c2eacb5a5cbf055c3fc814137e46c1855e40`

## Verdict

**FAIL / NOT PROVEN — two HIGH findings.**

The PowerShell scoping correction itself is valid: both replacement fences parse, both exact inherited blocks match their byte/hash pins, and dot-sourcing each script block in the same persistent parent retains preparation variables and the launch handle/clock/PID. The old `&` child-scope defect is removed without changing the extracted preparation or launch bytes.

Execution is nevertheless blocked. The candidate relies on an unproven retained tab binding that appears in none of its pinned predecessors, and its failure cleanup does not safely disposition a possibly running retained owner after launch uncertainty. Either defect can leave target/browser authority ambiguous or a residual credential-owner process/file set. Static PASS would therefore be unsafe.

This review authorizes no execution, retry, browser action, process action, cleanup, Cloudflare action, credential action, VM action, or routing mutation.

## Integrity and static checks

- Replacement brief: `8636` bytes, SHA-256 `786F9CF9666F03C5663F59868B5064A9E0182EDEF733F2C12372E865F9E34D2A`.
- Incident record: `4296` bytes, SHA-256 `24FCC2686B8BA176BC26158CD48D09AB1B991DE617D0D523C15FC06C3C448605`.
- `HEAD` is the pinned replacement commit and changes exactly the replacement-brief path.
- The Git index is empty and the unrelated dirty baseline remains exactly `12`.
- The replacement brief is UTF-8 without BOM, LF-only, and ends with the expected trailing LF.
- Both and only two replacement `powershell` fences parse with the PowerShell language parser with zero errors. Parsing did not execute either fence.
- The first replacement fence is `2017` bytes and contains exactly one dot-source invocation, zero child-scope `&` invocations, zero `Start-Process`, and one fixed success write.
- The second replacement fence is `952` bytes and contains exactly one dot-source invocation, zero child-scope `&` invocations, zero direct `Start-Process`, and one fixed success write.

## Dot-sourcing correction

The pinned live-brief blob at the reviewed commit is unchanged in `HEAD`: `62054` bytes, SHA-256 `995CA4D59E564EAF53417B9F577808F9C307C5CDEE93FB8E91DC73A5211F52CC`.

Static extraction using the replacement's exact header/regex logic produced:

| Inherited fence | Bytes | SHA-256 | Parse errors | `return` statements |
| --- | ---: | --- | ---: | ---: |
| Credential-free preparation | `3983` | `784E91D71AB0B07A65C6FDA429CC4A86C3E6107C76E258BC608F75DA893C1D4A` | 0 | 0 |
| Launch | `655` | `995185FA04790564F4CDCA967E87CAB82EB97731D8458EF85CEF942D4606A293` | 0 | 0 |

The first inherited block creates `$transferRoot`, `$ownerScriptPath`, `$r5ScriptPath`, and `$safeLogPath` in its invocation scope after exact source, parser, path, and written-file guards. Dot-sourcing it in the retained parent therefore makes those variables persist for the second fence. The replacement then rechecks nonempty paths, direct-child containment, exact written hashes, and safe-log absence before emitting its fixed preparation terminal.

The second inherited block starts the exact bundled pwsh owner, starts `$ownerClock`, stores the retained `$owner` handle, and derives `$expectedOwnerPid`. Dot-sourcing it in that same parent makes all three persist for nonblocking coordination and the inherited final bounded wait/termination/cleanup block. Its immediate guard correctly detects missing scope retention.

The incident's sole semantic root cause was executing preparation with `&`, which placed its variables in a child scope and caused the launch's redirected-output path to be null. Replacing `&` with `.` is the sole change to execution semantics of the exact inherited blocks. The wrappers add credential-free extraction/hash/state guards and redacted terminals; they do not alter the inherited block bytes or create a second start.

## Finding 1 — HIGH: retained tab binding has no pinned provenance or validation

**Evidence:** replacement brief line 48 requires use only of `secureConsoleTaskTabV1` while forbidding reconnect, reacquisition, or a tab list.

`secureConsoleTaskTabV1` occurs nowhere in any pinned predecessor:

- fixed live brief `7af3ab75ec87d81d75811ff8f2e9b4fa9d0c3e3b`: zero occurrences;
- retained-Chrome recovery brief `70b6b1087748b0612b195f4b1d7e1a78d13bafb7`: zero occurrences;
- retained-Chrome recovery classification `788d38a5db1fd598631fee4f8db764d3719f9186`: zero occurrences; and
- launch-scope incident `029cf42275d2d61b6f69f38b7d94a1478702f135`: zero occurrences.

The only occurrence is the new replacement brief itself. The pinned retained-Chrome recovery proves `secureConsoleChromeV1` and one already consumed count of zero; it does not create, name, retain, or classify `secureConsoleTaskTabV1`. The incident reports authenticated Cloudflare reads but does not pin a tab creation/selection count, binding name, same-session identity, URL/target ownership, or retained-tab disposition.

Consequently, the replacement cannot establish which object the name denotes, whether it exists in the exact persistent session, whether it belongs to the proven `secureConsoleChromeV1`, whether it is still live, or whether it targets the intended Cloudflare form. Merely naming it creates an unreviewed retained-authority dependency. The no-reconnect/no-reacquire rule then provides no safe fail-closed way to recover from absence or ambiguity.

**Required correction:** choose and document exactly one path:

1. If a retained task tab genuinely exists, pin the prior direct evidence that created and retained it, including exact same-session provenance and its unique binding name. Add a new one-shot, fixed-redacted, `typeof`-first precondition that validates declaration, non-null shape, exact browser ownership/session provenance, and required target state without serializing or emitting URL/page/tab metadata. It must perform no list, reconnect, reacquisition, mutation, alternate selector, or fallback, and any uncertainty must spend the replacement before later action.
2. If no such pinned retained tab exists, remove `secureConsoleTaskTabV1` from this contract. Define a separate independently reviewed browser/tab acquisition contract with exact lifecycle and disposition, or redesign the replacement to rely only on the already proven retained browser binding and user-native page ownership. Do not invent or alias a tab binding inside this scope-only gate.

The corrected scope replacement must identify the exact source commit and evidence for whichever binding clause it inherits. This cannot be repaired by an action-time assertion or manual verdict.

## Finding 2 — HIGH: pre-accept failure cleanup omits retained-owner disposition

**Evidence:** the launch fence can successfully start the owner before the wrapper guard and terminal (replacement lines 90–99). The contract then says any discrepancy spends the gate (line 125), but its pre-accept cleanup directs proxy and temp-file/root removal only (lines 128–131). It reserves the inherited bounded owner path only for “after masked acceptance.”

A rejected, interrupted, timed-out, missing-output, or tool-uncertain result after `Start-Process` may leave:

- the exact `$owner` process running at its masked prompt;
- `$owner`, `$ownerClock`, and `$expectedOwnerPid` retained or uncertain;
- redirected safe-log ownership active;
- the owner and R5 script files in use until owner common cleanup; and
- the temp root nonempty or locked.

The owner has not accepted a credential, but it is still the credential-owner process and can remain able to accept masked input. Deleting scripts/root without first proving owner exit is both ambiguous and unsafe. On Windows the redirected safe log may remain open, and the replacement's direct-file cleanup cannot prove the root empty while the process is live. Conversely, simply waiting for eventual self-timeout without a fixed retained-handle disposition leaves residual process state unclassified.

The inherited live contract already has the correct primitives: a launch-time `1800000 ms` stopwatch, one final remaining-budget wait, at most one exact-retained-handle termination attempt, one `10000 ms` exit proof, no process enumeration/reacquisition, and no file/root deletion before proven exit. The replacement must explicitly route every post-launch/pre-accept failure and output uncertainty through those primitives.

**Required correction:** add a monotonic launch-state and cleanup matrix:

- increment start attempted immediately before the inherited launch call and record start fulfilled/handle retained only after it returns;
- if failure occurs before a start can have happened, perform only the guarded proxy and prepared-file cleanup allowed for the no-process state;
- if an exact retained handle exists, never delete the safe log, scripts, or root until that handle has proven exit; let the owner take its bounded pre-accept/common-cleanup path, then use only the inherited remaining-budget wait and, if necessary, its sole exact-handle termination plus bounded exit proof;
- if start may have occurred but no exact handle is retained, classify owner/process and temp state `NOT PROVEN`, perform no process lookup/enumeration/reacquisition and no unsafe file/root deletion, and stop;
- if exact-handle exit proof fails, retain the handle, report fixed residual state, do not delete temp artifacts, and stop without retry;
- only after proven exit may fixed-hash/direct-child guards authorize removal of remaining files, safe log, and now-empty root; and
- emit fixed counters/booleans for start, handle retention, wait, termination, exit proof, file cleanup, root cleanup, and residual state. No exception text or process metadata may enter evidence.

This correction must cover failures in launch extraction, launch hash validation, dot-sourced launch, post-launch handle guard, success-terminal transport, nonblocking safe-log tuple inspection, and every interruption before masked acceptance.

## Preserved boundaries that are otherwise adequate

Subject to the two fixes above, the candidate correctly preserves:

- a genuinely new one-shot gate while leaving the incident gate spent;
- full fresh byte/hash, worktree, Windows identity/policy, VM, proxy/listener/network, Cloudflare, token-row, DNS, and OmniRoute-key revalidation;
- a new credential-free clipboard clear/read-empty proof rather than reusing the incident count;
- exact absence of incident temp/process residue before preparation;
- exactly one new private-proxy start and one deterministic R5 POST maximum;
- exact token name, zone, specific-zone scope, and only `Zone WAF Edit` plus `Zone Read`;
- no DNS, Tunnel, Access, public rollout, OmniRoute rollout key, model request, alternate bridge, second start/POST, dashboard Rulesets mutation, PATCH/edit, retry, fallback, handoff, or verdict relaxation;
- nonblocking safe-log proof of retained PID, `OWNER_READY=PASS`, and `SECRET_PROMPT_READY=PASS` before enabling final Create;
- separate mandatory action-time confirmation for final Create/native Copy/masked Paste and later exact-row deletion;
- zero agent inspection of the generated-token page or credential clipboard after Create;
- same-process token verification, private Zone-ID derivation, bounded exact-hash R5 child, universal post-accept revocation hold, invalidity proof, and guarded cleanup; and
- exact success only on the inherited terminal tuple, external owner exit, cleanup, refreshed `0 / 0`, and HTTP `401`.

Standing unattended authority does not waive either mandatory user confirmation and does not authorize retry of the incident or this replacement after any uncertainty.

## Disposition

The scope correction is technically sound, but the replacement contract is not yet safe or unambiguous as a whole. Fix both HIGH findings in a new committed brief and obtain a fresh independent Sol High review. Until then, the incident gate remains spent, this candidate authorizes no execution, and no browser, process, proxy, credential, Cloudflare, VM, routing, or cleanup action may be taken under it.
