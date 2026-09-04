import test from "node:test";
import assert from "node:assert/strict";
import { dirname, join, resolve } from "node:path";
import { mkdtemp, mkdir, readFile, readdir, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { createRequire } from "node:module";
import { runInNewContext } from "node:vm";
import { buildNativeTlsClientOptions } from "../../../open-sse/services/tlsClientDownloadDir.ts";
import { installPinnedTlsClient, selectTlsClientAsset, verifyTlsClientBytes } from "../../../scripts/build/installPinnedTlsClient.mjs";

test("Docker immutable TLS library bypasses writable cache and runtime release lookup", async () => {
  const original = process.env.OMNIROUTE_TLS_NATIVE_LIBRARY;
  const originalFetch = globalThis.fetch;
  try {
    const libraryPath = resolve("fixture-immutable", "tls-client.so");
    process.env.OMNIROUTE_TLS_NATIVE_LIBRARY = libraryPath;
    assert.deepEqual(buildNativeTlsClientOptions(), { runtimeMode: "native", nativeLibraryPath: libraryPath });
    globalThis.fetch = async () => { throw new Error("runtime network must not be used"); };
    const { ensureNativeLibrary } = await import("../../../node_modules/tls-client-node/dist/binary.js");
    assert.equal((await ensureNativeLibrary(buildNativeTlsClientOptions())).libraryPath, libraryPath);
    process.env.OMNIROUTE_TLS_NATIVE_LIBRARY = "relative/untrusted.so";
    assert.throws(() => buildNativeTlsClientOptions(), /absolute/);
    delete process.env.OMNIROUTE_TLS_NATIVE_LIBRARY;
    assert.equal(typeof buildNativeTlsClientOptions().downloadDir, "string");
  } finally {
    globalThis.fetch = originalFetch;
    if (original === undefined) delete process.env.OMNIROUTE_TLS_NATIVE_LIBRARY;
    else process.env.OMNIROUTE_TLS_NATIVE_LIBRARY = original;
  }
});

test("both pinned xgo assets remain discoverable by the actual locked Linux loader", async () => {
  const require = createRequire(import.meta.url);
  const loaderPath = join(dirname(require.resolve("tls-client-node/package.json")), "dist", "binary.js");
  const loader = await readFile(loaderPath, "utf8");
  for (const [arch, assetName, filename] of [
    ["x64", "tls-client-xgo-1.16.0-linux-amd64.so", "tls-client-linux-ubuntu-amd64-1.16.0.so"],
    ["arm64", "tls-client-xgo-1.16.0-linux-arm64.so", "tls-client-linux-arm64-1.16.0.so"],
  ]) {
    const asset = selectTlsClientAsset("linux", arch);
    assert.equal(asset.url, "https://github.com/bogdanfinn/tls-client/releases/download/v1.16.0/" + assetName);
    assert.equal(asset.filename, filename);
    const bin = await mkdtemp(join(tmpdir(), "omni-pinned-tls-discovery-"));
    await writeFile(join(bin, filename), "discovery fixture; never loaded");
    const module = { exports: {} as any };
    const evaluate = runInNewContext("(function(require,module,exports,process){" + loader + "\n})", { fetch: async () => { throw new Error("loader must not download"); } });
    evaluate(createRequire(loaderPath), module, module.exports, { platform: "linux", arch });
    const found = await module.exports.ensureNativeLibrary({ downloadDir: bin, version: "1.16.0" });
    assert.equal(found.libraryPath, join(bin, filename));
    assert.equal(found.version, "1.16.0");
  }
  assert.throws(() => selectTlsClientAsset("linux", "ia32"), /Unsupported/);
  assert.throws(() => selectTlsClientAsset("win32", "x64"), /Unsupported/);
});

test("checksum or version mismatch fails installation before an executable file is created", async () => {
  const rootDir = await mkdtemp(join(tmpdir(), "omni-pinned-tls-install-"));
  const packageDir = join(rootDir, "node_modules", "tls-client-node");
  await mkdir(packageDir, { recursive: true });
  await writeFile(join(packageDir, "package.json"), JSON.stringify({ name: "tls-client-node", version: "0.2.0" }));
  let downloads = 0;
  const options = { rootDir, platform: "linux", arch: "x64", fetchImpl: async (url: string) => {
    downloads++;
    assert.equal(url, "https://github.com/bogdanfinn/tls-client/releases/download/v1.16.0/tls-client-xgo-1.16.0-linux-amd64.so");
    return new Response("tampered artifact");
  } };
  await assert.rejects(installPinnedTlsClient(options), /SHA256 mismatch/);
  assert.equal(downloads, 1);
  assert.deepEqual(await readdir(packageDir), ["package.json"]);
  const candidate = Buffer.alloc(17412432);
  candidate.set([0x7f, 0x45, 0x4c, 0x46, 2, 1]);
  candidate.writeUInt16LE(62, 18);
  assert.throws(() => verifyTlsClientBytes(candidate, "linux", "x64"), /SHA256 mismatch/);
  await writeFile(join(packageDir, "package.json"), JSON.stringify({ name: "tls-client-node", version: "0.3.0" }));
  await assert.rejects(installPinnedTlsClient(options), /locked tls-client-node/);
  assert.equal(downloads, 1, "unknown loader ABI must fail before downloading");
});
