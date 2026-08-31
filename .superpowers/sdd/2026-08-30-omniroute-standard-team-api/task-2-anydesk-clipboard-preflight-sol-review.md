# Task 2 AnyDesk clipboard preflight independent Sol High review

Reviewed at: `2026-08-31` (`Asia/Bangkok`)

Reviewer role: fresh independent Sol High, direct-byte, review-only. No script
was run; no browser, clipboard, process, VM1205, Cloudflare, OmniRoute,
proxy/proof/R5, Rulesets, evidence, token, credential, revocation, or authority
gate was touched. The only write is this review artifact.

## Verdict

**FAIL / REVISE BEFORE EXECUTION / NOT AUTHORIZED.**

The exact script is credential-free and directionally strong: it generates one
fresh CSPRNG challenge, validates a narrow temporary path, binds the emitted PID
to the retained handle, proves an empty baseline, permits only the exact
one-shot copy sequence, performs comparison reads only for `COPY_DONE`, and
converges its own terminal paths on clipboard and exact-script cleanup. The
brief also preserves the bounded conclusion and additive-evidence boundary.

Execution is not review-clean because the exact control/coordinator contract
has five IMPORTANT defects: a deadline race can accept a control line observed
after the monotonic timeout; blocking `ReadToEnd()` defeats the advertised
retained-handle exit timeout; startup/browser exceptions are not enclosed in an
executable coordinator cleanup state machine; the coordinator never
machine-validates the required output labels and counters; and destructive path
checks do not reject Windows reparse points.

No preflight execution is authorized. This review also authorizes no token,
credential, browser, clipboard, Cloudflare, VM1205, OmniRoute, proxy/proof/R5,
Rulesets, evidence mutation, revocation, deletion, or other live action.

## Direct-byte inputs

| Input | Independent result |
| --- | --- |
| Brief commit | `cca419b9958865360a2ae4f0efaa4f0805df6147` |
| Parent | exactly `d22c0250558ac92b9b4fdc0606e2e1003899698f` |
| Commit scope | exactly `task-2-anydesk-clipboard-preflight-live-brief.md` |
| Brief | `24,848` bytes; SHA-256 `1D251E7878077F11B5D638524646995A53673C5BE9D387C30367FAF170719F55`; blob `64cf802c2d47d806de68a0b87c8d69e9c8253902` |
| Working/direct equality | working file hashes to the exact committed blob |
| Brief encoding | strict UTF-8, no BOM, LF-only, one trailing LF |
| Exact fenced script contract | `8,301` bytes; SHA-256 `47CC3228B184D61328315D582748A7C145C98D9F4082D106E2E981F40A682F68` |
| Implementer report | SHA-256 `402110B6A93AE46ED353A61FD87AF09D33F5DA46488FCD3D27C44A1EECA549D7` |
| Diff package | SHA-256 `0B7D0FBF4177AACB678A871B18449CC27C8345F846C1F9BA2FC871DA0166E271` |

The supplied implementer parser/capability checks were not rerun because this
review found no concrete doubt about their reported script extraction, syntax,
PowerShell 7 overload availability, or static call counts. The exact committed
script and coordinator text were reviewed directly.

## Required-dimension results

