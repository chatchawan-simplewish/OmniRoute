# V61 exact retained-scope source package

Non-executable source container. Use only under the independently reviewed V61 contract; no predecessor gate is reopened.

## Exact retained preparation

```powershell
$briefRawForScope = [IO.File]::ReadAllText((Resolve-Path -LiteralPath '.superpowers\sdd\2026-08-30-omniroute-standard-team-api\task-2-secure-console-transfer-v61-live-source.md'), [Text.UTF8Encoding]::new($false, $true))
$prepTailForScope = $briefRawForScope.Substring($briefRawForScope.IndexOf('## Credential-free script preparation'))
$prepMatchForScope = [regex]::Match($prepTailForScope, '(?ms)^```powershell\n(?<code>.*?)^```$')
if (-not $prepMatchForScope.Success) { throw 'PREP_SCOPE_EXTRACTION_FAILED' }
$prepBytesForScope = [Text.UTF8Encoding]::new($false).GetBytes($prepMatchForScope.Groups['code'].Value)
$prepHashForScope = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($prepBytesForScope))
if ($prepBytesForScope.Length -ne 3988 -or $prepHashForScope -cne '83440D05C9B2486509D2DC9A51F10C4916FFAFFC1C6B7B6FABCE07188FAE76D5') { throw 'PREP_SCOPE_BYTE_PIN_FAILED' }
. ([scriptblock]::Create($prepMatchForScope.Groups['code'].Value))
if ([string]::IsNullOrWhiteSpace($transferRoot) -or [string]::IsNullOrWhiteSpace($ownerScriptPath) -or [string]::IsNullOrWhiteSpace($r5ScriptPath) -or [string]::IsNullOrWhiteSpace($safeLogPath)) { throw 'PREP_SCOPE_VARIABLES_MISSING' }
if ([IO.Path]::GetDirectoryName([IO.Path]::GetFullPath($ownerScriptPath)) -cne [IO.Path]::GetFullPath($transferRoot) -or [IO.Path]::GetDirectoryName([IO.Path]::GetFullPath($r5ScriptPath)) -cne [IO.Path]::GetFullPath($transferRoot) -or [IO.Path]::GetDirectoryName([IO.Path]::GetFullPath($safeLogPath)) -cne [IO.Path]::GetFullPath($transferRoot)) { throw 'PREP_SCOPE_CHILD_GUARD_FAILED' }
if ((Get-FileHash -Algorithm SHA256 -LiteralPath $ownerScriptPath).Hash -cne '383E21D339AD67D704F1515F2091D1363809CC23DC61176EE65246012A5E476A' -or (Get-FileHash -Algorithm SHA256 -LiteralPath $r5ScriptPath).Hash -cne 'DB75253CD851075C1D612A54EC4B02C8016C034C8BC192A3DB9D02DB9890AD41' -or (Test-Path -LiteralPath $safeLogPath)) { throw 'PREP_SCOPE_WRITTEN_STATE_FAILED' }
[Console]::Out.WriteLine('EXACT_RETAINED_SCOPE_PREPARATION=PASS')
```

## Exact retained launch

