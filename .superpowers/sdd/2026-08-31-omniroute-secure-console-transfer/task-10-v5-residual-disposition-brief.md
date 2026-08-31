# Task 10 v5 residual-disposition brief

Status: fresh static cleanup candidate. `authorizes_live_execution=false`.

This contract is cleanup/disposition only after the consumed v5 preflight
timed out and reset its JavaScript kernel. It is not a v5 retry, continuation,
fallback, replacement transport, or verdict override. The reset erased the
private bindings, so this contract permits one documented Chrome bootstrap,
one count-only enumeration, at most one exact-shape sole-tab close, and only
then one clipboard clear/empty proof.

## Pinned evidence and API chain

- current base and v5 classification commit:
  `9e5f8574381135f9765548e2c50c85833f63732b`;
- v5 live report commit `311f51d68f57fbfaf75891c28dcad2f165ce4059`:
  `1863` bytes, SHA-256
  `2338D9DBCD0C27C5FD6D410316EBEB6C89D2CC6DDFFC2F0BACCACEAD316DF751`;
- v5 classification: `5504` bytes, SHA-256
  `D75F71328360FCF82BC309970446F0AF7DE1C62092ACC3A4C2E95ED31D11C497`;
- prior successful residual-v2 contract: `10430` bytes, SHA-256
  `1F1BC20040C6498648E0752E0FA5000F1AA4E9E63A473C3E32C21A54DA405222`;
- browser module
  `C:/Users/chatc/.codex/plugins/cache/openai-bundled/browser/26.825.51511/scripts/browser-client.mjs`:
  `149210` bytes, SHA-256
  `C52BA09202F0E82CAA6F6D2A6463A8635C1B1316567975D9B91C1A05FB5AF501`;
- installed API document: `58477` bytes, SHA-256
  `4BFEB97E958025DB37D52AEA11B75BC70BCA417B4995B0F711C0F07F3DDCCB08`;
- project-root `AGENTS.md`: `6051` bytes, SHA-256
  `AD0EA394F694C7795870C2B66D745EDC1FCA8997E7D7041A21E5659B0C349DDC`.

Exact installed declarations:

```text
list(): Promise<Array<TabInfo>>; // List open tabs in the browser.
get(id: string): Promise<Tab>; // Get a tab by id.
close(): Promise<void>; // Close this tab.
```

`TabInfo` documents `id`, optional `title`, and optional `url`. This contract
reads only the sole `id` needed privately by `tabs.get` and the sole `url`
needed for an in-memory exact-shape decision. It never reads title and never
emits ID, URL, title, content, metadata, `TabInfo`, `Tab`, or handle.

A future result must be written only to
`.superpowers/sdd/2026-08-31-omniroute-secure-console-transfer/task-10-v5-residual-disposition-live-report.md`
and independently classified. It must remain redacted and set
`authorizes_live_execution=false`.

## Authority and one-shot boundary

Standing unattended authority permits the sole Sol High owner to consume this
fresh cleanup gate only after independent direct-byte PASS and action-time
verification of exact brief/review/evidence/module/API/authority pins, empty
Git index, unchanged exact 12-path dirty source baseline, and no intervening
browser, clipboard, listener/process, credential, or routing action.

The three calls below are serial. Any invocation, failure, rejection, timeout,
missing/malformed output, or tool uncertainty spends the gate and stops before
the next call. There is no second bootstrap, documentation call, connection,
enumeration, get, close, clipboard clear/read, retry, fallback, alternate
handle, or reacquisition.

This contract permits no preflight retry, navigation, reload, keyboard,
snapshot, screenshot, content inspection, listener, port, server, socket, PID,
process, credential, provider, Cloudflare, OmniRoute, VM, proxy, key, token,
routing, permission, deletion, or secret inspection/action.

## Call 1 — one documented Chrome bootstrap

Run this exact JavaScript cell once in the fresh Node session created by the
v5 kernel reset. It performs one module import, runtime setup, Chrome
connection, and documentation call. It does not enumerate or mutate tabs.
Missing, truncated, malformed, rejected, or tool-uncertain documentation stops
without a second bootstrap.

```javascript
const { setupBrowserRuntime: residualV5SetupBrowserRuntime } = await import("C:/Users/chatc/.codex/plugins/cache/openai-bundled/browser/26.825.51511/scripts/browser-client.mjs");
const residualV5Agent = await residualV5SetupBrowserRuntime();
const residualV5Chrome = await residualV5Agent.browsers.get("chrome");
nodeRepl.write(await residualV5Chrome.documentation());
```

Call 2 may follow only if complete documentation confirms the pinned
`Tabs.list -> Tabs.get -> Tab.close` chain. Documentation output is not tab
state evidence.

## Call 2 — one count, exact sole-URL shape decision, optional close

Run this exact cell once. Eligibility is consumed before the binding check or
first browser call. It lists once. Count zero proves zero tabs without get or
close. Count one permits get/close only when the sole URL is exactly
`http://127.0.0.1:<port>/omni-preflight-v5-<32 lowercase hex>`, where port is
decimal 1 through 65535 without a leading zero. Count greater than one or a
sole-tab mismatch stops without get or close.

