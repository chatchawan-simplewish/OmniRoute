import { isAbsolute, join } from "node:path";
import { resolveDataDir } from "@/lib/dataPaths";

/**
 * Writable cache directory for tls-client-node's native binary.
 *
 * Without an explicit `downloadDir`, the library defaults to its own package
 * `node_modules/tls-client-node/bin`, which is root-owned on global installs
 * and fails with EACCES for normal users (#8579).
 */
export function resolveTlsClientDownloadDir(): string {
  return join(resolveDataDir(), "tls-client", "bin");
}

export function buildNativeTlsClientOptions(): {
  runtimeMode: "native";
  downloadDir?: string;
  nativeLibraryPath?: string;
} {
  // Docker supplies a checksum-verified, root-owned image asset. An explicit
  // native path bypasses the package's mutable cache and runtime GitHub lookup.
  const nativeLibraryPath = process.env.OMNIROUTE_TLS_NATIVE_LIBRARY;
  if (nativeLibraryPath) {
    if (!isAbsolute(nativeLibraryPath)) throw new Error("OMNIROUTE_TLS_NATIVE_LIBRARY must be absolute");
    return { runtimeMode: "native", nativeLibraryPath };
  }
  return {
    runtimeMode: "native",
    downloadDir: resolveTlsClientDownloadDir(),
  };
}
