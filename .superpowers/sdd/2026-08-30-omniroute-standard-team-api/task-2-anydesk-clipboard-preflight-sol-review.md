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

## Fix round 1 scoped re-review

Reviewed fixed commit:
`c4cdbed6ce3356c6764d00e9c49aa1256e504844` with exact parent
`3766434cc21aed398c1789c0aa71f5adef0c59f7` and exactly one changed path: the
preflight brief. The working brief equals its exact committed blob.

| Input | Direct-byte result |
| --- | --- |
| Revised brief | `41,311` bytes; SHA-256 `267744B2428AD23FB096F364686BD894D283323096A52FD15CAAA43E20DE28B1`; blob `39fc31e00188408cd6b716133f220381c29222ae` |
| Revised fenced script | `12,839` bytes; SHA-256 `2DC4024A95E916FFA1DE38DBD31F878F4593AEFFF50B393AD02E4177C6FEF1B6` |
| Fix report | SHA-256 `B27C8F6F5508A53E3B6A7EA6C2EB7585A0CE25C04E11F3760828606C72EF4EE8` |
| Fix diff package | SHA-256 `55F46FBF8BA9CB597A06439835DFAE83B93D140F17D36C7CC614211ED3ED3D24` |

### Scoped verdict

**FAIL / REVISE BEFORE EXECUTION / NOT AUTHORIZED.**

F1, F2, and F4 are **ADDRESSED**. F3 and F5 are **NOT ADDRESSED**. The fix
adds no new Critical, HIGH, or IMPORTANT defect outside those two residual
original findings. The remaining gaps are still IMPORTANT: resource cleanup
does not cover temp creation or a failed spawn, and the Win32 identity helper
closes each handle before the path-based write/delete that it is meant to
protect.

No preflight execution is authorized. This scoped review also authorizes no
token, credential, browser, clipboard, Cloudflare, VM1205, OmniRoute,
proxy/proof/R5, Rulesets, evidence mutation, revocation, deletion, permission
change, or other live action.

### F1 — ADDRESSED

`brief:231-250` polls the cancellable read under a monotonic stopwatch, captures
`$deadlineReached` immediately after the loop, and gives deadline/tie precedence
before examining any completed line. Every elapsed-at-or-beyond-deadline case
cancels and observes the task, emits only `PREFLIGHT=TIMEOUT`, exits `2`, and
leaves comparison reads at `0`. A line is processed only when the deadline was
not reached (`brief:250-273`). This closes the late-line false-accept race.

The startup-line helper applies the same fail-closed ordering at
`brief:433-472`. The scoped review finds no new timeout-tie defect in the fix
diff.

### F2 — ADDRESSED

The coordinator calls retained-handle `WaitForExit(15000)` before either
`ReadToEnd` (`brief:716-727`). Only confirmed exit permits bounded post-exit
stdout/stderr collection and exit-code access. Unconfirmed exit records the
exact residual PID, performs no kill, and blocks destructive absence cleanup
(`brief:728-760`). Page closure is still attempted and the retained handle is
disposed (`brief:735-763`). The previously ineffective timeout is now reachable
and fail closed.

### F3 — NOT ADDRESSED

The fix supplies a coherent post-spawn state machine for startup reads,
browser adapters, one control attempt, ABORT, stdin closure, exit/output, exact
page closure, external absence checks, and handle disposal
(`brief:637-763`). That closes the browser/startup exception paths after the
state variables and process object exist.

However, the coordinator creates the fresh root, writes the reviewed script,
captures identities/hashes, and performs pre-start checks before entering that
`try` (`brief:592-617`; the `try` begins at `brief:658`). A failure after root
creation or script write therefore exits the program without any coordinator
cleanup. A `Process.Start()` failure inside the `try` also leaves
`$spawned=false`; the `finally` then skips both the exit-confirmed absence block
and any exact pre-spawn script/root cleanup (`brief:658-662,711-760`). The result
can be a retained exact script and temporary root with no child available to run
the script's self-cleanup.

Minimum correction: begin the coordinator resource `try/finally` before fresh
root creation and track `rootCreated`, `scriptCreated`, spawn-attempted,
spawn-confirmed, and residual-process state. When no child was spawned, use the
same independently reviewed identity/hash guard to delete only the exact script
and then the exact empty root. When spawn outcome or PID is uncertain, perform
no deletion and report the exact retained path/PID for owner disposition. Always
dispose any created process handle. The outer state machine must cover every
return/throw after the first filesystem mutation, not only work after `Start()`.

