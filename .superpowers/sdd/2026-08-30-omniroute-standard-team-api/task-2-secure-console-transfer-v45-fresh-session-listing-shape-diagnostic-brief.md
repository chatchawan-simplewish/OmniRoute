# OmniRoute V45 fresh-session listing-shape diagnostic brief

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Purpose and predecessor

V44 is consumed and failed cleanly. Its fixed incident is commit `f5b11d7f7`
at `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v44-listing-validation-live-incident.md`.
V44 must never be retried, continued, reinterpreted, relaxed, or reused.

V44 proved that its sole `openTabs()` call fulfilled and that rejection
occurred inside its trusted array-or-record structural validation before a
bounded offered count or candidate count was returned. The exact rejecting
subpredicate remains **NOT PROVEN**.

V45 is the smallest new one-shot diagnostic. In one fresh Node realm it attaches
to the already user-offered Chrome profile/window/task-tab surface, reads the
complete pinned API documentation, names the session, calls `openTabs()` once,
and emits only fixed booleans and one bounded count that correspond to V44's
existing structural predicates. It never filters candidates, reads or emits a
tab field value, claims a tab, creates or closes a tab, navigates, waits, reads
a page URL or snapshot, or performs a provider action.

V45 is not executable until this exact committed brief receives independent
Sol High PASS with zero unresolved Critical, HIGH, or IMPORTANT findings,
followed by a non-self-referential execution classification and separate
post-commit coordinator tuple.

## Immutable runtime and API boundary

