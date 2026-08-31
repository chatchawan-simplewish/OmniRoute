# Task 19 OmniRoute copy-button clipboard preflight v10 brief

Status: fresh static candidate. `authorizes_live_execution=false`.

This is a new one-shot non-secret local copy-button preflight, not a retry,
continuation, fallback, or override of v9 or any consumed gate. It preserves
v9's reviewed loopback request handling, sticky uncertainty, exact tab/server
cleanup, forced connection teardown, and corrected bundled PowerShell child.
It replaces keyboard selection and `Control+C` with one semantic Playwright
click on one local HTML button whose synchronous handler invokes
`navigator.clipboard.writeText` exactly once.

## Pins, APIs, and future artifacts

- current base / Task 18 cleanup PASS classification commit:
  `9dfad4dc3de78b92c963f8378ddd63eebf76de7d`;
- Task 18 classification: `4441` bytes / SHA-256
  `C6A32F8620FA44284AEA3B800D1CF47548E42DC31582A045BC88CE2B09EE5ECA`;
- proven v9 pattern commit
  `4a5c6e83a1fd7e44556fd1352698b3854f6a5ca9`: `31149` bytes /
  SHA-256
  `2F39D6128A09EFE8D8C3CAEC1587ABAA469539D88CACD1C521BC0CB0F15C1FBD`;
- installed browser API: `58477` bytes / SHA-256
  `4BFEB97E958025DB37D52AEA11B75BC70BCA417B4995B0F711C0F07F3DDCCB08`;
- installed browser module: `149210` bytes / SHA-256
  `C52BA09202F0E82CAA6F6D2A6463A8635C1B1316567975D9B91C1A05FB5AF501`;
- bundled Node executable:
  `C:/Users/chatc/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe`,
  version `v24.19.0`, file version `24.19.0`, `92825416` bytes, SHA-256
  `3602F2BB1A10F2CBAB4C36886218A33C1AB3DB87290E73B033C46C77147D0237`;
- bundled PowerShell executable:
  `C:/Users/chatc/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/powershell/pwsh.exe`,
  file version `7.6.4.500`, `301368` bytes, SHA-256
  `DB6DD81183FE57D22E03B911EC9A30A2FD7C40542E97743615355A6FB44F458F`.

Action-time pins must re-prove the exact runtime, API, module, evidence, and
authority bytes. Exact Node `v24.19.0` must still expose callable
`http.Server.prototype.closeIdleConnections` and `closeAllConnections`. The
browser API must still expose `Browser.nameSession`, `Tabs.new`, `Tab.goto`,
`PlaywrightPage.getByLabel`, `PlaywrightPage.getByText`,
`PlaywrightLocator.click`, `PlaywrightLocator.waitFor`, and `Tab.close` with the
reviewed declarations.

The only future report path is
`.superpowers/sdd/2026-08-31-omniroute-secure-console-transfer/task-19-v10-copy-button-preflight-live-report.md`.
The only future classification path is
`.superpowers/sdd/2026-08-31-omniroute-secure-console-transfer/task-19-v10-copy-button-preflight-classification.md`.
Both remain redacted and set `authorizes_live_execution=false`.

## Authority and immutable boundary

Standing unattended authority applies only after independent direct-byte PASS
and action-time verification of exact pins, empty Git index, unchanged exact
12-path dirty source baseline, the same connected non-null
`residualV5Chrome`, zero intervening live action, and never-declared fresh v10
bindings.

Calls are strictly serial and stop at first failure. Any invocation, rejection,
timeout, missing/malformed output, or uncertainty spends the gate. No retry,
fallback, override, continuation, reconnect, enumeration, alternate tab,
second child, later cleanup, or verdict relaxation exists. Call 2 uses one
60000 ms control timeout. Call 3's sole child uses its exact 30000 ms deadline.

No output includes the challenge, clipboard value, HTML, URL, port, request
path, tab handle/ID/title/URL, page content/metadata, exception message/stack,
credential, key, or token. There is no direct `Tab.clipboard` API, keyboard
press, DOM/page-content serialization, screenshot, CUA, external URL, data URL
navigation, token-page inspection, credential action, or routing authority.
The server binds only `127.0.0.1` on one fresh ephemeral port.

## Call 1 — clear and prove the Windows clipboard empty

Run this exact PowerShell 7 block once. Anything except exit 0 and the exact
success fields stops the contract.

