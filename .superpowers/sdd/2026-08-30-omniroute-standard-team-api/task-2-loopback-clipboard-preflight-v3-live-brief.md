# Task 2 loopback clipboard preflight v3 live brief

Status: static candidate; **NOT AUTHORIZED until an independent Sol High
direct-byte review says exactly `PASS FOR ONE NON-SECRET LOOPBACK PREFLIGHT
EXECUTION ONLY` and the user then gives fresh exact one-shot approval.**

This is a replacement static contract. It does not retry either consumed v2
authority, the rejected top-level data URL navigation, or the abandoned
terminal bridge. It creates no live report and authorizes no execution.

## Authority and proof boundary

- The future execution has exactly three calls and no retry, fallback,
  alternate tab, helper or background process in Call 2, timer race, or
  `Promise.race`.
- It tests only one fresh non-secret challenge through one one-use HTTP server
  bound to `127.0.0.1`, one exact Chrome tab, and the local Windows current
  clipboard.
- A rejected or tool-transport-uncertain browser promise is
  `BROWSER_UNCERTAIN`. It forbids every later browser or clipboard mutation,
  retains the exact tab binding when creation fulfilled, and never infers
  closure from an attempted close.
- Server cleanup is local-resource cleanup only. It may follow browser
  uncertainty, but it may not trigger any later browser or clipboard mutation.
  Server ownership remains in the Call 2 cell until one fulfilled close and a
  false `server.listening` check. Any uncertain server state or residual
  listener forbids Call 3.
- Output is redacted. No call emits the challenge, clipboard text, HTML, URL,
  port, request path, tab object, stack, exception message, credential, key, or
  token.

## Exact in-memory Call 2 to Call 3 handoff

Call 2 keeps the fresh challenge only in the persistent private Node binding
`loopbackPreflightV3ExpectedChallenge`. Its one emitted result contains only
challenge shape and length, never the value. Call 3 is one later Node cell in
that same persistent session. Only after the exact Call 2 success object, it
starts exactly one synchronous, no-shell PowerShell 7 child and passes the
challenge once through that child's standard input. The challenge is never an
argument, environment value, file, network message, or tool output.

This narrow in-memory handoff is not the abandoned terminal bridge: Call 2 has
already proved the exact tab closed, the server close fulfilled, and no
listener remains before Call 3 may start. No browser mutation can still be in
flight. The PowerShell child owns the comparison and its single `finally`
cleanup. Call 3 has a fixed 30-second child deadline, no shell, no descendants,
no background action, a bounded redacted stdout schema, and no later browser
or clipboard mutation. Spawn, standard-input, timeout, exit, parse, output, or
session-binding uncertainty fails closed.

## Preconditions

1. The repo HEAD and exact committed brief bytes match the independent PASS.
2. The persistent `chrome` binding is the already initialized Chrome session,
   and the two v3 bindings below have never been declared in that session.
3. There is no retained preflight tab, active preflight server, helper,
   background process, or earlier preflight execution.
4. The sole owner runs Calls 1, 2, and 3 serially, records counters locally,
   and stops on the first mismatch or uncertain tool result.

## Call 1 — clear and prove the current clipboard empty

Run this exact block once in PowerShell 7. It clears once, reads once, emits
only v3 labels/counters, and exits nonzero on every error or mismatch.

