// Read-only baseline comparison; does not claim the TypeScript backlog is clean.
import ts from "typescript";
import { execFileSync } from "node:child_process";
import path from "node:path";

const base = process.argv[2];
if (!/^[0-9a-f]{40}$/.test(base ?? "")) throw new Error("Pass the exact 40-character base commit");
const cwd = process.cwd();
const key = name => path.resolve(name).replaceAll("\\", "/").toLowerCase();
const relative = name => path.relative(cwd, name).replaceAll("\\", "/");
const config = ts.readConfigFile("tsconfig.typecheck-agent-route.json", ts.sys.readFile);
if (config.error) throw new Error(ts.flattenDiagnosticMessageText(config.error.messageText, " "));
const parsed = ts.parseJsonConfigFileContent(config.config, ts.sys, cwd);
const changed = execFileSync("git", ["diff", "--name-only", base, "--", "*.ts", "*.tsx"], { encoding: "utf8" }).trim().split(/\r?\n/).filter(Boolean);
const added = execFileSync("git", ["ls-files", "--others", "--exclude-standard", "--", "*.ts", "*.tsx"], { encoding: "utf8" }).trim().split(/\r?\n/).filter(Boolean);
const baseline = new Map();
for (const file of new Set([...changed, ...added])) {
  let content = null;
  try { content = execFileSync("git", ["show", `${base}:${file}`], { encoding: "utf8", stdio: ["ignore", "pipe", "ignore"], maxBuffer: 8 * 1024 * 1024 }); } catch {}
  baseline.set(key(file), content);
}
function diagnostics(useBase) {
  const host = ts.createCompilerHost(parsed.options);
  const read = host.readFile, exists = host.fileExists;
  host.readFile = name => useBase && baseline.has(key(name)) ? baseline.get(key(name)) ?? undefined : read(name);
  host.fileExists = name => useBase && baseline.has(key(name)) ? baseline.get(key(name)) !== null : exists(name);
  host.getSourceFile = (name, languageVersion) => {
    const content = host.readFile(name);
    return content === undefined ? undefined : ts.createSourceFile(name, content, languageVersion, true);
  };
  const roots = parsed.fileNames.filter(name => host.fileExists(name));
  const program = ts.createProgram(roots, parsed.options, host);
  return ts.getPreEmitDiagnostics(program);
}
// Additional native roots can change TypeScript's display order of these unions.
// Normalize ordering only; keep the entire diagnostic text, expression, and count.
const message = d => ts.flattenDiagnosticMessageText(d.messageText, " ")
  .replaceAll("Headers | Record<string, unknown>", "Record<string, unknown> | Headers")
  .replaceAll("string | URLSearchParams | Record<string, string>", "string | Record<string, string> | URLSearchParams");
const fingerprint = d => JSON.stringify([d.file ? relative(d.file.fileName) : "config", d.code,
  message(d), d.file && d.start !== undefined ? d.file.text.slice(d.start, d.start + (d.length ?? 0)) : ""]);
const old = diagnostics(true);
const remaining = new Map();
for (const d of old) { const k = fingerprint(d); remaining.set(k, (remaining.get(k) ?? 0) + 1); }
const current = diagnostics(false);
const introduced = current.filter(d => { const k = fingerprint(d), count = remaining.get(k) ?? 0; if (!count) return true; remaining.set(k, count - 1); return false; });
console.log(JSON.stringify({ base, roots: parsed.fileNames.map(relative), baselineDiagnostics: old.length, currentDiagnostics: current.length, introducedDiagnostics: introduced.length }, null, 2));
if (introduced.length) console.log(ts.formatDiagnosticsWithColorAndContext(introduced, { getCurrentDirectory: () => cwd, getCanonicalFileName: x => x, getNewLine: () => "\n" }));
process.exitCode = introduced.length ? 1 : 0;
