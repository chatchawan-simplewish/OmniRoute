import assert from "node:assert/strict";
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";

const directory = path.dirname(fileURLToPath(import.meta.url));
const sourcePath = path.join(directory,
  "task-2-secure-console-transfer-v54-current-token-table-readiness-source.js");
const executablePath = path.join(directory,
  "task-2-secure-console-transfer-v54-current-token-table-readiness-executable.js");
const designPath = path.join(directory,
  "task-2-secure-console-transfer-v54-current-token-table-readiness-design.md");
const source = fs.readFileSync(sourcePath, "utf8").replace(/\r\n/g, "\n");
const candidate = fs.readFileSync(executablePath, "utf8").replace(/\r\n/g, "\n");
const design = fs.readFileSync(designPath, "utf8");
const sha256 = (value) => crypto.createHash("sha256").update(value).digest("hex").toUpperCase();

const persistentBindings = [
  "secureConsoleOwnedTaskTabV54", "secureConsoleOwnedTaskTabV54Eligible",
  "secureConsoleOwnedTaskTabV54State", "secureConsoleV54Consumed",
  "secureConsoleOwnedTaskTabV54PreCreateDetachConsumed",
  "secureConsoleOwnedTaskTabV54PostNativeDetachConsumed",
  "secureConsoleCloudflareReadsV54Consumed",
];
const require = createRequire(import.meta.url);
const terser = require("next/dist/compiled/terser");
const minimized = await terser.minify(source, {
  module: true,
  compress: { passes: 10, toplevel: true, top_retain: persistentBindings,
    unsafe: true, unsafe_comps: true, hoist_props: true, hoist_vars: true,
    evaluate: false },
  mangle: { toplevel: true, reserved: persistentBindings },
  format: { ascii_only: true, comments: false },
});
assert.equal(minimized.error, undefined);
assert.equal(candidate, minimized.code);
assert.ok(Buffer.byteLength(candidate) <= 25000);
assert.match(candidate, /^[\x00-\x7F]*$/);
for (const binding of persistentBindings) assert.match(candidate, new RegExp(`\\b${binding}\\b`));
for (const pin of [
  "10619", "89D36435A31AE04E560A27D53D8A0953F19E837DF60837FADCF3DC174C0B9477",
  "B9B9BC2319D5EE6AA0B1E481D63BB2130D28102FC7C9080803AB5552185D9037",
  "FC7966FFBC9010252AD3EA745E061068BEC3919EFFF860A87E6013A38A7E277F",
]) assert.ok(design.includes(pin));
new (Object.getPrototypeOf(async function () {}).constructor)(candidate);

const occurrences = (needle) => source.split(needle).length - 1;
assert.equal(occurrences("await import("), 1);
assert.equal(occurrences(".openTabs()"), 1);
assert.equal(occurrences(".claimTab("), 1);
assert.equal(occurrences('goto("https://dash.cloudflare.com/")'), 1);
assert.equal(occurrences('goto("https://dash.cloudflare.com/profile/api-tokens")'), 1);
assert.equal(occurrences('.fill("OmniRoute secure console R5 20260901")'), 1);
for (const prohibited of [
  ".click(", ".check(", ".uncheck(", ".setChecked(", ".type(",
  ".press(", ".selectOption(", ".clipboard", ".close(", ".new()",
  "localStorage", "sessionStorage", "document.cookie", "eval(",
]) assert.equal(occurrences(prohibited), 0, prohibited);

const importLiteral = 'import("file:///C:/Users/chatc/.codex/plugins/cache/openai-bundled/chrome/26.901.20858/scripts/browser-client.mjs")';
assert.equal(candidate.split(importLiteral).length - 1, 1);
const executable = candidate.replace(importLiteral, "Promise.resolve(__module)");
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;
const targetName = "OmniRoute secure console R5 20260901";
const tokenUrl = "https://dash.cloudflare.com/profile/api-tokens";
const accountHomeUrl = `https://dash.cloudflare.com/${"a".repeat(32)}/home`;
const exactTab = { id: "tab-v54", title: "API Tokens | Cloudflare", url: tokenUrl };
const requiredDocs = [
  "openTabs(): Promise<Array<BrowserUserTabInfo>>",
  "claimTab(tab: string | BrowserUserTabInfo): Promise<Tab>",
  "id: string", "lastOpened?: string", "providerTabId?: string",
  "tabGroup?: string", "title?: string", "url?: string",
].join("\n").padEnd(42370, " ");
const defaults = {
  docs: requiredDocs, offered: [exactTab], claimId: exactTab.id,
  homeSnapshot: { hostExact: true, accountHomePath: true, exactZoneHrefCount: 1,
    allAnchorCount: 112, busyCount: 0 },
  searchCount: 1, tableCount: 1, initialValue: "",
  baseline: { headerExact: true, rowCount: 9, targetCount: 0, ready: true },
  noResultsCount: 1,
  filteredUrl: `${tokenUrl}?search=OmniRoute+secure+console+R5+20260901`,
  terminal: { exact: true, actions: 0 },
  createButtonCount: 1, createLinkCount: 0, tokenNameCount: 0,
  matchingRowCount: 0, throwAt: null, failFinalWrite: false,
};

