# Task 2 secure-console transfer — fresh-Chrome replacement amendment

`authorizes_live_execution=false`

Status: fresh static candidate for independent Sol High review. This document
does not retry, continue, restore, or execute the closed retained-binding
contract. It performs and authorizes no Chrome connection, tab enumeration,
browser mutation, clipboard action, credential action, process action,
Cloudflare action, VM action, proxy action, routing action, or deletion.

## Exact pins and disposition

- Closed approved live brief commit:
  `7af3ab75ec87d81d75811ff8f2e9b4fa9d0c3e3b`; exact file `62054` bytes,
  SHA-256
  `995CA4D59E564EAF53417B9F577808F9C307C5CDEE93FB8E91DC73A5211F52CC`.
- Independent PASS review commit:
  `ce47c2eacb5a5cbf055c3fc814137e46c1855e40`; exact review file
  `task-2-secure-console-transfer-live-fix2-sol-review.md`, `10082` bytes,
  SHA-256
  `2DB6E77877B49AE751733A5CD5682F85A078F06EA0D20C8249E7D2EC34D5A01F`.
- Drift report commit `e670c64d9945d9b92ae318f1cd7a16956e57c963`;
  exact report `1998` bytes, SHA-256
  `F8CBA72AB2322CEB0206C94182CAB0A686A74AE954C527617096E2D0B5E9A07B`.
- Drift classification commit
  `f65b21278caf23326af3de570f265cea54d907c5`; exact classification
  `8392` bytes, SHA-256
  `6FBDC067A6863BFCA4648B6F1A14F354FECD7FD50DF8CDF9262CA2FA046A29BB`.
- Installed Chrome control version: exact `26.825.51511`. Its unmodified
  `skills/control-chrome/SKILL.md` is `12813` bytes, SHA-256
  `3359692CE61D149B01EE21812A9F9E7381B060A35C28FDA8493057CBE90C0C3A`.
- Exact native bootstrap module:
  `C:\Users\chatc\.codex\plugins\cache\openai-bundled\chrome\26.825.51511\scripts\browser-client.mjs`,
  `149210` bytes, SHA-256
  `C52BA09202F0E82CAA6F6D2A6463A8635C1B1316567975D9B91C1A05FB5AF501`.
- Installed API reference `docs/api.json`: `58477` bytes, SHA-256
  `4BFEB97E958025DB37D52AEA11B75BC70BCA417B4995B0F711C0F07F3DDCCB08`;
  it documents `Browser.documentation(): Promise<string>` and
  `Tabs.list(): Promise<Array<TabInfo>>`.
- Future redacted report:
  `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-fresh-chrome-replacement-report.md`.
- Future independent classification:
  `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-fresh-chrome-replacement-classification.md`.

The prior action-time lookup was compliant and the credential-consuming gate
remains unconsumed, but the old approved contract is closed and ineligible.
The missing historical object is never recreated. This is a new one-shot
connection amendment with new identity and new review requirements.

## Authority and one-shot boundary

Only the sole Sol High live owner may later consume this amendment, in the
same current persistent JavaScript session that will retain the new object.
Before any call, it must pin this amendment, its independent PASS, the exact
installed skill/bootstrap bytes above, current Git/index/baseline state, and
the intended existing user Chrome session. The user must visually confirm that
the installed ChatGPT browser extension is attached to that intended Chrome
profile/window; the contract performs no profile, cookie, storage, password,
or session-metadata inspection. The project standing authority applies only
after those pins. This static document alone grants no live authority.

The amendment permits exactly:

1. one bootstrap of the pinned native module and one
   `agent.browsers.get("chrome")` fresh connection attempt;
2. the required complete documentation emission for that selected Chrome
   object; then
3. only after exact connection success, one `tabs.list()` call whose returned
   array is used solely for its integer length and immediately released.

There is no JavaScript-session reset, second import/bootstrap, second browser
selection, reconnect, alternate family/default/extension selector, browser
list, fallback, recovery documentation path, reacquisition, object alias,
serialization, task/process handoff, or substitution. There is no use or
creation of `residualV5Chrome`, and no global-name scan. Any rejected,
malformed, interrupted, timed-out, missing, wrong-session, tool-uncertain, or
non-exact output spends this new amendment and stops before tab mutation and
all later Task 2 action. A nonzero tab count also stops; closing or inspecting
those tabs would require a separate independently reviewed cleanup contract.

