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
- Exact extracted byte size: `23,758`.
- Exact extracted SHA-256: `16470D5E7F68773B259B49C7EC24D46B3A2D4B5238DCB71986990D6B73C5C367`.
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
$scriptLifetimeHandle = $null
$scriptDeleteHandle = $null
$rootCheckHandle = $null
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

public static class OmniRoutePreflightFileHandle
{
    private const uint GenericRead = 0x80000000;
    private const uint GenericWrite = 0x40000000;
    private const uint DeleteAccess = 0x00010000;
    private const uint FileReadAttributes = 0x00000080;
    private const uint ShareRead = 0x00000001;
    private const uint ShareWrite = 0x00000002;
    private const uint ShareDelete = 0x00000004;
    private const uint CreateNew = 1;
    private const uint OpenExisting = 3;
    private const uint FileAttributeNormal = 0x00000080;
    private const uint BackupSemantics = 0x02000000;
    private const uint OpenReparsePoint = 0x00200000;
    private const uint DirectoryAttribute = 0x00000010;
    private const uint ReparseAttribute = 0x00000400;
    private const uint FileBegin = 0;
    private const int FileDispositionInfo = 4;
    private const int MaximumReviewedBytes = 1048576;

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

    [StructLayout(LayoutKind.Sequential)]
    private struct FileDispositionInformation
    {
        [MarshalAs(UnmanagedType.Bool)]
        public bool DeleteFile;
    }

