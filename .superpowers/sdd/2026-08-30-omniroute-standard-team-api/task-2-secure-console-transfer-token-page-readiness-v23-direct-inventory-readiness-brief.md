# OmniRoute V23 direct-inventory readiness replacement brief

`authorizes_live_execution=false`

This is a new fresh-session, one-shot readiness-only contract. It performs no
fill, keypress, click, submit, Create, provider-persistent mutation, credential
read, clipboard operation, VM mutation, DNS change, routing change, listener
start, or process start. It does not invoke, reuse, continue, or reinterpret
consumed V20, V19, V18, V17, V16, V3, or any earlier gate. V21 and V22 were
never evaluated and every one of their persistent declarations must remain
absent.

## Root cause and predecessor boundary

V20 is immutable and consumed-failed-clean at incident commit
`237ca08aa206deac4c642bdd7dd69c5c673e6739`. It proved the exact authenticated
page baseline, an empty unique search input, zero empty marker, five visible
candidate rows, exact non-secret fill value, and then failed cleanly because the
candidate set did not settle.

The two proposed Enter replacements were rejected before execution:

- V21 Sol High FAIL review commit:
  `b48d557bc8a48eee13ed60dfa7c0b8917a18b748`;
- V22 brief commit:
  `be0f466e28df313e7aeab153481e92b52745de24`;
- V22 Sol High FAIL review commit:
  `9f8340c2e9f9209d52beb205e0115e6f5e14c324`;
- V22 review path:
  `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-token-page-readiness-v22-guarded-search-activation-sol-review.md`;
- V22 review bytes: `11451`;
- V22 review SHA-256:
  `830093CF1CF35809F3D94D21F9DF7CFCB57FA7194AC080EF19181598F5B0A0EA`;
- V22 review blob: `30f550112e66ed496022e5f87fe83b7347113080`;
- unresolved HIGH `V22-001`: any real Enter event can invoke an unproven
  application handler with same-URL AJAX/provider effects.

V21 and V22 are static failed-review evidence only. Neither is consumed, and
neither is retried, continued, or reinterpreted.

## Design decision

V23 removes the Enter hypothesis and every query mutation. It uses only a fresh
owned tab, exact navigation, synchronous fixed-key DOM projection, locator
counts, and exact cleanup/retention. It directly proves the current unfiltered
inventory is complete for this page by requiring the inherited V4/V15
authenticated signature, exactly five visible table rows, zero pagination,
zero busy state, one empty visible search input, zero empty-result marker, and
five visible non-empty candidate rows.

Against that complete unfiltered inventory, it requires one global actionable
exact `Create Token`, zero exact target-name matches, and zero target-matching
rows. No filter activation is needed to establish target absence. This removes
the only unbounded application-event path from V21/V22.

There is no fill, keypress, click, page-resident timer, observer, Promise, async
evaluator, expando, background work, polling loop, retry, fallback, manual
integration, or verdict relaxation.

## Exact inherited boundary

V23 preserves the V20 fresh-tab, exact navigation, structural baseline,
prefill marker and five-candidate proof, V4/V15 page signatures,
Create/name/row completeness, fixed-key cross-realm validation, exact success
retention, fail-closed cleanup, fixed safe output, secret exclusions,
no-residue/no-retry rules, and both mandatory confirmation boundaries.

V23 requires the exact consumed-failed-clean V20 through V16
null/ineligible/no-detach/no-read predecessor bindings, all earlier retained
null bindings, the exact V4 state, and every V21/V22 declaration absent. The
mandatory final Create/native Copy/native masked Paste confirmation and later
separate exact-row deletion confirmation remain unreached and mandatory.

## One-shot V23 executable

