import test from "node:test";
import assert from "node:assert/strict";
import { randomUUID } from "node:crypto";

process.env.API_KEY_SECRET = "agent-route-fixture-only";
process.env.OMNIROUTE_DISABLE_BACKGROUND_SERVICES = "true";
const core = await import("../../src/lib/db/core.ts");
const providers = await import("../../src/lib/db/providers.ts");
const keys = await import("../../src/lib/db/apiKeys.ts");
const settings = await import("../../src/lib/db/settings.ts");
const { handleChat } = await import("../../src/sse/handlers/chat.ts");
const chatEndpoint = await import("../../src/app/api/v1/chat/completions/route.ts");
const responsesEndpoint = await import("../../src/app/api/v1/responses/route.ts");
const eventsEndpoint = await import("../../src/app/api/v1/agent-routes/events/route.ts");
const { getAgentRouteTurn } = await import("../../src/lib/db/agentRouteRuns.ts");
const { initTranslators } = await import("../../open-sse/translator/index.ts");
const { resetAllCircuitBreakers } = await import("../../src/shared/utils/circuitBreaker.ts");
const { clearProviderFailure } = await import("../../open-sse/services/accountFallback.ts");
const { getProviderCredentials, clearAccountError } = await import("../../src/sse/services/auth.ts");
const { upsertSessionAccountAffinity } = await import("../../src/lib/db/sessionAccountAffinity.ts");
const originalFetch = globalThis.fetch;
const marker = "private-task-marker-" + randomUUID();
let key: any, binding: any;
const calls: any[] = [];

test.before(async () => {
  await core.ensureDbInitialized();
  await initTranslators();
  await settings.updateSettings({ requireApiKey: true, semanticCacheEnabled: true, call_log_pipeline_enabled: true, logToolSources: true, promptCompressionEnabled: false });
  const connection = await providers.createProviderConnection({ provider: "openai", name: "fixture", authType: "apikey", apiKey: "synthetic-upstream", isActive: true, testStatus: "active" });
  const codex = await providers.createProviderConnection({ provider: "codex", name: "fixture-codex", authType: "oauth", accessToken: "synthetic-codex", isActive: true, testStatus: "active" });
  assert.ok(connection && codex);
  const bind = (model: string) => ({ provider: "openai", model, connectionId: connection.id });
  binding = { vm1201: bind("gpt-4o-mini"), bellPc: bind("gpt-4o"), free: [bind("gpt-4.1-mini"), bind("o3-mini"), bind("o4-mini")], codex: { provider: "codex", model: "gpt-5.6-sol", reasoningEffort: "high", connectionId: codex.id }, codexNormal: { provider: "codex", model: "gpt-5.6-terra", reasoningEffort: "medium", connectionId: codex.id }, cheapChineseReviewers: [bind("gpt-4.1-nano"), bind("gpt-4.1")], strongChineseReviewers: [bind("gpt-4.1"), bind("gpt-4.1-nano")] };
  process.env.OMNIROUTE_AGENT_ROUTE_BINDINGS_JSON = JSON.stringify(binding);
  key = await keys.createApiKey("harness-fixture", "fixture", ["agent:route"]);
  await keys.updateApiKeyPermissions(key.id, { noLog: true, allowedModels: ["agent/normal", "agent/high", ...Object.values(binding).flat().map((b: any) => b.provider + "/" + b.model)], allowedConnections: [String(connection.id), String(codex.id)] });
});
test.beforeEach(async () => {
  calls.length = 0;
  resetAllCircuitBreakers();
  clearProviderFailure("openai");
  const connection = await providers.getProviderConnectionById(binding.vm1201.connectionId);
  await clearAccountError(binding.vm1201.connectionId, connection!);
  globalThis.fetch = (async (url, init) => {
    if (String(url).endsWith("/slots")) return Response.json([{ is_processing: false }, { is_processing: false }]);
    const body = JSON.parse(String(init?.body ?? "{}"));
    calls.push({ url: String(url), body, headers: Object.fromEntries(new Headers(init?.headers)), signal: init?.signal });
    const reviewer = body.model === "gpt-4.1-nano" || body.model === "gpt-4.1";
    return Response.json({ id: "chatcmpl-fixture", object: "chat.completion", model: body.model, choices: [{ index: 0, message: { role: "assistant", content: reviewer ? '{"verdict":"PASS","findings":""}' : marker + "-answer" }, finish_reason: "stop" }], usage: { prompt_tokens: 8, completion_tokens: 5, total_tokens: 13 } });
  }) as typeof fetch;
});
test.after(() => { globalThis.fetch = originalFetch; });
function identity() { return { taskId: randomUUID(), runId: randomUUID(), turnId: randomUUID(), idempotencyKey: randomUUID(), apiKeyId: key.id }; }
function request(ids: ReturnType<typeof identity>, responses = false, overrides: Record<string, unknown> = {}, auth = key.key) {
  return new Request("http://localhost/v1/" + (responses ? "responses" : "chat/completions"), { method: "POST",
    headers: { "content-type": "application/json", authorization: "Bearer " + auth, "x-omniroute-task-id": ids.taskId, "x-omniroute-run-id": ids.runId, "x-omniroute-turn-id": ids.turnId, "x-omniroute-idempotency-key": ids.idempotencyKey, "x-omniroute-review-class": "standard" },
    body: JSON.stringify({ model: "agent/normal", stream: false, ...(responses ? { input: marker } : { messages: [{ role: "user", content: marker }] }), ...overrides }) });
}

