$ErrorActionPreference = 'Stop'
$parseErrors = $null
$ast = [Management.Automation.Language.Parser]::ParseFile((Join-Path $PSScriptRoot 'check-v65-eligibility.ps1'),[ref]$null,[ref]$parseErrors)
if ($parseErrors.Count) { throw 'V65_PARSE_FAILURE' }
$helper = @($ast.FindAll({param($n) $n -is [Management.Automation.Language.FunctionDefinitionAst] -and $n.Name -eq 'Get-V65Eligibility'},$false))
if ($helper.Count -ne 1) { throw 'V65_HELPER_COUNT' }
. ([scriptblock]::Create($helper[0].Extent.Text))
if ((Get-V65Eligibility $true $true $true $true) -cne 'REJECT_MISSING_AUTHORITATIVE_ORIGIN_BINDING') { throw 'V65_MISSING_ORIGIN_ACCEPTED' }
if ((Get-V65Eligibility $false $true $true $true) -cne 'REJECT_CURRENT_SHAPE') { throw 'V65_SHAPE_DRIFT_ACCEPTED' }
if ((Get-V65Eligibility $true $false $true $true) -cne 'REJECT_FILESYSTEM_OWNER_MISMATCH') { throw 'V65_ROOT_OWNER_MISMATCH_ACCEPTED' }
if ((Get-V65Eligibility $true $true $false $true) -cne 'REJECT_FILESYSTEM_OWNER_MISMATCH') { throw 'V65_LOG_OWNER_MISMATCH_ACCEPTED' }
if ((Get-V65Eligibility $true $true $true $false) -cne 'STOP_NEW_PROVENANCE_REQUIRES_REVIEW') { throw 'V65_UNKNOWN_PROVENANCE_AUTOAPPROVED' }
'V65_ELIGIBILITY_TEST=PASS CASES=5 LIVE_TARGET_ACCESS=0'
