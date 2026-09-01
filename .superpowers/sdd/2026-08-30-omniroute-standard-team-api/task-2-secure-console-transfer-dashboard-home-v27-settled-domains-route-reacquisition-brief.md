# OmniRoute V27 settled-home Domains-route reacquisition replacement brief

`authorizes_live_execution=false`

## Scope and predecessor

This is the smallest fresh-tab replacement for the route boundary that spent
the V23 prestart gate failed-clean. It relies only on the fixed safe result in
V25 live report commit `01a5977398cf5d653e1bfe81a76cd6cb32439454`:
the dashboard resolves to an account-home path, the direct zone anchor is
absent, and exactly one normalized Domains action exists.

V26 is consumed failed-clean at incident commit
`04bc5e467caa057ab44ea49935a6b66c8e87a1b2`. Its first URL read completed
before the account-home redirect had settled, so it stopped before the
V25-proven visible-anchor wait/snapshot and before any click. V27 changes only
that timing boundary: the initial URL check is host-only, then the existing
condition-based first-visible-anchor wait completes, and a distinct second URL
read parses the original account-home segment before the click. Every later
Domains/zone route must match that segment; it is never emitted.

V27 creates one owned tab, navigates once to the fixed dashboard home,
revalidates a complete fixed-key semantic signature, clicks exactly one visible
Domains action, validates the account-bound Domains route, validates exactly
one visible `mysw.me` anchor and its same-account route shape, navigates to that
exact validated zone URL, verifies the exact zone route and marker, and retains
only that tab on success for a separately reviewed read gate.

It emits no URL, href, account/zone ID, DOM, HTML, screenshot, provider
response, credential, token, secret, or clipboard value. It performs no DNS,
rate-rule, Tunnel, Access, API-token, permission, Create, edit, delete, fill,
press, submit, VM, routing, listener, process, reconnect, or tab-discovery
action. The sole click is the guarded read-only Domains navigation action.

## One-shot executable

