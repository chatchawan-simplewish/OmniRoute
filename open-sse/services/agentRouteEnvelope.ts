import { z } from "zod";

/** Decode only the supported public response envelope, never raw wire truthiness. */
export function decodeAgentRouteEnvelope(bytes: Uint8Array) {
  const raw = new TextDecoder().decode(bytes);
  const sse = /^\s*(?:event:|data:|:)/.test(raw);
  const frames = sse ? raw.split(/\r?\n/).filter(line => line.startsWith("data:")).map(line => line.slice(5).trim()).filter(line => line && line !== "[DONE]").map(line => JSON.parse(line)) : [JSON.parse(raw)];
  let text = "", recognized = false, complete = !sse;
  let promptTokens: number | undefined, completionTokens: number | undefined;
  const tools = new Map<string, { name: string; args: string }>();
  function responseItems(items: any[]) {
    for (const item of items) {
      if (item.type === "message") for (const content of item.content ?? []) if (content.type === "output_text" && typeof content.text === "string") text += content.text;
      if (item.type === "function_call") tools.set(item.call_id ?? item.id, { name: item.name, args: item.arguments });
    }
  }
  for (const frame of frames) {
    const usage = frame.usage ?? frame.response?.usage;
    if (usage) {
      const prompt = usage.prompt_tokens ?? usage.input_tokens, completion = usage.completion_tokens ?? usage.output_tokens;
      if (Number.isFinite(prompt) && prompt >= 0) promptTokens = prompt;
      if (Number.isFinite(completion) && completion >= 0) completionTokens = completion;
    }
    if (frame.error || frame.type === "error" || frame.type === "response.failed" || frame.type === "response.incomplete") throw new Error("invalid_candidate");
    if (Array.isArray(frame.choices)) {
      recognized = true;
      if (frame.choices.length > 1) throw new Error("multiple_candidates");
      const choice = frame.choices[0];
      if (!choice) continue;
      if (choice.finish_reason) complete = true;
      if (["length", "content_filter"].includes(choice.finish_reason)) throw new Error("incomplete_candidate");
      const message = choice.message ?? choice.delta;
      if (typeof message?.content === "string") text += message.content;
      for (const tool of message?.tool_calls ?? []) {
        const key = String(tool.index ?? tool.id);
        const old = tools.get(key) ?? { name: "", args: "" };
        tools.set(key, { name: old.name + (tool.function?.name ?? ""), args: old.args + (tool.function?.arguments ?? "") });
      }
    } else if (Array.isArray(frame.output)) { recognized = true; responseItems(frame.output); }
    else if (frame.type === "response.completed") { recognized = true; complete = true; text = ""; tools.clear(); responseItems(frame.response?.output ?? []); }
    else if (frame.type === "response.output_text.delta") { recognized = true; text += frame.delta ?? ""; }
    else if (typeof frame.output_text === "string") { recognized = true; text += frame.output_text; }
  }
  if (!recognized || !complete) throw new Error("invalid_candidate_envelope");
  for (const tool of tools.values()) {
    if (typeof tool.name !== "string" || !tool.name) throw new Error("invalid_tool_name");
    const args = JSON.parse(tool.args);
    if (!args || typeof args !== "object" || Array.isArray(args)) throw new Error("invalid_tool_arguments");
  }
  return { output: new TextEncoder().encode(text), toolNames: [...tools.values()].map(tool => tool.name), promptTokens, completionTokens };
}
const reviewSchema = z.object({ verdict: z.enum(["PASS", "REVISE", "BLOCKED"]), findings: z.string().max(16000) }).strict().superRefine((v, ctx) => {
  if (v.verdict !== "PASS" && !v.findings.trim()) ctx.addIssue({ code: "custom", message: "findings required" });
});
export function decodeAgentRouteReview(bytes: Uint8Array) {
  try {
    const decoded = decodeAgentRouteEnvelope(bytes);
    if (decoded.toolNames.length) return null;
    return reviewSchema.parse(JSON.parse(new TextDecoder().decode(decoded.output)));
  } catch { return null; }
}
