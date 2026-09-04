import { getDbInstance } from "./core";

export type AgentRouteRunInput = {
  runId: string;
  apiKeyId: string;
  taskId: string;
  turnId: string;
  idempotencyKey: string;
  virtualRoute: "agent/normal" | "agent/high";
  effectiveReviewClass: "standard" | "high_risk";
};

export type AgentRouteEventInput = {
  eventId: string;
  runId: string;
  apiKeyId: string;
  kind: "output_started" | "tool_started";
  occurredAt: string;
};

const now = () => new Date().toISOString();

export function createOrResumeAgentRouteRun(input: AgentRouteRunInput) {
  const db = getDbInstance();
  const existing = db
    .prepare(
      `SELECT run_id, output_started, tool_started FROM agent_route_runs
       WHERE api_key_id = ? AND task_id = ? AND turn_id = ? AND idempotency_key = ?`
    )
    .get(input.apiKeyId, input.taskId, input.turnId, input.idempotencyKey) as { run_id: string } | undefined;
  if (existing) return { kind: "resume_required" as const, runId: existing.run_id };

  const latched = db
    .prepare(
      `SELECT run_id FROM agent_route_runs
       WHERE api_key_id = ? AND task_id = ? AND (output_started = 1 OR tool_started = 1)
       ORDER BY updated_at DESC LIMIT 1`
    )
    .get(input.apiKeyId, input.taskId) as { run_id: string } | undefined;
  if (latched) return { kind: "resume_required" as const, runId: latched.run_id };

  const timestamp = now();
  db.prepare(
    `INSERT INTO agent_route_runs
       (run_id, task_id, turn_id, idempotency_key, api_key_id, virtual_route,
        effective_review_class, state, created_at, updated_at)
     VALUES (?, ?, ?, ?, ?, ?, ?, 'created', ?, ?)`
  ).run(
    input.runId,
    input.taskId,
    input.turnId,
    input.idempotencyKey,
    input.apiKeyId,
    input.virtualRoute,
    input.effectiveReviewClass,
    timestamp,
    timestamp
  );
  return { kind: "created" as const, runId: input.runId };
}

export function getAgentRouteRun(runId: string, apiKeyId: string) {
  const row = getDbInstance()
    .prepare(
      "SELECT run_id, output_started, tool_started FROM agent_route_runs WHERE run_id = ? AND api_key_id = ?"
    )
    .get(runId, apiKeyId) as
    | { run_id: string; output_started: number; tool_started: number }
    | undefined;
  return row
    ? { runId: row.run_id, outputStarted: row.output_started === 1, toolStarted: row.tool_started === 1 }
    : null;
}

export function appendAgentRouteEvent(input: AgentRouteEventInput): "created" | "duplicate" | "forbidden" {
  const db = getDbInstance();
  const owned = db
    .prepare("SELECT run_id FROM agent_route_runs WHERE run_id = ? AND api_key_id = ?")
    .get(input.runId, input.apiKeyId);
  if (!owned) return "forbidden";
  const inserted = db
    .prepare(
      "INSERT OR IGNORE INTO agent_route_events (event_id, run_id, kind, occurred_at) VALUES (?, ?, ?, ?)"
    )
    .run(input.eventId, input.runId, input.kind, input.occurredAt);
  if (inserted.changes === 0) return "duplicate";
  db.prepare(
    `UPDATE agent_route_runs
     SET output_started = CASE WHEN ? = 'output_started' THEN 1 ELSE output_started END,
         tool_started = CASE WHEN ? = 'tool_started' THEN 1 ELSE tool_started END,
         updated_at = ?
     WHERE run_id = ? AND api_key_id = ?`
  ).run(input.kind, input.kind, now(), input.runId, input.apiKeyId);
  return "created";
}
