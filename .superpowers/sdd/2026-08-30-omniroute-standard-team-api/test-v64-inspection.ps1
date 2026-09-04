$ErrorActionPreference = 'Stop'
$parseErrors = $null
$ast = [Management.Automation.Language.Parser]::ParseFile((Join-Path $PSScriptRoot 'inspect-v64-log.ps1'),[ref]$null,[ref]$parseErrors)
if ($parseErrors.Count) { throw 'V64_PARSE_FAILURE' }
$helper = @($ast.FindAll({param($n) $n -is [Management.Automation.Language.FunctionDefinitionAst] -and $n.Name -eq 'Get-V64StatusSummary'},$false))
if ($helper.Count -ne 1) { throw 'V64_HELPER_COUNT' }
. ([scriptblock]::Create($helper[0].Extent.Text))
function Convert-TestBytes([string]$value) { return [Text.Encoding]::UTF8.GetBytes($value) }
$result = Get-V64StatusSummary (Convert-TestBytes "TOKEN_VERIFY=0/0`nOWNER_RESULT=FAIL_STOP_NO_RETRY`n")
if ($result.Grammar -cne 'ALLOWLIST_ONLY' -or $result.Fields.TOKEN_VERIFY -cne '0/0' -or $result.Fields.OWNER_RESULT -cne 'FAIL_STOP_NO_RETRY') { throw 'V64_ALLOWED_STATUS_NOT_PARSED' }
$result = Get-V64StatusSummary (Convert-TestBytes "OWNER_PID=123456`nOWNER_RESULT=FAIL_STOP_NO_RETRY`n")
if ($result.Fields.OWNER_PID -cne 'PRESENT_REDACTED' -or (($result | ConvertTo-Json -Depth 6) -match '123456')) { throw 'V64_PID_LEAK' }
$bad = @(
    "Bearer SYNTHETIC_PRIVATE_MARKER`nOWNER_RESULT=FAIL_STOP_NO_RETRY`n",
    "OWNER_RESULT=FAIL_STOP_NO_RETRY SYNTHETIC_PRIVATE_MARKER`n",
    "OWNER_RESULT=FAIL_STOP_NO_RETRY`nOWNER_RESULT=FAIL_STOP_NO_RETRY`n",
    "TOKEN_VERIFY=4/9`nOWNER_RESULT=FAIL_STOP_NO_RETRY`n",
    "TOKEN_VERIFY=0/0`n",
    '',
    ('A' * 477),
    "OWNER_RESULT=FAIL_STOP_NO_RETRY`n`n"
)
foreach ($value in $bad) {
    $result = Get-V64StatusSummary (Convert-TestBytes $value)
    if ($result.Grammar -cne 'REJECTED_REDACTED' -or $result.Fields.Count -ne 0 -or (($result | ConvertTo-Json -Depth 6) -match 'SYNTHETIC_PRIVATE_MARKER')) { throw 'V64_UNSAFE_STATUS_EXPOSED' }
}
$result = Get-V64StatusSummary ([byte[]]@(0xc0,0xaf))
if ($result.Grammar -cne 'REJECTED_REDACTED' -or $result.Fields.Count) { throw 'V64_BAD_UTF8_ACCEPTED' }
'V64_PARSER_TESTS=PASS CASES=11'
Add-Type -Path (Join-Path $PSScriptRoot 'V64ExactReader.cs')
$fixture = Get-Item -LiteralPath (Join-Path $PSScriptRoot 'v64-reader-fixture.txt')
if ($fixture.Length -ne 476) { throw 'V64_FIXTURE_SIZE' }
$bytes = [V64ExactReader]::ReadExact($fixture.FullName,$fixture.CreationTimeUtc.ToFileTimeUtc(),$fixture.LastWriteTimeUtc.ToFileTimeUtc())
if ($bytes.Length -ne 476 -or $bytes[0] -ne 65 -or $bytes[475] -ne 10) { throw 'V64_READER_BYTES' }
$rejected = $false
try { $null = [V64ExactReader]::ReadExact($fixture.FullName,0,$fixture.LastWriteTimeUtc.ToFileTimeUtc()) } catch { $rejected = $true }
if (-not $rejected) { throw 'V64_READER_IGNORED_IDENTITY' }
$writer = [IO.File]::Open($fixture.FullName,[IO.FileMode]::Open,[IO.FileAccess]::Write,[IO.FileShare]::ReadWrite)
try {
    $rejected = $false
    try { $null = [V64ExactReader]::ReadExact($fixture.FullName,$fixture.CreationTimeUtc.ToFileTimeUtc(),$fixture.LastWriteTimeUtc.ToFileTimeUtc()) } catch { $rejected = $true }
    if (-not $rejected) { throw 'V64_READER_IGNORED_WRITER' }
} finally { $writer.Dispose() }
[Array]::Clear($bytes,0,$bytes.Length)
'V64_READER_TESTS=PASS CASES=3 LIVE_RESIDUAL_ACCESS=0'
