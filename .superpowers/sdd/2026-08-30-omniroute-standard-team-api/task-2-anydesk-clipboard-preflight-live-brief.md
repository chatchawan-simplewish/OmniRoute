# Task 2 AnyDesk / Chrome / Windows clipboard transport-preflight live brief

Status: prepared for fresh independent direct-byte review only; no preflight or live execution is authorized

## Authority and fixed boundary

The sole authority is the latest `Fix round 2 scoped re-review` PASS in
`task-2-secure-console-transfer-sol-review.md` at commit
`d22c0250558ac92b9b4fdc0606e2e1003899698f`. The authoritative design is
`task-2-secure-console-transfer-design.md`, `19,055` bytes, SHA-256
`39254F4AE68A9AC9F856BEB4E8C2CE0CCE771263E5496A5E23A90B6BD6C4901F`.
That PASS authorizes preparation and independent review of this brief only.

This brief is credential-free. It authorizes no process start, browser or
clipboard action, AnyDesk action, Cloudflare or OmniRoute action, VM1205
access, token creation, evidence mutation, proxy/proof/R5 action, Rulesets
action, revocation, retry, fallback, alternate bridge, or permission change.
Execution remains blocked until a fresh independent Sol High direct-byte
review explicitly passes this exact brief and exact extracted script bytes,
followed by separate action-time preflight authority in the sole owner task.

A future observed `PREFLIGHT=PASS` proves only that one fresh non-secret
challenge crossed the observed local data-page -> semantic Chrome focus ->
`Control+A` -> `Control+C` -> AnyDesk/Windows clipboard -> fixed PowerShell 7
path at that time. It cannot prove the semantics of Cloudflare's native Copy
control and authorizes no token, credential, or other live action.

## Exact script-byte contract

- Reviewed filename: `omniroute-transport-preflight.ps1`.
- The exact script bytes are the complete contents of the single fenced
  `powershell` block below, beginning with `param(` and ending with the LF after
  `exit $exitCode`; the fence markers and surrounding Markdown are excluded.
- Encoding is strict UTF-8 without BOM, LF-only, with exactly one trailing LF.
- Exact extracted byte size: `8,301`.
- Exact extracted SHA-256: `47CC3228B184D61328315D582748A7C145C98D9F4082D106E2E981F40A682F68`.
- The challenge is exactly 128 bits (`16` bytes), freshly filled at runtime by
  the .NET `RandomNumberGenerator`; no static or reused challenge is permitted.
- The script is credential-free and emits only fixed non-secret labels,
  numeric counters, its PID, and the fresh non-secret challenge.