    [DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
    private static extern bool CreateDirectoryW(string path, IntPtr securityAttributes);

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
    private static extern SafeFileHandle ReOpenFile(
        SafeFileHandle originalFile,
        uint desiredAccess,
        uint shareMode,
        uint flagsAndAttributes);

    [DllImport("kernel32.dll", SetLastError = true)]
    private static extern bool GetFileInformationByHandle(
        SafeFileHandle file,
        out ByHandleFileInformation information);

    [DllImport("kernel32.dll", SetLastError = true)]
    private static extern bool SetFilePointerEx(
        SafeFileHandle file,
        long distance,
        out long newPosition,
        uint moveMethod);

    [DllImport("kernel32.dll", SetLastError = true)]
    private static extern bool SetEndOfFile(SafeFileHandle file);

    [DllImport("kernel32.dll", SetLastError = true)]
    private static extern bool GetFileSizeEx(SafeFileHandle file, out long fileSize);

    [DllImport("kernel32.dll", SetLastError = true)]
    private static extern bool ReadFile(
        SafeFileHandle file,
        IntPtr buffer,
        uint bytesToRead,
        out uint bytesRead,
        IntPtr overlapped);

    [DllImport("kernel32.dll", SetLastError = true)]
    private static extern bool WriteFile(
        SafeFileHandle file,
        IntPtr buffer,
        uint bytesToWrite,
        out uint bytesWritten,
        IntPtr overlapped);

    [DllImport("kernel32.dll", SetLastError = true)]
    private static extern bool FlushFileBuffers(SafeFileHandle file);

    [DllImport("kernel32.dll", SetLastError = true)]
    private static extern bool SetFileInformationByHandle(
        SafeFileHandle file,
        int informationClass,
        ref FileDispositionInformation information,
        uint bufferSize);

    public static void CreateDirectoryNew(string path)
    {
        if (!CreateDirectoryW(path, IntPtr.Zero))
            throw new Win32Exception(Marshal.GetLastWin32Error());
    }

    public static SafeFileHandle OpenRootForLifetime(string path)
    {
        SafeFileHandle handle = CreateFileW(
            path,
            FileReadAttributes | DeleteAccess,
            ShareRead | ShareWrite,
            IntPtr.Zero,
            OpenExisting,
            BackupSemantics | OpenReparsePoint,
            IntPtr.Zero);
        try { ValidateOrdinary(handle, true); return handle; }
        catch { handle.Dispose(); throw; }
    }

    public static SafeFileHandle OpenRootForCheck(string path)
    {
        SafeFileHandle handle = CreateFileW(
            path,
            FileReadAttributes,
            ShareRead | ShareWrite | ShareDelete,
            IntPtr.Zero,
            OpenExisting,
            BackupSemantics | OpenReparsePoint,
            IntPtr.Zero);
        try { ValidateOrdinary(handle, true); return handle; }
        catch { handle.Dispose(); throw; }
    }

    public static SafeFileHandle CreateScriptNew(string path)
    {
        SafeFileHandle handle = CreateFileW(
            path,
            GenericRead | GenericWrite | FileReadAttributes | DeleteAccess,
            ShareRead,
            IntPtr.Zero,
            CreateNew,
            FileAttributeNormal | OpenReparsePoint,
            IntPtr.Zero);
        try { ValidateOrdinary(handle, false); return handle; }
        catch { handle.Dispose(); throw; }
    }

    public static SafeFileHandle OpenScriptForLifetime(string path)
    {
        SafeFileHandle handle = CreateFileW(
            path,
            GenericRead | FileReadAttributes,
            ShareRead | ShareDelete,
            IntPtr.Zero,
            OpenExisting,
            FileAttributeNormal | OpenReparsePoint,
            IntPtr.Zero);
        try { ValidateOrdinary(handle, false); return handle; }
        catch { handle.Dispose(); throw; }
    }

    public static SafeFileHandle OpenScriptGuard(string path)
    {
        SafeFileHandle handle = CreateFileW(
            path,
            GenericRead | FileReadAttributes,
            ShareRead,
            IntPtr.Zero,
            OpenExisting,
            FileAttributeNormal | OpenReparsePoint,
            IntPtr.Zero);
        try { ValidateOrdinary(handle, false); return handle; }
        catch { handle.Dispose(); throw; }
    }

    public static SafeFileHandle OpenScriptForDelete(string path)
    {
        SafeFileHandle handle = CreateFileW(
            path,
            GenericRead | FileReadAttributes | DeleteAccess,
            ShareRead | ShareDelete,
            IntPtr.Zero,
            OpenExisting,
            FileAttributeNormal | OpenReparsePoint,
            IntPtr.Zero);
        try { ValidateOrdinary(handle, false); return handle; }
        catch { handle.Dispose(); throw; }
    }

    public static SafeFileHandle ReopenScriptForDelete(SafeFileHandle originalFile)
    {
        ValidateOrdinary(originalFile, false);
        SafeFileHandle handle = ReOpenFile(
            originalFile,
            GenericRead | FileReadAttributes | DeleteAccess,
            ShareRead | ShareDelete,
            OpenReparsePoint);
        try { ValidateOrdinary(handle, false); return handle; }
        catch { handle.Dispose(); throw; }
    }

    public static string GetIdentity(SafeFileHandle handle, bool requireDirectory)
    {
        ByHandleFileInformation information = ValidateOrdinary(handle, requireDirectory);
        return string.Format(
            "{0:X8}:{1:X8}:{2:X8}",
            information.VolumeSerialNumber,
            information.FileIndexHigh,
            information.FileIndexLow);
    }

    public static void WriteExact(SafeFileHandle handle, byte[] bytes)
    {
        ValidateOrdinary(handle, false);
        if (bytes == null || bytes.Length < 1 || bytes.Length > MaximumReviewedBytes)
            throw new InvalidOperationException("WRITE_SIZE_REJECTED");

        long position;
        if (!SetFilePointerEx(handle, 0, out position, FileBegin))
            throw new Win32Exception(Marshal.GetLastWin32Error());

        IntPtr buffer = Marshal.AllocHGlobal(bytes.Length);
        try
        {
            Marshal.Copy(bytes, 0, buffer, bytes.Length);
            int offset = 0;
            while (offset < bytes.Length)
            {
                uint written;
                if (!WriteFile(handle, IntPtr.Add(buffer, offset), (uint)(bytes.Length - offset), out written, IntPtr.Zero))
                    throw new Win32Exception(Marshal.GetLastWin32Error());
                if (written == 0)
                    throw new InvalidOperationException("ZERO_BYTE_WRITE");
                offset += checked((int)written);
            }
            if (!SetEndOfFile(handle))
                throw new Win32Exception(Marshal.GetLastWin32Error());
            if (!FlushFileBuffers(handle))
                throw new Win32Exception(Marshal.GetLastWin32Error());
            if (!SetFilePointerEx(handle, 0, out position, FileBegin))
                throw new Win32Exception(Marshal.GetLastWin32Error());
        }
        finally
        {
            Marshal.FreeHGlobal(buffer);
        }
    }

    public static byte[] ReadExact(SafeFileHandle handle)
    {
        ValidateOrdinary(handle, false);
        long length;
        if (!GetFileSizeEx(handle, out length))
            throw new Win32Exception(Marshal.GetLastWin32Error());
        if (length < 1 || length > MaximumReviewedBytes)
            throw new InvalidOperationException("READ_SIZE_REJECTED");

        long position;
        if (!SetFilePointerEx(handle, 0, out position, FileBegin))
            throw new Win32Exception(Marshal.GetLastWin32Error());

        byte[] bytes = new byte[checked((int)length)];
        IntPtr buffer = Marshal.AllocHGlobal(bytes.Length);
        try
        {
            int offset = 0;
            while (offset < bytes.Length)
            {
                uint read;
                if (!ReadFile(handle, IntPtr.Add(buffer, offset), (uint)(bytes.Length - offset), out read, IntPtr.Zero))
                    throw new Win32Exception(Marshal.GetLastWin32Error());
                if (read == 0)
                    throw new InvalidOperationException("UNEXPECTED_EOF");
                offset += checked((int)read);
            }
            Marshal.Copy(buffer, bytes, 0, bytes.Length);
            if (!SetFilePointerEx(handle, 0, out position, FileBegin))
                throw new Win32Exception(Marshal.GetLastWin32Error());
            return bytes;
        }
        finally
        {
            Marshal.FreeHGlobal(buffer);
        }
    }

    public static void MarkDelete(SafeFileHandle handle, bool requireDirectory)
    {
        ValidateOrdinary(handle, requireDirectory);
        FileDispositionInformation information = new FileDispositionInformation { DeleteFile = true };
        if (!SetFileInformationByHandle(
            handle,
            FileDispositionInfo,
            ref information,
            (uint)Marshal.SizeOf<FileDispositionInformation>()))
            throw new Win32Exception(Marshal.GetLastWin32Error());
    }

    private static ByHandleFileInformation ValidateOrdinary(
        SafeFileHandle handle,
        bool requireDirectory)
    {
        if (handle == null || handle.IsInvalid || handle.IsClosed)
            throw new InvalidOperationException("HANDLE_REJECTED");

        ByHandleFileInformation information;
        if (!GetFileInformationByHandle(handle, out information))
            throw new Win32Exception(Marshal.GetLastWin32Error());
        if ((information.FileAttributes & ReparseAttribute) != 0)
            throw new InvalidOperationException("REPARSE_POINT_REJECTED");

        bool isDirectory = (information.FileAttributes & DirectoryAttribute) != 0;
        if (isDirectory != requireDirectory)
            throw new InvalidOperationException("OBJECT_KIND_REJECTED");
        return information;
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
    if (-not $pathComparer.Equals([IO.Path]::GetDirectoryName($scriptPath), $tempRoot)) {
        throw 'SCRIPT_NOT_DIRECT_CHILD'
    }
    if ([IO.Path]::GetFileName($scriptPath) -cne $reviewedLeaf) {
        throw 'SCRIPT_LEAF_REJECTED'
    }
    if (-not $pathComparer.Equals($actualCommandPath, $scriptPath)) {
        throw 'COMMAND_PATH_MISMATCH'
    }
    $rootCheckHandle = [OmniRoutePreflightFileHandle]::OpenRootForCheck($tempRoot)
    $actualTempRootIdentity = [OmniRoutePreflightFileHandle]::GetIdentity($rootCheckHandle, $true)
    $rootCheckHandle.Dispose()
    $rootCheckHandle = $null
    $scriptLifetimeHandle = [OmniRoutePreflightFileHandle]::OpenScriptForLifetime($scriptPath)
    $actualScriptIdentity = [OmniRoutePreflightFileHandle]::GetIdentity($scriptLifetimeHandle, $false)
    if ($actualTempRootIdentity -cne $ExpectedTempRootIdentity -or $actualScriptIdentity -cne $ExpectedScriptIdentity) {
        throw 'START_IDENTITY_DRIFT'
    }
    $startScriptBytes = [OmniRoutePreflightFileHandle]::ReadExact($scriptLifetimeHandle)
    $startScriptSha256 = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($startScriptBytes))
    if ($startScriptBytes.LongLength -ne $ExpectedScriptBytes -or $startScriptSha256 -cne $ExpectedScriptSha256) {
        throw 'START_HASH_OR_SIZE_MISMATCH'
    }
    [Array]::Clear($startScriptBytes, 0, $startScriptBytes.Length)
    $startScriptBytes = $null

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
        $rootCheckHandle = [OmniRoutePreflightFileHandle]::OpenRootForCheck($tempRootForDelete)
        $rootIdentityBeforeHash = [OmniRoutePreflightFileHandle]::GetIdentity($rootCheckHandle, $true)
        $rootCheckHandle.Dispose()
        $rootCheckHandle = $null
        if ($null -eq $scriptLifetimeHandle -or $scriptLifetimeHandle.IsInvalid -or $scriptLifetimeHandle.IsClosed) {
            throw 'DELETE_SCRIPT_HANDLE_UNAVAILABLE'
        }
        $scriptDeleteHandle = [OmniRoutePreflightFileHandle]::ReopenScriptForDelete($scriptLifetimeHandle)
        $scriptIdentityBeforeHash = [OmniRoutePreflightFileHandle]::GetIdentity($scriptDeleteHandle, $false)
        if ($rootIdentityBeforeHash -cne $ExpectedTempRootIdentity -or $scriptIdentityBeforeHash -cne $ExpectedScriptIdentity) {
            throw 'DELETE_IDENTITY_DRIFT_BEFORE_HASH'
        }
        $scriptBytes = [OmniRoutePreflightFileHandle]::ReadExact($scriptDeleteHandle)
        $actualScriptBytes = [long]$scriptBytes.LongLength
        $actualScriptSha256 = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($scriptBytes))
        [Array]::Clear($scriptBytes, 0, $scriptBytes.Length)
        $scriptBytes = $null
        if ($actualScriptBytes -ne $ExpectedScriptBytes -or $actualScriptSha256 -cne $ExpectedScriptSha256) {
            throw 'DELETE_HASH_OR_SIZE_MISMATCH'
        }
        $rootCheckHandle = [OmniRoutePreflightFileHandle]::OpenRootForCheck($tempRootForDelete)
        $rootIdentityImmediatelyBeforeDelete = [OmniRoutePreflightFileHandle]::GetIdentity($rootCheckHandle, $true)
        $rootCheckHandle.Dispose()
        $rootCheckHandle = $null
        $scriptIdentityImmediatelyBeforeDelete = [OmniRoutePreflightFileHandle]::GetIdentity($scriptDeleteHandle, $false)
        if ($rootIdentityImmediatelyBeforeDelete -cne $ExpectedTempRootIdentity -or $scriptIdentityImmediatelyBeforeDelete -cne $ExpectedScriptIdentity) {
            throw 'DELETE_IDENTITY_DRIFT'
        }
        $deleteGuard = $true
        [OmniRoutePreflightFileHandle]::MarkDelete($scriptDeleteHandle, $false)
        $scriptDeleteHandle.Dispose()
        $scriptDeleteHandle = $null
        $scriptLifetimeHandle.Dispose()
        $scriptLifetimeHandle = $null
        $deleteSucceeded = -not [IO.File]::Exists($scriptPathForDelete)
    } catch {
        $cleanupOk = $false
        $exitCode = 1
    } finally {
        if ($null -ne $rootCheckHandle) {
            $rootCheckHandle.Dispose()
            $rootCheckHandle = $null
        }
        if ($null -ne $scriptLifetimeHandle) {
            $scriptLifetimeHandle.Dispose()
            $scriptLifetimeHandle = $null
        }
        if ($null -ne $scriptDeleteHandle) {
            $scriptDeleteHandle.Dispose()
            $scriptDeleteHandle = $null
        }
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
only by the later sole-owner execution task through the exact host-rendezvous
bridge runner below, with the exact full commit and SHA-256 copied from the
fresh PASS review. The coordinator block remains exactly `23,958` bytes with
SHA-256
`A42E058813231AF53D6502A2FB3341641E32040E22DBC130E62C6453F3A871AE`.
The runner supplies three authority-constrained adapters: `OpenExactPage` opens only
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

$cancelableReadLineOverloads = @([Console]::In.GetType().GetMethods() | Where-Object {
    $_.Name -eq 'ReadLineAsync' -and
    $_.GetParameters().Count -eq 1 -and
    $_.GetParameters()[0].ParameterType -eq [Threading.CancellationToken]
})
if ($PSVersionTable.PSVersion.Major -ne 7 -or $cancelableReadLineOverloads.Count -ne 1) { throw 'POWERSHELL_RUNTIME_CAPABILITY_FAIL' }

$briefRelativePath = '.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-anydesk-clipboard-preflight-live-brief.md'
$briefPath = 'C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-agent-routing-source\.superpowers\sdd\2026-08-30-omniroute-standard-team-api\task-2-anydesk-clipboard-preflight-live-brief.md'
$repoRoot = 'C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-agent-routing-source'
$reviewedScriptBytes = 23758
$reviewedScriptSha256 = '16470D5E7F68773B259B49C7EC24D46B3A2D4B5238DCB71986990D6B73C5C367'
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

$handleSourceMatches = [regex]::Matches($scriptText, "(?ms)Add-Type -TypeDefinition @'\n(?<source>using System;.*?^}\n)'@ -ErrorAction Stop")
if ($handleSourceMatches.Count -ne 1) { throw 'HANDLE_SOURCE_EXTRACTION_FAIL' }
$handleSource = $handleSourceMatches[0].Groups['source'].Value

$tempBase = [IO.Path]::GetFullPath([IO.Path]::GetTempPath()).TrimEnd([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
$tempRoot = [IO.Path]::GetFullPath((Join-Path $tempBase ('omniroute-transport-preflight-' + [Guid]::NewGuid().ToString('N'))))
if (-not [StringComparer]::OrdinalIgnoreCase.Equals([IO.Path]::GetDirectoryName($tempRoot), $tempBase)) { throw 'TEMP_ROOT_VALIDATION_FAIL' }
if ([IO.Path]::GetFileName($tempRoot) -cnotmatch '^omniroute-transport-preflight-[0-9a-f]{32}$') { throw 'TEMP_ROOT_NAME_FAIL' }
$scriptPath = [IO.Path]::GetFullPath((Join-Path $tempRoot $reviewedScriptLeaf))
if (-not [StringComparer]::OrdinalIgnoreCase.Equals([IO.Path]::GetDirectoryName($scriptPath), $tempRoot)) { throw 'SCRIPT_DIRECT_CHILD_FAIL' }
if ([IO.Path]::GetFileName($scriptPath) -cne $reviewedScriptLeaf) { throw 'SCRIPT_LEAF_FAIL' }

function Assert-ReviewedScriptHandle {
    param(
        [Parameter(Mandatory)] [Microsoft.Win32.SafeHandles.SafeFileHandle]$Handle,
        [Parameter(Mandatory)] [string]$ExpectedIdentity,
        [Parameter(Mandatory)] [long]$ExpectedBytes,
        [Parameter(Mandatory)] [string]$ExpectedSha256
    )
    if ([OmniRoutePreflightFileHandle]::GetIdentity($Handle, $false) -cne $ExpectedIdentity) { throw 'CLEANUP_SCRIPT_IDENTITY_FAIL' }
    $cleanupBytes = [OmniRoutePreflightFileHandle]::ReadExact($Handle)
    try {
        $cleanupSha256 = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($cleanupBytes))
        if ($cleanupBytes.LongLength -ne $ExpectedBytes -or $cleanupSha256 -cne $ExpectedSha256) { throw 'CLEANUP_SCRIPT_HASH_FAIL' }
    } finally {
        [Array]::Clear($cleanupBytes, 0, $cleanupBytes.Length)
    }
    if ([OmniRoutePreflightFileHandle]::GetIdentity($Handle, $false) -cne $ExpectedIdentity) { throw 'CLEANUP_SCRIPT_IDENTITY_DRIFT' }
}

function Set-ReviewedScriptDeleteDisposition {
    param(
        [Parameter(Mandatory)] [Microsoft.Win32.SafeHandles.SafeFileHandle]$Handle,
        [Parameter(Mandatory)] [string]$ExpectedIdentity,
        [Parameter(Mandatory)] [long]$ExpectedBytes,
        [Parameter(Mandatory)] [string]$ExpectedSha256
    )
    Assert-ReviewedScriptHandle -Handle $Handle -ExpectedIdentity $ExpectedIdentity -ExpectedBytes $ExpectedBytes -ExpectedSha256 $ExpectedSha256
    [OmniRoutePreflightFileHandle]::MarkDelete($Handle, $false)
}

function Set-ReviewedRootDeleteDisposition {
    param(
        [Parameter(Mandatory)] [Microsoft.Win32.SafeHandles.SafeFileHandle]$Handle,
        [Parameter(Mandatory)] [string]$Path,
        [Parameter(Mandatory)] [string]$ExpectedIdentity
    )
    if ([OmniRoutePreflightFileHandle]::GetIdentity($Handle, $true) -cne $ExpectedIdentity) { throw 'CLEANUP_ROOT_IDENTITY_FAIL' }
    $materializedEntries = @([IO.Directory]::GetFileSystemEntries($Path))
    if ($materializedEntries.Count -ne 0) { throw 'CLEANUP_ROOT_NOT_EMPTY' }
    if ([OmniRoutePreflightFileHandle]::GetIdentity($Handle, $true) -cne $ExpectedIdentity) { throw 'CLEANUP_ROOT_IDENTITY_DRIFT' }
    [OmniRoutePreflightFileHandle]::MarkDelete($Handle, $true)
}

$rootCreated = $false
$scriptCreated = $false
$spawnAttempted = $false
$spawnConfirmed = $false
$spawnOutcomeUncertain = $false
$residualProcess = $false
$rootLifetimeHandle = $null
$scriptCreationHandle = $null
$scriptGuardHandle = $null
$scriptCleanupHandle = $null
$preflightHandle = $null
$recordedRootIdentity = $null
$recordedScriptIdentity = $null
$expectedPid = $null
$startupLines = [Collections.Generic.List[string]]::new()
$controlSent = $false
$controlValue = $null
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
    Add-Type -TypeDefinition $handleSource -ErrorAction Stop
    [OmniRoutePreflightFileHandle]::CreateDirectoryNew($tempRoot)
    $rootCreated = $true
    $rootLifetimeHandle = [OmniRoutePreflightFileHandle]::OpenRootForLifetime($tempRoot)
    $recordedRootIdentity = [OmniRoutePreflightFileHandle]::GetIdentity($rootLifetimeHandle, $true)
    if (@([IO.Directory]::GetFileSystemEntries($tempRoot)).Count -ne 0) { throw 'NEW_ROOT_NOT_EMPTY' }

    $scriptCreationHandle = [OmniRoutePreflightFileHandle]::CreateScriptNew($scriptPath)
    $scriptCreated = $true
    [OmniRoutePreflightFileHandle]::WriteExact($scriptCreationHandle, $scriptBytes)
    $recordedScriptIdentity = [OmniRoutePreflightFileHandle]::GetIdentity($scriptCreationHandle, $false)
    $recordedScriptBytes = [OmniRoutePreflightFileHandle]::ReadExact($scriptCreationHandle)
    $recordedScriptSha256 = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($recordedScriptBytes))
    if ($recordedScriptBytes.LongLength -ne $reviewedScriptBytes -or $recordedScriptSha256 -cne $reviewedScriptSha256) { throw 'RECORDED_SCRIPT_BYTES_FAIL' }
    [Array]::Clear($recordedScriptBytes, 0, $recordedScriptBytes.Length)
    $recordedScriptBytes = $null

    $scriptCreationHandle.Dispose()
    $scriptCreationHandle = $null
    $scriptGuardHandle = [OmniRoutePreflightFileHandle]::OpenScriptGuard($scriptPath)
    Assert-ReviewedScriptHandle -Handle $scriptGuardHandle -ExpectedIdentity $recordedScriptIdentity -ExpectedBytes $reviewedScriptBytes -ExpectedSha256 $reviewedScriptSha256
    if ([OmniRoutePreflightFileHandle]::GetIdentity($rootLifetimeHandle, $true) -cne $recordedRootIdentity) { throw 'ROOT_IDENTITY_DRIFT_BEFORE_START' }
    if ([OmniRoutePreflightFileHandle]::GetIdentity($scriptGuardHandle, $false) -cne $recordedScriptIdentity) { throw 'SCRIPT_IDENTITY_DRIFT_BEFORE_START' }

    [Array]::Clear($scriptBytes, 0, $scriptBytes.Length)
    $scriptBytes = $null
    $scriptText = $null
    $briefText = $null
    [Array]::Clear($briefRaw, 0, $briefRaw.Length)
    $briefRaw = $null

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
    $spawnAttempted = $true
    try {
        $startConfirmed = $preflightHandle.Start()
    } catch {
        $spawnOutcomeUncertain = $true
        $residualProcess = $true
        try {
            if ($preflightHandle.Id -gt 0) {
                $expectedPid = $preflightHandle.Id
                $residualPid = $expectedPid
            }
        } catch {}
        throw 'PREFLIGHT_SPAWN_OUTCOME_UNCERTAIN'
    }
    if (-not $startConfirmed) { throw 'PREFLIGHT_NO_CHILD_SPAWNED' }
    $spawned = $true
    $spawnConfirmed = $true
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
    $scriptGuardHandle.Dispose()
    $scriptGuardHandle = $null

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

}
} catch {
    if ($null -eq $coordinatorFailure) { $coordinatorFailure = 'COORDINATOR_RESOURCE_TRY_FAIL' }
} finally {
    if ($spawnOutcomeUncertain -or ($spawnConfirmed -and -not $exitConfirmed)) {
        $residualProcess = $true
    }

    if ($residualProcess) {
        if ($null -eq $residualPid) {
            if ($null -ne $expectedPid) { $residualPid = $expectedPid } else { $residualPid = 'UNKNOWN' }
        }
        "RETAINED_PID=$residualPid"
        "RETAINED_SCRIPT_PATH=$scriptPath"
        "RETAINED_ROOT_PATH=$tempRoot"
    } else {
        try {
            if ($scriptCreated) {
                if ($null -ne $scriptCreationHandle) {
                    Set-ReviewedScriptDeleteDisposition -Handle $scriptCreationHandle -ExpectedIdentity $recordedScriptIdentity -ExpectedBytes $reviewedScriptBytes -ExpectedSha256 $reviewedScriptSha256
                    $scriptCreationHandle.Dispose()
                    $scriptCreationHandle = $null
                } elseif ($null -ne $scriptGuardHandle) {
                    Assert-ReviewedScriptHandle -Handle $scriptGuardHandle -ExpectedIdentity $recordedScriptIdentity -ExpectedBytes $reviewedScriptBytes -ExpectedSha256 $reviewedScriptSha256
                    $scriptGuardHandle.Dispose()
                    $scriptGuardHandle = $null
                    $scriptCleanupHandle = [OmniRoutePreflightFileHandle]::OpenScriptForDelete($scriptPath)
                    Set-ReviewedScriptDeleteDisposition -Handle $scriptCleanupHandle -ExpectedIdentity $recordedScriptIdentity -ExpectedBytes $reviewedScriptBytes -ExpectedSha256 $reviewedScriptSha256
                    $scriptCleanupHandle.Dispose()
                    $scriptCleanupHandle = $null
                } elseif ([IO.File]::Exists($scriptPath)) {
                    $scriptCleanupHandle = [OmniRoutePreflightFileHandle]::OpenScriptForDelete($scriptPath)
                    Set-ReviewedScriptDeleteDisposition -Handle $scriptCleanupHandle -ExpectedIdentity $recordedScriptIdentity -ExpectedBytes $reviewedScriptBytes -ExpectedSha256 $reviewedScriptSha256
                    $scriptCleanupHandle.Dispose()
                    $scriptCleanupHandle = $null
                }
                if ([IO.File]::Exists($scriptPath)) { throw 'CLEANUP_SCRIPT_ABSENCE_FAIL' }
            } elseif ([IO.File]::Exists($scriptPath)) {
                throw 'UNCREATED_SCRIPT_PATH_PRESENT'
            }
            $externalScriptAbsence = 'PASS'

            if ($rootCreated) {
                if ($null -eq $rootLifetimeHandle) { throw 'CLEANUP_ROOT_HANDLE_UNAVAILABLE' }
                Set-ReviewedRootDeleteDisposition -Handle $rootLifetimeHandle -Path $tempRoot -ExpectedIdentity $recordedRootIdentity
                $rootLifetimeHandle.Dispose()
                $rootLifetimeHandle = $null
                if ([IO.Directory]::Exists($tempRoot)) { throw 'CLEANUP_ROOT_ABSENCE_FAIL' }
            } elseif ([IO.Directory]::Exists($tempRoot)) {
                throw 'UNCREATED_ROOT_PATH_PRESENT'
            }
            $externalRootAbsence = 'PASS'
        } catch {
            $coordinatorFailure = 'COORDINATOR_HANDLE_CLEANUP_FAIL'
            if ($spawnConfirmed -and $null -ne $expectedPid) { "RETAINED_PID=$expectedPid" } else { 'RETAINED_PID=NONE' }
            "RETAINED_SCRIPT_PATH=$scriptPath"
            "RETAINED_ROOT_PATH=$tempRoot"
        }
    }

    if ($null -ne $scriptCreationHandle) { try { $scriptCreationHandle.Dispose() } catch {}; $scriptCreationHandle = $null }
    if ($null -ne $scriptGuardHandle) { try { $scriptGuardHandle.Dispose() } catch {}; $scriptGuardHandle = $null }
    if ($null -ne $scriptCleanupHandle) { try { $scriptCleanupHandle.Dispose() } catch {}; $scriptCleanupHandle = $null }
    if ($null -ne $rootLifetimeHandle) { try { $rootLifetimeHandle.Dispose() } catch {}; $rootLifetimeHandle = $null }
    if ($null -ne $preflightHandle) {
        try { $preflightHandle.Dispose() } catch { $coordinatorFailure = 'COORDINATOR_HANDLE_DISPOSE_FAIL' }
    }
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
The outer resource `try/finally` begins before `CreateDirectoryNew` and tracks
root/script creation, spawn attempt/confirmation, uncertain outcome, and a
residual process. The inner process `finally` closes stdin, calls
`WaitForExit(15000)` before either `ReadToEnd`, and closes only the retained
page handle. The outer `finally` performs handle-bound cleanup when no child
spawned or confirmed exit occurred. An uncertain spawn or unconfirmed exit
performs no disposition, records exact retained paths plus PID or `UNKNOWN`,
and always disposes every created safe/process handle without killing.

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

The coordinator creates the script with Win32 `CREATE_NEW`; any existing file,
hard link, symlink, or reparse leaf fails before bytes are written. Writing,
flush, identity, size, and hash checks use the returned safe handle. It shares
read only, so no outstanding writer or delete/rename can coexist. After
write/hash, the coordinator closes it and immediately opens an ordinary
read-only guard that also shares read only, then rechecks the recorded
identity/size/hash. An incompatible writer, guard acquisition failure,
substitution, or hash drift stops before spawn with no retry. The guard remains
open across process spawn until the child has opened and validated its own
ordinary read handle and emitted exact `OWNER_READY=PASS`, so the path and
reviewed bytes remain immutable during `pwsh -File` load and child validation.
The child's lifetime handle shares read plus delete but not write, preserving
immutability after the guard closes. It verifies exact identity/hash at entry,
obtains final delete access from that object via `ReOpenFile`, then verifies
exact identity/hash on the reopened handle in its one `finally` and applies
`FileDispositionInfo` through
`SetFileInformationByHandle`; no path delete is used.

The coordinator retains one ordinary root handle opened without delete sharing
from creation through cleanup. Pre-spawn failure with no child uses the retained
exact script handle for the same identity/hash/disposition guard, then checks a
materialized empty root and applies root disposition through the still-open
root handle. Confirmed child exit uses the same outer cleanup. An uncertain
spawn, residual process, absent handle, reparse, identity/hash mismatch,
nonempty root, or disposition failure stops without deleting any path-resolved
substitute. All path calls after handle close are absence proofs only; there is
no `Remove-Item`, `WriteAllBytes`, or path-based directory deletion.

## Exact host-rendezvous bridge runner

The coordinator cannot call the selected persistent `chrome` Node binding
directly. The following exact PowerShell 7 bridge runner supplies its three
scriptblock adapters through a bounded stdin/stdout rendezvous with the sole
owner. This is host orchestration, not a browser clipboard API: PowerShell
never receives a browser `Tab` object, and Chrome never reads or writes the
clipboard through an API. The bridge adds no credential or live-resource
authority.

The exact bridge-runner bytes are the complete contents of the single fenced
`powershell` block below, beginning with `param(` and ending with the LF after
`exit $bridgeExitCode`; the fence and surrounding Markdown are excluded. The
exact extracted byte size is `19,375` and its SHA-256 is
`2EBD922B5156CFCE9E643E39DE3C5F7CB6987002E592D2F2A3CEF940B6872C77`.
The fresh independent review must reproduce both values. At action
time the sole owner must provide all eight pins: reviewed brief commit and
SHA-256, coordinator byte size and SHA-256, bridge-runner byte size and
SHA-256, and the already-reviewed child byte size and SHA-256. The runner
rejects any working/commit drift or extracted-block mismatch before it starts
the nested coordinator.

```powershell
param(
    [Parameter(Mandatory)]
    [ValidatePattern('^[0-9a-f]{40}$')]
    [string]$ReviewedBriefCommit,

    [Parameter(Mandatory)]
    [ValidatePattern('^[0-9A-F]{64}$')]
    [string]$ReviewedBriefSha256,

    [Parameter(Mandatory)]
    [ValidateRange(1, 1048576)]
    [long]$ReviewedCoordinatorBytes,

    [Parameter(Mandatory)]
    [ValidatePattern('^[0-9A-F]{64}$')]
    [string]$ReviewedCoordinatorSha256,

    [Parameter(Mandatory)]
    [ValidateRange(1, 1048576)]
    [long]$ReviewedBridgeRunnerBytes,

    [Parameter(Mandatory)]
    [ValidatePattern('^[0-9A-F]{64}$')]
    [string]$ReviewedBridgeRunnerSha256,

    [Parameter(Mandatory)]
    [ValidateRange(1, 1048576)]
    [long]$ReviewedChildBytes,

    [Parameter(Mandatory)]
    [ValidatePattern('^[0-9A-F]{64}$')]
    [string]$ReviewedChildSha256
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$cancelableReadLineOverloads = @([Console]::In.GetType().GetMethods() | Where-Object {
    $_.Name -eq 'ReadLineAsync' -and
    $_.GetParameters().Count -eq 1 -and
    $_.GetParameters()[0].ParameterType -eq [Threading.CancellationToken]
})
if ($PSVersionTable.PSVersion.Major -ne 7 -or $cancelableReadLineOverloads.Count -ne 1) { throw 'BRIDGE_POWERSHELL_RUNTIME_CAPABILITY_FAIL' }

function ConvertTo-Base64Url {
    param([Parameter(Mandatory)] [string]$Value)
    return [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($Value)).TrimEnd('=').Replace('+', '-').Replace('/', '_')
}

function Read-LineBeforeDeadline {
    param(
        [Parameter(Mandatory)] [IO.TextReader]$Reader,
        [Parameter(Mandatory)] [Diagnostics.Stopwatch]$Clock,
        [Parameter(Mandatory)] [TimeSpan]$Deadline,
        [Parameter(Mandatory)] [string]$TimeoutCode,
        [Parameter(Mandatory)] [string]$EofCode
    )

    $readCts = [Threading.CancellationTokenSource]::new()
    $lineTask = $null
    try {
        $lineTask = $Reader.ReadLineAsync($readCts.Token)
        while (-not $lineTask.IsCompleted -and $Clock.Elapsed -lt $Deadline) {
            [Threading.Thread]::Sleep(25)
        }
        $deadlineReached = $Clock.Elapsed -ge $Deadline
        if ($deadlineReached) {
            $readCts.Cancel()
            try { $null = $lineTask.GetAwaiter().GetResult() } catch {}
            throw $TimeoutCode
        }
        if (-not $lineTask.IsCompleted) {
            $readCts.Cancel()
            try { $null = $lineTask.GetAwaiter().GetResult() } catch {}
            throw $TimeoutCode
        }
        $line = $lineTask.GetAwaiter().GetResult()
        if ($null -eq $line) { throw $EofCode }
        return $line
    } finally {
        if ($null -ne $lineTask -and -not $lineTask.IsCompleted) {
            $readCts.Cancel()
            try { $null = $lineTask.GetAwaiter().GetResult() } catch {}
        }
        $readCts.Dispose()
    }
}

$briefRelativePath = '.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-anydesk-clipboard-preflight-live-brief.md'
$briefPath = 'C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-agent-routing-source\.superpowers\sdd\2026-08-30-omniroute-standard-team-api\task-2-anydesk-clipboard-preflight-live-brief.md'
$repoRoot = 'C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-agent-routing-source'
$expectedCoordinatorBytes = 23958
$expectedCoordinatorSha256 = 'A42E058813231AF53D6502A2FB3341641E32040E22DBC130E62C6453F3A871AE'
$expectedChildBytes = 23758
$expectedChildSha256 = '16470D5E7F68773B259B49C7EC24D46B3A2D4B5238DCB71986990D6B73C5C367'
$bridgeResponseTimeoutSeconds = 45
$coordinatorTimeoutSeconds = 180
$coordinatorExitTimeoutMilliseconds = 15000
$utf8NoBom = [Text.UTF8Encoding]::new($false, $true)

if ($ReviewedCoordinatorBytes -ne $expectedCoordinatorBytes -or $ReviewedCoordinatorSha256 -cne $expectedCoordinatorSha256) {
    throw 'ACTION_COORDINATOR_PIN_FAIL'
}
if ($ReviewedChildBytes -ne $expectedChildBytes -or $ReviewedChildSha256 -cne $expectedChildSha256) {
    throw 'ACTION_CHILD_PIN_FAIL'
}

$briefRaw = [IO.File]::ReadAllBytes($briefPath)
$observedBriefSha256 = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($briefRaw))
if ($observedBriefSha256 -cne $ReviewedBriefSha256) { throw 'ACTION_BRIEF_SHA256_FAIL' }
$workingBriefBlob = (& git -C $repoRoot hash-object --no-filters -- $briefRelativePath).Trim()
if ($LASTEXITCODE -ne 0 -or $workingBriefBlob -cnotmatch '^[0-9a-f]{40}$') { throw 'ACTION_WORKING_BRIEF_BLOB_FAIL' }
$reviewedBriefBlob = (& git -C $repoRoot rev-parse ($ReviewedBriefCommit + ':' + $briefRelativePath)).Trim()
if ($LASTEXITCODE -ne 0 -or $reviewedBriefBlob -cnotmatch '^[0-9a-f]{40}$') { throw 'ACTION_REVIEWED_BRIEF_COMMIT_FAIL' }
if ($workingBriefBlob -cne $reviewedBriefBlob) { throw 'ACTION_BRIEF_COMMIT_WORKING_DRIFT' }

$briefText = $utf8NoBom.GetString($briefRaw)
if ($briefText.Contains("`r") -or -not $briefText.EndsWith("`n") -or $briefText.EndsWith("`n`n")) { throw 'ACTION_BRIEF_ENCODING_FAIL' }
$childMatch = [regex]::Match($briefText, '(?ms)^## Exact script-byte contract.*?^```powershell\n(?<block>param\(.*?^exit \$exitCode\n)```\n')
$coordinatorMatch = [regex]::Match($briefText, '(?ms)^## Exact coordinator state machine.*?^```powershell\n(?<block>param\(.*?^exit 1\n)```\n')
$runnerMatch = [regex]::Match($briefText, '(?ms)^## Exact host-rendezvous bridge runner.*?^```powershell\n(?<block>param\(.*?^exit \$bridgeExitCode\n)```\n')
if (-not $childMatch.Success -or -not $coordinatorMatch.Success -or -not $runnerMatch.Success) { throw 'ACTION_BLOCK_EXTRACTION_FAIL' }

$childBytes = $utf8NoBom.GetBytes($childMatch.Groups['block'].Value)
$coordinatorBytes = $utf8NoBom.GetBytes($coordinatorMatch.Groups['block'].Value)
$runnerBytes = $utf8NoBom.GetBytes($runnerMatch.Groups['block'].Value)
$childSha256 = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($childBytes))
$coordinatorSha256 = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($coordinatorBytes))
$runnerSha256 = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($runnerBytes))
if ($childBytes.LongLength -ne $ReviewedChildBytes -or $childSha256 -cne $ReviewedChildSha256) { throw 'ACTION_CHILD_BYTES_FAIL' }
if ($coordinatorBytes.LongLength -ne $ReviewedCoordinatorBytes -or $coordinatorSha256 -cne $ReviewedCoordinatorSha256) { throw 'ACTION_COORDINATOR_BYTES_FAIL' }
if ($runnerBytes.LongLength -ne $ReviewedBridgeRunnerBytes -or $runnerSha256 -cne $ReviewedBridgeRunnerSha256) { throw 'ACTION_BRIDGE_RUNNER_BYTES_FAIL' }

$bridgeNonceBytes = [byte[]]::new(16)
[Security.Cryptography.RandomNumberGenerator]::Fill($bridgeNonceBytes)
$bridgeNonce = [Convert]::ToHexString($bridgeNonceBytes)
[Array]::Clear($bridgeNonceBytes, 0, $bridgeNonceBytes.Length)
$bridgeHandle = 'H-' + $bridgeNonce
$bridgeState = 'EXPECT_OPEN'
$bridgeProtocolError = $false
$openRequests = 0
$openResponses = 0
$copyRequests = 0
$copyResponses = 0
$closeRequests = 0
$closeResponses = 0
$coordinatorLines = [Collections.Generic.List[string]]::new()
$coordinatorProcess = $null
$coordinatorExited = $false
$coordinatorExitCode = $null
$coordinatorStderr = $null
$bridgeExitCode = 1

$coordinatorBase64 = [Convert]::ToBase64String($coordinatorBytes)
$commitBase64 = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($ReviewedBriefCommit))
$briefShaBase64 = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($ReviewedBriefSha256))
$nonceBase64 = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($bridgeNonce))
$handleBase64 = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($bridgeHandle))

$wrapperText = @'
$ErrorActionPreference = 'Stop'
$coordinatorText = [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String('__COORDINATOR__'))
$reviewedCommit = [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String('__COMMIT__'))
$reviewedBriefSha = [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String('__BRIEF_SHA__'))
$bridgeNonce = [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String('__NONCE__'))
$bridgeHandle = [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String('__HANDLE__'))

function ConvertTo-Base64Url {
    param([Parameter(Mandatory)] [string]$Value)
    return [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($Value)).TrimEnd('=').Replace('+', '-').Replace('/', '_')
}

$openAdapter = {
    param([string]$DataUrl)
    [Console]::Out.WriteLine('BRIDGE_OPEN_REQUEST|' + $bridgeNonce + '|' + (ConvertTo-Base64Url $DataUrl))
    [Console]::Out.Flush()
    $response = [Console]::In.ReadLine()
    if ($response -cne ('BRIDGE_OPEN_RESPONSE|' + $bridgeNonce + '|' + $bridgeHandle)) { throw 'BRIDGE_OPEN_ABORT' }
    return $bridgeHandle
}
$copyAdapter = {
    param([string]$OpaqueHandle, [string]$AccessibleName)
    if ($OpaqueHandle -cne $bridgeHandle) { throw 'BRIDGE_COPY_HANDLE_FAIL' }
    [Console]::Out.WriteLine('BRIDGE_COPY_REQUEST|' + $bridgeNonce + '|' + $bridgeHandle + '|' + (ConvertTo-Base64Url $AccessibleName))
    [Console]::Out.Flush()
    $response = [Console]::In.ReadLine()
    if ($response -cne ('BRIDGE_COPY_RESPONSE|' + $bridgeNonce + '|' + $bridgeHandle + '|COPY_DONE')) { throw 'BRIDGE_COPY_ABORT' }
    return 'COPY_DONE'
}
$closeAdapter = {
    param([string]$OpaqueHandle)
    if ($OpaqueHandle -cne $bridgeHandle) { throw 'BRIDGE_CLOSE_HANDLE_FAIL' }
    [Console]::Out.WriteLine('BRIDGE_CLOSE_REQUEST|' + $bridgeNonce + '|' + $bridgeHandle)
    [Console]::Out.Flush()
    $response = [Console]::In.ReadLine()
    if ($response -cne ('BRIDGE_CLOSE_RESPONSE|' + $bridgeNonce + '|' + $bridgeHandle + '|PASS')) { throw 'BRIDGE_CLOSE_ABORT' }
    return 'PASS'
}

& ([ScriptBlock]::Create($coordinatorText)) -ReviewedBriefCommit $reviewedCommit -ReviewedBriefSha256 $reviewedBriefSha -OpenExactPage $openAdapter -PerformExactCopy $copyAdapter -CloseExactPage $closeAdapter
'@
$wrapperText = $wrapperText.Replace('__COORDINATOR__', $coordinatorBase64).Replace('__COMMIT__', $commitBase64).Replace('__BRIEF_SHA__', $briefShaBase64).Replace('__NONCE__', $nonceBase64).Replace('__HANDLE__', $handleBase64)
$wrapperEncoded = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($wrapperText))

$startInfo = [Diagnostics.ProcessStartInfo]::new()
$startInfo.FileName = (Get-Command pwsh -ErrorAction Stop).Source
$startInfo.UseShellExecute = $false
$startInfo.CreateNoWindow = $true
$startInfo.RedirectStandardInput = $true
$startInfo.RedirectStandardOutput = $true
$startInfo.RedirectStandardError = $true
foreach ($argument in @('-NoLogo', '-NoProfile', '-NonInteractive', '-EncodedCommand', $wrapperEncoded)) {
    $startInfo.ArgumentList.Add($argument)
}

try {
    $coordinatorProcess = [Diagnostics.Process]::new()
    $coordinatorProcess.StartInfo = $startInfo
    if (-not $coordinatorProcess.Start()) { throw 'BRIDGE_COORDINATOR_START_FAIL' }
    $stderrTask = $coordinatorProcess.StandardError.ReadToEndAsync()
    $coordinatorClock = [Diagnostics.Stopwatch]::StartNew()
    $coordinatorDeadline = [TimeSpan]::FromSeconds($coordinatorTimeoutSeconds)

    while ($true) {
        try {
            $line = Read-LineBeforeDeadline -Reader $coordinatorProcess.StandardOutput -Clock $coordinatorClock -Deadline $coordinatorDeadline -TimeoutCode 'BRIDGE_COORDINATOR_OUTPUT_TIMEOUT' -EofCode 'BRIDGE_COORDINATOR_OUTPUT_EOF'
        } catch {
            if ($_.Exception.Message -ceq 'BRIDGE_COORDINATOR_OUTPUT_EOF') { break }
            throw
        }
        if ($line.StartsWith('BRIDGE_OPEN_REQUEST|', [StringComparison]::Ordinal)) {
            $openRequests++
            if ($bridgeState -cne 'EXPECT_OPEN' -or $openRequests -ne 1 -or $line -cnotmatch ('^BRIDGE_OPEN_REQUEST\|' + $bridgeNonce + '\|[A-Za-z0-9_-]+$')) {
                $bridgeProtocolError = $true
                $response = 'BRIDGE_ABORT|' + $bridgeNonce + '|OPEN'
            } else {
                $bridgeState = 'WAIT_OPEN_RESPONSE'
                [Console]::Out.WriteLine($line)
                [Console]::Out.Flush()
                $responseClock = [Diagnostics.Stopwatch]::StartNew()
                $responseDeadline = [TimeSpan]::FromSeconds($bridgeResponseTimeoutSeconds)
                try {
                    $response = Read-LineBeforeDeadline -Reader ([Console]::In) -Clock $responseClock -Deadline $responseDeadline -TimeoutCode 'BRIDGE_OPEN_RESPONSE_TIMEOUT' -EofCode 'BRIDGE_OPEN_RESPONSE_EOF'
                } catch {
                    $bridgeProtocolError = $true
                    $response = 'BRIDGE_ABORT|' + $bridgeNonce + '|OPEN'
                } finally {
                    $responseClock.Stop()
                }
                $openResponses++
                if ($response -ceq ('BRIDGE_OPEN_RESPONSE|' + $bridgeNonce + '|' + $bridgeHandle)) {
                    $bridgeState = 'OPENED'
                } else {
                    $bridgeProtocolError = $true
                    $bridgeState = 'OPEN_ABORTED'
                    $response = 'BRIDGE_ABORT|' + $bridgeNonce + '|OPEN'
                }
            }
            $coordinatorProcess.StandardInput.WriteLine($response)
            $coordinatorProcess.StandardInput.Flush()
        } elseif ($line.StartsWith('BRIDGE_COPY_REQUEST|', [StringComparison]::Ordinal)) {
            $copyRequests++
            $exactName = ConvertTo-Base64Url 'OmniRoute transport preflight challenge'
            if ($bridgeState -cne 'OPENED' -or $copyRequests -ne 1 -or $line -cne ('BRIDGE_COPY_REQUEST|' + $bridgeNonce + '|' + $bridgeHandle + '|' + $exactName)) {
                $bridgeProtocolError = $true
                $response = 'BRIDGE_ABORT|' + $bridgeNonce + '|COPY'
            } else {
                $bridgeState = 'WAIT_COPY_RESPONSE'
                [Console]::Out.WriteLine($line)
                [Console]::Out.Flush()
                $responseClock = [Diagnostics.Stopwatch]::StartNew()
                $responseDeadline = [TimeSpan]::FromSeconds($bridgeResponseTimeoutSeconds)
                try {
                    $response = Read-LineBeforeDeadline -Reader ([Console]::In) -Clock $responseClock -Deadline $responseDeadline -TimeoutCode 'BRIDGE_COPY_RESPONSE_TIMEOUT' -EofCode 'BRIDGE_COPY_RESPONSE_EOF'
                } catch {
                    $bridgeProtocolError = $true
                    $response = 'BRIDGE_ABORT|' + $bridgeNonce + '|COPY'
                } finally {
                    $responseClock.Stop()
                }
                $copyResponses++
                if ($response -ceq ('BRIDGE_COPY_RESPONSE|' + $bridgeNonce + '|' + $bridgeHandle + '|COPY_DONE')) {
                    $bridgeState = 'COPIED'
                } else {
                    $bridgeProtocolError = $true
                    $bridgeState = 'COPY_ABORTED'
                    $response = 'BRIDGE_ABORT|' + $bridgeNonce + '|COPY'
                }
            }
            $coordinatorProcess.StandardInput.WriteLine($response)
            $coordinatorProcess.StandardInput.Flush()
        } elseif ($line.StartsWith('BRIDGE_CLOSE_REQUEST|', [StringComparison]::Ordinal)) {
            $closeRequests++
            if ($bridgeState -cnotin @('COPIED', 'COPY_ABORTED') -or $closeRequests -ne 1 -or $line -cne ('BRIDGE_CLOSE_REQUEST|' + $bridgeNonce + '|' + $bridgeHandle)) {
                $bridgeProtocolError = $true
                $response = 'BRIDGE_ABORT|' + $bridgeNonce + '|CLOSE'
            } else {
                $bridgeState = 'WAIT_CLOSE_RESPONSE'
                [Console]::Out.WriteLine($line)
                [Console]::Out.Flush()
                $responseClock = [Diagnostics.Stopwatch]::StartNew()
                $responseDeadline = [TimeSpan]::FromSeconds($bridgeResponseTimeoutSeconds)
                try {
                    $response = Read-LineBeforeDeadline -Reader ([Console]::In) -Clock $responseClock -Deadline $responseDeadline -TimeoutCode 'BRIDGE_CLOSE_RESPONSE_TIMEOUT' -EofCode 'BRIDGE_CLOSE_RESPONSE_EOF'
                } catch {
                    $bridgeProtocolError = $true
                    $response = 'BRIDGE_ABORT|' + $bridgeNonce + '|CLOSE'
                } finally {
                    $responseClock.Stop()
                }
                $closeResponses++
                if ($response -ceq ('BRIDGE_CLOSE_RESPONSE|' + $bridgeNonce + '|' + $bridgeHandle + '|PASS')) {
                    $bridgeState = 'CLOSED'
                } else {
                    $bridgeProtocolError = $true
                    $bridgeState = 'CLOSE_ABORTED'
                    $response = 'BRIDGE_ABORT|' + $bridgeNonce + '|CLOSE'
                }
            }
            $coordinatorProcess.StandardInput.WriteLine($response)
            $coordinatorProcess.StandardInput.Flush()
        } elseif ($line.StartsWith('BRIDGE_', [StringComparison]::Ordinal)) {
            $bridgeProtocolError = $true
            throw 'BRIDGE_UNKNOWN_OR_OUT_OF_ORDER_REQUEST'
        } else {
            $coordinatorLines.Add($line)
        }
    }

    $coordinatorClock.Stop()
    $coordinatorProcess.StandardInput.Close()
    $coordinatorExited = $coordinatorProcess.WaitForExit($coordinatorExitTimeoutMilliseconds)
    if (-not $coordinatorExited) { throw 'BRIDGE_COORDINATOR_EXIT_TIMEOUT' }
    $coordinatorExitCode = $coordinatorProcess.ExitCode
    $coordinatorStderr = $stderrTask.GetAwaiter().GetResult()

    $expectedCoordinatorPass = @(
        'MACHINE_OUTPUT_VALID=PASS',
        'RETAINED_HANDLE_EXIT=PASS',
        'EXACT_PREFLIGHT_PAGE_CLOSE=PASS',
        'EXTERNAL_SCRIPT_ABSENCE=PASS',
        'EXTERNAL_TEMP_ROOT_ABSENCE=PASS',
        'PREFLIGHT_ACCEPTANCE=PASS'
    )
    $coordinatorPass = $coordinatorLines.Count -eq $expectedCoordinatorPass.Count
    for ($index = 0; $coordinatorPass -and $index -lt $expectedCoordinatorPass.Count; $index++) {
        if ($coordinatorLines[$index] -cne $expectedCoordinatorPass[$index]) { $coordinatorPass = $false }
    }
    $bridgeCountsPass = $openRequests -eq 1 -and $openResponses -eq 1 -and
        $copyRequests -eq 1 -and $copyResponses -eq 1 -and
        $closeRequests -eq 1 -and $closeResponses -eq 1
    $bridgePass = $coordinatorPass -and $coordinatorExitCode -eq 0 -and
        $coordinatorStderr.Length -eq 0 -and $bridgeState -ceq 'CLOSED' -and
        $bridgeCountsPass -and -not $bridgeProtocolError

    foreach ($coordinatorLine in $coordinatorLines) { $coordinatorLine }
    if ($bridgePass) { 'BRIDGE_PROTOCOL=PASS' } else { 'BRIDGE_PROTOCOL=FAIL' }
    if ($bridgePass) { $bridgeExitCode = 0 }
} catch {
    $bridgeProtocolError = $true
    'BRIDGE_PROTOCOL=FAIL'
} finally {
    if ($null -ne $coordinatorProcess) {
        if (-not $coordinatorExited) {
            try { $coordinatorProcess.StandardInput.Close() } catch {}
        }
        try { $coordinatorProcess.Dispose() } catch {}
    }
    [Array]::Clear($childBytes, 0, $childBytes.Length)
    [Array]::Clear($coordinatorBytes, 0, $coordinatorBytes.Length)
    [Array]::Clear($runnerBytes, 0, $runnerBytes.Length)
    [Array]::Clear($briefRaw, 0, $briefRaw.Length)
}

"BRIDGE_COUNTER_OPEN_REQUESTS=$openRequests"
"BRIDGE_COUNTER_OPEN_RESPONSES=$openResponses"
"BRIDGE_COUNTER_COPY_REQUESTS=$copyRequests"
"BRIDGE_COUNTER_COPY_RESPONSES=$copyResponses"
"BRIDGE_COUNTER_CLOSE_REQUESTS=$closeRequests"
"BRIDGE_COUNTER_CLOSE_RESPONSES=$closeResponses"
if ($bridgeExitCode -eq 0) { 'BRIDGE_ACCEPTANCE=PASS' } else { 'BRIDGE_ACCEPTANCE=FAIL' }
exit $bridgeExitCode
```

The runner's response reader starts one cancellable `ReadLineAsync` per
request, uses a monotonic 45-second deadline, and gives timeout/tie precedence
before inspecting a completed line. EOF, timeout, malformed, duplicate,
unknown, or out-of-order input becomes one canonical `BRIDGE_ABORT` response
to the waiting adapter and then follows the coordinator's existing
`catch`/`finally`; there is no retry. Each request permits at most one host
response line. The nested coordinator is extracted from the committed brief,
passed to a new PowerShell 7 process as an in-memory encoded command, and never
written to another file. That isolation lets its reviewed `exit` execute
without terminating the parent bridge parser.

Exact success protocol:

1. `EXPECT_OPEN` emits
   `BRIDGE_OPEN_REQUEST|<NONCE>|<BASE64URL_DATA_URL>`. The response must be
   exactly `BRIDGE_OPEN_RESPONSE|<NONCE>|H-<NONCE>`.
2. `OPENED` emits
   `BRIDGE_COPY_REQUEST|<NONCE>|H-<NONCE>|<BASE64URL_ACCESSIBLE_NAME>`.
   The response must be exactly
   `BRIDGE_COPY_RESPONSE|<NONCE>|H-<NONCE>|COPY_DONE`.
3. `COPIED` emits `BRIDGE_CLOSE_REQUEST|<NONCE>|H-<NONCE>`. The response
   must be exactly `BRIDGE_CLOSE_RESPONSE|<NONCE>|H-<NONCE>|PASS`.
4. `CLOSED` can produce `BRIDGE_ACCEPTANCE=PASS` only when coordinator
   acceptance is its exact ordered six-line PASS output, coordinator stderr is
   empty, its exit is `0`, all six bridge counters are exactly `1`, and no
   unknown, duplicate, malformed, or out-of-order message occurred.

`H-<NONCE>` is the only PowerShell-visible handle. It is bound to the runtime
CSPRNG nonce and has no browser meaning outside this one rendezvous. The actual
`Tab` object remains only in the persistent Node binding.

## Exact sole-owner Chrome action sequence

The action owner must already have the selected persistent `chrome` binding
required by the Chrome-control skill. The owner starts the exact reviewed
bridge runner in one live PTY with the eight fresh-review pins above. For each
request, the owner reads exactly one complete request line from that PTY,
performs only the corresponding Node block below, and writes the block's one
exact returned response line plus LF through the same PTY. Every Node call has
a 12-second deadline, below both the 45-second bridge-response deadline and the
child's 120-second control deadline.

The execution order is fixed: encode the exact extracted bridge-runner block
plus its literal eight-pin invocation in memory; start it once as
`pwsh -NoLogo -NoProfile -NonInteractive -EncodedCommand <REVIEWED_BASE64>` in
one live PTY; initialize the Node state once; service OPEN, then COPY, then
CLOSE from that PTY; wait for bridge exit; and accept only its exact parser
output. `<REVIEWED_BASE64>` is produced from the fresh reviewed runner bytes
and action-time pins, never from an unreviewed copy. Neither the bridge runner
nor the extracted coordinator is written to a new file.

Initialize once before the first request:

```javascript
let bridgeTab = null;
let bridgeNonce = null;
let bridgeHandle = null;
let bridgeState = 'IDLE';
const bridgeNodeDeadlineMs = 12000;
const bridgeWithinDeadline = async (operation, code) => {
  let timer;
  try {
    return await Promise.race([
      operation(),
      new Promise((_, reject) => { timer = setTimeout(() => reject(new Error(code)), bridgeNodeDeadlineMs); }),
    ]);
  } finally {
    clearTimeout(timer);
  }
};
```

For the single open request, substitute the two exact observed request fields
as JSON string literals. Decode only the supplied non-secret data URL. There
is exactly one `chrome.tabs.new()` and one `goto(dataUrl)`. If either operation
fails, close the exact created tab once when it exists, retain no replacement,
and return exact `BRIDGE_ABORT|<NONCE>|OPEN` only after that close attempt has
settled; there is no alternate tab or retry.

```javascript
bridgeNonce = <OPEN_NONCE_JSON>;
const bridgeDataUrlBase64 = <OPEN_DATA_URL_BASE64URL_JSON>;
bridgeHandle = `H-${bridgeNonce}`;
try {
  if (!/^[0-9A-F]{32}$/.test(bridgeNonce) || bridgeState !== 'IDLE') throw new Error('OPEN_REQUEST_REJECTED');
  const bridgeDataUrl = Buffer.from(bridgeDataUrlBase64, 'base64url').toString('utf8');
  if (!bridgeDataUrl.startsWith('data:text/html;charset=utf-8,')) throw new Error('OPEN_DATA_URL_REJECTED');
  bridgeState = 'OPENING';
  bridgeTab = await bridgeWithinDeadline(() => chrome.tabs.new(), 'OPEN_NEW_TIMEOUT');
  await bridgeWithinDeadline(() => bridgeTab.goto(bridgeDataUrl), 'OPEN_GOTO_TIMEOUT');
  bridgeState = 'OPENED';
  `BRIDGE_OPEN_RESPONSE|${bridgeNonce}|${bridgeHandle}`;
} catch (error) {
  bridgeState = 'OPEN_ABORTED';
  if (bridgeTab !== null) {
    try {
      await bridgeWithinDeadline(() => bridgeTab.close(), 'OPEN_CLOSE_TIMEOUT');
      bridgeTab = null;
    } catch (closeError) {
      bridgeState = 'OPEN_ABORT_RETAINED';
    }
  }
  `BRIDGE_ABORT|${bridgeNonce}|OPEN`;
}
```

For the single copy request, substitute its exact nonce and opaque-handle
fields as JSON string literals and require equality with the retained values.
The accessible-name field must decode to the one literal below. Focus is one
semantic-locator click, never coordinates. Perform one `Control+A` and one
`Control+C`. On any failure, keep the retained tab, return exact
`BRIDGE_ABORT|<NONCE>|COPY`, and wait for the coordinator's later close request.

```javascript
const copyNonce = <COPY_NONCE_JSON>;
const copyHandle = <COPY_HANDLE_JSON>;
const copyAccessibleNameBase64 = <COPY_ACCESSIBLE_NAME_BASE64URL_JSON>;
const copyAccessibleName = Buffer.from(copyAccessibleNameBase64, 'base64url').toString('utf8');
try {
  if (bridgeState !== 'OPENED' || copyNonce !== bridgeNonce || copyHandle !== bridgeHandle || copyAccessibleName !== 'OmniRoute transport preflight challenge') throw new Error('COPY_REQUEST_REJECTED');
  bridgeState = 'COPYING';
  const challengeField = bridgeTab.playwright.getByLabel('OmniRoute transport preflight challenge',{exact:true});
  await bridgeWithinDeadline(() => challengeField.click(), 'COPY_FOCUS_TIMEOUT');
  await bridgeWithinDeadline(() => challengeField.press('Control+A'), 'COPY_SELECT_TIMEOUT');
  await bridgeWithinDeadline(() => challengeField.press('Control+C'), 'COPY_COPY_TIMEOUT');
  bridgeState = 'COPIED';
  `BRIDGE_COPY_RESPONSE|${bridgeNonce}|${bridgeHandle}|COPY_DONE`;
} catch (error) {
  bridgeState = 'COPY_ABORTED';
  `BRIDGE_ABORT|${bridgeNonce}|COPY`;
}
```

For the single close request, substitute its exact fields as JSON string
literals. It is valid after copy success or copy abort only, and it closes only
the retained tab with exactly one `tab.close()`. Only exact `PASS` is accepted.

```javascript
const closeNonce = <CLOSE_NONCE_JSON>;
const closeHandle = <CLOSE_HANDLE_JSON>;
try {
  if (!['COPIED', 'COPY_ABORTED'].includes(bridgeState) || closeNonce !== bridgeNonce || closeHandle !== bridgeHandle || bridgeTab === null) throw new Error('CLOSE_REQUEST_REJECTED');
  bridgeState = 'CLOSING';
  await bridgeWithinDeadline(() => bridgeTab.close(), 'CLOSE_TIMEOUT');
  bridgeTab = null;
  bridgeState = 'CLOSED';
  `BRIDGE_CLOSE_RESPONSE|${bridgeNonce}|${bridgeHandle}|PASS`;
} catch (error) {
  bridgeState = 'CLOSE_ABORTED';
  `BRIDGE_ABORT|${bridgeNonce}|CLOSE`;
}
```

The host performs no DOM snapshot, screenshot, content extraction, title or
URL lookup, browser clipboard API call, coordinate action, reload, alternate
tab, fallback, or retry. On open failure it attempts closure of the exact
created tab before responding ABORT. On copy failure it responds ABORT without
closing, then closes only the retained tab when the coordinator requests it.
Any Node deadline, ABORT, EOF, invalid response, or tool error is terminal and
converges through the bridge and coordinator cleanup states; the owner does
not improvise another response or action.

## Structural counters and non-overlap

| Counter | Preflight maximum | Later credential stage |
| --- | ---: | ---: |
| fixed processes | `1` | credential-owner process exactly `1` only under a later gate |
| simultaneous preflight/credential processes | preflight must exit first | never overlap |
| local pages / bridge handles | `1 / 1` | separately reviewed later page only |
| bridge open/copy/close requests | `1 / 1 / 1` on PASS | separately counted |
| bridge open/copy/close responses | `1 / 1 / 1` on PASS | separately counted |
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

Stop after committing this one ignored brief and writing its ignored fix-round-4
report. A fresh independent Sol High reviewer must verify the direct committed
bytes; exact child, coordinator, and bridge-runner extraction; strict encoding;
single committed-path scope; no unresolved marker or secret; static syntax and
structure; both bounded async-read tie rules; exact bridge state/counter parser;
cleanup/deletion guards; prohibited-action scan; and every authority boundary
above. `FAIL / REVISE` authorizes nothing. Even a future PASS authorizes only a
later explicit preflight action-time decision.