```powershell
$ErrorActionPreference = 'Stop'
$clearAttempted = 0
$clearFulfilled = 0
$readAttempted = 0
$readFulfilled = 0
$empty = $false
$errorClass = 'NONE'
try {
    $clearAttempted++
    Set-Clipboard -Value ''
    $clearFulfilled++
    $readAttempted++
    $value = [string](Get-Clipboard -Raw)
    $readFulfilled++
    $empty = $value.Length -eq 0
} catch {
    $name = $_.Exception.GetType().Name
    $errorClass = if ($name -cmatch '^[A-Za-z][A-Za-z0-9_.-]{0,63}$') { $name } else { 'ERROR' }
} finally {
    $value = $null
}
'PREFLIGHT_V10_BASELINE_CLEAR_ATTEMPTED=' + $clearAttempted
'PREFLIGHT_V10_BASELINE_CLEAR_FULFILLED=' + $clearFulfilled
'PREFLIGHT_V10_BASELINE_READ_ATTEMPTED=' + $readAttempted
'PREFLIGHT_V10_BASELINE_READ_FULFILLED=' + $readFulfilled
'PREFLIGHT_V10_BASELINE_EMPTY=' + $empty.ToString().ToUpperInvariant()
'PREFLIGHT_V10_BASELINE_ERROR=' + $errorClass
if ($clearAttempted -eq 1 -and $clearFulfilled -eq 1 -and $readAttempted -eq 1 -and $readFulfilled -eq 1 -and $empty -and $errorClass -eq 'NONE') { exit 0 }
exit 2
```

Exact Call 1 success requires clear/read `1 / 1`, empty true, error `NONE`, and
exit 0. Anything else forbids Call 2.

## Call 2 — one local copy button and exact tab/server cleanup

Run this exact JavaScript cell once with `timeout_ms=60000` in the persistent
session owning `residualV5Chrome`.

