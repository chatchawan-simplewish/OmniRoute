import assert from "node:assert/strict";
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import { fileURLToPath } from "node:url";

const fixturePath = fileURLToPath(import.meta.url);
const directory = path.dirname(fixturePath);
const fixture = fs.readFileSync(fixturePath);
const briefPath = path.join(
  directory,
  "task-2-secure-console-transfer-v49-fresh-realm-token-page-readiness-brief.md",
);
const brief = fs.readFileSync(briefPath, "utf8");
const executablePath = path.join(
  directory,
  "task-2-secure-console-transfer-v49-fresh-realm-token-page-readiness-executable.js",
);
const executable = fs.readFileSync(executablePath, "utf8").replace(/\r\n/g, "\n");
const executableBytes = Buffer.byteLength(executable);
const executableSha256 = crypto.createHash("sha256").update(executable).digest("hex").toUpperCase();
assert.ok(brief.includes("55C8833CF0E405022B747298CE71E7ED6DCF4A301A6C429026A598004444050E"));
assert.ok(brief.includes(`- Executable length: \`${executableBytes}\` bytes.`));
assert.ok(brief.includes(`  \`${executableSha256}\``));
const fixtureBytes = fixture.length;
const fixtureSha256 = crypto.createHash("sha256").update(fixture).digest("hex").toUpperCase();
assert.ok(brief.includes(`- Pure fixture length: \`${fixtureBytes}\` bytes.`));
assert.ok(brief.includes(`  \`${fixtureSha256}\``));
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;
new AsyncFunction(executable);

const occurrences = (needle) => executable.split(needle).length - 1;
assert.equal(occurrences("await import("), 1);
assert.equal(occurrences(".openTabs()"), 1);
assert.equal(occurrences(".claimTab("), 1);
assert.equal(
  occurrences("secureConsoleChromeV49Attachment.user.claimTab(candidate.tab)"),
  1,
);
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

const listingBlock = executable.match(
  /\/\/ BEGIN_V49Attachment_PURE_TRUSTED_LISTING\n([\s\S]*?)\n\s*\/\/ END_V49Attachment_PURE_TRUSTED_LISTING/,
);
assert.notEqual(listingBlock, null);
const trustedListing = new Function(
  `${listingBlock[1]}\nreturn trustedListing;`,
)();
const listingAccount = "1".repeat(32);
const listingTargetUrl =
  `https://dash.cloudflare.com/${listingAccount}/account`;
const listingSummary = (value) => value === null ? null : {
  id: value.id,
  count: value.count,
  urlPresent: value.urlPresent,
  urlCloudflare: value.urlCloudflare,
};
const validFirst = { id: "task-tab", url: listingTargetUrl };
const validListing = {
  id: "task-tab",
  count: 2,
  urlPresent: true,
  urlCloudflare: true,
};
const validListingResult = trustedListing([
  validFirst,
  { id: "other-tab", url: "https://example.invalid/" },
]);
assert.deepEqual(listingSummary(validListingResult), validListing);
assert.equal(validListingResult.tab, validFirst);
const foreignListing = vm.runInNewContext(`[
  { id: "task-tab", url: "${listingTargetUrl}" },
  { id: "other-tab", url: "https://example.invalid/" }
]`);
assert.notEqual(Object.getPrototypeOf(foreignListing), Array.prototype);
const foreignListingResult = trustedListing(foreignListing);
assert.deepEqual(listingSummary(foreignListingResult), validListing);
assert.equal(foreignListingResult.tab, foreignListing[0]);
assert.equal(trustedListing([]), null);
assert.equal(trustedListing(new Array(1)), null);
assert.equal(trustedListing([
  { id: "other", url: "https://example.invalid/" },
  { id: "task-tab", url: listingTargetUrl },
]), null);
const absentUrlRecord = { id: "task-tab" };
const absentUrlResult = trustedListing([absentUrlRecord]);
assert.deepEqual(listingSummary(absentUrlResult), {
  id: "task-tab",
  count: 1,
  urlPresent: false,
  urlCloudflare: false,
});
assert.equal(absentUrlResult.tab, absentUrlRecord);
assert.equal(Object.hasOwn(absentUrlRecord, "title"), false);
assert.equal(trustedListing([{
  id: "task-tab",
  url: "https://dash.cloudflare.com.evil.invalid/",
}]), null);
assert.equal(trustedListing([{
  id: "task-tab",
  url: listingTargetUrl,
  extra: "unexpected",
}]), null);
const symbolListing = [{ id: "task-tab", url: listingTargetUrl }];
symbolListing[Symbol("unexpected")] = true;
assert.equal(trustedListing(symbolListing), null);
const namedListing = [{ id: "task-tab", url: listingTargetUrl }];
namedListing.extra = true;
assert.equal(trustedListing(namedListing), null);
let listingGetterCalls = 0;
const indexAccessor = [];
Object.defineProperty(indexAccessor, "0", {
  enumerable: true,
  configurable: true,
  get() {
    listingGetterCalls++;
    return { id: "task-tab", url: listingTargetUrl };
  },
});
indexAccessor.length = 1;
assert.equal(trustedListing(indexAccessor), null);
const recordAccessor = { url: listingTargetUrl };
Object.defineProperty(recordAccessor, "id", {
  enumerable: true,
  configurable: true,
  get() {
    listingGetterCalls++;
    return "task-tab";
  },
});
assert.equal(trustedListing([recordAccessor]), null);
const laterHostileRecord = {};
Object.defineProperty(laterHostileRecord, "id", {
  enumerable: true,
  configurable: true,
  get() {
    listingGetterCalls++;
    throw new Error("later record must not be inspected");
  },
});
const hostileTailFirst = { id: "task-tab", url: listingTargetUrl };
const hostileTailResult = trustedListing([
  hostileTailFirst,
  laterHostileRecord,
]);
assert.deepEqual(listingSummary(hostileTailResult), validListing);
assert.equal(hostileTailResult.tab, hostileTailFirst);
assert.equal(listingGetterCalls, 0);
const nullRecord = Object.assign(Object.create(null), {
  id: "task-tab",
  url: listingTargetUrl,
});
const nullRecordResult = trustedListing([nullRecord]);
assert.equal(nullRecordResult.urlCloudflare, true);
assert.equal(nullRecordResult.urlPresent, true);
assert.equal(nullRecordResult.tab, nullRecord);

