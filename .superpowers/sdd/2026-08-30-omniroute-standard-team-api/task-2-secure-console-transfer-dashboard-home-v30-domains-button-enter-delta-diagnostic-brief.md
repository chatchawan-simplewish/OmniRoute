# OmniRoute V30 Domains-button Enter delta diagnostic brief

`authorizes_live_execution=false`

## Design and scope

V29 consumed once and failed clean before any Enter press at evidence commit
`48359250c6346ba31225b42331867d4273788c6c`. It re-proved the unique visible
hit-testable, keyboard-reachable native button with no form owner, an existing
`aria-controls` target, and `aria-expanded` not true. It also proved that the
controlled container is geometrically visible even in that unexpanded state,
so container visibility is not a valid collapsed-state proxy.

Three candidate activation mechanisms were considered:

1. Press `Enter` exactly once on the uniquely revalidated button, then poll
   read-only state for at most five seconds. This is selected because it uses
   the button's proven keyboard semantics and preserves one-shot accounting.
2. Attempt another locator or coordinate click. Rejected because V27 already
   consumed and failed at that interaction class.
3. Navigate directly to an inferred Domains URL. Rejected because no Domains
   route or href has yet been observed.

V30 opens one fresh owned tab through the persistent V5 controller, restores
the exact settled account-home signature, and takes a fixed-key pre-snapshot.
It may press `Enter` only if the Domains button is still unique, visible,
enabled, non-inert, hit-testable, not already expanded, and its controlled
target exists and remains geometrically visible as V29 observed. Both the
fixed-key body snapshot and a separate read-only evaluation of the exact
counted press locator must prove `button.form === null`, excluding
browser-default form submission. The pre-snapshot also records bounded
controlled-link counts. One asynchronous read-only poll then waits only for a
real delta: expanded state, same-account Domains route, or a change in those
controlled-link counts. It closes the exact created tab on every reachable
path.

V30 emits no tag, role, ID, `aria-controls` value, href, URL, path, account or
zone identifier, text, DOM, HTML, screenshot, provider response, credential,
token, secret, clipboard value, or free-form exception message. It performs no
click, fill, submit, Create, edit, delete, DNS, rate-rule, Tunnel, Access,
API-token, permission, VM, routing, listener, process, reconnect, tab listing,
or tab reacquisition action. A rejection, timeout, uncertain result, cleanup
failure, or consumed state spends V30 permanently; there is no retry,
fallback, second key, click substitution, direct navigation, manual
integration, or verdict relaxation.

The mandatory later final Create/native Copy/native masked Paste confirmation
and the separate exact-row deletion confirmation remain untouched and cannot
be satisfied by V30.

## One-shot executable

