# Task 2 secure-console token-page readiness V7 owned-tab replacement brief

Date: 2026-09-01 (Asia/Bangkok)

## Purpose and exact predecessor

V5 selected-tab reacquisition and V6 exact-one offered-tab listing are both
consumed and failed before navigation. V6 returned zero offered tabs. The
immutable V6 incident is commit `4acecd710db9a31eab2af7797df0ad8bd93e3073`.

V7 never retries, continues, reinterprets, or re-executes V5 or V6. It uses
the surviving, already pinned Chrome controller in the same persistent Node
REPL session and requires the exact completed V6 failure state.

Pinned static Chrome API documentation states:

- `Tabs.new(): Promise<Tab>` creates and returns a new tab; and
- `Tab.close(): Promise<void>` closes that exact tab.

## Selected minimal mechanism

V7 creates one controller-owned task tab with exactly one
`secureConsoleChromeV5.tabs.new()` call. It captures the returned exact
handle before any shape or elapsed verdict, then uses only that handle for the
fixed Cloudflare navigation and unchanged V5/V4 semantic-readiness body.

V7 does not call `browsers.get`, reconnect, `tabs.selected`, `tabs.list`,
`tabs.get`, a second `tabs.new`, alternate-browser logic, selector fallback,
or retry. It emits no tab ID, title, pre-navigation URL, profile/window data,
cookie/storage/password/session data, DOM serialization, screenshot, or
secret.

## Exact-handle failure disposition

On every completed non-PASS after a handle is captured, the same cell attempts
exactly one `adopted.close()` and waits for settlement. A fulfilled close
nulls the local handle and proves the created tab closed. A rejected close
retains the exact handle only in `secureConsoleV7RetainedTab`, marks residue
unconverged, leaves the V4 binding null/ineligible, and stops for a new reviewed
disposition contract. It never hides a retained handle or substitutes another
tab.

If `tabs.new()` rejects or fulfills without a usable handle, residue is
explicitly unproven and V7 fails closed. A timeout, truncated output, tool
error, or uncertainty is consumed and authorizes no inspection, retry, or
cleanup improvisation; a new offline reviewed disposition contract is
required.

## Preserved semantic, completeness, and secret boundary

After exact-handle capture, the navigation target, title-free semantic page
signature, terminal-list completeness proof, filter query-echo proof, exact
token-name absence, no-Create rule, counter completeness, sanitized error
class, and V4-compatible success binding are inherited from V6/V5 without
semantic relaxation.

V7 performs no provider-persistent Create/edit/delete, clipboard, keyboard,
native Copy/Paste, credential, proxy, listener, owner, DNS, routing, VM, or
Cloudflare mutation.

## One-shot executable cell

Execute this cell at most once in the same persistent Node REPL session, only
after the committed incident, V7 brief, independent Sol High PASS review,
non-self-referential classification, post-commit tuple, and every action-time
pin pass. The executable is complete only with its final LF.

Executable bytes: `14103`.

Executable SHA-256:
`1683849B04EE4638BDC8764C69EB0DAB6ABC27233357E6D68C3C4E86BC735B45`.

