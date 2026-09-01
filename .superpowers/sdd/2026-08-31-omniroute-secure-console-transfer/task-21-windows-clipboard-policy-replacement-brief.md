# Task 21 Windows clipboard policy replacement brief

`authorizes_live_execution=false`

Status: fresh static replacement candidate only. Task 21 is not a retry,
reuse, resumption, continuation, or relaxation of Task 20. This document does
not perform or authorize a registry, elevation, UAC, clipboard, browser,
credential, Cloudflare, process, remoting, or routing action.

## Authority, lineage, and owned artifacts

- Current static base and Task 20 classification commit:
  `09e18549188e9032f4e78076efefd6e9331bbd26`.
- Spent Task 20 fixed brief commit:
  `70c82f67a02a0c394416da2818c88bc22da13e58`.
- Task 20 classification: `FAIL / NOT PROVEN`; writes/readbacks
  `0 / 0`, both target values freshly proven `ABSENT`, policy key proven to
  exist, OS identity proven unchanged, gate `CONSUMED / SPENT`.
- Task 20's proven wrong-host fact: the attempted block ran in Windows
  PowerShell, while Task 20 required PowerShell 7/Core. No Task 20 action may
  be rerun or continued.
- Future Task 21 live report:
  `.superpowers/sdd/2026-08-31-omniroute-secure-console-transfer/task-21-windows-clipboard-policy-replacement-live-report.md`.
- Future Task 21 independent classification:
  `.superpowers/sdd/2026-08-31-omniroute-secure-console-transfer/task-21-windows-clipboard-policy-replacement-classification.md`.

Only a fresh independent Sol High direct-byte `PASS` plus fresh action-time
pins may make Task 21 eligible for one user-performed run. Task 21 has exactly
one attempt. A rejected call, nonzero exit, partial write, missing/duplicate or
extra output, malformed result, interruption, or observation uncertainty spends
Task 21 and stops. There is no retry, fallback, repair, rollback, continuation,
alternate shell, alternate interface, or verdict relaxation.

## Exact mutation scope

If independently approved, the sole mutation scope is exactly two serial
DWORD writes below the already-existing machine policy key
`HKLM:\SOFTWARE\Policies\Microsoft\Windows\System`:

1. `AllowClipboardHistory=0`;
2. `AllowCrossDeviceClipboard=0`.

No key creation, key deletion, value deletion, rollback, HKCU write, sibling
value write, Settings-app action, Local Group Policy Editor action, Registry
Editor action, credential, browser, Cloudflare, VM, proxy, provider, routing,
process spawn, remoting, service, scheduled task, UAC automation, or Computer
Use action is authorized.

## Task 21 fresh action-time state

The block must freshly prove every row before the first write. The Task 20
classification proves only the cited post-action facts; Task 21 does not infer
that a precondition remains current.

| Source/field | Exact required state |
| --- | --- |
| Shell family | Windows PowerShell 5.1 Desktop; not PowerShell 7/Core |
| `$PSVersionTable.PSEdition` | exact `Desktop` |
| `$PSVersionTable.PSVersion` | exact major/minor `5.1` |
| Process bitness | 64-bit |
| Administrator token | elevated / Administrator role `True` |
| CIM `Caption` | `Microsoft Windows 11 Pro` |
| CIM `Version` | `10.0.26200` |
| CIM `BuildNumber` | `26200` |
| CIM `OSArchitecture` | `64-bit` |
| Registry `ProductName` | `Windows 10 Pro` |
| Registry `EditionID` | `Professional` |
| Registry `DisplayVersion` | `25H2` |
| Registry `CurrentBuildNumber` | `26200` |
| Registry `UBR` | `9278` |
| `[Environment]::OSVersion` | major/minor/build `10 / 0 / 26200` |
| Policy key exists | exact `True` |
| `AllowClipboardHistory` | exact `ABSENT` |
| `AllowCrossDeviceClipboard` | exact `ABSENT` |
| HKCU `EnableClipboardHistory` | exact kind/value `DWord / 1` |

Major/minor `5.1` is the exact reviewed Windows PowerShell product version for
this contract. A Core edition, any other major or minor, a 32-bit process, or
an unelevated token fails before any write. The block emits no username,
machine name, machine identifier, registry content other than the intended safe
zero result labels, or exception text.

## Manual execution boundary

Neither Codex nor Computer Use may open the shell, click UAC, paste/type the
block, or otherwise automate the terminal. After independent review and fresh
eligibility validation, the user must perform these steps personally:

1. Open the Start menu and locate **Windows PowerShell** (not PowerShell 7 and
   not `pwsh`).
2. Right-click **Windows PowerShell**, choose **Run as administrator**, and
   respond to UAC manually.
3. In that one elevated 64-bit Windows PowerShell 5.1 Desktop window, copy the
   entire block below from its first `$ErrorActionPreference` line through its
   final closing brace, paste it, and run it as **one block exactly once**.
