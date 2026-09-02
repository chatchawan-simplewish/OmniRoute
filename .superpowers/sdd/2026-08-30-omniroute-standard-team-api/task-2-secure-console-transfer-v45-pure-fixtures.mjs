import assert from "node:assert/strict";
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import { fileURLToPath, pathToFileURL } from "node:url";

const fixturePath = fileURLToPath(import.meta.url);
const directory = path.dirname(fixturePath);
const fixture = fs.readFileSync(fixturePath);
const briefPath = path.join(
  directory,
  "task-2-secure-console-transfer-v45-fresh-session-listing-shape-diagnostic-brief.md",
);
const brief = fs.readFileSync(briefPath, "utf8");
const runtimeModulePath =
  "C:/Users/chatc/.codex/plugins/cache/openai-bundled/chrome/26.831.21537/scripts/browser-client.mjs";
const runtimeModule = await import(pathToFileURL(runtimeModulePath).href);
assert.equal(typeof runtimeModule, "object");
assert.notEqual(runtimeModule, null);
assert.equal(typeof runtimeModule.setupBrowserRuntime, "function");
assert.equal("BROWSER_CLIENT_ID" in runtimeModule, false);
const cells = [...brief.matchAll(/~~~javascript\r?\n([\s\S]*?)\r?\n~~~/g)];
assert.equal(cells.length, 1);
const cell = cells[0][1].replace(/\r\n/g, "\n");
const fixtureSha256 = crypto.createHash("sha256").update(fixture).digest("hex").toUpperCase();
assert.ok(brief.includes("D4469DA4ECA7BF2667894A7780C6F022D02827548BE873B716EA2D778B0AE81F"));
assert.ok(brief.includes(`- Pure fixture length: \`${fixture.length}\` bytes.`));
assert.ok(brief.includes(`  \`${fixtureSha256}\``));
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;
assert.doesNotThrow(() => new AsyncFunction(cell));

