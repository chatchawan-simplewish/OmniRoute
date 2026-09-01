# Task 2 secure-console token-page readiness V13 validation-stage diagnostic brief

Date: 2026-09-02 (Asia/Bangkok)

## Purpose and boundary

V12 is consumed and failed cleanly after its unique visible-input count and
before diagnostic fulfillment. Its immutable incident is commit `5b56ce93f`.
V13 never retries or continues V12. It retains the same visible selector and
byte-identical page evaluator, while replacing throw-only controller validation
with safe boolean/integer stage evidence that distinguishes evaluator rejection
from shape, key, type, range, tuple, or sentinel failure.

V13 creates one controller-owned tab, navigates only to the fixed public token
URL, waits at most 10000 ms for the visible placeholder locator, evaluates one
bounded diagnostic, validates without emitting untrusted values or keys, and
closes that exact tab.
It does not fill, click, press, Create, edit, delete, inspect a generated
secret, use the clipboard, or mutate provider state.

Permitted output is limited to booleans and integer counts/depths for fixed
candidate predicates. No raw ID, URL, href, title, attribute value, page text,
DOM, HTML, screenshot, fingerprint, token, secret, credential, cookie, storage,
session, or clipboard content may be emitted.

## Diagnostic surface

The one page-local evaluation reports the unchanged 60 structural fields. The
controller additionally reports only: evaluator-returned, object/prototype,
exact-key, boolean-type, integer-type, integer-range, found-tuple,
missing-tuple, and count-sentinel booleans plus a capped key count.

- unique visible placeholder-input connection, visibility, and empty-value booleans;
- page table/grid/pagination/busy counts;
- nearest ancestor containing any table, nearest ancestor containing exactly
  one table, nearest ancestor containing exactly two tables, and nearest
  section/region metrics as bounded depths and descendant counts;
- table, search-input, status-role, recognized empty-status, `tbody`, body-row,
  busy, and Create-actionable counts inside the exact DOM-derived candidates;
- page-wide exact normalized-text counts for `Create Token`, `Create API Token`,
  and `Create`;
- matching actionable element, `aria-label`, same-origin fixed Create-path,
  API-token Create-like href-shape, and bounded data-marker counts.

Raw strings used for comparison remain inside the page evaluator and are never
returned. The controller treats the evaluator result as untrusted: it requires
one object with the exact 60-key allowlist, exact boolean types, safe integer
types/ranges, and consistent found/missing ancestor tuples, then copies only
those allowlisted fields into a new local object. Validation failure emits only
the fixed safe stage booleans and capped key count. V13 PASS authorizes only offline
interpretation and a new reviewed readiness contract.

## One-shot and no-residue contract

V13 contains exactly one `tabs.new()`, one fixed `goto()`, one bounded
`waitFor({ state: "visible", timeout: 10000 })`, one page-local `evaluate()`,
one `close()`, and one terminal write call site. The exact new
handle is assigned simultaneously to local and durable top-level state before
every later await. Diagnostic PASS requires completed exact close, null
retained handle, and converged residue. Any rejection, malformed value, close
failure, timeout, truncation, tool error, or uncertainty consumes V13 and
stops. A close failure retains the exact handle for a new reviewed disposition.
No retry, fallback, alternate tab, selected/list/get, reconnect, detach, or
cleanup improvisation is authorized.

## Executable cell

Execute at most once only after commit, independent Sol High PASS review,
non-self-referential classification, post-commit tuple, and fresh action-time
pins. The executable is complete only with its final LF.

Executable bytes: `20104`.

Executable SHA-256:
`FCB3EFCC7E066237EEBBD6D1A0688D086E4E7273868CAA94DD211012E21946D7`.