```powershell
$ErrorActionPreference = 'Stop'
$clearCalls = 0
$clearFulfilled = 0
$readCalls = 0
$readFulfilled = 0
$baselineEmpty = $false
$errorClass = 'NONE'
try {
    $clearCalls++
    Set-Clipboard -Value ''
    $clearFulfilled++
    $readCalls++
    $baseline = [string](Get-Clipboard -Raw)
    $readFulfilled++
    $baselineEmpty = $baseline.Length -eq 0
} catch {
    $caughtName = $_.Exception.GetType().Name
    $errorClass = if ($caughtName -cmatch '^[A-Za-z][A-Za-z0-9_.-]{0,63}$') { $caughtName } else { 'ERROR' }
}
'PREFLIGHT_V3_BASELINE_CLEAR_CALLS=' + $clearCalls
'PREFLIGHT_V3_BASELINE_CLEAR_FULFILLED=' + $clearFulfilled
'PREFLIGHT_V3_BASELINE_READ_CALLS=' + $readCalls
'PREFLIGHT_V3_BASELINE_READ_FULFILLED=' + $readFulfilled
'PREFLIGHT_V3_BASELINE_EMPTY=' + $baselineEmpty.ToString().ToUpperInvariant()
'PREFLIGHT_V3_BASELINE_ERROR=' + $errorClass
if ($clearCalls -eq 1 -and $clearFulfilled -eq 1 -and $readCalls -eq 1 -and $readFulfilled -eq 1 -and $baselineEmpty -and $errorClass -eq 'NONE') { exit 0 }
exit 2
```

Required result: exit `0`, all four counters `1`, `BASELINE_EMPTY=TRUE`, and
`BASELINE_ERROR=NONE`. Anything else stops before Call 2.

## Call 2 — one atomic loopback browser cell

Run this exact cell once in the initialized persistent Node session. It uses
only Node standard-library crypto and HTTP modules plus the existing `chrome`
binding. Every browser mutation is directly awaited in order.

