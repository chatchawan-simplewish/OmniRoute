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
exactly one table. That exact root and table identity is retained across the
sole fill. The page must reproduce the full relevant V8 signature: zero ARIA
textbox/search-name matches, one placeholder input, no `aria-controls`, two
page tables, no grid, no pagination/next/previous controls, and zero
Create-token buttons. Preserving V4's unique Create-control semantic further
requires exactly one exact Create-token link.

An exact-root MutationObserver remains active from the completed baseline
through the filtered terminal. Each proof requires at least 1200 ms elapsed,
1000 ms mutation quiet, an unchanged internal row-content fingerprint,
connected exact identities, no busy/progress marker, one physical `tbody`, and
no row-count or common virtualizer marker inconsistent with the materialized
rows. A zero-row baseline requires one recognized status-role empty-token
marker scoped to the exact root. A nonempty baseline retains its private table
fingerprint and requires an exact-table descendant mutation after the captured
input event plus a changed final table fingerprint; unrelated root mutations
cannot satisfy the causal proof.
After the fill, the input must exactly echo
`OmniRoute secure console R5 20260901`, the exact table must have zero body
rows, the empty-token status must be unique, and both exact token-text and
matching-row counts must be zero. Internal fingerprints and page text are
never emitted. A listener installed before the fill must observe its input
event and exact query value.

## One-shot ownership and residue

V9 has exactly one `tabs.new()`, one fixed `goto()`, one page-local `fill()`,
and one failure-only `close()` call site. The created handle is assigned to
local and durable top-level state in the fulfillment assignment before any
later await. The Node tool awaits the outer async cell. Exact PASS transfers
that same handle to the V4 binding and clears
the V9 alias without closing it. Any failure closes only the exact created
handle; rejected close retains that exact handle for a new reviewed
disposition. Rejection, malformed output, timeout, truncation, tool error, or
uncertainty consumes V9 and stops. No retry, fallback, alternate tab, selected,
list, get, reconnect, manual selector, detach, or cleanup improvisation is
authorized. Predecessor drift leaves every inherited V4 binding field untouched
and reports only fixed-equality booleans.

## Executable cell

Execute at most once only after commit, independent Sol High PASS review,
non-self-referential classification, post-commit tuple, and fresh action-time
pins. The executable is complete only with its final LF.

Executable bytes: `22483`.

Executable SHA-256:
`288B6070C8843F787305FF6D11E91CBD3BB59FB86E97E8024BD59BA015D9DD4E`.