### F4 — ADDRESSED

`brief:765-837` parses exactly eleven ordered tail lines after the already
validated five startup lines. It derives the only permitted comparison count
and exit code from the single terminal label, constructs an exact expected
sequence, rejects missing/duplicate/unknown/blank/out-of-order output, requires
empty stderr, and gates overall PASS on exact `COPY_DONE`, exit `0`, page close,
script/root absence, no coordinator failure, and no residual PID.

The parser correctly requires comparison `1` for PASS or COPY_DONE mismatch and
`0` for ABORT/EOF/TIMEOUT; cleanup counters are exactly `1 / 1 / 1 / 1` around
that comparison value (`brief:789-819`). No manual verdict relaxation remains.

### F5 — NOT ADDRESSED

The added Win32 helper is useful but does not make creation or deletion
identity-safe. `GetOrdinaryIdentity` opens with
`FILE_FLAG_OPEN_REPARSE_POINT`, rejects reparse/kind mismatch, returns the
volume/file ID, and then disposes the handle (`brief:97-176,475-554`). Every
later write, read, `Remove-Item`, or `Directory.Delete` is a new path lookup.

Two concrete substitution windows remain:

1. The coordinator calls `WriteAllBytes($scriptPath, ...)` before it first opens
   the script path with the identity helper (`brief:592-603`). `WriteAllBytes`
   uses replace/create semantics; an existing raced symlink/reparse object at
   that fresh leaf can be followed and overwritten before the subsequent
   reparse check rejects it.
2. The child closes its final root/script identity handles and then performs a
   path-based `Remove-Item` (`brief:353-373`). A same-user swap after the last
   identity check can redirect deletion without another hash/identity check.
   External root deletion similarly closes the identity handle before the
   path-based delete (`brief:745-755`), although non-recursive emptiness limits
   that consequence.

Minimum correction:

- create the script atomically with create-new/no-overwrite semantics so any
  pre-existing file, hard link, symlink, or reparse object fails before bytes
  are written;
- extend the Win32 helper to return/retain ordinary safe handles and perform
  the final identity/hash verification and script disposition through the same
  retained handle (for example, `SetFileInformationByHandle` with reviewed
  delete disposition), rather than closing the handle and calling
  path-based `Remove-Item`;
- retain or equivalently bind the ordinary root handle through the final
  materialized-empty check and non-recursive root disposition; and
- on any handle, identity, reparse, hash, or disposition mismatch, stop without
  deleting a path-resolved substitute.

The current reparse checks reduce risk but do not close the Windows TOCTOU
boundary promised by the fix.

### Fix-round-1 conclusion

The revised brief cannot yet earn **PASS FOR ONE NON-SECRET PREFLIGHT EXECUTION
ONLY**. A narrow second fix should extend the coordinator state machine over
all filesystem mutations/spawn failure and replace check-then-path-write/delete
with atomic create-new and retained-handle disposition. A fresh scoped
direct-byte review is required afterward. Any eventual PASS must still require
separate exact action-time preflight authority and authorize no credential or
other live action.

## Fix round 2 scoped re-review

Reviewed fixed commit:
`016e4c97c00afcd9206b4e1d54591149509cd730` with exact parent
`499ce07ca160e963ac5c9196173d3e243b8ede9e` and exactly one changed path: the
preflight brief. The working brief equals its exact committed blob.

| Input | Direct-byte result |
| --- | --- |
| Revised brief | `58,187` bytes; SHA-256 `E2CC2303E3028D9D1E3DAE244F00B05CC3658C59E435F2365BF35F76900CCAC8`; blob `6ca618fb2b8dbd591d99c33cde7b41fca58f1859` |
| Revised child script | `23,823` bytes; SHA-256 `4972F7C274E18A90E70DF35DCD2BBADC583A708E9B183B7C3F21627CE7522E04` |
| Revised coordinator | `23,958` bytes; SHA-256 `EB9812BF3DA8A42011C27D83F05A4A1879CE9F1ADF8E5912F4E93AB749BE5569` |
| Fix report | SHA-256 `013F41053E5F1451081E39B00DE41D7E34F4D8374E8472C5DDC3EA325D59777F` |
| Fix diff package | SHA-256 `5142449E9868465C18089BB3A8C4A5E98B6D926111A335B7AA70EF6B21CBE9F2` |

