# Task 5 v3 residual-state disposition brief

Status: static candidate; **NOT AUTHORIZED** until an independent Sol High
direct-byte review passes and the user gives fresh exact action-time authority
for the complete conditional disposition below.

This contract is cleanup/disposition only after the consumed v3 preflight lost
its private bindings. It is not a retry or continuation of Call 2 or Call 3.

## Fixed evidence

- Execution report commit:
  `ac4101401a7c74c32e2415be803e6429a34b1679`
- Independent classification commit:
  `1749c51ad8c901dbee3ede6e2e935d0dd2bacfdc`
- Classification: Call 1 PASS; Call 2 `BROWSER_UNCERTAIN / NOT PROVEN` after
  one consumed invocation; Call 3 not attempted.
- Post-timeout retained-tab absence: `NOT PROVEN`.
- Final current-clipboard empty state: `NOT PROVEN`.
- Loopback listener/process absence: `NOT PROVEN`.
- Preserved unrelated source baseline: exactly `12` dirty paths.
- Browser client module:
  `C:/Users/chatc/.codex/plugins/cache/openai-bundled/browser/26.825.51511/scripts/browser-client.mjs`
- Browser client SHA-256:
  `C52BA09202F0E82CAA6F6D2A6463A8635C1B1316567975D9B91C1A05FB5AF501`
- Browser client size: `149210` bytes.

## Exact authority boundary

The required user approval must explicitly authorize all and only these
conditional actions once:

1. re-establish the documented Chrome connection;
2. enumerate Chrome tabs once and emit only their count;
3. if and only if the count is exactly `1`, directly await at most one close
   of that sole returned handle; and
4. only after zero tabs are proven, clear the current Windows clipboard once
   and read it once to prove empty.

If the user does not explicitly accept the conditional sole-tab close before
enumeration, execute nothing. Count `0` makes no close call. Count greater than
`1` stops without closing anything. A rejected/uncertain enumeration or close
stops without retry, reacquisition, alternate handle, second enumeration, or
clipboard mutation.

This authority permits no tab ID, URL, title, content, metadata, snapshot,
screenshot, lookup, navigation, reload, coordinate, keyboard, challenge,
preflight, listener, port, process, credential, provider, Cloudflare,
OmniRoute, VM, proxy, key, token, routing, permission, deletion, or secret
inspection or action.

## Preconditions

1. The exact committed brief and independent Sol High PASS review match their
   pinned bytes; the user has supplied the exact conditional authority above.
2. The v3 preflight gate remains consumed and no Call 1, Call 2, or Call 3
   continuation is permitted.
3. The browser-client module exists with the exact pinned size and hash.
4. The source worktree still has the exact preserved 12-path dirty baseline
   and an empty Git index.
5. No later browser, clipboard, listener, process, credential, or routing
   disposition has intervened.

Any drift, missing review/authority, malformed output, or tool-transport
uncertainty stops before the next call.

## Call 1 — re-establish and document the Chrome connection

Run this exact cell once in the fresh Node session created by the recorded
kernel reset. It performs no tab enumeration or mutation. The complete
documentation output must be read before Call 2. Missing, truncated, malformed,
or tool-uncertain documentation stops without another connection attempt.

```javascript
const { setupBrowserRuntime: residualV3SetupBrowserRuntime } = await import("C:/Users/chatc/.codex/plugins/cache/openai-bundled/browser/26.825.51511/scripts/browser-client.mjs");
const residualV3Agent = await residualV3SetupBrowserRuntime();
const residualV3Chrome = await residualV3Agent.browsers.get("chrome");
nodeRepl.write(await residualV3Chrome.documentation());
```

No connection output is accepted as tab-state evidence. Call 2 may follow only
after the documented `tabs.list()` and exact tab-handle `close()` APIs are
confirmed present in the complete documentation.

## Call 2 — one count-only enumeration and conditional sole-tab close

Run this exact cell once only after Call 1 succeeds and the prior user
authority explicitly includes closing the sole tab when the count is exactly
`1`. The persistent eligibility is consumed before the first browser call, so
every failure is non-retryable.

```javascript
let residualV3DispositionEligible = true;
await (async () => {
  const safeErrorClass = (error, defaultClass) => {
    const name = typeof error?.name === "string" ? error.name : "";
    return /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(name) ? name : defaultClass;
  };
  const conditionalSoleTabCloseAuthorized = true;
  const eligible = residualV3DispositionEligible === true;
  residualV3DispositionEligible = false;
  let result = "ENUMERATION_UNCERTAIN";
  let errorClass = "NONE";
  let enumerationAttempted = 0;
  let enumerationFulfilled = 0;
  let tabCount = -1;
  let closeAttempted = 0;
  let closeFulfilled = 0;
  let zeroTabsProven = false;
  let tabs = null;
  let soleTab = null;
  if (!eligible || !conditionalSoleTabCloseAuthorized) {
    result = "PRECONDITION_NOT_AUTHORIZED";
  } else {
    enumerationAttempted++;
    try {
      tabs = await residualV3Chrome.tabs.list();
      enumerationFulfilled++;
      if (!Array.isArray(tabs)) {
        result = "ENUMERATION_INVALID";
      } else {
        tabCount = tabs.length;
        if (tabCount === 0) {
          zeroTabsProven = true;
          result = "ZERO_TABS_ALREADY";
        } else if (tabCount === 1) {
          soleTab = tabs[0];
          closeAttempted++;
          result = "CLOSE_UNCERTAIN";
          try {
            await soleTab.close();
            closeFulfilled++;
            zeroTabsProven = true;
            result = "SOLE_TAB_CLOSED";
          } catch (closeError) {
            errorClass = safeErrorClass(closeError, "CLOSE_ERROR");
            result = "CLOSE_UNCERTAIN";
          }
        } else {
          result = "MULTIPLE_TABS_STOP";
        }
      }
    } catch (enumerationError) {
      errorClass = safeErrorClass(enumerationError, "ENUMERATION_ERROR");
      result = "ENUMERATION_UNCERTAIN";
    }
  }
  tabs = null;
  soleTab = null;
  nodeRepl.write({
    result,
    errorClass,
    conditionalSoleTabCloseAuthorized,
    enumerationAttempted,
    enumerationFulfilled,
    tabCount,
    closeAttempted,
    closeFulfilled,
    zeroTabsProven
  });
})();
```

