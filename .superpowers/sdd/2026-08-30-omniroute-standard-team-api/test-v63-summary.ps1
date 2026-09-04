$ErrorActionPreference = 'Stop'
$parseErrors = $null
$ast = [Management.Automation.Language.Parser]::ParseFile((Join-Path $PSScriptRoot 'inspect-v63-residual.ps1'), [ref]$null, [ref]$parseErrors)
if ($parseErrors.Count) { throw 'V63_PARSE_FAILURE' }
$helper = @($ast.FindAll({ param($n) $n -is [Management.Automation.Language.FunctionDefinitionAst] -and $n.Name -eq 'Get-V63ChildSummary' }, $false))
if ($helper.Count -ne 1) { throw 'V63_HELPER_COUNT' }
. ([scriptblock]::Create($helper[0].Extent.Text))
$root = 'C:\Synthetic\Residual'
$stamp = [datetime]::Parse('2026-09-03T14:41:21.7482409Z').ToUniversalTime()
function New-TestEntry([string]$name, [string]$path, [bool]$directory=$false, [IO.FileAttributes]$attributes=[IO.FileAttributes]::Normal) {
    [pscustomobject]@{Name=$name; FullName=$path; PSIsContainer=$directory; Attributes=$attributes; Length=22118; CreationTimeUtc=$stamp; LastWriteTimeUtc=$stamp}
}
$known = New-TestEntry 'omniroute-secure-console-owner.ps1' 'C:\Synthetic\Residual\omniroute-secure-console-owner.ps1'
$summary = Get-V63ChildSummary $root @($known)
if ($summary.Known.Count -ne 1 -or $summary.Known[0].Label -cne 'OWNER_SCRIPT' -or $summary.Known[0].Length -ne 22118 -or $summary.UnknownCount -ne 0) { throw 'V63_KNOWN_NOT_PRESERVED' }
$unknown = New-TestEntry 'PRIVATE_VALUE_DO_NOT_EMIT' 'C:\Synthetic\Residual\PRIVATE_VALUE_DO_NOT_EMIT'
$summary = Get-V63ChildSummary $root @($known,$unknown)
if ($summary.UnknownCount -ne 1 -or (($summary | ConvertTo-Json -Depth 8) -match 'PRIVATE_VALUE')) { throw 'V63_UNKNOWN_NAME_LEAK' }
$summary = Get-V63ChildSummary $root @((New-TestEntry 'omniroute-secure-console-owner.ps1' 'C:\Outside\omniroute-secure-console-owner.ps1'))
if ($summary.UnsafeKnownCount -ne 1 -or $summary.Known.Count -ne 0) { throw 'V63_OUTSIDE_PATH_ACCEPTED' }
$summary = Get-V63ChildSummary $root @((New-TestEntry $known.Name $known.FullName $false ([IO.FileAttributes]::ReparsePoint)))
if ($summary.UnsafeKnownCount -ne 1 -or $summary.Known.Count -ne 0) { throw 'V63_REPARSE_ACCEPTED' }
$summary = Get-V63ChildSummary $root @((New-TestEntry $known.Name $known.FullName $true ([IO.FileAttributes]::Directory)))
if ($summary.UnsafeKnownCount -ne 1 -or $summary.Known.Count -ne 0) { throw 'V63_DIRECTORY_ACCEPTED' }
$summary = Get-V63ChildSummary $root @()
if ($summary.EntryCount -ne 0 -or $summary.Known.Count -ne 0) { throw 'V63_EMPTY_MISCOUNT' }
'V63_PURE_METADATA_TEST=PASS CASES=6 LIVE_TARGET_ACCESS=0'
