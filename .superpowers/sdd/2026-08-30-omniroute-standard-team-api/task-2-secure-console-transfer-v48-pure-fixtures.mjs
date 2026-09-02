import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import { fileURLToPath } from "node:url";

const directory = path.dirname(fileURLToPath(import.meta.url));
const executablePath = path.join(
  directory,
  "task-2-secure-console-transfer-v48-fresh-realm-listing-shape-diagnostic-executable.js",
);
const cell = fs.readFileSync(executablePath, "utf8").replace(/\r\n/g, "\n");
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;
assert.doesNotThrow(() => new AsyncFunction(cell));

const inspectorMatch = cell.match(
  /\/\/ BEGIN_V48_PURE_INSPECTOR\n([\s\S]*?)\n  \/\/ END_V48_PURE_INSPECTOR/,
);
assert.ok(inspectorMatch);
const inspectOpenTabsV48 = new Function(
  `${inspectorMatch[1].trim()}\nreturn inspectOpenTabsV48;`,
)();

const expectedKeys = [
  "arrayIsArray",
  "arrayOwnSymbolCountZero",
  "lengthDescriptorPresent",
  "lengthDescriptorData",
  "lengthDescriptorNonEnumerable",
  "lengthDescriptorNoAccessor",
  "boundedLength",
  "offeredCount",
  "arrayOwnNamesExact",
  "allIndexDescriptorsDataEnumerable",
  "descriptorIndexCountMatchesLength",
  "rankZeroNonNullObject",
  "rankZeroOrdinaryPrototype",
  "rankZeroPrototypeDepthBounded",
  "rankZeroOwnSymbolCountZero",
  "rankZeroKnownKeysOnly",
  "rankZeroRequiredIdentityPresent",
  "rankZeroUnexpectedKeyCount",
  "rankZeroDescriptorsSafe",
  "rankZeroRequiredValuesSafeStrings",
  "rankZeroOptionalValuesStringOrUndefined",
  "rankZeroAllValuesV47Safe",
  "urlFieldPresent",
  "urlFieldSafeString",
  "urlParseSucceeded",
  "urlHttps",
  "urlCloudflareHostExact",
  "urlPortEmpty",
  "urlUsernameEmpty",
  "urlPasswordEmpty",
  "urlCloudflareV47",
  "urlAbsentOrCloudflareV47",
  "documentedKeyChecks",
];
const expectedDocumentedKeys = [
  "id", "lastOpened", "providerTabId", "tabGroup", "title", "url",
];
const inspect = (value) => {
  const result = inspectOpenTabsV48(value);
  assert.deepEqual(Object.keys(result), expectedKeys);
  assert.deepEqual(Object.keys(result.documentedKeyChecks), expectedDocumentedKeys);
  assert.ok(result.offeredCount === -1 ||
    (Number.isSafeInteger(result.offeredCount) &&
     result.offeredCount >= 1 && result.offeredCount <= 1000));
  assert.ok(result.rankZeroUnexpectedKeyCount === -1 ||
    (Number.isSafeInteger(result.rankZeroUnexpectedKeyCount) &&
     result.rankZeroUnexpectedKeyCount >= 0 &&
     result.rankZeroUnexpectedKeyCount <= 1000));
  return result;
};

const ordinaryRecord = () => ({
  id: "tab-1",
  lastOpened: "2026-09-02T16:00:00.000Z",
  providerTabId: "provider-1",
  tabGroup: "group-1",
  title: "API Tokens | Cloudflare",
  url: "https://dash.cloudflare.com/profile/api-tokens",
});
const exact = inspect([ordinaryRecord()]);
for (const [key, value] of Object.entries(exact)) {
  if (key === "offeredCount") assert.equal(value, 1);
  else if (key === "rankZeroUnexpectedKeyCount") assert.equal(value, 0);
  else if (key !== "documentedKeyChecks") assert.equal(value, true);
}
for (const key of expectedDocumentedKeys) {
  for (const [field, value] of Object.entries(exact.documentedKeyChecks[key])) {
    if (field === "required") assert.equal(value, key === "id");
    else assert.equal(value, true);
  }
}
const serializedExact = JSON.stringify(exact);
for (const raw of Object.values(ordinaryRecord())) {
  assert.equal(serializedExact.includes(raw), false);
}

const foreign = inspect(vm.runInNewContext("[{ id: 'tab-foreign' }]"));
assert.equal(foreign.arrayIsArray, true);
assert.equal(foreign.rankZeroOrdinaryPrototype, true);
assert.equal(JSON.stringify(foreign).includes("tab-foreign"), false);