```javascript
let secureConsoleV13StructuralDiagnosticConsumed = false;
let secureConsoleV13RetainedTab = null;
await (async () => {
  const gateWasFresh = secureConsoleV13StructuralDiagnosticConsumed === false;
  secureConsoleV13StructuralDiagnosticConsumed = true;
  const counters = {
    newAttempted: 0, newFulfilled: 0,
    navigationAttempted: 0, navigationFulfilled: 0,
    urlAttempted: 0, urlFulfilled: 0,
    waitAttempted: 0, waitFulfilled: 0,
    countAttempted: 0, countFulfilled: 0,
    diagnosticAttempted: 0, diagnosticFulfilled: 0,
    closeAttempted: 0, closeFulfilled: 0,
    writeAttempted: 0,
  };
  const emptyStructure = () => ({
    inputConnected: false,
    inputVisible: false,
    inputValueEmpty: false,
    pageTableCount: -1,
    pageGridCount: -1,
    pagePaginationCount: -1,
    pageBusyCount: -1,
    firstAnyFound: false,
    firstAnyDepth: -1,
    firstAnyTableCount: -1,
    firstAnySearchCount: -1,
    firstAnyStatusCount: -1,
    firstAnyEmptyStatusCount: -1,
    firstAnyTbodyCount: -1,
    firstAnyRowCount: -1,
    firstAnyBusyCount: -1,
    firstAnyCreateActionableCount: -1,
    firstSingleFound: false,
    firstSingleDepth: -1,
    firstSingleTableCount: -1,
    firstSingleSearchCount: -1,
    firstSingleStatusCount: -1,
    firstSingleEmptyStatusCount: -1,
    firstSingleTbodyCount: -1,
    firstSingleRowCount: -1,
    firstSingleBusyCount: -1,
    firstSingleCreateActionableCount: -1,
    firstTwoFound: false,
    firstTwoDepth: -1,
    firstTwoTableCount: -1,
    firstTwoSearchCount: -1,
    firstTwoStatusCount: -1,
    firstTwoEmptyStatusCount: -1,
    firstTwoTbodyCount: -1,
    firstTwoRowCount: -1,
    firstTwoBusyCount: -1,
    firstTwoCreateActionableCount: -1,
    sectionFound: false,
    sectionDepth: -1,
    sectionTableCount: -1,
    sectionSearchCount: -1,
    sectionStatusCount: -1,
    sectionEmptyStatusCount: -1,
    sectionTbodyCount: -1,
    sectionRowCount: -1,
    sectionBusyCount: -1,
    sectionCreateActionableCount: -1,
    exactCreateTokenElementCount: -1,
    exactCreateApiTokenElementCount: -1,
    exactCreateElementCount: -1,
    createAndTokenElementCount: -1,
    exactCreateTokenActionableCount: -1,
    exactCreateApiTokenActionableCount: -1,
    exactCreateActionableCount: -1,
    createAndTokenActionableCount: -1,
    ariaLabelCreateTokenCount: -1,
    ariaLabelCreateApiTokenCount: -1,
    sameOriginExactCreatePathCount: -1,
    sameOriginCreateLikePathCount: -1,
    dataCreateMarkerCount: -1,
  });
  let structure = emptyStructure();
  let result = "PRECONDITION_FAIL";
  let errorClass = "NONE";
  let declarationShape = false;
  let predecessorStateExact = false;
  let controllerOwnership = false;
  let tabShape = false;
  let createdHandleCaptured = false;
  let navigationTargetExact = false;
  let placeholderSearchCount = -1;
  let evaluatorReturned = false;
  let resultObjectNonNull = false;
  let resultPrototypeObjectExact = false;
  let resultKeyCount = -1;
  let resultExactKeys = false;
  let resultBooleanTypesExact = false;
  let resultIntegerTypesExact = false;
  let resultIntegerRangesExact = false;
  let resultFoundTuplesExact = false;
  let resultMissingTuplesExact = false;
  let resultCountSentinelsExact = false;
  let cleanupState = "NOT_REQUIRED_NO_HANDLE";
  let failureResidueConverged = true;
  let tab = null;
  const safeErrorClass = (error) => {
    const name = typeof error?.name === "string" ? error.name : "StructuralDiagnosticError";
    return /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(name) ? name : "StructuralDiagnosticError";
  };
  try {
    declarationShape =
      typeof secureConsoleChromeV5 === "object" &&
      secureConsoleChromeV5 !== null &&
      typeof secureConsoleChromeV5.tabs?.new === "function" &&
      typeof secureConsoleV9ReadinessConsumed === "boolean" &&
      typeof secureConsoleV12StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV11StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV10StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV13StructuralDiagnosticConsumed === "boolean";
    if (!declarationShape) throw new Error("StructuralDeclarationShapeError");
    predecessorStateExact =
      gateWasFresh === true &&
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
      secureConsoleCloudflareReadsV4Consumed === false;
    if (!predecessorStateExact) throw new Error("StructuralPredecessorStateError");

    counters.newAttempted++;
    secureConsoleV13RetainedTab = tab = await secureConsoleChromeV5.tabs.new();
    counters.newFulfilled++;
    createdHandleCaptured = typeof tab === "object" && tab !== null;
    if (!createdHandleCaptured) {
      cleanupState = "NEW_FULFILLED_WITHOUT_TAB_HANDLE";
      failureResidueConverged = false;
      throw new Error("StructuralTabHandleCaptureError");
    }
    controllerOwnership = typeof tab.id === "string";
    tabShape =
      controllerOwnership &&
      typeof tab.close === "function" &&
      typeof tab.goto === "function" &&
      typeof tab.url === "function" &&
      typeof tab.playwright?.locator === "function";
    if (!tabShape) throw new Error("StructuralTabShapeError");

    counters.navigationAttempted++;
    await tab.goto("https://dash.cloudflare.com/profile/api-tokens");
    counters.navigationFulfilled++;
    counters.urlAttempted++;
    const diagnosticUrl = new URL(await tab.url());
    counters.urlFulfilled++;
    navigationTargetExact = diagnosticUrl.href === "https://dash.cloudflare.com/profile/api-tokens";
    if (!navigationTargetExact) throw new Error("StructuralNavigationTargetError");

    const tokenFilter = tab.playwright.locator('input[placeholder*="search" i]:visible');
    if (typeof tokenFilter?.waitFor !== "function") {
      throw new Error("StructuralFilterWaitShapeError");
    }
    counters.waitAttempted++;
    await tokenFilter.waitFor({ state: "visible", timeout: 10000 });
    counters.waitFulfilled++;
    counters.countAttempted++;
    placeholderSearchCount = await tokenFilter.count();
    counters.countFulfilled++;
    if (placeholderSearchCount !== 1) throw new Error("StructuralFilterCountError");

    counters.diagnosticAttempted++;
    const untrustedStructure = await tokenFilter.evaluate((input) => {
      const normalize = (value) => (value || "").replace(/\s+/g, " ").trim().toLowerCase();
      const statusText = new Set(["no api tokens found", "no tokens found", "no results"]);
      const actionSelector = 'button, a, [role="button"], [role="link"]';
      const metrics = (root, depth) => {
        if (root === null) {
          return {
            found: false, depth: -1, tableCount: -1, searchCount: -1,
            statusCount: -1, emptyStatusCount: -1, tbodyCount: -1,
            rowCount: -1, busyCount: -1, createActionableCount: -1,
          };
        }
        const statuses = [...root.querySelectorAll('[role="status"]')];
        const actions = [...root.querySelectorAll(actionSelector)];
        return {
          found: true,
          depth,
          tableCount: root.querySelectorAll("table").length,
          searchCount: root.querySelectorAll('input[placeholder*="search" i]').length,
          statusCount: statuses.length,
          emptyStatusCount: statuses.filter((node) => statusText.has(normalize(node.textContent))).length,
          tbodyCount: root.querySelectorAll("tbody").length,
          rowCount: root.querySelectorAll("tbody tr").length,
          busyCount: root.querySelectorAll('[aria-busy="true"], [role="progressbar"]').length,
          createActionableCount: actions.filter((node) => {
            const text = normalize(node.textContent);
            return text === "create token" || text === "create api token" || text === "create";
          }).length,
        };
      };
      let depth = 1;
      let node = input.parentElement;
      let firstAny = null;
      let firstSingle = null;
      let firstTwo = null;
      let section = null;
      let firstAnyDepth = -1;
      let firstSingleDepth = -1;
      let firstTwoDepth = -1;
      let sectionDepth = -1;
      while (node !== null && node !== document.body && depth <= 32) {
        const tables = node.querySelectorAll("table").length;
        if (firstAny === null && tables > 0) {
          firstAny = node;
          firstAnyDepth = depth;
        }
        if (firstSingle === null && tables === 1) {
          firstSingle = node;
          firstSingleDepth = depth;
        }
        if (firstTwo === null && tables === 2) {
          firstTwo = node;
          firstTwoDepth = depth;
        }
        if (
          section === null &&
          (node.tagName === "SECTION" || ["region", "group"].includes(node.getAttribute("role")))
        ) {
          section = node;
          sectionDepth = depth;
        }
        node = node.parentElement;
        depth++;
      }
      const anyMetrics = metrics(firstAny, firstAnyDepth);
      const singleMetrics = metrics(firstSingle, firstSingleDepth);
      const twoMetrics = metrics(firstTwo, firstTwoDepth);
      const sectionMetrics = metrics(section, sectionDepth);
      const elements = [...document.querySelectorAll("body *")];
      const actions = [...document.querySelectorAll(actionSelector)];
      const anchors = [...document.querySelectorAll("a[href]")];
      const textCount = (text) => elements.filter((element) => normalize(element.textContent) === text).length;
      const actionCount = (predicate) => actions.filter((element) => predicate(normalize(element.textContent))).length;
      const safePathCount = (predicate) => anchors.filter((anchor) => {
        try {
          const parsed = new URL(anchor.getAttribute("href"), location.href);
          return parsed.origin === location.origin && predicate(parsed.pathname);
        } catch {
          return false;
        }
      }).length;
      return {
        inputConnected: input.isConnected === true,
        inputVisible: input.getClientRects().length === 1,
        inputValueEmpty: input.value === "",
        pageTableCount: document.querySelectorAll("table").length,
        pageGridCount: document.querySelectorAll('[role="grid"]').length,
        pagePaginationCount: document.querySelectorAll('[aria-label="Pagination"], [aria-label="Next page"], [aria-label="Previous page"]').length,
        pageBusyCount: document.querySelectorAll('[aria-busy="true"], [role="progressbar"]').length,
        firstAnyFound: anyMetrics.found,
        firstAnyDepth: anyMetrics.depth,
        firstAnyTableCount: anyMetrics.tableCount,
        firstAnySearchCount: anyMetrics.searchCount,
        firstAnyStatusCount: anyMetrics.statusCount,
        firstAnyEmptyStatusCount: anyMetrics.emptyStatusCount,
        firstAnyTbodyCount: anyMetrics.tbodyCount,
        firstAnyRowCount: anyMetrics.rowCount,
        firstAnyBusyCount: anyMetrics.busyCount,
        firstAnyCreateActionableCount: anyMetrics.createActionableCount,
        firstSingleFound: singleMetrics.found,
        firstSingleDepth: singleMetrics.depth,
        firstSingleTableCount: singleMetrics.tableCount,
        firstSingleSearchCount: singleMetrics.searchCount,
        firstSingleStatusCount: singleMetrics.statusCount,
        firstSingleEmptyStatusCount: singleMetrics.emptyStatusCount,
        firstSingleTbodyCount: singleMetrics.tbodyCount,
        firstSingleRowCount: singleMetrics.rowCount,
        firstSingleBusyCount: singleMetrics.busyCount,
        firstSingleCreateActionableCount: singleMetrics.createActionableCount,
        firstTwoFound: twoMetrics.found,
        firstTwoDepth: twoMetrics.depth,
        firstTwoTableCount: twoMetrics.tableCount,
        firstTwoSearchCount: twoMetrics.searchCount,
        firstTwoStatusCount: twoMetrics.statusCount,
        firstTwoEmptyStatusCount: twoMetrics.emptyStatusCount,
        firstTwoTbodyCount: twoMetrics.tbodyCount,
        firstTwoRowCount: twoMetrics.rowCount,
        firstTwoBusyCount: twoMetrics.busyCount,
        firstTwoCreateActionableCount: twoMetrics.createActionableCount,
        sectionFound: sectionMetrics.found,
        sectionDepth: sectionMetrics.depth,
        sectionTableCount: sectionMetrics.tableCount,
        sectionSearchCount: sectionMetrics.searchCount,
        sectionStatusCount: sectionMetrics.statusCount,
        sectionEmptyStatusCount: sectionMetrics.emptyStatusCount,
        sectionTbodyCount: sectionMetrics.tbodyCount,
        sectionRowCount: sectionMetrics.rowCount,
        sectionBusyCount: sectionMetrics.busyCount,
        sectionCreateActionableCount: sectionMetrics.createActionableCount,
        exactCreateTokenElementCount: textCount("create token"),
        exactCreateApiTokenElementCount: textCount("create api token"),
        exactCreateElementCount: textCount("create"),
        createAndTokenElementCount: elements.filter((element) => {
          const text = normalize(element.textContent);
          return text.includes("create") && text.includes("token");
        }).length,
        exactCreateTokenActionableCount: actionCount((text) => text === "create token"),
        exactCreateApiTokenActionableCount: actionCount((text) => text === "create api token"),
        exactCreateActionableCount: actionCount((text) => text === "create"),
        createAndTokenActionableCount: actionCount((text) => text.includes("create") && text.includes("token")),
        ariaLabelCreateTokenCount: document.querySelectorAll('[aria-label="Create Token" i]').length,
        ariaLabelCreateApiTokenCount: document.querySelectorAll('[aria-label="Create API Token" i]').length,
        sameOriginExactCreatePathCount: safePathCount((path) => path === "/profile/api-tokens/create"),
        sameOriginCreateLikePathCount: safePathCount((path) => /\/api-tokens\/create\/?$/.test(path)),
        dataCreateMarkerCount: document.querySelectorAll('[data-testid*="create" i], [data-test*="create" i]').length,
      };
    });
    evaluatorReturned = true;
    const expectedKeys = Object.keys(emptyStructure()).sort();
    const booleanKeys = new Set([
      "inputConnected", "inputVisible", "inputValueEmpty",
      "firstAnyFound", "firstSingleFound", "firstTwoFound", "sectionFound",
    ]);
    resultObjectNonNull = typeof untrustedStructure === "object" && untrustedStructure !== null;
    const actualKeys = resultObjectNonNull ? Object.keys(untrustedStructure).sort() : [];
    resultKeyCount = Math.min(actualKeys.length, 1000000);
    resultPrototypeObjectExact =
      resultObjectNonNull && Object.getPrototypeOf(untrustedStructure) === Object.prototype;
    resultExactKeys =
      actualKeys.length === expectedKeys.length &&
      actualKeys.every((key, index) => key === expectedKeys[index]);
    resultBooleanTypesExact =
      resultExactKeys &&
      expectedKeys.filter((key) => booleanKeys.has(key))
        .every((key) => typeof untrustedStructure[key] === "boolean");
    const integerKeys = expectedKeys.filter((key) => !booleanKeys.has(key));
    resultIntegerTypesExact =
      resultExactKeys &&
      integerKeys.every((key) => Number.isSafeInteger(untrustedStructure[key]));
    resultIntegerRangesExact =
      resultIntegerTypesExact &&
      integerKeys.every((key) => {
        const upper = key.endsWith("Depth") ? 32 : 1000000;
        return untrustedStructure[key] >= -1 && untrustedStructure[key] <= upper;
      });
    const metricKeys = [
      "TableCount", "SearchCount", "StatusCount", "EmptyStatusCount",
      "TbodyCount", "RowCount", "BusyCount", "CreateActionableCount",
    ];
    resultFoundTuplesExact =
      resultBooleanTypesExact &&
      resultIntegerRangesExact &&
      ["firstAny", "firstSingle", "firstTwo", "section"].every((prefix) => {
        if (!untrustedStructure[`${prefix}Found`]) return true;
        return untrustedStructure[`${prefix}Depth`] >= 1 &&
          metricKeys.every((suffix) => untrustedStructure[`${prefix}${suffix}`] >= 0);
      });
    resultMissingTuplesExact =
      resultBooleanTypesExact &&
      resultIntegerRangesExact &&
      ["firstAny", "firstSingle", "firstTwo", "section"].every((prefix) => {
        if (untrustedStructure[`${prefix}Found`]) return true;
        return untrustedStructure[`${prefix}Depth`] === -1 &&
          metricKeys.every((suffix) => untrustedStructure[`${prefix}${suffix}`] === -1);
      });
    const pageAndCandidateKeys = expectedKeys.filter(
      (key) => !booleanKeys.has(key) && !key.endsWith("Depth") &&
        !/^(firstAny|firstSingle|firstTwo|section)/.test(key),
    );
    resultCountSentinelsExact =
      resultIntegerRangesExact &&
      pageAndCandidateKeys.every((key) => untrustedStructure[key] >= 0);
    if (
      !resultPrototypeObjectExact ||
      !resultExactKeys ||
      !resultBooleanTypesExact ||
      !resultIntegerTypesExact ||
      !resultIntegerRangesExact ||
      !resultFoundTuplesExact ||
      !resultMissingTuplesExact ||
      !resultCountSentinelsExact
    ) {
      throw new Error("StructuralResultValidationError");
    }
    structure = {};
    for (const key of expectedKeys) structure[key] = untrustedStructure[key];
    counters.diagnosticFulfilled++;
    result = "V13_STRUCTURAL_DIAGNOSTIC_BODY_COMPLETE";
  } catch (error) {
    errorClass = safeErrorClass(error);
  }

  if (tab !== null && tab !== undefined) {
    if (typeof tab.close === "function") {
      counters.closeAttempted++;
      try {
        await tab.close();
        counters.closeFulfilled++;
        tab = null;
        secureConsoleV13RetainedTab = null;
        cleanupState = "CREATED_TAB_CLOSED";
        failureResidueConverged = true;
      } catch (cleanupError) {
        cleanupState = "CLOSE_FAILED_EXACT_HANDLE_RETAINED";
        failureResidueConverged = false;
        if (errorClass === "NONE") errorClass = safeErrorClass(cleanupError);
      }
    } else {
      cleanupState = "MALFORMED_EXACT_HANDLE_RETAINED";
      failureResidueConverged = false;
    }
  } else if (counters.newAttempted === 1 && counters.newFulfilled === 0) {
    cleanupState = "NEW_REJECTED_RESIDUE_UNPROVEN";
    failureResidueConverged = false;
  }

  if (
    result === "V13_STRUCTURAL_DIAGNOSTIC_BODY_COMPLETE" &&
    cleanupState === "CREATED_TAB_CLOSED" &&
    failureResidueConverged === true &&
    secureConsoleV13RetainedTab === null
  ) {
    result = "EXACT_V13_STRUCTURAL_DIAGNOSTIC_PASS";
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
    evaluatorReturned,
    resultObjectNonNull,
    resultPrototypeObjectExact,
    resultKeyCount,
    resultExactKeys,
    resultBooleanTypesExact,
    resultIntegerTypesExact,
    resultIntegerRangesExact,
    resultFoundTuplesExact,
    resultMissingTuplesExact,
    resultCountSentinelsExact,
    ...structure,
    cleanupState,
    failureResidueConverged,
    retainedExactHandle: secureConsoleV13RetainedTab !== null,
    ...counters,
    errorClass,
    consumed: secureConsoleV13StructuralDiagnosticConsumed,
    v4BindingNull: secureConsoleOwnedTaskTabV4 === null,
    v4BindingIneligible: secureConsoleOwnedTaskTabV4Eligible === false,
    v4BindingStateExact:
      secureConsoleOwnedTaskTabV4State === "V9_OWNED_TAB_READINESS_FAILED_CLEAN",
  });
})();
```

Exact success is `EXACT_V13_STRUCTURAL_DIAGNOSTIC_PASS` with completed new,
navigation, URL, wait, count, diagnostic, close, and write counters; fixed
target true; evaluator returned; result key count exactly `60`; every fixed
validation-stage boolean true; exact close; converged residue; null retained
handle; and unchanged null/ineligible V4 state.

## Preserved constraints

V13 PASS authorizes only offline interpretation and a fresh independently
reviewed readiness replacement. The visible predicate and page evaluator remain
unchanged. Only controller-local validation observability is added; the
no-mutation boundary remains unchanged. V4 prestart and provider mutation remain
blocked. The exact token name, title-free authenticated semantics, complete-
list and no-existing-token proofs, no-Create rule, secret exclusions,
exact-handle cleanup, no-retry rule, final Create/native Copy/native masked
Paste confirmation, and later separate exact-row deletion confirmation remain
mandatory and unchanged.

## Static review gate

Independent Sol High review must verify predecessor exactness, bounded/safe
stage output with no untrusted value or key emission, byte-identical page
evaluator, exact call cardinality, durable handle ownership, exact-close
acceptance, count-only comparison logic, and absence of provider mutation.
Static review sets `authorizes_live_execution=false`.