| Dimension | Result |
| --- | --- |
| PowerShell 7 executability | **REVISE.** Script syntax/capability checks are reported clean, but the timeout and coordinator sequencing defects below prevent bounded execution. |
| Fresh CSPRNG challenge | **PASS.** `brief:131-135` fills a new 16-byte array at runtime and emits its 32-hex non-secret encoding. |
| Temp path/hash/size/deletion guard | **REVISE.** Lexical root/direct-child/leaf/command/hash/size checks are strong (`brief:88-115,233-275`), but reparse-point substitution is not rejected. |
| Retained handle/PID equality | **PASS for the normal path.** `brief:369-389` retains the process object and rejects PID mismatch before page creation. Exceptional cleanup remains underspecified. |
| Empty baseline | **PASS.** `brief:119-129` performs one clear and one shape-only empty read before challenge generation. |
| Exact copy sequence | **PASS.** `brief:401-431` pins one retained page, semantic focus, one `Control+A`, one `Control+C`, and exactly one terminal control action with no retry. |
| Cancelled read / no orphan race | **REVISE.** Cancellation is observed, but a line completing at the deadline can be accepted after timeout, and coordinator exit waiting is not actually bounded. |
| State comparison counts | **PASS in script logic.** `brief:146-177` increments comparison only for exact `COPY_DONE`, giving `1 / 0 / 0 / 0` for COPY_DONE / ABORT / EOF / timeout. |
| Script `finally` cleanup | **PASS in ordinary execution.** `brief:185-282` always attempts final clear, post-clear read, exact guarded deletion, counters, and cleanup label. Coordinator exceptional paths still need correction. |
| Page close / external exit / absence | **REVISE.** Required in prose, but not enclosed in a complete executable coordinator `finally`; the exit timeout is placed after blocking reads. |
| Counter consistency | **PASS in production script; REVISE in acceptance.** Script counters match its call sites, but the coordinator does not parse/enforce them. |
| Prohibited actions | **PASS.** No page serialization, screenshot, coordinate action, browser clipboard API, retry, fallback, alternate bridge, credential, network, or live-resource action is permitted. |
| Additive evidence and bounded conclusion | **PASS.** `brief:508-535` is additive-only and redacted; `brief:22-26` limits PASS to the observed non-secret local transport and authorizes no credential action. |

## Findings and minimum corrections

### F1 — IMPORTANT: deadline race can accept a control line after timeout

The script polls while both the read is incomplete and elapsed time is below the
deadline (`brief:137-144`). After leaving the loop, it checks only
`$readTask.IsCompleted` (`brief:146-178`). If the line completes at or just
after the deadline but before that post-loop check, the task is completed and
the script accepts `COPY_DONE` even though the monotonic deadline has expired.
The same race occurs when task completion makes the loop condition short-circuit
before elapsed time is evaluated.

This does not expose a credential, but it violates the exact timeout state and
can misclassify a late copy as the one allowed transport PASS.

Minimum correction: make deadline precedence fail closed. At loop exit, capture
and test a monotonic `deadlineReached` result before processing any completed
line. If elapsed time is at or beyond the deadline, cancel and observe the read
task and emit only `PREFLIGHT=TIMEOUT`, even if a line completed concurrently.
Alternatively use one exact reviewed `Task.WhenAny`/delay winner contract. Pin
the tie rule as TIMEOUT and preserve comparison count `0` for that state.

### F2 — IMPORTANT: blocking output reads make the 15-second exit timeout ineffective

The coordinator calls `StandardOutput.ReadToEnd()` and
`StandardError.ReadToEnd()` before `WaitForExit(15000)` (`brief:451-462`).
`ReadToEnd()` blocks until the child closes the stream, normally at process
exit. If the child hangs in cancellation, clipboard cleanup, filesystem access,
or another terminal path, the coordinator never reaches the stated timeout.
The retained-handle exit proof is therefore unbounded despite the label
`RETAINED_HANDLE_EXIT_TIMEOUT_NO_KILL_AUTHORIZED`.

Minimum correction: because the reviewed script's output is strictly bounded,
call `WaitForExit(15000)` first, then read stdout/stderr only after confirmed
exit. Or begin both stream reads asynchronously before the wait and bound all
three tasks. On timeout, do not kill; record the exact retained PID/process
residual, skip destructive root cleanup, close only the exact page, and stop
FAIL / NOT PROVEN for owner disposition.

### F3 — IMPORTANT: promised coordinator cleanup is prose, not one executable state machine

The startup block performs five blocking `ReadLine()` calls and throws directly
on any mismatch (`brief:369-389`). The prose then says a startup mismatch sends
`ABORT` and enters common cleanup (`brief:395-399`), but the exact coordinator
commands are not enclosed in a `try/catch/finally` that performs that sequence.
The browser path similarly relies on prose to send ABORT on ambiguity
(`brief:401-431`) and to close the exact page in a coordinator finally
(`brief:464-480`).

