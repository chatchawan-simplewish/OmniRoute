# Task 6 v3 residual-disposition v2 brief

Status: static replacement candidate; **NOT EXECUTABLE** until an independent
Sol High direct-byte review passes and the sole owner revalidates every
action-time pin and precondition below.

The project-root standing authority permits the independently reviewed
replacement gate to be consumed without another chat approval. It does not
permit retry, fallback, continuation, verdict relaxation, or reuse after any
failure or uncertainty. The earlier residual-disposition gate is spent.

## Fixed evidence and root cause

- Failed live report commit:
  `f793a513c00834397b169c297dae9b8a4ace8e49`
- Independent classification commit:
  `be670a0070dba57b66ad1f8b736363064c47203a`
- Prior brief commit:
  `0d8f888a3c0ed5f7a0146821def64f8c262bbf6e`
- Prior result: enumeration `1 / 1`, count `1`, close `1 / 0`,
  `errorClass=TypeError`, zero tabs not proven, clipboard block not run.
- Root cause: the prior contract called `close()` on the sole `TabInfo`
  returned by `Tabs.list()`. `TabInfo` has metadata fields but no documented
  `close()` method.
- Existing documented Chrome binding: `residualV3Chrome`. This replacement
  reuses it and performs no reconnect or documentation call. A missing binding
  stops before enumeration.
- Preserved unrelated source baseline: exactly `12` dirty paths.

## Exact installed module and API evidence

- Browser client module:
  `C:/Users/chatc/.codex/plugins/cache/openai-bundled/browser/26.825.51511/scripts/browser-client.mjs`
- Browser client size / SHA-256: `149210` /
  `C52BA09202F0E82CAA6F6D2A6463A8635C1B1316567975D9B91C1A05FB5AF501`
- Official installed API document:
  `C:/Users/chatc/.codex/plugins/cache/openai-bundled/browser/26.825.51511/docs/api.json`
- API document size / SHA-256: `58477` /
  `4BFEB97E958025DB37D52AEA11B75BC70BCA417B4995B0F711C0F07F3DDCCB08`
- Exact `Tabs.list` declaration:
  `list(): Promise<Array<TabInfo>>; // List open tabs in the browser.`
- Exact `Tabs.get` declaration:
  `get(id: string): Promise<Tab>; // Get a tab by id.`
- Exact `Tab.close` declaration:
  `close(): Promise<void>; // Close this tab.`
- Project-root authority file size / SHA-256: `6051` /
  `AD0EA394F694C7795870C2B66D745EDC1FCA8997E7D7041A21E5659B0C349DDC`.

The reviewed interface chain is therefore exactly:

`Tabs.list() -> sole TabInfo.id -> Tabs.get(id) -> Tab.close()`.

No title, URL, content, ID value, `TabInfo`, `Tab`, or handle may be emitted.

## Authority and action-time boundary

After independent PASS, the sole Sol High owner may consume this replacement
once under standing authority only after revalidating:

1. exact brief/review bytes and hashes;
2. exact browser module, API document, and authority-file pins above;
3. the existing `residualV3Chrome` binding is present;
4. the Git index is empty and the exact 12-path source baseline is unchanged;
5. no later browser, clipboard, listener/process, credential, or routing
   disposition has intervened; and
6. the earlier preflight and residual-disposition gates remain spent and are
   not being retried or continued.

Any drift or uncertainty stops before execution. Once Call 1 is invoked, this
replacement gate is spent regardless of outcome. There is no second
enumeration, get, close, clipboard clear/read, retry, fallback, reconnection,
or alternate handle.

This contract permits no tab title/URL/content inspection, metadata output,
snapshot, screenshot, navigation, reload, coordinate, keyboard, challenge,
preflight continuation, listener, port, process, credential, provider,
Cloudflare, OmniRoute, VM, proxy, key, token, routing, permission, deletion,
or secret inspection or action.

## Call 1 — one enumeration, conditional get, and conditional close

Run this exact cell once in the persistent Node session that owns the existing
`residualV3Chrome` binding. Eligibility is consumed before the binding check or
first browser call, making every outcome non-retryable.

