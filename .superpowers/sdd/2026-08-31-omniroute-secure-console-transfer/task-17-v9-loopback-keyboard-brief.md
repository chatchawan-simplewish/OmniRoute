# Task 17 OmniRoute loopback Windows clipboard preflight v9 brief

Status: fresh static candidate. `authorizes_live_execution=false`.

This is a new one-shot non-secret loopback keyboard preflight, not a retry,
continuation, fallback, or override of v5, v8, or any consumed gate. It combines
only independently reviewed patterns: v5's unique favicon-aware loopback
handler, v8's explicit locator timeouts and retained-tab lifecycle, v7's
corrected bundled PowerShell comparison child, and Task 16's proven v8 exact-tab
cleanup. Old listener/process residuals remain untouched and `NOT PROVEN`.

## Pins, runtime APIs, and future report

- current base / Task 16 PASS classification commit:
  `a9632463a94371d2556fe8f7b4de928461c4eab2`;
- Task 16 classification: `4254` bytes / SHA-256
  `4394B488F07B4AEA28B29ADCE9A1B42051B15A3D2BA7CCC18F89E22B995A2775`;
- proven v5 loopback pattern commit
  `f31cbc18b10d132e14909b09acb4047a18248fff`: `26264` bytes /
  SHA-256
  `C5C6C9A699253AB1D3C2D5D50C0E68D1B3F03C09A5865B82DE3B6021F42E9476`;
- proven v8 keyboard pattern commit
  `bb37efde0705001e892344fe7c6437a4c66f9a14`: `23152` bytes /
  SHA-256
  `075DE9C7BFCE48088D1E75C401CCBB455EBBA9786889044A19E6D9C749637508`;
- corrected v7 child pattern commit
  `a2b887bb4fad01343b5d2957a27363ee877c7c72`: `20581` bytes /
  SHA-256
  `9B84E07C0F6B5B3CBAEB0BD8A67B9D81139921F49011B113BC80D46D7285FDC9`;
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

Static host evidence under exact Node `v24.19.0` proves
`typeof http.Server.prototype.closeAllConnections === "function"` and
`typeof http.Server.prototype.closeIdleConnections === "function"`.
Action-time pins must reproduce both results and the exact runtime bytes before
Call 1. The installed browser API must still expose `Browser.nameSession`,
`Tabs.new`, `Tab.goto`, `PlaywrightPage.getByLabel`,
`PlaywrightLocator.click`, `PlaywrightLocator.press`, and `Tab.close` with the
reviewed declarations.

The future report path is
`.superpowers/sdd/2026-08-31-omniroute-secure-console-transfer/task-17-v9-loopback-keyboard-live-report.md`.
It remains redacted and sets `authorizes_live_execution=false`.

## Authority and immutable boundary

Standing unattended authority may permit the sole Sol High owner to consume
this fresh gate only after independent direct-byte PASS and action-time proof
of exact brief/review/evidence/API/module/runtime/authority pins, empty Git
index, unchanged exact 12-path source baseline, same connected non-null
`residualV5Chrome`, zero intervening live action, and never-declared fresh v9
bindings.

Calls are strictly serial and stop at first failure. Any invocation, rejection,
timeout, missing/malformed output, or uncertainty spends the gate. No retry,
fallback, override, continuation, reconnect, enumeration, alternate tab,
second child, later cleanup, or verdict relaxation exists. Invoke the sole
Call 2 control operation with `timeout_ms=60000`; its internal browser actions
remain individually bounded as written. Call 3's child deadline is 30000 ms.

