import { createHash } from "node:crypto";
import { lstat, mkdir, readFile, writeFile } from "node:fs/promises";
import { join, resolve } from "node:path";
import { pathToFileURL } from "node:url";

// Official v1.16.0 release metadata, verified 2026-09-04. Do not resolve latest.
const assets = Object.freeze({
  x64: Object.freeze({ asset: "tls-client-xgo-1.16.0-linux-amd64.so", filename: "tls-client-linux-ubuntu-amd64-1.16.0.so", size: 17412432, machine: 62, sha256: "75f19133e3cb9b16ab3d2dfe3376c7590aab2fe6f2294debac661bfd63dca6a3" }),
  arm64: Object.freeze({ asset: "tls-client-xgo-1.16.0-linux-arm64.so", filename: "tls-client-linux-arm64-1.16.0.so", size: 16398336, machine: 183, sha256: "91f88d35fa64284c811373003d2a26caa3145eaeefd1c0e9576f10724a914332" }),
});

export function selectTlsClientAsset(platform = process.platform, arch = process.arch) {
  if (platform !== "linux" || !Object.hasOwn(assets, arch)) throw new Error(`Unsupported pinned TLS platform: ${platform}/${arch}`);
  const asset = assets[arch];
  return { ...asset, version: "1.16.0", url: `https://github.com/bogdanfinn/tls-client/releases/download/v1.16.0/${asset.asset}` };
}

export function verifyTlsClientBytes(bytes, platform = process.platform, arch = process.arch) {
  const asset = selectTlsClientAsset(platform, arch);
  const sha256 = createHash("sha256").update(bytes).digest("hex");
  if (bytes.length !== asset.size || sha256 !== asset.sha256) throw new Error("Pinned TLS artifact size/SHA256 mismatch");
  if (bytes.subarray(0, 4).toString("hex") !== "7f454c46" || bytes[4] !== 2 || bytes[5] !== 1 || bytes.readUInt16LE(18) !== asset.machine) throw new Error("Pinned TLS artifact ELF architecture mismatch");
  return asset;
}

export async function verifyTlsClientFile(file, platform = process.platform, arch = process.arch) {
  if (!(await lstat(file)).isFile()) throw new Error("Pinned TLS artifact must be a regular file");
  return verifyTlsClientBytes(await readFile(file), platform, arch);
}

export async function installPinnedTlsClient({ rootDir = process.cwd(), platform = process.platform, arch = process.arch, fetchImpl = globalThis.fetch } = {}) {
  const asset = selectTlsClientAsset(platform, arch);
  const packageDir = join(rootDir, "node_modules", "tls-client-node");
  const metadata = JSON.parse(await readFile(join(packageDir, "package.json"), "utf8"));
  if (metadata.name !== "tls-client-node" || metadata.version !== "0.2.0") throw new Error("Pinned TLS loader requires locked tls-client-node 0.2.0");
  const file = join(packageDir, "bin", asset.filename);
  try {
    await lstat(file);
    await verifyTlsClientFile(file, platform, arch);
    return file;
  } catch (error) {
    if (error.code !== "ENOENT") throw error; // Never overwrite a mismatched existing artifact.
  }
  const response = await fetchImpl(asset.url, { signal: AbortSignal.timeout(120_000) });
  if (!response.ok || !response.body) throw new Error(`Pinned TLS download failed: HTTP ${response.status}`);
  const reader = response.body.getReader(), chunks = [];
  let size = 0;
  try {
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      size += value.length;
      if (size > asset.size) throw new Error("Pinned TLS download exceeds expected size");
      chunks.push(value);
    }
  } catch (error) { await reader.cancel(); throw error; }
  finally { reader.releaseLock(); }
  const bytes = Buffer.concat(chunks);
  verifyTlsClientBytes(bytes, platform, arch); // Verify before materializing executable content.
  await mkdir(join(packageDir, "bin"), { recursive: true });
  await writeFile(file, bytes, { flag: "wx", mode: 0o644 });
  return file;
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  const file = await installPinnedTlsClient();
  console.log(`Pinned TLS v1.16.0 verified: ${file}`);
}