The fixed brief is strict UTF-8 without BOM, LF-only, and has exactly one
trailing LF. This review was direct-byte/static only. It did not compile or run
the child, helper, coordinator, browser adapter, clipboard operation, process,
or deletion.

### Scoped verdict

**FAIL / REVISE BEFORE EXECUTION / NOT AUTHORIZED.** F3 is **ADDRESSED**. F5 is
**NOT ADDRESSED** because the new handle implementation leaves one HIGH script
integrity break. No Critical or additional IMPORTANT/HIGH breakage was found in
the fix diff.

### F3 — ADDRESSED

The outer resource `try` now starts at `brief:879`, before the first filesystem
mutation at `brief:881`, and the state declared at `brief:851-877` tracks root
and script creation, spawn attempt/confirmation/uncertainty, residual process,
PID, and every safe/process handle. Setup and all later throws remain inside
that resource scope (`brief:879-1007`). The inner `catch/finally` attempts the
single ABORT only for a confirmed live child, closes stdin, waits for exit,
captures bounded output only after confirmed exit, and closes the exact page
(`brief:1007-1054`).

The outer `finally` treats a thrown `Start()` as uncertain and retains exact
paths/PID without disposition, treats an explicit no-child result as eligible
for cleanup, performs no-child/confirmed-exit cleanup, reports any retained
artifacts, and disposes all handles without killing (`brief:1055-1121`). This
closes the original missing pre-mutation and failed-spawn state-machine scope.
The handle integrity issue below is classified under F5 rather than reopening
F3's control-flow finding.

### F5 — NOT ADDRESSED; new HIGH script-integrity break

The intended TOCTOU corrections are otherwise present: script creation is
Win32 `CREATE_NEW`, and write/flush/identity/read/hash all use the returned
handle (`brief:246-258,887-895`); the child derives delete access from its
already retained object with `ReOpenFile`, revalidates identity/hash, and calls
`SetFileInformationByHandle` on that object (`brief:619-646`); coordinator
fallback opens an ordinary non-reparse handle and validates identity/hash on
that same handle before disposition (`brief:288-312,1070-1090`); and the exact
ordinary root handle is retained from `brief:883` through materialized
emptiness and handle disposition at `brief:1096-1101`. The destructive
disposition calls themselves are handle-based; no `Remove-Item`, path-based
`Directory.Delete`, or recursive deletion was introduced.

However, both `CreateScriptNew` and the coordinator's supposed lifetime guard
grant `FILE_SHARE_WRITE` (`brief:246-255,274-283`). After the exact guard hash at
`brief:899-900`, that guard remains write-shareable while `pwsh -File` opens and
loads the script (`brief:919-985`). A same-user writer can therefore mutate the
reviewed file after validation and while PowerShell is parsing it. The child's
own validation cannot make this safe: it occurs only after the potentially
modified script has already been loaded and begun executing. Moreover, the
child lifetime handle also grants `FILE_SHARE_WRITE` (`brief:260-269`), allowing
post-ownership mutation that can defeat deterministic final hash/deletion.
This is a new **HIGH** issue in the fix diff because unreviewed script bytes can
execute under the preflight owner process.

Minimum correction: make `OpenScriptGuard` share read only (no write or delete),
then revalidate identity/size/hash after that guard is successfully acquired
and retain it through exact `OWNER_READY=PASS`. Make the child's lifetime handle
share read plus delete, but not write, so the coordinator-to-child handoff
preserves immutability and the child can still derive delete access with
`ReOpenFile`. Any incompatible outstanding writer, acquisition failure, or hash
drift must stop before spawn or before acceptance with no retry. A fresh scoped
direct-byte review is required.

### Fix-round-2 conclusion and authority boundary

This revision does not earn **PASS FOR ONE NON-SECRET PREFLIGHT EXECUTION
ONLY**. It authorizes no preflight, script/helper/coordinator execution,
browser, clipboard, token, credential, Cloudflare, VM1205, OmniRoute,
proxy/proof/R5, Rulesets, evidence mutation, revocation, deletion, permission
change, or other live action. Any later corrected PASS would still require a
separate exact action-time authorization for one non-secret preflight only.

## Fix round 3 scoped re-review

Reviewed fixed commit:
`49bb3ab533b91b98c1a3cb70a7c20cb626093928` with exact parent
`b72a70ab7c9d2c36ac2e91ac30549dcc24d50a2b` and exactly one changed path: the
preflight brief. The working brief equals its exact committed blob.