```javascript
let secureConsoleDashboardV30ExpansionConsumed = false;
let secureConsoleDashboardV30RetainedTab = null;
let secureConsoleDashboardV30State = "UNCREATED";
await (async () => {
  const gateWasFresh = secureConsoleDashboardV30ExpansionConsumed === false;
  secureConsoleDashboardV30ExpansionConsumed = true;
  const counters = {
    newAttempted: 0, newFulfilled: 0,
    navigationAttempted: 0, navigationFulfilled: 0,
    initialUrlAttempted: 0, initialUrlFulfilled: 0,
    waitAttempted: 0, waitFulfilled: 0,
    settledUrlAttempted: 0, settledUrlFulfilled: 0,
    preSnapshotAttempted: 0, preSnapshotFulfilled: 0,
    locatorCountAttempted: 0, locatorCountFulfilled: 0,
    targetSafetyAttempted: 0, targetSafetyFulfilled: 0,
    pressAttempted: 0, pressFulfilled: 0,
    postSnapshotAttempted: 0, postSnapshotFulfilled: 0,
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
  const preBooleanKeys = [
    "hostExact", "accountHomePath", "uniqueButton", "visibleButton",
    "tagButton", "hrefAbsent", "nativeClickAbsent", "enabled",
    "nonInert", "formAbsent", "rectPositive", "withinViewport",
    "centerHitSelfOrDescendant", "pointerEventsEnabled", "controlsPresent",
    "controlsTargetPresent", "controlsTargetVisible", "expandedTrue",
    "tabStopPresent",
  ];
  const preIntegerKeys = [
    "buttonCount", "visibleButtonCount", "controlledAnchorCount",
    "controlledVisibleAnchorCount", "controlledAccountDomainsHrefCount",
    "controlledZoneHrefCount", "busyCount",
  ];
  const postBooleanKeys = [
    "hostExact", "accountHomePath", "accountDomainsPath", "routeChanged",
    "buttonUnique", "buttonVisible", "expandedTrue", "controlsPresent",
    "controlsTargetPresent", "controlsTargetVisible", "settleConditionMet",
  ];
  const postIntegerKeys = [
    "samples", "buttonCount", "visibleButtonCount", "controlledAnchorCount",
    "controlledVisibleAnchorCount", "controlledAccountDomainsHrefCount",
    "controlledZoneHrefCount", "allAnchorCount", "visibleAnchorCount",
    "exactZoneTextAnchorCount", "exactZoneHrefCount", "busyCount",
  ];
  const trustedRecord = (value, booleanKeys, integerKeys) => {
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
  let preSnapshotValidated = false;
  let preShapeExact = false;
  let pressTargetSafe = false;
  let postSnapshotValidated = false;
  let postSnapshotComplete = false;
  let preSnapshot = null;
  let postSnapshot = null;
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
      typeof secureConsoleDashboardV28DiagnosticConsumed === "boolean" &&
      typeof secureConsoleDashboardV29ExpansionConsumed === "boolean" &&
      typeof secureConsoleOwnedTaskTabV23PreCreateDetachConsumed === "boolean" &&
      typeof secureConsoleOwnedTaskTabV23PostNativeDetachConsumed === "boolean" &&
      typeof secureConsoleDashboardV26PreCreateDetachConsumed === "boolean" &&
      typeof secureConsoleDashboardV26PostNativeDetachConsumed === "boolean" &&
      typeof secureConsoleDashboardV27PreCreateDetachConsumed === "boolean" &&
      typeof secureConsoleDashboardV27PostNativeDetachConsumed === "boolean" &&
      typeof secureConsoleDashboardV30ExpansionConsumed === "boolean";
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
      secureConsoleDashboardV28DiagnosticConsumed === true &&
      secureConsoleDashboardV28RetainedTab === null &&
      secureConsoleDashboardV28State === "V28_DIAGNOSTIC_PASS_CLEAN" &&
      secureConsoleDashboardV29ExpansionConsumed === true &&
      secureConsoleDashboardV29RetainedTab === null &&
      secureConsoleDashboardV29State === "V29_DIAGNOSTIC_FAILED_CLEAN" &&
      secureConsoleDashboardV30RetainedTab === null &&
      secureConsoleDashboardV30State === "UNCREATED";
    if (!predecessorExact) throw new Error("DomainsExpansionPreconditionError");

    counters.newAttempted++;
    secureConsoleDashboardV30RetainedTab = tab =
      await secureConsoleChromeV5.tabs.new();
    counters.newFulfilled++;
    createdHandleCaptured = typeof tab === "object" && tab !== null;
    if (!createdHandleCaptured) throw new Error("DomainsExpansionHandleError");
    controllerOwnership = secureConsoleDashboardV30RetainedTab === tab;
    tabShape =
      controllerOwnership &&
      typeof tab.goto === "function" &&
      typeof tab.url === "function" &&
      typeof tab.close === "function" &&
      typeof tab.playwright?.locator === "function" &&
      typeof tab.playwright?.evaluate === "function";
    if (!tabShape) throw new Error("DomainsExpansionTabError");
    secureConsoleDashboardV30State = "DOMAINS_EXPANSION_RUNNING_V30";

    counters.navigationAttempted++;
    await tab.goto("https://dash.cloudflare.com");
    counters.navigationFulfilled++;
    counters.initialUrlAttempted++;
    const initialUrl = new URL(await tab.url());
    counters.initialUrlFulfilled++;
    if (initialUrl.protocol !== "https:" ||
        initialUrl.hostname !== "dash.cloudflare.com") {
      throw new Error("DomainsExpansionInitialNavigationError");
    }

    const firstVisibleAnchor = tab.playwright.locator("a[href]:visible").first();
    if (typeof firstVisibleAnchor?.waitFor !== "function") {
      throw new Error("DomainsExpansionWaitShapeError");
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
      throw new Error("DomainsExpansionSettledNavigationError");
    }
    const homeAccountSegment = homePath[1];

    counters.preSnapshotAttempted++;
    const untrustedPreSnapshot = await tab.playwright.locator("body").evaluate(
      (body, accountSegment) => {
        const normalize = (value) =>
          (value || "").replace(/\s+/g, " ").trim().toLowerCase();
        const buttons = [...body.querySelectorAll("button")].filter((item) =>
          normalize(item.textContent) === "domains");
        const visibleButtons = buttons.filter((item) =>
          item.getClientRects().length > 0);
        const button = buttons.length === 1 ? buttons[0] : null;
        const controls = button?.getAttribute("aria-controls") || "";
        const target = controls.length > 0 ? document.getElementById(controls) : null;
        const rect = button?.getBoundingClientRect();
        const rectPositive = rect !== undefined && rect.width > 0 && rect.height > 0;
        const centerX = rectPositive ? rect.left + rect.width / 2 : -1;
        const centerY = rectPositive ? rect.top + rect.height / 2 : -1;
        const withinViewport = rectPositive && centerX >= 0 && centerY >= 0 &&
          centerX < innerWidth && centerY < innerHeight;
        const centerHit = withinViewport
          ? document.elementFromPoint(centerX, centerY)
          : null;
        const disabled = button !== null &&
          (("disabled" in button && button.disabled === true) ||
            button.hasAttribute("disabled") ||
            button.getAttribute("aria-disabled") === "true");
        const targetVisible = target !== null && target.getClientRects().length > 0 &&
          getComputedStyle(target).display !== "none" &&
          getComputedStyle(target).visibility !== "hidden";
        const controlledAnchors = target === null
          ? []
          : [...target.querySelectorAll("a[href]")];
        const controlledVisibleAnchors = controlledAnchors.filter((item) =>
          item.getClientRects().length > 0);
        const controlledPaths = controlledAnchors.map((item) => {
          try {
            const url = new URL(item.getAttribute("href") || "", location.href);
            return url.protocol === "https:" &&
              url.hostname === "dash.cloudflare.com" ? url.pathname : "";
          } catch {
            return "";
          }
        });
        return {
          hostExact: location.protocol === "https:" &&
            location.hostname === "dash.cloudflare.com",
          accountHomePath: /^\/[0-9a-f]{32}\/home\/?$/.test(location.pathname),
          uniqueButton: buttons.length === 1,
          visibleButton: visibleButtons.length === 1,
          tagButton: button?.tagName === "BUTTON",
          hrefAbsent: !button?.hasAttribute("href"),
          nativeClickAbsent: typeof button?.click !== "function",
          enabled: button !== null && !disabled,
          nonInert: button !== null && !button.hasAttribute("inert"),
          formAbsent: button !== null && "form" in button && button.form === null,
          rectPositive,
          withinViewport,
          centerHitSelfOrDescendant:
            button !== null && centerHit !== null &&
            (centerHit === button || button.contains(centerHit)),
          pointerEventsEnabled:
            button !== null && getComputedStyle(button).pointerEvents !== "none",
          controlsPresent: controls.length > 0,
          controlsTargetPresent: target !== null,
          controlsTargetVisible: targetVisible,
          expandedTrue: button?.getAttribute("aria-expanded") === "true",
          tabStopPresent: button !== null && button.tabIndex >= 0,
          buttonCount: buttons.length,
          visibleButtonCount: visibleButtons.length,
          controlledAnchorCount: controlledAnchors.length,
          controlledVisibleAnchorCount: controlledVisibleAnchors.length,
          controlledAccountDomainsHrefCount: controlledPaths.filter((path) =>
            new RegExp(`^/${accountSegment}/home/domains/?$`).test(path)).length,
          controlledZoneHrefCount: controlledPaths.filter((path) =>
            new RegExp(`^/${accountSegment}/mysw\\.me/?$`).test(path)).length,
          busyCount:
            body.querySelectorAll('[aria-busy="true"], [role="progressbar"]').length,
        };
      },
      homeAccountSegment,
    );
    counters.preSnapshotFulfilled++;
    const trustedPreSnapshot = trustedRecord(
      untrustedPreSnapshot,
      preBooleanKeys,
      preIntegerKeys,
    );
    preSnapshotValidated = trustedPreSnapshot !== null;
    if (!preSnapshotValidated) {
      throw new Error("DomainsExpansionPreSnapshotValidationError");
    }
    preSnapshot = trustedPreSnapshot;
    preShapeExact =
      preSnapshot.hostExact === true &&
      preSnapshot.accountHomePath === true &&
      preSnapshot.uniqueButton === true &&
      preSnapshot.visibleButton === true &&
      preSnapshot.tagButton === true &&
      preSnapshot.hrefAbsent === true &&
      preSnapshot.nativeClickAbsent === true &&
      preSnapshot.enabled === true &&
      preSnapshot.nonInert === true &&
      preSnapshot.formAbsent === true &&
      preSnapshot.rectPositive === true &&
      preSnapshot.withinViewport === true &&
      preSnapshot.centerHitSelfOrDescendant === true &&
      preSnapshot.pointerEventsEnabled === true &&
      preSnapshot.controlsPresent === true &&
      preSnapshot.controlsTargetPresent === true &&
      preSnapshot.controlsTargetVisible === true &&
      preSnapshot.expandedTrue === false &&
      preSnapshot.tabStopPresent === true &&
      preSnapshot.buttonCount === 1 &&
      preSnapshot.visibleButtonCount === 1 &&
      preSnapshot.busyCount === 0;
    if (!preShapeExact) throw new Error("DomainsExpansionPreShapeError");

    const domainsButton = tab.playwright.locator("button").filter({
      hasText: /^\s*Domains\s*$/i,
      visible: true,
    });
    if (typeof domainsButton?.count !== "function" ||
        typeof domainsButton?.press !== "function") {
      throw new Error("DomainsExpansionLocatorShapeError");
    }
    counters.locatorCountAttempted++;
    const domainsButtonCount = await domainsButton.count();
    counters.locatorCountFulfilled++;
    if (domainsButtonCount !== 1) {
      throw new Error("DomainsExpansionLocatorCountError");
    }
    counters.targetSafetyAttempted++;
    pressTargetSafe = await domainsButton.evaluate((button) =>
      button.tagName === "BUTTON" && "form" in button && button.form === null,
    );
    counters.targetSafetyFulfilled++;
    if (pressTargetSafe !== true) {
      throw new Error("DomainsExpansionSubmitSafetyError");
    }
    counters.pressAttempted++;
    await domainsButton.press("Enter", { timeoutMs: 5000 });
    counters.pressFulfilled++;

    counters.postSnapshotAttempted++;
    const untrustedPostSnapshot = await tab.playwright.evaluate(
      async (baseline) => {
        const normalize = (value) =>
          (value || "").replace(/\s+/g, " ").trim().toLowerCase();
        const started = Date.now();
        let samples = 0;
        while (true) {
          samples++;
          const body = document.body;
          const buttons = body === null ? [] :
            [...body.querySelectorAll("button")].filter((item) =>
              normalize(item.textContent) === "domains");
          const visibleButtons = buttons.filter((item) =>
            item.getClientRects().length > 0);
          const button = buttons.length === 1 ? buttons[0] : null;
          const controls = button?.getAttribute("aria-controls") || "";
          const target = controls.length > 0
            ? document.getElementById(controls)
            : null;
          const targetVisible = target !== null &&
            target.getClientRects().length > 0 &&
            getComputedStyle(target).display !== "none" &&
            getComputedStyle(target).visibility !== "hidden";
          const controlledAnchors = target === null
            ? []
            : [...target.querySelectorAll("a[href]")];
          const controlledVisibleAnchors = controlledAnchors.filter((item) =>
            item.getClientRects().length > 0);
          const allAnchors = body === null ? [] :
            [...body.querySelectorAll("a[href]")];
          const visibleAnchors = allAnchors.filter((item) =>
            item.getClientRects().length > 0);
          const pathOf = (item) => {
            try {
              const url = new URL(item.getAttribute("href") || "", location.href);
              return url.protocol === "https:" &&
                url.hostname === "dash.cloudflare.com" ? url.pathname : "";
            } catch {
              return "";
            }
          };
          const controlledPaths = controlledAnchors.map(pathOf);
          const allPaths = allAnchors.map(pathOf);
          const accountHomePath =
            new RegExp(`^/${baseline.accountSegment}/home/?$`).test(
              location.pathname,
            );
          const accountDomainsPath =
            new RegExp(`^/${baseline.accountSegment}/home/domains/?$`).test(
              location.pathname,
            );
          const expandedTrue = button?.getAttribute("aria-expanded") === "true";
          const controlledAccountDomainsHrefCount = controlledPaths.filter((path) =>
            new RegExp(`^/${baseline.accountSegment}/home/domains/?$`).test(
              path,
            )).length;
          const controlledZoneHrefCount = controlledPaths.filter((path) =>
            new RegExp(`^/${baseline.accountSegment}/mysw\\.me/?$`).test(
              path,
            )).length;
          const settleConditionMet = accountDomainsPath || expandedTrue ||
            controlledAnchors.length !== baseline.controlledAnchorCount ||
            controlledVisibleAnchors.length !==
              baseline.controlledVisibleAnchorCount ||
            controlledAccountDomainsHrefCount !==
              baseline.controlledAccountDomainsHrefCount ||
            controlledZoneHrefCount !== baseline.controlledZoneHrefCount;
          const expired = Date.now() - started >= 5000;
          if (settleConditionMet || expired) {
            return {
              hostExact: location.protocol === "https:" &&
                location.hostname === "dash.cloudflare.com",
              accountHomePath,
              accountDomainsPath,
              routeChanged: !accountHomePath,
              buttonUnique: buttons.length === 1,
              buttonVisible: visibleButtons.length === 1,
              expandedTrue,
              controlsPresent: controls.length > 0,
              controlsTargetPresent: target !== null,
              controlsTargetVisible: targetVisible,
              settleConditionMet,
              samples,
              buttonCount: buttons.length,
              visibleButtonCount: visibleButtons.length,
              controlledAnchorCount: controlledAnchors.length,
              controlledVisibleAnchorCount: controlledVisibleAnchors.length,
              controlledAccountDomainsHrefCount,
              controlledZoneHrefCount,
              allAnchorCount: allAnchors.length,
              visibleAnchorCount: visibleAnchors.length,
              exactZoneTextAnchorCount: allAnchors.filter((item) =>
                normalize(item.textContent) === "mysw.me").length,
              exactZoneHrefCount: allPaths.filter((path) =>
                new RegExp(`^/${baseline.accountSegment}/mysw\\.me/?$`).test(
                  path,
                )).length,
              busyCount: body === null ? 0 :
                body.querySelectorAll(
                  '[aria-busy="true"], [role="progressbar"]',
                ).length,
            };
          }
          await new Promise((resolve) => setTimeout(resolve, 100));
        }
      },
      {
        accountSegment: homeAccountSegment,
        controlledAnchorCount: preSnapshot.controlledAnchorCount,
        controlledVisibleAnchorCount: preSnapshot.controlledVisibleAnchorCount,
        controlledAccountDomainsHrefCount:
          preSnapshot.controlledAccountDomainsHrefCount,
        controlledZoneHrefCount: preSnapshot.controlledZoneHrefCount,
      },
      { timeoutMs: 7000 },
    );
    counters.postSnapshotFulfilled++;
    const trustedPostSnapshot = trustedRecord(
      untrustedPostSnapshot,
      postBooleanKeys,
      postIntegerKeys,
    );
    postSnapshotValidated = trustedPostSnapshot !== null;
    if (!postSnapshotValidated) {
      throw new Error("DomainsExpansionPostSnapshotValidationError");
    }
    postSnapshot = trustedPostSnapshot;
    postSnapshotComplete =
      postSnapshot.hostExact === true &&
      (postSnapshot.accountHomePath === true ||
        postSnapshot.accountDomainsPath === true) &&
      !(postSnapshot.accountHomePath === true &&
        postSnapshot.accountDomainsPath === true) &&
      postSnapshot.samples > 0 &&
      postSnapshot.allAnchorCount > 0 &&
      postSnapshot.visibleAnchorCount > 0 &&
      postSnapshot.busyCount === 0;
    if (!postSnapshotComplete) {
      throw new Error("DomainsExpansionPostSnapshotCompletenessError");
    }
    result = "EXACT_V30_DOMAINS_BUTTON_ENTER_DELTA_DIAGNOSTIC_PASS";
  } catch (error) {
    errorClass = safeErrorClass(error);
  }

  if (tab !== null && tab !== undefined && typeof tab.close === "function") {
    counters.closeAttempted++;
    try {
      await tab.close();
      counters.closeFulfilled++;
      secureConsoleDashboardV30RetainedTab = null;
      secureConsoleDashboardV30State =
        result === "EXACT_V30_DOMAINS_BUTTON_ENTER_DELTA_DIAGNOSTIC_PASS"
          ? "V30_DIAGNOSTIC_PASS_CLEAN"
          : "V30_DIAGNOSTIC_FAILED_CLEAN";
      cleanupState = "EXACT_TAB_CLOSED";
      residueConverged = true;
    } catch (closeError) {
      if (errorClass === "NONE") errorClass = safeErrorClass(closeError);
      secureConsoleDashboardV30RetainedTab = tab;
      secureConsoleDashboardV30State = "V30_DIAGNOSTIC_FAILED_TAB_RETAINED";
      cleanupState = "EXACT_TAB_CLOSE_REJECTED";
      residueConverged = false;
      result = "PRECONDITION_FAIL";
    }
  } else if (counters.newAttempted === 0) {
    secureConsoleDashboardV30State = "V30_DIAGNOSTIC_FAILED_CLEAN";
    cleanupState = "NO_TAB_CREATED";
  } else {
    secureConsoleDashboardV30State = "V30_DIAGNOSTIC_FAILED_RESIDUE_UNPROVEN";
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
    preSnapshotValidated,
    preShapeExact,
    pressTargetSafe,
    postSnapshotValidated,
    postSnapshotComplete,
    preSnapshot,
    postSnapshot,
    cleanupState,
    residueConverged,
    retainedExactHandle: secureConsoleDashboardV30RetainedTab !== null,
    state: secureConsoleDashboardV30State,
    consumed: secureConsoleDashboardV30ExpansionConsumed,
    ...counters,
    errorClass,
  });
})();
```

