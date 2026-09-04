# V61 exact live-source package

Non-executable source container; authority and ordered preconditions are only in the V61 replacement contract. Original gates remain closed. No fence may be evaluated during review.

## Credential-free private proxy start and 19-label proof

```powershell
$ErrorActionPreference = 'Stop'
$sshPath = 'C:\Windows\System32\OpenSSH\ssh.exe'
$sshKey = 'C:\Users\chatc\.ssh\codex-prox01-vms-ed25519'
$sshTarget = 'belladmin@192.168.1.68'
$sshWallDeadlineMs = 60000
$sshExitProofDeadlineMs = 10000
$sshStreamDrainDeadlineMs = 5000
$sshRetainedProcess = $null

function Invoke-ExactSsh([string]$Operation, [string]$RemoteCommand) {
    $startInfo = [Diagnostics.ProcessStartInfo]::new()
    $startInfo.FileName = $sshPath
    $startInfo.UseShellExecute = $false
    $startInfo.RedirectStandardOutput = $true
    $startInfo.RedirectStandardError = $true
    foreach ($name in @('CLOUDFLARE_API_TOKEN','CLOUDFLARE_ZONE_ID')) {
        $null = $startInfo.Environment.Remove($name)
    }
    foreach ($arg in @('-i',$sshKey,'-o','BatchMode=yes','-o','ConnectTimeout=10','-o','ServerAliveInterval=5','-o','ServerAliveCountMax=3',$sshTarget,$RemoteCommand)) {
        $null = $startInfo.ArgumentList.Add($arg)
    }
    $script:sshRetainedProcess = [Diagnostics.Process]::new()
    $script:sshRetainedProcess.StartInfo = $startInfo
    if (-not $script:sshRetainedProcess.Start()) { throw "SSH_${Operation}_START_FAILED_NO_RETRY" }
    $outTask = $script:sshRetainedProcess.StandardOutput.ReadToEndAsync()
    $errTask = $script:sshRetainedProcess.StandardError.ReadToEndAsync()
    if (-not $script:sshRetainedProcess.WaitForExit($sshWallDeadlineMs)) {
        $terminationAttempted = 1
        $terminationFulfilled = 0
        try {
            $script:sshRetainedProcess.Kill()
            $terminationFulfilled = 1
        }
        catch {}
        $exitProven = $script:sshRetainedProcess.WaitForExit($sshExitProofDeadlineMs)
        throw ("SSH_{0}_TIMEOUT_NO_RETRY TERMINATION={1}/{2} EXIT_PROVEN={3}" -f
            $Operation,$terminationAttempted,$terminationFulfilled,$exitProven.ToString().ToUpperInvariant())
    }
    if (-not [Threading.Tasks.Task]::WaitAll(@($outTask,$errTask),$sshStreamDrainDeadlineMs)) {
        throw "SSH_${Operation}_STREAM_DRAIN_UNCERTAIN_NO_RETRY"
    }
    $exit = $script:sshRetainedProcess.ExitCode
    $out = $outTask.Result
    $err = $errTask.Result
    $script:sshRetainedProcess.Dispose()
    $script:sshRetainedProcess = $null
    [pscustomobject]@{ Exit = $exit; Out = $out; Err = $err; WallDeadlineMs = $sshWallDeadlineMs }
}

$startCommand = 'sudo docker run -d --name team-api-proxy --restart unless-stopped --network omniroute-internal --read-only --cap-drop ALL --cap-add NET_BIND_SERVICE --security-opt no-new-privileges:true --memory 128m --cpus 0.5 --tmpfs /data:rw,noexec,nosuid,size=16m --tmpfs /config:rw,noexec,nosuid,size=16m --mount type=bind,src=/opt/omniroute-team-api/Caddyfile,dst=/etc/caddy/Caddyfile,readonly caddy@sha256:5f5c8640aae01df9654968d946d8f1a56c497f1dd5c5cda4cf95ab7c14d58648 caddy run --config /etc/caddy/Caddyfile'
$startResult = Invoke-ExactSsh 'START' $startCommand
$startLines = @($startResult.Out -split "`r?`n" | Where-Object { $_ })
if ($startResult.Exit -ne 0 -or $startLines.Count -ne 1 -or
    $startLines[0] -notmatch '^[0-9a-f]{64}$' -or
    -not [string]::IsNullOrWhiteSpace($startResult.Err)) {
    throw 'EXACT_PROXY_START_FAILED_OR_UNCERTAIN_NO_RETRY'
}
$proxyId = $startLines[0]
$startResult = $null
$startLines = $null

$remoteProof = @'
set -u
expected_id='__PROXY_ID__'
pass() { printf 'ASSERT=%s STATUS=PASS\n' "$1"; }
fail() { printf 'ASSERT=%s STATUS=FAIL ACTUAL=%s EXPECTED=%s\n' "$1" "$2" "$3" >&2; exit 90; }
check_eq() {
    label="$1"; expected="$2"; shift 2
    actual="$("$@" 2>&1)"; rc=$?
    if [ "$rc" -ne 0 ]; then fail "$label" "command_exit_$rc" "$expected"; fi
    if [ "$actual" != "$expected" ]; then fail "$label" "$actual" "$expected"; fi
    pass "$label"
}
check_eq same_container_id "$expected_id" sudo docker inspect -f '{{.Id}}' team-api-proxy
check_eq state_running running sudo docker inspect -f '{{.State.Status}}' team-api-proxy
check_eq image_id sha256:5f5c8640aae01df9654968d946d8f1a56c497f1dd5c5cda4cf95ab7c14d58648 sudo docker inspect -f '{{.Image}}' team-api-proxy
check_eq port_bindings '{}' sudo docker inspect -f '{{json .HostConfig.PortBindings}}' team-api-proxy
check_eq readonly_rootfs true sudo docker inspect -f '{{.HostConfig.ReadonlyRootfs}}' team-api-proxy
check_eq cap_drop '["ALL"]' sudo docker inspect -f '{{json .HostConfig.CapDrop}}' team-api-proxy
check_eq cap_add '["CAP_NET_BIND_SERVICE"]' sudo docker inspect -f '{{json .HostConfig.CapAdd}}' team-api-proxy
check_eq security_opt '["no-new-privileges:true"]' sudo docker inspect -f '{{json .HostConfig.SecurityOpt}}' team-api-proxy
check_eq memory 134217728 sudo docker inspect -f '{{.HostConfig.Memory}}' team-api-proxy
check_eq nano_cpus 500000000 sudo docker inspect -f '{{.HostConfig.NanoCpus}}' team-api-proxy
check_eq restart_policy unless-stopped sudo docker inspect -f '{{.HostConfig.RestartPolicy.Name}}' team-api-proxy
check_eq caddy_mount 'bind:/opt/omniroute-team-api/Caddyfile:/etc/caddy/Caddyfile:false' sudo docker inspect -f '{{range .Mounts}}{{if eq .Destination "/etc/caddy/Caddyfile"}}{{.Type}}:{{.Source}}:{{.Destination}}:{{.RW}}{{end}}{{end}}' team-api-proxy
sha_line="$(sudo sha256sum /opt/omniroute-team-api/Caddyfile 2>&1)"; rc=$?
if [ "$rc" -ne 0 ]; then fail caddy_sha "command_exit_$rc" a31c2010bb47767e25a826cebcd2469cb51d8af5c5ae089e46d2051edd69d9bb; fi
actual_sha="${sha_line%% *}"
if [ "$actual_sha" != a31c2010bb47767e25a826cebcd2469cb51d8af5c5ae089e46d2051edd69d9bb ]; then fail caddy_sha "$actual_sha" a31c2010bb47767e25a826cebcd2469cb51d8af5c5ae089e46d2051edd69d9bb; fi
pass caddy_sha
check_eq network_members 3 sudo docker network inspect omniroute-internal --format '{{len .Containers}}'
listen_out="$(sudo ss -lntH 2>&1)"; rc=$?
if [ "$rc" -ne 0 ]; then fail listener_20130 "command_exit_$rc" absent; fi
if printf '%s\n' "$listen_out" | grep -Eq '(^|:)20130([[:space:]]|$)'; then fail listener_20130 present absent; fi
pass listener_20130
ip="$(sudo docker inspect -f '{{with index .NetworkSettings.Networks "omniroute-internal"}}{{.IPAddress}}{{end}}' team-api-proxy 2>&1)"; rc=$?
if [ "$rc" -ne 0 ] || [ -z "$ip" ]; then fail proxy_ip "command_exit_or_empty_$rc" nonempty; fi
pass proxy_ip
check_eq allow_get_models 401 curl --max-time 10 -sS -o /dev/null -w '%{http_code}' "http://$ip:20130/v1/models"
check_eq deny_dashboard 404 curl --max-time 10 -sS -o /dev/null -w '%{http_code}' "http://$ip:20130/dashboard"
check_eq deny_wrong_method 404 curl --max-time 10 -sS -o /dev/null -w '%{http_code}' -X POST "http://$ip:20130/v1/models"
printf 'PROXY_PROOF=PASS ASSERTIONS=19\n'
'@.Replace('__PROXY_ID__',$proxyId)

$proofResult = Invoke-ExactSsh 'PROOF' $remoteProof
$proofLines = @($proofResult.Out -split "`r?`n" | Where-Object { $_ })
$expectedLabels = @('same_container_id','state_running','image_id','port_bindings','readonly_rootfs','cap_drop','cap_add','security_opt','memory','nano_cpus','restart_policy','caddy_mount','caddy_sha','network_members','listener_20130','proxy_ip','allow_get_models','deny_dashboard','deny_wrong_method')
$proofPass = $proofResult.Exit -eq 0 -and [string]::IsNullOrWhiteSpace($proofResult.Err) -and $proofLines.Count -eq 20
foreach ($label in $expectedLabels) {
    if (@($proofLines | Where-Object { $_ -eq "ASSERT=$label STATUS=PASS" }).Count -ne 1) { $proofPass = $false }
}
if (@($proofLines | Where-Object { $_ -eq 'PROXY_PROOF=PASS ASSERTIONS=19' }).Count -ne 1) { $proofPass = $false }
if (-not $proofPass) {
    $rollback = @'
set -eu
expected='__PROXY_ID__'
actual="$(sudo docker inspect -f '{{.Id}}' team-api-proxy 2>/dev/null || true)"
test "$actual" = "$expected"
sudo docker rm -f "$expected" >/dev/null
test -z "$(sudo docker ps -aq -f name='^/team-api-proxy$')"
test "$(sudo docker network inspect omniroute-internal --format '{{len .Containers}}')" = 2
! sudo ss -lntH | grep -Eq '(^|:)20130([[:space:]]|$)'
printf 'EXACT_PROXY_ROLLBACK=PASS\n'
'@.Replace('__PROXY_ID__',$proxyId)
    $rollbackResult = Invoke-ExactSsh 'ROLLBACK' $rollback
    if ($rollbackResult.Exit -ne 0 -or $rollbackResult.Out.Trim() -ne 'EXACT_PROXY_ROLLBACK=PASS' -or
        -not [string]::IsNullOrWhiteSpace($rollbackResult.Err)) {
        throw 'PROXY_PROOF_AND_ROLLBACK_UNCERTAIN_NO_RETRY'
    }
    throw 'PROXY_PROOF_FAILED_ROLLED_BACK_NO_RETRY'
}
$proofResult = $null
$proofLines = $null
$remoteProof = $null
[Console]::Out.WriteLine('PROXY_START_AND_PROOF=PASS')
```