The only allowed module is
`C:/Users/chatc/.codex/plugins/cache/openai-bundled/chrome/26.831.21537/scripts/browser-client.mjs`.
Action time must reproduce `149771` bytes and SHA-256
`A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`.
The paired `docs/api.json` must reproduce `58480` bytes and SHA-256
`A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.

Candidate-package pins:

- Extracted executable length: `18106` normalized UTF-8 bytes.
- Extracted executable SHA-256:
  `D30020117449F9738B89EB6F1D9834A9BD19675EE903505C20C42D00F770C838`.
- Pure fixture:
  `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v45-pure-fixtures.mjs`.
- Pure fixture length: `15043` bytes.
- Pure fixture SHA-256:
  `B37CCD1783887DB149B792A4712E750F01A6536F159323236BCE4B31BE2B2EF4`.

The fixture terminal must directly emit the brief, executable, and fixture
byte/hash tuple. The brief hash is intentionally not embedded here.

The complete documentation must be read through `Browser.documentation()` and
written once to the terminal before session naming or enumeration. The exact
reviewed API declares `browsers.get(id)`, `Browser.nameSession(name)`,
`Browser.user`, and `BrowserUser.openTabs()`. `openTabs()` returns
`Array<BrowserUserTabInfo>` ordered by `lastOpened` descending. The documented
record keys are only `id`, `lastOpened`, `providerTabId`, `tabGroup`, `title`,
and `url`; `id` is required and every documented value is a string.

## Fixed diagnostic semantics

- All output property names are fixed in the executable below.
- `offeredCount` remains `-1` unless the own `length` descriptor is a bounded
  data value in `[1,1000]`; no direct `value.length` read is allowed.
- Array indices are accessed only through cached own data descriptors. No
  untrusted iterator, getter, setter, `for...of`, spread, `map`, `filter`,
  `reduce`, callback enumerator, or direct indexed property read is allowed.
- Record keys and descriptors may be inspected only after the cached index
  descriptor proves an own data value. No record field value may be emitted.
- `allRecordValuesV37Safe` retains its historical field name and reproduces the
  V44 rule: every own documented field
  must be a non-empty bounded control-free string.
- `allOptionalValuesStringOrUndefined` separately identifies the only benign
  optional-field representation that V44 did not allow, without identifying a
  record, key occurrence, or value.
- A captured diagnostic is permanently ineligible for tab adoption. Success
  means the fixed diagnostic was captured, not that any structural predicate
  passed.
- The outer catch never inspects, stringifies, coerces, prototype-tests, or
  reads a property from the thrown value. It assigns only literal `"Error"`.
- Every thrown or transport-uncertain outcome consumes V45 and requires Node
  realm disposal. There is no retry, fallback, manual inspection, raw-output
  relaxation, or continuation.

## Exact one-cell executable

The following is the sole V45 executable source.

~~~javascript
let secureConsoleSetupBrowserRuntimeV45 = null;
let secureConsoleAgentV45 = null;
let secureConsoleChromeV45 = null;
let secureConsoleOwnedTaskTabV45 = null;
let secureConsoleOwnedTaskTabV45Eligible = false;
let secureConsoleV45Consumed = false;
let secureConsoleV45State = "UNCREATED";
await (async () => {
  const gateWasFresh = secureConsoleV45Consumed === false;
  secureConsoleV45Consumed = true;
  const counters = {
    importAttempted: 0, importFulfilled: 0,
    setupAttempted: 0, setupFulfilled: 0,
    connectAttempted: 0, connectFulfilled: 0,
    documentationAttempted: 0, documentationFulfilled: 0,
    documentationWriteAttempted: 0, documentationWriteFulfilled: 0,
    nameAttempted: 0, nameFulfilled: 0,
    openTabsAttempted: 0, openTabsFulfilled: 0,
    claimAttempted: 0, navigationAttempted: 0,
    urlAttempted: 0, snapshotAttempted: 0,
    writeAttempted: 0,
  };
  let result = "V45_FRESH_LISTING_SHAPE_DIAGNOSTIC_FAILED_STOP";
  let declarationShape = false;
  let moduleShape = false;
  let agentShape = false;
  let connectedShape = false;
  let documentationValidated = false;
  let documentationLength = -1;
  let sessionNamed = false;
  let arrayIsArray = null;
  let arrayPrototypeExact = null;
  let arraySymbolsZero = null;
  let lengthDescriptorPresent = null;
  let lengthDescriptorData = null;
  let lengthDescriptorNonEnumerable = null;
  let lengthDescriptorSafeBounded = null;
  let offeredCount = -1;
  let arrayOwnNamesReadable = null;
  let arrayNameCountExact = null;
  let arrayNamesExpectedOnly = null;
  let allIndexDescriptorsPresent = null;
  let allIndexDescriptorsData = null;
  let allIndexDescriptorsEnumerable = null;
  let allRecordsPlain = null;
  let allRecordSymbolsZero = null;
  let allRecordKeysAllowedWithId = null;
  let allRecordDescriptorsPresent = null;
  let allRecordDescriptorsData = null;
  let allRecordDescriptorsEnumerable = null;
  let allRecordIdsV37Safe = null;
  let allRecordUrlsAbsentOrV37Safe = null;
  let allOptionalValuesStringOrUndefined = null;
  let allRecordValuesV37Safe = null;
  let errorClass = "NONE";
  // BEGIN_V45_PURE_LISTING_DIAGNOSTIC
  const inspectListingV45 = (offered) => {
    const diagnostic = {
      arrayIsArray: null,
      arrayPrototypeExact: null,
      arraySymbolsZero: null,
      lengthDescriptorPresent: null,
      lengthDescriptorData: null,
      lengthDescriptorNonEnumerable: null,
      lengthDescriptorSafeBounded: null,
      offeredCount: -1,
      arrayOwnNamesReadable: null,
      arrayNameCountExact: null,
      arrayNamesExpectedOnly: null,
      allIndexDescriptorsPresent: null,
      allIndexDescriptorsData: null,
      allIndexDescriptorsEnumerable: null,
      allRecordsPlain: null,
      allRecordSymbolsZero: null,
      allRecordKeysAllowedWithId: null,
      allRecordDescriptorsPresent: null,
      allRecordDescriptorsData: null,
      allRecordDescriptorsEnumerable: null,
      allRecordIdsV37Safe: null,
      allRecordUrlsAbsentOrV37Safe: null,
      allOptionalValuesStringOrUndefined: null,
      allRecordValuesV37Safe: null,
    };
    const v37SafeString = (key, value) => {
      const limit = key === "url" ? 16384 : key === "title" ? 4096 : 512;
      return typeof value === "string" && value.length > 0 &&
        value.length <= limit && !/[\u0000-\u001f\u007f]/.test(value);
    };
    const plainRecord = (value) => {
      if (typeof value !== "object" || value === null) return false;
      const prototype = Object.getPrototypeOf(value);
      return prototype === null ||
        (prototype !== null && Object.getPrototypeOf(prototype) === null);
    };

    diagnostic.arrayIsArray = Array.isArray(offered);
    if (!diagnostic.arrayIsArray) return diagnostic;
    diagnostic.arrayPrototypeExact =
      Object.getPrototypeOf(offered) === Array.prototype;
    diagnostic.arraySymbolsZero =
      Object.getOwnPropertySymbols(offered).length === 0;
    const lengthDescriptor =
      Object.getOwnPropertyDescriptor(offered, "length");
    diagnostic.lengthDescriptorPresent = lengthDescriptor !== undefined;
    diagnostic.lengthDescriptorData =
      diagnostic.lengthDescriptorPresent &&
      Object.prototype.hasOwnProperty.call(lengthDescriptor, "value");
    diagnostic.lengthDescriptorNonEnumerable =
      diagnostic.lengthDescriptorPresent &&
      lengthDescriptor.enumerable === false;
    diagnostic.lengthDescriptorSafeBounded =
      diagnostic.lengthDescriptorData &&
      Number.isSafeInteger(lengthDescriptor.value) &&
      lengthDescriptor.value >= 1 && lengthDescriptor.value <= 1000;
    if (!diagnostic.lengthDescriptorSafeBounded) return diagnostic;

    diagnostic.offeredCount = lengthDescriptor.value;
    const arrayNames = Object.getOwnPropertyNames(offered);
    diagnostic.arrayOwnNamesReadable = true;
    diagnostic.arrayNameCountExact =
      arrayNames.length === diagnostic.offeredCount + 1;
    const expectedNames = new Set(["length"]);
    for (let index = 0; index < diagnostic.offeredCount; index++) {
      expectedNames.add(String(index));
    }
    diagnostic.arrayNamesExpectedOnly = true;
    for (let index = 0; index < arrayNames.length; index++) {
      if (!expectedNames.has(arrayNames[index])) {
        diagnostic.arrayNamesExpectedOnly = false;
      }
    }

    const indexDescriptors = [];
    diagnostic.allIndexDescriptorsPresent = true;
    diagnostic.allIndexDescriptorsData = true;
    diagnostic.allIndexDescriptorsEnumerable = true;
    for (let index = 0; index < diagnostic.offeredCount; index++) {
      const descriptor =
        Object.getOwnPropertyDescriptor(offered, String(index));
      indexDescriptors.push(descriptor);
      if (descriptor === undefined) {
        diagnostic.allIndexDescriptorsPresent = false;
        diagnostic.allIndexDescriptorsData = false;
        diagnostic.allIndexDescriptorsEnumerable = false;
        continue;
      }
      if (!Object.prototype.hasOwnProperty.call(descriptor, "value")) {
        diagnostic.allIndexDescriptorsData = false;
      }
      if (descriptor.enumerable !== true) {
        diagnostic.allIndexDescriptorsEnumerable = false;
      }
    }
    if (!diagnostic.allIndexDescriptorsPresent ||
        !diagnostic.allIndexDescriptorsData) return diagnostic;

    diagnostic.allRecordsPlain = true;
    for (let index = 0; index < indexDescriptors.length; index++) {
      if (!plainRecord(indexDescriptors[index].value)) {
        diagnostic.allRecordsPlain = false;
      }
    }
    if (!diagnostic.allRecordsPlain) return diagnostic;

    const allowed = new Set([
      "id", "lastOpened", "providerTabId", "tabGroup", "title", "url",
    ]);
    diagnostic.allRecordSymbolsZero = true;
    diagnostic.allRecordKeysAllowedWithId = true;
    diagnostic.allRecordDescriptorsPresent = true;
    diagnostic.allRecordDescriptorsData = true;
    diagnostic.allRecordDescriptorsEnumerable = true;
    diagnostic.allRecordIdsV37Safe = true;
    diagnostic.allRecordUrlsAbsentOrV37Safe = true;
    diagnostic.allOptionalValuesStringOrUndefined = true;
    diagnostic.allRecordValuesV37Safe = true;
    for (let index = 0; index < indexDescriptors.length; index++) {
      const item = indexDescriptors[index].value;
      if (Object.getOwnPropertySymbols(item).length !== 0) {
        diagnostic.allRecordSymbolsZero = false;
      }
      const keys = Object.getOwnPropertyNames(item);
      let hasId = false;
      for (let keyIndex = 0; keyIndex < keys.length; keyIndex++) {
        const key = keys[keyIndex];
        const keyAllowed = allowed.has(key);
        const optionalAllowed = keyAllowed && key !== "id";
        if (key === "id") hasId = true;
        if (!keyAllowed) diagnostic.allRecordKeysAllowedWithId = false;
        const descriptor = Object.getOwnPropertyDescriptor(item, key);
        if (descriptor === undefined) {
          diagnostic.allRecordDescriptorsPresent = false;
          diagnostic.allRecordDescriptorsData = false;
          diagnostic.allRecordDescriptorsEnumerable = false;
          diagnostic.allRecordValuesV37Safe = false;
          if (key === "id") diagnostic.allRecordIdsV37Safe = false;
          if (key === "url") {
            diagnostic.allRecordUrlsAbsentOrV37Safe = false;
          }
          if (optionalAllowed) {
            diagnostic.allOptionalValuesStringOrUndefined = false;
          }
          continue;
        }
        const data =
          Object.prototype.hasOwnProperty.call(descriptor, "value");
        if (!data) diagnostic.allRecordDescriptorsData = false;
        if (descriptor.enumerable !== true) {
          diagnostic.allRecordDescriptorsEnumerable = false;
        }
        if (!data) {
          diagnostic.allRecordValuesV37Safe = false;
          if (key === "id") diagnostic.allRecordIdsV37Safe = false;
          if (key === "url") {
            diagnostic.allRecordUrlsAbsentOrV37Safe = false;
          }
          if (optionalAllowed) {
            diagnostic.allOptionalValuesStringOrUndefined = false;
          }
          continue;
        }
        const value = descriptor.value;
        const safe = v37SafeString(key, value);
        if (!safe) diagnostic.allRecordValuesV37Safe = false;
        if (key === "id" && !safe) diagnostic.allRecordIdsV37Safe = false;
        if (key === "url" && !safe) {
          diagnostic.allRecordUrlsAbsentOrV37Safe = false;
        }
        if (optionalAllowed &&
            !(typeof value === "string" || value === undefined)) {
          diagnostic.allOptionalValuesStringOrUndefined = false;
        }
      }
      if (!hasId) {
        diagnostic.allRecordKeysAllowedWithId = false;
        diagnostic.allRecordIdsV37Safe = false;
      }
    }
    return diagnostic;
  };
  // END_V45_PURE_LISTING_DIAGNOSTIC
  try {
    declarationShape =
      gateWasFresh === true &&
      typeof secureConsoleV35AttachmentConsumed === "undefined" &&
      typeof secureConsoleV35AdoptionConsumed === "undefined" &&
      typeof secureConsoleV36Consumed === "undefined" &&
      typeof secureConsoleV37Consumed === "undefined" &&
      typeof secureConsoleV38Consumed === "undefined" &&
      typeof secureConsoleV39Consumed === "undefined" &&
      typeof secureConsoleV40Consumed === "undefined" &&
      typeof secureConsoleV41Consumed === "undefined" &&
      typeof secureConsoleV42Consumed === "undefined" &&
      typeof secureConsoleV43Consumed === "undefined" &&
      typeof secureConsoleV44Consumed === "undefined" &&
      typeof secureConsoleOwnedTaskTabV38 === "undefined" &&
      typeof secureConsoleOwnedTaskTabV39 === "undefined" &&
      typeof secureConsoleOwnedTaskTabV40 === "undefined" &&
      typeof secureConsoleOwnedTaskTabV41 === "undefined" &&
      typeof secureConsoleOwnedTaskTabV42 === "undefined" &&
      typeof secureConsoleOwnedTaskTabV43 === "undefined" &&
      typeof secureConsoleOwnedTaskTabV44 === "undefined" &&
      typeof secureConsoleSetupBrowserRuntimeV38 === "undefined" &&
      typeof secureConsoleSetupBrowserRuntimeV39 === "undefined" &&
      typeof secureConsoleSetupBrowserRuntimeV40 === "undefined" &&
      typeof secureConsoleSetupBrowserRuntimeV41 === "undefined" &&
      typeof secureConsoleCloudflareReadsV42Consumed === "undefined" &&
      typeof secureConsoleCloudflareReadsV43Consumed === "undefined" &&
      typeof secureConsoleCloudflareReadsV44Consumed === "undefined" &&
      secureConsoleSetupBrowserRuntimeV45 === null &&
      secureConsoleAgentV45 === null &&
      secureConsoleChromeV45 === null &&
      secureConsoleOwnedTaskTabV45 === null &&
      secureConsoleOwnedTaskTabV45Eligible === false &&
      secureConsoleV45State === "UNCREATED";
    if (!declarationShape) throw new Error("FreshRealmDeclarationError");
    secureConsoleV45State = "V45_CONSUMING";

    counters.importAttempted++;
    const imported = await import(
      "file:///C:/Users/chatc/.codex/plugins/cache/openai-bundled/chrome/26.831.21537/scripts/browser-client.mjs"
    );
    counters.importFulfilled++;
    moduleShape = typeof imported === "object" && imported !== null &&
      typeof imported.setupBrowserRuntime === "function";
    if (!moduleShape) throw new Error("BrowserModuleShapeError");
    secureConsoleSetupBrowserRuntimeV45 = imported.setupBrowserRuntime;

    counters.setupAttempted++;
    secureConsoleAgentV45 = await secureConsoleSetupBrowserRuntimeV45();
    counters.setupFulfilled++;
    agentShape =
      typeof secureConsoleAgentV45 === "object" &&
      secureConsoleAgentV45 !== null &&
      typeof secureConsoleAgentV45.browsers?.get === "function";
    if (!agentShape) throw new Error("BrowserAgentShapeError");

    counters.connectAttempted++;
    secureConsoleChromeV45 = await secureConsoleAgentV45.browsers.get("chrome");
    counters.connectFulfilled++;
    connectedShape =
      typeof secureConsoleChromeV45 === "object" &&
      secureConsoleChromeV45 !== null &&
      typeof secureConsoleChromeV45.documentation === "function" &&
      typeof secureConsoleChromeV45.nameSession === "function" &&
      typeof secureConsoleChromeV45.user?.openTabs === "function";
    if (!connectedShape) throw new Error("ConnectedBrowserShapeError");

    counters.documentationAttempted++;
    const documentation = await secureConsoleChromeV45.documentation();
    counters.documentationFulfilled++;
    documentationValidated =
      typeof documentation === "string" &&
      documentation.length >= 40000 && documentation.length <= 50000 &&
      documentation.includes("openTabs(): Promise<Array<BrowserUserTabInfo>>") &&
      documentation.includes("id: string") &&
      documentation.includes("lastOpened?: string") &&
      documentation.includes("providerTabId?: string") &&
      documentation.includes("tabGroup?: string") &&
      documentation.includes("title?: string") &&
      documentation.includes("url?: string");
    documentationLength = documentationValidated ? documentation.length : -1;
    if (!documentationValidated) {
      throw new Error("CompleteDocumentationValidationError");
    }
    counters.documentationWriteAttempted++;
    await nodeRepl.write(documentation);
    counters.documentationWriteFulfilled++;

    counters.nameAttempted++;
    await secureConsoleChromeV45.nameSession(
      "OmniRoute V45 listing-shape diagnostic",
    );
    counters.nameFulfilled++;
    sessionNamed = true;

    counters.openTabsAttempted++;
    const offered = await secureConsoleChromeV45.user.openTabs();
    counters.openTabsFulfilled++;

    ({
      arrayIsArray,
      arrayPrototypeExact,
      arraySymbolsZero,
      lengthDescriptorPresent,
      lengthDescriptorData,
      lengthDescriptorNonEnumerable,
      lengthDescriptorSafeBounded,
      offeredCount,
      arrayOwnNamesReadable,
      arrayNameCountExact,
      arrayNamesExpectedOnly,
      allIndexDescriptorsPresent,
      allIndexDescriptorsData,
      allIndexDescriptorsEnumerable,
      allRecordsPlain,
      allRecordSymbolsZero,
      allRecordKeysAllowedWithId,
      allRecordDescriptorsPresent,
      allRecordDescriptorsData,
      allRecordDescriptorsEnumerable,
      allRecordIdsV37Safe,
      allRecordUrlsAbsentOrV37Safe,
      allOptionalValuesStringOrUndefined,
      allRecordValuesV37Safe,
    } = inspectListingV45(offered));

    const exactCounters =
      counters.importAttempted === 1 && counters.importFulfilled === 1 &&
      counters.setupAttempted === 1 && counters.setupFulfilled === 1 &&
      counters.connectAttempted === 1 && counters.connectFulfilled === 1 &&
      counters.documentationAttempted === 1 &&
      counters.documentationFulfilled === 1 &&
      counters.documentationWriteAttempted === 1 &&
      counters.documentationWriteFulfilled === 1 &&
      counters.nameAttempted === 1 && counters.nameFulfilled === 1 &&
      counters.openTabsAttempted === 1 && counters.openTabsFulfilled === 1 &&
      counters.claimAttempted === 0 && counters.navigationAttempted === 0 &&
      counters.urlAttempted === 0 && counters.snapshotAttempted === 0;
    if (!exactCounters) throw new Error("V45CompletenessError");
    result = "EXACT_V45_FIXED_LISTING_SHAPE_DIAGNOSTIC_CAPTURED";
  } catch {
    errorClass = "Error";
  }

  secureConsoleSetupBrowserRuntimeV45 = null;
  secureConsoleAgentV45 = null;
  secureConsoleChromeV45 = null;
  secureConsoleOwnedTaskTabV45 = null;
  secureConsoleOwnedTaskTabV45Eligible = false;
  secureConsoleV45State = result ===
      "EXACT_V45_FIXED_LISTING_SHAPE_DIAGNOSTIC_CAPTURED"
    ? "V45_DIAGNOSTIC_CAPTURED_INELIGIBLE"
    : "V45_DIAGNOSTIC_FAILED_INELIGIBLE";
  counters.writeAttempted++;
  try {
    await nodeRepl.write({
      result,
      declarationShape,
      moduleShape,
      agentShape,
      connectedShape,
      documentationValidated,
      documentationLength,
      sessionNamed,
      arrayIsArray,
      arrayPrototypeExact,
      arraySymbolsZero,
      lengthDescriptorPresent,
      lengthDescriptorData,
      lengthDescriptorNonEnumerable,
      lengthDescriptorSafeBounded,
      offeredCount,
      arrayOwnNamesReadable,
      arrayNameCountExact,
      arrayNamesExpectedOnly,
      allIndexDescriptorsPresent,
      allIndexDescriptorsData,
      allIndexDescriptorsEnumerable,
      allRecordsPlain,
      allRecordSymbolsZero,
      allRecordKeysAllowedWithId,
      allRecordDescriptorsPresent,
      allRecordDescriptorsData,
      allRecordDescriptorsEnumerable,
      allRecordIdsV37Safe,
      allRecordUrlsAbsentOrV37Safe,
      allOptionalValuesStringOrUndefined,
      allRecordValuesV37Safe,
      ...counters,
      errorClass,
      consumed: secureConsoleV45Consumed,
      bindingEligible: secureConsoleOwnedTaskTabV45Eligible,
      bindingNull: secureConsoleOwnedTaskTabV45 === null,
      state: secureConsoleV45State,
    });
  } catch (terminalError) {
    secureConsoleSetupBrowserRuntimeV45 = null;
    secureConsoleAgentV45 = null;
    secureConsoleChromeV45 = null;
    secureConsoleOwnedTaskTabV45 = null;
    secureConsoleOwnedTaskTabV45Eligible = false;
    secureConsoleV45State = "V45_FINAL_OUTPUT_FAILED_STOP";
    throw terminalError;
  }
})();
~~~

## Required offline syntax and pure-fixture check

The committed fixture is
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v45-pure-fixtures.mjs`.
It reads this committed working-tree brief, requires exactly one JavaScript
cell, normalizes that cell to LF, constructs an `AsyncFunction` without
invoking it, extracts the exact marked `inspectListingV45` helper from that
cell, and runs the helper only against synthetic values. It imports the pinned
module without calling setup and proves the corrected module namespace shape.
It also replaces only the dynamic-import expression in memory, executes that
transformed cell with inert setup/browser/documentation/listing/terminal stubs,
and proves the exact terminal schema, success counters, permanent ineligibility,
binding cleanup, and zero action counters. It performs no real browser setup,
Chrome get, enumeration, provider, network, or VM action.

