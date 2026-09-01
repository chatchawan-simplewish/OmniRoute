# OmniRoute V25 dashboard-home route-shape diagnostic replacement brief

`authorizes_live_execution=false`

## Scope and predecessor

This is a fresh-tab, one-shot, read-only diagnostic for the exact boundary that
failed in the consumed V23 prestart gate. Its direct predecessor is the V24
Sol High FAIL review commit
`675c5e467467aa1fa96384d12f93a7ec18002e50`.

V24 was never evaluated. Its review found one IMPORTANT completeness gap:
integer sentinels could remain `-1`. V25 closes only that gap by requiring
every projected integer key to be nonnegative before diagnostic PASS.

V23 readiness is consumed PASS. Its prestart-read gate is consumed
failed-clean after one dashboard-home navigation and before any click, wait, or
fill. The exact V23 tab closed and its binding is null/ineligible. V21 and V22
were never evaluated.

V25 does not retry or continue V23. It creates one new owned tab, navigates once
to the fixed dashboard home, waits only for the first visible anchor, takes one
synchronous fixed-key route-shape snapshot, closes the exact tab, and emits
only validated booleans, bounded counts, fixed state strings, counters, and a
sanitized error class.

It emits no href, URL, path, account/zone ID, anchor text, DOM, HTML,
screenshot, credential, token, secret, clipboard value, or provider response.
It performs no click, fill, press, submit, Create, edit, delete, reconnect,
tab discovery, VM, DNS, routing, listener, process, or provider-persistent
action.

## One-shot executable

