# Task 11 OmniRoute native clipboard preflight v6 brief

Status: fresh static candidate. `authorizes_live_execution=false`.

This is a new one-shot non-secret transport preflight, not a retry,
continuation, fallback, or override of any consumed gate. V6 uses documented
`TabClipboardAPI.writeText` directly: no URL, loopback server, listener,
navigation, DOM locator, or keyboard action exists.

## Pins, API, and report path

- current base / Task 10 PASS classification:
  `86f51e3d04fb070fa6c5bf2444bc1861e84cfc53`;
- Task 10 report `9f5a2561eb956b324b7135cafa529ccaf2fe3c30`:
  `1934` bytes / SHA-256
  `D63CA21D2F2389260B1F7402C447AF2D37F35F38F28B7C04799B18C9439E657C`;
- Task 10 classification: `4539` bytes / SHA-256
  `2BE4913B9B32901C0FF082DB7AEFA23F77B5C7068AE9C89122B43C3970B17357`;
- installed module: `149210` bytes / SHA-256
  `C52BA09202F0E82CAA6F6D2A6463A8635C1B1316567975D9B91C1A05FB5AF501`;
- installed API: `58477` bytes / SHA-256
  `4BFEB97E958025DB37D52AEA11B75BC70BCA417B4995B0F711C0F07F3DDCCB08`.

```text
nameSession(name: string): Promise<void>; // Name the current browser automation session.
new(): Promise<Tab>; // Create and return a new tab in the browser.
writeText(text: string): Promise<void>; // Write plain text to the browser clipboard.
close(): Promise<void>; // Close this tab.
```

Task 10 proves zero Chrome tabs, current clipboard empty, and the connected
`residualV5Chrome` binding. Old v3/v5 listener/process residuals remain
`NOT PROVEN` and are untouched. The future report path is
`.superpowers/sdd/2026-08-31-omniroute-secure-console-transfer/task-11-v6-native-clipboard-live-report.md`;
it is redacted and sets `authorizes_live_execution=false`.

## Authority and immutable boundary

Standing unattended authority may permit the sole Sol High owner to consume
this fresh gate only after independent direct-byte PASS and action-time pins:
exact brief/review/evidence/API/module/authority bytes, empty index, unchanged
12-path baseline, same connected non-null `residualV5Chrome`, zero
intervening live action, and never-declared fresh v6 bindings.

Calls are strictly serial and stop at first failure. Any invocation, rejection,
timeout, missing/malformed output, or uncertainty spends the gate. No retry,
fallback, override, continuation, reconnect, enumeration, alternate tab,
second child, or verdict relaxation is permitted.