## Call 1 — sole fresh Chrome connection

The sole owner invokes the JavaScript tool once with this exact cell in the
current persistent session. The absolute module path, stable Chrome family
selector, fresh binding name, and direct complete documentation call are
load-bearing. The documentation output is setup documentation only; it is not
browser/session/tab metadata. The cell's terminal value must match the fixed
redacted schema below. Use one `60000 ms` tool-control deadline. If the
JavaScript tool is called through code-mode orchestration, the outer call must
begin with exact first-line pragma
`// @exec: {"max_output_tokens": 20000}` and forward the complete
`nodeRepl.write` result; truncation is failure.

```javascript
const { setupBrowserRuntime: secureConsoleSetupBrowserRuntimeV1 } = await import("C:/Users/chatc/.codex/plugins/cache/openai-bundled/chrome/26.825.51511/scripts/browser-client.mjs");
const secureConsoleAgentV1 = await secureConsoleSetupBrowserRuntimeV1();
let secureConsoleChromeV1 = null;
let secureConsoleChromeV1ConnectAttempted = 0;
let secureConsoleChromeV1ConnectFulfilled = 0;
let secureConsoleChromeV1DocumentationAttempted = 0;
let secureConsoleChromeV1DocumentationFulfilled = 0;
let secureConsoleChromeV1ConnectedShape = false;
let secureConsoleChromeV1ConnectErrorClass = "NONE";
try {
  secureConsoleChromeV1ConnectAttempted++;
  secureConsoleChromeV1 = await secureConsoleAgentV1.browsers.get("chrome");
  secureConsoleChromeV1ConnectFulfilled++;
  secureConsoleChromeV1ConnectedShape = !!secureConsoleChromeV1 &&
    typeof secureConsoleChromeV1.documentation === "function" &&
    !!secureConsoleChromeV1.tabs &&
    typeof secureConsoleChromeV1.tabs.list === "function";
  if (!secureConsoleChromeV1ConnectedShape) throw new Error("SAFE_SHAPE_FAILURE");
  secureConsoleChromeV1DocumentationAttempted++;
  nodeRepl.write(await secureConsoleChromeV1.documentation());
  secureConsoleChromeV1DocumentationFulfilled++;
} catch {
  secureConsoleChromeV1ConnectErrorClass = "FRESH_CHROME_CONNECT_OR_DOCUMENTATION_FAILED";
}
const secureConsoleChromeV1ConnectExact =
  secureConsoleChromeV1ConnectAttempted === 1 &&
  secureConsoleChromeV1ConnectFulfilled === 1 &&
  secureConsoleChromeV1DocumentationAttempted === 1 &&
  secureConsoleChromeV1DocumentationFulfilled === 1 &&
  secureConsoleChromeV1ConnectedShape === true &&
  secureConsoleChromeV1ConnectErrorClass === "NONE";
({
  result: secureConsoleChromeV1ConnectExact ? "EXACT_FRESH_CHROME_CONNECTED" : "FRESH_CHROME_CONNECTION_FAILED_STOP",
  connectAttempted: secureConsoleChromeV1ConnectAttempted,
  connectFulfilled: secureConsoleChromeV1ConnectFulfilled,
  documentationAttempted: secureConsoleChromeV1DocumentationAttempted,
  documentationFulfilled: secureConsoleChromeV1DocumentationFulfilled,
  connectedShape: secureConsoleChromeV1ConnectedShape,
  errorClass: secureConsoleChromeV1ConnectErrorClass
});
```

Exact success requires terminal `EXACT_FRESH_CHROME_CONNECTED`, counters
`1 / 1` and `1 / 1`, `connectedShape=true`, and `errorClass=NONE`, with the
complete documentation output delivered and read. Tool-output truncation,
missing terminal fields, extra unsafe fields, or any ambiguity is failure.
The exact non-null `secureConsoleChromeV1` object and `secureConsoleAgentV1`
remain retained in this same owner/session. They are never renamed or copied.

## Call 2 — sole count-only enumeration

Only after exact Call 1 success, the same sole owner invokes this exact second
cell in the same persistent session. It does not inspect, iterate, serialize,
filter, map, log, or emit any element. The temporary array is nulled in
`finally`; only its integer count enters the redacted terminal. Use one
`30000 ms` tool-control deadline.

