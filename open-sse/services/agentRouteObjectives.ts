import { createHash } from "node:crypto";

export type ObjectiveCheck =
  | { kind: "nonempty" }
  | { kind: "json_schema"; schema: { type: "object"; required?: string[]; properties?: Record<string, { type: "string" | "number" | "boolean" | "array" | "object"; enum?: unknown[] }>; additionalProperties?: false } }
  | { kind: "tool_call"; required_names: string[]; allow_unrequested: false }
  | { kind: "evidence_hash"; algorithm: "sha256"; expected: string[] }
  | { kind: "policy"; policy_ids: string[] };

export type ObjectiveOutcome = { verdict: "PASS" | "REVISE" | "BLOCKED"; checkIds: string[]; hashes: string[] };

function matchesType(value: unknown, type: "string" | "number" | "boolean" | "array" | "object") {
  return type === "array" ? Array.isArray(value) : type === "object" ? !!value && typeof value === "object" && !Array.isArray(value) : typeof value === type;
}

export function evaluateAgentRouteObjectives(
  checks: ObjectiveCheck[],
  output: Uint8Array,
  toolNames: string[] = [],
  allowedPolicyIds: readonly string[] = []
): ObjectiveOutcome {
  if (checks.length > 8) return { verdict: "BLOCKED", checkIds: [], hashes: [] };
  const seen = new Set<string>();
  const checkIds: string[] = [];
  const hashes: string[] = [];
  let text = "";
  try { text = new TextDecoder().decode(output); } catch { return { verdict: "BLOCKED", checkIds, hashes }; }
  for (const [index, check] of checks.entries()) {
    const id = `${check.kind}:${index}`;
    const fingerprint = JSON.stringify(check);
    if (seen.has(fingerprint)) return { verdict: "BLOCKED", checkIds, hashes };
    seen.add(fingerprint);
    checkIds.push(id);
    if (check.kind === "nonempty" && text.trim().length === 0) return { verdict: "REVISE", checkIds, hashes };
    if (check.kind === "tool_call") {
      if (check.allow_unrequested !== false || check.required_names.some((name) => !toolNames.includes(name)) || toolNames.some((name) => !check.required_names.includes(name))) return { verdict: "REVISE", checkIds, hashes };
    }
    if (check.kind === "evidence_hash") {
      if (check.algorithm !== "sha256") return { verdict: "BLOCKED", checkIds, hashes };
      const hash = createHash("sha256").update(output).digest("hex");
      hashes.push(hash);
      if (!check.expected.includes(hash)) return { verdict: "REVISE", checkIds, hashes };
    }
    if (check.kind === "policy" && check.policy_ids.some((id) => !allowedPolicyIds.includes(id))) return { verdict: "BLOCKED", checkIds, hashes };
    if (check.kind === "json_schema") {
      try {
        const value = JSON.parse(text);
        if (!value || typeof value !== "object" || Array.isArray(value) || check.schema.type !== "object") return { verdict: "REVISE", checkIds, hashes };
        const record = value as Record<string, unknown>;
        if (check.schema.required?.some((key) => !(key in record))) return { verdict: "REVISE", checkIds, hashes };
        if (check.schema.additionalProperties === false && Object.keys(record).some((key) => !check.schema.properties?.[key])) return { verdict: "REVISE", checkIds, hashes };
        for (const [key, definition] of Object.entries(check.schema.properties ?? {})) {
          if (!(key in record)) continue;
          if (!matchesType(record[key], definition.type) || (definition.enum && !definition.enum.includes(record[key]))) return { verdict: "REVISE", checkIds, hashes };
        }
      } catch { return { verdict: "BLOCKED", checkIds, hashes }; }
    }
  }
  return { verdict: "PASS", checkIds, hashes };
}