```javascript
let loopbackPreflightV3ExpectedChallenge = null;
let loopbackPreflightV3RetainedTab = null;
await (async () => {
  const safeErrorClass = (error, defaultClass) => {
    const name = typeof error?.name === "string" ? error.name : "";
    return /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(name) ? name : defaultClass;
  };
  const counters = {
    serverStartAttempted: 0,
    serverStartFulfilled: 0,
    serverRequestAttempted: 0,
    serverRequestFulfilled: 0,
    serverResponseAttempted: 0,
    serverResponseFulfilled: 0,
    serverCloseAttempted: 0,
    serverCloseFulfilled: 0,
    browserOpenAttempted: 0,
    browserOpenFulfilled: 0,
    browserGotoAttempted: 0,
    browserGotoFulfilled: 0,
    browserFocusAttempted: 0,
    browserFocusFulfilled: 0,
    browserSelectAllAttempted: 0,
    browserSelectAllFulfilled: 0,
    browserCopyAttempted: 0,
    browserCopyFulfilled: 0,
    browserCloseAttempted: 0,
    browserCloseFulfilled: 0
  };
  let result = "SERVER_UNCERTAIN";
  let errorClass = "NONE";
  let challengeShape = false;
  let challengeLength = 0;
  let tabState = "NOT_ATTEMPTED";
  let serverState = "NOT_CREATED";
  let server = null;
  let exactRequestServed = false;
  let browserUncertain = false;
  try {
    const { randomBytes } = await import("node:crypto");
    const { createServer } = await import("node:http");
    const challenge = `OMNI-PREFLIGHT-${randomBytes(16).toString("hex").toUpperCase()}`;
    const requestPath = `/omni-preflight-${randomBytes(16).toString("hex")}`;
    const accessibleName = "OmniRoute loopback transport preflight challenge";
    const html = `<!doctype html><html><head><meta charset="utf-8"><title>OmniRoute transport preflight</title></head><body><label for="challenge">${accessibleName}</label><input id="challenge" aria-label="${accessibleName}" value="${challenge}" readonly autofocus></body></html>`;
    loopbackPreflightV3ExpectedChallenge = challenge;
    challengeShape = /^OMNI-PREFLIGHT-[0-9A-F]{32}$/.test(challenge);
    challengeLength = challenge.length;
    server = createServer((request, response) => {
      counters.serverRequestAttempted++;
      if (exactRequestServed || request.method !== "GET" || request.url !== requestPath) {
        response.writeHead(404, {
          "Cache-Control": "no-store",
          "Content-Length": "0",
          "Content-Type": "text/plain; charset=utf-8",
          "Referrer-Policy": "no-referrer",
          "X-Content-Type-Options": "nosniff"
        });
        response.end();
        return;
      }
      exactRequestServed = true;
      counters.serverRequestFulfilled++;
      counters.serverResponseAttempted++;
      response.once("finish", () => {
        counters.serverResponseFulfilled++;
        serverState = "RESPONSE_FULFILLED";
      });
      response.once("error", () => {
        serverState = "RESPONSE_UNCERTAIN";
      });
      response.writeHead(200, {
        "Cache-Control": "no-store",
        "Content-Type": "text/html; charset=utf-8",
        "Referrer-Policy": "no-referrer",
        "X-Content-Type-Options": "nosniff"
      });
      response.end(html);
    });
    server.on("clientError", (_error, socket) => {
      serverState = "CLIENT_ERROR";
      socket.destroy();
    });
    server.on("error", () => {
      serverState = "SERVER_ERROR";
    });
    counters.serverStartAttempted++;
    serverState = "START_UNCERTAIN";
    await new Promise((resolve, reject) => {
      const onError = (error) => {
        server.off("listening", onListening);
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
      throw new Error("LoopbackAddressError");
    }
    const url = `http://127.0.0.1:${address.port}${requestPath}`;
    tabState = "OPEN_UNCERTAIN";
    counters.browserOpenAttempted++;
    const tab = await chrome.tabs.new();
    counters.browserOpenFulfilled++;
    loopbackPreflightV3RetainedTab = tab;
    tabState = "OPEN";
    if (serverState !== "LISTENING") throw new Error("ServerStateError");
    tabState = "GOTO_UNCERTAIN";
    counters.browserGotoAttempted++;
    await tab.goto(url);
    counters.browserGotoFulfilled++;
    tabState = "LOADED";
    if (serverState !== "RESPONSE_FULFILLED" || counters.serverRequestAttempted !== 1 || counters.serverRequestFulfilled !== 1 || counters.serverResponseAttempted !== 1 || counters.serverResponseFulfilled !== 1) {
      throw new Error("ServerExchangeError");
    }
    const field = tab.playwright.getByLabel(accessibleName, { exact: true });
    tabState = "FOCUS_UNCERTAIN";
    counters.browserFocusAttempted++;
    await field.focus();
    counters.browserFocusFulfilled++;
    tabState = "FOCUSED";
    if (serverState !== "RESPONSE_FULFILLED") throw new Error("ServerStateError");
    tabState = "SELECT_ALL_UNCERTAIN";
    counters.browserSelectAllAttempted++;
    await field.press("Control+A");
    counters.browserSelectAllFulfilled++;
    tabState = "SELECTED";
    if (serverState !== "RESPONSE_FULFILLED") throw new Error("ServerStateError");
    tabState = "COPY_UNCERTAIN";
    counters.browserCopyAttempted++;
    await field.press("Control+C");
    counters.browserCopyFulfilled++;
    tabState = "COPIED";
    if (serverState !== "RESPONSE_FULFILLED") throw new Error("ServerStateError");
    tabState = "CLOSE_UNCERTAIN";
    counters.browserCloseAttempted++;
    await loopbackPreflightV3RetainedTab.close();
    counters.browserCloseFulfilled++;
    loopbackPreflightV3RetainedTab = null;
    tabState = "CLOSED";
    result = "BROWSER_SETTLED_PENDING_SERVER_CLOSE";
  } catch (error) {
    errorClass = safeErrorClass(error, "ERROR");
    browserUncertain = tabState.endsWith("_UNCERTAIN");
    result = browserUncertain ? "BROWSER_UNCERTAIN" : "SERVER_UNCERTAIN";
  } finally {
    if (server !== null && server.listening) {
      counters.serverCloseAttempted++;
      serverState = "CLOSE_UNCERTAIN";
      try {
        await new Promise((resolve, reject) => {
          server.close((error) => error ? reject(error) : resolve());
        });
        counters.serverCloseFulfilled++;
        serverState = server.listening ? "RESIDUAL_LISTENER" : "CLOSED";
      } catch (error) {
        if (errorClass === "NONE") errorClass = safeErrorClass(error, "SERVER_CLOSE_ERROR");
        serverState = "CLOSE_UNCERTAIN";
      }
    } else if (server !== null && serverState !== "CLOSED") {
      serverState = server.listening ? "RESIDUAL_LISTENER" : "NOT_LISTENING_UNPROVEN_CLOSE";
    }
    const exactCounters = Object.values(counters).every((value) => value === 1);
    const exactTabClosed = tabState === "CLOSED" && loopbackPreflightV3RetainedTab === null;
    const exactServerClosed = serverState === "CLOSED" && server !== null && server.listening === false;
    if (result === "BROWSER_SETTLED_PENDING_SERVER_CLOSE" && errorClass === "NONE" && challengeShape && challengeLength === 47 && exactCounters && exactTabClosed && exactServerClosed && !browserUncertain) {
      result = "COPY_SETTLED_TAB_AND_SERVER_CLOSED";
    }
    nodeRepl.write({
      result,
      errorClass,
      challengeShape,
      challengeLength,
      counters,
      tabState,
      exactTabClosed,
      retainedTabBinding: loopbackPreflightV3RetainedTab !== null,
      serverState,
      serverListening: server?.listening === true
    });
  }
})();
```

The exact Call 2 success object requires:

- `result=COPY_SETTLED_TAB_AND_SERVER_CLOSED`, `errorClass=NONE`,
  `challengeShape=true`, and `challengeLength=47`;
- every attempted and fulfilled counter exactly `1`;
- `tabState=CLOSED`, `exactTabClosed=true`, and
  `retainedTabBinding=false`; and
- `serverState=CLOSED` and `serverListening=false`.

Every other object, missing or malformed output, rejected tool call, or
transport uncertainty forbids Call 3. After any browser rejection, the
`finally` path may close only the owned local server; it makes no browser or
clipboard mutation. If exact tab creation had fulfilled, its binding remains
non-null unless exact close fulfilled.

## Call 3 — one bounded in-memory handoff to PowerShell 7

Run this exact Node cell only after the exact Call 2 success object. It starts
one synchronous PowerShell 7 child without a shell. The static PowerShell
program is carried in the encoded command; the challenge is supplied only on
standard input. PowerShell reads the current clipboard exactly once for the
comparison and owns one `finally` path that clears once and reads once to prove
empty.

```javascript
await (async () => {
  const { spawnSync } = await import("node:child_process");
  const safeErrorClass = (value, defaultClass) => /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(value) ? value : defaultClass;
  const expectedShape = /^OMNI-PREFLIGHT-[0-9A-F]{32}$/;
  const result = {
    result: "HANDOFF_UNCERTAIN",
    errorClass: "NONE",
    childStartAttempted: 0,
    childExitFulfilled: 0,
    childExitCode: null,
    stdoutSchemaValid: false,
    comparison: null
  };
  if (typeof loopbackPreflightV3ExpectedChallenge !== "string" || !expectedShape.test(loopbackPreflightV3ExpectedChallenge)) {
    result.result = "HANDOFF_BINDING_INVALID";
    nodeRepl.write(result);
    return;
  }
  const script = String.raw`$ErrorActionPreference = 'Stop'
$handoffReads = 0
$expectedShape = $false
$expectedLength = -1
$comparisonReads = 0
$comparisonMatch = $false
$observedShape = $false
$observedLength = -1
$comparisonError = 'NONE'
$finalClearCalls = 0
$finalClearFulfilled = 0
$finalEmptyReads = 0
$finalEmptyReadFulfilled = 0
$finalEmpty = $false
$cleanupError = 'NONE'
$expected = $null
try {
    $handoffReads++
    $expected = [Console]::In.ReadLine()
    $expectedShape = $expected -cmatch '^OMNI-PREFLIGHT-[0-9A-F]{32}$'
    $expectedLength = if ($null -eq $expected) { -1 } else { $expected.Length }
    if (-not $expectedShape -or $expectedLength -ne 47) {
        $comparisonError = 'HANDOFF_SHAPE_FAIL'
    } else {
        $comparisonReads++
        $observed = [string](Get-Clipboard -Raw)
        $comparisonMatch = $observed -ceq $expected
        $observedShape = $observed -cmatch '^OMNI-PREFLIGHT-[0-9A-F]{32}$'
        $observedLength = $observed.Length
    }
} catch {
    $caughtName = $_.Exception.GetType().Name
    $comparisonError = if ($caughtName -cmatch '^[A-Za-z][A-Za-z0-9_.-]{0,63}$') { $caughtName } else { 'ERROR' }
} finally {
    $finalClearCalls++
    try {
        Set-Clipboard -Value ''
        $finalClearFulfilled++
    } catch {
        $caughtName = $_.Exception.GetType().Name
        $cleanupError = if ($caughtName -cmatch '^[A-Za-z][A-Za-z0-9_.-]{0,57}$') { 'CLEAR_' + $caughtName } else { 'CLEAR_ERROR' }
    }
    $finalEmptyReads++
    try {
        $postClear = [string](Get-Clipboard -Raw)
        $finalEmptyReadFulfilled++
        $finalEmpty = $postClear.Length -eq 0
    } catch {
        if ($cleanupError -eq 'NONE') {
            $caughtName = $_.Exception.GetType().Name
            $cleanupError = if ($caughtName -cmatch '^[A-Za-z][A-Za-z0-9_.-]{0,58}$') { 'READ_' + $caughtName } else { 'READ_ERROR' }
        }
    }
    $expected = $null
    $observed = $null
    $postClear = $null
}
$pass = $handoffReads -eq 1 -and $expectedShape -and $expectedLength -eq 47 -and $comparisonReads -eq 1 -and $comparisonMatch -and $observedShape -and $observedLength -eq 47 -and $comparisonError -eq 'NONE' -and $finalClearCalls -eq 1 -and $finalClearFulfilled -eq 1 -and $finalEmptyReads -eq 1 -and $finalEmptyReadFulfilled -eq 1 -and $finalEmpty -and $cleanupError -eq 'NONE'
'PREFLIGHT_V3_HANDOFF_READS=' + $handoffReads
'PREFLIGHT_V3_EXPECTED_SHAPE=' + $expectedShape.ToString().ToUpperInvariant()
'PREFLIGHT_V3_EXPECTED_LENGTH=' + $expectedLength
'PREFLIGHT_V3_COMPARISON_READS=' + $comparisonReads
'PREFLIGHT_V3_COMPARISON_MATCH=' + $comparisonMatch.ToString().ToUpperInvariant()
'PREFLIGHT_V3_OBSERVED_SHAPE=' + $observedShape.ToString().ToUpperInvariant()
'PREFLIGHT_V3_OBSERVED_LENGTH=' + $observedLength
'PREFLIGHT_V3_COMPARISON_ERROR=' + $comparisonError
'PREFLIGHT_V3_FINAL_CLEAR_CALLS=' + $finalClearCalls
'PREFLIGHT_V3_FINAL_CLEAR_FULFILLED=' + $finalClearFulfilled
'PREFLIGHT_V3_FINAL_EMPTY_READS=' + $finalEmptyReads
'PREFLIGHT_V3_FINAL_EMPTY_READ_FULFILLED=' + $finalEmptyReadFulfilled
'PREFLIGHT_V3_FINAL_EMPTY=' + $finalEmpty.ToString().ToUpperInvariant()
'PREFLIGHT_V3_CLEANUP_ERROR=' + $cleanupError
'PREFLIGHT_V3_RESULT=' + $(if ($pass) { 'PASS' } else { 'FAIL' })
if ($pass) { exit 0 }
exit 2`;
  result.childStartAttempted = 1;
  const child = spawnSync("C:\\Program Files\\PowerShell\\7\\pwsh.exe", ["-NoLogo", "-NoProfile", "-NonInteractive", "-EncodedCommand", Buffer.from(script, "utf16le").toString("base64")], {
    shell: false,
    windowsHide: true,
    encoding: "utf8",
    input: `${loopbackPreflightV3ExpectedChallenge}\n`,
    timeout: 30000,
    killSignal: "SIGKILL",
    maxBuffer: 16384,
    env: {
      SystemRoot: "C:\\Windows",
      WINDIR: "C:\\Windows"
    }
  });
  const childErrorName = typeof child.error?.code === "string" ? child.error.code : (typeof child.error?.name === "string" ? child.error.name : "NONE");
  result.errorClass = safeErrorClass(childErrorName, "CHILD_ERROR");
  result.childExitCode = Number.isInteger(child.status) ? child.status : null;
  result.childExitFulfilled = child.error === undefined && child.signal === null && Number.isInteger(child.status) ? 1 : 0;
  const stdout = typeof child.stdout === "string" ? child.stdout : "";
  const stderr = typeof child.stderr === "string" ? child.stderr : "";
  const lines = stdout.split(/\r?\n/);
  if (lines.at(-1) === "") lines.pop();
  const expectedKeys = [
    "PREFLIGHT_V3_HANDOFF_READS",
    "PREFLIGHT_V3_EXPECTED_SHAPE",
    "PREFLIGHT_V3_EXPECTED_LENGTH",
    "PREFLIGHT_V3_COMPARISON_READS",
    "PREFLIGHT_V3_COMPARISON_MATCH",
    "PREFLIGHT_V3_OBSERVED_SHAPE",
    "PREFLIGHT_V3_OBSERVED_LENGTH",
    "PREFLIGHT_V3_COMPARISON_ERROR",
    "PREFLIGHT_V3_FINAL_CLEAR_CALLS",
    "PREFLIGHT_V3_FINAL_CLEAR_FULFILLED",
    "PREFLIGHT_V3_FINAL_EMPTY_READS",
    "PREFLIGHT_V3_FINAL_EMPTY_READ_FULFILLED",
    "PREFLIGHT_V3_FINAL_EMPTY",
    "PREFLIGHT_V3_CLEANUP_ERROR",
    "PREFLIGHT_V3_RESULT"
  ];
  const parsed = {};
  let schemaValid = lines.length === expectedKeys.length && Buffer.byteLength(stdout, "utf8") <= 4096 && stderr.length === 0;
  for (let index = 0; schemaValid && index < expectedKeys.length; index++) {
    const match = /^([A-Z0-9_]+)=([A-Z0-9_-]{1,64})$/.exec(lines[index]);
    if (match === null || match[1] !== expectedKeys[index] || Object.hasOwn(parsed, match[1])) {
      schemaValid = false;
    } else {
      parsed[match[1]] = match[2];
    }
  }
  result.stdoutSchemaValid = schemaValid;
  if (schemaValid) {
    result.comparison = {
      handoffReads: Number(parsed.PREFLIGHT_V3_HANDOFF_READS),
      expectedShape: parsed.PREFLIGHT_V3_EXPECTED_SHAPE,
      expectedLength: Number(parsed.PREFLIGHT_V3_EXPECTED_LENGTH),
      comparisonReads: Number(parsed.PREFLIGHT_V3_COMPARISON_READS),
      comparisonMatch: parsed.PREFLIGHT_V3_COMPARISON_MATCH,
      observedShape: parsed.PREFLIGHT_V3_OBSERVED_SHAPE,
      observedLength: Number(parsed.PREFLIGHT_V3_OBSERVED_LENGTH),
      comparisonError: parsed.PREFLIGHT_V3_COMPARISON_ERROR,
      finalClearCalls: Number(parsed.PREFLIGHT_V3_FINAL_CLEAR_CALLS),
      finalClearFulfilled: Number(parsed.PREFLIGHT_V3_FINAL_CLEAR_FULFILLED),
      finalEmptyReads: Number(parsed.PREFLIGHT_V3_FINAL_EMPTY_READS),
      finalEmptyReadFulfilled: Number(parsed.PREFLIGHT_V3_FINAL_EMPTY_READ_FULFILLED),
      finalEmpty: parsed.PREFLIGHT_V3_FINAL_EMPTY,
      cleanupError: parsed.PREFLIGHT_V3_CLEANUP_ERROR,
      powerShellResult: parsed.PREFLIGHT_V3_RESULT
    };
  }
  const exactSuccess = result.errorClass === "NONE" && result.childExitFulfilled === 1 && result.childExitCode === 0 && schemaValid && result.comparison.handoffReads === 1 && result.comparison.expectedShape === "TRUE" && result.comparison.expectedLength === 47 && result.comparison.comparisonReads === 1 && result.comparison.comparisonMatch === "TRUE" && result.comparison.observedShape === "TRUE" && result.comparison.observedLength === 47 && result.comparison.comparisonError === "NONE" && result.comparison.finalClearCalls === 1 && result.comparison.finalClearFulfilled === 1 && result.comparison.finalEmptyReads === 1 && result.comparison.finalEmptyReadFulfilled === 1 && result.comparison.finalEmpty === "TRUE" && result.comparison.cleanupError === "NONE" && result.comparison.powerShellResult === "PASS";
  result.result = exactSuccess ? "EXACT_MATCH_AND_FINAL_EMPTY" : "HANDOFF_OR_COMPARISON_UNCERTAIN";
  if (exactSuccess) loopbackPreflightV3ExpectedChallenge = null;
  nodeRepl.write(result);
})();
```

The exact Call 3 success object requires `result=EXACT_MATCH_AND_FINAL_EMPTY`,
`errorClass=NONE`, child counters `1 / 1`, child exit `0`, valid bounded stdout,
one handoff read, one clipboard comparison read, exact equality, expected and
observed shape `TRUE`, lengths `47 / 47`, one fulfilled final clear, one
fulfilled final empty read, `FINAL_EMPTY=TRUE`, and both errors `NONE`.

Any missing binding, child error, timeout, signal, nonzero or unknown exit,
stderr, oversized/extra/missing/duplicate/reordered output, parse mismatch,
counter mismatch, comparison mismatch, or cleanup mismatch is FAIL / NOT
PROVEN. It permits no second child, browser call, clipboard call, retry, or
fallback.

## Sole-owner acceptance and authority boundary

PASS requires the exact three-call success path and every condition below:

- Call 1 exact exit and all expected counters `1`, with the baseline empty;
- Call 2 exact success object, all 20 attempted/fulfilled counters `1`, exact
  tab closed and binding null, server close fulfilled, and no residual
  listener;
- Call 3 exact success object, one exact comparison, exact equality, one final
  clear, one final empty read, final clipboard empty, and child exit proven;
  and
- zero retry, fallback, alternate tab, helper/background action in Call 2,
  tool uncertainty, credential exposure, or residual browser/server/child
  state.

Everything else is **FAIL / NOT PROVEN**. A later redacted report may contain
only committed brief hash/size, timestamps, result/error classes, challenge
shape/length, exact counters, tab/binding closure state, server lifecycle,
PowerShell child exit/schema state, equality, and final-empty state. It must
omit the challenge and clipboard value and set
`authorizes_live_execution=false`.

Static PASS authorizes no execution. Future v3 execution requires a fresh
exact one-shot user approval after independent Sol High review. That approval
covers only one non-secret preflight. It authorizes no credential creation or
transmission, clipboard-history change, permission change, deletion,
Cloudflare, OmniRoute, VM1205, provider, proxy, key, token, or routing
mutation.