```javascript
let secureConsoleDashboardV25DiagnosticConsumed = false;
let secureConsoleDashboardV25RetainedTab = null;
let secureConsoleDashboardV25State = "UNCREATED";
await (async () => {
  const gateWasFresh = secureConsoleDashboardV25DiagnosticConsumed === false;
  secureConsoleDashboardV25DiagnosticConsumed = true;
  const counters = {
    newAttempted: 0, newFulfilled: 0,
    navigationAttempted: 0, navigationFulfilled: 0,
    urlAttempted: 0, urlFulfilled: 0,
    waitAttempted: 0, waitFulfilled: 0,
    snapshotAttempted: 0, snapshotFulfilled: 0,
    closeAttempted: 0, closeFulfilled: 0,
    writeAttempted: 0,
  };
  const emptySnapshot = () => ({
    hostExact: false,
    rootPath: false,
    accountRootPath: false,
    accountHomePath: false,
    accountDomainsPath: false,
    allAnchorCount: -1,
    visibleAnchorCount: -1,
    exactZoneTextAnchorCount: -1,
    containsZoneTextAnchorCount: -1,
    exactZoneHrefCount: -1,
    nestedZoneHrefCount: -1,
    accountRootHrefCount: -1,
    accountHomeHrefCount: -1,
    accountDomainsHrefCount: -1,
    websitesActionCount: -1,
    domainsActionCount: -1,
    overviewActionCount: -1,
    accountActionCount: -1,
    mainCount: -1,
    navigationCount: -1,
    busyCount: -1,
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
  const booleanKeys = [
    "hostExact", "rootPath", "accountRootPath", "accountHomePath",
    "accountDomainsPath",
  ];
  const integerKeys = [
    "allAnchorCount", "visibleAnchorCount", "exactZoneTextAnchorCount",
    "containsZoneTextAnchorCount", "exactZoneHrefCount",
    "nestedZoneHrefCount", "accountRootHrefCount", "accountHomeHrefCount",
    "accountDomainsHrefCount", "websitesActionCount", "domainsActionCount",
    "overviewActionCount", "accountActionCount", "mainCount",
    "navigationCount", "busyCount",
  ];
  const trustedSnapshot = (value) => {
    if (!exactKeys(value, [...booleanKeys, ...integerKeys])) return null;
    const projected = {};
    for (const key of booleanKeys) {
      if (typeof value[key] !== "boolean") return null;
      projected[key] = value[key];
    }
    for (const key of integerKeys) {
      if (!Number.isSafeInteger(value[key]) || value[key] < -1 ||
          value[key] > 1000000) {
        return null;
      }
      projected[key] = value[key];
    }
    return projected;
  };
  let result = "PRECONDITION_FAIL";
  let declarationShape = false;
  let predecessorExact = false;
  let controllerOwnership = false;
  let createdHandleCaptured = false;
  let tabShape = false;
  let snapshot = emptySnapshot();
  let snapshotValidated = false;
  let snapshotComplete = false;
  let cleanupState = "NO_TAB_CREATED";
  let residueConverged = true;
  let errorClass = "NONE";
  let tab = null;
  try {
    declarationShape =
      typeof secureConsoleChromeV5 === "object" &&
      secureConsoleChromeV5 !== null &&
      typeof secureConsoleChromeV5.tabs?.new === "function" &&
      typeof secureConsoleV23ReadinessConsumed === "boolean" &&
      typeof secureConsoleCloudflareReadsV23Consumed === "boolean" &&
      typeof secureConsoleDashboardV25DiagnosticConsumed === "boolean";
    predecessorExact =
      declarationShape &&
      gateWasFresh === true &&
      secureConsoleV23ReadinessConsumed === true &&
      secureConsoleCloudflareReadsV23Consumed === true &&
      secureConsoleOwnedTaskTabV23 === null &&
      secureConsoleOwnedTaskTabV23Eligible === false &&
      secureConsoleOwnedTaskTabV23State ===
        "CLOUDFLARE_PRESTART_READS_FAILED_CLEAN_V23" &&
      secureConsoleOwnedTaskTabV23PreCreateDetachConsumed === false &&
      secureConsoleOwnedTaskTabV23PostNativeDetachConsumed === false &&
      typeof secureConsoleV21ReadinessConsumed === "undefined" &&
      typeof secureConsoleV22ReadinessConsumed === "undefined" &&
      typeof secureConsoleDashboardV24DiagnosticConsumed === "undefined" &&
      typeof secureConsoleDashboardV24RetainedTab === "undefined" &&
      typeof secureConsoleDashboardV24State === "undefined" &&
      secureConsoleDashboardV25RetainedTab === null &&
      secureConsoleDashboardV25State === "UNCREATED";
    if (!predecessorExact) throw new Error("DashboardDiagnosticPreconditionError");

    counters.newAttempted++;
    secureConsoleDashboardV25RetainedTab = tab =
      await secureConsoleChromeV5.tabs.new();
    counters.newFulfilled++;
    createdHandleCaptured = typeof tab === "object" && tab !== null;
    if (!createdHandleCaptured) throw new Error("DashboardDiagnosticHandleError");
    controllerOwnership = secureConsoleDashboardV25RetainedTab === tab;
    tabShape =
      controllerOwnership &&
      typeof tab.goto === "function" &&
      typeof tab.url === "function" &&
      typeof tab.close === "function" &&
      typeof tab.playwright?.locator === "function";
    if (!tabShape) throw new Error("DashboardDiagnosticTabShapeError");
    secureConsoleDashboardV25State = "DASHBOARD_DIAGNOSTIC_RUNNING_V25";

    counters.navigationAttempted++;
    await tab.goto("https://dash.cloudflare.com");
    counters.navigationFulfilled++;
    counters.urlAttempted++;
    const initialUrl = new URL(await tab.url());
    counters.urlFulfilled++;
    if (initialUrl.protocol !== "https:" ||
        initialUrl.hostname !== "dash.cloudflare.com") {
      throw new Error("DashboardDiagnosticNavigationError");
    }

    const firstVisibleAnchor = tab.playwright.locator("a[href]:visible").first();
    if (typeof firstVisibleAnchor?.waitFor !== "function") {
      throw new Error("DashboardDiagnosticAnchorShapeError");
    }
    counters.waitAttempted++;
    await firstVisibleAnchor.waitFor({ state: "visible", timeoutMs: 20000 });
    counters.waitFulfilled++;

    counters.snapshotAttempted++;
    const untrustedSnapshot = await tab.playwright.locator("body").evaluate((body) => {
      const normalize = (value) =>
        (value || "").replace(/\s+/g, " ").trim().toLowerCase();
      const anchors = [...body.querySelectorAll("a[href]")];
      const visibleAnchors = anchors.filter((item) =>
        item.getClientRects().length > 0);
      const actions = [...body.querySelectorAll(
        'button, a, [role="button"], [role="link"]',
      )];
      const paths = anchors.map((item) => {
        try {
          const url = new URL(item.getAttribute("href") || "", location.href);
          return url.protocol === "https:" &&
            url.hostname === "dash.cloudflare.com" ? url.pathname : "";
        } catch {
          return "";
        }
      });
      const textCount = (expected) =>
        actions.filter((item) => normalize(item.textContent) === expected).length;
      return {
        hostExact: location.protocol === "https:" &&
          location.hostname === "dash.cloudflare.com",
        rootPath: location.pathname === "/",
        accountRootPath: /^\/[0-9a-f]{32}\/?$/.test(location.pathname),
        accountHomePath:
          /^\/[0-9a-f]{32}\/home\/?$/.test(location.pathname),
        accountDomainsPath:
          /^\/[0-9a-f]{32}\/home\/domains\/?$/.test(location.pathname),
        allAnchorCount: anchors.length,
        visibleAnchorCount: visibleAnchors.length,
        exactZoneTextAnchorCount: anchors.filter((item) =>
          normalize(item.textContent) === "mysw.me").length,
        containsZoneTextAnchorCount: anchors.filter((item) =>
          normalize(item.textContent).includes("mysw.me")).length,
        exactZoneHrefCount: paths.filter((path) =>
          /^\/[0-9a-f]{32}\/mysw\.me\/?$/.test(path)).length,
        nestedZoneHrefCount: paths.filter((path) =>
          /^\/[0-9a-f]{32}\/mysw\.me\//.test(path)).length,
        accountRootHrefCount: paths.filter((path) =>
          /^\/[0-9a-f]{32}\/?$/.test(path)).length,
        accountHomeHrefCount: paths.filter((path) =>
          /^\/[0-9a-f]{32}\/home\/?$/.test(path)).length,
        accountDomainsHrefCount: paths.filter((path) =>
          /^\/[0-9a-f]{32}\/home\/domains\/?$/.test(path)).length,
        websitesActionCount: textCount("websites"),
        domainsActionCount: textCount("domains"),
        overviewActionCount: textCount("overview"),
        accountActionCount: actions.filter((item) =>
          /^account(?:s)?$/.test(normalize(item.textContent))).length,
        mainCount: body.querySelectorAll("main").length,
        navigationCount: body.querySelectorAll("nav, [role=\"navigation\"]").length,
        busyCount:
          body.querySelectorAll('[aria-busy="true"], [role="progressbar"]').length,
      };
    });
    counters.snapshotFulfilled++;
    const trusted = trustedSnapshot(untrustedSnapshot);
    snapshotValidated = trusted !== null;
    if (!snapshotValidated) throw new Error("DashboardDiagnosticSnapshotValidationError");
    snapshot = trusted;
    snapshotComplete =
      snapshot.hostExact === true &&
      integerKeys.every((key) => snapshot[key] >= 0) &&
      snapshot.allAnchorCount > 0 &&
      snapshot.visibleAnchorCount > 0 &&
      snapshot.mainCount >= 0 &&
      snapshot.navigationCount >= 0 &&
      snapshot.busyCount >= 0;
    if (!snapshotComplete) throw new Error("DashboardDiagnosticSnapshotIncompleteError");
    result = "EXACT_V25_DASHBOARD_ROUTE_SHAPE_DIAGNOSTIC_PASS";
  } catch (error) {
    errorClass = safeErrorClass(error);
  }

  if (tab !== null && tab !== undefined && typeof tab.close === "function") {
    counters.closeAttempted++;
    try {
      await tab.close();
      counters.closeFulfilled++;
      secureConsoleDashboardV25RetainedTab = null;
      secureConsoleDashboardV25State =
        result === "EXACT_V25_DASHBOARD_ROUTE_SHAPE_DIAGNOSTIC_PASS"
          ? "V25_DIAGNOSTIC_PASS_CLEAN"
          : "V25_DIAGNOSTIC_FAILED_CLEAN";
      cleanupState = "EXACT_TAB_CLOSED";
      residueConverged = true;
    } catch (closeError) {
      if (errorClass === "NONE") errorClass = safeErrorClass(closeError);
      secureConsoleDashboardV25RetainedTab = tab;
      secureConsoleDashboardV25State = "V25_DIAGNOSTIC_FAILED_TAB_RETAINED";
      cleanupState = "EXACT_TAB_CLOSE_REJECTED";
      residueConverged = false;
      result = "PRECONDITION_FAIL";
    }
  } else if (counters.newAttempted === 0) {
    secureConsoleDashboardV25State = "V25_DIAGNOSTIC_FAILED_CLEAN";
    cleanupState = "NO_TAB_CREATED";
  } else {
    secureConsoleDashboardV25State = "V25_DIAGNOSTIC_FAILED_RESIDUE_UNPROVEN";
    cleanupState = "RESIDUE_UNPROVEN";
    residueConverged = false;
    result = "PRECONDITION_FAIL";
  }

  counters.writeAttempted++;
  nodeRepl.write({
    result,
    declarationShape,
    predecessorExact,
    controllerOwnership,
    createdHandleCaptured,
    tabShape,
    snapshotValidated,
    snapshotComplete,
    snapshot,
    cleanupState,
    residueConverged,
    retainedExactHandle: secureConsoleDashboardV25RetainedTab !== null,
    state: secureConsoleDashboardV25State,
    consumed: secureConsoleDashboardV25DiagnosticConsumed,
    ...counters,
    errorClass,
  });
})();
```