Consequences include an unbounded startup read, a throw before ABORT/stdin
closure, writing ABORT to a child that may already have exited, missed retained
handle disposal/exit proof, or skipped exact-page/root cleanup. The child has a
120-second self-timeout after reaching its control read, but that does not make
the coordinator contract atomic or prove cleanup on failures before that point.

Minimum correction: replace the fragments with one complete reviewed
coordinator `try/catch/finally` after `Start()` that:

1. bounds all five startup reads and checks retained-process exit while waiting;
2. records whether a control line was sent and permits exactly one;
3. on any startup/browser/key exception, sends ABORT only if stdin remains open
   and the retained child is alive, then closes stdin;
4. performs the bounded exit/output sequence from F2;
5. closes only the retained page handle if created;
6. proves script/root absence only after confirmed process exit; and
7. always disposes the retained process handle.

Before spawn, the same exact block should verify the reviewed brief commit/hash
and exact script hash so coordinator drift stops before process creation.

### F4 — IMPORTANT: PASS acceptance does not machine-validate labels or counters

After startup, the coordinator stores the remaining output and exit code but
does not parse them (`brief:454-462`). The prose requires all expected labels
and counters (`brief:482-488`), yet no executable check rejects duplicates,
missing/unexpected lines, a terminal label inconsistent with exit code, or
counter values inconsistent with the selected state. This is especially
material because the prior incident involved a misleading unconditional PASS
label.

Minimum correction: add an exact output parser to the coordinator contract.
For overall PASS require exactly one each of:

- `PREFLIGHT=PASS`;
- both clipboard cleanup PASS labels;
- script guard/delete PASS;
- counters `baseline writes=1`, `baseline reads=1`, `comparison reads=1`,
  `final writes=1`, `post-clear reads=1`;
- `CLEANUP=PASS`; and
- exit code `0`, empty stderr, retained-handle exit, exact-page close, and
  external absence PASS.

For ABORT/EOF/TIMEOUT require comparison `0`, the matching single terminal
label, cleanup counters/labels, and the reviewed nonzero exit. Reject duplicate,
unknown, missing, or out-of-order output and never relax the result manually.

### F5 — IMPORTANT: deletion safety is lexical and does not reject reparse points

The script and coordinator validate normalized strings, direct-child layout,
leaf name, size, and hash (`brief:88-115,233-275,310-340,469-480`). They never
reject `FileAttributes.ReparsePoint` on the fresh root or script. On Windows, a
same-user process could replace the temporary root with a junction/symlink
between creation and deletion. Lexical parent checks would still pass while the
resolved object could be outside the reviewed temporary directory. The hash
guard limits the target content but does not restore the promised location
boundary.

Minimum correction: after creation, before script start, immediately before
internal deletion, and before external root deletion, require that the temp root
and script exist as ordinary non-reparse directory/file objects; reject any
reparse attribute or identity drift. Use a non-recursive external deletion only
after confirmed child exit and exact emptiness. Dispose the directory enumerator
or use a materialized non-recursive entry list before deleting the root. Any
reparse/drift mismatch stops without deletion.

## Conditions for a future PASS

A revised exact brief may earn **PASS FOR ONE NON-SECRET PREFLIGHT EXECUTION
ONLY** after a fresh direct-byte reviewer confirms:

1. timeout wins every deadline race and preserves comparison `0`;
2. retained-handle wait/output collection is actually bounded;
3. one executable coordinator state machine covers startup, browser ambiguity,
   control send, page closure, exit, absence proof, and disposal;
4. exact labels/counters are machine-validated; and
5. destructive path checks reject reparse/identity drift.

Even that future PASS must require a separate exact action-time preflight
decision and must authorize no token/credential, Cloudflare, VM1205, OmniRoute,
proxy/proof/R5, Rulesets, evidence mutation, revocation, or other live action.