## Credential-free script preparation

```powershell
$ErrorActionPreference = 'Stop'
$utf8 = [Text.UTF8Encoding]::new($false, $true)
$briefPath = '.superpowers\sdd\2026-08-30-omniroute-standard-team-api\task-2-secure-console-transfer-v61-live-source.md'
$r5ReviewPath = '.superpowers\sdd\2026-08-30-omniroute-standard-team-api\task-2-rulesets-api-incident-sol-review.md'
$expectedOwnerBytes = 22582
$expectedOwnerHash = '383E21D339AD67D704F1515F2091D1363809CC23DC61176EE65246012A5E476A'
$expectedR5Bytes = 10890
$expectedR5Hash = 'DB75253CD851075C1D612A54EC4B02C8016C034C8BC192A3DB9D02DB9890AD41'
$expectedR5ReviewBytes = 32520
$expectedR5ReviewHash = '1950DC72285AA349E33CDFEDCE948C7A99CADF1F70528DF22F643FBA07FBB33A'

$briefRaw = [IO.File]::ReadAllText((Resolve-Path -LiteralPath $briefPath), $utf8)
$ownerTail = $briefRaw.Substring($briefRaw.IndexOf('## Exact owner script'))
$ownerMatch = [regex]::Match($ownerTail, '(?ms)^```powershell\n(?<code>.*?)^```$')
if (-not $ownerMatch.Success) { throw 'OWNER_SOURCE_EXTRACTION_FAILED' }
$ownerBytes = [Text.UTF8Encoding]::new($false).GetBytes($ownerMatch.Groups['code'].Value)
$ownerHash = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($ownerBytes))
if ($ownerBytes.Length -ne $expectedOwnerBytes -or $ownerHash -cne $expectedOwnerHash) {
    throw 'OWNER_SOURCE_BYTE_PIN_FAILED'
}

$r5ReviewBytes = [IO.File]::ReadAllBytes((Resolve-Path -LiteralPath $r5ReviewPath))
$r5ReviewHash = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($r5ReviewBytes))
if ($r5ReviewBytes.Length -ne $expectedR5ReviewBytes -or $r5ReviewHash -cne $expectedR5ReviewHash) {
    throw 'R5_REVIEW_BYTE_PIN_FAILED'
}
$r5ReviewRaw = $utf8.GetString($r5ReviewBytes)
$r5Tail = $r5ReviewRaw.Substring($r5ReviewRaw.IndexOf('### Deterministic R5 script'))
$r5Match = [regex]::Match($r5Tail, '(?ms)^```powershell\n(?<code>.*?)^```$')
if (-not $r5Match.Success) { throw 'R5_SOURCE_EXTRACTION_FAILED' }
$r5Bytes = [Text.UTF8Encoding]::new($false).GetBytes($r5Match.Groups['code'].Value)
$r5Hash = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($r5Bytes))
if ($r5Bytes.Length -ne $expectedR5Bytes -or $r5Hash -cne $expectedR5Hash) {
    throw 'R5_SOURCE_BYTE_PIN_FAILED'
}

$parseTokens = $null
$parseErrors = $null
$null = [Management.Automation.Language.Parser]::ParseInput($ownerMatch.Groups['code'].Value, [ref]$parseTokens, [ref]$parseErrors)
if (@($parseErrors).Count -ne 0) { throw 'OWNER_SOURCE_PARSE_FAILED' }
$parseTokens = $null
$parseErrors = $null
$null = [Management.Automation.Language.Parser]::ParseInput($r5Match.Groups['code'].Value, [ref]$parseTokens, [ref]$parseErrors)
if (@($parseErrors).Count -ne 0) { throw 'R5_SOURCE_PARSE_FAILED' }

$resolvedTemp = [IO.Path]::GetFullPath([IO.Path]::GetTempPath())
$transferRoot = [IO.Path]::GetFullPath((Join-Path $resolvedTemp ("omniroute-secure-console-{0}" -f [guid]::NewGuid().ToString('N'))))
if ([IO.Path]::GetDirectoryName($transferRoot) -cne $resolvedTemp.TrimEnd('\')) {
    throw 'TEMP_ROOT_GUARD_FAILED'
}
if (Test-Path -LiteralPath $transferRoot) { throw 'V61_PREP_ROOT_PREEXISTS' }
$scopePreparationRootCreateAttempted++
$null = [IO.Directory]::CreateDirectory($transferRoot)
$scopePreparationRootCreateFulfilled++
$ownerScriptPath = [IO.Path]::GetFullPath((Join-Path $transferRoot 'omniroute-secure-console-owner.ps1'))
$r5ScriptPath = [IO.Path]::GetFullPath((Join-Path $transferRoot 'omniroute-r5-exact.ps1'))
$safeLogPath = [IO.Path]::GetFullPath((Join-Path $transferRoot 'omniroute-secure-console-safe.log'))
foreach ($path in @($ownerScriptPath,$r5ScriptPath,$safeLogPath)) {
    if ([IO.Path]::GetDirectoryName($path) -cne $transferRoot) { throw 'TEMP_CHILD_GUARD_FAILED' }
}
if (Test-Path -LiteralPath $safeLogPath) { throw 'SAFE_LOG_PREEXISTS' }
[IO.File]::WriteAllBytes($ownerScriptPath, $ownerBytes)
[IO.File]::WriteAllBytes($r5ScriptPath, $r5Bytes)
if ((Get-FileHash -Algorithm SHA256 -LiteralPath $ownerScriptPath).Hash -cne $expectedOwnerHash -or
    (Get-FileHash -Algorithm SHA256 -LiteralPath $r5ScriptPath).Hash -cne $expectedR5Hash) {
    throw 'WRITTEN_SCRIPT_HASH_FAILED'
}
[Console]::Out.WriteLine('EXACT_OWNER_AND_R5_SCRIPTS_PREPARED=PASS')
```

