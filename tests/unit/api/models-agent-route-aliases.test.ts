import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import test from "node:test";

const testDataDir = fs.mkdtempSync(path.join(os.tmpdir(), "omniroute-agent-route-catalog-"));
process.env.DATA_DIR = testDataDir;
process.env.API_KEY_SECRET = process.env.API_KEY_SECRET || "agent-route-catalog-test-secret";

const core = await import("../../../src/lib/db/core.ts");
const apiKeysDb = await import("../../../src/lib/db/apiKeys.ts");
const settingsDb = await import("../../../src/lib/db/settings.ts");
const agentRoute = await import("../../../open-sse/services/agentRoute.ts");

async function loadCatalog() {
  return import("../../../src/app/api/v1/models/catalog.ts");
}

async function loadRoute() {
  return import("../../../src/app/api/v1/models/route.ts");
}

async function resetStorage() {
  core.resetDbInstance();
  apiKeysDb.resetApiKeyState();
  fs.rmSync(testDataDir, { recursive: true, force: true });
  fs.mkdirSync(testDataDir, { recursive: true });
  (await loadCatalog()).__resetCatalogBuilderRunsForTest();
}

async function modelIdsFor(key: string) {
  const response = await (
    await loadRoute()
  ).GET(
    new Request("http://localhost/api/v1/models", { headers: { authorization: `Bearer ${key}` } })
  );
  assert.equal(response.status, 200);
  return ((await response.json()) as { data: Array<{ id: string }> }).data.map(({ id }) => id);
}

test.beforeEach(resetStorage);
test.after(async () => {
  await resetStorage();
  fs.rmSync(testDataDir, { recursive: true, force: true });
});

test("an authenticated no-log key authorized for slash aliases sees only both aliases", async () => {
  assert.equal(agentRoute.isAgentRouteAlias("agent/normal"), true);
  await settingsDb.updateSettings({
    requireLogin: true,
    password: "hashed",
    requireAuthForModels: true,
  });
  const key = await apiKeysDb.createApiKey("agent-route", "agent-route-test");
  await apiKeysDb.updateApiKeyPermissions(key.id, {
    noLog: true,
    allowedModels: ["agent/normal", "agent/high"],
  });

  assert.deepEqual(await modelIdsFor(key.key), ["agent/normal", "agent/high"]);
});

test("ordinary or unauthorized keys do not see slash aliases", async () => {
  assert.equal(agentRoute.isAgentRouteAlias("agent/high"), true);
  await settingsDb.updateSettings({
    requireLogin: true,
    password: "hashed",
    requireAuthForModels: true,
  });
  const ordinary = await apiKeysDb.createApiKey("ordinary", "agent-route-test");

  assert.equal(
    (await modelIdsFor(ordinary.key)).some((id) => id.startsWith("agent/")),
    false
  );
  const unauthorized = await (
    await loadCatalog()
  ).getUnifiedModelsResponse(
    new Request("http://localhost/api/v1/models", { headers: { authorization: "Bearer invalid" } })
  );
  assert.equal(unauthorized.status, 401);
});

test("existing hyphen aliases remain distinct and catalog lookup cannot dispatch a slash alias", async () => {
  assert.equal(agentRoute.isAgentRouteAlias("agent-normal"), false);
  await settingsDb.updateSettings({
    requireLogin: true,
    password: "hashed",
    requireAuthForModels: true,
  });
  const key = await apiKeysDb.createApiKey("agent-route", "agent-route-test");
  await apiKeysDb.updateApiKeyPermissions(key.id, {
    noLog: true,
    allowedModels: ["agent/normal", "agent/high", "agent-normal", "agent-high"],
  });

  const originalFetch = globalThis.fetch;
  let providerDispatches = 0;
  globalThis.fetch = (async () => {
    providerDispatches++;
    throw new Error("/v1/models must not dispatch an agent provider");
  }) as typeof globalThis.fetch;
  try {
    const ids = await modelIdsFor(key.key);
    assert.deepEqual(
      ids.filter((id) => id.startsWith("agent")),
      ["agent-normal", "agent-high", "agent/normal", "agent/high"]
    );
    assert.equal(ids.includes("agent/normal"), true);
    assert.equal(providerDispatches, 0, "/v1/models must not dispatch an agent provider");
  } finally {
    globalThis.fetch = originalFetch;
  }
});
