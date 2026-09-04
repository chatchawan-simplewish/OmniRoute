import { z } from "zod";
import type { CodexWeeklyEvidence } from "./codexQuotaFetcher.ts";
import { evaluateAgentRouteObjectives, type ObjectiveCheck } from "./agentRouteObjectives.ts";
import type { RouteMetadata } from "../../src/lib/db/agentRouteRuns.ts";
import { acquire } from "./rateLimitSemaphore.ts";

export const AGENT_ROUTE_ALIASES = ["agent/normal", "agent/high"] as const;
export type AgentRouteAlias = (typeof AGENT_ROUTE_ALIASES)[number];
export type RouteVerdict = "PASS" | "REVISE" | "BLOCKED";
export type ReviewClass = "standard" | "high_risk";
export const ADMISSION_MS = 5_000;
export const MAX_FREE_ATTEMPTS = 6;
const binding = z.object({ provider: z.string().regex(/^[a-zA-Z0-9_.-]+$/), model: z.string().min(1).max(200), connectionId: z.string().min(1).max(100), reasoningEffort: z.enum(["low", "medium", "high", "xhigh"]).optional() }).strict();
const bindingsSchema = z.object({ vm1201: binding, bellPc: binding, free: z.tuple([binding, binding, binding]), codex: binding, codexNormal: binding,
  cheapChineseReviewers: z.array(binding).min(1), strongChineseReviewers: z.array(binding).min(1),
}).strict().superRefine((v, ctx) => {
  if (v.codex.provider !== "codex") ctx.addIssue({ code: "custom", message: "codex binding required" });
  if (v.codexNormal.provider !== "codex" || v.codexNormal.model !== "gpt-5.6-terra" || v.codexNormal.reasoningEffort !== "medium" || v.codex.model !== "gpt-5.6-sol" || v.codex.reasoningEffort !== "high" || v.codex.connectionId !== v.codexNormal.connectionId) ctx.addIssue({ code: "custom", message: "explicit Terra-medium candidate and Sol-high candidate/reviewer roles on one approved account required" });
  if (new Set((v.free as AgentRouteBinding[]).map(x => x.model)).size !== 3) ctx.addIssue({ code: "custom", message: "distinct free models required" });
});
export type AgentRouteBinding = z.infer<typeof binding>;
export type AgentRouteBindings = { vm1201: AgentRouteBinding; bellPc: AgentRouteBinding; free: [AgentRouteBinding, AgentRouteBinding, AgentRouteBinding]; codex: AgentRouteBinding; codexNormal: AgentRouteBinding; cheapChineseReviewers: AgentRouteBinding[]; strongChineseReviewers: AgentRouteBinding[] };
export function getAgentRouteBindings(raw = process.env.OMNIROUTE_AGENT_ROUTE_BINDINGS_JSON): AgentRouteBindings { return bindingsSchema.parse(JSON.parse(raw ?? "{}")) as AgentRouteBindings; }
export function isAgentRouteAlias(v: unknown): v is AgentRouteAlias { return v === "agent/normal" || v === "agent/high"; }
export function resolveEffectiveReviewClass(alias: AgentRouteAlias, requested: ReviewClass, stored?: ReviewClass): ReviewClass {
  return alias === "agent/high" || requested === "high_risk" || stored === "high_risk" ? "high_risk" : "standard";
}
export function subscriptionEligible(e: CodexWeeklyEvidence | null) {
  const age = e ? Date.now() - Date.parse(e.fetchedAt) : NaN;
  return e?.source === "provider-live" && Number.isFinite(e.weeklyPercentUsed) && e.weeklyPercentUsed >= 0 && e.weeklyPercentUsed < 80 && age >= 0 && age <= 30_000;
}
export type Admission = "admitted" | "full" | "offline" | "failed";
export type DispatchResult = Response | { response: Response; admission: Admission };
export type DispatchOptions = { reviewer: boolean; repair: boolean; local: boolean; reasoningEffort?: "low" | "medium" | "high" | "xhigh"; candidate?: Uint8Array; feedback?: string; signal: AbortSignal; evidence?: CodexWeeklyEvidence; checkAdmission: () => void; onAdmitted: () => void; onSubmitted: () => void; onSlots: (busy: number) => void };
export type ReviewResult = { verdict: RouteVerdict; findings: string };
type Input = {
  alias: AgentRouteAlias; bindings: AgentRouteBindings; reviewClass?: ReviewClass;
  checks?: ObjectiveCheck[]; toolNames?: string[]; allowedPolicyIds?: string[];
  dispatch: (target: AgentRouteBinding, options: DispatchOptions) => Promise<DispatchResult>;
  review: (candidate: Uint8Array, reviewerOutput: Uint8Array, target: AgentRouteBinding, reviewClass: ReviewClass) => Promise<ReviewResult | RouteVerdict | null>;
  decode?: (bytes: Uint8Array) => { output: Uint8Array; toolNames: string[]; promptTokens?: number; completionTokens?: number };
  fetchEvidence?: (target: AgentRouteBinding) => Promise<CodexWeeklyEvidence | null>;
  authorize?: (target: AgentRouteBinding) => Promise<boolean>;
  beforeDispatch?: (metadata: RouteMetadata) => boolean;
  afterDispatch?: () => void;
  canContinue?: () => boolean;
  getReviewClass?: () => ReviewClass;
  record?: (kind: "result" | "subscription", metadata: RouteMetadata) => void;
  signal?: AbortSignal;
  now?: () => number;
};
export async function runAgentRoute(input: Input) {
  const { bindings: b } = input;
  const now = input.now ?? (() => performance.now());
  let candidateAttempts = 0, repairAttempts = 0, reviewerAttempts = 0, freeAttempts = 0;
  let fallbackReason = "initial", stopped = false;
  const live = () => !stopped && !input.signal?.aborted && (input.canContinue?.() ?? true);
  const summary = () => ({ candidateAttempts, repairAttempts, reviewerAttempts, fallbackReason });
  const blocked = () => ({ verdict: "BLOCKED" as const, checkIds: [] as string[], hashes: [] as string[], ...summary(), response: undefined as Response | undefined, target: undefined as AgentRouteBinding | undefined });
  const usedEvidence = new Set<string>();
  let dispatchEvidence: CodexWeeklyEvidence | undefined;
  async function eligible(target: AgentRouteBinding) {
    dispatchEvidence = undefined;
    if (!live() || input.authorize && !await input.authorize(target)) return false;
    if (target.provider !== "codex") { input.record?.("subscription", { subscription_decision: "not_selected", provider: target.provider, model: target.model }); return true; }
    const evidence = await input.fetchEvidence?.(target).catch(() => null) ?? null;
    const ok = subscriptionEligible(evidence) && evidence?.connectionId === target.connectionId && !!evidence?.evidenceId && !usedEvidence.has(evidence.evidenceId);
    if (evidence?.evidenceId) usedEvidence.add(evidence.evidenceId);
    if (ok) dispatchEvidence = evidence!;
    input.record?.("subscription", { provider: target.provider, model: target.model, connection_id: target.connectionId,
      subscription_decision: ok ? "eligible" : "skip", ...(evidence && subscriptionEligible(evidence) ? {
        subscription_percent: evidence.weeklyPercentUsed, subscription_evidence_id: evidence.evidenceId, subscription_evidence_at: evidence.fetchedAt,
      } : {}) });
    return ok && live();
  }
  async function call(target: AgentRouteBinding, reviewer: boolean, repair: boolean, candidate?: Uint8Array, feedback?: string) {
    const started = now();
    const deadline = started + ADMISSION_MS;
    const local = target === b.vm1201 || target === b.bellPc;
    if (!await eligible(target)) return null;
    const metadata = { provider: target.provider, model: target.model, connection_id: target.connectionId,
      candidate_attempt: candidateAttempts, repair_attempt: repairAttempts, reviewer_attempt: reviewerAttempts, fallback_reason: fallbackReason };
    if (local && now() >= deadline) {
      input.record?.("result", { ...metadata, admission_state: "full", latency_ms: Math.max(0, Math.round(now() - started)) });
      return { admission: "full" as const, response: undefined, bytes: new Uint8Array() };
    }
    if (!live() || input.beforeDispatch && !input.beforeDispatch(metadata)) { stopped = true; return null; }
    const abort = new AbortController();
    const cancel = () => abort.abort();
    input.signal?.addEventListener("abort", cancel, { once: true });
    let admitted = false, submitted = false, expired = false;
    const checkAdmission = () => {
      if (local && !admitted && (expired || now() >= deadline)) { expired = true; cancel(); }
      abort.signal.throwIfAborted();
    };
    const timer = local ? setTimeout(() => { expired = true; cancel(); }, Math.max(0, deadline - now())) : null;
    const onAdmitted = () => {
      // Recheck the absolute clock even if the event-loop timer has not fired.
      // Abort the native body on expiry without stranding an already returned Response.
      try { checkAdmission(); } catch { return; }
      admitted = true;
      if (timer) clearTimeout(timer);
    };
    // Cross-worker latch commits are observed while I/O is pending. Never settle a
    // claim until the underlying dispatch AND body consumption have settled.
    const watcher = input.canContinue ? setInterval(() => { if (!live()) cancel(); }, 50) : null;
    let admission: Admission = "failed", response: Response | undefined, bytes = new Uint8Array();
    let release: (() => void) | undefined;
    try {
      checkAdmission();
      if (local) {
        try { release = await acquire("agent-local:" + target.connectionId, { maxConcurrency: 2, maxQueueSize: 0, timeoutMs: Math.max(0, deadline - now()) }); }
        catch { admission = "full"; throw new Error("agent_route_local_full"); }
      }
      checkAdmission();
      const result = await input.dispatch(target, { reviewer, repair, local, candidate, feedback, signal: abort.signal, evidence: dispatchEvidence, checkAdmission,
        onSlots: busy => input.record?.("result", { ...metadata, busy_slots: busy, processing_requests: busy }),
        onSubmitted: () => { checkAdmission(); submitted = true; }, onAdmitted,
        ...(input.alias === "agent/high" && target === b.vm1201 ? { reasoningEffort: "xhigh" as const } : target.reasoningEffort ? { reasoningEffort: target.reasoningEffort } : {}),
      });
      response = result instanceof Response ? result : result.response;
      if (result instanceof Response || result.admission === "admitted") onAdmitted();
      admission = expired && !admitted ? "full" : result instanceof Response ? "admitted" : result.admission;
      bytes = new Uint8Array(await response.arrayBuffer());
    } catch { admission = expired && !admitted ? "full" : admitted || submitted ? "admitted" : admission === "full" ? "full" : "offline"; }
    finally {
      if (timer) clearTimeout(timer);
      if (watcher) clearInterval(watcher);
      input.signal?.removeEventListener("abort", cancel);
      release?.();
      input.afterDispatch?.();
    }
    if (admitted || admission === "admitted") {
      if (reviewer) reviewerAttempts++;
      else { candidateAttempts++; if (repair) repairAttempts++; if (b.free.includes(target)) freeAttempts++; }
    }
    input.record?.("result", { ...metadata, admission_state: admission, latency_ms: Math.max(0, Math.round(now() - started)),
      candidate_attempt: candidateAttempts, repair_attempt: repairAttempts, reviewer_attempt: reviewerAttempts });
    if (!live()) { stopped = true; return null; }
    return { admission, response, bytes };
  }
  const chineseCandidates = input.alias === "agent/high" ? b.strongChineseReviewers : b.cheapChineseReviewers;
  const candidates = input.alias === "agent/high" ? [b.vm1201, b.codex, ...chineseCandidates] : [b.vm1201, ...b.free, b.codexNormal, ...chineseCandidates];
  for (let index = 0; index < candidates.length && live(); index++) {
    const target = candidates[index];
    if (!target) continue;
    const budget = b.free.includes(target) ? 2 : 1;
    let feedback: string | undefined, prior: Uint8Array | undefined;
    for (let attempt = 0; attempt < budget && live(); attempt++) {
      if (b.free.includes(target) && freeAttempts >= MAX_FREE_ATTEMPTS) break;
      const result = await call(target, false, attempt === 1, prior, feedback);
      if (!result) break;
      if (target === b.vm1201 && input.alias === "agent/normal" && ["full", "offline"].includes(result.admission)) candidates.splice(index + 1, 0, b.bellPc);
      if (result.admission !== "admitted") { fallbackReason = result.admission; break; }
      // Eligibility scanning is not an additional Chinese candidate budget.
      // Once one is admitted, technical/quality failure ends this final stage.
      if (chineseCandidates.includes(target)) candidates.length = index + 1;
      prior = result.bytes;
      if (!result.response?.ok) { feedback = "The prior attempt failed technically. Produce a complete valid result for the original task."; fallbackReason = "technical_failure"; continue; }
      let semantic: { output: Uint8Array; toolNames: string[]; promptTokens?: number; completionTokens?: number };
      try { semantic = input.decode ? input.decode(result.bytes) : { output: result.bytes, toolNames: input.toolNames ?? [] }; }
      catch { return blocked(); }
      const objectives = evaluateAgentRouteObjectives(input.checks?.length ? input.checks : [{ kind: "nonempty" }], semantic.output, semantic.toolNames, input.allowedPolicyIds);
      input.record?.("result", { provider: target.provider, model: target.model, objective_outcome: objectives.verdict, candidate_attempt: candidateAttempts, prompt_tokens: semantic.promptTokens, completion_tokens: semantic.completionTokens });
      if (objectives.verdict === "BLOCKED") return blocked();
      if (objectives.verdict === "REVISE") { feedback = `Objective checks failed: ${objectives.checkIds.join(", ")}. Correct these requirements: ${JSON.stringify(input.checks ?? [{ kind: "nonempty" }])}`; fallbackReason = "objective_revise"; continue; }
      const reviewClass = resolveEffectiveReviewClass(input.alias, input.reviewClass ?? "standard", input.getReviewClass?.());
      const reviewers = reviewClass === "high_risk" ? [b.codex, ...b.strongChineseReviewers] : b.cheapChineseReviewers;
      let review: ReviewResult | null = null;
      for (const reviewer of reviewers) {
        // Concrete model identity remains independent even across provider aliases.
        if (reviewer.model.toLowerCase().replace(/-(low|medium|high|xhigh|max)$/, "") === target.model.toLowerCase().replace(/-(low|medium|high|xhigh|max)$/, "")) continue;
        const reviewed = await call(reviewer, true, false, result.bytes);
        if (!reviewed?.response?.ok || reviewed.admission !== "admitted") continue;
        try {
          const parsed = await input.review(result.bytes, reviewed.bytes, reviewer, reviewClass);
          review = typeof parsed === "string" ? { verdict: parsed, findings: parsed } : parsed;
        } catch { review = null; }
        input.record?.("result", { provider: target.provider, model: target.model, reviewer_model: reviewer.model, reviewer_class: reviewClass, reviewer_verdict: review?.verdict ?? "technical_failure", reviewer_attempt: reviewerAttempts });
        if (review) break;
      }
      if (!live() || !review || review.verdict === "BLOCKED") return blocked();
      if (review.verdict === "PASS") return { ...objectives, ...summary(), response: new Response(result.bytes, { status: result.response.status, headers: result.response.headers }), target };
      feedback = review.findings;
      fallbackReason = "review_revise";
    }
  }
  return blocked();
}
