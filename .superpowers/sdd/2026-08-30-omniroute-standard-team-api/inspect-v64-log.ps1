function Get-V64StatusSummary {
    param([byte[]]$Bytes)
    $reject = [pscustomobject]@{Grammar='REJECTED_REDACTED'; Fields=[ordered]@{}}
    $raw = $null; $lines = $null; $line = $null
    try {
        if ($Bytes.Length -lt 1 -or $Bytes.Length -gt 476) { return $reject }
        $raw = [Text.UTF8Encoding]::new($false,$true).GetString($Bytes)
        if ($raw.StartsWith([string][char]0xfeff,[StringComparison]::Ordinal)) { $raw = $raw.Substring(1) }
        if ($raw -cmatch '[^\x20-\x7E\r\n]') { return $reject }
        $lines = @([regex]::Split($raw,'\r?\n'))
        if ($lines[-1] -ceq '') { $lines = @($lines | Select-Object -SkipLast 1) }
        if ($lines.Count -lt 1 -or $lines.Count -gt 32) { return $reject }
        $map = [Collections.Generic.Dictionary[string,object]]::new([StringComparer]::Ordinal)
        $values = [ordered]@{
            CLIPBOARD_CLEAR=@('0/0','1/0','1/1'); CLIPBOARD_READ=@('0/0','1/0','1/1')
            CLIPBOARD_EMPTY=@('TRUE','FALSE'); TOKEN_VERIFY=@('0/0','1/0','1/1')
            ZONE_LOOKUP=@('0/0','1/0','1/1'); R5_CHILD=@('0/0/0','1/0/0','1/1/0','1/1/1')
            R5_WAIT=@('0/0 TIMEOUT=0','1/0 TIMEOUT=0','1/0 TIMEOUT=1','1/1 TIMEOUT=0')
            R5_TERMINATION=@('0/0','1/0','1/1'); R5_EXIT_PROOF=@('0/0','1/0','1/1')
            R5_STREAM_CAPTURE=@('0/0','0/1','1/0','1/1'); R5_PRIVATE_ENV_CLEAR=@('0/0','1/0','1/1')
            R5_RESIDUAL=@('NONE','EXACT_CHILD_EXIT_NOT_PROVEN','STREAM_CAPTURE_NOT_PROVEN')
            INVALID_CHECK=@('0/0','1/0','1/1'); R5_SCRIPT_DELETE=@('0/0','1/0','1/1')
            OWNER_SCRIPT_DELETE=@('0/0','1/0','1/1')
            POST_ACCEPT_ERROR=@('NONE','VERIFY_ZONE_OR_CONVERSION_FAILED','R5_TIMEOUT_TERMINATED_NO_RETRY','R5_FAILED_OR_UNCERTAIN','R5_EXIT_NOT_PROVEN','POST_ACCEPT_OPERATION_UNEXPECTED_FAILURE','REVOCATION_PROMPT_OUTPUT_UNCERTAIN','REVOCATION_INVALIDITY_NOT_PROVEN','REVOCATION_INVALIDITY_NOT_PROVEN_NO_USABLE_TOKEN','ACTIVE_TOKEN_REVOCATION_NOT_PROVEN','REVOCATION_HOLD_FAILED_OR_UNCERTAIN','SAFE_OUTPUT_UNCERTAIN','POST_ACCEPT_UNEXPECTED_FAILURE_AFTER_HOLD')
            SAFE_OUTPUT_UNCERTAIN=@('TRUE','FALSE')
            CLEANUP_ERROR=@('NONE','CLIPBOARD_CLEANUP_FAILED','SCRIPT_CLEANUP_FAILED')
            OWNER_RESULT=@('FAIL_STOP_NO_RETRY','EXACT_CORRECTION_PASS_TOKEN_REVOKED','FAIL_TOKEN_REVOKED_NO_RETRY','FAIL_CLEANUP_NOT_PROVEN_NO_RETRY')
            OWNER_READY=@('PASS'); SECRET_PROMPT_READY=@('PASS'); R5_RESULT=@('PASS','FAIL')
            REVOCATION_REQUIRED=@('PASS'); REVOCATION_AUTHORITY=@('WAITING','GRANTED','DENIED','TIMEOUT')
            INVALID_TOKEN_HTTP=@('401','NOT_PROVEN_NO_USABLE_TOKEN')
            CREDENTIAL_INCIDENT=@('ACTIVE_TOKEN_REVOCATION_NOT_PROVEN')
        }
        foreach ($key in $values.Keys) {
            foreach ($value in $values[$key]) { $map.Add(($key+'='+$value),[pscustomobject]@{Key=$key; Value=$value}) }
        }
        $map.Add('REVOCATION_ROW_NAME=OmniRoute secure console R5 20260901',[pscustomobject]@{Key='REVOCATION_ROW_NAME'; Value='EXPECTED_NAME_REDACTED'})
        $fields = [ordered]@{}
        foreach ($line in $lines) {
            if ($line.Length -gt 160) { return $reject }
            if ($line -cmatch '^OWNER_PID=[0-9]{1,10}$') { $record = [pscustomobject]@{Key='OWNER_PID'; Value='PRESENT_REDACTED'} }
            elseif ($map.ContainsKey($line)) { $record = $map[$line] }
            else { return $reject }
            if ($fields.Contains($record.Key)) { return $reject }
            $fields[$record.Key] = $record.Value
        }
        if (-not $fields.Contains('OWNER_RESULT')) { return $reject }
        return [pscustomobject]@{Grammar='ALLOWLIST_ONLY'; Fields=$fields}
    } catch { return $reject }
    finally { $raw=$null; $lines=$null; $line=$null }
}

