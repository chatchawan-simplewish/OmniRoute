import assert from "node:assert/strict";
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import { fileURLToPath, pathToFileURL } from "node:url";

const directory = path.dirname(fileURLToPath(import.meta.url));
const briefPath = path.join(
  directory,
  "task-2-secure-console-transfer-v41-fresh-session-rank-zero-only-selected-tab-reacquisition-brief.md",
);
const brief = fs.readFileSync(briefPath, "utf8");
const runtimeModulePath =
  "C:/Users/chatc/.codex/plugins/cache/openai-bundled/chrome/26.831.20005/scripts/browser-client.mjs";
const runtimeModule = await import(pathToFileURL(runtimeModulePath).href);
assert.equal(typeof runtimeModule, "object");
assert.notEqual(runtimeModule, null);
assert.equal(typeof runtimeModule.setupBrowserRuntime, "function");
assert.equal("BROWSER_CLIENT_ID" in runtimeModule, false);

const cells = [...brief.matchAll(/~~~javascript\r?\n([\s\S]*?)\r?\n~~~/g)];
assert.equal(cells.length, 1);
const cell = cells[0][1].replace(/\r\n/g, "\n");
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;
new AsyncFunction(cell);

const occurrences = (needle) => cell.split(needle).length - 1;
assert.equal(occurrences("await import("), 1);
assert.equal(occurrences("secureConsoleSetupBrowserRuntimeV41();"), 1);
assert.equal(occurrences('browsers.get("chrome")'), 1);
assert.equal(occurrences("secureConsoleChromeV41.documentation()"), 1);
assert.equal(occurrences("secureConsoleChromeV41.nameSession("), 1);
assert.equal(occurrences("secureConsoleChromeV41.user.openTabs()"), 1);
assert.equal(occurrences("secureConsoleChromeV41.user.claimTab(candidate.id)"), 1);
assert.equal(occurrences('adopted.goto("https://dash.cloudflare.com/")'), 1);
assert.equal(occurrences("adopted.playwright.waitForTimeout(20000)"), 1);
assert.equal(occurrences("adopted.url()"), 1);
assert.equal(occurrences('adopted.playwright.locator("body").evaluate('), 1);
assert.equal(cell.includes("Object.getPrototypeOf(value) !== Array.prototype"), false);
assert.equal(cell.includes("catch (error)"), false);
assert.match(cell, /  } catch \{\n    errorClass = "Error";\n  }/);
for (const forbidden of [
  "reconnect", ".selected", ".list(", ".closeTab", ".newTab",
  ".clipboard", "provider.", "credential", "Invoke-WebRequest",
]) {
  assert.equal(cell.includes(forbidden), false, forbidden);
}

const blockMatch = cell.match(
  /\/\/ BEGIN_V41_PURE_TRUSTED_LISTING\n([\s\S]*?)\n  \/\/ END_V41_PURE_TRUSTED_LISTING/,
);
assert.notEqual(blockMatch, null);
const trustedListing = new Function(
  `${blockMatch[1]}\nreturn trustedListing;`,
)();

const account = "0".repeat(32);
const targetUrl = `https://dash.cloudflare.com/${account}/account`;
const validLocal = trustedListing([
  { id: "task-tab", url: targetUrl },
  { id: "other-tab", url: "https://example.invalid/" },
]);
assert.deepEqual(validLocal, {
  id: "task-tab",
  count: 2,
  urlCloudflare: true,
});

const foreign = vm.runInNewContext(`[
  { id: "task-tab", url: "${targetUrl}" },
  { id: "other-tab", url: "https://example.invalid/" }
]`);
assert.equal(Array.isArray(foreign), true);
assert.notEqual(Object.getPrototypeOf(foreign), Array.prototype);
assert.deepEqual(trustedListing(foreign), validLocal);

assert.equal(trustedListing([
  { id: "other", url: "https://example.invalid/" },
  { id: "task-tab", url: targetUrl },
]), null);
assert.deepEqual(trustedListing([
  { id: "task-1", url: targetUrl },
  { id: "task-2", url: `${targetUrl}/later` },
]), {
  id: "task-1",
  count: 2,
  urlCloudflare: true,
});
assert.equal(trustedListing([{ id: "task-tab" }]), null);

