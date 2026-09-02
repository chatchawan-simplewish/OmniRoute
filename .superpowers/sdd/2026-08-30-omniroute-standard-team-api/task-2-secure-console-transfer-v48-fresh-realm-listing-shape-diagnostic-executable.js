let secureConsoleV48Consumed = false;
let secureConsoleV48State = "UNCONSUMED";
let secureConsoleV48Result = null;
await (async () => {
  let setupBrowserRuntimeV48 = null;
  let agentV48 = null;
  let chromeV48 = null;
  let offeredV48 = null;
  let bindingsCleared = false;
  const counters = {
    importAttempted: 0,
    importFulfilled: 0,
    setupAttempted: 0,
    setupFulfilled: 0,
    connectAttempted: 0,
    connectFulfilled: 0,
    documentationAttempted: 0,
    documentationFulfilled: 0,
    documentationWriteAttempted: 0,
    documentationWriteFulfilled: 0,
    nameAttempted: 0,
    nameFulfilled: 0,
    openTabsAttempted: 0,
    openTabsFulfilled: 0,
    claimAttempted: 0,
    navigationAttempted: 0,
    waitAttempted: 0,
    urlReadAttempted: 0,
    snapshotAttempted: 0,
    domActionAttempted: 0,
    clipboardAttempted: 0,
    providerMutationAttempted: 0,
  };
  const emptyKeyCheck = (required) => ({
    present: false,
    data: false,
    enumerable: false,
    noAccessor: false,
    required,
    valueTypeAllowed: !required,
  });
  const emptyDiagnostic = () => ({
    arrayIsArray: false,
    arrayOwnSymbolCountZero: false,
    lengthDescriptorPresent: false,
    lengthDescriptorData: false,
    lengthDescriptorNonEnumerable: false,
    lengthDescriptorNoAccessor: false,
    boundedLength: false,
    offeredCount: -1,
    arrayOwnNamesExact: false,
    allIndexDescriptorsDataEnumerable: false,
    allIndexValuesNonNullObjects: false,
    descriptorIndexCountMatchesLength: false,
    rankZeroNonNullObject: false,
    rankZeroOrdinaryPrototype: false,
    rankZeroPrototypeDepthBounded: false,
    rankZeroOwnSymbolCountZero: false,
    rankZeroKnownKeysOnly: false,
    rankZeroRequiredIdentityPresent: false,
    rankZeroUnexpectedKeyCount: -1,
    rankZeroDescriptorsSafe: false,
    rankZeroRequiredValuesSafeStrings: false,
    rankZeroOptionalValuesStringOrUndefined: false,
    rankZeroAllValuesV47Safe: false,
    urlFieldPresent: false,
    urlFieldSafeString: false,
    urlParseSucceeded: false,
    urlHttps: false,
    urlCloudflareHostExact: false,
    urlApiTokensPathExact: false,
    documentedKeyChecks: {
      id: emptyKeyCheck(true),
      lastOpened: emptyKeyCheck(false),
      providerTabId: emptyKeyCheck(false),
      tabGroup: emptyKeyCheck(false),
      title: emptyKeyCheck(false),
      url: emptyKeyCheck(false),
    },
  });

  // BEGIN_V48_PURE_INSPECTOR
  const inspectOpenTabsV48 = (offered) => {
    const arrayIsArray = Array.isArray;
    const getOwnPropertyDescriptor = Object.getOwnPropertyDescriptor;
    const getOwnPropertyNames = Object.getOwnPropertyNames;
    const getOwnPropertySymbols = Object.getOwnPropertySymbols;
    const getPrototypeOf = Object.getPrototypeOf;
    const hasOwn = Object.hasOwn;
    const isSafeInteger = Number.isSafeInteger;
    const SetConstructor = Set;
    const URLConstructor = URL;
    const stringFrom = String;
    const safeString = (key, value) => {
      const limit = key === "url" ? 16384 : key === "title" ? 4096 : 512;
      return typeof value === "string" && value.length > 0 &&
        value.length <= limit && !/[\u0000-\u001f\u007f]/.test(value);
    };
    const keyCheck = (required) => ({
      present: false,
      data: false,
      enumerable: false,
      noAccessor: false,
      required,
      valueTypeAllowed: !required,
    });
    const diagnostic = {
      arrayIsArray: false,
      arrayOwnSymbolCountZero: false,
      lengthDescriptorPresent: false,
      lengthDescriptorData: false,
      lengthDescriptorNonEnumerable: false,
      lengthDescriptorNoAccessor: false,
      boundedLength: false,
      offeredCount: -1,
      arrayOwnNamesExact: false,
      allIndexDescriptorsDataEnumerable: false,
      allIndexValuesNonNullObjects: false,
      descriptorIndexCountMatchesLength: false,
      rankZeroNonNullObject: false,
      rankZeroOrdinaryPrototype: false,
      rankZeroPrototypeDepthBounded: false,
      rankZeroOwnSymbolCountZero: false,
      rankZeroKnownKeysOnly: false,
      rankZeroRequiredIdentityPresent: false,
      rankZeroUnexpectedKeyCount: -1,
      rankZeroDescriptorsSafe: false,
      rankZeroRequiredValuesSafeStrings: false,
      rankZeroOptionalValuesStringOrUndefined: false,
      rankZeroAllValuesV47Safe: false,
      urlFieldPresent: false,
      urlFieldSafeString: false,
      urlParseSucceeded: false,
      urlHttps: false,
      urlCloudflareHostExact: false,
      urlApiTokensPathExact: false,
      documentedKeyChecks: {
        id: keyCheck(true),
        lastOpened: keyCheck(false),
        providerTabId: keyCheck(false),
        tabGroup: keyCheck(false),
        title: keyCheck(false),
        url: keyCheck(false),
      },
    };

    diagnostic.arrayIsArray = arrayIsArray(offered);
    if (!diagnostic.arrayIsArray) return diagnostic;
    diagnostic.arrayOwnSymbolCountZero =
      getOwnPropertySymbols(offered).length === 0;
    const lengthDescriptor = getOwnPropertyDescriptor(offered, "length");
    diagnostic.lengthDescriptorPresent = lengthDescriptor !== undefined;
    diagnostic.lengthDescriptorData =
      diagnostic.lengthDescriptorPresent && hasOwn(lengthDescriptor, "value");
    diagnostic.lengthDescriptorNonEnumerable =
      diagnostic.lengthDescriptorPresent && lengthDescriptor.enumerable === false;
    diagnostic.lengthDescriptorNoAccessor =
      diagnostic.lengthDescriptorPresent && !hasOwn(lengthDescriptor, "get") &&
      !hasOwn(lengthDescriptor, "set");
    diagnostic.boundedLength = diagnostic.lengthDescriptorData &&
      isSafeInteger(lengthDescriptor.value) &&
      lengthDescriptor.value >= 1 && lengthDescriptor.value <= 1000;
    if (!diagnostic.boundedLength) return diagnostic;

    const length = lengthDescriptor.value;
    diagnostic.offeredCount = length;
    const names = getOwnPropertyNames(offered);
    let namesExact = names.length === length + 1;
    const expectedNames = new SetConstructor(["length"]);
    for (let index = 0; index < length; index++) {
      expectedNames.add(stringFrom(index));
    }
    for (let index = 0; index < names.length; index++) {
      if (!expectedNames.has(names[index])) namesExact = false;
    }
    diagnostic.arrayOwnNamesExact = namesExact;

    const descriptors = [];
    let descriptorsSafe = true;
    let valuesObjects = true;
    for (let index = 0; index < length; index++) {
      const descriptor = getOwnPropertyDescriptor(offered, stringFrom(index));
      descriptors.push(descriptor);
      const data = descriptor !== undefined && hasOwn(descriptor, "value") &&
        !hasOwn(descriptor, "get") && !hasOwn(descriptor, "set");
      if (!data || descriptor.enumerable !== true) descriptorsSafe = false;
      if (!data || typeof descriptor.value !== "object" ||
          descriptor.value === null) valuesObjects = false;
    }
    diagnostic.allIndexDescriptorsDataEnumerable = descriptorsSafe;
    diagnostic.allIndexValuesNonNullObjects = valuesObjects;
    diagnostic.descriptorIndexCountMatchesLength = descriptors.length === length;

    const firstDescriptor = descriptors[0];
    if (firstDescriptor === undefined || !hasOwn(firstDescriptor, "value") ||
        hasOwn(firstDescriptor, "get") || hasOwn(firstDescriptor, "set")) {
      return diagnostic;
    }
    const first = firstDescriptor.value;
    diagnostic.rankZeroNonNullObject =
      typeof first === "object" && first !== null;
    if (!diagnostic.rankZeroNonNullObject) return diagnostic;

    const prototype = getPrototypeOf(first);
    let prototypeParent = null;
    if (prototype !== null) prototypeParent = getPrototypeOf(prototype);
    diagnostic.rankZeroOrdinaryPrototype =
      prototype === null || prototypeParent === null;
    diagnostic.rankZeroPrototypeDepthBounded =
      prototype === null ||
      (typeof prototype === "object" && prototype !== null &&
       prototypeParent === null);
    diagnostic.rankZeroOwnSymbolCountZero =
      getOwnPropertySymbols(first).length === 0;

    const allowed = new SetConstructor([
      "id", "lastOpened", "providerTabId", "tabGroup", "title", "url",
    ]);
    const recordNames = getOwnPropertyNames(first);
    if (!isSafeInteger(recordNames.length) || recordNames.length > 1000) {
      return diagnostic;
    }
    let unexpectedCount = 0;
    for (let index = 0; index < recordNames.length; index++) {
      if (!allowed.has(recordNames[index])) unexpectedCount++;
    }
    diagnostic.rankZeroUnexpectedKeyCount = unexpectedCount;
    diagnostic.rankZeroKnownKeysOnly = unexpectedCount === 0;
    diagnostic.rankZeroRequiredIdentityPresent = recordNames.includes("id");
    diagnostic.rankZeroDescriptorsSafe = true;
    diagnostic.rankZeroRequiredValuesSafeStrings = true;
    diagnostic.rankZeroOptionalValuesStringOrUndefined = true;
    diagnostic.rankZeroAllValuesV47Safe = true;

    const documentedKeys = [
      "id", "lastOpened", "providerTabId", "tabGroup", "title", "url",
    ];
    let urlValue = null;
    for (let index = 0; index < recordNames.length; index++) {
      const key = recordNames[index];
      const descriptor = getOwnPropertyDescriptor(first, key);
      const data = descriptor !== undefined && hasOwn(descriptor, "value") &&
        !hasOwn(descriptor, "get") && !hasOwn(descriptor, "set");
      if (!data || descriptor.enumerable !== true) {
        diagnostic.rankZeroDescriptorsSafe = false;
      }
      if (allowed.has(key)) {
        const check = diagnostic.documentedKeyChecks[key];
        check.present = true;
        check.data = data;
        check.enumerable = descriptor !== undefined &&
          descriptor.enumerable === true;
        check.noAccessor = descriptor !== undefined &&
          !hasOwn(descriptor, "get") && !hasOwn(descriptor, "set");
        if (!data) {
          check.valueTypeAllowed = false;
          diagnostic.rankZeroAllValuesV47Safe = false;
          if (key === "id") {
            diagnostic.rankZeroRequiredValuesSafeStrings = false;
          } else {
            diagnostic.rankZeroOptionalValuesStringOrUndefined = false;
          }
        } else {
          const value = descriptor.value;
          const strictSafe = safeString(key, value);
          const optionalAllowed = key !== "id" &&
            (value === undefined || strictSafe);
          check.valueTypeAllowed = key === "id" ? strictSafe : optionalAllowed;
          if (!strictSafe) diagnostic.rankZeroAllValuesV47Safe = false;
          if (key === "id" && !strictSafe) {
            diagnostic.rankZeroRequiredValuesSafeStrings = false;
          }
          if (key !== "id" && !optionalAllowed) {
            diagnostic.rankZeroOptionalValuesStringOrUndefined = false;
          }
          if (key === "url" && strictSafe) urlValue = value;
        }
      }
    }

    for (let index = 0; index < documentedKeys.length; index++) {
      const key = documentedKeys[index];
      const check = diagnostic.documentedKeyChecks[key];
      if (key === "id" && !check.present) {
        diagnostic.rankZeroRequiredValuesSafeStrings = false;
        diagnostic.rankZeroAllValuesV47Safe = false;
      }
    }

    const urlCheck = diagnostic.documentedKeyChecks.url;
    diagnostic.urlFieldPresent = urlCheck.present;
    diagnostic.urlFieldSafeString = urlCheck.present && urlCheck.data &&
      urlCheck.valueTypeAllowed && urlValue !== null;
    if (diagnostic.urlFieldSafeString) {
      let parsed = null;
      try {
        parsed = new URLConstructor(urlValue);
        diagnostic.urlParseSucceeded = true;
        diagnostic.urlHttps = parsed.protocol === "https:";
        diagnostic.urlCloudflareHostExact =
          parsed.hostname === "dash.cloudflare.com";
        diagnostic.urlApiTokensPathExact =
          parsed.pathname === "/profile/api-tokens";
      } catch {
        diagnostic.urlParseSucceeded = false;
      }
      parsed = null;
    }
    urlValue = null;
    return diagnostic;
  };
  // END_V48_PURE_INSPECTOR

  let result = "V48_FRESH_LISTING_SHAPE_DIAGNOSTIC_FAILED_STOP";
  let errorClass = "NONE";
  let declarationShape = false;
  let moduleShape = false;
  let agentShape = false;
  let connectedShape = false;
  let documentationValidated = false;
  let documentationLength = -1;
  let sessionNamed = false;
  let diagnostic = emptyDiagnostic();
  try {
    const gateWasFresh = secureConsoleV48Consumed === false &&
      secureConsoleV48State === "UNCONSUMED" && secureConsoleV48Result === null;
    secureConsoleV48Consumed = true;
    declarationShape = gateWasFresh &&
      typeof secureConsoleV47Consumed === "undefined";
    if (!declarationShape) throw new Error("FreshRealmDeclarationError");
    secureConsoleV48State = "CONSUMING";

    counters.importAttempted++;
    const imported = await import(
      "file:///C:/Users/chatc/.codex/plugins/cache/openai-bundled/chrome/26.831.21537/scripts/browser-client.mjs"
    );
    counters.importFulfilled++;
    moduleShape = typeof imported === "object" && imported !== null &&
      typeof imported.setupBrowserRuntime === "function";
    if (!moduleShape) throw new Error("FreshRuntimeModuleShapeError");
    setupBrowserRuntimeV48 = imported.setupBrowserRuntime;

    counters.setupAttempted++;
    agentV48 = await setupBrowserRuntimeV48();
    counters.setupFulfilled++;
    agentShape = typeof agentV48 === "object" && agentV48 !== null &&
      typeof agentV48.browsers?.get === "function";
    if (!agentShape) throw new Error("FreshRuntimeAgentShapeError");

    counters.connectAttempted++;
    chromeV48 = await agentV48.browsers.get("chrome");
    counters.connectFulfilled++;
    connectedShape = typeof chromeV48 === "object" && chromeV48 !== null &&
      typeof chromeV48.documentation === "function" &&
      typeof chromeV48.nameSession === "function" &&
      typeof chromeV48.user?.openTabs === "function";
    if (!connectedShape) throw new Error("FreshChromeShapeError");

    counters.documentationAttempted++;
    const documentation = await chromeV48.documentation();
    counters.documentationFulfilled++;
    documentationValidated = typeof documentation === "string" &&
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
    try {
      await nodeRepl.write(documentation);
      counters.documentationWriteFulfilled++;
    } catch {
      throw new Error("V48DocumentationOutputError");
    }

    counters.nameAttempted++;
    await chromeV48.nameSession("🔐 OmniRoute V48 listing diagnostic");
    counters.nameFulfilled++;
    sessionNamed = true;

    counters.openTabsAttempted++;
    offeredV48 = await chromeV48.user.openTabs();
    counters.openTabsFulfilled++;
    diagnostic = inspectOpenTabsV48(offeredV48);

    const exactCounters = counters.importAttempted === 1 &&
      counters.importFulfilled === 1 && counters.setupAttempted === 1 &&
      counters.setupFulfilled === 1 && counters.connectAttempted === 1 &&
      counters.connectFulfilled === 1 &&
      counters.documentationAttempted === 1 &&
      counters.documentationFulfilled === 1 &&
      counters.documentationWriteAttempted === 1 &&
      counters.documentationWriteFulfilled === 1 &&
      counters.nameAttempted === 1 &&
      counters.nameFulfilled === 1 && counters.openTabsAttempted === 1 &&
      counters.openTabsFulfilled === 1 && counters.claimAttempted === 0 &&
      counters.navigationAttempted === 0 && counters.waitAttempted === 0 &&
      counters.urlReadAttempted === 0 && counters.snapshotAttempted === 0 &&
      counters.domActionAttempted === 0 && counters.clipboardAttempted === 0 &&
      counters.providerMutationAttempted === 0;
    if (!exactCounters) throw new Error("V48CompletenessError");
    result = "EXACT_V48_FIXED_LISTING_SHAPE_DIAGNOSTIC_CAPTURED";
    secureConsoleV48State = "DIAGNOSTIC_CAPTURED_INELIGIBLE";
  } catch {
    errorClass = "Error";
    secureConsoleV48State = "FAILED_INELIGIBLE";
  } finally {
    offeredV48 = null;
    chromeV48 = null;
    agentV48 = null;
    setupBrowserRuntimeV48 = null;
    bindingsCleared = offeredV48 === null && chromeV48 === null &&
      agentV48 === null && setupBrowserRuntimeV48 === null;
  }

  secureConsoleV48Result = {
    result,
    declarationShape,
    moduleShape,
    agentShape,
    connectedShape,
    documentationValidated,
    documentationLength,
    sessionNamed,
    ...diagnostic,
    ...counters,
    errorClass,
    consumed: secureConsoleV48Consumed,
    bindingEligible: false,
    bindingsCleared,
    state: secureConsoleV48State,
  };
  await nodeRepl.write(secureConsoleV48Result);
})();