const optionalUndefined = ordinaryRecord();
optionalUndefined.title = undefined;
const optionalResult = inspect([optionalUndefined]);
assert.equal(optionalResult.rankZeroOptionalValuesStringOrUndefined, true);
assert.equal(optionalResult.rankZeroAllValuesV47Safe, false);
assert.equal(optionalResult.documentedKeyChecks.title.valueTypeAllowed, true);

const symbolArray = [ordinaryRecord()];
symbolArray[Symbol("private")] = true;
assert.equal(inspect(symbolArray).arrayOwnSymbolCountZero, false);

const sparse = new Array(2);
sparse[0] = ordinaryRecord();
const sparseResult = inspect(sparse);
assert.equal(sparseResult.arrayOwnNamesExact, false);
assert.equal(sparseResult.allIndexDescriptorsDataEnumerable, false);

const laterRankPrimitive = inspect([ordinaryRecord(), 42]);
assert.equal(laterRankPrimitive.allIndexDescriptorsDataEnumerable, true);
assert.equal(laterRankPrimitive.rankZeroAllValuesV47Safe, true);
assert.equal(laterRankPrimitive.urlCloudflareV47, true);

let indexGetterCalls = 0;
const accessorArray = new Array(1);
Object.defineProperty(accessorArray, "0", {
  enumerable: true,
  get() {
    indexGetterCalls++;
    throw new Error("index getter invoked");
  },
});
assert.equal(inspect(accessorArray).allIndexDescriptorsDataEnumerable, false);
assert.equal(indexGetterCalls, 0);

const extraKey = ordinaryRecord();
extraKey.extra = "not-emitted";
const extraResult = inspect([extraKey]);
assert.equal(extraResult.rankZeroKnownKeysOnly, false);
assert.equal(extraResult.rankZeroUnexpectedKeyCount, 1);
assert.equal(JSON.stringify(extraResult).includes("not-emitted"), false);

let recordGetterCalls = 0;
const accessorRecord = ordinaryRecord();
Object.defineProperty(accessorRecord, "title", {
  enumerable: true,
  get() {
    recordGetterCalls++;
    throw new Error("record getter invoked");
  },
});
const accessorRecordResult = inspect([accessorRecord]);
assert.equal(accessorRecordResult.rankZeroDescriptorsSafe, false);
assert.equal(accessorRecordResult.documentedKeyChecks.title.data, false);
assert.equal(recordGetterCalls, 0);

const symbolRecord = ordinaryRecord();
symbolRecord[Symbol("private")] = true;
assert.equal(inspect([symbolRecord]).rankZeroOwnSymbolCountZero, false);

class NonOrdinaryRecord {
  constructor() {
    Object.assign(this, ordinaryRecord());
  }
}
assert.equal(
  inspect([new NonOrdinaryRecord()]).rankZeroOrdinaryPrototype,
  false,
);

assert.equal(inspect(new Array(1001)).boundedLength, false);
assert.equal(inspect(new Array(1001)).offeredCount, -1);

const malformedUrl = ordinaryRecord();
malformedUrl.url = "not a url";
const malformedUrlResult = inspect([malformedUrl]);
assert.equal(malformedUrlResult.urlFieldSafeString, true);
assert.equal(malformedUrlResult.urlParseSucceeded, false);
assert.equal(malformedUrlResult.urlCloudflareHostExact, false);
assert.equal(malformedUrlResult.urlAbsentOrCloudflareV47, false);

const portUrl = ordinaryRecord();
portUrl.url = "https://dash.cloudflare.com:8443/profile/api-tokens";
const portResult = inspect([portUrl]);
assert.equal(portResult.urlHttps, true);
assert.equal(portResult.urlCloudflareHostExact, true);
assert.equal(portResult.urlPortEmpty, false);
assert.equal(portResult.urlCloudflareV47, false);

const userInfoUrl = ordinaryRecord();
userInfoUrl.url = "https://user:pass@dash.cloudflare.com/profile/api-tokens";
const userInfoResult = inspect([userInfoUrl]);
assert.equal(userInfoResult.urlUsernameEmpty, false);
assert.equal(userInfoResult.urlPasswordEmpty, false);
assert.equal(userInfoResult.urlCloudflareV47, false);