## Pre-execution gates

Before any V30 Node call:

- commit this exact brief alone and record its byte count, SHA-256, blob, and
  normalized executable byte count/SHA-256;
- obtain an independent `gpt-5.6-sol` High review with zero unresolved
  Critical, HIGH, or IMPORTANT findings;
- commit a non-self-referential classification whose direct parent is that
  PASS review and record the post-commit coordinator tuple;
- revalidate the exact source projection, empty index, exact 12-path dirty
  baseline, runtime hashes, evidence worktree, no temporary/process residue,
  VM1205 safe checkpoint, absent public DNS, persistent controller, exact
  predecessor state, and absent V30 declarations;
- extract the executable from the committed brief and require its exact
  reviewed normalized bytes and SHA-256 before the sole Node call.

Only a fresh state satisfying all gates is eligible. The first Node call that
receives the executable consumes V30 before any precondition is evaluated.

## Success and failure classification

`PASS_CLEAN` requires the fixed PASS result, every declared validation and
completeness boolean true, `pressAttempted/pressFulfilled=1/1`,
`closeAttempted/closeFulfilled=1/1`, `EXACT_TAB_CLOSED`, residue convergence,
no retained exact handle, state `V30_DIAGNOSTIC_PASS_CLEAN`, consumed true,
and error class `NONE`. `settleConditionMet` is diagnostic evidence and need
not be true for the bounded interaction itself to classify PASS.

Anything else is failed, uncertain, or residue-bearing. Close only the exact
created handle when possible, record sanitized fixed evidence, classify V30
spent, and stop. Never retry or continue V30.
