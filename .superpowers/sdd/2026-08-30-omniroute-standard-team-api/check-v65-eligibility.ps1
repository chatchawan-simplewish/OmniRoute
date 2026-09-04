function Get-V65Eligibility {
    param([bool]$ShapeMatches,[bool]$RootOwnerMatches,[bool]$LogOwnerMatches,[bool]$OriginReferenceAbsent)
    if (-not $ShapeMatches) { return 'REJECT_CURRENT_SHAPE' }
    if (-not $RootOwnerMatches -or -not $LogOwnerMatches) { return 'REJECT_FILESYSTEM_OWNER_MISMATCH' }
    if ($OriginReferenceAbsent) { return 'REJECT_MISSING_AUTHORITATIVE_ORIGIN_BINDING' }
    return 'STOP_NEW_PROVENANCE_REQUIRES_REVIEW'
}

$ErrorActionPreference = 'Stop'
$stage = 'RUNTIME_PINS'
try {
    $runtime = 'C:\Users\chatc\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\powershell\pwsh.exe'
    if (-not [string]::Equals((Join-Path $PSHOME 'pwsh.exe'),$runtime,[StringComparison]::OrdinalIgnoreCase)) { throw 'PIN' }
    $runtimeItem = Get-Item -LiteralPath $runtime -Force
    if ($runtimeItem.Length -ne 301368 -or $runtimeItem.VersionInfo.FileVersion -ne '7.6.5.500' -or
        (Get-FileHash -LiteralPath $runtime -Algorithm SHA256).Hash -ne '362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139') { throw 'PIN' }
    $signature = Get-AuthenticodeSignature -LiteralPath $runtime
    if ($signature.Status -ne 'Valid' -or $signature.SignerCertificate.Subject -cne 'CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US') { throw 'PIN' }
    $stage = 'PINNED_PROVENANCE_SNAPSHOT'
    $env:GIT_NO_REPLACE_OBJECTS = '1'
    git -c core.longpaths=true grep --quiet -F '9df5f87e00bc4a36b3133b32f4e095ba' 893563137ea4f866b00c793831208b139f0404b3 -- .superpowers/sdd/2026-08-30-omniroute-standard-team-api 2>$null
    if ($LASTEXITCODE -notin @(0,1)) { throw 'PIN' }
    $originAbsent = $LASTEXITCODE -eq 1
    $stage = 'CURRENT_EXACT_METADATA'
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
    $stage = 'ONE_CHILD_SHAPE_AND_OWNER_METADATA'
    $children = @(Get-ChildItem -LiteralPath $rootPath -Force)
    $shape = $children.Count -eq 1 -and
        [string]::Equals($children[0].FullName,$logPath,[StringComparison]::Ordinal) -and
        -not $children[0].PSIsContainer -and -not ($children[0].Attributes -band [IO.FileAttributes]::ReparsePoint)
    $expectedSid = 'S-1-5-21-2948832038-1864667924-1544628304-1001'
    $currentSid = [Security.Principal.WindowsIdentity]::GetCurrent().User.Value
    if ($currentSid -cne $expectedSid) { throw 'PIN' }
    $rootSid = (Get-Acl -LiteralPath $rootPath).GetOwner([Security.Principal.SecurityIdentifier]).Value
    $logSid = (Get-Acl -LiteralPath $logPath).GetOwner([Security.Principal.SecurityIdentifier]).Value
    $rootOwner = $rootSid -ceq $expectedSid
    $logOwner = $logSid -ceq $expectedSid
    $decision = Get-V65Eligibility $shape $rootOwner $logOwner $originAbsent
    [ordered]@{
        State='V65_CLOSED_CLEANUP_ELIGIBILITY_REJECTED'; CleanupEligibility='REJECTED_UNDER_V65'
        Decision=$decision; CurrentMetadataPins='PASS'; OnlyExactLogChild=$shape
        RootOwnerMatchesCurrentUser=$rootOwner; LogOwnerMatchesCurrentUser=$logOwner
        PreV62CommittedOriginReferenceAbsent=$originAbsent
        ProvenanceSearchScope='PINNED_PRE_V62_EVIDENCE_SNAPSHOT_ONLY'
        HistoricalOriginAndLifecycleBinding='NOT_ESTABLISHED'
        ProcessChecks='NOT_PERFORMED_ORIGIN_PREREQUISITE_UNMET'; ContentReread='NOT_PERFORMED'
        Disposition='LEAVE_DIRECTORY_AND_LOG_UNTOUCHED'
    } | ConvertTo-Json -Compress
} catch {
    [ordered]@{State='V65_CLOSED_STOP_UNCERTAIN'; Stage=$stage; CleanupEligibility='REJECTED_UNDER_V65'; NoRetry=$true; Disposition='LEAVE_DIRECTORY_AND_LOG_UNTOUCHED'} | ConvertTo-Json -Compress
    exit 1
}
