# Task 2 secure-console token-page readiness V5 fresh-session reacquisition brief

Status: **PROPOSED — offline contract only; not executable until independent Sol High PASS review, non-self-referential execution classification, and post-commit coordinator tuple**

`authorizes_live_execution=false`

## Purpose and exact predecessor boundary

This is the smallest fresh-session replacement for only the task-local Chrome
attachment and retained-tab adoption boundary in V4. It does not retry,
continue, repair, reinterpret, or execute V3 or V4.

- Safe-pause base commit:
  `a32c53c2d5fba3940e44af691bcd8feae75d1681`, direct parent
  `7e2bf2341d88113536507298b3df8f1f25e8f417`.
- Consumed V3 incident:
  `172da50d2b841398c6e4c1d55942e3f6a75d38eb`; exact incident file `5104`
  bytes, SHA-256
  `E57C82BA099832C4FFD2EB096CE7439288F8688E75C19D1A0F29AA1BA6FD1CFD`.
- Static V4 brief commit:
  `82971f2d7165325b616dab293e275cb7287d1914`; exact brief `54334` bytes,
  SHA-256
  `89E52D8157677821FC44E84CFCABFC4AEB01A1F9CF23D0DDBCD31E56085B8EE8`.
- Independent V4 Sol High PASS review commit:
  `7e2bf2341d88113536507298b3df8f1f25e8f417`; exact review `7813` bytes,
  SHA-256
  `547449928E647AE5E229A4ECAEEF4BFD9473410F494BE1B88E0197F9FD7ACADB`;
  `authorizes_live_execution=false`.
- Inherited live-owner brief: exact file `62054` bytes, SHA-256
  `995CA4D59E564EAF53417B9F577808F9C307C5CDEE93FB8E91DC73A5211F52CC`.

V3 remains `V3_ADOPTION_OR_READINESS_FAILED / GATE_AND_DISPOSITION_SPENT /
NO_CONTINUATION`. V4 remains static evidence only. No persistent Node, agent,
Chrome, tab, or V2/V3/V4 declaration is inherited into this task.

## Selected minimal mechanism

The installed Chrome API exposes
`Tabs.selected(): Promise<undefined | Tab>`. V5 therefore performs:

1. one pinned bootstrap and one exact `agent.browsers.get("chrome")` call;
2. the required complete documentation emission and read;
3. only after exact attachment PASS, one `chrome.tabs.selected()` call; and
4. V4's title-free semantic navigation/readiness proof against that one
   freshly bound selected tab.

There is no `browsers.list`, `getDefault`, `getForUrl`, `get("extension")`,
`tabs.list`, `user.openTabs`, `user.claimTab`, `tabs.get`, `tabs.new`, second
selection, reconnect, retry, fallback, alternate browser, tab ID handoff,
profile inspection, cookie/storage/password/session inspection, screenshot,
DOM serialization, clipboard action, keyboard action, Create/edit/delete,
provider mutation, process start, VM action, proxy action, routing action, or
credential action.

Immediately before a future live Call 1, the user must visually confirm that
the ChatGPT browser extension is attached to Chrome Profile
`Codex-Chrome-Bell-PC2`, that the intended task tab in that profile is selected,
and that no other Chrome profile/window is being offered to the extension. The
contract never reads profile metadata. This is an attachment precondition, not
the later combined Create/native Copy/native masked Paste authority.

## Exact installed runtime pins

- Chrome control version: `26.825.51511`.
- `skills/control-chrome/SKILL.md`: `12813` bytes, SHA-256
  `3359692CE61D149B01EE21812A9F9E7381B060A35C28FDA8493057CBE90C0C3A`.
- `scripts/browser-client.mjs`: `149210` bytes, SHA-256
  `C52BA09202F0E82CAA6F6D2A6463A8635C1B1316567975D9B91C1A05FB5AF501`.
- `docs/api.json`: `58477` bytes, SHA-256
  `4BFEB97E958025DB37D52AEA11B75BC70BCA417B4995B0F711C0F07F3DDCCB08`.

