$ErrorActionPreference = 'Stop'
$dir = $PSScriptRoot
$utf8 = [Text.UTF8Encoding]::new($false, $true)
function Assert-V61([bool]$condition, [string]$label) {
    if (-not $condition) { throw "V61_STATIC_FAIL=$label" }
}
function Get-V61Fences([string]$name) {
    $raw = [IO.File]::ReadAllText((Join-Path $dir $name), $utf8)
    @([regex]::Matches($raw, '(?ms)^```powershell\n(?<code>.*?)^```$') | ForEach-Object { $_.Groups['code'].Value })
}
$live = @(Get-V61Fences 'task-2-secure-console-transfer-v61-live-source.md')
$scope = @(Get-V61Fences 'task-2-secure-console-transfer-v61-scope-source.md')
$originalLive = @(Get-V61Fences 'task-2-secure-console-transfer-live-brief.md')
$originalScope = @(Get-V61Fences 'task-2-secure-console-transfer-scope-replacement-brief.md')
Assert-V61 ($live.Count -eq 5 -and $scope.Count -eq 4) 'fence_counts'
Assert-V61 ($live[0].Contains("`$rollback = @'`nset -eu") -and $live[0].Contains('sudo docker rm -f "$expected" >/dev/null')) 'rollback_immutable_id'
Assert-V61 ($scope[0].Contains('test "$id" = "$expected"') -and $scope[0].Contains('sudo docker rm -f "$expected" >/dev/null')) 'cleanup_immutable_id'
$expected = @(
    @(8378, '75725F1BAD87DD1C1EF0A3BC8E5B34FF2B290F6F107F55440E69682B725E0E67'),
    @(4144, '1BF3A613363B755BC15F35560FC1738D597CAFEFD41159DBC0B2CE1727F80C1C'),
    @(22582, '383E21D339AD67D704F1515F2091D1363809CC23DC61176EE65246012A5E476A'),
    @(675, 'C4DDD2E84C14C125830DD422C613CE9DC4CFCDBCABB760F003B9187811B7D2FA'),
    @(2779, '9316DE2F7C84A89947E57C8563E9381E97D7C52F0DFFE56CA7E4DE616DD8F637'),
    @(12727, 'A6B05C135B95DF685EA4518BAF5298BE6C528AA7C48F1143918B20D3220AAD61'),
    @(2975, '3C2BF4B1B0BE81F8B58B2C7B583A819D8237FC70E519494EAD6018FC36F2C0A0'),
    @(3178, 'AFA0E0389E8F0E0224849B772428B0CA95232C0150255577E5BC22526EC0BA7A'),
    @(3308, 'B8087F2CB77A695C1B6DD145DDD3D39D48F8AABEBBA00863BEA0610C8BE6518E')
)
$all = @($live) + @($scope)
for ($i = 0; $i -lt $all.Count; $i++) {
    $bytes = $utf8.GetBytes($all[$i])
    $hash = ([BitConverter]::ToString([Security.Cryptography.SHA256]::Create().ComputeHash($bytes))).Replace('-', '')
    Assert-V61 ($bytes.Length -eq $expected[$i][0] -and $hash -ceq $expected[$i][1]) "fence_${i}_pin"
    Assert-V61 (-not $all[$i].Contains("`r") -and $all[$i].EndsWith("`n") -and -not $all[$i].EndsWith("`n`n")) "fence_${i}_shape"
    $tokens = $null; $errors = $null
    $null = [Management.Automation.Language.Parser]::ParseInput($all[$i], [ref]$tokens, [ref]$errors)
    Assert-V61 (@($errors).Count -eq 0) "fence_${i}_parse"
}
Assert-V61 ($live[4] -ceq $originalLive[4] -and $scope[3] -ceq $originalScope[2]) 'unchanged_final_disposition'
Assert-V61 ($scope[0].Contains('function Remove-ExactScopePreparedFiles') -and -not $scope[0].Contains('. ([scriptblock]::Create') -and $scope[1].Contains('V61_PREPARATION_FAILED_NO_RETRY')) 'preload_before_preparation'
Assert-V61 (($all -join '').IndexOf('347FCD60A41DF780CE4A94E4FC14C87E5059112068C689EF73636ABC5B0F0B6C') -eq -1) 'no_old_owner_hash'
Assert-V61 (($all -join '').IndexOf('DB6DD81183FE57D22E03B911EC9A30A2FD7C40542E97743615355A6FB44F458F') -eq -1) 'no_old_runtime_hash'
$readyGuard = $live[2].IndexOf("throw 'OWNER_PWSH_ACTION_TIME_PIN_DRIFT'", [StringComparison]::Ordinal)
$readyMarker = $live[2].IndexOf("Write-Safe 'OWNER_READY=PASS'", [StringComparison]::Ordinal)
$r5Guard = $live[2].IndexOf("throw 'R5_PWSH_ACTION_TIME_PIN_DRIFT'", [StringComparison]::Ordinal)
$r5Start = $live[2].IndexOf('$r5Process.Start()', [StringComparison]::Ordinal)
Assert-V61 ($readyGuard -gt 0 -and $readyGuard -lt $readyMarker -and $r5Guard -gt $readyMarker -and $r5Guard -lt $r5Start) 'guard_order'
$manifest = @(Get-Content -LiteralPath (Join-Path $dir 'task-2-secure-console-transfer-v61-product-baseline.json') -Raw | ConvertFrom-Json)
Assert-V61 ($manifest.Count -eq 12) 'product_count'
foreach ($entry in $manifest) {
    Assert-V61 ((Get-FileHash -LiteralPath $entry.Path).Hash -ceq $entry.Hash) 'product_hash'
}
$parseTokens = $null; $parseErrors = $null
$setupAst = [Management.Automation.Language.Parser]::ParseInput($scope[0], [ref]$parseTokens, [ref]$parseErrors)
$cleanupDefinition = $setupAst.Find({ param($a) $a -is [Management.Automation.Language.FunctionDefinitionAst] -and $a.Name -eq 'Remove-ExactScopePreparedFiles' }, $true).Extent.Text
& {
    param($definition)
    $scopePreparationRootCreateAttempted = 1
    $scopePreparationRootCreateFulfilled = 1
    $transferRoot = [IO.Path]::GetFullPath((Join-Path ([IO.Path]::GetTempPath()) 'omniroute-secure-console-00000000000000000000000000000061'))
    $fixture = @{ Children = @(); Removed = [Collections.Generic.List[string]]::new(); BadHash = $false }
    function Get-Item { param($LiteralPath) [pscustomobject]@{ Attributes = [IO.FileAttributes]::Directory } }
    function Get-ChildItem { param($LiteralPath, [switch]$Force) $fixture.Children }
    function Get-FileHash { param($Algorithm, $LiteralPath)
        [pscustomobject]@{ Hash = if ($fixture.BadHash) { 'MISMATCH' } else { '383E21D339AD67D704F1515F2091D1363809CC23DC61176EE65246012A5E476A' } }
    }
    function Remove-Item { param($LiteralPath, [switch]$Force)
        $fixture.Removed.Add($LiteralPath)
        $fixture.Children = @($fixture.Children | Where-Object { $_.FullName -cne $LiteralPath })
    }
    . ([scriptblock]::Create($definition))
    Remove-ExactScopePreparedFiles
    Assert-V61 ($fixture.Removed.Count -eq 1) 'mock_empty_root_cleanup'
    $owner = [pscustomobject]@{Name='omniroute-secure-console-owner.ps1';FullName=(Join-Path $transferRoot 'omniroute-secure-console-owner.ps1');PSIsContainer=$false;Attributes=[IO.FileAttributes]::Normal}
    $fixture.Children = @($owner); $fixture.Removed.Clear()
    Remove-ExactScopePreparedFiles
    Assert-V61 ($fixture.Removed.Count -eq 2) 'mock_partial_owner_cleanup'
    $fixture.Children = @($owner); $fixture.Removed.Clear(); $fixture.BadHash = $true
    $failed = $false
    try { Remove-ExactScopePreparedFiles } catch { $failed = $true }
    Assert-V61 ($failed -and $fixture.Removed.Count -eq 0) 'mock_bad_hash_retained'
    $fixture.BadHash = $false; $scopePreparationRootCreateFulfilled = 0; $failed = $false
    try { Remove-ExactScopePreparedFiles } catch { $failed = $true }
    Assert-V61 ($failed -and $fixture.Removed.Count -eq 0) 'mock_uncertain_root_retained'
    $scopePreparationRootCreateAttempted = 0
    Remove-ExactScopePreparedFiles
    Assert-V61 ($fixture.Removed.Count -eq 0) 'mock_uncreated_root_untouched'
} $cleanupDefinition
[Console]::Out.WriteLine('V61_STATIC=PASS FENCES=9 PARSE_ERRORS=0 IMMUTABLE_PROXY_ID=TRUE PRELOAD=TRUE MOCK_PARTIAL_CLEANUP=5/5 GUARD_ORDER=TRUE PRODUCT_HASHES=12/12 LIVE_ACTIONS=0')
