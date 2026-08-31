# Task 15 OmniRoute Windows clipboard keyboard preflight v8 brief

Status: fresh static candidate. `authorizes_live_execution=false`.

This is a new one-shot non-secret Windows clipboard preflight, not a retry,
continuation, fallback, or override of v7 or any consumed gate. V7 proved that
the tab-native clipboard API is isolated from the Windows clipboard visible to
PowerShell. V8 instead uses the documented Playwright locator keyboard path on
one local `data:text/html` document and preserves the corrected v7 comparison
child and fail-closed binding lifecycle.

## Pins, API, and future report

- current base / Task 14 PASS classification commit:
  `d17f557cd3981ec306b6d39c74b8823dcfe880f3`;
- corrected Task 13 contract commit
  `a2b887bb4fad01343b5d2957a27363ee877c7c72`: `20581` bytes,
  SHA-256
  `9B84E07C0F6B5B3CBAEB0BD8A67B9D81139921F49011B113BC80D46D7285FDC9`;
- Task 13 classification commit
  `c2312314afd2e0fa46095e751917315d799ae285`: `5509` bytes,
  SHA-256
  `269A8F2A27F3662C69DBF0CC85E977D1DE91E7EA043C250F21833AB530EA8BA9`;
- Task 14 PASS classification: `4145` bytes, SHA-256
  `52B50688C8A20CA26B5F995813D9A7DBAF74FAA56CD45C875566F9AD09A020F0`;
- installed child executable:
  `C:/Users/chatc/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/powershell/pwsh.exe`;
- child executable bytes / SHA-256: `301368` /
  `DB6DD81183FE57D22E03B911EC9A30A2FD7C40542E97743615355A6FB44F458F`;
- child file version: `7.6.4.500`;
- installed browser API: `58477` bytes / SHA-256
  `4BFEB97E958025DB37D52AEA11B75BC70BCA417B4995B0F711C0F07F3DDCCB08`.

The installed API must continue to expose these exact declarations:

```text
nameSession(name: string): Promise<void>;
new(): Promise<Tab>;
goto(url: string): Promise<void>;
getByLabel(text: TextMatcher, options: { exact?: boolean }): PlaywrightLocator;
click(options: LocatorClickOptions): Promise<void>;
press(value: string, options: { timeoutMs?: number }): Promise<void>;
close(): Promise<void>;
```

Task 14 independently proves the v7 retained challenge binding null and its
cleanup gate spent. Its classification also preserves Task 13's final Windows
clipboard-empty proof without claiming a new read. V8 uses fresh bindings and
only the existing connected `residualV5Chrome` binding. Old v3/v5
listener/process residuals remain untouched and `NOT PROVEN`.

Action-time pins must re-prove the exact child path is a regular file and
matches the pinned bytes, SHA-256, and file version. They must also re-prove
the exact browser API bytes/declarations, evidence/authority bytes, empty Git
index, unchanged 12-path source baseline, same connected non-null
`residualV5Chrome`, zero intervening live action, and never-declared fresh v8
bindings. Drift or ambiguity stops before Call 1.

The future report path is
`.superpowers/sdd/2026-08-31-omniroute-secure-console-transfer/task-15-v8-keyboard-clipboard-live-report.md`.
It remains redacted and sets `authorizes_live_execution=false`.

## Authority and immutable boundary

Standing unattended authority may permit the sole Sol High owner to consume
this fresh gate only after independent direct-byte PASS and all action-time
pins. Calls are strictly serial and stop at first failure. Any invocation,
rejection, timeout, missing/malformed output, or uncertainty spends the gate.
There is no retry, fallback, override, continuation, reconnect, enumeration,
alternate tab, second child, later cleanup, or verdict relaxation.