| Input | Direct-byte result |
| --- | --- |
| Revised brief | `58,331` bytes; SHA-256 `514320C3D80BA7529847A3634BAF0837BE71C325DE80016A78EE6293D239F4B6`; blob `13df28dfeeb3b152222ba99adc2383d7eeb5db84` |
| Revised child script | `23,758` bytes; SHA-256 `16470D5E7F68773B259B49C7EC24D46B3A2D4B5238DCB71986990D6B73C5C367` |
| Revised coordinator | `23,958` bytes; SHA-256 `A42E058813231AF53D6502A2FB3341641E32040E22DBC130E62C6453F3A871AE` |
| Fix report | SHA-256 `FD6303A4B3785257E858FAEF9F2FE519B3954FC1D58E60D7213C612F2215AAD6` |
| Fix diff package | SHA-256 `E7A753A6F1138F339B06E569BE4BB0CD1E176AC57D4DF006C94961142FCD3B1D` |

The fixed brief is strict UTF-8 without BOM, LF-only, and has exactly one
trailing LF. Direct-byte extraction yields exactly two fenced PowerShell
blocks and independently reproduces the pinned child/coordinator sizes and
hashes above. This review did not compile or run any script, helper,
coordinator, browser adapter, clipboard operation, process, or deletion.

### Scoped verdict

**PASS FOR ONE NON-SECRET PREFLIGHT EXECUTION ONLY.** The sole HIGH F5 finding
is **ADDRESSED**. The narrow fix diff introduces no new Critical, HIGH, or
IMPORTANT issue, and the prior F1-F5 corrections remain intact.

### F5 — ADDRESSED

Atomic `CREATE_NEW` now returns a write-capable creation handle whose share mode
is exactly `ShareRead`, excluding every concurrent writer and delete/rename
handle while the reviewed bytes are written, flushed, identified, sized, and
hashed (`brief:246-258,887-895`). After that handle closes, the coordinator
opens a guard whose share mode is also exactly `ShareRead` and validates the
recorded identity, byte size, and SHA-256 through that guard before the sole
spawn (`brief:274-285,897-900,950-968`). A writer retained across the handoff
would make guard acquisition fail; a mutation or substitution completed in the
transition is rejected by the post-acquisition identity/size/hash validation.

The guard remains retained while `pwsh -File` loads the exact script and until
the coordinator has received and validated exact `OWNER_READY=PASS`
(`brief:919-927,970-986`). Before emitting that label, the child opens its exact
ordinary script object, verifies identity/size/hash, and retains the handle
(`brief:453-488`). That lifetime handle shares `ShareRead | ShareDelete` and
never `ShareWrite` (`brief:260-271`), so when the coordinator releases its
guard, no write window opens. The delete-capable child and coordinator handles
and the child's `ReOpenFile` handle likewise share read plus delete without
write (`brief:288-312`). The child's final identity/hash verification and
`SetFileInformationByHandle` disposition remain on the retained object
(`brief:612-646`). Thus unreviewed script bytes cannot be introduced between
pre-spawn validation, PowerShell load, child ownership, and final disposition.

The diff changes only these file share modes, the exact script pins, and the
corresponding explanatory prose. It preserves the prior fresh challenge,
deadline-tie cancellation, bounded retained-process exit/output handling,
single coordinator resource state machine, ordered terminal parser and
counters, atomic no-overwrite creation, identity/reparse guards, handle-based
file/root disposition, no-retry rule, and fail-closed authority boundaries.

### Fix-round-3 conclusion and authority boundary

This is a static contract PASS for the exact brief, child, and coordinator
bytes above. It does not itself authorize or perform the preflight. One exact
non-secret preflight still requires a separate action-time authorization. This
review authorizes no token, credential, Cloudflare, VM1205, OmniRoute,
proxy/proof/R5, Rulesets, evidence mutation, revocation, permission change, or
other live action.

## Fix round 4 scoped re-review — host-rendezvous bridge amendment

Reviewed exact head `e1af4b67d156e115aa451cb778a3a454d0a0df4f`
against exact base/parent `571815925a5b48d7d1388a44e6f7bf8afe48a18e`.
The commit changes exactly one path: the preflight live brief. The working file
equals the exact committed blob.

