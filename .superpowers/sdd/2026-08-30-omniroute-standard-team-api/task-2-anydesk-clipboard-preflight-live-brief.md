# Task 2 AnyDesk / Chrome / Windows clipboard transport-preflight live brief

Status: prepared for fresh independent direct-byte review only; no preflight or live execution is authorized

## Authority and fixed boundary

The sole authority is the latest `Fix round 2 scoped re-review` PASS in
`task-2-secure-console-transfer-sol-review.md` at commit
`d22c0250558ac92b9b4fdc0606e2e1003899698f`. The authoritative design is
`task-2-secure-console-transfer-design.md`, `19,055` bytes, SHA-256
`39254F4AE68A9AC9F856BEB4E8C2CE0CCE771263E5496A5E23A90B6BD6C4901F`.
That PASS authorizes preparation and independent review of this brief only.

This brief is credential-free. It authorizes no process start, browser or
clipboard action, AnyDesk action, Cloudflare or OmniRoute action, VM1205
access, token creation, evidence mutation, proxy/proof/R5 action, Rulesets
action, revocation, retry, fallback, alternate bridge, or permission change.
Execution remains blocked until a fresh independent Sol High direct-byte
review explicitly passes this exact brief and exact extracted script bytes,
followed by separate action-time preflight authority in the sole owner task.

A future observed `PREFLIGHT=PASS` proves only that one fresh non-secret
challenge crossed the observed local data-page -> semantic Chrome focus ->
`Control+A` -> `Control+C` -> AnyDesk/Windows clipboard -> fixed PowerShell 7
path at that time. It cannot prove the semantics of Cloudflare's native Copy
control and authorizes no token, credential, or other live action.

## Exact script-byte contract

- Reviewed filename: `omniroute-transport-preflight.ps1`.
- The exact script bytes are the complete contents of the single fenced
  `powershell` block below, beginning with `param(` and ending with the LF after
  `exit $exitCode`; the fence markers and surrounding Markdown are excluded.
- Encoding is strict UTF-8 without BOM, LF-only, with exactly one trailing LF.
- Exact extracted byte size: `12,839`.
- Exact extracted SHA-256: `2DC4024A95E916FFA1DE38DBD31F878F4593AEFFF50B393AD02E4177C6FEF1B6`.
- The challenge is exactly 128 bits (`16` bytes), freshly filled at runtime by
  the .NET `RandomNumberGenerator`; no static or reused challenge is permitted.
- The script is credential-free and emits only fixed non-secret labels,
  numeric counters, its PID, and the fresh non-secret challenge.