```javascript
let secureConsoleChromeV1TabListAttempted = 0;
let secureConsoleChromeV1TabListFulfilled = 0;
let secureConsoleChromeV1TabListShapeValid = false;
let secureConsoleChromeV1TabCount = -1;
let secureConsoleChromeV1TabInfos = null;
let secureConsoleChromeV1TabListErrorClass = "NONE";
if (secureConsoleChromeV1ConnectExact === true && secureConsoleChromeV1 !== null) {
  try {
    secureConsoleChromeV1TabListAttempted++;
    secureConsoleChromeV1TabInfos = await secureConsoleChromeV1.tabs.list();
    secureConsoleChromeV1TabListFulfilled++;
    secureConsoleChromeV1TabListShapeValid = Array.isArray(secureConsoleChromeV1TabInfos);
    if (!secureConsoleChromeV1TabListShapeValid) throw new Error("SAFE_LIST_SHAPE_FAILURE");
    secureConsoleChromeV1TabCount = secureConsoleChromeV1TabInfos.length;
  } catch {
    secureConsoleChromeV1TabListErrorClass = "COUNT_ONLY_TAB_LIST_FAILED";
  } finally {
    secureConsoleChromeV1TabInfos = null;
  }
} else {
  secureConsoleChromeV1TabListErrorClass = "CONNECT_PRECONDITION_NOT_EXACT";
}
const secureConsoleChromeV1ZeroTabsExact =
  secureConsoleChromeV1TabListAttempted === 1 &&
  secureConsoleChromeV1TabListFulfilled === 1 &&
  secureConsoleChromeV1TabListShapeValid === true &&
  Number.isInteger(secureConsoleChromeV1TabCount) &&
  secureConsoleChromeV1TabCount === 0 &&
  secureConsoleChromeV1TabListErrorClass === "NONE";
({
  result: secureConsoleChromeV1ZeroTabsExact ? "EXACT_FRESH_CHROME_ZERO_TABS" : "FRESH_CHROME_TAB_PRECONDITION_FAILED_STOP",
  tabListAttempted: secureConsoleChromeV1TabListAttempted,
  tabListFulfilled: secureConsoleChromeV1TabListFulfilled,
  tabListShapeValid: secureConsoleChromeV1TabListShapeValid,
  tabCount: secureConsoleChromeV1TabCount,
  errorClass: secureConsoleChromeV1TabListErrorClass
});
```

Exact success requires terminal `EXACT_FRESH_CHROME_ZERO_TABS`, list counters
`1 / 1`, valid array shape, integer `tabCount=0`, and `errorClass=NONE`.
The `-1` integer is only the fixed unknown/failure sentinel. No tab handle,
ID, title, URL, favicon, metadata, DOM, content, screenshot, or array enters
output. Calls to `tabs.get`, `tabs.new`, tab close, navigation, Playwright,
clipboard, keyboard, evaluation, or any other browser API are exactly zero.

## Sole amendment to the approved live brief

If and only if both calls have exact success, this document supersedes only
the approved brief's Chrome precondition clause at lines 158–159. Interpret it
as follows:

> `secureConsoleChromeV1` is the exact newly connected, non-null, retained
> Chrome object in the sole owner's same persistent JavaScript session; its one
> count-only `tabs.list()` returned integer zero. No reconnect or tab metadata
> output occurred.

The identifier `secureConsoleChromeV1` replaces `residualV5Chrome` only in that
single clause. The approved brief file is not edited. Every other byte-level
pin, target, permission, counter, owner/R5 script, deadline, confirmation,
revocation, cleanup, evidence, failure, and exclusion contract in commit
`7af3ab75ec87d81d75811ff8f2e9b4fa9d0c3e3b` remains intact and mandatory.

## Complete fresh action-time revalidation

Connection/count success is necessary but not sufficient. Before proxy start,
script preparation, owner launch, final Create, or any other consuming action,
the same sole owner must freshly revalidate the complete approved precondition
set in its original serial order:

- exact amendment/PASS plus approved brief/PASS, deterministic R5, proxy proof,
  Caddy, bundled pwsh, Chrome skill, and bootstrap bytes/hashes;
- evidence worktree clean at exact
  `80adaa7d5d63d1d2c7bfa63b236c6bee93b3b1d8`, Git index empty, and the pinned
  unrelated baseline unchanged;