test("real Chat and Responses endpoints dispatch exact candidate+isolated reviewer and retain only metadata", async () => {
  const logs: string[] = [];
  const originalLog = console.log, originalWarn = console.warn, originalError = console.error;
  console.log = (...args) => { logs.push(args.map(String).join(" ")); };
  console.warn = (...args) => { logs.push(args.map(String).join(" ")); };
  console.error = (...args) => { logs.push(args.map(String).join(" ")); };
  try {
    for (const responses of [false, true]) {
      calls.length = 0;
      const ids = identity();
      const endpoint = responses ? responsesEndpoint : chatEndpoint;
      const response = await endpoint.POST(request(ids, responses, { omniroute_route: { checks: [{ kind: "nonempty" }] } }));
      const body = await response.text();
      assert.equal(response.status, 200, body);
      assert.match(body, new RegExp(marker));
      assert.equal(response.headers.get("x-omniroute-run-id"), ids.runId);
      assert.equal(response.headers.get("x-omniroute-candidate-attempt"), "1");
      assert.equal(response.headers.get("x-omniroute-reviewer-verdict"), "PASS");
      assert.deepEqual(calls.map(call => call.body.model), ["gpt-4o-mini", "gpt-4.1-nano"]);
      assert.equal(calls[0].headers.authorization, "Bearer synthetic-upstream");
      assert.equal(calls[0].body.omniroute_route, undefined);
      assert.equal(calls[1].body.input, undefined);
      assert.equal(calls[1].body.tools, undefined);
      assert.match(JSON.stringify(calls[1].body), new RegExp(marker + "-answer"));
      assert.equal(getAgentRouteTurn(ids)?.state, "completed");
      assert.equal(getAgentRouteTurn(ids)?.output_started, 1);
      const replay = await endpoint.POST(request(ids, responses));
      assert.equal(replay.status, 409);
      assert.equal((await replay.json()).error.code, "agent_route_resume_required");
      assert.equal(calls.length, 2);
      const nextIds = { ...ids, turnId: randomUUID(), idempotencyKey: randomUUID() };
      const next = await handleChat(request(nextIds, responses));
      assert.equal(next.status, 200, await next.clone().text());
      await next.text();
      assert.equal(getAgentRouteTurn(ids)?.output_started, 1);
      assert.equal(getAgentRouteTurn(nextIds)?.state, "completed");
    }
    const db = core.getDbInstance();
    for (const table of db.prepare("SELECT name FROM sqlite_master WHERE type='table'").all() as { name: string }[]) {
      assert.equal(JSON.stringify(db.prepare('SELECT * FROM "' + table.name.replaceAll('"', '""') + '"').all()).includes(marker), false, table.name + " retained payload");
    }
    assert.equal(logs.join("\n").includes(marker), false);
    assert.ok(db.prepare("SELECT * FROM agent_route_events WHERE kind='result' AND admission_state='admitted'").all().length >= 4);
  } finally { console.log = originalLog; console.warn = originalWarn; console.error = originalError; }
});

test("no-log alias permission alone cannot unlock paid models; invalid objectives consume no run", async () => {
  const team = await keys.createApiKey("team-fixture", "fixture");
  await keys.updateApiKeyPermissions(team.id, { noLog: true, allowedModels: ["agent/normal"] });
  assert.equal((await handleChat(request(identity(), false, {}, team.key))).status, 403);
  const restricted = await keys.createApiKey("restricted-fixture", "fixture", ["agent:route"]);
  await keys.updateApiKeyPermissions(restricted.id, { noLog: true, allowedModels: ["agent/normal", "openai/gpt-4o-mini"] });
  assert.equal((await handleChat(request(identity(), false, {}, restricted.key))).status, 503);
  const ids = identity();
  assert.equal((await handleChat(request(ids, false, { omniroute_route: { checks: [{ kind: "unknown" }] } }))).status, 400);
  assert.equal(getAgentRouteTurn(ids), undefined);
  assert.equal(calls.length, 0);
});

