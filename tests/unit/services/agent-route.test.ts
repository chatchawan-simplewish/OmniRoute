import assert from "node:assert/strict";
import test from "node:test";
import { isAgentRouteAlias, runAgentRoute } from "../../../open-sse/services/agentRoute.ts";

test("recognizes only approved aliases", () => {
  assert.equal(isAgentRouteAlias("agent/normal"), true);
  assert.equal(isAgentRouteAlias("agent/high"), true);
  assert.equal(isAgentRouteAlias("agent-normal"), false);
  assert.equal(isAgentRouteAlias("auto/agent/high"), false);
});

test("normal dispatches VM1201 before Bell-PC and preserves the provider response", async () => {
  const dispatched: string[] = [];
  const result = await runAgentRoute({
    alias: "agent/normal",
    bindings: {
      vm1201: { provider: "local", model: "q6", connectionId: "vm" },
      bellPc: { provider: "bell", model: "q4", connectionId: "bell" },
      free: [
        { provider: "free-a", model: "a", connectionId: "a" },
        { provider: "free-b", model: "b", connectionId: "b" },
        { provider: "free-c", model: "c", connectionId: "c" },
      ],
      codex: { provider: "codex", model: "paid", connectionId: "codex" },
      cheapChineseReviewers: [{ provider: "cn", model: "cheap", connectionId: "cn" }],
      strongChineseReviewers: [{ provider: "cn", model: "strong", connectionId: "strong" }],
    },
    dispatch: async (target: { provider: string }) => {
      dispatched.push(target.provider);
      return new Response("ok", { status: 200 });
    },
    review: async () => "PASS",
  });
  assert.equal(await result.response?.text(), "ok");
  assert.deepEqual(dispatched, ["local", "cn"]);
});

test("quality rejection skips Bell-PC and capacity rejection uses it", async () => {
  const bindings = {
    vm1201: { provider: "local", model: "q6", connectionId: "vm" }, bellPc: { provider: "bell", model: "q4", connectionId: "bell" },
    free: [{ provider: "free-a", model: "a", connectionId: "a" }, { provider: "free-b", model: "b", connectionId: "b" }, { provider: "free-c", model: "c", connectionId: "c" }],
    codex: { provider: "codex", model: "paid", connectionId: "codex" }, cheapChineseReviewers: [{ provider: "cn", model: "cheap", connectionId: "cn" }], strongChineseReviewers: [{ provider: "cn", model: "strong", connectionId: "strong" }],
  } as const;
  const calls: string[] = [];
  await runAgentRoute({ alias: "agent/normal", bindings: bindings as any, checks: [{ kind: "json_schema", schema: { type: "object", required: ["ok"] } }], dispatch: async (t) => { calls.push(t.provider); return new Response(t.provider === "local" ? "{}" : '{"ok":true}'); }, review: async () => "PASS" });
  assert.equal(calls.includes("bell"), false);
  calls.length = 0;
  await runAgentRoute({ alias: "agent/normal", bindings: bindings as any, dispatch: async (t) => { calls.push(t.provider); return t.provider === "local" ? { response: new Response(""), admission: "full" } : new Response("ok"); }, review: async () => "PASS" });
  assert.equal(calls[1], "bell");
});

test("objective checks reject wrong property type and unexpected tools", async () => {
  const { evaluateAgentRouteObjectives } = await import("../../../open-sse/services/agentRouteObjectives.ts");
  assert.equal(evaluateAgentRouteObjectives([{ kind: "json_schema", schema: { type: "object", properties: { count: { type: "number" } } } }], new TextEncoder().encode('{"count":"bad"}')).verdict, "REVISE");
  assert.equal(evaluateAgentRouteObjectives([{ kind: "tool_call", required_names: ["allowed"], allow_unrequested: false }], new Uint8Array(), ["allowed", "extra"]).verdict, "REVISE");
});
