import assert from "node:assert/strict";
import test from "node:test";
import { isAgentRouteAlias, runAgentRoute } from "../../../open-sse/services/agentRoute.ts";
import { subscriptionEligible, type AgentRouteBindings } from "../../../open-sse/services/agentRoute.ts";
import { decodeAgentRouteEnvelope, decodeAgentRouteReview } from "../../../open-sse/services/agentRouteEnvelope.ts";
import { fetchProviderLiveCodexWeeklyEvidence } from "../../../open-sse/services/codexQuotaFetcher.ts";
import { randomUUID } from "node:crypto";

const bind = (model: string, provider = "test") => ({ model, provider, connectionId: provider === "codex" ? "subscription" : model });
const bindings: AgentRouteBindings = { vm1201: bind("q6"), bellPc: bind("q4"), free: [bind("a"), bind("b"), bind("c")], codex: bind("sol", "codex"), codexNormal: bind("terra", "codex"), cheapChineseReviewers: [bind("cheap"), bind("cheap2")], strongChineseReviewers: [bind("strong"), bind("strong2")] };
const evidence = (percent = 79, age = 0) => ({ connectionId: "subscription", source: "provider-live" as const, weeklyPercentUsed: percent, fetchedAt: new Date(Date.now() - age).toISOString(), evidenceId: randomUUID() });
const content = (value: string) => new TextEncoder().encode(JSON.stringify({ choices: [{ message: { content: value } }] }));

test("fresh quota evidence rejects threshold, stale, future, missing and malformed raw windows", async () => {
  for (const [percent, eligible] of [[79, true], [80, false], [85, false], [-1, false], [NaN, false], [101, false]] as const) assert.equal(subscriptionEligible(evidence(percent)), eligible);
  assert.equal(subscriptionEligible(evidence(79, 31000)), false);
  assert.equal(subscriptionEligible(evidence(79, -1000)), false);
  assert.equal(subscriptionEligible(null), false);
  const original = globalThis.fetch;
  try {
    for (const raw of [{ rate_limit: { primary_window: { used_percent: 1 } } }, { rate_limit: { secondary_window: { used_percent: "garbage" } } }, { rate_limit: { secondary_window: { used_percent: null } } }, { rate_limit: { allowed: false, secondary_window: { used_percent: 1 } } }, { rate_limit: { secondary_window: { used_percent: 1, limit_window_seconds: 18000 } } }]) {
      globalThis.fetch = async () => Response.json(raw);
      assert.equal(await fetchProviderLiveCodexWeeklyEvidence("fixture", { accessToken: "synthetic-only" }), null);
    }
    globalThis.fetch = async (_url, init) => { assert.equal(init?.cache, "no-store"); return Response.json({ rate_limit: { secondary_window: { used_percent: 79 } } }); };
    const a = await fetchProviderLiveCodexWeeklyEvidence("fixture", { accessToken: "synthetic-only" });
    const b = await fetchProviderLiveCodexWeeklyEvidence("fixture", { accessToken: "synthetic-only" });
    assert.equal(a?.weeklyPercentUsed, 79);
    assert.equal(a?.connectionId, "fixture");
    assert.notEqual(a?.evidenceId, b?.evidenceId);
  } finally { globalThis.fetch = original; }
});

test("free models receive one concrete-feedback repair and repaired bytes get a fresh review", async () => {
  const calls: string[] = [], metadata: any[] = [];
  const result = await runAgentRoute({ alias: "agent/normal", bindings,
    record: (_kind, data) => metadata.push(data), fetchEvidence: async () => evidence(80),
    dispatch: async (target, options) => {
      calls.push(target.model + (options.reviewer ? ":review" : options.repair ? ":repair" : ""));
      if (target.model === "q6") return { response: new Response("", { status: 503 }), admission: "failed" };
      if (options.repair) { assert.match(options.feedback!, /fix count/); assert.ok(options.candidate!.length); }
      return new Response("candidate");
    }, review: async () => ({ verdict: "REVISE", findings: "fix count" }),
  });
  assert.deepEqual(calls.filter(x => /^[abc](?::repair)?$/.test(x)), ["a", "a:repair", "b", "b:repair", "c", "c:repair"]);
  assert.equal(result.repairAttempts, 3);
  assert.equal(result.candidateAttempts, 7);
  assert.equal(calls.includes("q4"), false);
  assert.equal(calls.filter(x => x === "cheap:review").length, 6);
  assert.equal(calls.at(-1), "cheap2:review", "Chinese producer needs an independent reviewer");
  assert.ok(metadata.some(x => x.reviewer_verdict === "REVISE"));
});