```powershell
param(
    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string]$ExpectedTempRoot,

    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string]$ExpectedScriptPath,

    [Parameter(Mandatory)]
    [ValidatePattern('^[0-9A-F]{8}:[0-9A-F]{8}:[0-9A-F]{8}$')]
    [string]$ExpectedTempRootIdentity,

    [Parameter(Mandatory)]
    [ValidatePattern('^[0-9A-F]{8}:[0-9A-F]{8}:[0-9A-F]{8}$')]
    [string]$ExpectedScriptIdentity,

    [Parameter(Mandatory)]
    [ValidatePattern('^[0-9A-F]{64}$')]
    [string]$ExpectedScriptSha256,

    [Parameter(Mandatory)]
    [ValidateRange(1, 1048576)]
    [long]$ExpectedScriptBytes,

    [ValidateRange(1, 900)]
    [int]$ControlTimeoutSeconds = 120
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$reviewedLeaf = 'omniroute-transport-preflight.ps1'
$exitCode = 1
$terminalEmitted = $false
$cleanupOk = $true
$tempRoot = $null
$scriptPath = $null
$challengeBytes = $null
$challenge = $null
$baseline = $null
$observed = $null
$postClear = $null
$controlCts = $null
$readTask = $null
$controlClock = $null
$controlLine = $null
$baselineWrites = 0
$baselineReads = 0
$comparisonReads = 0
$finalWrites = 0
$postClearReads = 0

try {
    Add-Type -TypeDefinition @'
using System;
using System.ComponentModel;
using System.Runtime.InteropServices;
using Microsoft.Win32.SafeHandles;

public static class OmniRoutePreflightFileIdentity
{
    private const uint ShareRead = 0x00000001;
    private const uint ShareWrite = 0x00000002;
    private const uint ShareDelete = 0x00000004;
    private const uint OpenExisting = 3;
    private const uint BackupSemantics = 0x02000000;
    private const uint OpenReparsePoint = 0x00200000;
    private const uint DirectoryAttribute = 0x00000010;
    private const uint ReparseAttribute = 0x00000400;

    [StructLayout(LayoutKind.Sequential)]
    private struct ByHandleFileInformation
    {
        public uint FileAttributes;
        public System.Runtime.InteropServices.ComTypes.FILETIME CreationTime;
        public System.Runtime.InteropServices.ComTypes.FILETIME LastAccessTime;
        public System.Runtime.InteropServices.ComTypes.FILETIME LastWriteTime;
        public uint VolumeSerialNumber;
        public uint FileSizeHigh;
        public uint FileSizeLow;
        public uint NumberOfLinks;
        public uint FileIndexHigh;
        public uint FileIndexLow;
    }

    [DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
    private static extern SafeFileHandle CreateFileW(
        string fileName,
        uint desiredAccess,
        uint shareMode,
        IntPtr securityAttributes,
        uint creationDisposition,
        uint flagsAndAttributes,
        IntPtr templateFile);

    [DllImport("kernel32.dll", SetLastError = true)]
    private static extern bool GetFileInformationByHandle(
        SafeFileHandle file,
        out ByHandleFileInformation information);

    public static string GetOrdinaryIdentity(string path, bool requireDirectory)
    {
        using (SafeFileHandle handle = CreateFileW(
            path,
            0,
            ShareRead | ShareWrite | ShareDelete,
            IntPtr.Zero,
            OpenExisting,
            BackupSemantics | OpenReparsePoint,
            IntPtr.Zero))
        {
            if (handle.IsInvalid)
                throw new Win32Exception(Marshal.GetLastWin32Error());

            ByHandleFileInformation information;
            if (!GetFileInformationByHandle(handle, out information))
                throw new Win32Exception(Marshal.GetLastWin32Error());
            if ((information.FileAttributes & ReparseAttribute) != 0)
                throw new InvalidOperationException("REPARSE_POINT_REJECTED");

            bool isDirectory = (information.FileAttributes & DirectoryAttribute) != 0;
            if (isDirectory != requireDirectory)
                throw new InvalidOperationException("OBJECT_KIND_REJECTED");

            return string.Format(
                "{0:X8}:{1:X8}:{2:X8}",
                information.VolumeSerialNumber,
                information.FileIndexHigh,
                information.FileIndexLow);
        }
    }
}
'@ -ErrorAction Stop

    $tempBase = [IO.Path]::GetFullPath([IO.Path]::GetTempPath()).TrimEnd([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
    $tempRoot = [IO.Path]::GetFullPath($ExpectedTempRoot).TrimEnd([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
    $scriptPath = [IO.Path]::GetFullPath($ExpectedScriptPath)
    $actualCommandPath = [IO.Path]::GetFullPath($PSCommandPath)
    $pathComparer = [StringComparer]::OrdinalIgnoreCase

    if (-not $pathComparer.Equals([IO.Path]::GetDirectoryName($tempRoot), $tempBase)) {
        throw 'TEMP_ROOT_NOT_DIRECT_CHILD'
    }
    if ([IO.Path]::GetFileName($tempRoot) -cnotmatch '^omniroute-transport-preflight-[0-9a-f]{32}$') {
        throw 'TEMP_ROOT_NAME_REJECTED'
    }
    if (-not [IO.Directory]::Exists($tempRoot)) {
        throw 'TEMP_ROOT_ABSENT'
    }
    if (-not $pathComparer.Equals([IO.Path]::GetDirectoryName($scriptPath), $tempRoot)) {
        throw 'SCRIPT_NOT_DIRECT_CHILD'
    }
    if ([IO.Path]::GetFileName($scriptPath) -cne $reviewedLeaf) {
        throw 'SCRIPT_LEAF_REJECTED'
    }
    if (-not $pathComparer.Equals($actualCommandPath, $scriptPath)) {
        throw 'COMMAND_PATH_MISMATCH'
    }
    if (-not [IO.File]::Exists($scriptPath)) {
        throw 'SCRIPT_ABSENT'
    }
    $actualTempRootIdentity = [OmniRoutePreflightFileIdentity]::GetOrdinaryIdentity($tempRoot, $true)
    $actualScriptIdentity = [OmniRoutePreflightFileIdentity]::GetOrdinaryIdentity($scriptPath, $false)
    if ($actualTempRootIdentity -cne $ExpectedTempRootIdentity -or $actualScriptIdentity -cne $ExpectedScriptIdentity) {
        throw 'START_IDENTITY_DRIFT'
    }

    "OWNER_PID=$PID"

    $baselineWrites++
    Set-Clipboard -Value $null -ErrorAction Stop
    'BASELINE_CLEAR=PASS'

    $baselineReads++
    $baseline = Get-Clipboard -Raw -ErrorAction Stop
    if ($null -ne $baseline -and (-not ($baseline -is [string]) -or $baseline.Length -ne 0)) {
        throw 'BASELINE_NOT_EMPTY'
    }
    'BASELINE_EMPTY=PASS'
    $baseline = $null

    $challengeBytes = [byte[]]::new(16)
    [Security.Cryptography.RandomNumberGenerator]::Fill($challengeBytes)
    $challenge = [Convert]::ToHexString($challengeBytes)
    "CHALLENGE=$challenge"
    'OWNER_READY=PASS'

    $controlCts = [Threading.CancellationTokenSource]::new()
    $readTask = [Console]::In.ReadLineAsync($controlCts.Token)
    $controlClock = [Diagnostics.Stopwatch]::StartNew()
    $controlDeadline = [TimeSpan]::FromSeconds($ControlTimeoutSeconds)

    while (-not $readTask.IsCompleted -and $controlClock.Elapsed -lt $controlDeadline) {
        [Threading.Thread]::Sleep(25)
    }

    $deadlineReached = $controlClock.Elapsed -ge $controlDeadline
    if ($deadlineReached) {
        $controlCts.Cancel()
        try {
            $null = $readTask.GetAwaiter().GetResult()
        } catch {
        }
        'PREFLIGHT=TIMEOUT'
        $terminalEmitted = $true
        $exitCode = 2
    } else {
        $controlLine = $readTask.GetAwaiter().GetResult()
        if ($null -eq $controlLine) {
            'PREFLIGHT=EOF'
            $terminalEmitted = $true
            $exitCode = 2
        } elseif ($controlLine -ceq 'COPY_DONE') {
            $comparisonReads++
            $observed = Get-Clipboard -Raw -ErrorAction Stop
            if ($observed -is [string] -and $observed -ceq $challenge) {
                'PREFLIGHT=PASS'
                $exitCode = 0
            } else {
                'PREFLIGHT=FAIL'
                $exitCode = 1
            }
            $terminalEmitted = $true
            $observed = $null
        } else {
            'PREFLIGHT=ABORTED'
            $terminalEmitted = $true
            $exitCode = 2
        }
    }
} catch {
    if (-not $terminalEmitted) {
        'PREFLIGHT=FAIL'
        $terminalEmitted = $true
    }
    $exitCode = 1
} finally {
    if ($null -ne $controlClock) {
        $controlClock.Stop()
    }
    if ($null -ne $readTask -and -not $readTask.IsCompleted) {
        $controlCts.Cancel()
        try {
            $null = $readTask.GetAwaiter().GetResult()
        } catch {
        }
    }
    if ($null -ne $controlCts) {
        $controlCts.Dispose()
    }

    try {
        $finalWrites++
        Set-Clipboard -Value $null -ErrorAction Stop
        'CLEANUP_CLIPBOARD_CLEAR=PASS'
    } catch {
        'CLEANUP_CLIPBOARD_CLEAR=FAIL'
        $cleanupOk = $false
        $exitCode = 1
    }

    try {
        $postClearReads++
        $postClear = Get-Clipboard -Raw -ErrorAction Stop
        if ($null -ne $postClear -and (-not ($postClear -is [string]) -or $postClear.Length -ne 0)) {
            throw 'POST_CLEAR_NOT_EMPTY'
        }
        'CLEANUP_CLIPBOARD_EMPTY=PASS'
    } catch {
        'CLEANUP_CLIPBOARD_EMPTY=FAIL'
        $cleanupOk = $false
        $exitCode = 1
    }

    $baseline = $null
    $observed = $null
    $postClear = $null
    $controlLine = $null
    $challenge = $null
    if ($null -ne $challengeBytes) {
        [Array]::Clear($challengeBytes, 0, $challengeBytes.Length)
    }
    $challengeBytes = $null

    $deleteGuard = $false
    $deleteSucceeded = $false
    try {
        if ($null -eq $tempRoot -or $null -eq $scriptPath) {
            throw 'DELETE_PATH_UNAVAILABLE'
        }
        $tempBaseForDelete = [IO.Path]::GetFullPath([IO.Path]::GetTempPath()).TrimEnd([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
        $tempRootForDelete = [IO.Path]::GetFullPath($tempRoot).TrimEnd([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
        $scriptPathForDelete = [IO.Path]::GetFullPath($scriptPath)
        $pathComparerForDelete = [StringComparer]::OrdinalIgnoreCase
        if (-not $pathComparerForDelete.Equals([IO.Path]::GetDirectoryName($tempRootForDelete), $tempBaseForDelete)) {
            throw 'DELETE_ROOT_REJECTED'
        }
        if ([IO.Path]::GetFileName($tempRootForDelete) -cnotmatch '^omniroute-transport-preflight-[0-9a-f]{32}$') {
            throw 'DELETE_ROOT_NAME_REJECTED'
        }
        if (-not $pathComparerForDelete.Equals([IO.Path]::GetDirectoryName($scriptPathForDelete), $tempRootForDelete)) {
            throw 'DELETE_SCRIPT_NOT_DIRECT_CHILD'
        }
        if ([IO.Path]::GetFileName($scriptPathForDelete) -cne $reviewedLeaf) {
            throw 'DELETE_SCRIPT_LEAF_REJECTED'
        }
        if (-not $pathComparerForDelete.Equals([IO.Path]::GetFullPath($PSCommandPath), $scriptPathForDelete)) {
            throw 'DELETE_COMMAND_PATH_MISMATCH'
        }
        $rootIdentityBeforeHash = [OmniRoutePreflightFileIdentity]::GetOrdinaryIdentity($tempRootForDelete, $true)
        $scriptIdentityBeforeHash = [OmniRoutePreflightFileIdentity]::GetOrdinaryIdentity($scriptPathForDelete, $false)
        if ($rootIdentityBeforeHash -cne $ExpectedTempRootIdentity -or $scriptIdentityBeforeHash -cne $ExpectedScriptIdentity) {
            throw 'DELETE_IDENTITY_DRIFT_BEFORE_HASH'
        }
        $scriptBytes = [IO.File]::ReadAllBytes($scriptPathForDelete)
        $actualScriptBytes = [long]$scriptBytes.LongLength
        $actualScriptSha256 = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($scriptBytes))
        [Array]::Clear($scriptBytes, 0, $scriptBytes.Length)
        $scriptBytes = $null
        if ($actualScriptBytes -ne $ExpectedScriptBytes -or $actualScriptSha256 -cne $ExpectedScriptSha256) {
            throw 'DELETE_HASH_OR_SIZE_MISMATCH'
        }
        $rootIdentityImmediatelyBeforeDelete = [OmniRoutePreflightFileIdentity]::GetOrdinaryIdentity($tempRootForDelete, $true)
        $scriptIdentityImmediatelyBeforeDelete = [OmniRoutePreflightFileIdentity]::GetOrdinaryIdentity($scriptPathForDelete, $false)
        if ($rootIdentityImmediatelyBeforeDelete -cne $ExpectedTempRootIdentity -or $scriptIdentityImmediatelyBeforeDelete -cne $ExpectedScriptIdentity) {
            throw 'DELETE_IDENTITY_DRIFT'
        }
        $deleteGuard = $true
        Remove-Item -LiteralPath $scriptPathForDelete -Force -ErrorAction Stop
        $deleteSucceeded = -not [IO.File]::Exists($scriptPathForDelete)
    } catch {
        $cleanupOk = $false
        $exitCode = 1
    }

    if ($deleteGuard) { 'SCRIPT_DELETE_GUARD=PASS' } else { 'SCRIPT_DELETE_GUARD=FAIL' }
    if ($deleteSucceeded) { 'SCRIPT_DELETE=PASS' } else { 'SCRIPT_DELETE=FAIL' }
    "COUNTER_BASELINE_WRITES=$baselineWrites"
    "COUNTER_BASELINE_READS=$baselineReads"
    "COUNTER_COMPARISON_READS=$comparisonReads"
    "COUNTER_FINAL_WRITES=$finalWrites"
    "COUNTER_POST_CLEAR_READS=$postClearReads"
    if ($cleanupOk) { 'CLEANUP=PASS' } else { 'CLEANUP=FAIL' }
}

exit $exitCode
```

