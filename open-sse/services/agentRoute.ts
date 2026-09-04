import { z } from "zod";
import type { CodexWeeklyEvidence } from "./codexQuotaFetcher.ts";
import { evaluateAgentRouteObjectives, type ObjectiveCheck } from "./agentRouteObjectives.ts";

export const AGENT_ROUTE_ALIASES = ["agent/normal", "agent/high"] as const;
export type AgentRouteAlias = (typeof AGENT_ROUTE_ALIASES)[number];
export type RouteVerdict = "PASS" | "REVISE" | "BLOCKED";
export type ReviewClass = "standard" | "high_risk";
export const ADMISSION_MS = 5_000;
export const MAX_FREE_ATTEMPTS = 6;

const binding = z.object({ provider: z.string().min(1), model: z.string().min(1), connectionId: z.string().min(1) }).strict();
const bindingsSchema = z.object({
  vm1201: binding,
  bellPc: binding,
  free: z.array(binding).length(3),
  codex: binding,
  cheapChineseReviewers: z.array(binding).min(1),
  strongChineseReviewers: z.array(binding).min(1),
}).strict().superRefine((value, ctx) => {
  if (value.codex.provider !== "codex") ctx.addIssue({ code: "custom", message: "codex binding required" });
  if (new Set(value.free.map((entry) => `${entry.provider}/${entry.model}`)).size !== 3) ctx.addIssue({ code: "custom", message: "free bindings must be distinct" });
});

export function isAgentRouteAlias(value: unknown): value is AgentRouteAlias {
  return value === "agent/normal" || value === "agent/high";
}

export function subscriptionEligible(current: CodexWeeklyEvidence | null) {
  return current?.source === "provider-live" && Number.isFinite(current.weeklyPercentUsed)
    && Date.now() - Date.parse(current.fetchedAt) <= 30_000 && current.weeklyPercentUsed < 80;
}

export function getAgentRouteBindings(raw = process.env.OMNIROUTE_AGENT_ROUTE_BINDINGS_JSON) {
  return bindingsSchema.parse(JSON.parse(raw ?? "{}"));
}

export function resolveEffectiveReviewClass(alias: AgentRouteAlias, requested: ReviewClass, stored?: ReviewClass): ReviewClass {
  if (alias === "agent/high" || requested === "high_risk" || stored === "high_risk") return "high_risk";
  return "standard";
}

export async function runAgentRoute(input: {
  checks?: ObjectiveCheck[];
  output?: Uint8Array;
  toolNames?: string[];
  allowedPolicyIds?: string[];
} = {}): Promise<{ verdict: RouteVerdict; checkIds: string[]; hashes: string[] }> {
  const result = evaluateAgentRouteObjectives(input.checks ?? [], input.output ?? new Uint8Array(), input.toolNames, input.allowedPolicyIds);
  return result;
}
