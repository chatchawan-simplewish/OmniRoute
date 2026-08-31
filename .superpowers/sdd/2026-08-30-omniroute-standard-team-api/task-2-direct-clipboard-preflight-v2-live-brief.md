# Task 2 direct clipboard preflight v2 live brief

Status: static candidate; **NOT AUTHORIZED until an independent Sol High direct-byte review says exactly `PASS FOR ONE NON-SECRET PREFLIGHT EXECUTION ONLY`.**

This is an additive successor to the terminally rejected bridge brief. It does
not revise, retry, or authorize that path. The sole purpose is to test once
whether an awaited semantic `Control+C` in the existing Chrome session places
a fresh non-secret challenge on the local Windows current clipboard after the
user disabled AnyDesk clipboard sync.

## Authority and proof boundary

- One execution consumes the one non-secret preflight authority already given
  by the user. There is no retry, fallback, alternate tab, second challenge,
  credential, token, Cloudflare, OmniRoute, VM1205, proxy/proof/R5, Rulesets,
  permission, deletion, or evidence-worktree action.
- PASS proves only this observed local path:
  `fresh local data URL -> semantic focus -> Control+A -> Control+C -> local
  Windows current clipboard -> exact PowerShell comparison`.
- The challenge is non-secret and may be emitted. Clipboard contents other than
  the exact generated challenge are never emitted, serialized, hashed, or
  inspected beyond length and exact equality.
- The rejected bridge brief, scripts, hashes, and review remain unchanged and
  must never be executed.

## Why this path cannot reproduce the rejected race

There are exactly three serial host calls. Call 2 is one Node REPL cell. Every
browser mutation is directly awaited; the cell has no `Promise.race`, timer,
background task, helper process, stdin/stdout bridge, or independent cleanup.
A rejected browser-client promise is always classified as remote-state
uncertainty. It causes no later browser mutation and forbids Call 3. Call 3 may
start only after all six browser calls fulfill and the cell explicitly emits
the exact success object.

Do not add an outer mutation deadline. If Call 2 returns a tool-transport error,
times out outside the reviewed cell, or has an uncertain outcome rather than
the exact result object, stop immediately with `NOT_PROVEN_TOOL_UNCERTAIN` and
perform no later browser or clipboard mutation. That fail-closed state may
leave only the non-secret challenge, an uncertain created tab, or the exact
retained `directPreflightV2RetainedTab`; it cannot be accepted or retried.

## Preconditions

1. Current repo HEAD and this committed brief match the independent PASS.
2. The existing persistent Node REPL binding `chrome` is the named Chrome
   session already initialized under the Chrome-control skill.
3. No earlier preflight process, helper, bridge, or preflight tab is active.
4. AnyDesk clipboard sync is disabled as the user stated. This is a user-state
   precondition, not a claim that the agent can independently inspect AnyDesk.
5. The sole owner records counters locally and stops on the first mismatch.

## Call 1 — clear and prove the local current clipboard empty

Run once in PowerShell 7. This call emits only labels and numeric counters.

```powershell
$ErrorActionPreference = 'Stop'
Set-Clipboard -Value ''
$baseline = [string](Get-Clipboard -Raw)
$baselineEmpty = $baseline.Length -eq 0
'PREFLIGHT_V2_BASELINE_CLEAR_CALLS=1'
'PREFLIGHT_V2_BASELINE_READ_CALLS=1'
'PREFLIGHT_V2_BASELINE_EMPTY=' + $baselineEmpty.ToString().ToUpperInvariant()
if (-not $baselineEmpty) { exit 2 }
exit 0
```

Required result: exit `0`, clear/read `1 / 1`, and `BASELINE_EMPTY=TRUE`.
Any error or mismatch stops before Call 2 and does not consume a browser copy.

## Call 2 — one atomic awaited Node REPL browser cell

Run this exact IIFE once in the already initialized persistent Node REPL. The
IIFE prevents persistent-binding redeclaration. Its only output is one explicit
`nodeRepl.write(...)` containing the fresh non-secret challenge, terminal
label, safe error class, tab state, and counters. If tab creation fulfills, the
actual tab object is assigned immediately to the one-shot top-level retained
binding `directPreflightV2RetainedTab` and stays there until exact close
fulfills. The binding is declared once and must never be redeclared or reused.

