# OmniRoute V33 zone-route outer-locator signature diagnostic brief

`authorizes_live_execution=false`

## Design and scope

V32 was consumed exactly once and failed cleanly at evidence commit
`7563e19717d5bf6a8b7ba09f4290167cdf554e53`. It proved that the private,
unique same-account `mysw.me` href can be captured, validated, navigated
without reconstruction, and settled on the expected Cloudflare zone prefix.
Its single post-navigation `body.evaluate` rejected before returning a
snapshot, so API-token/profile/manage-account signatures remain unproven.

Three successor designs were considered:

1. repeat the page evaluator with a timeout or smaller callback;
2. take a whole DOM/accessibility snapshot and project it afterward; or
3. keep the proven private navigation and replace the failing evaluator with
   fixed outer-realm locator counts.

Design 3 is selected under the standing preapproval. It changes one component
boundary, avoids replaying the unproven evaluator, and does not acquire or emit
a whole-page snapshot. Each outer count has an explicit attempted/fulfilled
pair and a fixed `postStage`, so a rejection identifies the exact boundary.
Every returned count is validated immediately as a safe integer in
`0..1000000` before the next probe, then projected again through the existing
exact-key validator. Fresh private URL reads bracket the probe sequence and
require exact origin, empty credentials/port, the same account/zone prefix, and
exact pre/post URL continuity. The counts are sequential route-bounded evidence,
not an atomic page-state snapshot.

V33 is diagnostic-only. It opens one exact new tab through the existing
`secureConsoleChromeV5` binding, loads account home, repeats V32's proven
private observed-href validation/navigation, and counts only:

- body and anchor presence;
- accessible exact `API Tokens` links and buttons;
- raw `/api-tokens` href-attribute candidate shapes, including literal
  relative profile/account forms;
- exact `Manage Account`, `My Profile`, and `Profile` text; and
- busy/progress indicators.

No raw href, URL, account identifier, page text, DOM snapshot, credential,
secret, or token value is written. There is no reconnect, tab listing,
reacquisition, click, press, fill, Create, Copy, Paste, provider mutation,
retry, fallback, manual integration, or verdict relaxation. V3 through V32
remain spent or static exactly as recorded. The mandatory later final
Create/native Copy/native masked Paste confirmation and the separate exact-row
deletion confirmation remain untouched.

## One-shot executable

