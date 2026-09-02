# OmniRoute V38 fresh-session listing-shape diagnostic brief

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Purpose and predecessor

V37 is consumed and failed cleanly. Its fixed incident is commit
`2389694b7043adcb6ac31a74376f695ad8800d7f` at
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v37-listing-shape-live-incident.md`.
V37 must never be retried, continued, reinterpreted, relaxed, or reused.

V37 proved that its sole `openTabs()` call fulfilled and that rejection
occurred inside its trusted array-or-record structural validation before a
bounded offered count or candidate count was returned. The exact rejecting
subpredicate remains **NOT PROVEN**.

V38 is the smallest new one-shot diagnostic. In one fresh Node realm it attaches
to the already user-offered Chrome profile/window/task-tab surface, reads the
complete pinned API documentation, names the session, calls `openTabs()` once,
and emits only fixed booleans and one bounded count that correspond to V37's
existing structural predicates. It never filters candidates, reads or emits a
tab field value, claims a tab, creates or closes a tab, navigates, waits, reads
a page URL or snapshot, or performs a provider action.

V38 is not executable until this exact committed brief receives independent
Sol High PASS with zero unresolved Critical, HIGH, or IMPORTANT findings,
followed by a non-self-referential execution classification and separate
post-commit coordinator tuple.

## Immutable runtime and API boundary

The only allowed module is
`C:/Users/chatc/.codex/plugins/cache/openai-bundled/chrome/26.831.20005/scripts/browser-client.mjs`.
Action time must reproduce `149771` bytes and SHA-256
`A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`.
The paired `docs/api.json` must reproduce `58480` bytes and SHA-256
`A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.

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
- `allRecordValuesV37Safe` reproduces the V37 rule: every own documented field
  must be a non-empty bounded control-free string.
- `allOptionalValuesStringOrUndefined` separately identifies the only benign
  optional-field representation that V37 did not allow, without identifying a
  record, key occurrence, or value.
- A captured diagnostic is permanently ineligible for tab adoption. Success
  means the fixed diagnostic was captured, not that any structural predicate
  passed.
- Every thrown or transport-uncertain outcome consumes V38 and requires Node
  realm disposal. There is no retry, fallback, manual inspection, raw-output
  relaxation, or continuation.

## Exact one-cell executable

The following is the sole V38 executable source.