function makeFixture(overrides = {}) {
  const config = { ...defaults, ...overrides };
  const effects = { setup: 0, connect: 0, docs: 0, names: 0, openTabs: 0,
    claims: 0, gotos: [], fills: 0, outputs: [], finalWriteFailed: false };
  const state = { currentUrl: tokenUrl, filterValue: config.initialValue, filtered: false };
  const fail = (name) => { if (config.throwAt === name) throw Object.create(null); };
  const countLocator = (count, waitName) => ({ count: async () => count,
    waitFor: async () => { fail(waitName); } });
  const input = {
    count: async () => config.searchCount,
    waitFor: async () => { fail("searchWait"); },
    evaluate: async (fn) => { fail("inputEval"); return fn({ value: state.filterValue }); },
    fill: async (value) => { fail("fill"); effects.fills++; state.filterValue = value;
      state.filtered = true; state.currentUrl = config.filteredUrl; },
  };
  const table = {
    count: async () => config.tableCount,
    waitFor: async () => { fail("tableWait"); },
    evaluate: async () => { if (!state.filtered) { fail("initialEval"); return config.baseline; }
      fail("terminalEval"); return config.terminal; },
    getByText: () => countLocator(config.noResultsCount, "noResultsWait"),
    locator: () => ({ getByText: () => countLocator(config.tokenNameCount, "unused") }),
    getByRole: () => ({ filter: () => countLocator(config.matchingRowCount, "unused") }),
  };
  const body = { evaluate: async () => { fail("homeSnapshot"); return config.homeSnapshot; } };
  const playwright = {
    waitForTimeout: async () => { fail("homeWait"); },
    locator: (selector) => {
      if (selector === "body") return body;
      if (selector === "#user-api-tokens-search") return input;
      if (selector === "table") return { filter: () => table };
      throw new Error(`unexpected locator ${selector}`);
    },
    getByRole: (role) => {
      if (role === "button") return countLocator(config.createButtonCount, "unused");
      if (role === "link") return countLocator(config.createLinkCount, "unused");
      throw new Error(`unexpected role ${role}`);
    },
    getByText: () => countLocator(0, "unused"),
  };
  const tab = { id: config.claimId, playwright,
    goto: async (url) => { fail(url === "https://dash.cloudflare.com/" ? "gotoHome" : "gotoToken");
      effects.gotos.push(url); state.currentUrl = url === "https://dash.cloudflare.com/" ?
        accountHomeUrl : tokenUrl; state.filterValue = config.initialValue; state.filtered = false; },
    url: async () => { fail(state.filtered ? "filteredUrl" :
      state.currentUrl === accountHomeUrl ? "homeUrl" : "tokenUrl"); return state.currentUrl; } };
  const chrome = { documentation: async () => { effects.docs++; fail("docs"); return config.docs; },
    nameSession: async () => { effects.names++; fail("name"); },
    user: { openTabs: async () => { effects.openTabs++; fail("openTabs"); return config.offered; },
      claimTab: async () => { effects.claims++; fail("claim"); return tab; } } };
  const agent = { browsers: { get: async () => { effects.connect++; fail("connect"); return chrome; } } };
  const module = { setupBrowserRuntime: async () => { effects.setup++; fail("setup"); return agent; } };
  const nodeRepl = { write: async (value) => { if (typeof value === "object" && value !== null && config.failFinalWrite) {
    effects.finalWriteFailed = true; throw new Error("fixture final output failure"); }
    effects.outputs.push(value); } };
  return { effects, module, nodeRepl };
}

async function run(overrides = {}, prelude = "") {
  const fixture = makeFixture(overrides);
  let caught = null;
  try { await new AsyncFunction("__module", "nodeRepl", `${prelude}${executable}`)(
    fixture.module, fixture.nodeRepl); } catch (error) { caught = error; }
  const output = fixture.effects.outputs.find((value) => typeof value === "object" && value !== null) ?? null;
  return { fixture, output, caught };
}

const success = await run();
assert.equal(success.caught, null);
assert.equal(success.output.result, "EXACT_V54_TOKEN_PAGE_SEMANTIC_READINESS_PASS");
assert.equal(success.output.attachment.result,
  "EXACT_V54Attachment_CROSS_REALM_TASK_TAB_ACCOUNT_HOME_REACQUISITION_PASS");
for (const [key, value] of Object.entries({ consumed: true, bindingEligible: true,
  bindingNull: false, navigationTargetExact: true, createControlCount: 1,
  tokenNameCount: 0, matchingRowCount: 0, tokenInitialFilterEmpty: true,
  baselineRowCount: 9, noResultsRowCount: 1, actionResidueCount: 0,
  queryUrlExact: true, tokenFilterComplete: true, tokenSemanticSignature: true,
  continuationBindingsRetained: true })) assert.equal(success.output[key], value, key);