const symbolArray = [{ id: "task-tab", url: targetUrl }];
symbolArray[Symbol("unexpected")] = true;
assert.equal(trustedListing(symbolArray), null);
const unexpectedName = [{ id: "task-tab", url: targetUrl }];
unexpectedName.extra = true;
assert.equal(trustedListing(unexpectedName), null);
assert.equal(trustedListing(new Array(1)), null);

let getterCalls = 0;
const indexAccessor = [];
Object.defineProperty(indexAccessor, "0", {
  enumerable: true,
  configurable: true,
  get() {
    getterCalls++;
    return { id: "task-tab", url: targetUrl };
  },
});
indexAccessor.length = 1;
assert.equal(trustedListing(indexAccessor), null);
assert.equal(getterCalls, 0);

const recordAccessor = {};
Object.defineProperty(recordAccessor, "id", {
  enumerable: true,
  configurable: true,
  get() {
    getterCalls++;
    return "task-tab";
  },
});
recordAccessor.url = targetUrl;
assert.equal(trustedListing([recordAccessor]), null);
assert.equal(getterCalls, 0);

const laterHostileRecord = {};
Object.defineProperty(laterHostileRecord, "id", {
  enumerable: true,
  configurable: true,
  get() {
    getterCalls++;
    throw new Error("later record must not be inspected");
  },
});
assert.deepEqual(trustedListing([
  { id: "task-tab", url: targetUrl },
  laterHostileRecord,
]), validLocal);
assert.equal(getterCalls, 0);

assert.equal(trustedListing([{ id: "task-tab", url: targetUrl, title: undefined }]), null);
assert.equal(trustedListing([{ id: "task-tab", url: targetUrl, extra: "x" }]), null);
assert.equal(trustedListing([{ id: "task\n tab", url: targetUrl }]), null);

const nullRecord = Object.assign(Object.create(null), {
  id: "task-tab",
  url: targetUrl,
});
assert.equal(trustedListing([nullRecord]).urlCloudflare, true);

const documentationSeed = [
  "openTabs(): Promise<Array<BrowserUserTabInfo>>",
  "claimTab(tab: string | BrowserUserTabInfo): Promise<Tab>",
  "id: string",
  "lastOpened?: string",
  "providerTabId?: string",
  "tabGroup?: string",
  "title?: string",
  "url?: string",
].join("\n");
const documentation = documentationSeed.padEnd(42596, "x");
const terminalWrites = [];
let throwFromClaim = null;
let claimCalls = 0;
let gotoCalls = 0;
let waitCalls = 0;
let urlCalls = 0;
let snapshotCalls = 0;

const fixtureTab = {
  id: "task-tab",
  async goto(url) {
    assert.equal(url, "https://dash.cloudflare.com/");
    gotoCalls++;
  },
  async url() {
    urlCalls++;
    return `https://dash.cloudflare.com/${account}/home`;
  },
  playwright: {
    async waitForTimeout(ms) {
      assert.equal(ms, 20000);
      waitCalls++;
    },
    locator(selector) {
      assert.equal(selector, "body");
      return {
        async evaluate(_callback, segment) {
          assert.equal(segment, account);
          snapshotCalls++;
          return {
            hostExact: true,
            accountHomePath: true,
            exactZoneHrefCount: 1,
            allAnchorCount: 4,
            busyCount: 0,
          };
        },
      };
    },
  },
};

const fixtureBrowser = {
  async documentation() {
    return documentation;
  },
  async nameSession(name) {
    assert.equal(name, "🔐 OmniRoute secure console");
  },
  user: {
    async openTabs() {
      return vm.runInNewContext(`[
        { id: "task-tab", url: "${targetUrl}" },
        { id: "other-tab", url: "https://example.invalid/" }
      ]`);
    },
    async claimTab(id) {
      claimCalls++;
      assert.equal(id, "task-tab");
      if (throwFromClaim !== null) throw throwFromClaim;
      return fixtureTab;
    },
  },
};
const fixtureImported = {
  async setupBrowserRuntime() {
    return {
      browsers: {
        async get(id) {
          assert.equal(id, "chrome");
          return fixtureBrowser;
        },
      },
    };
  },
};

