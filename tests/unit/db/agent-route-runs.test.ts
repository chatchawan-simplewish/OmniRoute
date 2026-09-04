import assert from "node:assert/strict";
import test from "node:test";
import { ensureDbInitialized, getDbInstance, resetDbInstance } from "../../../src/lib/db/core.ts";
import {
  appendAgentRouteEvent,
  createOrResumeAgentRouteRun,
  getAgentRouteRun,
} from "../../../src/lib/db/agentRouteRuns.ts";

const ids = {
  key: "00000000-0000-4000-8000-000000000001",
  task: "00000000-0000-4000-8000-000000000002",
  turn: "00000000-0000-4000-8000-000000000003",
  run: "00000000-0000-4000-8000-000000000004",
  event: "00000000-0000-4000-8000-000000000005",
};

test.beforeEach(async () => {
  resetDbInstance();
  await ensureDbInitialized();
});

test("duplicate identity requires resume and a latched task rejects a fresh run", () => {
  const first = createOrResumeAgentRouteRun({
    runId: ids.run,
    apiKeyId: ids.key,
    taskId: ids.task,
    turnId: ids.turn,
    idempotencyKey: "00000000-0000-4000-8000-000000000006",
    virtualRoute: "agent/normal",
    effectiveReviewClass: "standard",
  });
  assert.equal(first.kind, "created");
  const duplicate = createOrResumeAgentRouteRun({
    runId: "00000000-0000-4000-8000-000000000007",
    apiKeyId: ids.key,
    taskId: ids.task,
    turnId: ids.turn,
    idempotencyKey: "00000000-0000-4000-8000-000000000006",
    virtualRoute: "agent/normal",
    effectiveReviewClass: "standard",
  });
  assert.deepEqual(duplicate, { kind: "resume_required", runId: ids.run });
  appendAgentRouteEvent({
    eventId: ids.event,
    runId: ids.run,
    apiKeyId: ids.key,
    kind: "output_started",
    occurredAt: "2026-08-30T12:00:00.000Z",
  });
  const fresh = createOrResumeAgentRouteRun({
    runId: "00000000-0000-4000-8000-000000000008",
    apiKeyId: ids.key,
    taskId: ids.task,
    turnId: "00000000-0000-4000-8000-000000000009",
    idempotencyKey: "00000000-0000-4000-8000-000000000010",
    virtualRoute: "agent/normal",
    effectiveReviewClass: "standard",
  });
  assert.deepEqual(fresh, { kind: "resume_required", runId: ids.run });
});

test("events are idempotent, monotonic, and never store request payload columns", () => {
  const second = {
    key: "00000000-0000-4000-8000-000000000021",
    task: "00000000-0000-4000-8000-000000000022",
    turn: "00000000-0000-4000-8000-000000000023",
    run: "00000000-0000-4000-8000-000000000024",
    event: "00000000-0000-4000-8000-000000000025",
  };
  createOrResumeAgentRouteRun({
    runId: second.run,
    apiKeyId: second.key,
    taskId: second.task,
    turnId: second.turn,
    idempotencyKey: "00000000-0000-4000-8000-000000000006",
    virtualRoute: "agent/high",
    effectiveReviewClass: "high_risk",
  });
  assert.equal(
    appendAgentRouteEvent({
      eventId: second.event,
      runId: second.run,
      apiKeyId: second.key,
      kind: "tool_started",
      occurredAt: "2026-08-30T12:00:00.000Z",
    }),
    "created"
  );
  assert.equal(
    appendAgentRouteEvent({
      eventId: second.event,
      runId: second.run,
      apiKeyId: second.key,
      kind: "tool_started",
      occurredAt: "2026-08-30T12:00:01.000Z",
    }),
    "duplicate"
  );
  assert.deepEqual(getAgentRouteRun(second.run, second.key), {
    runId: second.run,
    outputStarted: false,
    toolStarted: true,
  });
  const columns = getDbInstance()
    .prepare("PRAGMA table_info(agent_route_events)")
    .all()
    .map((column: { name: string }) => column.name);
  assert.equal(columns.some((column: string) => /payload|body|text|blob/i.test(column)), false);
});
