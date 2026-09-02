# OmniRoute V36 fresh-session ordered selected-tab reacquisition — review brief

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Purpose

Replace consumed V35 with the smallest fresh-session one-shot attachment and
reacquisition gate. V35 proved that the selected Chrome window can contain
multiple valid tabs: one `openTabs()` returned eight records and the exact-one
total-cardinality gate stopped before claim or navigation. The owner confirmed
that Chrome profile `Codex-Chrome-Bell-PC2`, the intended window, and the
intended task tab are selected, with no other Chrome profile/window offered to
the extension. Current browser documentation states that `openTabs()` returns
top-level user tabs ordered by `lastOpened` descending.

V36 therefore validates the complete returned array privately, requires the
documented rank-zero record to be a current Cloudflare Dashboard tab, and
claims exactly that original record. It does not require the selected window to
contain only one tab and emits no tab metadata.

## Consumed predecessor boundary

- V35 incident commit:
  `1d9adba04a8d432865b2b28e1e4eb06a5945169a`.
- V35 Call 1 is consumed/PASS. V35 Call 2 is consumed/failed cleanly with
  `candidateCount=8`, `openTabsAttempted=1`, `openTabsFulfilled=1`, and every
  claim/navigation/wait/URL/snapshot count zero.
- V35 retained tab was null, eligibility false, failure state exact, and
  setup/agent/browser bindings null before the Node realm was reset.
- Never retry, continue, reinterpret, or reuse V35 or any earlier consumed
  gate. V4 remains static evidence only.

## Immutable runtime and semantic boundary

- Browser-client module:
  `C:\Users\chatc\.codex\plugins\cache\openai-bundled\chrome\26.831.20005\scripts\browser-client.mjs`
  at bytes `149771`, SHA-256
  `A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`.
- API documentation:
  `C:\Users\chatc\.codex\plugins\cache\openai-bundled\chrome\26.831.20005\docs\api.json`
  at bytes `58480`, SHA-256
  `A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.
- Required current APIs: `browsers.get(id)`, `Browser.documentation()`,
  `Browser.nameSession(name)`, `Browser.user`, `BrowserUser.openTabs()`,
  `BrowserUser.claimTab(tab)`, `Tab.id`, `Tab.goto`, `Tab.url`,
  `playwright.waitForTimeout(timeoutMs)`, locator evaluation.
- Current allowed `BrowserUserTabInfo` own fields are exactly `id`,
  `lastOpened`, `providerTabId`, `tabGroup`, `title`, and `url`; only `id` is
  mandatory in the API, while V36 additionally requires a safe rank-zero URL
  on the exact Cloudflare Dashboard origin.
- The source projection remains exactly `10661` records with SHA-256
  `C4C85893769D133224AC7404B628C8B0D4B0EBBFF471620B158E652E152B4EBD`
  under the fixed exclusion algorithm. Index must be empty and the exact
  12-path dirty product baseline must remain unchanged.

## One-shot semantics

The executable is one cell and one consuming gate. It consumes before import,
setup, browser attachment, documentation, naming, enumeration, or claim. It may
perform exactly one import, setup, browser get, complete documentation read and
write, session-name call, `openTabs()`, `claimTab()`, navigation, 20000 ms wait,
URL read, and body snapshot. There is no retry, fallback, loop over candidates,
selected-tab fallback, second enumeration, second claim, new tab, tab close,
manual integration, alternate browser, or alternate profile/window.

The returned list is rejected unless it is a bounded nonempty array and every
entry is an exact stable plain record: no symbols, no accessors, all own fields
enumerable data descriptors, only the current allowed names, mandatory nonempty
bounded control-free ID, and every present value a nonempty bounded control-free
string. The projector reads and caches each ID descriptor once. The rank-zero
record is the only candidate because the API contract orders records by most
recent open/focus and the owner has externally selected the intended task tab.
Its private URL must parse as HTTPS `dash.cloudflare.com`, with no port,
username, or password. Neither the record nor any field value is emitted.

The exact original rank-zero record is passed once to `claimTab()`. The claimed
tab's ID must equal the privately cached ID. V36 then navigates the claimed tab
to `https://dash.cloudflare.com/`, waits once for 20000 ms, and requires the
same account-home signature used by the reviewed predecessors:

- exact URL `https://dash.cloudflare.com/<32-lowercase-hex>/home`;
- exact HTTPS host with no port;
- exact same-account `/mysw.me` zone href count `1`;
- anchor count greater than zero;
- busy/progress count `0`.

The output is a fixed sanitized schema of booleans, bounded counts, states, and
error class only. It must not contain a tab ID, provider tab ID, title, URL,
group, timestamp, account ID, zone ID, href, secret, token, credential, raw
exception, raw listing, or raw documentation in the final evidence object. The
complete documentation is written separately only to satisfy the browser
runtime completeness contract.

