# OmniRoute V19 synchronous input-value readiness replacement brief

`authorizes_live_execution=false`

This is a new fresh-session, one-shot readiness-only contract. It performs no
Create, click, press, provider-persistent mutation, credential read, clipboard
operation, VM mutation, DNS change, routing change, listener start, or process
start. It does not invoke, reuse, continue, or reinterpret consumed V18, V17,
V16, V3, or any earlier gate.

## Root cause and consumed-gate boundary

V18 is immutable and consumed-failed-clean:

- incident commit: `512663814f570587edd2a05859b5f9fe30d00199`;
- incident path:
  `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-token-page-readiness-v18-live-incident.md`;
- incident bytes: `4437`;
- incident SHA-256:
  `6C026035CD5006EB13933F4DAAAEFB76251B3C3C9A81494FC2445DC573CBF170`;
- incident blob: `8ea0e14f54376f2276d25f2e151d1f4c26666e38`.

V18 proved the exact empty baseline, prefill marker absence, and one fulfilled
fixed non-secret fill. It then rejected at the native query-echo wait before
the terminal-marker wait or terminal evaluator. The query-echo locator was
`getByText(exact target)`, but the target is an input value, not element text.
That locator therefore cannot prove the typed value. V19 removes only that
category error.

## Design decision

V19 keeps the V18 fresh-tab, navigation, baseline, section, marker, terminal,
Create/name/row, retention, cleanup, output, and secret boundaries. After the
single awaited fill it uses one synchronous read-only evaluation on the exact
search input to validate a fixed-key projection:

- the input remains connected and visible;
- its normalized value equals the fixed non-secret query; and
- exactly one search input in the exact section has that value.

Only after that proof does V19 perform the inherited native terminal-marker
wait, followed by the inherited synchronous terminal structural evaluation.
There is no page-resident timer, observer, Promise, async evaluator, expando,
background work, polling loop, retry, fallback, manual integration, or verdict
relaxation.

The absent-before side remains exact: the trusted baseline proves the unique
section search input is empty, and the terminal marker count is zero before
fill. The present-after side requires the synchronous query-state projection,
one visible terminal marker, the exact terminal row shape, exact query echo in
the input, zero candidate/matching rows, one Create control, and zero exact
token-name/row matches.

## Exact inherited boundary

V19 preserves every V4 semantic page signature, completeness constraint,
fixed URL and non-secret query, exact success retention, fail-closed cleanup,
no-residue rule, no-retry rule, fixed safe output, secret exclusion, and
confirmation boundary. The mandatory final Create/native Copy/native masked
Paste confirmation and later separate exact-row deletion confirmation remain
unreached and mandatory.

V19 additionally requires the exact consumed-failed-clean V18, V17, and V16
null/ineligible/no-detach/no-read predecessor bindings, all earlier retained
null bindings, and the exact V4 state. Any missing, malformed, drifted,
uncertain, timed-out, truncated, or non-PASS state consumes V19 and stops.

## One-shot V19 executable