No output includes the challenge, clipboard value, data URL, HTML, tab
handle/ID/title/URL, content/metadata, exception message/stack, credential,
key, or token. The data URL is constructed and consumed only in Call 2 memory;
it performs no external request or transmission. No server/listener action,
native tab clipboard API, CUA, credential action, or routing authority exists.
The only process is Call 3's one bounded synchronous PowerShell child.

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
'PREFLIGHT_V8_BASELINE_CLEAR_ATTEMPTED=' + $clearAttempted
'PREFLIGHT_V8_BASELINE_CLEAR_FULFILLED=' + $clearFulfilled
'PREFLIGHT_V8_BASELINE_READ_ATTEMPTED=' + $readAttempted
'PREFLIGHT_V8_BASELINE_READ_FULFILLED=' + $readFulfilled
'PREFLIGHT_V8_BASELINE_EMPTY=' + $empty.ToString().ToUpperInvariant()
'PREFLIGHT_V8_BASELINE_ERROR=' + $errorClass
if ($clearAttempted -eq 1 -and $clearFulfilled -eq 1 -and $readAttempted -eq 1 -and $readFulfilled -eq 1 -and $empty -and $errorClass -eq 'NONE') { exit 0 }
exit 2
```

Exact Call 1 success requires clear `1 / 1`, read `1 / 1`, empty true, error
`NONE`, and exit 0. Anything else forbids Call 2.

## Call 2 — one local document, one keyboard copy, one exact tab close

Invoke the orchestrator's sole Call 2 control operation with
`timeout_ms=30000`. Run this cell once in the session owning
`residualV5Chrome`. It names the session, creates one tab, navigates it once to
one locally constructed `data:text/html` document containing one labelled
readonly input whose value is the fresh non-secret 50-character challenge,
gets that field by exact label, then serially performs exact click,
`Control+A`, `Control+C`, and exact-tab close. Click and both press calls each
have `timeoutMs:5000`.

```javascript
let keyboardClipboardPreflightV8ExpectedChallenge = null;
let keyboardClipboardPreflightV8Call3Eligible = false;
let keyboardClipboardPreflightV8RetainedTab = null;
await (async () => {
  const safeErrorClass = (error, fallback) => {
    const name = typeof error?.name === "string" ? error.name : "";
    return /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(name) ? name : fallback;
  };
  const counters = {
    sessionNameAttempted: 0, sessionNameFulfilled: 0,
    browserOpenAttempted: 0, browserOpenFulfilled: 0,
    navigationAttempted: 0, navigationFulfilled: 0,
    locatorAttempted: 0, locatorFulfilled: 0,
    clickAttempted: 0, clickFulfilled: 0,
    selectAttempted: 0, selectFulfilled: 0,
    copyAttempted: 0, copyFulfilled: 0,
    browserCloseAttempted: 0, browserCloseFulfilled: 0
  };
  let result = "PRECONDITION_FAILED";
  let errorClass = "NONE";
  let challengeShape = false;
  let challengeLength = 0;
  let tabState = "NOT_ATTEMPTED";
  let sessionNameUncertain = false;
  let browserCallUnsettled = false;
  let browserUncertain = false;
  try {
    if (typeof residualV5Chrome !== "object" || residualV5Chrome === null || typeof residualV5Chrome.nameSession !== "function" || typeof residualV5Chrome.tabs?.new !== "function") {
      throw new Error("ResidualChromeBindingError");
    }
    counters.sessionNameAttempted++;
    sessionNameUncertain = true;
    result = "SESSION_NAME_UNCERTAIN";
    await residualV5Chrome.nameSession("omniroute-v8-keyboard-clipboard");
    counters.sessionNameFulfilled++;
    sessionNameUncertain = false;
    const { randomBytes } = await import("node:crypto");
    const challenge = `OMNI-PREFLIGHT-V8-${randomBytes(16).toString("hex").toUpperCase()}`;
    challengeShape = /^OMNI-PREFLIGHT-V8-[0-9A-F]{32}$/.test(challenge);
    challengeLength = challenge.length;
    const html = `<!doctype html><meta charset="utf-8"><title>OmniRoute V8</title><label>OmniRoute V8 Challenge<input readonly value="${challenge}"></label>`;
    const dataUrl = `data:text/html;charset=utf-8,${encodeURIComponent(html)}`;
    tabState = "OPEN_UNCERTAIN";
    browserCallUnsettled = true;
    counters.browserOpenAttempted++;
    const tab = await residualV5Chrome.tabs.new();
    counters.browserOpenFulfilled++;
    browserCallUnsettled = false;
    keyboardClipboardPreflightV8RetainedTab = tab;
    tabState = "OPEN";
    if (tab === null || (typeof tab !== "object" && typeof tab !== "function") || typeof tab.goto !== "function" || typeof tab.playwright?.getByLabel !== "function" || typeof tab.close !== "function") {
      result = "TAB_API_INVALID";
      throw new Error("TabApiError");
    }
    tabState = "NAVIGATION_UNCERTAIN";
    browserCallUnsettled = true;
    counters.navigationAttempted++;
    await keyboardClipboardPreflightV8RetainedTab.goto(dataUrl);
    counters.navigationFulfilled++;
    browserCallUnsettled = false;
    tabState = "NAVIGATED";
    tabState = "LOCATOR_UNCERTAIN";
    browserCallUnsettled = true;
    counters.locatorAttempted++;
    const field = keyboardClipboardPreflightV8RetainedTab.playwright.getByLabel("OmniRoute V8 Challenge", { exact: true });
    if (field === null || (typeof field !== "object" && typeof field !== "function") || typeof field.click !== "function" || typeof field.press !== "function") {
      result = "LOCATOR_API_INVALID";
      throw new Error("LocatorApiError");
    }
    counters.locatorFulfilled++;
    browserCallUnsettled = false;
    tabState = "LOCATED";
    tabState = "CLICK_UNCERTAIN";
    browserCallUnsettled = true;
    counters.clickAttempted++;
    await field.click({ timeoutMs: 5000 });
    counters.clickFulfilled++;
    browserCallUnsettled = false;
    tabState = "FOCUSED";
    tabState = "SELECT_UNCERTAIN";
    browserCallUnsettled = true;
    counters.selectAttempted++;
    await field.press("Control+A", { timeoutMs: 5000 });
    counters.selectFulfilled++;
    browserCallUnsettled = false;
    tabState = "SELECTED";
    tabState = "COPY_UNCERTAIN";
    browserCallUnsettled = true;
    counters.copyAttempted++;
    await field.press("Control+C", { timeoutMs: 5000 });
    counters.copyFulfilled++;
    browserCallUnsettled = false;
    tabState = "COPIED";
    tabState = "CLOSE_UNCERTAIN";
    browserCallUnsettled = true;
    counters.browserCloseAttempted++;
    await keyboardClipboardPreflightV8RetainedTab.close();
    counters.browserCloseFulfilled++;
    browserCallUnsettled = false;
    keyboardClipboardPreflightV8RetainedTab = null;
    tabState = "CLOSED";
    if (challengeShape && challengeLength === 50 && Object.values(counters).every((value) => value === 1) && !sessionNameUncertain && !browserCallUnsettled && !browserUncertain) {
      keyboardClipboardPreflightV8ExpectedChallenge = challenge;
      keyboardClipboardPreflightV8Call3Eligible = true;
      result = "KEYBOARD_COPY_SETTLED_TAB_CLOSED";
    } else {
      result = "COUNTER_OR_CHALLENGE_SHAPE_INVALID";
    }
  } catch (error) {
    errorClass = safeErrorClass(error, "BROWSER_ERROR");
    browserUncertain = browserUncertain || sessionNameUncertain || browserCallUnsettled || tabState.endsWith("_UNCERTAIN");
    if (result !== "TAB_API_INVALID" && result !== "LOCATOR_API_INVALID") result = browserUncertain ? "BROWSER_UNCERTAIN" : "PRECONDITION_OR_RUNTIME_FAILED";
  } finally {
    if (result !== "KEYBOARD_COPY_SETTLED_TAB_CLOSED") {
      keyboardClipboardPreflightV8Call3Eligible = false;
    }
    nodeRepl.write({
      result, errorClass, challengeShape, challengeLength, counters, tabState,
      exactTabClosed: tabState === "CLOSED" && keyboardClipboardPreflightV8RetainedTab === null,
      retainedTabBinding: keyboardClipboardPreflightV8RetainedTab !== null,
      browserCallUnsettled,
      browserUncertain,
      sessionNameUncertain
    });
  }
})();
```

Exact Call 2 success requires result `KEYBOARD_COPY_SETTLED_TAB_CLOSED`, error
`NONE`, shape true, length 50, all sixteen counters 1, tab `CLOSED`, exact tab
closed true, retained tab binding false, browser-call unsettled false, browser
uncertainty false, and session-name uncertainty false. Only this branch
publishes the lexical challenge to the persistent binding immediately before
enabling Call 3. The control invocation itself must settle within 30000 ms;
timeout or tool uncertainty is terminal even if later state appears favorable.

Every browser action is serial. Current-call unsettled state is set immediately
before each browser/locator operation and cleared only after its fulfillment.
Failure records browser uncertainty monotonically and never clears it. If tab
creation fulfilled, its exact binding remains non-null unless close fulfilled.
There is no cleanup close after uncertainty. On failure the challenge remains
lexical and is never published; Call 3 eligibility remains false. Later tab or
binding cleanup requires a new reviewed contract.

## Call 3 — consume eligibility, compare once, then clear and prove empty

Run this exact JavaScript cell once only after exact Call 2 success.
Eligibility is consumed before the sole child attempt. The challenge is passed
only through child stdin, retained on every terminal failure, and nulled only
after fully validated exact child success. It is never disk, environment,
argument, network, or output data.

```javascript
await (async () => {
  const result = { result: "HANDOFF_UNCERTAIN_RETAINED_BINDING", errorClass: "NONE", childStartAttempted: 0, childExitFulfilled: 0, childExitCode: null, stdoutSchemaValid: false, comparison: null, challengeBindingRetained: keyboardClipboardPreflightV8ExpectedChallenge !== null };
  const safeClass = (value, fallback) => /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(value) ? value : fallback;
  const consumedEligibility = keyboardClipboardPreflightV8Call3Eligible === true;
  keyboardClipboardPreflightV8Call3Eligible = false;
  if (!consumedEligibility || typeof keyboardClipboardPreflightV8ExpectedChallenge !== "string" || !/^OMNI-PREFLIGHT-V8-[0-9A-F]{32}$/.test(keyboardClipboardPreflightV8ExpectedChallenge)) {
    result.result = "HANDOFF_BINDING_INVALID_RETAINED_AS_FOUND";
    result.challengeBindingRetained = keyboardClipboardPreflightV8ExpectedChallenge !== null;
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
    if ($null -eq $expected -or $expected -cnotmatch '^OMNI-PREFLIGHT-V8-[0-9A-F]{32}$' -or $expected.Length -ne 50) { $comparisonError='HANDOFF_SHAPE_FAIL' }
    else {
        $comparisonReads++
        $observed=[string](Get-Clipboard -Raw)
        $comparisonMatch=$observed -ceq $expected
        $observedShape=$observed -cmatch '^OMNI-PREFLIGHT-V8-[0-9A-F]{32}$'
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
'PREFLIGHT_V8_HANDOFF_READS='+$handoffReads
'PREFLIGHT_V8_COMPARISON_READS='+$comparisonReads
'PREFLIGHT_V8_COMPARISON_MATCH='+$comparisonMatch.ToString().ToUpperInvariant()
'PREFLIGHT_V8_OBSERVED_SHAPE='+$observedShape.ToString().ToUpperInvariant()
'PREFLIGHT_V8_OBSERVED_LENGTH='+$observedLength
'PREFLIGHT_V8_COMPARISON_ERROR='+$comparisonError
'PREFLIGHT_V8_FINAL_CLEAR_ATTEMPTED='+$finalClearAttempted
'PREFLIGHT_V8_FINAL_CLEAR_FULFILLED='+$finalClearFulfilled
'PREFLIGHT_V8_FINAL_READ_ATTEMPTED='+$finalReadAttempted
'PREFLIGHT_V8_FINAL_READ_FULFILLED='+$finalReadFulfilled
'PREFLIGHT_V8_FINAL_EMPTY='+$finalEmpty.ToString().ToUpperInvariant()
'PREFLIGHT_V8_CLEANUP_ERROR='+$cleanupError
'PREFLIGHT_V8_RESULT='+$(if($pass){'PASS'}else{'FAIL'})
if($pass){exit 0}; exit 2`;
  result.childStartAttempted = 1;
  let child;
  try {
    child = spawnSync("C:\\Users\\chatc\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe", ["-NoLogo", "-NoProfile", "-NonInteractive", "-EncodedCommand", Buffer.from(script, "utf16le").toString("base64")], {
      shell: false, windowsHide: true, encoding: "utf8", input: `${keyboardClipboardPreflightV8ExpectedChallenge}\n`, timeout: 30000, killSignal: "SIGKILL", maxBuffer: 16384,
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
  const keys = ["PREFLIGHT_V8_HANDOFF_READS","PREFLIGHT_V8_COMPARISON_READS","PREFLIGHT_V8_COMPARISON_MATCH","PREFLIGHT_V8_OBSERVED_SHAPE","PREFLIGHT_V8_OBSERVED_LENGTH","PREFLIGHT_V8_COMPARISON_ERROR","PREFLIGHT_V8_FINAL_CLEAR_ATTEMPTED","PREFLIGHT_V8_FINAL_CLEAR_FULFILLED","PREFLIGHT_V8_FINAL_READ_ATTEMPTED","PREFLIGHT_V8_FINAL_READ_FULFILLED","PREFLIGHT_V8_FINAL_EMPTY","PREFLIGHT_V8_CLEANUP_ERROR","PREFLIGHT_V8_RESULT"];
  const parsed = {};
  let schema = lines.length === keys.length && Buffer.byteLength(stdout, "utf8") <= 4096 && stderr.length === 0;
  for (let i=0; schema && i<keys.length; i++) {
    const match = /^([A-Z0-9_]+)=([A-Z0-9_-]{1,64})$/.exec(lines[i]);
    if (match === null || match[1] !== keys[i] || Object.hasOwn(parsed, match[1])) schema = false; else parsed[match[1]] = match[2];
  }
  result.stdoutSchemaValid = schema;
  if (schema) result.comparison = { handoffReads:Number(parsed.PREFLIGHT_V8_HANDOFF_READS), comparisonReads:Number(parsed.PREFLIGHT_V8_COMPARISON_READS), comparisonMatch:parsed.PREFLIGHT_V8_COMPARISON_MATCH, observedShape:parsed.PREFLIGHT_V8_OBSERVED_SHAPE, observedLength:Number(parsed.PREFLIGHT_V8_OBSERVED_LENGTH), comparisonError:parsed.PREFLIGHT_V8_COMPARISON_ERROR, finalClearAttempted:Number(parsed.PREFLIGHT_V8_FINAL_CLEAR_ATTEMPTED), finalClearFulfilled:Number(parsed.PREFLIGHT_V8_FINAL_CLEAR_FULFILLED), finalReadAttempted:Number(parsed.PREFLIGHT_V8_FINAL_READ_ATTEMPTED), finalReadFulfilled:Number(parsed.PREFLIGHT_V8_FINAL_READ_FULFILLED), finalEmpty:parsed.PREFLIGHT_V8_FINAL_EMPTY, cleanupError:parsed.PREFLIGHT_V8_CLEANUP_ERROR, powerShellResult:parsed.PREFLIGHT_V8_RESULT };
  const c = result.comparison;
  const exact = result.errorClass === "NONE" && result.childExitFulfilled === 1 && result.childExitCode === 0 && schema && c.handoffReads === 1 && c.comparisonReads === 1 && c.comparisonMatch === "TRUE" && c.observedShape === "TRUE" && c.observedLength === 50 && c.comparisonError === "NONE" && c.finalClearAttempted === 1 && c.finalClearFulfilled === 1 && c.finalReadAttempted === 1 && c.finalReadFulfilled === 1 && c.finalEmpty === "TRUE" && c.cleanupError === "NONE" && c.powerShellResult === "PASS";
  if (exact) {
    keyboardClipboardPreflightV8ExpectedChallenge = null;
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
`NONE`, child start/exit `1 / 1`, exit 0, exact bounded ordered stdout schema,
one handoff read, one comparison read, exact equality, observed shape true and
length 50, one fulfilled final clear, one fulfilled final empty read, final
empty true, and both PowerShell error labels `NONE`, with challenge binding
retained false. Every failure, timeout, signal, stderr, parse/output
uncertainty, or counter mismatch is terminal, retains the non-secret challenge
binding as redacted failure evidence, and permits no second child or later
browser/clipboard mutation. Only exact fully validated success clears it.

## Static and acceptance boundary

Independent review must verify strict UTF-8/LF bytes, Call 1 PowerShell
parsing, and embedded-child syntax through the exact pinned bundled PowerShell
parser without evaluating the child. It must verify non-evaluating JavaScript
syntax and the installed declarations for `Tabs.new`, `Tab.goto`,
`PlaywrightPage.getByLabel`, `PlaywrightLocator.click`,
`PlaywrightLocator.press`, and `Tab.close`.

Review must prove fresh v8 bindings; lexical-only Call 2 challenge until exact
browser success; session and browser uncertainty ordering; one local data URL;
one `nameSession`, `tabs.new`, `goto`, exact-label lookup, click, `Control+A`,
`Control+C`, exact-tab close, and `spawnSync`; exactly three `timeoutMs:5000`
action options; one `timeout_ms=30000` control requirement; eligibility
consumption before the child; one persistent challenge publication; failure
retention; success-only challenge nulling; exact stdout schema; redaction; and
zero server/listener, external URL, native clipboard API, CUA, reconnect,
enumeration, retry, credential, key, token, or routing action.

PASS requires exact Call 1 baseline empty, exact Call 2 keyboard copy/tab
close, and exact Call 3 equality/final-empty proof. Otherwise FAIL / NOT
PROVEN and no later action. Browser uncertainty may retain the exact v8 tab
binding for a new cleanup contract. Old listener/process residuals remain
`NOT PROVEN`. This brief authorizes no live execution; independent PASS and
action-time pins remain mandatory.
