# Task 20 Windows clipboard policy fix round 1 — independent Sol High static review

Review timestamp: `20260901 041513` (Asia/Bangkok)  
Fixed brief commit: `70c82f67a02a0c394416da2818c88bc22da13e58`  
Fix base / initial FAIL-review commit: `edd80f8752ade996a5cf68cff64e048b66f76027`  
Original brief commit: `1c45e8e5deb19e2f1bbd5ef6dbabfbf532424a32`  
Direct-byte fix package: `10365` bytes / SHA-256 `EE9998F77F129F761F03926309F088D06AB3A6AB1C7F3937108C96DCF603181D`  
Scope: static fix-delta, committed-byte, parser, cardinality, and native-policy review only. No registry, policy, elevation, UAC, terminal, clipboard, browser, credential, process, service, remoting, VM, proxy, or routing action was performed.  
`authorizes_live_execution=false`

## Verdict

- Fix-round specification/security verdict: **PASS**.
- Quality verdict: **PASS**.
- Prior findings F1, F2, and F3: **ADDRESSED**.
- New blocking, HIGH, or IMPORTANT findings: **0**.
- This static PASS authorizes no execution. A later user-owned elevated run still requires separate exact authority and action-time pin verification.

## Prior-finding disposition

### F1 — unauthorized conditional policy-key creation: ADDRESSED

- The bare `New-Item` key-creation branch is removed. Executable code contains zero bare `New-Item` calls.
- The fixed starting-state table now pins that `HKLM:\SOFTWARE\Policies\Microsoft\Windows\System` exists (`task-20-windows-clipboard-policy-brief.md:40-49`).
- Before either policy-value write, the block calls `Test-Path` for that exact key and throws fixed safe label `PRECONDITION_POLICY_KEY_ABSENT` if it is missing (`task-20-windows-clipboard-policy-brief.md:169-172`). Thus missing-key state fails before any write and cannot silently expand scope.
- The only mutation calls remaining are exactly two `New-ItemProperty` calls, targeting only `AllowClipboardHistory` and `AllowCrossDeviceClipboard`, each with `PropertyType DWord`, value `0`, `-Force`, and terminating error behavior (`task-20-windows-clipboard-policy-brief.md:185-192`).

Classification: **fully addressed**. The executable mutation surface is now exactly the two reviewed DWORD-zero value writes.

### F2 — optimistic attempted counters: ADDRESSED

- `$writeAttempted++` appears exactly twice and each increment is immediately followed by its corresponding individual `New-ItemProperty` call; `$writeFulfilled++` follows only after that call returns (`task-20-windows-clipboard-policy-brief.md:185-192`).
- `$readbackAttempted++` appears exactly twice and each increment is immediately followed by its corresponding individual `Get-RegistryValueState` call; `$readbackFulfilled++` follows only after that call returns (`task-20-windows-clipboard-policy-brief.md:194-201`).
- The fixed prose explicitly classifies `1/0`, `2/1`, and every other partial tuple as unrepaired `FAIL / NOT PROVEN`; no retry or rollback is inferred (`task-20-windows-clipboard-policy-brief.md:245-256`).

Classification: **fully addressed**. First-call and second-call write/readback failure are now distinguishable in the redacted terminal counters without adding a recovery path.

### F3 — missing CIM-versus-registry identity proof: ADDRESSED

- The starting-state table now pins exact CIM fields independently from the legacy registry fields: caption `Microsoft Windows 11 Pro`, version `10.0.26200`, build number `26200`, and architecture `64-bit`; registry `ProductName` remains distinctly pinned as `Windows 10 Pro` (`task-20-windows-clipboard-policy-brief.md:36-49`).
- Before mutation, the block makes exactly one read-only `Get-CimInstance -ClassName Win32_OperatingSystem` call requesting only those four properties with terminating error behavior (`task-20-windows-clipboard-policy-brief.md:159`).
- It compares all four CIM values exactly, while separately retaining the environment-version, runtime x64, registry `ProductName`, `EditionID`, `DisplayVersion`, build, and UBR comparisons (`task-20-windows-clipboard-policy-brief.md:160-167`). Any mismatch throws fixed `PRECONDITION_OS_DRIFT` before the policy-key or value checks and before writes.

Classification: **fully addressed**. The Windows 11 CIM identity and legacy registry `ProductName` are independently pinned and fail closed at action time.

## Native policy semantics and supported host