Any byte, version, capability, documentation, worktree, index, dirty-baseline,
profile/window confirmation, Prox-01, VM1205, DNS, provider, or coordinator-pin
drift stops before Call 1 and requires a new independently reviewed contract.

## Fresh one-shot state and completeness rule

Both calls run only in the sole Sol High owner task and the same persistent
JavaScript session. Call 1 has one `60000 ms` tool-control deadline. Call 2 has
one `60000 ms` tool-control deadline. Missing, rejected, interrupted, timed-out,
truncated, malformed, uncertain, or non-exact output spends V5 and permits no
later browser or cleanup call.

Every emitted terminal must be complete and the tool status completed. Output
is fixed redacted metadata only. No tab ID, browser ID, URL other than the
fixed public navigation target, title, page content, DOM, selector result,
href, account/zone/rule identifier, token, credential, clipboard bytes, header,
response body, or exception message may be emitted or persisted.

## Call 1 — sole fresh-session Chrome attachment

The code-mode outer call, if used, begins with exact first-line pragma
`// @exec: {"max_output_tokens": 20000}` and forwards the complete required
documentation output. The direct documentation call is load-bearing.

```javascript
const { setupBrowserRuntime: secureConsoleSetupBrowserRuntimeV5 } = await import("C:/Users/chatc/.codex/plugins/cache/openai-bundled/chrome/26.825.51511/scripts/browser-client.mjs");
const secureConsoleAgentV5 = await secureConsoleSetupBrowserRuntimeV5();
let secureConsoleChromeV5 = null;
let secureConsoleV5AttachmentConsumed = false;
let secureConsoleV5AttachmentExact = false;
let secureConsoleV5ConnectAttempted = 0;
let secureConsoleV5ConnectFulfilled = 0;
let secureConsoleV5DocumentationAttempted = 0;
let secureConsoleV5DocumentationFulfilled = 0;
let secureConsoleV5ConnectedShape = false;
let secureConsoleV5AttachmentErrorClass = "NONE";
await (async () => {
  if (secureConsoleV5AttachmentConsumed !== false) {
    secureConsoleV5AttachmentErrorClass = "ATTACHMENT_ALREADY_CONSUMED";
  } else {
    try {
      secureConsoleV5ConnectAttempted++;
      secureConsoleChromeV5 = await secureConsoleAgentV5.browsers.get("chrome");
      secureConsoleV5ConnectFulfilled++;
      secureConsoleV5ConnectedShape =
        typeof secureConsoleChromeV5 === "object" && secureConsoleChromeV5 !== null &&
        typeof secureConsoleChromeV5.documentation === "function" &&
        typeof secureConsoleChromeV5.tabs?.selected === "function";
      if (!secureConsoleV5ConnectedShape) throw new Error("FreshChromeShapeError");
      secureConsoleV5DocumentationAttempted++;
      nodeRepl.write(await secureConsoleChromeV5.documentation());
      secureConsoleV5DocumentationFulfilled++;
    } catch {
      secureConsoleV5AttachmentErrorClass = "FRESH_CHROME_ATTACHMENT_OR_DOCUMENTATION_FAILED";
    }
    secureConsoleV5AttachmentConsumed = true;
  }
  secureConsoleV5AttachmentExact =
    secureConsoleV5AttachmentConsumed === true &&
    secureConsoleV5ConnectAttempted === 1 &&
    secureConsoleV5ConnectFulfilled === 1 &&
    secureConsoleV5DocumentationAttempted === 1 &&
    secureConsoleV5DocumentationFulfilled === 1 &&
    secureConsoleV5ConnectedShape === true &&
    secureConsoleV5AttachmentErrorClass === "NONE";
  if (!secureConsoleV5AttachmentExact) secureConsoleChromeV5 = null;
  nodeRepl.write({
    result: secureConsoleV5AttachmentExact ? "EXACT_V5_FRESH_CHROME_ATTACHMENT_PASS" : "V5_FRESH_CHROME_ATTACHMENT_FAILED_STOP",
    consumed: secureConsoleV5AttachmentConsumed,
    connectAttempted: secureConsoleV5ConnectAttempted,
    connectFulfilled: secureConsoleV5ConnectFulfilled,
    documentationAttempted: secureConsoleV5DocumentationAttempted,
    documentationFulfilled: secureConsoleV5DocumentationFulfilled,
    connectedShape: secureConsoleV5ConnectedShape,
    errorClass: secureConsoleV5AttachmentErrorClass,
  });
})();
```

