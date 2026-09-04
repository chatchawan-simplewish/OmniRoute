import assert from "node:assert/strict";
import test from "node:test";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

const dataDir = fs.mkdtempSync(path.join(os.tmpdir(), "omniroute-agent-route-events-"));
process.env.DATA_DIR = dataDir;
process.env.API_KEY_SECRET = "agent-route-events-test-secret";

const core = await import("../../../src/lib/db/core.ts");
const apiKeys = await import("../../../src/lib/db/apiKeys.ts");
const route = await import("../../../src/app/api/v1/agent-routes/events/route.ts");
const runs = await import("../../../src/lib/db/agentRouteRuns.ts");

const ids = {
  task: "00000000-0000-4000-8000-000000000011",
  turn: "00000000-0000-4000-8000-000000000012",
  run: "00000000-0000-4000-8000-000000000013",
  idempotency: "00000000-0000-4000-8000-000000000014",
  event: "00000000-0000-4000-8000-000000000015",
};

test.beforeEach(async () => {
  core.resetDbInstance();
  apiKeys.resetApiKeyState();
  fs.rmSync(dataDir, { recursive: true, force: true });
  fs.mkdirSync(dataDir, { recursive: true });
  await core.ensureDbInitialized();
});
test.after(() => {
  core.resetDbInstance();
  fs.rmSync(dataDir, { recursive: true, force: true });
});

async function ownedKey(noLog: boolean) {
  const key = await apiKeys.createApiKey("agent-events", "agent-events-test");
  await apiKeys.updateApiKeyPermissions(key.id, { noLog, allowedModels: ["agent/normal"] });
  runs.createOrResumeAgentRouteRun({
    runId: ids.run,
    apiKeyId: key.id,
    taskId: ids.task,
    turnId: ids.turn,
    idempotencyKey: ids.idempotency,
    virtualRoute: "agent/normal",
    effectiveReviewClass: "standard",
  });
  return key;
}

function request(key: string, extra: RequestInit = {}) {
  return new Request("http://localhost/api/v1/agent-routes/events", {
    method: "POST",
    headers: {
      authorization: `Bearer ${key}`,
      "content-type": "application/json",
      "x-omniroute-task-id": ids.task,
      "x-omniroute-run-id": ids.run,
      "x-omniroute-turn-id": ids.turn,
      "x-omniroute-idempotency-key": ids.idempotency,
      ...extra.headers,
    },
    body: JSON.stringify({
      event_id: ids.event,
      task_id: ids.task,
      run_id: ids.run,
      turn_id: ids.turn,
      idempotency_key: ids.idempotency,
      kind: "output_started",
      occurred_at: "2026-08-30T12:00:00.000Z",
    }),
    ...extra,
  });
}

test("requires a valid no-log bearer key and accepts an owned lifecycle event idempotently", async () => {
  assert.equal((await route.POST(request("missing"))).status, 401);
  const ordinary = await apiKeys.createApiKey("ordinary", "agent-events-test");
  await apiKeys.updateApiKeyPermissions(ordinary.id, { noLog: false });
  assert.equal((await route.POST(request(ordinary.key))).status, 403);
  const key = await ownedKey(true);
  assert.equal((await route.POST(request(key.key))).status, 202);
  assert.equal((await route.POST(request(key.key))).status, 202);
});

test("rejects query, secondary credentials, and recursive payload-bearing fields", async () => {
  const key = await ownedKey(true);
  assert.equal((await route.POST(new Request("http://localhost/api/v1/agent-routes/events?x=1", request(key.key)))).status, 400);
  assert.equal((await route.POST(request(key.key, { headers: { cookie: "session=secret" } }))).status, 400);
  const unsafe = request(key.key);
  const body = await unsafe.json();
  body.details = { authorization: "secret" };
  assert.equal(
    (await route.POST(
      new Request("http://localhost/api/v1/agent-routes/events", {
        method: "POST",
        headers: unsafe.headers,
        body: JSON.stringify(body),
      })
    )).status,
    400
  );
});