~~~javascript
let secureConsoleZoneV33Consumed = false;
let secureConsoleZoneV33RetainedTab = null;
let secureConsoleZoneV33State = "UNCREATED";
await (async () => {
  const gateWasFresh = secureConsoleZoneV33Consumed === false;
  secureConsoleZoneV33Consumed = true;
  const counters = {
    newAttempted: 0, newFulfilled: 0,
    homeNavigationAttempted: 0, homeNavigationFulfilled: 0,
    homeWaitAttempted: 0, homeWaitFulfilled: 0,
    homeUrlAttempted: 0, homeUrlFulfilled: 0,
    preSnapshotAttempted: 0, preSnapshotFulfilled: 0,
    zoneNavigationAttempted: 0, zoneNavigationFulfilled: 0,
    zoneWaitAttempted: 0, zoneWaitFulfilled: 0,
    zoneUrlAttempted: 0, zoneUrlFulfilled: 0,
    postUrlAttempted: 0, postUrlFulfilled: 0,
    postSnapshotAttempted: 0, postSnapshotFulfilled: 0,
    bodyCountAttempted: 0, bodyCountFulfilled: 0,
    allAnchorCountAttempted: 0, allAnchorCountFulfilled: 0,
    roleApiTokensLinkCountAttempted: 0, roleApiTokensLinkCountFulfilled: 0,
    rawApiTokensHrefCandidateCountAttempted: 0, rawApiTokensHrefCandidateCountFulfilled: 0,
    rawRelativeProfileApiTokensHrefCandidateCountAttempted: 0, rawRelativeProfileApiTokensHrefCandidateCountFulfilled: 0,
    rawRelativeAccountApiTokensHrefCandidateCountAttempted: 0, rawRelativeAccountApiTokensHrefCandidateCountFulfilled: 0,
    roleApiTokensButtonCountAttempted: 0, roleApiTokensButtonCountFulfilled: 0,
    manageAccountTextCountAttempted: 0, manageAccountTextCountFulfilled: 0,
    myProfileTextCountAttempted: 0, myProfileTextCountFulfilled: 0,
    profileTextCountAttempted: 0, profileTextCountFulfilled: 0,
    busyCountAttempted: 0, busyCountFulfilled: 0,
    closeAttempted: 0, closeFulfilled: 0,
    writeAttempted: 0,
  };
  const safeErrorClass = (error) => {
    const name = typeof error?.name === "string" ? error.name : "Error";
    return /^[A-Za-z][A-Za-z0-9_]{0,63}$/.test(name) ? name : "Error";
  };
  const requireSafeCount = (value) => {
    if (!Number.isSafeInteger(value) || value < 0 || value > 1000000) {
      throw new Error("OuterLocatorUnsafeCountError");
    }
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
    "routeContinuous",
  ];
  const postIntegerKeys = [
    "bodyCount", "allAnchorCount", "roleApiTokensLinkCount",
    "rawApiTokensHrefCandidateCount", "rawRelativeProfileApiTokensHrefCandidateCount",
    "rawRelativeAccountApiTokensHrefCandidateCount", "roleApiTokensButtonCount",
    "manageAccountTextCount", "myProfileTextCount", "profileTextCount",
    "busyCount",
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
  let postUrlValidated = false;
  let routeContinuous = false;
  let postSnapshotValidated = false;
  let postSnapshotComplete = false;
  let preSnapshot = null;
  let postSnapshot = null;
  let cleanupState = "NO_TAB_CREATED";
  let residueConverged = true;
  let errorClass = "NONE";
  let postStage = "NOT_STARTED";
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
      typeof secureConsoleZoneV32Consumed === "boolean" &&
      typeof secureConsoleZoneV33Consumed === "boolean";
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
      secureConsoleZoneV32Consumed === true &&
      secureConsoleZoneV32RetainedTab === null &&
      secureConsoleZoneV32State === "V32_DIAGNOSTIC_FAILED_CLEAN" &&
      secureConsoleZoneV33RetainedTab === null &&
      secureConsoleZoneV33State === "UNCREATED";
    if (!predecessorExact) throw new Error("ZoneRoutePreconditionError");

    counters.newAttempted++;
    secureConsoleZoneV33RetainedTab = tab =
      await secureConsoleChromeV5.tabs.new();
    counters.newFulfilled++;
    createdHandleCaptured = typeof tab === "object" && tab !== null;
    if (!createdHandleCaptured) throw new Error("ZoneRouteHandleError");
    controllerOwnership = secureConsoleZoneV33RetainedTab === tab;
    tabShape =
      controllerOwnership &&
      typeof tab.goto === "function" &&
      typeof tab.url === "function" &&
      typeof tab.close === "function" &&
      typeof tab.playwright?.waitForTimeout === "function" &&
      typeof tab.playwright?.locator === "function" &&
      typeof tab.playwright?.getByRole === "function" &&
      typeof tab.playwright?.getByText === "function";
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
      settledZoneParsed.port === "" &&
      settledZoneParsed.username === "" &&
      settledZoneParsed.password === "" &&
      new RegExp(
        "^/" + accountSegment + "/mysw\\.me(?:/|$)",
      ).test(settledZoneParsed.pathname);
    if (!zoneUrlValidated) throw new Error("ZoneRouteSettledUrlError");

    counters.postSnapshotAttempted++;

    postStage = "BODY_COUNT";
    counters.bodyCountAttempted++;
    const bodyCount = await tab.playwright.locator("body").count();
    counters.bodyCountFulfilled++;
    requireSafeCount(bodyCount);

    postStage = "ALL_ANCHOR_COUNT";
    counters.allAnchorCountAttempted++;
    const allAnchorCount = await tab.playwright.locator("a[href]").count();
    counters.allAnchorCountFulfilled++;
    requireSafeCount(allAnchorCount);

    postStage = "ROLE_API_TOKENS_LINK_COUNT";
    counters.roleApiTokensLinkCountAttempted++;
    const roleApiTokensLinkCount = await tab.playwright.getByRole(
      "link",
      { name: "API Tokens", exact: true },
    ).count();
    counters.roleApiTokensLinkCountFulfilled++;
    requireSafeCount(roleApiTokensLinkCount);

    postStage = "API_TOKENS_HREF_COUNT";
    counters.rawApiTokensHrefCandidateCountAttempted++;
    const rawApiTokensHrefCandidateCount =
      await tab.playwright.locator('a[href*="/api-tokens"]').count();
    counters.rawApiTokensHrefCandidateCountFulfilled++;
    requireSafeCount(rawApiTokensHrefCandidateCount);

    postStage = "PROFILE_API_TOKENS_HREF_COUNT";
    counters.rawRelativeProfileApiTokensHrefCandidateCountAttempted++;
    const rawRelativeProfileApiTokensHrefCandidateCount = await tab.playwright.locator(
      'a[href="/profile/api-tokens"], a[href="/profile/api-tokens/"]',
    ).count();
    counters.rawRelativeProfileApiTokensHrefCandidateCountFulfilled++;
    requireSafeCount(rawRelativeProfileApiTokensHrefCandidateCount);

    postStage = "ACCOUNT_API_TOKENS_HREF_COUNT";
    counters.rawRelativeAccountApiTokensHrefCandidateCountAttempted++;
    const rawRelativeAccountApiTokensHrefCandidateCount = await tab.playwright.locator(
      'a[href^="/' + accountSegment + '/"][href*="/api-tokens"]',
    ).count();
    counters.rawRelativeAccountApiTokensHrefCandidateCountFulfilled++;
    requireSafeCount(rawRelativeAccountApiTokensHrefCandidateCount);

    postStage = "ROLE_API_TOKENS_BUTTON_COUNT";
    counters.roleApiTokensButtonCountAttempted++;
    const roleApiTokensButtonCount = await tab.playwright.getByRole(
      "button",
      { name: "API Tokens", exact: true },
    ).count();
    counters.roleApiTokensButtonCountFulfilled++;
    requireSafeCount(roleApiTokensButtonCount);

    postStage = "MANAGE_ACCOUNT_TEXT_COUNT";
    counters.manageAccountTextCountAttempted++;
    const manageAccountTextCount = await tab.playwright.getByText(
      "Manage Account",
      { exact: true },
    ).count();
    counters.manageAccountTextCountFulfilled++;
    requireSafeCount(manageAccountTextCount);

    postStage = "MY_PROFILE_TEXT_COUNT";
    counters.myProfileTextCountAttempted++;
    const myProfileTextCount =
      await tab.playwright.getByText("My Profile", { exact: true }).count();
    counters.myProfileTextCountFulfilled++;
    requireSafeCount(myProfileTextCount);

    postStage = "PROFILE_TEXT_COUNT";
    counters.profileTextCountAttempted++;
    const profileTextCount =
      await tab.playwright.getByText("Profile", { exact: true }).count();
    counters.profileTextCountFulfilled++;
    requireSafeCount(profileTextCount);

    postStage = "BUSY_COUNT";
    counters.busyCountAttempted++;
    const busyCount = await tab.playwright.locator(
      '[aria-busy="true"], [role="progressbar"]',
    ).count();
    counters.busyCountFulfilled++;
    requireSafeCount(busyCount);
    postStage = "POST_URL";
    counters.postUrlAttempted++;
    const postProbeUrl = await tab.url();
    counters.postUrlFulfilled++;
    let postProbeParsed = null;
    try {
      postProbeParsed = new URL(postProbeUrl);
    } catch {}
    postUrlValidated =
      postProbeParsed !== null &&
      postProbeParsed.protocol === "https:" &&
      postProbeParsed.hostname === "dash.cloudflare.com" &&
      postProbeParsed.port === "" &&
      postProbeParsed.username === "" &&
      postProbeParsed.password === "" &&
      new RegExp(
        "^/" + accountSegment + "/mysw\\.me(?:/|$)",
      ).test(postProbeParsed.pathname);
    routeContinuous =
      postUrlValidated === true &&
      postProbeUrl === settledZoneUrl;
    if (!postUrlValidated || !routeContinuous) {
      throw new Error("ZoneRoutePostProbeUrlError");
    }
    counters.postSnapshotFulfilled++;

    postStage = "PROJECT_RESULT";
    postSnapshot = trustedRecord(
      {
        hostExact: postProbeParsed.protocol === "https:" &&
          postProbeParsed.hostname === "dash.cloudflare.com",
        zonePathExact: new RegExp(
          "^/" + accountSegment + "/mysw\\.me/?$",
        ).test(postProbeParsed.pathname),
        zonePathPrefix: new RegExp(
          "^/" + accountSegment + "/mysw\\.me(?:/|$)",
        ).test(postProbeParsed.pathname),
        accountHomePath: new RegExp(
          "^/" + accountSegment + "/home/?$",
        ).test(postProbeParsed.pathname),
        routeContinuous,
        bodyCount,
        allAnchorCount,
        roleApiTokensLinkCount,
        rawApiTokensHrefCandidateCount,
        rawRelativeProfileApiTokensHrefCandidateCount,
        rawRelativeAccountApiTokensHrefCandidateCount,
        roleApiTokensButtonCount,
        manageAccountTextCount,
        myProfileTextCount,
        profileTextCount,
        busyCount,
      },
      postBooleanKeys,
      postIntegerKeys,
    );
    postSnapshotValidated = postSnapshot !== null;
    postSnapshotComplete =
      postSnapshotValidated &&
      postUrlValidated === true &&
      routeContinuous === true &&
      postSnapshot.hostExact === true &&
      postSnapshot.zonePathPrefix === true &&
      postSnapshot.accountHomePath === false &&
      postSnapshot.routeContinuous === true &&
      postSnapshot.bodyCount === 1 &&
      postSnapshot.allAnchorCount > 0 &&
      postSnapshot.busyCount === 0;
    if (!postSnapshotComplete) {
      throw new Error("ZoneRouteOuterLocatorSnapshotError");
    }
    postStage = "COMPLETE";
    result = "EXACT_V33_ZONE_ROUTE_OUTER_LOCATOR_SIGNATURE_PASS";
  } catch (error) {
    errorClass = safeErrorClass(error);
  }

  if (tab !== null && tab !== undefined && typeof tab.close === "function") {
    counters.closeAttempted++;
    try {
      await tab.close();
      counters.closeFulfilled++;
      secureConsoleZoneV33RetainedTab = null;
      secureConsoleZoneV33State =
        result === "EXACT_V33_ZONE_ROUTE_OUTER_LOCATOR_SIGNATURE_PASS"
          ? "V33_DIAGNOSTIC_PASS_CLEAN"
          : "V33_DIAGNOSTIC_FAILED_CLEAN";
      cleanupState = "EXACT_TAB_CLOSED";
      residueConverged = true;
    } catch (closeError) {
      if (errorClass === "NONE") errorClass = safeErrorClass(closeError);
      secureConsoleZoneV33RetainedTab = tab;
      secureConsoleZoneV33State = "V33_DIAGNOSTIC_FAILED_TAB_RETAINED";
      cleanupState = "EXACT_TAB_CLOSE_REJECTED";
      residueConverged = false;
      result = "PRECONDITION_FAIL";
    }
  } else if (counters.newAttempted === 0) {
    secureConsoleZoneV33State = "V33_DIAGNOSTIC_FAILED_CLEAN";
    cleanupState = "NO_TAB_CREATED";
  } else {
    secureConsoleZoneV33State = "V33_DIAGNOSTIC_FAILED_RESIDUE_UNPROVEN";
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
    postUrlValidated,
    routeContinuous,
    postSnapshotValidated,
    postSnapshotComplete,
    postStage,
    preSnapshot,
    postSnapshot,
    cleanupState,
    residueConverged,
    retainedExactHandle: secureConsoleZoneV33RetainedTab !== null,
    state: secureConsoleZoneV33State,
    consumed: secureConsoleZoneV33Consumed,
    ...counters,
    errorClass,
  });
})();
~~~

