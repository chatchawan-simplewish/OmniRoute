# Task 20 Windows clipboard policy — independent Sol High static review

Review timestamp: `20260901 040119` (Asia/Bangkok)  
Reviewed brief commit: `1c45e8e5deb19e2f1bbd5ef6dbabfbf532424a32`  
Pinned base: `3f871b2d583ea1b04673ecbe7ca3e2362a9bbead`  
Direct-byte package: `14161` bytes / SHA-256 `84C8E12131C2411CA360C7DABCFE46B1A89B9792B5CC01BE7A5DDA8C9B7D82A8`  
Scope: static committed-byte, parser, cardinality, and official-documentation review only. No registry, policy, elevation, UAC, terminal, clipboard, browser, credential, process, service, scheduled-task, remoting, or routing action was performed.  
`authorizes_live_execution=false`

## Verdict

- Specification/security verdict: **FAIL / REVISE BEFORE EXECUTION**.
- Quality verdict: **FAIL**.
- Findings: **2 HIGH, 1 IMPORTANT**.
- Microsoft policy names, registry mappings, value semantics, edition support, and minimum-build applicability are otherwise correct.
- This review grants no execution, retry, repair, rollback, terminal, or UAC authority.

## Confirmed Microsoft semantics

The brief accurately cites the two authoritative device policies:

