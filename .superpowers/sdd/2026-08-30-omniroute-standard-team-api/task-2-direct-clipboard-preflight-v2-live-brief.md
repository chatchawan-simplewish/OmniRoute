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
Its `finally` starts only after the active browser promise settles. Call 3 may
start only after Call 2 returns its exact result object, which proves that the
cell and its `finally` completed.

Do not add an outer mutation deadline. If Call 2 returns a tool-transport error,
times out outside the reviewed cell, or has an uncertain outcome rather than
the exact result object, stop immediately with `NOT_PROVEN_TOOL_UNCERTAIN` and
perform no later browser or clipboard mutation. That fail-closed state may
leave only the non-secret challenge or the exact retained `directPreflightTab`;
it cannot be accepted or retried.

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

Run this exact cell once in the already initialized persistent Node REPL. The
only returned content is the fresh non-secret challenge, terminal label, safe
error class, and counters. The actual tab object remains in
`directPreflightTab` only if exact close failed.

```javascript
const { randomBytes: directPreflightRandomBytes } = await import("node:crypto");
const directPreflightChallenge = `OMNI-PREFLIGHT-${directPreflightRandomBytes(16).toString("hex").toUpperCase()}`;
const directPreflightAccessibleName = "OmniRoute transport preflight challenge";
const directPreflightHtml = `<!doctype html><meta charset="utf-8"><title>OmniRoute transport preflight</title><label for="challenge">${directPreflightAccessibleName}</label><input id="challenge" aria-label="${directPreflightAccessibleName}" value="${directPreflightChallenge}" readonly>`;
const directPreflightDataUrl = `data:text/html;charset=utf-8,${encodeURIComponent(directPreflightHtml)}`;
let directPreflightTab = null;
let directPreflightResult = "ABORT";
let directPreflightErrorClass = "NONE";
const directPreflightCounters = { open: 0, goto: 0, focus: 0, selectAll: 0, copy: 0, close: 0 };
try {
  directPreflightTab = await chrome.tabs.new();
  directPreflightCounters.open++;
  await directPreflightTab.goto(directPreflightDataUrl);
  directPreflightCounters.goto++;
  const directPreflightField = directPreflightTab.playwright.getByLabel(directPreflightAccessibleName, { exact: true });
  await directPreflightField.click();
  directPreflightCounters.focus++;
  await directPreflightField.press("Control+A");
  directPreflightCounters.selectAll++;
  await directPreflightField.press("Control+C");
  directPreflightCounters.copy++;
  directPreflightResult = "COPY_SETTLED";
} catch (directPreflightError) {
  directPreflightErrorClass = typeof directPreflightError?.name === "string" ? directPreflightError.name : "ERROR";
  directPreflightResult = "ABORT";
} finally {
  if (directPreflightTab !== null) {
    try {
      await directPreflightTab.close();
      directPreflightCounters.close++;
      directPreflightTab = null;
    } catch (directPreflightCloseError) {
      directPreflightErrorClass = typeof directPreflightCloseError?.name === "string" ? directPreflightCloseError.name : "CLOSE_ERROR";
      directPreflightResult = "RETAINED_TAB";
    }
  }
}
({
  challenge: directPreflightChallenge,
  result: directPreflightResult,
  errorClass: directPreflightErrorClass,
  counters: directPreflightCounters,
  exactTabClosed: directPreflightTab === null
});
```

Prohibited in this call: snapshot, screenshot, DOM/content extraction, browser
clipboard API, coordinates, reload, navigation lookup, alternate tab, retry,
timer, `Promise.race`, background work, or any network URL.

Call 2 is eligible for comparison only when it returns one exact object with:

- challenge matching `^OMNI-PREFLIGHT-[0-9A-F]{32}$`;
- `result=COPY_SETTLED`, `errorClass=NONE`, `exactTabClosed=true`;
- counters `open/goto/focus/selectAll/copy/close = 1/1/1/1/1/1`.

If an exact result object returns with any other value, Call 3 still performs
one shape-only compare and final clear because every browser promise and the
cell `finally` have settled; the overall verdict is FAIL. If no exact object
returns, Call 3 is forbidden to avoid racing an uncertain mutation.

## Call 3 — exact compare, shape-only report, and final clear

Substitute only the exact regex-validated non-secret challenge returned by
Call 2 for `<EXPECTED_CHALLENGE>`. Run once in PowerShell 7 after the exact
Call 2 object returns. Never emit `$observed`.

```powershell
$ErrorActionPreference = 'Stop'
$expected = '<EXPECTED_CHALLENGE>'
if ($expected -cnotmatch '^OMNI-PREFLIGHT-[0-9A-F]{32}$') { throw 'EXPECTED_CHALLENGE_SHAPE_FAIL' }
$observed = [string](Get-Clipboard -Raw)
$comparison = $observed -ceq $expected
$observedLength = $observed.Length
Set-Clipboard -Value ''
$postClear = [string](Get-Clipboard -Raw)
$postClearEmpty = $postClear.Length -eq 0
'PREFLIGHT_V2_COMPARISON_READS=1'
'PREFLIGHT_V2_COMPARISON_MATCH=' + $comparison.ToString().ToUpperInvariant()
'PREFLIGHT_V2_OBSERVED_LENGTH=' + $observedLength
'PREFLIGHT_V2_FINAL_CLEAR_CALLS=1'
'PREFLIGHT_V2_FINAL_EMPTY_READS=1'
'PREFLIGHT_V2_FINAL_EMPTY=' + $postClearEmpty.ToString().ToUpperInvariant()
if ($comparison -and $postClearEmpty) { exit 0 }
exit 2
```

## Sole-owner verdict

PASS requires every condition below; otherwise FAIL / NOT PROVEN:

- Call 1 exact exit/labels/counters and empty baseline;
- one exact Call 2 result object with challenge shape, no error, exact tab
  closed, and all six counters exactly `1`;
- Call 3 exact exit `0`, one comparison, exact equality, one final clear, one
  final empty read, and final empty `TRUE`;
- no tool-transport uncertainty, retry, fallback, retained tab, residual
  process, secret, live-resource action, or prohibited browser operation.

The sole owner then records a redacted local report. The report contains the
committed brief hash/size, timestamps, labels/counters, challenge shape and
length only, observed length, PASS/FAIL/NOT PROVEN, exact-tab closure, and
current-clipboard cleanup. It never contains clipboard text or a credential
and sets `authorizes_live_execution=false`.
