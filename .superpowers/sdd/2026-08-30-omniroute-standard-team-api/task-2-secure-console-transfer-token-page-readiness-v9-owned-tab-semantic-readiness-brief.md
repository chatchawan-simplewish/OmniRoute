# Task 2 secure-console token-page readiness V9 owned-tab semantic readiness brief

Date: 2026-09-02 (Asia/Bangkok)

## Purpose and authority boundary

V8 returned `EXACT_V8_SAFE_SEMANTIC_DIAGNOSTIC_PASS`, closed its exact owned
tab, and left V4 null/ineligible. Its immutable live report is commit
`9f3343de6`.

V9 is a fresh one-shot readiness replacement, never a retry or continuation of
V3-V8. It uses the V8-observed page signature: one placeholder-addressable
search input, two page tables, no ARIA textbox/`aria-controls`, and no
pagination. It preserves V4's fixed URL, exact token name, title-free
authenticated semantics, unique Create control, initial-filter state,
complete-list proof, exact query echo, no-existing-token proof, and counters.

V9 may navigate one newly owned exact tab and fill only the page-local search
input. It cannot click, press, Create, edit, delete, inspect a generated secret,
use the clipboard, or mutate provider state. Static artifacts set
`authorizes_live_execution=false`.

## Completeness replacement

The unique placeholder search input is bound to the nearest ancestor containing
exactly one table. The page must contain exactly two tables and no pagination,
next, or previous controls. Before and after the sole fill, the scoped table
must remain connected and unchanged for five consecutive 100 ms observations,
with no `aria-busy=true` or progressbar marker. The initial input must be empty.
After the fill, its value must exactly echo
`OmniRoute secure console R5 20260901`, the scoped table must contain zero body
rows, and both exact token-text and matching-row counts must be zero. These
requirements replace only the disproved ARIA-controlled paginator proof; they
do not weaken the complete-list or no-existing-token requirement.

## One-shot ownership and residue

V9 has exactly one `tabs.new()`, one fixed `goto()`, one page-local `fill()`,
and one failure-only `close()` call site. The created handle is assigned to
local and durable top-level state in the fulfillment assignment before any
later await. Exact PASS transfers that same handle to the V4 binding and clears
the V9 alias without closing it. Any failure closes only the exact created
handle; rejected close retains that exact handle for a new reviewed
disposition. Rejection, malformed output, timeout, truncation, tool error, or
uncertainty consumes V9 and stops. No retry, fallback, alternate tab, selected,
list, get, reconnect, manual selector, detach, or cleanup improvisation is
authorized.

## Executable cell

Execute at most once only after commit, independent Sol High PASS review,
non-self-referential classification, post-commit tuple, and fresh action-time
pins. The executable is complete only with its final LF.

Executable bytes: `11825`.

Executable SHA-256:
`3E5C0310A0419D859485E8FE4752848D8D5C40D19DB6603BA1C55173FF7951E7`.

