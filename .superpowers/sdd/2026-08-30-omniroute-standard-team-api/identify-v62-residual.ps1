function Select-V62Target {
    param([string]$Parent, [string[]]$Candidates)
    if (@($Candidates).Count -ne 1) { throw 'V62_TARGET_COUNT' }
    $raw = $Candidates[0]
    if (-not [IO.Path]::IsPathFullyQualified($raw)) { throw 'V62_TARGET_RELATIVE' }
    $full = [IO.Path]::GetFullPath($raw)
    if (-not [string]::Equals($raw, $full, [StringComparison]::Ordinal)) { throw 'V62_TARGET_NONCANONICAL' }
    $container = [IO.Path]::GetDirectoryName($full)
    if (-not [string]::Equals($container, $Parent, [StringComparison]::OrdinalIgnoreCase)) { throw 'V62_TARGET_OUTSIDE_PARENT' }
    if ([IO.Path]::GetFileName($full) -cnotmatch '^omniroute-secure-console-[0-9a-f]{32}$') { throw 'V62_TARGET_LEAF' }
    return $full
}

# One reviewed identification attempt only. No file contents or child enumeration.
$ErrorActionPreference = 'Stop'
try {
    $runtime = 'C:\Users\chatc\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\powershell\pwsh.exe'
    if (-not [string]::Equals((Join-Path $PSHOME 'pwsh.exe'), $runtime, [StringComparison]::OrdinalIgnoreCase)) { throw 'RUNTIME_PATH' }
    $runtimeItem = Get-Item -LiteralPath $runtime -Force
    if ($runtimeItem.Length -ne 301368 -or $runtimeItem.VersionInfo.FileVersion -ne '7.6.5.500') { throw 'RUNTIME_IDENTITY' }
    if ((Get-FileHash -LiteralPath $runtime -Algorithm SHA256).Hash -ne '362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139') { throw 'RUNTIME_HASH' }
    $signature = Get-AuthenticodeSignature -LiteralPath $runtime
    if ($signature.Status -ne 'Valid' -or $signature.SignerCertificate.Subject -cne 'CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US') { throw 'RUNTIME_SIGNER' }
    $parent = 'C:\Users\chatc\AppData\Local\Temp'
    if (-not [string]::Equals([IO.Path]::GetFullPath([IO.Path]::GetTempPath()).TrimEnd('\'), $parent, [StringComparison]::OrdinalIgnoreCase)) { throw 'TEMP_PARENT' }
    # Parent ancestry metadata only: do not follow reparse ancestors.
    foreach ($ancestor in @('C:\', 'C:\Users', 'C:\Users\chatc', 'C:\Users\chatc\AppData', 'C:\Users\chatc\AppData\Local', $parent)) {
        $entry = Get-Item -LiteralPath $ancestor -Force
        if (-not $entry.PSIsContainer -or ($entry.Attributes -band [IO.FileAttributes]::ReparsePoint)) { throw 'PARENT_REPARSE_OR_TYPE' }
    }
    $candidates = @([IO.Directory]::GetDirectories($parent, 'omniroute-secure-console-*', [IO.SearchOption]::TopDirectoryOnly))
    # No candidate metadata call, output, or retention before this exact-path bind.
    $target = Select-V62Target $parent $candidates
    $entry = Get-Item -LiteralPath $target -Force
    if (-not $entry.PSIsContainer -or ($entry.Attributes -band [IO.FileAttributes]::ReparsePoint)) { throw 'TARGET_REPARSE_OR_TYPE' }
    if (-not [string]::Equals($entry.FullName, $target, [StringComparison]::Ordinal)) { throw 'TARGET_IDENTITY' }
    [ordered]@{
        State = 'V62_CLOSED_IDENTIFIED_PATH_ONLY'
        InventoryCount = 1
        Target = $target
        IsDirectory = $true
        IsReparsePoint = $false
        CreationTimeUtc = $entry.CreationTimeUtc.ToString('o')
        LastWriteTimeUtc = $entry.LastWriteTimeUtc.ToString('o')
        Contents = 'NOT_INSPECTED'
        Ownership = 'NOT_PROVEN'
        PhysicalIdentity = 'NOT_PROVEN'
        CleanupEligibility = 'NOT_PROVEN'
    } | ConvertTo-Json -Compress
} catch {
    # Never expose exception details or an unvalidated candidate path.
    Write-Output 'V62_CLOSED_STOP_UNCERTAIN NO_RETRY TARGET_NOT_RETAINED'
    exit 1
}
