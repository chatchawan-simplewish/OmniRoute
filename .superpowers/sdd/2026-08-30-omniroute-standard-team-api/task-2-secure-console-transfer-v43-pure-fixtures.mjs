import assert from "node:assert/strict";
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import { fileURLToPath } from "node:url";

const directory = path.dirname(fileURLToPath(import.meta.url));
const executablePath = path.join(
  directory,
  "task-2-secure-console-transfer-v43-fresh-realm-token-page-readiness-executable.js",
);
const executable = fs.readFileSync(executablePath, "utf8").replace(/\r\n/g, "\n");
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;
new AsyncFunction(executable);

const occurrences = (needle) => executable.split(needle).length - 1;
assert.equal(occurrences("await import("), 1);
assert.equal(occurrences(".openTabs()"), 1);
assert.equal(occurrences(".claimTab("), 1);
assert.equal(occurrences('goto("https://dash.cloudflare.com/")'), 1);
assert.equal(
  occurrences('goto("https://dash.cloudflare.com/profile/api-tokens")'),
  1,
);
assert.equal(occurrences('fill("OmniRoute secure console R5 20260901")'), 1);
assert.equal(occurrences("nodeRepl.write("), 2);
for (const forbidden of [
  ".click(", "clipboard", "navigator.clipboard", "Copy Token", "Create API Token",
  "localStorage", "sessionStorage", "document.cookie",
]) {
  assert.equal(executable.includes(forbidden), false, forbidden);
}

const importSource = `const imported = await import(
      "file:///C:/Users/chatc/.codex/plugins/cache/openai-bundled/chrome/26.831.20005/scripts/browser-client.mjs"
    );`;
const observationHook =
  "    globalThis.__v43Fixture.observed = {\n" +
  "      consumed: secureConsoleV43Consumed,\n" +
  "      tabNull: secureConsoleOwnedTaskTabV43 === null,\n" +
  "      eligible: secureConsoleOwnedTaskTabV43Eligible,\n" +
  "      state: secureConsoleOwnedTaskTabV43State,\n" +
  "      attachmentTabNull: secureConsoleOwnedTaskTabV43Attachment === null,\n" +
  "      attachmentEligible: secureConsoleOwnedTaskTabV43AttachmentEligible,\n" +
  "      attachmentState: secureConsoleV43AttachmentState,\n" +
  "      chromeNull: secureConsoleChromeV43Attachment === null,\n" +
  "      agentNull: secureConsoleAgentV43Attachment === null,\n" +
  "      setupNull: secureConsoleSetupBrowserRuntimeV43Attachment === null,\n" +
  "      counters: { ...counters },\n" +
  "    };\n";
const documentationFailureHook =
  "  globalThis.__v43Fixture.documentationFailureObserved = {\n" +
  "    consumed: secureConsoleV43Consumed,\n" +
  "    attachmentTabNull: secureConsoleOwnedTaskTabV43Attachment === null,\n" +
  "    attachmentEligible: secureConsoleOwnedTaskTabV43AttachmentEligible,\n" +
  "    attachmentState: secureConsoleV43AttachmentState,\n" +
  "    chromeNull: secureConsoleChromeV43Attachment === null,\n" +
  "    agentNull: secureConsoleAgentV43Attachment === null,\n" +
  "    setupNull: secureConsoleSetupBrowserRuntimeV43Attachment === null,\n" +
  "  };\n";
const instrumented = executable
  .replace(importSource, "const imported = globalThis.__v43Fixture.imported;")
  .replace(
    "if (secureConsoleV43TerminalOutputFailure !== null) {\n" +
      "  throw secureConsoleV43TerminalOutputFailure;",
    "if (secureConsoleV43TerminalOutputFailure !== null) {\n" +
      documentationFailureHook +
      "  throw secureConsoleV43TerminalOutputFailure;",
  )
  .replace(
    "    });\n  } catch (terminalError) {",
    "    });\n" + observationHook + "  } catch (terminalError) {",
  )
  .replace(
    "    throw terminalError;\n  }\n})();\n",
    observationHook + "    throw terminalError;\n  }\n})();\n",
  );
assert.notEqual(instrumented, executable);
assert.equal(instrumented.includes("await import("), false);

const account = "0".repeat(32);
const accountUrl = `https://dash.cloudflare.com/${account}/home`;
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