```javascript
let secureConsoleOwnedTaskTabV19 = null;
let secureConsoleOwnedTaskTabV19Eligible = false;
let secureConsoleOwnedTaskTabV19State = "UNCREATED";
let secureConsoleOwnedTaskTabV19PreCreateDetachConsumed = false;
let secureConsoleOwnedTaskTabV19PostNativeDetachConsumed = false;
let secureConsoleCloudflareReadsV19Consumed = false;
let secureConsoleV19ReadinessConsumed = false;
await (async () => {
  const gateWasFresh = secureConsoleV19ReadinessConsumed === false;
  secureConsoleV19ReadinessConsumed = true;
  const counters = {
    newAttempted: 0, newFulfilled: 0,
    navigationAttempted: 0, navigationFulfilled: 0,
    urlAttempted: 0, urlFulfilled: 0,
    waitAttempted: 0, waitFulfilled: 0,
    countAttempted: 0, countFulfilled: 0,
    scopeAttempted: 0, scopeFulfilled: 0,
    baselineAttempted: 0, baselineFulfilled: 0,
    fillAttempted: 0, fillFulfilled: 0,
    terminalAttempted: 0, terminalFulfilled: 0,
    prefillMarkerAttempted: 0, prefillMarkerFulfilled: 0,
    queryAttempted: 0, queryFulfilled: 0,
    markerAttempted: 0, markerFulfilled: 0,
    createAttempted: 0, createFulfilled: 0,
    nameAttempted: 0, nameFulfilled: 0,
    rowAttempted: 0, rowFulfilled: 0,
    closeAttempted: 0, closeFulfilled: 0,
    writeAttempted: 0,
  };
  const emptyBaseline = () => ({
    inputConnected: false, inputVisible: false, inputValueEmpty: false,
    sectionFound: false, sectionDepth: -1,
    pageTableCount: -1, pageGridCount: -1, pagePaginationCount: -1,
    pageBusyCount: -1, sectionTableCount: -1, sectionSearchCount: -1,
    sectionStatusCount: -1, sectionEmptyStatusCount: -1,
    sectionTbodyCount: -1, sectionRowCount: -1,
    sectionVisibleRowCount: -1, sectionBusyCount: -1,
    sectionCreateActionableCount: -1,
  });
  const emptyTerminal = () => ({
    terminalObserved: false,
    inputConnected: false, inputVisible: false, inputValueExact: false,
    queryInputExactCount: -1, sectionFound: false, sectionDepth: -1,
    pageTableCount: -1, pageGridCount: -1, pagePaginationCount: -1,
    pageBusyCount: -1, sectionTableCount: -1, sectionSearchCount: -1,
    sectionStatusCount: -1, sectionEmptyStatusCount: -1,
    sectionTbodyCount: -1, sectionRowCount: -1,
    sectionVisibleRowCount: -1, sectionVisibleCandidateRowCount: -1,
    sectionEmptyRowCount: -1, sectionBusyCount: -1,
    matchingRowCount: -1,
  });
  const safeErrorClass = (error) => {
    const name = typeof error?.name === "string" ? error.name : "Error";
    return /^[A-Za-z][A-Za-z0-9_]{0,63}$/.test(name) ? name : "Error";
  };
  const plainRecord = (value) => {
    if (typeof value !== "object" || value === null) return false;
    const prototype = Object.getPrototypeOf(value);
    return prototype === null ||
      (prototype !== null && Object.getPrototypeOf(prototype) === null);
  };
  const exactKeys = (value, expected) => {
    if (!plainRecord(value)) return false;
    const actual = Object.keys(value).sort();
    const wanted = [...expected].sort();
    return actual.length === wanted.length &&
      actual.every((key, index) => key === wanted[index]);
  };
  const trustedProjection = (value, booleanKeys, integerKeys) => {
    const expectedKeys = [...booleanKeys, ...integerKeys];
    if (!exactKeys(value, expectedKeys)) return null;
    const projected = {};
    for (const key of booleanKeys) {
      const item = value[key];
      if (typeof item !== "boolean") return null;
      projected[key] = item;
    }
    for (const key of integerKeys) {
      const item = value[key];
      if (!Number.isSafeInteger(item) || item < -1 || item > 1000000) return null;
      projected[key] = item;
    }
    return projected;
  };
  let result = "PRECONDITION_FAIL";
  let declarationShape = false;
  let predecessorStateExact = false;
  let controllerOwnership = false;
  let tabShape = false;
  let createdHandleCaptured = false;
  let navigationTargetExact = false;
  let placeholderSearchCount = -1;
  let baselineValidated = false;
  let baselineSemanticExact = false;
  let terminalValidated = false;
  let terminalSemanticExact = false;
  let prefillQueryInputExactCount = -1;
  let prefillEmptyMarkerCount = -1;
  let postfillQueryInputExactCount = -1;
  let createControlCount = -1;
  let tokenNameCount = -1;
  let matchingRowCount = -1;
  let filterComplete = false;
  let tokenSemanticSignature = false;
  let baseline = emptyBaseline();
  let terminal = emptyTerminal();
  let cleanupState = "NO_TAB_CREATED";
  let residueConverged = true;
  let errorClass = "NONE";
  let tab = null;
  try {
    declarationShape =
      typeof secureConsoleChromeV5 === "object" &&
      secureConsoleChromeV5 !== null &&
      typeof secureConsoleChromeV5.tabs?.new === "function" &&
      typeof secureConsoleV18ReadinessConsumed === "boolean" &&
      typeof secureConsoleV17ReadinessConsumed === "boolean" &&
      typeof secureConsoleV16ReadinessConsumed === "boolean" &&
      typeof secureConsoleV15StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV14StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV13StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV12StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV11StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV10StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV9ReadinessConsumed === "boolean" &&
      typeof secureConsoleV19ReadinessConsumed === "boolean";
    if (!declarationShape) throw new Error("ReadinessDeclarationShapeError");
    predecessorStateExact =
      gateWasFresh === true &&
      secureConsoleV18ReadinessConsumed === true &&
      secureConsoleOwnedTaskTabV18 === null &&
      secureConsoleOwnedTaskTabV18Eligible === false &&
      secureConsoleOwnedTaskTabV18State === "V18_READINESS_FAILED_CLEAN" &&
      secureConsoleOwnedTaskTabV18PreCreateDetachConsumed === false &&
      secureConsoleOwnedTaskTabV18PostNativeDetachConsumed === false &&
      secureConsoleCloudflareReadsV18Consumed === false &&
      secureConsoleV17ReadinessConsumed === true &&
      secureConsoleOwnedTaskTabV17 === null &&
      secureConsoleOwnedTaskTabV17Eligible === false &&
      secureConsoleOwnedTaskTabV17State === "V17_READINESS_FAILED_CLEAN" &&
      secureConsoleOwnedTaskTabV17PreCreateDetachConsumed === false &&
      secureConsoleOwnedTaskTabV17PostNativeDetachConsumed === false &&
      secureConsoleCloudflareReadsV17Consumed === false &&
      secureConsoleV16ReadinessConsumed === true &&
      secureConsoleOwnedTaskTabV16 === null &&
      secureConsoleOwnedTaskTabV16Eligible === false &&
      secureConsoleOwnedTaskTabV16State === "V16_READINESS_FAILED_CLEAN" &&
      secureConsoleOwnedTaskTabV16PreCreateDetachConsumed === false &&
      secureConsoleOwnedTaskTabV16PostNativeDetachConsumed === false &&
      secureConsoleCloudflareReadsV16Consumed === false &&
      secureConsoleV15StructuralDiagnosticConsumed === true &&
      secureConsoleV15RetainedTab === null &&
      secureConsoleV14StructuralDiagnosticConsumed === true &&
      secureConsoleV14RetainedTab === null &&
      secureConsoleV13StructuralDiagnosticConsumed === true &&
      secureConsoleV13RetainedTab === null &&
      secureConsoleV12StructuralDiagnosticConsumed === true &&
      secureConsoleV12RetainedTab === null &&
      secureConsoleV11StructuralDiagnosticConsumed === true &&
      secureConsoleV11RetainedTab === null &&
      secureConsoleV10StructuralDiagnosticConsumed === true &&
      secureConsoleV10RetainedTab === null &&
      secureConsoleV9ReadinessConsumed === true &&
      secureConsoleV9RetainedTab === null &&
      secureConsoleV4AdoptionConsumed === true &&
      secureConsoleOwnedTaskTabV4 === null &&
      secureConsoleOwnedTaskTabV4Eligible === false &&
      secureConsoleOwnedTaskTabV4State === "V9_OWNED_TAB_READINESS_FAILED_CLEAN" &&
      secureConsoleOwnedTaskTabV4PreCreateDetachConsumed === false &&
      secureConsoleOwnedTaskTabV4PostNativeDetachConsumed === false &&
      secureConsoleCloudflareReadsV4Consumed === false &&
      secureConsoleOwnedTaskTabV19 === null &&
      secureConsoleOwnedTaskTabV19Eligible === false &&
      secureConsoleOwnedTaskTabV19State === "UNCREATED" &&
      secureConsoleOwnedTaskTabV19PreCreateDetachConsumed === false &&
      secureConsoleOwnedTaskTabV19PostNativeDetachConsumed === false &&
      secureConsoleCloudflareReadsV19Consumed === false;
    if (!predecessorStateExact) throw new Error("ReadinessPredecessorStateError");

    counters.newAttempted++;
    secureConsoleOwnedTaskTabV19 = tab = await secureConsoleChromeV5.tabs.new();
    counters.newFulfilled++;
    createdHandleCaptured = typeof tab === "object" && tab !== null;
    if (!createdHandleCaptured) throw new Error("ReadinessCreatedHandleError");
    controllerOwnership = secureConsoleOwnedTaskTabV19 === tab;
    tabShape =
      controllerOwnership &&
      typeof tab.goto === "function" &&
      typeof tab.url === "function" &&
      typeof tab.close === "function" &&
      typeof tab.playwright?.locator === "function" &&
      typeof tab.playwright?.getByRole === "function";
    if (!tabShape) throw new Error("ReadinessTabShapeError");

    counters.navigationAttempted++;
    await tab.goto("https://dash.cloudflare.com/profile/api-tokens");
    counters.navigationFulfilled++;
    counters.urlAttempted++;
    const tokenUrl = new URL(await tab.url());
    counters.urlFulfilled++;
    navigationTargetExact = tokenUrl.href === "https://dash.cloudflare.com/profile/api-tokens";
    if (!navigationTargetExact) throw new Error("ReadinessNavigationTargetError");

    const tokenFilter = tab.playwright.locator('input[placeholder*="search" i]:visible');
    if (typeof tokenFilter?.waitFor !== "function" ||
        typeof tokenFilter?.count !== "function" ||
        typeof tokenFilter?.evaluate !== "function" ||
        typeof tokenFilter?.fill !== "function" ||
        typeof tokenFilter?.locator !== "function") {
      throw new Error("ReadinessFilterShapeError");
    }
    counters.waitAttempted++;
    await tokenFilter.waitFor({ state: "visible", timeoutMs: 10000 });
    counters.waitFulfilled++;
    counters.countAttempted++;
    placeholderSearchCount = await tokenFilter.count();
    counters.countFulfilled++;
    if (placeholderSearchCount !== 1) throw new Error("ReadinessFilterCountError");
    const tokenSection = tokenFilter.locator("xpath=ancestor::section[1]");
    if (typeof tokenSection?.count !== "function" ||
        typeof tokenSection?.locator !== "function" ||
        typeof tokenSection?.getByText !== "function" ||
        typeof tokenSection?.getByRole !== "function") {
      throw new Error("ReadinessSectionShapeError");
    }
    counters.scopeAttempted++;
    const tokenSectionCount = await tokenSection.count();
    counters.scopeFulfilled++;
    if (tokenSectionCount !== 1) throw new Error("ReadinessSectionCountError");

    counters.baselineAttempted++;
    const untrustedBaseline = await tokenFilter.evaluate((input) => {
      const normalize = (value) => (value || "").replace(/\s+/g, " ").trim().toLowerCase();
      const statusText = new Set(["no api tokens found", "no tokens found", "no results"]);
      const actionSelector = 'button, a, [role="button"], [role="link"]';
      let depth = 1;
      let node = input.parentElement;
      let section = null;
      let sectionDepth = -1;
      while (node !== null && node !== document.body && depth <= 32) {
        if (section === null &&
            (node.tagName === "SECTION" || ["region", "group"].includes(node.getAttribute("role")))) {
          section = node;
          sectionDepth = depth;
        }
        node = node.parentElement;
        depth++;
      }
      const statuses = section === null ? [] : [...section.querySelectorAll('[role="status"]')];
      const rows = section === null ? [] : [...section.querySelectorAll("tbody tr")];
      const actions = section === null ? [] : [...section.querySelectorAll(actionSelector)];
      return {
        inputConnected: input.isConnected === true,
        inputVisible: input.getClientRects().length === 1,
        inputValueEmpty: input.value === "",
        sectionFound: section !== null,
        sectionDepth,
        pageTableCount: document.querySelectorAll("table").length,
        pageGridCount: document.querySelectorAll('[role="grid"]').length,
        pagePaginationCount: document.querySelectorAll('[aria-label="Pagination"], [aria-label="Next page"], [aria-label="Previous page"]').length,
        pageBusyCount: document.querySelectorAll('[aria-busy="true"], [role="progressbar"]').length,
        sectionTableCount: section === null ? -1 : section.querySelectorAll("table").length,
        sectionSearchCount: section === null ? -1 : section.querySelectorAll('input[placeholder*="search" i]').length,
        sectionStatusCount: statuses.length,
        sectionEmptyStatusCount: statuses.filter((item) => statusText.has(normalize(item.textContent))).length,
        sectionTbodyCount: section === null ? -1 : section.querySelectorAll("tbody").length,
        sectionRowCount: section === null ? -1 : rows.length,
        sectionVisibleRowCount: section === null ? -1 : rows.filter((row) => row.getClientRects().length > 0).length,
        sectionBusyCount: section === null ? -1 : section.querySelectorAll('[aria-busy="true"], [role="progressbar"]').length,
        sectionCreateActionableCount: section === null ? -1 : actions.filter((item) => {
          const text = normalize(item.textContent);
          return text === "create token" || text === "create api token" || text === "create";
        }).length,
      };
    });
    counters.baselineFulfilled++;
    const baselineBooleanKeys = [
      "inputConnected", "inputVisible", "inputValueEmpty", "sectionFound",
    ];
    const baselineIntegerKeys = [
      "sectionDepth", "pageTableCount", "pageGridCount", "pagePaginationCount",
      "pageBusyCount", "sectionTableCount", "sectionSearchCount",
      "sectionStatusCount", "sectionEmptyStatusCount", "sectionTbodyCount",
      "sectionRowCount", "sectionVisibleRowCount", "sectionBusyCount",
      "sectionCreateActionableCount",
    ];
    const trustedBaseline = trustedProjection(
      untrustedBaseline,
      baselineBooleanKeys,
      baselineIntegerKeys,
    );
    baselineValidated = trustedBaseline !== null;
    if (!baselineValidated) throw new Error("ReadinessBaselineValidationError");
    baseline = trustedBaseline;
    baselineSemanticExact =
      baseline.inputConnected === true &&
      baseline.inputVisible === true &&
      baseline.inputValueEmpty === true &&
      baseline.sectionFound === true &&
      baseline.sectionDepth === 3 &&
      baseline.pageTableCount === 2 &&
      baseline.pageGridCount === 0 &&
      baseline.pagePaginationCount === 0 &&
      baseline.pageBusyCount === 0 &&
      baseline.sectionTableCount === 1 &&
      baseline.sectionSearchCount === 1 &&
      baseline.sectionStatusCount === 0 &&
      baseline.sectionEmptyStatusCount === 0 &&
      baseline.sectionTbodyCount === 1 &&
      baseline.sectionRowCount === 5 &&
      baseline.sectionVisibleRowCount === 5 &&
      baseline.sectionBusyCount === 0 &&
      baseline.sectionCreateActionableCount === 0;
    if (!baselineSemanticExact) throw new Error("ReadinessBaselineSemanticError");

    const terminalEmptyStatus = tokenSection.getByRole("status").filter({
      hasText: /^(?:No API Tokens Found|No Tokens Found)$/i,
    });
    const terminalEmptyRow = tokenSection.getByRole("row").filter({
      hasText: /^(?:No API Tokens Found|No Tokens Found)$/i,
    });
    if (typeof terminalEmptyStatus?.or !== "function") {
      throw new Error("ReadinessTerminalLocatorShapeError");
    }
    const terminalMarker = terminalEmptyStatus.or(terminalEmptyRow);
    if (typeof terminalMarker?.waitFor !== "function" ||
        typeof terminalMarker?.count !== "function") {
      throw new Error("ReadinessTerminalMarkerShapeError");
    }
    prefillQueryInputExactCount =
      baseline.inputValueEmpty === true && baseline.sectionSearchCount === 1 ? 0 : -1;
    counters.prefillMarkerAttempted++;
    prefillEmptyMarkerCount = await terminalMarker.count();
    counters.prefillMarkerFulfilled++;
    if (prefillQueryInputExactCount !== 0 || prefillEmptyMarkerCount !== 0) {
      throw new Error("ReadinessPrefillMarkerStateError");
    }

    counters.fillAttempted++;
    await tokenFilter.fill("OmniRoute secure console R5 20260901");
    counters.fillFulfilled++;

    counters.queryAttempted++;
    const untrustedQueryState = await tokenFilter.evaluate((input) => {
      const target = "omniroute secure console r5 20260901";
      const normalize = (value) => (value || "").replace(/\s+/g, " ").trim().toLowerCase();
      let depth = 1;
      let node = input.parentElement;
      let section = null;
      while (node !== null && node !== document.body && depth <= 32) {
        if (section === null &&
            (node.tagName === "SECTION" || ["region", "group"].includes(node.getAttribute("role")))) {
          section = node;
        }
        node = node.parentElement;
        depth++;
      }
      return {
        inputConnected: input.isConnected === true,
        inputVisible: input.getClientRects().length === 1,
        inputValueExact: normalize(input.value) === target,
        queryInputExactCount: section === null ? -1 :
          [...section.querySelectorAll('input[placeholder*="search" i]')]
            .filter((item) => normalize(item.value) === target).length,
      };
    });
    counters.queryFulfilled++;
    const trustedQueryState = trustedProjection(
      untrustedQueryState,
      ["inputConnected", "inputVisible", "inputValueExact"],
      ["queryInputExactCount"],
    );
    if (trustedQueryState === null) throw new Error("ReadinessQueryStateValidationError");
    postfillQueryInputExactCount = trustedQueryState.queryInputExactCount;
    if (trustedQueryState.inputConnected !== true ||
        trustedQueryState.inputVisible !== true ||
        trustedQueryState.inputValueExact !== true ||
        postfillQueryInputExactCount !== 1) {
      throw new Error("ReadinessQueryStateSemanticError");
    }

    counters.markerAttempted++;
    await terminalMarker.waitFor({ state: "visible", timeoutMs: 20000 });
    const terminalMarkerCount = await terminalMarker.count();
    counters.markerFulfilled++;
    if (terminalMarkerCount !== 1) throw new Error("ReadinessTerminalMarkerCountError");

    counters.terminalAttempted++;
    const untrustedTerminal = await tokenFilter.evaluate((input) => {
      const target = "omniroute secure console r5 20260901";
      const normalize = (value) => (value || "").replace(/\s+/g, " ").trim().toLowerCase();
      const statusText = new Set(["no api tokens found", "no tokens found"]);
      let depth = 1;
      let node = input.parentElement;
      let section = null;
      let sectionDepth = -1;
      while (node !== null && node !== document.body && depth <= 32) {
        if (section === null &&
            (node.tagName === "SECTION" || ["region", "group"].includes(node.getAttribute("role")))) {
          section = node;
          sectionDepth = depth;
        }
        node = node.parentElement;
        depth++;
      }
      const rows = section === null ? [] : [...section.querySelectorAll("tbody tr")];
      const statuses = section === null ? [] : [...section.querySelectorAll('[role="status"]')];
      const visibleRows = rows.filter((row) => row.getClientRects().length > 0);
      const emptyRows = rows.filter((row) => statusText.has(normalize(row.textContent)));
      const visibleEmptyRows = emptyRows.filter((row) => row.getClientRects().length > 0);
      const emptyStatuses = statuses.filter((item) => statusText.has(normalize(item.textContent)));
      const visibleEmptyStatuses = emptyStatuses.filter((item) => item.getClientRects().length > 0);
      const visibleCandidateRows = visibleRows.filter((row) => !statusText.has(normalize(row.textContent)));
      const terminalMarkerCount = visibleEmptyStatuses.length + visibleEmptyRows.length;
      const rowShape =
        (rows.length === 0 && visibleEmptyStatuses.length === 1) ||
        (rows.length === 5 && visibleRows.length === 0 && visibleEmptyStatuses.length === 1) ||
        (rows.length === 1 && emptyRows.length === 1 &&
          visibleEmptyRows.length === 1 && visibleCandidateRows.length === 0);
      return {
        terminalObserved: terminalMarkerCount === 1 && rowShape,
        inputConnected: input.isConnected === true,
        inputVisible: input.getClientRects().length === 1,
        inputValueExact: normalize(input.value) === target,
        queryInputExactCount: section === null ? -1 : [...section.querySelectorAll('input[placeholder*="search" i]')].filter((item) => normalize(item.value) === target).length,
        sectionFound: section !== null,
        sectionDepth,
        pageTableCount: document.querySelectorAll("table").length,
        pageGridCount: document.querySelectorAll('[role="grid"]').length,
        pagePaginationCount: document.querySelectorAll('[aria-label="Pagination"], [aria-label="Next page"], [aria-label="Previous page"]').length,
        pageBusyCount: document.querySelectorAll('[aria-busy="true"], [role="progressbar"]').length,
        sectionTableCount: section === null ? -1 : section.querySelectorAll("table").length,
        sectionSearchCount: section === null ? -1 : section.querySelectorAll('input[placeholder*="search" i]').length,
        sectionStatusCount: statuses.length,
        sectionEmptyStatusCount: emptyStatuses.length,
        sectionVisibleEmptyStatusCount: visibleEmptyStatuses.length,
        sectionTbodyCount: section === null ? -1 : section.querySelectorAll("tbody").length,
        sectionRowCount: section === null ? -1 : rows.length,
        sectionVisibleRowCount: section === null ? -1 : visibleRows.length,
        sectionVisibleCandidateRowCount: section === null ? -1 : visibleCandidateRows.length,
        sectionEmptyRowCount: section === null ? -1 : emptyRows.length,
        sectionVisibleEmptyRowCount: section === null ? -1 : visibleEmptyRows.length,
        sectionBusyCount: section === null ? -1 : section.querySelectorAll('[aria-busy="true"], [role="progressbar"]').length,
        matchingRowCount: section === null ? -1 : rows.filter((row) => normalize(row.textContent).includes(target)).length,
        terminalMarkerCount,
      };
    });
    counters.terminalFulfilled++;
    const terminalBooleanKeys = [
      "terminalObserved", "inputConnected", "inputVisible",
      "inputValueExact", "sectionFound",
    ];
    const terminalIntegerKeys = [
      "queryInputExactCount", "sectionDepth", "pageTableCount", "pageGridCount",
      "pagePaginationCount", "pageBusyCount", "sectionTableCount",
      "sectionSearchCount", "sectionStatusCount", "sectionEmptyStatusCount",
      "sectionVisibleEmptyStatusCount", "sectionTbodyCount", "sectionRowCount",
      "sectionVisibleRowCount", "sectionVisibleCandidateRowCount",
      "sectionEmptyRowCount", "sectionVisibleEmptyRowCount",
      "sectionBusyCount", "matchingRowCount", "terminalMarkerCount",
    ];
    const trustedTerminal = trustedProjection(
      untrustedTerminal,
      terminalBooleanKeys,
      terminalIntegerKeys,
    );
    terminalValidated = trustedTerminal !== null;
    if (!terminalValidated) throw new Error("ReadinessTerminalValidationError");
    terminal = trustedTerminal;
    const terminalRowShapeExact =
      terminal.sectionRowCount === 0 ||
      (terminal.sectionRowCount === 5 && terminal.sectionVisibleRowCount === 0) ||
      (terminal.sectionRowCount === 1 && terminal.sectionEmptyRowCount === 1 &&
        terminal.sectionVisibleCandidateRowCount === 0);
    terminalSemanticExact =
      terminal.terminalObserved === true &&
      terminal.inputConnected === true &&
      terminal.inputVisible === true &&
      terminal.inputValueExact === true &&
      terminal.queryInputExactCount === 1 &&
      terminal.sectionFound === true &&
      terminal.sectionDepth === 3 &&
      terminal.pageTableCount === 2 &&
      terminal.pageGridCount === 0 &&
      terminal.pagePaginationCount === 0 &&
      terminal.pageBusyCount === 0 &&
      terminal.sectionTableCount === 1 &&
      terminal.sectionSearchCount === 1 &&
      terminal.sectionStatusCount === terminal.sectionEmptyStatusCount &&
      terminal.sectionStatusCount >= 0 && terminal.sectionStatusCount <= 1 &&
      terminal.sectionVisibleEmptyStatusCount >= 0 &&
      terminal.sectionVisibleEmptyStatusCount <= 1 &&
      terminal.sectionTbodyCount === 1 &&
      terminal.sectionVisibleCandidateRowCount === 0 &&
      terminal.sectionEmptyRowCount >= 0 && terminal.sectionEmptyRowCount <= 1 &&
      terminal.sectionVisibleEmptyRowCount >= 0 &&
      terminal.sectionVisibleEmptyRowCount <= 1 &&
      terminal.sectionBusyCount === 0 &&
      terminal.terminalMarkerCount === 1 &&
      terminal.matchingRowCount === 0 &&
      terminalRowShapeExact;
    if (!terminalSemanticExact) throw new Error("ReadinessTerminalSemanticError");

    counters.createAttempted++;
    createControlCount =
      await tab.playwright.getByRole("button", { name: "Create Token", exact: true }).count() +
      await tab.playwright.getByRole("link", { name: "Create Token", exact: true }).count();
    counters.createFulfilled++;
    counters.nameAttempted++;
    tokenNameCount = await tokenSection.locator("table tbody").getByText("OmniRoute secure console R5 20260901", { exact: true }).count();
    counters.nameFulfilled++;
    counters.rowAttempted++;
    matchingRowCount = await tokenSection.getByRole("row").filter({ hasText: "OmniRoute secure console R5 20260901" }).count();
    counters.rowFulfilled++;
    filterComplete =
      baseline.inputValueEmpty === true &&
      prefillQueryInputExactCount === 0 &&
      prefillEmptyMarkerCount === 0 &&
      terminal.inputValueExact === true &&
      terminal.queryInputExactCount === 1 &&
      postfillQueryInputExactCount === 1 &&
      terminal.terminalMarkerCount === 1 &&
      terminal.terminalObserved === true;
    tokenSemanticSignature =
      navigationTargetExact === true &&
      baselineSemanticExact === true &&
      terminalSemanticExact === true &&
      createControlCount === 1 &&
      postfillQueryInputExactCount === 1 &&
      tokenNameCount === 0 &&
      matchingRowCount === 0 &&
      terminal.matchingRowCount === 0 &&
      filterComplete === true;
    if (!tokenSemanticSignature) throw new Error("AuthenticatedTokenPageSemanticStateError");
    result = "V19_TOKEN_PAGE_SEMANTIC_READINESS_BODY_COMPLETE";
  } catch (error) {
    errorClass = safeErrorClass(error);
  }

  if (result === "V19_TOKEN_PAGE_SEMANTIC_READINESS_BODY_COMPLETE") {
    secureConsoleOwnedTaskTabV19 = tab;
    secureConsoleOwnedTaskTabV19Eligible = true;
    secureConsoleOwnedTaskTabV19State = "TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE_V19";
    cleanupState = "SUCCESS_TAB_RETAINED";
    residueConverged = true;
    result = "EXACT_V19_TOKEN_PAGE_SEMANTIC_READINESS_PASS";
  } else if (counters.newAttempted === 1 && counters.newFulfilled === 0) {
    cleanupState = "NEW_REJECTED_RESIDUE_UNPROVEN";
    residueConverged = false;
    secureConsoleOwnedTaskTabV19State = "V19_READINESS_FAILED_RESIDUE_UNPROVEN";
  } else if (counters.newFulfilled === 1 && createdHandleCaptured === false) {
    cleanupState = "NEW_FULFILLED_WITHOUT_HANDLE_RESIDUE_UNPROVEN";
    residueConverged = false;
    secureConsoleOwnedTaskTabV19State = "V19_READINESS_FAILED_RESIDUE_UNPROVEN";
  } else if (tab !== null && tab !== undefined) {
    if (typeof tab.close !== "function") {
      cleanupState = "MALFORMED_EXACT_HANDLE_RETAINED";
      residueConverged = false;
      secureConsoleOwnedTaskTabV19 = tab;
      secureConsoleOwnedTaskTabV19Eligible = false;
      secureConsoleOwnedTaskTabV19State = "V19_READINESS_FAILED_TAB_RETAINED";
    } else {
      try {
        counters.closeAttempted++;
        await tab.close();
        counters.closeFulfilled++;
        tab = null;
        secureConsoleOwnedTaskTabV19 = null;
        secureConsoleOwnedTaskTabV19Eligible = false;
        secureConsoleOwnedTaskTabV19State = "V19_READINESS_FAILED_CLEAN";
        cleanupState = "CREATED_TAB_CLOSED";
        residueConverged = true;
      } catch (cleanupError) {
        cleanupState = "CLOSE_FAILED_EXACT_HANDLE_RETAINED";
        residueConverged = false;
        secureConsoleOwnedTaskTabV19 = tab;
        secureConsoleOwnedTaskTabV19Eligible = false;
        secureConsoleOwnedTaskTabV19State = "V19_READINESS_FAILED_TAB_RETAINED";
      }
    }
  } else {
    cleanupState = "NO_TAB_CREATED";
    residueConverged = true;
    secureConsoleOwnedTaskTabV19State = "V19_READINESS_FAILED_CLEAN";
  }

  counters.writeAttempted++;
  nodeRepl.write({
    result,
    declarationShape,
    predecessorStateExact,
    controllerOwnership,
    tabShape,
    createdHandleCaptured,
    navigationTargetExact,
    placeholderSearchCount,
    baselineValidated,
    baselineSemanticExact,
    terminalValidated,
    terminalSemanticExact,
    prefillQueryInputExactCount,
    prefillEmptyMarkerCount,
    postfillQueryInputExactCount,
    createControlCount,
    tokenNameCount,
    matchingRowCount,
    filterComplete,
    tokenSemanticSignature,
    baseline,
    terminal,
    cleanupState,
    residueConverged,
    retainedExactHandle: secureConsoleOwnedTaskTabV19 !== null,
    eligible: secureConsoleOwnedTaskTabV19Eligible,
    stateExact:
      secureConsoleOwnedTaskTabV19State === "TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE_V19",
    ...counters,
    errorClass,
    consumed: secureConsoleV19ReadinessConsumed,
    v18BindingNull: secureConsoleOwnedTaskTabV18 === null,
    v18BindingIneligible: secureConsoleOwnedTaskTabV18Eligible === false,
    v18BindingStateExact:
      secureConsoleOwnedTaskTabV18State === "V18_READINESS_FAILED_CLEAN",
    v17BindingNull: secureConsoleOwnedTaskTabV17 === null,
    v17BindingIneligible: secureConsoleOwnedTaskTabV17Eligible === false,
    v17BindingStateExact:
      secureConsoleOwnedTaskTabV17State === "V17_READINESS_FAILED_CLEAN",
    v16BindingNull: secureConsoleOwnedTaskTabV16 === null,
    v16BindingIneligible: secureConsoleOwnedTaskTabV16Eligible === false,
    v16BindingStateExact:
      secureConsoleOwnedTaskTabV16State === "V16_READINESS_FAILED_CLEAN",
    v4BindingNull: secureConsoleOwnedTaskTabV4 === null,
    v4BindingIneligible: secureConsoleOwnedTaskTabV4Eligible === false,
    v4BindingStateExact:
      secureConsoleOwnedTaskTabV4State === "V9_OWNED_TAB_READINESS_FAILED_CLEAN",
  });
})();
```

## PASS and review gate

Exact PASS retains only the exact V19-created tab and marks only that handle
eligible for a separately committed and independently reviewed prestart read
contract. Every other disposition consumes V19 and follows the reviewed
cleanup state machine.

Before the sole call, revalidate exact committed brief/executable/review and
classification bytes, direct-parent and one-path shapes, the separate
post-commit tuple, source projection, empty index, exact 12-path dirty
baseline, installed Chrome runtime hashes, clean evidence worktree, zero
temporary/process residue, VM1205 safe state, public DNS absence, exact
persistent V18-through-V4 bindings, and every V19 declaration absent.

Independent Sol High review must verify the root-cause correction, exact V18
incident ancestry, synchronous fixed-key query projection, serial native
terminal wait, inherited page signatures and completeness, output cardinality,
retention/cleanup, no secret/provider action, no retry, and both mandatory
confirmation boundaries.

`authorizes_live_execution=false`

