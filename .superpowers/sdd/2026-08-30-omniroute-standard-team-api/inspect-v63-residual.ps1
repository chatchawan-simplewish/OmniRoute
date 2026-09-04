function Get-V63ChildSummary {
    param([string]$Root, [object[]]$Children)
    $labels = @{
        'omniroute-secure-console-owner.ps1' = 'OWNER_SCRIPT'
        'omniroute-r5-exact.ps1' = 'R5_SCRIPT'
        'omniroute-secure-console-safe.log' = 'SAFE_LOG'
    }
    $known = [Collections.Generic.List[object]]::new()
    $unknown = 0
    $unsafeKnown = 0
    foreach ($child in $Children) {
        if (@($labels.Keys) -cnotcontains $child.Name) { $unknown++; continue }
        $expectedPath = Join-Path $Root $child.Name
        if (-not [string]::Equals($child.FullName, $expectedPath, [StringComparison]::Ordinal) -or
            $child.PSIsContainer -or ($child.Attributes -band [IO.FileAttributes]::ReparsePoint)) {
            $unsafeKnown++; continue
        }
        $known.Add([pscustomobject]@{
            Label = $labels[$child.Name]
            Length = [long]$child.Length
            CreationTimeUtc = $child.CreationTimeUtc.ToString('o')
            LastWriteTimeUtc = $child.LastWriteTimeUtc.ToString('o')
        })
    }
    return [pscustomobject]@{EntryCount=@($Children).Count; UnknownCount=$unknown; UnsafeKnownCount=$unsafeKnown; Known=$known.ToArray()}
}

# Fresh V63 attempt only; no content reads, child ACLs, hashes, or process lookup.
$ErrorActionPreference = 'Stop'
$stage = 'RUNTIME_PINS'
try {
    $runtime = 'C:\Users\chatc\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\powershell\pwsh.exe'
    if (-not [string]::Equals((Join-Path $PSHOME 'pwsh.exe'), $runtime, [StringComparison]::OrdinalIgnoreCase)) { throw 'PIN' }
    $runtimeItem = Get-Item -LiteralPath $runtime -Force
    if ($runtimeItem.Length -ne 301368 -or $runtimeItem.VersionInfo.FileVersion -ne '7.6.5.500' -or
        (Get-FileHash -LiteralPath $runtime -Algorithm SHA256).Hash -ne '362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139') { throw 'PIN' }
    $signature = Get-AuthenticodeSignature -LiteralPath $runtime
    if ($signature.Status -ne 'Valid' -or $signature.SignerCertificate.Subject -cne 'CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US') { throw 'PIN' }
    $stage = 'EXACT_ROOT_METADATA'
    $parent = 'C:\Users\chatc\AppData\Local\Temp'
    $target = 'C:\Users\chatc\AppData\Local\Temp\omniroute-secure-console-9df5f87e00bc4a36b3133b32f4e095ba'
    if (-not [string]::Equals([IO.Path]::GetFullPath([IO.Path]::GetTempPath()).TrimEnd('\'), $parent, [StringComparison]::OrdinalIgnoreCase)) { throw 'PIN' }
    foreach ($ancestor in @('C:\','C:\Users','C:\Users\chatc','C:\Users\chatc\AppData','C:\Users\chatc\AppData\Local',$parent)) {
        $item = Get-Item -LiteralPath $ancestor -Force
        if (-not $item.PSIsContainer -or ($item.Attributes -band [IO.FileAttributes]::ReparsePoint)) { throw 'PIN' }
    }
    $root = Get-Item -LiteralPath $target -Force
    if (-not $root.PSIsContainer -or ($root.Attributes -band [IO.FileAttributes]::ReparsePoint) -or
        -not [string]::Equals($root.FullName,$target,[StringComparison]::Ordinal) -or
        $root.CreationTimeUtc.ToString('o') -cne '2026-09-03T14:41:21.7482409Z' -or
        $root.LastWriteTimeUtc.ToString('o') -cne '2026-09-03T14:52:31.0363608Z') { throw 'PIN' }
    $stage = 'ROOT_OWNER_ONLY'
    $acl = Get-Acl -LiteralPath $target
    $ownerSid = $acl.GetOwner([Security.Principal.SecurityIdentifier]).Value
    $currentSid = [Security.Principal.WindowsIdentity]::GetCurrent().User.Value
    if ($ownerSid -cnotmatch '^S-1-[0-9]+(?:-[0-9]+)+$' -or $currentSid -cnotmatch '^S-1-[0-9]+(?:-[0-9]+)+$') { throw 'PIN' }
    $stage = 'ONE_CHILD_METADATA_ENUMERATION'
    $children = @(Get-ChildItem -LiteralPath $target -Force)
    $summary = Get-V63ChildSummary $target $children
    [ordered]@{
        State = 'V63_CLOSED_METADATA_INSPECTED'
        Target = $target
        DirectoryOwnerSid = $ownerSid
        OwnerMatchesCurrentUser = ($ownerSid -ceq $currentSid)
        ChildMetadata = $summary
        FileContents = 'NOT_READ'
        ScriptIdentity = 'NOT_PROVEN'
        ChildOwnership = 'NOT_PROVEN'
        CreatorOrProcessOwnership = 'NOT_PROVEN'
        PhysicalIdentityContinuity = 'NOT_PROVEN'
        CleanupEligibility = 'NOT_PROVEN_LEAVE_UNTOUCHED'
    } | ConvertTo-Json -Depth 6 -Compress
} catch {
    [ordered]@{State='V63_CLOSED_STOP_UNCERTAIN'; Stage=$stage; NoRetry=$true; CleanupEligibility='NOT_PROVEN_LEAVE_UNTOUCHED'} | ConvertTo-Json -Compress
    exit 1
}