```javascript
let secureConsoleDashboardV27RouteConsumed = false;
let secureConsoleDashboardV27RetainedTab = null;
let secureConsoleDashboardV27Eligible = false;
let secureConsoleDashboardV27State = "UNCREATED";
let secureConsoleDashboardV27PreCreateDetachConsumed = false;
let secureConsoleDashboardV27PostNativeDetachConsumed = false;
let secureConsoleCloudflareReadsV27Consumed = false;
await (async () => {
  const gateWasFresh = secureConsoleDashboardV27RouteConsumed === false;
  secureConsoleDashboardV27RouteConsumed = true;
  const counters = {
    newAttempted: 0, newFulfilled: 0,
    homeNavigationAttempted: 0, homeNavigationFulfilled: 0,
    homeUrlAttempted: 0, homeUrlFulfilled: 0,
    homeWaitAttempted: 0, homeWaitFulfilled: 0,
    settledHomeUrlAttempted: 0, settledHomeUrlFulfilled: 0,
    homeSnapshotAttempted: 0, homeSnapshotFulfilled: 0,
    domainsCountAttempted: 0, domainsCountFulfilled: 0,
    domainsVisibleAttempted: 0, domainsVisibleFulfilled: 0,
    domainsClickAttempted: 0, domainsClickFulfilled: 0,
    domainsUrlAttempted: 0, domainsUrlFulfilled: 0,
    zoneWaitAttempted: 0, zoneWaitFulfilled: 0,
    zoneCountAttempted: 0, zoneCountFulfilled: 0,
    zoneHrefAttempted: 0, zoneHrefFulfilled: 0,
    zoneNavigationAttempted: 0, zoneNavigationFulfilled: 0,
    finalUrlAttempted: 0, finalUrlFulfilled: 0,
    markerWaitAttempted: 0, markerWaitFulfilled: 0,
    markerCountAttempted: 0, markerCountFulfilled: 0,
    closeAttempted: 0, closeFulfilled: 0,
    writeAttempted: 0,
  };
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
      if (!Number.isSafeInteger(value[key]) || value[key] < 0 ||
          value[key] > 1000000) return null;
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
  let homeSnapshotValidated = false;
  let homeSignatureExact = false;
  let domainsActionCount = -1;
  let domainsActionVisible = false;
  let domainsRouteExact = false;
  let zoneAnchorCount = -1;
  let zoneHrefShapeExact = false;
  let zoneNavigationExact = false;
  let zoneMarkerCount = -1;
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
      typeof secureConsoleDashboardV25DiagnosticConsumed === "boolean" &&
      typeof secureConsoleDashboardV26RouteConsumed === "boolean" &&
      typeof secureConsoleCloudflareReadsV26Consumed === "boolean" &&
      typeof secureConsoleDashboardV27RouteConsumed === "boolean";
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
      typeof secureConsoleDashboardV24DiagnosticConsumed === "undefined" &&
      typeof secureConsoleDashboardV24RetainedTab === "undefined" &&
      typeof secureConsoleDashboardV24State === "undefined" &&
      secureConsoleDashboardV25DiagnosticConsumed === true &&
      secureConsoleDashboardV25RetainedTab === null &&
      secureConsoleDashboardV25State === "V25_DIAGNOSTIC_PASS_CLEAN" &&
      secureConsoleDashboardV26RouteConsumed === true &&
      secureConsoleDashboardV26RetainedTab === null &&
      secureConsoleDashboardV26Eligible === false &&
      secureConsoleDashboardV26State === "V26_ROUTE_FAILED_CLEAN" &&
      secureConsoleDashboardV26PreCreateDetachConsumed === false &&
      secureConsoleDashboardV26PostNativeDetachConsumed === false &&
      secureConsoleCloudflareReadsV26Consumed === false &&
      secureConsoleDashboardV27RetainedTab === null &&
      secureConsoleDashboardV27Eligible === false &&
      secureConsoleDashboardV27State === "UNCREATED" &&
      secureConsoleDashboardV27PreCreateDetachConsumed === false &&
      secureConsoleDashboardV27PostNativeDetachConsumed === false &&
      secureConsoleCloudflareReadsV27Consumed === false;
    if (!predecessorExact) throw new Error("DomainsRoutePreconditionError");

    counters.newAttempted++;
    secureConsoleDashboardV27RetainedTab = tab =
      await secureConsoleChromeV5.tabs.new();
    counters.newFulfilled++;
    createdHandleCaptured = typeof tab === "object" && tab !== null;
    if (!createdHandleCaptured) throw new Error("DomainsRouteHandleError");
    controllerOwnership = secureConsoleDashboardV27RetainedTab === tab;
    tabShape =
      controllerOwnership &&
      typeof tab.goto === "function" &&
      typeof tab.url === "function" &&
      typeof tab.close === "function" &&
      typeof tab.playwright?.locator === "function" &&
      typeof tab.playwright?.getByText === "function";
    if (!tabShape) throw new Error("DomainsRouteTabShapeError");
    secureConsoleDashboardV27State = "DOMAINS_ROUTE_RUNNING_V27";

    counters.homeNavigationAttempted++;
    await tab.goto("https://dash.cloudflare.com");
    counters.homeNavigationFulfilled++;
    counters.homeUrlAttempted++;
    const homeUrl = new URL(await tab.url());
    counters.homeUrlFulfilled++;
    if (homeUrl.protocol !== "https:" ||
        homeUrl.hostname !== "dash.cloudflare.com") {
      throw new Error("DomainsRouteHomeNavigationError");
    }

    const firstVisibleAnchor = tab.playwright.locator("a[href]:visible").first();
    if (typeof firstVisibleAnchor?.waitFor !== "function") {
      throw new Error("DomainsRouteAnchorShapeError");
    }
    counters.homeWaitAttempted++;
    await firstVisibleAnchor.waitFor({ state: "visible", timeoutMs: 20000 });
    counters.homeWaitFulfilled++;
    counters.settledHomeUrlAttempted++;
    const settledHomeUrl = new URL(await tab.url());
    counters.settledHomeUrlFulfilled++;
    const homePath = /^\/([0-9a-f]{32})\/home\/?$/.exec(
      settledHomeUrl.pathname,
    );
    if (settledHomeUrl.protocol !== "https:" ||
        settledHomeUrl.hostname !== "dash.cloudflare.com" ||
        homePath === null) {
      throw new Error("DomainsRouteSettledHomeError");
    }
    const homeAccountSegment = homePath[1];
    counters.homeSnapshotAttempted++;
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
        navigationCount: body.querySelectorAll('nav, [role="navigation"]').length,
        busyCount:
          body.querySelectorAll('[aria-busy="true"], [role="progressbar"]').length,
      };
    });
    counters.homeSnapshotFulfilled++;
    const homeSnapshot = trustedSnapshot(untrustedSnapshot);
    homeSnapshotValidated = homeSnapshot !== null;
    if (!homeSnapshotValidated) throw new Error("DomainsRouteSnapshotValidationError");
    homeSignatureExact =
      homeSnapshot.hostExact === true &&
      homeSnapshot.accountHomePath === true &&
      homeSnapshot.rootPath === false &&
      homeSnapshot.accountRootPath === false &&
      homeSnapshot.accountDomainsPath === false &&
      homeSnapshot.allAnchorCount > 0 &&
      homeSnapshot.visibleAnchorCount > 0 &&
      homeSnapshot.exactZoneTextAnchorCount === 0 &&
      homeSnapshot.containsZoneTextAnchorCount === 0 &&
      homeSnapshot.exactZoneHrefCount === 0 &&
      homeSnapshot.nestedZoneHrefCount === 0 &&
      homeSnapshot.domainsActionCount === 1 &&
      homeSnapshot.busyCount === 0;
    if (!homeSignatureExact) throw new Error("DomainsRouteHomeSignatureError");

    const domainsAction = tab.playwright
      .locator('button, a, [role="button"], [role="link"]')
      .filter({ hasText: /^\s*Domains\s*$/i, visible: true });
    if (typeof domainsAction?.count !== "function" ||
        typeof domainsAction?.isVisible !== "function" ||
        typeof domainsAction?.click !== "function") {
      throw new Error("DomainsRouteActionShapeError");
    }
    counters.domainsCountAttempted++;
    domainsActionCount = await domainsAction.count();
    counters.domainsCountFulfilled++;
    if (domainsActionCount !== 1) throw new Error("DomainsRouteActionCountError");
    counters.domainsVisibleAttempted++;
    domainsActionVisible = await domainsAction.isVisible();
    counters.domainsVisibleFulfilled++;
    if (!domainsActionVisible) throw new Error("DomainsRouteActionVisibilityError");
    counters.domainsClickAttempted++;
    await domainsAction.click({ timeoutMs: 10000 });
    counters.domainsClickFulfilled++;

    const zoneAnchor = tab.playwright.locator("a[href]").filter({
      hasText: /^\s*mysw\.me\s*$/i,
      visible: true,
    });
    if (typeof zoneAnchor?.waitFor !== "function" ||
        typeof zoneAnchor?.count !== "function" ||
        typeof zoneAnchor?.getAttribute !== "function") {
      throw new Error("DomainsRouteZoneAnchorShapeError");
    }
    counters.zoneWaitAttempted++;
    await zoneAnchor.waitFor({ state: "visible", timeoutMs: 20000 });
    counters.zoneWaitFulfilled++;
    counters.domainsUrlAttempted++;
    const domainsUrl = new URL(await tab.url());
    counters.domainsUrlFulfilled++;
    const domainsPath = /^\/([0-9a-f]{32})\/home\/domains\/?$/.exec(
      domainsUrl.pathname,
    );
    domainsRouteExact =
      domainsUrl.protocol === "https:" &&
      domainsUrl.hostname === "dash.cloudflare.com" &&
      domainsPath !== null &&
      domainsPath[1] === homeAccountSegment;
    if (!domainsRouteExact) throw new Error("DomainsRouteTargetError");
    const accountSegment = homeAccountSegment;

    counters.zoneCountAttempted++;
    zoneAnchorCount = await zoneAnchor.count();
    counters.zoneCountFulfilled++;
    if (zoneAnchorCount !== 1) throw new Error("DomainsRouteZoneAnchorCountError");
    counters.zoneHrefAttempted++;
    const zoneHref = await zoneAnchor.getAttribute("href");
    counters.zoneHrefFulfilled++;
    if (typeof zoneHref !== "string") throw new Error("DomainsRouteZoneHrefError");
    const zoneUrl = new URL(zoneHref, "https://dash.cloudflare.com");
    const zonePath = /^\/([0-9a-f]{32})\/mysw\.me\/?$/.exec(zoneUrl.pathname);
    zoneHrefShapeExact =
      zoneUrl.protocol === "https:" &&
      zoneUrl.hostname === "dash.cloudflare.com" &&
      zonePath !== null &&
      zonePath[1] === accountSegment;
    if (!zoneHrefShapeExact) throw new Error("DomainsRouteZoneHrefShapeError");

    counters.zoneNavigationAttempted++;
    await tab.goto(zoneUrl.href);
    counters.zoneNavigationFulfilled++;
    counters.finalUrlAttempted++;
    const finalUrl = new URL(await tab.url());
    counters.finalUrlFulfilled++;
    const finalPath = /^\/([0-9a-f]{32})\/mysw\.me\/?$/.exec(finalUrl.pathname);
    zoneNavigationExact =
      finalUrl.protocol === "https:" &&
      finalUrl.hostname === "dash.cloudflare.com" &&
      finalPath !== null &&
      finalPath[1] === accountSegment;
    if (!zoneNavigationExact) throw new Error("DomainsRouteZoneNavigationError");

    const zoneMarker = tab.playwright.getByText("mysw.me", { exact: true })
      .filter({ visible: true });
    if (typeof zoneMarker?.waitFor !== "function" ||
        typeof zoneMarker?.count !== "function") {
      throw new Error("DomainsRouteZoneMarkerShapeError");
    }
    counters.markerWaitAttempted++;
    await zoneMarker.waitFor({ state: "visible", timeoutMs: 20000 });
    counters.markerWaitFulfilled++;
    counters.markerCountAttempted++;
    zoneMarkerCount = await zoneMarker.count();
    counters.markerCountFulfilled++;
    if (zoneMarkerCount !== 1) throw new Error("DomainsRouteZoneMarkerCountError");

    secureConsoleDashboardV27Eligible = true;
    secureConsoleDashboardV27State = "ZONE_ROUTE_READY_ELIGIBLE_V27";
    cleanupState = "SUCCESS_TAB_RETAINED";
    residueConverged = true;
    result = "EXACT_V27_DOMAINS_ROUTE_REACQUISITION_PASS";
  } catch (error) {
    errorClass = safeErrorClass(error);
  }

  if (result !== "EXACT_V27_DOMAINS_ROUTE_REACQUISITION_PASS") {
    secureConsoleDashboardV27Eligible = false;
    if (tab !== null && tab !== undefined && typeof tab.close === "function") {
      counters.closeAttempted++;
      try {
        await tab.close();
        counters.closeFulfilled++;
        secureConsoleDashboardV27RetainedTab = null;
        secureConsoleDashboardV27State = "V27_ROUTE_FAILED_CLEAN";
        cleanupState = "EXACT_TAB_CLOSED";
        residueConverged = true;
      } catch (closeError) {
        if (errorClass === "NONE") errorClass = safeErrorClass(closeError);
        secureConsoleDashboardV27RetainedTab = tab;
        secureConsoleDashboardV27State = "V27_ROUTE_FAILED_TAB_RETAINED";
        cleanupState = "EXACT_TAB_CLOSE_REJECTED";
        residueConverged = false;
      }
    } else if (counters.newAttempted === 0) {
      secureConsoleDashboardV27State = "V27_ROUTE_FAILED_CLEAN";
      cleanupState = "NO_TAB_CREATED";
    } else {
      secureConsoleDashboardV27State = "V27_ROUTE_FAILED_RESIDUE_UNPROVEN";
      cleanupState = "RESIDUE_UNPROVEN";
      residueConverged = false;
    }
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
    homeSnapshotValidated,
    homeSignatureExact,
    domainsActionCount,
    domainsActionVisible,
    domainsRouteExact,
    zoneAnchorCount,
    zoneHrefShapeExact,
    zoneNavigationExact,
    zoneMarkerCount,
    cleanupState,
    residueConverged,
    retainedExactHandle: secureConsoleDashboardV27RetainedTab !== null,
    eligible: secureConsoleDashboardV27Eligible,
    state: secureConsoleDashboardV27State,
    routeConsumed: secureConsoleDashboardV27RouteConsumed,
    readsConsumed: secureConsoleCloudflareReadsV27Consumed,
    preCreateDetachConsumed: secureConsoleDashboardV27PreCreateDetachConsumed,
    postNativeDetachConsumed: secureConsoleDashboardV27PostNativeDetachConsumed,
    ...counters,
    errorClass,
  });
})();
```

