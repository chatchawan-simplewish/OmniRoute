# OmniRoute V28 Domains-action shape diagnostic replacement brief

`authorizes_live_execution=false`

## Scope and predecessor

V27 is consumed failed-clean at incident commit
`30bdcaa68ed5349e93905937683a6e7d286a9104`: the complete settled-home
signature, same-account bind, unique Domains count, and visibility passed, but
the sole locator click rejected before fulfillment. V23, V26, and V27 have now
failed at three different guarded route boundaries. V28 therefore does not
guess or attempt another activation method.

Fix round 1 closes IMPORTANT `V28-001` from independent review commit
`20e7795247f575cc87fcedca131feb83f8a892bb` by requiring all six V23, V26,
and V27 pre-create/post-native detach flags to exist as booleans and remain
false in the exact predecessor boundary.

V28 is a fresh-tab, one-shot, read-only structural diagnostic. It reproduces
only the proven condition-based settled-home boundary, takes one synchronous
fixed-key snapshot of the unique visible Domains element and its safe
activation characteristics, closes the exact tab, and emits only validated
booleans, bounded counts, counters, fixed states, and a sanitized error class.

It emits no tag name, role string, href, URL, path, account/zone ID, text, DOM,
HTML, attribute value, screenshot, provider response, credential, token,
secret, or clipboard value. It performs no click, fill, press, submit, Create,
edit, delete, DNS, rate-rule, Tunnel, Access, API-token, permission, VM,
routing, listener, process, reconnect, or tab-discovery action.

## One-shot executable

