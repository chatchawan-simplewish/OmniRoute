# OmniRoute V39 fresh-session cross-realm task-tab reacquisition — review brief

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Purpose

Replace the consumed V37 reacquisition with the smallest fresh-session
one-shot that accepts the exact cross-realm listing shape proven by consumed
V38, selects exactly one owner-intended Cloudflare `mysw.me` task tab from
bounded descriptor-validated records, claims it once, and proves the unchanged
account-home semantic signature. V39 performs no provider mutation.

## Consumed predecessor boundary

V3 is consumed and failed. V4 is static evidence only. V34 Call 2, V35, V36,
V37, and V38 are consumed and may never be retried, continued, reinterpreted,
or used as inherited state. V38 proved `Array.isArray=true`, local prototype
identity false, offered count `9`, and every reviewed array/record/descriptor/
value predicate true; it claimed and navigated zero tabs and its realm was
reset.

## Design delta and fail-closed boundary

V39 retains the reviewed V37 selection, claim, account-home URL, exact zone
anchor, busy-state, bounded evidence, completeness, and cleanup semantics. The
only listing-shape change is removal of local `Array.prototype` identity as a
precondition. The listing must still be an array; have no symbols; have an own
non-enumerable data `length` safe integer in `1..1000`; have exactly `length`
plus every numeric own name; have every numeric index as an enumerable own data
descriptor; and contain only plain, symbol-free records with the fixed allowed
key set, required ID, enumerable own data descriptors, bounded nonempty strings,
and no control characters.

Exactly one record URL must parse to HTTPS `dash.cloudflare.com`, with no port,
credentials, or origin ambiguity, and a path matching exactly
`/<32 lowercase hex>/mysw.me` plus an optional suffix. Zero or multiple matches
stop before claim. No ID, URL, title, provider ID, group, timestamp, raw
listing, descriptor, prototype, error, secret, or credential is emitted.

The outer handler is an unbound `catch` and assigns only literal
`errorClass="Error"`; it never binds, reads, stringifies, coerces, or
prototype-tests the thrown value. Success retains only the reviewed runtime,
browser, and claimed-tab bindings in this fresh realm for a later separately
reviewed step. Failure clears all such bindings. Terminal-write failure repeats
cleanup and rethrows. Any timeout or transport uncertainty consumes V39 and
requires realm disposal; no retry or continuation is permitted.

## One-shot executable

The following is the sole live cell. It must be extracted from committed bytes,
LF-normalized exactly as reviewed, hash-checked, syntax-checked, and sent once
without wrapper or modification.