const makeFixture = ({
  claimThrown = null,
  failStage = null,
  failTokenNavigation = false,
  failWriteAt = 0,
} = {}) => {
  const fixture = {
    writes: [],
    writeCalls: 0,
    observed: null,
    documentationFailureObserved: null,
    claimThrown,
    failStage,
    failTokenNavigation,
    failWriteAt,
    outputThrown: { fixture: "output" },
    importCalls: 0,
    setupCalls: 0,
    connectCalls: 0,
    documentationCalls: 0,
    nameCalls: 0,
    openTabsCalls: 0,
    claimCalls: 0,
    gotoCalls: 0,
    waitCalls: 0,
    urlCalls: 0,
    accountSnapshotCalls: 0,
    tokenEvaluateCalls: 0,
    filterValue: "",
  };
  const fail = (stage) => {
    if (fixture.failStage === stage) throw { name: `Hidden-${stage}` };
  };

  const queryEcho = {
    async waitFor(options) {
      assert.deepEqual(options, { state: "visible", timeoutMs: 20000 });
    },
    async count() { return 1; },
  };
  const emptyStatus = {
    async waitFor(options) {
      assert.deepEqual(options, { state: "visible", timeoutMs: 20000 });
    },
    async count() { return 1; },
  };
  const paginator = {
    async count() { return 1; },
    async waitFor(options) {
      assert.deepEqual(options, { state: "visible", timeoutMs: 20000 });
    },
  };
  const resultsRoot = {
    async count() { return 1; },
    locator(selector) {
      if (selector === '[aria-label="Pagination"]') return paginator;
      assert.equal(selector, "table tbody");
      return {
        getByText(text, options) {
          assert.equal(text, "OmniRoute secure console R5 20260901");
          assert.deepEqual(options, { exact: true });
          return { async count() { return 0; } };
        },
      };
    },
    async evaluate() {
      fixture.tokenEvaluateCalls++;
      return fixture.tokenEvaluateCalls === 1
        ? { terminalZero: true, completeNonempty: false }
        : true;
    },
    getByText(text, options) {
      assert.equal(text, "OmniRoute secure console R5 20260901");
      assert.deepEqual(options, { exact: true });
      return queryEcho;
    },
    getByRole(role) {
      if (role === "status") {
        return {
          filter(options) {
            assert.ok(options.hasText instanceof RegExp);
            return emptyStatus;
          },
        };
      }
      assert.equal(role, "row");
      return {
        filter(options) {
          assert.deepEqual(options, {
            hasText: "OmniRoute secure console R5 20260901",
          });
          return { async count() { return 0; } };
        },
      };
    },
  };
  const tokenFilter = {
    async count() {
      if (fixture.failStage === "tokenSignature") return 0;
      return 1;
    },
    async getAttribute(name) {
      assert.equal(name, "aria-controls");
      return "token-results";
    },
    async evaluate() {
      return fixture.filterValue === "" ||
        fixture.filterValue === "OmniRoute secure console R5 20260901";
    },
    async fill(value) {
      assert.equal(value, "OmniRoute secure console R5 20260901");
      fail("tokenFill");
      fixture.filterValue = value;
    },
  };

  let currentUrl = accountUrl;
  const tab = {
    id: "task-tab",
    async goto(url) {
      fixture.gotoCalls++;
      if (fixture.gotoCalls === 1) {
        assert.equal(url, "https://dash.cloudflare.com/");
        fail("accountNavigation");
        currentUrl = accountUrl;
        return;
      }
      assert.equal(url, "https://dash.cloudflare.com/profile/api-tokens");
      if (fixture.failTokenNavigation || fixture.failStage === "tokenNavigation") {
        throw { name: "HiddenToken" };
      }
      currentUrl = url;
    },
    async url() {
      fixture.urlCalls++;
      return currentUrl;
    },
    playwright: {
      async waitForTimeout(ms) {
        assert.equal(ms, 20000);
        fail("accountWait");
        fixture.waitCalls++;
      },
      locator(selector) {
        if (selector === "body") {
          return {
            async evaluate(_callback, segment) {
              assert.equal(segment, account);
              fixture.accountSnapshotCalls++;
              if (fixture.failStage === "accountSignature") {
                return {
                  hostExact: true,
                  accountHomePath: true,
                  exactZoneHrefCount: 0,
                  allAnchorCount: 4,
                  busyCount: 0,
                };
              }
              return {
                hostExact: true,
                accountHomePath: true,
                exactZoneHrefCount: 1,
                allAnchorCount: 4,
                busyCount: 0,
              };
            },
          };
        }
        assert.equal(selector, "#token-results");
        return resultsRoot;
      },
      getByRole(role, options) {
        if (role === "textbox") {
          assert.ok(options.name instanceof RegExp);
          return tokenFilter;
        }
        assert.ok(role === "button" || role === "link");
        assert.deepEqual(options, { name: "Create Token", exact: true });
        return { async count() { return role === "button" ? 1 : 0; } };
      },
      getByText() {
        throw new Error("top-level getByText must not be used");
      },
    },
  };

  const browser = {
    async documentation() {
      fixture.documentationCalls++;
      fail("documentation");
      return documentation;
    },
    async nameSession(name) {
      fixture.nameCalls++;
      assert.equal(name, "🔐 OmniRoute secure console");
      fail("sessionName");
    },
    user: {
      async openTabs() {
        fixture.openTabsCalls++;
        fail("enumeration");
        return vm.runInNewContext(`[
          { id: "task-tab", url: "${accountUrl}" },
          { id: "other-tab", url: "https://example.invalid/" }
        ]`);
      },
      async claimTab(id) {
        fixture.claimCalls++;
        assert.equal(id, "task-tab");
        fail("claim");
        if (fixture.claimThrown !== null) throw fixture.claimThrown;
        return tab;
      },
    },
  };
  fixture.imported = {
    async setupBrowserRuntime() {
      fixture.setupCalls++;
      fail("setup");
      return {
        browsers: {
          async get(id) {
            fixture.connectCalls++;
            assert.equal(id, "chrome");
            fail("connect");
            return browser;
          },
        },
      };
    },
  };
  if (fixture.failStage === "import") {
    Object.defineProperty(fixture, "imported", {
      configurable: true,
      get() { throw { name: "Hidden-import" }; },
    });
  }
  return fixture;
};