No output includes challenge, clipboard value, tab handle/ID/title/URL,
content/metadata, exception message/stack, credential, key, or token. No
credential/routing authority exists. No URL/server/listener action or
listener/process inspection occurs. The only permitted process is Call 3's
one bounded synchronous PowerShell comparison child.

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
'PREFLIGHT_V6_BASELINE_CLEAR_ATTEMPTED=' + $clearAttempted
'PREFLIGHT_V6_BASELINE_CLEAR_FULFILLED=' + $clearFulfilled
'PREFLIGHT_V6_BASELINE_READ_ATTEMPTED=' + $readAttempted
'PREFLIGHT_V6_BASELINE_READ_FULFILLED=' + $readFulfilled
'PREFLIGHT_V6_BASELINE_EMPTY=' + $empty.ToString().ToUpperInvariant()
'PREFLIGHT_V6_BASELINE_ERROR=' + $errorClass
if ($clearAttempted -eq 1 -and $clearFulfilled -eq 1 -and $readAttempted -eq 1 -and $readFulfilled -eq 1 -and $empty -and $errorClass -eq 'NONE') { exit 0 }
exit 2
```

## Call 2 — one native write on one fresh exact tab

Run this cell once in the session owning `residualV5Chrome`. It names the
session once, creates one tab, writes one fresh non-secret 50-character
challenge through that exact tab's native clipboard API, then closes that tab.
It performs no navigation, URL access, DOM, locator, or keyboard operation.

```javascript
let nativeClipboardPreflightV6ExpectedChallenge = null;
let nativeClipboardPreflightV6Call3Eligible = false;
let nativeClipboardPreflightV6RetainedTab = null;
await (async () => {
  const safeErrorClass = (error, fallback) => {
    const name = typeof error?.name === "string" ? error.name : "";
    return /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(name) ? name : fallback;
  };
  const counters = {
    sessionNameAttempted: 0, sessionNameFulfilled: 0,
    browserOpenAttempted: 0, browserOpenFulfilled: 0,
    clipboardWriteAttempted: 0, clipboardWriteFulfilled: 0,
    browserCloseAttempted: 0, browserCloseFulfilled: 0
  };
  let result = "PRECONDITION_FAILED";
  let errorClass = "NONE";
  let challengeShape = false;
  let challengeLength = 0;
  let tabState = "NOT_ATTEMPTED";
  let browserUncertain = false;
  let sessionNameUncertain = false;
  try {
    if (typeof residualV5Chrome !== "object" || residualV5Chrome === null || typeof residualV5Chrome.nameSession !== "function" || typeof residualV5Chrome.tabs?.new !== "function") {
      throw new Error("ResidualChromeBindingError");
    }
    counters.sessionNameAttempted++;
    sessionNameUncertain = true;
    result = "SESSION_NAME_UNCERTAIN";
    await residualV5Chrome.nameSession("omniroute-v6-native-clipboard");
    counters.sessionNameFulfilled++;
    sessionNameUncertain = false;
    const { randomBytes } = await import("node:crypto");
    const challenge = `OMNI-PREFLIGHT-V6-${randomBytes(16).toString("hex").toUpperCase()}`;
    challengeShape = /^OMNI-PREFLIGHT-V6-[0-9A-F]{32}$/.test(challenge);
    challengeLength = challenge.length;
    tabState = "OPEN_UNCERTAIN";
    counters.browserOpenAttempted++;
    const tab = await residualV5Chrome.tabs.new();
    counters.browserOpenFulfilled++;
    nativeClipboardPreflightV6RetainedTab = tab;
    tabState = "OPEN";
    if (tab === null || (typeof tab !== "object" && typeof tab !== "function") || typeof tab.clipboard?.writeText !== "function" || typeof tab.close !== "function") {
      result = "TAB_CLIPBOARD_API_INVALID";
      throw new Error("TabClipboardApiError");
    }
    tabState = "WRITE_UNCERTAIN";
    counters.clipboardWriteAttempted++;
    await nativeClipboardPreflightV6RetainedTab.clipboard.writeText(challenge);
    counters.clipboardWriteFulfilled++;
    tabState = "WRITTEN";
    tabState = "CLOSE_UNCERTAIN";
    counters.browserCloseAttempted++;
    await nativeClipboardPreflightV6RetainedTab.close();
    counters.browserCloseFulfilled++;
    nativeClipboardPreflightV6RetainedTab = null;
    tabState = "CLOSED";
    if (challengeShape && challengeLength === 50 && Object.values(counters).every((value) => value === 1) && !sessionNameUncertain && !browserUncertain) {
      nativeClipboardPreflightV6ExpectedChallenge = challenge;
      nativeClipboardPreflightV6Call3Eligible = true;
      result = "NATIVE_WRITE_SETTLED_TAB_CLOSED";
    } else {
      result = "COUNTER_OR_CHALLENGE_SHAPE_INVALID";
    }
  } catch (error) {
    errorClass = safeErrorClass(error, "BROWSER_ERROR");
    browserUncertain = sessionNameUncertain || tabState.endsWith("_UNCERTAIN");
    if (result !== "TAB_CLIPBOARD_API_INVALID") result = browserUncertain ? "BROWSER_UNCERTAIN" : "PRECONDITION_OR_RUNTIME_UNCERTAIN";
  } finally {
    if (result !== "NATIVE_WRITE_SETTLED_TAB_CLOSED") {
      nativeClipboardPreflightV6Call3Eligible = false;
    }
    nodeRepl.write({
      result, errorClass, challengeShape, challengeLength, counters, tabState,
      exactTabClosed: tabState === "CLOSED" && nativeClipboardPreflightV6RetainedTab === null,
      retainedTabBinding: nativeClipboardPreflightV6RetainedTab !== null,
      browserUncertain,
      sessionNameUncertain
    });
  }
})();
```

Success requires result `NATIVE_WRITE_SETTLED_TAB_CLOSED`, error `NONE`,
shape true, length 50, all eight counters 1, tab `CLOSED`, exact-tab-closed
true, retained binding false, browser uncertainty false, and session-name
uncertainty false. Only it publishes the lexical challenge to the persistent
binding and then enables Call 3.

Any uncertain browser call stops. If tab creation fulfilled, its exact binding
remains non-null unless close fulfilled. No cleanup close follows uncertainty.
On failure the challenge remains lexical and is never published to the
persistent binding; eligibility remains false. Later cleanup requires a new
reviewed contract.

## Call 3 — consume eligibility, compare once, then clear and prove empty

Run this exact JavaScript cell once only after exact Call 2 success. Eligibility
is consumed before the sole child attempt, so retained failure evidence cannot
authorize retry. The persistent challenge is passed only through child stdin,
retained on every terminal failure, and nulled only after fully validated exact
child success. It is never disk, environment, argument, network, or output
data.

```javascript
await (async () => {
  const result = { result: "HANDOFF_UNCERTAIN_RETAINED_BINDING", errorClass: "NONE", childStartAttempted: 0, childExitFulfilled: 0, childExitCode: null, stdoutSchemaValid: false, comparison: null, challengeBindingRetained: nativeClipboardPreflightV6ExpectedChallenge !== null };
  const safeClass = (value, fallback) => /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(value) ? value : fallback;
  const consumedEligibility = nativeClipboardPreflightV6Call3Eligible === true;
  nativeClipboardPreflightV6Call3Eligible = false;
  if (!consumedEligibility || typeof nativeClipboardPreflightV6ExpectedChallenge !== "string" || !/^OMNI-PREFLIGHT-V6-[0-9A-F]{32}$/.test(nativeClipboardPreflightV6ExpectedChallenge)) {
    result.result = "HANDOFF_BINDING_INVALID_RETAINED_AS_FOUND";
    result.challengeBindingRetained = nativeClipboardPreflightV6ExpectedChallenge !== null;
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
    if ($null -eq $expected -or $expected -cnotmatch '^OMNI-PREFLIGHT-V6-[0-9A-F]{32}$' -or $expected.Length -ne 50) { $comparisonError='HANDOFF_SHAPE_FAIL' }
    else {
        $comparisonReads++
        $observed=[string](Get-Clipboard -Raw)
        $comparisonMatch=$observed -ceq $expected
        $observedShape=$observed -cmatch '^OMNI-PREFLIGHT-V6-[0-9A-F]{32}$'
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
'PREFLIGHT_V6_HANDOFF_READS='+$handoffReads
'PREFLIGHT_V6_COMPARISON_READS='+$comparisonReads
'PREFLIGHT_V6_COMPARISON_MATCH='+$comparisonMatch.ToString().ToUpperInvariant()
'PREFLIGHT_V6_OBSERVED_SHAPE='+$observedShape.ToString().ToUpperInvariant()
'PREFLIGHT_V6_OBSERVED_LENGTH='+$observedLength
'PREFLIGHT_V6_COMPARISON_ERROR='+$comparisonError
'PREFLIGHT_V6_FINAL_CLEAR_ATTEMPTED='+$finalClearAttempted
'PREFLIGHT_V6_FINAL_CLEAR_FULFILLED='+$finalClearFulfilled
'PREFLIGHT_V6_FINAL_READ_ATTEMPTED='+$finalReadAttempted
'PREFLIGHT_V6_FINAL_READ_FULFILLED='+$finalReadFulfilled
'PREFLIGHT_V6_FINAL_EMPTY='+$finalEmpty.ToString().ToUpperInvariant()
'PREFLIGHT_V6_CLEANUP_ERROR='+$cleanupError
'PREFLIGHT_V6_RESULT='+$(if($pass){'PASS'}else{'FAIL'})
if($pass){exit 0}; exit 2`;
  result.childStartAttempted = 1;
  let child;
  try {
    child = spawnSync("C:\\Program Files\\PowerShell\\7\\pwsh.exe", ["-NoLogo", "-NoProfile", "-NonInteractive", "-EncodedCommand", Buffer.from(script, "utf16le").toString("base64")], {
      shell: false, windowsHide: true, encoding: "utf8", input: `${nativeClipboardPreflightV6ExpectedChallenge}\n`, timeout: 30000, killSignal: "SIGKILL", maxBuffer: 16384,
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
  const keys = ["PREFLIGHT_V6_HANDOFF_READS","PREFLIGHT_V6_COMPARISON_READS","PREFLIGHT_V6_COMPARISON_MATCH","PREFLIGHT_V6_OBSERVED_SHAPE","PREFLIGHT_V6_OBSERVED_LENGTH","PREFLIGHT_V6_COMPARISON_ERROR","PREFLIGHT_V6_FINAL_CLEAR_ATTEMPTED","PREFLIGHT_V6_FINAL_CLEAR_FULFILLED","PREFLIGHT_V6_FINAL_READ_ATTEMPTED","PREFLIGHT_V6_FINAL_READ_FULFILLED","PREFLIGHT_V6_FINAL_EMPTY","PREFLIGHT_V6_CLEANUP_ERROR","PREFLIGHT_V6_RESULT"];
  const parsed = {};
  let schema = lines.length === keys.length && Buffer.byteLength(stdout, "utf8") <= 4096 && stderr.length === 0;
  for (let i=0; schema && i<keys.length; i++) {
    const match = /^([A-Z0-9_]+)=([A-Z0-9_-]{1,64})$/.exec(lines[i]);
    if (match === null || match[1] !== keys[i] || Object.hasOwn(parsed, match[1])) schema = false; else parsed[match[1]] = match[2];
  }
  result.stdoutSchemaValid = schema;
  if (schema) result.comparison = { handoffReads:Number(parsed.PREFLIGHT_V6_HANDOFF_READS), comparisonReads:Number(parsed.PREFLIGHT_V6_COMPARISON_READS), comparisonMatch:parsed.PREFLIGHT_V6_COMPARISON_MATCH, observedShape:parsed.PREFLIGHT_V6_OBSERVED_SHAPE, observedLength:Number(parsed.PREFLIGHT_V6_OBSERVED_LENGTH), comparisonError:parsed.PREFLIGHT_V6_COMPARISON_ERROR, finalClearAttempted:Number(parsed.PREFLIGHT_V6_FINAL_CLEAR_ATTEMPTED), finalClearFulfilled:Number(parsed.PREFLIGHT_V6_FINAL_CLEAR_FULFILLED), finalReadAttempted:Number(parsed.PREFLIGHT_V6_FINAL_READ_ATTEMPTED), finalReadFulfilled:Number(parsed.PREFLIGHT_V6_FINAL_READ_FULFILLED), finalEmpty:parsed.PREFLIGHT_V6_FINAL_EMPTY, cleanupError:parsed.PREFLIGHT_V6_CLEANUP_ERROR, powerShellResult:parsed.PREFLIGHT_V6_RESULT };
  const c = result.comparison;
  const exact = result.errorClass === "NONE" && result.childExitFulfilled === 1 && result.childExitCode === 0 && schema && c.handoffReads === 1 && c.comparisonReads === 1 && c.comparisonMatch === "TRUE" && c.observedShape === "TRUE" && c.observedLength === 50 && c.comparisonError === "NONE" && c.finalClearAttempted === 1 && c.finalClearFulfilled === 1 && c.finalReadAttempted === 1 && c.finalReadFulfilled === 1 && c.finalEmpty === "TRUE" && c.cleanupError === "NONE" && c.powerShellResult === "PASS";
  if (exact) {
    nativeClipboardPreflightV6ExpectedChallenge = null;
    result.challengeBindingRetained = false;
    result.result = "EXACT_MATCH_AND_FINAL_EMPTY";
  } else {
    result.challengeBindingRetained = true;
    result.result = "HANDOFF_OR_COMPARISON_UNCERTAIN_RETAINED_BINDING";
  }
  nodeRepl.write(result);
})();
```

Exact Call 3 success requires the named success result, error `NONE`, child
counters 1/1, exit 0, exact bounded ordered stdout schema, one handoff read,
one comparison read, exact equality, observed shape true and length 50, one
fulfilled final clear, one fulfilled final empty read, final empty true, and
both PowerShell error labels `NONE`, with `challengeBindingRetained=false`.
Every failure, timeout, signal, stderr,
parse/output uncertainty, or counter mismatch is terminal, retains the
non-secret challenge binding as redacted failure evidence, and permits no
second child or later browser/clipboard mutation. Only exact fully validated
success clears that binding.

## Static and acceptance boundary

Review must prove UTF-8/LF bytes, PowerShell parsing, non-evaluating JavaScript
syntax, fresh v6 bindings, lexical-only Call 2 challenge until exact browser
success, session-name uncertainty tracking, eligibility consumption before the
sole child, exactly one persistent challenge publication, failure retention,
success-only challenge nulling, and exact
cardinality for `nameSession`, `tabs.new`,
`tab.clipboard.writeText`, exact-tab close, `spawnSync`, one comparison
read, one final clear, and one final empty read. It must prove the 30000 ms
child deadline, redaction, and zero navigation, URL, DOM/locator, keyboard,
server/listener, reconnect, enumeration, credential, key, token, or routing
action.

PASS requires exact Call 1 baseline empty, exact Call 2 native write/tab close,
and exact Call 3 equality/final-empty proof. Otherwise FAIL / NOT PROVEN and
no later action. Browser uncertainty may retain the exact v6 tab binding for a
new cleanup contract. Old listener/process residuals remain `NOT PROVEN`.
This brief authorizes no live execution; independent PASS and action-time pins
remain mandatory.
