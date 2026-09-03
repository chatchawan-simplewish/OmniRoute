import assert from "node:assert/strict";
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";

const directory = path.dirname(fileURLToPath(import.meta.url));
const sourcePath = path.join(directory,
  "task-2-secure-console-transfer-v57-vm-module-source.js");
const executablePath = path.join(directory,
  "task-2-secure-console-transfer-v57-vm-module-executable.mjs");
const designPath = path.join(directory,
  "task-2-secure-console-transfer-v57-vm-module-design.md");
const loaderPath = path.join(directory,
  "task-2-secure-console-transfer-v57-vm-module-loader-cell.js");
const v56SourcePath = path.join(directory,
  "task-2-secure-console-transfer-v56-disk-module-source.js");
const source = fs.readFileSync(sourcePath, "utf8").replace(/\r\n/g, "\n");
const candidate = fs.readFileSync(executablePath, "utf8").replace(/\r\n/g, "\n");
const design = fs.readFileSync(designPath, "utf8");
const loader = fs.readFileSync(loaderPath, "utf8").replace(/\r\n/g, "\n");
const v56Source = fs.readFileSync(v56SourcePath, "utf8").replace(/\r\n/g, "\n");
const sha256 = (value) => crypto.createHash("sha256").update(value).digest("hex").toUpperCase();

const persistentBindings = [
  "secureConsoleOwnedTaskTabV57", "secureConsoleOwnedTaskTabV57Eligible",
  "secureConsoleOwnedTaskTabV57State", "secureConsoleV57Consumed",
  "secureConsoleOwnedTaskTabV57PreCreateDetachConsumed",
  "secureConsoleOwnedTaskTabV57PostNativeDetachConsumed",
  "secureConsoleCloudflareReadsV57Consumed",
];
const freshV56Names = [
  "secureConsoleOwnedTaskTabV56", "secureConsoleOwnedTaskTabV56Eligible",
  "secureConsoleOwnedTaskTabV56State",
  "secureConsoleOwnedTaskTabV56PreCreateDetachConsumed",
  "secureConsoleOwnedTaskTabV56PostNativeDetachConsumed",
  "secureConsoleCloudflareReadsV56Consumed", "secureConsoleV56Consumed",
  "secureConsoleV56Module",
];
const predecessorNeedle = '      typeof secureConsoleV54Consumed === "undefined";';
const predecessorReplacement = `${predecessorNeedle.slice(0, -1)} &&\n${
  freshV56Names.map((name, index) =>
    `      typeof ${name} === "undefined"${index === freshV56Names.length - 1 ? ";" : " &&"}`
  ).join("\n")}`;
const renamedV56Source = v56Source.replaceAll("V56", "V57");
assert.equal(renamedV56Source.split(predecessorNeedle).length - 1, 1);
assert.equal(source, renamedV56Source.replace(predecessorNeedle, predecessorReplacement));
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
assert.ok(Buffer.byteLength(candidate) < Buffer.byteLength(source));
assert.match(candidate, /^[\x00-\x7F]*$/);
assert.equal((candidate.match(/\\u[0-9a-fA-F]{4}/g) ?? []).length, 0);
assert.equal([...candidate].filter((character) => character.codePointAt(0) > 127).length, 0);
assert.equal((candidate.match(/String\.fromCodePoint\(/g) ?? []).length, 1);
assert.ok(source.includes('String.fromCodePoint(0x1F510) + " OmniRoute secure console"'));
for (const binding of persistentBindings) assert.match(candidate, new RegExp(`\\b${binding}\\b`));
const withoutModuleExport = (value) => {
  const matches = [...value.matchAll(/export\{([^}]+)\};/g)];
  assert.equal(matches.length, 1);
  const exported = matches[0][1].split(",").map((name) => name.trim()).sort();
  assert.deepEqual(exported, [...persistentBindings].sort());
  return value.replace(matches[0][0], "");
};
const candidateBody = withoutModuleExport(candidate);
for (const pin of [
  "10619", "89D36435A31AE04E560A27D53D8A0953F19E837DF60837FADCF3DC174C0B9477",
]) assert.ok(candidate.includes(pin));
new (Object.getPrototypeOf(async function () {}).constructor)(candidateBody);

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
const executable = candidateBody.replace(importLiteral, "Promise.resolve(__module)");
const terminalNeedle = `secureConsoleV57AttachmentEvidence = null;
      secureConsoleV57TerminalOutputFailure = null;
      throw terminalError;`;