```javascript
let residualV5DispositionEligible = true;
await (async () => {
  const safeErrorClass = (error, fallback) => {
    const name = typeof error?.name === "string" ? error.name : "";
    return /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(name) ? name : fallback;
  };
  const eligible = residualV5DispositionEligible === true;
  residualV5DispositionEligible = false;
  let result = "PRECONDITION_FAILED";
  let errorClass = "NONE";
  let enumerationAttempted = 0;
  let enumerationFulfilled = 0;
  let tabCount = -1;
  let soleUrlShapeMatched = false;
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
  } else if (typeof residualV5Chrome === "undefined" || residualV5Chrome === null) {
    result = "CHROME_BINDING_MISSING";
  } else {
    enumerationAttempted++;
    result = "ENUMERATION_UNCERTAIN";
    try {
      tabInfos = await residualV5Chrome.tabs.list();
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
          if (soleInfo === null || typeof soleInfo !== "object" || typeof soleInfo.id !== "string" || soleInfo.id.length === 0 || soleInfo.id.length > 512 || typeof soleInfo.url !== "string") {
            result = "SOLE_TAB_INFO_INVALID";
          } else {
            const match = /^http:\/\/127\.0\.0\.1:([1-9][0-9]{0,4})\/omni-preflight-v5-[0-9a-f]{32}$/.exec(soleInfo.url);
            soleUrlShapeMatched = match !== null && Number(match[1]) <= 65535;
            if (!soleUrlShapeMatched) {
              result = "SOLE_TAB_MISMATCH_STOP";
            } else {
              getAttempted++;
              result = "GET_UNCERTAIN";
              try {
                soleTab = await residualV5Chrome.tabs.get(soleInfo.id);
                getFulfilled++;
                if (soleTab === null || (typeof soleTab !== "object" && typeof soleTab !== "function") || typeof soleTab.close !== "function") {
                  result = "GET_INVALID";
                } else {
                  closeAttempted++;
                  result = "CLOSE_UNCERTAIN";
                  try {
                    await soleTab.close();
                    closeFulfilled++;
                    zeroTabsProven = true;
                    result = "MATCHED_SOLE_TAB_CLOSED";
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
    soleUrlShapeMatched,
    getAttempted,
    getFulfilled,
    closeAttempted,
    closeFulfilled,
    zeroTabsProven
  });
})();
```

Exact accepted outcomes are only:

- `ZERO_TABS_ALREADY`: error `NONE`, enumeration `1 / 1`, count `0`, shape
  false, get `0 / 0`, close `0 / 0`, and `zeroTabsProven=true`; or
- `MATCHED_SOLE_TAB_CLOSED`: error `NONE`, enumeration `1 / 1`, count `1`,
  shape true, get `1 / 1`, close `1 / 1`, and `zeroTabsProven=true`.

`SOLE_TAB_MISMATCH_STOP` requires enumeration `1 / 1`, count `1`, shape false,
get `0 / 0`, close `0 / 0`, and zero proof false. `MULTIPLE_TABS_STOP`
requires count greater than `1`, get/close `0 / 0`, and zero proof false. Both
stop without Call 3. Any binding/API/object/schema/counter uncertainty or
missing/malformed/rejected/tool-uncertain output is FAIL / NOT PROVEN.

## Call 3 — one clipboard clear and one empty read

Run this exact PowerShell 7 block once only after an exact accepted Call 2
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
    $name = $_.Exception.GetType().Name
    $errorClass = if ($name -cmatch '^[A-Za-z][A-Za-z0-9_.-]{0,63}$') { $name } else { 'ERROR' }
} finally {
    $currentClipboard = $null
}
'RESIDUAL_V5_CLIPBOARD_CLEAR_ATTEMPTED=' + $clearAttempted
'RESIDUAL_V5_CLIPBOARD_CLEAR_FULFILLED=' + $clearFulfilled
'RESIDUAL_V5_CLIPBOARD_EMPTY_READ_ATTEMPTED=' + $emptyReadAttempted
'RESIDUAL_V5_CLIPBOARD_EMPTY_READ_FULFILLED=' + $emptyReadFulfilled
'RESIDUAL_V5_CLIPBOARD_EMPTY=' + $clipboardEmpty.ToString().ToUpperInvariant()
'RESIDUAL_V5_CLIPBOARD_ERROR=' + $errorClass
if ($clearAttempted -eq 1 -and $clearFulfilled -eq 1 -and $emptyReadAttempted -eq 1 -and $emptyReadFulfilled -eq 1 -and $clipboardEmpty -and $errorClass -eq 'NONE') { exit 0 }
exit 2
```

Clipboard PASS requires exit 0, all four counters exactly 1, empty true, and
error `NONE`. Every other state is FAIL / NOT PROVEN and permits no second
clear/read.

## Residual and reporting boundary

This contract performs no listener/server/process inspection or action. Both
the unrelated old v3 listener/process and the uncertain v5 listener/process
remain `NOT PROVEN` after every outcome. Browser-tab disposition plus current
clipboard empty proof cannot establish listener/process absence.

The future report may contain only pins, timestamps, safe result/error classes,
numeric counters, count, URL-shape-match boolean, zero-tabs proof, clipboard
empty proof, and both listener/process residuals as `NOT PROVEN`. It must emit
no ID, URL, title, content, metadata, object, handle, clipboard value,
challenge, secret, credential, key, or token. Static PASS authorizes no live
execution; independent PASS and action-time pins remain mandatory.