## Exact owner script

```powershell
param(
    [Parameter(Mandatory)][string]$ExpectedOwnerSha256,
    [Parameter(Mandatory)][string]$R5ScriptPath
)

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
$ownerFileName = 'omniroute-secure-console-owner.ps1'
$r5FileName = 'omniroute-r5-exact.ps1'
$pwshPath = 'C:\Users\chatc\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\powershell\pwsh.exe'
$r5ExpectedBytes = 10890
$r5ExpectedHash = 'DB75253CD851075C1D612A54EC4B02C8016C034C8BC192A3DB9D02DB9890AD41'
$pwshExpectedBytes = 301368
$pwshExpectedHash = '362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139'
$pwshExpectedVersion = '7.6.5.500'
$secretDeadline = [TimeSpan]::FromSeconds(600)
$revocationDeadline = [TimeSpan]::FromSeconds(600)
$r5WallDeadlineMs = 180000
$r5ExitProofDeadlineMs = 10000
$r5StreamDrainDeadlineMs = 5000
$tokenName = 'OmniRoute secure console R5 20260901'
$zoneName = 'mysw.me'
$tempRoot = [IO.Path]::GetFullPath([IO.Path]::GetTempPath())
$ownerPath = [IO.Path]::GetFullPath($PSCommandPath)
$r5Path = [IO.Path]::GetFullPath($R5ScriptPath)
$ownerRoot = [IO.Path]::GetFullPath([IO.Path]::GetDirectoryName($ownerPath))
$secret = [Security.SecureString]::new()
$key = $null
$keyChar = $null
$ctrl = $null
$revocationKey = $null
$revocationKeyChar = $null
$bstr = [IntPtr]::Zero
$token = $null
$zoneId = $null
$headers = $null
$authorization = $null
$verifyResponse = $null
$zoneResponse = $null
$invalidResponse = $null
$r5Process = $null
$r5StartInfo = $null
$r5Raw = $null
$r5Err = $null
$r5State = $null
$r5OutTask = $null
$r5ErrTask = $null
$maskedAccepted = $false
$tokenAccepted = $false
$r5Passed = $false
$revocationGranted = $false
$invalid401 = $false
$clipboardClearAttempted = 0
$clipboardClearFulfilled = 0
$clipboardReadAttempted = 0
$clipboardReadFulfilled = 0
$clipboardFinalEmpty = $false
$tokenVerifyAttempted = 0
$tokenVerifyFulfilled = 0
$zoneLookupAttempted = 0
$zoneLookupFulfilled = 0
$r5ChildAttempted = 0
$r5ChildStarted = 0
$r5ChildExited = 0
$r5WaitAttempted = 0
$r5WaitFulfilled = 0
$r5TimeoutObserved = 0
$r5TerminationAttempted = 0
$r5TerminationFulfilled = 0
$r5ExitProofAttempted = 0
$r5ExitProofFulfilled = 0
$r5StdoutCaptureFulfilled = 0
$r5StderrCaptureFulfilled = 0
$r5PrivateEnvClearAttempted = 0
$r5PrivateEnvClearFulfilled = 0
$r5Residual = 'NONE'
$invalidCheckAttempted = 0
$invalidCheckFulfilled = 0
$ownerDeleteAttempted = 0
$ownerDeleteFulfilled = 0
$r5DeleteAttempted = 0
$r5DeleteFulfilled = 0
$cleanupError = 'NONE'
$postAcceptError = 'NONE'
$safeOutputUncertain = $false
$terminal = 'FAIL_STOP_NO_RETRY'
$exitCode = 90

function Write-Safe([string]$Line) {
    try {
        [Console]::Out.WriteLine($Line)
        [Console]::Out.Flush()
    }
    catch {
        $script:safeOutputUncertain = $true
    }
}

function Set-PostAcceptFailure([string]$Code) {
    if ($script:postAcceptError -eq 'NONE') { $script:postAcceptError = $Code }
}

function Clear-R5PrivateEnvironmentOnce {
    if (-not $script:r5StartInfo -or $script:r5PrivateEnvClearAttempted -ne 0) { return }
    foreach ($name in @('CLOUDFLARE_API_TOKEN','CLOUDFLARE_ZONE_ID')) {
        $script:r5PrivateEnvClearAttempted++
        $null = $script:r5StartInfo.Environment.Remove($name)
        $script:r5PrivateEnvClearFulfilled++
    }
}

function Clear-CurrentClipboardOnce {
    if ($script:clipboardClearAttempted -ne 0 -or $script:clipboardReadAttempted -ne 0) {
        throw 'CLIPBOARD_CLEANUP_ALREADY_ATTEMPTED'
    }
    $script:clipboardClearAttempted++
    Set-Clipboard -Value '' -ErrorAction Stop
    $script:clipboardClearFulfilled++
    $script:clipboardReadAttempted++
    $observed = Get-Clipboard -Raw -ErrorAction Stop
    $script:clipboardReadFulfilled++
    $script:clipboardFinalEmpty = [string]::IsNullOrEmpty([string]$observed)
    $observed = $null
    if (-not $script:clipboardFinalEmpty) { throw 'CLIPBOARD_NOT_EMPTY_AFTER_CLEAR' }
}

try {
    if ([IO.Path]::GetFileName($ownerPath) -cne $ownerFileName -or
        [IO.Path]::GetFileName($r5Path) -cne $r5FileName -or
        [IO.Path]::GetDirectoryName($r5Path) -cne $ownerRoot -or
        [IO.Path]::GetDirectoryName($ownerRoot) -cne $tempRoot.TrimEnd('\') -or
        -not (Test-Path -LiteralPath $ownerPath -PathType Leaf) -or
        -not (Test-Path -LiteralPath $r5Path -PathType Leaf)) {
        throw 'TEMP_PATH_GUARD_FAILED'
    }
    $ownerHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $ownerPath).Hash
    $r5Item = Get-Item -LiteralPath $r5Path -ErrorAction Stop
    $r5Hash = (Get-FileHash -Algorithm SHA256 -LiteralPath $r5Path).Hash
    if ($ownerHash -cne $ExpectedOwnerSha256 -or
        $r5Item.Length -ne $r5ExpectedBytes -or $r5Hash -cne $r5ExpectedHash) {
        throw 'SCRIPT_BYTE_GUARD_FAILED'
    }
    if (-not [string]::IsNullOrEmpty([Environment]::GetEnvironmentVariable('CLOUDFLARE_API_TOKEN')) -or
        -not [string]::IsNullOrEmpty([Environment]::GetEnvironmentVariable('CLOUDFLARE_ZONE_ID'))) {
        throw 'OWNER_PRIVATE_ENV_NOT_EMPTY'
    }

    $readyPwshItem = Get-Item -LiteralPath $pwshPath -ErrorAction Stop
    if ($readyPwshItem.FullName -cne $pwshPath -or
        $readyPwshItem.Length -ne $pwshExpectedBytes -or
        (Get-FileHash -Algorithm SHA256 -LiteralPath $pwshPath).Hash -cne $pwshExpectedHash -or
        [Diagnostics.FileVersionInfo]::GetVersionInfo($pwshPath).FileVersion -cne $pwshExpectedVersion) {
        throw 'OWNER_PWSH_ACTION_TIME_PIN_DRIFT'
    }
    $readyPwshItem = $null

    Write-Safe 'OWNER_READY=PASS'
    Write-Safe ("OWNER_PID={0}" -f $PID)
    Write-Safe 'SECRET_PROMPT_READY=PASS'
    [Console]::Error.WriteLine('Paste once into this masked prompt. Before pressing Enter, close the exact generated-token page natively. Then return here and press Enter once. Escape or Ctrl+C cancels.')

    $clock = [Diagnostics.Stopwatch]::StartNew()
    $accepted = $false
    $cancelled = $false
    while ($clock.Elapsed -lt $secretDeadline) {
        if (-not [Console]::KeyAvailable) {
            [Threading.Thread]::Sleep(25)
            continue
        }
        try {
            $key = [Console]::ReadKey($true)
            $keyChar = $key.KeyChar
            $ctrl = ($key.Modifiers -band [ConsoleModifiers]::Control) -ne 0
            if ($key.Key -eq [ConsoleKey]::Escape -or
                ($ctrl -and $key.Key -eq [ConsoleKey]::C)) {
                $cancelled = $true
                break
            }
            if ($key.Key -eq [ConsoleKey]::Enter) {
                $accepted = $secret.Length -gt 0
                break
            }
            if ($key.Key -eq [ConsoleKey]::Backspace) {
                if ($secret.Length -gt 0) { $secret.RemoveAt($secret.Length - 1) }
                continue
            }
            if (-not [char]::IsControl($keyChar)) { $secret.AppendChar($keyChar) }
        }
        finally {
            $keyChar = $null
            $key = $null
            $ctrl = $null
        }
    }
    $clock.Stop()
    if ($cancelled) { throw 'MASKED_INPUT_CANCELLED' }
    if (-not $accepted) { throw 'MASKED_INPUT_EMPTY_OR_TIMEOUT' }
    $secret.MakeReadOnly()
    $maskedAccepted = $true
    try {
        try {
            Clear-CurrentClipboardOnce

            $bstr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secret)
            $token = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($bstr)
            if ([string]::IsNullOrWhiteSpace($token)) { throw 'TOKEN_CONVERSION_EMPTY' }

            $authorization = "Bearer $token"
        $headers = @{ Authorization = $authorization }
        $tokenVerifyAttempted++
        $verifyResponse = Invoke-RestMethod -Method Get -Uri 'https://api.cloudflare.com/client/v4/user/tokens/verify' -Headers $headers -TimeoutSec 20
        $tokenVerifyFulfilled++
        if (-not $verifyResponse.success -or $verifyResponse.result.status -ne 'active') {
            throw 'ACTIVE_TOKEN_VERIFICATION_FAILED'
        }
        $tokenAccepted = $true

        $zoneLookupAttempted++
        $zoneResponse = Invoke-RestMethod -Method Get -Uri 'https://api.cloudflare.com/client/v4/zones?name=mysw.me&status=active&per_page=2' -Headers $headers -TimeoutSec 20
        $zoneLookupFulfilled++
        $zones = @($zoneResponse.result)
        if (-not $zoneResponse.success -or $zones.Count -ne 1 -or
            [int]$zoneResponse.result_info.total_count -ne 1 -or
            [string]$zones[0].name -cne $zoneName -or
            [string]$zones[0].id -notmatch '^[0-9a-f]{32}$') {
            throw 'EXACT_ZONE_LOOKUP_FAILED'
        }
        $zoneId = [string]$zones[0].id
        $zones = $null
        }
        catch {
            Set-PostAcceptFailure 'VERIFY_ZONE_OR_CONVERSION_FAILED'
        }
        finally {
            if ($headers) { $headers.Authorization = $null }
            $headers = $null
            $authorization = $null
            $verifyResponse = $null
            $zoneResponse = $null
        }

        if ($tokenAccepted -and $postAcceptError -eq 'NONE') {
        try {
            $r5StartInfo = [Diagnostics.ProcessStartInfo]::new()
            $r5StartInfo.FileName = $pwshPath
            $r5StartInfo.UseShellExecute = $false
            $r5StartInfo.RedirectStandardOutput = $true
            $r5StartInfo.RedirectStandardError = $true
            foreach ($arg in @('-NoLogo','-NoProfile','-NonInteractive','-File',$r5Path)) {
                $null = $r5StartInfo.ArgumentList.Add($arg)
            }
            foreach ($name in @('CLOUDFLARE_API_TOKEN','CLOUDFLARE_ZONE_ID','R5_MODE','R5_RULESET_ID','R5_RULE_ID','R5_BEFORE_IDS')) {
                $null = $r5StartInfo.Environment.Remove($name)
            }
            $r5StartInfo.Environment['CLOUDFLARE_API_TOKEN'] = $token
            $r5StartInfo.Environment['CLOUDFLARE_ZONE_ID'] = $zoneId
            $r5StartInfo.Environment['R5_MODE'] = 'create'
            $r5Process = [Diagnostics.Process]::new()
            $r5Process.StartInfo = $r5StartInfo
            $resolvedPwshPath = [IO.Path]::GetFullPath($r5StartInfo.FileName)
            $pwshItem = Get-Item -LiteralPath $resolvedPwshPath -ErrorAction Stop
            $pwshHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $resolvedPwshPath).Hash
            $pwshVersion = [Diagnostics.FileVersionInfo]::GetVersionInfo($resolvedPwshPath).FileVersion
            if ($resolvedPwshPath -cne $pwshPath -or $pwshItem.FullName -cne $pwshPath -or
                $pwshItem.Length -ne $pwshExpectedBytes -or $pwshHash -cne $pwshExpectedHash -or
                $pwshVersion -cne $pwshExpectedVersion) {
                throw 'R5_PWSH_ACTION_TIME_PIN_DRIFT'
            }
            $r5ChildAttempted++
            if (-not $r5Process.Start()) { throw 'R5_CHILD_START_FAILED' }
            $r5ChildStarted++
            Clear-R5PrivateEnvironmentOnce
            $zoneId = $null
            $r5OutTask = $r5Process.StandardOutput.ReadToEndAsync()
            $r5ErrTask = $r5Process.StandardError.ReadToEndAsync()
            $r5WaitAttempted++
            $r5ExitedWithinDeadline = $r5Process.WaitForExit($r5WallDeadlineMs)
            $r5WaitFulfilled++
            if (-not $r5ExitedWithinDeadline) {
                $r5TimeoutObserved++
                $r5TerminationAttempted++
                try {
                    $r5Process.Kill()
                    $r5TerminationFulfilled++
                }
                catch {}
                $r5ExitProofAttempted++
                if ($r5Process.WaitForExit($r5ExitProofDeadlineMs)) {
                    $r5ExitProofFulfilled++
                    $r5ChildExited++
                }
                else {
                    $r5Residual = 'EXACT_CHILD_EXIT_NOT_PROVEN'
                    throw 'R5_TIMEOUT_EXIT_NOT_PROVEN'
                }
                Set-PostAcceptFailure 'R5_TIMEOUT_TERMINATED_NO_RETRY'
                throw 'R5_WALL_DEADLINE_EXPIRED'
            }
            $r5ChildExited++
            if (-not [Threading.Tasks.Task]::WaitAll(@($r5OutTask,$r5ErrTask),$r5StreamDrainDeadlineMs)) {
                $r5Residual = 'STREAM_CAPTURE_NOT_PROVEN'
                throw 'R5_STREAM_DRAIN_UNCERTAIN'
            }
            $r5Raw = $r5OutTask.Result
            $r5StdoutCaptureFulfilled++
            $r5Err = $r5ErrTask.Result
            $r5StderrCaptureFulfilled++
            $r5Exit = $r5Process.ExitCode
            $r5Lines = @($r5Raw -split "`r?`n" | Where-Object { $_ })
            if ($r5Lines.Count -ne 1 -or -not [string]::IsNullOrWhiteSpace($r5Err)) {
                throw 'R5_OUTPUT_SHAPE_FAILED'
            }
            $r5State = $r5Lines[0] | ConvertFrom-Json -ErrorAction Stop
            if ($r5Exit -ne 0 -or $r5State.status -ne 'PASS' -or
                [int]$r5State.delete_count -ne 0 -or
                [string]$r5State.ruleset_id -notmatch '^[0-9a-f]{32}$' -or
                [string]$r5State.rule_id -notmatch '^[0-9a-f]{32}$' -or
                @($r5State.before_ids).Count -ne 1) {
                throw 'R5_TERMINAL_FAILED'
            }
            $r5Passed = $true
            Write-Safe 'R5_RESULT=PASS'
        }
        catch {
            Set-PostAcceptFailure 'R5_FAILED_OR_UNCERTAIN'
            Write-Safe 'R5_RESULT=FAIL'
        }
        finally {
            if ($r5Process -and $r5ChildStarted -eq 1 -and $r5ChildExited -eq 0) {
                if ($r5TerminationAttempted -eq 0) {
                    $r5TerminationAttempted++
                    try {
                        $r5Process.Kill()
                        $r5TerminationFulfilled++
                    }
                    catch {}
                }
                if ($r5ExitProofAttempted -eq 0) {
                    $r5ExitProofAttempted++
                    if ($r5Process.WaitForExit($r5ExitProofDeadlineMs)) {
                        $r5ExitProofFulfilled++
                        $r5ChildExited++
                    }
                    else {
                        $r5Residual = 'EXACT_CHILD_EXIT_NOT_PROVEN'
                        Set-PostAcceptFailure 'R5_EXIT_NOT_PROVEN'
                    }
                }
            }
            if ($r5StartInfo) {
                Clear-R5PrivateEnvironmentOnce
            }
            if ($r5Process -and $r5ChildExited -eq 1) { $r5Process.Dispose() }
            $r5Process = $null
            $r5StartInfo = $null
            $r5OutTask = $null
            $r5ErrTask = $null
            $r5Raw = $null
            $r5Err = $null
            $r5State = $null
            $r5Lines = $null
            $r5Exit = $null
            $zoneId = $null
            $resolvedPwshPath = $null
            $pwshItem = $null
            $pwshHash = $null
            $pwshVersion = $null
            $r5ExitedWithinDeadline = $null
        }
        }
    }
    catch {
        Set-PostAcceptFailure 'POST_ACCEPT_OPERATION_UNEXPECTED_FAILURE'
    }
    finally {

    if ($maskedAccepted) {
        try {
            Write-Safe 'REVOCATION_REQUIRED=PASS'
            Write-Safe ("REVOCATION_ROW_NAME={0}" -f $tokenName)
            Write-Safe 'REVOCATION_AUTHORITY=WAITING'
            try {
                [Console]::Error.WriteLine('After separate chat confirmation, delete only the exact token row and prove refreshed name/row counts 0/0. Then press G here. Press D to deny. No automation may press either key.')
            }
            catch {
                Set-PostAcceptFailure 'REVOCATION_PROMPT_OUTPUT_UNCERTAIN'
            }
            $revocationClock = [Diagnostics.Stopwatch]::StartNew()
            $revocationDecision = 'TIMEOUT'
            while ($revocationClock.Elapsed -lt $revocationDeadline) {
                if (-not [Console]::KeyAvailable) {
                    [Threading.Thread]::Sleep(25)
                    continue
                }
                try {
                    $revocationKey = [Console]::ReadKey($true)
                    $revocationKeyChar = $revocationKey.KeyChar
                    if ($revocationKey.Key -eq [ConsoleKey]::G) {
                        $revocationDecision = 'GRANTED'
                        break
                    }
                    if ($revocationKey.Key -eq [ConsoleKey]::D -or
                        $revocationKey.Key -eq [ConsoleKey]::Escape) {
                        $revocationDecision = 'DENIED'
                        break
                    }
                }
                finally {
                    $revocationKeyChar = $null
                    $revocationKey = $null
                }
            }
            $revocationClock.Stop()
            Write-Safe ("REVOCATION_AUTHORITY={0}" -f $revocationDecision)
            if ($revocationDecision -eq 'GRANTED') {
                $revocationGranted = $true
                if (-not [string]::IsNullOrWhiteSpace($token)) {
                    try {
                        $authorization = "Bearer $token"
                        $headers = @{ Authorization = $authorization }
                        $invalidCheckAttempted++
                        try {
                            $invalidResponse = Invoke-RestMethod -Method Get -Uri 'https://api.cloudflare.com/client/v4/user/tokens/verify' -Headers $headers -TimeoutSec 20
                            $invalidCheckFulfilled++
                        }
                        catch {
                            $statusCode = [int]$_.Exception.Response.StatusCode
                            $invalidCheckFulfilled++
                        }
                        if ($statusCode -ne 401) { throw 'EXACT_TOKEN_INVALIDITY_NOT_401' }
                        $invalid401 = $true
                        Write-Safe 'INVALID_TOKEN_HTTP=401'
                    }
                    catch {
                        Set-PostAcceptFailure 'REVOCATION_INVALIDITY_NOT_PROVEN'
                    }
                    finally {
                        if ($headers) { $headers.Authorization = $null }
                        $headers = $null
                        $authorization = $null
                        $invalidResponse = $null
                        $statusCode = $null
                    }
                }
                else {
                    Set-PostAcceptFailure 'REVOCATION_INVALIDITY_NOT_PROVEN_NO_USABLE_TOKEN'
                    Write-Safe 'INVALID_TOKEN_HTTP=NOT_PROVEN_NO_USABLE_TOKEN'
                }
            }
            else {
                Set-PostAcceptFailure 'ACTIVE_TOKEN_REVOCATION_NOT_PROVEN'
                Write-Safe 'CREDENTIAL_INCIDENT=ACTIVE_TOKEN_REVOCATION_NOT_PROVEN'
            }
        }
        catch {
            Set-PostAcceptFailure 'REVOCATION_HOLD_FAILED_OR_UNCERTAIN'
            Write-Safe 'CREDENTIAL_INCIDENT=ACTIVE_TOKEN_REVOCATION_NOT_PROVEN'
        }
    }
    }

    if ($safeOutputUncertain) { Set-PostAcceptFailure 'SAFE_OUTPUT_UNCERTAIN' }
    if ($r5Passed -and $revocationGranted -and $invalid401 -and $postAcceptError -eq 'NONE') {
        $terminal = 'EXACT_CORRECTION_PASS_TOKEN_REVOKED'
        $exitCode = 0
    }
    elseif ($revocationGranted -and $invalid401) {
        $terminal = 'FAIL_TOKEN_REVOKED_NO_RETRY'
        $exitCode = 91
    }
}
catch {
    if ($maskedAccepted) {
        Set-PostAcceptFailure 'POST_ACCEPT_UNEXPECTED_FAILURE_AFTER_HOLD'
        Write-Safe 'CREDENTIAL_INCIDENT=ACTIVE_TOKEN_REVOCATION_NOT_PROVEN'
    }
}
finally {
    try {
        if ($clipboardClearAttempted -eq 0) { Clear-CurrentClipboardOnce }
    }
    catch {
        $cleanupError = 'CLIPBOARD_CLEANUP_FAILED'
        $terminal = 'FAIL_CLEANUP_NOT_PROVEN_NO_RETRY'
        $exitCode = 92
    }
    if ($headers) { $headers.Authorization = $null }
    $headers = $null
    $authorization = $null
    $zoneId = $null
    $token = $null
    if ($bstr -ne [IntPtr]::Zero) {
        [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr)
        $bstr = [IntPtr]::Zero
    }
    if ($secret) { $secret.Dispose() }
    $secret = $null
    $keyChar = $null
    $key = $null
    $ctrl = $null
    $revocationKeyChar = $null
    $revocationKey = $null
    $verifyResponse = $null
    $zoneResponse = $null
    $invalidResponse = $null
    $r5Raw = $null
    $r5Err = $null
    $r5State = $null
    $r5OutTask = $null
    $r5ErrTask = $null
    try {
        if ((Get-FileHash -Algorithm SHA256 -LiteralPath $r5Path).Hash -cne $r5ExpectedHash) {
            throw 'R5_DELETE_GUARD_FAILED'
        }
        $r5DeleteAttempted++
        Remove-Item -LiteralPath $r5Path -Force -ErrorAction Stop
        $r5DeleteFulfilled++
        if ((Get-FileHash -Algorithm SHA256 -LiteralPath $ownerPath).Hash -cne $ExpectedOwnerSha256) {
            throw 'OWNER_DELETE_GUARD_FAILED'
        }
        $ownerDeleteAttempted++
        Remove-Item -LiteralPath $ownerPath -Force -ErrorAction Stop
        $ownerDeleteFulfilled++
    }
    catch {
        $cleanupError = 'SCRIPT_CLEANUP_FAILED'
        $terminal = 'FAIL_CLEANUP_NOT_PROVEN_NO_RETRY'
        $exitCode = 93
    }
    Write-Safe ("CLIPBOARD_CLEAR={0}/{1}" -f $clipboardClearAttempted,$clipboardClearFulfilled)
    Write-Safe ("CLIPBOARD_READ={0}/{1}" -f $clipboardReadAttempted,$clipboardReadFulfilled)
    Write-Safe ("CLIPBOARD_EMPTY={0}" -f $clipboardFinalEmpty.ToString().ToUpperInvariant())
    Write-Safe ("TOKEN_VERIFY={0}/{1}" -f $tokenVerifyAttempted,$tokenVerifyFulfilled)
    Write-Safe ("ZONE_LOOKUP={0}/{1}" -f $zoneLookupAttempted,$zoneLookupFulfilled)
    Write-Safe ("R5_CHILD={0}/{1}/{2}" -f $r5ChildAttempted,$r5ChildStarted,$r5ChildExited)
    Write-Safe ("R5_WAIT={0}/{1} TIMEOUT={2}" -f $r5WaitAttempted,$r5WaitFulfilled,$r5TimeoutObserved)
    Write-Safe ("R5_TERMINATION={0}/{1}" -f $r5TerminationAttempted,$r5TerminationFulfilled)
    Write-Safe ("R5_EXIT_PROOF={0}/{1}" -f $r5ExitProofAttempted,$r5ExitProofFulfilled)
    Write-Safe ("R5_STREAM_CAPTURE={0}/{1}" -f $r5StdoutCaptureFulfilled,$r5StderrCaptureFulfilled)
    Write-Safe ("R5_PRIVATE_ENV_CLEAR={0}/{1}" -f $r5PrivateEnvClearAttempted,$r5PrivateEnvClearFulfilled)
    Write-Safe ("R5_RESIDUAL={0}" -f $r5Residual)
    Write-Safe ("INVALID_CHECK={0}/{1}" -f $invalidCheckAttempted,$invalidCheckFulfilled)
    Write-Safe ("R5_SCRIPT_DELETE={0}/{1}" -f $r5DeleteAttempted,$r5DeleteFulfilled)
    Write-Safe ("OWNER_SCRIPT_DELETE={0}/{1}" -f $ownerDeleteAttempted,$ownerDeleteFulfilled)
    Write-Safe ("POST_ACCEPT_ERROR={0}" -f $postAcceptError)
    Write-Safe ("SAFE_OUTPUT_UNCERTAIN={0}" -f $safeOutputUncertain.ToString().ToUpperInvariant())
    Write-Safe ("CLEANUP_ERROR={0}" -f $cleanupError)
    Write-Safe ("OWNER_RESULT={0}" -f $terminal)
}

exit $exitCode
```

