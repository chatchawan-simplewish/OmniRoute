# OmniRoute V32 observed zone-route API-signature brief

authorizes_live_execution=false

## Design and scope

V31 consumed once and passed clean at evidence commit
cfb34f1b1ae5dc2efe7d3f664cd539a88607a14c. It proved that the reviewed
Domains-button Enter press caused no route, expansion, or controlled-link
delta after five seconds. It also proved exactly one anchor href matching the
same-account mysw.me zone route. The report is 3834 bytes, SHA-256
F73D45DDACB2C9A2FF3CF6A98027ED726AD166210BC08D86889828E2E31C4778,
and blob 6336bbeb3dfc6f1b1952dd37e9c04f407e8280bc.

V32 takes the minimum native route now supported by direct evidence. It opens
one fresh owned tab through the persistent V5 controller, restores the exact
account-home signature, and freshly requires exactly one anchor href whose
parsed host and pathname match the same-account mysw.me zone route. It then
uses one direct goto to the freshly observed and strictly validated href,
including any observed query or fragment, then waits once for bounded network
idle, reads the settled URL once, and takes one synchronous fixed-shape page
snapshot. No UI activation is retried.

The post snapshot emits only booleans and bounded counters for the exact zone
route/prefix, visible anchors, API-token text and href signatures, profile and
same-account token-route signatures, account/profile navigation labels, and
busy state. It never emits an href, URL, path, account ID, zone identifier,
text, DOM, HTML, screenshot, provider response, credential, token, secret,
clipboard value, or free-form exception message.

V32 performs no click, press, fill, submit, Create, edit, delete, DNS,
rate-rule, Tunnel, Access, API-token, permission, VM, routing, listener,
process, reconnect, tab listing, or tab reacquisition action. Any failure,
rejection, timeout, uncertainty, residue, or cleanup mismatch spends V32
permanently; there is no retry, fallback, UI substitution, inferred route,
manual integration, or verdict relaxation.

The mandatory later final Create/native Copy/native masked Paste confirmation
and the separate exact-row deletion confirmation remain untouched.

## One-shot executable

