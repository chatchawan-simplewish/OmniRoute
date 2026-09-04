import { AsyncLocalStorage } from "node:async_hooks";
import type { AgentRouteBinding, DispatchOptions } from "./agentRoute.ts";
import { subscriptionEligible } from "./agentRoute.ts";

// Request-scoped only: never serialize this context or attach it to client input.
export const agentRouteContext = new AsyncLocalStorage<{
  private: true; target?: AgentRouteBinding; options?: DispatchOptions;
  executorCalls?: number; upstreamCalls?: number; admission?: "full" | "offline";
}>();
export async function agentRouteBeforeFetch(url: string, headers: HeadersInit | undefined) {
  const context = agentRouteContext.getStore();
  if (!context?.options) return;
  const { options } = context;
  options.signal.throwIfAborted();
  if (context.upstreamCalls) throw new Error("agent_route_hidden_retry_blocked");
  if (context.target?.provider === "codex" && (!subscriptionEligible(options.evidence ?? null) || options.evidence?.connectionId !== context.target.connectionId)) throw new Error("agent_route_evidence_expired");
  if (options.local) {
    // One signal spans slot precheck, native queues, and HTTP acceptance.
    context.admission = "offline";
    const response = await fetch(new URL("/slots", url), { headers, signal: options.signal, cache: "no-store" });
    if (!response.ok) throw new Error("agent_route_local_offline");
    const slots = await response.json();
    if (!Array.isArray(slots) || slots.length !== 2 || slots.some(slot => typeof slot.is_processing !== "boolean")) throw new Error("agent_route_local_slots_unavailable");
    options.onSlots(slots.filter(slot => slot.is_processing).length);
    if (slots.every(slot => slot.is_processing)) { context.admission = "full"; throw new Error("agent_route_local_full"); }
    context.admission = undefined;
  }
  options.signal.throwIfAborted();
  context.upstreamCalls = 1;
  options.onSubmitted();
}
export function agentRouteAfterFetch(response: Response) {
  if (response.ok) agentRouteContext.getStore()?.options?.onAdmitted();
}
export function guardAgentRouteExecutor<T extends { execute: (...args: any[]) => any }>(executor: T): T {
  const context = agentRouteContext.getStore();
  if (!context?.target) return executor;
  return new Proxy(executor, { get(target, key, receiver) {
    if (key !== "execute") return Reflect.get(target, key, receiver);
    return async (input: any) => {
      context.options!.signal.throwIfAborted();
      if (context.executorCalls || input.model !== context.target!.model || input.credentials?.connectionId !== context.target!.connectionId) throw new Error("agent_route_dispatch_identity_conflict");
      context.executorCalls = 1;
      return target.execute({ ...input, skipUpstreamRetry: true });
    };
  } });
}
