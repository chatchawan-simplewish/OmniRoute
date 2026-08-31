# Task 20 Windows clipboard policy hardening brief

`authorizes_live_execution=false`

Status: static contract only. This brief does not authorize or perform a
registry write, UAC interaction, browser action, clipboard-content access,
credential action, Cloudflare action, routing action, or later secure-console
transfer.

## Scope and pins

- Original Task 20 source/worktree base:
  `3f871b2d583ea1b04673ecbe7ca3e2362a9bbead`.
- Fix-round-1 base and FAIL-review commit:
  `edd80f8752ade996a5cf68cff64e048b66f76027`.
- Reviewed brief commit:
  `1c45e8e5deb19e2f1bbd5ef6dbabfbf532424a32`.
- FAIL review direct bytes: `10111` bytes, SHA-256
  `DACE74BC7E62916AB0F7F6BB9C610E3ACE874F955082525067355A0EB617165D`.
- Owned future live report:
  `.superpowers/sdd/2026-08-31-omniroute-secure-console-transfer/task-20-windows-clipboard-policy-live-report.md`.
- Owned future independent classification:
  `.superpowers/sdd/2026-08-31-omniroute-secure-console-transfer/task-20-windows-clipboard-policy-classification.md`.
- Mutation scope, if separately reviewed and authorized: exactly two DWORD
  values below the one machine policy key
  `HKLM:\SOFTWARE\Policies\Microsoft\Windows\System`:
  `AllowClipboardHistory=0` and `AllowCrossDeviceClipboard=0`.
- No other registry key/value, Windows setting, process, browser, clipboard,
  credential, permission, Cloudflare object, VM, proxy, or route is in scope.
- One attempt only. A failed, interrupted, malformed, or tool-uncertain run is
  spent and stops for independent classification. There is no retry, repair,
  fallback, alternate command, Settings-app path, Group Policy Editor path,
  registry-editor path, or verdict relaxation.

## Pinned read-only starting state

The prior live read-only observation is pinned as follows; this brief does not
repeat it:

| Fact | Pinned state |
| --- | --- |
| Operating system | Windows 11 Pro |
| CIM `Caption` | `Microsoft Windows 11 Pro` |
| CIM `Version` | `10.0.26200` |
| CIM `BuildNumber` | `26200` |
| CIM `OSArchitecture` | `64-bit` |
| Registry `ProductName` | `Windows 10 Pro` |
| Version/build | `10.0.26200` / build `26200` |
| DisplayVersion | `25H2` |
| UBR | `9278` |
| Architecture | `x64` |
| `HKLM ...\Windows\System` policy key exists | `True` |
| `HKLM ...\System\AllowClipboardHistory` | `ABSENT` |
| `HKLM ...\System\AllowCrossDeviceClipboard` | `ABSENT` |
| `HKCU ...\Clipboard\EnableClipboardHistory` | DWORD `1` |
| Current Codex process | non-administrator / not elevated |

The non-elevated Codex process must not attempt the write, launch an elevated
terminal, interact with UAC, or automate PowerShell. The eventual user-owned
run occurs only in a separately opened **Administrator: PowerShell 7** window.

## Microsoft policy semantics

