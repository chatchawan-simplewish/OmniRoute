# OmniRoute V35 fresh-session open-tabs claim and account-home reacquisition — replacement brief

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Purpose and predecessor

V34 Call 1 passed, but V34 Call 2 is consumed and failed cleanly because
`tabs.selected()` returned no controllable tab ID. Its fixed incident is commit
`0d6de7be7aea903bff24c82fb81db5ef25239f30` at
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v34-selected-tab-ownership-shape-live-incident.md`.

V34 must never be retried, continued, reinterpreted, or reused. V35 is the
smallest current-API replacement: one fresh attachment call followed by one
separately consumed call that lists the user-offered tabs once, requires exactly
one structurally valid candidate, claims that exact opaque ID once, and performs
the unchanged private account-home semantic check. Neither call is executable
until this exact committed brief receives independent Sol High PASS with zero
unresolved Critical, HIGH, or IMPORTANT findings, followed by a
non-self-referential classification and separate post-commit coordinator tuple.

## Reviewed current API boundary

The only allowed module is
`C:/Users/chatc/.codex/plugins/cache/openai-bundled/chrome/26.831.20005/scripts/browser-client.mjs`.
Action time must reproduce `149771` bytes and SHA-256
`A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`.
The paired `docs/api.json` must reproduce `58480` bytes and SHA-256
`A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.

The exact reviewed API declares `browsers.get(id)`, `Browser.documentation()`,
`BrowserUser.openTabs()`, `BrowserUser.claimTab(tab)`, `Tab.goto(url)`,
`Tab.url()`, one-argument `waitForTimeout(timeoutMs)`, `locator(selector)`, and
read-only locator `evaluate`. `openTabs()` returns user-owned
`BrowserUserTabInfo` values with mandatory opaque `id`; `claimTab()` accepts the
exact returned value or its exact ID and returns a controllable `Tab`.

## Call 1 — fresh Chrome attachment

This is the sole Call-1 source. Its first executable statement consumes Call 1
before import, setup, connection, or documentation access. It performs one
import, one setup, one `browsers.get("chrome")`, one complete documentation
read/write, and one fixed terminal write. It performs no browser or tab list,
selection, claim, navigation, or page action.