const makeListing = (first) => [first];
const validRecord = (overrides = {}) => ({
  id: "task-tab",
  url: listingTargetUrl,
  ...overrides,
});
const rankZeroSymbolRecord = validRecord();
rankZeroSymbolRecord[Symbol("unexpected")] = true;
class ListingRecord {
  constructor() {
    this.id = "task-tab";
    this.url = listingTargetUrl;
  }
}
const nonEnumerableFieldRecord = validRecord();
Object.defineProperty(nonEnumerableFieldRecord, "id", {
  value: "task-tab",
  enumerable: false,
  configurable: true,
});
const nonEnumerableSlot = [];
Object.defineProperty(nonEnumerableSlot, "0", {
  value: validRecord(),
  enumerable: false,
  configurable: true,
});
nonEnumerableSlot.length = 1;
const oversizedListing = [];
oversizedListing.length = 1001;
const fieldBoundaryListings = [
  ["id-empty", makeListing(validRecord({ id: "" }))],
  ["id-over-limit", makeListing(validRecord({ id: "i".repeat(513) }))],
  ["id-control", makeListing(validRecord({ id: "task\u0000tab" }))],
  ["id-non-string", makeListing(validRecord({ id: 7 }))],
  ["url-empty", makeListing(validRecord({ url: "" }))],
  ["url-over-limit", makeListing(validRecord({ url: "u".repeat(16385) }))],
  ["url-control", makeListing(validRecord({ url: `${listingTargetUrl}\u007f` }))],
  ["url-non-string", makeListing(validRecord({ url: 7 }))],
  ["optional-empty", makeListing(validRecord({ title: "" }))],
  ["optional-over-limit", makeListing(validRecord({ title: "t".repeat(4097) }))],
  ["optional-control", makeListing(validRecord({ title: "bad\u001ftitle" }))],
  ["optional-non-string", makeListing(validRecord({ title: 7 }))],
  ["optional-undefined-present", makeListing(validRecord({ title: undefined }))],
];
const rejectedListings = [
  ["non-array", {}],
  ["over-bounded-maximum", oversizedListing],
  ["rank-zero-symbol", makeListing(rankZeroSymbolRecord)],
  ["rank-zero-class", makeListing(new ListingRecord())],
  ["rank-zero-primitive", ["task-tab"]],
  ["non-enumerable-field", makeListing(nonEnumerableFieldRecord)],
  ["non-enumerable-slot", nonEnumerableSlot],
  ...fieldBoundaryListings,
  ["invalid-url-parse", makeListing(validRecord({ url: "not a URL" }))],
  ["http-scheme", makeListing(validRecord({ url: "http://dash.cloudflare.com/x" }))],
  ["explicit-port", makeListing(validRecord({ url: "https://dash.cloudflare.com:8443/x" }))],
  ["username", makeListing(validRecord({ url: "https://user@dash.cloudflare.com/x" }))],
  ["password", makeListing(validRecord({ url: "https://user:pass@dash.cloudflare.com/x" }))],
];
for (const [name, listing] of rejectedListings) {
  assert.equal(trustedListing(listing), null, name);
}

const importSource = `const imported = await import(
        "file:///C:/Users/chatc/.codex/plugins/cache/openai-bundled/chrome/26.831.21537/scripts/browser-client.mjs"
      );`;
const observationHook =
  "    globalThis.__v49Fixture.observed = {\n" +
  "      consumed: secureConsoleV49Consumed,\n" +
  "      tabNull: secureConsoleOwnedTaskTabV49 === null,\n" +
  "      eligible: secureConsoleOwnedTaskTabV49Eligible,\n" +
  "      state: secureConsoleOwnedTaskTabV49State,\n" +
  "      attachmentTabNull: secureConsoleOwnedTaskTabV49Attachment === null,\n" +
  "      attachmentEligible: secureConsoleOwnedTaskTabV49AttachmentEligible,\n" +
  "      attachmentState: secureConsoleV49AttachmentState,\n" +
  "      chromeNull: secureConsoleChromeV49Attachment === null,\n" +
  "      agentNull: secureConsoleAgentV49Attachment === null,\n" +
  "      setupNull: secureConsoleSetupBrowserRuntimeV49Attachment === null,\n" +
  "      evidenceNull: secureConsoleV49AttachmentEvidence === null,\n" +
  "      outputErrorNull: secureConsoleV49TerminalOutputFailure === null,\n" +
  "      counters: { ...counters },\n" +
  "    };\n";
const documentationFailureHook =
  "  globalThis.__v49Fixture.documentationFailureObserved = {\n" +
  "    consumed: secureConsoleV49Consumed,\n" +
  "    tabNull: secureConsoleOwnedTaskTabV49 === null,\n" +
  "    eligible: secureConsoleOwnedTaskTabV49Eligible,\n" +
  "    state: secureConsoleOwnedTaskTabV49State,\n" +
  "    attachmentTabNull: secureConsoleOwnedTaskTabV49Attachment === null,\n" +
  "    attachmentEligible: secureConsoleOwnedTaskTabV49AttachmentEligible,\n" +
  "    attachmentState: secureConsoleV49AttachmentState,\n" +
  "    chromeNull: secureConsoleChromeV49Attachment === null,\n" +
  "    agentNull: secureConsoleAgentV49Attachment === null,\n" +
  "    setupNull: secureConsoleSetupBrowserRuntimeV49Attachment === null,\n" +
  "    evidenceNull: secureConsoleV49AttachmentEvidence === null,\n" +
  "    outputErrorNull: secureConsoleV49TerminalOutputFailure === null,\n" +
  "  };\n";