Run it from the worktree root with:

```powershell
node .superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v45-pure-fixtures.mjs
```

The sole acceptable result is one JSON object with
`result="V45_PURE_FIXTURES_PASS"`, `syntax="PASS"`, `moduleShape=true`,
`fixedSchema=true`, and `getterCalls=0`, plus the current bounded brief and
executable byte/hash pins.

The fixture matrix must remain exact and passing for ordinary and foreign-realm
Arrays; array symbols; empty/oversize length; unexpected names; holes; index
accessors and non-enumerable indices; ordinary, null-prototype, and non-plain
records; record symbols; missing and unexpected keys; unstable missing
descriptors; enumerable and non-enumerable record accessors; optional
`undefined`; empty, oversize, and control-bearing values; fixed schema; and
traps proving no getter, iterator, or direct array/record property read. A
foreign-realm fixture is only a diagnostic expectation and is not evidence
about the live listing. The inert full-cell fixture must also prove one each of
documentation, session naming, and enumeration, exact fixed terminal schema,
success/consume/cleanup state, and zero claim/navigation/URL/snapshot actions.
It also proves a V44 declaration contaminant consumes and stops before import,
documentation, session naming, or enumeration.
Two inert reflection-failure fixtures must throw, respectively, a plain object
with data `name="ASecretLikeToken"` and an object whose `name` getter itself
throws. Both must produce exactly one fixed failure terminal after the required
documentation write, emit literal `errorClass="Error"`, contain no thrown data,
invoke the getter zero times, preserve exact failure counters, clear every
binding, and end consumed/permanently ineligible.

