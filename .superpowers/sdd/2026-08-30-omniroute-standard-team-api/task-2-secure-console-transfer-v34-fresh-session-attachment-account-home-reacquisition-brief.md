# OmniRoute V34 fresh-session Chrome attachment and account-home reacquisition brief

`authorizes_live_execution=false`

## Design and predecessor

V33 was never executed and is permanently action-time ineligible at drift
incident commit `60358392f188fe3706c36aa518c9947a21e8ba7b`. Its pinned
API document disappeared after the installed browser runtime moved to
`26.831.20005`, and the persistent Node controller/predecessor bindings are
absent. Substituting runtime files into V33 or assuming the lost bindings would
violate its reviewed contract.

Three successor designs were considered:

1. send V33 directly with the new module;
2. list or discover Chrome profiles/tabs through a different control surface;
   or
3. reuse the independently proven V5 two-stage architecture with new
   declarations and current exact runtime pins.

Design 3 is selected under standing preapproval. Design 1 cannot satisfy
V33's controller/predecessor checks. Design 2 violates the owner's
profile/window/tab boundary. V34 performs exactly two separately classified,
no-retry Node calls:

1. a sole fresh-session runtime import/setup/Chrome attachment plus complete
   documentation emission; then
2. only after exact Call-1 PASS, one selected-tab adoption followed by
   read-only navigation to Cloudflare account home and a fixed title-free
   semantic signature.

The owner already supplied the exact external attachment confirmation:
Chrome Profile `Codex-Chrome-Bell-PC2`, intended window, and intended task
tab are selected, and no other Chrome profile/window is offered to the
extension. The contract reads no profile, window, extension, cookie, storage,
password, or session metadata.

## Current runtime pins

- Bootstrap module:
  `C:/Users/chatc/.codex/plugins/cache/openai-bundled/chrome/26.831.20005/scripts/browser-client.mjs`;
  `149771` bytes; SHA-256
  `A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`.