```javascript
let secureConsoleOwnedTaskTabV23 = null;
let secureConsoleOwnedTaskTabV23Eligible = false;
let secureConsoleOwnedTaskTabV23State = "UNCREATED";
let secureConsoleOwnedTaskTabV23PreCreateDetachConsumed = false;
let secureConsoleOwnedTaskTabV23PostNativeDetachConsumed = false;
let secureConsoleCloudflareReadsV23Consumed = false;
let secureConsoleV23ReadinessConsumed = false;
await (async () => {
  const gateWasFresh = secureConsoleV23ReadinessConsumed === false;
  secureConsoleV23ReadinessConsumed = true;
  const counters = {
    newAttempted: 0, newFulfilled: 0,
    navigationAttempted: 0, navigationFulfilled: 0,
    urlAttempted: 0, urlFulfilled: 0,
    waitAttempted: 0, waitFulfilled: 0,
    countAttempted: 0, countFulfilled: 0,
    scopeAttempted: 0, scopeFulfilled: 0,
    baselineAttempted: 0, baselineFulfilled: 0,
    prefillMarkerAttempted: 0, prefillMarkerFulfilled: 0,
    candidateAttempted: 0, candidateFulfilled: 0,
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
  let prefillQueryInputExactCount = -1;
  let prefillEmptyMarkerCount = -1;
  let prefillVisibleCandidateRowCount = -1;
  let createControlCount = -1;
  let tokenNameCount = -1;
  let matchingRowCount = -1;
  let inventoryComplete = false;
  let tokenSemanticSignature = false;
  let baseline = emptyBaseline();
  let cleanupState = "NO_TAB_CREATED";
  let residueConverged = true;
  let errorClass = "NONE";
  let tab = null;
  try {
    declarationShape =
      typeof secureConsoleChromeV5 === "object" &&
      secureConsoleChromeV5 !== null &&
      typeof secureConsoleChromeV5.tabs?.new === "function" &&
      typeof secureConsoleV20ReadinessConsumed === "boolean" &&
      typeof secureConsoleV19ReadinessConsumed === "boolean" &&
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
      typeof secureConsoleV21ReadinessConsumed === "undefined" &&
      typeof secureConsoleOwnedTaskTabV21 === "undefined" &&
      typeof secureConsoleOwnedTaskTabV21Eligible === "undefined" &&
      typeof secureConsoleOwnedTaskTabV21State === "undefined" &&
      typeof secureConsoleOwnedTaskTabV21PreCreateDetachConsumed === "undefined" &&
      typeof secureConsoleOwnedTaskTabV21PostNativeDetachConsumed === "undefined" &&
      typeof secureConsoleCloudflareReadsV21Consumed === "undefined" &&
      typeof secureConsoleV22ReadinessConsumed === "undefined" &&
      typeof secureConsoleOwnedTaskTabV22 === "undefined" &&
      typeof secureConsoleOwnedTaskTabV22Eligible === "undefined" &&
      typeof secureConsoleOwnedTaskTabV22State === "undefined" &&
      typeof secureConsoleOwnedTaskTabV22PreCreateDetachConsumed === "undefined" &&
      typeof secureConsoleOwnedTaskTabV22PostNativeDetachConsumed === "undefined" &&
      typeof secureConsoleCloudflareReadsV22Consumed === "undefined" &&
      typeof secureConsoleV23ReadinessConsumed === "boolean";
    if (!declarationShape) throw new Error("ReadinessDeclarationShapeError");
    predecessorStateExact =
      gateWasFresh === true &&
      secureConsoleV20ReadinessConsumed === true &&
      secureConsoleOwnedTaskTabV20 === null &&
      secureConsoleOwnedTaskTabV20Eligible === false &&
      secureConsoleOwnedTaskTabV20State === "V20_READINESS_FAILED_CLEAN" &&
      secureConsoleOwnedTaskTabV20PreCreateDetachConsumed === false &&
      secureConsoleOwnedTaskTabV20PostNativeDetachConsumed === false &&
      secureConsoleCloudflareReadsV20Consumed === false &&
      secureConsoleV19ReadinessConsumed === true &&
      secureConsoleOwnedTaskTabV19 === null &&
      secureConsoleOwnedTaskTabV19Eligible === false &&
      secureConsoleOwnedTaskTabV19State === "V19_READINESS_FAILED_CLEAN" &&
      secureConsoleOwnedTaskTabV19PreCreateDetachConsumed === false &&
      secureConsoleOwnedTaskTabV19PostNativeDetachConsumed === false &&
      secureConsoleCloudflareReadsV19Consumed === false &&
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
      secureConsoleOwnedTaskTabV23 === null &&
      secureConsoleOwnedTaskTabV23Eligible === false &&
      secureConsoleOwnedTaskTabV23State === "UNCREATED" &&
      secureConsoleOwnedTaskTabV23PreCreateDetachConsumed === false &&
      secureConsoleOwnedTaskTabV23PostNativeDetachConsumed === false &&
      secureConsoleCloudflareReadsV23Consumed === false;
    if (!predecessorStateExact) throw new Error("ReadinessPredecessorStateError");

    counters.newAttempted++;
    secureConsoleOwnedTaskTabV23 = tab = await secureConsoleChromeV5.tabs.new();
    counters.newFulfilled++;
    createdHandleCaptured = typeof tab === "object" && tab !== null;
    if (!createdHandleCaptured) throw new Error("ReadinessCreatedHandleError");
    controllerOwnership = secureConsoleOwnedTaskTabV23 === tab;
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
    const visibleCandidateRows = tokenSection.locator("tbody tr").filter({
      hasNotText: /^(?:No API Tokens Found|No Tokens Found)$/i,
      visible: true,
    });
    if (typeof terminalMarker?.count !== "function" ||
        typeof visibleCandidateRows?.count !== "function") {
      throw new Error("ReadinessInventoryLocatorShapeError");
    }
    prefillQueryInputExactCount =
      baseline.inputValueEmpty === true && baseline.sectionSearchCount === 1 ? 0 : -1;
    counters.prefillMarkerAttempted++;
    prefillEmptyMarkerCount = await terminalMarker.count();
    counters.prefillMarkerFulfilled++;
    counters.candidateAttempted++;
    prefillVisibleCandidateRowCount = await visibleCandidateRows.count();
    counters.candidateFulfilled++;
    if (prefillQueryInputExactCount !== 0 ||
        prefillEmptyMarkerCount !== 0 ||
        prefillVisibleCandidateRowCount !== 5) {
      throw new Error("ReadinessPrefillMarkerStateError");
    }

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
    inventoryComplete =
      baseline.inputValueEmpty === true &&
      baseline.pagePaginationCount === 0 &&
      baseline.pageBusyCount === 0 &&
      baseline.sectionRowCount === 5 &&
      baseline.sectionVisibleRowCount === 5 &&
      baseline.sectionBusyCount === 0 &&
      prefillQueryInputExactCount === 0 &&
      prefillEmptyMarkerCount === 0 &&
      prefillVisibleCandidateRowCount === 5;
    tokenSemanticSignature =
      navigationTargetExact === true &&
      baselineSemanticExact === true &&
      createControlCount === 1 &&
      tokenNameCount === 0 &&
      matchingRowCount === 0 &&
      inventoryComplete === true;
    if (!tokenSemanticSignature) throw new Error("AuthenticatedTokenPageSemanticStateError");
    result = "V23_TOKEN_PAGE_SEMANTIC_READINESS_BODY_COMPLETE";
  } catch (error) {
    errorClass = safeErrorClass(error);
  }

  if (result === "V23_TOKEN_PAGE_SEMANTIC_READINESS_BODY_COMPLETE") {
    secureConsoleOwnedTaskTabV23 = tab;
    secureConsoleOwnedTaskTabV23Eligible = true;
    secureConsoleOwnedTaskTabV23State = "TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE_V23";
    cleanupState = "SUCCESS_TAB_RETAINED";
    residueConverged = true;
    result = "EXACT_V23_TOKEN_PAGE_SEMANTIC_READINESS_PASS";
  } else if (counters.newAttempted === 1 && counters.newFulfilled === 0) {
    cleanupState = "NEW_REJECTED_RESIDUE_UNPROVEN";
    residueConverged = false;
    secureConsoleOwnedTaskTabV23State = "V23_READINESS_FAILED_RESIDUE_UNPROVEN";
  } else if (counters.newFulfilled === 1 && createdHandleCaptured === false) {
    cleanupState = "NEW_FULFILLED_WITHOUT_HANDLE_RESIDUE_UNPROVEN";
    residueConverged = false;
    secureConsoleOwnedTaskTabV23State = "V23_READINESS_FAILED_RESIDUE_UNPROVEN";
  } else if (tab !== null && tab !== undefined) {
    if (typeof tab.close !== "function") {
      cleanupState = "MALFORMED_EXACT_HANDLE_RETAINED";
      residueConverged = false;
      secureConsoleOwnedTaskTabV23 = tab;
      secureConsoleOwnedTaskTabV23Eligible = false;
      secureConsoleOwnedTaskTabV23State = "V23_READINESS_FAILED_TAB_RETAINED";
    } else {
      try {
        counters.closeAttempted++;
        await tab.close();
        counters.closeFulfilled++;
        tab = null;
        secureConsoleOwnedTaskTabV23 = null;
        secureConsoleOwnedTaskTabV23Eligible = false;
        secureConsoleOwnedTaskTabV23State = "V23_READINESS_FAILED_CLEAN";
        cleanupState = "CREATED_TAB_CLOSED";
        residueConverged = true;
      } catch (cleanupError) {
        cleanupState = "CLOSE_FAILED_EXACT_HANDLE_RETAINED";
        residueConverged = false;
        secureConsoleOwnedTaskTabV23 = tab;
        secureConsoleOwnedTaskTabV23Eligible = false;
        secureConsoleOwnedTaskTabV23State = "V23_READINESS_FAILED_TAB_RETAINED";
      }
    }
  } else {
    cleanupState = "NO_TAB_CREATED";
    residueConverged = true;
    secureConsoleOwnedTaskTabV23State = "V23_READINESS_FAILED_CLEAN";
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
    prefillQueryInputExactCount,
    prefillEmptyMarkerCount,
    prefillVisibleCandidateRowCount,
    createControlCount,
    tokenNameCount,
    matchingRowCount,
    inventoryComplete,
    tokenSemanticSignature,
    baseline,
    cleanupState,
    residueConverged,
    retainedExactHandle: secureConsoleOwnedTaskTabV23 !== null,
    eligible: secureConsoleOwnedTaskTabV23Eligible,
    stateExact:
      secureConsoleOwnedTaskTabV23State === "TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE_V23",
    ...counters,
    errorClass,
    consumed: secureConsoleV23ReadinessConsumed,
    v20BindingNull: secureConsoleOwnedTaskTabV20 === null,
    v20BindingIneligible: secureConsoleOwnedTaskTabV20Eligible === false,
    v20BindingStateExact:
      secureConsoleOwnedTaskTabV20State === "V20_READINESS_FAILED_CLEAN",
    v19BindingNull: secureConsoleOwnedTaskTabV19 === null,
    v19BindingIneligible: secureConsoleOwnedTaskTabV19Eligible === false,
    v19BindingStateExact:
      secureConsoleOwnedTaskTabV19State === "V19_READINESS_FAILED_CLEAN",
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

Exact PASS retains only the exact V23-created tab and marks only that handle
eligible for a separately committed and independently reviewed prestart read
contract. Every other disposition consumes V23 and follows the reviewed
cleanup state machine.

Before the sole call, revalidate exact committed brief/executable/review and
classification bytes, direct-parent and one-path shapes, the separate
post-commit tuple, source projection, empty index, exact 12-path dirty
baseline, installed Chrome runtime hashes, clean evidence worktree, zero
temporary/process residue, VM1205 safe state, public DNS absence, exact
persistent V20-through-V4 bindings, every V21/V22 declaration absent, and
every V23 declaration absent.

Independent Sol High review must verify the consumed V20 and static
failed-review V21/V22 boundaries; declaration absence; direct unfiltered
inventory completeness from exact five visible rows plus zero pagination/busy
state; V4/V15 authenticated page signature; exact Create/name/row counts;
zero fill/keypress/click/submit/provider mutation; synchronous fixed-key output;
call cardinality; retention/cleanup; secret/no-retry rules; and both mandatory
confirmation boundaries.

`authorizes_live_execution=false`
