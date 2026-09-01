# Task 21 Windows clipboard policy replacement live report

Status: target policy state proven; exact one-shot terminal result not proven.
Task 21 is consumed and spent.

## Pins

- Task 20 failure classification commit: `09e18549188e9032f4e78076efefd6e9331bbd26`
- Task 21 brief commit: `e7482fe91932cba4d63942460a04782128f23185`
- Task 21 independent PASS review commit: `cfd78d507618f8eead3ea195f94b68c5ca09f555`
- reviewed brief: `task-21-windows-clipboard-policy-replacement-brief.md`
- reviewed static review: `task-21-windows-clipboard-policy-replacement-sol-review.md`

Fresh action-time pins immediately before the operator action matched the
reviewed contract: both target policy values were absent; the existing HKCU
history value was DWORD `1`; the exact OS identity matched; and 64-bit Windows
PowerShell Desktop `5.1.26100.9278` was available.

## Operator observation

The owner reported that the manually elevated Windows PowerShell window closed
automatically after the reviewed block was run and that no console output was
captured. This is consistent with either reviewed terminal path because the
block ends with `exit 0` on success and `exit 1` on failure. Window closure is
not execution-result evidence. The block must not be run again.

## Fresh read-only post-state

A local read-only query after the operator observation returned:

- policy key: present
- `AllowClipboardHistory`: present, kind `DWord`, value `0`
- `AllowCrossDeviceClipboard`: present, kind `DWord`, value `0`
- caption: `Microsoft Windows 11 Pro`
- version/build: `10.0.26200` / `26200`
- architecture: `64-bit`
- display version: `25H2`
- UBR: `9278`

This proves the intended machine-policy target state on the unchanged reviewed
host. The read-only query performed no mutation.

## Event-log check

Read-only checks covered `Windows PowerShell` and
`Microsoft-Windows-PowerShell/Operational` for the preceding 30 minutes. Both
logs were readable. The operational log contained a PowerShell script-block
source fragment (event ID `4104`, record ID `2673924`, time
`2026-09-01 09:47:29` local) containing the fixed failure-label source text.
Script-block source logging records code text, not the path taken or console
stdout; the fragment therefore proves neither success nor failure and cannot
recover the missing counters or terminal result.

## Evidence classification boundary

- **PROVEN:** both required machine-policy values are present as DWORD `0` on
  the unchanged host.
- **PROVEN:** Task 20 was not retried; Task 21 was the fresh replacement gate.
- **NOT PROVEN:** `TASK21_PRECONDITIONS=PASS`, all four runtime counters, process
  exit code, and the exact `RESULT=EXACT_TASK21_CLIPBOARD_POLICIES_DISABLED`
  console terminal.
- **SPENT:** Task 21 must not be retried, reused, continued, relaxed, or given a
  reconstructed success terminal.
- This report authorizes no additional registry mutation, credential action,
  browser action, provider change, or routing change.

Independent review must decide whether the proven effective policy state is
sufficient for the downstream secure-transfer prerequisite while preserving
the exact-terminal `NOT PROVEN` limitation.
