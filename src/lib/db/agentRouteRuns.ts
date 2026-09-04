import { randomUUID } from "node:crypto";
import { getDbInstance } from "./core";

export type AgentRouteRunInput = {
  runId: string; apiKeyId: string; taskId: string; turnId: string; idempotencyKey: string;
  virtualRoute: "agent/normal" | "agent/high";
  effectiveReviewClass: "standard" | "high_risk";
};
export type TurnIdentity = Pick<AgentRouteRunInput, "runId" | "apiKeyId" | "taskId" | "turnId" | "idempotencyKey">;
export type AgentRouteEventInput = TurnIdentity & {
  eventId: string; kind: "output_started" | "tool_started"; occurredAt: string;
};
export type RouteMetadata = Partial<Record<
  "provider" | "model" | "connection_id" | "admission_state" | "fallback_reason" | "objective_outcome" |
  "reviewer_class" | "reviewer_model" | "reviewer_verdict" | "subscription_evidence_id" |
  "subscription_evidence_at" | "subscription_decision", string>> & Partial<Record<
  "candidate_attempt" | "repair_attempt" | "reviewer_attempt" | "latency_ms" | "prompt_tokens" |
  "completion_tokens" | "subscription_percent" | "busy_slots" | "processing_requests", number>>;
const metadataColumns = ["provider", "model", "connection_id", "candidate_attempt", "repair_attempt", "reviewer_attempt", "admission_state", "fallback_reason", "latency_ms", "prompt_tokens", "completion_tokens", "objective_outcome", "reviewer_class", "reviewer_model", "reviewer_verdict", "subscription_percent", "subscription_evidence_id", "subscription_evidence_at", "subscription_decision", "busy_slots", "processing_requests"] as const;
const now = () => new Date().toISOString();
type TurnRow = { state: string; dispatch_claimed: number; output_started: number; tool_started: number; effective_review_class: "standard" | "high_risk" };

