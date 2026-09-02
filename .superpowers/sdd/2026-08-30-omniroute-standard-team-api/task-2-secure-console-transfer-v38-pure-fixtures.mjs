import assert from "node:assert/strict";
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import { fileURLToPath, pathToFileURL } from "node:url";

const directory = path.dirname(fileURLToPath(import.meta.url));
const briefPath = path.join(
  directory,
  "task-2-secure-console-transfer-v38-fresh-session-listing-shape-diagnostic-brief.md",
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
assert.doesNotThrow(() => new AsyncFunction(cell));

const blockMatch = cell.match(
  /\/\/ BEGIN_V38_PURE_LISTING_DIAGNOSTIC\n([\s\S]*?)\n  \/\/ END_V38_PURE_LISTING_DIAGNOSTIC/,
);
assert.ok(blockMatch);
const inspectListingV38 = new Function(
  `${blockMatch[1]}\nreturn inspectListingV38;`,
)();

const expectedKeys = [
  "arrayIsArray",
  "arrayPrototypeExact",
  "arraySymbolsZero",
  "lengthDescriptorPresent",
  "lengthDescriptorData",
  "lengthDescriptorNonEnumerable",
  "lengthDescriptorSafeBounded",
  "offeredCount",
  "arrayOwnNamesReadable",
  "arrayNameCountExact",
  "arrayNamesExpectedOnly",
  "allIndexDescriptorsPresent",
  "allIndexDescriptorsData",
  "allIndexDescriptorsEnumerable",
  "allRecordsPlain",
  "allRecordSymbolsZero",
  "allRecordKeysAllowedWithId",
  "allRecordDescriptorsPresent",
  "allRecordDescriptorsData",
  "allRecordDescriptorsEnumerable",
  "allRecordIdsV37Safe",
  "allRecordUrlsAbsentOrV37Safe",
  "allOptionalValuesStringOrUndefined",
  "allRecordValuesV37Safe",
];
const ordinary = () => [{ id: "tab-1", url: "https://example.invalid/" }];
const inspect = (value) => {
  const result = inspectListingV38(value);
  assert.deepEqual(Object.keys(result), expectedKeys);
  return result;
};

const exact = inspect(ordinary());
for (const key of expectedKeys) {
  if (key === "offeredCount") assert.equal(exact[key], 1);
  else assert.equal(exact[key], true);
}

const foreign = inspect(vm.runInNewContext("[{ id: 'tab-1' }]"));
assert.equal(foreign.arrayIsArray, true);
assert.equal(foreign.arrayPrototypeExact, false);
assert.equal(foreign.allRecordsPlain, true);

const symbolArray = ordinary();
symbolArray[Symbol("private")] = true;
assert.equal(inspect(symbolArray).arraySymbolsZero, false);
assert.equal(inspect([]).offeredCount, -1);
assert.equal(inspect(new Array(1001)).offeredCount, -1);

const unexpectedName = ordinary();
unexpectedName.extra = true;
const unexpectedNameResult = inspect(unexpectedName);
assert.equal(unexpectedNameResult.arrayNameCountExact, false);
assert.equal(unexpectedNameResult.arrayNamesExpectedOnly, false);

const hole = new Array(2);
hole[0] = { id: "tab-1" };
const holeResult = inspect(hole);
assert.equal(holeResult.arrayNameCountExact, false);
assert.equal(holeResult.allIndexDescriptorsPresent, false);
assert.equal(holeResult.allIndexDescriptorsData, false);
assert.equal(holeResult.allIndexDescriptorsEnumerable, false);

let indexGetterCalls = 0;
const indexAccessor = new Array(1);
Object.defineProperty(indexAccessor, "0", {
  configurable: true,
  enumerable: true,
  get() {
    indexGetterCalls++;
    throw new Error("index getter invoked");
  },
});
const indexAccessorResult = inspect(indexAccessor);
assert.equal(indexAccessorResult.allIndexDescriptorsData, false);
assert.equal(indexAccessorResult.allIndexDescriptorsEnumerable, true);
assert.equal(indexGetterCalls, 0);

const nonEnumerableIndex = new Array(1);
Object.defineProperty(nonEnumerableIndex, "0", {
  configurable: true,
  enumerable: false,
  value: { id: "tab-1" },
});
assert.equal(
  inspect(nonEnumerableIndex).allIndexDescriptorsEnumerable,
  false,
);

const nullPrototypeRecord = Object.assign(Object.create(null), { id: "tab-1" });
assert.equal(inspect([nullPrototypeRecord]).allRecordsPlain, true);
class NonPlainRecord {
  constructor() {
    this.id = "tab-1";
  }
}
const nonPlain = inspect([new NonPlainRecord()]);
assert.equal(nonPlain.allRecordsPlain, false);
for (const key of expectedKeys.slice(15)) assert.equal(nonPlain[key], null);

const recordSymbol = { id: "tab-1" };
recordSymbol[Symbol("private")] = true;
assert.equal(inspect([recordSymbol]).allRecordSymbolsZero, false);
assert.equal(inspect([{ title: "missing id" }]).allRecordKeysAllowedWithId, false);
assert.equal(inspect([{ id: "tab-1", extra: "x" }]).allRecordKeysAllowedWithId, false);

const phantomRecord = new Proxy(
  { id: "tab-1" },
  {
    ownKeys() {
      return ["id", "url"];
    },
    getOwnPropertyDescriptor(target, key) {
      if (key === "url") return undefined;
      return Reflect.getOwnPropertyDescriptor(target, key);
    },
  },
);
const phantom = inspect([phantomRecord]);
assert.equal(phantom.allRecordDescriptorsPresent, false);
assert.equal(phantom.allRecordDescriptorsData, false);
assert.equal(phantom.allRecordDescriptorsEnumerable, false);
assert.equal(phantom.allOptionalValuesStringOrUndefined, false);
assert.equal(phantom.allRecordUrlsAbsentOrV37Safe, false);

for (const enumerable of [true, false]) {
  let recordGetterCalls = 0;
  const record = { id: "tab-1" };
  Object.defineProperty(record, "url", {
    configurable: true,
    enumerable,
    get() {
      recordGetterCalls++;
      throw new Error("record getter invoked");
    },
  });
  const result = inspect([record]);
  assert.equal(result.allRecordDescriptorsData, false);
  assert.equal(result.allRecordDescriptorsEnumerable, enumerable);
  assert.equal(result.allOptionalValuesStringOrUndefined, false);
  assert.equal(result.allRecordUrlsAbsentOrV37Safe, false);
  assert.equal(recordGetterCalls, 0);
}

const optionalUndefined = inspect([{ id: "tab-1", title: undefined }]);
assert.equal(optionalUndefined.allOptionalValuesStringOrUndefined, true);
assert.equal(optionalUndefined.allRecordValuesV37Safe, false);
assert.equal(inspect([{ id: "" }]).allRecordIdsV37Safe, false);
assert.equal(inspect([{ id: "x".repeat(513) }]).allRecordIdsV37Safe, false);
assert.equal(inspect([{ id: "tab\u0000" }]).allRecordIdsV37Safe, false);
assert.equal(
  inspect([{ id: "tab-1", url: "" }]).allRecordUrlsAbsentOrV37Safe,
  false,
);
assert.equal(
  inspect([{ id: "tab-1", url: "x".repeat(16385) }])
    .allRecordUrlsAbsentOrV37Safe,
  false,
);

let arrayGetCalls = 0;
const noReadArray = new Proxy(ordinary(), {
  get() {
    arrayGetCalls++;
    throw new Error("direct array property read");
  },
});
assert.equal(inspect(noReadArray).allRecordValuesV37Safe, true);
assert.equal(arrayGetCalls, 0);

let recordGetCalls = 0;
const noReadRecord = new Proxy(
  { id: "tab-1", url: "https://example.invalid/" },
  {
    get() {
      recordGetCalls++;
      throw new Error("direct record property read");
    },
  },
);
assert.equal(inspect([noReadRecord]).allRecordValuesV37Safe, true);
assert.equal(recordGetCalls, 0);

const documentationSeed = [
  "openTabs(): Promise<Array<BrowserUserTabInfo>>",
  "id: string",
  "lastOpened?: string",
  "providerTabId?: string",
  "tabGroup?: string",
  "title?: string",
  "url?: string",
].join("\n");
const documentation =
  documentationSeed + "x".repeat(42000 - documentationSeed.length);
const terminalWrites = [];
let documentationCalls = 0;
let nameCalls = 0;
let openTabsCalls = 0;
const fixtureBrowser = {
  async documentation() {
    documentationCalls++;
    return documentation;
  },
  async nameSession(name) {
    nameCalls++;
    assert.equal(name, "OmniRoute V38 listing-shape diagnostic");
  },
  user: {
    async openTabs() {
      openTabsCalls++;
      return ordinary();
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
const transformedCell = cell.replace(
  /const imported = await import\([\s\S]*?\n    \);/,
  "const imported = globalThis.__v38FixtureImported;",
);
assert.notEqual(transformedCell, cell);
const previousNodeRepl = globalThis.nodeRepl;
globalThis.__v38FixtureImported = fixtureImported;
globalThis.nodeRepl = {
  async write(value) {
    terminalWrites.push(value);
  },
};
try {
  await new AsyncFunction(transformedCell)();
} finally {
  delete globalThis.__v38FixtureImported;
  if (previousNodeRepl === undefined) delete globalThis.nodeRepl;
  else globalThis.nodeRepl = previousNodeRepl;
}
assert.equal(documentationCalls, 1);
assert.equal(nameCalls, 1);
assert.equal(openTabsCalls, 1);
assert.equal(terminalWrites.length, 2);
assert.equal(terminalWrites[0], documentation);
const terminal = terminalWrites[1];
const expectedTerminalKeys = [
  "result",
  "declarationShape",
  "moduleShape",
  "agentShape",
  "connectedShape",
  "documentationValidated",
  "documentationLength",
  "sessionNamed",
  ...expectedKeys,
  "importAttempted",
  "importFulfilled",
  "setupAttempted",
  "setupFulfilled",
  "connectAttempted",
  "connectFulfilled",
  "documentationAttempted",
  "documentationFulfilled",
  "documentationWriteAttempted",
  "documentationWriteFulfilled",
  "nameAttempted",
  "nameFulfilled",
  "openTabsAttempted",
  "openTabsFulfilled",
  "claimAttempted",
  "navigationAttempted",
  "urlAttempted",
  "snapshotAttempted",
  "writeAttempted",
  "errorClass",
  "consumed",
  "bindingEligible",
  "bindingNull",
  "state",
];
assert.deepEqual(Object.keys(terminal), expectedTerminalKeys);
assert.equal(terminal.result, "EXACT_V38_FIXED_LISTING_SHAPE_DIAGNOSTIC_CAPTURED");
assert.equal(terminal.errorClass, "NONE");
assert.equal(terminal.consumed, true);
assert.equal(terminal.bindingEligible, false);
assert.equal(terminal.bindingNull, true);
assert.equal(terminal.state, "V38_DIAGNOSTIC_CAPTURED_INELIGIBLE");
for (const key of [
  "importAttempted", "importFulfilled",
  "setupAttempted", "setupFulfilled",
  "connectAttempted", "connectFulfilled",
  "documentationAttempted", "documentationFulfilled",
  "documentationWriteAttempted", "documentationWriteFulfilled",
  "nameAttempted", "nameFulfilled",
  "openTabsAttempted", "openTabsFulfilled", "writeAttempted",
]) assert.equal(terminal[key], 1);
for (const key of [
  "claimAttempted", "navigationAttempted", "urlAttempted", "snapshotAttempted",
]) assert.equal(terminal[key], 0);

const report = {
  result: "V38_PURE_FIXTURES_PASS",
  briefBytes: Buffer.byteLength(brief),
  briefSha256: crypto.createHash("sha256").update(brief).digest("hex").toUpperCase(),
  executableBytes: Buffer.byteLength(cell),
  executableSha256: crypto.createHash("sha256").update(cell).digest("hex").toUpperCase(),
  syntax: "PASS",
  moduleShape: true,
  fixedSchema: true,
  getterCalls: indexGetterCalls + arrayGetCalls + recordGetCalls,
};
console.log(JSON.stringify(report));