test("lifecycle identity conflict is rejected through the real endpoint", async () => {
  const ids = identity();
  const accepted = await handleChat(request(ids)); await accepted.text();
  const eventRequest = (turnId: string) => new Request("http://localhost/v1/agent-routes/events", { method: "POST", headers: {
    authorization: "Bearer " + key.key, "content-type": "application/json", "x-omniroute-task-id": ids.taskId, "x-omniroute-run-id": ids.runId, "x-omniroute-turn-id": turnId, "x-omniroute-idempotency-key": ids.idempotencyKey,
  }, body: JSON.stringify({ event_id: randomUUID(), task_id: ids.taskId, run_id: ids.runId, turn_id: turnId, idempotency_key: ids.idempotencyKey, kind: "tool_started", occurred_at: new Date().toISOString() }) });
  assert.equal((await eventsEndpoint.POST(eventRequest(randomUUID()))).status, 403);
  assert.equal((await eventsEndpoint.POST(eventRequest(ids.turnId))).status, 202);
  assert.equal(getAgentRouteTurn(ids)?.tool_started, 1);
});

test("native exact connection pin defeats a conflicting affinity and rejects synthetic no-auth", async () => {
  const other = await providers.createProviderConnection({ provider: "openai", name: "other-fixture", authType: "apikey", apiKey: "synthetic-other", isActive: true, testStatus: "active" });
  assert.ok(other);
  const session = randomUUID();
  upsertSessionAccountAffinity(session, "openai", String(other.id), Date.now(), 60000);
  const chosen = await getProviderCredentials("openai", null, [binding.vm1201.connectionId, String(other.id)], binding.vm1201.model,
    { forcedConnectionId: binding.vm1201.connectionId, hardConnectionPin: true, sessionKey: session, sessionAffinityTtlMs: 60000 });
  assert.equal(chosen?.connectionId, binding.vm1201.connectionId);
  assert.equal(await getProviderCredentials("opencode", null, null, "any", { forcedConnectionId: "synthetic", hardConnectionPin: true }), null);
  assert.equal(calls.length, 0);
});

test("public streaming endpoints release no early frame before independent acceptance", async () => {
  for (const responses of [false, true]) {
    const fetchFixture = globalThis.fetch;
    let reviewerReached!: () => void, finishReview!: () => void;
    const reached = new Promise<void>(resolve => { reviewerReached = resolve; });
    const reviewGate = new Promise<void>(resolve => { finishReview = resolve; });
    globalThis.fetch = (async (url, init) => {
      if (JSON.parse(String(init?.body ?? "{}"))?.model === "gpt-4.1-nano") { reviewerReached(); await reviewGate; }
      return fetchFixture(url, init);
    }) as typeof fetch;
    const ids = identity();
    let returned = false;
    const pending = (responses ? responsesEndpoint.POST(request(ids, true, { stream: true })) : chatEndpoint.POST(request(ids, false, { stream: true }))).then(response => { returned = true; return response; });
    await reached;
    assert.equal(returned, false);
    assert.equal(getAgentRouteTurn(ids)?.output_started, 0);
    finishReview();
    const response = await pending;
    assert.equal(response.status, 200, await response.clone().text());
    assert.equal(getAgentRouteTurn(ids)?.output_started, 1);
    assert.match(await response.text(), /data:/);
    assert.equal(getAgentRouteTurn(ids)?.state, "completed");
    globalThis.fetch = fetchFixture;
  }
});