```javascript
let secureConsoleV9ReadinessConsumed = false;
let secureConsoleV9RetainedTab = null;
await (async () => {
  const gateWasFresh = secureConsoleV9ReadinessConsumed === false;
  secureConsoleV9ReadinessConsumed = true;
  const targetName = "OmniRoute secure console R5 20260901";
  const inheritedV4BindingNull =
    typeof secureConsoleOwnedTaskTabV4 !== "undefined" &&
    secureConsoleOwnedTaskTabV4 === null;
  const inheritedV4BindingIneligible =
    typeof secureConsoleOwnedTaskTabV4Eligible === "boolean" &&
    secureConsoleOwnedTaskTabV4Eligible === false;
  const inheritedV4BindingStateExact =
    typeof secureConsoleOwnedTaskTabV4State === "string" &&
    secureConsoleOwnedTaskTabV4State === "V7_OWNED_TAB_REACQUISITION_OR_READINESS_FAILED_CLEAN";
  const counters = {
    newAttempted: 0, newFulfilled: 0,
    navigationAttempted: 0, navigationFulfilled: 0,
    urlAttempted: 0, urlFulfilled: 0,
    countAttempted: 0, countFulfilled: 0,
    attributeAttempted: 0, attributeFulfilled: 0,
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
  let currentSearchNameCount = -1;
  let anySearchNameCount = -1;
  let allTextboxCount = -1;
  let placeholderSearchCount = -1;
  let createTokenButtonCount = -1;
  let createTokenLinkCount = -1;
  let createApiTokenButtonCount = -1;
  let pageTableCount = -1;
  let pageGridCount = -1;
  let ariaControlsAbsent = false;
  let createControlCount = -1;
  let initialTokenNameCount = -1;
  let finalTokenNameCount = -1;
  let matchingRowCount = -1;
  let baselineEmptyStatusCount = -1;
  let filteredEmptyStatusCount = -1;
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
  const settle = async (root, expectedValue, initializeIdentity) => {
    counters.settleAttempted++;
    const proof = await root.evaluate(async (exactRoot, args) => {
      const { expected, initialize, minimumElapsedMs } = args;
      const pause = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
      const input = exactRoot.querySelector('input[placeholder*="search" i]');
      const exactTable = exactRoot.querySelector("table");
      const identityKey = "__omnirouteV9ExactResultIdentity";
      if (initialize) {
        if (Object.prototype.hasOwnProperty.call(globalThis, identityKey)) {
          throw new Error("ReadinessIdentityCollisionError");
        }
        globalThis[identityKey] = { root: exactRoot, table: exactTable };
      }
      const retainedIdentity = globalThis[identityKey];
      const started = performance.now();
      if (initialize) {
        retainedIdentity.mutationCount = 0;
        retainedIdentity.lastMutation = started;
        retainedIdentity.inputEventCount = 0;
        retainedIdentity.lastInputValue = null;
        retainedIdentity.lastInputAt = 0;
        retainedIdentity.tableMutationCount = 0;
        retainedIdentity.lastTableMutation = 0;
        retainedIdentity.baselineFingerprint = null;
        retainedIdentity.baselineRowCount = -1;
        retainedIdentity.inputListener = () => {
          retainedIdentity.inputEventCount++;
          retainedIdentity.lastInputValue = input.value;
          retainedIdentity.lastInputAt = performance.now();
        };
        input.addEventListener("input", retainedIdentity.inputListener);
        retainedIdentity.observer = new MutationObserver((records) => {
          retainedIdentity.mutationCount++;
          retainedIdentity.lastMutation = performance.now();
          if (
            records.some(
              (record) =>
                record.target === exactTable || exactTable?.contains(record.target) === true,
            )
          ) {
            retainedIdentity.tableMutationCount++;
            retainedIdentity.lastTableMutation = performance.now();
          }
        });
        retainedIdentity.observer.observe(exactRoot, {
          subtree: true,
          childList: true,
          characterData: true,
          attributes: true,
        });
      }
      const observer = retainedIdentity?.observer;
      if (typeof observer?.disconnect !== "function") {
        throw new Error("ReadinessIdentityObserverError");
      }
      const fingerprint = () => {
        if (exactTable === null) return "MISSING";
        let hash = 2166136261;
        const text = [...exactTable.querySelectorAll("tbody tr")]
          .map((row) => (row.textContent || "").replace(/\s+/g, " ").trim())
          .join("\n");
        for (let index = 0; index < text.length; index++) {
          hash ^= text.charCodeAt(index);
          hash = Math.imul(hash, 16777619);
        }
        return `${text.length}:${hash >>> 0}`;
      };
      const snapshot = () => {
        const rows = exactTable === null ? [] : [...exactTable.querySelectorAll("tbody tr")];
        const contentFingerprint = fingerprint();
        const tbody = exactTable?.querySelector("tbody") ?? null;
        const ariaRowCount = exactTable?.getAttribute("aria-rowcount") ?? null;
        const physicalRowsExact =
          tbody !== null &&
          tbody.children.length === rows.length &&
          [...tbody.children].every((child) => child.tagName === "TR");
        const nonVirtualized =
          exactTable !== null &&
          exactTable.querySelectorAll("tbody").length === 1 &&
          physicalRowsExact === true &&
          (ariaRowCount === null || Number(ariaRowCount) === rows.length) &&
          exactRoot.querySelectorAll('[data-virtualized], [data-virtualizer], [aria-rowindex], tr[style*="transform" i]').length === 0;
        return {
          rootIdentityExact: retainedIdentity?.root === exactRoot,
          tableIdentityExact:
            retainedIdentity?.table === exactTable &&
            exactRoot.querySelector("table") === exactTable,
          rootConnected: exactRoot.isConnected === true,
          tableConnected: exactTable?.isConnected === true,
          inputConnected: input?.isConnected === true,
          inputVisible: input?.getClientRects().length === 1,
          inputValueExact: input?.value === expected,
          inputEventObserved: retainedIdentity.inputEventCount > 0,
          inputEventValueExact: retainedIdentity.lastInputValue === expected,
          causalTableTransitionObserved:
            retainedIdentity.tableMutationCount > 0 &&
            retainedIdentity.lastTableMutation >= retainedIdentity.lastInputAt &&
            retainedIdentity.baselineRowCount > 0 &&
            retainedIdentity.baselineFingerprint !== contentFingerprint,
          pageTableCount: document.querySelectorAll("table").length,
          rootSearchCount: exactRoot.querySelectorAll('input[placeholder*="search" i]').length,
          rootTableCount: exactRoot.querySelectorAll("table").length,
          rowCount: rows.length,
          busyCount: exactRoot.querySelectorAll('[aria-busy="true"], [role="progressbar"]').length,
          paginationCount: document.querySelectorAll('[aria-label="Pagination"], [aria-label="Next page"], [aria-label="Previous page"]').length,
          nonVirtualized,
          fingerprint: contentFingerprint,
        };
      };
      let previous = JSON.stringify(snapshot());
      let current = JSON.parse(previous);
      let contentStable = false;
      for (let index = 0; index < 80; index++) {
        await pause(100);
        current = snapshot();
        const encoded = JSON.stringify(current);
        const elapsed = performance.now() - started;
        const quietFor = performance.now() - retainedIdentity.lastMutation;
        contentStable =
          encoded === previous &&
          elapsed >= minimumElapsedMs &&
          quietFor >= 1000 &&
          current.busyCount === 0;
        previous = encoded;
        if (contentStable) {
          const mutationCount = retainedIdentity.mutationCount;
          if (initialize) {
            retainedIdentity.baselineFingerprint = current.fingerprint;
            retainedIdentity.baselineRowCount = current.rowCount;
            retainedIdentity.mutationCount = 0;
            retainedIdentity.lastMutation = performance.now();
            retainedIdentity.tableMutationCount = 0;
            retainedIdentity.lastTableMutation = 0;
          } else {
            observer.disconnect();
            input.removeEventListener("input", retainedIdentity.inputListener);
            delete globalThis[identityKey];
          }
          const { fingerprint: omitted, ...safe } = current;
          return { ...safe, mutationCount, quiescent: true, contentStable: true };
        }
      }
      observer.disconnect();
      input?.removeEventListener("input", retainedIdentity.inputListener);
      delete globalThis[identityKey];
      const { fingerprint: omitted, ...safe } = current;
      return { ...safe, mutationCount: retainedIdentity.mutationCount, quiescent: false, contentStable };
    }, { expected: expectedValue, initialize: initializeIdentity, minimumElapsedMs: 1200 });
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

    const currentSearch = tab.playwright.getByRole("textbox", { name: /search api tokens/i });
    currentSearchNameCount = await counted(currentSearch);
    anySearchNameCount = await counted(tab.playwright.getByRole("textbox", { name: /search/i }));
    allTextboxCount = await counted(tab.playwright.getByRole("textbox"));
    const tokenFilter = tab.playwright.locator('input[placeholder*="search" i]');
    placeholderSearchCount = await counted(tokenFilter);
    createTokenButtonCount = await counted(
      tab.playwright.getByRole("button", { name: "Create Token", exact: true }),
    );
    createTokenLinkCount = await counted(
      tab.playwright.getByRole("link", { name: "Create Token", exact: true }),
    );
    createApiTokenButtonCount = await counted(
      tab.playwright.getByRole("button", { name: /create api token/i }),
    );
    pageTableCount = await counted(tab.playwright.locator("table"));
    pageGridCount = await counted(tab.playwright.locator('[role="grid"]'));
    counters.attributeAttempted++;
    const ariaControls = await tokenFilter.getAttribute("aria-controls");
    counters.attributeFulfilled++;
    ariaControlsAbsent = ariaControls === null;
    const v8SignatureExact =
      currentSearchNameCount === 0 &&
      anySearchNameCount === 0 &&
      allTextboxCount === 0 &&
      placeholderSearchCount === 1 &&
      createTokenButtonCount === 0 &&
      createApiTokenButtonCount === 0 &&
      pageTableCount === 2 &&
      pageGridCount === 0 &&
      ariaControlsAbsent === true;
    if (!v8SignatureExact) throw new Error("ReadinessV8SignatureDriftError");
    createControlCount = createTokenButtonCount + createTokenLinkCount;

    const tokenRoot = tokenFilter.locator("xpath=ancestor::*[.//table][1]");
    if (await counted(tokenRoot) !== 1) throw new Error("ReadinessRootCountError");
    if (await counted(tokenRoot.locator("table")) !== 1) throw new Error("ReadinessRootTableCountError");
    const emptyStatus = tokenRoot
      .getByRole("status")
      .filter({ hasText: /^(no api tokens found|no tokens found|no results)$/i });
    baseline = await settle(tokenRoot, "", true);
    baselineEmptyStatusCount = await counted(emptyStatus);
    const baselineComplete =
      baseline.quiescent === true &&
      baseline.contentStable === true &&
      baseline.rootIdentityExact === true &&
      baseline.tableIdentityExact === true &&
      baseline.rootConnected === true &&
      baseline.tableConnected === true &&
      baseline.inputConnected === true &&
      baseline.inputVisible === true &&
      baseline.inputValueExact === true &&
      baseline.pageTableCount === 2 &&
      baseline.rootSearchCount === 1 &&
      baseline.rootTableCount === 1 &&
      baseline.rowCount >= 0 &&
      baseline.busyCount === 0 &&
      baseline.paginationCount === 0 &&
      baseline.nonVirtualized === true &&
      (baseline.rowCount === 0
        ? baselineEmptyStatusCount === 1
        : baselineEmptyStatusCount === 0);
    if (!baselineComplete) throw new Error("ReadinessBaselineIncompleteError");
    initialTokenNameCount = await counted(tab.playwright.getByText(targetName, { exact: true }));

    counters.fillAttempted++;
    await tokenFilter.fill(targetName);
    counters.fillFulfilled++;
    filtered = await settle(tokenRoot, targetName, false);
    filteredEmptyStatusCount = await counted(emptyStatus);
    finalTokenNameCount = await counted(tab.playwright.getByText(targetName, { exact: true }));
    matchingRowCount = await counted(tab.playwright.getByRole("row").filter({ hasText: targetName }));
    const filteredComplete =
      filtered.quiescent === true &&
      filtered.contentStable === true &&
      filtered.rootIdentityExact === true &&
      filtered.tableIdentityExact === true &&
      filtered.rootConnected === true &&
      filtered.tableConnected === true &&
      filtered.inputConnected === true &&
      filtered.inputVisible === true &&
      filtered.inputValueExact === true &&
      filtered.inputEventObserved === true &&
      filtered.inputEventValueExact === true &&
      filtered.pageTableCount === 2 &&
      filtered.rootSearchCount === 1 &&
      filtered.rootTableCount === 1 &&
      filtered.rowCount === 0 &&
      filtered.busyCount === 0 &&
      filtered.paginationCount === 0 &&
      filtered.nonVirtualized === true &&
      filteredEmptyStatusCount === 1 &&
      (baseline.rowCount === 0 || filtered.causalTableTransitionObserved === true);
    semanticSignature =
      navigationTargetExact === true &&
      v8SignatureExact === true &&
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
    if (predecessorStateExact !== true) {
      cleanupState = "PREDECESSOR_REJECTED_INHERITED_BINDING_UNTOUCHED";
      failureResidueConverged =
        counters.newAttempted === 0 &&
        secureConsoleV9RetainedTab === null;
    } else {
      secureConsoleOwnedTaskTabV4 = null;
      secureConsoleOwnedTaskTabV4Eligible = false;
    }
    if (
      predecessorStateExact === true &&
      tab !== null &&
      tab !== undefined &&
      typeof tab.close === "function"
    ) {
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
    } else if (predecessorStateExact === true && tab !== null && tab !== undefined) {
      cleanupState = "MALFORMED_EXACT_HANDLE_RETAINED";
      failureResidueConverged = false;
      secureConsoleOwnedTaskTabV4State = "V9_MALFORMED_EXACT_HANDLE_RETAINED";
    } else if (
      predecessorStateExact === true &&
      counters.newAttempted === 1 &&
      counters.newFulfilled === 0
    ) {
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
    currentSearchNameCount,
    anySearchNameCount,
    allTextboxCount,
    placeholderSearchCount,
    createTokenButtonCount,
    createTokenLinkCount,
    createApiTokenButtonCount,
    pageTableCount,
    pageGridCount,
    ariaControlsAbsent,
    createControlCount,
    initialTokenNameCount,
    finalTokenNameCount,
    matchingRowCount,
    baselineQuiescent: baseline?.quiescent === true,
    baselineContentStable: baseline?.contentStable === true,
    baselineRootIdentityExact: baseline?.rootIdentityExact === true,
    baselineTableIdentityExact: baseline?.tableIdentityExact === true,
    baselineRootConnected: baseline?.rootConnected === true,
    baselineTableConnected: baseline?.tableConnected === true,
    baselineInputEmpty: baseline?.inputValueExact === true,
    baselinePageTableCount: baseline?.pageTableCount ?? -1,
    baselineRootSearchCount: baseline?.rootSearchCount ?? -1,
    baselineRootTableCount: baseline?.rootTableCount ?? -1,
    baselineRowCount: baseline?.rowCount ?? -1,
    baselineBusyCount: baseline?.busyCount ?? -1,
    baselinePaginationCount: baseline?.paginationCount ?? -1,
    baselineNonVirtualized: baseline?.nonVirtualized === true,
    baselineEmptyStatusCount,
    filteredQuiescent: filtered?.quiescent === true,
    filteredContentStable: filtered?.contentStable === true,
    filteredRootIdentityExact: filtered?.rootIdentityExact === true,
    filteredTableIdentityExact: filtered?.tableIdentityExact === true,
    filteredRootConnected: filtered?.rootConnected === true,
    filteredTableConnected: filtered?.tableConnected === true,
    filteredQueryEchoExact: filtered?.inputValueExact === true,
    filteredInputEventObserved: filtered?.inputEventObserved === true,
    filteredInputEventValueExact: filtered?.inputEventValueExact === true,
    filteredPageTableCount: filtered?.pageTableCount ?? -1,
    filteredRootSearchCount: filtered?.rootSearchCount ?? -1,
    filteredRootTableCount: filtered?.rootTableCount ?? -1,
    filteredRowCount: filtered?.rowCount ?? -1,
    filteredBusyCount: filtered?.busyCount ?? -1,
    filteredPaginationCount: filtered?.paginationCount ?? -1,
    filteredNonVirtualized: filtered?.nonVirtualized === true,
    filteredCausalTableTransitionObserved:
      baseline !== null &&
      (baseline.rowCount === 0 || filtered?.causalTableTransitionObserved === true),
    filteredEmptyStatusCount,
    semanticSignature,
    ownershipTransferred,
    cleanupState,
    failureResidueConverged,
    retainedExactHandle: secureConsoleV9RetainedTab !== null,
    ...counters,
    errorClass,
    consumed: secureConsoleV9ReadinessConsumed,
    inheritedV4BindingNull,
    inheritedV4BindingIneligible,
    inheritedV4BindingStateExact,
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
