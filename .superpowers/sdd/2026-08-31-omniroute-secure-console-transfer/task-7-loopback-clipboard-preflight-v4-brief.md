# Task 7 loopback clipboard preflight v4 brief

Status: static candidate. `authorizes_live_execution=false`.

This is a fresh non-secret v4 contract, not a retry or continuation of any
spent v3 or residual-disposition gate. The independently classified residual
v2 result proves zero current Chrome tabs and an empty current clipboard. The
old lost listener/server/process remains `NOT PROVEN`; this contract neither
inspects nor acts on it.

## Pinned static evidence

- corrected v3 brief commit `f7fd70caeae9c0b0caa6b2f87d894efcb32f25f7`:
  `27048` bytes, SHA-256
  `AF8BAEFF29EE1DB77967798B39A6CAEFA3D18F5047FBE3F440B8F88CD0CBD214`;
- v3 timeout report commit `ac4101401a7c74c32e2415be803e6429a34b1679`:
  `3082` bytes, SHA-256
  `2F7BB3B41BC7FCB78EDC56C620B26334FB7577FF7F894BB29D9F675704C731DE`;
- v3 classification commit `1749c51ad8c901dbee3ede6e2e935d0dd2bacfdc`:
  `5312` bytes, SHA-256
  `09D059A757D5D4215CC9ACF9BB6251043D13502294D48917D06CB73FA9CDB26E`;
- residual v2 PASS report commit
  `0f312bb51c58310ce25f5252048cc216c2c32e2b`: `2651` bytes, SHA-256
  `A550F841ECB4FC12EBE300ED15716B922CA963F1F6FA69AAEF0A886E8116906C`;
- residual v2 classification commit
  `c8bbb803661d20a8041a98635436269dd0c4ae1f`: `5200` bytes, SHA-256
  `AAE12DE7901EA3EEDC1502A0FF05ECC114A0AF1F5D50F8C4DFD5CCDC7594362E`;
- installed `browser-client.mjs`: `149210` bytes, SHA-256
  `C52BA09202F0E82CAA6F6D2A6463A8635C1B1316567975D9B91C1A05FB5AF501`;
- installed `docs/api.json`: `58477` bytes, SHA-256
  `4BFEB97E958025DB37D52AEA11B75BC70BCA417B4995B0F711C0F07F3DDCCB08`;
- project-root `AGENTS.md`: `6051` bytes, SHA-256
  `AD0EA394F694C7795870C2B66D745EDC1FCA8997E7D7041A21E5659B0C349DDC`.

The installed API evidence declares `Tabs.new(): Promise<Tab>`,
`Tab.goto(url: string): Promise<void>`, `PlaywrightLocator.click(...)`,
`PlaywrightLocator.press(...)`, and `Tab.close(): Promise<void>`.

## Authority and immutable execution envelope

Execution is permitted only after an independent Sol High direct-byte review
returns its separately pinned exact PASS and the sole-owner executor revalidates
at action time: this brief and review bytes/hashes, project-root `AGENTS.md`
standing authority, an empty Git index, the exact 12-path dirty source baseline,
and the existing non-null `residualV3Chrome` binding. Standing authority permits
that reviewed one-shot consumption without another chat approval. A missing pin,
mismatch, rejection, timeout, malformed result, or uncertainty spends the gate
and forbids retry, fallback, continuation, or later calls.

The orchestrator must invoke the exact Call 2 control cell once with
`timeout_ms=120000`. Any other control timeout or a second invocation is outside
this contract. Call 3's child deadline remains exactly 30000 milliseconds.

The three calls are serial. Call 2 must not start unless Call 1 exactly passes;
Call 3 must not start unless Call 2 returns its exact success object. Output is
redacted: no challenge, clipboard value, URL, port, path, HTML, tab ID/title/URL,
tab/content/handle, exception message/stack, credential, key, or token may be
emitted.