const run = async (options = {}, prelude = "", source = instrumented) => {
  const fixture = makeFixture(options);
  globalThis.__v43Fixture = fixture;
  const nodeReplPrelude = `
const nodeRepl = {
  async write(value) {
    globalThis.__v43Fixture.writeCalls++;
    if (globalThis.__v43Fixture.failWriteAt === globalThis.__v43Fixture.writeCalls) {
      throw globalThis.__v43Fixture.outputThrown;
    }
    globalThis.__v43Fixture.writes.push(value);
  },
};
`;
  let caught = null;
  try {
    await new AsyncFunction(prelude + nodeReplPrelude + source)();
  } catch (error) {
    caught = error;
  } finally {
    delete globalThis.__v43Fixture;
  }
  return { fixture, caught, output: fixture.writes.at(-1) ?? null };
};

const expectedTopKeys = [
  "attachment", "bindingAttempted", "bindingEligible", "bindingFulfilled",
  "bindingNull", "consumed", "continuationBindingsRetained",
  "controllerOwnership", "createControlCount", "createReadAttempted",
  "createReadFulfilled", "declarationShape", "errorClass",
  "failureCleanupComplete", "fillAttempted", "fillFulfilled",
  "matchingRowCount", "nameReadAttempted", "nameReadFulfilled",
  "navigationAttempted", "navigationFulfilled", "navigationTargetExact",
  "predecessorBindingNull", "predecessorRuntimeCleared",
  "predecessorState", "predecessorStateExact", "readinessAttempted",
  "readinessFulfilled", "result", "rowReadAttempted", "rowReadFulfilled",
  "state", "tabShape", "tokenFilterComplete", "tokenInitialFilterEmpty",
  "tokenNameCount", "tokenQueryEchoCount", "tokenSemanticSignature",
  "urlAttempted", "urlFulfilled", "writeAttempted",
].sort();
const expectedAttachmentKeys = [
  "agentShape", "bindingEligible", "bindingNull", "candidateUrlCloudflare",
  "candidateValidated", "claimAttempted", "claimFulfilled", "connectAttempted",
  "connectFulfilled", "connectedShape", "consumed",
  "continuationBindingsRetained", "controllerOwnership", "declarationShape",
  "documentationAttempted", "documentationFulfilled", "documentationLength",
  "documentationValidated", "documentationWriteAttempted",
  "documentationWriteFulfilled", "errorClass", "failureCleanupComplete",
  "homeUrlValidated", "importAttempted", "importFulfilled",
  "listingValidated", "moduleShape", "nameAttempted", "nameFulfilled",
  "navigationAttempted", "navigationFulfilled", "offeredCount",
  "openTabsAttempted", "openTabsFulfilled", "rankZeroSelected", "result",
  "semanticComplete", "sessionNamed", "setupAttempted", "setupFulfilled",
  "snapshot", "snapshotAttempted", "snapshotFulfilled", "snapshotValidated",
  "state", "tabShape", "urlAttempted", "urlFulfilled", "waitAttempted",
  "waitFulfilled", "writeAttempted",
].sort();