~~~javascript
let secureConsoleZoneV32Consumed = false;
let secureConsoleZoneV32RetainedTab = null;
let secureConsoleZoneV32State = "UNCREATED";
await (async () => {
  const gateWasFresh = secureConsoleZoneV32Consumed === false;
  secureConsoleZoneV32Consumed = true;
  const counters = {
    newAttempted: 0, newFulfilled: 0,
    homeNavigationAttempted: 0, homeNavigationFulfilled: 0,
    homeWaitAttempted: 0, homeWaitFulfilled: 0,
    homeUrlAttempted: 0, homeUrlFulfilled: 0,
    preSnapshotAttempted: 0, preSnapshotFulfilled: 0,
    zoneNavigationAttempted: 0, zoneNavigationFulfilled: 0,
    zoneWaitAttempted: 0, zoneWaitFulfilled: 0,
    zoneUrlAttempted: 0, zoneUrlFulfilled: 0,
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
  const preBooleanKeys = ["hostExact", "accountHomePath"];
  const preIntegerKeys = [
    "exactZoneHrefCount", "allAnchorCount", "busyCount",
  ];
  const postBooleanKeys = [
    "hostExact", "zonePathExact", "zonePathPrefix", "accountHomePath",
  ];
  const postIntegerKeys = [
    "allAnchorCount", "visibleAnchorCount",
    "exactApiTokensTextAnchorCount", "visibleExactApiTokensTextAnchorCount",
    "apiTokensHrefCount", "profileApiTokensHrefCount",
    "accountApiTokensHrefCount", "exactApiTokensTextButtonCount",
    "manageAccountTextCount", "profileTextCount", "busyCount",
  ];
  let result = "PRECONDITION_FAIL";
  let declarationShape = false;
  let predecessorExact = false;
  let controllerOwnership = false;
  let createdHandleCaptured = false;
  let tabShape = false;
  let homeUrlValidated = false;
  let preSnapshotValidated = false;
  let preShapeExact = false;
  let observedZoneUrlValidated = false;
  let zoneUrlValidated = false;
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
      typeof secureConsoleDashboardV30ExpansionConsumed === "boolean" &&
      typeof secureConsoleDashboardV31ExpansionConsumed === "boolean" &&
      typeof secureConsoleZoneV32Consumed === "boolean";
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
      secureConsoleDashboardV30ExpansionConsumed === true &&
      secureConsoleDashboardV30RetainedTab === null &&
      secureConsoleDashboardV30State === "V30_DIAGNOSTIC_FAILED_CLEAN" &&
      secureConsoleDashboardV31ExpansionConsumed === true &&
      secureConsoleDashboardV31RetainedTab === null &&
      secureConsoleDashboardV31State === "V31_DIAGNOSTIC_PASS_CLEAN" &&
      secureConsoleZoneV32RetainedTab === null &&
      secureConsoleZoneV32State === "UNCREATED";
    if (!predecessorExact) throw new Error("ZoneRoutePreconditionError");

    counters.newAttempted++;
    secureConsoleZoneV32RetainedTab = tab =
      await secureConsoleChromeV5.tabs.new();
    counters.newFulfilled++;
    createdHandleCaptured = typeof tab === "object" && tab !== null;
    if (!createdHandleCaptured) throw new Error("ZoneRouteHandleError");
    controllerOwnership = secureConsoleZoneV32RetainedTab === tab;
    tabShape =
      controllerOwnership &&
      typeof tab.goto === "function" &&
      typeof tab.url === "function" &&
      typeof tab.close === "function" &&
      typeof tab.playwright?.waitForTimeout === "function" &&
      typeof tab.playwright?.locator === "function";
    if (!tabShape) throw new Error("ZoneRouteTabShapeError");

    counters.homeNavigationAttempted++;
    await tab.goto("https://dash.cloudflare.com/");
    counters.homeNavigationFulfilled++;
    counters.homeWaitAttempted++;
    await tab.playwright.waitForTimeout(20000, { state: "networkidle" });
    counters.homeWaitFulfilled++;
    counters.homeUrlAttempted++;
    const homeUrl = await tab.url();
    counters.homeUrlFulfilled++;
    const homeMatch =
      /^https:\/\/dash\.cloudflare\.com\/([0-9a-f]{32})\/home\/?$/.exec(
        homeUrl,
      );
    homeUrlValidated = homeMatch !== null;
    if (!homeUrlValidated) throw new Error("ZoneRouteHomeUrlError");
    const accountSegment = homeMatch[1];

    counters.preSnapshotAttempted++;
    const untrustedPreSnapshot =
      await tab.playwright.locator("body").evaluate(
        (body, segment) => {
          const anchors = [...body.querySelectorAll("a[href]")];
          const exactZoneAnchors = anchors.filter((item) => {
            try {
              const url = new URL(
                item.getAttribute("href") || "",
                location.href,
              );
              return url.protocol === "https:" &&
                url.hostname === "dash.cloudflare.com" &&
                new RegExp("^/" + segment + "/mysw\\.me/?$").test(
                  url.pathname,
                );
            } catch {
              return false;
            }
          });
          const exactZoneHrefCount = exactZoneAnchors.length;
          return {
            hostExact: location.protocol === "https:" &&
              location.hostname === "dash.cloudflare.com",
            accountHomePath:
              new RegExp("^/" + segment + "/home/?$").test(location.pathname),
            exactZoneHrefCount,
            observedZoneHref: exactZoneHrefCount === 1
              ? exactZoneAnchors[0].getAttribute("href") || ""
              : "",
            allAnchorCount: anchors.length,
            busyCount: body.querySelectorAll(
              '[aria-busy="true"], [role="progressbar"]',
            ).length,
          };
        },
        accountSegment,
      );
    counters.preSnapshotFulfilled++;
    const untrustedPreShape =
      plainRecord(untrustedPreSnapshot) &&
      exactKeys(
        untrustedPreSnapshot,
        [...preBooleanKeys, ...preIntegerKeys, "observedZoneHref"],
      ) &&
      typeof untrustedPreSnapshot.observedZoneHref === "string" &&
      untrustedPreSnapshot.observedZoneHref.length > 0 &&
      untrustedPreSnapshot.observedZoneHref.length <= 2048 &&
      !/[\u0000-\u001f\u007f]/.test(
        untrustedPreSnapshot.observedZoneHref,
      );
    let observedZoneUrl = null;
    if (untrustedPreShape) {
      try {
        observedZoneUrl = new URL(
          untrustedPreSnapshot.observedZoneHref,
          homeUrl,
        );
      } catch {}
    }
    observedZoneUrlValidated =
      observedZoneUrl !== null &&
      observedZoneUrl.protocol === "https:" &&
      observedZoneUrl.hostname === "dash.cloudflare.com" &&
      observedZoneUrl.port === "" &&
      observedZoneUrl.username === "" &&
      observedZoneUrl.password === "" &&
      new RegExp(
        "^/" + accountSegment + "/mysw\\.me/?$",
      ).test(observedZoneUrl.pathname);
    preSnapshot = trustedRecord(
      untrustedPreShape ? {
        hostExact: untrustedPreSnapshot.hostExact,
        accountHomePath: untrustedPreSnapshot.accountHomePath,
        exactZoneHrefCount: untrustedPreSnapshot.exactZoneHrefCount,
        allAnchorCount: untrustedPreSnapshot.allAnchorCount,
        busyCount: untrustedPreSnapshot.busyCount,
      } : null,
      preBooleanKeys,
      preIntegerKeys,
    );
    preSnapshotValidated = preSnapshot !== null;
    preShapeExact =
      preSnapshotValidated &&
      preSnapshot.hostExact === true &&
      preSnapshot.accountHomePath === true &&
      preSnapshot.exactZoneHrefCount === 1 &&
      preSnapshot.allAnchorCount > 0 &&
      preSnapshot.busyCount === 0 &&
      observedZoneUrlValidated === true;
    if (!preShapeExact) throw new Error("ZoneRoutePreShapeError");

    counters.zoneNavigationAttempted++;
    await tab.goto(observedZoneUrl.href);
    counters.zoneNavigationFulfilled++;
    counters.zoneWaitAttempted++;
    await tab.playwright.waitForTimeout(20000, { state: "networkidle" });
    counters.zoneWaitFulfilled++;
    counters.zoneUrlAttempted++;
    const settledZoneUrl = await tab.url();
    counters.zoneUrlFulfilled++;
    let settledZoneParsed = null;
    try {
      settledZoneParsed = new URL(settledZoneUrl);
    } catch {}
    zoneUrlValidated =
      settledZoneParsed !== null &&
      settledZoneParsed.protocol === "https:" &&
      settledZoneParsed.hostname === "dash.cloudflare.com" &&
      new RegExp(
        "^/" + accountSegment + "/mysw\\.me(?:/|$)",
      ).test(settledZoneParsed.pathname);
    if (!zoneUrlValidated) throw new Error("ZoneRouteSettledUrlError");

    counters.postSnapshotAttempted++;
    const untrustedPostSnapshot =
      await tab.playwright.locator("body").evaluate(
        (body, segment) => {
          const normalize = (value) =>
            (value || "").replace(/\s+/g, " ").trim().toLowerCase();
          const anchors = [...body.querySelectorAll("a[href]")];
          const visibleAnchors = anchors.filter((item) =>
            item.getClientRects().length > 0);
          const buttons = [...body.querySelectorAll("button")];
          const paths = anchors.map((item) => {
            try {
              const url = new URL(
                item.getAttribute("href") || "",
                location.href,
              );
              return url.protocol === "https:" &&
                url.hostname === "dash.cloudflare.com" ? url.pathname : "";
            } catch {
              return "";
            }
          });
          const apiTokensPattern = /(^|\/)api-tokens(\/|$)/i;
          const profileApiTokensPattern = /^\/profile\/api-tokens\/?$/i;
          const accountApiTokensPattern = new RegExp(
            "^/" + segment + "/(?:[^/]+/)*api-tokens/?$",
            "i",
          );
          const zoneExactPattern = new RegExp(
            "^/" + segment + "/mysw\\.me/?$",
          );
          const zonePrefixPattern = new RegExp(
            "^/" + segment + "/mysw\\.me(?:/|$)",
          );
          return {
            hostExact: location.protocol === "https:" &&
              location.hostname === "dash.cloudflare.com",
            zonePathExact: zoneExactPattern.test(location.pathname),
            zonePathPrefix: zonePrefixPattern.test(location.pathname),
            accountHomePath:
              new RegExp("^/" + segment + "/home/?$").test(location.pathname),
            allAnchorCount: anchors.length,
            visibleAnchorCount: visibleAnchors.length,
            exactApiTokensTextAnchorCount: anchors.filter((item) =>
              normalize(item.textContent) === "api tokens").length,
            visibleExactApiTokensTextAnchorCount:
              visibleAnchors.filter((item) =>
                normalize(item.textContent) === "api tokens").length,
            apiTokensHrefCount:
              paths.filter((path) => apiTokensPattern.test(path)).length,
            profileApiTokensHrefCount:
              paths.filter((path) =>
                profileApiTokensPattern.test(path)).length,
            accountApiTokensHrefCount:
              paths.filter((path) =>
                accountApiTokensPattern.test(path)).length,
            exactApiTokensTextButtonCount: buttons.filter((item) =>
              normalize(item.textContent) === "api tokens").length,
            manageAccountTextCount:
              [...anchors, ...buttons].filter((item) =>
                normalize(item.textContent) === "manage account").length,
            profileTextCount: [...anchors, ...buttons].filter((item) =>
              normalize(item.textContent) === "my profile" ||
              normalize(item.textContent) === "profile").length,
            busyCount: body.querySelectorAll(
              '[aria-busy="true"], [role="progressbar"]',
            ).length,
          };
        },
        accountSegment,
        { timeoutMs: 5000 },
      );
    counters.postSnapshotFulfilled++;
    postSnapshot = trustedRecord(
      untrustedPostSnapshot,
      postBooleanKeys,
      postIntegerKeys,
    );
    postSnapshotValidated = postSnapshot !== null;
    postSnapshotComplete =
      postSnapshotValidated &&
      postSnapshot.hostExact === true &&
      postSnapshot.zonePathPrefix === true &&
      postSnapshot.accountHomePath === false &&
      postSnapshot.allAnchorCount > 0 &&
      postSnapshot.visibleAnchorCount > 0 &&
      postSnapshot.busyCount === 0;
    if (!postSnapshotComplete) {
      throw new Error("ZoneRoutePostSnapshotError");
    }
    result = "EXACT_V32_OBSERVED_ZONE_ROUTE_API_SIGNATURE_PASS";
  } catch (error) {
    errorClass = safeErrorClass(error);
  }

  if (tab !== null && tab !== undefined && typeof tab.close === "function") {
    counters.closeAttempted++;
    try {
      await tab.close();
      counters.closeFulfilled++;
      secureConsoleZoneV32RetainedTab = null;
      secureConsoleZoneV32State =
        result === "EXACT_V32_OBSERVED_ZONE_ROUTE_API_SIGNATURE_PASS"
          ? "V32_DIAGNOSTIC_PASS_CLEAN"
          : "V32_DIAGNOSTIC_FAILED_CLEAN";
      cleanupState = "EXACT_TAB_CLOSED";
      residueConverged = true;
    } catch (closeError) {
      if (errorClass === "NONE") errorClass = safeErrorClass(closeError);
      secureConsoleZoneV32RetainedTab = tab;
      secureConsoleZoneV32State = "V32_DIAGNOSTIC_FAILED_TAB_RETAINED";
      cleanupState = "EXACT_TAB_CLOSE_REJECTED";
      residueConverged = false;
      result = "PRECONDITION_FAIL";
    }
  } else if (counters.newAttempted === 0) {
    secureConsoleZoneV32State = "V32_DIAGNOSTIC_FAILED_CLEAN";
    cleanupState = "NO_TAB_CREATED";
  } else {
    secureConsoleZoneV32State = "V32_DIAGNOSTIC_FAILED_RESIDUE_UNPROVEN";
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
    homeUrlValidated,
    preSnapshotValidated,
    preShapeExact,
    observedZoneUrlValidated,
    zoneUrlValidated,
    postSnapshotValidated,
    postSnapshotComplete,
    preSnapshot,
    postSnapshot,
    cleanupState,
    residueConverged,
    retainedExactHandle: secureConsoleZoneV32RetainedTab !== null,
    state: secureConsoleZoneV32State,
    consumed: secureConsoleZoneV32Consumed,
    ...counters,
    errorClass,
  });
})();
~~~

## Pre-execution gates

Before any V32 Node call, commit this exact brief alone; obtain an independent
gpt-5.6-sol High review with zero unresolved Critical, HIGH, or IMPORTANT
findings; commit a non-self-referential classification whose direct parent is
that PASS review; record the post-commit coordinator tuple; and freshly
revalidate projection, index, exact 12-path baseline, runtime hashes, evidence
worktree, residue, VM1205, public DNS, persistent controller, exact predecessor
state, and absent V32 declarations. Extract the executable from the committed
brief and require its exact reviewed normalized bytes and SHA-256 before the
sole Node call.

The first Node call receiving the executable consumes V32 before any
precondition. PASS_CLEAN requires the fixed PASS result, every validation and
completeness boolean true, each declared non-cleanup attempted/fulfilled pair
1/1, close 1/1, EXACT_TAB_CLOSED, residue convergence, no retained handle,
state V32_DIAGNOSTIC_PASS_CLEAN, consumed true, and error class NONE.

Anything else is failed, uncertain, or residue-bearing. Close only the exact
created handle when possible, record fixed sanitized evidence, classify V32
spent, and stop. Never retry or continue V32.