```javascript
let directPreflightV2RetainedTab = null;
await (async () => {
  const { randomBytes: directPreflightRandomBytes } = await import("node:crypto");
  const directPreflightChallenge = `OMNI-PREFLIGHT-${directPreflightRandomBytes(16).toString("hex").toUpperCase()}`;
  const directPreflightAccessibleName = "OmniRoute transport preflight challenge";
  const directPreflightHtml = `<!doctype html><meta charset="utf-8"><title>OmniRoute transport preflight</title><label for="challenge">${directPreflightAccessibleName}</label><input id="challenge" aria-label="${directPreflightAccessibleName}" value="${directPreflightChallenge}" readonly>`;
  const directPreflightDataUrl = `data:text/html;charset=utf-8,${encodeURIComponent(directPreflightHtml)}`;
  let directPreflightResult = "BROWSER_UNCERTAIN";
  let directPreflightErrorClass = "NONE";
  let directPreflightTabState = "NOT_ATTEMPTED";
  const directPreflightCounters = { open: 0, goto: 0, focus: 0, selectAll: 0, copy: 0, close: 0 };
  try {
    directPreflightTabState = "CREATE_UNCERTAIN";
    const directPreflightCreatedTab = await chrome.tabs.new();
    directPreflightV2RetainedTab = directPreflightCreatedTab;
    directPreflightCounters.open++;
    directPreflightTabState = "OPEN";
    await directPreflightCreatedTab.goto(directPreflightDataUrl);
    directPreflightCounters.goto++;
    const directPreflightField = directPreflightCreatedTab.playwright.getByLabel(directPreflightAccessibleName, { exact: true });
    await directPreflightField.click();
    directPreflightCounters.focus++;
    await directPreflightField.press("Control+A");
    directPreflightCounters.selectAll++;
    await directPreflightField.press("Control+C");
    directPreflightCounters.copy++;
    directPreflightResult = "COPY_SETTLED";
    directPreflightTabState = "COPY_SETTLED";
  } catch (directPreflightError) {
    directPreflightErrorClass = typeof directPreflightError?.name === "string" ? directPreflightError.name : "ERROR";
    directPreflightResult = "BROWSER_UNCERTAIN";
    if (directPreflightTabState !== "CREATE_UNCERTAIN") directPreflightTabState += "_MUTATION_UNCERTAIN";
  }
  if (directPreflightResult === "COPY_SETTLED") {
    directPreflightTabState = "CLOSE_UNCERTAIN";
    try {
      await directPreflightV2RetainedTab.close();
      directPreflightCounters.close++;
      directPreflightV2RetainedTab = null;
      directPreflightTabState = "CLOSED";
      directPreflightResult = "COPY_SETTLED_AND_CLOSED";
    } catch (directPreflightCloseError) {
      directPreflightErrorClass = typeof directPreflightCloseError?.name === "string" ? directPreflightCloseError.name : "CLOSE_ERROR";
      directPreflightResult = "BROWSER_UNCERTAIN";
      directPreflightTabState = "CLOSE_UNCERTAIN";
    }
  }
  nodeRepl.write({
    challenge: directPreflightChallenge,
    result: directPreflightResult,
    errorClass: directPreflightErrorClass,
    tabState: directPreflightTabState,
    counters: directPreflightCounters,
    exactTabClosed: directPreflightTabState === "CLOSED" && directPreflightV2RetainedTab === null
  });
})();
```

Prohibited in this call: snapshot, screenshot, DOM/content extraction, browser
clipboard API, coordinates, reload, navigation lookup, alternate tab, retry,
timer, `Promise.race`, background work, or any network URL.

Call 2 is eligible for comparison only when it returns one exact object with:

- challenge matching `^OMNI-PREFLIGHT-[0-9A-F]{32}$`;
- `result=COPY_SETTLED_AND_CLOSED`, `errorClass=NONE`, `tabState=CLOSED`,
  `exactTabClosed=true`;
- counters `open/goto/focus/selectAll/copy/close = 1/1/1/1/1/1`.