const successRun = await run();
assert.equal(successRun.caught, null);
assert.equal(successRun.fixture.writes.length, 2);
assert.equal(successRun.fixture.writes[0], documentation);
const success = successRun.output;
assert.deepEqual(Object.keys(success).sort(), expectedTopKeys);
assert.deepEqual(Object.keys(success.attachment).sort(), expectedAttachmentKeys);
assert.equal(success.result, "EXACT_V43_TOKEN_PAGE_SEMANTIC_READINESS_PASS");
assert.equal(
  success.attachment.result,
  "EXACT_V43Attachment_CROSS_REALM_TASK_TAB_ACCOUNT_HOME_REACQUISITION_PASS",
);
assert.equal(success.tokenSemanticSignature, true);
assert.equal(success.continuationBindingsRetained, true);
assert.equal(success.predecessorRuntimeCleared, true);
assert.equal(success.bindingEligible, true);
assert.equal(success.bindingNull, false);
assert.equal(success.consumed, true);
assert.equal(success.errorClass, "NONE");
assert.equal(successRun.fixture.importCalls, 0);
assert.equal(successRun.fixture.setupCalls, 1);
assert.equal(successRun.fixture.connectCalls, 1);
assert.equal(successRun.fixture.openTabsCalls, 1);
assert.equal(successRun.fixture.claimCalls, 1);
assert.equal(successRun.fixture.gotoCalls, 2);
assert.equal(successRun.fixture.waitCalls, 1);
assert.equal(successRun.fixture.urlCalls, 2);
assert.equal(successRun.fixture.accountSnapshotCalls, 1);
assert.deepEqual(successRun.fixture.observed, {
  consumed: true,
  tabNull: false,
  eligible: true,
  state: "TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE",
  attachmentTabNull: true,
  attachmentEligible: false,
  attachmentState: "V43Attachment_TRANSFERRED_TO_V43",
  chromeNull: true,
  agentNull: true,
  setupNull: true,
  counters: {
    bindingAttempted: 1, bindingFulfilled: 1,
    navigationAttempted: 1, navigationFulfilled: 1,
    urlAttempted: 1, urlFulfilled: 1,
    readinessAttempted: 3, readinessFulfilled: 3,
    fillAttempted: 1, fillFulfilled: 1,
    createReadAttempted: 1, createReadFulfilled: 1,
    nameReadAttempted: 1, nameReadFulfilled: 1,
    rowReadAttempted: 1, rowReadFulfilled: 1,
    writeAttempted: 1,
  },
});

const contaminated = await run({}, "let secureConsoleV41Consumed = false;\n");
assert.equal(contaminated.caught, null);
assert.equal(contaminated.fixture.setupCalls, 0);
assert.equal(contaminated.fixture.openTabsCalls, 0);
assert.equal(contaminated.output.result, "V43_TOKEN_PAGE_SEMANTIC_READINESS_FAILED_STOP");
assert.equal(contaminated.output.attachment.declarationShape, false);
assert.equal(contaminated.output.attachment.importAttempted, 0);
assert.equal(contaminated.output.bindingEligible, false);
assert.equal(contaminated.output.failureCleanupComplete, true);
assert.deepEqual(Object.keys(contaminated.output).sort(), expectedTopKeys);

const nonfreshSource = instrumented.replace(
  "let secureConsoleV43Consumed = false;",
  "let secureConsoleV43Consumed = true;",
);
const nonfresh = await run({}, "", nonfreshSource);
assert.equal(nonfresh.caught, null);
assert.equal(nonfresh.fixture.setupCalls, 0);
assert.equal(nonfresh.output.attachment.declarationShape, false);
assert.equal(nonfresh.output.attachment.importAttempted, 0);
assert.equal(nonfresh.output.failureCleanupComplete, true);