```javascript
let secureConsoleDashboardV28DiagnosticConsumed = false;
let secureConsoleDashboardV28RetainedTab = null;
let secureConsoleDashboardV28State = "UNCREATED";
await (async () => {
  const gateWasFresh = secureConsoleDashboardV28DiagnosticConsumed === false;
  secureConsoleDashboardV28DiagnosticConsumed = true;
  const counters = {
    newAttempted: 0, newFulfilled: 0,
    navigationAttempted: 0, navigationFulfilled: 0,
    initialUrlAttempted: 0, initialUrlFulfilled: 0,
    waitAttempted: 0, waitFulfilled: 0,
    settledUrlAttempted: 0, settledUrlFulfilled: 0,
    snapshotAttempted: 0, snapshotFulfilled: 0,
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
    "accountDomainsPath", "tagAnchor", "tagButton", "roleLink",
    "roleButton", "hrefPresent", "hrefSameHost",
    "hrefSameAccountDomainsPath", "nativeClickPresent", "disabledTrue",
    "ariaDisabledTrue", "inertTrue", "rectPositive", "withinViewport",
    "centerHitSelfOrDescendant", "pointerEventsNone", "targetBlank",
    "downloadPresent", "ariaControlsPresent", "ariaControlsTargetPresent",
    "dataHrefPresent", "tabStopPresent",
  ];
  const integerKeys = [
    "allAnchorCount", "visibleAnchorCount", "exactZoneTextAnchorCount",
    "containsZoneTextAnchorCount", "exactZoneHrefCount",
    "nestedZoneHrefCount", "accountRootHrefCount", "accountHomeHrefCount",
    "accountDomainsHrefCount", "websitesActionCount", "domainsActionCount",
    "visibleDomainsActionCount", "overviewActionCount", "accountActionCount",
    "mainCount", "navigationCount", "busyCount",
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
  let snapshotValidated = false;
  let snapshotComplete = false;
  let snapshot = null;
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
      typeof secureConsoleDashboardV27RouteConsumed === "boolean" &&
      typeof secureConsoleOwnedTaskTabV23PreCreateDetachConsumed === "boolean" &&
      typeof secureConsoleOwnedTaskTabV23PostNativeDetachConsumed === "boolean" &&
      typeof secureConsoleDashboardV26PreCreateDetachConsumed === "boolean" &&
      typeof secureConsoleDashboardV26PostNativeDetachConsumed === "boolean" &&
      typeof secureConsoleDashboardV27PreCreateDetachConsumed === "boolean" &&
      typeof secureConsoleDashboardV27PostNativeDetachConsumed === "boolean" &&
      typeof secureConsoleDashboardV28DiagnosticConsumed === "boolean";
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
      secureConsoleDashboardV27RouteConsumed === true &&
      secureConsoleDashboardV27RetainedTab === null &&
      secureConsoleDashboardV27Eligible === false &&
      secureConsoleDashboardV27State === "V27_ROUTE_FAILED_CLEAN" &&
      secureConsoleDashboardV27PreCreateDetachConsumed === false &&
      secureConsoleDashboardV27PostNativeDetachConsumed === false &&
      secureConsoleCloudflareReadsV27Consumed === false &&
      secureConsoleDashboardV28RetainedTab === null &&
      secureConsoleDashboardV28State === "UNCREATED";
    if (!predecessorExact) throw new Error("DomainsShapePreconditionError");

    counters.newAttempted++;
    secureConsoleDashboardV28RetainedTab = tab =
      await secureConsoleChromeV5.tabs.new();
    counters.newFulfilled++;
    createdHandleCaptured = typeof tab === "object" && tab !== null;
    if (!createdHandleCaptured) throw new Error("DomainsShapeHandleError");
    controllerOwnership = secureConsoleDashboardV28RetainedTab === tab;
    tabShape =
      controllerOwnership &&
      typeof tab.goto === "function" &&
      typeof tab.url === "function" &&
      typeof tab.close === "function" &&
      typeof tab.playwright?.locator === "function";
    if (!tabShape) throw new Error("DomainsShapeTabError");
    secureConsoleDashboardV28State = "DOMAINS_SHAPE_RUNNING_V28";

    counters.navigationAttempted++;
    await tab.goto("https://dash.cloudflare.com");
    counters.navigationFulfilled++;
    counters.initialUrlAttempted++;
    const initialUrl = new URL(await tab.url());
    counters.initialUrlFulfilled++;
    if (initialUrl.protocol !== "https:" ||
        initialUrl.hostname !== "dash.cloudflare.com") {
      throw new Error("DomainsShapeInitialNavigationError");
    }

    const firstVisibleAnchor = tab.playwright.locator("a[href]:visible").first();
    if (typeof firstVisibleAnchor?.waitFor !== "function") {
      throw new Error("DomainsShapeWaitShapeError");
    }
    counters.waitAttempted++;
    await firstVisibleAnchor.waitFor({ state: "visible", timeoutMs: 20000 });
    counters.waitFulfilled++;
    counters.settledUrlAttempted++;
    const settledUrl = new URL(await tab.url());
    counters.settledUrlFulfilled++;
    const homePath = /^\/([0-9a-f]{32})\/home\/?$/.exec(settledUrl.pathname);
    if (settledUrl.protocol !== "https:" ||
        settledUrl.hostname !== "dash.cloudflare.com" ||
        homePath === null) {
      throw new Error("DomainsShapeSettledNavigationError");
    }
    const homeAccountSegment = homePath[1];

    counters.snapshotAttempted++;
    const untrustedSnapshot = await tab.playwright.locator("body").evaluate(
      (body, accountSegment) => {
        const normalize = (value) =>
          (value || "").replace(/\s+/g, " ").trim().toLowerCase();
        const actionSelector = 'button, a, [role="button"], [role="link"]';
        const anchors = [...body.querySelectorAll("a[href]")];
        const visibleAnchors = anchors.filter((item) =>
          item.getClientRects().length > 0);
        const actions = [...body.querySelectorAll(actionSelector)];
        const domainsActions = actions.filter((item) =>
          normalize(item.textContent) === "domains");
        const visibleDomainsActions = domainsActions.filter((item) =>
          item.getClientRects().length > 0);
        const action = domainsActions.length === 1 ? domainsActions[0] : null;
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
        const tagName = action?.tagName || "";
        const role = normalize(action?.getAttribute("role"));
        const href = action?.getAttribute("href");
        let hrefSameHost = false;
        let hrefSameAccountDomainsPath = false;
        if (typeof href === "string" && href.length > 0) {
          try {
            const url = new URL(href, location.href);
            hrefSameHost = url.protocol === "https:" &&
              url.hostname === "dash.cloudflare.com";
            const match = /^\/([0-9a-f]{32})\/home\/domains\/?$/.exec(
              url.pathname,
            );
            hrefSameAccountDomainsPath =
              hrefSameHost && match !== null && match[1] === accountSegment;
          } catch {}
        }
        const rect = action?.getBoundingClientRect();
        const rectPositive = rect !== undefined && rect.width > 0 && rect.height > 0;
        const centerX = rectPositive ? rect.left + rect.width / 2 : -1;
        const centerY = rectPositive ? rect.top + rect.height / 2 : -1;
        const withinViewport = rectPositive && centerX >= 0 && centerY >= 0 &&
          centerX < innerWidth && centerY < innerHeight;
        const centerHit = withinViewport ? document.elementFromPoint(centerX, centerY) : null;
        const controls = action?.getAttribute("aria-controls") || "";
        const disabledTrue = action !== null &&
          (("disabled" in action && action.disabled === true) ||
            action.hasAttribute("disabled"));
        return {
          hostExact: location.protocol === "https:" &&
            location.hostname === "dash.cloudflare.com",
          rootPath: location.pathname === "/",
          accountRootPath: /^\/[0-9a-f]{32}\/?$/.test(location.pathname),
          accountHomePath:
            /^\/[0-9a-f]{32}\/home\/?$/.test(location.pathname),
          accountDomainsPath:
            /^\/[0-9a-f]{32}\/home\/domains\/?$/.test(location.pathname),
          tagAnchor: tagName === "A",
          tagButton: tagName === "BUTTON",
          roleLink: role === "link",
          roleButton: role === "button",
          hrefPresent: typeof href === "string" && href.length > 0,
          hrefSameHost,
          hrefSameAccountDomainsPath,
          nativeClickPresent: typeof action?.click === "function",
          disabledTrue,
          ariaDisabledTrue: action?.getAttribute("aria-disabled") === "true",
          inertTrue: action?.hasAttribute("inert") === true,
          rectPositive,
          withinViewport,
          centerHitSelfOrDescendant:
            action !== null && centerHit !== null &&
            (centerHit === action || action.contains(centerHit)),
          pointerEventsNone:
            action !== null && getComputedStyle(action).pointerEvents === "none",
          targetBlank: action?.getAttribute("target") === "_blank",
          downloadPresent: action?.hasAttribute("download") === true,
          ariaControlsPresent: controls.length > 0,
          ariaControlsTargetPresent:
            controls.length > 0 && document.getElementById(controls) !== null,
          dataHrefPresent: action?.hasAttribute("data-href") === true,
          tabStopPresent: action !== null && action.tabIndex >= 0,
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
          domainsActionCount: domainsActions.length,
          visibleDomainsActionCount: visibleDomainsActions.length,
          overviewActionCount: textCount("overview"),
          accountActionCount: actions.filter((item) =>
            /^account(?:s)?$/.test(normalize(item.textContent))).length,
          mainCount: body.querySelectorAll("main").length,
          navigationCount:
            body.querySelectorAll('nav, [role="navigation"]').length,
          busyCount:
            body.querySelectorAll('[aria-busy="true"], [role="progressbar"]').length,
        };
      },
      homeAccountSegment,
    );
    counters.snapshotFulfilled++;
    const trusted = trustedSnapshot(untrustedSnapshot);
    snapshotValidated = trusted !== null;
    if (!snapshotValidated) throw new Error("DomainsShapeValidationError");
    snapshot = trusted;
    snapshotComplete =
      snapshot.hostExact === true &&
      snapshot.accountHomePath === true &&
      snapshot.rootPath === false &&
      snapshot.accountRootPath === false &&
      snapshot.accountDomainsPath === false &&
      snapshot.allAnchorCount > 0 &&
      snapshot.visibleAnchorCount > 0 &&
      snapshot.exactZoneTextAnchorCount === 0 &&
      snapshot.containsZoneTextAnchorCount === 0 &&
      snapshot.exactZoneHrefCount === 0 &&
      snapshot.nestedZoneHrefCount === 0 &&
      snapshot.domainsActionCount === 1 &&
      snapshot.visibleDomainsActionCount === 1 &&
      snapshot.busyCount === 0;
    if (!snapshotComplete) throw new Error("DomainsShapeCompletenessError");
    result = "EXACT_V28_DOMAINS_ACTION_SHAPE_DIAGNOSTIC_PASS";
  } catch (error) {
    errorClass = safeErrorClass(error);
  }

  if (tab !== null && tab !== undefined && typeof tab.close === "function") {
    counters.closeAttempted++;
    try {
      await tab.close();
      counters.closeFulfilled++;
      secureConsoleDashboardV28RetainedTab = null;
      secureConsoleDashboardV28State =
        result === "EXACT_V28_DOMAINS_ACTION_SHAPE_DIAGNOSTIC_PASS"
          ? "V28_DIAGNOSTIC_PASS_CLEAN"
          : "V28_DIAGNOSTIC_FAILED_CLEAN";
      cleanupState = "EXACT_TAB_CLOSED";
      residueConverged = true;
    } catch (closeError) {
      if (errorClass === "NONE") errorClass = safeErrorClass(closeError);
      secureConsoleDashboardV28RetainedTab = tab;
      secureConsoleDashboardV28State = "V28_DIAGNOSTIC_FAILED_TAB_RETAINED";
      cleanupState = "EXACT_TAB_CLOSE_REJECTED";
      residueConverged = false;
      result = "PRECONDITION_FAIL";
    }
  } else if (counters.newAttempted === 0) {
    secureConsoleDashboardV28State = "V28_DIAGNOSTIC_FAILED_CLEAN";
    cleanupState = "NO_TAB_CREATED";
  } else {
    secureConsoleDashboardV28State = "V28_DIAGNOSTIC_FAILED_RESIDUE_UNPROVEN";
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
    retainedExactHandle: secureConsoleDashboardV28RetainedTab !== null,
    state: secureConsoleDashboardV28State,
    consumed: secureConsoleDashboardV28DiagnosticConsumed,
    ...counters,
    errorClass,
  });
})();
```