```javascript
let copyButtonPreflightV10ExpectedChallenge = null;
let copyButtonPreflightV10Call3Eligible = false;
let copyButtonPreflightV10RetainedTab = null;
await (async () => {
  const safeErrorClass = (error, fallback) => {
    const name = typeof error?.name === "string" ? error.name : "";
    return /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(name) ? name : fallback;
  };
  const counters = {
    sessionNameAttempted: 0, sessionNameFulfilled: 0,
    serverStartAttempted: 0, serverStartFulfilled: 0,
    mainRequestAttempted: 0, mainRequestFulfilled: 0,
    mainResponseAttempted: 0, mainResponseFulfilled: 0,
    faviconRequestAttempted: 0, faviconRequestFulfilled: 0,
    faviconResponseAttempted: 0, faviconResponseFulfilled: 0,
    unexpectedRequestAttempted: 0,
    browserOpenAttempted: 0, browserOpenFulfilled: 0,
    browserGotoAttempted: 0, browserGotoFulfilled: 0,
    buttonLocatorAttempted: 0, buttonLocatorFulfilled: 0,
    buttonClickAttempted: 0, buttonClickFulfilled: 0,
    statusLocatorAttempted: 0, statusLocatorFulfilled: 0,
    statusWaitAttempted: 0, statusWaitFulfilled: 0,
    browserCloseAttempted: 0, browserCloseFulfilled: 0,
    closeIdleAttempted: 0, closeIdleFulfilled: 0,
    closeAllAttempted: 0, closeAllFulfilled: 0,
    serverCloseAttempted: 0, serverCloseFulfilled: 0
  };
  let result = "PRECONDITION_FAILED";
  let errorClass = "NONE";
  let challenge = null;
  let challengeShape = false;
  let challengeLength = 0;
  let tabState = "NOT_ATTEMPTED";
  let serverState = "NOT_CREATED";
  let server = null;
  let sessionNameUncertain = false;
  let browserCallUnsettled = false;
  let browserUncertain = false;
  let serverUncertain = false;
  const markServerUncertain = (state) => {
    serverUncertain = true;
    serverState = state;
  };
  try {
    if (typeof residualV5Chrome !== "object" || residualV5Chrome === null || typeof residualV5Chrome.nameSession !== "function" || typeof residualV5Chrome.tabs?.new !== "function") {
      throw new Error("ResidualChromeBindingError");
    }
    counters.sessionNameAttempted++;
    sessionNameUncertain = true;
    result = "SESSION_NAME_UNCERTAIN";
    await residualV5Chrome.nameSession("omniroute-v10-copy-button");
    counters.sessionNameFulfilled++;
    sessionNameUncertain = false;
    const { randomBytes } = await import("node:crypto");
    const { createServer } = await import("node:http");
    challenge = `OMNI-PREFLIGHT-V10-${randomBytes(16).toString("hex").toUpperCase()}`;
    const requestPath = `/omni-preflight-v10-${randomBytes(16).toString("hex")}`;
    const buttonName = "Copy OmniRoute V10 challenge";
    challengeShape = /^OMNI-PREFLIGHT-V10-[0-9A-F]{32}$/.test(challenge);
    challengeLength = challenge.length;
    const html = `<!doctype html><html><head><meta charset="utf-8"><link rel="icon" href="data:,"><title>OmniRoute V10</title></head><body><button id="copy" aria-label="${buttonName}">Copy</button><output id="status" aria-label="Copy status"></output><script>(()=>{const button=document.getElementById("copy");const status=document.getElementById("status");button.addEventListener("click",()=>{button.disabled=true;navigator.clipboard.writeText("${challenge}").then(()=>{status.textContent="COPIED";},()=>{status.textContent="FAILED";});},{once:true});})();<\/script></body></html>`;
    const attachLifecycle = (request, response, responseKind) => {
      request.once("aborted", () => markServerUncertain("REQUEST_UNCERTAIN"));
      request.once("error", () => markServerUncertain("REQUEST_UNCERTAIN"));
      response.once("finish", () => {
        if (responseKind === "MAIN") counters.mainResponseFulfilled++;
        else counters.faviconResponseFulfilled++;
      });
      response.once("error", () => markServerUncertain("RESPONSE_UNCERTAIN"));
      response.once("close", () => {
        if (!response.writableFinished) markServerUncertain("RESPONSE_UNCERTAIN");
      });
    };
    server = createServer((request, response) => {
      if (request.method === "GET" && request.url === requestPath) {
        counters.mainRequestAttempted++;
        if (counters.mainRequestAttempted !== 1) {
          markServerUncertain("DUPLICATE_MAIN_REQUEST");
          response.writeHead(409, { "Cache-Control": "no-store", "Content-Length": "0", "Content-Type": "text/plain; charset=utf-8", "Referrer-Policy": "no-referrer", "X-Content-Type-Options": "nosniff" });
          response.end();
          return;
        }
        counters.mainRequestFulfilled++;
        counters.mainResponseAttempted++;
        attachLifecycle(request, response, "MAIN");
        response.writeHead(200, { "Cache-Control": "no-store", "Content-Type": "text/html; charset=utf-8", "Permissions-Policy": "clipboard-write=(self)", "Referrer-Policy": "no-referrer", "X-Content-Type-Options": "nosniff" });
        response.end(html);
        return;
      }
      if (request.method === "GET" && request.url === "/favicon.ico") {
        counters.faviconRequestAttempted++;
        if (counters.faviconRequestAttempted !== 1) {
          markServerUncertain("DUPLICATE_FAVICON_REQUEST");
          response.writeHead(409, { "Cache-Control": "no-store", "Content-Length": "0", "Content-Type": "text/plain; charset=utf-8", "Referrer-Policy": "no-referrer", "X-Content-Type-Options": "nosniff" });
          response.end();
          return;
        }
        counters.faviconRequestFulfilled++;
        counters.faviconResponseAttempted++;
        attachLifecycle(request, response, "FAVICON");
        response.writeHead(204, { "Cache-Control": "no-store", "Content-Length": "0", "Referrer-Policy": "no-referrer", "X-Content-Type-Options": "nosniff" });
        response.end();
        return;
      }
      counters.unexpectedRequestAttempted++;
      markServerUncertain("UNEXPECTED_REQUEST");
      response.writeHead(404, { "Cache-Control": "no-store", "Content-Length": "0", "Content-Type": "text/plain; charset=utf-8", "Referrer-Policy": "no-referrer", "X-Content-Type-Options": "nosniff" });
      response.end();
    });
    if (typeof server.closeAllConnections !== "function" || typeof server.closeIdleConnections !== "function") {
      markServerUncertain("SERVER_TEARDOWN_API_INVALID");
      throw new Error("ServerTeardownApiError");
    }
    server.on("clientError", (_error, socket) => {
      markServerUncertain("CLIENT_ERROR");
      socket.destroy();
    });
    server.on("error", () => markServerUncertain("SERVER_ERROR"));
    counters.serverStartAttempted++;
    serverState = "START_UNCERTAIN";
    await new Promise((resolve, reject) => {
      const onError = (error) => {
        server.off("listening", onListening);
        markServerUncertain("START_UNCERTAIN");
        reject(error);
      };
      const onListening = () => {
        server.off("error", onError);
        resolve();
      };
      server.once("error", onError);
      server.once("listening", onListening);
      server.listen({ host: "127.0.0.1", port: 0, exclusive: true });
    });
    counters.serverStartFulfilled++;
    serverState = "LISTENING";
    const address = server.address();
    if (address === null || typeof address === "string" || address.address !== "127.0.0.1" || address.port < 1) {
      markServerUncertain("INVALID_LISTENER_ADDRESS");
      throw new Error("LoopbackAddressError");
    }
    const url = `http://127.0.0.1:${address.port}${requestPath}`;
    tabState = "OPEN_UNCERTAIN";
    browserCallUnsettled = true;
    counters.browserOpenAttempted++;
    const tab = await residualV5Chrome.tabs.new();
    counters.browserOpenFulfilled++;
    browserCallUnsettled = false;
    copyButtonPreflightV10RetainedTab = tab;
    tabState = "OPEN";
    if (tab === null || (typeof tab !== "object" && typeof tab !== "function") || typeof tab.goto !== "function" || typeof tab.playwright?.getByLabel !== "function" || typeof tab.playwright?.getByText !== "function" || typeof tab.close !== "function") {
      result = "TAB_API_INVALID";
      throw new Error("TabApiError");
    }
    tabState = "GOTO_UNCERTAIN";
    browserCallUnsettled = true;
    counters.browserGotoAttempted++;
    await copyButtonPreflightV10RetainedTab.goto(url);
    counters.browserGotoFulfilled++;
    browserCallUnsettled = false;
    tabState = "LOADED";
    if (serverUncertain || counters.mainRequestAttempted !== 1 || counters.mainRequestFulfilled !== 1 || counters.mainResponseAttempted !== 1 || counters.mainResponseFulfilled !== 1) {
      markServerUncertain("INVALID_MAIN_EXCHANGE_LIFECYCLE");
      throw new Error("ServerExchangeError");
    }
    tabState = "BUTTON_LOCATOR_UNCERTAIN";
    browserCallUnsettled = true;
    counters.buttonLocatorAttempted++;
    const button = copyButtonPreflightV10RetainedTab.playwright.getByLabel(buttonName, { exact: true });
    if (button === null || (typeof button !== "object" && typeof button !== "function") || typeof button.click !== "function") {
      result = "BUTTON_LOCATOR_API_INVALID";
      throw new Error("ButtonLocatorApiError");
    }
    counters.buttonLocatorFulfilled++;
    browserCallUnsettled = false;
    tabState = "BUTTON_LOCATED";
    if (serverUncertain) throw new Error("ServerStateError");
    tabState = "BUTTON_CLICK_UNCERTAIN";
    browserCallUnsettled = true;
    counters.buttonClickAttempted++;
    await button.click({ timeoutMs: 5000 });
    counters.buttonClickFulfilled++;
    browserCallUnsettled = false;
    tabState = "BUTTON_CLICKED";
    if (serverUncertain) throw new Error("ServerStateError");
    tabState = "STATUS_LOCATOR_UNCERTAIN";
    browserCallUnsettled = true;
    counters.statusLocatorAttempted++;
    const copiedStatus = copyButtonPreflightV10RetainedTab.playwright.getByText("COPIED", { exact: true });
    if (copiedStatus === null || (typeof copiedStatus !== "object" && typeof copiedStatus !== "function") || typeof copiedStatus.waitFor !== "function") {
      result = "STATUS_LOCATOR_API_INVALID";
      throw new Error("StatusLocatorApiError");
    }
    counters.statusLocatorFulfilled++;
    browserCallUnsettled = false;
    tabState = "STATUS_LOCATED";
    tabState = "STATUS_WAIT_UNCERTAIN";
    browserCallUnsettled = true;
    counters.statusWaitAttempted++;
    await copiedStatus.waitFor({ state: "visible", timeoutMs: 5000 });
    counters.statusWaitFulfilled++;
    browserCallUnsettled = false;
    tabState = "COPY_CONFIRMED";
    if (serverUncertain) throw new Error("ServerStateError");
    tabState = "CLOSE_UNCERTAIN";
    browserCallUnsettled = true;
    counters.browserCloseAttempted++;
    await copyButtonPreflightV10RetainedTab.close();
    counters.browserCloseFulfilled++;
    browserCallUnsettled = false;
    copyButtonPreflightV10RetainedTab = null;
    tabState = "CLOSED";
    result = "BROWSER_SETTLED_PENDING_SERVER_CLOSE";
  } catch (error) {
    errorClass = safeErrorClass(error, "ERROR");
    browserUncertain = browserUncertain || sessionNameUncertain || browserCallUnsettled || tabState.endsWith("_UNCERTAIN");
    if (result !== "TAB_API_INVALID" && result !== "BUTTON_LOCATOR_API_INVALID" && result !== "STATUS_LOCATOR_API_INVALID") result = browserUncertain ? "BROWSER_UNCERTAIN" : "SERVER_OR_PRECONDITION_UNCERTAIN";
  } finally {
    if (server !== null && server.listening) {
      serverState = "CLOSE_UNCERTAIN";
      counters.closeIdleAttempted++;
      try {
        server.closeIdleConnections();
        counters.closeIdleFulfilled++;
      } catch (error) {
        if (errorClass === "NONE") errorClass = safeErrorClass(error, "SERVER_TEARDOWN_ERROR");
        markServerUncertain("CLOSE_IDLE_UNCERTAIN");
      }
      counters.closeAllAttempted++;
      try {
        server.closeAllConnections();
        counters.closeAllFulfilled++;
      } catch (error) {
        if (errorClass === "NONE") errorClass = safeErrorClass(error, "SERVER_TEARDOWN_ERROR");
        markServerUncertain("CLOSE_ALL_UNCERTAIN");
      }
      counters.serverCloseAttempted++;
      try {
        await new Promise((resolve, reject) => server.close((error) => error ? reject(error) : resolve()));
        counters.serverCloseFulfilled++;
        if (server.listening) markServerUncertain("RESIDUAL_LISTENER");
        serverState = server.listening ? "RESIDUAL_LISTENER" : (serverUncertain ? "CLOSED_AFTER_UNCERTAINTY" : "CLOSED");
      } catch (error) {
        if (errorClass === "NONE") errorClass = safeErrorClass(error, "SERVER_CLOSE_ERROR");
        markServerUncertain("CLOSE_UNCERTAIN");
      }
    } else if (server !== null && serverState !== "CLOSED") {
      markServerUncertain(server.listening ? "RESIDUAL_LISTENER" : "NOT_LISTENING_UNPROVEN_CLOSE");
    }
    const exactRequiredCounters = [
      counters.sessionNameAttempted, counters.sessionNameFulfilled,
      counters.serverStartAttempted, counters.serverStartFulfilled,
      counters.mainRequestAttempted, counters.mainRequestFulfilled,
      counters.mainResponseAttempted, counters.mainResponseFulfilled,
      counters.browserOpenAttempted, counters.browserOpenFulfilled,
      counters.browserGotoAttempted, counters.browserGotoFulfilled,
      counters.buttonLocatorAttempted, counters.buttonLocatorFulfilled,
      counters.buttonClickAttempted, counters.buttonClickFulfilled,
      counters.statusLocatorAttempted, counters.statusLocatorFulfilled,
      counters.statusWaitAttempted, counters.statusWaitFulfilled,
      counters.browserCloseAttempted, counters.browserCloseFulfilled,
      counters.closeIdleAttempted, counters.closeIdleFulfilled,
      counters.closeAllAttempted, counters.closeAllFulfilled,
      counters.serverCloseAttempted, counters.serverCloseFulfilled
    ].every((value) => value === 1);
    const exactOptionalFavicon =
      (counters.faviconRequestAttempted === 0 && counters.faviconRequestFulfilled === 0 && counters.faviconResponseAttempted === 0 && counters.faviconResponseFulfilled === 0) ||
      (counters.faviconRequestAttempted === 1 && counters.faviconRequestFulfilled === 1 && counters.faviconResponseAttempted === 1 && counters.faviconResponseFulfilled === 1);
    const exactTabClosed = tabState === "CLOSED" && copyButtonPreflightV10RetainedTab === null;
    const exactServerClosed = serverState === "CLOSED" && server !== null && server.listening === false;
    const exact = result === "BROWSER_SETTLED_PENDING_SERVER_CLOSE" && errorClass === "NONE" && challengeShape && challengeLength === 51 && exactRequiredCounters && exactOptionalFavicon && counters.unexpectedRequestAttempted === 0 && exactTabClosed && exactServerClosed && !sessionNameUncertain && !browserCallUnsettled && !browserUncertain && !serverUncertain;
    if (exact) {
      copyButtonPreflightV10ExpectedChallenge = challenge;
      copyButtonPreflightV10Call3Eligible = true;
      result = "COPY_BUTTON_SETTLED_TAB_AND_SERVER_CLOSED";
    } else {
      copyButtonPreflightV10Call3Eligible = false;
    }
    nodeRepl.write({ result, errorClass, challengeShape, challengeLength, counters, tabState, exactTabClosed, retainedTabBinding: copyButtonPreflightV10RetainedTab !== null, serverState, serverListening: server?.listening === true, serverUncertain, browserCallUnsettled, browserUncertain, sessionNameUncertain });
  }
})();
```

Exact Call 2 success requires result
`COPY_BUTTON_SETTLED_TAB_AND_SERVER_CLOSED`, error `NONE`, challenge shape true
and length 51, every required counter pair `1 / 1`, favicon counters
all zero or all one, unexpected requests zero, exact tab and server closed,
listener false, retained tab binding false, and every uncertainty flag false.
The handler is registered once, disables the button synchronously, calls
`navigator.clipboard.writeText` exactly once, and exposes only `COPIED` or
`FAILED`; it never exposes the challenge or its length. The contract performs
one semantic button click and waits only for safe exact `COPIED` visibility.

Duplicate main/favicon, any other method/path, request/response/client/server
error, invalid lifecycle, or teardown error makes server uncertainty sticky.
`closeIdleConnections()` and `closeAllConnections()` occur before directly
awaited `server.close()`. Successful close never clears prior uncertainty.
Only exact success publishes the lexical challenge and enables Call 3.

## Call 3 — consume eligibility, compare once, clear, and prove empty

Run this exact JavaScript cell once only after exact Call 2 success.
Eligibility is consumed before the sole child attempt. The challenge is passed
only through child stdin, retained on every failure, and nulled only after
fully validated exact child success.

```javascript
await (async () => {
  const result = { result: "HANDOFF_UNCERTAIN_RETAINED_BINDING", errorClass: "NONE", childStartAttempted: 0, childExitFulfilled: 0, childExitCode: null, stdoutSchemaValid: false, comparison: null, challengeBindingRetained: copyButtonPreflightV10ExpectedChallenge !== null };
  const safeClass = (value, fallback) => /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(value) ? value : fallback;
  const consumedEligibility = copyButtonPreflightV10Call3Eligible === true;
  copyButtonPreflightV10Call3Eligible = false;
  if (!consumedEligibility || typeof copyButtonPreflightV10ExpectedChallenge !== "string" || !/^OMNI-PREFLIGHT-V10-[0-9A-F]{32}$/.test(copyButtonPreflightV10ExpectedChallenge) || copyButtonPreflightV10ExpectedChallenge.length !== 51) {
    result.result = "HANDOFF_BINDING_INVALID_RETAINED_AS_FOUND";
    result.challengeBindingRetained = copyButtonPreflightV10ExpectedChallenge !== null;
    nodeRepl.write(result);
    return;
  }
  let spawnSync;
  try { ({ spawnSync } = await import("node:child_process")); }
  catch (error) {
    result.errorClass = safeClass(typeof error?.name === "string" ? error.name : "", "IMPORT_ERROR");
    result.result = "CHILD_IMPORT_UNCERTAIN_RETAINED_BINDING";
    result.challengeBindingRetained = true;
    nodeRepl.write(result);
    return;
  }
  const script = String.raw`$ErrorActionPreference = 'Stop'
$handoffReads=0; $comparisonReads=0; $comparisonMatch=$false; $observedShape=$false; $observedLength=-1; $comparisonError='NONE'
$finalClearAttempted=0; $finalClearFulfilled=0; $finalReadAttempted=0; $finalReadFulfilled=0; $finalEmpty=$false; $cleanupError='NONE'
$expected=$null; $observed=$null; $postClear=$null
try {
    $handoffReads++
    $expected=[Console]::In.ReadLine()
    if ($null -eq $expected -or $expected -cnotmatch '^OMNI-PREFLIGHT-V10-[0-9A-F]{32}$' -or $expected.Length -ne 51) { $comparisonError='HANDOFF_SHAPE_FAIL' }
    else {
        $comparisonReads++
        $observed=[string](Get-Clipboard -Raw)
        $comparisonMatch=$observed -ceq $expected
        $observedShape=$observed -cmatch '^OMNI-PREFLIGHT-V10-[0-9A-F]{32}$'
        $observedLength=$observed.Length
    }
} catch {
    $name=$_.Exception.GetType().Name
    $comparisonError=if ($name -cmatch '^[A-Za-z][A-Za-z0-9_.-]{0,63}$') { $name } else { 'ERROR' }
} finally {
    $finalClearAttempted++
    try { Set-Clipboard -Value ''; $finalClearFulfilled++ } catch { $cleanupError='CLEAR_ERROR' }
    $finalReadAttempted++
    try { $postClear=[string](Get-Clipboard -Raw); $finalReadFulfilled++; $finalEmpty=$postClear.Length -eq 0 } catch { if ($cleanupError -eq 'NONE') { $cleanupError='READ_ERROR' } }
    $expected=$null; $observed=$null; $postClear=$null
}
$pass=$handoffReads -eq 1 -and $comparisonReads -eq 1 -and $comparisonMatch -and $observedShape -and $observedLength -eq 51 -and $comparisonError -eq 'NONE' -and $finalClearAttempted -eq 1 -and $finalClearFulfilled -eq 1 -and $finalReadAttempted -eq 1 -and $finalReadFulfilled -eq 1 -and $finalEmpty -and $cleanupError -eq 'NONE'
'PREFLIGHT_V10_HANDOFF_READS='+$handoffReads
'PREFLIGHT_V10_COMPARISON_READS='+$comparisonReads
'PREFLIGHT_V10_COMPARISON_MATCH='+$comparisonMatch.ToString().ToUpperInvariant()
'PREFLIGHT_V10_OBSERVED_SHAPE='+$observedShape.ToString().ToUpperInvariant()
'PREFLIGHT_V10_OBSERVED_LENGTH='+$observedLength
'PREFLIGHT_V10_COMPARISON_ERROR='+$comparisonError
'PREFLIGHT_V10_FINAL_CLEAR_ATTEMPTED='+$finalClearAttempted
'PREFLIGHT_V10_FINAL_CLEAR_FULFILLED='+$finalClearFulfilled
'PREFLIGHT_V10_FINAL_READ_ATTEMPTED='+$finalReadAttempted
'PREFLIGHT_V10_FINAL_READ_FULFILLED='+$finalReadFulfilled
'PREFLIGHT_V10_FINAL_EMPTY='+$finalEmpty.ToString().ToUpperInvariant()
'PREFLIGHT_V10_CLEANUP_ERROR='+$cleanupError
'PREFLIGHT_V10_RESULT='+$(if($pass){'PASS'}else{'FAIL'})
if($pass){exit 0}; exit 2`;
  result.childStartAttempted = 1;
  let child;
  try {
    child = spawnSync("C:\\Users\\chatc\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe", ["-NoLogo", "-NoProfile", "-NonInteractive", "-EncodedCommand", Buffer.from(script, "utf16le").toString("base64")], {
      shell: false, windowsHide: true, encoding: "utf8", input: `${copyButtonPreflightV10ExpectedChallenge}\n`, timeout: 30000, killSignal: "SIGKILL", maxBuffer: 16384,
      env: { SystemRoot: "C:\\Windows", WINDIR: "C:\\Windows" }
    });
  } catch (error) {
    result.errorClass = safeClass(typeof error?.name === "string" ? error.name : "", "CHILD_ERROR");
    result.result = "CHILD_SPAWN_UNCERTAIN_RETAINED_BINDING";
    result.challengeBindingRetained = true;
    nodeRepl.write(result);
    return;
  }
  const childError = typeof child.error?.code === "string" ? child.error.code : (typeof child.error?.name === "string" ? child.error.name : "NONE");
  result.errorClass = safeClass(childError, "CHILD_ERROR");
  result.childExitCode = Number.isInteger(child.status) ? child.status : null;
  result.childExitFulfilled = child.error === undefined && child.signal === null && Number.isInteger(child.status) ? 1 : 0;
  const stdout = typeof child.stdout === "string" ? child.stdout : "";
  const stderr = typeof child.stderr === "string" ? child.stderr : "";
  const lines = stdout.split(/\r?\n/); if (lines.at(-1) === "") lines.pop();
  const keys = ["PREFLIGHT_V10_HANDOFF_READS","PREFLIGHT_V10_COMPARISON_READS","PREFLIGHT_V10_COMPARISON_MATCH","PREFLIGHT_V10_OBSERVED_SHAPE","PREFLIGHT_V10_OBSERVED_LENGTH","PREFLIGHT_V10_COMPARISON_ERROR","PREFLIGHT_V10_FINAL_CLEAR_ATTEMPTED","PREFLIGHT_V10_FINAL_CLEAR_FULFILLED","PREFLIGHT_V10_FINAL_READ_ATTEMPTED","PREFLIGHT_V10_FINAL_READ_FULFILLED","PREFLIGHT_V10_FINAL_EMPTY","PREFLIGHT_V10_CLEANUP_ERROR","PREFLIGHT_V10_RESULT"];
  const parsed = {};
  let schema = lines.length === keys.length && Buffer.byteLength(stdout, "utf8") <= 4096 && stderr.length === 0;
  for (let i=0; schema && i<keys.length; i++) {
    const match = /^([A-Z0-9_]+)=([A-Z0-9_-]{1,64})$/.exec(lines[i]);
    if (match === null || match[1] !== keys[i] || Object.hasOwn(parsed, match[1])) schema = false; else parsed[match[1]] = match[2];
  }
  result.stdoutSchemaValid = schema;
  if (schema) result.comparison = { handoffReads:Number(parsed.PREFLIGHT_V10_HANDOFF_READS), comparisonReads:Number(parsed.PREFLIGHT_V10_COMPARISON_READS), comparisonMatch:parsed.PREFLIGHT_V10_COMPARISON_MATCH, observedShape:parsed.PREFLIGHT_V10_OBSERVED_SHAPE, observedLength:Number(parsed.PREFLIGHT_V10_OBSERVED_LENGTH), comparisonError:parsed.PREFLIGHT_V10_COMPARISON_ERROR, finalClearAttempted:Number(parsed.PREFLIGHT_V10_FINAL_CLEAR_ATTEMPTED), finalClearFulfilled:Number(parsed.PREFLIGHT_V10_FINAL_CLEAR_FULFILLED), finalReadAttempted:Number(parsed.PREFLIGHT_V10_FINAL_READ_ATTEMPTED), finalReadFulfilled:Number(parsed.PREFLIGHT_V10_FINAL_READ_FULFILLED), finalEmpty:parsed.PREFLIGHT_V10_FINAL_EMPTY, cleanupError:parsed.PREFLIGHT_V10_CLEANUP_ERROR, powerShellResult:parsed.PREFLIGHT_V10_RESULT };
  const c = result.comparison;
  const exact = result.errorClass === "NONE" && result.childExitFulfilled === 1 && result.childExitCode === 0 && schema && c.handoffReads === 1 && c.comparisonReads === 1 && c.comparisonMatch === "TRUE" && c.observedShape === "TRUE" && c.observedLength === 51 && c.comparisonError === "NONE" && c.finalClearAttempted === 1 && c.finalClearFulfilled === 1 && c.finalReadAttempted === 1 && c.finalReadFulfilled === 1 && c.finalEmpty === "TRUE" && c.cleanupError === "NONE" && c.powerShellResult === "PASS";
  if (exact) {
    copyButtonPreflightV10ExpectedChallenge = null;
    result.challengeBindingRetained = false;
    result.result = "EXACT_MATCH_AND_FINAL_EMPTY";
  } else {
    result.challengeBindingRetained = true;
    result.result = "HANDOFF_OR_COMPARISON_UNCERTAIN_RETAINED_BINDING";
  }
  nodeRepl.write(result);
})();
```

Exact Call 3 success requires result `EXACT_MATCH_AND_FINAL_EMPTY`, error
`NONE`, child start/exit `1 / 1`, exit 0, exact ordered bounded stdout schema,
one handoff read, one comparison read, exact internal equality, observed shape
true and length 51, final
clear/read `1 / 1`, final empty true, both error labels `NONE`, and retained
challenge binding false. Every failure or uncertainty retains the binding and
permits no second child or later browser/clipboard mutation.

## Proof boundary and static acceptance

A v10 PASS proves only that this fresh local loopback DOM button path invoked
the browser Clipboard API and produced an exact Windows clipboard match, then
proved final empty cleanup. It can support a later credential gate only if the
Cloudflare copy control is separately verified, under a new non-secret and
independently reviewed contract, to use the same mechanism. V10 authorizes no
Cloudflare/token-page inspection, credential capture, credential entry,
provider change, permission change, or routing action.

Independent review must verify UTF-8/LF bytes, non-evaluating PowerShell and
JavaScript syntax, exact runtime/API pins, fresh bindings, one synchronous
button handler, exactly one `navigator.clipboard.writeText` occurrence, one
semantic button click, one exact `COPIED` locator wait, zero keyboard press,
zero direct tab clipboard API, zero page-content serialization/screenshots,
unique main and optional favicon routing, sticky uncertainty, forced teardown
before awaited server close, lexical-only challenge publication, eligibility
consumption, failure retention, success-only null, redaction, and operation
cardinality/order. It must verify index 0, baseline 12, exact-path diff, and no
external URL, CUA, enumeration, retry, credential, token, or routing action.

The v9 transport remains failed/not proven and older residuals remain
`NOT PROVEN`. This brief authorizes no live execution; independent PASS and
exact action-time pins remain mandatory.
