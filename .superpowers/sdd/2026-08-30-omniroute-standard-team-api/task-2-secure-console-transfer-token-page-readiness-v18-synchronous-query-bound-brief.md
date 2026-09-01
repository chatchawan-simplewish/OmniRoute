# OmniRoute V18 synchronous query-bound readiness replacement brief

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Root cause and consumed-gate boundary

V16 and V17 were each consumed once and failed clean at the same terminal
locator-evaluate boundary. V17's explicit `timeoutMs: 25000` did not change
the attempted/not-fulfilled result, disproving the transport-timeout hypothesis.
Both exact tabs closed once with converged residue; no later read, provider
mutation, secret action, or retained handle occurred. Neither gate may ever be
retried, continued, reinterpreted, or invoked.

The installed Chrome API documents locator `evaluate` as a read-only scope.
Earlier independently reviewed project evidence at fix-round-2
`080f9bec66a3b8f94b93e59e0c5e5463d9695401` rejected page-resident
`MutationObserver`, timer, Promise, and asynchronous-evaluate state. The
fix-round-4 Sol High PASS at
`139c0b971d120647c319d3b5b5672aca67f94db9` requires synchronous read-only
snapshots plus serial native locator `waitFor` calls. V16/V17 violated that
known runtime boundary by running an asynchronous locator evaluator containing
a `MutationObserver`, page timer, and Promise. Their immediate identical
rejections are consistent with that violation.

## Design decision

V18 removes every asynchronous evaluator, `MutationObserver`, page timer,
page Promise, performance clock, expando, and cross-evaluate page state. It
uses only synchronous read-only snapshots and serial native locator calls.

Causal completeness is not relaxed. A fresh exact baseline proves the fixed
target text and the exact empty marker are both absent before the single fill.
After the fill, V18 waits serially for the exact visible query echo and one
exact visible V4 empty-result marker (`No API Tokens Found` or
`No Tokens Found`). A final synchronous snapshot requires the exact input,
section/page tuple, one marker, no busy state, zero visible candidate rows, and
zero matching target rows. This absent-before/present-after query-bound UI
transition replaces the rejected time-based page observer while preserving the
V4 semantic signature.

Repeated controller snapshots, relaxed stability predicates, alternate tabs,
and any V16/V17 retry are rejected.

## Exact inherited boundary

V18 preserves the fixed public URL, fixed non-secret target, one fresh owned
tab, one navigation, one fill, exact V15 baseline, fixed-key cross-realm trusted
projection, exact Create/name/row semantics, success retention, fail-closed
cleanup, no secrets, no provider mutation, no retry/fallback, and every
mandatory final Create/native Copy/native masked Paste and later separate
exact-row deletion confirmation.

It adds the exact consumed-failed-clean V17 and V16 null/ineligible/no-detach/
no-read predecessor tuples. Any missing, rejected, timed-out, truncated,
malformed, uncertain, or non-PASS result spends V18 permanently.

## One-shot V18 executable

The sole Sol High owner may run this exact cell once in the same persistent
Node session only after independent Sol High PASS review, non-self-referential
classification, separate post-commit coordinator tuple, and all fresh
action-time pins pass.