## Call 1 — clear and prove the current clipboard empty

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
'PREFLIGHT_V4_BASELINE_CLEAR_ATTEMPTED=' + $clearAttempted
'PREFLIGHT_V4_BASELINE_CLEAR_FULFILLED=' + $clearFulfilled
'PREFLIGHT_V4_BASELINE_READ_ATTEMPTED=' + $readAttempted
'PREFLIGHT_V4_BASELINE_READ_FULFILLED=' + $readFulfilled
'PREFLIGHT_V4_BASELINE_EMPTY=' + $empty.ToString().ToUpperInvariant()
'PREFLIGHT_V4_BASELINE_ERROR=' + $errorClass
if ($clearAttempted -eq 1 -and $clearFulfilled -eq 1 -and $readAttempted -eq 1 -and $readFulfilled -eq 1 -and $empty -and $errorClass -eq 'NONE') { exit 0 }
exit 2
```

## Call 2 — one fresh loopback server and one new controllable tab

Run this exact JavaScript cell once in the persistent session that owns
`residualV3Chrome`. It performs no reconnect, documentation call, or tab
enumeration. Every browser mutation is directly awaited and serial.

```javascript
let loopbackPreflightV4ExpectedChallenge = null;
let loopbackPreflightV4Call3Eligible = false;
let loopbackPreflightV4RetainedTab = null;
await (async () => {
  const safeErrorClass = (error, fallback) => {
    const name = typeof error?.name === "string" ? error.name : "";
    return /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(name) ? name : fallback;
  };
  const counters = {
    serverStartAttempted: 0, serverStartFulfilled: 0,
    serverRequestAttempted: 0, serverRequestFulfilled: 0,
    serverResponseAttempted: 0, serverResponseFulfilled: 0,
    serverCloseAttempted: 0, serverCloseFulfilled: 0,
    browserOpenAttempted: 0, browserOpenFulfilled: 0,
    browserGotoAttempted: 0, browserGotoFulfilled: 0,
    browserFocusAttempted: 0, browserFocusFulfilled: 0,
    browserSelectAllAttempted: 0, browserSelectAllFulfilled: 0,
    browserCopyAttempted: 0, browserCopyFulfilled: 0,
    browserCloseAttempted: 0, browserCloseFulfilled: 0
  };
  let result = "PRECONDITION_FAIL";
  let errorClass = "NONE";
  let challengeShape = false;
  let challengeLength = 0;
  let tabState = "NOT_ATTEMPTED";
  let serverState = "NOT_CREATED";
  let server = null;
  let exactRequestServed = false;
  let browserUncertain = false;
  let serverUncertain = false;
  const markServerUncertain = (state) => {
    serverUncertain = true;
    serverState = state;
  };
  try {
    if (typeof residualV3Chrome !== "object" || residualV3Chrome === null || typeof residualV3Chrome.tabs?.new !== "function") {
      throw new Error("ResidualChromeBindingError");
    }
    const { randomBytes } = await import("node:crypto");
    const { createServer } = await import("node:http");
    const challenge = `OMNI-PREFLIGHT-V4-${randomBytes(16).toString("hex").toUpperCase()}`;
    const requestPath = `/omni-preflight-v4-${randomBytes(16).toString("hex")}`;
    const accessibleName = "OmniRoute loopback transport preflight v4 challenge";
    const html = `<!doctype html><html><head><meta charset="utf-8"><title>OmniRoute transport preflight</title></head><body><label for="challenge">${accessibleName}</label><input id="challenge" aria-label="${accessibleName}" value="${challenge}" readonly></body></html>`;
    loopbackPreflightV4ExpectedChallenge = challenge;
    challengeShape = /^OMNI-PREFLIGHT-V4-[0-9A-F]{32}$/.test(challenge);
    challengeLength = challenge.length;
    server = createServer((request, response) => {
      counters.serverRequestAttempted++;
      if (exactRequestServed || request.method !== "GET" || request.url !== requestPath) {
        markServerUncertain("REQUEST_REJECTED");
        response.writeHead(404, { "Cache-Control": "no-store", "Content-Length": "0", "Content-Type": "text/plain; charset=utf-8", "Referrer-Policy": "no-referrer", "X-Content-Type-Options": "nosniff" });
        response.end();
        return;
      }
      exactRequestServed = true;
      counters.serverRequestFulfilled++;
      counters.serverResponseAttempted++;
      request.once("aborted", () => markServerUncertain("REQUEST_UNCERTAIN"));
      request.once("error", () => markServerUncertain("REQUEST_UNCERTAIN"));
      response.once("finish", () => {
        counters.serverResponseFulfilled++;
        if (!serverUncertain) serverState = "RESPONSE_FULFILLED";
      });
      response.once("error", () => markServerUncertain("RESPONSE_UNCERTAIN"));
      response.once("close", () => {
        if (!response.writableFinished) markServerUncertain("RESPONSE_UNCERTAIN");
      });
      response.writeHead(200, { "Cache-Control": "no-store", "Content-Type": "text/html; charset=utf-8", "Referrer-Policy": "no-referrer", "X-Content-Type-Options": "nosniff" });
      response.end(html);
    });
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
    counters.browserOpenAttempted++;
    const tab = await residualV3Chrome.tabs.new();
    counters.browserOpenFulfilled++;
    loopbackPreflightV4RetainedTab = tab;
    tabState = "OPEN";
    if (serverState !== "LISTENING" || serverUncertain) {
      markServerUncertain("INVALID_SERVER_LIFECYCLE");
      throw new Error("ServerStateError");
    }
    tabState = "GOTO_UNCERTAIN";
    counters.browserGotoAttempted++;
    await tab.goto(url);
    counters.browserGotoFulfilled++;
    tabState = "LOADED";
    if (serverState !== "RESPONSE_FULFILLED" || serverUncertain || counters.serverRequestAttempted !== 1 || counters.serverRequestFulfilled !== 1 || counters.serverResponseAttempted !== 1 || counters.serverResponseFulfilled !== 1) {
      markServerUncertain("INVALID_EXCHANGE_LIFECYCLE");
      throw new Error("ServerExchangeError");
    }
    const field = tab.playwright.getByLabel(accessibleName, { exact: true });
    tabState = "FOCUS_UNCERTAIN";
    counters.browserFocusAttempted++;
    await field.click();
    counters.browserFocusFulfilled++;
    tabState = "FOCUSED";
    if (serverUncertain) throw new Error("ServerStateError");
    tabState = "SELECT_ALL_UNCERTAIN";
    counters.browserSelectAllAttempted++;
    await field.press("Control+A");
    counters.browserSelectAllFulfilled++;
    tabState = "SELECTED";
    if (serverUncertain) throw new Error("ServerStateError");
    tabState = "COPY_UNCERTAIN";
    counters.browserCopyAttempted++;
    await field.press("Control+C");
    counters.browserCopyFulfilled++;
    tabState = "COPIED";
    if (serverUncertain) throw new Error("ServerStateError");
    tabState = "CLOSE_UNCERTAIN";
    counters.browserCloseAttempted++;
    await loopbackPreflightV4RetainedTab.close();
    counters.browserCloseFulfilled++;
    loopbackPreflightV4RetainedTab = null;
    tabState = "CLOSED";
    result = "BROWSER_SETTLED_PENDING_SERVER_CLOSE";
  } catch (error) {
    errorClass = safeErrorClass(error, "ERROR");
    browserUncertain = tabState.endsWith("_UNCERTAIN");
    result = browserUncertain ? "BROWSER_UNCERTAIN" : "SERVER_OR_PRECONDITION_UNCERTAIN";
  } finally {
    if (server !== null && server.listening) {
      counters.serverCloseAttempted++;
      serverState = "CLOSE_UNCERTAIN";
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
    const exactCounters = Object.values(counters).every((value) => value === 1);
    const exactTabClosed = tabState === "CLOSED" && loopbackPreflightV4RetainedTab === null;
    const exactServerClosed = serverState === "CLOSED" && server !== null && server.listening === false;
    if (result === "BROWSER_SETTLED_PENDING_SERVER_CLOSE" && errorClass === "NONE" && challengeShape && challengeLength === 50 && exactCounters && exactTabClosed && exactServerClosed && !browserUncertain && !serverUncertain) {
      loopbackPreflightV4Call3Eligible = true;
      result = "COPY_SETTLED_TAB_AND_SERVER_CLOSED";
    }
    nodeRepl.write({ result, errorClass, challengeShape, challengeLength, counters, tabState, exactTabClosed, retainedTabBinding: loopbackPreflightV4RetainedTab !== null, serverState, serverListening: server?.listening === true, serverUncertain });
  }
})();
```

Exact Call 2 success requires the named success result, error `NONE`, shape
true, length 50, every one of the 20 counters exactly 1, tab state `CLOSED`,
exact-tab-closed true, retained binding false, server state `CLOSED`, listener
false, and sticky server uncertainty false. Every other or uncertain result
stops. A fulfilled cleanup cannot clear prior uncertainty.

## Call 3 — consume eligibility, compare once, then clear and prove empty

Run this exact JavaScript cell once only after exact Call 2 success. Eligibility
and the persistent challenge are consumed before the sole child spawn attempt,
so every failure is non-retryable. The challenge exists only in the local
binding and child stdin: never disk, environment, argument, network, or output.

```javascript
await (async () => {
  const result = { result: "HANDOFF_UNCERTAIN", errorClass: "NONE", childStartAttempted: 0, childExitFulfilled: 0, childExitCode: null, stdoutSchemaValid: false, comparison: null };
  const safeClass = (value, fallback) => /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(value) ? value : fallback;
  const consumedEligibility = loopbackPreflightV4Call3Eligible === true;
  let call3Challenge = loopbackPreflightV4ExpectedChallenge;
  loopbackPreflightV4Call3Eligible = false;
  loopbackPreflightV4ExpectedChallenge = null;
  if (!consumedEligibility || typeof call3Challenge !== "string" || !/^OMNI-PREFLIGHT-V4-[0-9A-F]{32}$/.test(call3Challenge)) {
    call3Challenge = null;
    result.result = "HANDOFF_BINDING_INVALID";
    nodeRepl.write(result);
    return;
  }
  let spawnSync;
  try {
    ({ spawnSync } = await import("node:child_process"));
  } catch (error) {
    call3Challenge = null;
    result.errorClass = safeClass(typeof error?.name === "string" ? error.name : "", "IMPORT_ERROR");
    result.result = "CHILD_IMPORT_UNCERTAIN";
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
    if ($null -eq $expected -or $expected -cnotmatch '^OMNI-PREFLIGHT-V4-[0-9A-F]{32}$' -or $expected.Length -ne 50) { $comparisonError='HANDOFF_SHAPE_FAIL' }
    else {
        $comparisonReads++
        $observed=[string](Get-Clipboard -Raw)
        $comparisonMatch=$observed -ceq $expected
        $observedShape=$observed -cmatch '^OMNI-PREFLIGHT-V4-[0-9A-F]{32}$'
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
'PREFLIGHT_V4_HANDOFF_READS='+$handoffReads
'PREFLIGHT_V4_COMPARISON_READS='+$comparisonReads
'PREFLIGHT_V4_COMPARISON_MATCH='+$comparisonMatch.ToString().ToUpperInvariant()
'PREFLIGHT_V4_OBSERVED_SHAPE='+$observedShape.ToString().ToUpperInvariant()
'PREFLIGHT_V4_OBSERVED_LENGTH='+$observedLength
'PREFLIGHT_V4_COMPARISON_ERROR='+$comparisonError
'PREFLIGHT_V4_FINAL_CLEAR_ATTEMPTED='+$finalClearAttempted
'PREFLIGHT_V4_FINAL_CLEAR_FULFILLED='+$finalClearFulfilled
'PREFLIGHT_V4_FINAL_READ_ATTEMPTED='+$finalReadAttempted
'PREFLIGHT_V4_FINAL_READ_FULFILLED='+$finalReadFulfilled
'PREFLIGHT_V4_FINAL_EMPTY='+$finalEmpty.ToString().ToUpperInvariant()
'PREFLIGHT_V4_CLEANUP_ERROR='+$cleanupError
'PREFLIGHT_V4_RESULT='+$(if($pass){'PASS'}else{'FAIL'})
if($pass){exit 0}; exit 2`;
  result.childStartAttempted = 1;
  let child;
  try {
    child = spawnSync("C:\\Program Files\\PowerShell\\7\\pwsh.exe", ["-NoLogo", "-NoProfile", "-NonInteractive", "-EncodedCommand", Buffer.from(script, "utf16le").toString("base64")], {
      shell: false, windowsHide: true, encoding: "utf8", input: `${call3Challenge}\n`, timeout: 30000, killSignal: "SIGKILL", maxBuffer: 16384,
      env: { SystemRoot: "C:\\Windows", WINDIR: "C:\\Windows" }
    });
  } catch (error) {
    result.errorClass = safeClass(typeof error?.name === "string" ? error.name : "", "CHILD_ERROR");
    result.result = "CHILD_SPAWN_UNCERTAIN";
    nodeRepl.write(result);
    return;
  } finally {
    call3Challenge = null;
  }
  const childError = typeof child.error?.code === "string" ? child.error.code : (typeof child.error?.name === "string" ? child.error.name : "NONE");
  result.errorClass = safeClass(childError, "CHILD_ERROR");
  result.childExitCode = Number.isInteger(child.status) ? child.status : null;
  result.childExitFulfilled = child.error === undefined && child.signal === null && Number.isInteger(child.status) ? 1 : 0;
  const stdout = typeof child.stdout === "string" ? child.stdout : "";
  const stderr = typeof child.stderr === "string" ? child.stderr : "";
  const lines = stdout.split(/\r?\n/); if (lines.at(-1) === "") lines.pop();
  const keys = ["PREFLIGHT_V4_HANDOFF_READS","PREFLIGHT_V4_COMPARISON_READS","PREFLIGHT_V4_COMPARISON_MATCH","PREFLIGHT_V4_OBSERVED_SHAPE","PREFLIGHT_V4_OBSERVED_LENGTH","PREFLIGHT_V4_COMPARISON_ERROR","PREFLIGHT_V4_FINAL_CLEAR_ATTEMPTED","PREFLIGHT_V4_FINAL_CLEAR_FULFILLED","PREFLIGHT_V4_FINAL_READ_ATTEMPTED","PREFLIGHT_V4_FINAL_READ_FULFILLED","PREFLIGHT_V4_FINAL_EMPTY","PREFLIGHT_V4_CLEANUP_ERROR","PREFLIGHT_V4_RESULT"];
  const parsed = {};
  let schema = lines.length === keys.length && Buffer.byteLength(stdout, "utf8") <= 4096 && stderr.length === 0;
  for (let i=0; schema && i<keys.length; i++) {
    const match = /^([A-Z0-9_]+)=([A-Z0-9_-]{1,64})$/.exec(lines[i]);
    if (match === null || match[1] !== keys[i] || Object.hasOwn(parsed, match[1])) schema = false; else parsed[match[1]] = match[2];
  }
  result.stdoutSchemaValid = schema;
  if (schema) result.comparison = { handoffReads:Number(parsed.PREFLIGHT_V4_HANDOFF_READS), comparisonReads:Number(parsed.PREFLIGHT_V4_COMPARISON_READS), comparisonMatch:parsed.PREFLIGHT_V4_COMPARISON_MATCH, observedShape:parsed.PREFLIGHT_V4_OBSERVED_SHAPE, observedLength:Number(parsed.PREFLIGHT_V4_OBSERVED_LENGTH), comparisonError:parsed.PREFLIGHT_V4_COMPARISON_ERROR, finalClearAttempted:Number(parsed.PREFLIGHT_V4_FINAL_CLEAR_ATTEMPTED), finalClearFulfilled:Number(parsed.PREFLIGHT_V4_FINAL_CLEAR_FULFILLED), finalReadAttempted:Number(parsed.PREFLIGHT_V4_FINAL_READ_ATTEMPTED), finalReadFulfilled:Number(parsed.PREFLIGHT_V4_FINAL_READ_FULFILLED), finalEmpty:parsed.PREFLIGHT_V4_FINAL_EMPTY, cleanupError:parsed.PREFLIGHT_V4_CLEANUP_ERROR, powerShellResult:parsed.PREFLIGHT_V4_RESULT };
  const c = result.comparison;
  const exact = result.errorClass === "NONE" && result.childExitFulfilled === 1 && result.childExitCode === 0 && schema && c.handoffReads === 1 && c.comparisonReads === 1 && c.comparisonMatch === "TRUE" && c.observedShape === "TRUE" && c.observedLength === 50 && c.comparisonError === "NONE" && c.finalClearAttempted === 1 && c.finalClearFulfilled === 1 && c.finalReadAttempted === 1 && c.finalReadFulfilled === 1 && c.finalEmpty === "TRUE" && c.cleanupError === "NONE" && c.powerShellResult === "PASS";
  result.result = exact ? "EXACT_MATCH_AND_FINAL_EMPTY" : "HANDOFF_OR_COMPARISON_UNCERTAIN";
  nodeRepl.write(result);
})();
```

Exact Call 3 success requires the named success result, error `NONE`, child
counters 1/1, exit 0, exact bounded ordered stdout schema, one handoff read,
one comparison read, exact equality, observed shape true and length 50, one
fulfilled final clear, one fulfilled final empty read, final empty true, and
both PowerShell error labels `NONE`. Every failure, timeout, signal, stderr,
parse/output uncertainty, or counter mismatch is terminal and permits no
second child or later browser/clipboard mutation.

## Static evidence and acceptance boundary

The independent review must verify strict UTF-8/LF bytes, PowerShell parser
success for Call 1 and the embedded child script, Node syntax for both
JavaScript cells without evaluation, exact operation cardinality, prohibited
actions, fresh v4 binding names, the existing `residualV3Chrome` precondition,
the 120000 control timeout, the 30000 child timeout, and these installed API
declarations: `Tabs.new(): Promise<Tab>`, `Tab.goto(url: string): Promise<void>`,
`PlaywrightLocator.click(...)`, `PlaywrightLocator.press(...)`, and
`Tab.close(): Promise<void>`.

PASS proves only this fresh non-secret clipboard transport and final cleanup.
It neither inspects nor resolves the old lost listener/server/process, which
remains `NOT PROVEN`. It authorizes no reconnect, tabs list/get, retry,
fallback, alternate tab, old-listener/process action, navigation outside the
fresh loopback URL, keyboard action outside the labelled readonly field,
credential, permission, deletion, provider, Cloudflare, VM, proxy, API key,
token, OmniRoute, or routing action. Every gate remains spent after its single
invocation. A live report must be separately committed and independently
classified; this brief itself authorizes no live execution.