```powershell
$scopeOwnerStartAttempted = 0
$scopeOwnerStartFulfilled = 0
$scopeOwnerHandleRetained = $false
$scopeOwnerWaitAttempted = 0
$scopeOwnerWaitFulfilled = 0
$scopeOwnerFileCleanup = 0
$scopeOwnerRootCleanup = 0
$scopeProxyCleanup = 0
$scopeProxyChildStartAttempted = 0
$scopeProxyChildStartFulfilled = 0
$scopeProxyChildWaitAttempted = 0
$scopeProxyChildWaitFulfilled = 0
$scopeProxyChildTerminationAttempted = 0
$scopeProxyChildTerminationFulfilled = 0
$scopeProxyChildExitProofAttempted = 0
$scopeProxyChildExitProofFulfilled = 0
$scopeProxyChildDrainAttempted = 0
$scopeProxyChildDrainFulfilled = 0
$scopeProxyChildDisposeAttempted = 0
$scopeProxyChildDisposeFulfilled = 0
$scopeProxyChildResidual = 'NONE'
$scopeProxyCleanupProcess = $null
$scopeProxyCleanupOutTask = $null
$scopeProxyCleanupErrTask = $null
$scopeOwnerResidual = 'NONE'
$ownerTerminationAttempted = 0
$ownerTerminationFulfilled = 0
$ownerExitProofAttempted = 0
$ownerExitProofFulfilled = 0
$owner = $null
$expectedOwnerPid = $null
$ownerClock = $null

function Invoke-ExactScopeProxyCleanup {
    $remote = @'
set -eu
id="$(sudo docker inspect -f '{{.Id}}' team-api-proxy)"
printf '%s' "$id" | grep -Eq '^[0-9a-f]{64}$'
test "$(sudo docker inspect -f '{{.State.Status}}' team-api-proxy)" = running
test "$(sudo docker inspect -f '{{.Image}}' team-api-proxy)" = sha256:5f5c8640aae01df9654968d946d8f1a56c497f1dd5c5cda4cf95ab7c14d58648
test "$(sudo docker inspect -f '{{json .HostConfig.PortBindings}}' team-api-proxy)" = '{}'
test "$(sudo docker network inspect omniroute-internal --format '{{len .Containers}}')" = 3
! sudo ss -lntH | grep -Eq '(^|:)20130([[:space:]]|$)'
sudo docker rm -f team-api-proxy >/dev/null
test -z "$(sudo docker ps -aq -f name='^/team-api-proxy$')"
test "$(sudo docker network inspect omniroute-internal --format '{{len .Containers}}')" = 2
! sudo ss -lntH | grep -Eq '(^|:)20130([[:space:]]|$)'
printf 'EXACT_PROXY_CLEANUP=PASS\n'
'@
    $startInfo = [Diagnostics.ProcessStartInfo]::new()
    $startInfo.FileName = 'C:\Windows\System32\OpenSSH\ssh.exe'
    $startInfo.UseShellExecute = $false
    $startInfo.RedirectStandardOutput = $true
    $startInfo.RedirectStandardError = $true
    foreach ($arg in @('-i','C:\Users\chatc\.ssh\codex-prox01-vms-ed25519','-o','BatchMode=yes','-o','ConnectTimeout=10','-o','ServerAliveInterval=5','-o','ServerAliveCountMax=3','belladmin@192.168.1.68',$remote)) {
        $null = $startInfo.ArgumentList.Add($arg)
    }
    $script:scopeProxyCleanupProcess = [Diagnostics.Process]::new()
    $script:scopeProxyCleanupProcess.StartInfo = $startInfo
    $script:scopeProxyChildStartAttempted++
    try { $started = $script:scopeProxyCleanupProcess.Start() }
    catch {
        $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_START_UNCERTAIN'
        throw 'SCOPE_PROXY_CLEANUP_START_UNCERTAIN'
    }
    if (-not $started) {
        $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_START_FAILED'
        $script:scopeProxyChildDisposeAttempted++
        try { $script:scopeProxyCleanupProcess.Dispose() }
        catch {
            $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_START_FAILED_DISPOSE_NOT_PROVEN'
            throw 'SCOPE_PROXY_CLEANUP_START_FAILED_DISPOSE_NOT_PROVEN'
        }
        $script:scopeProxyChildDisposeFulfilled++
        $script:scopeProxyCleanupProcess = $null
        throw 'SCOPE_PROXY_CLEANUP_START_FAILED'
    }
    $script:scopeProxyChildStartFulfilled++
    try {
        $script:scopeProxyCleanupOutTask = $script:scopeProxyCleanupProcess.StandardOutput.ReadToEndAsync()
        $script:scopeProxyCleanupErrTask = $script:scopeProxyCleanupProcess.StandardError.ReadToEndAsync()
    }
    catch {
        $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_STREAM_TASK_START_NOT_PROVEN'
        throw 'SCOPE_PROXY_CLEANUP_STREAM_TASK_START_NOT_PROVEN'
    }
    $script:scopeProxyChildWaitAttempted++
    try { $scopeProxyChildExited = $script:scopeProxyCleanupProcess.WaitForExit(60000) }
    catch {
        $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_WAIT_NOT_PROVEN'
        throw 'SCOPE_PROXY_CLEANUP_WAIT_NOT_PROVEN'
    }
    $scopeProxyChildTimedOut = $false
    if (-not $scopeProxyChildExited) {
        $script:scopeProxyChildTerminationAttempted++
        try {
            $script:scopeProxyCleanupProcess.Kill()
            $script:scopeProxyChildTerminationFulfilled++
        }
        catch {
            $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_TERMINATION_NOT_PROVEN'
            throw 'SCOPE_PROXY_CLEANUP_TERMINATION_NOT_PROVEN'
        }
        $script:scopeProxyChildExitProofAttempted++
        try { $scopeProxyChildExitProven = $script:scopeProxyCleanupProcess.WaitForExit(10000) }
        catch {
            $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_EXIT_PROOF_NOT_PROVEN'
            throw 'SCOPE_PROXY_CLEANUP_EXIT_PROOF_NOT_PROVEN'
        }
        if (-not $scopeProxyChildExitProven) {
            $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_EXIT_NOT_PROVEN'
            throw 'SCOPE_PROXY_CLEANUP_TIMEOUT_EXIT_NOT_PROVEN'
        }
        $script:scopeProxyChildExitProofFulfilled++
        $scopeProxyChildTimedOut = $true
    }
    else { $script:scopeProxyChildWaitFulfilled++ }
    $script:scopeProxyChildDrainAttempted++
    try { $scopeProxyChildDrained = [Threading.Tasks.Task]::WaitAll(@($script:scopeProxyCleanupOutTask,$script:scopeProxyCleanupErrTask),5000) }
    catch {
        $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_DRAIN_WAIT_NOT_PROVEN'
        throw 'SCOPE_PROXY_CLEANUP_DRAIN_WAIT_NOT_PROVEN'
    }
    if (-not $scopeProxyChildDrained) {
        $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_DRAIN_TIMEOUT'
        throw 'SCOPE_PROXY_CLEANUP_DRAIN_TIMEOUT'
    }
    try {
        $scopeProxyChildStdout = $script:scopeProxyCleanupOutTask.Result
        $scopeProxyChildStderr = $script:scopeProxyCleanupErrTask.Result
        $scopeProxyChildExitCode = $script:scopeProxyCleanupProcess.ExitCode
    }
    catch {
        $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_DRAIN_RESULT_NOT_PROVEN'
        throw 'SCOPE_PROXY_CLEANUP_DRAIN_RESULT_NOT_PROVEN'
    }
    $script:scopeProxyChildDrainFulfilled++
    if ($scopeProxyChildTimedOut) {
        $scopeProxyChildTerminalResidual = 'PROXY_CLEANUP_CHILD_TIMEOUT_EXIT_PROVEN'
    }
    elseif ($scopeProxyChildExitCode -ne 0 -or $scopeProxyChildStdout.Trim() -ne 'EXACT_PROXY_CLEANUP=PASS' -or -not [string]::IsNullOrWhiteSpace($scopeProxyChildStderr)) {
        $scopeProxyChildTerminalResidual = 'PROXY_CLEANUP_CHILD_TERMINAL_NOT_PROVEN'
    }
    else { $scopeProxyChildTerminalResidual = 'NONE' }
    $script:scopeProxyChildResidual = $scopeProxyChildTerminalResidual
    $script:scopeProxyChildDisposeAttempted++
    try { $script:scopeProxyCleanupProcess.Dispose() }
    catch {
        if ($scopeProxyChildTerminalResidual -eq 'NONE') {
            $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_DISPOSE_NOT_PROVEN_AFTER_PASS'
        }
        elseif ($scopeProxyChildTimedOut) {
            $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_DISPOSE_NOT_PROVEN_AFTER_TIMEOUT_EXIT'
        }
        else {
            $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_DISPOSE_NOT_PROVEN_AFTER_TERMINAL_FAILURE'
        }
        throw 'SCOPE_PROXY_CLEANUP_DISPOSE_NOT_PROVEN'
    }
    $script:scopeProxyChildDisposeFulfilled++
    $script:scopeProxyCleanupProcess = $null
    $script:scopeProxyCleanupOutTask = $null
    $script:scopeProxyCleanupErrTask = $null
    if ($scopeProxyChildTerminalResidual -eq 'PROXY_CLEANUP_CHILD_TIMEOUT_EXIT_PROVEN') {
        throw 'SCOPE_PROXY_CLEANUP_TIMEOUT_EXIT_PROVEN'
    }
    if ($scopeProxyChildTerminalResidual -ne 'NONE') { throw 'SCOPE_PROXY_CLEANUP_NOT_PROVEN' }
}

function Remove-ExactScopePreparedFiles {
    $tempRoot = [IO.Path]::GetFullPath([IO.Path]::GetTempPath()).TrimEnd('\')
    $root = [IO.Path]::GetFullPath($transferRoot)
    if ([IO.Path]::GetDirectoryName($root).TrimEnd('\') -cne $tempRoot) { throw 'SCOPE_TEMP_ROOT_GUARD_FAILED' }
    foreach ($path in @($ownerScriptPath,$r5ScriptPath,$safeLogPath)) {
        if ([IO.Path]::GetDirectoryName([IO.Path]::GetFullPath($path)) -cne $root) { throw 'SCOPE_TEMP_CHILD_GUARD_FAILED' }
    }
    if (Test-Path -LiteralPath $safeLogPath) { throw 'SCOPE_SAFE_LOG_UNEXPECTED' }
    if (@(Get-ChildItem -LiteralPath $root -Force).Count -ne 2) { throw 'SCOPE_PREPARED_FILE_COUNT_DRIFT' }
    if ((Get-FileHash -Algorithm SHA256 -LiteralPath $ownerScriptPath).Hash -cne '383E21D339AD67D704F1515F2091D1363809CC23DC61176EE65246012A5E476A' -or
        (Get-FileHash -Algorithm SHA256 -LiteralPath $r5ScriptPath).Hash -cne 'DB75253CD851075C1D612A54EC4B02C8016C034C8BC192A3DB9D02DB9890AD41') {
        throw 'SCOPE_PREPARED_HASH_DRIFT'
    }
    Remove-Item -LiteralPath $ownerScriptPath -Force
    Remove-Item -LiteralPath $r5ScriptPath -Force
    if (@(Get-ChildItem -LiteralPath $root -Force).Count -ne 0) { throw 'SCOPE_TEMP_NOT_EMPTY' }
    Remove-Item -LiteralPath $root -Force
}

try {
    $launchPwshV61 = 'C:\Users\chatc\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\powershell\pwsh.exe'
    if ((Get-Item -LiteralPath $launchPwshV61).Length -ne 301368 -or
        (Get-FileHash -Algorithm SHA256 -LiteralPath $launchPwshV61).Hash -cne '362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139' -or
        [Diagnostics.FileVersionInfo]::GetVersionInfo($launchPwshV61).FileVersion -cne '7.6.5.500') {
        throw 'V61_PRELAUNCH_RUNTIME_PIN_DRIFT'
    }
    $launchTailForScope = $briefRawForScope.Substring($briefRawForScope.IndexOf('## Launch and transfer sequence'))
    $launchMatchForScope = [regex]::Match($launchTailForScope, '(?ms)^```powershell\n(?<code>.*?)^```$')
    if (-not $launchMatchForScope.Success) { throw 'LAUNCH_SCOPE_EXTRACTION_FAILED' }
    $launchBytesForScope = [Text.UTF8Encoding]::new($false).GetBytes($launchMatchForScope.Groups['code'].Value)
    $launchHashForScope = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($launchBytesForScope))
    if ($launchBytesForScope.Length -ne 675 -or $launchHashForScope -cne 'C4DDD2E84C14C125830DD422C613CE9DC4CFCDBCABB760F003B9187811B7D2FA') { throw 'LAUNCH_SCOPE_BYTE_PIN_FAILED' }

    $finalMatchesForScope = [regex]::Matches($launchTailForScope, '(?ms)^```powershell\n(?<code>.*?)^```$')
    if ($finalMatchesForScope.Count -ne 2) { throw 'FINAL_SCOPE_EXTRACTION_COUNT_FAILED' }
    $ownerFinalCodeForScope = $finalMatchesForScope[1].Groups['code'].Value
    $ownerFinalBytesForScope = [Text.UTF8Encoding]::new($false).GetBytes($ownerFinalCodeForScope)
    $ownerFinalHashForScope = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($ownerFinalBytesForScope))
    if ($ownerFinalBytesForScope.Length -ne 2779 -or $ownerFinalHashForScope -cne '9316DE2F7C84A89947E57C8563E9381E97D7C52F0DFFE56CA7E4DE616DD8F637') { throw 'FINAL_SCOPE_BYTE_PIN_FAILED' }

    $replacementPathForScope = '.superpowers\sdd\2026-08-30-omniroute-standard-team-api\task-2-secure-console-transfer-v61-scope-source.md'
    $replacementRawForScope = [IO.File]::ReadAllText((Resolve-Path -LiteralPath $replacementPathForScope),[Text.UTF8Encoding]::new($false,$true))
    $dispositionTailForScope = $replacementRawForScope.Substring($replacementRawForScope.IndexOf('### Exact post-launch pre-accept failure disposition'))
    $dispositionMatchForScope = [regex]::Match($dispositionTailForScope, '(?ms)^```powershell\n(?<code>.*?)^```$')
    if (-not $dispositionMatchForScope.Success) { throw 'DISPOSITION_SCOPE_EXTRACTION_FAILED' }
    $ownerPreacceptDispositionCodeForScope = $dispositionMatchForScope.Groups['code'].Value
    $dispositionBytesForScope = [Text.UTF8Encoding]::new($false).GetBytes($ownerPreacceptDispositionCodeForScope)
    $dispositionHashForScope = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($dispositionBytesForScope))
    if ($dispositionBytesForScope.Length -ne 3308 -or $dispositionHashForScope -cne 'B8087F2CB77A695C1B6DD145DDD3D39D48F8AABEBBA00863BEA0610C8BE6518E') { throw 'DISPOSITION_SCOPE_BYTE_PIN_FAILED' }

    $scopeOwnerStartAttempted++
    . ([scriptblock]::Create($launchMatchForScope.Groups['code'].Value))
    if ($null -eq $owner -or $owner.Id -ne $expectedOwnerPid -or $null -eq $ownerClock) { throw 'LAUNCH_SCOPE_HANDLE_MISSING' }
    $scopeOwnerStartFulfilled++
    $scopeOwnerHandleRetained = $true
    [Console]::Out.WriteLine(('EXACT_RETAINED_SCOPE_OWNER_LAUNCHED=PASS START={0}/{1} HANDLE={2}' -f $scopeOwnerStartAttempted,$scopeOwnerStartFulfilled,$scopeOwnerHandleRetained.ToString().ToUpperInvariant()))
}
catch {
    if ($scopeOwnerStartAttempted -eq 0) {
        try {
            Remove-ExactScopePreparedFiles
            $scopeOwnerFileCleanup = 1
            $scopeOwnerRootCleanup = 1
            Invoke-ExactScopeProxyCleanup
            $scopeProxyCleanup = 1
            $scopeOwnerResidual = 'PRESTART_CLEANUP_PASS'
        }
        catch { $scopeOwnerResidual = 'PRESTART_CLEANUP_NOT_PROVEN' }
        [Console]::Out.WriteLine(('EXACT_RETAINED_SCOPE_OWNER_LAUNCH=FAIL START={0}/{1} HANDLE=FALSE FILE_CLEANUP={2} ROOT_CLEANUP={3} PROXY_CLEANUP={4} RESIDUAL={5} PROXY_CHILD_START={6}/{7} WAIT={8}/{9} TERMINATION={10}/{11} EXIT_PROOF={12}/{13} DRAIN={14}/{15} DISPOSE={16}/{17} CHILD_RESIDUAL={18}' -f $scopeOwnerStartAttempted,$scopeOwnerStartFulfilled,$scopeOwnerFileCleanup,$scopeOwnerRootCleanup,$scopeProxyCleanup,$scopeOwnerResidual,$scopeProxyChildStartAttempted,$scopeProxyChildStartFulfilled,$scopeProxyChildWaitAttempted,$scopeProxyChildWaitFulfilled,$scopeProxyChildTerminationAttempted,$scopeProxyChildTerminationFulfilled,$scopeProxyChildExitProofAttempted,$scopeProxyChildExitProofFulfilled,$scopeProxyChildDrainAttempted,$scopeProxyChildDrainFulfilled,$scopeProxyChildDisposeAttempted,$scopeProxyChildDisposeFulfilled,$scopeProxyChildResidual))
        throw 'RETAINED_SCOPE_PRESTART_FAILURE_NO_RETRY'
    }
    if ($owner -is [Diagnostics.Process] -and $null -ne $ownerClock) {
        $scopeOwnerHandleRetained = $true
        if ($null -eq $expectedOwnerPid) { $expectedOwnerPid = $owner.Id }
        . ([scriptblock]::Create($ownerPreacceptDispositionCodeForScope))
        throw 'RETAINED_SCOPE_POSTSTART_FAILURE_DISPOSED_NO_RETRY'
    }
    $scopeOwnerResidual = 'START_UNCERTAIN_NO_HANDLE'
    [Console]::Out.WriteLine(('EXACT_RETAINED_SCOPE_OWNER_LAUNCH=FAIL START={0}/{1} HANDLE=FALSE WAIT=0/0 TERMINATION=0/0 EXIT_PROOF=0/0 FILE_CLEANUP=0 ROOT_CLEANUP=0 PROXY_CLEANUP=0 RESIDUAL={2} PROXY_CHILD_START=0/0 WAIT=0/0 TERMINATION=0/0 EXIT_PROOF=0/0 DRAIN=0/0 DISPOSE=0/0 CHILD_RESIDUAL=NONE' -f $scopeOwnerStartAttempted,$scopeOwnerStartFulfilled,$scopeOwnerResidual))
    throw 'RETAINED_SCOPE_START_UNCERTAIN_NO_HANDLE_NO_RETRY'
}
```