- Microsoft documents `AllowClipboardHistory` for Pro and later editions on Windows 10 version 1809 and later, mapped to `Software\Policies\Microsoft\Windows\System\AllowClipboardHistory`; value `0` means history is not allowed and the change takes effect immediately. See [Policy CSP - Experience: AllowClipboardHistory](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-experience#allowclipboardhistory).
- Microsoft documents `AllowCrossDeviceClipboard` for Pro and later editions on Windows 10 version 1809 and later, mapped to `Software\Policies\Microsoft\Windows\System\AllowCrossDeviceClipboard`; value `0` means clipboard content cannot be shared to other devices and the change takes effect immediately. See [Policy CSP - Privacy: AllowCrossDeviceClipboard](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-privacy#allowcrossdeviceclipboard).
- Windows 11 Pro build `26200` is beyond both policies' minimum supported build `17763`; Microsoft's Windows 11 25H2 material identifies build family `26200`. The legacy registry `ProductName=Windows 10 Pro` is not itself a contradiction with a separately observed Windows 11 identity, but the contract must revalidate both distinct sources exactly.

These correct semantics do not close the mutation-scope, counter, and action-time identity defects below.

## Findings

### F1 — HIGH: the block can perform an uncounted third registry mutation

**Evidence:** `task-20-windows-clipboard-policy-brief.md:172-176` conditionally calls:

```powershell
if (-not (Test-Path -LiteralPath $policyPath)) {
    $null = New-Item -Path $policyPath -Force -ErrorAction Stop
}
```

The brief's immutable scope permits exactly two DWORD-value writes and explicitly excludes every other registry key/value mutation (`task-20-windows-clipboard-policy-brief.md:19-25`). Creating `HKLM:\SOFTWARE\Policies\Microsoft\Windows\System` is a registry-key mutation, is not one of the two DWORD writes, has no attempted/fulfilled counter, and is not read back as a key-creation postcondition. The pinned facts establish that the two values are absent; they do not establish that the parent key exists (`task-20-windows-clipboard-policy-brief.md:32-44`). Therefore the executable block can exceed its stated authority and its exact mutation count.

**Required fix:** remove the `New-Item` branch. Before either value write, require the exact policy key already exists; if absent, emit a fixed safe precondition failure and stop with zero writes. If key creation is genuinely required, it needs a separately explicit mutation scope, counter, original-state pin, readback, failure disposition, and review; it cannot be hidden inside an “exactly two DWORD writes” contract.

### F2 — HIGH: attempted counters are assigned optimistically before individual operations

**Evidence:** the script sets `$writeAttempted = 2` before the first `New-ItemProperty` (`task-20-windows-clipboard-policy-brief.md:177-182`) and `$readbackAttempted = 2` before the first readback (`task-20-windows-clipboard-policy-brief.md:183-188`). There are zero `$writeAttempted++` and zero `$readbackAttempted++` operations in executable code.

If the first property write rejects before fulfillment, the terminal failure tuple reports `WRITES_ATTEMPTED=2` although only one write call was reached. The same false count occurs if the first readback rejects. This destroys the exact partial-write/readback audit that the fail-closed no-retry contract makes load-bearing. It can no longer distinguish first-call failure from second-call failure using its own redacted evidence.

**Required fix:** increment each attempted counter immediately before its corresponding individual call, then increment fulfilled only after that call returns. Apply the same pattern separately to both writes and both readbacks. Do not preassign maxima. Retain the no-retry/no-repair behavior and classify any `2/1`, `1/0`, or other non-exact tuple as `FAIL / NOT PROVEN` without rollback.

### F3 — IMPORTANT: the action-time block does not revalidate the pinned CIM Windows identity

**Evidence:** the starting-state table distinguishes “Operating system: Windows 11 Pro” from registry `ProductName: Windows 10 Pro` (`task-20-windows-clipboard-policy-brief.md:32-40`). The block checks `[Environment]::OSVersion.Version` and registry `CurrentVersion` fields (`task-20-windows-clipboard-policy-brief.md:151-160`) but contains zero `Get-CimInstance` calls and never checks the separately pinned CIM caption/identity.

The result can therefore report `PRECONDITIONS=PASS` without proving the exact live fact that motivated the explicit CIM-versus-registry distinction. Edition/build applicability is security-relevant because the policy contract claims exact host/edition/build drift checks.

**Required fix:** pin the exact raw CIM fields from the prior read-only observation—not a normalized paraphrase—and re-read them before any mutation. At minimum, require the exact `Win32_OperatingSystem` caption, version, build number, and OS architecture to match their pinned values while separately retaining the legacy registry `ProductName`, `EditionID`, `DisplayVersion`, build, and UBR checks. Emit no machine identifier. If the exact original CIM strings were not preserved, reacquire them in a separate read-only preparation step and revise/re-review the brief before any write authority.

## Other required dimensions

- **Elevation and PowerShell 7:** the block correctly checks Administrator-role membership and requires Core PowerShell major version 7 or later before mutation (`task-20-windows-clipboard-policy-brief.md:137-149`). The procedural boundary correctly requires the user to open and operate the Administrator PowerShell 7 window manually; Codex, Computer Use, terminal automation, UAC automation, scheduled tasks, services, remote shells, and alternate interfaces remain forbidden.
- **Partial-write disposition:** the catch path stops with exit 1, does not repair or retry, and emits no exception detail. The rollback section correctly states original values `ABSENT / ABSENT` as facts only, gives no removal/key-deletion/HKCU authority, and requires a separately reviewed rollback contract. F2 must still be fixed so the partial state is evidenced accurately.
- **Safe output:** output contains fixed labels, small counters, and the intended safe zero values only. No exception text, clipboard content, username, machine identifier, credential, or routing data is emitted.
- **Post-PASS proof:** the brief correctly limits live PASS to contemporaneous DWORD `0/0` readback and requires a fresh, same-build, read-only `DWord 0/0` proof before any later credential creation, copy, paste, transmission, or secure-console gate. It correctly states that clearing the current clipboard does not prove history erasure (`task-20-windows-clipboard-policy-brief.md:253-261`).
- **No rollback or authority expansion:** the document and future artifact paths set `authorizes_live_execution=false`; static review, a later live result, and a later classification do not grant retry, rollback, terminal, credential, Cloudflare, or routing authority.

## Parser, cardinality, redaction, and repository evidence

- The sole PowerShell fence parses with zero errors under `System.Management.Automation.Language.Parser.ParseInput`; the block was not invoked.
- Executable cardinality is two `New-ItemProperty` calls, one additional conditional `New-Item` key-creation call, zero `Remove-Item`/`Remove-ItemProperty`, zero `Set-Clipboard`, zero process spawn, zero remoting, zero scheduled-task/service operation, zero browser/credential/Cloudflare/VM/proxy/routing operation, zero attempted-write increments, zero attempted-readback increments, and zero CIM calls.
- Reviewed HEAD is exactly `1c45e8e5deb19e2f1bbd5ef6dbabfbf532424a32`; its parent is exactly `3f871b2d583ea1b04673ecbe7ca3e2362a9bbead`.
- The commit changes exactly one path: `.superpowers/sdd/2026-08-31-omniroute-secure-console-transfer/task-20-windows-clipboard-policy-brief.md`.
- Before creating this assigned untracked review, Git index count was `0` and the preserved dirty source baseline count was exactly `12`.
- The committed brief is `13146` bytes / SHA-256 `24A297FA85C1DA476B72607A35CFF0DB747164A60FFBC6D9CE3758AB3E1FF808`, UTF-8 without BOM and LF-only (`283` LF bytes, zero CR bytes).
- The direct-byte package exactly matches its supplied `14161`-byte SHA-256 pin.

## Final disposition

**FAIL / REVISE BEFORE EXECUTION.** Fix the unauthorized conditional policy-key creation, make attempted counters reflect each individual operation, and add exact CIM-versus-registry action-time identity proof. Then produce a new one-commit direct-byte package for fresh independent review. No current or future write, repair, rollback, retry, elevation, terminal, UAC, clipboard, credential, or routing action is authorized by this review.  
`authorizes_live_execution=false`
