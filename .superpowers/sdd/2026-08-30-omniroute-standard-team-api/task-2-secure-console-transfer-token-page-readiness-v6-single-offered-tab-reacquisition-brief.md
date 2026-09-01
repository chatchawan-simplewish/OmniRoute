# Task 2 secure-console token-page readiness V6 single-offered-tab reacquisition brief

Date: 2026-09-01 (Asia/Bangkok)

## Purpose and exact predecessor boundary

V5 Call 1 attached to Chrome and read the complete pinned Chrome documentation
exactly once. V5 Call 2 was then consumed and failed before navigation because
the fulfilled `tabs.selected()` result did not satisfy controller ownership or
tab shape. The immutable incident is commit `00ec3dc60c6ffa8aa27e2a161c52aee5fd52c031`.

V5 is spent. This V6 contract never retries, continues, reinterprets, or
re-executes either V5 call. It uses the surviving V5 Chrome controller in the
same persistent JavaScript session and requires the exact completed V5 failure
state before making one new browser call.

The user has confirmed that Chrome Profile `Codex-Chrome-Bell-PC2`, the
intended window, and intended task tab are selected, and that no other Chrome
profile/window is offered to the extension. V6 additionally requires the
controller to offer exactly one tab. Zero, two, or more offered tabs fails
closed without choosing among them.

## Selected minimal mechanism

V6 makes exactly one `secureConsoleChromeV5.tabs.list()` call. It does not call
`browsers.get`, `browsers.list`, `getDefault`, `getForUrl`,
`tabs.selected`, `tabs.get`, `tabs.new`, a second list, reconnect, retry,
fallback, or alternate-browser logic.

The returned array is used only for exact cardinality and controller-object
shape. V6 does not emit any tab ID, title, URL, profile, window, cookie,
storage, password, session, DOM, screenshot, or secret data. Only when the
array contains exactly one well-shaped tab does V6 navigate that object to the
fixed public Cloudflare token page and run the unchanged V5/V4 semantic
readiness logic.

## Preserved V4 semantic and security contract

The title-free semantic page signature, terminal-list completeness proof,
fixed token-name absence proof, exact navigation target, no-Create rule,
counter completeness, error-class sanitization, null/ineligible failure
binding, and V4-compatible success binding are byte-for-byte inherited from
the V5 semantic body except for:

1. the one selected-tab acquisition being replaced by one exact-cardinality
   offered-tab list acquisition;
2. V6-specific counter and terminal-result names; and
3. the exact V5-failure predecessor and V6-consumption state.

V6 performs no Create/edit/delete, clipboard, keyboard, native Copy/Paste,
credential, proxy, listener, owner, DNS, routing, VM, or provider-persistent
action.

## One-shot executable cell

Execute this cell at most once, only in the same persistent Node REPL session
that produced the recorded V5 terminal state, and only after action-time pins
again prove the reviewed commits, exact 12-path dirty baseline, index zero,
public DNS absence, credential-free VM safe state, no residual owner/temp
state, and the current user visual-isolation confirmation.

Executable bytes: `12381`.

Executable SHA-256:
`CEC306737C33AC561428579671AA44BDB766C45A41B6AAE1A43FAD884CD2693D`.

The executable is complete only with its final LF.