## Launch and transfer sequence

```powershell
$ownerWallDeadlineMs = 1800000
$ownerExitProofDeadlineMs = 10000
$ownerTerminationAttempted = 0
$ownerTerminationFulfilled = 0
$ownerExitProofAttempted = 0
$ownerExitProofFulfilled = 0
$ownerTimedOut = $false
$ownerClock = [Diagnostics.Stopwatch]::StartNew()
$owner = Start-Process -FilePath 'C:\Users\chatc\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\powershell\pwsh.exe' -ArgumentList @('-NoLogo','-NoProfile','-File',$ownerScriptPath,'-ExpectedOwnerSha256','383E21D339AD67D704F1515F2091D1363809CC23DC61176EE65246012A5E476A','-R5ScriptPath',$r5ScriptPath) -WindowStyle Normal -RedirectStandardOutput $safeLogPath -PassThru
$expectedOwnerPid = $owner.Id
```

```powershell
$ownerElapsedMs = [int64]$ownerClock.ElapsedMilliseconds
$ownerRemainingMs = [int64]$ownerWallDeadlineMs - $ownerElapsedMs
[Console]::Out.WriteLine(("OWNER_ELAPSED_MS={0} OWNER_REMAINING_MS={1}" -f $ownerElapsedMs,$ownerRemainingMs))
if ($ownerRemainingMs -le 0) {
    $ownerTimedOut = $true
}
elseif (-not $owner.WaitForExit([int]$ownerRemainingMs)) {
    $ownerTimedOut = $true
}
if ($ownerTimedOut) {
    [Console]::Out.WriteLine('OWNER_WALL_DEADLINE=EXPIRED')
    [Console]::Out.WriteLine('OWNER_TIMEOUT_STATE=TOKEN_AND_REVOCATION_NOT_PROVEN')
    if (-not $owner.HasExited) {
        $ownerTerminationAttempted++
        try {
            $owner.Kill()
            $ownerTerminationFulfilled++
        }
        catch {}
        $ownerExitProofAttempted++
        if ($owner.WaitForExit($ownerExitProofDeadlineMs)) {
            $ownerExitProofFulfilled++
        }
        else {
            [Console]::Out.WriteLine(("OWNER_TERMINATION={0}/{1} EXIT_PROOF={2}/{3} RESIDUAL=EXACT_OWNER_RUNNING_NOT_PROVEN" -f $ownerTerminationAttempted,$ownerTerminationFulfilled,$ownerExitProofAttempted,$ownerExitProofFulfilled))
            throw 'OWNER_TIMEOUT_EXIT_NOT_PROVEN_NO_RETRY'
        }
    }
}
$ownerClock.Stop()
$ownerExit = $owner.ExitCode
$owner.Dispose()
$owner = $null
$safeLines = @(Get-Content -LiteralPath $safeLogPath -ErrorAction Stop)
if (@($safeLines | Where-Object { $_ -eq "OWNER_PID=$expectedOwnerPid" }).Count -ne 1) {
    throw 'OWNER_PID_OUTPUT_MISMATCH'
}
if (Test-Path -LiteralPath $ownerScriptPath -PathType Leaf) { throw 'OWNER_SCRIPT_REMAINS' }
if (Test-Path -LiteralPath $r5ScriptPath -PathType Leaf) { throw 'R5_SCRIPT_REMAINS' }
if ($safeLines -match '(?i)bearer\s|authorization|cfut_|eyJ[A-Za-z0-9_-]*\.|[A-Fa-f0-9]{32}') {
    throw 'SAFE_LOG_REDACTION_FAILED'
}
$safeLogBytes = [IO.File]::ReadAllBytes($safeLogPath)
$safeLogHash = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($safeLogBytes))
$safeLogLength = $safeLogBytes.Length
$resolvedSafeLog = [IO.Path]::GetFullPath($safeLogPath)
if ([IO.Path]::GetDirectoryName($resolvedSafeLog) -cne $transferRoot) { throw 'SAFE_LOG_DELETE_GUARD_FAILED' }
Remove-Item -LiteralPath $resolvedSafeLog -Force -ErrorAction Stop
if (@(Get-ChildItem -LiteralPath $transferRoot -Force -ErrorAction Stop).Count -ne 0) {
    throw 'TEMP_ROOT_NOT_EMPTY'
}
Remove-Item -LiteralPath $transferRoot -Force -ErrorAction Stop
[Console]::Out.WriteLine(("OWNER_TIMEOUT={0} TERMINATION={1}/{2} EXIT_PROOF={3}/{4}" -f $ownerTimedOut.ToString().ToUpperInvariant(),$ownerTerminationAttempted,$ownerTerminationFulfilled,$ownerExitProofAttempted,$ownerExitProofFulfilled))
[Console]::Out.WriteLine(("OWNER_EXIT={0} SAFE_LOG_BYTES={1} SAFE_LOG_SHA256={2} CLEANUP=PASS" -f $ownerExit,$safeLogLength,$safeLogHash))
```
