globalThis.secureConsoleV57Module = null;
try {
  const { readFileSync } = await import("node:fs");
  const { createHash } = await import("node:crypto");
  const { createContext, SourceTextModule, SyntheticModule } = await import("node:vm");
  const modulePath = "C:/ChatGPT Projects/SW-Selfhosted-Network/.worktrees/omniroute-agent-routing-source/.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v57-vm-module-executable.mjs";
  const browserClientUrl = "file:///C:/Users/chatc/.codex/plugins/cache/openai-bundled/chrome/26.901.20858/scripts/browser-client.mjs";
  const expectedBytes = 27336;
  const expectedSha256 = "48DD581AE424042D42002AA8D32D017B7156A65CEE729A983BFB878200051A38";
  if (typeof createContext !== "function" ||
      typeof SourceTextModule !== "function" ||
      typeof SyntheticModule !== "function") {
    throw new Error("V57_VM_MODULE_UNAVAILABLE");
  }
  const moduleBytes = readFileSync(modulePath);
  const moduleSha256 = createHash("sha256").update(moduleBytes).digest("hex").toUpperCase();
  if (moduleBytes.length !== expectedBytes ||
      moduleSha256 !== expectedSha256 ||
      !moduleBytes.every((byte) => byte < 128)) {
    throw new Error("V57_VM_MODULE_FIDELITY_FAILED");
  }
  let bridgeCount = 0;
  const context = createContext({ nodeRepl, URL });
  const sourceModule = new SourceTextModule(moduleBytes.toString("utf8"), {
    context,
    identifier: modulePath,
    importModuleDynamically: async (specifier) => {
      if (specifier !== browserClientUrl || bridgeCount !== 0) {
        throw new Error("V57_DYNAMIC_IMPORT_REJECTED");
      }
      bridgeCount++;
      const browserClient = await import(browserClientUrl);
      if (typeof browserClient.setupBrowserRuntime !== "function") {
        throw new Error("V57_BROWSER_BRIDGE_SHAPE_FAILED");
      }
      const bridge = new SyntheticModule(["setupBrowserRuntime"], function () {
        this.setExport("setupBrowserRuntime", browserClient.setupBrowserRuntime);
      }, { context, identifier: browserClientUrl });
      await bridge.link(() => { throw new Error("V57_BRIDGE_STATIC_IMPORT_REJECTED"); });
      await bridge.evaluate();
      return bridge;
    },
  });
  await sourceModule.link(() => { throw new Error("V57_STATIC_IMPORT_REJECTED"); });
  await sourceModule.evaluate();
  if (bridgeCount !== 1) throw new Error("V57_DYNAMIC_IMPORT_COUNT_FAILED");
  globalThis.secureConsoleV57Module = sourceModule.namespace;
} catch (error) {
  globalThis.secureConsoleV57Module = null;
  throw error;
}
