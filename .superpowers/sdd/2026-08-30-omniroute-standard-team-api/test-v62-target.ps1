$ErrorActionPreference = 'Stop'
# Extract only the pure validator: never execute the live identification body.
$parseErrors = $null
$ast = [Management.Automation.Language.Parser]::ParseFile((Join-Path $PSScriptRoot 'identify-v62-residual.ps1'), [ref]$null, [ref]$parseErrors)
if ($parseErrors.Count) { throw 'V62_PARSE_FAILURE' }
$helper = @($ast.FindAll({ param($node) $node -is [Management.Automation.Language.FunctionDefinitionAst] -and $node.Name -eq 'Select-V62Target' }, $false))
if ($helper.Count -ne 1) { throw 'V62_HELPER_COUNT' }
. ([scriptblock]::Create($helper[0].Extent.Text))
$parent = 'C:\Synthetic\Temp'
$good = 'C:\Synthetic\Temp\omniroute-secure-console-0123456789abcdef0123456789abcdef'
if ((Select-V62Target $parent @($good)) -cne $good) { throw 'DIRECT_TARGET_NOT_ACCEPTED' }
$badCases = @(
    @{ Name='zero'; Paths=@() },
    @{ Name='multiple'; Paths=@($good,$good) },
    @{ Name='outside'; Paths=@('C:\Other\omniroute-secure-console-0123456789abcdef0123456789abcdef') },
    @{ Name='bad_leaf'; Paths=@('C:\Synthetic\Temp\omniroute-secure-console-not-a-guid') },
    @{ Name='nested'; Paths=@('C:\Synthetic\Temp\nested\omniroute-secure-console-0123456789abcdef0123456789abcdef') },
    @{ Name='traversal'; Paths=@('C:\Synthetic\Temp\nested\..\omniroute-secure-console-0123456789abcdef0123456789abcdef') },
    @{ Name='relative'; Paths=@('omniroute-secure-console-0123456789abcdef0123456789abcdef') },
    @{ Name='ads'; Paths=@($good + ':stream') }
)
foreach ($case in $badCases) {
    $rejected = $false
    try { $null = Select-V62Target $parent $case.Paths } catch { $rejected = $true }
    if (-not $rejected) { throw ('ACCEPTED_BAD_TARGET_' + $case.Name) }
}
'V62_PURE_TARGET_TEST=PASS CASES=9 LIVE_INVENTORY=0'
