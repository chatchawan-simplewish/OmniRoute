# OmniRoute V16 structural token-page readiness — execution brief

Status: **PROPOSED — not executable until independent Sol High PASS review,
non-self-referential classification, post-commit tuple, and fresh action-time
pins**

`authorizes_live_execution=false`

## Selected design

Three bounded approaches were considered:

1. **Direct structural readiness, selected.** Bind the fresh tab to the exact
   V15 page structure, perform the one inherited non-secret token-name filter,
   prove terminal zero matching rows without pagination or busy state, and
   retain the exact tab only on PASS.
2. Add another post-filter diagnostic before readiness. This adds another
   one-shot review/consumption chain without resolving an identified safety
   ambiguity because the terminal predicate can validate all allowed DOM
   variants inside one bounded readiness wait.
3. Reuse V4's `aria-controls` and paginator assumptions. V15 proved those
   markers absent on the current page, so this would knowingly spend a gate on
   a stale contract.

The project standing rule pre-approves the safest recommended routine design.
Approach 1 is the smallest design that preserves V4's semantic protections
while using only structure V15 directly proved.

## Exact predecessor and evidence

V15 was consumed exactly once and returned
`EXACT_V15_STRUCTURAL_DIAGNOSTIC_PASS`. Sanitized live evidence is committed at
`c0127cc5340a44958853cb3bc871527632edb72a` in exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-token-page-readiness-v15-live-report.md`,
bytes `4381`, SHA-256
`0123216F0C2E042128BA04574D3B14BB3DA952BF0732D7D1D7B3785C3AF25725`,
blob `8dc8c73e9397b4c0ce9039fae27b1a0e2bfbc1e4`.

The immutable V15 result proved:

- exact URL, unique visible empty placeholder-search input, and current
  controller ownership;
- two page tables, no grid, pagination, or busy marker;
- the nearest section at input-parent depth `3`, containing one search input,
  one table, one table body, five rows, and no busy, status, empty-status, or
  Create-like actionable control;
- one exact actionable `Create Token` control globally;
- the installed bridge cross-realm plain-record predicate; and
- exact created-tab close with converged residue and null retained V15 handle.

V15 is spent. V16 never invokes, continues, resets, reinterprets, reuses,
retries, or falls back to V15 or V4.

## Inherited boundary without relaxation

V16 inherits every fixed target, token name, permission, secret exclusion,
confirmation, revocation hold, cleanup rule, and downstream ordering constraint
from V4 and the reviewed secure-console chain. In particular:

- fixed public navigation target only:
  `https://dash.cloudflare.com/profile/api-tokens`;
- fixed non-secret filter value only:
  `OmniRoute secure console R5 20260901`;
- no title read, tabs list, reconnect, alternate-tab selection, screenshot,
  clipboard operation, keyboard operation, Create/edit/delete click, provider
  mutation, cookie/storage/session read, retry, or fallback;
- any missing, rejected, timed-out, truncated, malformed, uncertain, or
  non-PASS invocation spends V16 permanently;
- on non-PASS after exact tab creation, close only that exact handle once;
  close uncertainty retains the exact handle and cannot claim clean residue;
- on exact PASS, retain only that exact handle in the V16 binding for the later
  separately reviewed prestart read; and
- the mandatory final Create/native Copy/native masked Paste confirmation and
  later separate exact-row deletion confirmation remain mandatory.

## One-shot V16 executable

The sole Sol High owner runs this exact cell once in the same persistent Node
session with fixed outer deadline `60000 ms`. The bounded page-local terminal
wait is `20000 ms` with `100 ms` observation intervals. Observation is not a
retry: the filter is filled once and no page or provider action is repeated.

