# Task 21 Windows clipboard policy replacement — independent Sol High review

## Verdict

**PASS — zero blocking, HIGH, or IMPORTANT findings.** Task 21 is a fresh,
fail-closed replacement gate with its own one-shot lifecycle; it does not retry,
reuse, continue, relax, or rehabilitate spent Task 20. The reviewed contract is
internally consistent with the plan's Windows clipboard-history and
cross-device-sync prerequisite, and its executable block is limited to the two
intended machine-policy DWORD-zero writes.

This is a static review only. A PASS does not consume the gate and does not
authorize live execution.

`authorizes_live_execution=false`

## Reviewed evidence and integrity

- Static base / committed Task 20 classification:
  `09e18549188e9032f4e78076efefd6e9331bbd26`.
- Candidate Task 21 brief commit:
  `e7482fe91932cba4d63942460a04782128f23185`; its direct parent is the pinned
  Task 20 classification commit.
- The candidate commit adds exactly
  `.superpowers/sdd/2026-08-31-omniroute-secure-console-transfer/task-21-windows-clipboard-policy-replacement-brief.md`.
- Brief bytes: `14511`; SHA-256:
  `758D3CEF02439EFB404FBF91C5B074653F290C711E2FB0C0435C6B9A7E3B5B2B`.
- Direct-byte review package bytes: `15583`; SHA-256:
  `2FE5F55934C65B2FC836E96F2A07BFEEC85893D74D37ACA05138D06D5654E85F`.
- Before this review artifact was created, the Git index was empty and the
  unrelated worktree baseline remained exactly 12 status entries.
- The brief is strict UTF-8, has no BOM, uses LF only, and ends in exactly one
  LF. Its sole `powershell` fence parses with zero PowerShell parser errors.

No passing live check was rerun. The only checks performed were static byte,
Git, parser, AST, cardinality, ordering, prohibition, and redaction checks; the
embedded block was not evaluated or invoked.

## Specification and security review

### Fresh replacement-gate identity

PASS. The contract explicitly keeps Task 20 consumed and spent, assigns Task 21
its own eligibility and exactly one attempt, uses Task 21-specific success and
failure terminals, and forbids reuse, retry, continuation, fallback, repair,
rollback, alternate shell/interface, and verdict relaxation. Task 21's host
contract is deliberately different from Task 20's failed host contract: the
new gate requires an elevated 64-bit Windows PowerShell 5.1 Desktop process.
It does not claim that Task 20 remains eligible merely because Task 20 made zero
writes.

Standing unattended authority is correctly bounded. Task 21 becomes eligible
only after this fresh independent PASS and fresh action-time pins. Any rejected
call, nonzero exit, partial result, malformed/duplicate/extra output,
interruption, or observation uncertainty spends Task 21. The contract grants no
authority to revive either spent gate.

### Exact manual host and fresh preconditions

PASS. Before the first write, the block requires all of the following in the
same process:

- Administrator role is true;
- `PSEdition` is exactly `Desktop` and PowerShell major/minor are exactly
  `5 / 1`;
- both the OS and process are 64-bit;
- `[Environment]::OSVersion` is exactly `10 / 0 / 26200`;
- the four CIM values are exact: Windows 11 Pro, `10.0.26200`, build `26200`,
  and `64-bit`;
- the registry identity is exact: `Windows 10 Pro`, `Professional`, `25H2`,
  build `26200`, UBR `9278`;
- the machine policy key already exists;
- both target machine-policy values are absent; and
- HKCU `EnableClipboardHistory` is exactly `DWord / 1`.

Every lookup is under `$ErrorActionPreference = 'Stop'`; drift, missing data,
wrong type, wrong host, wrong bitness, or uncertainty reaches the fixed failure
path before mutation. The instructions require the user—not Codex, Computer
Use, terminal automation, or UAC automation—to open the exact elevated shell
and submit the reviewed block once as one block.

### Native policy mutation and serial state machine

PASS. The only executable registry mutation commands are exactly these two
serial `New-ItemProperty` calls against the already-existing
`HKLM:\SOFTWARE\Policies\Microsoft\Windows\System` key:

1. `AllowClipboardHistory`, `DWord`, value `0`;
2. `AllowCrossDeviceClipboard`, `DWord`, value `0`.

These are the two intended machine-policy states: disable clipboard history and
disable cross-device clipboard synchronization. There is no key-creation call.
The AST contains exactly two `New-ItemProperty` commands and zero bare
`New-Item`, `Set-ItemProperty`, `Remove-Item`, `Remove-ItemProperty`,
`Set-Clipboard`, `Get-Clipboard`, process-spawn, remoting, or dynamic-invocation
commands.

The exact executable ordering is:

1. increment first write-attempt counter;
2. perform the history write;
3. increment first write-fulfilled counter;
4. increment second write-attempt counter;
5. perform the cross-device write;
6. increment second write-fulfilled counter;
7. increment first readback-attempt counter, read history, then increment its
   fulfilled counter;
8. increment second readback-attempt counter, read cross-device, then increment
   its fulfilled counter;
9. require counters `2 / 2 / 2 / 2` and both exact `DWord / 0` states before
   emitting success.

Static cardinality confirms exactly two increments for each of the four counter
variables. Attempt counters are immediately before their corresponding calls;
fulfilled counters occur only after return. Because the operations are awaited
synchronous PowerShell commands in one displayed sequence and terminating
errors are enabled, no later operation begins after an earlier throw.

### Partial-write, failure, and residual-state handling

PASS. The catch path emits only the four reached counters plus
`RESULT=FAIL_STOP_NO_RETRY`, then exits `1`. It emits no exception object,
message, stack, registry value, identity, username, machine identifier, or
secret. A first-write success followed by any later failure is deliberately
left for independent classification; no deletion, rollback, repair, missing
operation, alternate interface, or retry is permitted. This is the correct
fail-closed treatment because attempting cleanup under uncertain partial state
would consume new mutation authority.

Success requires exit `0`, one fixed success terminal, exact counters, and both
exact readbacks. Missing, duplicate, additional, ambiguous, or uncertain output
cannot be interpreted as success. The fixed output includes only safe task/gate
states, counters, and the intended zero values.

### Prohibited authority and actions

PASS. Executable code contains no browser, clipboard content, credential,
Cloudflare, provider, VM, proxy, routing, service, scheduled-task, remoting,
process-spawn, UAC, Settings, Registry Editor, Local Group Policy Editor, HKCU
mutation, sibling-value mutation, key creation/deletion, value deletion,
fallback, retry, or rollback action. Static scanning found no credential marker
or secret-bearing value. The only member invocations are the required identity,
registry-read, role-check, output, and local object-close/dispose methods.

### Post-success proof and downstream boundary

PASS. Even an exact Task 21 terminal proves only this process's two calls and
immediate readbacks. The brief correctly requires a fresh read-only proof of the
same OS identity, existing policy key, and both target `DWord / 0` values,
followed by a separate Sol High classification, before any credential creation,
secret transfer, Cloudflare action, or later secure-console gate may rely on the
result. It also correctly states that clearing the current clipboard does not
prove clipboard-history erasure.

## Findings

None.

## Disposition

The Task 21 replacement contract is statically reviewable and fail-closed as
written. This PASS is evidence for eligibility review only. It neither performs
nor authorizes the one-shot action. A future owner must freshly pin the exact
committed brief and this review, revalidate every action-time precondition, and
then treat the first invocation—regardless of result—as the sole Task 21 gate
consumption. Any failure or uncertainty leaves Task 21 spent and requires a new
reviewed contract rather than a retry.