```powershell
param(
    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string]$ExpectedTempRoot,

    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string]$ExpectedScriptPath,

    [Parameter(Mandatory)]
    [ValidatePattern('^[0-9A-F]{64}$')]
    [string]$ExpectedScriptSha256,

    [Parameter(Mandatory)]
    [ValidateRange(1, 1048576)]
    [long]$ExpectedScriptBytes,

    [ValidateRange(1, 900)]
    [int]$ControlTimeoutSeconds = 120
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$reviewedLeaf = 'omniroute-transport-preflight.ps1'
$exitCode = 1
$terminalEmitted = $false
$cleanupOk = $true
$tempRoot = $null
$scriptPath = $null
$challengeBytes = $null
$challenge = $null
$baseline = $null
$observed = $null
$postClear = $null
$controlCts = $null
$readTask = $null
$controlClock = $null
$controlLine = $null
$baselineWrites = 0
$baselineReads = 0
$comparisonReads = 0
$finalWrites = 0
$postClearReads = 0

try {
    $tempBase = [IO.Path]::GetFullPath([IO.Path]::GetTempPath()).TrimEnd([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
    $tempRoot = [IO.Path]::GetFullPath($ExpectedTempRoot).TrimEnd([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
    $scriptPath = [IO.Path]::GetFullPath($ExpectedScriptPath)
    $actualCommandPath = [IO.Path]::GetFullPath($PSCommandPath)
    $pathComparer = [StringComparer]::OrdinalIgnoreCase

    if (-not $pathComparer.Equals([IO.Path]::GetDirectoryName($tempRoot), $tempBase)) {
        throw 'TEMP_ROOT_NOT_DIRECT_CHILD'
    }
    if ([IO.Path]::GetFileName($tempRoot) -cnotmatch '^omniroute-transport-preflight-[0-9a-f]{32}$') {
        throw 'TEMP_ROOT_NAME_REJECTED'
    }
    if (-not [IO.Directory]::Exists($tempRoot)) {
        throw 'TEMP_ROOT_ABSENT'
    }
    if (-not $pathComparer.Equals([IO.Path]::GetDirectoryName($scriptPath), $tempRoot)) {
        throw 'SCRIPT_NOT_DIRECT_CHILD'
    }
    if ([IO.Path]::GetFileName($scriptPath) -cne $reviewedLeaf) {
        throw 'SCRIPT_LEAF_REJECTED'
    }
    if (-not $pathComparer.Equals($actualCommandPath, $scriptPath)) {
        throw 'COMMAND_PATH_MISMATCH'
    }
    if (-not [IO.File]::Exists($scriptPath)) {
        throw 'SCRIPT_ABSENT'
    }

    "OWNER_PID=$PID"

    $baselineWrites++
    Set-Clipboard -Value $null -ErrorAction Stop
    'BASELINE_CLEAR=PASS'

    $baselineReads++
    $baseline = Get-Clipboard -Raw -ErrorAction Stop
    if ($null -ne $baseline -and (-not ($baseline -is [string]) -or $baseline.Length -ne 0)) {
        throw 'BASELINE_NOT_EMPTY'
    }
    'BASELINE_EMPTY=PASS'
    $baseline = $null

    $challengeBytes = [byte[]]::new(16)
    [Security.Cryptography.RandomNumberGenerator]::Fill($challengeBytes)
    $challenge = [Convert]::ToHexString($challengeBytes)
    "CHALLENGE=$challenge"
    'OWNER_READY=PASS'

    $controlCts = [Threading.CancellationTokenSource]::new()
    $readTask = [Console]::In.ReadLineAsync($controlCts.Token)
    $controlClock = [Diagnostics.Stopwatch]::StartNew()
    $controlDeadline = [TimeSpan]::FromSeconds($ControlTimeoutSeconds)

    while (-not $readTask.IsCompleted -and $controlClock.Elapsed -lt $controlDeadline) {
        [Threading.Thread]::Sleep(25)
    }

    if (-not $readTask.IsCompleted) {
        $controlCts.Cancel()
        try {
            $null = $readTask.GetAwaiter().GetResult()
        } catch [OperationCanceledException] {
        }
        'PREFLIGHT=TIMEOUT'
        $terminalEmitted = $true
        $exitCode = 2
    } else {
        $controlLine = $readTask.GetAwaiter().GetResult()
        if ($null -eq $controlLine) {
            'PREFLIGHT=EOF'
            $terminalEmitted = $true
            $exitCode = 2
        } elseif ($controlLine -ceq 'COPY_DONE') {
            $comparisonReads++
            $observed = Get-Clipboard -Raw -ErrorAction Stop
            if ($observed -is [string] -and $observed -ceq $challenge) {
                'PREFLIGHT=PASS'
                $exitCode = 0
            } else {
                'PREFLIGHT=FAIL'
                $exitCode = 1
            }
            $terminalEmitted = $true
            $observed = $null
        } else {
            'PREFLIGHT=ABORTED'
            $terminalEmitted = $true
            $exitCode = 2
        }
    }
} catch {
    if (-not $terminalEmitted) {
        'PREFLIGHT=FAIL'
        $terminalEmitted = $true
    }
    $exitCode = 1
} finally {
    if ($null -ne $controlClock) {
        $controlClock.Stop()
    }
    if ($null -ne $readTask -and -not $readTask.IsCompleted) {
        $controlCts.Cancel()
        try {
            $null = $readTask.GetAwaiter().GetResult()
        } catch {
        }
    }
    if ($null -ne $controlCts) {
        $controlCts.Dispose()
    }

    try {
        $finalWrites++
        Set-Clipboard -Value $null -ErrorAction Stop
        'CLEANUP_CLIPBOARD_CLEAR=PASS'
    } catch {
        'CLEANUP_CLIPBOARD_CLEAR=FAIL'
        $cleanupOk = $false
        $exitCode = 1
    }

    try {
        $postClearReads++
        $postClear = Get-Clipboard -Raw -ErrorAction Stop
        if ($null -ne $postClear -and (-not ($postClear -is [string]) -or $postClear.Length -ne 0)) {
            throw 'POST_CLEAR_NOT_EMPTY'
        }
        'CLEANUP_CLIPBOARD_EMPTY=PASS'
    } catch {
        'CLEANUP_CLIPBOARD_EMPTY=FAIL'
        $cleanupOk = $false
        $exitCode = 1
    }

    $baseline = $null
    $observed = $null
    $postClear = $null
    $controlLine = $null
    $challenge = $null
    if ($null -ne $challengeBytes) {
        [Array]::Clear($challengeBytes, 0, $challengeBytes.Length)
    }
    $challengeBytes = $null

    $deleteGuard = $false
    $deleteSucceeded = $false
    try {
        if ($null -eq $tempRoot -or $null -eq $scriptPath) {
            throw 'DELETE_PATH_UNAVAILABLE'
        }
        $tempBaseForDelete = [IO.Path]::GetFullPath([IO.Path]::GetTempPath()).TrimEnd([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
        $tempRootForDelete = [IO.Path]::GetFullPath($tempRoot).TrimEnd([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
        $scriptPathForDelete = [IO.Path]::GetFullPath($scriptPath)
        $pathComparerForDelete = [StringComparer]::OrdinalIgnoreCase
        if (-not $pathComparerForDelete.Equals([IO.Path]::GetDirectoryName($tempRootForDelete), $tempBaseForDelete)) {
            throw 'DELETE_ROOT_REJECTED'
        }
        if ([IO.Path]::GetFileName($tempRootForDelete) -cnotmatch '^omniroute-transport-preflight-[0-9a-f]{32}$') {
            throw 'DELETE_ROOT_NAME_REJECTED'
        }
        if (-not $pathComparerForDelete.Equals([IO.Path]::GetDirectoryName($scriptPathForDelete), $tempRootForDelete)) {
            throw 'DELETE_SCRIPT_NOT_DIRECT_CHILD'
        }
        if ([IO.Path]::GetFileName($scriptPathForDelete) -cne $reviewedLeaf) {
            throw 'DELETE_SCRIPT_LEAF_REJECTED'
        }
        if (-not $pathComparerForDelete.Equals([IO.Path]::GetFullPath($PSCommandPath), $scriptPathForDelete)) {
            throw 'DELETE_COMMAND_PATH_MISMATCH'
        }
        $scriptBytes = [IO.File]::ReadAllBytes($scriptPathForDelete)
        $actualScriptBytes = [long]$scriptBytes.LongLength
        $actualScriptSha256 = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($scriptBytes))
        [Array]::Clear($scriptBytes, 0, $scriptBytes.Length)
        $scriptBytes = $null
        if ($actualScriptBytes -ne $ExpectedScriptBytes -or $actualScriptSha256 -cne $ExpectedScriptSha256) {
            throw 'DELETE_HASH_OR_SIZE_MISMATCH'
        }
        $deleteGuard = $true
        Remove-Item -LiteralPath $scriptPathForDelete -Force -ErrorAction Stop
        $deleteSucceeded = -not [IO.File]::Exists($scriptPathForDelete)
    } catch {
        $cleanupOk = $false
        $exitCode = 1
    }

    if ($deleteGuard) { 'SCRIPT_DELETE_GUARD=PASS' } else { 'SCRIPT_DELETE_GUARD=FAIL' }
    if ($deleteSucceeded) { 'SCRIPT_DELETE=PASS' } else { 'SCRIPT_DELETE=FAIL' }
    "COUNTER_BASELINE_WRITES=$baselineWrites"
    "COUNTER_BASELINE_READS=$baselineReads"
    "COUNTER_COMPARISON_READS=$comparisonReads"
    "COUNTER_FINAL_WRITES=$finalWrites"
    "COUNTER_POST_CLEAR_READS=$postClearReads"
    if ($cleanupOk) { 'CLEANUP=PASS' } else { 'CLEANUP=FAIL' }
}

exit $exitCode
```

