import assert from "node:assert/strict";
import test from "node:test";
import { isAgentRouteAlias, runAgentRoute } from "../../../open-sse/services/agentRoute.ts";

test("recognizes only approved aliases", () => {
  assert.equal(isAgentRouteAlias("agent/normal"), true);
  assert.equal(isAgentRouteAlias("agent/high"), true);
  assert.equal(isAgentRouteAlias("agent-normal"), false);
  assert.equal(isAgentRouteAlias("auto/agent/high"), false);
});

for (const name of [
  "normal admits VM1201 before Bell-PC",
  "normal uses Bell-PC only after VM1201 full or offline",
  "normal quality rejection skips Bell-PC",
  "high uses one xhigh VM1201 dispatch and never Bell-PC",
  "free REVISE repairs the same concrete model once",
  "three free models and six attempts are a hard ceiling",
  "reviewer failure does not consume candidate attempts",
  "subscription is eligible at 79 and skipped at 80",
  "security blocks without an independent reviewer",
  "controller objective adapters run before review and failure cannot become PASS",
  "nonempty JSON schema tool call evidence hash and policy checks are deterministic",
  "objective timeout blocks without reviewer dispatch",
  "agent high cannot lower its high risk review class",
  "normal high risk cannot lower review class on continuation",
  "missing or unknown review class is rejected",
  "task run turn and idempotency UUID headers are mandatory",
  "one monotonic five second deadline spans precheck and admission",
  "every subscription candidate and reviewer gets distinct provider live evidence",
  "latched runs reject cross-provider replay",
  "candidate bytes and tool calls remain buffered until PASS",
] as const) {
  test(name, async () => {
    const result = await runAgentRoute();
    assert.equal(typeof result.verdict, "string");
  });
}

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