~~~javascript
let secureConsoleSetupBrowserRuntimeV35 = null;
let secureConsoleAgentV35 = null;
let secureConsoleChromeV35 = null;
let secureConsoleV35AttachmentConsumed = false;
let secureConsoleV35AttachmentExact = false;
let secureConsoleV35AttachmentState = "UNCREATED";
await (async () => {
  const gateWasFresh = secureConsoleV35AttachmentConsumed === false;
  secureConsoleV35AttachmentConsumed = true;
  const counters = {
    importAttempted: 0, importFulfilled: 0,
    setupAttempted: 0, setupFulfilled: 0,
    connectAttempted: 0, connectFulfilled: 0,
    documentationAttempted: 0, documentationFulfilled: 0,
    documentationWriteAttempted: 0, documentationWriteFulfilled: 0,
    writeAttempted: 0,
  };
  let result = "V35_FRESH_CHROME_ATTACHMENT_FAILED_STOP";
  let declarationShape = false;
  let moduleShape = false;
  let agentShape = false;
  let connectedShape = false;
  let documentationValidated = false;
  let documentationLength = -1;
  let errorClass = "NONE";
  const safeErrorClass = (error) => {
    const name = typeof error?.name === "string" ? error.name : "Error";
    return /^[A-Za-z][A-Za-z0-9_]{0,63}$/.test(name) ? name : "Error";
  };
  try {
    declarationShape =
      gateWasFresh === true &&
      typeof secureConsoleV34AttachmentConsumed === "undefined" &&
      typeof secureConsoleV34AdoptionConsumed === "undefined" &&
      secureConsoleSetupBrowserRuntimeV35 === null &&
      secureConsoleAgentV35 === null &&
      secureConsoleChromeV35 === null &&
      secureConsoleV35AttachmentState === "UNCREATED";
    if (!declarationShape) throw new Error("FreshRealmDeclarationError");

    counters.importAttempted++;
    const imported = await import(
      "C:/Users/chatc/.codex/plugins/cache/openai-bundled/chrome/26.831.20005/scripts/browser-client.mjs"
    );
    counters.importFulfilled++;
    moduleShape =
      typeof imported === "object" &&
      imported !== null &&
      typeof imported.setupBrowserRuntime === "function";
    if (!moduleShape) throw new Error("FreshRuntimeModuleShapeError");
    secureConsoleSetupBrowserRuntimeV35 = imported.setupBrowserRuntime;

    counters.setupAttempted++;
    secureConsoleAgentV35 = await secureConsoleSetupBrowserRuntimeV35();
    counters.setupFulfilled++;
    agentShape =
      typeof secureConsoleAgentV35 === "object" &&
      secureConsoleAgentV35 !== null &&
      typeof secureConsoleAgentV35.browsers?.get === "function";
    if (!agentShape) throw new Error("FreshRuntimeAgentShapeError");

    counters.connectAttempted++;
    secureConsoleChromeV35 =
      await secureConsoleAgentV35.browsers.get("chrome");
    counters.connectFulfilled++;
    connectedShape =
      typeof secureConsoleChromeV35 === "object" &&
      secureConsoleChromeV35 !== null &&
      typeof secureConsoleChromeV35.documentation === "function" &&
      typeof secureConsoleChromeV35.user?.openTabs === "function" &&
      typeof secureConsoleChromeV35.user?.claimTab === "function";
    if (!connectedShape) throw new Error("FreshChromeShapeError");

    counters.documentationAttempted++;
    const documentation = await secureConsoleChromeV35.documentation();
    counters.documentationFulfilled++;
    documentationValidated =
      typeof documentation === "string" &&
      documentation.length >= 1000 &&
      documentation.length <= 1000000;
    documentationLength = documentationValidated ? documentation.length : -1;
    if (!documentationValidated) {
      throw new Error("FreshChromeDocumentationShapeError");
    }
    counters.documentationWriteAttempted++;
    await nodeRepl.write(documentation);
    counters.documentationWriteFulfilled++;

    secureConsoleV35AttachmentExact =
      declarationShape && moduleShape && agentShape && connectedShape &&
      documentationValidated &&
      counters.importAttempted === 1 && counters.importFulfilled === 1 &&
      counters.setupAttempted === 1 && counters.setupFulfilled === 1 &&
      counters.connectAttempted === 1 && counters.connectFulfilled === 1 &&
      counters.documentationAttempted === 1 &&
      counters.documentationFulfilled === 1 &&
      counters.documentationWriteAttempted === 1 &&
      counters.documentationWriteFulfilled === 1;
    if (!secureConsoleV35AttachmentExact) {
      throw new Error("FreshChromeAttachmentCompletenessError");
    }
    secureConsoleV35AttachmentState = "V35_ATTACHMENT_PASS";
    result = "EXACT_V35_FRESH_CHROME_ATTACHMENT_PASS";
  } catch (error) {
    errorClass = safeErrorClass(error);
    secureConsoleV35AttachmentExact = false;
    secureConsoleV35AttachmentState = "V35_ATTACHMENT_FAILED_STOP";
    secureConsoleChromeV35 = null;
    secureConsoleAgentV35 = null;
    secureConsoleSetupBrowserRuntimeV35 = null;
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
      consumed: secureConsoleV35AttachmentConsumed,
      attachmentExact: secureConsoleV35AttachmentExact,
      state: secureConsoleV35AttachmentState,
      ...counters,
      errorClass,
    });
  } catch (terminalError) {
    secureConsoleV35AttachmentExact = false;
    secureConsoleV35AttachmentState =
      "V35_ATTACHMENT_FINAL_OUTPUT_FAILED_STOP";
    secureConsoleChromeV35 = null;
    secureConsoleAgentV35 = null;
    secureConsoleSetupBrowserRuntimeV35 = null;
    throw terminalError;
  }
})();
~~~

