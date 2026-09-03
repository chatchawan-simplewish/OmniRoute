globalThis.secureConsoleV56Module = null;
try {
  const { readFileSync } = await import("node:fs");
  const { createHash } = await import("node:crypto");
  const modulePath = "C:/ChatGPT Projects/SW-Selfhosted-Network/.worktrees/omniroute-agent-routing-source/.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v56-disk-module-executable.mjs";
  const moduleUrl = "file:///C:/ChatGPT%20Projects/SW-Selfhosted-Network/.worktrees/omniroute-agent-routing-source/.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v56-disk-module-executable.mjs";
  const expectedBytes = 26875;
  const expectedSha256 = "932A9A06331C5683AB68471E7DA6E9AB9277819722323405B7711CFFB1B25CAA";
  const moduleBytes = readFileSync(modulePath);
  const moduleSha256 = createHash("sha256").update(moduleBytes).digest("hex").toUpperCase();
  if (moduleBytes.length !== expectedBytes || moduleSha256 !== expectedSha256 ||
      moduleBytes.some((byte) => byte > 0x7F)) {
    throw new Error("V56_DISK_MODULE_FIDELITY_FAILED");
  }
  globalThis.secureConsoleV56Module =
    await import(moduleUrl + "?sha256=" + moduleSha256);
} catch (error) {
  globalThis.secureConsoleV56Module = null;
  throw error;
}