### Exact post-launch pre-accept failure disposition

```powershell
$scopeOwnerWaitAttempted++
try {
    . ([scriptblock]::Create($ownerFinalCodeForScope))
    $scopeOwnerWaitFulfilled++
    if ((Test-Path -LiteralPath $ownerScriptPath -PathType Leaf) -or (Test-Path -LiteralPath $r5ScriptPath -PathType Leaf) -or (Test-Path -LiteralPath $safeLogPath -PathType Leaf)) { throw 'SCOPE_OWNER_FILES_REMAIN' }
    $scopeOwnerFileCleanup = 1
    if (Test-Path -LiteralPath $transferRoot) { throw 'SCOPE_OWNER_ROOT_REMAINS' }
    $scopeOwnerRootCleanup = 1
    Invoke-ExactScopeProxyCleanup
    $scopeProxyCleanup = 1
    $scopeOwnerResidual = 'NONE'
    [Console]::Out.WriteLine(('EXACT_PREACCEPT_OWNER_DISPOSITION=PASS START={0}/{1} HANDLE={2} WAIT={3}/{4} TERMINATION={5}/{6} EXIT_PROOF={7}/{8} FILE_CLEANUP={9} ROOT_CLEANUP={10} PROXY_CLEANUP={11} RESIDUAL={12} PROXY_CHILD_START={13}/{14} WAIT={15}/{16} TERMINATION={17}/{18} EXIT_PROOF={19}/{20} DRAIN={21}/{22} DISPOSE={23}/{24} CHILD_RESIDUAL={25}' -f $scopeOwnerStartAttempted,$scopeOwnerStartFulfilled,$scopeOwnerHandleRetained.ToString().ToUpperInvariant(),$scopeOwnerWaitAttempted,$scopeOwnerWaitFulfilled,$ownerTerminationAttempted,$ownerTerminationFulfilled,$ownerExitProofAttempted,$ownerExitProofFulfilled,$scopeOwnerFileCleanup,$scopeOwnerRootCleanup,$scopeProxyCleanup,$scopeOwnerResidual,$scopeProxyChildStartAttempted,$scopeProxyChildStartFulfilled,$scopeProxyChildWaitAttempted,$scopeProxyChildWaitFulfilled,$scopeProxyChildTerminationAttempted,$scopeProxyChildTerminationFulfilled,$scopeProxyChildExitProofAttempted,$scopeProxyChildExitProofFulfilled,$scopeProxyChildDrainAttempted,$scopeProxyChildDrainFulfilled,$scopeProxyChildDisposeAttempted,$scopeProxyChildDisposeFulfilled,$scopeProxyChildResidual))
}
catch {
    if ($null -ne $owner) {
        try {
            if (-not $owner.HasExited) { $scopeOwnerResidual = 'EXACT_OWNER_EXIT_NOT_PROVEN' }
            else { $scopeOwnerResidual = 'POSTEXIT_CLEANUP_NOT_PROVEN' }
        }
        catch { $scopeOwnerResidual = 'EXACT_OWNER_STATE_NOT_PROVEN' }
    }
    elseif ($scopeOwnerResidual -eq 'NONE') { $scopeOwnerResidual = 'POSTEXIT_CLEANUP_NOT_PROVEN' }
    [Console]::Out.WriteLine(('EXACT_PREACCEPT_OWNER_DISPOSITION=FAIL START={0}/{1} HANDLE={2} WAIT={3}/{4} TERMINATION={5}/{6} EXIT_PROOF={7}/{8} FILE_CLEANUP={9} ROOT_CLEANUP={10} PROXY_CLEANUP={11} RESIDUAL={12} PROXY_CHILD_START={13}/{14} WAIT={15}/{16} TERMINATION={17}/{18} EXIT_PROOF={19}/{20} DRAIN={21}/{22} DISPOSE={23}/{24} CHILD_RESIDUAL={25}' -f $scopeOwnerStartAttempted,$scopeOwnerStartFulfilled,$scopeOwnerHandleRetained.ToString().ToUpperInvariant(),$scopeOwnerWaitAttempted,$scopeOwnerWaitFulfilled,$ownerTerminationAttempted,$ownerTerminationFulfilled,$ownerExitProofAttempted,$ownerExitProofFulfilled,$scopeOwnerFileCleanup,$scopeOwnerRootCleanup,$scopeProxyCleanup,$scopeOwnerResidual,$scopeProxyChildStartAttempted,$scopeProxyChildStartFulfilled,$scopeProxyChildWaitAttempted,$scopeProxyChildWaitFulfilled,$scopeProxyChildTerminationAttempted,$scopeProxyChildTerminationFulfilled,$scopeProxyChildExitProofAttempted,$scopeProxyChildExitProofFulfilled,$scopeProxyChildDrainAttempted,$scopeProxyChildDrainFulfilled,$scopeProxyChildDisposeAttempted,$scopeProxyChildDisposeFulfilled,$scopeProxyChildResidual))
    throw 'RETAINED_SCOPE_PREACCEPT_DISPOSITION_NOT_PROVEN_NO_RETRY'
}
```