Exact PASS requires result `EXACT_V5_FRESH_CHROME_ATTACHMENT_PASS`, consumed
true, connect `1/1`, documentation `1/1`, connected shape true, error class
`NONE`, complete documentation output, complete terminal output, and completed
tool status. Any other result spends V5 and stops.

## Call 2 — selected-tab reacquisition plus V4 semantic readiness

Call 2 is permitted only after exact Call 1 PASS in the same session. It calls
`tabs.selected()` exactly once. `undefined`, a malformed tab, uncertainty, or
any semantic mismatch fails closed. It creates no tab, so completed failure
leaves no created-tab residue. It leaves the V4-compatible binding established
by V5 null and ineligible on every completed non-PASS.

```javascript
let secureConsoleOwnedTaskTabV4 = null;
let secureConsoleOwnedTaskTabV4Eligible = false;
let secureConsoleOwnedTaskTabV4State = "UNADOPTED";
let secureConsoleOwnedTaskTabV4PreCreateDetachConsumed = false;
let secureConsoleOwnedTaskTabV4PostNativeDetachConsumed = false;
let secureConsoleCloudflareReadsV4Consumed = false;
let secureConsoleV4AdoptionConsumed = false;
await (async () => {
  const counters = {
    selectedAttempted: 0,
    selectedFulfilled: 0,
    navigationAttempted: 0,
    navigationFulfilled: 0,
    urlAttempted: 0,
    urlFulfilled: 0,
    readinessAttempted: 0,
    readinessFulfilled: 0,
    fillAttempted: 0,
    fillFulfilled: 0,
    createAttempted: 0,
    createFulfilled: 0,
    nameAttempted: 0,
    nameFulfilled: 0,
    rowAttempted: 0,
    rowFulfilled: 0,
    writeAttempted: 0,
  };
  let result = "PRECONDITION_FAIL";
  let errorClass = "NONE";
  let declarationShape = false;
  let predecessorStateExact = false;
  let controllerOwnership = false;
  let tabShape = false;
  let navigationTargetExact = false;
  let createControlCount = -1;
  let tokenNameCount = -1;
  let matchingRowCount = -1;
  let tokenInitialFilterEmpty = false;
  let tokenQueryEchoCount = -1;
  let tokenFilterComplete = false;
  let tokenSemanticSignature = false;
  let adopted = null;
  const safeErrorClass = (error) => {
    const name = typeof error?.name === "string" ? error.name : "";
    return /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(name) ? name : "TokenPageSemanticReadinessError";
  };
  try {
    declarationShape =
      typeof secureConsoleAgentV5 === "object" && secureConsoleAgentV5 !== null &&
      typeof secureConsoleChromeV5 === "object" && secureConsoleChromeV5 !== null &&
      typeof secureConsoleChromeV5.tabs?.selected === "function" &&
      typeof secureConsoleV5AttachmentConsumed === "boolean" &&
      typeof secureConsoleV5AttachmentExact === "boolean";
    if (!declarationShape) throw new Error("FreshSessionDeclarationShapeError");
    predecessorStateExact =
      secureConsoleV5AttachmentConsumed === true &&
      secureConsoleV5AttachmentExact === true &&
      secureConsoleV5ConnectAttempted === 1 &&
      secureConsoleV5ConnectFulfilled === 1 &&
      secureConsoleV5DocumentationAttempted === 1 &&
      secureConsoleV5DocumentationFulfilled === 1 &&
      secureConsoleV5ConnectedShape === true &&
      secureConsoleV5AttachmentErrorClass === "NONE" &&
      secureConsoleV4AdoptionConsumed === false;
    if (!predecessorStateExact) throw new Error("FreshSessionPredecessorStateError");

    counters.selectedAttempted++;
    adopted = await secureConsoleChromeV5.tabs.selected();
    counters.selectedFulfilled++;
    controllerOwnership = typeof adopted === "object" && adopted !== null && typeof adopted.id === "string";
    tabShape =
      controllerOwnership &&
      typeof adopted.goto === "function" &&
      typeof adopted.url === "function" &&
      typeof adopted.playwright?.getByRole === "function" &&
      typeof adopted.playwright?.getByText === "function";
    if (!tabShape) throw new Error("SelectedTabOwnershipError");

    counters.navigationAttempted++;
    await adopted.goto("https://dash.cloudflare.com/profile/api-tokens");
    counters.navigationFulfilled++;
    counters.urlAttempted++;
    const tokenUrl = new URL(await adopted.url());
    counters.urlFulfilled++;
    navigationTargetExact = tokenUrl.href === "https://dash.cloudflare.com/profile/api-tokens";
    if (!navigationTargetExact) throw new Error("TokenNavigationTargetError");

    const tokenFilter = adopted.playwright.getByRole("textbox", { name: /search api tokens/i });
    if (await tokenFilter.count() !== 1) throw new Error("TokenFilterCountError");
    const tokenRegionId = await tokenFilter.getAttribute("aria-controls");
    if (typeof tokenRegionId !== "string" || !/^[A-Za-z][A-Za-z0-9_-]{0,127}$/.test(tokenRegionId)) throw new Error("TokenRegionBindingError");
    const tokenResultsRoot = adopted.playwright.locator(`#${tokenRegionId}`);
    if (await tokenResultsRoot.count() !== 1) throw new Error("TokenResultsRootCountError");
    const tokenPaginator = tokenResultsRoot.locator('[aria-label="Pagination"]');
    if (await tokenPaginator.count() !== 1) throw new Error("TokenPaginatorCountError");
    counters.readinessAttempted++;
    await tokenPaginator.waitFor({ state: "visible", timeoutMs: 20000 });
    counters.readinessFulfilled++;
    tokenInitialFilterEmpty = await tokenFilter.evaluate((input) => input.value === "");
    if (!tokenInitialFilterEmpty) throw new Error("TokenInitialFilterStateError");
    const tokenBaseline = await tokenResultsRoot.evaluate((root) => {
      const pager = root.querySelector('[aria-label="Pagination"]');
      const match = /^(\d+)\s*[-–]\s*(\d+)\s+of\s+(\d+)$/.exec((pager?.textContent || "").replace(/\s+/g, " ").trim());
      const rows = root.querySelectorAll("table tbody tr").length;
      const busy = root.matches('[aria-busy="true"]') || root.querySelector('[aria-busy="true"]') !== null;
      const statuses = [...root.querySelectorAll('[role="status"]')].filter((item) => /^(?:no api tokens found|no tokens found)$/i.test((item.textContent || "").trim()));
      const buttons = pager === null ? [] : [...pager.querySelectorAll("button")];
      const next = buttons.filter((item) => item.getAttribute("aria-label") === "Next page");
      const previous = buttons.filter((item) => item.getAttribute("aria-label") === "Previous page");
      const disabled = (item) => item.hasAttribute("disabled") || item.getAttribute("aria-disabled") === "true";
      if (busy || match === null || next.length !== 1 || previous.length !== 1) return { terminalZero: false, completeNonempty: false };
      const start = Number(match[1]), end = Number(match[2]), total = Number(match[3]);
      return {
        terminalZero: start === 0 && end === 0 && total === 0 && rows === 0 && statuses.length === 1 && disabled(next[0]) && disabled(previous[0]),
        completeNonempty: start === 1 && end === rows && total >= rows && rows > 0 && statuses.length === 0 && disabled(previous[0]) && disabled(next[0]) === (end >= total),
      };
    });
    if (!tokenBaseline.terminalZero && !tokenBaseline.completeNonempty) throw new Error("TokenBaselineIncompleteError");

    counters.fillAttempted++;
    await tokenFilter.fill("OmniRoute secure console R5 20260901");
    counters.fillFulfilled++;
    const tokenQueryEcho = tokenResultsRoot.getByText("OmniRoute secure console R5 20260901", { exact: true });
    counters.readinessAttempted++;
    await tokenQueryEcho.waitFor({ state: "visible", timeoutMs: 20000 });
    counters.readinessFulfilled++;
    tokenQueryEchoCount = await tokenQueryEcho.count();
    if (tokenQueryEchoCount !== 1) throw new Error("TokenQueryEchoCountError");
    const tokenEmptyStatus = tokenResultsRoot.getByRole("status").filter({ hasText: /^(?:no api tokens found|no tokens found)$/i });
    counters.readinessAttempted++;
    await tokenEmptyStatus.waitFor({ state: "visible", timeoutMs: 20000 });
    counters.readinessFulfilled++;
    if (await tokenEmptyStatus.count() !== 1) throw new Error("TokenEmptyStatusCountError");
    const tokenValueExact = await tokenFilter.evaluate((input) => input.value === "OmniRoute secure console R5 20260901");
    const tokenTerminal = await tokenResultsRoot.evaluate((root) => {
      const pager = root.querySelector('[aria-label="Pagination"]');
      const match = /^(\d+)\s*[-–]\s*(\d+)\s+of\s+(\d+)$/.exec((pager?.textContent || "").replace(/\s+/g, " ").trim());
      const rows = root.querySelectorAll("table tbody tr").length;
      const statuses = [...root.querySelectorAll('[role="status"]')].filter((item) => /^(?:no api tokens found|no tokens found)$/i.test((item.textContent || "").trim()));
      const buttons = pager === null ? [] : [...pager.querySelectorAll("button")];
      const next = buttons.filter((item) => item.getAttribute("aria-label") === "Next page");
      const previous = buttons.filter((item) => item.getAttribute("aria-label") === "Previous page");
      const disabled = (item) => item.hasAttribute("disabled") || item.getAttribute("aria-disabled") === "true";
      const busy = root.matches('[aria-busy="true"]') || root.querySelector('[aria-busy="true"]') !== null;
      return !busy && match !== null && Number(match[1]) === 0 && Number(match[2]) === 0 && Number(match[3]) === 0 && rows === 0 && statuses.length === 1 && next.length === 1 && previous.length === 1 && disabled(next[0]) && disabled(previous[0]);
    });

    counters.createAttempted++;
    createControlCount =
      await adopted.playwright.getByRole("button", { name: "Create Token", exact: true }).count() +
      await adopted.playwright.getByRole("link", { name: "Create Token", exact: true }).count();
    counters.createFulfilled++;
    counters.nameAttempted++;
    tokenNameCount = await tokenResultsRoot.locator("table tbody").getByText("OmniRoute secure console R5 20260901", { exact: true }).count();
    counters.nameFulfilled++;
    counters.rowAttempted++;
    matchingRowCount = await tokenResultsRoot.getByRole("row").filter({ hasText: "OmniRoute secure console R5 20260901" }).count();
    counters.rowFulfilled++;
    tokenFilterComplete = tokenInitialFilterEmpty && tokenQueryEchoCount === 1 && tokenValueExact && tokenTerminal &&
      (tokenBaseline.terminalZero || tokenBaseline.completeNonempty);
    tokenSemanticSignature = navigationTargetExact && createControlCount === 1 && tokenNameCount === 0 &&
      matchingRowCount === 0 && tokenFilterComplete;
    if (!tokenSemanticSignature || counters.readinessAttempted !== 3 || counters.readinessFulfilled !== 3 ||
        counters.fillAttempted !== 1 || counters.fillFulfilled !== 1) {
      throw new Error("AuthenticatedTokenPageSemanticStateError");
    }
    result = "EXACT_V5_SELECTED_TOKEN_PAGE_SEMANTIC_READINESS_PASS";
  } catch (error) {
    errorClass = safeErrorClass(error);
  }
  secureConsoleV4AdoptionConsumed = true;
  if (result === "EXACT_V5_SELECTED_TOKEN_PAGE_SEMANTIC_READINESS_PASS") {
    secureConsoleOwnedTaskTabV4 = adopted;
    secureConsoleOwnedTaskTabV4Eligible = true;
    secureConsoleOwnedTaskTabV4State = "TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE";
  } else {
    secureConsoleOwnedTaskTabV4 = null;
    secureConsoleOwnedTaskTabV4Eligible = false;
    secureConsoleOwnedTaskTabV4State = "V5_REACQUISITION_OR_READINESS_FAILED";
  }
  counters.writeAttempted++;
  nodeRepl.write({
    result,
    declarationShape,
    predecessorStateExact,
    controllerOwnership,
    tabShape,
    navigationTargetExact,
    createControlCount,
    tokenNameCount,
    matchingRowCount,
    tokenInitialFilterEmpty,
    tokenQueryEchoCount,
    tokenFilterComplete,
    tokenSemanticSignature,
    selectedAttempted: counters.selectedAttempted,
    selectedFulfilled: counters.selectedFulfilled,
    navigationAttempted: counters.navigationAttempted,
    navigationFulfilled: counters.navigationFulfilled,
    urlAttempted: counters.urlAttempted,
    urlFulfilled: counters.urlFulfilled,
    readinessAttempted: counters.readinessAttempted,
    readinessFulfilled: counters.readinessFulfilled,
    fillAttempted: counters.fillAttempted,
    fillFulfilled: counters.fillFulfilled,
    createAttempted: counters.createAttempted,
    createFulfilled: counters.createFulfilled,
    nameAttempted: counters.nameAttempted,
    nameFulfilled: counters.nameFulfilled,
    rowAttempted: counters.rowAttempted,
    rowFulfilled: counters.rowFulfilled,
    writeAttempted: counters.writeAttempted,
    errorClass,
    consumed: secureConsoleV4AdoptionConsumed,
    bindingEligible: secureConsoleOwnedTaskTabV4Eligible,
    bindingNull: secureConsoleOwnedTaskTabV4 === null,
    bindingState: secureConsoleOwnedTaskTabV4State,
  });
})();
```

Exact PASS requires the fixed PASS terminal; declaration, predecessor,
ownership, tab-shape, navigation-target, initial-filter, filter-complete, and
semantic-signature booleans true; Create/query-echo counts `1/1`; token
name/row `0/0`; selected, navigation, URL, Create, name, and row counters
`1/1`; readiness `3/3`; fill `1/1`; write `1`; error class `NONE`; consumed
true; binding eligible true; binding null false; state
`TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE`; complete output; and completed tool
status.

A completed non-PASS must show consumed true, binding eligible false, binding
null true, and state `V5_REACQUISITION_OR_READINESS_FAILED`. No detachment cell
is then required or permitted. Because no tab was created, there is no created
tab to close. No second selected call or recovery action is permitted.

## Inherited V4 semantics after V5 PASS

Only after exact V5 Call 2 PASS may the sole future owner use the unchanged V4
downstream cells. Call 2 deliberately establishes the exact V4-compatible
retained-binding names and state, so no downstream source adaptation is
permitted:

- fresh Cloudflare prestart read cell: V4 executable block `20437` bytes,
  SHA-256
  `FAB457F36F3AEA9EFF89716DD28C30751B2F7607683E31CCCBA4D7F9C4A6AEBB`;
- pre-Create detach cell: V4 executable block `2309` bytes, SHA-256
  `60692947118FCD2CA765B8C7C850490B79B9ED3C0D3942D14CB5F429F924746D`;
- post-native detach cell: V4 executable block `2305` bytes, SHA-256
  `5ABC144ABA9866294EC4A7746906E3D3132ADAE993B93969C426295085FE102D`.

The future independent review must direct-byte verify these executable blocks
against their V4 hashes before classification. No runtime substitution, suffix
rewrite, or ad hoc editing is allowed.

## Fixed ordering and mandatory confirmations

The order remains:

1. validate committed V5 bytes, independent PASS, non-self-referential
   classification, post-commit coordinator tuple, runtime pins, baseline 12,
   index zero, profile/window/selected-tab confirmation, Prox-01/VM1205 online
   confirmation, and every inherited action-time pin;
2. run V5 Call 1 once;
3. only after exact Call 1 PASS, run V5 Call 2 once;
4. on any V5 non-PASS or uncertainty, stop with the gate spent;
5. only after exact V5 PASS, run the unchanged independently reviewed V4
   prestart cell once against the V4-compatible binding established by V5;
6. on proven pre-Create failure after a live eligible V5 binding, run only the
   unchanged reviewed V4 pre-Create zero-browser-call detach and stop;
7. only after all pre-Create cells PASS, run inherited clipboard-empty proof,
   private-proxy wrapper, preparation, retained owner launch, safe readiness,
   and form preparation in reviewed order;
8. pause for the mandatory combined final Create, user-native semantic Copy,
   and user-native masked Paste confirmation;
9. after the user's native generated-page close report, run only the reviewed
   unchanged V4 post-native zero-browser-call detach; and
10. preserve the separate exact-row deletion confirmation, universal
    revocation hold, invalid-token proof, retained-owner disposition, proxy
    cleanup, local cleanup, and redacted evidence terminals unchanged.

After final Create, no agent/browser inspection of the generated-token page or
clipboard is permitted. The user alone performs the one semantic Copy, one
native masked Paste, native generated-page close, and Enter. Standing authority
cannot bypass either mandatory confirmation.

## Failure and no-residue contract

Any failed, malformed, interrupted, timed-out, missing, truncated, or uncertain
consuming action spends its fresh gate. There is no retry, second selected
call, second readiness cell, alternate selector/path, list, reconnect, new tab,
claim, fallback, manual integration, task handoff, permission expansion,
cleanup reuse, or verdict relaxation.

The executable cells add no page-resident observer, timer, promise, expando,
event listener, interval, storage value, cookie, or injected helper. Browser
native waits and scoped reads only are permitted. All temporary local values
remain invocation-local except the reviewed retained controller/tab bindings
and fixed scalar counters/state. Completed failure nulls the V4-compatible
task-tab binding. Missing or uncertain output is `FAIL / NOT PROVEN`, never evidence of
cleanup.

## Offline verification and static review gate

Before commit and independent review, verify:

- strict UTF-8 without BOM, LF-only, one trailing LF;
- JavaScript parse for both exact cells;
- exact cell extraction bytes and SHA-256;
- mocked PASS, attachment failure, no-selected-tab, malformed-tab, navigation
  failure, initial-filter failure, baseline incomplete, query-echo failure,
  semantic mismatch, and safe error-class terminals;
- success/failure counter cardinality and complete fixed output keys;
- zero forbidden API/member strings in executable code except prose assertions;
- no secret-shaped values and no unsafe exception output;
- direct-byte comparison proving the V4 semantic page-signature body is
  unchanged except fresh-session declarations, `selected()` acquisition,
  V5 names, and fixed output/state labels;
- Git index zero before staging; exact-path staging of this brief only; commit
  direct parent `a32c53c2d5fba3940e44af691bcd8feae75d1681`; and exact dirty
  baseline 12 before and after commit.

Independent Sol High review must report one verdict, all findings by severity,
the direct bytes/commit reviewed, executable-cell hashes, fixture results,
prohibited-call counts, secret scan, baseline/index proof, residual limits,
and `authorizes_live_execution=false`. Only a committed PASS with zero
blocking, HIGH, or IMPORTANT findings may proceed to a separately committed
non-self-referential classification and post-commit coordinator tuple.

This brief performs and authorizes no live action.