Microsoft Learn documents `AllowClipboardHistory` as a device policy supported
on Windows Pro from Windows 10 version 1809 onward. DWORD `0` means clipboard
history is not allowed; the policy maps to
`Software\Policies\Microsoft\Windows\System\AllowClipboardHistory`; and the
change takes effect immediately. See [Policy CSP - Experience:
AllowClipboardHistory](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-experience#allowclipboardhistory).

Microsoft Learn likewise documents `AllowCrossDeviceClipboard` as a device
policy supported on Windows Pro from Windows 10 version 1809 onward. DWORD `0`
prevents clipboard contents from being shared to other devices; the policy
maps to
`Software\Policies\Microsoft\Windows\System\AllowCrossDeviceClipboard`; and
the change takes effect immediately. See [Policy CSP - Privacy:
AllowCrossDeviceClipboard](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-privacy#allowcrossdeviceclipboard).

Windows 11 Pro build `26200` is therefore inside both documented edition/build
support envelopes. The live block still fails closed unless every pinned host,
edition, build, user-setting, policy-absence, architecture, PowerShell, and
elevation precondition matches at action time.

## Mandatory review and action boundary

Preparation and independent review of this brief are credential-free. They do
not authorize the block. A fresh independent Sol High direct-byte `PASS` and
action-time pin verification are required before the user manually runs it.

The user must make the one elevated run personally. Computer Use, browser
automation, Codex terminal automation, scheduled tasks, services, remote
shells, and UAC automation are forbidden. The user must not paste or enter a
credential into this block; it contains and accepts no credential.

## Exact user terminal instructions

After independent review and explicit action-time authority:

1. Manually open **PowerShell 7** by right-clicking it and choosing **Run as
   administrator**. Approve UAC yourself. Do not ask Computer Use or Codex to
   click or type in that window.
2. Confirm the title bar identifies an Administrator PowerShell window.
3. Copy the entire block below, from the first `$ErrorActionPreference` line
   through the final closing brace, paste it into that Administrator
   PowerShell 7 window, and run it as **one block exactly once**.
4. Do not edit, split, rerun, or supplement the block. Record only its safe
   fixed output labels in the future live report. On any nonzero exit, missing
   terminal label, or output uncertainty, stop.

```powershell
$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
$policyPath = 'HKLM:\SOFTWARE\Policies\Microsoft\Windows\System'
$userClipboardPath = 'HKCU:\Software\Microsoft\Clipboard'
$currentVersionPath = 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion'
$historyName = 'AllowClipboardHistory'
$crossDeviceName = 'AllowCrossDeviceClipboard'
$writeAttempted = 0
$writeFulfilled = 0
$readbackAttempted = 0
$readbackFulfilled = 0

function Get-RegistryValueState {
    param(
        [Parameter(Mandatory)][string]$Path,
        [Parameter(Mandatory)][string]$Name
    )
    if (-not (Test-Path -LiteralPath $Path)) {
        return [pscustomobject]@{ Present = $false; Kind = 'ABSENT'; Value = $null }
    }
    $key = Get-Item -LiteralPath $Path -ErrorAction Stop
    try {
        if ($key.GetValueNames() -notcontains $Name) {
            return [pscustomobject]@{ Present = $false; Kind = 'ABSENT'; Value = $null }
        }
        return [pscustomobject]@{
            Present = $true
            Kind = [string]$key.GetValueKind($Name)
            Value = $key.GetValue($Name, $null, [Microsoft.Win32.RegistryValueOptions]::DoNotExpandEnvironmentNames)
        }
    }
    finally {
        $key.Close()
        $key.Dispose()
    }
}

try {
    $identity = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = [Security.Principal.WindowsPrincipal]::new($identity)
    if (-not $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
        throw 'PRECONDITION_NOT_ELEVATED'
    }
    if ($PSVersionTable.PSEdition -ne 'Core' -or $PSVersionTable.PSVersion.Major -lt 7) {
        throw 'PRECONDITION_NOT_POWERSHELL_7'
    }
    if ([Runtime.InteropServices.RuntimeInformation]::OSArchitecture -ne
        [Runtime.InteropServices.Architecture]::X64) {
        throw 'PRECONDITION_ARCHITECTURE_DRIFT'
    }

    $osVersion = [Environment]::OSVersion.Version
    $os = Get-ItemProperty -LiteralPath $currentVersionPath -ErrorAction Stop
    $cimOs = Get-CimInstance -ClassName Win32_OperatingSystem -Property Caption,Version,BuildNumber,OSArchitecture -ErrorAction Stop
    if ($osVersion.Major -ne 10 -or $osVersion.Minor -ne 0 -or
        $osVersion.Build -ne 26200 -or
        [string]$cimOs.Caption -ne 'Microsoft Windows 11 Pro' -or
        [string]$cimOs.Version -ne '10.0.26200' -or
        [string]$cimOs.BuildNumber -ne '26200' -or
        [string]$cimOs.OSArchitecture -ne '64-bit' -or
        [string]$os.ProductName -ne 'Windows 10 Pro' -or
        [string]$os.EditionID -ne 'Professional' -or
        [string]$os.DisplayVersion -ne '25H2' -or
        [int]$os.CurrentBuildNumber -ne 26200 -or [int]$os.UBR -ne 9278) {
        throw 'PRECONDITION_OS_DRIFT'
    }

    if (-not (Test-Path -LiteralPath $policyPath)) {
        throw 'PRECONDITION_POLICY_KEY_ABSENT'
    }
    $historyBefore = Get-RegistryValueState -Path $policyPath -Name $historyName
    $crossDeviceBefore = Get-RegistryValueState -Path $policyPath -Name $crossDeviceName
    $userHistoryBefore = Get-RegistryValueState -Path $userClipboardPath -Name 'EnableClipboardHistory'
    if ($historyBefore.Present -or $crossDeviceBefore.Present -or
        -not $userHistoryBefore.Present -or $userHistoryBefore.Kind -ne 'DWord' -or
        [int]$userHistoryBefore.Value -ne 1) {
        throw 'PRECONDITION_REGISTRY_DRIFT'
    }

    [Console]::Out.WriteLine('PRECONDITIONS=PASS')
    [Console]::Out.WriteLine('ORIGINAL_POLICY_STATE=ABSENT_ABSENT')

    $writeAttempted++
    $null = New-ItemProperty -LiteralPath $policyPath -Name $historyName -PropertyType DWord -Value 0 -Force -ErrorAction Stop
    $writeFulfilled++
    $writeAttempted++
    $null = New-ItemProperty -LiteralPath $policyPath -Name $crossDeviceName -PropertyType DWord -Value 0 -Force -ErrorAction Stop
    $writeFulfilled++

    $readbackAttempted++
    $historyAfter = Get-RegistryValueState -Path $policyPath -Name $historyName
    $readbackFulfilled++
    $readbackAttempted++
    $crossDeviceAfter = Get-RegistryValueState -Path $policyPath -Name $crossDeviceName
    $readbackFulfilled++
    if (-not $historyAfter.Present -or $historyAfter.Kind -ne 'DWord' -or
        [int]$historyAfter.Value -ne 0 -or
        -not $crossDeviceAfter.Present -or $crossDeviceAfter.Kind -ne 'DWord' -or
        [int]$crossDeviceAfter.Value -ne 0) {
        throw 'POSTCONDITION_READBACK_FAILED'
    }

    [Console]::Out.WriteLine("WRITES_ATTEMPTED=$writeAttempted")
    [Console]::Out.WriteLine("WRITES_FULFILLED=$writeFulfilled")
    [Console]::Out.WriteLine("READBACKS_ATTEMPTED=$readbackAttempted")
    [Console]::Out.WriteLine("READBACKS_FULFILLED=$readbackFulfilled")
    [Console]::Out.WriteLine('ALLOW_CLIPBOARD_HISTORY=0')
    [Console]::Out.WriteLine('ALLOW_CROSS_DEVICE_CLIPBOARD=0')
    [Console]::Out.WriteLine('RESULT=EXACT_CLIPBOARD_POLICIES_DISABLED')
    exit 0
}
catch {
    [Console]::Out.WriteLine("WRITES_ATTEMPTED=$writeAttempted")
    [Console]::Out.WriteLine("WRITES_FULFILLED=$writeFulfilled")
    [Console]::Out.WriteLine("READBACKS_ATTEMPTED=$readbackAttempted")
    [Console]::Out.WriteLine("READBACKS_FULFILLED=$readbackFulfilled")
    [Console]::Out.WriteLine('RESULT=FAIL_STOP_NO_RETRY')
    exit 1
}
finally {
    $identity = $null
    $principal = $null
    $osVersion = $null
    $os = $null
    $cimOs = $null
    $historyBefore = $null
    $crossDeviceBefore = $null
    $userHistoryBefore = $null
    $historyAfter = $null
    $crossDeviceAfter = $null
}
```

## Exact success and failure contract

Success requires one process exit `0`, exactly one each of the fixed
`PRECONDITIONS`, original-state, two write-counter, two readback-counter, two
policy-value, and terminal result labels; counters must be writes `2 / 2` and
readbacks `2 / 2`; values must be DWORD `0 / 0`; and the terminal result must
be `EXACT_CLIPBOARD_POLICIES_DISABLED`.

Any other exit, counter, label, type, value, missing output, duplicated output,
extra output, partial write, parser uncertainty, or terminal/tool uncertainty
is `FAIL / NOT PROVEN`. It authorizes no retry. The attempted counter increments
immediately before each individual write or readback, and its paired fulfilled
counter increments only after that call returns. In particular, `1 / 0`,
`2 / 1`, or any other partial tuple is not repaired in the same gate and
rollback is not inferred.

The output contains only fixed safe labels and small counters. The catch block
does not emit exception text, registry content beyond the two intended safe
zero values, usernames, machine identifiers, clipboard content, credentials,
or routing data.

## Rollback facts, not authority

The pinned original machine-policy values are `ABSENT / ABSENT`. A future
rollback contract, if separately designed, independently reviewed, and
explicitly authorized, would have to target only those two exact values and
prove their restored absence without changing any sibling value. This brief
does **not** authorize removing either value, deleting the policy key, changing
the HKCU preference, or performing any rollback. Failure after one fulfilled
write therefore stops for classification rather than improvising cleanup.

## Credential-gate prerequisite after Task 20

Even a classified Task 20 `PASS` proves only the two machine-policy DWORDs were
read back as zero during this one run. Before any later credential creation,
copy, masked paste, sensitive transmission, or secure-console gate, a fresh
read-only action-time proof must independently show both exact values still
exist as DWORD `0 / 0` on the same pinned Windows build. Missing, enabled,
wrong-type, ambiguous, policy-drifted, or tool-uncertain state stops before the
credential action. Current-clipboard clearing does not prove history erasure.

## Static verification contract

Static preparation/review may only:

1. read the direct bytes of this brief and verify strict UTF-8, no BOM,
   LF-only, and one trailing LF;
2. extract the sole `powershell` fence and parse it with
   `[System.Management.Automation.Language.Parser]::ParseInput`, without
   invoking the block;
3. assert exact cardinality of the two `New-ItemProperty` calls and exact names,
   `DWord` types, and zero values; assert exactly two individual
   `$writeAttempted++` and two individual `$readbackAttempted++` operations,
   each immediately before its corresponding call;
4. assert exactly one read-only `Get-CimInstance Win32_OperatingSystem` call,
   all four exact CIM comparisons, exact policy-key-exists precondition, and
   zero bare `New-Item` key-creation calls;
5. assert zero `Remove-Item`, `Remove-ItemProperty`, `Set-Clipboard`, browser,
   credential, Cloudflare, VM, proxy, routing, process-spawn, UAC-automation,
   scheduled-task, service, remoting, or retry operations in executable code;
6. assert the fix base remains exact, Git index count is `0`, the unrelated dirty
   baseline remains `12`, and the only new path is this ignored brief.

These checks do not execute the embedded block and do not authorize its later
execution. After the future live result, write only the redacted report path
above, obtain an independent classification at the pinned classification path,
and stop.
