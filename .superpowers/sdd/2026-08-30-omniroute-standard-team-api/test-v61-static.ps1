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
Assert-V61 ($live.Count -eq 5 -and $scope.Count -eq 3) 'fence_counts'
$expected = @(
    @(8380, 'A7C7F04705344160030C3BF1CA383179616507555F56D2288E3BFD9B46FEF2AC'),
    @(3988, '83440D05C9B2486509D2DC9A51F10C4916FFAFFC1C6B7B6FABCE07188FAE76D5'),
    @(22582, '383E21D339AD67D704F1515F2091D1363809CC23DC61176EE65246012A5E476A'),
    @(675, 'C4DDD2E84C14C125830DD422C613CE9DC4CFCDBCABB760F003B9187811B7D2FA'),
    @(2779, '9316DE2F7C84A89947E57C8563E9381E97D7C52F0DFFE56CA7E4DE616DD8F637'),
    @(2022, 'C34931235DB0BC7AD5CC441D9C6CD1BEF27DA436C902F21023FE2682881F3AA8'),
    @(14846, '80DC8090F28FE6FB949616F8295C1CE14F637E049C69750B5ED8F83EAF83CFF5'),
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
Assert-V61 ($live[0] -ceq $originalLive[0] -and $live[4] -ceq $originalLive[4] -and $scope[2] -ceq $originalScope[2]) 'unchanged_proxy_and_cleanup'
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
[Console]::Out.WriteLine('V61_STATIC=PASS FENCES=8 PARSE_ERRORS=0 UNCHANGED_PROXY_AND_CLEANUP=TRUE GUARD_ORDER=TRUE PRODUCT_HASHES=12/12 LIVE_ACTIONS=0')
