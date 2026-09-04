import { z } from "zod";
import { getApiKeyMetadata } from "@/lib/db/apiKeys";
import { appendAgentRouteEvent } from "@/lib/db/agentRouteRuns";
import { extractApiKey, isValidApiKey } from "@/sse/services/auth";

const uuid = z.string().uuid();
const bodySchema = z
  .object({
    event_id: uuid,
    task_id: uuid,
    run_id: uuid,
    turn_id: uuid,
    idempotency_key: uuid,
    kind: z.enum(["output_started", "tool_started"]),
    occurred_at: z.iso.datetime(),
  })
  .strict();
const forbiddenKey = /^(prompt|response|reasoning|tool_payload|cookie|credentials|authorization)$/i;
const secondaryCredentials = new Set([
  "cookie",
  "x-api-key",
  "proxy-authorization",
  "x-forwarded-authorization",
]);

function unsafeBody(value: unknown): boolean {
  if (Array.isArray(value)) return value.some(unsafeBody);
  if (!value || typeof value !== "object") return false;
  return Object.entries(value as Record<string, unknown>).some(
    ([key, child]) => forbiddenKey.test(key) || unsafeBody(child)
  );
}

function reject(status: number, code: string) {
  return Response.json({ error: { code } }, { status });
}

export async function POST(request: Request) {
  if (new URL(request.url).search) return reject(400, "agent_route_invalid_request");
  for (const [name] of request.headers) {
    if (secondaryCredentials.has(name.toLowerCase())) return reject(400, "agent_route_invalid_request");
  }
  const apiKey = extractApiKey(request, { allowUrl: false });
  if (!apiKey || !(await isValidApiKey(apiKey))) return reject(401, "unauthorized");
  const metadata = await getApiKeyMetadata(apiKey);
  if (!metadata?.id || metadata.noLog !== true) return reject(403, "agent_route_no_log_required");
  let raw: unknown;
  try {
    raw = await request.json();
  } catch {
    return reject(400, "agent_route_invalid_request");
  }
  if (unsafeBody(raw)) return reject(400, "agent_route_invalid_request");
  const parsed = bodySchema.safeParse(raw);
  if (!parsed.success) return reject(400, "agent_route_invalid_request");
  const body = parsed.data;
  const headerIds = [
    ["x-omniroute-task-id", body.task_id],
    ["x-omniroute-run-id", body.run_id],
    ["x-omniroute-turn-id", body.turn_id],
    ["x-omniroute-idempotency-key", body.idempotency_key],
  ] as const;
  if (headerIds.some(([name, value]) => request.headers.get(name) !== value)) {
    return reject(400, "agent_route_invalid_request");
  }
  const result = appendAgentRouteEvent({
    eventId: body.event_id,
    runId: body.run_id,
    apiKeyId: metadata.id,
    kind: body.kind,
    occurredAt: body.occurred_at,
    taskId: body.task_id,
    turnId: body.turn_id,
    idempotencyKey: body.idempotency_key,
  });
  if (result === "forbidden") return reject(403, "agent_route_run_forbidden");
  if (result === "conflict") return reject(409, "agent_route_event_conflict");
  return Response.json({ accepted: true }, { status: 202 });
}