```javascript
let secureConsoleOwnedTaskTabV16 = null;
let secureConsoleOwnedTaskTabV16Eligible = false;
let secureConsoleOwnedTaskTabV16State = "UNCREATED";
let secureConsoleOwnedTaskTabV16PreCreateDetachConsumed = false;
let secureConsoleOwnedTaskTabV16PostNativeDetachConsumed = false;
let secureConsoleCloudflareReadsV16Consumed = false;
let secureConsoleV16ReadinessConsumed = false;
await (async () => {
  const gateWasFresh = secureConsoleV16ReadinessConsumed === false;
  secureConsoleV16ReadinessConsumed = true;
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
    queryAttempted: 0, queryFulfilled: 0,
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
  const exactTypes = (value, booleanKeys, integerKeys) =>
    booleanKeys.every((key) => typeof value[key] === "boolean") &&
    integerKeys.every((key) => Number.isSafeInteger(value[key]));
  const integerRangeExact = (value, integerKeys) =>
    integerKeys.every((key) => value[key] >= -1 && value[key] <= 1000000);
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
      typeof secureConsoleV15StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV14StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV13StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV12StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV11StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV10StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV9ReadinessConsumed === "boolean" &&
      typeof secureConsoleV16ReadinessConsumed === "boolean";
    if (!declarationShape) throw new Error("ReadinessDeclarationShapeError");
    predecessorStateExact =
      gateWasFresh === true &&
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
      secureConsoleOwnedTaskTabV16 === null &&
      secureConsoleOwnedTaskTabV16Eligible === false &&
      secureConsoleOwnedTaskTabV16State === "UNCREATED" &&
      secureConsoleOwnedTaskTabV16PreCreateDetachConsumed === false &&
      secureConsoleOwnedTaskTabV16PostNativeDetachConsumed === false &&
      secureConsoleCloudflareReadsV16Consumed === false;
    if (!predecessorStateExact) throw new Error("ReadinessPredecessorStateError");

    counters.newAttempted++;
    secureConsoleOwnedTaskTabV16 = tab = await secureConsoleChromeV5.tabs.new();
    counters.newFulfilled++;
    createdHandleCaptured = typeof tab === "object" && tab !== null;
    if (!createdHandleCaptured) throw new Error("ReadinessCreatedHandleError");
    controllerOwnership = secureConsoleOwnedTaskTabV16 === tab;
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
    await tokenFilter.waitFor({ state: "visible", timeout: 10000 });
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
    const baselineExpectedKeys = [...baselineBooleanKeys, ...baselineIntegerKeys];
    baselineValidated =
      exactKeys(untrustedBaseline, baselineExpectedKeys) &&
      exactTypes(untrustedBaseline, baselineBooleanKeys, baselineIntegerKeys) &&
      integerRangeExact(untrustedBaseline, baselineIntegerKeys);
    if (!baselineValidated) throw new Error("ReadinessBaselineValidationError");
    baseline = { ...untrustedBaseline };
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

    counters.fillAttempted++;
    await tokenFilter.fill("OmniRoute secure console R5 20260901");
    counters.fillFulfilled++;

    counters.terminalAttempted++;
    const untrustedTerminal = await tokenFilter.evaluate(async (input) => {
      const target = "omniroute secure console r5 20260901";
      const normalize = (value) => (value || "").replace(/\s+/g, " ").trim().toLowerCase();
      const statusText = new Set(["no api tokens found", "no tokens found", "no results"]);
      const snapshot = () => {
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
        const visibleCandidateRows = visibleRows.filter((row) => !statusText.has(normalize(row.textContent)));
        return {
          terminalObserved: false,
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
          sectionEmptyStatusCount: statuses.filter((item) => statusText.has(normalize(item.textContent))).length,
          sectionTbodyCount: section === null ? -1 : section.querySelectorAll("tbody").length,
          sectionRowCount: section === null ? -1 : rows.length,
          sectionVisibleRowCount: section === null ? -1 : visibleRows.length,
          sectionVisibleCandidateRowCount: section === null ? -1 : visibleCandidateRows.length,
          sectionEmptyRowCount: section === null ? -1 : emptyRows.length,
          sectionBusyCount: section === null ? -1 : section.querySelectorAll('[aria-busy="true"], [role="progressbar"]').length,
          matchingRowCount: section === null ? -1 : rows.filter((row) => normalize(row.textContent).includes(target)).length,
        };
      };
      const terminalShape = (value) => {
        const rowShape =
          value.sectionRowCount === 0 ||
          (value.sectionRowCount === 5 && value.sectionVisibleRowCount === 0) ||
          (value.sectionRowCount === 1 && value.sectionEmptyRowCount === 1 &&
            value.sectionVisibleCandidateRowCount === 0);
        return value.inputConnected === true &&
          value.inputVisible === true &&
          value.inputValueExact === true &&
          value.queryInputExactCount === 1 &&
          value.sectionFound === true &&
          value.sectionDepth === 3 &&
          value.pageTableCount === 2 &&
          value.pageGridCount === 0 &&
          value.pagePaginationCount === 0 &&
          value.pageBusyCount === 0 &&
          value.sectionTableCount === 1 &&
          value.sectionSearchCount === 1 &&
          value.sectionStatusCount === value.sectionEmptyStatusCount &&
          value.sectionStatusCount >= 0 && value.sectionStatusCount <= 1 &&
          value.sectionTbodyCount === 1 &&
          value.sectionVisibleCandidateRowCount === 0 &&
          value.sectionEmptyRowCount >= 0 && value.sectionEmptyRowCount <= 1 &&
          value.sectionBusyCount === 0 &&
          value.matchingRowCount === 0 &&
          rowShape;
      };
      const deadline = Date.now() + 20000;
      let observed = snapshot();
      while (!terminalShape(observed) && Date.now() < deadline) {
        await new Promise((resolve) => setTimeout(resolve, 100));
        observed = snapshot();
      }
      return { ...observed, terminalObserved: terminalShape(observed) };
    });
    counters.terminalFulfilled++;
    const terminalBooleanKeys = [
      "terminalObserved", "inputConnected", "inputVisible", "inputValueExact",
      "sectionFound",
    ];
    const terminalIntegerKeys = [
      "queryInputExactCount", "sectionDepth", "pageTableCount", "pageGridCount",
      "pagePaginationCount", "pageBusyCount", "sectionTableCount",
      "sectionSearchCount", "sectionStatusCount", "sectionEmptyStatusCount",
      "sectionTbodyCount", "sectionRowCount", "sectionVisibleRowCount",
      "sectionVisibleCandidateRowCount", "sectionEmptyRowCount",
      "sectionBusyCount", "matchingRowCount",
    ];
    const terminalExpectedKeys = [...terminalBooleanKeys, ...terminalIntegerKeys];
    terminalValidated =
      exactKeys(untrustedTerminal, terminalExpectedKeys) &&
      exactTypes(untrustedTerminal, terminalBooleanKeys, terminalIntegerKeys) &&
      integerRangeExact(untrustedTerminal, terminalIntegerKeys);
    if (!terminalValidated) throw new Error("ReadinessTerminalValidationError");
    terminal = { ...untrustedTerminal };
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
      terminal.sectionTbodyCount === 1 &&
      terminal.sectionVisibleCandidateRowCount === 0 &&
      terminal.sectionEmptyRowCount >= 0 && terminal.sectionEmptyRowCount <= 1 &&
      terminal.sectionBusyCount === 0 &&
      terminal.matchingRowCount === 0 &&
      terminalRowShapeExact;
    if (!terminalSemanticExact) throw new Error("ReadinessTerminalSemanticError");

    counters.queryAttempted++;
    tokenQueryEchoCount = await tokenSection.getByText("OmniRoute secure console R5 20260901", { exact: true }).count();
    counters.queryFulfilled++;
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
      terminal.inputValueExact === true &&
      terminal.queryInputExactCount === 1 &&
      tokenQueryEchoCount === 1 &&
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
    result = "V16_TOKEN_PAGE_SEMANTIC_READINESS_BODY_COMPLETE";
  } catch (error) {
    errorClass = safeErrorClass(error);
  }

  if (result === "V16_TOKEN_PAGE_SEMANTIC_READINESS_BODY_COMPLETE") {
    secureConsoleOwnedTaskTabV16 = tab;
    secureConsoleOwnedTaskTabV16Eligible = true;
    secureConsoleOwnedTaskTabV16State = "TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE_V16";
    cleanupState = "SUCCESS_TAB_RETAINED";
    residueConverged = true;
    result = "EXACT_V16_TOKEN_PAGE_SEMANTIC_READINESS_PASS";
  } else if (tab !== null) {
    if (typeof tab.close !== "function") {
      cleanupState = "MALFORMED_EXACT_HANDLE_RETAINED";
      residueConverged = false;
      secureConsoleOwnedTaskTabV16 = tab;
      secureConsoleOwnedTaskTabV16Eligible = false;
      secureConsoleOwnedTaskTabV16State = "V16_READINESS_FAILED_TAB_RETAINED";
    } else {
      try {
        counters.closeAttempted++;
        await tab.close();
        counters.closeFulfilled++;
        tab = null;
        secureConsoleOwnedTaskTabV16 = null;
        secureConsoleOwnedTaskTabV16Eligible = false;
        secureConsoleOwnedTaskTabV16State = "V16_READINESS_FAILED_CLEAN";
        cleanupState = "CREATED_TAB_CLOSED";
        residueConverged = true;
      } catch (cleanupError) {
        cleanupState = "CLOSE_FAILED_EXACT_HANDLE_RETAINED";
        residueConverged = false;
        secureConsoleOwnedTaskTabV16 = tab;
        secureConsoleOwnedTaskTabV16Eligible = false;
        secureConsoleOwnedTaskTabV16State = "V16_READINESS_FAILED_TAB_RETAINED";
      }
    }
  } else if (counters.newAttempted === 1 && counters.newFulfilled === 0) {
    cleanupState = "NEW_REJECTED_RESIDUE_UNPROVEN";
    residueConverged = false;
    secureConsoleOwnedTaskTabV16State = "V16_READINESS_FAILED_RESIDUE_UNPROVEN";
  } else if (counters.newFulfilled === 1 && createdHandleCaptured === false) {
    cleanupState = "NEW_FULFILLED_WITHOUT_HANDLE_RESIDUE_UNPROVEN";
    residueConverged = false;
    secureConsoleOwnedTaskTabV16State = "V16_READINESS_FAILED_RESIDUE_UNPROVEN";
  } else {
    cleanupState = "NO_TAB_CREATED";
    residueConverged = true;
    secureConsoleOwnedTaskTabV16State = "V16_READINESS_FAILED_CLEAN";
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
    retainedExactHandle: secureConsoleOwnedTaskTabV16 !== null,
    eligible: secureConsoleOwnedTaskTabV16Eligible,
    stateExact:
      secureConsoleOwnedTaskTabV16State === "TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE_V16",
    ...counters,
    errorClass,
    consumed: secureConsoleV16ReadinessConsumed,
    v4BindingNull: secureConsoleOwnedTaskTabV4 === null,
    v4BindingIneligible: secureConsoleOwnedTaskTabV4Eligible === false,
    v4BindingStateExact:
      secureConsoleOwnedTaskTabV4State === "V9_OWNED_TAB_READINESS_FAILED_CLEAN",
  });
})();
```