## Exact coordinator commands before any browser action

These commands are one continuous PowerShell 7 coordinator session. They
create only a fresh validated temporary root and the exact reviewed direct-child
script. They retain the exact `System.Diagnostics.Process` handle. They do not
start until the later review and action-time authority both exist.

```powershell
$ErrorActionPreference = 'Stop'
$cancelableReadLineOverloads = @([Console]::In.GetType().GetMethods() | Where-Object {
    $_.Name -eq 'ReadLineAsync' -and
    $_.GetParameters().Count -eq 1 -and
    $_.GetParameters()[0].ParameterType -eq [Threading.CancellationToken]
})
if ($PSVersionTable.PSVersion.Major -ne 7 -or $cancelableReadLineOverloads.Count -ne 1) { throw 'POWERSHELL_RUNTIME_CAPABILITY_FAIL' }
"RECORDED_POWERSHELL_VERSION=$($PSVersionTable.PSVersion)"
"RECORDED_DOTNET_VERSION=$([Environment]::Version)"
$reviewedScriptBytes = 8301
$reviewedScriptSha256 = '47CC3228B184D61328315D582748A7C145C98D9F4082D106E2E981F40A682F68'
$reviewedScriptLeaf = 'omniroute-transport-preflight.ps1'
$controlTimeoutSeconds = 120
$utf8NoBom = [Text.UTF8Encoding]::new($false, $true)

$tempBase = [IO.Path]::GetFullPath([IO.Path]::GetTempPath()).TrimEnd([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
$tempRoot = Join-Path -Path $tempBase -ChildPath ('omniroute-transport-preflight-' + [Guid]::NewGuid().ToString('N'))
$tempRoot = [IO.Path]::GetFullPath($tempRoot)
if (-not [StringComparer]::OrdinalIgnoreCase.Equals([IO.Path]::GetDirectoryName($tempRoot), $tempBase)) { throw 'TEMP_ROOT_VALIDATION_FAIL' }
if ([IO.Path]::GetFileName($tempRoot) -cnotmatch '^omniroute-transport-preflight-[0-9a-f]{32}$') { throw 'TEMP_ROOT_NAME_FAIL' }
$null = [IO.Directory]::CreateDirectory($tempRoot)

$scriptPath = [IO.Path]::GetFullPath((Join-Path -Path $tempRoot -ChildPath $reviewedScriptLeaf))
if (-not [StringComparer]::OrdinalIgnoreCase.Equals([IO.Path]::GetDirectoryName($scriptPath), $tempRoot)) { throw 'SCRIPT_DIRECT_CHILD_FAIL' }
if ([IO.Path]::GetFileName($scriptPath) -cne $reviewedScriptLeaf) { throw 'SCRIPT_LEAF_FAIL' }

$briefPath = 'C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-agent-routing-source\.superpowers\sdd\2026-08-30-omniroute-standard-team-api\task-2-anydesk-clipboard-preflight-live-brief.md'
$briefText = [IO.File]::ReadAllText($briefPath, $utf8NoBom)
$scriptMatch = [regex]::Match($briefText, '(?ms)^```powershell\n(?<script>param\(.*?^exit \$exitCode\n)```\n')
if (-not $scriptMatch.Success) { throw 'EXACT_SCRIPT_EXTRACTION_FAIL' }
$scriptText = $scriptMatch.Groups['script'].Value
if ($scriptText.Contains("`r") -or -not $scriptText.EndsWith("`n") -or $scriptText.EndsWith("`n`n")) { throw 'SCRIPT_LINE_ENDING_FAIL' }
$scriptBytes = $utf8NoBom.GetBytes($scriptText)
$scriptSha256 = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($scriptBytes))
if ($scriptBytes.LongLength -ne $reviewedScriptBytes -or $scriptSha256 -cne $reviewedScriptSha256) { throw 'REVIEWED_SCRIPT_BYTES_FAIL' }
[IO.File]::WriteAllBytes($scriptPath, $scriptBytes)

$recordedScriptBytes = [IO.File]::ReadAllBytes($scriptPath)
$recordedScriptSha256 = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($recordedScriptBytes))
if ($recordedScriptBytes.LongLength -ne $reviewedScriptBytes -or $recordedScriptSha256 -cne $reviewedScriptSha256) { throw 'RECORDED_SCRIPT_BYTES_FAIL' }
"RECORDED_TEMP_ROOT=$tempRoot"
"RECORDED_SCRIPT_PATH=$scriptPath"
"RECORDED_SCRIPT_BYTES=$($recordedScriptBytes.LongLength)"
"RECORDED_SCRIPT_SHA256=$recordedScriptSha256"
[Array]::Clear($recordedScriptBytes, 0, $recordedScriptBytes.Length)
$recordedScriptBytes = $null
[Array]::Clear($scriptBytes, 0, $scriptBytes.Length)
$scriptBytes = $null
$scriptText = $null
$briefText = $null

$startInfo = [Diagnostics.ProcessStartInfo]::new()
$startInfo.FileName = (Get-Command pwsh -ErrorAction Stop).Source
$startInfo.UseShellExecute = $false
$startInfo.CreateNoWindow = $true
$startInfo.RedirectStandardInput = $true
$startInfo.RedirectStandardOutput = $true
$startInfo.RedirectStandardError = $true
$startInfo.ArgumentList.Add('-NoLogo')
$startInfo.ArgumentList.Add('-NoProfile')
$startInfo.ArgumentList.Add('-NonInteractive')
$startInfo.ArgumentList.Add('-File')
$startInfo.ArgumentList.Add($scriptPath)
$startInfo.ArgumentList.Add('-ExpectedTempRoot')
$startInfo.ArgumentList.Add($tempRoot)
$startInfo.ArgumentList.Add('-ExpectedScriptPath')
$startInfo.ArgumentList.Add($scriptPath)
$startInfo.ArgumentList.Add('-ExpectedScriptSha256')
$startInfo.ArgumentList.Add($reviewedScriptSha256)
$startInfo.ArgumentList.Add('-ExpectedScriptBytes')
$startInfo.ArgumentList.Add([string]$reviewedScriptBytes)
$startInfo.ArgumentList.Add('-ControlTimeoutSeconds')
$startInfo.ArgumentList.Add([string]$controlTimeoutSeconds)

$preflightHandle = [Diagnostics.Process]::new()
$preflightHandle.StartInfo = $startInfo
if (-not $preflightHandle.Start()) { throw 'PREFLIGHT_SPAWN_FAIL' }
$expectedPid = $preflightHandle.Id

$ownerPidLine = $preflightHandle.StandardOutput.ReadLine()
$baselineClearLine = $preflightHandle.StandardOutput.ReadLine()
$baselineEmptyLine = $preflightHandle.StandardOutput.ReadLine()
$challengeLine = $preflightHandle.StandardOutput.ReadLine()
$ownerReadyLine = $preflightHandle.StandardOutput.ReadLine()
if ($ownerPidLine -cnotmatch '^OWNER_PID=([0-9]+)$') { throw 'OWNER_PID_LABEL_FAIL' }
$observedOwnerPid = [int]$Matches[1]
if ($observedOwnerPid -ne $expectedPid) { throw 'OWNER_PID_EQUALITY_FAIL' }
if ($baselineClearLine -cne 'BASELINE_CLEAR=PASS') { throw 'BASELINE_CLEAR_LABEL_FAIL' }
if ($baselineEmptyLine -cne 'BASELINE_EMPTY=PASS') { throw 'BASELINE_EMPTY_LABEL_FAIL' }
if ($challengeLine -cnotmatch '^CHALLENGE=([0-9A-F]{32})$') { throw 'CHALLENGE_LABEL_FAIL' }
$challenge = $Matches[1]
if ($ownerReadyLine -cne 'OWNER_READY=PASS') { throw 'OWNER_READY_LABEL_FAIL' }
"EXPECTED_PID=$expectedPid"
"OBSERVED_OWNER_PID=$observedOwnerPid"
'OWNER_PID_EQUALITY=PASS'

$pageHtml = '<!doctype html><meta charset="utf-8"><title>OmniRoute transport preflight</title><label for="c">Challenge</label><input id="c" aria-label="OmniRoute transport preflight challenge" readonly value="' + $challenge + '">'
$pageUrl = 'data:text/html;charset=utf-8,' + [Uri]::EscapeDataString($pageHtml)
```

The five startup reads above occur only after spawn and before the page opens;
the script emits those five lines synchronously before it starts its bounded
asynchronous control read. On any missing/mismatched startup line, the
coordinator sends exact `ABORT`, flushes, closes stdin, closes no unrelated
page, and proceeds only through the common cleanup/proof sequence below.

## Exact one-shot browser and control sequence

1. With no Cloudflare or token page open or touched, open exactly one new local
   Chrome `data:` page using the exact `$pageUrl`. Retain the exact returned
   page/tab handle as the preflight-page handle. Do not inspect, serialize,
   snapshot, screenshot, or extract the page or its contents.
2. Using the existing AnyDesk-visible Chrome surface, resolve only the input by
   its exact semantic accessible name `OmniRoute transport preflight challenge`
   and focus it exactly once. Do not use coordinates.
3. Issue exactly one `Control+A`, then exactly one `Control+C`. Do not use the
   browser clipboard API. Do not repeat either key or focus action.
4. Immediately send the one permitted successful control line from the same
   coordinator PowerShell 7 session:

```powershell
$preflightHandle.StandardInput.WriteLine('COPY_DONE')
$preflightHandle.StandardInput.Flush()
$preflightHandle.StandardInput.Close()
```

If any browser/focus/key action is not unambiguously complete, do not send
`COPY_DONE`; send exactly one fail-closed `ABORT` line instead, with no retry:

```powershell
$preflightHandle.StandardInput.WriteLine('ABORT')
$preflightHandle.StandardInput.Flush()
$preflightHandle.StandardInput.Close()
```

EOF is induced only by closing stdin without a line. Timeout is induced only
by sending no line. Neither is a fallback or retry; each is a terminal state.
The script reads at most one line, uses the monotonic 120-second deadline, and
cancels and observes its pending `ReadLineAsync(CancellationToken)` before
cleanup, so no blocking read is left orphaned.

| Terminal state | Comparison reads | Required emitted classification |
| --- | ---: | --- |
| exact `COPY_DONE` | `1` | internal exact compare; `PREFLIGHT=PASS` only on equality, otherwise `PREFLIGHT=FAIL` |
| `ABORT` or any rejected non-exact control line | `0` | `PREFLIGHT=ABORTED` |
| EOF | `0` | `PREFLIGHT=EOF` |
| monotonic timeout | `0` | `PREFLIGHT=TIMEOUT` |

## Common cleanup and external proof sequence

Every terminal state converges on the script's one `finally`. It performs the
single final OS-clipboard clear, one shape-only empty read, emits fixed cleanup
labels and actual counters, revalidates temp-root/direct-child/leaf/command
path plus the externally supplied exact size and SHA-256, deletes only that
exact-hash script, and exits. It never prints clipboard contents.

After sending the chosen control (or deliberately causing EOF/timeout), use
the retained handle and no PID lookup:

```powershell
$remainingStdout = $preflightHandle.StandardOutput.ReadToEnd()
$remainingStderr = $preflightHandle.StandardError.ReadToEnd()
if (-not $preflightHandle.WaitForExit(15000)) { throw 'RETAINED_HANDLE_EXIT_TIMEOUT_NO_KILL_AUTHORIZED' }
$observedExitCode = $preflightHandle.ExitCode
if ($remainingStderr.Length -ne 0) { throw 'PREFLIGHT_STDERR_NOT_EMPTY' }
"RETAINED_HANDLE_EXIT=PASS"
"OBSERVED_EXIT_CODE=$observedExitCode"
```

In a coordinator `finally`, close only the retained exact preflight-page handle
if it was created. Do not locate a page by title or URL and do not close any
other page. Then externally prove only the reviewed script and its fresh root
are absent; never kill an unverified PID and never delete on a hash mismatch:

```powershell
if ([IO.File]::Exists($scriptPath)) { throw 'EXTERNAL_SCRIPT_ABSENCE_FAIL' }
'EXTERNAL_SCRIPT_ABSENCE=PASS'
if ([IO.Directory]::Exists($tempRoot)) {
    $remainingEntries = [IO.Directory]::EnumerateFileSystemEntries($tempRoot)
    if ($remainingEntries.MoveNext()) { throw 'TEMP_ROOT_NOT_EMPTY' }
    [IO.Directory]::Delete($tempRoot, $false)
}
if ([IO.Directory]::Exists($tempRoot)) { throw 'EXTERNAL_TEMP_ROOT_ABSENCE_FAIL' }
'EXTERNAL_TEMP_ROOT_ABSENCE=PASS'
$preflightHandle.Dispose()
```

The exact page-close result must be recorded as
`EXACT_PREFLIGHT_PAGE_CLOSE=PASS|FAIL`. Overall PASS requires all expected
labels, exact PID equality, `PREFLIGHT=PASS`, `CLEANUP=PASS`, exit code `0`,
exact-page close PASS, retained-handle exit PASS, and external script/root
absence PASS. Any missing label, nonzero exit, cleanup failure, ambiguity, or
drift is FAIL / NOT PROVEN and stops. No process kill, second page, second
focus, second copy, retry, fallback, or alternate bridge is authorized.

## Structural counters and non-overlap

| Counter | Preflight maximum | Later credential stage |
| --- | ---: | ---: |
| fixed processes | `1` | credential-owner process exactly `1` only under a later gate |
| simultaneous preflight/credential processes | preflight must exit first | never overlap |
| local pages | `1` | separately reviewed later page only |
| transfer attempts | `1` | separately counted |
| semantic focuses / `Control+A` / `Control+C` | `1 / 1 / 1` | separately counted |
| baseline / comparison / post-clear reads | `1 / 0..1 / 1` | not shared |
| baseline / final cleanup writes | `1 / 1` | not shared |
| browser clipboard API reads/writes | `0 / 0` | `0 / 0` |
| retries / fallbacks / alternate bridges | `0 / 0 / 0` | `0 / 0 / 0` |

Credential-process counters are never rolled into preflight counters. A
preflight process must be externally proven exited and its exact script absent
before any later credential-owner process may start.

## Future additive evidence fields; no mutation now

This preparation writes no evidence. Only a later separately reviewed,
exact-path evidence gate may add `secure_console_transfer_v1.transport_preflight`
alongside all existing incident fields. That object must contain these fields:

| Field | Required non-secret value type |
| --- | --- |
| `reviewed_contract` | path, SHA-256, byte size |
| `reviewed_brief` | path, SHA-256, byte size |
| `reviewed_script` | filename, SHA-256, byte size |
| `started_at`, `ended_at` | bounded timestamps |
| `expected_pid`, `observed_owner_pid`, `owner_pid_equal` | retained-handle binding and equality result |
| `exit_proof` | retained-handle exit result and exit code |
| `counters` | exact preflight-only process/page/action/read/write/retry values |
| `result` | PASS, FAIL, ABORTED, EOF, or TIMEOUT |
| `cleanup_labels` | exact fixed emitted cleanup labels and results |
| `exact_page_close` | exact retained-page close result |
| `current_clipboard_cleanup` | final clear and shape-only empty results; never content |
| `exact_script_deletion` | internal guard/delete plus external script/root absence results |
| `authorizes_live_execution` | literal `false` |

The later additive object must contain no challenge, clipboard content,
credential, token, header, private identifier, page serialization, keystroke,
prompt, response body, or managed string. It must preserve every prior
incident fact, including overall FAIL, acceptance NOT PROVEN, private
transcript exposure, capture failure, and invalid-token HTTP 401 NOT PROVEN.
No evidence file is read or mutated under this brief-preparation authority.

## Independent-review stop

Stop after committing this one ignored brief and its ignored preparation
report. A fresh independent Sol High reviewer must verify the direct committed
bytes, extracted-script equality, strict encoding, exact two-path preparation
scope, no unresolved marker, no secret, executable syntax, control-read cancellation,
four-state counters, cleanup/deletion guards, prohibited-action scan, and every
authority boundary above. `FAIL / REVISE` authorizes nothing. Even a future
PASS authorizes only a later explicit preflight action-time decision.