## Exact coordinator state machine

The following is one complete PowerShell 7 coordinator program. It is invoked
only by the later sole-owner execution task with the exact full commit and
SHA-256 copied from the fresh PASS review plus three host-provided browser
adapters. The adapters are authority-constrained: `OpenExactPage` opens only
the supplied local `data:` URL and returns its opaque page handle;
`PerformExactCopy` uses that handle for one semantic focus by the exact
accessible name, one `Control+A`, and one `Control+C`, then returns only
`COPY_DONE` or throws; `CloseExactPage` closes only that opaque handle and
returns only `PASS` or throws. They may not inspect, serialize, snapshot,
screenshot, extract, use coordinates, use a browser clipboard API, retry, or
touch another page. The coordinator retains the handle; no title/URL lookup is
permitted for closure. `OpenExactPage` is atomic: it returns the handle for
every page it creates and must create no page when it throws. Every adapter has
a host-enforced deadline below the fixed process's 120-second deadline and must
return or throw within that bound.

```powershell
param(
    [Parameter(Mandatory)]
    [ValidatePattern('^[0-9a-f]{40}$')]
    [string]$ReviewedBriefCommit,

    [Parameter(Mandatory)]
    [ValidatePattern('^[0-9A-F]{64}$')]
    [string]$ReviewedBriefSha256,

    [Parameter(Mandatory)]
    [scriptblock]$OpenExactPage,

    [Parameter(Mandatory)]
    [scriptblock]$PerformExactCopy,

    [Parameter(Mandatory)]
    [scriptblock]$CloseExactPage
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Read-ChildLineBeforeDeadline {
    param(
        [Parameter(Mandatory)] [IO.TextReader]$Reader,
        [Parameter(Mandatory)] [Diagnostics.Process]$Process,
        [Parameter(Mandatory)] [Diagnostics.Stopwatch]$Clock,
        [Parameter(Mandatory)] [TimeSpan]$Deadline
    )

    $readCts = [Threading.CancellationTokenSource]::new()
    $lineTask = $null
    try {
        $lineTask = $Reader.ReadLineAsync($readCts.Token)
        while (-not $lineTask.IsCompleted -and $Clock.Elapsed -lt $Deadline) {
            if ($Process.HasExited) {
                $readCts.Cancel()
                try { $null = $lineTask.GetAwaiter().GetResult() } catch {}
                throw 'CHILD_EXIT_DURING_STARTUP'
            }
            [Threading.Thread]::Sleep(25)
        }
        if ($Clock.Elapsed -ge $Deadline) {
            $readCts.Cancel()
            try { $null = $lineTask.GetAwaiter().GetResult() } catch [OperationCanceledException] {}
            throw 'STARTUP_READ_TIMEOUT'
        }
        if (-not $lineTask.IsCompleted) {
            $readCts.Cancel()
            try { $null = $lineTask.GetAwaiter().GetResult() } catch {}
            throw 'STARTUP_READ_INCOMPLETE'
        }
        $line = $lineTask.GetAwaiter().GetResult()
        if ($null -eq $line) { throw 'STARTUP_EOF' }
        return $line
    } finally {
        if ($null -ne $lineTask -and -not $lineTask.IsCompleted) {
            $readCts.Cancel()
            try { $null = $lineTask.GetAwaiter().GetResult() } catch {}
        }
        $readCts.Dispose()
    }
}

Add-Type -TypeDefinition @'
using System;
using System.ComponentModel;
using System.Runtime.InteropServices;
using Microsoft.Win32.SafeHandles;

public static class OmniRoutePreflightFileIdentity
{
    private const uint ShareRead = 0x00000001;
    private const uint ShareWrite = 0x00000002;
    private const uint ShareDelete = 0x00000004;
    private const uint OpenExisting = 3;
    private const uint BackupSemantics = 0x02000000;
    private const uint OpenReparsePoint = 0x00200000;
    private const uint DirectoryAttribute = 0x00000010;
    private const uint ReparseAttribute = 0x00000400;

    [StructLayout(LayoutKind.Sequential)]
    private struct ByHandleFileInformation
    {
        public uint FileAttributes;
        public System.Runtime.InteropServices.ComTypes.FILETIME CreationTime;
        public System.Runtime.InteropServices.ComTypes.FILETIME LastAccessTime;
        public System.Runtime.InteropServices.ComTypes.FILETIME LastWriteTime;
        public uint VolumeSerialNumber;
        public uint FileSizeHigh;
        public uint FileSizeLow;
        public uint NumberOfLinks;
        public uint FileIndexHigh;
        public uint FileIndexLow;
    }

    [DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
    private static extern SafeFileHandle CreateFileW(
        string fileName,
        uint desiredAccess,
        uint shareMode,
        IntPtr securityAttributes,
        uint creationDisposition,
        uint flagsAndAttributes,
        IntPtr templateFile);

    [DllImport("kernel32.dll", SetLastError = true)]
    private static extern bool GetFileInformationByHandle(
        SafeFileHandle file,
        out ByHandleFileInformation information);

    public static string GetOrdinaryIdentity(string path, bool requireDirectory)
    {
        using (SafeFileHandle handle = CreateFileW(
            path,
            0,
            ShareRead | ShareWrite | ShareDelete,
            IntPtr.Zero,
            OpenExisting,
            BackupSemantics | OpenReparsePoint,
            IntPtr.Zero))
        {
            if (handle.IsInvalid)
                throw new Win32Exception(Marshal.GetLastWin32Error());

            ByHandleFileInformation information;
            if (!GetFileInformationByHandle(handle, out information))
                throw new Win32Exception(Marshal.GetLastWin32Error());
            if ((information.FileAttributes & ReparseAttribute) != 0)
                throw new InvalidOperationException("REPARSE_POINT_REJECTED");

            bool isDirectory = (information.FileAttributes & DirectoryAttribute) != 0;
            if (isDirectory != requireDirectory)
                throw new InvalidOperationException("OBJECT_KIND_REJECTED");

            return string.Format(
                "{0:X8}:{1:X8}:{2:X8}",
                information.VolumeSerialNumber,
                information.FileIndexHigh,
                information.FileIndexLow);
        }
    }
}
'@ -ErrorAction Stop

$cancelableReadLineOverloads = @([Console]::In.GetType().GetMethods() | Where-Object {
    $_.Name -eq 'ReadLineAsync' -and
    $_.GetParameters().Count -eq 1 -and
    $_.GetParameters()[0].ParameterType -eq [Threading.CancellationToken]
})
if ($PSVersionTable.PSVersion.Major -ne 7 -or $cancelableReadLineOverloads.Count -ne 1) { throw 'POWERSHELL_RUNTIME_CAPABILITY_FAIL' }

$briefRelativePath = '.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-anydesk-clipboard-preflight-live-brief.md'
$briefPath = 'C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-agent-routing-source\.superpowers\sdd\2026-08-30-omniroute-standard-team-api\task-2-anydesk-clipboard-preflight-live-brief.md'
$repoRoot = 'C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-agent-routing-source'
$reviewedScriptBytes = 12839
$reviewedScriptSha256 = '2DC4024A95E916FFA1DE38DBD31F878F4593AEFFF50B393AD02E4177C6FEF1B6'
$reviewedScriptLeaf = 'omniroute-transport-preflight.ps1'
$controlTimeoutSeconds = 120
$startupTimeoutSeconds = 15
$exitTimeoutMilliseconds = 15000
$utf8NoBom = [Text.UTF8Encoding]::new($false, $true)

$briefRaw = [IO.File]::ReadAllBytes($briefPath)
$observedBriefSha256 = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($briefRaw))
if ($observedBriefSha256 -cne $ReviewedBriefSha256) { throw 'REVIEWED_BRIEF_SHA256_FAIL' }
$workingBriefBlob = (& git -C $repoRoot hash-object --no-filters -- $briefRelativePath).Trim()
if ($LASTEXITCODE -ne 0 -or $workingBriefBlob -cnotmatch '^[0-9a-f]{40}$') { throw 'WORKING_BRIEF_BLOB_FAIL' }
$reviewedBriefBlob = (& git -C $repoRoot rev-parse ($ReviewedBriefCommit + ':' + $briefRelativePath)).Trim()
if ($LASTEXITCODE -ne 0 -or $reviewedBriefBlob -cnotmatch '^[0-9a-f]{40}$') { throw 'REVIEWED_BRIEF_COMMIT_FAIL' }
if ($workingBriefBlob -cne $reviewedBriefBlob) { throw 'REVIEWED_BRIEF_COMMIT_WORKING_DRIFT' }

$briefText = $utf8NoBom.GetString($briefRaw)
if ($briefText.Contains("`r") -or -not $briefText.EndsWith("`n") -or $briefText.EndsWith("`n`n")) { throw 'BRIEF_ENCODING_FAIL' }
$scriptMatches = [regex]::Matches($briefText, '(?ms)^```powershell\n(?<script>param\(.*?^exit \$exitCode\n)```\n')
if ($scriptMatches.Count -ne 1) { throw 'EXACT_SCRIPT_EXTRACTION_FAIL' }
$scriptText = $scriptMatches[0].Groups['script'].Value
$scriptBytes = $utf8NoBom.GetBytes($scriptText)
$scriptSha256 = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($scriptBytes))
if ($scriptBytes.LongLength -ne $reviewedScriptBytes -or $scriptSha256 -cne $reviewedScriptSha256) { throw 'REVIEWED_SCRIPT_BYTES_FAIL' }

$tempBase = [IO.Path]::GetFullPath([IO.Path]::GetTempPath()).TrimEnd([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
$tempRoot = [IO.Path]::GetFullPath((Join-Path $tempBase ('omniroute-transport-preflight-' + [Guid]::NewGuid().ToString('N'))))
if (-not [StringComparer]::OrdinalIgnoreCase.Equals([IO.Path]::GetDirectoryName($tempRoot), $tempBase)) { throw 'TEMP_ROOT_VALIDATION_FAIL' }
if ([IO.Path]::GetFileName($tempRoot) -cnotmatch '^omniroute-transport-preflight-[0-9a-f]{32}$') { throw 'TEMP_ROOT_NAME_FAIL' }
$null = [IO.Directory]::CreateDirectory($tempRoot)
$scriptPath = [IO.Path]::GetFullPath((Join-Path $tempRoot $reviewedScriptLeaf))
if (-not [StringComparer]::OrdinalIgnoreCase.Equals([IO.Path]::GetDirectoryName($scriptPath), $tempRoot)) { throw 'SCRIPT_DIRECT_CHILD_FAIL' }
if ([IO.Path]::GetFileName($scriptPath) -cne $reviewedScriptLeaf) { throw 'SCRIPT_LEAF_FAIL' }
[IO.File]::WriteAllBytes($scriptPath, $scriptBytes)

$recordedRootIdentity = [OmniRoutePreflightFileIdentity]::GetOrdinaryIdentity($tempRoot, $true)
$recordedScriptIdentity = [OmniRoutePreflightFileIdentity]::GetOrdinaryIdentity($scriptPath, $false)
$recordedScriptBytes = [IO.File]::ReadAllBytes($scriptPath)
$recordedScriptSha256 = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($recordedScriptBytes))
if ($recordedScriptBytes.LongLength -ne $reviewedScriptBytes -or $recordedScriptSha256 -cne $reviewedScriptSha256) { throw 'RECORDED_SCRIPT_BYTES_FAIL' }
[Array]::Clear($recordedScriptBytes, 0, $recordedScriptBytes.Length)
$recordedScriptBytes = $null
[Array]::Clear($scriptBytes, 0, $scriptBytes.Length)
$scriptBytes = $null
$scriptText = $null
$briefText = $null
[Array]::Clear($briefRaw, 0, $briefRaw.Length)
$briefRaw = $null

if ([OmniRoutePreflightFileIdentity]::GetOrdinaryIdentity($tempRoot, $true) -cne $recordedRootIdentity) { throw 'ROOT_IDENTITY_DRIFT_BEFORE_START' }
if ([OmniRoutePreflightFileIdentity]::GetOrdinaryIdentity($scriptPath, $false) -cne $recordedScriptIdentity) { throw 'SCRIPT_IDENTITY_DRIFT_BEFORE_START' }

$startInfo = [Diagnostics.ProcessStartInfo]::new()
$startInfo.FileName = (Get-Command pwsh -ErrorAction Stop).Source
$startInfo.UseShellExecute = $false
$startInfo.CreateNoWindow = $true
$startInfo.RedirectStandardInput = $true
$startInfo.RedirectStandardOutput = $true
$startInfo.RedirectStandardError = $true
foreach ($argument in @(
    '-NoLogo', '-NoProfile', '-NonInteractive', '-File', $scriptPath,
    '-ExpectedTempRoot', $tempRoot,
    '-ExpectedScriptPath', $scriptPath,
    '-ExpectedTempRootIdentity', $recordedRootIdentity,
    '-ExpectedScriptIdentity', $recordedScriptIdentity,
    '-ExpectedScriptSha256', $reviewedScriptSha256,
    '-ExpectedScriptBytes', [string]$reviewedScriptBytes,
    '-ControlTimeoutSeconds', [string]$controlTimeoutSeconds
)) { $startInfo.ArgumentList.Add($argument) }

$preflightHandle = [Diagnostics.Process]::new()
$preflightHandle.StartInfo = $startInfo
$spawned = $false
$expectedPid = $null
$startupLines = [Collections.Generic.List[string]]::new()
$controlAttempted = $false
$controlSent = $false
$controlValue = $null
$stdinClosed = $false
$preflightPageHandle = $null
$pageCreated = $false
$exactPageClose = 'FAIL'
$exitConfirmed = $false
$observedExitCode = $null
$remainingStdout = $null
$remainingStderr = $null
$externalScriptAbsence = 'FAIL'
$externalRootAbsence = 'FAIL'
$coordinatorFailure = $null
$residualPid = $null

try {
    if (-not $preflightHandle.Start()) { throw 'PREFLIGHT_SPAWN_FAIL' }
    $spawned = $true
    $expectedPid = $preflightHandle.Id

    $startupClock = [Diagnostics.Stopwatch]::StartNew()
    $startupDeadline = [TimeSpan]::FromSeconds($startupTimeoutSeconds)
    1..5 | ForEach-Object {
        $startupLines.Add((Read-ChildLineBeforeDeadline -Reader $preflightHandle.StandardOutput -Process $preflightHandle -Clock $startupClock -Deadline $startupDeadline))
    }
    $startupClock.Stop()

    if ($startupLines[0] -cnotmatch '^OWNER_PID=([0-9]+)$') { throw 'OWNER_PID_LABEL_FAIL' }
    $observedOwnerPid = [int]$Matches[1]
    if ($observedOwnerPid -ne $expectedPid) { throw 'OWNER_PID_EQUALITY_FAIL' }
    if ($startupLines[1] -cne 'BASELINE_CLEAR=PASS') { throw 'BASELINE_CLEAR_LABEL_FAIL' }
    if ($startupLines[2] -cne 'BASELINE_EMPTY=PASS') { throw 'BASELINE_EMPTY_LABEL_FAIL' }
    if ($startupLines[3] -cnotmatch '^CHALLENGE=([0-9A-F]{32})$') { throw 'CHALLENGE_LABEL_FAIL' }
    $challenge = $Matches[1]
    if ($startupLines[4] -cne 'OWNER_READY=PASS') { throw 'OWNER_READY_LABEL_FAIL' }

    $pageHtml = '<!doctype html><meta charset="utf-8"><title>OmniRoute transport preflight</title><label for="c">Challenge</label><input id="c" aria-label="OmniRoute transport preflight challenge" readonly value="' + $challenge + '">'
    $pageUrl = 'data:text/html;charset=utf-8,' + [Uri]::EscapeDataString($pageHtml)
    $pageOpenResults = @(& $OpenExactPage $pageUrl)
    if ($pageOpenResults.Count -ne 1 -or $null -eq $pageOpenResults[0]) { throw 'EXACT_PAGE_HANDLE_MISSING' }
    $preflightPageHandle = $pageOpenResults[0]
    $pageCreated = $true

    $browserResults = @(& $PerformExactCopy $preflightPageHandle 'OmniRoute transport preflight challenge')
    if ($browserResults.Count -ne 1 -or $browserResults[0] -cnotin @('COPY_DONE', 'ABORT')) { throw 'BROWSER_RESULT_REJECTED' }
    $browserResult = $browserResults[0]
    $controlValue = $browserResult
    if ($controlAttempted) { throw 'SECOND_CONTROL_FORBIDDEN' }
    if ($preflightHandle.HasExited) { throw 'CHILD_EXITED_BEFORE_CONTROL' }
    $controlAttempted = $true
    $preflightHandle.StandardInput.WriteLine($controlValue)
    $preflightHandle.StandardInput.Flush()
    $controlSent = $true
    $preflightHandle.StandardInput.Close()
    $stdinClosed = $true
} catch {
    $coordinatorFailure = 'COORDINATOR_TRY_FAIL'
    if ($spawned -and -not $controlAttempted -and -not $stdinClosed -and -not $preflightHandle.HasExited) {
        try {
            $controlAttempted = $true
            $controlValue = 'ABORT'
            $preflightHandle.StandardInput.WriteLine('ABORT')
            $preflightHandle.StandardInput.Flush()
            $controlSent = $true
        } catch {
            $coordinatorFailure = 'COORDINATOR_ABORT_SEND_FAIL'
        }
    }
} finally {
    if ($spawned -and -not $stdinClosed) {
        try { $preflightHandle.StandardInput.Close(); $stdinClosed = $true } catch { $coordinatorFailure = 'COORDINATOR_STDIN_CLOSE_FAIL' }
    }

    if ($spawned) {
        try {
            $exitConfirmed = $preflightHandle.WaitForExit($exitTimeoutMilliseconds)
            if ($exitConfirmed) {
                $remainingStdout = $preflightHandle.StandardOutput.ReadToEnd()
                $remainingStderr = $preflightHandle.StandardError.ReadToEnd()
                $observedExitCode = $preflightHandle.ExitCode
            }
        } catch {
            $exitConfirmed = $false
            $coordinatorFailure = 'COORDINATOR_EXIT_OR_OUTPUT_FAIL'
        }
        if (-not $exitConfirmed) {
            $residualPid = $expectedPid
            "RETAINED_PID_RESIDUAL=$residualPid"
            'RETAINED_HANDLE_EXIT=FAIL'
        }
    }

    if ($pageCreated) {
        try {
            $pageCloseResults = @(& $CloseExactPage $preflightPageHandle)
            if ($pageCloseResults.Count -ne 1 -or $pageCloseResults[0] -cne 'PASS') { throw 'EXACT_PAGE_CLOSE_REJECTED' }
            $exactPageClose = 'PASS'
        } catch {
            $exactPageClose = 'FAIL'
        }
    }

    if ($exitConfirmed) {
        try {
            if ([IO.File]::Exists($scriptPath)) { throw 'EXTERNAL_SCRIPT_ABSENCE_FAIL' }
            $externalScriptAbsence = 'PASS'
            if (-not [IO.Directory]::Exists($tempRoot)) { throw 'EXTERNAL_ROOT_UNEXPECTEDLY_ABSENT' }
            if ([OmniRoutePreflightFileIdentity]::GetOrdinaryIdentity($tempRoot, $true) -cne $recordedRootIdentity) { throw 'EXTERNAL_ROOT_IDENTITY_DRIFT' }
            $materializedEntries = @([IO.Directory]::GetFileSystemEntries($tempRoot))
            if ($materializedEntries.Count -ne 0) { throw 'EXTERNAL_ROOT_NOT_EMPTY' }
            if ([OmniRoutePreflightFileIdentity]::GetOrdinaryIdentity($tempRoot, $true) -cne $recordedRootIdentity) { throw 'EXTERNAL_ROOT_IDENTITY_DRIFT_BEFORE_DELETE' }
            [IO.Directory]::Delete($tempRoot, $false)
            if ([IO.Directory]::Exists($tempRoot)) { throw 'EXTERNAL_ROOT_DELETE_FAIL' }
            $externalRootAbsence = 'PASS'
        } catch {
            $coordinatorFailure = 'COORDINATOR_EXTERNAL_ABSENCE_FAIL'
        }
    }

    try { $preflightHandle.Dispose() } catch { $coordinatorFailure = 'COORDINATOR_HANDLE_DISPOSE_FAIL' }
}

$machineOutputValid = $false
$terminalLine = $null
if ($exitConfirmed -and $startupLines.Count -eq 5 -and $null -ne $remainingStdout -and $null -ne $remainingStderr) {
    $normalizedTail = $remainingStdout.Replace("`r`n", "`n")
    if (-not $normalizedTail.Contains("`r") -and $normalizedTail.EndsWith("`n") -and -not $normalizedTail.EndsWith("`n`n")) {
        $tailLines = @($normalizedTail.Substring(0, $normalizedTail.Length - 1).Split("`n"))
        if ($tailLines.Count -eq 11) {
            $terminalLine = $tailLines[0]
            $comparisonCount = switch -CaseSensitive ($terminalLine) {
                'PREFLIGHT=PASS' { 1; break }
                'PREFLIGHT=FAIL' { 1; break }
                'PREFLIGHT=ABORTED' { 0; break }
                'PREFLIGHT=EOF' { 0; break }
                'PREFLIGHT=TIMEOUT' { 0; break }
                default { -1 }
            }
            $requiredExitCode = switch -CaseSensitive ($terminalLine) {
                'PREFLIGHT=PASS' { 0; break }
                'PREFLIGHT=FAIL' { 1; break }
                'PREFLIGHT=ABORTED' { 2; break }
                'PREFLIGHT=EOF' { 2; break }
                'PREFLIGHT=TIMEOUT' { 2; break }
                default { -1 }
            }
            $expectedTail = @(
                $terminalLine,
                'CLEANUP_CLIPBOARD_CLEAR=PASS',
                'CLEANUP_CLIPBOARD_EMPTY=PASS',
                'SCRIPT_DELETE_GUARD=PASS',
                'SCRIPT_DELETE=PASS',
                'COUNTER_BASELINE_WRITES=1',
                'COUNTER_BASELINE_READS=1',
                "COUNTER_COMPARISON_READS=$comparisonCount",
                'COUNTER_FINAL_WRITES=1',
                'COUNTER_POST_CLEAR_READS=1',
                'CLEANUP=PASS'
            )
            $sequenceEqual = $comparisonCount -ge 0 -and $requiredExitCode -ge 0
            for ($index = 0; $sequenceEqual -and $index -lt $expectedTail.Count; $index++) {
                if ($tailLines[$index] -cne $expectedTail[$index]) { $sequenceEqual = $false }
            }
            $machineOutputValid = $sequenceEqual -and $observedExitCode -eq $requiredExitCode -and $remainingStderr.Length -eq 0
        }
    }
}