const instrumented = executable
  .replace(importSource, "const imported = globalThis.__v49Fixture.imported;")
  .replace(
    "if (secureConsoleV49TerminalOutputFailure !== null) {\n" +
      "    const terminalOutputFailure = secureConsoleV49TerminalOutputFailure;\n" +
      "    secureConsoleV49TerminalOutputFailure = null;\n" +
      "    secureConsoleV49AttachmentEvidence = null;\n" +
      "    throw terminalOutputFailure;",
    "if (secureConsoleV49TerminalOutputFailure !== null) {\n" +
      "    const terminalOutputFailure = secureConsoleV49TerminalOutputFailure;\n" +
      "    globalThis.__v49Fixture.documentationFailureAttachment =\n" +
      "      { ...secureConsoleV49AttachmentEvidence };\n" +
      "    secureConsoleV49TerminalOutputFailure = null;\n" +
      "    secureConsoleV49AttachmentEvidence = null;\n" +
      documentationFailureHook +
      "    throw terminalOutputFailure;",
  )
  .replace(
    "      await nodeRepl.write({",
    "      globalThis.__v49Fixture.finalWriteAttachment =\n" +
      "        { ...secureConsoleV49AttachmentEvidence };\n" +
      "      await nodeRepl.write({",
  )
  .replace(
    "      secureConsoleV49AttachmentEvidence = null;\n" +
      "      secureConsoleV49TerminalOutputFailure = null;\n" +
      "    } catch (terminalError) {",
    "      secureConsoleV49AttachmentEvidence = null;\n" +
      "      secureConsoleV49TerminalOutputFailure = null;\n" +
      observationHook +
      "    } catch (terminalError) {",
  )
  .replace(
    "      secureConsoleV49AttachmentEvidence = null;\n" +
      "      secureConsoleV49TerminalOutputFailure = null;\n" +
      "      throw terminalError;",
    "      secureConsoleV49AttachmentEvidence = null;\n" +
      "      secureConsoleV49TerminalOutputFailure = null;\n" +
      observationHook +
      "      throw terminalError;",
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
let outputGetterCalls = 0;

const makeFixture = ({
  claimThrown = null,
  failStage = null,
  failTokenNavigation = false,
  failWriteAt = 0,
  listingValue = null,
} = {}) => {
  const fixture = {
    writes: [],
    writeCalls: 0,
    observed: null,
    documentationFailureObserved: null,
    documentationFailureAttachment: null,
    finalWriteAttachment: null,
    claimThrown,
    failStage,
    failTokenNavigation,
    failWriteAt,
    listingValue,
    offeredFirst: null,
    outputThrown: null,
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
    filterEvaluateCalls: 0,
    filterValue: "",
  };
  fixture.outputThrown = {};
  Object.defineProperty(fixture.outputThrown, "name", {
    get() {
      outputGetterCalls++;
      throw new Error("output name must not be read");
    },
  });
  const fail = (stage) => {
    if (fixture.failStage === stage) throw { name: `Hidden-${stage}` };
  };

  const queryEcho = {
    async waitFor(options) {
      assert.deepEqual(options, { state: "visible", timeoutMs: 20000 });
      fail("queryEchoWait");
    },
    async count() {
      if (fixture.failStage === "queryEchoCount") return 0;
      return 1;
    },
  };
  const emptyStatus = {
    async waitFor(options) {
      assert.deepEqual(options, { state: "visible", timeoutMs: 20000 });
      fail("emptyStatusWait");
    },
    async count() {
      if (fixture.failStage === "emptyStatusCount") return 0;
      return 1;
    },
  };
  const paginator = {
    async count() {
      if (fixture.failStage === "paginatorShape") return 0;
      return 1;
    },
    async waitFor(options) {
      assert.deepEqual(options, { state: "visible", timeoutMs: 20000 });
      fail("readinessWait");
    },
  };
  const resultsRoot = {
    async count() {
      if (fixture.failStage === "controlledRoot") return 0;
      return 1;
    },
    locator(selector) {
      if (selector === '[aria-label="Pagination"]') return paginator;
      assert.equal(selector, "table tbody");
      return {
        getByText(text, options) {
          assert.equal(text, "OmniRoute secure console R5 20260901");
          assert.deepEqual(options, { exact: true });
          return {
            async count() {
              if (fixture.failStage === "nameReadThrow") fail("nameReadThrow");
              if (fixture.failStage === "nameReadInvalid") return 1;
              return 0;
            },
          };
        },
      };
    },
    async evaluate() {
      fixture.tokenEvaluateCalls++;
      if (fixture.failStage === "baselineInvalid" &&
          fixture.tokenEvaluateCalls === 1) {
        return { terminalZero: false, completeNonempty: false };
      }
      if (fixture.failStage === "terminalInvalid" &&
          fixture.tokenEvaluateCalls === 2) return false;
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
          return {
            async count() {
              if (fixture.failStage === "rowReadThrow") fail("rowReadThrow");
              if (fixture.failStage === "rowReadInvalid") return 1;
              return 0;
            },
          };
        },
      };
    },
  };
  const tokenFilter = {
    async waitFor(options) {
      assert.deepEqual(options, { state: "visible", timeoutMs: 20000 });
      fail("tokenFilterWait");
    },
    async count() {
      if (fixture.failStage === "tokenSignature") return 0;
      return 1;
    },
    async getAttribute(name) {
      assert.equal(name, "aria-controls");
      if (fixture.failStage === "regionBinding") return "bad region id!";
      return "token-results";
    },
    async evaluate() {
      fixture.filterEvaluateCalls++;
      if (fixture.failStage === "initialFilterInvalid" &&
          fixture.filterEvaluateCalls === 1) return false;
      if (fixture.failStage === "tokenValueInvalid" &&
          fixture.filterEvaluateCalls === 2) return false;
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
      if (fixture.failStage === "accountUrlThrow" && fixture.gotoCalls === 1) {
        fail("accountUrlThrow");
      }
      if (fixture.failStage === "tokenUrlThrow" && fixture.gotoCalls === 2) {
        fail("tokenUrlThrow");
      }
      if (fixture.failStage === "accountUrl" && fixture.gotoCalls === 1) {
        return "https://dash.cloudflare.com/not-an-account/home";
      }
      if (fixture.failStage === "tokenUrl" && fixture.gotoCalls === 2) {
        return "https://dash.cloudflare.com/profile/not-api-tokens";
      }
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
        return {
          async count() {
            if (fixture.failStage === "createReadThrow" && role === "button") {
              fail("createReadThrow");
            }
            if (fixture.failStage === "createReadInvalid") return 0;
            return role === "button" ? 1 : 0;
          },
        };
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
      if (fixture.failStage === "documentationInvalid") return "incomplete";
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
        if (fixture.failStage === "listingShape") return new Array(1);
        const offered = fixture.listingValue !== null
          ? fixture.listingValue
          : vm.runInNewContext(`[
              { id: "task-tab", url: "${accountUrl}" },
              { id: "other-tab", url: "https://example.invalid/" }
            ]`);
        fixture.offeredFirst = offered[0];
        return offered;
      },
      async claimTab(tabInfo) {
        fixture.claimCalls++;
        assert.equal(tabInfo, fixture.offeredFirst);
        assert.equal(tabInfo.id, "task-tab");
        fail("claim");
        if (fixture.claimThrown !== null) throw fixture.claimThrown;
        if (fixture.failStage === "controllerShape") return { ...tab, id: "wrong" };
        if (fixture.failStage === "tabShape") return { id: "task-tab" };
        return tab;
      },
    },
  };
  fixture.imported = {
    async setupBrowserRuntime() {
      fixture.setupCalls++;
      fail("setup");
      if (fixture.failStage === "agentShape") return {};
      return {
        browsers: {
          async get(id) {
            fixture.connectCalls++;
            assert.equal(id, "chrome");
            fail("connect");
            if (fixture.failStage === "chromeShape") return {};
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
  } else if (fixture.failStage === "moduleShape") {
    fixture.imported = {};
  }
  return fixture;
};

const run = async (options = {}, prelude = "", source = instrumented) => {
  const fixture = makeFixture(options);
  globalThis.__v49Fixture = fixture;
  const nodeReplPrelude = `
const nodeRepl = {
  async write(value) {
    globalThis.__v49Fixture.writeCalls++;
    if (globalThis.__v49Fixture.failWriteAt === globalThis.__v49Fixture.writeCalls) {
      throw globalThis.__v49Fixture.outputThrown;
    }
    globalThis.__v49Fixture.writes.push(value);
  },
};
`;
  let caught = null;
  try {
    await new AsyncFunction(prelude + nodeReplPrelude + source)();
  } catch (error) {
    caught = error;
  } finally {
    delete globalThis.__v49Fixture;
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
  "candidateUrlPresent",
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
assert.equal(success.result, "EXACT_V49_TOKEN_PAGE_SEMANTIC_READINESS_PASS");
assert.equal(success.attachment.candidateUrlPresent, true);
assert.equal(success.attachment.candidateUrlCloudflare, true);
const absentUrlSuccessRun = await run({ listingValue: [{ id: "task-tab" }] });
assert.equal(absentUrlSuccessRun.caught, null);
assert.equal(absentUrlSuccessRun.output.result, "EXACT_V49_TOKEN_PAGE_SEMANTIC_READINESS_PASS");
assert.equal(absentUrlSuccessRun.output.attachment.candidateUrlPresent, false);
assert.equal(absentUrlSuccessRun.output.attachment.candidateUrlCloudflare, false);
assert.equal(
  success.attachment.result,
  "EXACT_V49Attachment_CROSS_REALM_TASK_TAB_ACCOUNT_HOME_REACQUISITION_PASS",
);
const attachmentSuccessCounters = {
  importAttempted: 1, importFulfilled: 1,
  setupAttempted: 1, setupFulfilled: 1,
  connectAttempted: 1, connectFulfilled: 1,
  documentationAttempted: 1, documentationFulfilled: 1,
  documentationWriteAttempted: 1, documentationWriteFulfilled: 1,
  nameAttempted: 1, nameFulfilled: 1,
  openTabsAttempted: 1, openTabsFulfilled: 1,
  claimAttempted: 1, claimFulfilled: 1,
  navigationAttempted: 1, navigationFulfilled: 1,
  waitAttempted: 1, waitFulfilled: 1,
  urlAttempted: 1, urlFulfilled: 1,
  snapshotAttempted: 1, snapshotFulfilled: 1,
  writeAttempted: 0,
};
assert.deepEqual(
  Object.fromEntries(
    Object.keys(attachmentSuccessCounters).map((key) => [key, success.attachment[key]]),
  ),
  attachmentSuccessCounters,
);
assert.equal(success.tokenSemanticSignature, true);
assert.equal(success.continuationBindingsRetained, true);
assert.equal(success.predecessorRuntimeCleared, true);
assert.equal(success.bindingEligible, true);
assert.equal(success.bindingNull, false);
assert.equal(success.consumed, true);
assert.equal(success.errorClass, "NONE");
assert.equal(successRun.fixture.setupCalls, 1);
assert.equal(successRun.fixture.connectCalls, 1);
assert.equal(successRun.fixture.openTabsCalls, 1);
assert.equal(successRun.fixture.claimCalls, 1);
assert.equal(successRun.fixture.gotoCalls, 2);
assert.equal(successRun.fixture.waitCalls, 1);
assert.equal(successRun.fixture.urlCalls, 2);
assert.equal(successRun.fixture.accountSnapshotCalls, 1);
assert.deepEqual(
  Object.keys(success.attachment.snapshot).sort(),
  [
    "accountHomePath", "allAnchorCount", "busyCount", "exactZoneHrefCount",
    "hostExact",
  ],
);
assert.equal(typeof success.attachment.snapshot.hostExact, "boolean");
assert.equal(typeof success.attachment.snapshot.accountHomePath, "boolean");
for (const key of ["allAnchorCount", "busyCount", "exactZoneHrefCount"]) {
  assert.equal(Number.isSafeInteger(success.attachment.snapshot[key]), true, key);
  assert.ok(success.attachment.snapshot[key] >= 0, key);
  assert.ok(success.attachment.snapshot[key] <= 100000, key);
}
assert.deepEqual(successRun.fixture.observed, {
  consumed: true,
  tabNull: false,
  eligible: true,
  state: "TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE",
  attachmentTabNull: true,
  attachmentEligible: false,
  attachmentState: "V49Attachment_TRANSFERRED_TO_V49",
  chromeNull: true,
  agentNull: true,
  setupNull: true,
  evidenceNull: true,
  outputErrorNull: true,
  counters: {
    bindingAttempted: 1, bindingFulfilled: 1,
    navigationAttempted: 1, navigationFulfilled: 1,
    urlAttempted: 1, urlFulfilled: 1,
    readinessAttempted: 4, readinessFulfilled: 4,
    fillAttempted: 1, fillFulfilled: 1,
    createReadAttempted: 1, createReadFulfilled: 1,
    nameReadAttempted: 1, nameReadFulfilled: 1,
    rowReadAttempted: 1, rowReadFulfilled: 1,
    writeAttempted: 1,
  },
});

for (const prelude of [
  "let secureConsoleV41Consumed = false;\n",
  "let secureConsoleOwnedTaskTabV40 = null;\n",
  "let secureConsoleChromeV39 = {};\n",
  "let secureConsoleOwnedTaskTabV35Eligible = false;\n",
  "let secureConsoleOwnedTaskTabV35State = \"DIRTY\";\n",
  "let secureConsoleSetupBrowserRuntimeV41 = {};\n",
  "let secureConsoleAgentV35 = {};\n",
  "let secureConsoleCloudflareReadsV42Consumed = false;\n",
  "let secureConsoleOwnedTaskTabV43 = null;\n",
  "let secureConsoleOwnedTaskTabV43Eligible = false;\n",
  "let secureConsoleOwnedTaskTabV43State = \"DIRTY\";\n",
  "let secureConsoleOwnedTaskTabV43PreCreateDetachConsumed = false;\n",
  "let secureConsoleOwnedTaskTabV43PostNativeDetachConsumed = false;\n",
  "let secureConsoleCloudflareReadsV43Consumed = false;\n",
  "let secureConsoleV43Consumed = false;\n",
  "let secureConsoleOwnedTaskTabV44 = null;\n",
  "let secureConsoleOwnedTaskTabV44Eligible = false;\n",
  "let secureConsoleOwnedTaskTabV44State = \"DIRTY\";\n",
  "let secureConsoleOwnedTaskTabV44PreCreateDetachConsumed = false;\n",
  "let secureConsoleOwnedTaskTabV44PostNativeDetachConsumed = false;\n",
  "let secureConsoleCloudflareReadsV44Consumed = false;\n",
  "let secureConsoleV44Consumed = false;\n",
  "let secureConsoleSetupBrowserRuntimeV45 = null;\n",
  "let secureConsoleAgentV45 = null;\n",
  "let secureConsoleChromeV45 = null;\n",
  "let secureConsoleOwnedTaskTabV45 = null;\n",
  "let secureConsoleOwnedTaskTabV45Eligible = false;\n",
  "let secureConsoleV45Consumed = false;\n",
  "let secureConsoleV45State = \"DIRTY\";\n",
  "let secureConsoleOwnedTaskTabV46 = null;\n",
  "let secureConsoleOwnedTaskTabV46Eligible = false;\n",
  "let secureConsoleOwnedTaskTabV46State = \"DIRTY\";\n",
  "let secureConsoleOwnedTaskTabV46PreCreateDetachConsumed = false;\n",
  "let secureConsoleOwnedTaskTabV46PostNativeDetachConsumed = false;\n",
  "let secureConsoleCloudflareReadsV46Consumed = false;\n",
  "let secureConsoleV46Consumed = false;\n",
  "let secureConsoleOwnedTaskTabV47 = null;\n",
  "let secureConsoleOwnedTaskTabV47Eligible = false;\n",
  "let secureConsoleOwnedTaskTabV47State = \"DIRTY\";\n",
  "let secureConsoleOwnedTaskTabV47PreCreateDetachConsumed = false;\n",
  "let secureConsoleOwnedTaskTabV47PostNativeDetachConsumed = false;\n",
  "let secureConsoleCloudflareReadsV47Consumed = false;\n",
  "let secureConsoleV47Consumed = false;\n",
  "let secureConsoleV48Consumed = false;\n",
  "let secureConsoleV48State = \"DIRTY\";\n",
  "let secureConsoleV48Result = {};\n",
]) {
  const contaminated = await run({}, prelude);
  assert.equal(contaminated.caught, null);
  assert.equal(contaminated.fixture.setupCalls, 0);
  assert.equal(contaminated.fixture.openTabsCalls, 0);
  assert.equal(contaminated.output.result, "V49_TOKEN_PAGE_SEMANTIC_READINESS_FAILED_STOP");
  assert.equal(contaminated.output.attachment.declarationShape, false);
  for (const key of [
    "importAttempted", "setupAttempted", "documentationAttempted",
    "nameAttempted", "openTabsAttempted", "claimAttempted",
    "navigationAttempted", "waitAttempted", "urlAttempted",
    "snapshotAttempted",
  ]) assert.equal(contaminated.output.attachment[key], 0, `${prelude.trim()} ${key}`);
  assert.equal(contaminated.output.consumed, true);
  assert.equal(contaminated.output.bindingEligible, false);
  assert.equal(contaminated.output.bindingNull, true);
  assert.equal(
    contaminated.output.state,
    "V49_TOKEN_PAGE_SEMANTIC_READINESS_FAILED",
  );
  assert.equal(contaminated.output.failureCleanupComplete, true);
  assert.deepEqual(Object.keys(contaminated.output).sort(), expectedTopKeys);
}

const nonfreshSource = instrumented.replace(
  "let secureConsoleV49Consumed = false;",
  "let secureConsoleV49Consumed = true;",
);
const nonfresh = await run({}, "", nonfreshSource);
assert.equal(nonfresh.caught, null);
assert.equal(nonfresh.fixture.setupCalls, 0);
assert.equal(nonfresh.output.attachment.declarationShape, false);
assert.equal(nonfresh.output.attachment.importAttempted, 0);
assert.equal(nonfresh.output.failureCleanupComplete, true);
for (const [before, after] of [
  ["let secureConsoleOwnedTaskTabV49 = null;", "let secureConsoleOwnedTaskTabV49 = {};"],
  ["let secureConsoleOwnedTaskTabV49Eligible = false;", "let secureConsoleOwnedTaskTabV49Eligible = true;"],
  ["let secureConsoleOwnedTaskTabV49State = \"UNADOPTED\";", "let secureConsoleOwnedTaskTabV49State = \"DIRTY\";"],
  ["let secureConsoleOwnedTaskTabV49PreCreateDetachConsumed = false;", "let secureConsoleOwnedTaskTabV49PreCreateDetachConsumed = true;"],
  ["let secureConsoleOwnedTaskTabV49PostNativeDetachConsumed = false;", "let secureConsoleOwnedTaskTabV49PostNativeDetachConsumed = true;"],
  ["let secureConsoleCloudflareReadsV49Consumed = false;", "let secureConsoleCloudflareReadsV49Consumed = true;"],
  ["let secureConsoleSetupBrowserRuntimeV49Attachment = null;", "let secureConsoleSetupBrowserRuntimeV49Attachment = {};"],
  ["let secureConsoleAgentV49Attachment = null;", "let secureConsoleAgentV49Attachment = {};"],
  ["let secureConsoleChromeV49Attachment = null;", "let secureConsoleChromeV49Attachment = {};"],
  ["let secureConsoleOwnedTaskTabV49Attachment = null;", "let secureConsoleOwnedTaskTabV49Attachment = {};"],
  ["let secureConsoleOwnedTaskTabV49AttachmentEligible = false;", "let secureConsoleOwnedTaskTabV49AttachmentEligible = true;"],
  ["let secureConsoleV49AttachmentState = \"UNCREATED\";", "let secureConsoleV49AttachmentState = \"DIRTY\";"],
]) {
  const altered = instrumented.replace(before, after);
  assert.notEqual(altered, instrumented);
  const dirtyDefault = await run({}, "", altered);
  assert.equal(dirtyDefault.caught, null);
  assert.equal(dirtyDefault.fixture.setupCalls, 0);
  assert.equal(dirtyDefault.output.attachment.declarationShape, false);
  assert.equal(dirtyDefault.output.attachment.importAttempted, 0);
  assert.equal(dirtyDefault.output.failureCleanupComplete, true);
}

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
  const operation = {
    moduleShape: "import",
    agentShape: "setup",
    chromeShape: "connect",
    documentationInvalid: "documentation",
    listingShape: "enumeration",
    controllerShape: "claim",
    tabShape: "claim",
    accountUrl: null,
    accountUrlThrow: null,
  }[stage] ?? stage;
  const fulfilledInvalid = new Set([
    "moduleShape", "agentShape", "chromeShape", "documentationInvalid",
    "listingShape", "controllerShape", "tabShape", "accountUrl",
    "accountSignature",
  ]);
  let stopped = false;
  for (const [attempted, fulfilled, failureStage] of attachmentCounterPairs) {
    if (stopped) continue;
    expected[attempted] = 1;
    const stopsHere = ["accountUrl", "accountUrlThrow"].includes(stage)
      ? attempted === "urlAttempted"
      : failureStage === operation;
    if (stopsHere) {
      if (fulfilledInvalid.has(stage)) expected[fulfilled] = 1;
      stopped = true;
    } else {
      expected[fulfilled] = 1;
    }
  }
  return expected;
};
const zeroReadiness = Object.fromEntries(readinessCounterKeys.map((key) => [key, 0]));
zeroReadiness.writeAttempted = 1;

const malformedListing = new Array(1);
const listingRejected = await run({ listingValue: malformedListing });
assert.equal(listingRejected.caught, null);
assert.equal(listingRejected.fixture.claimCalls, 0);
assert.equal(listingRejected.output.attachment.listingValidated, false);
assert.equal(listingRejected.output.attachment.claimAttempted, 0);
assert.equal(listingRejected.output.attachment.claimFulfilled, 0);
assert.equal(listingRejected.output.failureCleanupComplete, true);
const listingFailureCounters = expectedAttachmentFailure("claim");
listingFailureCounters.claimAttempted = 0;
assert.deepEqual(
  select(listingRejected.output.attachment, attachmentCounterKeys),
  listingFailureCounters,
);
assert.deepEqual(select(listingRejected.output, readinessCounterKeys), zeroReadiness);
for (const [name, listing] of rejectedListings) {
  const rejected = await run({ listingValue: listing });
  assert.equal(rejected.caught, null, name);
  assert.equal(rejected.fixture.claimCalls, 0, name);
  assert.equal(rejected.output.consumed, true, name);
  assert.equal(rejected.output.bindingEligible, false, name);
  assert.equal(rejected.output.failureCleanupComplete, true, name);
  assert.deepEqual(
    select(rejected.output.attachment, attachmentCounterKeys),
    listingFailureCounters,
    name,
  );
  assert.deepEqual(select(rejected.output, readinessCounterKeys), zeroReadiness, name);
}

for (const stage of [
  "import", "moduleShape", "setup", "agentShape", "connect", "chromeShape",
  "documentation", "documentationInvalid", "sessionName", "enumeration",
  "listingShape", "claim", "controllerShape", "tabShape",
  "accountNavigation", "accountWait", "accountUrl", "accountUrlThrow",
  "accountSignature",
]) {
  const failed = await run({ failStage: stage });
  assert.equal(failed.caught, null, stage);
  assert.equal(failed.output.result, "V49_TOKEN_PAGE_SEMANTIC_READINESS_FAILED_STOP", stage);
  assert.equal(failed.output.attachment.errorClass, "Error", stage);
  assert.equal(failed.output.failureCleanupComplete, true, stage);
  assert.equal(failed.output.bindingEligible, false, stage);
  assert.equal(failed.output.consumed, true, stage);
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
  if (stage === "tokenUrlThrow") {
    expected.writeAttempted = 1;
    return expected;
  }
  expected.urlFulfilled = 1;
  if (stage === "tokenUrl") {
    expected.writeAttempted = 1;
    return expected;
  }
  expected.readinessAttempted = 1;
  if (stage === "tokenFilterWait") {
    expected.writeAttempted = 1;
    return expected;
  }
  expected.readinessFulfilled = 1;
  if ([
    "tokenSignature", "regionBinding", "controlledRoot", "paginatorShape",
  ].includes(stage)) {
    expected.writeAttempted = 1;
    return expected;
  }
  expected.readinessAttempted = 2;
  if (stage === "readinessWait") {
    expected.writeAttempted = 1;
    return expected;
  }
  expected.readinessFulfilled = 2;
  if (["initialFilterInvalid", "baselineInvalid"].includes(stage)) {
    expected.writeAttempted = 1;
    return expected;
  }
  expected.fillAttempted = 1;
  if (stage === "tokenFill") {
    expected.writeAttempted = 1;
    return expected;
  }
  expected.fillFulfilled = 1;
  expected.readinessAttempted = 3;
  if (stage === "queryEchoWait") {
    expected.writeAttempted = 1;
    return expected;
  }
  expected.readinessFulfilled = 3;
  if (stage === "queryEchoCount") {
    expected.writeAttempted = 1;
    return expected;
  }
  expected.readinessAttempted = 4;
  if (stage === "emptyStatusWait") {
    expected.writeAttempted = 1;
    return expected;
  }
  expected.readinessFulfilled = 4;
  if (stage === "emptyStatusCount") {
    expected.writeAttempted = 1;
    return expected;
  }
  expected.createReadAttempted = 1;
  if (stage === "createReadThrow") {
    expected.writeAttempted = 1;
    return expected;
  }
  expected.createReadFulfilled = 1;
  expected.nameReadAttempted = 1;
  if (stage === "nameReadThrow") {
    expected.writeAttempted = 1;
    return expected;
  }
  expected.nameReadFulfilled = 1;
  expected.rowReadAttempted = 1;
  if (stage === "rowReadThrow") {
    expected.writeAttempted = 1;
    return expected;
  }
  expected.rowReadFulfilled = 1;
  expected.writeAttempted = 1;
  return expected;
};
for (const stage of [
  "tokenNavigation", "tokenUrl", "tokenUrlThrow", "tokenFilterWait",
  "tokenSignature", "regionBinding", "controlledRoot", "paginatorShape",
  "readinessWait",
  "initialFilterInvalid", "baselineInvalid", "tokenFill", "queryEchoWait",
  "queryEchoCount", "emptyStatusWait", "emptyStatusCount",
  "tokenValueInvalid", "terminalInvalid", "createReadThrow",
  "createReadInvalid", "nameReadThrow", "nameReadInvalid", "rowReadThrow",
  "rowReadInvalid",
]) {
  const failed = await run({ failStage: stage });
  assert.equal(failed.caught, null, stage);
  assert.equal(failed.output.errorClass, "Error", stage);
  assert.equal(failed.output.failureCleanupComplete, true, stage);
  assert.equal(failed.output.bindingEligible, false, stage);
  assert.equal(failed.output.consumed, true, stage);
  assert.deepEqual(
    select(failed.output, readinessCounterKeys),
    expectedReadinessFailure(stage),
    stage,
  );
  assert.deepEqual(Object.keys(failed.output).sort(), expectedTopKeys, stage);
  assert.equal(JSON.stringify(failed.output).includes(`Hidden-${stage}`), false, stage);
}

const attachmentCounterMismatchSource = instrumented.replace(
  "counters.snapshotFulfilled++;",
  "void 0;",
);
assert.notEqual(attachmentCounterMismatchSource, instrumented);
const attachmentCounterMismatch = await run({}, "", attachmentCounterMismatchSource);
assert.equal(attachmentCounterMismatch.caught, null);
assert.equal(attachmentCounterMismatch.output.attachment.semanticComplete, true);
assert.equal(attachmentCounterMismatch.output.attachment.snapshotAttempted, 1);
assert.equal(attachmentCounterMismatch.output.attachment.snapshotFulfilled, 0);
assert.equal(attachmentCounterMismatch.output.attachment.errorClass, "Error");
assert.equal(attachmentCounterMismatch.output.failureCleanupComplete, true);

const readinessCounterMismatchSource = instrumented.replace(
  "counters.rowReadFulfilled++;",
  "void 0;",
);
assert.notEqual(readinessCounterMismatchSource, instrumented);
const readinessCounterMismatch = await run({}, "", readinessCounterMismatchSource);
assert.equal(readinessCounterMismatch.caught, null);
assert.equal(readinessCounterMismatch.output.rowReadAttempted, 1);
assert.equal(readinessCounterMismatch.output.rowReadFulfilled, 0);
assert.equal(readinessCounterMismatch.output.errorClass, "Error");
assert.equal(readinessCounterMismatch.output.failureCleanupComplete, true);

let getterCalls = 0;
const assertHostileClaimFailure = async (thrown, token) => {
  const failureRun = await run({ claimThrown: thrown });
  assert.equal(failureRun.caught, null);
  assert.equal(failureRun.output.result, "V49_TOKEN_PAGE_SEMANTIC_READINESS_FAILED_STOP");
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
assert.deepEqual(
  select(finalOutputFailure.fixture.finalWriteAttachment, attachmentCounterKeys),
  attachmentSuccessCounters,
);
assert.deepEqual(
  finalOutputFailure.fixture.observed.counters,
  select(success, readinessCounterKeys),
);
assert.equal(finalOutputFailure.fixture.observed.consumed, true);
assert.equal(finalOutputFailure.fixture.observed.tabNull, true);
assert.equal(finalOutputFailure.fixture.observed.eligible, false);
assert.equal(finalOutputFailure.fixture.observed.state, "V49_FINAL_OUTPUT_FAILED_STOP");
assert.equal(finalOutputFailure.fixture.observed.attachmentTabNull, true);
assert.equal(finalOutputFailure.fixture.observed.attachmentEligible, false);
assert.equal(
  finalOutputFailure.fixture.observed.attachmentState,
  "V49Attachment_DOWNSTREAM_OUTPUT_FAILURE_DETACHED",
);
assert.equal(finalOutputFailure.fixture.observed.chromeNull, true);
assert.equal(finalOutputFailure.fixture.observed.agentNull, true);
assert.equal(finalOutputFailure.fixture.observed.setupNull, true);
assert.equal(finalOutputFailure.fixture.observed.evidenceNull, true);
assert.equal(finalOutputFailure.fixture.observed.outputErrorNull, true);

const documentationOutputFailure = await run({ failWriteAt: 1 });
assert.equal(
  documentationOutputFailure.caught,
  documentationOutputFailure.fixture.outputThrown,
);
assert.equal(documentationOutputFailure.fixture.writeCalls, 1);
assert.equal(documentationOutputFailure.fixture.writes.length, 0);
assert.deepEqual(
  select(
    documentationOutputFailure.fixture.documentationFailureAttachment,
    attachmentCounterKeys,
  ),
  {
    importAttempted: 1, importFulfilled: 1,
    setupAttempted: 1, setupFulfilled: 1,
    connectAttempted: 1, connectFulfilled: 1,
    documentationAttempted: 1, documentationFulfilled: 1,
    documentationWriteAttempted: 1, documentationWriteFulfilled: 0,
    nameAttempted: 0, nameFulfilled: 0,
    openTabsAttempted: 0, openTabsFulfilled: 0,
    claimAttempted: 0, claimFulfilled: 0,
    navigationAttempted: 0, navigationFulfilled: 0,
    waitAttempted: 0, waitFulfilled: 0,
    urlAttempted: 0, urlFulfilled: 0,
    snapshotAttempted: 0, snapshotFulfilled: 0,
    writeAttempted: 0,
  },
);
assert.deepEqual(documentationOutputFailure.fixture.documentationFailureObserved, {
  consumed: true,
  tabNull: true,
  eligible: false,
  state: "UNADOPTED",
  attachmentTabNull: true,
  attachmentEligible: false,
  attachmentState: "V49Attachment_REACQUISITION_OR_READINESS_FAILED",
  chromeNull: true,
  agentNull: true,
  setupNull: true,
  evidenceNull: true,
  outputErrorNull: true,
});
assert.equal(outputGetterCalls, 0);

const modelCoordinatorCleanup = (proofFails) => {
  let proofAttempts = 0;
  let correctedQueryAttempts = 0;
  let resetAttempts = 0;
  const order = [];
  try {
    proofAttempts++;
    order.push("proof");
    if (proofFails) throw new Error("fixed proof failure");
  } catch {
    // Record uncertainty; never correct or retry the failed proof.
  } finally {
    resetAttempts++;
    order.push("reset");
  }
  return { proofAttempts, correctedQueryAttempts, resetAttempts, order };
};
const cleanupProofSuccess = modelCoordinatorCleanup(false);
const cleanupProofFailure = modelCoordinatorCleanup(true);
for (const scenario of [cleanupProofSuccess, cleanupProofFailure]) {
  assert.equal(scenario.proofAttempts, 1);
  assert.equal(scenario.correctedQueryAttempts, 0);
  assert.equal(scenario.resetAttempts, 1);
  assert.deepEqual(scenario.order, ["proof", "reset"]);
}

console.log(JSON.stringify({
  result: "V49_PURE_FIXTURES_PASS",
  briefBytes: Buffer.byteLength(brief),
  briefSha256: crypto.createHash("sha256").update(brief).digest("hex").toUpperCase(),
  executableBytes,
  executableSha256,
  fixtureBytes,
  fixtureSha256,
  syntax: "PASS",
  declarationFree: true,
  v48PredecessorsAbsent: true,
  listingMatrix: true,
  exactOutputKeys: true,
  fullCellSuccess: true,
  fixedFailureCleanup: true,
  hostileThrownValues: true,
  terminalOutputCleanup: true,
  oneProofOnlyCleanup: true,
  cleanupProofScenarioCount: 2,
  cleanupProofAttempts: 2,
  cleanupCorrectedQueryAttempts: 0,
  cleanupResetAttempts: 2,
  completeCounterVectors: true,
  getterCalls,
  listingGetterCalls,
  outputGetterCalls,
}));