const blockMatch = cell.match(
  /\/\/ BEGIN_V45_PURE_LISTING_DIAGNOSTIC\n([\s\S]*?)\n  \/\/ END_V45_PURE_LISTING_DIAGNOSTIC/,
);
assert.ok(blockMatch);
const inspectListingV45 = new Function(
  `${blockMatch[1]}\nreturn inspectListingV45;`,
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
  const result = inspectListingV45(value);
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
let currentListingFactory = ordinary;
const fixtureBrowser = {
  async documentation() {
    documentationCalls++;
    return documentation;
  },
  async nameSession(name) {
    nameCalls++;
    assert.equal(name, "OmniRoute V45 listing-shape diagnostic");
  },
  user: {
    async openTabs() {
      openTabsCalls++;
      return currentListingFactory();
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
  "const imported = globalThis.__v45FixtureImported;",
);
assert.notEqual(transformedCell, cell);
const runTransformedCell = async (prelude = "") => {
  const previousNodeRepl = globalThis.nodeRepl;
  globalThis.__v45FixtureImported = fixtureImported;
  globalThis.nodeRepl = {
    async write(value) {
      terminalWrites.push(value);
    },
  };
  try {
    await new AsyncFunction(`${prelude}${transformedCell}`)();
  } finally {
    delete globalThis.__v45FixtureImported;
    if (previousNodeRepl === undefined) delete globalThis.nodeRepl;
    else globalThis.nodeRepl = previousNodeRepl;
  }
};
await runTransformedCell();
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
assert.equal(terminal.result, "EXACT_V45_FIXED_LISTING_SHAPE_DIAGNOSTIC_CAPTURED");
assert.equal(terminal.errorClass, "NONE");
assert.equal(terminal.consumed, true);
assert.equal(terminal.bindingEligible, false);
assert.equal(terminal.bindingNull, true);
assert.equal(terminal.state, "V45_DIAGNOSTIC_CAPTURED_INELIGIBLE");
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

const resetFullCellFixture = () => {
  terminalWrites.length = 0;
  documentationCalls = 0;
  nameCalls = 0;
  openTabsCalls = 0;
};
for (const prelude of [
  "let secureConsoleV44Consumed = true;\n",
  "let secureConsoleAgentV35 = {};\n",
  "let secureConsoleChromeV41 = {};\n",
  "let secureConsoleOwnedTaskTabV35 = null;\n",
  "let secureConsoleOwnedTaskTabV44Eligible = false;\n",
  "let secureConsoleOwnedTaskTabV44State = \"DIRTY\";\n",
  "let secureConsoleOwnedTaskTabV44PreCreateDetachConsumed = false;\n",
  "let secureConsoleOwnedTaskTabV44PostNativeDetachConsumed = false;\n",
  "let secureConsoleSetupBrowserRuntimeV35 = () => {};\n",
  "let secureConsoleV35AttachmentExact = false;\n",
  "let secureConsoleCloudflareReadsV43Consumed = false;\n",
]) {
  resetFullCellFixture();
  await runTransformedCell(prelude);
  assert.equal(documentationCalls, 0);
  assert.equal(nameCalls, 0);
  assert.equal(openTabsCalls, 0);
  assert.equal(terminalWrites.length, 1);
  const contaminated = terminalWrites[0];
  assert.deepEqual(Object.keys(contaminated), expectedTerminalKeys);
  assert.equal(contaminated.result, "V45_FRESH_LISTING_SHAPE_DIAGNOSTIC_FAILED_STOP");
  assert.equal(contaminated.declarationShape, false);
  assert.equal(contaminated.consumed, true);
  assert.equal(contaminated.bindingEligible, false);
  assert.equal(contaminated.bindingNull, true);
  assert.equal(contaminated.state, "V45_DIAGNOSTIC_FAILED_INELIGIBLE");
  for (const key of [
    "importAttempted", "importFulfilled", "setupAttempted", "setupFulfilled",
    "connectAttempted", "connectFulfilled", "documentationAttempted",
    "documentationFulfilled", "documentationWriteAttempted",
    "documentationWriteFulfilled", "nameAttempted", "nameFulfilled",
    "openTabsAttempted", "openTabsFulfilled", "claimAttempted",
    "navigationAttempted", "urlAttempted", "snapshotAttempted",
  ]) assert.equal(contaminated[key], 0);
  assert.equal(contaminated.writeAttempted, 1);
}

const assertFixedFailure = async (thrown) => {
  resetFullCellFixture();
  currentListingFactory = () => new Proxy(ordinary(), {
    getPrototypeOf() {
      throw thrown;
    },
  });
  await runTransformedCell();
  assert.equal(documentationCalls, 1);
  assert.equal(nameCalls, 1);
  assert.equal(openTabsCalls, 1);
  assert.equal(terminalWrites.length, 2);
  assert.equal(terminalWrites[0], documentation);
  const failure = terminalWrites[1];
  assert.deepEqual(Object.keys(failure), expectedTerminalKeys);
  assert.equal(failure.result, "V45_FRESH_LISTING_SHAPE_DIAGNOSTIC_FAILED_STOP");
  assert.equal(failure.errorClass, "Error");
  assert.equal(failure.consumed, true);
  assert.equal(failure.bindingEligible, false);
  assert.equal(failure.bindingNull, true);
  assert.equal(failure.state, "V45_DIAGNOSTIC_FAILED_INELIGIBLE");
  assert.equal(JSON.stringify(failure).includes("ASecretLikeToken"), false);
  for (const key of [
    "importAttempted", "importFulfilled",
    "setupAttempted", "setupFulfilled",
    "connectAttempted", "connectFulfilled",
    "documentationAttempted", "documentationFulfilled",
    "documentationWriteAttempted", "documentationWriteFulfilled",
    "nameAttempted", "nameFulfilled",
    "openTabsAttempted", "openTabsFulfilled", "writeAttempted",
  ]) assert.equal(failure[key], 1);
  for (const key of [
    "claimAttempted", "navigationAttempted", "urlAttempted", "snapshotAttempted",
  ]) assert.equal(failure[key], 0);
};

await assertFixedFailure({ name: "ASecretLikeToken" });
let thrownNameGetterCalls = 0;
const getterThrown = {};
Object.defineProperty(getterThrown, "name", {
  get() {
    thrownNameGetterCalls++;
    throw new Error("thrown name getter invoked");
  },
});
await assertFixedFailure(getterThrown);
assert.equal(thrownNameGetterCalls, 0);

const report = {
  result: "V45_PURE_FIXTURES_PASS",
  briefBytes: Buffer.byteLength(brief),
  briefSha256: crypto.createHash("sha256").update(brief).digest("hex").toUpperCase(),
  executableBytes: Buffer.byteLength(cell),
  executableSha256: crypto.createHash("sha256").update(cell).digest("hex").toUpperCase(),
  fixtureBytes: fixture.length,
  fixtureSha256,
  syntax: "PASS",
  moduleShape: true,
  fixedSchema: true,
  getterCalls:
    indexGetterCalls + arrayGetCalls + recordGetCalls + thrownNameGetterCalls,
};
console.log(JSON.stringify(report));