const importSource = `const imported = await import(
      "file:///C:/Users/chatc/.codex/plugins/cache/openai-bundled/chrome/26.831.20005/scripts/browser-client.mjs"
    );`;
const transformedCell = cell.replace(
  importSource,
  "const imported = globalThis.__v41FixtureImported;",
);
assert.notEqual(transformedCell, cell);
assert.equal(transformedCell.includes("await import("), false);

const runTransformedCell = async () => {
  terminalWrites.length = 0;
  claimCalls = 0;
  gotoCalls = 0;
  waitCalls = 0;
  urlCalls = 0;
  snapshotCalls = 0;
  globalThis.__v41FixtureImported = fixtureImported;
  globalThis.nodeRepl = {
    async write(value) {
      terminalWrites.push(value);
    },
  };
  try {
    await new AsyncFunction(transformedCell)();
  } finally {
    delete globalThis.__v41FixtureImported;
    delete globalThis.nodeRepl;
  }
};

await runTransformedCell();
assert.equal(terminalWrites.length, 2);
assert.equal(terminalWrites[0], documentation);
const success = terminalWrites[1];
assert.equal(success.result,
  "EXACT_V41_CROSS_REALM_TASK_TAB_ACCOUNT_HOME_REACQUISITION_PASS");
assert.equal(success.offeredCount, 2);
assert.equal(success.rankZeroSelected, true);
assert.equal(success.listingValidated, true);
assert.equal(success.candidateValidated, true);
assert.equal(success.candidateUrlCloudflare, true);
assert.equal(success.semanticComplete, true);
assert.equal(success.continuationBindingsRetained, true);
assert.equal(success.failureCleanupComplete, false);
assert.equal(success.errorClass, "NONE");
assert.equal(success.consumed, true);
assert.equal(success.bindingEligible, true);
assert.equal(success.bindingNull, false);
assert.equal(success.state, "V41_ACCOUNT_HOME_READY_ELIGIBLE");
assert.equal(claimCalls, 1);
assert.equal(gotoCalls, 1);
assert.equal(waitCalls, 1);
assert.equal(urlCalls, 1);
assert.equal(snapshotCalls, 1);

const assertFixedFailure = async (thrown) => {
  throwFromClaim = thrown;
  await runTransformedCell();
  assert.equal(terminalWrites.length, 2);
  const failure = terminalWrites[1];
  assert.equal(failure.result,
    "V41_FRESH_CROSS_REALM_TASK_REACQUISITION_FAILED_STOP");
  assert.equal(failure.errorClass, "Error");
  assert.equal(failure.consumed, true);
  assert.equal(failure.bindingEligible, false);
  assert.equal(failure.bindingNull, true);
  assert.equal(failure.continuationBindingsRetained, false);
  assert.equal(failure.failureCleanupComplete, true);
  assert.equal(failure.state, "V41_REACQUISITION_OR_READINESS_FAILED");
  assert.equal(claimCalls, 1);
  assert.equal(gotoCalls, 0);
  assert.equal(waitCalls, 0);
  assert.equal(urlCalls, 0);
  assert.equal(snapshotCalls, 0);
};

await assertFixedFailure({ name: "ASecretLikeToken" });
const getterThrown = {};
Object.defineProperty(getterThrown, "name", {
  get() {
    getterCalls++;
    throw new Error("must not read");
  },
});
await assertFixedFailure(getterThrown);
assert.equal(getterCalls, 0);
throwFromClaim = null;

const report = {
  result: "V41_PURE_FIXTURES_PASS",
  briefBytes: Buffer.byteLength(brief),
  briefSha256: crypto.createHash("sha256").update(brief).digest("hex").toUpperCase(),
  executableBytes: Buffer.byteLength(cell),
  executableSha256: crypto.createHash("sha256").update(cell).digest("hex").toUpperCase(),
  syntax: "PASS",
  moduleShape: true,
  foreignRealmAccepted: true,
  rankZeroOnly: true,
  laterRecordUninspected: true,
  fullCellSuccess: true,
  fixedFailure: true,
  getterCalls,
};
console.log(JSON.stringify(report));