~~~javascript
let secureConsoleSetupBrowserRuntimeV38 = null;
let secureConsoleAgentV38 = null;
let secureConsoleChromeV38 = null;
let secureConsoleOwnedTaskTabV38 = null;
let secureConsoleOwnedTaskTabV38Eligible = false;
let secureConsoleV38Consumed = false;
let secureConsoleV38State = "UNCREATED";
await (async () => {
  const gateWasFresh = secureConsoleV38Consumed === false;
  secureConsoleV38Consumed = true;
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
  let result = "V38_FRESH_LISTING_SHAPE_DIAGNOSTIC_FAILED_STOP";
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
  const safeErrorClass = (error) => {
    const name = typeof error?.name === "string" ? error.name : "Error";
    return /^[A-Za-z][A-Za-z0-9_]{0,63}$/.test(name) ? name : "Error";
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
  try {
    declarationShape =
      gateWasFresh === true &&
      typeof secureConsoleV35AttachmentConsumed === "undefined" &&
      typeof secureConsoleV35AdoptionConsumed === "undefined" &&
      typeof secureConsoleV36Consumed === "undefined" &&
      typeof secureConsoleV37Consumed === "undefined" &&
      secureConsoleSetupBrowserRuntimeV38 === null &&
      secureConsoleAgentV38 === null &&
      secureConsoleChromeV38 === null &&
      secureConsoleOwnedTaskTabV38 === null &&
      secureConsoleOwnedTaskTabV38Eligible === false &&
      secureConsoleV38State === "UNCREATED";
    if (!declarationShape) throw new Error("FreshRealmDeclarationError");
    secureConsoleV38State = "V38_CONSUMING";

    counters.importAttempted++;
    const imported = await import(
      "file:///C:/Users/chatc/.codex/plugins/cache/openai-bundled/chrome/26.831.20005/scripts/browser-client.mjs"
    );
    counters.importFulfilled++;
    moduleShape =
      typeof imported.setupBrowserRuntime === "function" &&
      imported.BROWSER_CLIENT_ID === "chrome";
    if (!moduleShape) throw new Error("BrowserModuleShapeError");
    secureConsoleSetupBrowserRuntimeV38 = imported.setupBrowserRuntime;

    counters.setupAttempted++;
    secureConsoleAgentV38 = await secureConsoleSetupBrowserRuntimeV38({
      transport: "cdp",
    });
    counters.setupFulfilled++;
    agentShape =
      typeof secureConsoleAgentV38 === "object" &&
      secureConsoleAgentV38 !== null &&
      typeof secureConsoleAgentV38.browsers?.get === "function";
    if (!agentShape) throw new Error("BrowserAgentShapeError");

    counters.connectAttempted++;
    secureConsoleChromeV38 = await secureConsoleAgentV38.browsers.get("chrome");
    counters.connectFulfilled++;
    connectedShape =
      typeof secureConsoleChromeV38 === "object" &&
      secureConsoleChromeV38 !== null &&
      typeof secureConsoleChromeV38.documentation === "function" &&
      typeof secureConsoleChromeV38.nameSession === "function" &&
      typeof secureConsoleChromeV38.user?.openTabs === "function";
    if (!connectedShape) throw new Error("ConnectedBrowserShapeError");

    counters.documentationAttempted++;
    const documentation = await secureConsoleChromeV38.documentation();
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
    await secureConsoleChromeV38.nameSession(
      "OmniRoute V38 listing-shape diagnostic",
    );
    counters.nameFulfilled++;
    sessionNamed = true;

    counters.openTabsAttempted++;
    const offered = await secureConsoleChromeV38.user.openTabs();
    counters.openTabsFulfilled++;

    arrayIsArray = Array.isArray(offered);
    if (arrayIsArray) {
      arrayPrototypeExact = Object.getPrototypeOf(offered) === Array.prototype;
      arraySymbolsZero = Object.getOwnPropertySymbols(offered).length === 0;
      const lengthDescriptor =
        Object.getOwnPropertyDescriptor(offered, "length");
      lengthDescriptorPresent = lengthDescriptor !== undefined;
      lengthDescriptorData = lengthDescriptorPresent &&
        Object.prototype.hasOwnProperty.call(lengthDescriptor, "value");
      lengthDescriptorNonEnumerable = lengthDescriptorPresent &&
        lengthDescriptor.enumerable === false;
      lengthDescriptorSafeBounded = lengthDescriptorData &&
        Number.isSafeInteger(lengthDescriptor.value) &&
        lengthDescriptor.value >= 1 && lengthDescriptor.value <= 1000;
      if (lengthDescriptorSafeBounded) {
        offeredCount = lengthDescriptor.value;
        const arrayNames = Object.getOwnPropertyNames(offered);
        arrayOwnNamesReadable = true;
        arrayNameCountExact = arrayNames.length === offeredCount + 1;
        const expectedNames = new Set(["length"]);
        for (let index = 0; index < offeredCount; index++) {
          expectedNames.add(String(index));
        }
        arrayNamesExpectedOnly = true;
        for (let index = 0; index < arrayNames.length; index++) {
          if (!expectedNames.has(arrayNames[index])) {
            arrayNamesExpectedOnly = false;
          }
        }

        const indexDescriptors = [];
        allIndexDescriptorsPresent = true;
        allIndexDescriptorsData = true;
        allIndexDescriptorsEnumerable = true;
        for (let index = 0; index < offeredCount; index++) {
          const descriptor =
            Object.getOwnPropertyDescriptor(offered, String(index));
          indexDescriptors.push(descriptor);
          if (descriptor === undefined) allIndexDescriptorsPresent = false;
          if (descriptor === undefined ||
              !Object.prototype.hasOwnProperty.call(descriptor, "value")) {
            allIndexDescriptorsData = false;
          }
          if (descriptor === undefined || descriptor.enumerable !== true) {
            allIndexDescriptorsEnumerable = false;
          }
        }

        if (allIndexDescriptorsPresent && allIndexDescriptorsData) {
          const allowed = new Set([
            "id", "lastOpened", "providerTabId", "tabGroup", "title", "url",
          ]);
          allRecordsPlain = true;
          allRecordSymbolsZero = true;
          allRecordKeysAllowedWithId = true;
          allRecordDescriptorsPresent = true;
          allRecordDescriptorsData = true;
          allRecordDescriptorsEnumerable = true;
          allRecordIdsV37Safe = true;
          allRecordUrlsAbsentOrV37Safe = true;
          allOptionalValuesStringOrUndefined = true;
          allRecordValuesV37Safe = true;
          for (let index = 0; index < indexDescriptors.length; index++) {
            const item = indexDescriptors[index].value;
            const itemPlain = plainRecord(item);
            if (!itemPlain) {
              allRecordsPlain = false;
              allRecordSymbolsZero = false;
              allRecordKeysAllowedWithId = false;
              allRecordDescriptorsPresent = false;
              allRecordDescriptorsData = false;
              allRecordDescriptorsEnumerable = false;
              allRecordIdsV37Safe = false;
              allRecordUrlsAbsentOrV37Safe = false;
              allOptionalValuesStringOrUndefined = false;
              allRecordValuesV37Safe = false;
              continue;
            }
            if (Object.getOwnPropertySymbols(item).length !== 0) {
              allRecordSymbolsZero = false;
            }
            const keys = Object.getOwnPropertyNames(item);
            let hasId = false;
            for (let keyIndex = 0; keyIndex < keys.length; keyIndex++) {
              const key = keys[keyIndex];
              if (key === "id") hasId = true;
              if (!allowed.has(key)) allRecordKeysAllowedWithId = false;
              const descriptor = Object.getOwnPropertyDescriptor(item, key);
              if (descriptor === undefined) {
                allRecordDescriptorsPresent = false;
                allRecordDescriptorsData = false;
                allRecordDescriptorsEnumerable = false;
                allRecordValuesV37Safe = false;
                if (key === "id") allRecordIdsV37Safe = false;
                if (key === "url") allRecordUrlsAbsentOrV37Safe = false;
                continue;
              }
              const data =
                Object.prototype.hasOwnProperty.call(descriptor, "value");
              if (!data) {
                allRecordDescriptorsData = false;
                allRecordValuesV37Safe = false;
                if (key === "id") allRecordIdsV37Safe = false;
                if (key === "url") allRecordUrlsAbsentOrV37Safe = false;
                continue;
              }
              if (descriptor.enumerable !== true) {
                allRecordDescriptorsEnumerable = false;
              }
              const value = descriptor.value;
              const safe = v37SafeString(key, value);
              if (!safe) allRecordValuesV37Safe = false;
              if (key === "id" && !safe) allRecordIdsV37Safe = false;
              if (key === "url" && !safe) {
                allRecordUrlsAbsentOrV37Safe = false;
              }
              if (key !== "id" &&
                  !(typeof value === "string" || value === undefined)) {
                allOptionalValuesStringOrUndefined = false;
              }
            }
            if (!hasId) {
              allRecordKeysAllowedWithId = false;
              allRecordIdsV37Safe = false;
            }
          }
        }
      }
    }

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
    if (!exactCounters) throw new Error("V38CompletenessError");
    result = "EXACT_V38_FIXED_LISTING_SHAPE_DIAGNOSTIC_CAPTURED";
  } catch (error) {
    errorClass = safeErrorClass(error);
  }

  secureConsoleSetupBrowserRuntimeV38 = null;
  secureConsoleAgentV38 = null;
  secureConsoleChromeV38 = null;
  secureConsoleOwnedTaskTabV38 = null;
  secureConsoleOwnedTaskTabV38Eligible = false;
  secureConsoleV38State = result ===
      "EXACT_V38_FIXED_LISTING_SHAPE_DIAGNOSTIC_CAPTURED"
    ? "V38_DIAGNOSTIC_CAPTURED_INELIGIBLE"
    : "V38_DIAGNOSTIC_FAILED_INELIGIBLE";
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
      consumed: secureConsoleV38Consumed,
      bindingEligible: secureConsoleOwnedTaskTabV38Eligible,
      bindingNull: secureConsoleOwnedTaskTabV38 === null,
      state: secureConsoleV38State,
    });
  } catch (terminalError) {
    secureConsoleSetupBrowserRuntimeV38 = null;
    secureConsoleAgentV38 = null;
    secureConsoleChromeV38 = null;
    secureConsoleOwnedTaskTabV38 = null;
    secureConsoleOwnedTaskTabV38Eligible = false;
    secureConsoleV38State = "V38_FINAL_OUTPUT_FAILED_STOP";
    throw terminalError;
  }
})();
~~~

## Action-time pins and single-use procedure

Immediately before any live send, the sole Sol High owner must prove and record:

1. this brief's commit, blob, bytes, SHA-256, executable bytes, and executable
   SHA-256;
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
8. a freshly reset Node realm in which every named V35/V36/V37/V38 declaration
   is absent; and
9. byte-for-byte extraction of exactly the sole fenced executable above.

The first executable statement consumes V38 before import or attachment. Send
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

V38 handles no secret and performs no credential, token, provider, DNS, route,
proxy, listener, tunnel, VM, or repository-product mutation. It must never
print, commit, log, or infer a secret or raw tab metadata. The final later
Create/native Copy/native masked Paste confirmation and the separate later
exact-row deletion confirmation remain mandatory and cannot be pre-approved,
automated, delegated, or waived by V38.

Session naming is the only permitted browser-session side effect and is
non-provider-persistent. No background process or owner may remain. V38 can
only classify the structural mismatch for a separately reviewed successor; it
cannot authorize attachment reuse, tab adoption, or provider execution.