4. Do not edit, split, supplement, rerun, or translate the block. If the window
   exits nonzero, a terminal label is absent, output is uncertain, or the
   fixed failure terminal appears, stop. Do not run Task 20 or Task 21 again.

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
    $principal = New-Object Security.Principal.WindowsPrincipal($identity)
    if (-not $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
        throw 'PRECONDITION_NOT_ELEVATED'
    }
    if ($PSVersionTable.PSEdition -ne 'Desktop' -or
        $PSVersionTable.PSVersion.Major -ne 5 -or
        $PSVersionTable.PSVersion.Minor -ne 1) {
        throw 'PRECONDITION_NOT_WINDOWS_POWERSHELL_5_1_DESKTOP'
    }
    if (-not [Environment]::Is64BitOperatingSystem -or -not [Environment]::Is64BitProcess) {
        throw 'PRECONDITION_NOT_64_BIT'
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

    [Console]::Out.WriteLine('TASK21_PRECONDITIONS=PASS')
    [Console]::Out.WriteLine('TASK20_GATE=SPENT_NOT_RETRIED')
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

    if ($writeAttempted -ne 2 -or $writeFulfilled -ne 2 -or
        $readbackAttempted -ne 2 -or $readbackFulfilled -ne 2 -or
        -not $historyAfter.Present -or $historyAfter.Kind -ne 'DWord' -or
        [int]$historyAfter.Value -ne 0 -or
        -not $crossDeviceAfter.Present -or $crossDeviceAfter.Kind -ne 'DWord' -or
        [int]$crossDeviceAfter.Value -ne 0) {
        throw 'POSTCONDITION_READBACK_OR_COUNTER_FAILED'
    }

    [Console]::Out.WriteLine("WRITES_ATTEMPTED=$writeAttempted")
    [Console]::Out.WriteLine("WRITES_FULFILLED=$writeFulfilled")
    [Console]::Out.WriteLine("READBACKS_ATTEMPTED=$readbackAttempted")
    [Console]::Out.WriteLine("READBACKS_FULFILLED=$readbackFulfilled")
    [Console]::Out.WriteLine('ALLOW_CLIPBOARD_HISTORY=0')
    [Console]::Out.WriteLine('ALLOW_CROSS_DEVICE_CLIPBOARD=0')
    [Console]::Out.WriteLine('RESULT=EXACT_TASK21_CLIPBOARD_POLICIES_DISABLED')
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

## Exact success, failure, and counter contract

Success requires process exit `0` and exactly one of every fixed success label.
The sole terminal must be
`RESULT=EXACT_TASK21_CLIPBOARD_POLICIES_DISABLED`. Writes and readbacks must
each be exactly `2 / 2`; both readback kinds/values must be `DWord / 0`; the
Task 20 terminal must state only `SPENT_NOT_RETRIED`.

Each attempted counter increments immediately before its one corresponding
call. Each fulfilled counter increments only after that call returns. The
operations are serial in the displayed order: first history write, second
cross-device write, first history readback, second cross-device readback. No
second operation begins if the preceding call throws.

Every failure or uncertainty emits fixed terminal
`RESULT=FAIL_STOP_NO_RETRY`, the actual counters reached at that boundary, and
exit `1`. No exception text is emitted. Any `1 / 0`, `2 / 1`, missing label,
duplicate label, extra label, ambiguous exit, partial write, partial readback,
or output uncertainty is `FAIL / NOT PROVEN`; it spends Task 21 and authorizes
no repair or rollback.

## Post-success proof and independent classification

A Task 21 success terminal proves only the two serial calls and their immediate
same-process readbacks. Before any credential creation, secret copy/paste,
sensitive transmission, Cloudflare action, or secure-console gate, a fresh
read-only proof must show on the same pinned host:

- the exact policy key still exists;
- both target values exist, are `DWord`, and equal `0 / 0`;
- the CIM and registry OS identity fields still match; and
- no uncertainty occurred.

Current-clipboard clearing does not prove clipboard-history erasure. The future
live report is candidate evidence only. A separate independent Sol High
classification must issue `PASS` before any downstream contract may rely on
Task 21. Neither report nor classification authorizes a retry or unrelated
action, and both must set `authorizes_live_execution=false`.

## Rollback and residual boundary

Task 20's post-action target state was `ABSENT / ABSENT` with zero writes.
Task 21 includes no rollback. If one or both Task 21 writes fulfill and a later
step fails, leave the observed state for independent classification. Do not
delete either value, delete the policy key, change HKCU, retry the missing
operation, or use another interface. Any rollback would require its own fresh
contract, review, action-time state, authority, and evidence.

## Static non-execution checks

Static preparation and review may only:

1. verify strict UTF-8 without BOM, LF-only bytes, and one trailing LF;
2. extract the sole `powershell` fence and parse it with
   `[System.Management.Automation.Language.Parser]::ParseInput` without
   invoking it;
3. require exact host checks: `PSEdition=Desktop`, version major/minor `5 / 1`,
   64-bit OS and process, and Administrator role;
4. require one CIM read and the exact four CIM comparisons, the exact registry
   identity comparisons, one policy-key-exists check, both target values
   absent, and HKCU `DWord / 1` before writes;
5. require exactly two `New-ItemProperty` calls, each `DWord`, value `0`, in
   exact serial name order; exactly two write-attempt/two write-fulfilled and
   two read-attempt/two read-fulfilled increments in the reviewed order;
6. require explicit exact `2 / 2` success counter comparisons and exact
   `DWord / 0` readback comparisons;
7. require zero bare `New-Item`, `Set-ItemProperty`, `Remove-Item`,
   `Remove-ItemProperty`, `Set-Clipboard`, `Get-Clipboard`, process spawn,
   remoting, UAC automation, retry, credential, browser, Cloudflare, VM,
   provider, proxy, or routing operations in executable code; and
8. require HEAD `09e18549188e9032f4e78076efefd6e9331bbd26`, empty Git
   index, preserved unrelated baseline `12`, and only this owned path added.

These checks execute no embedded code and authorize no live action.