- Microsoft documents `AllowClipboardHistory` as a device policy supported on Pro from Windows 10 version 1809 onward, mapped to `Software\Policies\Microsoft\Windows\System\AllowClipboardHistory`; value `0` means clipboard history is not allowed and the policy takes effect immediately. See [Policy CSP - Experience](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-experience#allowclipboardhistory).
- Microsoft documents `AllowCrossDeviceClipboard` as a device policy supported on Pro from Windows 10 version 1809 onward, mapped to `Software\Policies\Microsoft\Windows\System\AllowCrossDeviceClipboard`; value `0` prevents cross-device clipboard sharing and the policy takes effect immediately. See [Policy CSP - Privacy](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-privacy#allowcrossdeviceclipboard).
- The pinned Windows 11 Pro build `26200` is within both support envelopes. The fixed action-time checks preserve edition/build/architecture exactness rather than relying solely on the legacy `ProductName` string.

## Exact write/readback and failure contract

- Precondition order remains fail-closed: elevation, Core PowerShell 7+, runtime x64, environment/registry/CIM identity, existing policy key, both policy values absent, and HKCU history preference exactly DWORD `1` must all pass before the first mutation.
- The two value writes are serial and terminating. A failure after zero or one fulfillment reaches the common catch, emits actual counters, returns `FAIL_STOP_NO_RETRY`, and exits 1. It performs no repair, removal, second attempt, or fallback.
- Readback is serial and exact. Success requires both values present, kind exactly `DWord`, value exactly `0`; then and only then may the block emit write/readback `2/2`, both safe zero labels, terminal `EXACT_CLIPBOARD_POLICIES_DISABLED`, and exit 0.
- The original policy values remain pinned `ABSENT / ABSENT` as facts only. There are zero `Remove-Item` or `Remove-ItemProperty` calls; this contract grants no rollback, key deletion, HKCU mutation, or sibling-value mutation.
- The manual boundary is unchanged: the user must personally open Administrator PowerShell 7 and approve UAC, then paste/run the exact block once. Codex, Computer Use, terminal automation, UAC automation, scheduled tasks, services, remoting, Settings, Group Policy Editor, Registry Editor, retries, and alternate commands remain forbidden.
- Safe output remains limited to fixed labels, small counters, and the two intended zero values. Exception text, registry data beyond those safe values, machine/user identifiers, clipboard content, credentials, Cloudflare data, and routing data are not emitted.
- Even a later classified PASS proves only contemporaneous exact DWORD `0/0` readback. The contract correctly requires a fresh same-build read-only proof before any later credential creation, native copy, masked paste, sensitive transmission, or secure-console gate; current-clipboard clearing is not history erasure.

## Parser, cardinality, and prohibited operations

- The sole PowerShell fence parses with zero errors under `System.Management.Automation.Language.Parser.ParseInput`; it was not invoked.
- Exact executable cardinality: two `New-ItemProperty` calls; two DWORD-zero write shapes; two `$writeAttempted++`; two `$readbackAttempted++`; one read-only `Get-CimInstance Win32_OperatingSystem`; four exact CIM comparisons; one exact missing-policy-key fail-closed precondition; zero bare `New-Item`; zero `Remove-Item`/`Remove-ItemProperty`.
- Each of the four attempted increments is immediately adjacent to its corresponding individual operation, with no intervening command.
- Executable code contains zero `Set-Clipboard`, browser, credential, Cloudflare, VM, proxy, routing, process-spawn, remoting, scheduled-task, service, UAC-automation, retry, or rollback operations.
- No new contradiction or authority expansion was introduced by the fix delta.

## Integrity and repository boundary

- Reviewed HEAD is exactly `70c82f67a02a0c394416da2818c88bc22da13e58`; its parent is exactly `edd80f8752ade996a5cf68cff64e048b66f76027`.
- The fix commit changes exactly one path: `.superpowers/sdd/2026-08-31-omniroute-secure-console-transfer/task-20-windows-clipboard-policy-brief.md`.
- The initial FAIL review remains unchanged at `10111` bytes / SHA-256 `DACE74BC7E62916AB0F7F6BB9C610E3ACE874F955082525067355A0EB617165D`.
- The fixed brief is `14584` bytes / SHA-256 `593C2290A946FED60DBB737D43033516CDA9C77E940211A4BB66BB56ECD56249`, UTF-8 without BOM and LF-only (`310` LF bytes, zero CR bytes).
- Before creating this assigned untracked fix-round review, Git index count was `0` and the preserved dirty source baseline count was exactly `12`.
- The direct-byte package exactly matches its supplied SHA-256 pin.

## Final disposition

**PASS — zero blocking, HIGH, or IMPORTANT findings.** Fix round 1 removes the out-of-scope key creation, makes each operation's attempted counter truthful, and adds exact CIM identity revalidation while preserving the exact two-value mutation, serial readback, fail-closed no-retry/no-rollback semantics, safe output, manual elevation boundary, fresh post-PASS proof requirement, and artifact limits. This review authorizes no live execution.  
`authorizes_live_execution=false`