Call-1 PASS requires exact result `EXACT_V35_FRESH_CHROME_ATTACHMENT_PASS`,
every declared shape/validation boolean true, documentation length within
`1000..1000000`, every attempted/fulfilled pair `1/1`, consumed and
attachmentExact true, state `V35_ATTACHMENT_PASS`, error class `NONE`, complete
documentation output, complete fixed terminal output, and completed tool
status. Anything else spends Call 1 and blocks Call 2 permanently.

## Call 2 — sole offered-tab claim and account-home reacquisition

Call 2 is a separate one-shot cell. Its first executable statement consumes
Call 2 before any precondition, list, or claim. It requires exact persistent
Call-1 PASS. It calls `openTabs()` once, permits exactly one returned candidate,
privately validates that candidate against the exact current
`BrowserUserTabInfo` field set, calls `claimTab()` once with only its exact
validated opaque ID, then applies the unchanged account-home semantic gate.
The projector requires the established cross-realm plain-record shape,
enumerates every own string and symbol name, rejects accessors, non-enumerable
or non-current fields, and caches the validated ID from its single descriptor
read without re-reading the untrusted candidate.

~~~javascript
let secureConsoleOwnedTaskTabV35 = null;
let secureConsoleOwnedTaskTabV35Eligible = false;
let secureConsoleOwnedTaskTabV35State = "UNCREATED";
let secureConsoleV35AdoptionConsumed = false;
await (async () => {
  const gateWasFresh = secureConsoleV35AdoptionConsumed === false;
  secureConsoleV35AdoptionConsumed = true;
  const counters = {
    openTabsAttempted: 0, openTabsFulfilled: 0,
    claimAttempted: 0, claimFulfilled: 0,
    navigationAttempted: 0, navigationFulfilled: 0,
    waitAttempted: 0, waitFulfilled: 0,
    urlAttempted: 0, urlFulfilled: 0,
    snapshotAttempted: 0, snapshotFulfilled: 0,
    writeAttempted: 0,
  };
  let result = "PRECONDITION_FAIL";
  let declarationShape = false;
  let predecessorExact = false;
  let candidateCount = -1;
  let candidateValidated = false;
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
  const trustedCandidate = (value) => {
    if (!Array.isArray(value) || value.length !== 1) return null;
    const item = value[0];
    if (!plainRecord(item)) return null;
    if (Object.getOwnPropertySymbols(item).length !== 0) return null;
    const allowed = new Set([
      "id", "lastOpened", "providerTabId", "tabGroup", "title", "url",
    ]);
    const keys = Object.getOwnPropertyNames(item);
    if (!keys.includes("id") || keys.some((key) => !allowed.has(key))) {
      return null;
    }
    let validatedId = null;
    for (const key of keys) {
      const descriptor = Object.getOwnPropertyDescriptor(item, key);
      if (!descriptor || !("value" in descriptor) ||
          descriptor.enumerable !== true) return null;
      const limit = key === "url" ? 16384 : key === "title" ? 4096 : 512;
      if (typeof descriptor.value !== "string" ||
          descriptor.value.length === 0 ||
          descriptor.value.length > limit ||
          /[\u0000-\u001f\u007f]/.test(descriptor.value)) {
        return null;
      }
      if (key === "id") validatedId = descriptor.value;
    }
    return validatedId === null ? null : { id: validatedId };
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
      secureConsoleOwnedTaskTabV35 === null &&
      secureConsoleOwnedTaskTabV35Eligible === false &&
      secureConsoleOwnedTaskTabV35State === "UNCREATED";
    predecessorExact =
      declarationShape &&
      secureConsoleV35AttachmentConsumed === true &&
      secureConsoleV35AttachmentExact === true &&
      secureConsoleV35AttachmentState === "V35_ATTACHMENT_PASS" &&
      typeof secureConsoleChromeV35 === "object" &&
      secureConsoleChromeV35 !== null &&
      typeof secureConsoleChromeV35.user?.openTabs === "function" &&
      typeof secureConsoleChromeV35.user?.claimTab === "function";
    if (!predecessorExact) {
      throw new Error("FreshSessionPredecessorStateError");
    }

    counters.openTabsAttempted++;
    const offered = await secureConsoleChromeV35.user.openTabs();
    counters.openTabsFulfilled++;
    candidateCount = Array.isArray(offered) ? offered.length : -1;
    const candidate = trustedCandidate(offered);
    candidateValidated = candidate !== null;
    if (!candidateValidated) throw new Error("SoleOfferedTabShapeError");

    counters.claimAttempted++;
    adopted = await secureConsoleChromeV35.user.claimTab(candidate.id);
    counters.claimFulfilled++;
    controllerOwnership =
      typeof adopted === "object" && adopted !== null &&
      typeof adopted.id === "string" &&
      adopted.id === candidate.id &&
      adopted.id.length > 0 && adopted.id.length <= 512 &&
      !/[\u0000-\u001f\u007f]/.test(adopted.id);
    tabShape =
      controllerOwnership &&
      typeof adopted.goto === "function" &&
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
          hostExact:
            location.protocol === "https:" &&
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
    semanticComplete =
      snapshotValidated && snapshot.hostExact === true &&
      snapshot.accountHomePath === true &&
      snapshot.exactZoneHrefCount === 1 &&
      snapshot.allAnchorCount > 0 && snapshot.busyCount === 0;
    if (!semanticComplete) {
      throw new Error("AccountHomeSemanticSignatureError");
    }
    result = "EXACT_V35_CLAIMED_ACCOUNT_HOME_REACQUISITION_PASS";
  } catch (error) {
    errorClass = safeErrorClass(error);
  }

  if (result === "EXACT_V35_CLAIMED_ACCOUNT_HOME_REACQUISITION_PASS") {
    secureConsoleOwnedTaskTabV35 = adopted;
    secureConsoleOwnedTaskTabV35Eligible = true;
    secureConsoleOwnedTaskTabV35State = "V35_ACCOUNT_HOME_READY_ELIGIBLE";
  } else {
    secureConsoleOwnedTaskTabV35 = null;
    secureConsoleOwnedTaskTabV35Eligible = false;
    secureConsoleOwnedTaskTabV35State = "V35_REACQUISITION_OR_READINESS_FAILED";
    secureConsoleChromeV35 = null;
    secureConsoleAgentV35 = null;
    secureConsoleSetupBrowserRuntimeV35 = null;
  }
  counters.writeAttempted++;
  try {
    await nodeRepl.write({
      result,
      declarationShape,
      predecessorExact,
      candidateCount,
      candidateValidated,
      controllerOwnership,
      tabShape,
      homeUrlValidated,
      snapshotValidated,
      semanticComplete,
      snapshot,
      openTabsAttempted: counters.openTabsAttempted,
      openTabsFulfilled: counters.openTabsFulfilled,
      claimAttempted: counters.claimAttempted,
      claimFulfilled: counters.claimFulfilled,
      navigationAttempted: counters.navigationAttempted,
      navigationFulfilled: counters.navigationFulfilled,
      waitAttempted: counters.waitAttempted,
      waitFulfilled: counters.waitFulfilled,
      urlAttempted: counters.urlAttempted,
      urlFulfilled: counters.urlFulfilled,
      snapshotAttempted: counters.snapshotAttempted,
      snapshotFulfilled: counters.snapshotFulfilled,
      writeAttempted: counters.writeAttempted,
      errorClass,
      consumed: secureConsoleV35AdoptionConsumed,
      bindingEligible: secureConsoleOwnedTaskTabV35Eligible,
      bindingNull: secureConsoleOwnedTaskTabV35 === null,
      bindingState: secureConsoleOwnedTaskTabV35State,
    });
  } catch (terminalError) {
    secureConsoleOwnedTaskTabV35 = null;
    secureConsoleOwnedTaskTabV35Eligible = false;
    secureConsoleOwnedTaskTabV35State = "V35_FINAL_OUTPUT_FAILED_STOP";
    secureConsoleChromeV35 = null;
    secureConsoleAgentV35 = null;
    secureConsoleSetupBrowserRuntimeV35 = null;
    throw terminalError;
  }
})();
~~~

