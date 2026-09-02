# OmniRoute V41 fresh-session rank-zero-only selected-tab reacquisition — review brief

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`
## Purpose and boundary

Replace consumed V40 with the smallest ordered-selected-tab gate that does not
let irrelevant later-record value drift veto the owner-selected rank-zero tab.
V38 proved the foreign-realm array contract; V39 proved a complete 10-record
listing; V40 later failed full-list validation before classification and stopped
with zero claim. V3, V4-live, V34 Call 2, and V35-V40 remain consumed/static and
may never be retried, continued, reinterpreted, or inherited.

V41 preserves V40 exactly except for the listing projection. It still validates
the canonical array envelope, bounded own length, exact own numeric names, zero
symbols, and every numeric index as an enumerable own data descriptor. It then
inspects only index zero: the record must be plain and symbol-free, use only the
fixed key set, contain required ID and URL as enumerable own data descriptors,
and contain only bounded nonempty control-free strings. The rank-zero URL must
parse to exact HTTPS `dash.cloudflare.com` with no port, username, or password.
Later record values are never read, iterated, emitted, filtered, or used.

This is justified solely by the documented last-opened/focused ordering and the
owner's exact selected-tab/no-other-profile-window confirmation. Any rank-zero
or array-envelope mismatch stops before claim. Post-claim controller identity,
account-home URL, exact one-zone-anchor page signature, counters, fixed error,
success binding retention, failure/terminal cleanup, and no-retry semantics are
unchanged. No metadata, raw error, secret, or credential is emitted, and no
provider or infrastructure mutation occurs.

## One-shot executable

Extract from committed bytes, LF-normalize, byte/hash/syntax check, and send
exactly once without wrapper.

~~~javascript
let secureConsoleSetupBrowserRuntimeV41 = null;
let secureConsoleAgentV41 = null;
let secureConsoleChromeV41 = null;
let secureConsoleOwnedTaskTabV41 = null;
let secureConsoleOwnedTaskTabV41Eligible = false;
let secureConsoleV41Consumed = false;
let secureConsoleV41State = "UNCREATED";
await (async () => {
  const gateWasFresh = secureConsoleV41Consumed === false;
  secureConsoleV41Consumed = true;
  const counters = {
    importAttempted: 0, importFulfilled: 0,
    setupAttempted: 0, setupFulfilled: 0,
    connectAttempted: 0, connectFulfilled: 0,
    documentationAttempted: 0, documentationFulfilled: 0,
    documentationWriteAttempted: 0, documentationWriteFulfilled: 0,
    nameAttempted: 0, nameFulfilled: 0,
    openTabsAttempted: 0, openTabsFulfilled: 0,
    claimAttempted: 0, claimFulfilled: 0,
    navigationAttempted: 0, navigationFulfilled: 0,
    waitAttempted: 0, waitFulfilled: 0,
    urlAttempted: 0, urlFulfilled: 0,
    snapshotAttempted: 0, snapshotFulfilled: 0,
    writeAttempted: 0,
  };
  let result = "V41_FRESH_CROSS_REALM_TASK_REACQUISITION_FAILED_STOP";
  let declarationShape = false;
  let moduleShape = false;
  let agentShape = false;
  let connectedShape = false;
  let documentationValidated = false;
  let documentationLength = -1;
  let sessionNamed = false;
  let offeredCount = -1;
  let listingValidated = false;
  let rankZeroSelected = false;
  let candidateValidated = false;
  let candidateUrlCloudflare = false;
  let controllerOwnership = false;
  let tabShape = false;
  let homeUrlValidated = false;
  let snapshotValidated = false;
  let semanticComplete = false;
  let continuationBindingsRetained = false;
  let failureCleanupComplete = false;
  let snapshot = null;
  let adopted = null;
  let errorClass = "NONE";
  // BEGIN_V41_PURE_TRUSTED_LISTING
  const plainRecord = (value) => {
    if (typeof value !== "object" || value === null) return false;
    const prototype = Object.getPrototypeOf(value);
    return prototype === null ||
      (prototype !== null && Object.getPrototypeOf(prototype) === null);
  };
  const trustedListing = (value) => {
    if (!Array.isArray(value) ||
        Object.getOwnPropertySymbols(value).length !== 0) return null;
    const lengthDescriptor = Object.getOwnPropertyDescriptor(value, "length");
    if (!lengthDescriptor ||
        !Object.prototype.hasOwnProperty.call(lengthDescriptor, "value") ||
        lengthDescriptor.enumerable !== false ||
        !Number.isSafeInteger(lengthDescriptor.value) ||
        lengthDescriptor.value < 1 || lengthDescriptor.value > 1000) return null;
    const length = lengthDescriptor.value;
    const arrayNames = Object.getOwnPropertyNames(value);
    if (arrayNames.length !== length + 1 ||
        !arrayNames.includes("length")) return null;
    const expectedNames = new Set(["length"]);
    for (let index = 0; index < length; index++) {
      expectedNames.add(String(index));
    }
    if (arrayNames.some((name) => !expectedNames.has(name))) return null;
    const indexDescriptors = [];
    for (let index = 0; index < length; index++) {
      const descriptor =
        Object.getOwnPropertyDescriptor(value, String(index));
      if (!descriptor ||
          !Object.prototype.hasOwnProperty.call(descriptor, "value") ||
          descriptor.enumerable !== true) return null;
      indexDescriptors.push(descriptor);
    }
    if (indexDescriptors.length !== length) return null;
    const first = indexDescriptors[0].value;
    if (!plainRecord(first) ||
        Object.getOwnPropertySymbols(first).length !== 0) return null;
    const allowed = new Set([
      "id", "lastOpened", "providerTabId", "tabGroup", "title", "url",
    ]);
    const keys = Object.getOwnPropertyNames(first);
    if (!keys.includes("id") || keys.some((key) => !allowed.has(key))) {
      return null;
    }
    let validatedId = null;
    let validatedUrl = null;
    for (const key of keys) {
      const descriptor = Object.getOwnPropertyDescriptor(first, key);
      if (!descriptor ||
          !Object.prototype.hasOwnProperty.call(descriptor, "value") ||
          descriptor.enumerable !== true) return null;
      const limit = key === "url" ? 16384 : key === "title" ? 4096 : 512;
      if (typeof descriptor.value !== "string" ||
          descriptor.value.length === 0 ||
          descriptor.value.length > limit ||
          /[\u0000-\u001f\u007f]/.test(descriptor.value)) return null;
      if (key === "id") validatedId = descriptor.value;
      if (key === "url") validatedUrl = descriptor.value;
    }
    if (validatedId === null || validatedUrl === null) return null;
    let parsed = null;
    try {
      parsed = new URL(validatedUrl);
    } catch {
      return null;
    }
    const urlCloudflare =
      parsed.protocol === "https:" &&
      parsed.hostname === "dash.cloudflare.com" &&
      parsed.port === "" && parsed.username === "" && parsed.password === "";
    return urlCloudflare ? {
      id: validatedId,
      count: length,
      urlCloudflare,
    } : null;
  };
  // END_V41_PURE_TRUSTED_LISTING
  const trustedSnapshot = (value) => {
    if (!plainRecord(value)) return null;
    const expected = [
      "accountHomePath", "allAnchorCount", "busyCount",
      "exactZoneHrefCount", "hostExact",
    ];
    const keys = Object.keys(value).sort();
    if (keys.length !== expected.length ||
        keys.some((key, index) => key !== expected[index])) return null;
    if (typeof value.hostExact !== "boolean" ||
        typeof value.accountHomePath !== "boolean") return null;
    for (const key of ["exactZoneHrefCount", "allAnchorCount", "busyCount"]) {
      if (!Number.isSafeInteger(value[key]) || value[key] < 0 ||
          value[key] > 1000000) return null;
    }
    return {
      hostExact: value.hostExact,
      accountHomePath: value.accountHomePath,
      exactZoneHrefCount: value.exactZoneHrefCount,
      allAnchorCount: value.allAnchorCount,
      busyCount: value.busyCount,
    };
  };
  try {
    declarationShape =
      gateWasFresh === true &&
      typeof secureConsoleV35AttachmentConsumed === "undefined" &&
      typeof secureConsoleV35AdoptionConsumed === "undefined" &&
      typeof secureConsoleV36Consumed === "undefined" &&
      typeof secureConsoleV37Consumed === "undefined" &&
      typeof secureConsoleV38Consumed === "undefined" &&
      typeof secureConsoleOwnedTaskTabV38 === "undefined" &&
      typeof secureConsoleV39Consumed === "undefined" &&
      typeof secureConsoleOwnedTaskTabV39 === "undefined" &&
      typeof secureConsoleV40Consumed === "undefined" &&
      typeof secureConsoleOwnedTaskTabV40 === "undefined" &&
      secureConsoleSetupBrowserRuntimeV41 === null &&
      secureConsoleAgentV41 === null && secureConsoleChromeV41 === null &&
      secureConsoleOwnedTaskTabV41 === null &&
      secureConsoleOwnedTaskTabV41Eligible === false &&
      secureConsoleV41State === "UNCREATED";
    if (!declarationShape) throw new Error("FreshRealmDeclarationError");
    secureConsoleV41State = "V41_CONSUMING";

    counters.importAttempted++;
    const imported = await import(
      "file:///C:/Users/chatc/.codex/plugins/cache/openai-bundled/chrome/26.831.20005/scripts/browser-client.mjs"
    );
    counters.importFulfilled++;
    moduleShape = typeof imported === "object" && imported !== null &&
      typeof imported.setupBrowserRuntime === "function";
    if (!moduleShape) throw new Error("FreshRuntimeModuleShapeError");
    secureConsoleSetupBrowserRuntimeV41 = imported.setupBrowserRuntime;

    counters.setupAttempted++;
    secureConsoleAgentV41 = await secureConsoleSetupBrowserRuntimeV41();
    counters.setupFulfilled++;
    agentShape = typeof secureConsoleAgentV41 === "object" &&
      secureConsoleAgentV41 !== null &&
      typeof secureConsoleAgentV41.browsers?.get === "function";
    if (!agentShape) throw new Error("FreshRuntimeAgentShapeError");

    counters.connectAttempted++;
    secureConsoleChromeV41 =
      await secureConsoleAgentV41.browsers.get("chrome");
    counters.connectFulfilled++;
    connectedShape = typeof secureConsoleChromeV41 === "object" &&
      secureConsoleChromeV41 !== null &&
      typeof secureConsoleChromeV41.documentation === "function" &&
      typeof secureConsoleChromeV41.nameSession === "function" &&
      typeof secureConsoleChromeV41.user?.openTabs === "function" &&
      typeof secureConsoleChromeV41.user?.claimTab === "function";
    if (!connectedShape) throw new Error("FreshChromeShapeError");

    counters.documentationAttempted++;
    const documentation = await secureConsoleChromeV41.documentation();
    counters.documentationFulfilled++;
    documentationValidated =
      typeof documentation === "string" &&
      documentation.length >= 40000 && documentation.length <= 50000 &&
      documentation.includes("openTabs(): Promise<Array<BrowserUserTabInfo>>") &&
      documentation.includes(
        "claimTab(tab: string | BrowserUserTabInfo): Promise<Tab>",
      ) &&
      documentation.includes("id: string") &&
      documentation.includes("lastOpened?: string") &&
      documentation.includes("providerTabId?: string") &&
      documentation.includes("tabGroup?: string") &&
      documentation.includes("title?: string") &&
      documentation.includes("url?: string");
    documentationLength = documentationValidated ? documentation.length : -1;
    if (!documentationValidated) {
      throw new Error("CompleteDocumentationValidationError");
    }
    counters.documentationWriteAttempted++;
    await nodeRepl.write(documentation);
    counters.documentationWriteFulfilled++;

    counters.nameAttempted++;
    await secureConsoleChromeV41.nameSession("🔐 OmniRoute secure console");
    counters.nameFulfilled++;
    sessionNamed = true;

    counters.openTabsAttempted++;
    const offered = await secureConsoleChromeV41.user.openTabs();
    counters.openTabsFulfilled++;
    const candidate = trustedListing(offered);
    listingValidated = candidate !== null;
    offeredCount = listingValidated ? candidate.count : -1;
    rankZeroSelected = listingValidated;
    candidateValidated = listingValidated;
    candidateUrlCloudflare = listingValidated && candidate.urlCloudflare;
    if (!candidateValidated) throw new Error("OrderedTaskTabShapeError");

    counters.claimAttempted++;
    adopted = await secureConsoleChromeV41.user.claimTab(candidate.id);
    counters.claimFulfilled++;
    controllerOwnership = typeof adopted === "object" && adopted !== null &&
      typeof adopted.id === "string" && adopted.id === candidate.id &&
      adopted.id.length > 0 && adopted.id.length <= 512 &&
      !/[\u0000-\u001f\u007f]/.test(adopted.id);
    tabShape = controllerOwnership && typeof adopted.goto === "function" &&
      typeof adopted.url === "function" &&
      typeof adopted.playwright?.waitForTimeout === "function" &&
      typeof adopted.playwright?.locator === "function";
    if (!tabShape) throw new Error("ClaimedTabOwnershipError");

    counters.navigationAttempted++;
    await adopted.goto("https://dash.cloudflare.com/");
    counters.navigationFulfilled++;
    counters.waitAttempted++;
    await adopted.playwright.waitForTimeout(20000);
    counters.waitFulfilled++;
    counters.urlAttempted++;
    const homeUrl = await adopted.url();
    counters.urlFulfilled++;
    const homeMatch =
      /^https:\/\/dash\.cloudflare\.com\/([0-9a-f]{32})\/home\/?$/.exec(
        homeUrl,
      );
    homeUrlValidated = homeMatch !== null;
    if (!homeUrlValidated) throw new Error("AccountHomeUrlError");
    const accountSegment = homeMatch[1];

    counters.snapshotAttempted++;
    const untrusted = await adopted.playwright.locator("body").evaluate(
      (body, segment) => {
        const anchors = [...body.querySelectorAll("a[href]")];
        const exactZoneHrefCount = anchors.filter((item) => {
          try {
            const url = new URL(item.getAttribute("href") || "", location.href);
            return url.protocol === "https:" &&
              url.hostname === "dash.cloudflare.com" &&
              url.port === "" && url.username === "" && url.password === "" &&
              new RegExp("^/" + segment + "/mysw\\.me/?$").test(url.pathname);
          } catch {
            return false;
          }
        }).length;
        return {
          hostExact: location.protocol === "https:" &&
            location.hostname === "dash.cloudflare.com" &&
            location.port === "",
          accountHomePath:
            new RegExp("^/" + segment + "/home/?$").test(location.pathname),
          exactZoneHrefCount,
          allAnchorCount: anchors.length,
          busyCount: body.querySelectorAll(
            '[aria-busy="true"], [role="progressbar"]',
          ).length,
        };
      },
      accountSegment,
    );
    counters.snapshotFulfilled++;
    snapshot = trustedSnapshot(untrusted);
    snapshotValidated = snapshot !== null;
    semanticComplete = snapshotValidated && snapshot.hostExact === true &&
      snapshot.accountHomePath === true && snapshot.exactZoneHrefCount === 1 &&
      snapshot.allAnchorCount > 0 && snapshot.busyCount === 0;
    if (!semanticComplete) {
      throw new Error("AccountHomeSemanticSignatureError");
    }

    const exactCounters =
      counters.importAttempted === 1 && counters.importFulfilled === 1 &&
      counters.setupAttempted === 1 && counters.setupFulfilled === 1 &&
      counters.connectAttempted === 1 && counters.connectFulfilled === 1 &&
      counters.documentationAttempted === 1 &&
      counters.documentationFulfilled === 1 &&
      counters.documentationWriteAttempted === 1 &&
      counters.documentationWriteFulfilled === 1 &&
      counters.nameAttempted === 1 && counters.nameFulfilled === 1 &&
      counters.openTabsAttempted === 1 && counters.openTabsFulfilled === 1 &&
      counters.claimAttempted === 1 && counters.claimFulfilled === 1 &&
      counters.navigationAttempted === 1 &&
      counters.navigationFulfilled === 1 && counters.waitAttempted === 1 &&
      counters.waitFulfilled === 1 && counters.urlAttempted === 1 &&
      counters.urlFulfilled === 1 && counters.snapshotAttempted === 1 &&
      counters.snapshotFulfilled === 1;
    if (!exactCounters) throw new Error("V41CompletenessError");
    result = "EXACT_V41_CROSS_REALM_TASK_TAB_ACCOUNT_HOME_REACQUISITION_PASS";
  } catch {
    errorClass = "Error";
  }

  if (result ===
      "EXACT_V41_CROSS_REALM_TASK_TAB_ACCOUNT_HOME_REACQUISITION_PASS") {
    secureConsoleOwnedTaskTabV41 = adopted;
    secureConsoleOwnedTaskTabV41Eligible = true;
    secureConsoleV41State = "V41_ACCOUNT_HOME_READY_ELIGIBLE";
    continuationBindingsRetained =
      typeof secureConsoleSetupBrowserRuntimeV41 === "function" &&
      secureConsoleAgentV41 !== null && secureConsoleChromeV41 !== null &&
      secureConsoleOwnedTaskTabV41 !== null;
  } else {
    secureConsoleOwnedTaskTabV41 = null;
    secureConsoleOwnedTaskTabV41Eligible = false;
    secureConsoleV41State = "V41_REACQUISITION_OR_READINESS_FAILED";
    secureConsoleChromeV41 = null;
    secureConsoleAgentV41 = null;
    secureConsoleSetupBrowserRuntimeV41 = null;
    failureCleanupComplete =
      secureConsoleSetupBrowserRuntimeV41 === null &&
      secureConsoleAgentV41 === null && secureConsoleChromeV41 === null &&
      secureConsoleOwnedTaskTabV41 === null &&
      secureConsoleOwnedTaskTabV41Eligible === false;
  }
  counters.writeAttempted++;
  try {
    await nodeRepl.write({
      result,
      declarationShape,
      moduleShape,
      agentShape,
      connectedShape,
      documentationValidated,
      documentationLength,
      sessionNamed,
      offeredCount,
      listingValidated,
      rankZeroSelected,
      candidateValidated,
      candidateUrlCloudflare,
      controllerOwnership,
      tabShape,
      homeUrlValidated,
      snapshotValidated,
      semanticComplete,
      continuationBindingsRetained,
      failureCleanupComplete,
      snapshot,
      ...counters,
      errorClass,
      consumed: secureConsoleV41Consumed,
      bindingEligible: secureConsoleOwnedTaskTabV41Eligible,
      bindingNull: secureConsoleOwnedTaskTabV41 === null,
      state: secureConsoleV41State,
    });
  } catch (terminalError) {
    secureConsoleOwnedTaskTabV41 = null;
    secureConsoleOwnedTaskTabV41Eligible = false;
    secureConsoleV41State = "V41_FINAL_OUTPUT_FAILED_STOP";
    secureConsoleChromeV41 = null;
    secureConsoleAgentV41 = null;
    secureConsoleSetupBrowserRuntimeV41 = null;
    throw terminalError;
  }
})();
~~~

## Review and action-time requirements

A committed pure fixture must prove exact foreign-realm rank-zero success,
array-envelope rejection, first-record accessor rejection with zero getter
calls, later hostile-record non-observation with zero getter calls, exact
Cloudflare-origin selection, full-cell success, fixed hostile failure output,
success binding retention, and failure cleanup without real Chrome.

Independent Sol High review must report all severity counts zero. Before live
use require a non-self-referential classification and post-commit tuple; exact
package hashes; stable 10,661-record projection; empty index; exact 12-path
baseline; runtime/docs, evidence-worktree, residue, DNS, VM, archived-owner,
sole-owner, exact Chrome-selection, and fresh declaration-free V35-V41 pins.

Success authorizes no provider mutation or secret action. All V4 page-signature,
completeness, no-residue, no-retry, secret, confirmation, and cleanup constraints
remain binding. The final Create/native Copy/native masked Paste confirmation
and later separate exact-row deletion confirmation remain mandatory external
gates and cannot be pre-approved, automated, delegated, or waived.

`authorizes_live_execution=false`