The result object is bounded and contains no tab handle or metadata. Accepted
zero-tab outcomes are exactly:

- `ZERO_TABS_ALREADY`: error `NONE`, enumeration `1 / 1`, count `0`, close
  `0 / 0`, and `zeroTabsProven=true`; or
- `SOLE_TAB_CLOSED`: error `NONE`, enumeration `1 / 1`, count `1`, close
  `1 / 1`, and `zeroTabsProven=true`.

`MULTIPLE_TABS_STOP` requires enumeration `1 / 1`, count greater than `1`,
close `0 / 0`, and no later action. Every other result, rejected promise,
missing object, transport uncertainty, counter mismatch, non-array response,
or false zero-tab proof is FAIL / NOT PROVEN. No second enumeration, close,
lookup, reacquisition, alternate handle, retry, or fallback is allowed.

## Call 3 — clear and prove the current clipboard empty

Run this exact block once in PowerShell 7 only after one exact accepted Call 2
zero-tab result. It clears the current clipboard once and reads once to prove
empty. It never emits clipboard content.

```powershell
$ErrorActionPreference = 'Stop'
$clearAttempted = 0
$clearFulfilled = 0
$emptyReadAttempted = 0
$emptyReadFulfilled = 0
$clipboardEmpty = $false
$errorClass = 'NONE'
try {
    $clearAttempted++
    Set-Clipboard -Value ''
    $clearFulfilled++
    $emptyReadAttempted++
    $currentClipboard = [string](Get-Clipboard -Raw)
    $emptyReadFulfilled++
    $clipboardEmpty = $currentClipboard.Length -eq 0
} catch {
    $caughtName = $_.Exception.GetType().Name
    $errorClass = if ($caughtName -cmatch '^[A-Za-z][A-Za-z0-9_.-]{0,63}$') { $caughtName } else { 'ERROR' }
} finally {
    $currentClipboard = $null
}
'RESIDUAL_V3_CLIPBOARD_CLEAR_ATTEMPTED=' + $clearAttempted
'RESIDUAL_V3_CLIPBOARD_CLEAR_FULFILLED=' + $clearFulfilled
'RESIDUAL_V3_CLIPBOARD_EMPTY_READ_ATTEMPTED=' + $emptyReadAttempted
'RESIDUAL_V3_CLIPBOARD_EMPTY_READ_FULFILLED=' + $emptyReadFulfilled
'RESIDUAL_V3_CLIPBOARD_EMPTY=' + $clipboardEmpty.ToString().ToUpperInvariant()
'RESIDUAL_V3_CLIPBOARD_ERROR=' + $errorClass
if ($clearAttempted -eq 1 -and $clearFulfilled -eq 1 -and $emptyReadAttempted -eq 1 -and $emptyReadFulfilled -eq 1 -and $clipboardEmpty -and $errorClass -eq 'NONE') { exit 0 }
exit 2
```

Clipboard disposition PASS requires exit `0`, all four counters exactly `1`,
`CLIPBOARD_EMPTY=TRUE`, and `CLIPBOARD_ERROR=NONE`. Any other output is FAIL /
NOT PROVEN and permits no second clear or read.

## Loopback listener/process residual remains NOT PROVEN

This contract deliberately performs no listener, port, PID, socket, or process
inspection or action. The reset destroyed the exact Call 2 server binding and
its lifecycle counters. A broad port/process scan cannot reconstruct ownership,
and a close or termination without the exact owned handle could affect an
unrelated local service. Proving browser tabs absent and clearing the clipboard
does not prove that `server.close()` fulfilled or that no listener/process
residual exists.

Therefore the server/listener/process residual remains **NOT PROVEN** after
every outcome of this contract. It is recorded, not weakened or inferred away,
and it continues to block credential and routing work until a separately
scoped, independently reviewed authority path resolves it.

## Disposition verdict and evidence boundary

Browser-and-clipboard disposition PASS requires one exact accepted Call 2
zero-tab result followed by exact Call 3 PASS, with:

- one documented Chrome connection and zero connection retry;
- one fulfilled count-only enumeration;
- either zero close calls at count `0`, or exactly one fulfilled close at
  count `1` under the pre-approved conditional authority;
- no close at count greater than `1`;
- one fulfilled clipboard clear and one fulfilled empty read; and
- zero retry, fallback, reacquisition, alternate handle, metadata/content
  output, navigation, keyboard, challenge access, preflight continuation, or
  prohibited live-resource action.

The later report may contain only pinned brief/review hashes and sizes,
timestamps, safe result/error classes, numeric counters, tab count,
zero-tab proof, clipboard-empty proof, and the unchanged
`server_residual=NOT_PROVEN`. It must set
`authorizes_live_execution=false`.

Static implementation or review PASS authorizes no execution. This contract
does not authorize a preflight retry, credential, provider, Cloudflare,
OmniRoute, VM, proxy, key, token, routing, permission, deletion, listener, or
process action. A fresh exact user approval remains mandatory after the exact
brief receives an independent Sol High PASS.