$ErrorActionPreference = 'Stop'
$stage = 'RUNTIME_AND_HELPER_PINS'
$bytes = $null
$result = $null
$exitCode = 0
try {
    $runtime = 'C:\Users\chatc\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\powershell\pwsh.exe'
    if (-not [string]::Equals((Join-Path $PSHOME 'pwsh.exe'),$runtime,[StringComparison]::OrdinalIgnoreCase)) { throw 'PIN' }
    $runtimeItem = Get-Item -LiteralPath $runtime -Force
    if ($runtimeItem.Length -ne 301368 -or $runtimeItem.VersionInfo.FileVersion -ne '7.6.5.500' -or
        (Get-FileHash -LiteralPath $runtime -Algorithm SHA256).Hash -ne '362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139') { throw 'PIN' }
    $signature = Get-AuthenticodeSignature -LiteralPath $runtime
    if ($signature.Status -ne 'Valid' -or $signature.SignerCertificate.Subject -cne 'CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US') { throw 'PIN' }
    $helperPath = Join-Path $PSScriptRoot 'V64ExactReader.cs'
    if ((Get-FileHash -LiteralPath $helperPath -Algorithm SHA256).Hash -ne 'EDD25482367C87F5904E18327D88A08AAC2A2ACF0ABD3E431596AD3FF4D4B061') { throw 'PIN' }
    Add-Type -Path $helperPath
    $stage = 'EXACT_PATH_METADATA'
    $parent = 'C:\Users\chatc\AppData\Local\Temp'
    $rootPath = 'C:\Users\chatc\AppData\Local\Temp\omniroute-secure-console-9df5f87e00bc4a36b3133b32f4e095ba'
    $logPath = 'C:\Users\chatc\AppData\Local\Temp\omniroute-secure-console-9df5f87e00bc4a36b3133b32f4e095ba\omniroute-secure-console-safe.log'
    if (-not [string]::Equals([IO.Path]::GetFullPath([IO.Path]::GetTempPath()).TrimEnd('\'),$parent,[StringComparison]::OrdinalIgnoreCase)) { throw 'PIN' }
    foreach ($ancestor in @('C:\','C:\Users','C:\Users\chatc','C:\Users\chatc\AppData','C:\Users\chatc\AppData\Local',$parent)) {
        $item = Get-Item -LiteralPath $ancestor -Force
        if (-not $item.PSIsContainer -or ($item.Attributes -band [IO.FileAttributes]::ReparsePoint)) { throw 'PIN' }
    }
    $root = Get-Item -LiteralPath $rootPath -Force
    if (-not $root.PSIsContainer -or ($root.Attributes -band [IO.FileAttributes]::ReparsePoint) -or
        -not [string]::Equals($root.FullName,$rootPath,[StringComparison]::Ordinal) -or
        $root.CreationTimeUtc.ToString('o') -cne '2026-09-03T14:41:21.7482409Z' -or
        $root.LastWriteTimeUtc.ToString('o') -cne '2026-09-03T14:52:31.0363608Z') { throw 'PIN' }
    $log = Get-Item -LiteralPath $logPath -Force
    if ($log.PSIsContainer -or ($log.Attributes -band [IO.FileAttributes]::ReparsePoint) -or
        -not [string]::Equals($log.FullName,$logPath,[StringComparison]::Ordinal) -or $log.Length -ne 476 -or
        $log.CreationTimeUtc.ToString('o') -cne '2026-09-03T14:42:30.2964752Z' -or
        $log.LastWriteTimeUtc.ToString('o') -cne '2026-09-03T14:52:31.0440727Z') { throw 'PIN' }
    $stage = 'ONE_HANDLE_BOUNDED_READ'
    $bytes = [V64ExactReader]::ReadExact($logPath,$log.CreationTimeUtc.ToFileTimeUtc(),$log.LastWriteTimeUtc.ToFileTimeUtc())
    $stage = 'FIXED_STATUS_PARSE'
    $summary = Get-V64StatusSummary $bytes
    $state = 'V64_CLOSED_STATUS_INSPECTED'
    if ($summary.Grammar -cne 'ALLOWLIST_ONLY') { $state='V64_CLOSED_REDACTED_CONTENT_UNCERTAIN'; $exitCode=2 }
    $result = [ordered]@{
        State=$state; ReadBound='476_BYTES_ONCE'; Grammar=$summary.Grammar
        HistoricalLogStatuses=$summary.Fields; RawOutput='SUPPRESSED'
        LiveProcessOrProviderState='NOT_PROVEN'; HistoricalProvenance='NOT_PROVEN'
        CleanupEligibility='NOT_PROVEN_LEAVE_UNTOUCHED'
    }
} catch {
    $exitCode = 1
    $result = [ordered]@{State='V64_CLOSED_STOP_UNCERTAIN'; Stage=$stage; RawOutput='SUPPRESSED'; NoRetry=$true; CleanupEligibility='NOT_PROVEN_LEAVE_UNTOUCHED'}
} finally {
    if ($null -ne $bytes) { [Array]::Clear($bytes,0,$bytes.Length) }
    $bytes = $null
}
$result | ConvertTo-Json -Depth 6 -Compress
exit $exitCode