```javascript
let secureConsoleV7OwnedTabReacquisitionConsumed = false;
let secureConsoleV7RetainedTab = null;
await (async () => {
  const secureConsoleV7GateWasFresh = secureConsoleV7OwnedTabReacquisitionConsumed === false;
  secureConsoleV7OwnedTabReacquisitionConsumed = true;
  const counters = {
    newAttempted: 0,
    newFulfilled: 0,
    navigationAttempted: 0,
    navigationFulfilled: 0,
    urlAttempted: 0,
    urlFulfilled: 0,
    readinessAttempted: 0,
    readinessFulfilled: 0,
    fillAttempted: 0,
    fillFulfilled: 0,
    createAttempted: 0,
    createFulfilled: 0,
    nameAttempted: 0,
    nameFulfilled: 0,
    rowAttempted: 0,
    rowFulfilled: 0,
    writeAttempted: 0,
  };
  let result = "PRECONDITION_FAIL";
  let errorClass = "NONE";
  let declarationShape = false;
  let predecessorStateExact = false;
  let controllerOwnership = false;
  let tabShape = false;
  let createdHandleCaptured = false;
  let cleanupAttempted = 0;
  let cleanupFulfilled = 0;
  let cleanupState = "NOT_NEEDED_NO_TAB";
  let failureResidueConverged = true;
  let navigationTargetExact = false;
  let createControlCount = -1;
  let tokenNameCount = -1;
  let matchingRowCount = -1;
  let tokenInitialFilterEmpty = false;
  let tokenQueryEchoCount = -1;
  let tokenFilterComplete = false;
  let tokenSemanticSignature = false;
  let adopted = null;
  const safeErrorClass = (error) => {
    const name = typeof error?.name === "string" ? error.name : "";
    return /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(name) ? name : "TokenPageSemanticReadinessError";
  };
  try {
    declarationShape =
      typeof secureConsoleAgentV5 === "object" && secureConsoleAgentV5 !== null &&
      typeof secureConsoleChromeV5 === "object" && secureConsoleChromeV5 !== null &&
      typeof secureConsoleChromeV5.tabs?.new === "function" &&
      typeof secureConsoleV5AttachmentConsumed === "boolean" &&
      typeof secureConsoleV5AttachmentExact === "boolean" &&
      typeof secureConsoleV6ListReacquisitionConsumed === "boolean" &&
      typeof secureConsoleV7OwnedTabReacquisitionConsumed === "boolean";
    if (!declarationShape) throw new Error("FreshSessionDeclarationShapeError");
    predecessorStateExact =
      secureConsoleV7GateWasFresh === true &&
      secureConsoleV6ListReacquisitionConsumed === true &&
      secureConsoleV5AttachmentConsumed === true &&
      secureConsoleV5AttachmentExact === true &&
      secureConsoleV5ConnectAttempted === 1 &&
      secureConsoleV5ConnectFulfilled === 1 &&
      secureConsoleV5DocumentationAttempted === 1 &&
      secureConsoleV5DocumentationFulfilled === 1 &&
      secureConsoleV5ConnectedShape === true &&
      secureConsoleV5AttachmentErrorClass === "NONE" &&
      secureConsoleV4AdoptionConsumed === true &&
      secureConsoleOwnedTaskTabV4 === null &&
      secureConsoleOwnedTaskTabV4Eligible === false &&
      secureConsoleOwnedTaskTabV4State === "V6_LIST_REACQUISITION_OR_READINESS_FAILED" &&
      secureConsoleOwnedTaskTabV4PreCreateDetachConsumed === false &&
      secureConsoleOwnedTaskTabV4PostNativeDetachConsumed === false &&
      secureConsoleCloudflareReadsV4Consumed === false;
    if (!predecessorStateExact) throw new Error("FreshSessionPredecessorStateError");

    counters.newAttempted++;
    adopted = await secureConsoleChromeV5.tabs.new();
    counters.newFulfilled++;
    createdHandleCaptured = typeof adopted === "object" && adopted !== null;
    if (!createdHandleCaptured) {
      failureResidueConverged = false;
      cleanupState = "NEW_FULFILLED_WITHOUT_TAB_HANDLE";
      throw new Error("OwnedTabHandleCaptureError");
    }
    controllerOwnership = typeof adopted.id === "string";
    tabShape =
      controllerOwnership &&
      typeof adopted.close === "function" &&
      typeof adopted.goto === "function" &&
      typeof adopted.url === "function" &&
      typeof adopted.playwright?.getByRole === "function" &&
      typeof adopted.playwright?.getByText === "function";
    if (!tabShape) throw new Error("SelectedTabOwnershipError");

    counters.navigationAttempted++;
    await adopted.goto("https://dash.cloudflare.com/profile/api-tokens");
    counters.navigationFulfilled++;
    counters.urlAttempted++;
    const tokenUrl = new URL(await adopted.url());
    counters.urlFulfilled++;
    navigationTargetExact = tokenUrl.href === "https://dash.cloudflare.com/profile/api-tokens";
    if (!navigationTargetExact) throw new Error("TokenNavigationTargetError");

    const tokenFilter = adopted.playwright.getByRole("textbox", { name: /search api tokens/i });
    if (await tokenFilter.count() !== 1) throw new Error("TokenFilterCountError");
    const tokenRegionId = await tokenFilter.getAttribute("aria-controls");
    if (typeof tokenRegionId !== "string" || !/^[A-Za-z][A-Za-z0-9_-]{0,127}$/.test(tokenRegionId)) throw new Error("TokenRegionBindingError");
    const tokenResultsRoot = adopted.playwright.locator(`#${tokenRegionId}`);
    if (await tokenResultsRoot.count() !== 1) throw new Error("TokenResultsRootCountError");
    const tokenPaginator = tokenResultsRoot.locator('[aria-label="Pagination"]');
    if (await tokenPaginator.count() !== 1) throw new Error("TokenPaginatorCountError");
    counters.readinessAttempted++;
    await tokenPaginator.waitFor({ state: "visible", timeoutMs: 20000 });
    counters.readinessFulfilled++;
    tokenInitialFilterEmpty = await tokenFilter.evaluate((input) => input.value === "");
    if (!tokenInitialFilterEmpty) throw new Error("TokenInitialFilterStateError");
    const tokenBaseline = await tokenResultsRoot.evaluate((root) => {
      const pager = root.querySelector('[aria-label="Pagination"]');
      const match = /^(\d+)\s*[-–]\s*(\d+)\s+of\s+(\d+)$/.exec((pager?.textContent || "").replace(/\s+/g, " ").trim());
      const rows = root.querySelectorAll("table tbody tr").length;
      const busy = root.matches('[aria-busy="true"]') || root.querySelector('[aria-busy="true"]') !== null;
      const statuses = [...root.querySelectorAll('[role="status"]')].filter((item) => /^(?:no api tokens found|no tokens found)$/i.test((item.textContent || "").trim()));
      const buttons = pager === null ? [] : [...pager.querySelectorAll("button")];
      const next = buttons.filter((item) => item.getAttribute("aria-label") === "Next page");
      const previous = buttons.filter((item) => item.getAttribute("aria-label") === "Previous page");
      const disabled = (item) => item.hasAttribute("disabled") || item.getAttribute("aria-disabled") === "true";
      if (busy || match === null || next.length !== 1 || previous.length !== 1) return { terminalZero: false, completeNonempty: false };
      const start = Number(match[1]), end = Number(match[2]), total = Number(match[3]);
      return {
        terminalZero: start === 0 && end === 0 && total === 0 && rows === 0 && statuses.length === 1 && disabled(next[0]) && disabled(previous[0]),
        completeNonempty: start === 1 && end === rows && total >= rows && rows > 0 && statuses.length === 0 && disabled(previous[0]) && disabled(next[0]) === (end >= total),
      };
    });
    if (!tokenBaseline.terminalZero && !tokenBaseline.completeNonempty) throw new Error("TokenBaselineIncompleteError");

    counters.fillAttempted++;
    await tokenFilter.fill("OmniRoute secure console R5 20260901");
    counters.fillFulfilled++;
    const tokenQueryEcho = tokenResultsRoot.getByText("OmniRoute secure console R5 20260901", { exact: true });
    counters.readinessAttempted++;
    await tokenQueryEcho.waitFor({ state: "visible", timeoutMs: 20000 });
    counters.readinessFulfilled++;
    tokenQueryEchoCount = await tokenQueryEcho.count();
    if (tokenQueryEchoCount !== 1) throw new Error("TokenQueryEchoCountError");
    const tokenEmptyStatus = tokenResultsRoot.getByRole("status").filter({ hasText: /^(?:no api tokens found|no tokens found)$/i });
    counters.readinessAttempted++;
    await tokenEmptyStatus.waitFor({ state: "visible", timeoutMs: 20000 });
    counters.readinessFulfilled++;
    if (await tokenEmptyStatus.count() !== 1) throw new Error("TokenEmptyStatusCountError");
    const tokenValueExact = await tokenFilter.evaluate((input) => input.value === "OmniRoute secure console R5 20260901");
    const tokenTerminal = await tokenResultsRoot.evaluate((root) => {
      const pager = root.querySelector('[aria-label="Pagination"]');
      const match = /^(\d+)\s*[-–]\s*(\d+)\s+of\s+(\d+)$/.exec((pager?.textContent || "").replace(/\s+/g, " ").trim());
      const rows = root.querySelectorAll("table tbody tr").length;
      const statuses = [...root.querySelectorAll('[role="status"]')].filter((item) => /^(?:no api tokens found|no tokens found)$/i.test((item.textContent || "").trim()));
      const buttons = pager === null ? [] : [...pager.querySelectorAll("button")];
      const next = buttons.filter((item) => item.getAttribute("aria-label") === "Next page");
      const previous = buttons.filter((item) => item.getAttribute("aria-label") === "Previous page");
      const disabled = (item) => item.hasAttribute("disabled") || item.getAttribute("aria-disabled") === "true";
      const busy = root.matches('[aria-busy="true"]') || root.querySelector('[aria-busy="true"]') !== null;
      return !busy && match !== null && Number(match[1]) === 0 && Number(match[2]) === 0 && Number(match[3]) === 0 && rows === 0 && statuses.length === 1 && next.length === 1 && previous.length === 1 && disabled(next[0]) && disabled(previous[0]);
    });

    counters.createAttempted++;
    createControlCount =
      await adopted.playwright.getByRole("button", { name: "Create Token", exact: true }).count() +
      await adopted.playwright.getByRole("link", { name: "Create Token", exact: true }).count();
    counters.createFulfilled++;
    counters.nameAttempted++;
    tokenNameCount = await tokenResultsRoot.locator("table tbody").getByText("OmniRoute secure console R5 20260901", { exact: true }).count();
    counters.nameFulfilled++;
    counters.rowAttempted++;
    matchingRowCount = await tokenResultsRoot.getByRole("row").filter({ hasText: "OmniRoute secure console R5 20260901" }).count();
    counters.rowFulfilled++;
    tokenFilterComplete = tokenInitialFilterEmpty && tokenQueryEchoCount === 1 && tokenValueExact && tokenTerminal &&
      (tokenBaseline.terminalZero || tokenBaseline.completeNonempty);
    tokenSemanticSignature = navigationTargetExact && createControlCount === 1 && tokenNameCount === 0 &&
      matchingRowCount === 0 && tokenFilterComplete;
    if (!tokenSemanticSignature || counters.readinessAttempted !== 3 || counters.readinessFulfilled !== 3 ||
        counters.fillAttempted !== 1 || counters.fillFulfilled !== 1) {
      throw new Error("AuthenticatedTokenPageSemanticStateError");
    }
    result = "EXACT_V7_OWNED_TAB_TOKEN_PAGE_SEMANTIC_READINESS_PASS";
  } catch (error) {
    errorClass = safeErrorClass(error);
  }
  if (result !== "EXACT_V7_OWNED_TAB_TOKEN_PAGE_SEMANTIC_READINESS_PASS") {
    if (adopted !== null && adopted !== undefined) {
      if (typeof adopted.close === "function") {
        cleanupAttempted++;
        try {
          await adopted.close();
          cleanupFulfilled++;
          adopted = null;
          cleanupState = "CREATED_TAB_CLOSED";
          failureResidueConverged = true;
        } catch (cleanupError) {
          secureConsoleV7RetainedTab = adopted;
          cleanupState = "CLOSE_FAILED_EXACT_HANDLE_RETAINED";
          failureResidueConverged = false;
          if (errorClass === "NONE") errorClass = safeErrorClass(cleanupError);
        }
      } else {
        secureConsoleV7RetainedTab = adopted;
        cleanupState = "MALFORMED_EXACT_HANDLE_RETAINED";
        failureResidueConverged = false;
      }
    } else if (counters.newAttempted === 1 && counters.newFulfilled === 0) {
      cleanupState = "NEW_REJECTED_RESIDUE_UNPROVEN";
      failureResidueConverged = false;
    }
  } else {
    cleanupState = "BOUND_SUCCESS";
  }
  secureConsoleV4AdoptionConsumed = true;
  if (result === "EXACT_V7_OWNED_TAB_TOKEN_PAGE_SEMANTIC_READINESS_PASS") {
    secureConsoleOwnedTaskTabV4 = adopted;
    secureConsoleOwnedTaskTabV4Eligible = true;
    secureConsoleOwnedTaskTabV4State = "TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE";
  } else {
    secureConsoleOwnedTaskTabV4 = null;
    secureConsoleOwnedTaskTabV4Eligible = false;
    secureConsoleOwnedTaskTabV4State = secureConsoleV7RetainedTab === null
      ? "V7_OWNED_TAB_REACQUISITION_OR_READINESS_FAILED_CLEAN"
      : "V7_OWNED_TAB_FAILURE_EXACT_HANDLE_RETAINED";
  }
  counters.writeAttempted++;
  nodeRepl.write({
    result,
    declarationShape,
    predecessorStateExact,
    controllerOwnership,
    tabShape,
    createdHandleCaptured,
    cleanupAttempted,
    cleanupFulfilled,
    cleanupState,
    failureResidueConverged,
    retainedExactHandle: secureConsoleV7RetainedTab !== null,
    navigationTargetExact,
    createControlCount,
    tokenNameCount,
    matchingRowCount,
    tokenInitialFilterEmpty,
    tokenQueryEchoCount,
    tokenFilterComplete,
    tokenSemanticSignature,
    newAttempted: counters.newAttempted,
    newFulfilled: counters.newFulfilled,
    navigationAttempted: counters.navigationAttempted,
    navigationFulfilled: counters.navigationFulfilled,
    urlAttempted: counters.urlAttempted,
    urlFulfilled: counters.urlFulfilled,
    readinessAttempted: counters.readinessAttempted,
    readinessFulfilled: counters.readinessFulfilled,
    fillAttempted: counters.fillAttempted,
    fillFulfilled: counters.fillFulfilled,
    createAttempted: counters.createAttempted,
    createFulfilled: counters.createFulfilled,
    nameAttempted: counters.nameAttempted,
    nameFulfilled: counters.nameFulfilled,
    rowAttempted: counters.rowAttempted,
    rowFulfilled: counters.rowFulfilled,
    writeAttempted: counters.writeAttempted,
    errorClass,
    consumed: secureConsoleV7OwnedTabReacquisitionConsumed,
    bindingEligible: secureConsoleOwnedTaskTabV4Eligible,
    bindingNull: secureConsoleOwnedTaskTabV4 === null,
    bindingState: secureConsoleOwnedTaskTabV4State,
  });
})();
```

Exact success is
`EXACT_V7_OWNED_TAB_TOKEN_PAGE_SEMANTIC_READINESS_PASS` with consumed true,
new attempted/fulfilled exactly once, captured controller/tab shape true,
unchanged semantic counters exact, cleanup state `BOUND_SUCCESS`, no retained
failure handle, and V4 binding eligible in state
`TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE`.

Anything else is a consumed V7 non-PASS. Only a completed failure with
`failureResidueConverged=true`, cleanup state `CREATED_TAB_CLOSED` or
`NOT_NEEDED_NO_TAB`, no retained handle, null V4 binding, and exact counters
proves clean no-residue disposition. Every other failure stops with residue
unproven or an exact retained handle.

## Fixed ordering after exact V7 PASS

Only exact V7 PASS permits the unchanged pinned V4 prestart cell once in the
same persistent JavaScript session. After V4 prestart PASS:

1. perform the fresh clipboard clear and shape-only empty proof once;
2. start the private proxy wrapper once and prove all 19 labels;
3. prepare and launch the retained owner and reach safe form readiness;
4. stop for the mandatory final Create/native Copy/native masked Paste
   confirmation;
5. after the user's native generated-page close report, run the exact V4
   post-native detach once;
6. later stop for the separate exact-row deletion confirmation; and
7. complete revocation hold, invalid-token proof, cleanup, redacted evidence,
   standard-team API work, and final Sol High audit.

Standing unattended authority never waives either manual confirmation.

If V7 passes but V4 prestart fails after binding, run only the exact pinned V4
pre-Create zero-browser-call detach once and stop.

## Static review and execution gate

Before live execution, this brief must be committed by exact path, reviewed
independently by Sol High with PASS and no unresolved Critical/HIGH/IMPORTANT
finding, classified non-self-referentially, and followed by a separate
post-commit coordinator tuple proving exact bytes/hash, ancestry, projection,
index zero, and the exact 12-path dirty baseline.

Static review and classification set
`authorizes_live_execution=false`. The sole owner must revalidate all local,
runtime, process-residue, VM1205, DNS, and persistent-binding pins immediately
before the one-shot call.

No secret may be printed, committed, logged, returned by a browser call, or
placed in review evidence. Only redacted identifiers, hashes, counters, and
status fields may persist.