const attachmentCounterPairs = [
  ["importAttempted", "importFulfilled", "import"],
  ["setupAttempted", "setupFulfilled", "setup"],
  ["connectAttempted", "connectFulfilled", "connect"],
  ["documentationAttempted", "documentationFulfilled", "documentation"],
  ["documentationWriteAttempted", "documentationWriteFulfilled", null],
  ["nameAttempted", "nameFulfilled", "sessionName"],
  ["openTabsAttempted", "openTabsFulfilled", "enumeration"],
  ["claimAttempted", "claimFulfilled", "claim"],
  ["navigationAttempted", "navigationFulfilled", "accountNavigation"],
  ["waitAttempted", "waitFulfilled", "accountWait"],
  ["urlAttempted", "urlFulfilled", null],
  ["snapshotAttempted", "snapshotFulfilled", "accountSignature"],
];
const attachmentCounterKeys = [
  ...attachmentCounterPairs.flatMap(([attempted, fulfilled]) => [attempted, fulfilled]),
  "writeAttempted",
];
const readinessCounterKeys = [
  "bindingAttempted", "bindingFulfilled", "navigationAttempted",
  "navigationFulfilled", "urlAttempted", "urlFulfilled",
  "readinessAttempted", "readinessFulfilled", "fillAttempted",
  "fillFulfilled", "createReadAttempted", "createReadFulfilled",
  "nameReadAttempted", "nameReadFulfilled", "rowReadAttempted",
  "rowReadFulfilled", "writeAttempted",
];
const select = (value, keys) => Object.fromEntries(keys.map((key) => [key, value[key]]));
const expectedAttachmentFailure = (stage) => {
  const expected = Object.fromEntries(attachmentCounterKeys.map((key) => [key, 0]));
  let stopped = false;
  for (const [attempted, fulfilled, failureStage] of attachmentCounterPairs) {
    if (stopped) continue;
    expected[attempted] = 1;
    if (failureStage === stage) {
      if (stage === "accountSignature") expected[fulfilled] = 1;
      stopped = true;
    } else {
      expected[fulfilled] = 1;
    }
  }
  return expected;
};
const zeroReadiness = Object.fromEntries(readinessCounterKeys.map((key) => [key, 0]));
zeroReadiness.writeAttempted = 1;

for (const stage of [
  "import", "setup", "connect", "documentation", "sessionName",
  "enumeration", "claim", "accountNavigation", "accountWait",
  "accountSignature",
]) {
  const failed = await run({ failStage: stage });
  assert.equal(failed.caught, null, stage);
  assert.equal(failed.output.result, "V43_TOKEN_PAGE_SEMANTIC_READINESS_FAILED_STOP", stage);
  assert.equal(failed.output.attachment.errorClass, "Error", stage);
  assert.equal(failed.output.failureCleanupComplete, true, stage);
  assert.equal(failed.output.bindingEligible, false, stage);
  assert.deepEqual(
    select(failed.output.attachment, attachmentCounterKeys),
    expectedAttachmentFailure(stage),
    stage,
  );
  assert.deepEqual(select(failed.output, readinessCounterKeys), zeroReadiness, stage);
  assert.deepEqual(Object.keys(failed.output).sort(), expectedTopKeys, stage);
  assert.deepEqual(Object.keys(failed.output.attachment).sort(), expectedAttachmentKeys, stage);
  assert.equal(JSON.stringify(failed.output).includes(`Hidden-${stage}`), false, stage);
}

const expectedReadinessFailure = (stage) => {
  const expected = Object.fromEntries(readinessCounterKeys.map((key) => [key, 0]));
  expected.bindingAttempted = 1;
  expected.bindingFulfilled = 1;
  expected.navigationAttempted = 1;
  if (stage === "tokenNavigation") {
    expected.writeAttempted = 1;
    return expected;
  }
  expected.navigationFulfilled = 1;
  expected.urlAttempted = 1;
  expected.urlFulfilled = 1;
  if (stage === "tokenSignature") {
    expected.writeAttempted = 1;
    return expected;
  }
  expected.readinessAttempted = 1;
  expected.readinessFulfilled = 1;
  expected.fillAttempted = 1;
  expected.writeAttempted = 1;
  return expected;
};
for (const stage of ["tokenNavigation", "tokenSignature", "tokenFill"]) {
  const failed = await run({ failStage: stage });
  assert.equal(failed.caught, null, stage);
  assert.equal(failed.output.errorClass, "Error", stage);
  assert.equal(failed.output.failureCleanupComplete, true, stage);
  assert.equal(failed.output.bindingEligible, false, stage);
  assert.deepEqual(
    select(failed.output, readinessCounterKeys),
    expectedReadinessFailure(stage),
    stage,
  );
  assert.deepEqual(Object.keys(failed.output).sort(), expectedTopKeys, stage);
  assert.equal(JSON.stringify(failed.output).includes(`Hidden-${stage}`), false, stage);
}