On any failure, eligibility is false, the retained tab is null, setup/agent/
browser bindings are cleared, and state is terminal failure. The coordinator
must record sanitized evidence and reset the Node realm. A claim that occurred
before a later failure is released by realm disposal; no tab is closed. Any
non-exact output, exception, timeout, partial result, or uncertainty consumes
V36 permanently.

## One-shot executable

~~~javascript
let secureConsoleSetupBrowserRuntimeV36 = null;
let secureConsoleAgentV36 = null;
let secureConsoleChromeV36 = null;
let secureConsoleOwnedTaskTabV36 = null;
let secureConsoleOwnedTaskTabV36Eligible = false;
let secureConsoleV36Consumed = false;
let secureConsoleV36State = "UNCREATED";
await (async () => {
  const gateWasFresh = secureConsoleV36Consumed === false;
  secureConsoleV36Consumed = true;
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
  let result = "V36_FRESH_ORDERED_REACQUISITION_FAILED_STOP";
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
  let candidateUrlCloudflare = false;
  let controllerOwnership = false;
  let tabShape = false;
  let homeUrlValidated = false;
  let snapshotValidated = false;
  let semanticComplete = false;
  let snapshot = null;
  let adopted = null;
  let errorClass = "NONE";
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
  const trustedListing = (value) => {
    if (!Array.isArray(value) || value.length < 1 || value.length > 1000) {
      return null;
    }
    const allowed = new Set([
      "id", "lastOpened", "providerTabId", "tabGroup", "title", "url",
    ]);
    const projected = [];
    for (const item of value) {
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
        if (!descriptor || !("value" in descriptor) ||
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
      projected.push({ record: item, id: validatedId, url: validatedUrl });
    }
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
      record: first.record,
      id: first.id,
      count: value.length,
      urlCloudflare,
    } : null;
  };
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
      typeof secureConsoleOwnedTaskTabV35 === "undefined" &&
      secureConsoleSetupBrowserRuntimeV36 === null &&
      secureConsoleAgentV36 === null && secureConsoleChromeV36 === null &&
      secureConsoleOwnedTaskTabV36 === null &&
      secureConsoleOwnedTaskTabV36Eligible === false &&
      secureConsoleV36State === "UNCREATED";
    if (!declarationShape) throw new Error("FreshRealmDeclarationError");

    counters.importAttempted++;
    const imported = await import(
      "C:/Users/chatc/.codex/plugins/cache/openai-bundled/chrome/26.831.20005/scripts/browser-client.mjs"
    );
    counters.importFulfilled++;
    moduleShape = typeof imported === "object" && imported !== null &&
      typeof imported.setupBrowserRuntime === "function";
    if (!moduleShape) throw new Error("FreshRuntimeModuleShapeError");
    secureConsoleSetupBrowserRuntimeV36 = imported.setupBrowserRuntime;

    counters.setupAttempted++;
    secureConsoleAgentV36 = await secureConsoleSetupBrowserRuntimeV36();
    counters.setupFulfilled++;
    agentShape = typeof secureConsoleAgentV36 === "object" &&
      secureConsoleAgentV36 !== null &&
      typeof secureConsoleAgentV36.browsers?.get === "function";
    if (!agentShape) throw new Error("FreshRuntimeAgentShapeError");

    counters.connectAttempted++;
    secureConsoleChromeV36 =
      await secureConsoleAgentV36.browsers.get("chrome");
    counters.connectFulfilled++;
    connectedShape = typeof secureConsoleChromeV36 === "object" &&
      secureConsoleChromeV36 !== null &&
      typeof secureConsoleChromeV36.documentation === "function" &&
      typeof secureConsoleChromeV36.nameSession === "function" &&
      typeof secureConsoleChromeV36.user?.openTabs === "function" &&
      typeof secureConsoleChromeV36.user?.claimTab === "function";
    if (!connectedShape) throw new Error("FreshChromeShapeError");

    counters.documentationAttempted++;
    const documentation = await secureConsoleChromeV36.documentation();
    counters.documentationFulfilled++;
    documentationValidated = typeof documentation === "string" &&
      documentation.length >= 1000 && documentation.length <= 1000000;
    documentationLength = documentationValidated ? documentation.length : -1;
    if (!documentationValidated) {
      throw new Error("FreshChromeDocumentationShapeError");
    }
    counters.documentationWriteAttempted++;
    await nodeRepl.write(documentation);
    counters.documentationWriteFulfilled++;

    counters.nameAttempted++;
    await secureConsoleChromeV36.nameSession("🔐 OmniRoute secure console");
    counters.nameFulfilled++;
    sessionNamed = true;

    counters.openTabsAttempted++;
    const offered = await secureConsoleChromeV36.user.openTabs();
    counters.openTabsFulfilled++;
    offeredCount = Array.isArray(offered) ? offered.length : -1;
    const candidate = trustedListing(offered);
    listingValidated = candidate !== null;
    rankZeroSelected = listingValidated;
    candidateUrlCloudflare = listingValidated && candidate.urlCloudflare;
    if (!listingValidated) throw new Error("OrderedTabListingShapeError");

    counters.claimAttempted++;
    adopted = await secureConsoleChromeV36.user.claimTab(candidate.record);
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
    if (!exactCounters) throw new Error("V36CompletenessError");
    result = "EXACT_V36_ORDERED_SELECTED_TAB_ACCOUNT_HOME_REACQUISITION_PASS";
  } catch (error) {
    errorClass = safeErrorClass(error);
  }

  if (result ===
      "EXACT_V36_ORDERED_SELECTED_TAB_ACCOUNT_HOME_REACQUISITION_PASS") {
    secureConsoleOwnedTaskTabV36 = adopted;
    secureConsoleOwnedTaskTabV36Eligible = true;
    secureConsoleV36State = "V36_ACCOUNT_HOME_READY_ELIGIBLE";
  } else {
    secureConsoleOwnedTaskTabV36 = null;
    secureConsoleOwnedTaskTabV36Eligible = false;
    secureConsoleV36State = "V36_REACQUISITION_OR_READINESS_FAILED";
    secureConsoleChromeV36 = null;
    secureConsoleAgentV36 = null;
    secureConsoleSetupBrowserRuntimeV36 = null;
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
      candidateUrlCloudflare,
      controllerOwnership,
      tabShape,
      homeUrlValidated,
      snapshotValidated,
      semanticComplete,
      snapshot,
      ...counters,
      errorClass,
      consumed: secureConsoleV36Consumed,
      bindingEligible: secureConsoleOwnedTaskTabV36Eligible,
      bindingNull: secureConsoleOwnedTaskTabV36 === null,
      state: secureConsoleV36State,
    });
  } catch (terminalError) {
    secureConsoleOwnedTaskTabV36 = null;
    secureConsoleOwnedTaskTabV36Eligible = false;
    secureConsoleV36State = "V36_FINAL_OUTPUT_FAILED_STOP";
    secureConsoleChromeV36 = null;
    secureConsoleAgentV36 = null;
    secureConsoleSetupBrowserRuntimeV36 = null;
    throw terminalError;
  }
})();
~~~