```javascript
let secureConsoleV9ReadinessConsumed = false;
let secureConsoleV9RetainedTab = null;
void (async () => {
  const gateWasFresh = secureConsoleV9ReadinessConsumed === false;
  secureConsoleV9ReadinessConsumed = true;
  const targetName = "OmniRoute secure console R5 20260901";
  const counters = {
    newAttempted: 0, newFulfilled: 0,
    navigationAttempted: 0, navigationFulfilled: 0,
    urlAttempted: 0, urlFulfilled: 0,
    countAttempted: 0, countFulfilled: 0,
    settleAttempted: 0, settleFulfilled: 0,
    fillAttempted: 0, fillFulfilled: 0,
    closeAttempted: 0, closeFulfilled: 0,
    writeAttempted: 0,
  };
  let result = "PRECONDITION_FAIL";
  let errorClass = "NONE";
  let declarationShape = false;
  let predecessorStateExact = false;
  let controllerOwnership = false;
  let tabShape = false;
  let createdHandleCaptured = false;
  let navigationTargetExact = false;
  let createControlCount = -1;
  let initialTokenNameCount = -1;
  let finalTokenNameCount = -1;
  let matchingRowCount = -1;
  let baseline = null;
  let filtered = null;
  let semanticSignature = false;
  let ownershipTransferred = false;
  let cleanupState = "NOT_REQUIRED_NO_HANDLE";
  let failureResidueConverged = true;
  let tab = null;
  const safeErrorClass = (error) => {
    const name = typeof error?.name === "string" ? error.name : "OwnedTabSemanticReadinessError";
    return /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(name) ? name : "OwnedTabSemanticReadinessError";
  };
  const counted = async (locator) => {
    counters.countAttempted++;
    const value = await locator.count();
    counters.countFulfilled++;
    return value;
  };
  const settle = async (filter, expectedValue) => {
    counters.settleAttempted++;
    const proof = await filter.evaluate(async (input, expected) => {
      const pause = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
      const snapshot = () => {
        let root = input.parentElement;
        while (root !== null && root !== document.body && root.querySelectorAll("table").length !== 1) {
          root = root.parentElement;
        }
        const table = root !== null && root !== document.body ? root.querySelector("table") : null;
        return {
          inputConnected: input.isConnected === true,
          inputVisible: input.getClientRects().length === 1,
          inputValueExact: input.value === expected,
          pageTableCount: document.querySelectorAll("table").length,
          rootFound: root !== null && root !== document.body,
          rootSearchCount: root === null ? -1 : root.querySelectorAll('input[placeholder*="search" i]').length,
          rootTableCount: root === null ? -1 : root.querySelectorAll("table").length,
          rowCount: table === null ? -1 : table.querySelectorAll("tbody tr").length,
          busyCount: root === null ? -1 : root.querySelectorAll('[aria-busy="true"], [role="progressbar"]').length,
          paginationCount: document.querySelectorAll('[aria-label="Pagination"], [aria-label="Next page"], [aria-label="Previous page"]').length,
        };
      };
      let previous = JSON.stringify(snapshot());
      let stable = 0;
      let current = JSON.parse(previous);
      for (let index = 0; index < 40; index++) {
        await pause(100);
        current = snapshot();
        const encoded = JSON.stringify(current);
        stable = encoded === previous && current.busyCount === 0 ? stable + 1 : 0;
        previous = encoded;
        if (stable === 5) return { ...current, quiescent: true };
      }
      return { ...current, quiescent: false };
    }, expectedValue);
    counters.settleFulfilled++;
    return proof;
  };
  try {
    declarationShape =
      typeof secureConsoleChromeV5 === "object" &&
      secureConsoleChromeV5 !== null &&
      typeof secureConsoleChromeV5.tabs?.new === "function" &&
      typeof secureConsoleV8DiagnosticConsumed === "boolean" &&
      typeof secureConsoleV9ReadinessConsumed === "boolean";
    if (!declarationShape) throw new Error("ReadinessDeclarationShapeError");
    predecessorStateExact =
      gateWasFresh === true &&
      secureConsoleV8DiagnosticConsumed === true &&
      secureConsoleV8RetainedTab === null &&
      secureConsoleV4AdoptionConsumed === true &&
      secureConsoleOwnedTaskTabV4 === null &&
      secureConsoleOwnedTaskTabV4Eligible === false &&
      secureConsoleOwnedTaskTabV4State === "V7_OWNED_TAB_REACQUISITION_OR_READINESS_FAILED_CLEAN" &&
      secureConsoleOwnedTaskTabV4PreCreateDetachConsumed === false &&
      secureConsoleOwnedTaskTabV4PostNativeDetachConsumed === false &&
      secureConsoleCloudflareReadsV4Consumed === false;
    if (!predecessorStateExact) throw new Error("ReadinessPredecessorStateError");

    counters.newAttempted++;
    secureConsoleV9RetainedTab = tab = await secureConsoleChromeV5.tabs.new();
    counters.newFulfilled++;
    createdHandleCaptured = typeof tab === "object" && tab !== null;
    if (!createdHandleCaptured) {
      cleanupState = "NEW_FULFILLED_WITHOUT_TAB_HANDLE";
      failureResidueConverged = false;
      throw new Error("ReadinessTabHandleCaptureError");
    }
    controllerOwnership = typeof tab.id === "string";
    tabShape =
      controllerOwnership &&
      typeof tab.close === "function" &&
      typeof tab.goto === "function" &&
      typeof tab.url === "function" &&
      typeof tab.playwright?.getByRole === "function" &&
      typeof tab.playwright?.getByText === "function" &&
      typeof tab.playwright?.locator === "function";
    if (!tabShape) throw new Error("ReadinessTabShapeError");

    counters.navigationAttempted++;
    await tab.goto("https://dash.cloudflare.com/profile/api-tokens");
    counters.navigationFulfilled++;
    counters.urlAttempted++;
    const tokenUrl = new URL(await tab.url());
    counters.urlFulfilled++;
    navigationTargetExact = tokenUrl.href === "https://dash.cloudflare.com/profile/api-tokens";
    if (!navigationTargetExact) throw new Error("ReadinessNavigationTargetError");

    const tokenFilter = tab.playwright.locator('input[placeholder*="search" i]');
    if (await counted(tokenFilter) !== 1) throw new Error("ReadinessFilterCountError");
    baseline = await settle(tokenFilter, "");
    const baselineComplete =
      baseline.quiescent === true &&
      baseline.inputConnected === true &&
      baseline.inputVisible === true &&
      baseline.inputValueExact === true &&
      baseline.pageTableCount === 2 &&
      baseline.rootFound === true &&
      baseline.rootSearchCount === 1 &&
      baseline.rootTableCount === 1 &&
      baseline.rowCount >= 0 &&
      baseline.busyCount === 0 &&
      baseline.paginationCount === 0;
    if (!baselineComplete) throw new Error("ReadinessBaselineIncompleteError");
    createControlCount =
      await counted(tab.playwright.getByRole("button", { name: "Create Token", exact: true })) +
      await counted(tab.playwright.getByRole("link", { name: "Create Token", exact: true }));
    initialTokenNameCount = await counted(tab.playwright.getByText(targetName, { exact: true }));

    counters.fillAttempted++;
    await tokenFilter.fill(targetName);
    counters.fillFulfilled++;
    filtered = await settle(tokenFilter, targetName);
    finalTokenNameCount = await counted(tab.playwright.getByText(targetName, { exact: true }));
    matchingRowCount = await counted(tab.playwright.getByRole("row").filter({ hasText: targetName }));
    const filteredComplete =
      filtered.quiescent === true &&
      filtered.inputConnected === true &&
      filtered.inputVisible === true &&
      filtered.inputValueExact === true &&
      filtered.pageTableCount === 2 &&
      filtered.rootFound === true &&
      filtered.rootSearchCount === 1 &&
      filtered.rootTableCount === 1 &&
      filtered.rowCount === 0 &&
      filtered.busyCount === 0 &&
      filtered.paginationCount === 0;
    semanticSignature =
      navigationTargetExact === true &&
      createControlCount === 1 &&
      initialTokenNameCount === 0 &&
      finalTokenNameCount === 0 &&
      matchingRowCount === 0 &&
      baselineComplete === true &&
      filteredComplete === true;
    if (!semanticSignature) throw new Error("AuthenticatedTokenPageSemanticStateError");

    secureConsoleOwnedTaskTabV4 = tab;
    secureConsoleOwnedTaskTabV4Eligible = true;
    secureConsoleOwnedTaskTabV4State = "TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE";
    secureConsoleV9RetainedTab = null;
    tab = null;
    ownershipTransferred = true;
    cleanupState = "EXACT_HANDLE_TRANSFERRED_TO_V4_BINDING";
    result = "EXACT_V9_OWNED_TAB_SEMANTIC_READINESS_PASS";
  } catch (error) {
    errorClass = safeErrorClass(error);
  }

  if (result !== "EXACT_V9_OWNED_TAB_SEMANTIC_READINESS_PASS") {
    secureConsoleOwnedTaskTabV4 = null;
    secureConsoleOwnedTaskTabV4Eligible = false;
    if (tab !== null && tab !== undefined && typeof tab.close === "function") {
      counters.closeAttempted++;
      try {
        await tab.close();
        counters.closeFulfilled++;
        tab = null;
        secureConsoleV9RetainedTab = null;
        cleanupState = "CREATED_TAB_CLOSED";
        failureResidueConverged = true;
        secureConsoleOwnedTaskTabV4State = "V9_OWNED_TAB_READINESS_FAILED_CLEAN";
      } catch (cleanupError) {
        cleanupState = "CLOSE_FAILED_EXACT_HANDLE_RETAINED";
        failureResidueConverged = false;
        secureConsoleOwnedTaskTabV4State = "V9_OWNED_TAB_READINESS_FAILED_RETAINED";
        if (errorClass === "NONE") errorClass = safeErrorClass(cleanupError);
      }
    } else if (tab !== null && tab !== undefined) {
      cleanupState = "MALFORMED_EXACT_HANDLE_RETAINED";
      failureResidueConverged = false;
      secureConsoleOwnedTaskTabV4State = "V9_MALFORMED_EXACT_HANDLE_RETAINED";
    } else if (counters.newAttempted === 1 && counters.newFulfilled === 0) {
      cleanupState = "NEW_REJECTED_RESIDUE_UNPROVEN";
      failureResidueConverged = false;
      secureConsoleOwnedTaskTabV4State = "V9_NEW_REJECTED_RESIDUE_UNPROVEN";
    }
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
    createControlCount,
    initialTokenNameCount,
    finalTokenNameCount,
    matchingRowCount,
    baselineQuiescent: baseline?.quiescent === true,
    baselineInputEmpty: baseline?.inputValueExact === true,
    baselinePageTableCount: baseline?.pageTableCount ?? -1,
    baselineRootFound: baseline?.rootFound === true,
    baselineRootSearchCount: baseline?.rootSearchCount ?? -1,
    baselineRootTableCount: baseline?.rootTableCount ?? -1,
    baselineRowCount: baseline?.rowCount ?? -1,
    baselineBusyCount: baseline?.busyCount ?? -1,
    baselinePaginationCount: baseline?.paginationCount ?? -1,
    filteredQuiescent: filtered?.quiescent === true,
    filteredQueryEchoExact: filtered?.inputValueExact === true,
    filteredPageTableCount: filtered?.pageTableCount ?? -1,
    filteredRootFound: filtered?.rootFound === true,
    filteredRootSearchCount: filtered?.rootSearchCount ?? -1,
    filteredRootTableCount: filtered?.rootTableCount ?? -1,
    filteredRowCount: filtered?.rowCount ?? -1,
    filteredBusyCount: filtered?.busyCount ?? -1,
    filteredPaginationCount: filtered?.paginationCount ?? -1,
    semanticSignature,
    ownershipTransferred,
    cleanupState,
    failureResidueConverged,
    retainedExactHandle: secureConsoleV9RetainedTab !== null,
    ...counters,
    errorClass,
    consumed: secureConsoleV9ReadinessConsumed,
    v4BindingPresent: secureConsoleOwnedTaskTabV4 !== null,
    v4BindingEligible: secureConsoleOwnedTaskTabV4Eligible === true,
    v4BindingStateExact:
      secureConsoleOwnedTaskTabV4State === "TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE",
  });
})();
```

Exact PASS is `EXACT_V9_OWNED_TAB_SEMANTIC_READINESS_PASS` with all invoked
counters complete, both completeness proofs true, semantic signature true,
ownership transferred, cleanup state `EXACT_HANDLE_TRANSFERRED_TO_V4_BINDING`,
no V9-retained alias, and the exact eligible V4 binding state.

V9 PASS authorizes only offline preparation and independent review of the next
prestart compatibility step. It does not itself authorize the stale V4
prestart cell or any provider mutation.

## Preserved downstream constraints

The V4 fixed targets, permission set, exact token name, non-secret counters,
no-generated-secret inspection rule, clipboard boundaries, Create/native
Copy/native masked Paste confirmation, later exact-row deletion confirmation,
revocation hold, invalid-token proof, retained-owner disposition, and cleanup
terminals remain unchanged. No secret value may be printed, committed, logged,
or placed in review evidence.

## Static review gate

Independent Sol High review must verify predecessor exactness, page-signature
equivalence, quiescent completeness, exact call cardinality, durable ownership
across every await, failure-close convergence, safe outputs, and absence of
provider mutation. Static review does not authorize live execution.