export function getAgentRouteTurn(input: TurnIdentity): TurnRow | undefined {
  return getDbInstance().prepare(`SELECT t.*, r.effective_review_class FROM agent_route_turns t
    JOIN agent_route_runs r ON r.run_id = t.run_id WHERE r.run_id=? AND r.api_key_id=? AND r.task_id=?
    AND t.turn_id=? AND t.idempotency_key=?`).get(input.runId, input.apiKeyId, input.taskId, input.turnId, input.idempotencyKey) as TurnRow | undefined;
}
export function createOrResumeAgentRouteRun(input: AgentRouteRunInput) {
  const db = getDbInstance();
  return db.transaction(() => {
    // Acquire SQLite's write reservation before reading admission state. The
    // shared adapter's transaction is DEFERRED on some supported runtimes.
    db.prepare("UPDATE agent_route_runs SET updated_at=updated_at WHERE run_id=?").run(input.runId);
    const conflict = { kind: "resume_required" as const };
    const run = db.prepare("SELECT * FROM agent_route_runs WHERE run_id=? OR (api_key_id=? AND task_id=?)").all(input.runId, input.apiKeyId, input.taskId) as Array<{ run_id: string; api_key_id: string; task_id: string; effective_review_class: string }>;
    if (run.some(r => r.run_id !== input.runId || r.api_key_id !== input.apiKeyId || r.task_id !== input.taskId)) return conflict;
    if (db.prepare("SELECT 1 FROM agent_route_turns WHERE run_id=? AND (turn_id=? OR idempotency_key=? OR state IN ('active','stopping'))").get(input.runId, input.turnId, input.idempotencyKey)) return conflict;
    const effectiveReviewClass = input.virtualRoute === "agent/high" || input.effectiveReviewClass === "high_risk" || run[0]?.effective_review_class === "high_risk" ? "high_risk" as const : "standard" as const;
    if (!run.length) db.prepare("INSERT INTO agent_route_runs VALUES (?,?,?,?,?,?)").run(input.runId, input.apiKeyId, input.taskId, effectiveReviewClass, now(), now());
    else db.prepare("UPDATE agent_route_runs SET effective_review_class=?, updated_at=? WHERE run_id=?").run(effectiveReviewClass, now(), input.runId);
    db.prepare("INSERT INTO agent_route_turns (run_id,turn_id,idempotency_key,virtual_route,state,created_at,updated_at) VALUES (?,?,?,?,'active',?,?)").run(input.runId, input.turnId, input.idempotencyKey, input.virtualRoute, now(), now());
    return { kind: "created" as const, runId: input.runId, effectiveReviewClass };
  })();
}
function insertMetadata(input: TurnIdentity, kind: "dispatch" | "result" | "subscription", metadata: RouteMetadata) {
  // The fixed column list prevents accidental payload persistence from a future caller.
  const values = metadataColumns.map(key => metadata[key] ?? null);
  getDbInstance().prepare(`INSERT INTO agent_route_events (event_id,run_id,turn_id,idempotency_key,kind,occurred_at,${metadataColumns.join(",")}) VALUES (${Array(6 + values.length).fill("?").join(",")})`).run(randomUUID(), input.runId, input.turnId, input.idempotencyKey, kind, now(), ...values);
}
export function recordAgentRouteMetadata(input: TurnIdentity, kind: "result" | "subscription", metadata: RouteMetadata) {
  if (!getAgentRouteTurn(input)) throw new Error("agent_route_identity_conflict");
  insertMetadata(input, kind, metadata);
}
export function claimAgentRouteDispatch(input: TurnIdentity, metadata: RouteMetadata) {
  const db = getDbInstance();
  return db.transaction(() => {
    db.prepare("UPDATE agent_route_runs SET updated_at=updated_at WHERE run_id=?").run(input.runId);
    const turn = getAgentRouteTurn(input);
    if (!turn || turn.state !== "active" || turn.dispatch_claimed || turn.output_started || turn.tool_started) return false;
    db.prepare("UPDATE agent_route_turns SET dispatch_claimed=1,updated_at=? WHERE run_id=? AND turn_id=?").run(now(), input.runId, input.turnId);
    insertMetadata(input, "dispatch", metadata);
    return true;
  })();
}
export function settleAgentRouteDispatch(input: TurnIdentity) {
  if (!getAgentRouteTurn(input)) throw new Error("agent_route_identity_conflict");
  getDbInstance().prepare("UPDATE agent_route_turns SET dispatch_claimed=0,updated_at=? WHERE run_id=? AND turn_id=?").run(now(), input.runId, input.turnId);
}
export function finishAgentRouteTurn(input: TurnIdentity, state: "completed" | "blocked" | "failed" | "cancelled") {
  const db = getDbInstance();
  return db.transaction(() => {
    db.prepare("UPDATE agent_route_runs SET updated_at=updated_at WHERE run_id=?").run(input.runId);
    const turn = getAgentRouteTurn(input);
    if (!turn || turn.dispatch_claimed || !["active", "stopping"].includes(turn.state)) return false;
    db.prepare("UPDATE agent_route_turns SET state=?,updated_at=? WHERE run_id=? AND turn_id=?").run(state, now(), input.runId, input.turnId);
    return true;
  })();
}
export function appendAgentRouteEvent(input: AgentRouteEventInput): "created" | "duplicate" | "forbidden" | "conflict" {
  const db = getDbInstance();
  return db.transaction(() => {
    db.prepare("UPDATE agent_route_runs SET updated_at=updated_at WHERE run_id=?").run(input.runId);
    if (!getAgentRouteTurn(input)) return "forbidden" as const;
    const existing = db.prepare("SELECT run_id,turn_id,idempotency_key,kind FROM agent_route_events WHERE event_id=?").get(input.eventId) as Record<string, string> | undefined;
    if (existing) return existing.run_id === input.runId && existing.turn_id === input.turnId && existing.idempotency_key === input.idempotencyKey && existing.kind === input.kind ? "duplicate" as const : "conflict" as const;
    db.prepare("INSERT INTO agent_route_events (event_id,run_id,turn_id,idempotency_key,kind,occurred_at) VALUES (?,?,?,?,?,?)").run(input.eventId, input.runId, input.turnId, input.idempotencyKey, input.kind, input.occurredAt);
    const column = input.kind === "output_started" ? "output_started" : "tool_started";
    db.prepare(`UPDATE agent_route_turns SET ${column}=1,state=CASE WHEN state='active' THEN 'stopping' ELSE state END,updated_at=? WHERE run_id=? AND turn_id=?`).run(now(), input.runId, input.turnId);
    return "created" as const;
  })();
}
export function commitAgentRouteOutput(input: TurnIdentity) {
  return getDbInstance().transaction(() => {
    getDbInstance().prepare("UPDATE agent_route_runs SET updated_at=updated_at WHERE run_id=?").run(input.runId);
    const turn = getAgentRouteTurn(input);
    if (!turn || turn.state !== "active" || turn.dispatch_claimed || turn.output_started || turn.tool_started) return false;
    return appendAgentRouteEvent({ ...input, eventId: randomUUID(), kind: "output_started", occurredAt: now() }) === "created";
  })();
}