assert.deepEqual({
  binding: [success.output.bindingAttempted, success.output.bindingFulfilled],
  navigation: [success.output.navigationAttempted, success.output.navigationFulfilled],
  url: [success.output.urlAttempted, success.output.urlFulfilled],
  readiness: [success.output.readinessAttempted, success.output.readinessFulfilled],
  initialRead: [success.output.initialReadAttempted, success.output.initialReadFulfilled],
  fill: [success.output.fillAttempted, success.output.fillFulfilled],
  filteredRead: [success.output.filteredReadAttempted, success.output.filteredReadFulfilled],
  createRead: [success.output.createReadAttempted, success.output.createReadFulfilled],
  nameRead: [success.output.nameReadAttempted, success.output.nameReadFulfilled],
  rowRead: [success.output.rowReadAttempted, success.output.rowReadFulfilled],
}, { binding: [1, 1], navigation: [1, 1], url: [2, 2], readiness: [3, 3],
  initialRead: [1, 1], fill: [1, 1], filteredRead: [1, 1], createRead: [1, 1],
  nameRead: [1, 1], rowRead: [1, 1] });

const failureCases = [
  { docs: "bad" }, { offered: [] },
  { offered: [exactTab, { ...exactTab, id: "duplicate" }] }, { claimId: "wrong" },
  { homeSnapshot: { ...defaults.homeSnapshot, exactZoneHrefCount: 0 } },
  { searchCount: 0 }, { tableCount: 2 }, { initialValue: "stale" },
  { baseline: { ...defaults.baseline, headerExact: false } },
  { baseline: { ...defaults.baseline, rowCount: 0, ready: false } },
  { baseline: { ...defaults.baseline, rowCount: 1001, ready: false } },
  { baseline: { ...defaults.baseline, targetCount: 1 } }, { noResultsCount: 0 },
  { filteredUrl: `${tokenUrl}?wrong=${encodeURIComponent(targetName)}` },
  { terminal: { exact: false, actions: 0 } }, { terminal: { exact: false, actions: 1 } },
  { createButtonCount: 0 }, { tokenNameCount: 1 }, { matchingRowCount: 1 },
];
for (const overrides of failureCases) {
  const failed = await run(overrides);
  assert.equal(failed.caught, null);
  for (const [key, value] of Object.entries({
    result: "V54_TOKEN_PAGE_SEMANTIC_READINESS_FAILED_STOP", errorClass: "Error",
    consumed: true, bindingEligible: false, bindingNull: true,
    predecessorRuntimeCleared: true, failureCleanupComplete: true,
  })) assert.equal(failed.output[key], value, key);
}

const throwStages = ["setup", "connect", "docs", "name", "openTabs", "claim", "gotoHome",
  "homeWait", "homeUrl", "homeSnapshot", "gotoToken", "tokenUrl", "searchWait",
  "tableWait", "inputEval", "initialEval", "fill", "noResultsWait", "filteredUrl",
  "terminalEval"];
for (const throwAt of throwStages) {
  const failed = await run({ throwAt });
  assert.equal(failed.caught, null, throwAt);
  assert.equal(failed.output.result, "V54_TOKEN_PAGE_SEMANTIC_READINESS_FAILED_STOP", throwAt);
  assert.equal(failed.output.errorClass, "Error", throwAt);
  assert.equal(failed.output.failureCleanupComplete, true, throwAt);
}

const predecessorBlock = source.slice(source.indexOf("const predecessorDeclarationsAbsent"),
  source.indexOf("const counters"));
const predecessorNames = [...predecessorBlock.matchAll(
  /typeof (secureConsole[A-Za-z0-9]+) === "undefined"/g)].map((match) => match[1]);
assert.equal(predecessorNames.length, 125);
for (const name of predecessorNames) {
  const contaminated = await run({}, `let ${name} = false;\n`);
  assert.equal(contaminated.caught, null, name);
  assert.equal(contaminated.fixture.effects.setup, 0, name);
  assert.equal(contaminated.fixture.effects.openTabs, 0, name);
  assert.equal(contaminated.output.result, "V54_TOKEN_PAGE_SEMANTIC_READINESS_FAILED_STOP", name);
  assert.equal(contaminated.output.consumed, true, name);
  assert.equal(contaminated.output.bindingEligible, false, name);
  assert.equal(contaminated.output.failureCleanupComplete, true, name);
}

const outputFailure = await run({ failFinalWrite: true });
assert.ok(outputFailure.caught instanceof Error);
assert.equal(outputFailure.fixture.effects.finalWriteFailed, true);
assert.equal(outputFailure.output, null);

console.log(JSON.stringify({ result: "PASS", executableBytes: Buffer.byteLength(candidate),
  executableSha256: sha256(candidate), sourceBytes: Buffer.byteLength(source),
  sourceSha256: sha256(source), fixtureBytes: fs.statSync(fileURLToPath(import.meta.url)).size,
  predecessorContaminations: predecessorNames.length,
  behavioralExecutions: 1 + failureCases.length + throwStages.length + predecessorNames.length + 1,
  terminalOutputCleanup: true, completeCounterVector: true }));
