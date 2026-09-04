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
  const fetchedAt = current ? Date.parse(current.fetchedAt) : NaN;
  const age = Date.now() - fetchedAt;
  return current?.source === "provider-live" && Number.isFinite(current.weeklyPercentUsed)
    && current.weeklyPercentUsed >= 0 && current.weeklyPercentUsed <= 100
    && Number.isFinite(fetchedAt) && age >= 0 && age <= 30_000 && current.weeklyPercentUsed < 80;
}

export function getAgentRouteBindings(raw = process.env.OMNIROUTE_AGENT_ROUTE_BINDINGS_JSON) {
  return bindingsSchema.parse(JSON.parse(raw ?? "{}"));
}

export function resolveEffectiveReviewClass(alias: AgentRouteAlias, requested: ReviewClass, stored?: ReviewClass): ReviewClass {
  if (alias === "agent/high" || requested === "high_risk" || stored === "high_risk") return "high_risk";
  return "standard";
}

export type AgentRouteBinding = { provider: string; model: string; connectionId: string };
export type AgentRouteBindings = {
  vm1201: AgentRouteBinding;
  bellPc: AgentRouteBinding;
  free: [AgentRouteBinding, AgentRouteBinding, AgentRouteBinding];
  codex: AgentRouteBinding;
  cheapChineseReviewers: AgentRouteBinding[];
  strongChineseReviewers: AgentRouteBinding[];
};

export type Admission = "admitted" | "full" | "offline" | "failed";
export type DispatchResult = Response | { response: Response; admission: Admission };
type Dispatch = (target: AgentRouteBinding, options: { reasoningEffort?: "xhigh"; reviewer: boolean; repair: boolean; candidate?: Uint8Array; feedback?: string; signal?: AbortSignal }) => Promise<DispatchResult>;
type Review = (candidate: Uint8Array, reviewerOutput: Uint8Array, target: AgentRouteBinding, reviewClass: ReviewClass) => Promise<RouteVerdict>;

function usable(response: Response) {
  return response.ok && response.status !== 408 && response.status !== 429;
}

function cloneResponse(response: Response, bytes: Uint8Array) {
  return new Response(bytes, { status: response.status, statusText: response.statusText, headers: response.headers });
}

function dispatched(result: DispatchResult) {
  return result instanceof Response ? { response: result, admission: "admitted" as const } : result;
}

/**
 * Executes the approved ladder through a caller-supplied native dispatch seam.
 * The chat handler supplies that seam with forced connection IDs and no retry.
 */