const unrelatedPathUrl = ordinaryRecord();
unrelatedPathUrl.url = "https://dash.cloudflare.com/unrelated";
const unrelatedPathResult = inspect([unrelatedPathUrl]);
assert.equal(unrelatedPathResult.urlCloudflareV47, true);
assert.equal(unrelatedPathResult.urlAbsentOrCloudflareV47, true);

assert.throws(() => inspect(new Proxy([], {
  ownKeys() {
    throw new Error("throwing proxy");
  },
})));

const documentationSeed = [
  "openTabs(): Promise<Array<BrowserUserTabInfo>>",
  "id: string",
  "lastOpened?: string",
  "providerTabId?: string",
  "tabGroup?: string",
  "title?: string",
  "url?: string",
].join("\n");
const documentation = documentationSeed.padEnd(42370, "x");
let listingFactory = () => [ordinaryRecord()];
let importCalls = 0;
let setupCalls = 0;
let connectCalls = 0;
let documentationCalls = 0;
let nameCalls = 0;
let openTabsCalls = 0;
let terminalWrites = [];
const fixtureImported = {
  async setupBrowserRuntime() {
    setupCalls++;
    return {
      browsers: {
        async get(id) {
          connectCalls++;
          assert.equal(id, "chrome");
          return {
            async documentation() {
              documentationCalls++;
              return documentation;
            },
            async nameSession(name) {
              nameCalls++;
              assert.equal(name, "🔐 OmniRoute V48 listing diagnostic");
            },
            user: {
              async openTabs() {
                openTabsCalls++;
                return listingFactory();
              },
            },
          };
        },
      },
    };
  },
};
const importPattern = /await import\(\n\s*"file:\/\/\/C:\/Users\/chatc\/\.codex\/plugins\/cache\/openai-bundled\/chrome\/26\.831\.21537\/scripts\/browser-client\.mjs"\n\s*\)/;
const transformedCell = cell.replace(
  importPattern,
  "await Promise.resolve(fixtureImported)",
);
assert.notEqual(transformedCell, cell);
const runCell = async () => {
  terminalWrites = [];
  const nodeRepl = {
    async write(value) {
      terminalWrites.push(value);
    },
  };
  importCalls++;
  await new AsyncFunction("fixtureImported", "nodeRepl", transformedCell)(
    fixtureImported,
    nodeRepl,
  );
  assert.equal(terminalWrites.length, 2);
  assert.equal(terminalWrites[0], documentation);
  return terminalWrites[1];
};

const terminal = await runCell();
assert.equal(importCalls, 1);
assert.equal(setupCalls, 1);
assert.equal(connectCalls, 1);
assert.equal(documentationCalls, 1);
assert.equal(nameCalls, 1);
assert.equal(openTabsCalls, 1);
assert.equal(terminal.result,
  "EXACT_V48_FIXED_LISTING_SHAPE_DIAGNOSTIC_CAPTURED");
assert.equal(terminal.errorClass, "NONE");
assert.equal(terminal.consumed, true);
assert.equal(terminal.bindingEligible, false);
assert.equal(terminal.bindingsCleared, true);
assert.equal(terminal.state, "DIAGNOSTIC_CAPTURED_INELIGIBLE");
for (const key of [
  "importAttempted", "importFulfilled", "setupAttempted", "setupFulfilled",
  "connectAttempted", "connectFulfilled", "documentationAttempted",
  "documentationFulfilled", "documentationWriteAttempted",
  "documentationWriteFulfilled", "nameAttempted", "nameFulfilled",
  "openTabsAttempted", "openTabsFulfilled",
]) assert.equal(terminal[key], 1);
for (const key of [
  "claimAttempted", "navigationAttempted", "waitAttempted",
  "urlReadAttempted", "snapshotAttempted", "domActionAttempted",
  "clipboardAttempted", "providerMutationAttempted",
]) assert.equal(terminal[key], 0);

listingFactory = () => {
  throw { name: "ASecretLikeToken", value: "never-emit-this" };
};
const failure = await runCell();
assert.equal(failure.result, "V48_FRESH_LISTING_SHAPE_DIAGNOSTIC_FAILED_STOP");
assert.equal(failure.errorClass, "Error");
assert.equal(failure.state, "FAILED_INELIGIBLE");
assert.equal(failure.bindingsCleared, true);
assert.equal(JSON.stringify(failure).includes("ASecretLikeToken"), false);
assert.equal(JSON.stringify(failure).includes("never-emit-this"), false);

console.log("V48_PURE_FIXTURES_PASS");