## Acceptance and review gate

Exact diagnostic PASS requires predecessor and ownership fields true; one
new/navigation/URL/wait/snapshot/write; snapshot validation/completeness true;
exact host true; positive total and visible anchor counts; a complete fixed-key
route/action/count snapshot; exact close `1/1`; no retained handle; state
`V25_DIAGNOSTIC_PASS_CLEAN`; residue converged; consumed true; error
`NONE`; and completed tool output.

The diagnostic intentionally accepts zero for every candidate route and label
count. Its purpose is to distinguish known fixed shapes without exposing
content. A replacement may use only the resulting fixed counts/booleans and
must receive a new independent review before any navigation click or fill.

Any non-PASS spends V25. No retry, fallback, continuation, reinterpretation,
manual integration, verdict relaxation, tab discovery, or alternate browser
path is allowed.

Independent Sol High review must verify the V23 consumed-failed-clean boundary,
the static/unconsumed V24 FAIL boundary and declaration absence, the
all-integer-nonnegative correction, one-shot state, exact new-handle ownership,
fixed target, wait/evaluator safety,
fixed-key cross-realm projection, no identifier/text leakage, cleanup,
cardinality, secrets, no provider mutation, no retry, and both mandatory manual
confirmation boundaries.

`authorizes_live_execution=false`