Any rejection from `tabs.new`, `goto`, `click`, either `press`, or `close`
produces `BROWSER_UNCERTAIN`; no later browser call is made. A rejected
`tabs.new` keeps `tabState=CREATE_UNCERTAIN` and `exactTabClosed=false` even
though the local tab binding is null. Any exact object other than the exact
success object, any missing object, or any tool-transport error forbids Call 3
and stops without further browser or clipboard mutation.

## Call 3 — exact compare, shape-only report, and final clear

Substitute only the exact regex-validated non-secret challenge returned by
Call 2 for `<EXPECTED_CHALLENGE>`. Run once in PowerShell 7 only after the exact
Call 2 success object returns. Never emit `$observed`.

```powershell
$ErrorActionPreference = 'Stop'
$expected = '<EXPECTED_CHALLENGE>'
$comparisonReads = 0
$comparison = $false
$observedLength = -1
$comparisonError = 'NONE'
$finalClearCalls = 0
$finalClearSucceeded = $false
$finalEmptyReads = 0
$postClearEmpty = $false
$cleanupError = 'NONE'
try {
    if ($expected -cnotmatch '^OMNI-PREFLIGHT-[0-9A-F]{32}$') {
        $comparisonError = 'EXPECTED_CHALLENGE_SHAPE_FAIL'
    } else {
        $comparisonReads++
        try {
            $observed = [string](Get-Clipboard -Raw)
            $comparison = $observed -ceq $expected
            $observedLength = $observed.Length
        } catch {
            $comparisonError = $_.Exception.GetType().Name
        }
    }
} finally {
    $finalClearCalls++
    try {
        Set-Clipboard -Value ''
        $finalClearSucceeded = $true
    } catch {
        $cleanupError = 'CLEAR_' + $_.Exception.GetType().Name
    }
    $finalEmptyReads++
    try {
        $postClear = [string](Get-Clipboard -Raw)
        $postClearEmpty = $postClear.Length -eq 0
    } catch {
        if ($cleanupError -eq 'NONE') { $cleanupError = 'READ_' + $_.Exception.GetType().Name }
    }
}
'PREFLIGHT_V2_COMPARISON_READS=' + $comparisonReads
'PREFLIGHT_V2_COMPARISON_MATCH=' + $comparison.ToString().ToUpperInvariant()
'PREFLIGHT_V2_OBSERVED_LENGTH=' + $observedLength
'PREFLIGHT_V2_COMPARISON_ERROR=' + $comparisonError
'PREFLIGHT_V2_FINAL_CLEAR_CALLS=' + $finalClearCalls
'PREFLIGHT_V2_FINAL_CLEAR_SUCCEEDED=' + $finalClearSucceeded.ToString().ToUpperInvariant()
'PREFLIGHT_V2_FINAL_EMPTY_READS=' + $finalEmptyReads
'PREFLIGHT_V2_FINAL_EMPTY=' + $postClearEmpty.ToString().ToUpperInvariant()
'PREFLIGHT_V2_CLEANUP_ERROR=' + $cleanupError
if ($comparison -and $comparisonError -eq 'NONE' -and $finalClearSucceeded -and $postClearEmpty -and $cleanupError -eq 'NONE') { exit 0 }
exit 2
```

## Sole-owner verdict

PASS requires every condition below; otherwise FAIL / NOT PROVEN:

- Call 1 exact exit/labels/counters and empty baseline;
- one exact Call 2 result object with challenge shape, no error, exact tab
  closed, and all six counters exactly `1`;
- Call 3 exact exit `0`, one comparison, exact equality, comparison error
  `NONE`, one final clear, clear success `TRUE`, one final empty read, final
  empty `TRUE`, and cleanup error `NONE`;
- no tool-transport uncertainty, retry, fallback, retained tab, residual
  process, secret, live-resource action, or prohibited browser operation.

The sole owner then records a redacted local report. The report contains the
committed brief hash/size, timestamps, labels/counters, challenge shape and
length only, observed length, PASS/FAIL/NOT PROVEN, exact-tab closure, and
current-clipboard cleanup. It never contains clipboard text or a credential
and sets `authorizes_live_execution=false`.