$overallPass = $machineOutputValid -and
    $terminalLine -ceq 'PREFLIGHT=PASS' -and
    $controlSent -and $controlValue -ceq 'COPY_DONE' -and
    $observedExitCode -eq 0 -and
    $exactPageClose -ceq 'PASS' -and
    $externalScriptAbsence -ceq 'PASS' -and
    $externalRootAbsence -ceq 'PASS' -and
    $null -eq $coordinatorFailure -and
    $null -eq $residualPid

if ($overallPass) {
    'MACHINE_OUTPUT_VALID=PASS'
    'RETAINED_HANDLE_EXIT=PASS'
    'EXACT_PREFLIGHT_PAGE_CLOSE=PASS'
    'EXTERNAL_SCRIPT_ABSENCE=PASS'
    'EXTERNAL_TEMP_ROOT_ABSENCE=PASS'
    'PREFLIGHT_ACCEPTANCE=PASS'
    exit 0
}

if ($machineOutputValid) { 'MACHINE_OUTPUT_VALID=PASS' } else { 'MACHINE_OUTPUT_VALID=FAIL' }
if ($exitConfirmed) { 'RETAINED_HANDLE_EXIT=PASS' } else { 'RETAINED_HANDLE_EXIT=FAIL' }
"EXACT_PREFLIGHT_PAGE_CLOSE=$exactPageClose"
"EXTERNAL_SCRIPT_ABSENCE=$externalScriptAbsence"
"EXTERNAL_TEMP_ROOT_ABSENCE=$externalRootAbsence"
'PREFLIGHT_ACCEPTANCE=FAIL'
exit 1
```

The coordinator program's three browser adapters are part of the same one-shot
orchestration call: any adapter exception reaches the coordinator `catch`,
which attempts exact `ABORT` only when no control was attempted, the retained
child is alive, and stdin is still open. It never retries an uncertain write.
The `finally` closes stdin, calls `WaitForExit(15000)` before either
`ReadToEnd`, closes only the retained page handle, skips all destructive root
cleanup if exit is unconfirmed, records the exact residual PID without killing
it, and always disposes the retained process handle.

The exact output sequence comparison rejects every duplicate, unknown,
missing, blank, or out-of-order line. PASS requires baseline/comparison/final
counters `1 / 1 / 1 / 1 / 1`, all cleanup/delete labels PASS, terminal PASS,
exit `0`, empty stderr, retained exit, exact-page close, and external
script/root absence. ABORT/EOF/TIMEOUT require comparison `0`, their single
matching terminal label, exit `2`, and the same cleanup labels/counters. A
COPY_DONE mismatch may produce exact `PREFLIGHT=FAIL`, comparison `1`, and exit
`1`; it remains FAIL / NOT PROVEN. No manual parsing or verdict relaxation is
permitted.

| Terminal state | Comparison reads | Required emitted classification |
| --- | ---: | --- |
| exact `COPY_DONE` | `1` | internal exact compare; `PREFLIGHT=PASS` only on equality, otherwise `PREFLIGHT=FAIL` |
| `ABORT` or any rejected non-exact control line | `0` | `PREFLIGHT=ABORTED` |
| EOF | `0` | `PREFLIGHT=EOF` |
| monotonic timeout, including every deadline tie | `0` | `PREFLIGHT=TIMEOUT` |

Every terminal state converges on the fixed script's one `finally`. Immediately
before internal deletion it reopens both root and script with
`FILE_FLAG_OPEN_REPARSE_POINT`, rejects reparse objects or kind mismatch,
requires stable volume/file identities, rechecks exact bytes/hash, rechecks
identities again, and deletes only the reviewed script path. External root
deletion occurs only after retained exit, script absence, ordinary stable root
identity, an exact materialized empty entry array, and one immediate identity
recheck; deletion is non-recursive. Reparse, identity drift, residual PID, or
nonempty root stops without deletion.

## Structural counters and non-overlap

| Counter | Preflight maximum | Later credential stage |
| --- | ---: | ---: |
| fixed processes | `1` | credential-owner process exactly `1` only under a later gate |
| simultaneous preflight/credential processes | preflight must exit first | never overlap |
| local pages | `1` | separately reviewed later page only |
| transfer attempts / child control lines | `1 / 0..1` | separately counted |
| semantic focuses / `Control+A` / `Control+C` | `1 / 1 / 1` | separately counted |
| baseline / comparison / post-clear reads | `1 / 0..1 / 1` | not shared |
| baseline / final cleanup writes | `1 / 1` | not shared |
| browser clipboard API reads/writes | `0 / 0` | `0 / 0` |
| retries / fallbacks / alternate bridges / process kills | `0 / 0 / 0 / 0` | `0 / 0 / 0 / 0` |

Credential-process counters are never rolled into preflight counters. A
preflight process must be externally proven exited and its exact script absent
before any later credential-owner process may start.

## Future additive evidence fields; no mutation now

This preparation writes no evidence. Only a later separately reviewed,
exact-path evidence gate may add `secure_console_transfer_v1.transport_preflight`
alongside all existing incident fields. That object must contain these fields:

| Field | Required non-secret value type |
| --- | --- |
| `reviewed_contract` | path, SHA-256, byte size |
| `reviewed_brief` | path, SHA-256, byte size |
| `reviewed_script` | filename, SHA-256, byte size |
| `started_at`, `ended_at` | bounded timestamps |
| `expected_pid`, `observed_owner_pid`, `owner_pid_equal` | retained-handle binding and equality result |
| `exit_proof` | retained-handle exit result and exit code |
| `counters` | exact preflight-only process/page/action/read/write/retry values |
| `result` | PASS, FAIL, ABORTED, EOF, or TIMEOUT |
| `cleanup_labels` | exact fixed emitted cleanup labels and results |
| `exact_page_close` | exact retained-page close result |
| `current_clipboard_cleanup` | final clear and shape-only empty results; never content |
| `exact_script_deletion` | internal guard/delete plus external script/root absence results |
| `authorizes_live_execution` | literal `false` |

The later additive object must contain no challenge, clipboard content,
credential, token, header, private identifier, page serialization, keystroke,
prompt, response body, or managed string. It must preserve every prior
incident fact, including overall FAIL, acceptance NOT PROVEN, private
transcript exposure, capture failure, and invalid-token HTTP 401 NOT PROVEN.
No evidence file is read or mutated under this brief-preparation authority.

## Independent-review stop

Stop after committing this one ignored brief and its ignored preparation
report. A fresh independent Sol High reviewer must verify the direct committed
bytes, extracted-script equality, strict encoding, exact two-path preparation
scope, no unresolved marker, no secret, executable syntax, control-read cancellation,
four-state counters, cleanup/deletion guards, prohibited-action scan, and every
authority boundary above. `FAIL / REVISE` authorizes nothing. Even a future
PASS authorizes only a later explicit preflight action-time decision.