## Exact PASS and failure semantics

PASS requires the fixed terminal
`EXACT_V16_TOKEN_PAGE_SEMANTIC_READINESS_PASS`; every declaration,
predecessor, ownership, tab-shape, navigation, baseline-validation,
baseline-semantic, terminal-validation, terminal-semantic, filter-complete, and
token-signature boolean true; placeholder/query-echo/Create counts `1/1/1`;
token-name/matching-row counts `0/0`; exact baseline
tuple `2` page tables, depth-`3` section, `1` table/body/search, `5` visible
rows, and zero grid/pagination/busy/status/Create-in-section markers; terminal
zero matching rows; exact counter cardinalities; fixed
success retention state; retained exact handle true; V16 eligibility true;
consumed true; and the unchanged V4 null/ineligible/state tuple.

The terminal row shape accepts only one of three equivalent complete filtered
representations: no rows; the five baseline rows retained but all hidden; or
one exact allowlisted empty-state row with no visible candidate row. Any status
marker must be zero or one and every such marker must have an exact allowlisted
empty-state meaning. No arbitrary page text is accepted or output.

Any non-PASS spends V16. If the exact created handle closes successfully, the
failure state is clean and null. A malformed handle, close rejection, new-tab
rejection, missing output, truncation, or uncertain tool status cannot be
reclassified as PASS and permits no retry, fallback, provider action, or manual
integration.

## Action-time pins and review gate

Before the sole V16 call, reproduce exact committed brief/executable bytes,
independent Sol High PASS review, non-self-referential classification and
post-commit tuple, source projection, empty index, exact 12-path dirty baseline,
installed browser runtime hashes, clean evidence worktree, zero temp/process
residue, VM1205 safe state, public DNS absence, and exact persistent predecessor
bindings with every V16 declaration still absent.

The independent Sol High reviewer must verify syntax; exact predecessor and
consumption order; cross-realm validation; the two page-local evaluators;
bounded terminal wait; exact semantic tuples; fixed-value-only output; call
cardinality; success retention; every failure cleanup branch; no secret sink;
no provider mutation; no retry/fallback; and all inherited confirmations.

`authorizes_live_execution=false`