## Action-time pins and single-use procedure

Immediately before any live send, the sole Sol High owner must prove and record:

1. this brief and fixture's commit, paths, blobs, bytes, and SHA-256; exactly one
   extracted executable; its normalized UTF-8 bytes and SHA-256; exact syntax
   PASS; and exact `V45_PURE_FIXTURES_PASS` output with every fixed field above;
2. an independent Sol High PASS review of these exact committed bytes, with zero
   unresolved Critical, HIGH, or IMPORTANT findings;
3. a later non-self-referential execution-classification commit whose parent is
   the PASS review commit, followed by a separate post-commit tuple proving the
   exact one-path classification commit, empty index, exact 12-path dirty
   baseline, and stable projection `10661` records / SHA-256
   `C4C85893769D133224AC7404B628C8B0D4B0EBBFF471620B158E652E152B4EBD`;
4. the exact runtime module/docs pins above and the reviewed API declarations;
5. clean evidence worktree HEAD
   `80adaa7d5d63d1d2c7bfa63b236c6bee93b3b1d8`;
6. Windows residue zero, VM1205's full safe checkpoint, and public A/CNAME zero
   through both `1.1.1.1` and `8.8.8.8`;
7. the owner's exact confirmation that Chrome Profile
   `Codex-Chrome-Bell-PC2`, the intended window, and intended task tab are
   selected and no other Chrome profile/window is offered to the extension;