| Input | Direct-byte result |
| --- | --- |
| Revised brief | `87,225` bytes; SHA-256 `7DBC9154EEE21AEE42726340B91E170CC7DDA43EA70BE1DB922066422FA391A1`; blob `17bae8404a7cb3c11e296455278c5de28b27c554` |
| Child script | unchanged `23,758` bytes; SHA-256 `16470D5E7F68773B259B49C7EC24D46B3A2D4B5238DCB71986990D6B73C5C367` |
| Coordinator | unchanged `23,958` bytes; SHA-256 `A42E058813231AF53D6502A2FB3341641E32040E22DBC130E62C6453F3A871AE` |
| Bridge runner | `19,375` bytes; SHA-256 `2EBD922B5156CFCE9E643E39DE3C5F7CB6987002E592D2F2A3CEF940B6872C77` |
| Fix report | `6,690` bytes; SHA-256 `ECFB8D786DA13F4A23E0A09841D70930E2B577054F631FCD289BA5E175A9091C` |
| Review package | `35,299` bytes; SHA-256 `96D0ED0DC6FA446D0008460603469CB6EE4354FE62832A40ED4E1982D88C24EB` |

The brief is strict UTF-8 without BOM, LF-only, with exactly one trailing LF.
Direct extraction finds exactly three PowerShell blocks and independently
reproduces all three pinned block sizes/hashes. No script, helper, runner,
coordinator, Node block, browser action, clipboard action, or preflight was
compiled or executed in this review.

### Scoped verdict

**FAIL / REVISE BEFORE EXECUTION / NOT AUTHORIZED.** The PowerShell bridge's
normal-path nonce and OPEN/COPY/CLOSE parser are coherent, but the amendment
has one new HIGH and three new IMPORTANT execution-contract defects. It does not
earn **PASS FOR ONE NON-SECRET PREFLIGHT EXECUTION ONLY**.

### Verified portions

The runner creates one fresh 16-byte CSPRNG nonce and derives its sole opaque
PowerShell handle from that nonce (`brief:1415-1419`). It checks the working
brief against the reviewed commit and all action-time block pins before spawn
(`brief:1370-1413`). Its PowerShell line reader uses `Stopwatch`, one
cancellable `ReadLineAsync`, and elapsed-at-or-beyond-deadline precedence before
examining a completed line (`brief:1331-1368`). The normal success parser binds
every request/response to the nonce and opaque handle, enforces OPEN then COPY
then CLOSE, permits one accepted line at each state, requires exact six-line
coordinator PASS/exit `0`/empty stderr, and gates PASS on all six counters being
`1` (`brief:1505-1639`).

The documented normal Chrome sequence uses the persistent `chrome` binding,
one `tabs.new`, one data-URL navigation, one exact accessible-name locator and
semantic click, one `Control+A`, one `Control+C`, and one retained-tab close
(`brief:1746-1816`). Executable browser snapshot/screenshot/content extraction,
title/URL lookup, clipboard API, coordinate, reload, alternate-tab, fallback,
and retry calls remain absent. The prior child/coordinator fixes are unchanged.

### R4-F1 — HIGH: Node deadlines do not cancel, settle, or give ties fail-closed precedence

`bridgeWithinDeadline` is only `Promise.race(operation(), setTimeout(...))`
(`brief:1725-1735`). A losing Chrome/Playwright promise continues running after
the wrapper has returned an ABORT; there is no cancellation, no wait for the
loser to settle, and no monotonic elapsed-time check after an operation wins.
Thus a deadline tie can be accepted rather than rejected.

The consequences are load-bearing. If `chrome.tabs.new()` resolves after its
timer, assignment to `bridgeTab` never occurs and the late-created tab is
unowned and cannot be closed (`brief:1753-1768`). A late focus, select, or
`Control+C` can execute after COPY has returned ABORT and can repopulate the
clipboard after the child reported final clear (`brief:1786-1796`). A late
`goto` or `close` similarly leaves page state and exact closure unproven
(`brief:1754-1766,1806-1815`). This contradicts the claimed terminal
convergence at `brief:1821-1826` and the required atomic exact-tab ownership.

Minimum correction: do not impose mutation deadlines with an uncancelled
`Promise.race`. Use operations with native bounded cancellation/settlement, or
retain and observe each actual operation promise so no response is emitted
until it has settled and every created tab is captured. Use a monotonic clock
and recheck elapsed time after settlement so elapsed-at-or-beyond-deadline wins
every tie. On any timed-out copy action, prove the action cannot complete after
cleanup; on any timed-out page creation/navigation/close, prove the exact tab
closed or report its retained exact Node handle and stop without acceptance.