## Acceptance and review gate

Exact PASS requires the predecessor and controller ownership fields true; one
new tab; one home navigation, initial URL, visible-anchor wait, settled URL,
and snapshot; complete validated home signature;
a host-only first URL check, the condition-based visible-anchor settle, and a
second URL read that parses the original account-home segment before the click;
that segment is retained by every subsequent Domains/zone route;
exact Domains action count `1` and visibility true; click exactly `1 / 1`;
exact account Domains route; visible zone wait and count `1`; one href read with
same-account exact shape; one exact zone navigation/URL; visible zone marker
wait and count `1`; success retention; no close; route consumed true; reads and
both detach flags false; state `ZONE_ROUTE_READY_ELIGIBLE_V27`; error `NONE`;
and completed tool output.

Any non-PASS spends V27. No retry, fallback, continuation, reinterpretation,
manual integration, verdict relaxation, tab discovery, reconnect, alternate
browser path, or provider action is allowed. Failure must close only the exact
owned tab or retain that exact handle as residue evidence.

Independent Sol High review must verify the V23 consumed-failed-clean and V25
consumed-PASS-clean predecessors; V24 declaration absence; fixed target and
the consumed failed-clean V26 timing boundary; the condition-based settled-home
URL read; and binding every post-click route to that original pre-click account
segment; inherited V25 page signature and all-integer
completeness; unique visible action and zone cardinality; exact one-click and
navigation bounds; fixed-value-only output; success retention and failure
cleanup; no identifier/secret sink; no provider mutation; no retry; and both
mandatory manual confirmation boundaries.

Before a sole call, a later non-self-referential classification and fresh
action-time pins must revalidate exact committed artifacts and shape, source
projection, empty index, exact 12-path baseline, browser runtime hashes, clean
evidence worktree, zero residue, VM1205/DNS safe state, exact V23/V25/V26
persistent state, V24 declaration absence, and every V27 declaration absent.

The mandatory final Create/native Copy/native masked Paste confirmation and
later separate exact-row deletion confirmation remain unreached and mandatory.

`authorizes_live_execution=false`