- Installed API document:
  `C:/Users/chatc/.codex/plugins/cache/openai-bundled/chrome/26.831.20005/docs/api.json`;
  `58480` bytes; SHA-256
  `A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.
- The installed API declares:
  `Browsers.get(id: string): Promise<Browser>`,
  `Browser.documentation(): Promise<string>`,
  `Tabs.selected(): Promise<undefined | Tab>`,
  `Tab.url(): Promise<undefined | string>`, and
  `Tab.title(): Promise<undefined | string>`.
- The module exports exactly the reviewed `setupBrowserRuntime` entry point.

Any byte, path, method-shape, profile confirmation, worktree, projection,
runtime, VM, DNS, residue, or predecessor mismatch stops before its consuming
call. No fallback version or alternate module is permitted.

## Call 1 — sole fresh-session Chrome attachment

The first Node call receiving this cell consumes the V34 attachment gate before
module import, setup, connect, or documentation. It performs one dynamic import,
one runtime setup, one exact `agent.browsers.get("chrome")`, and one complete
`chrome.documentation()` read and direct output. The documentation string is
validated as a bounded nonempty string before emission. No browser/tab/profile
listing or tab method is called.

~~~javascript
let secureConsoleSetupBrowserRuntimeV34 = null;
let secureConsoleAgentV34 = null;
let secureConsoleChromeV34 = null;
let secureConsoleV34AttachmentConsumed = false;
let secureConsoleV34AttachmentExact = false;
let secureConsoleV34AttachmentState = "UNCREATED";
await (async () => {
  const gateWasFresh = secureConsoleV34AttachmentConsumed === false;
  secureConsoleV34AttachmentConsumed = true;
  const counters = {
    importAttempted: 0, importFulfilled: 0,
    setupAttempted: 0, setupFulfilled: 0,
    connectAttempted: 0, connectFulfilled: 0,
    documentationAttempted: 0, documentationFulfilled: 0,
    documentationWriteAttempted: 0, documentationWriteFulfilled: 0,
    writeAttempted: 0,
  };
  let result = "V34_FRESH_CHROME_ATTACHMENT_FAILED_STOP";
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
      typeof secureConsoleChromeV5 === "undefined" &&
      typeof secureConsoleZoneV32Consumed === "undefined" &&
      typeof secureConsoleZoneV33Consumed === "undefined" &&
      secureConsoleSetupBrowserRuntimeV34 === null &&
      secureConsoleAgentV34 === null &&
      secureConsoleChromeV34 === null &&
      secureConsoleV34AttachmentState === "UNCREATED";
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
    secureConsoleSetupBrowserRuntimeV34 = imported.setupBrowserRuntime;

    counters.setupAttempted++;
    secureConsoleAgentV34 = await secureConsoleSetupBrowserRuntimeV34();
    counters.setupFulfilled++;
    agentShape =
      typeof secureConsoleAgentV34 === "object" &&
      secureConsoleAgentV34 !== null &&
      typeof secureConsoleAgentV34.browsers?.get === "function";
    if (!agentShape) throw new Error("FreshRuntimeAgentShapeError");

    counters.connectAttempted++;
    secureConsoleChromeV34 =
      await secureConsoleAgentV34.browsers.get("chrome");
    counters.connectFulfilled++;
    connectedShape =
      typeof secureConsoleChromeV34 === "object" &&
      secureConsoleChromeV34 !== null &&
      typeof secureConsoleChromeV34.documentation === "function" &&
      typeof secureConsoleChromeV34.tabs?.selected === "function";
    if (!connectedShape) throw new Error("FreshChromeShapeError");

    counters.documentationAttempted++;
    const documentation = await secureConsoleChromeV34.documentation();
    counters.documentationFulfilled++;
    documentationValidated =
      typeof documentation === "string" &&
      documentation.length >= 1000 &&
      documentation.length <= 1000000;
    documentationLength =
      documentationValidated ? documentation.length : -1;
    if (!documentationValidated) {
      throw new Error("FreshChromeDocumentationShapeError");
    }
    counters.documentationWriteAttempted++;
    nodeRepl.write(documentation);
    counters.documentationWriteFulfilled++;

    secureConsoleV34AttachmentExact =
      declarationShape &&
      moduleShape &&
      agentShape &&
      connectedShape &&
      documentationValidated &&
      counters.importAttempted === 1 &&
      counters.importFulfilled === 1 &&
      counters.setupAttempted === 1 &&
      counters.setupFulfilled === 1 &&
      counters.connectAttempted === 1 &&
      counters.connectFulfilled === 1 &&
      counters.documentationAttempted === 1 &&
      counters.documentationFulfilled === 1 &&
      counters.documentationWriteAttempted === 1 &&
      counters.documentationWriteFulfilled === 1;
    if (!secureConsoleV34AttachmentExact) {
      throw new Error("FreshChromeAttachmentCompletenessError");
    }
    secureConsoleV34AttachmentState = "V34_ATTACHMENT_PASS";
    result = "EXACT_V34_FRESH_CHROME_ATTACHMENT_PASS";
  } catch (error) {
    errorClass = safeErrorClass(error);
    secureConsoleV34AttachmentExact = false;
    secureConsoleV34AttachmentState = "V34_ATTACHMENT_FAILED_STOP";
    secureConsoleChromeV34 = null;
    secureConsoleAgentV34 = null;
    secureConsoleSetupBrowserRuntimeV34 = null;
  }
  counters.writeAttempted++;
  nodeRepl.write({
    result,
    declarationShape,
    moduleShape,
    agentShape,
    connectedShape,
    documentationValidated,
    documentationLength,
    consumed: secureConsoleV34AttachmentConsumed,
    attachmentExact: secureConsoleV34AttachmentExact,
    state: secureConsoleV34AttachmentState,
    ...counters,
    errorClass,
  });
})();
~~~

Call-1 PASS requires exact result
`EXACT_V34_FRESH_CHROME_ATTACHMENT_PASS`, every shape/validation boolean true,
documentation length in `1000..1000000`, every declared attempted/fulfilled
pair `1/1`, consumed/attachmentExact true, state `V34_ATTACHMENT_PASS`,
error class `NONE`, complete documentation output, complete fixed terminal
output, and completed tool status. Anything else spends Call 1 and stops; Call
2 must not be sent.

## Call 2 — sole selected-tab account-home reacquisition

Call 2 is a separate one-shot cell. Its first Node call consumes adoption
before any precondition or selected-tab call. It requires exact Call-1 PASS,
calls `secureConsoleChromeV34.tabs.selected()` once, retains only that exact
existing handle on PASS, performs one read-only navigation to Cloudflare root,
waits once for bounded settlement, validates the private account-home URL, and
returns one fixed page signature. It never creates or closes a tab.

~~~javascript
let secureConsoleOwnedTaskTabV34 = null;
let secureConsoleOwnedTaskTabV34Eligible = false;
let secureConsoleOwnedTaskTabV34State = "UNADOPTED";
let secureConsoleV34AdoptionConsumed = false;
await (async () => {
  const gateWasFresh = secureConsoleV34AdoptionConsumed === false;
  secureConsoleV34AdoptionConsumed = true;
  const counters = {
    selectedAttempted: 0, selectedFulfilled: 0,
    navigationAttempted: 0, navigationFulfilled: 0,
    waitAttempted: 0, waitFulfilled: 0,
    urlAttempted: 0, urlFulfilled: 0,
    snapshotAttempted: 0, snapshotFulfilled: 0,
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
  const trustedSnapshot = (value) => {
    const expected = [
      "hostExact", "accountHomePath", "exactZoneHrefCount",
      "allAnchorCount", "busyCount",
    ].sort();
    if (!plainRecord(value)) return null;
    const actual = Object.keys(value).sort();
    if (actual.length !== expected.length ||
        !actual.every((key, index) => key === expected[index])) return null;
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
  let result = "PRECONDITION_FAIL";
  let declarationShape = false;
  let predecessorExact = false;
  let controllerOwnership = false;
  let tabShape = false;
  let homeUrlValidated = false;
  let snapshotValidated = false;
  let semanticComplete = false;
  let snapshot = null;
  let adopted = null;
  let errorClass = "NONE";
  try {
    declarationShape =
      gateWasFresh === true &&
      typeof secureConsoleAgentV34 === "object" &&
      secureConsoleAgentV34 !== null &&
      typeof secureConsoleChromeV34 === "object" &&
      secureConsoleChromeV34 !== null &&
      typeof secureConsoleChromeV34.tabs?.selected === "function" &&
      typeof secureConsoleV34AttachmentConsumed === "boolean" &&
      typeof secureConsoleV34AttachmentExact === "boolean";
    predecessorExact =
      declarationShape &&
      secureConsoleV34AttachmentConsumed === true &&
      secureConsoleV34AttachmentExact === true &&
      secureConsoleV34AttachmentState === "V34_ATTACHMENT_PASS";
    if (!predecessorExact) {
      throw new Error("FreshSessionPredecessorStateError");
    }

    counters.selectedAttempted++;
    adopted = await secureConsoleChromeV34.tabs.selected();
    counters.selectedFulfilled++;
    controllerOwnership =
      typeof adopted === "object" &&
      adopted !== null &&
      typeof adopted.id === "string" &&
      adopted.id.length > 0 &&
      adopted.id.length <= 512 &&
      !/[\u0000-\u001f\u007f]/.test(adopted.id);
    tabShape =
      controllerOwnership &&
      typeof adopted.goto === "function" &&
      typeof adopted.url === "function" &&
      typeof adopted.playwright?.waitForTimeout === "function" &&
      typeof adopted.playwright?.locator === "function";
    if (!tabShape) throw new Error("SelectedTabOwnershipError");

    counters.navigationAttempted++;
    await adopted.goto("https://dash.cloudflare.com/");
    counters.navigationFulfilled++;
    counters.waitAttempted++;
    await adopted.playwright.waitForTimeout(
      20000,
      { state: "networkidle" },
    );
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
            const url = new URL(
              item.getAttribute("href") || "",
              location.href,
            );
            return url.protocol === "https:" &&
              url.hostname === "dash.cloudflare.com" &&
              url.port === "" &&
              url.username === "" &&
              url.password === "" &&
              new RegExp("^/" + segment + "/mysw\\.me/?$").test(
                url.pathname,
              );
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
      snapshotValidated &&
      snapshot.hostExact === true &&
      snapshot.accountHomePath === true &&
      snapshot.exactZoneHrefCount === 1 &&
      snapshot.allAnchorCount > 0 &&
      snapshot.busyCount === 0;
    if (!semanticComplete) {
      throw new Error("AccountHomeSemanticSignatureError");
    }
    result = "EXACT_V34_SELECTED_ACCOUNT_HOME_REACQUISITION_PASS";
  } catch (error) {
    errorClass = safeErrorClass(error);
  }

  if (result === "EXACT_V34_SELECTED_ACCOUNT_HOME_REACQUISITION_PASS") {
    secureConsoleOwnedTaskTabV34 = adopted;
    secureConsoleOwnedTaskTabV34Eligible = true;
    secureConsoleOwnedTaskTabV34State =
      "V34_ACCOUNT_HOME_READY_ELIGIBLE";
  } else {
    secureConsoleOwnedTaskTabV34 = null;
    secureConsoleOwnedTaskTabV34Eligible = false;
    secureConsoleOwnedTaskTabV34State =
      "V34_REACQUISITION_OR_READINESS_FAILED";
    secureConsoleChromeV34 = null;
    secureConsoleAgentV34 = null;
    secureConsoleSetupBrowserRuntimeV34 = null;
  }
  counters.writeAttempted++;
  nodeRepl.write({
    result,
    declarationShape,
    predecessorExact,
    controllerOwnership,
    tabShape,
    homeUrlValidated,
    snapshotValidated,
    semanticComplete,
    snapshot,
    selectedAttempted: counters.selectedAttempted,
    selectedFulfilled: counters.selectedFulfilled,
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
    consumed: secureConsoleV34AdoptionConsumed,
    bindingEligible: secureConsoleOwnedTaskTabV34Eligible,
    bindingNull: secureConsoleOwnedTaskTabV34 === null,
    bindingState: secureConsoleOwnedTaskTabV34State,
  });
})();
~~~

Call-2 PASS requires exact result
`EXACT_V34_SELECTED_ACCOUNT_HOME_REACQUISITION_PASS`, every validation and
semantic boolean true, fixed snapshot shape, exact zone href count `1`,
positive anchor count, busy count `0`, every declared attempted/fulfilled
pair `1/1`, error class `NONE`, consumed/bindingEligible true, bindingNull
false, and state `V34_ACCOUNT_HOME_READY_ELIGIBLE`. Anything else spends Call
2, clears every V34 controller/owner binding, and stops. Never retry either
call.

## Prohibited actions and confirmation boundary

Neither call may use `browsers.list`, `getDefault`, `getForUrl`,
`get("extension")`, `tabs.list`, `tabs.get`, `tabs.new`, a second
selection, reconnect, retry, fallback, alternate browser, profile inspection,
screenshot, DOM serialization, clipboard, click, press, fill, Create, edit,
delete, provider mutation, process start, VM mutation, proxy/routing change, or
credential action.

Call 2 navigates the already selected task tab but does not create or close it.
The only retained state on PASS is the exact V34 runtime/controller and selected
tab handle. The final Create/native Copy/native masked Paste confirmation and
the later separate exact-row deletion confirmation remain mandatory and
unreached.

## Review and action-time gates

Before Call 1:

- commit this exact brief alone and pin its bytes, SHA-256, blob, and both
  normalized executable cells;
- obtain independent Sol High PASS with zero unresolved Critical, HIGH, or
  IMPORTANT findings;
- commit a non-self-referential classification directly parented to that PASS
  review and record the post-commit coordinator tuple;
- revalidate exact current module/API bytes, stable projection, empty index,
  exact 12-path dirty product baseline, clean evidence worktree, zero
  temporary/process residue, VM1205 safe checkpoint, absent public DNS, the
  owner's exact profile/window/tab confirmation, fresh Node realm, and absent
  V34 declarations; and
- extract Call 1 from the committed brief and require its exact reviewed bytes
  and SHA-256 before the sole Node call.

After exact Call-1 PASS and before Call 2, require the same immutable local,
runtime, worktree, residue, VM, DNS, and profile confirmation pins; exact
persistent Call-1 counters/state; absent Call-2 declarations; and exact
extracted Call-2 bytes/SHA-256.

A failed, uncertain, malformed, incomplete, or residue-bearing result consumes
that call and stops. Do not retry, continue, reinterpret, reconnect, fall back,
relax a verdict, or manually integrate.