### R4-F2 — IMPORTANT: OPEN failure can hide a retained exact tab

Even apart from the uncancelled-race defect, the OPEN catch converts a failed
or timed-out close into generic `BRIDGE_ABORT|<NONCE>|OPEN` while leaving
`bridgeTab` non-null in `OPEN_ABORT_RETAINED` (`brief:1758-1768`). The nested
`OpenExactPage` then throws without returning an opaque handle, so its
coordinator never issues CLOSE. The protocol carries neither retained-tab
status nor a later exact disposition request. This violates the existing
atomic adapter rule and the prose promise to return ABORT only after exact
created-tab closure has settled (`brief:681-696,1738-1743`).

Minimum correction: OPEN may return ordinary ABORT only after absence/closure
of every created tab is confirmed. If exact closure cannot be confirmed, emit
a distinct fail-closed retained-tab terminal state bound to the nonce, preserve
the actual Node `Tab`, report it for sole-owner disposition, and forbid bridge
or preflight acceptance. Do not retry or open a replacement.

### R4-F3 — IMPORTANT: bridge failure does not prove nested coordinator-process exit

The runner starts a new coordinator process without start-attempt,
start-confirmed, PID, or uncertain-spawn state (`brief:1497-1501`). Its normal
path performs one bounded exit wait (`brief:1611-1616`), but every exceptional
path merely closes stdin when convenient and disposes the process object
(`brief:1640-1649`). Disposing a `Process` object does not terminate or prove
exit of the OS process. A start exception, total-output timeout, failed pipe
write, or exit timeout can therefore leave an unreported nested coordinator
and its clipboard-owner child after the bridge itself exits.

Minimum correction: retain and report start-attempt/confirmation/uncertainty,
exact PID, stdin-close result, and process exit. On every failure, close stdin
once and perform one bounded retained-handle exit wait; do not read output
before confirmed exit. If spawn or exit remains uncertain, perform no retry or
kill, emit the exact retained/unknown PID and residual state, and keep all
acceptance false for owner disposition.

### Additional protocol strictness

The prose says every duplicate or unknown host input is rejected
(`brief:1666-1691`), but after accepting CLOSE the runner never reads host stdin
again (`brief:1582-1602,1611-1639`). A valid CLOSE response followed by a
duplicate or unknown line can therefore still produce bridge PASS. Before any
future PASS, either require bounded host-input EOF after the one CLOSE response
and reject any trailing line, or narrow the claimed protocol and provide an
equivalent host-enforced exact-one-write proof. This is an IMPORTANT parser
contract mismatch because the six counters count consumed responses, not all
supplied protocol lines.

### Round-4 conclusion and authority boundary

The exact bridge amendment is **FAIL / REVISE BEFORE EXECUTION**. No preflight,
PowerShell bridge, Node/Chrome action, clipboard action, token, credential,
Cloudflare, VM1205, OmniRoute, proxy/proof/R5, Rulesets, evidence mutation,
revocation, permission change, or other live action is authorized. A corrected
exact-byte bridge requires another fresh independent review and, even after
PASS, a separate exact action-time authorization for one non-secret preflight.

## Fix round 5 final scoped re-review

Reviewed exact head `1e0beb0b39fd054c178d6508e1baf65b092ace00`
against exact base/parent `6ed6c224591e36efe0f2639910decdc415dea0f0`.
The commit changes exactly one path: the preflight live brief. The working file
equals the committed blob.

| Input | Direct-byte result |
| --- | --- |
| Revised brief | `96,444` bytes; SHA-256 `E649220FA6FF3FA06C079A8BFEF68EEA16B50C6F344C2FFD93691C71DFDB2766`; blob `cbe6ab1b918515831cc2349480953541d8c29fea` |
| Child script | unchanged `23,758` bytes; SHA-256 `16470D5E7F68773B259B49C7EC24D46B3A2D4B5238DCB71986990D6B73C5C367` |
| Coordinator | unchanged `23,958` bytes; SHA-256 `A42E058813231AF53D6502A2FB3341641E32040E22DBC130E62C6453F3A871AE` |
| Bridge runner | `24,634` bytes; SHA-256 `739E597C0BE39AE9A4CFBAE97F327F4FA7398160B13367ED37F47954EBBAF552` |
| Fix report | `3,128` bytes; SHA-256 `683E0C2201A9B76A47C7543D346529A0562664D10715384753B89AD9A2BBBD49` |
| Review package | `33,261` bytes; SHA-256 `905B030AAC9C3D4B0165EC283CC2F9BE1C939E133C461B51DED67E3284DE8FA9` |