~~~javascript
let secureConsoleSetupBrowserRuntimeV39 = null;
let secureConsoleAgentV39 = null;
let secureConsoleChromeV39 = null;
let secureConsoleOwnedTaskTabV39 = null;
let secureConsoleOwnedTaskTabV39Eligible = false;
let secureConsoleV39Consumed = false;
let secureConsoleV39State = "UNCREATED";
await (async () => {
  const gateWasFresh = secureConsoleV39Consumed === false;
  secureConsoleV39Consumed = true;
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
  let result = "V39_FRESH_CROSS_REALM_TASK_REACQUISITION_FAILED_STOP";
  let declarationShape = false;
  let moduleShape = false;
  let agentShape = false;
  let connectedShape = false;
  let documentationValidated = false;
  let documentationLength = -1;
  let sessionNamed = false;
  let offeredCount = -1;
  let listingValidated = false;
  let targetCandidateCount = -1;
  let candidateValidated = false;
  let candidateTaskUrlValidated = false;
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
  // BEGIN_V39_PURE_TRUSTED_LISTING
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
    const candidates = [];
    for (let index = 0; index < projected.length; index++) {
      const entry = projected[index];
      if (entry.url === null) continue;
      let parsed = null;
      try {
        parsed = new URL(entry.url);
      } catch {
        continue;
      }
      const originExact =
        parsed.protocol === "https:" &&
        parsed.hostname === "dash.cloudflare.com" &&
        parsed.port === "" && parsed.username === "" &&
        parsed.password === "";
      const taskPath =
        /^\/[0-9a-f]{32}\/mysw\.me(?:\/.*)?$/.test(parsed.pathname);
      if (originExact && taskPath) candidates.push({ id: entry.id });
    }
    return {
      count: length,
      targetCount: candidates.length,
      candidate: candidates.length === 1 ? candidates[0] : null,
    };
  };
  // END_V39_PURE_TRUSTED_LISTING
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
      secureConsoleSetupBrowserRuntimeV39 === null &&
      secureConsoleAgentV39 === null && secureConsoleChromeV39 === null &&
      secureConsoleOwnedTaskTabV39 === null &&
      secureConsoleOwnedTaskTabV39Eligible === false &&
      secureConsoleV39State === "UNCREATED";
    if (!declarationShape) throw new Error("FreshRealmDeclarationError");
    secureConsoleV39State = "V39_CONSUMING";

    counters.importAttempted++;
    const imported = await import(
      "file:///C:/Users/chatc/.codex/plugins/cache/openai-bundled/chrome/26.831.20005/scripts/browser-client.mjs"
    );
    counters.importFulfilled++;
    moduleShape = typeof imported === "object" && imported !== null &&
      typeof imported.setupBrowserRuntime === "function";
    if (!moduleShape) throw new Error("FreshRuntimeModuleShapeError");
    secureConsoleSetupBrowserRuntimeV39 = imported.setupBrowserRuntime;

    counters.setupAttempted++;
    secureConsoleAgentV39 = await secureConsoleSetupBrowserRuntimeV39();
    counters.setupFulfilled++;
    agentShape = typeof secureConsoleAgentV39 === "object" &&
      secureConsoleAgentV39 !== null &&
      typeof secureConsoleAgentV39.browsers?.get === "function";
    if (!agentShape) throw new Error("FreshRuntimeAgentShapeError");

    counters.connectAttempted++;
    secureConsoleChromeV39 =
      await secureConsoleAgentV39.browsers.get("chrome");
    counters.connectFulfilled++;
    connectedShape = typeof secureConsoleChromeV39 === "object" &&
      secureConsoleChromeV39 !== null &&
      typeof secureConsoleChromeV39.documentation === "function" &&
      typeof secureConsoleChromeV39.nameSession === "function" &&
      typeof secureConsoleChromeV39.user?.openTabs === "function" &&
      typeof secureConsoleChromeV39.user?.claimTab === "function";
    if (!connectedShape) throw new Error("FreshChromeShapeError");

    counters.documentationAttempted++;
    const documentation = await secureConsoleChromeV39.documentation();
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
    await secureConsoleChromeV39.nameSession("🔐 OmniRoute secure console");
    counters.nameFulfilled++;
    sessionNamed = true;

    counters.openTabsAttempted++;
    const offered = await secureConsoleChromeV39.user.openTabs();
    counters.openTabsFulfilled++;
    const listing = trustedListing(offered);
    listingValidated = listing !== null;
    offeredCount = listingValidated ? listing.count : -1;
    targetCandidateCount = listingValidated ? listing.targetCount : -1;
    const candidate = listingValidated ? listing.candidate : null;
    candidateValidated = candidate !== null && targetCandidateCount === 1;
    candidateTaskUrlValidated = candidateValidated;
    if (!candidateValidated) throw new Error("UniqueTaskTabShapeError");

    counters.claimAttempted++;
    adopted = await secureConsoleChromeV39.user.claimTab(candidate.id);
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
    if (!exactCounters) throw new Error("V39CompletenessError");
    result = "EXACT_V39_CROSS_REALM_TASK_TAB_ACCOUNT_HOME_REACQUISITION_PASS";
  } catch {
    errorClass = "Error";
  }

  if (result ===
      "EXACT_V39_CROSS_REALM_TASK_TAB_ACCOUNT_HOME_REACQUISITION_PASS") {
    secureConsoleOwnedTaskTabV39 = adopted;
    secureConsoleOwnedTaskTabV39Eligible = true;
    secureConsoleV39State = "V39_ACCOUNT_HOME_READY_ELIGIBLE";
    continuationBindingsRetained =
      typeof secureConsoleSetupBrowserRuntimeV39 === "function" &&
      secureConsoleAgentV39 !== null && secureConsoleChromeV39 !== null &&
      secureConsoleOwnedTaskTabV39 !== null;
  } else {
    secureConsoleOwnedTaskTabV39 = null;
    secureConsoleOwnedTaskTabV39Eligible = false;
    secureConsoleV39State = "V39_REACQUISITION_OR_READINESS_FAILED";
    secureConsoleChromeV39 = null;
    secureConsoleAgentV39 = null;
    secureConsoleSetupBrowserRuntimeV39 = null;
    failureCleanupComplete =
      secureConsoleSetupBrowserRuntimeV39 === null &&
      secureConsoleAgentV39 === null && secureConsoleChromeV39 === null &&
      secureConsoleOwnedTaskTabV39 === null &&
      secureConsoleOwnedTaskTabV39Eligible === false;
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
      targetCandidateCount,
      candidateValidated,
      candidateTaskUrlValidated,
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
      consumed: secureConsoleV39Consumed,
      bindingEligible: secureConsoleOwnedTaskTabV39Eligible,
      bindingNull: secureConsoleOwnedTaskTabV39 === null,
      state: secureConsoleV39State,
    });
  } catch (terminalError) {
    secureConsoleOwnedTaskTabV39 = null;
    secureConsoleOwnedTaskTabV39Eligible = false;
    secureConsoleV39State = "V39_FINAL_OUTPUT_FAILED_STOP";
    secureConsoleChromeV39 = null;
    secureConsoleAgentV39 = null;
    secureConsoleSetupBrowserRuntimeV39 = null;
    throw terminalError;
  }
})();
~~~