## Pre-execution gates

Before any V33 Node call:

- commit this exact brief alone and record its bytes, SHA-256, blob, and
  normalized executable bytes/SHA-256;
- obtain an independent `gpt-5.6-sol` High review with zero unresolved
  Critical, HIGH, or IMPORTANT findings;
- commit a non-self-referential classification whose direct parent is that
  PASS review and record the post-commit coordinator tuple;
- freshly revalidate projection, empty index, exact 12-path dirty product
  baseline, runtime hashes, clean evidence worktree, zero temporary/process
  residue, VM1205 safe checkpoint, absent public DNS, persistent controller,
  exact V32 failed-clean predecessor, and absent V33 declarations; and
- extract the executable from the committed brief and require its exact
  reviewed normalized bytes and SHA-256 before the sole Node call.

The first Node call receiving the executable consumes V33 before any
precondition. PASS_CLEAN requires the fixed PASS result, every validation and
completeness boolean true, `postStage=COMPLETE`, every declared non-cleanup
attempted/fulfilled pair `1/1`, close `1/1`, `EXACT_TAB_CLOSED`, residue
convergence, no retained handle, state `V33_DIAGNOSTIC_PASS_CLEAN`, consumed
true, and error class `NONE`.

Anything else is failed, uncertain, or residue-bearing. Close only the exact
created handle when possible, record fixed sanitized evidence, classify V33
spent, and stop. Never retry or continue V33.

## Evidence interpretation

A clean V33 PASS proves only endpoint-bracketed route continuity and the fixed
outer locator counts. The three raw href-attribute candidate counts are not
same-origin pathname validation and must never be used as destination proof.
A positive candidate may support only a separately reviewed successor that
privately reads and validates one exact destination before navigation. A zero
candidate with a positive accessible account/profile signature may support a
separately reviewed exact activation diagnostic. Any incomplete probe, unsafe
count, or route mismatch stops at its originating fixed stage. V33 itself never
activates or mutates anything.