The brief is strict UTF-8 without BOM, LF-only, with exactly one trailing LF.
Direct extraction finds exactly three PowerShell blocks and independently
reproduces every pinned block size/hash. No embedded PowerShell, Node/browser,
clipboard, process, or preflight code was executed.

### Final scoped verdict

**FAIL / NOT AUTHORIZED.** One load-bearing HIGH defect from round 4 remains.
Therefore the exact amendment does not earn **PASS FOR ONE NON-SECRET
PREFLIGHT EXECUTION ONLY**. No additional new Critical, HIGH, or IMPORTANT
defect was found in the round-5 diff.

### Round-4 finding disposition

- **R4-F1 — NOT ADDRESSED.** The local JavaScript `Promise.race` was removed,
  but the independent bridge-response deadline still races the same browser
  mutation and can initiate cleanup before that mutation settles.
- **R4-F2 — ADDRESSED when a Node block returns.** Late tab creation is captured
  before its elapsed verdict; failed OPEN/CLOSE disposition retains the actual
  `bridgeTab` and returns a nonce/opaque-handle-bound retained-tab terminal line
  that forces acceptance false (`brief:1584-1595,1674-1683,1863-1906,1941-1974`).
- **R4-F3 — ADDRESSED.** The runner records start attempt/confirmation,
  uncertainty, PID, one stdin close, one bounded exit wait, confirmed exit, and
  residual state; every post-process failure reaches the same helpers, no kill
  or retry exists, and redirected stderr is read only after confirmed exit
  (`brief:1435-1474,1538-1554,1696-1700,1719-1739,1757-1764`).
- **R4-F4 — ADDRESSED.** Exact CLOSE success performs one bounded fourth read,
  accepts only EOF, rejects a trailing line or timeout, and includes EOF and
  trailing counters in PASS (`brief:1651-1673,1714-1723,1774-1777,1798-1806`).

Static inspection also confirms one runtime 16-byte CSPRNG nonce, no retry, no
process kill, and no executable browser clipboard, DOM snapshot/content,
screenshot, coordinate, reload, alternate-tab, or fallback API. The prior
child/coordinator fixes and hashes remain unchanged.

### R5-F1 — HIGH: the outer 45-second rendezvous can still abandon a live browser mutation

`bridgeObserveOperation` awaits an operation without any cancellation or
native upper bound and computes elapsed time only after it settles
(`brief:1844-1859`). In parallel, the PowerShell runner gives each host response
only 45 seconds (`brief:1377,1574-1583,1611-1620,1641-1650`). When that outer
deadline expires, it synthesizes `BRIDGE_ABORT` and sends it to the nested
coordinator even though the sole-owner Node call can still be awaiting the
browser mutation.

This preserves the exact round-4 hazard across a different boundary. A
`Control+C` that settles after 45 seconds can run after the coordinator has
sent ABORT and the child has performed its final clipboard clear
(`brief:1614-1631,1923-1938`). A late `tabs.new`, navigation, or close can settle
after the bridge has already failed without ever delivering the retained-tab
terminal signal (`brief:1577-1598,1880-1905,1952-1974`). The fact that the Node
block itself emits no response before settlement (`brief:1816-1823`) does not
prevent the independent bridge process from timing out and advancing cleanup.
Thus mutation settlement, exact tab ownership, final clipboard emptiness, and
retained-tab reporting are not guaranteed on every terminal path.

Closing this finding would require browser mutations with a native,
reviewed cancellation/settlement guarantee that completes before the outer
rendezvous deadline, or a protocol that cannot advance coordinator/clipboard
cleanup while the host reports an operation outstanding. Merely awaiting an
unbounded promise while another process times out is not fail closed.

### Final authority boundary

Round 5 is final and remains **FAIL / NOT AUTHORIZED**. No preflight, bridge,
Node/Chrome action, clipboard action, token, credential, Cloudflare, VM1205,
OmniRoute, proxy/proof/R5, Rulesets, evidence mutation, revocation, permission
change, or other live action is authorized. The earlier child/coordinator PASS
does not authorize this failed bridge path or any action-time gate consumption.