- Windows CIM/registry identity exactly as approved: Windows 11 Pro,
  `10.0.26200` / build `26200`, x64, registry ProductName `Windows 10 Pro`,
  EditionID `Professional`, DisplayVersion `25H2`, UBR `9278`;
- fresh read-only machine policy proof: both values present as DWORD and exact
  `AllowClipboardHistory=0` / `AllowCrossDeviceClipboard=0`;
- exactly one Windows current-clipboard clear/read-empty proof with
  attempted/fulfilled `1 / 1`, shape-only read `1 / 1`, empty `TRUE`, no retry,
  and no history-erasure claim;
- exact retained `secureConsoleChromeV1` identity plus the already consumed
  sole count result `0`; no second enumeration or connection;
- VM1205 existing `omniroute` and `bell-cloudflare-proxy` running; target
  `team-api-proxy` and team Tunnel absent; network members `2`; host listener
  `20130` absent; retained Caddy SHA-256
  `A31C2010BB47767E25A826CEBCD2469CB51D8AF5C5AE089E46D2051EDD69D9BB`;
- authenticated Cloudflare safe-count reads: exactly one unrelated
  `http_ratelimit` rule, zero target description/expression matches, target
  DNS/Tunnel/connector absent, overlapping Access application absent, exact
  token-name count `0`, and exact matching-row count `0`;
- OmniRoute `team-rollout-test` key absent; and
- exact zone `mysw.me`, hostname `ai-api-omniroute.mysw.me`, fixed rule
  description/expression/action/characteristics, fixed unique token name,
  specific-zone scope, and exactly `Zone WAF Edit` plus `Zone Read` unchanged.

Fresh proof emits only safe counts, booleans, fixed labels/names, hashes, and
residual classes. It emits no browser metadata, clipboard bytes, credential,
Zone/account/rule/token ID, Authorization header, provider response body, DOM,
page content, screenshot, or private process data. Any drift or uncertainty
stops before later action and spends this amendment without retry.

## Preserved confirmations, lifecycle, and exclusions

The sole Sol High owner and fixed owner process remain mandatory. The separate
action-time user confirmation immediately before final Cloudflare Create plus
user-native semantic Copy and masked Paste remains mandatory. The separate
action-time confirmation for deletion of the exact fixed token row remains
mandatory. Standing authority and either static PASS waive neither.

The approved same-process masked input, exact one clipboard cleanup, private
Zone lookup, sole exact-hash bounded R5 child, launch-time owner deadline,
universal post-accept revocation hold, exact-row refreshed `0 / 0`, retained
token HTTP `401`, guarded cleanup, redaction, no retry/fallback/handoff, and
fail-closed residual rules remain unchanged.

No Tunnel, DNS/public hostname, Access creation, team/rollout key, model
request, provider/routing change, OmniRoute restart, Bell change, VM power
action, permission expansion, credential output, evidence mutation, old
listener/process inspection, or unrelated deletion is added. After final
Create, all approved browser/Computer-Use/DOM/screenshot/clipboard prohibitions
remain exact.

## Static acceptance

Independent direct-byte Sol High review must verify:

- strict UTF-8 without BOM, LF-only, one trailing LF, exact Git/index/baseline,
  and only this new path changed;
- installed skill/bootstrap existence, bytes, SHA-256, and version path;
- both JavaScript fences parse as modules without evaluation;
- exactly one pinned bootstrap import, one `setupBrowserRuntime()`, one
  `browsers.get("chrome")`, one direct complete `documentation()` call, and one
  `tabs.list()`;
- zero `getDefault`, `getForUrl`, extension/Edge/IAB selection, browser list,
  reset, alternate import, reconnect, alias, tab get/new/close, navigation,
  Playwright, clipboard, keyboard, screenshot, serialization, or metadata
  output operations;
- exact new binding name and same-session retention; executable code contains no
  `residualV5Chrome` or `globalThis`;
- fixed redacted schemas/counters, count-only array release, exact-zero gate,
  complete fresh revalidation list, mandatory confirmations, preserved
  deadlines/revocation, and `authorizes_live_execution=false`.

Parser checks must not import or evaluate either cell and must perform no live
action. Only a new committed amendment plus fresh independent PASS and exact
action-time pins can make the one connection attempt eligible. This document
itself remains static and non-executing.
