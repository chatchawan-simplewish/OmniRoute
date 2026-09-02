# OmniRoute V40 fresh-session ordered selected-tab reacquisition — review brief

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`
## Purpose

Replace consumed V39 with the smallest fresh-session one-shot using the already
reviewed ordered-selected-tab design, corrected for the exact foreign-realm
listing proven by V38. The user externally confirmed the intended task tab is
selected and no other Chrome profile/window is offered. The documented
`openTabs` ordering places the last-opened/focused tab at rank zero.

## Consumed predecessor and design boundary

V3 is consumed and failed; V4 is static evidence only; V34 Call 2 and V35-V39
are consumed and may never be retried, continued, reinterpreted, or inherited.
V39 proved the complete listing contract with `offeredCount=10` but zero URLs
matching its overly narrow zone-path predicate, and stopped before claim.

V40 preserves every V39 descriptor, record, string, error-privacy, claim,
account-home URL, exact zone-anchor, busy-state, completeness, success-binding,
failure-cleanup, terminal-cleanup, and no-retry rule. The sole selector delta is
that the fully validated rank-zero record must have a nonempty safe URL whose
parsed origin is exactly HTTPS `dash.cloudflare.com`, with no port, username,
or password. It does not require a current zone path. If rank zero is absent,
malformed, non-Cloudflare, or the listing contract fails, V40 stops before
claim. After claim it still navigates to Cloudflare account home and proves the
unchanged exact `mysw.me` semantic signature before retaining an eligible
binding.

The cell emits no ID, URL, title, provider ID, group, timestamp, raw listing,
descriptor, prototype, thrown value, secret, or credential. It performs no
provider, clipboard, credential, DNS, routing, VM, listener, proxy, or owner
action. The unbound catch emits only literal `Error`. Success retains the
claimed tab only for a later separately reviewed step in the same realm;
failure clears every binding. Timeout or uncertainty consumes V40 and requires
realm disposal with no retry.

## One-shot executable

The following is the sole live cell and must be extracted from committed bytes,
LF-normalized, byte/hash/syntax checked, and sent exactly once without wrapper.

~~~javascript
let secureConsoleSetupBrowserRuntimeV40 = null;
let secureConsoleAgentV40 = null;
let secureConsoleChromeV40 = null;
let secureConsoleOwnedTaskTabV40 = null;
let secureConsoleOwnedTaskTabV40Eligible = false;
let secureConsoleV40Consumed = false;
let secureConsoleV40State = "UNCREATED";
await (async () => {
  const gateWasFresh = secureConsoleV40Consumed === false;
  secureConsoleV40Consumed = true;
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
  let result = "V40_FRESH_CROSS_REALM_TASK_REACQUISITION_FAILED_STOP";
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
  // BEGIN_V40_PURE_TRUSTED_LISTING
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
    const allowed = new Set([
      "id", "lastOpened", "providerTabId", "tabGroup", "title", "url",
    ]);
    const projected = [];
    for (let index = 0; index < length; index++) {
      const indexDescriptor =
        Object.getOwnPropertyDescriptor(value, String(index));
      if (!indexDescriptor ||
          !Object.prototype.hasOwnProperty.call(indexDescriptor, "value") ||
          indexDescriptor.enumerable !== true) return null;
      const item = indexDescriptor.value;
      if (!plainRecord(item) ||
          Object.getOwnPropertySymbols(item).length !== 0) return null;
      const keys = Object.getOwnPropertyNames(item);
      if (!keys.includes("id") || keys.some((key) => !allowed.has(key))) {
        return null;
      }
      let validatedId = null;
      let validatedUrl = null;
      for (const key of keys) {
        const descriptor = Object.getOwnPropertyDescriptor(item, key);
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
      if (validatedId === null) return null;
      projected.push({ id: validatedId, url: validatedUrl });
    }
    if (projected.length !== length) return null;
    const first = projected[0];
    if (first.url === null) return null;
    let parsed = null;
    try {
      parsed = new URL(first.url);
    } catch {
      return null;
    }
    const urlCloudflare =
      parsed.protocol === "https:" &&
      parsed.hostname === "dash.cloudflare.com" &&
      parsed.port === "" && parsed.username === "" && parsed.password === "";
    return urlCloudflare ? {
      id: first.id,
      count: length,
      urlCloudflare,
    } : null;
  };
  // END_V40_PURE_TRUSTED_LISTING
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
      secureConsoleSetupBrowserRuntimeV40 === null &&
      secureConsoleAgentV40 === null && secureConsoleChromeV40 === null &&
      secureConsoleOwnedTaskTabV40 === null &&
      secureConsoleOwnedTaskTabV40Eligible === false &&
      secureConsoleV40State === "UNCREATED";
    if (!declarationShape) throw new Error("FreshRealmDeclarationError");
    secureConsoleV40State = "V40_CONSUMING";

    counters.importAttempted++;
    const imported = await import(
      "file:///C:/Users/chatc/.codex/plugins/cache/openai-bundled/chrome/26.831.20005/scripts/browser-client.mjs"
    );
    counters.importFulfilled++;
    moduleShape = typeof imported === "object" && imported !== null &&
      typeof imported.setupBrowserRuntime === "function";
    if (!moduleShape) throw new Error("FreshRuntimeModuleShapeError");
    secureConsoleSetupBrowserRuntimeV40 = imported.setupBrowserRuntime;

    counters.setupAttempted++;
    secureConsoleAgentV40 = await secureConsoleSetupBrowserRuntimeV40();
    counters.setupFulfilled++;
    agentShape = typeof secureConsoleAgentV40 === "object" &&
      secureConsoleAgentV40 !== null &&
      typeof secureConsoleAgentV40.browsers?.get === "function";
    if (!agentShape) throw new Error("FreshRuntimeAgentShapeError");

    counters.connectAttempted++;
    secureConsoleChromeV40 =
      await secureConsoleAgentV40.browsers.get("chrome");
    counters.connectFulfilled++;
    connectedShape = typeof secureConsoleChromeV40 === "object" &&
      secureConsoleChromeV40 !== null &&
      typeof secureConsoleChromeV40.documentation === "function" &&
      typeof secureConsoleChromeV40.nameSession === "function" &&
      typeof secureConsoleChromeV40.user?.openTabs === "function" &&
      typeof secureConsoleChromeV40.user?.claimTab === "function";
    if (!connectedShape) throw new Error("FreshChromeShapeError");

    counters.documentationAttempted++;
    const documentation = await secureConsoleChromeV40.documentation();
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
    await secureConsoleChromeV40.nameSession("🔐 OmniRoute secure console");
    counters.nameFulfilled++;
    sessionNamed = true;

    counters.openTabsAttempted++;
    const offered = await secureConsoleChromeV40.user.openTabs();
    counters.openTabsFulfilled++;
    const candidate = trustedListing(offered);
    listingValidated = candidate !== null;
    offeredCount = listingValidated ? candidate.count : -1;
    rankZeroSelected = listingValidated;
    candidateValidated = listingValidated;
    candidateUrlCloudflare = listingValidated && candidate.urlCloudflare;
    if (!candidateValidated) throw new Error("OrderedTaskTabShapeError");

    counters.claimAttempted++;
    adopted = await secureConsoleChromeV40.user.claimTab(candidate.id);
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
    if (!exactCounters) throw new Error("V40CompletenessError");
    result = "EXACT_V40_CROSS_REALM_TASK_TAB_ACCOUNT_HOME_REACQUISITION_PASS";
  } catch {
    errorClass = "Error";
  }

  if (result ===
      "EXACT_V40_CROSS_REALM_TASK_TAB_ACCOUNT_HOME_REACQUISITION_PASS") {
    secureConsoleOwnedTaskTabV40 = adopted;
    secureConsoleOwnedTaskTabV40Eligible = true;
    secureConsoleV40State = "V40_ACCOUNT_HOME_READY_ELIGIBLE";
    continuationBindingsRetained =
      typeof secureConsoleSetupBrowserRuntimeV40 === "function" &&
      secureConsoleAgentV40 !== null && secureConsoleChromeV40 !== null &&
      secureConsoleOwnedTaskTabV40 !== null;
  } else {
    secureConsoleOwnedTaskTabV40 = null;
    secureConsoleOwnedTaskTabV40Eligible = false;
    secureConsoleV40State = "V40_REACQUISITION_OR_READINESS_FAILED";
    secureConsoleChromeV40 = null;
    secureConsoleAgentV40 = null;
    secureConsoleSetupBrowserRuntimeV40 = null;
    failureCleanupComplete =
      secureConsoleSetupBrowserRuntimeV40 === null &&
      secureConsoleAgentV40 === null && secureConsoleChromeV40 === null &&
      secureConsoleOwnedTaskTabV40 === null &&
      secureConsoleOwnedTaskTabV40Eligible === false;
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
      consumed: secureConsoleV40Consumed,
      bindingEligible: secureConsoleOwnedTaskTabV40Eligible,
      bindingNull: secureConsoleOwnedTaskTabV40 === null,
      state: secureConsoleV40State,
    });
  } catch (terminalError) {
    secureConsoleOwnedTaskTabV40 = null;
    secureConsoleOwnedTaskTabV40Eligible = false;
    secureConsoleV40State = "V40_FINAL_OUTPUT_FAILED_STOP";
    secureConsoleChromeV40 = null;
    secureConsoleAgentV40 = null;
    secureConsoleSetupBrowserRuntimeV40 = null;
    throw terminalError;
  }
})();
~~~

## Required offline review and action-time pins

A committed pure fixture must prove syntax and source-site counts; exact
foreign-realm rank-zero acceptance; non-Cloudflare rank-zero rejection; hostile
array/record accessor rejection with zero getter calls; zero/multiple later
Cloudflare records not influencing rank zero; full-cell success; fixed hostile
failure output; success binding retention; and failure cleanup. It must not set
up or touch real Chrome.

Independent Sol High review must report Critical `0`, HIGH `0`, IMPORTANT
`0`, Minor `0`. Before any live send, require a non-self-referential
classification and separate post-commit tuple; exact package hashes/blobs;
stable 10,661-record projection; empty index; exact 12-path product baseline;
runtime/docs pins; clean evidence worktree; zero residue; absent public DNS;
unchanged VM1205 safe checkpoint; archived prior owner; no competing owner; the
exact owner Chrome-selection confirmation; and a newly reset declaration-free
V35-V40 realm.

Success authorizes no provider mutation or secret action. All V4 page-signature,
completeness, no-residue, no-retry, secret, confirmation, and cleanup constraints
remain binding. The mandatory final Create/native Copy/native masked Paste
confirmation and later separate exact-row deletion confirmation remain external
and cannot be pre-approved, automated, delegated, or waived.

`authorizes_live_execution=false`