```javascript
let secureConsoleOwnedTaskTabV18 = null;
let secureConsoleOwnedTaskTabV18Eligible = false;
let secureConsoleOwnedTaskTabV18State = "UNCREATED";
let secureConsoleOwnedTaskTabV18PreCreateDetachConsumed = false;
let secureConsoleOwnedTaskTabV18PostNativeDetachConsumed = false;
let secureConsoleCloudflareReadsV18Consumed = false;
let secureConsoleV18ReadinessConsumed = false;
await (async () => {
  const gateWasFresh = secureConsoleV18ReadinessConsumed === false;
  secureConsoleV18ReadinessConsumed = true;
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
    prefillEchoAttempted: 0, prefillEchoFulfilled: 0,
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
  let prefillTargetTextCount = -1;
  let prefillEmptyMarkerCount = -1;
  let tokenQueryEchoCount = -1;
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
      typeof secureConsoleV17ReadinessConsumed === "boolean" &&
      typeof secureConsoleV16ReadinessConsumed === "boolean" &&
      typeof secureConsoleV15StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV14StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV13StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV12StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV11StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV10StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV9ReadinessConsumed === "boolean" &&
      typeof secureConsoleV18ReadinessConsumed === "boolean";
    if (!declarationShape) throw new Error("ReadinessDeclarationShapeError");
    predecessorStateExact =
      gateWasFresh === true &&
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
      secureConsoleOwnedTaskTabV18 === null &&
      secureConsoleOwnedTaskTabV18Eligible === false &&
      secureConsoleOwnedTaskTabV18State === "UNCREATED" &&
      secureConsoleOwnedTaskTabV18PreCreateDetachConsumed === false &&
      secureConsoleOwnedTaskTabV18PostNativeDetachConsumed === false &&
      secureConsoleCloudflareReadsV18Consumed === false;
    if (!predecessorStateExact) throw new Error("ReadinessPredecessorStateError");

    counters.newAttempted++;
    secureConsoleOwnedTaskTabV18 = tab = await secureConsoleChromeV5.tabs.new();
    counters.newFulfilled++;
    createdHandleCaptured = typeof tab === "object" && tab !== null;
    if (!createdHandleCaptured) throw new Error("ReadinessCreatedHandleError");
    controllerOwnership = secureConsoleOwnedTaskTabV18 === tab;
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

    const tokenQueryEcho = tokenSection.getByText("OmniRoute secure console R5 20260901", { exact: true });
    const terminalEmptyStatus = tokenSection.getByRole("status").filter({
      hasText: /^(?:No API Tokens Found|No Tokens Found)$/i,
    });
    const terminalEmptyRow = tokenSection.getByRole("row").filter({
      hasText: /^(?:No API Tokens Found|No Tokens Found)$/i,
    });
    if (typeof tokenQueryEcho?.waitFor !== "function" ||
        typeof tokenQueryEcho?.count !== "function" ||
        typeof terminalEmptyStatus?.or !== "function") {
      throw new Error("ReadinessTerminalLocatorShapeError");
    }
    const terminalMarker = terminalEmptyStatus.or(terminalEmptyRow);
    if (typeof terminalMarker?.waitFor !== "function" ||
        typeof terminalMarker?.count !== "function") {
      throw new Error("ReadinessTerminalMarkerShapeError");
    }
    counters.prefillEchoAttempted++;
    prefillTargetTextCount = await tokenQueryEcho.count();
    counters.prefillEchoFulfilled++;
    counters.prefillMarkerAttempted++;
    prefillEmptyMarkerCount = await terminalMarker.count();
    counters.prefillMarkerFulfilled++;
    if (prefillTargetTextCount !== 0 || prefillEmptyMarkerCount !== 0) {
      throw new Error("ReadinessPrefillMarkerStateError");
    }

    counters.fillAttempted++;
    await tokenFilter.fill("OmniRoute secure console R5 20260901");
    counters.fillFulfilled++;

    counters.queryAttempted++;
    await tokenQueryEcho.waitFor({ state: "visible", timeoutMs: 20000 });
    tokenQueryEchoCount = await tokenQueryEcho.count();
    counters.queryFulfilled++;
    if (tokenQueryEchoCount !== 1) throw new Error("ReadinessQueryEchoCountError");

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
      prefillTargetTextCount === 0 &&
      prefillEmptyMarkerCount === 0 &&
      terminal.inputValueExact === true &&
      terminal.queryInputExactCount === 1 &&
      tokenQueryEchoCount === 1 &&
      terminal.terminalMarkerCount === 1 &&
      terminal.terminalObserved === true;
    tokenSemanticSignature =
      navigationTargetExact === true &&
      baselineSemanticExact === true &&
      terminalSemanticExact === true &&
      createControlCount === 1 &&
      tokenQueryEchoCount === 1 &&
      tokenNameCount === 0 &&
      matchingRowCount === 0 &&
      terminal.matchingRowCount === 0 &&
      filterComplete === true;
    if (!tokenSemanticSignature) throw new Error("AuthenticatedTokenPageSemanticStateError");
    result = "V18_TOKEN_PAGE_SEMANTIC_READINESS_BODY_COMPLETE";
  } catch (error) {
    errorClass = safeErrorClass(error);
  }

  if (result === "V18_TOKEN_PAGE_SEMANTIC_READINESS_BODY_COMPLETE") {
    secureConsoleOwnedTaskTabV18 = tab;
    secureConsoleOwnedTaskTabV18Eligible = true;
    secureConsoleOwnedTaskTabV18State = "TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE_V18";
    cleanupState = "SUCCESS_TAB_RETAINED";
    residueConverged = true;
    result = "EXACT_V18_TOKEN_PAGE_SEMANTIC_READINESS_PASS";
  } else if (counters.newAttempted === 1 && counters.newFulfilled === 0) {
    cleanupState = "NEW_REJECTED_RESIDUE_UNPROVEN";
    residueConverged = false;
    secureConsoleOwnedTaskTabV18State = "V18_READINESS_FAILED_RESIDUE_UNPROVEN";
  } else if (counters.newFulfilled === 1 && createdHandleCaptured === false) {
    cleanupState = "NEW_FULFILLED_WITHOUT_HANDLE_RESIDUE_UNPROVEN";
    residueConverged = false;
    secureConsoleOwnedTaskTabV18State = "V18_READINESS_FAILED_RESIDUE_UNPROVEN";
  } else if (tab !== null && tab !== undefined) {
    if (typeof tab.close !== "function") {
      cleanupState = "MALFORMED_EXACT_HANDLE_RETAINED";
      residueConverged = false;
      secureConsoleOwnedTaskTabV18 = tab;
      secureConsoleOwnedTaskTabV18Eligible = false;
      secureConsoleOwnedTaskTabV18State = "V18_READINESS_FAILED_TAB_RETAINED";
    } else {
      try {
        counters.closeAttempted++;
        await tab.close();
        counters.closeFulfilled++;
        tab = null;
        secureConsoleOwnedTaskTabV18 = null;
        secureConsoleOwnedTaskTabV18Eligible = false;
        secureConsoleOwnedTaskTabV18State = "V18_READINESS_FAILED_CLEAN";
        cleanupState = "CREATED_TAB_CLOSED";
        residueConverged = true;
      } catch (cleanupError) {
        cleanupState = "CLOSE_FAILED_EXACT_HANDLE_RETAINED";
        residueConverged = false;
        secureConsoleOwnedTaskTabV18 = tab;
        secureConsoleOwnedTaskTabV18Eligible = false;
        secureConsoleOwnedTaskTabV18State = "V18_READINESS_FAILED_TAB_RETAINED";
      }
    }
  } else {
    cleanupState = "NO_TAB_CREATED";
    residueConverged = true;
    secureConsoleOwnedTaskTabV18State = "V18_READINESS_FAILED_CLEAN";
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
    prefillTargetTextCount,
    prefillEmptyMarkerCount,
    tokenQueryEchoCount,
    createControlCount,
    tokenNameCount,
    matchingRowCount,
    filterComplete,
    tokenSemanticSignature,
    baseline,
    terminal,
    cleanupState,
    residueConverged,
    retainedExactHandle: secureConsoleOwnedTaskTabV18 !== null,
    eligible: secureConsoleOwnedTaskTabV18Eligible,
    stateExact:
      secureConsoleOwnedTaskTabV18State === "TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE_V18",
    ...counters,
    errorClass,
    consumed: secureConsoleV18ReadinessConsumed,
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

PASS requires `EXACT_V18_TOKEN_PAGE_SEMANTIC_READINESS_PASS`; exact fresh
baseline; prefill target/marker counts `0/0`; post-fill visible query echo
count `1`; visible terminal-marker count `1`; synchronous terminal schema
and semantics; one actionable `Create Token`; zero target name/row matches;
exact counters; retained eligible V18 handle; exact failed-clean V17/V16 tuples;
and unchanged exact V4 tuple.

The Sol High reviewer must verify the root-cause evidence; zero asynchronous
evaluate/observer/timer/page-Promise state; exactly two synchronous evaluator
calls; exact absent-before/present-after query binding; serial native waits;
fixed output and cross-realm projection; cleanup; no secret/provider mutation;
and all inherited confirmations.

Immediately before the sole call, revalidate exact committed bytes, review,
classification/tuple, source projection, empty index, exact 12-path baseline,
runtime, evidence-worktree, residue, VM1205, DNS, persistent V17-through-V4
bindings, and absent V18 declarations.

`authorizes_live_execution=false`