test("objective REVISE repairs without reviewer; reviewer technical failure tries next and BLOCKED stops", async () => {
  const calls: string[] = [];
  const result = await runAgentRoute({ alias: "agent/normal", bindings, checks: [{ kind: "json_schema", schema: { type: "object", required: ["ok"] } }],
    dispatch: async (target, options) => {
      calls.push(target.model + (options.reviewer ? ":review" : options.repair ? ":repair" : ""));
      if (target.model === "q6") return new Response("{}");
      if (target.model === "a" && !options.repair) return new Response("{}");
      if (options.repair) assert.match(options.feedback!, /Objective checks failed/);
      if (target.model === "cheap") return new Response("unavailable", { status: 503 });
      return new Response('{"ok":true}');
    }, review: async () => "PASS",
  });
  assert.equal(result.target?.model, "a");
  assert.deepEqual(calls, ["q6", "a", "a:repair", "cheap:review", "cheap2:review"]);
  const blockedCalls: string[] = [];
  const blocked = await runAgentRoute({ alias: "agent/normal", bindings, dispatch: async t => { blockedCalls.push(t.model); return new Response("candidate"); }, review: async () => "BLOCKED" });
  assert.equal(blocked.verdict, "BLOCKED");
  assert.deepEqual(blockedCalls, ["q6", "cheap"]);
});

test("high has one xhigh local attempt, distinct fresh candidate/reviewer evidence, and no Bell/free", async () => {
  for (const percent of [79, 80, 85]) {
    const calls: string[] = [], ids: string[] = [];
    const result = await runAgentRoute({ alias: "agent/high", bindings,
      fetchEvidence: async () => { const e = evidence(percent); ids.push(e.evidenceId); return e; },
      dispatch: async (t, o) => { calls.push(t.model); if (t.model === "q6") { assert.equal(o.reasoningEffort, "xhigh"); return new Response("fail", { status: 502 }); } return new Response("candidate"); }, review: async () => "PASS" });
    assert.equal(result.target?.model, percent < 80 ? "sol" : "strong");
    assert.equal(calls.filter(x => x === "q6").length, 1);
    assert.equal(calls.some(x => ["q4", "a", "b", "c"].includes(x)), false);
    assert.equal(new Set(ids).size, ids.length);
    assert.equal(calls.at(-1), percent < 80 ? "strong" : "strong2");
  }
});

test("admission cancellation settles before fallback and acceptance cancels admission timer", async () => {
  let monotonic = 0, settled = false;
  const result = await runAgentRoute({ alias: "agent/normal", bindings, now: () => monotonic,
    dispatch: async (t, o) => {
      if (t.model === "q6") {
        monotonic = 5001;
        o.onAdmitted();
        await new Promise<void>(resolve => { if (o.signal.aborted) resolve(); else o.signal.addEventListener("abort", () => resolve(), { once: true }); });
        settled = true; throw new Error("cancelled");
      }
      assert.equal(settled, true);
      o.onAdmitted(); return new Response("candidate");
    }, review: async () => "PASS" });
  assert.equal(result.target?.model, "q4");
  assert.equal(result.candidateAttempts, 1, "unaccepted Q6 consumes no candidate");
});

test("latch after claim aborts in-flight I/O and suppresses every later call", async () => {
  let live = true, claimed = 0, settled = 0;
  const result = await runAgentRoute({ alias: "agent/normal", bindings, canContinue: () => live,
    beforeDispatch: () => { claimed++; return live; }, afterDispatch: () => { settled++; },
    dispatch: async (_t, o) => { o.onAdmitted(); live = false; await new Promise<void>(resolve => o.signal.addEventListener("abort", () => resolve(), { once: true })); return new Response("discarded"); }, review: async () => "PASS" });
  assert.equal(result.response, undefined); assert.equal(claimed, 1); assert.equal(settled, 1);
});

test("semantic Chat and Responses envelopes and strict reviewer verdicts", () => {
  assert.equal(new TextDecoder().decode(decodeAgentRouteEnvelope(content("answer")).output), "answer");
  assert.equal(new TextDecoder().decode(decodeAgentRouteEnvelope(new TextEncoder().encode(JSON.stringify({ status: "completed", output: [{ type: "message", content: [{ type: "output_text", text: "answer" }] }] }))).output), "answer");
  for (const value of ["PASS", "DO NOT PASS", '{"reasoning":"PASS","verdict":"REVISE"}', '{"verdict":"REVISE","findings":""}']) assert.equal(decodeAgentRouteReview(content(value)), null);
  assert.equal(decodeAgentRouteReview(content('{"verdict":"PASS","findings":""}'))?.verdict, "PASS");
  assert.throws(() => decodeAgentRouteEnvelope(new TextEncoder().encode("not-json")));
});

test("normal high-risk uses separate Terra candidate and Sol reviewer evidence; reused evidence is rejected", async () => {
  for (const reuse of [false, true]) {
    const calls: string[] = [], shared = evidence(79);
    const result = await runAgentRoute({ alias: "agent/normal", reviewClass: "high_risk", bindings,
      fetchEvidence: async () => reuse ? shared : evidence(79),
      dispatch: async (t, o) => { calls.push(t.model); if (["q6", "a", "b", "c"].includes(t.model)) return { response: new Response(null, { status: 503 }), admission: "failed" }; return new Response("candidate"); },
      review: async () => "PASS" });
    assert.equal(result.target?.model, "terra");
    assert.equal(calls.at(-1), reuse ? "strong" : "sol");
    assert.equal(calls.includes("q4"), false);
  }
});