assert.equal(source.split(terminalNeedle).length - 1, 1);
const terminalProbeSource = source.replace(terminalNeedle,
  `await nodeRepl.capture({tabNull:secureConsoleOwnedTaskTabV57===null,eligible:secureConsoleOwnedTaskTabV57Eligible,state:secureConsoleOwnedTaskTabV57State,preCreate:secureConsoleOwnedTaskTabV57PreCreateDetachConsumed,postNative:secureConsoleOwnedTaskTabV57PostNativeDetachConsumed,cloudflareReads:secureConsoleCloudflareReadsV57Consumed,consumed:secureConsoleV57Consumed,attachmentBindingNull:secureConsoleOwnedTaskTabV57Attachment===null,attachmentEligible:secureConsoleOwnedTaskTabV57AttachmentEligible,chromeNull:secureConsoleChromeV57Attachment===null,agentNull:secureConsoleAgentV57Attachment===null,setupNull:secureConsoleSetupBrowserRuntimeV57Attachment===null,downstreamCounters:{...counters},attachmentCounters:secureConsoleV57AttachmentEvidence});
      secureConsoleV57AttachmentEvidence = null;
      secureConsoleV57TerminalOutputFailure = null;
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
const terminalProbeExecutable = withoutModuleExport(terminalProbeMinimized.code).replace(
  importLiteral, "Promise.resolve(__module)");
const documentationNeedle = `secureConsoleV57AttachmentEvidence = null;
    throw terminalOutputFailure;`;
assert.equal(source.split(documentationNeedle).length - 1, 1);
const documentationProbeSource = source.replace(documentationNeedle,
  `await nodeRepl.capture({tabNull:secureConsoleOwnedTaskTabV57===null,eligible:secureConsoleOwnedTaskTabV57Eligible,state:secureConsoleOwnedTaskTabV57State,preCreate:secureConsoleOwnedTaskTabV57PreCreateDetachConsumed,postNative:secureConsoleOwnedTaskTabV57PostNativeDetachConsumed,cloudflareReads:secureConsoleCloudflareReadsV57Consumed,consumed:secureConsoleV57Consumed,attachmentBindingNull:secureConsoleOwnedTaskTabV57Attachment===null,attachmentEligible:secureConsoleOwnedTaskTabV57AttachmentEligible,chromeNull:secureConsoleChromeV57Attachment===null,agentNull:secureConsoleAgentV57Attachment===null,setupNull:secureConsoleSetupBrowserRuntimeV57Attachment===null,attachmentCounters:secureConsoleV57AttachmentEvidence});
    secureConsoleV57AttachmentEvidence = null;
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
const documentationProbeExecutable = withoutModuleExport(documentationProbeMinimized.code).replace(
  importLiteral, "Promise.resolve(__module)");
const ordinaryNeedle = `    counters.writeAttempted++;
    try {`;
assert.equal(source.split(ordinaryNeedle).length - 1, 1);
const ordinaryProbeSource = source.replace(ordinaryNeedle,
  `    await nodeRepl.capture({tabNull:secureConsoleOwnedTaskTabV57===null,eligible:secureConsoleOwnedTaskTabV57Eligible,state:secureConsoleOwnedTaskTabV57State,preCreate:secureConsoleOwnedTaskTabV57PreCreateDetachConsumed,postNative:secureConsoleOwnedTaskTabV57PostNativeDetachConsumed,cloudflareReads:secureConsoleCloudflareReadsV57Consumed,consumed:secureConsoleV57Consumed,attachmentBindingNull:secureConsoleOwnedTaskTabV57Attachment===null,attachmentEligible:secureConsoleOwnedTaskTabV57AttachmentEligible,chromeNull:secureConsoleChromeV57Attachment===null,agentNull:secureConsoleAgentV57Attachment===null,setupNull:secureConsoleSetupBrowserRuntimeV57Attachment===null});
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
const ordinaryProbeExecutable = withoutModuleExport(ordinaryProbeMinimized.code).replace(
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
  initialUrl: tokenUrl, initialTableFiltered: false, staleAfterNavigationRead: false,
  resetConverges: true, resetSettledUrl: tokenUrl, resetSettledTableFiltered: false,
};

function makeFixture(overrides = {}) {
  const config = { ...defaults, ...overrides };
  const effects = { setup: 0, connect: 0, docs: 0, names: 0, openTabs: 0,
    claims: 0, gotos: [], fills: 0, resetSnapshots: [], outputs: [], probes: [], ops: {},
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
      if (value === "") effects.resetSnapshots.push({ input: state.filterValue, url: state.currentUrl, filtered: state.filtered });
      else { state.filtered = true; state.currentUrl = config.filteredUrl; } }),
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
      state.filtered = config.resetSettledTableFiltered;
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
    url: async () => { const current = state.currentUrl;
      const name = state.filtered ? "filteredUrl" : current === accountHomeUrl ? "homeUrl" :
        baseUrlReadNumber++ === 0 ? "navigationUrl" : "resetUrlRead";
      return operate(name, () => { if (name === "navigationUrl" && config.staleAfterNavigationRead) {
        state.currentUrl = config.initialUrl; state.filtered = config.initialTableFiltered;
      } return current; }); } };
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

let behavioralExecutions = 0;
async function run(overrides = {}, prelude = "", mode = "ordinary") {
  behavioralExecutions++;
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
      "V57_TOKEN_PAGE_SEMANTIC_READINESS_FAILED",
    preCreate: false, postNative: false, cloudflareReads: false, consumed: true,
    attachmentBindingNull: true, attachmentEligible: false, chromeNull: true,
    agentNull: true, setupNull: true,
  })) assert.equal(probe[key], value, key);
}

const success = await run();
assert.equal(success.caught, null);
assert.equal(success.output.result, "EXACT_V57_TOKEN_PAGE_SEMANTIC_READINESS_PASS");
assert.equal(success.output.attachment.result,
  "EXACT_V57Attachment_CROSS_REALM_TASK_TAB_ACCOUNT_HOME_REACQUISITION_PASS");
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
assert.equal(linkOnlySuccess.output.result, "EXACT_V57_TOKEN_PAGE_SEMANTIC_READINESS_PASS");
assertCounterEvidence(linkOnlySuccess);
assertPersistentProbe(linkOnlySuccess, true);
const staleSuccess = await run({ initialValue: "stale", initialUrl: `${tokenUrl}?search=stale`,
  initialTableFiltered: true, staleAfterNavigationRead: true, resetSettledUrl: tokenUrl, resetSettledTableFiltered: false });
assert.equal(staleSuccess.output.result, "EXACT_V57_TOKEN_PAGE_SEMANTIC_READINESS_PASS");
assert.deepEqual([staleSuccess.output.resetFillAttempted, staleSuccess.output.resetFillFulfilled], [1, 1]);
assert.deepEqual(staleSuccess.fixture.effects.resetSnapshots, [{ input: "", url: `${tokenUrl}?search=stale`, filtered: true }]);
assert.equal(staleSuccess.fixture.effects.ops.resetUrlWait.fulfilled, 1);
assert.equal(staleSuccess.fixture.effects.ops.resetSentinelWait.fulfilled, 1);
assertCounterEvidence(staleSuccess);
assertPersistentProbe(staleSuccess, true);
for (const resetFailure of [
  { initialValue: "stale", initialUrl: `${tokenUrl}?search=stale`, initialTableFiltered: true, staleAfterNavigationRead: true, resetConverges: false },
  { initialValue: "stale", initialUrl: `${tokenUrl}?search=stale`, initialTableFiltered: true,
    staleAfterNavigationRead: true, resetSettledUrl: `${tokenUrl}?search=stale`, resetSettledTableFiltered: true },
]) {
  const failed = await run(resetFailure);
  assert.equal(failed.output.result, "V57_TOKEN_PAGE_SEMANTIC_READINESS_FAILED_STOP");
  assert.deepEqual([failed.output.resetUrlWaitAttempted, failed.output.resetUrlWaitFulfilled], [1, 0]);
  assert.deepEqual([failed.output.resetUrlReadAttempted, failed.output.resetUrlReadFulfilled], [0, 0]);
  assert.deepEqual([failed.output.baselineReadAttempted, failed.output.baselineReadFulfilled], [0, 0]);
  assertPersistentProbe(failed, false);
}
const visibleSentinel = await run({ initialValue: "stale", initialUrl: `${tokenUrl}?search=stale`,
  initialTableFiltered: true, staleAfterNavigationRead: true, resetSettledUrl: tokenUrl,
  resetSettledTableFiltered: true });
assert.equal(visibleSentinel.output.result, "V57_TOKEN_PAGE_SEMANTIC_READINESS_FAILED_STOP");
for (const [prefix, vector] of Object.entries({
  resetUrlWait: [1, 1], resetUrlRead: [1, 1], resetSentinelWait: [1, 0],
  resetSentinelRead: [0, 0], finalRead: [0, 0], baselineRead: [0, 0],
  fill: [0, 0], filteredRead: [0, 0], createRead: [0, 0], nameRead: [0, 0], rowRead: [0, 0],
})) assert.deepEqual([visibleSentinel.output[`${prefix}Attempted`], visibleSentinel.output[`${prefix}Fulfilled`]], vector, prefix);
assert.equal(visibleSentinel.output.bindingEligible, false);
assert.equal(visibleSentinel.output.bindingNull, true);
assert.equal(visibleSentinel.output.failureCleanupComplete, true);
assertPersistentProbe(visibleSentinel, false);

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
    result: "V57_TOKEN_PAGE_SEMANTIC_READINESS_FAILED_STOP", errorClass: "Error",
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
  assert.equal(failed.output.result, "V57_TOKEN_PAGE_SEMANTIC_READINESS_FAILED_STOP", throwAt);
  assert.equal(failed.output.errorClass, "Error", throwAt);
  assert.equal(failed.output.failureCleanupComplete, true, throwAt);
  assertCounterEvidence(failed);
  assertPersistentProbe(failed, false);
}

const predecessorBlock = source.slice(source.indexOf("const predecessorDeclarationsAbsent"),
  source.indexOf("const counters"));
const predecessorNames = [...predecessorBlock.matchAll(
  /typeof (secureConsole[A-Za-z0-9]+) === "undefined"/g)].map((match) => match[1]);
assert.equal(predecessorNames.length, 140);
assert.deepEqual(predecessorNames.slice(-freshV56Names.length), freshV56Names);
for (const name of predecessorNames) {
  const contaminated = await run({}, `let ${name} = false;\n`);
  assert.equal(contaminated.caught, null, name);
  assert.equal(contaminated.fixture.effects.setup, 0, name);
  assert.equal(contaminated.fixture.effects.openTabs, 0, name);
  assert.equal(contaminated.output.result, "V57_TOKEN_PAGE_SEMANTIC_READINESS_FAILED_STOP", name);
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
  "V57Attachment_FRESH_CROSS_REALM_TASK_REACQUISITION_FAILED_STOP");
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
assert.equal(outputFailureProbe.state, "V57_FINAL_OUTPUT_FAILED_STOP");
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
  "EXACT_V57Attachment_CROSS_REALM_TASK_TAB_ACCOUNT_HOME_REACQUISITION_PASS");
assertCounterEvidence({ fixture: outputFailure.fixture,
  output: { ...outputFailureProbe.downstreamCounters,
    attachment: outputFailureProbe.attachmentCounters } });

const terminalOutputCleanup = true;
const completeCounterVector = true;
assert.equal(behavioralExecutions - freshV56Names.length, 212);
assert.equal(behavioralExecutions, 220);

const expectedModulePath = "C:/ChatGPT Projects/SW-Selfhosted-Network/.worktrees/omniroute-agent-routing-source/.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v57-vm-module-executable.mjs";
const expectedModuleSha256 = sha256(candidate);
const browserClientUrl = "file:///C:/Users/chatc/.codex/plugins/cache/openai-bundled/chrome/26.901.20858/scripts/browser-client.mjs";
const browserImport = "import(browserClientUrl)";
assert.equal(loader.split('import("node:fs")').length - 1, 1);
assert.equal(loader.split('import("node:crypto")').length - 1, 1);
assert.equal(loader.split('import("node:vm")').length - 1, 1);
assert.equal(loader.split("readFileSync(modulePath)").length - 1, 1);
assert.equal(loader.split(browserImport).length - 1, 1);
assert.equal(loader.split("new SourceTextModule(").length - 1, 1);
assert.equal(loader.split("new SyntheticModule(").length - 1, 1);
assert.equal(loader.split("await sourceModule.evaluate()").length - 1, 1);
assert.equal(loader.split("await bridge.evaluate()").length - 1, 1);
assert.ok(loader.includes(`const expectedBytes = ${Buffer.byteLength(candidate)};`));
assert.ok(loader.includes(`const expectedSha256 = "${expectedModuleSha256}";`));
assert.ok(loader.includes(`const modulePath = "${expectedModulePath}";`));
assert.ok(loader.includes(`const browserClientUrl = "${browserClientUrl}";`));
assert.ok(loader.includes('new SyntheticModule(["setupBrowserRuntime"]'));
for (const prohibited of ["data:", "import(modulePath", "Promise.race", ".catch(",
  "while (", "for (", "http://", "https://"])
  assert.equal(loader.includes(prohibited), false, prohibited);

const loaderExecutable = loader
  .replace('import("node:fs")', "Promise.resolve(__fs)")
  .replace('import("node:crypto")', "Promise.resolve(__crypto)")
  .replace('import("node:vm")', "Promise.resolve(__vm)")
  .replace(browserImport, "__loadBrowser(browserClientUrl)")
  .replace(`const expectedBytes = ${Buffer.byteLength(candidate)};`,
    "const expectedBytes = __expectedBytes;")
  .replace(`const expectedSha256 = "${expectedModuleSha256}";`,
    "const expectedSha256 = __expectedSha256;")
  .replaceAll("globalThis.secureConsoleV57Module", "__global.secureConsoleV57Module");
async function runLoader({ bytes = Buffer.from(candidate), readError = false,
  acceptBytes = false, vmMissing = false, browserImportError = false,
  browserModule = null } = {}) {
  const state = { secureConsoleV57Module: "residue" };
  const reads = [];
  const browserImports = [];
  const stats = { sourceConstructed: 0, sourceLinks: 0, sourceEvaluations: 0,
    staticLinkRequests: 0, bridgeConstructed: 0, bridgeLinks: 0,
    bridgeEvaluations: 0 };
  const fixture = makeFixture();
  const __fs = { readFileSync(filePath) {
    reads.push(filePath);
    if (readError) throw new Error("fixture read failure");
    return bytes;
  } };
  class CountingSourceTextModule extends vm.SourceTextModule {
    constructor(...args) { super(...args); stats.sourceConstructed++; }
    async link(linker) {
      stats.sourceLinks++;
      return super.link((...args) => { stats.staticLinkRequests++; return linker(...args); });
    }
    async evaluate(...args) { stats.sourceEvaluations++; return super.evaluate(...args); }
  }
  class CountingSyntheticModule extends vm.SyntheticModule {
    constructor(...args) { super(...args); stats.bridgeConstructed++; }
    async link(...args) { stats.bridgeLinks++; return super.link(...args); }
    async evaluate(...args) { stats.bridgeEvaluations++; return super.evaluate(...args); }
  }
  const __vm = { createContext: vm.createContext,
    SourceTextModule: vmMissing ? undefined : CountingSourceTextModule,
    SyntheticModule: CountingSyntheticModule };
  const __loadBrowser = async (specifier) => {
    browserImports.push(specifier);
    if (browserImportError) throw new Error("fixture browser import failure");
    return browserModule ?? { setupBrowserRuntime: fixture.module.setupBrowserRuntime };
  };
  const expectedBytes = acceptBytes ? bytes.length : Buffer.byteLength(candidate);
  const expectedSha256 = acceptBytes ? sha256(bytes) : expectedModuleSha256;
  let caught = null;
  try { await new AsyncFunction("__fs", "__crypto", "__vm", "__loadBrowser",
    "__global", "__expectedBytes", "__expectedSha256", "nodeRepl", "URL",
    loaderExecutable)(__fs, crypto, __vm, __loadBrowser, state, expectedBytes,
    expectedSha256, fixture.nodeRepl, URL); } catch (error) { caught = error; }
  const output = fixture.effects.outputs.find(
    (value) => typeof value === "object" && value !== null) ?? null;
  return { browserImports, caught, fixture, output, reads, state, stats };
}

const loaderSuccess = await runLoader();
assert.equal(loaderSuccess.caught, null);
assert.deepEqual(loaderSuccess.reads, [expectedModulePath]);
assert.deepEqual(loaderSuccess.browserImports, [browserClientUrl]);
assert.deepEqual(loaderSuccess.stats, { sourceConstructed: 1, sourceLinks: 1,
  sourceEvaluations: 1, staticLinkRequests: 0, bridgeConstructed: 1,
  bridgeLinks: 1, bridgeEvaluations: 1 });
assert.equal(loaderSuccess.output.result,
  "EXACT_V57_TOKEN_PAGE_SEMANTIC_READINESS_PASS");
const moduleNamespace = loaderSuccess.state.secureConsoleV57Module;
assert.deepEqual(Object.keys(moduleNamespace).sort(), [...persistentBindings].sort());
assert.equal(moduleNamespace.secureConsoleOwnedTaskTabV57 === null, false);
assert.equal(moduleNamespace.secureConsoleOwnedTaskTabV57Eligible, true);
assert.equal(moduleNamespace.secureConsoleOwnedTaskTabV57State,
  "TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE");
assert.equal(moduleNamespace.secureConsoleOwnedTaskTabV57PreCreateDetachConsumed, false);
assert.equal(moduleNamespace.secureConsoleOwnedTaskTabV57PostNativeDetachConsumed, false);
assert.equal(moduleNamespace.secureConsoleCloudflareReadsV57Consumed, false);
assert.equal(moduleNamespace.secureConsoleV57Consumed, true);

const loaderByteFailure = await runLoader({
  bytes: Buffer.concat([Buffer.from(candidate), Buffer.from(" ")]),
});
const hashMismatchBytes = Buffer.from(candidate);
hashMismatchBytes[0] = hashMismatchBytes[0] === 65 ? 66 : 65;
const loaderHashFailure = await runLoader({ bytes: hashMismatchBytes });
const nonAsciiBytes = Buffer.from(candidate);
nonAsciiBytes[0] = 0x80;
const loaderAsciiFailure = await runLoader({ bytes: nonAsciiBytes, acceptBytes: true });
const loaderReadFailure = await runLoader({ readError: true });
const loaderVmFailure = await runLoader({ vmMissing: true });
const loaderParseFailure = await runLoader({ bytes: Buffer.from("export {"),
  acceptBytes: true });
const loaderStaticFailure = await runLoader({
  bytes: Buffer.from('import "blocked"; export const value = 1;'), acceptBytes: true,
});
const loaderWrongDynamicFailure = await runLoader({
  bytes: Buffer.from('await import("blocked"); export const value = 1;'),
  acceptBytes: true,
});
const loaderDuplicateDynamicFailure = await runLoader({ bytes: Buffer.from(
  `await import("${browserClientUrl}"); await import("${browserClientUrl}"); export const value = 1;`),
  acceptBytes: true });
const topLevelImportBytes = Buffer.from(
  `await import("${browserClientUrl}"); export const value = 1;`);
const loaderImportFailure = await runLoader({ bytes: topLevelImportBytes,
  acceptBytes: true, browserImportError: true });
const loaderBridgeShapeFailure = await runLoader({ bytes: topLevelImportBytes,
  acceptBytes: true, browserModule: { setupBrowserRuntime: null } });
const loaderEvaluationFailure = await runLoader({ bytes: Buffer.from(
  `await import("${browserClientUrl}"); throw new Error("fixture evaluation failure"); export const value = 1;`),
  acceptBytes: true });
const loaderBridgeCountFailure = await runLoader({
  bytes: Buffer.from("export const value = 1;"), acceptBytes: true,
});
const loaderFailureCases = [
  ["size", loaderByteFailure], ["hash", loaderHashFailure],
  ["ascii", loaderAsciiFailure], ["read", loaderReadFailure],
  ["vm-shape", loaderVmFailure], ["parse", loaderParseFailure],
  ["static-import", loaderStaticFailure],
  ["wrong-dynamic-import", loaderWrongDynamicFailure],
  ["duplicate-dynamic-import", loaderDuplicateDynamicFailure],
  ["browser-import", loaderImportFailure],
  ["bridge-shape", loaderBridgeShapeFailure],
  ["evaluation", loaderEvaluationFailure],
  ["bridge-count", loaderBridgeCountFailure],
];
for (const [label, failed] of loaderFailureCases) {
  assert.notEqual(failed.caught, null, label);
  assert.equal(failed.state.secureConsoleV57Module, null);
  assert.ok(failed.reads.length <= 1);
  assert.ok(failed.browserImports.length <= 1);
}
assert.equal(loaderStaticFailure.stats.staticLinkRequests, 1);
assert.equal(loaderStaticFailure.stats.sourceEvaluations, 0);
assert.equal(loaderWrongDynamicFailure.browserImports.length, 0);
assert.equal(loaderDuplicateDynamicFailure.browserImports.length, 1);
assert.equal(loaderDuplicateDynamicFailure.stats.bridgeEvaluations, 1);
assert.equal(loaderImportFailure.browserImports.length, 1);
assert.equal(loaderImportFailure.stats.bridgeEvaluations, 0);
assert.equal(loaderBridgeShapeFailure.browserImports.length, 1);
assert.equal(loaderBridgeShapeFailure.stats.bridgeEvaluations, 0);
assert.equal(loaderEvaluationFailure.stats.sourceEvaluations, 1);
assert.equal(loaderEvaluationFailure.stats.bridgeEvaluations, 1);
assert.equal(loaderBridgeCountFailure.stats.sourceEvaluations, 1);
assert.equal(loaderBridgeCountFailure.stats.bridgeEvaluations, 0);

console.log(JSON.stringify({ result: "PASS", executableBytes: Buffer.byteLength(candidate),
  executableSha256: sha256(candidate), sourceBytes: Buffer.byteLength(source),
  sourceSha256: sha256(source), fixtureBytes: fs.statSync(fileURLToPath(import.meta.url)).size,
  fixtureSha256: sha256(fs.readFileSync(fileURLToPath(import.meta.url))),
  loaderBytes: Buffer.byteLength(loader), loaderSha256: sha256(loader), moduleExports: 7,
  moduleExecutions: loaderSuccess.stats.sourceEvaluations,
  syntheticBridges: loaderSuccess.stats.bridgeEvaluations,
  allowlistedBrowserImports: loaderSuccess.browserImports.length,
  loaderCases: loaderFailureCases.length + 1,
  predecessorContaminations: predecessorNames.length,
  inheritedBehavioralExecutions: behavioralExecutions - freshV56Names.length,
  behavioralExecutions,
  terminalOutputCleanup, completeCounterVector }));