## Required offline checks before review

- Prove one executable fence, LF-normalized syntax, exact bytes and SHA-256.
- Run the committed pure fixture against an ordinary local listing, the exact
  foreign-realm shape, zero and multiple target candidates, unexpected array
  names, missing/index accessors, record accessors, invalid values, a full-cell
  success path, and hostile thrown values whose names must never be read.
- Statistically prove the one-site import/setup/browser-get/documentation-write/
  name/openTabs/claim/goto/wait/url/snapshot contract and absence of retry,
  selected/list/get fallback, reconnect, new/close-tab, provider, clipboard,
  credential, DNS, routing, VM, listener, proxy, or owner sites.
- Independent Sol High review must report Critical `0`, HIGH `0`, IMPORTANT `0`,
  Minor `0` and commit its review artifact. A PASS is evidence only.

## Action-time pins after independent PASS

Before a live send, require a non-self-referential classification and separate
post-commit tuple; exact brief/fixture/review ancestry and byte/hash/blob pins;
stable `10661`-record projection digest
`C4C85893769D133224AC7404B628C8B0D4B0EBBFF471620B158E652E152B4EBD`;
empty index; exact twelve-path product baseline; pinned runtime/docs bytes;
clean evidence worktree; zero Windows residue; absent public DNS; unchanged
VM1205 safe checkpoint; archived prior owner; no competing owner; the exact
owner-selected Chrome profile/window/task-tab confirmation; and a newly reset
realm with all named V35-V39 declarations absent.

Success authorizes only retention of the proven claimed account-home tab for
the next separately reviewed step in the same realm. It does not authorize any
provider mutation or secret action. Failure or uncertainty requires immediate
realm disposal and a new reviewed contract.

All V4 page-signature, completeness, no-residue, no-retry, secret,
confirmation, and cleanup constraints remain binding. The final Create/native
Copy/native masked Paste confirmation and the later separate exact-row deletion
confirmation remain mandatory external gates and cannot be pre-approved,
automated, delegated, or waived.

`authorizes_live_execution=false`