8. a freshly reset Node realm in which every named V35-V45 declaration
   is absent; and
9. byte-for-byte extraction of exactly the sole fenced executable above.

The first executable statement consumes V45 before import or attachment. Send
the exact cell once. Do not inspect Chrome, list tabs by any other path, retry,
reconnect, reacquire, claim, navigate, or perform provider actions outside that
cell. Capture only its fixed terminal object. Then run one state-only cleanup
query proving consumed true, setup/agent/browser bindings null, exact terminal
state, permanent ineligibility, and no retained tab binding; reset the Node
realm immediately afterward.

Any missing, false, malformed, surprising, incomplete, thrown, timed-out, or
transport-uncertain result is a consumed failure. Stop, dispose of the realm,
record a sanitized fixed-schema incident, and require a new reviewed contract.

## Secret, confirmation, and no-residue boundary

V45 handles no secret and performs no credential, token, provider, DNS, route,
proxy, listener, tunnel, VM, or repository-product mutation. It must never
print, commit, log, or infer a secret or raw tab metadata. The final later
Create/native Copy/native masked Paste confirmation and the separate later
exact-row deletion confirmation remain mandatory and cannot be pre-approved,
automated, delegated, or waived by V45.

Session naming is the only permitted browser-session side effect and is
non-provider-persistent. No background process or owner may remain. V45 can
only classify the structural mismatch for a separately reviewed successor; it
cannot authorize attachment reuse, tab adoption, or provider execution.