## Acceptance and review gate

Exact diagnostic PASS requires the exact consumed predecessors; one new tab;
one home navigation, initial URL, visible-anchor wait, settled URL, and fixed
snapshot; validation/completeness true; exact unique/visible Domains counts
`1 / 1`; exact close `1 / 1`; no retained handle; state
`V28_DIAGNOSTIC_PASS_CLEAN`; residue converged; consumed true; error `NONE`;
and completed tool output. All projected integers must be nonnegative.

The diagnostic intentionally accepts either value for every structural boolean.
Its purpose is to distinguish safe activation shapes without exposing content.
A replacement may use only the resulting fixed booleans/counts and must receive
a new independent review before any navigation click, native click, or press.

Any non-PASS spends V28. No retry, fallback, continuation, reinterpretation,
manual integration, verdict relaxation, tab discovery, reconnect, or alternate
browser path is allowed.

Independent Sol High review must verify the V27 consumed-failed-clean boundary,
the `V28-001` six-flag correction, the three-attempt architectural stop, the
diagnostic-only scope, complete
fixed-key cross-realm projection, account-local href comparison, no identifier
or attribute-value leakage, zero activation call sites, cleanup/cardinality,
secrets, no provider mutation, no retry, and both mandatory confirmations.

Before a sole call, a later non-self-referential classification and fresh
action-time pins must revalidate exact artifacts and shape, projection, empty
index, exact 12-path baseline, runtime hashes, clean evidence worktree, zero
residue, VM1205/DNS safe state, exact V23/V25/V26/V27 persistent state, V24
declaration absence, and all V28 declarations absent.

The mandatory final Create/native Copy/native masked Paste confirmation and
later separate exact-row deletion confirmation remain unreached and mandatory.

`authorizes_live_execution=false`