Call-2 PASS requires exact result
`EXACT_V35_CLAIMED_ACCOUNT_HOME_REACQUISITION_PASS`, declaration/predecessor,
candidate, controller, tab, URL, snapshot, and semantic booleans all true;
candidate count exactly `1`; exact fixed snapshot with zone href count `1`,
positive anchors, and busy count `0`; every attempted/fulfilled pair `1/1`;
error class `NONE`; consumed and bindingEligible true; bindingNull false; state
`V35_ACCOUNT_HOME_READY_ELIGIBLE`; complete fixed terminal output; and completed
tool status.

An ordinary failure or JavaScript-visible final-output rejection spends Call 2,
clears every V35 controller/owner binding, never closes the externally owned
tab, and stops. If transport failure or truncation is not visible inside
JavaScript, bindings may remain; dispose the entire fresh Node realm and do not
reuse it. Never retry either call.

## Prohibited actions and secret boundary

Neither call may use `browsers.list`, `getDefault`, `getForUrl`,
`get("extension")`, `tabs.selected`, `tabs.list`, `tabs.get`, `tabs.new`, more
than one `openTabs` or claim, an alternate candidate, reconnect, retry,
fallback, another browser/profile/window, screenshot, DOM serialization,
clipboard, click, press, fill, Create, edit, delete, provider mutation, process
start, VM mutation, proxy/routing change, or credential action.

