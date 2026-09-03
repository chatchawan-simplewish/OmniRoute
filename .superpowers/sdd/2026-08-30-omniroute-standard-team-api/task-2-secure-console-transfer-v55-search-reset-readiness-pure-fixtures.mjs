import assert from "node:assert/strict";
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";

const directory = path.dirname(fileURLToPath(import.meta.url));
const sourcePath = path.join(directory,
  "task-2-secure-console-transfer-v55-search-reset-readiness-source.js");
const executablePath = path.join(directory,
  "task-2-secure-console-transfer-v55-search-reset-readiness-executable.js");
const designPath = path.join(directory,
  "task-2-secure-console-transfer-v55-search-reset-readiness-design.md");
const source = fs.readFileSync(sourcePath, "utf8").replace(/\r\n/g, "\n");
const candidate = fs.readFileSync(executablePath, "utf8").replace(/\r\n/g, "\n");
const design = fs.readFileSync(designPath, "utf8");
const sha256 = (value) => crypto.createHash("sha256").update(value).digest("hex").toUpperCase();

const persistentBindings = [
  "secureConsoleOwnedTaskTabV55", "secureConsoleOwnedTaskTabV55Eligible",
  "secureConsoleOwnedTaskTabV55State", "secureConsoleV55Consumed",
  "secureConsoleOwnedTaskTabV55PreCreateDetachConsumed",
  "secureConsoleOwnedTaskTabV55PostNativeDetachConsumed",
  "secureConsoleCloudflareReadsV55Consumed",
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
assert.equal(candidate, minimized.code + "\n");
assert.ok(Buffer.byteLength(candidate) <= 27000);
assert.match(candidate, /^[\x00-\x7F]*$/);
assert.equal((candidate.match(/\\u[0-9a-fA-F]{4}/g) ?? []).length, 0);
assert.equal([...candidate].filter((character) => character.codePointAt(0) > 127).length, 0);
assert.equal((candidate.match(/String\.fromCodePoint\(/g) ?? []).length, 1);
assert.ok(source.includes('String.fromCodePoint(0x1F510) + " OmniRoute secure console"'));
for (const binding of persistentBindings) assert.match(candidate, new RegExp(`\\b${binding}\\b`));
for (const pin of [
  "10619", "89D36435A31AE04E560A27D53D8A0953F19E837DF60837FADCF3DC174C0B9477",
]) assert.ok(candidate.includes(pin));
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
const terminalNeedle = `secureConsoleV55AttachmentEvidence = null;
      secureConsoleV55TerminalOutputFailure = null;
      throw terminalError;`;
assert.equal(source.split(terminalNeedle).length - 1, 1);
const terminalProbeSource = source.replace(terminalNeedle,
  `await nodeRepl.capture({tabNull:secureConsoleOwnedTaskTabV55===null,eligible:secureConsoleOwnedTaskTabV55Eligible,state:secureConsoleOwnedTaskTabV55State,preCreate:secureConsoleOwnedTaskTabV55PreCreateDetachConsumed,postNative:secureConsoleOwnedTaskTabV55PostNativeDetachConsumed,cloudflareReads:secureConsoleCloudflareReadsV55Consumed,consumed:secureConsoleV55Consumed,attachmentBindingNull:secureConsoleOwnedTaskTabV55Attachment===null,attachmentEligible:secureConsoleOwnedTaskTabV55AttachmentEligible,chromeNull:secureConsoleChromeV55Attachment===null,agentNull:secureConsoleAgentV55Attachment===null,setupNull:secureConsoleSetupBrowserRuntimeV55Attachment===null,downstreamCounters:{...counters},attachmentCounters:secureConsoleV55AttachmentEvidence});
      secureConsoleV55AttachmentEvidence = null;
      secureConsoleV55TerminalOutputFailure = null;
      throw terminalError;`);
const terminalProbeMinimized = await terser.minify(terminalProbeSource, {
  module: true,
  compress: { passes: 10, toplevel: true, top_retain: persistentBindings,
    unsafe: true, unsafe_comps: true, hoist_props: true, hoist_vars: true,
    evaluate: false },
  mangle: { toplevel: true, reserved: persistentBindings },
  format: { ascii_only: true, comments: false },
});
assert.equal(terminalProbeMinimized.error, undefined);
const terminalProbeExecutable = terminalProbeMinimized.code.replace(
  importLiteral, "Promise.resolve(__module)");
const documentationNeedle = `secureConsoleV55AttachmentEvidence = null;
    throw terminalOutputFailure;`;
assert.equal(source.split(documentationNeedle).length - 1, 1);
const documentationProbeSource = source.replace(documentationNeedle,
  `await nodeRepl.capture({tabNull:secureConsoleOwnedTaskTabV55===null,eligible:secureConsoleOwnedTaskTabV55Eligible,state:secureConsoleOwnedTaskTabV55State,preCreate:secureConsoleOwnedTaskTabV55PreCreateDetachConsumed,postNative:secureConsoleOwnedTaskTabV55PostNativeDetachConsumed,cloudflareReads:secureConsoleCloudflareReadsV55Consumed,consumed:secureConsoleV55Consumed,attachmentBindingNull:secureConsoleOwnedTaskTabV55Attachment===null,attachmentEligible:secureConsoleOwnedTaskTabV55AttachmentEligible,chromeNull:secureConsoleChromeV55Attachment===null,agentNull:secureConsoleAgentV55Attachment===null,setupNull:secureConsoleSetupBrowserRuntimeV55Attachment===null,attachmentCounters:secureConsoleV55AttachmentEvidence});
    secureConsoleV55AttachmentEvidence = null;
    throw terminalOutputFailure;`);
const documentationProbeMinimized = await terser.minify(documentationProbeSource, {
  module: true,
  compress: { passes: 10, toplevel: true, top_retain: persistentBindings,
    unsafe: true, unsafe_comps: true, hoist_props: true, hoist_vars: true,
    evaluate: false },
  mangle: { toplevel: true, reserved: persistentBindings },
  format: { ascii_only: true, comments: false },
});
assert.equal(documentationProbeMinimized.error, undefined);
const documentationProbeExecutable = documentationProbeMinimized.code.replace(
  importLiteral, "Promise.resolve(__module)");
const ordinaryNeedle = `    counters.writeAttempted++;
    try {`;
assert.equal(source.split(ordinaryNeedle).length - 1, 1);
const ordinaryProbeSource = source.replace(ordinaryNeedle,
  `    await nodeRepl.capture({tabNull:secureConsoleOwnedTaskTabV55===null,eligible:secureConsoleOwnedTaskTabV55Eligible,state:secureConsoleOwnedTaskTabV55State,preCreate:secureConsoleOwnedTaskTabV55PreCreateDetachConsumed,postNative:secureConsoleOwnedTaskTabV55PostNativeDetachConsumed,cloudflareReads:secureConsoleCloudflareReadsV55Consumed,consumed:secureConsoleV55Consumed,attachmentBindingNull:secureConsoleOwnedTaskTabV55Attachment===null,attachmentEligible:secureConsoleOwnedTaskTabV55AttachmentEligible,chromeNull:secureConsoleChromeV55Attachment===null,agentNull:secureConsoleAgentV55Attachment===null,setupNull:secureConsoleSetupBrowserRuntimeV55Attachment===null});
    counters.writeAttempted++;
    try {`);
const ordinaryProbeMinimized = await terser.minify(ordinaryProbeSource, {
  module: true,
  compress: { passes: 10, toplevel: true, top_retain: persistentBindings,
    unsafe: true, unsafe_comps: true, hoist_props: true, hoist_vars: true,
    evaluate: false },
  mangle: { toplevel: true, reserved: persistentBindings },
  format: { ascii_only: true, comments: false },
});
assert.equal(ordinaryProbeMinimized.error, undefined);
const ordinaryProbeExecutable = ordinaryProbeMinimized.code.replace(
  importLiteral, "Promise.resolve(__module)");
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
  inputTagName: "INPUT", inputType: "search", inputDisabled: false,
  headerLabels: ["Token name", "Permissions", "Resources", "Last used", "Expires", "Status"],
  baselineRowCount: 9, baselineTargetCount: 0, baselineBusy: false,
  noResultsCount: 1,
  filteredUrl: `${tokenUrl}?search=OmniRoute+secure+console+R5+20260901`,
  filteredRows: ["No results found for your search"],
  filteredTargetCount: 0, filteredActions: 0, filteredBusy: false,
  createButtonCount: 1, createLinkCount: 0, tokenNameCount: 0,
  matchingRowCount: 0, createVisible: true, throwAt: null, failFinalWrite: false,
  resetConverges: true, resetSettledUrl: tokenUrl,
};

function makeFixture(overrides = {}) {
  const config = { ...defaults, ...overrides };
  const effects = { setup: 0, connect: 0, docs: 0, names: 0, openTabs: 0,
    claims: 0, gotos: [], fills: 0, outputs: [], probes: [], ops: {},
    finalWriteFailed: false };
  const state = { currentUrl: tokenUrl, filterValue: config.initialValue, filtered: false };
  let inputEvalNumber = 0;
  let textLocatorNumber = 0;
  let baseUrlReadNumber = 0;
  const fail = (name) => { if (config.throwAt === name) throw Object.create(null); };
  const operate = async (name, action) => {
    const counts = effects.ops[name] ??= { attempted: 0, fulfilled: 0 };
    counts.attempted++;
    fail(name);
    const value = await action();
    counts.fulfilled++;
    return value;
  };
  const countLocator = (count, waitName, visible = true) => ({
    count: async () => operate(`${waitName}Count`, () => count),
    waitFor: async (options) => operate(options?.state === "hidden" ? "resetSentinelWait" : waitName, () => {
      if (options?.state === "hidden" ? visible : !visible) throw new Error("locator state");
    }),
    or(other) { return countLocator(count + other._count, "createWait", config.createVisible); },
    _count: count,
  });
  const input = {
    count: async () => operate("searchCount", () => config.searchCount),
    waitFor: async () => operate("searchWait", () => undefined),
    evaluate: async (fn) => { const names = ["initialInputEval", "finalInputEval", "targetInputEval"];
      return operate(names[inputEvalNumber++] ?? "inputEval", () => fn({ value: state.filterValue,
      tagName: config.inputTagName, type: config.inputType, disabled: config.inputDisabled }));
    },
    fill: async (value) => operate(value === "" ? "resetFill" : "fill", () => { effects.fills++; state.filterValue = value;
      if (value !== "") { state.filtered = true; state.currentUrl = config.filteredUrl; } }),
  };
  const makeTableDom = () => {
    const cell = (textContent) => ({ textContent });
    const filtered = state.filtered;
    const rows = filtered ? config.filteredRows.map(cell) :
      Array.from({ length: config.baselineRowCount }, (_, index) => cell(`row ${index}`));
    const targetCells = Array.from({ length: filtered ? config.filteredTargetCount :
      config.baselineTargetCount }, () => cell(targetName));
    const busy = filtered ? config.filteredBusy : config.baselineBusy;
    return {
      querySelectorAll(selector) {
        if (selector === "thead tr:first-child th, thead tr:first-child td") {
          return config.headerLabels.map(cell);
        }
        if (selector === "tbody tr") return rows;
        if (selector === "tbody td") return targetCells;
        if (selector === '[aria-label="Actions"]') {
          return Array.from({ length: config.filteredActions }, () => ({}));
        }
        throw new Error(`unexpected table selector ${selector}`);
      },
      matches: (selector) => selector === '[aria-busy="true"]' && busy,
      querySelector: (selector) => selector === '[aria-busy="true"]' && busy ? {} : null,
    };
  };
  const table = {
    count: async () => operate("tableCount", () => config.tableCount),
    waitFor: async () => operate("tableWait", () => undefined),
    evaluate: async (fn) => operate(state.filtered ? "terminalEval" : "initialEval",
      () => fn(makeTableDom())),
    getByText: () => countLocator(config.noResultsCount,
      textLocatorNumber++ === 0 ? "resetSentinelWait" : "noResultsWait", state.filtered),
    locator: () => ({ getByText: () => countLocator(config.tokenNameCount, "nameRead") }),
    getByRole: () => ({ filter: () => countLocator(config.matchingRowCount, "rowRead") }),
  };
  const body = { evaluate: async () => operate("homeSnapshot", () => config.homeSnapshot) };
  const playwright = {
    waitForTimeout: async (ms) => operate(ms === 0 ? "resetUrlWait" : "homeWait", () => undefined),
    waitForURL: async (url) => operate("resetUrlWait", () => {
      if (!config.resetConverges) throw new Error("reset timeout");
      state.currentUrl = config.resetSettledUrl;
      state.filtered = state.currentUrl !== tokenUrl;
      if (state.currentUrl !== url) throw new Error("wrong reset url");
    }),
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
    goto: async (url) => operate(url === "https://dash.cloudflare.com/" ? "gotoHome" : "gotoToken", () => {
      effects.gotos.push(url); state.currentUrl = url === "https://dash.cloudflare.com/" ?
        accountHomeUrl : tokenUrl; state.filterValue = config.initialValue; state.filtered = false; }),
    url: async () => operate(state.filtered ? "filteredUrl" :
      state.currentUrl === accountHomeUrl ? "homeUrl" :
      baseUrlReadNumber++ === 0 ? "navigationUrl" : "resetUrlRead", () => state.currentUrl) };
  const chrome = { documentation: async () => operate("docs", () => { effects.docs++; return config.docs; }),
    nameSession: async () => operate("name", () => { effects.names++; }),
    user: { openTabs: async () => operate("openTabs", () => { effects.openTabs++; return config.offered; }),
      claimTab: async () => operate("claim", () => { effects.claims++; return tab; }) } };
  const agent = { browsers: { get: async () => operate("connect", () => { effects.connect++; return chrome; }) } };
  const module = { setupBrowserRuntime: async () => operate("setup", () => { effects.setup++; return agent; }) };
  const nodeRepl = { write: async (value) => {
    const final = typeof value === "object" && value !== null;
    const name = final ? "finalWrite" : "docsWrite";
    const counts = effects.ops[name] ??= { attempted: 0, fulfilled: 0 };
    counts.attempted++;
    fail(name);
    if (final && config.failFinalWrite) {
      effects.finalWriteFailed = true;
      throw new Error("fixture final output failure");
    }
    effects.outputs.push(value);
    counts.fulfilled++;
  },
    capture: async (value) => { effects.probes.push(value); },
  };
  return { effects, module, nodeRepl };
}

async function run(overrides = {}, prelude = "", mode = "ordinary") {
  const fixture = makeFixture(overrides);
  let caught = null;
  const body = mode === "exact" ? executable :
    overrides.throwAt === "docsWrite" ? documentationProbeExecutable :
    overrides.failFinalWrite ? terminalProbeExecutable : ordinaryProbeExecutable;
  try { await new AsyncFunction("__module", "nodeRepl", `${prelude}${body}`)(
    fixture.module, fixture.nodeRepl); } catch (error) { caught = error; }
  const output = fixture.effects.outputs.find((value) => typeof value === "object" && value !== null) ?? null;
  return { fixture, output, caught };
}

const pair = (effects, name) => {
  const value = effects.ops[name] ?? { attempted: 0, fulfilled: 0 };
  return [value.attempted, value.fulfilled];
};
const sumPairs = (effects, names) => names.reduce((total, name) => {
  const value = pair(effects, name);
  return [total[0] + value[0], total[1] + value[1]];
}, [0, 0]);
const assertPair = (object, prefix, expected) => {
  assert.deepEqual([object[`${prefix}Attempted`], object[`${prefix}Fulfilled`]],
    expected, prefix);
};
function assertAttachmentCounterEvidence(attachment, effects) {
  const importExpected = pair(effects, "setup")[0] > 0 ? [1, 1] : [0, 0];
  assertPair(attachment, "import", importExpected);
  for (const [prefix, operation] of [
    ["setup", "setup"], ["connect", "connect"],
    ["documentation", "docs"], ["documentationWrite", "docsWrite"],
    ["name", "name"], ["openTabs", "openTabs"], ["claim", "claim"],
    ["navigation", "gotoHome"], ["wait", "homeWait"],
    ["url", "homeUrl"], ["snapshot", "homeSnapshot"],
  ]) assertPair(attachment, prefix, pair(effects, operation));
}
function assertCounterEvidence(runResult) {
  const { output, fixture } = runResult;
  const effects = fixture.effects;
  assertAttachmentCounterEvidence(output.attachment, effects);
  const bindingExpected = pair(effects, "gotoToken")[0] > 0 ? [1, 1] : [0, 0];
  assertPair(output, "binding", bindingExpected);
  assertPair(output, "navigation", pair(effects, "gotoToken"));
  const resetUrlReads = pair(effects, "resetUrlWait")[1];
  const navigationUrl = pair(effects, "navigationUrl");
  assertPair(output, "url", [navigationUrl[0] + pair(effects, "filteredUrl")[0],
    navigationUrl[1] + pair(effects, "filteredUrl")[1]]);
  assertPair(output, "readiness",
    sumPairs(effects, ["searchWait", "tableWait", "noResultsWait"]));
  assertPair(output, "initialRead", pair(effects, "initialInputEval"));
  assertPair(output, "fill", pair(effects, "fill"));
  assertPair(output, "resetFill", pair(effects, "resetFill"));
  assertPair(output, "resetUrlWait", pair(effects, "resetUrlWait"));
  const resetWait = pair(effects, "resetUrlWait");
  const resetReads = pair(effects, "resetUrlRead");
  assertPair(output, "resetUrlRead", resetReads);
  assertPair(output, "resetSentinelWait", pair(effects, "resetSentinelWait"));
  assertPair(output, "resetSentinelRead", pair(effects, "resetSentinelWaitCount"));
  assertPair(output, "finalRead", pair(effects, "finalInputEval"));
  assertPair(output, "baselineRead", pair(effects, "initialEval"));
  assertPair(output, "filteredRead", pair(effects, "terminalEval"));
  const createAttempted = pair(effects, "createWait")[0] > 0 ? 1 : 0;
  const createFulfilled = pair(effects, "createWait")[1] === 1 &&
    pair(effects, "createWaitCount")[1] === 1 ? 1 : 0;
  assertPair(output, "createRead", [createAttempted, createFulfilled]);
  assertPair(output, "nameRead", pair(effects, "nameReadCount"));
  assertPair(output, "rowRead", pair(effects, "rowReadCount"));
  assert.equal(output.writeAttempted, pair(effects, "finalWrite")[0]);
}
function assertPersistentProbe(runResult, successful) {
  assert.equal(runResult.fixture.effects.probes.length, 1);
  const probe = runResult.fixture.effects.probes[0];
  for (const [key, value] of Object.entries({ tabNull: !successful,
    eligible: successful,
    state: successful ? "TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE" :
      "V55_TOKEN_PAGE_SEMANTIC_READINESS_FAILED",
    preCreate: false, postNative: false, cloudflareReads: false, consumed: true,
    attachmentBindingNull: true, attachmentEligible: false, chromeNull: true,
    agentNull: true, setupNull: true,
  })) assert.equal(probe[key], value, key);
}

const success = await run();
assert.equal(success.caught, null);
assert.equal(success.output.result, "EXACT_V55_TOKEN_PAGE_SEMANTIC_READINESS_PASS");
assert.equal(success.output.attachment.result,
  "EXACT_V55Attachment_CROSS_REALM_TASK_TAB_ACCOUNT_HOME_REACQUISITION_PASS");
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
assertCounterEvidence(success);
assertPersistentProbe(success, true);
const exactCandidateSuccess = await run({}, "", "exact");
assert.equal(exactCandidateSuccess.caught, null);
assert.deepEqual(exactCandidateSuccess.output, success.output);
assert.equal(exactCandidateSuccess.fixture.effects.probes.length, 0);
assertCounterEvidence(exactCandidateSuccess);
const linkOnlySuccess = await run({ createButtonCount: 0, createLinkCount: 1 });
assert.equal(linkOnlySuccess.output.result, "EXACT_V55_TOKEN_PAGE_SEMANTIC_READINESS_PASS");
assertCounterEvidence(linkOnlySuccess);
assertPersistentProbe(linkOnlySuccess, true);
const staleSuccess = await run({ initialValue: "stale" });
assert.equal(staleSuccess.output.result, "EXACT_V55_TOKEN_PAGE_SEMANTIC_READINESS_PASS");
assert.deepEqual([staleSuccess.output.resetFillAttempted, staleSuccess.output.resetFillFulfilled], [1, 1]);
assertCounterEvidence(staleSuccess);
assertPersistentProbe(staleSuccess, true);
for (const resetFailure of [
  { initialValue: "stale", resetConverges: false },
  { initialValue: "stale", resetSettledUrl: `${tokenUrl}?search=stale` },
]) {
  const failed = await run(resetFailure);
  assert.equal(failed.output.result, "V55_TOKEN_PAGE_SEMANTIC_READINESS_FAILED_STOP");
  assert.deepEqual([failed.output.resetUrlWaitAttempted, failed.output.resetUrlWaitFulfilled], [1, 0]);
  assert.deepEqual([failed.output.resetUrlReadAttempted, failed.output.resetUrlReadFulfilled], [0, 0]);
  assert.deepEqual([failed.output.baselineReadAttempted, failed.output.baselineReadFulfilled], [0, 0]);
  assertPersistentProbe(failed, false);
}

const failureCases = [
  { docs: "bad" }, { offered: [] },
  { offered: [exactTab, { ...exactTab, id: "duplicate" }] }, { claimId: "wrong" },
  { homeSnapshot: { ...defaults.homeSnapshot, exactZoneHrefCount: 0 } },
  { searchCount: 0 }, { searchCount: 2 }, { tableCount: 0 }, { tableCount: 2 },
  { inputTagName: "DIV" }, { inputType: "hidden" },
  { inputDisabled: true },
  { headerLabels: ["Permissions", "Token name", "Resources", "Last used", "Expires", "Status"] },
  { baselineRowCount: 0 }, { baselineRowCount: 1001 }, { baselineBusy: true },
  { baselineTargetCount: 1 }, { noResultsCount: 0 }, { noResultsCount: 2 },
  { filteredUrl: tokenUrl },
  { filteredUrl: `${tokenUrl}?wrong=${encodeURIComponent(targetName)}` },
  { filteredUrl: `https://example.com/profile/api-tokens?search=${encodeURIComponent(targetName)}` },
  { filteredUrl: `https://dash.cloudflare.com/wrong?search=${encodeURIComponent(targetName)}` },
  { filteredUrl: `${tokenUrl}?search=${encodeURIComponent(targetName)}#fragment` },
  { filteredUrl: `${tokenUrl}?search=${encodeURIComponent(targetName)}&extra=1` },
  { filteredUrl: `${tokenUrl}?search=${encodeURIComponent(targetName)}&search=${encodeURIComponent(targetName)}` },
  { filteredRows: [] },
  { filteredRows: ["No results found for your search", "No results found for your search"] },
  { filteredRows: ["Wrong result"] }, { filteredBusy: true },
  { filteredTargetCount: 1 }, { filteredActions: 1 },
  { createButtonCount: 0 }, { createButtonCount: 2 },
  { createButtonCount: 1, createLinkCount: 1 }, { createVisible: false },
  { tokenNameCount: 1 }, { matchingRowCount: 1 },
];
for (const overrides of failureCases) {
  const failed = await run(overrides);
  assert.equal(failed.caught, null);
  for (const [key, value] of Object.entries({
    result: "V55_TOKEN_PAGE_SEMANTIC_READINESS_FAILED_STOP", errorClass: "Error",
    consumed: true, bindingEligible: false, bindingNull: true,
    predecessorRuntimeCleared: true, failureCleanupComplete: true,
  })) assert.equal(failed.output[key], value, key);
  assertCounterEvidence(failed);
  assertPersistentProbe(failed, false);
}

const throwStages = ["setup", "connect", "docs", "name", "openTabs", "claim", "gotoHome",
  "homeWait", "homeUrl", "homeSnapshot", "gotoToken", "navigationUrl", "searchWait",
  "searchCount", "tableCount", "tableWait", "initialInputEval", "resetFill", "resetUrlWait",
  "resetUrlRead", "resetSentinelWait", "resetSentinelWaitCount", "finalInputEval", "initialEval", "fill",
  "noResultsWait", "noResultsWaitCount", "filteredUrl", "terminalEval",
  "createWait", "createWaitCount", "nameReadCount", "rowReadCount"];
for (const throwAt of throwStages) {
  const failed = await run({ throwAt, ...(throwAt === "resetFill" ? { initialValue: "stale" } : {}) });
  assert.equal(failed.caught, null, throwAt);
  assert.equal(failed.output.result, "V55_TOKEN_PAGE_SEMANTIC_READINESS_FAILED_STOP", throwAt);
  assert.equal(failed.output.errorClass, "Error", throwAt);
  assert.equal(failed.output.failureCleanupComplete, true, throwAt);
  assertCounterEvidence(failed);
  assertPersistentProbe(failed, false);
}

const predecessorBlock = source.slice(source.indexOf("const predecessorDeclarationsAbsent"),
  source.indexOf("const counters"));
const predecessorNames = [...predecessorBlock.matchAll(
  /typeof (secureConsole[A-Za-z0-9]+) === "undefined"/g)].map((match) => match[1]);
assert.equal(predecessorNames.length, 132);
for (const name of predecessorNames) {
  const contaminated = await run({}, `let ${name} = false;\n`);
  assert.equal(contaminated.caught, null, name);
  assert.equal(contaminated.fixture.effects.setup, 0, name);
  assert.equal(contaminated.fixture.effects.openTabs, 0, name);
  assert.equal(contaminated.output.result, "V55_TOKEN_PAGE_SEMANTIC_READINESS_FAILED_STOP", name);
  assert.equal(contaminated.output.consumed, true, name);
  assert.equal(contaminated.output.bindingEligible, false, name);
  assert.equal(contaminated.output.failureCleanupComplete, true, name);
  assertCounterEvidence(contaminated);
  assertPersistentProbe(contaminated, false);
}

const documentationOutputFailure = await run({ throwAt: "docsWrite" });
assert.ok(documentationOutputFailure.caught);
assert.equal(documentationOutputFailure.output, null);
assert.equal(documentationOutputFailure.fixture.effects.probes.length, 1);
const documentationFailureProbe = documentationOutputFailure.fixture.effects.probes[0];
for (const [key, value] of Object.entries({ tabNull: true, eligible: false,
  state: "UNADOPTED", preCreate: false, postNative: false,
  cloudflareReads: false, consumed: true, attachmentBindingNull: true,
  attachmentEligible: false, chromeNull: true, agentNull: true, setupNull: true,
})) assert.equal(documentationFailureProbe[key], value, key);
assert.equal(documentationFailureProbe.attachmentCounters.result,
  "V55Attachment_FRESH_CROSS_REALM_TASK_REACQUISITION_FAILED_STOP");
assert.equal(documentationFailureProbe.attachmentCounters.failureCleanupComplete, true);
assertAttachmentCounterEvidence(documentationFailureProbe.attachmentCounters,
  documentationOutputFailure.fixture.effects);

const outputFailure = await run({ failFinalWrite: true });
assert.ok(outputFailure.caught instanceof Error);
assert.equal(outputFailure.fixture.effects.finalWriteFailed, true);
assert.equal(outputFailure.output, null);
assert.equal(outputFailure.fixture.effects.probes.length, 1);
const outputFailureProbe = outputFailure.fixture.effects.probes[0];
assert.equal(outputFailureProbe.tabNull, true);
assert.equal(outputFailureProbe.eligible, false);
assert.equal(outputFailureProbe.state, "V55_FINAL_OUTPUT_FAILED_STOP");
assert.equal(outputFailureProbe.preCreate, false);
assert.equal(outputFailureProbe.postNative, false);
assert.equal(outputFailureProbe.cloudflareReads, false);
assert.equal(outputFailureProbe.consumed, true);
assert.equal(outputFailureProbe.attachmentBindingNull, true);
assert.equal(outputFailureProbe.attachmentEligible, false);
assert.equal(outputFailureProbe.chromeNull, true);
assert.equal(outputFailureProbe.agentNull, true);
assert.equal(outputFailureProbe.setupNull, true);
assert.equal(outputFailureProbe.attachmentCounters.result,
  "EXACT_V55Attachment_CROSS_REALM_TASK_TAB_ACCOUNT_HOME_REACQUISITION_PASS");
assertCounterEvidence({ fixture: outputFailure.fixture,
  output: { ...outputFailureProbe.downstreamCounters,
    attachment: outputFailureProbe.attachmentCounters } });

const terminalOutputCleanup = true;
const completeCounterVector = true;

console.log(JSON.stringify({ result: "PASS", executableBytes: Buffer.byteLength(candidate),
  executableSha256: sha256(candidate), sourceBytes: Buffer.byteLength(source),
  sourceSha256: sha256(source), fixtureBytes: fs.statSync(fileURLToPath(import.meta.url)).size,
  predecessorContaminations: predecessorNames.length,
  behavioralExecutions: 3 + failureCases.length + throwStages.length + predecessorNames.length + 2,
  terminalOutputCleanup, completeCounterVector }));