No output includes challenge, clipboard value, HTML, URL, port, request path,
tab handle/ID/title/URL, content/metadata, exception message/stack, credential,
key, or token. The server binds only `127.0.0.1` on one fresh ephemeral port.
No external URL/transmission, native tab clipboard API, data URL navigation,
CUA, credential action, or routing authority exists.

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
'PREFLIGHT_V9_BASELINE_CLEAR_ATTEMPTED=' + $clearAttempted
'PREFLIGHT_V9_BASELINE_CLEAR_FULFILLED=' + $clearFulfilled
'PREFLIGHT_V9_BASELINE_READ_ATTEMPTED=' + $readAttempted
'PREFLIGHT_V9_BASELINE_READ_FULFILLED=' + $readFulfilled
'PREFLIGHT_V9_BASELINE_EMPTY=' + $empty.ToString().ToUpperInvariant()
'PREFLIGHT_V9_BASELINE_ERROR=' + $errorClass
if ($clearAttempted -eq 1 -and $clearFulfilled -eq 1 -and $readAttempted -eq 1 -and $readFulfilled -eq 1 -and $empty -and $errorClass -eq 'NONE') { exit 0 }
exit 2
```

Exact Call 1 success requires clear `1 / 1`, read `1 / 1`, empty true, error
`NONE`, and exit 0. Anything else forbids Call 2.

## Call 2 — one loopback document, one keyboard copy, exact cleanup

Run this exact JavaScript cell once under a control timeout of 60000 ms in the
session owning `residualV5Chrome`.

```javascript
let loopbackKeyboardPreflightV9ExpectedChallenge = null;
let loopbackKeyboardPreflightV9Call3Eligible = false;
let loopbackKeyboardPreflightV9RetainedTab = null;
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
    locatorAttempted: 0, locatorFulfilled: 0,
    clickAttempted: 0, clickFulfilled: 0,
    selectAttempted: 0, selectFulfilled: 0,
    copyAttempted: 0, copyFulfilled: 0,
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
    await residualV5Chrome.nameSession("omniroute-v9-loopback-keyboard");
    counters.sessionNameFulfilled++;
    sessionNameUncertain = false;
    const { randomBytes } = await import("node:crypto");
    const { createServer } = await import("node:http");
    challenge = `OMNI-PREFLIGHT-V9-${randomBytes(16).toString("hex").toUpperCase()}`;
    const requestPath = `/omni-preflight-v9-${randomBytes(16).toString("hex")}`;
    const accessibleName = "OmniRoute V9 Challenge";
    const html = `<!doctype html><html><head><meta charset="utf-8"><link rel="icon" href="data:,"><title>OmniRoute V9</title></head><body><label for="challenge">${accessibleName}</label><input id="challenge" value="${challenge}" readonly></body></html>`;
    challengeShape = /^OMNI-PREFLIGHT-V9-[0-9A-F]{32}$/.test(challenge);
    challengeLength = challenge.length;
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
        response.writeHead(200, { "Cache-Control": "no-store", "Content-Type": "text/html; charset=utf-8", "Referrer-Policy": "no-referrer", "X-Content-Type-Options": "nosniff" });
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
    loopbackKeyboardPreflightV9RetainedTab = tab;
    tabState = "OPEN";
    if (tab === null || (typeof tab !== "object" && typeof tab !== "function") || typeof tab.goto !== "function" || typeof tab.playwright?.getByLabel !== "function" || typeof tab.close !== "function") {
      result = "TAB_API_INVALID";
      throw new Error("TabApiError");
    }
    tabState = "GOTO_UNCERTAIN";
    browserCallUnsettled = true;
    counters.browserGotoAttempted++;
    await loopbackKeyboardPreflightV9RetainedTab.goto(url);
    counters.browserGotoFulfilled++;
    browserCallUnsettled = false;
    tabState = "LOADED";
    if (serverUncertain || counters.mainRequestAttempted !== 1 || counters.mainRequestFulfilled !== 1 || counters.mainResponseAttempted !== 1 || counters.mainResponseFulfilled !== 1) {
      markServerUncertain("INVALID_MAIN_EXCHANGE_LIFECYCLE");
      throw new Error("ServerExchangeError");
    }
    tabState = "LOCATOR_UNCERTAIN";
    browserCallUnsettled = true;
    counters.locatorAttempted++;
    const field = loopbackKeyboardPreflightV9RetainedTab.playwright.getByLabel(accessibleName, { exact: true });
    if (field === null || (typeof field !== "object" && typeof field !== "function") || typeof field.click !== "function" || typeof field.press !== "function") {
      result = "LOCATOR_API_INVALID";
      throw new Error("LocatorApiError");
    }
    counters.locatorFulfilled++;
    browserCallUnsettled = false;
    tabState = "LOCATED";
    if (serverUncertain) throw new Error("ServerStateError");
    tabState = "CLICK_UNCERTAIN";
    browserCallUnsettled = true;
    counters.clickAttempted++;
    await field.click({ timeoutMs: 5000 });
    counters.clickFulfilled++;
    browserCallUnsettled = false;
    tabState = "FOCUSED";
    if (serverUncertain) throw new Error("ServerStateError");
    tabState = "SELECT_UNCERTAIN";
    browserCallUnsettled = true;
    counters.selectAttempted++;
    await field.press("Control+A", { timeoutMs: 5000 });
    counters.selectFulfilled++;
    browserCallUnsettled = false;
    tabState = "SELECTED";
    if (serverUncertain) throw new Error("ServerStateError");
    tabState = "COPY_UNCERTAIN";
    browserCallUnsettled = true;
    counters.copyAttempted++;
    await field.press("Control+C", { timeoutMs: 5000 });
    counters.copyFulfilled++;
    browserCallUnsettled = false;
    tabState = "COPIED";
    if (serverUncertain) throw new Error("ServerStateError");
    tabState = "CLOSE_UNCERTAIN";
    browserCallUnsettled = true;
    counters.browserCloseAttempted++;
    await loopbackKeyboardPreflightV9RetainedTab.close();
    counters.browserCloseFulfilled++;
    browserCallUnsettled = false;
    loopbackKeyboardPreflightV9RetainedTab = null;
    tabState = "CLOSED";
    result = "BROWSER_SETTLED_PENDING_SERVER_CLOSE";
  } catch (error) {
    errorClass = safeErrorClass(error, "ERROR");
    browserUncertain = browserUncertain || sessionNameUncertain || browserCallUnsettled || tabState.endsWith("_UNCERTAIN");
    if (result !== "TAB_API_INVALID" && result !== "LOCATOR_API_INVALID") result = browserUncertain ? "BROWSER_UNCERTAIN" : "SERVER_OR_PRECONDITION_UNCERTAIN";
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
      counters.locatorAttempted, counters.locatorFulfilled,
      counters.clickAttempted, counters.clickFulfilled,
      counters.selectAttempted, counters.selectFulfilled,
      counters.copyAttempted, counters.copyFulfilled,
      counters.browserCloseAttempted, counters.browserCloseFulfilled,
      counters.closeIdleAttempted, counters.closeIdleFulfilled,
      counters.closeAllAttempted, counters.closeAllFulfilled,
      counters.serverCloseAttempted, counters.serverCloseFulfilled
    ].every((value) => value === 1);
    const exactOptionalFavicon =
      (counters.faviconRequestAttempted === 0 && counters.faviconRequestFulfilled === 0 && counters.faviconResponseAttempted === 0 && counters.faviconResponseFulfilled === 0) ||
      (counters.faviconRequestAttempted === 1 && counters.faviconRequestFulfilled === 1 && counters.faviconResponseAttempted === 1 && counters.faviconResponseFulfilled === 1);
    const exactTabClosed = tabState === "CLOSED" && loopbackKeyboardPreflightV9RetainedTab === null;
    const exactServerClosed = serverState === "CLOSED" && server !== null && server.listening === false;
    const exact = result === "BROWSER_SETTLED_PENDING_SERVER_CLOSE" && errorClass === "NONE" && challengeShape && challengeLength === 50 && exactRequiredCounters && exactOptionalFavicon && counters.unexpectedRequestAttempted === 0 && exactTabClosed && exactServerClosed && !sessionNameUncertain && !browserCallUnsettled && !browserUncertain && !serverUncertain;
    if (exact) {
      loopbackKeyboardPreflightV9ExpectedChallenge = challenge;
      loopbackKeyboardPreflightV9Call3Eligible = true;
      result = "COPY_SETTLED_TAB_AND_SERVER_CLOSED";
    } else {
      loopbackKeyboardPreflightV9Call3Eligible = false;
    }
    nodeRepl.write({ result, errorClass, challengeShape, challengeLength, counters, tabState, exactTabClosed, retainedTabBinding: loopbackKeyboardPreflightV9RetainedTab !== null, serverState, serverListening: server?.listening === true, serverUncertain, browserCallUnsettled, browserUncertain, sessionNameUncertain });
  }
})();
```

Exact Call 2 success requires result `COPY_SETTLED_TAB_AND_SERVER_CLOSED`,
error `NONE`, challenge shape true/length 50, every required counter pair
`1 / 1`, favicon counters either all zero or all one, unexpected requests zero,
tab `CLOSED` with retained binding false, server `CLOSED` with listening false,
and every uncertainty flag false. The unique main path occurs exactly once.
Only one optional exact `GET /favicon.ico` is accepted with 204. Duplicate
main/favicon, any other method/path, request abort/error, response error or
premature close, client error, server error, invalid lifecycle, or teardown
error makes server uncertainty sticky. Connection teardown calls
`closeIdleConnections()` then `closeAllConnections()` before directly awaiting
`server.close()`, so keep-alive cannot make close unbounded. Successful close
never clears prior uncertainty.

Only exact success publishes the lexical challenge and then enables Call 3.
If tab creation fulfilled, the exact binding remains non-null unless close
fulfilled; no browser cleanup follows browser uncertainty. Every failure is
terminal and any later residual cleanup requires a new reviewed contract.

## Call 3 — consume eligibility, compare once, clear, and prove empty

Run this exact JavaScript cell once only after exact Call 2 success.
Eligibility is consumed before the sole child attempt. The persistent
challenge is passed only through child stdin, retained on every terminal
failure, and nulled only after fully validated exact child success.

```javascript
await (async () => {
  const result = { result: "HANDOFF_UNCERTAIN_RETAINED_BINDING", errorClass: "NONE", childStartAttempted: 0, childExitFulfilled: 0, childExitCode: null, stdoutSchemaValid: false, comparison: null, challengeBindingRetained: loopbackKeyboardPreflightV9ExpectedChallenge !== null };
  const safeClass = (value, fallback) => /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(value) ? value : fallback;
  const consumedEligibility = loopbackKeyboardPreflightV9Call3Eligible === true;
  loopbackKeyboardPreflightV9Call3Eligible = false;
  if (!consumedEligibility || typeof loopbackKeyboardPreflightV9ExpectedChallenge !== "string" || !/^OMNI-PREFLIGHT-V9-[0-9A-F]{32}$/.test(loopbackKeyboardPreflightV9ExpectedChallenge)) {
    result.result = "HANDOFF_BINDING_INVALID_RETAINED_AS_FOUND";
    result.challengeBindingRetained = loopbackKeyboardPreflightV9ExpectedChallenge !== null;
    nodeRepl.write(result);
    return;
  }
  let spawnSync;
  try {
    ({ spawnSync } = await import("node:child_process"));
  } catch (error) {
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
    if ($null -eq $expected -or $expected -cnotmatch '^OMNI-PREFLIGHT-V9-[0-9A-F]{32}$' -or $expected.Length -ne 50) { $comparisonError='HANDOFF_SHAPE_FAIL' }
    else {
        $comparisonReads++
        $observed=[string](Get-Clipboard -Raw)
        $comparisonMatch=$observed -ceq $expected
        $observedShape=$observed -cmatch '^OMNI-PREFLIGHT-V9-[0-9A-F]{32}$'
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
$pass=$handoffReads -eq 1 -and $comparisonReads -eq 1 -and $comparisonMatch -and $observedShape -and $observedLength -eq 50 -and $comparisonError -eq 'NONE' -and $finalClearAttempted -eq 1 -and $finalClearFulfilled -eq 1 -and $finalReadAttempted -eq 1 -and $finalReadFulfilled -eq 1 -and $finalEmpty -and $cleanupError -eq 'NONE'
'PREFLIGHT_V9_HANDOFF_READS='+$handoffReads
'PREFLIGHT_V9_COMPARISON_READS='+$comparisonReads
'PREFLIGHT_V9_COMPARISON_MATCH='+$comparisonMatch.ToString().ToUpperInvariant()
'PREFLIGHT_V9_OBSERVED_SHAPE='+$observedShape.ToString().ToUpperInvariant()
'PREFLIGHT_V9_OBSERVED_LENGTH='+$observedLength
'PREFLIGHT_V9_COMPARISON_ERROR='+$comparisonError
'PREFLIGHT_V9_FINAL_CLEAR_ATTEMPTED='+$finalClearAttempted
'PREFLIGHT_V9_FINAL_CLEAR_FULFILLED='+$finalClearFulfilled
'PREFLIGHT_V9_FINAL_READ_ATTEMPTED='+$finalReadAttempted
'PREFLIGHT_V9_FINAL_READ_FULFILLED='+$finalReadFulfilled
'PREFLIGHT_V9_FINAL_EMPTY='+$finalEmpty.ToString().ToUpperInvariant()
'PREFLIGHT_V9_CLEANUP_ERROR='+$cleanupError
'PREFLIGHT_V9_RESULT='+$(if($pass){'PASS'}else{'FAIL'})
if($pass){exit 0}; exit 2`;
  result.childStartAttempted = 1;
  let child;
  try {
    child = spawnSync("C:\\Users\\chatc\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe", ["-NoLogo", "-NoProfile", "-NonInteractive", "-EncodedCommand", Buffer.from(script, "utf16le").toString("base64")], {
      shell: false, windowsHide: true, encoding: "utf8", input: `${loopbackKeyboardPreflightV9ExpectedChallenge}\n`, timeout: 30000, killSignal: "SIGKILL", maxBuffer: 16384,
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
  const keys = ["PREFLIGHT_V9_HANDOFF_READS","PREFLIGHT_V9_COMPARISON_READS","PREFLIGHT_V9_COMPARISON_MATCH","PREFLIGHT_V9_OBSERVED_SHAPE","PREFLIGHT_V9_OBSERVED_LENGTH","PREFLIGHT_V9_COMPARISON_ERROR","PREFLIGHT_V9_FINAL_CLEAR_ATTEMPTED","PREFLIGHT_V9_FINAL_CLEAR_FULFILLED","PREFLIGHT_V9_FINAL_READ_ATTEMPTED","PREFLIGHT_V9_FINAL_READ_FULFILLED","PREFLIGHT_V9_FINAL_EMPTY","PREFLIGHT_V9_CLEANUP_ERROR","PREFLIGHT_V9_RESULT"];
  const parsed = {};
  let schema = lines.length === keys.length && Buffer.byteLength(stdout, "utf8") <= 4096 && stderr.length === 0;
  for (let i=0; schema && i<keys.length; i++) {
    const match = /^([A-Z0-9_]+)=([A-Z0-9_-]{1,64})$/.exec(lines[i]);
    if (match === null || match[1] !== keys[i] || Object.hasOwn(parsed, match[1])) schema = false; else parsed[match[1]] = match[2];
  }
  result.stdoutSchemaValid = schema;
  if (schema) result.comparison = { handoffReads:Number(parsed.PREFLIGHT_V9_HANDOFF_READS), comparisonReads:Number(parsed.PREFLIGHT_V9_COMPARISON_READS), comparisonMatch:parsed.PREFLIGHT_V9_COMPARISON_MATCH, observedShape:parsed.PREFLIGHT_V9_OBSERVED_SHAPE, observedLength:Number(parsed.PREFLIGHT_V9_OBSERVED_LENGTH), comparisonError:parsed.PREFLIGHT_V9_COMPARISON_ERROR, finalClearAttempted:Number(parsed.PREFLIGHT_V9_FINAL_CLEAR_ATTEMPTED), finalClearFulfilled:Number(parsed.PREFLIGHT_V9_FINAL_CLEAR_FULFILLED), finalReadAttempted:Number(parsed.PREFLIGHT_V9_FINAL_READ_ATTEMPTED), finalReadFulfilled:Number(parsed.PREFLIGHT_V9_FINAL_READ_FULFILLED), finalEmpty:parsed.PREFLIGHT_V9_FINAL_EMPTY, cleanupError:parsed.PREFLIGHT_V9_CLEANUP_ERROR, powerShellResult:parsed.PREFLIGHT_V9_RESULT };
  const c = result.comparison;
  const exact = result.errorClass === "NONE" && result.childExitFulfilled === 1 && result.childExitCode === 0 && schema && c.handoffReads === 1 && c.comparisonReads === 1 && c.comparisonMatch === "TRUE" && c.observedShape === "TRUE" && c.observedLength === 50 && c.comparisonError === "NONE" && c.finalClearAttempted === 1 && c.finalClearFulfilled === 1 && c.finalReadAttempted === 1 && c.finalReadFulfilled === 1 && c.finalEmpty === "TRUE" && c.cleanupError === "NONE" && c.powerShellResult === "PASS";
  if (exact) {
    loopbackKeyboardPreflightV9ExpectedChallenge = null;
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
one handoff read, one comparison read, exact equality, observed shape true and
length 50, final clear/read `1 / 1`, final empty true, and both PowerShell error
labels `NONE`, with challenge binding retained false. Every spawn, timeout,
signal, stderr, status, parse, output, or counter uncertainty is terminal,
retains the non-secret challenge binding, and permits no second child or later
browser/clipboard mutation.

## Static and acceptance boundary

Independent review must verify UTF-8/LF bytes, non-evaluating PowerShell and
JavaScript syntax, exact Node `v24.19.0` teardown method availability, browser
API declarations, fresh v9 bindings, lexical-only challenge publication,
session/browser/server uncertainty ordering, unique main and optional favicon
routing/counters, teardown-before-awaited-close ordering, redaction, and exact
cardinality for one server/listen, `nameSession`, `tabs.new`, loopback `goto`,
exact-label lookup, click, `Control+A`, `Control+C`, exact-tab close,
`closeIdleConnections`, `closeAllConnections`, server close, and `spawnSync`.
It must prove exactly three `timeoutMs:5000` action options, the 60000 ms Call 2
control timeout, 30000 ms child deadline, index 0, baseline 12, and zero
external URL, native clipboard API, data URL navigation, CUA, enumeration,
retry, credential, key, token, or routing action.

PASS requires exact Call 1 baseline empty, exact Call 2 keyboard copy plus tab
and server closure, and exact Call 3 equality/final-empty proof. Otherwise FAIL
/ NOT PROVEN and no later action. Old listener/process residuals remain
`NOT PROVEN`. This brief authorizes no live execution; independent PASS and
action-time pins remain mandatory.