test("a real lifecycle latch cancels the native pending fetch and prevents reviewer/fallback dispatch", async () => {
  let started!: () => void;
  const startedPromise = new Promise<void>(resolve => { started = resolve; });
  let generationCalls = 0, cancelled = false;
  globalThis.fetch = (async (url, init) => {
    if (String(url).endsWith("/slots")) return Response.json([{ is_processing: false }, { is_processing: false }]);
    generationCalls++; started();
    return new Promise<Response>((_resolve, reject) => {
      init!.signal!.addEventListener("abort", () => { cancelled = true; reject(new Error("fixture aborted")); }, { once: true });
    });
  }) as typeof fetch;
  const ids = identity();
  const pending = handleChat(request(ids));
  await startedPromise;
  const event = await eventsEndpoint.POST(new Request("http://localhost/v1/agent-routes/events", { method: "POST", headers: {
    authorization: "Bearer " + key.key, "content-type": "application/json", "x-omniroute-task-id": ids.taskId, "x-omniroute-run-id": ids.runId, "x-omniroute-turn-id": ids.turnId, "x-omniroute-idempotency-key": ids.idempotencyKey,
  }, body: JSON.stringify({ event_id: randomUUID(), task_id: ids.taskId, run_id: ids.runId, turn_id: ids.turnId, idempotency_key: ids.idempotencyKey, kind: "tool_started", occurred_at: new Date().toISOString() }) }));
  assert.equal(event.status, 202);
  const response = await pending;
  assert.equal(response.status, 409, await response.clone().text());
  assert.equal((await response.json()).error.code, "agent_route_resume_required");
  assert.equal(cancelled, true);
  assert.equal(generationCalls, 1);
  assert.equal(getAgentRouteTurn(ids)?.dispatch_claimed, 0);
  assert.equal(getAgentRouteTurn(ids)?.state, "blocked");
});

test("native five-second admission deadline aborts an unaccepted generation and charges no attempt", async () => {
  let cancelled = false;
  const generations: string[] = [];
  globalThis.fetch = (async (url, init) => {
    if (String(url).endsWith("/slots")) return Response.json([{ is_processing: false }, { is_processing: false }]);
    if (String(url) === "https://chatgpt.com/backend-api/wham/usage") return Response.json({ rate_limit: { secondary_window: { used_percent: 80 } } });
    const model = JSON.parse(String(init?.body)).model;
    generations.push(model);
    if (model !== binding.vm1201.model) {
      assert.equal(cancelled, true, "fallback must wait for cancelled I/O to settle");
      return Response.json({ choices: [{ message: { content: model === binding.bellPc.model ? "candidate" : '{"verdict":"PASS","findings":""}' }, finish_reason: "stop" }] });
    }
    return new Promise<Response>((_resolve, reject) => {
      const cancel = () => { cancelled = true; reject(new DOMException("cancelled", "AbortError")); };
      if (init?.signal?.aborted) cancel(); else init?.signal?.addEventListener("abort", cancel, { once: true });
    });
  }) as typeof fetch;
  const ids = identity(), started = performance.now();
  const response = await handleChat(request(ids));
  assert.equal(response.status, 200, await response.clone().text());
  await response.text();
  assert.equal(cancelled, true);
  assert.deepEqual(generations, [binding.vm1201.model, binding.bellPc.model, binding.cheapChineseReviewers[0].model]);
  assert.equal(response.headers.get("x-omniroute-candidate-attempt"), "1");
  assert.ok(performance.now() - started >= 4500);
  const metadata = core.getDbInstance().prepare("SELECT admission_state,candidate_attempt FROM agent_route_events WHERE run_id=? AND admission_state IS NOT NULL").all(ids.runId) as any[];
  assert.ok(metadata.some(row => row.admission_state === "full" && row.candidate_attempt === 0));
  assert.equal(getAgentRouteTurn(ids)?.dispatch_claimed, 0);
  assert.equal(getAgentRouteTurn(ids)?.state, "completed");
});

test("native provider failure cannot emergency-reroute or retain echoed payload in error metadata", async () => {
  let generationCalls = 0;
  globalThis.fetch = (async (url, init) => {
    if (String(url).endsWith("/slots")) return Response.json([{ is_processing: false }, { is_processing: false }]);
    if (String(url) === "https://chatgpt.com/backend-api/wham/usage") return Response.json({ rate_limit: { allowed: true, secondary_window: { used_percent: 80 } } });
    generationCalls++;
    assert.equal(JSON.parse(String(init?.body)).model, binding.vm1201.model);
    return Response.json({ error: { message: marker + " payment required", code: "insufficient_quota" }, warning: marker }, { status: 402 });
  }) as typeof fetch;
  const response = await handleChat(request(identity()));
  assert.equal(response.status, 503);
  assert.equal(generationCalls, 1, "cooldown suppresses configured same-account branches; native hidden fallback is forbidden");
  await new Promise(resolve => setImmediate(resolve));
  const db = core.getDbInstance();
  for (const table of db.prepare("SELECT name FROM sqlite_master WHERE type='table'").all() as { name: string }[]) {
    assert.equal(JSON.stringify(db.prepare('SELECT * FROM "' + table.name.replaceAll('"', '""') + '"').all()).includes(marker), false, table.name + " retained provider error payload");
  }
});
