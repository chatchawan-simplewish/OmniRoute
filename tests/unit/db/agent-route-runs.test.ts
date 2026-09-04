import assert from "node:assert/strict";
import test from "node:test";
import { randomUUID } from "node:crypto";
import { ensureDbInitialized, getDbInstance } from "../../../src/lib/db/core.ts";
import { appendAgentRouteEvent, createOrResumeAgentRouteRun, getAgentRouteTurn, claimAgentRouteDispatch, settleAgentRouteDispatch, finishAgentRouteTurn, commitAgentRouteOutput } from "../../../src/lib/db/agentRouteRuns.ts";

test("canonical task ownership, atomic turn/dispatch/latch lifecycle, and monotonic review floor", async () => {
  await ensureDbInitialized();
  const first = { runId: randomUUID(), apiKeyId: randomUUID(), taskId: randomUUID(), turnId: randomUUID(), idempotencyKey: randomUUID(), virtualRoute: "agent/high" as const, effectiveReviewClass: "high_risk" as const };
  assert.equal(createOrResumeAgentRouteRun(first).kind, "created");
  for (const change of [{}, { runId: randomUUID() }, { apiKeyId: randomUUID() }, { taskId: randomUUID() }, { idempotencyKey: randomUUID() }, { turnId: randomUUID() }, { turnId: randomUUID(), idempotencyKey: randomUUID() }]) {
    assert.deepEqual(createOrResumeAgentRouteRun({ ...first, ...change }), { kind: "resume_required" });
  }
  assert.equal(claimAgentRouteDispatch(first, { provider: "local", model: "q6" }), true);
  assert.equal(claimAgentRouteDispatch(first, {}), false);
  assert.equal(finishAgentRouteTurn(first, "cancelled"), false, "unsettled claim is not terminal");
  const event = { ...first, eventId: randomUUID(), kind: "tool_started" as const, occurredAt: new Date().toISOString() };
  assert.equal(appendAgentRouteEvent({ ...event, apiKeyId: randomUUID() }), "forbidden");
  assert.equal(appendAgentRouteEvent({ ...event, idempotencyKey: randomUUID() }), "forbidden");
  assert.equal(appendAgentRouteEvent(event), "created");
  assert.equal(appendAgentRouteEvent(event), "duplicate");
  assert.equal(appendAgentRouteEvent({ ...event, kind: "output_started" }), "conflict");
  assert.equal(getAgentRouteTurn(first)?.state, "stopping");
  assert.equal(finishAgentRouteTurn(first, "completed"), false);
  settleAgentRouteDispatch(first);
  assert.equal(claimAgentRouteDispatch(first, {}), false, "latch prevents every later dispatch");
  assert.equal(commitAgentRouteOutput(first), false, "tool latch forbids accepting output");
  assert.equal(finishAgentRouteTurn(first, "cancelled"), true);
  const second = { ...first, turnId: randomUUID(), idempotencyKey: randomUUID(), virtualRoute: "agent/normal" as const, effectiveReviewClass: "standard" as const };
  const admittedSecond = createOrResumeAgentRouteRun(second);
  assert.equal(admittedSecond.kind, "created");
  if (admittedSecond.kind === "created") assert.equal(admittedSecond.effectiveReviewClass, "high_risk");
  assert.equal(appendAgentRouteEvent({ ...event, eventId: randomUUID(), kind: "output_started" }), "created", "late event targets old turn");
  assert.equal(getAgentRouteTurn(first)?.output_started, 1);
  assert.equal(getAgentRouteTurn(second)?.output_started, 0);
  assert.equal(claimAgentRouteDispatch(second, {}), true);
  settleAgentRouteDispatch(second);
  assert.equal(commitAgentRouteOutput(second), true);
  assert.equal(getAgentRouteTurn(second)?.state, "stopping");
  assert.equal(finishAgentRouteTurn(second, "completed"), true);
  assert.equal(createOrResumeAgentRouteRun(second).kind, "resume_required");
  const orphan = { ...second, turnId: randomUUID(), idempotencyKey: randomUUID() };
  assert.equal(createOrResumeAgentRouteRun(orphan).kind, "created");
  assert.equal(claimAgentRouteDispatch(orphan, {}), true);
  assert.equal(createOrResumeAgentRouteRun(orphan).kind, "resume_required", "orphaned claim cannot auto-retry");
  const events = getDbInstance().prepare("SELECT * FROM agent_route_events WHERE run_id=?").all(first.runId);
  assert.equal(events.filter((e: any) => e.kind === "tool_started").length, 1);
  assert.ok(events.some((e: any) => e.kind === "dispatch" && e.provider === "local"));
});

test("event/latch insertion rolls back atomically on interrupted update", async () => {
  await ensureDbInitialized();
  const input = { runId: randomUUID(), apiKeyId: randomUUID(), taskId: randomUUID(), turnId: randomUUID(), idempotencyKey: randomUUID(), virtualRoute: "agent/normal" as const, effectiveReviewClass: "standard" as const };
  createOrResumeAgentRouteRun(input);
  const db = getDbInstance();
  db.exec("CREATE TRIGGER reject_test_latch BEFORE UPDATE OF tool_started ON agent_route_turns BEGIN SELECT RAISE(ABORT, 'test interruption'); END");
  const event = { ...input, eventId: randomUUID(), kind: "tool_started" as const, occurredAt: new Date().toISOString() };
  assert.throws(() => appendAgentRouteEvent(event));
  assert.equal(db.prepare("SELECT 1 FROM agent_route_events WHERE event_id=?").get(event.eventId), undefined);
  assert.equal(getAgentRouteTurn(input)?.tool_started, 0);
  db.exec("DROP TRIGGER reject_test_latch");
  assert.equal(appendAgentRouteEvent(event), "created");
});