export async function runAgentRoute(input: {
  checks?: ObjectiveCheck[];
  output?: Uint8Array;
  toolNames?: string[];
  allowedPolicyIds?: string[];
  alias?: AgentRouteAlias;
  bindings?: AgentRouteBindings;
  dispatch?: Dispatch;
  review?: Review;
  reviewClass?: ReviewClass;
  fetchEvidence?: () => Promise<CodexWeeklyEvidence | null>;
  now?: () => number;
} = {}): Promise<{ verdict: RouteVerdict; checkIds: string[]; hashes: string[]; response?: Response; target?: AgentRouteBinding }> {
  if (input.alias && input.bindings && input.dispatch && input.review) {
    const reviewClass = resolveEffectiveReviewClass(input.alias, input.reviewClass ?? "standard");
    const now = input.now ?? (() => performance.now());
    const localDeadline = now() + ADMISSION_MS;
    const candidates = input.alias === "agent/high"
      ? [input.bindings.vm1201, input.bindings.codex, input.bindings.strongChineseReviewers[0]]
      : [input.bindings.vm1201, ...input.bindings.free, input.bindings.codex, input.bindings.cheapChineseReviewers[0]];
    let freeAttempts = 0;
    for (let candidateIndex = 0; candidateIndex < candidates.length; candidateIndex += 1) {
      const target = candidates[candidateIndex];
      if (!target) continue;
      if (target === input.bindings.codex && !subscriptionEligible(await input.fetchEvidence?.() ?? null)) continue;
      let selectedTarget = target;
      const local = target === input.bindings.vm1201 || target === input.bindings.bellPc;
      const controller = local ? new AbortController() : null;
      const timeoutMs = local ? Math.max(0, localDeadline - now()) : 0;
      if (local && timeoutMs === 0) continue;
      let attempt = dispatched(await (local ? Promise.race([
        input.dispatch(target, {
          reviewer: false, repair: false, signal: controller!.signal,
          ...(input.alias === "agent/high" && target === input.bindings.vm1201 ? { reasoningEffort: "xhigh" } : {}),
        }),
        new Promise<DispatchResult>((resolve) => setTimeout(() => { controller!.abort(); resolve({ response: new Response(null, { status: 408 }), admission: "full" }); }, timeoutMs)),
      ]) : input.dispatch(target, {
        reviewer: false,
        repair: false,
        ...(input.alias === "agent/high" && target === input.bindings.vm1201 ? { reasoningEffort: "xhigh" } : {}),
      })));
      // Bell-PC is capacity escape only, never a quality fallback.
      if (target === input.bindings.vm1201 && input.alias === "agent/normal" && (attempt.admission === "full" || attempt.admission === "offline")) {
        attempt = dispatched(await input.dispatch(input.bindings.bellPc, { reviewer: false, repair: false }));
        selectedTarget = input.bindings.bellPc;
        if (attempt.admission !== "admitted" || !usable(attempt.response)) continue;
        // A Bell-PC candidate may be reviewed, but failure proceeds to free A.
      }
      if (attempt.admission !== "admitted") continue;
      const response = attempt.response;
      if (!usable(response)) continue;
      const bytes = new Uint8Array(await response.arrayBuffer());
      const objectives = evaluateAgentRouteObjectives(input.checks ?? [{ kind: "nonempty" }], bytes, input.toolNames, input.allowedPolicyIds);
      if (objectives.verdict === "BLOCKED") return objectives;
      if (objectives.verdict === "REVISE") continue;
      const reviewers = reviewClass === "high_risk"
        ? [input.bindings.codex, ...input.bindings.strongChineseReviewers]
        : input.bindings.cheapChineseReviewers;
      const evidence = await input.fetchEvidence?.() ?? null;
      const reviewer = reviewers.find((item) =>
        `${item.provider}/${item.model}` !== `${selectedTarget.provider}/${selectedTarget.model}` &&
        (item !== input.bindings.codex || subscriptionEligible(evidence))
      );
      if (!reviewer) return { ...objectives, verdict: "BLOCKED" };
      const reviewerResult = dispatched(await input.dispatch(reviewer, { reviewer: true, repair: false, candidate: bytes }));
      if (reviewerResult.admission !== "admitted" || !usable(reviewerResult.response)) continue;
      const reviewerBytes = new Uint8Array(await reviewerResult.response.arrayBuffer());
      if (await input.review(bytes, reviewerBytes, reviewer, reviewClass) === "PASS") {
        return { ...objectives, response: cloneResponse(response, bytes), target: selectedTarget };
      }
      if (input.alias === "agent/normal" && input.bindings.free.includes(target) && freeAttempts + 2 <= MAX_FREE_ATTEMPTS) {
        freeAttempts += 2;
        const repair = dispatched(await input.dispatch(target, { reviewer: false, repair: true, candidate: bytes, feedback: new TextDecoder().decode(reviewerBytes) }));
        if (repair.admission === "admitted" && usable(repair.response)) {
          const repairedBytes = new Uint8Array(await repair.response.arrayBuffer());
          const repairedObjectives = evaluateAgentRouteObjectives(input.checks ?? [{ kind: "nonempty" }], repairedBytes, input.toolNames, input.allowedPolicyIds);
          if (repairedObjectives.verdict === "PASS") {
            const reReviewResult = dispatched(await input.dispatch(reviewer, { reviewer: true, repair: false, candidate: repairedBytes }));
            if (reReviewResult.admission === "admitted" && usable(reReviewResult.response)) {
              const reReviewBytes = new Uint8Array(await reReviewResult.response.arrayBuffer());
              if (await input.review(repairedBytes, reReviewBytes, reviewer, reviewClass) === "PASS") return { ...repairedObjectives, response: cloneResponse(repair.response, repairedBytes), target };
            }
          }
        }
      }
    }
    return { verdict: "BLOCKED", checkIds: [], hashes: [] };
  }
  const result = evaluateAgentRouteObjectives(input.checks ?? [], input.output ?? new Uint8Array(), input.toolNames, input.allowedPolicyIds);
  return result;
}