test("recognizes only approved aliases", () => {
  assert.equal(isAgentRouteAlias("agent/normal"), true);
  assert.equal(isAgentRouteAlias("agent/high"), true);
  assert.equal(isAgentRouteAlias("agent-normal"), false);
  assert.equal(isAgentRouteAlias("auto/agent/high"), false);
});

test("every Codex binding needs evidence for its exact account, including pool entries", async () => {
  const poolCodex = { ...bind("pool-codex", "codex"), connectionId: "pool-account" };
  const configured = { ...bindings, cheapChineseReviewers: [poolCodex, bind("cheap2")] };
  const calls: string[] = [], checked: string[] = [];
  const result = await runAgentRoute({ alias: "agent/normal", bindings: configured,
    fetchEvidence: async target => { checked.push(target.connectionId); return evidence(79); },
    dispatch: async target => { calls.push(target.model); return new Response("candidate"); }, review: async () => "PASS" });
  assert.equal(result.verdict, "PASS");
  assert.deepEqual(checked, ["pool-account"]);
  assert.deepEqual(calls, ["q6", "cheap2"], "mismatched evidence must not authorize the alternate Codex object");
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
      codexNormal: { provider: "codex", model: "normal", connectionId: "codex" },
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

test("review F1: expired absolute admission deadline cannot be cleared by immediate acceptance", async () => {
  for (const phase of ["authorization", "submission", "acceptance", "return"] as const) {
    let clock = 0, q6Dispatches = 0;
    const result = await runAgentRoute({ alias: "agent/normal", bindings, now: () => clock,
      authorize: async target => { if (target === bindings.vm1201 && phase === "authorization") clock = 5001; return true; },
      dispatch: async (target, options) => {
        if (target === bindings.vm1201) {
          q6Dispatches++;
          clock = 5001;
          if (phase === "submission") options.onSubmitted();
          if (phase !== "return") options.onAdmitted();
        } else options.onAdmitted();
        return new Response("answer");
      }, review: async () => "PASS" });
    assert.equal(result.target?.model, "q4", phase);
    assert.equal(result.candidateAttempts, 1, phase + " must not charge expired Q6");
    if (phase === "authorization") assert.equal(q6Dispatches, 0, "do not enter dispatch after expired authorization");
  }
});

test("review F2: Responses completion status is authoritative for JSON and terminal SSE", () => {
  const encode = (value: unknown) => new TextEncoder().encode(JSON.stringify(value));
  const output = [{ type: "message", status: "completed", content: [{ type: "output_text", text: "answer" }] }];
  const complete = { object: "response", status: "completed", output };
  assert.equal(new TextDecoder().decode(decodeAgentRouteEnvelope(encode(complete)).output), "answer");
  for (const status of ["incomplete", "failed", "in_progress", "queued", "cancelled", undefined]) {
    const response = { object: "response", status, incomplete_details: status === "incomplete" ? { reason: "max_output_tokens" } : null, output };
    assert.throws(() => decodeAgentRouteEnvelope(encode(response)), String(status));
    assert.throws(() => decodeAgentRouteEnvelope(new TextEncoder().encode("data: " + JSON.stringify({ type: "response.completed", response }) + "\n\n")), "SSE " + status);
  }
  assert.throws(() => decodeAgentRouteEnvelope(encode({ ...complete, error: { message: "failed" } })));
  const tool = { type: "function_call", call_id: "call_fixture", name: "lookup", arguments: '{"id":1}' };
  assert.deepEqual(decodeAgentRouteEnvelope(encode({ ...complete, output: [tool] })).toolNames, ["lookup"]);
  assert.equal(new TextDecoder().decode(decodeAgentRouteEnvelope(content("chat answer")).output), "chat answer");
});

test("review F3: scan ranked Chinese eligibility but admit only one final-stage candidate", async () => {
  for (const alias of ["agent/normal", "agent/high"] as const) {
    const pool = [bind("rank1"), bind("rank2"), bind("rank3")];
    const configured = { ...bindings, cheapChineseReviewers: pool, strongChineseReviewers: pool };
    for (const mode of ["first-ineligible", "none-eligible", "revise", "technical-failure"] as const) {
      const calls: string[] = [];
      const result = await runAgentRoute({ alias, bindings: configured,
        authorize: async target => pool.includes(target) && mode !== "none-eligible" && target !== pool[0],
        dispatch: async (target, options) => { calls.push(target.model + (options.reviewer ? ":review" : ":candidate")); return new Response("answer", { status: mode === "technical-failure" && !options.reviewer ? 502 : 200 }); },
        review: async () => mode === "revise" ? { verdict: "REVISE", findings: "fix answer" } : "PASS" });
      if (mode === "none-eligible") { assert.equal(result.verdict, "BLOCKED"); assert.deepEqual(calls, []); }
      else {
        assert.equal(result.verdict, mode === "first-ineligible" ? "PASS" : "BLOCKED", alias + mode);
        assert.deepEqual(calls.filter(call => call.endsWith(":candidate")), ["rank2:candidate"]);
        assert.equal(result.candidateAttempts, 1);
        if (mode !== "technical-failure") assert.deepEqual(calls, ["rank2:candidate", "rank3:review"]);
      }
    }
  }
});