let getterCalls = 0;
const assertHostileClaimFailure = async (thrown, token) => {
  const failureRun = await run({ claimThrown: thrown });
  assert.equal(failureRun.caught, null);
  assert.equal(failureRun.output.result, "V43_TOKEN_PAGE_SEMANTIC_READINESS_FAILED_STOP");
  assert.equal(failureRun.output.attachment.errorClass, "Error");
  assert.equal(failureRun.output.attachment.claimAttempted, 1);
  assert.equal(failureRun.output.attachment.claimFulfilled, 0);
  assert.equal(failureRun.fixture.gotoCalls, 0);
  assert.equal(failureRun.output.bindingEligible, false);
  assert.equal(failureRun.output.failureCleanupComplete, true);
  assert.deepEqual(Object.keys(failureRun.output).sort(), expectedTopKeys);
  assert.equal(JSON.stringify(failureRun.output).includes(token), false);
};
await assertHostileClaimFailure({ name: "ASecretLikeToken" }, "ASecretLikeToken");
const getterThrown = {};
Object.defineProperty(getterThrown, "name", {
  get() {
    getterCalls++;
    throw new Error("must not read");
  },
});
await assertHostileClaimFailure(getterThrown, "must not read");
assert.equal(getterCalls, 0);

const navigationFailure = await run({ failTokenNavigation: true });
assert.equal(navigationFailure.caught, null);
assert.equal(navigationFailure.output.errorClass, "Error");
assert.equal(navigationFailure.output.navigationAttempted, 1);
assert.equal(navigationFailure.output.navigationFulfilled, 0);
assert.equal(navigationFailure.output.failureCleanupComplete, true);
assert.equal(navigationFailure.fixture.gotoCalls, 2);

const finalOutputFailure = await run({ failWriteAt: 2 });
assert.equal(finalOutputFailure.caught, finalOutputFailure.fixture.outputThrown);
assert.equal(finalOutputFailure.fixture.writeCalls, 2);
assert.equal(finalOutputFailure.fixture.writes.length, 1);
assert.equal(finalOutputFailure.fixture.observed.tabNull, true);
assert.equal(finalOutputFailure.fixture.observed.eligible, false);
assert.equal(finalOutputFailure.fixture.observed.chromeNull, true);
assert.equal(finalOutputFailure.fixture.observed.agentNull, true);
assert.equal(finalOutputFailure.fixture.observed.setupNull, true);

const documentationOutputFailure = await run({ failWriteAt: 1 });
assert.equal(
  documentationOutputFailure.caught,
  documentationOutputFailure.fixture.outputThrown,
);
assert.equal(documentationOutputFailure.fixture.writeCalls, 1);
assert.equal(documentationOutputFailure.fixture.writes.length, 0);
assert.deepEqual(documentationOutputFailure.fixture.documentationFailureObserved, {
  consumed: true,
  attachmentTabNull: true,
  attachmentEligible: false,
  attachmentState: "V43Attachment_REACQUISITION_OR_READINESS_FAILED",
  chromeNull: true,
  agentNull: true,
  setupNull: true,
});

console.log(JSON.stringify({
  result: "V43_PURE_FIXTURES_PASS",
  executableBytes: Buffer.byteLength(executable),
  executableSha256: crypto.createHash("sha256").update(executable).digest("hex").toUpperCase(),
  syntax: "PASS",
  declarationFree: true,
  exactOutputKeys: true,
  fullCellSuccess: true,
  fixedFailureCleanup: true,
  hostileThrownValues: true,
  terminalOutputCleanup: true,
  completeCounterVectors: true,
  getterCalls,
}));
