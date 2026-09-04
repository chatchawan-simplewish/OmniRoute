using System;
using System.IO;
using System.Runtime.InteropServices;
using System.Text;
using Microsoft.Win32.SafeHandles;
public static class V64ExactReader {
    [StructLayout(LayoutKind.Sequential)]
    private struct FileTime { public uint Low; public uint High; }
    [StructLayout(LayoutKind.Sequential)]
    private struct FileInfo {
        public uint Attributes;
        public FileTime Creation, Access, Write;
        public uint Volume, SizeHigh, SizeLow, Links, IndexHigh, IndexLow;
    }
    [DllImport("kernel32.dll", CharSet=CharSet.Unicode, ExactSpelling=true, SetLastError=true)]
    private static extern SafeFileHandle CreateFileW(string path, uint access, uint share, IntPtr security, uint disposition, uint flags, IntPtr template);
    [DllImport("kernel32.dll", ExactSpelling=true, SetLastError=true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool GetFileInformationByHandle(SafeFileHandle handle, out FileInfo info);
    [DllImport("kernel32.dll", CharSet=CharSet.Unicode, ExactSpelling=true, SetLastError=true)]
    private static extern uint GetFinalPathNameByHandleW(SafeFileHandle handle, StringBuilder path, uint capacity, uint flags);
    [DllImport("kernel32.dll", ExactSpelling=true, SetLastError=true)]
    private static extern uint GetFileType(SafeFileHandle handle);
    [DllImport("kernel32.dll", ExactSpelling=true, SetLastError=true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool ReadFile(SafeFileHandle handle, [Out] byte[] bytes, uint requested, out uint read, IntPtr overlapped);
    private static long Time(FileTime value) { return ((long)value.High << 32) | value.Low; }
    private static void RequirePath(SafeFileHandle handle, string expected) {
        var value = new StringBuilder(1024);
        uint length = GetFinalPathNameByHandleW(handle,value,1024,0);
        if (length == 0 || length >= 1024 || !String.Equals(value.ToString(), @"\\?\" + expected, StringComparison.Ordinal))
            throw new InvalidOperationException("V64_HANDLE_PATH");
    }
    private static FileInfo RequireInfo(SafeFileHandle handle, long creation, long lastWrite) {
        FileInfo info;
        if (!GetFileInformationByHandle(handle,out info) || GetFileType(handle) != 1 ||
            (info.Attributes & 0x1410) != 0 || info.SizeHigh != 0 || info.SizeLow != 476 ||
            info.Links != 1 || Time(info.Creation) != creation || Time(info.Write) != lastWrite)
            throw new InvalidOperationException("V64_HANDLE_METADATA");
        return info;
    }
    public static byte[] ReadExact(string path, long creation, long lastWrite) {
        if (!Path.IsPathFullyQualified(path) || !String.Equals(Path.GetFullPath(path),path,StringComparison.Ordinal))
            throw new InvalidOperationException("V64_INPUT_PATH");
        // GENERIC_READ, FILE_SHARE_READ only, OPEN_EXISTING, OPEN_REPARSE_POINT.
        // No creation, write/delete access, following final links, or retry.
        using (var handle = CreateFileW(path,0x80000000,1,IntPtr.Zero,3,0x00200000,IntPtr.Zero)) {
            if (handle.IsInvalid) throw new InvalidOperationException("V64_OPEN_FAILED");
            RequirePath(handle,path);
            var before = RequireInfo(handle,creation,lastWrite);
            var bytes = new byte[476];
            bool returned = false;
            try {
                uint read;
                if (!ReadFile(handle,bytes,476,out read,IntPtr.Zero) || read != 476)
                    throw new InvalidOperationException("V64_BOUNDED_READ_FAILED");
                var after = RequireInfo(handle,creation,lastWrite);
                RequirePath(handle,path);
                if (before.Volume != after.Volume || before.IndexHigh != after.IndexHigh ||
                    before.IndexLow != after.IndexLow || before.Attributes != after.Attributes)
                    throw new InvalidOperationException("V64_HANDLE_IDENTITY_DRIFT");
                returned = true;
                return bytes;
            } finally { if (!returned) Array.Clear(bytes,0,bytes.Length); }
        }
    }
}