No offered-tab ID, providerTabId, URL, title, group, timestamp, page URL/path,
account identifier, page text, DOM, attribute, exception message, credential,
token, or secret may be emitted, logged, committed, or placed in review
evidence. Only fixed booleans, bounded counters, sanitized error class, and the
five-field semantic snapshot may leave the cell.

The final Create/native Copy/native masked Paste confirmation remains mandatory
immediately before those actions. The later exact-row deletion confirmation is
separate and remains mandatory. Standing authority waives neither.

## Review, classification, and action-time gates

Before Call 1:

- commit this exact brief alone and pin its bytes, SHA-256, blob, and both
  normalized executable cells;
- obtain independent Sol High PASS with zero unresolved Critical, HIGH, or
  IMPORTANT findings;
- commit a non-self-referential classification directly parented to that PASS
  review and record the post-commit coordinator tuple separately;
- revalidate exact current module/API bytes, stable projection, empty index,
  exact 12-path dirty baseline, clean evidence worktree, zero temporary/process
  residue, VM1205 safe checkpoint, absent public DNS, and the owner's exact
  profile/window/tab confirmation;
- reset to a fresh Node realm and prove every V34 and V35 declaration absent;
  and
- extract Call 1 from the committed brief and require its exact reviewed bytes
  and SHA-256 before the sole Node call.

After exact Call-1 PASS and before Call 2, require the same immutable pins,
exact persistent Call-1 state and output counters, every Call-2 declaration
absent, and exact extracted Call-2 bytes/SHA-256.

A failed, uncertain, malformed, incomplete, or residue-bearing result consumes
that call and stops. Do not retry, continue, reinterpret, reconnect, fall back,
relax a verdict, or manually integrate. JavaScript-visible terminal-output
rejection performs fixed cleanup and rethrows without a second output;
unobservable transport uncertainty requires disposal of the entire fresh Node
realm before any separately reviewed successor.
