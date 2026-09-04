import test from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolveNextBuildBundlerFlag, resolveNextBuildEnv } from "../../../scripts/build/build-next-isolated.mjs";

test("Docker builder argument reaches the actual bundler helper without changing its default or heap", async () => {
  const dockerfile = await readFile(new URL("../../../Dockerfile", import.meta.url), "utf8");
  const builder = dockerfile.split(/^FROM .* AS builder\s*$/mi)[1]?.split(/^FROM /mi)[0];
  assert.ok(builder);
  // Evaluate the relevant Docker ARG/ENV assignment subset before npm run build;
  // this is a source-to-helper check, not a claim of executing a Docker build.
  function environment(overrides: Record<string, string>) {
    const values: Record<string, string> = {};
    for (const line of builder!.split(/\r?\n/)) {
      if (/^RUN .*npm run build/.test(line)) break;
      const assignment = /^(ARG|ENV) (OMNIROUTE_USE_TURBOPACK|OMNIROUTE_BUILD_MEMORY_MB|NODE_OPTIONS)=(.*)$/.exec(line);
      if (!assignment) continue;
      const [, kind, name, expression] = assignment;
      values[name] = kind === "ARG" && name in overrides ? overrides[name] : expression.replace(/^"|"$/g, "").replace(/\$\{(\w+)\}/g, (_, key) => values[key] ?? "");
    }
    return resolveNextBuildEnv(values, "linux");
  }
  const constrained = environment({ OMNIROUTE_USE_TURBOPACK: "0", OMNIROUTE_BUILD_MEMORY_MB: "8192" });
  assert.equal(resolveNextBuildBundlerFlag(constrained), "--webpack");
  assert.equal(constrained.NODE_OPTIONS, "--max-old-space-size=8192");
  const defaults = environment({});
  assert.equal(resolveNextBuildBundlerFlag(defaults), "--turbopack");
  assert.equal(defaults.NODE_OPTIONS, "--max-old-space-size=4096");
});