```javascript
let residualV3DispositionV2Eligible = true;
await (async () => {
  const safeErrorClass = (error, defaultClass) => {
    const name = typeof error?.name === "string" ? error.name : "";
    return /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(name) ? name : defaultClass;
  };
  const eligible = residualV3DispositionV2Eligible === true;
  residualV3DispositionV2Eligible = false;
  let result = "PRECONDITION_FAILED";
  let errorClass = "NONE";
  let enumerationAttempted = 0;
  let enumerationFulfilled = 0;
  let tabCount = -1;
  let getAttempted = 0;
  let getFulfilled = 0;
  let closeAttempted = 0;
  let closeFulfilled = 0;
  let zeroTabsProven = false;
  let tabInfos = null;
  let soleInfo = null;
  let soleTab = null;
  if (!eligible) {
    result = "ELIGIBILITY_CONSUMED";
  } else if (typeof residualV3Chrome === "undefined" || residualV3Chrome === null) {
    result = "CHROME_BINDING_MISSING";
  } else {
    enumerationAttempted++;
    result = "ENUMERATION_UNCERTAIN";
    try {
      tabInfos = await residualV3Chrome.tabs.list();
      enumerationFulfilled++;
      if (!Array.isArray(tabInfos)) {
        result = "ENUMERATION_INVALID";
      } else {
        tabCount = tabInfos.length;
        if (tabCount === 0) {
          zeroTabsProven = true;
          result = "ZERO_TABS_ALREADY";
        } else if (tabCount === 1) {
          soleInfo = tabInfos[0];
          if (soleInfo === null || typeof soleInfo !== "object" || typeof soleInfo.id !== "string" || soleInfo.id.length === 0 || soleInfo.id.length > 512) {
            result = "SOLE_TAB_INFO_INVALID";
          } else {
            getAttempted++;
            result = "GET_UNCERTAIN";
            try {
              soleTab = await residualV3Chrome.tabs.get(soleInfo.id);
              getFulfilled++;
              if (soleTab === null || (typeof soleTab !== "object" && typeof soleTab !== "function")) {
                result = "GET_INVALID";
              } else {
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
              }
            } catch (getError) {
              errorClass = safeErrorClass(getError, "GET_ERROR");
              result = "GET_UNCERTAIN";
            }
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
  tabInfos = null;
  soleInfo = null;
  soleTab = null;
  nodeRepl.write({
    result,
    errorClass,
    enumerationAttempted,
    enumerationFulfilled,
    tabCount,
    getAttempted,
    getFulfilled,
    closeAttempted,
    closeFulfilled,
    zeroTabsProven
  });
})();
```

The result object emits no ID, title, URL, content, metadata object, tab
object, or handle. Exact accepted zero-tab outcomes are:

- `ZERO_TABS_ALREADY`: error `NONE`, enumeration `1 / 1`, count `0`, get
  `0 / 0`, close `0 / 0`, `zeroTabsProven=true`; or
- `SOLE_TAB_CLOSED`: error `NONE`, enumeration `1 / 1`, count `1`, get
  `1 / 1`, close `1 / 1`, `zeroTabsProven=true`.

`MULTIPLE_TABS_STOP` requires enumeration `1 / 1`, count greater than `1`, get
`0 / 0`, close `0 / 0`, and no later action. Missing binding, malformed
`TabInfo`/`Tab`, any rejected promise, missing/malformed output, tool-transport
uncertainty, counter mismatch, or false zero-tab proof is FAIL / NOT PROVEN and
forbids Call 2.

## Call 2 — one clipboard clear and one empty read

Run this exact block once in PowerShell 7 only after one exact accepted Call 1
zero-tab outcome. It emits no clipboard content.

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
'RESIDUAL_V3_V2_CLIPBOARD_CLEAR_ATTEMPTED=' + $clearAttempted
'RESIDUAL_V3_V2_CLIPBOARD_CLEAR_FULFILLED=' + $clearFulfilled
'RESIDUAL_V3_V2_CLIPBOARD_EMPTY_READ_ATTEMPTED=' + $emptyReadAttempted
'RESIDUAL_V3_V2_CLIPBOARD_EMPTY_READ_FULFILLED=' + $emptyReadFulfilled
'RESIDUAL_V3_V2_CLIPBOARD_EMPTY=' + $clipboardEmpty.ToString().ToUpperInvariant()
'RESIDUAL_V3_V2_CLIPBOARD_ERROR=' + $errorClass
if ($clearAttempted -eq 1 -and $clearFulfilled -eq 1 -and $emptyReadAttempted -eq 1 -and $emptyReadFulfilled -eq 1 -and $clipboardEmpty -and $errorClass -eq 'NONE') { exit 0 }
exit 2
```

Clipboard disposition PASS requires exit `0`, all four counters exactly `1`,
`CLIPBOARD_EMPTY=TRUE`, and `CLIPBOARD_ERROR=NONE`. Every other state is FAIL /
NOT PROVEN and permits no second clear or read.

## Listener/process residual and final boundary

This replacement performs no listener, port, PID, socket, or process inspection
or action. Browser/clipboard disposition cannot prove the lost Call 2 server
binding closed, so `server_residual=NOT_PROVEN` remains unchanged after every
outcome and continues to block credential and routing work.

The redacted live report may contain only committed brief/review pins,
timestamps, safe result/error classes, numeric counters, count, zero-tab proof,
clipboard-empty proof, and `server_residual=NOT_PROVEN`. It must never contain
an ID, title, URL, content, object, handle, clipboard value, challenge, secret,
or credential and must set `authorizes_live_execution=false`.

Static implementation/review PASS authorizes only later consumption under the
standing authority after action-time pin verification. A failed or uncertain
invocation remains spent and authorizes no retry, fallback, continuation,
credential, provider, Cloudflare, OmniRoute, VM, proxy, key, token, routing,
permission, deletion, listener, or process action.