## Required offline checks before review

- Extract exactly one `~~~javascript` cell, normalize CRLF to LF, record UTF-8
  byte length and uppercase SHA-256, and compile with `AsyncFunction` without
  execution.
- Pure fixtures must prove acceptance of ordinary and null-prototype exact
  records, rejection of class instances, symbols, accessors, non-enumerable or
  unexpected fields, empty/oversize/control-bearing values, empty or oversized
  arrays, missing rank-zero URL, non-Cloudflare rank-zero URL, and claimed-ID
  mismatch.
- A multi-record fixture must prove the exact original rank-zero object is the
  sole object passed to a one-call claim stub; no later record is inspected for
  selection and no field value appears in output.
- Snapshot fixtures must prove exact PASS and rejection of class instances,
  missing/extra fields, non-safe counts, wrong host/path/zone count, zero
  anchors, and busy state.
- Static review must account for every counter, every terminal cleanup path,
  documentation completeness, session naming before enumeration, and the
  absence of retry, alternate selection, close, provider mutation, and secret
  output.

## Action-time pins after independent PASS

Coordinator offline evidence before review:

- executable cells: `1`;
- normalized UTF-8 cell bytes: `13929`;
- cell SHA-256:
  `035DA9B16658C3A8F1CCDCDADE735E53DE3271B9CC065D130CB2C1F214E1050D`;
- `node.exe --check` of an async-function wrapper: `PASS`;
- pure exact-record, null-prototype, rejection, rank-zero object identity,
  one-call claim stub, snapshot projector, and negative semantic fixtures:
  `V36_PURE_FIXTURES_PASS`.

Live execution remains forbidden until an independent Sol High review returns
PASS with zero Critical/HIGH/IMPORTANT/Minor findings, the PASS review is
committed directly on this brief, and a non-self-referential execution
classification plus separate post-commit coordinator tuple are complete.

Immediately before the one cell, revalidate exact HEAD/parent/one-path chain,
brief/review/classification bytes and hashes, source projection, empty index,
12-path baseline, runtime module/docs/API, clean evidence worktree, zero Windows
residue, complete VM1205 safe checkpoint, absent public DNS, no competing owner,
and the owner's exact profile/window/task-tab confirmation. Reset the Node realm
once and prove every V35 and V36 declaration absent. Extract the committed cell
at its reviewed bytes/hash and syntax-check it without execution.

Any mismatch stops before consumption. After the cell starts, every failure or
uncertainty is terminal and V36 is spent. Exact PASS retains only the reviewed
V36 browser and claimed account-home tab bindings for the next separately
reviewed action.

The mandatory final Create/native Copy/native masked Paste confirmation remains
unreached and cannot be preapproved. The later separate exact-row deletion
confirmation also remains unreached and separately mandatory. V36 grants no
authority for token creation, secret transmission, provider-persistent change,
proxy/tunnel/DNS/routing mutation, VM power action, or row deletion.