```javascript
let secureConsoleV6ListReacquisitionConsumed = false;
await (async () => {
  const secureConsoleV6GateWasFresh = secureConsoleV6ListReacquisitionConsumed === false;
  secureConsoleV6ListReacquisitionConsumed = true;
  const counters = {
    listAttempted: 0,
    listFulfilled: 0,
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
  let offeredTabCount = -1;
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
      typeof secureConsoleChromeV5.tabs?.list === "function" &&
      typeof secureConsoleV5AttachmentConsumed === "boolean" &&
      typeof secureConsoleV5AttachmentExact === "boolean" &&
      typeof secureConsoleV6ListReacquisitionConsumed === "boolean";
    if (!declarationShape) throw new Error("FreshSessionDeclarationShapeError");
    predecessorStateExact =
      secureConsoleV6GateWasFresh === true &&
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
      secureConsoleOwnedTaskTabV4State === "V5_REACQUISITION_OR_READINESS_FAILED" &&
      secureConsoleOwnedTaskTabV4PreCreateDetachConsumed === false &&
      secureConsoleOwnedTaskTabV4PostNativeDetachConsumed === false &&
      secureConsoleCloudflareReadsV4Consumed === false;
    if (!predecessorStateExact) throw new Error("FreshSessionPredecessorStateError");

    counters.listAttempted++;
    const offeredTabs = await secureConsoleChromeV5.tabs.list();
    counters.listFulfilled++;
    offeredTabCount = Array.isArray(offeredTabs) ? offeredTabs.length : -1;
    if (offeredTabCount !== 1) throw new Error("OfferedTabCardinalityError");
    adopted = offeredTabs[0];
    controllerOwnership = typeof adopted === "object" && adopted !== null && typeof adopted.id === "string";
    tabShape =
      controllerOwnership &&
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
    result = "EXACT_V6_SINGLE_OFFERED_TOKEN_PAGE_SEMANTIC_READINESS_PASS";
  } catch (error) {
    errorClass = safeErrorClass(error);
  }
  secureConsoleV4AdoptionConsumed = true;
  if (result === "EXACT_V6_SINGLE_OFFERED_TOKEN_PAGE_SEMANTIC_READINESS_PASS") {
    secureConsoleOwnedTaskTabV4 = adopted;
    secureConsoleOwnedTaskTabV4Eligible = true;
    secureConsoleOwnedTaskTabV4State = "TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE";
  } else {
    secureConsoleOwnedTaskTabV4 = null;
    secureConsoleOwnedTaskTabV4Eligible = false;
    secureConsoleOwnedTaskTabV4State = "V6_LIST_REACQUISITION_OR_READINESS_FAILED";
  }
  counters.writeAttempted++;
  nodeRepl.write({
    result,
    declarationShape,
    predecessorStateExact,
    controllerOwnership,
    tabShape,
    offeredTabCount,
    navigationTargetExact,
    createControlCount,
    tokenNameCount,
    matchingRowCount,
    tokenInitialFilterEmpty,
    tokenQueryEchoCount,
    tokenFilterComplete,
    tokenSemanticSignature,
    listAttempted: counters.listAttempted,
    listFulfilled: counters.listFulfilled,
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
    consumed: secureConsoleV6ListReacquisitionConsumed,
    bindingEligible: secureConsoleOwnedTaskTabV4Eligible,
    bindingNull: secureConsoleOwnedTaskTabV4 === null,
    bindingState: secureConsoleOwnedTaskTabV4State,
  });
})();
```

Exact success is
`EXACT_V6_SINGLE_OFFERED_TOKEN_PAGE_SEMANTIC_READINESS_PASS` with consumed
true, list attempted/fulfilled exactly once, offered-tab count exactly one,
all V5 semantic counters exact, binding eligible true, and binding state
`TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE`.

Anything else, including timeout, truncation, malformed output, tool error,
uncertainty, cardinality mismatch, controller-shape mismatch, semantic mismatch,
or incomplete counters is a consumed V6 failure.

## Fixed ordering after exact V6 PASS

Only exact V6 PASS permits the unchanged pinned V4 prestart cell, once, in the
same persistent JavaScript session. After V4 prestart PASS, the inherited
credential-free sequence remains fixed:

1. fresh clipboard clear and shape-only empty proof once;
2. private proxy wrapper once and exact 19-label proof;
3. preparation, retained owner launch, safe readiness, and form preparation;
4. stop for the mandatory final Create/native Copy/native masked Paste
   confirmation;
5. after the user's native generated-page close report, run the exact V4
   post-native detach once;
6. later stop for the separate exact-row deletion confirmation;
7. revocation hold, invalid-token proof, cleanup, redacted evidence,
   standard-team API completion, and final Sol High audit.

Standing unattended authority does not waive either manual confirmation.

## Failure, no-residue, and cleanup contract

Every completed non-PASS leaves
`secureConsoleOwnedTaskTabV4=null`,
`secureConsoleOwnedTaskTabV4Eligible=false`, and state
`V6_LIST_REACQUISITION_OR_READINESS_FAILED`. V6 creates no tab, so its failure
permits no detach call. It must never be retried, continued, reinterpreted, or
relaxed. A new reviewed replacement would be required.

If V6 passes but the unchanged V4 prestart fails after binding, execute only
the exact pinned V4 pre-Create zero-browser-call detach once and stop. The
post-native detach remains reserved for the later native-secret boundary.

No secret may be printed, committed, logged, returned by a browser call, or
placed in review evidence. Only redacted identifiers, hashes, counters, and
status fields may persist.

## Static review and execution gate

Before live execution, this brief must be committed by exact path, reviewed
independently by Sol High with a PASS and no unresolved Critical/HIGH/IMPORTANT
finding, classified non-self-referentially, and followed by a post-commit
coordinator tuple proving exact bytes/hash, parent chain, projection, index
zero, and the exact 12-path dirty baseline.

Static review and classification do not authorize execution. Execution is
eligible only after all action-time pins and visual-isolation confirmation
revalidate in the sole owner task.
