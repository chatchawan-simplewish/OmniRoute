import { createRequire } from "node:module";
import { join, resolve } from "node:path";
import { pathToFileURL } from "node:url";
import { selectTlsClientAsset, verifyTlsClientFile } from "./installPinnedTlsClient.mjs";

export async function smokePinnedTlsClient(file, rootDir = process.cwd()) {
  // Hash + real architecture checked before dlopen. No provider request is made.
  await verifyTlsClientFile(file);
  const require = createRequire(join(resolve(rootDir), "package.json"));
  if (require("tls-client-node/package.json").version !== "0.2.0") throw new Error("Unexpected TLS loader version");
  const originalFetch = globalThis.fetch;
  globalThis.fetch = async () => { throw new Error("Network prohibited in pinned TLS smoke"); };
  try {
    const { TLSClient } = require("tls-client-node");
    const client = new TLSClient({ runtimeMode: "native", nativeLibraryPath: file });
    await client.start(); // koffi loads the real library and binds all five ABI symbols.
    await client.stop(); // Native destroyAll executes and its response is decoded/freed.
  } finally { globalThis.fetch = originalFetch; }
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  const file = process.argv[2] ?? join(process.cwd(), "node_modules", "tls-client-node", "bin", selectTlsClientAsset().filename);
  await smokePinnedTlsClient(file);
  console.log("Pinned TLS native start/stop passed without network");
}
