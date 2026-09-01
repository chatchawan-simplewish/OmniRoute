# Task 2 secure-console token-page readiness replacement brief

Status: **PROPOSED — not executable until independent Sol High PASS review**

`authorizes_live_execution=false`

## Purpose and exact predecessor state

This is one fresh no-retry replacement for the gate spent at incident commit
`43e29ef46f274eaf3b6e15954a30869a5b512a06`. It is not a retry or continuation
of the replacement at `20cfaf30e57901b90126af973588bbb65601e7b2`, its
independent PASS at `1f1ec923e9cd3bab16315ab077c525be67525d07`, or its
execution classification at `c23aec59d87f55b6fc2a24ed0f85b5061767a3ab`.

The only reusable live objects are the same-session
`secureConsoleChromeV1` controller and exact retained
`secureConsoleTaskTabV1.id`. Before this contract, the exact predecessor tuple
must still be:

- `secureConsoleOwnedTaskTabV2 === null`;
- `secureConsoleOwnedTaskTabV2Eligible === false`;
- `secureConsoleOwnedTaskTabV2State === "RETAINED_UNTOUCHED_PRECREATE_FAILURE"`;
- `secureConsoleOwnedTaskTabV2PreCreateDetachConsumed === true`; and
- `secureConsoleOwnedTaskTabV2PostNativeDetachConsumed === false`.

The current browser page is `NOT_PROVEN`. No page, tab, title, URL, DOM,
screenshot, or metadata inspection is permitted before the V3 cell below.

## Inherited contract without relaxation

Except for the new V3 binding/readiness cells, inherit every target, fixed
value, permission, counter, timeout, secret boundary, confirmation, revocation
hold, cleanup rule, and terminal from:

- live brief commit `7af3ab75ec87d81d75811ff8f2e9b4fa9d0c3e3b`;
- scope-replacement brief commit
  `20cfaf30e57901b90126af973588bbb65601e7b2`;
- scope-replacement PASS review commit
  `1f1ec923e9cd3bab16315ab077c525be67525d07`; and
- execution classification commit
  `c23aec59d87f55b6fc2a24ed0f85b5061767a3ab`.

The fresh local, VM1205, public-DNS, and OmniRoute checks already recorded in
the incident remain the only accepted proof: exact local pins PASS, VM pins
PASS, both public resolvers target A/CNAME `0/0`, and OmniRoute key recheck
PASS with `team-rollout-test` count `0`. They may be inherited only while the
incident's zero-action boundary, exact same Node session, empty Git index, and
unrelated dirty baseline remain unchanged. Any drift stops before browser use.

The exact token remains `OmniRoute secure console R5 20260901`, zone `mysw.me`,
and only `Zone WAF Edit` plus `Zone Read`. No DNS, Tunnel, Access, account,
token-management, or other permission is added. No public rollout, Tunnel,
DNS/public-hostname, Access application, OmniRoute key/model request, alternate
bridge, retry, fallback, handoff, second start, or verdict relaxation is
authorized.

## Reproducible source-projection gate

Immediately before browser use, recompute this working-projection SHA-256 from
the repository root. The only excluded paths, compared as ordinal `/`-separated
strings, are `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/` plus
exactly `task-2-secure-console-transfer-token-page-readiness-replacement-brief.md`,
`task-2-secure-console-transfer-token-page-readiness-replacement-sol-review.md`,
`task-2-secure-console-transfer-token-page-readiness-replacement-fix1-sol-review.md`,
and `task-2-secure-console-transfer-token-page-readiness-replacement-fix1-execution-classification.md`.
No directory, glob, prefix, suffix, or other artifact is excluded.

Reject paths containing control characters. Enumerate every tracked path with
`git ls-files` and every nonignored untracked file with
`git ls-files --others --exclude-standard`. For each nonexcluded path emit the
ASCII line `K<TAB>PATH<TAB>LENGTH<TAB>SHA256<LF>`: `K` is `T` for a present
tracked file, `D` with length `-1` and hash `-` for a missing tracked file, or
`U` for an untracked file; length and uppercase SHA-256 cover exact working
bytes. Sort complete lines ordinally, concatenate without BOM or any other
transformation, and hash those bytes. Required digest:
`C4C9807FD5667E872BCBCFFD60FBF2AA71AEBC788AC744EFCD93FF18457C8E0F`.

`git diff --cached --quiet` must succeed. After the four exclusions, exact
`git status --porcelain=v1 --untracked-files=normal` is 12 records: modified
`open-sse/services/codexQuotaFetcher.ts`, `src/app/api/v1/models/catalog.ts`,
`src/lib/localDb.ts`, `tests/unit/api/models-agent-route-aliases.test.ts`, and
`tests/unit/services/agent-route.test.ts`; untracked
`open-sse/services/agentRoute.ts`, `open-sse/services/agentRouteObjectives.ts`,
`src/app/api/v1/agent-routes/`, `src/lib/db/agentRouteRuns.ts`,
`src/lib/db/migrations/134_agent_route_runs.sql`,
`tests/unit/api/agent-route-events.test.ts`, and
`tests/unit/db/agent-route-runs.test.ts`. Order and two-character status are
exact. Any projection, index, status, ignored/untracked classification, or path
drift stops before browser use.

At execution classification, verify direct bytes and ancestry: incident
`43e29ef46f274eaf3b6e15954a30869a5b512a06` is `3797` bytes SHA-256
`37C928A05B546A85AE3A56985A9B902BD1463E7D7AC2FE1630E5AFA1B283E784`;
initial brief `5620b33b26b5f6770c2fbe797116ab09629ab3b1` is `31326` bytes SHA-256
`5F5A30CB619F6828D79AF90BF377DC3DADE7B86E34A43C781247929C0E67C5E8`;
initial FAIL review `db8da1890e519997b2063cbf4c9bd947d9e43bd6` is `7648` bytes SHA-256
`A2F43F0CA40582BC36F0AEB8BED1CE6C6662E981ED7C926EC66C94FC4136B0AE`.
The fix1 brief commit must have `db8da189...` as parent, its fix1 review must
have the fix1 brief as parent, and the execution classification must have that
review as parent. Classification must record full commit, exact path, byte
length, and SHA-256 for itself, the fix1 brief, and fix1 review, and re-pin all
three known objects above. Missing, non-direct, merged, substituted, or
unpinned ancestry blocks execution.

## Exact executable pins

The consumed V2 JavaScript fences are historical state evidence only and must
not execute again:

| Historical V2 fence | Bytes | SHA-256 |
| --- | ---: | --- |
| adoption | `3608` | `73BD7B0DF858FA29C2C182CC535FBB4695732011898CF8718724CAD35259FD1D` |
| pre-Create detach | `2030` | `E457BC6BDF47A70A12BEEEC5ACE859A4CF7FEEC0B6B782C8A3EBAE7081887A20` |
| post-native detach | `2066` | `0A3554F25F598C98D60F35853019D4F0741AEE6EF68F4105A951D657E1CC2A1D` |

The unchanged inherited PowerShell fences remain executable only at their
original reviewed points:

| Inherited fence | Bytes | SHA-256 |
| --- | ---: | --- |
| proxy wrapper | `8380` | `A7C7F04705344160030C3BF1CA383179616507555F56D2288E3BFD9B46FEF2AC` |
| preparation source | `3983` | `784E91D71AB0B07A65C6FDA429CC4A86C3E6107C76E258BC608F75DA893C1D4A` |
| owner source | `22118` | `347FCD60A41DF780CE4A94E4FC14C87E5059112068C689EF73636ABC5B0F0B6C` |
| owner launch | `655` | `995185FA04790564F4CDCA967E87CAB82EB97731D8458EF85CEF942D4606A293` |
| owner final | `2779` | `9316DE2F7C84A89947E57C8563E9381E97D7C52F0DFFE56CA7E4DE616DD8F637` |
| retained-scope preparation | `2017` | `D438EFF617AA6983419D610A67FAC3DD01B4434E66300659A9A7821F1CE8C5D9` |
| retained-scope guarded launch | `14356` | `45EEA83B4DF95FDC2FB47CD969C117D3A5AEECE5060286059A3829528288FF05` |
| retained-scope disposition | `3308` | `B8087F2CB77A695C1B6DD145DDD3D39D48F8AABEBBA00863BEA0610C8BE6518E` |

The new JavaScript fence pins are filled from their direct LF-only UTF-8 bytes
below and are part of this contract:

| New V3 fence | Bytes | SHA-256 |
| --- | ---: | --- |
| adopt and token readiness | `7623` | `67E81CCD09F3F25B38EA3CB1A41DBA30A8A2A5281E19B5D1D9DDC1B1F0016926` |
| fresh Cloudflare prestart reads | `15903` | `8CAA901030E178725709F173984315D2F90802CB173670D9551031A3E9C23837` |
| pre-Create detach | `2196` | `467F98589FD335AC6393B8BFEF64D7A3101EBE27C5BAA74E37A7FABA68AC5F60` |
| post-native detach | `2201` | `55B407F463C351B64174800617E8B3F64B3CE98D60BAA1BEAEF1E6D3312B10A5` |

## V3 retained-tab adoption and token-page readiness

The sole owner runs this exact cell once in the same persistent Node session
with one fixed outer tool deadline of `60000 ms`. It validates the exact V1 and
spent-V2 declarations, calls `secureConsoleChromeV1.tabs.get()` exactly once
for the retained ID, performs exactly one navigation to
`https://dash.cloudflare.com/profile/api-tokens`, then performs exactly one
fixed `20000 ms` locator readiness wait after an exact page-local token-name
filter and before title/control/name/row checks.

```javascript
let secureConsoleOwnedTaskTabV3 = null;
let secureConsoleOwnedTaskTabV3Eligible = false;
let secureConsoleOwnedTaskTabV3State = "UNADOPTED";
let secureConsoleOwnedTaskTabV3PreCreateDetachConsumed = false;
let secureConsoleOwnedTaskTabV3PostNativeDetachConsumed = false;
let secureConsoleCloudflareReadsV3Consumed = false;
await (async () => {
  const counters = {
    getAttempted: 0,
    getFulfilled: 0,
    navigationAttempted: 0,
    navigationFulfilled: 0,
    readinessAttempted: 0,
    readinessFulfilled: 0,
    titleAttempted: 0,
    titleFulfilled: 0,
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
  let titleExact = false;
  let createControlCount = -1;
  let tokenNameCount = -1;
  let matchingRowCount = -1;
  let tokenFilterComplete = false;
  let adopted = null;
  const safeErrorClass = (error) => {
    const name = typeof error?.name === "string" ? error.name : "";
    return /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(name) ? name : "TokenPageReadinessError";
  };
  try {
    declarationShape =
      typeof secureConsoleAgentV1 === "object" && secureConsoleAgentV1 !== null &&
      typeof secureConsoleChromeV1 === "object" && secureConsoleChromeV1 !== null &&
      typeof secureConsoleChromeV1.tabs?.get === "function" &&
      typeof secureConsoleTaskTabV1 === "object" && secureConsoleTaskTabV1 !== null &&
      typeof secureConsoleTaskTabV1.id === "string" &&
      /^[A-Za-z0-9_-]{1,64}$/.test(secureConsoleTaskTabV1.id) &&
      typeof secureConsoleOwnedTaskTabV2 === "object" &&
      typeof secureConsoleOwnedTaskTabV2Eligible === "boolean" &&
      typeof secureConsoleOwnedTaskTabV2State === "string" &&
      typeof secureConsoleOwnedTaskTabV2PreCreateDetachConsumed === "boolean" &&
      typeof secureConsoleOwnedTaskTabV2PostNativeDetachConsumed === "boolean";
    if (!declarationShape) throw new Error("RetainedDeclarationShapeError");
    predecessorStateExact =
      secureConsoleOwnedTaskTabV2 === null &&
      secureConsoleOwnedTaskTabV2Eligible === false &&
      secureConsoleOwnedTaskTabV2State === "RETAINED_UNTOUCHED_PRECREATE_FAILURE" &&
      secureConsoleOwnedTaskTabV2PreCreateDetachConsumed === true &&
      secureConsoleOwnedTaskTabV2PostNativeDetachConsumed === false;
    if (!predecessorStateExact) throw new Error("RetainedPredecessorStateError");

    const retainedId = secureConsoleTaskTabV1.id;
    counters.getAttempted++;
    adopted = await secureConsoleChromeV1.tabs.get(retainedId);
    counters.getFulfilled++;
    controllerOwnership =
      typeof adopted === "object" && adopted !== null &&
      typeof adopted.id === "string" && adopted.id === retainedId;
    tabShape =
      controllerOwnership &&
      typeof adopted.goto === "function" &&
      typeof adopted.url === "function" &&
      typeof adopted.title === "function" &&
      typeof adopted.playwright?.getByRole === "function" &&
      typeof adopted.playwright?.getByText === "function";
    if (!tabShape) throw new Error("RetainedTabOwnershipError");

    counters.navigationAttempted++;
    await adopted.goto("https://dash.cloudflare.com/profile/api-tokens");
    counters.navigationFulfilled++;
    const tokenFilter = adopted.playwright.getByRole("textbox", { name: /search api tokens/i });
    if (await tokenFilter.count() !== 1) throw new Error("TokenFilterCountError");
    await tokenFilter.fill("OmniRoute secure console R5 20260901");
    const tokenResultsRoot = adopted.playwright.locator("main");
    if (await tokenResultsRoot.count() !== 1) throw new Error("TokenResultsRootCountError");
    const readinessMarker = tokenResultsRoot.getByText(/^(?:no api tokens found|no tokens found)$/i);
    if (await readinessMarker.count() !== 1) throw new Error("TokenFilteredResultMarkerCountError");
    counters.readinessAttempted++;
    await readinessMarker.waitFor({ state: "visible", timeoutMs: 20000 });
    counters.readinessFulfilled++;

    counters.titleAttempted++;
    const title = await adopted.title();
    counters.titleFulfilled++;
    titleExact = title === "API Tokens | Cloudflare";
    counters.createAttempted++;
    createControlCount =
      await adopted.playwright.getByRole("button", { name: "Create Token", exact: true }).count() +
      await adopted.playwright.getByRole("link", { name: "Create Token", exact: true }).count();
    counters.createFulfilled++;
    counters.nameAttempted++;
    tokenNameCount = await adopted.playwright.getByText("OmniRoute secure console R5 20260901", { exact: true }).count();
    counters.nameFulfilled++;
    counters.rowAttempted++;
    matchingRowCount = await adopted.playwright.getByRole("row").filter({ hasText: "OmniRoute secure console R5 20260901" }).count();
    counters.rowFulfilled++;
    const tokenFilterValueExact = await tokenFilter.evaluate((element) => element.value === "OmniRoute secure console R5 20260901");
    const tokenCompletion = await tokenResultsRoot.evaluate((root) => {
      const enabledNextCount = [...root.querySelectorAll("button,a,[role='button']")].filter((item) =>
        /^next(?: page)?$/i.test((item.getAttribute("aria-label") || item.textContent || "").trim()) &&
        !item.hasAttribute("disabled") && item.getAttribute("aria-disabled") !== "true",
      ).length;
      return { busyCount: root.querySelectorAll('[aria-busy="true"]').length, enabledNextCount };
    });
    tokenFilterComplete = tokenFilterValueExact && tokenCompletion.busyCount === 0 && tokenCompletion.enabledNextCount === 0;
    if (!titleExact || createControlCount !== 1 || tokenNameCount !== 0 || matchingRowCount !== 0 || !tokenFilterComplete) {
      throw new Error("AuthenticatedTokenPageStateError");
    }
    result = "EXACT_V3_TOKEN_PAGE_READINESS_PASS";
  } catch (error) {
    errorClass = safeErrorClass(error);
  }
  counters.writeAttempted++;
  nodeRepl.write({
    result,
    declarationShape,
    predecessorStateExact,
    controllerOwnership,
    tabShape,
    titleExact,
    createControlCount,
    tokenNameCount,
    matchingRowCount,
    tokenFilterComplete,
    getAttempted: counters.getAttempted,
    getFulfilled: counters.getFulfilled,
    navigationAttempted: counters.navigationAttempted,
    navigationFulfilled: counters.navigationFulfilled,
    readinessAttempted: counters.readinessAttempted,
    readinessFulfilled: counters.readinessFulfilled,
    titleAttempted: counters.titleAttempted,
    titleFulfilled: counters.titleFulfilled,
    createAttempted: counters.createAttempted,
    createFulfilled: counters.createFulfilled,
    nameAttempted: counters.nameAttempted,
    nameFulfilled: counters.nameFulfilled,
    rowAttempted: counters.rowAttempted,
    rowFulfilled: counters.rowFulfilled,
    writeAttempted: counters.writeAttempted,
    errorClass,
  });
  if (result === "EXACT_V3_TOKEN_PAGE_READINESS_PASS") {
    secureConsoleOwnedTaskTabV3 = adopted;
    secureConsoleOwnedTaskTabV3Eligible = true;
    secureConsoleOwnedTaskTabV3State = "TOKEN_PAGE_READY_ELIGIBLE";
    secureConsoleOwnedTaskTabV3PreCreateDetachConsumed = false;
    secureConsoleOwnedTaskTabV3PostNativeDetachConsumed = false;
    secureConsoleCloudflareReadsV3Consumed = false;
  } else {
    secureConsoleOwnedTaskTabV3 = null;
    secureConsoleOwnedTaskTabV3Eligible = false;
    secureConsoleOwnedTaskTabV3State = "V3_ADOPTION_OR_READINESS_FAILED";
  }
})();
```

Exact PASS requires the fixed PASS terminal; all declaration/ownership/title
booleans and `tokenFilterComplete` true; Create count `1`; token-name/row `0/0`; get, navigation, readiness,
title, Create, name, and row counters all `1/1`; write attempted `1`;
`errorClass=NONE`; complete untruncated output; completed tool status; and the
later private V3 alias/eligibility/state tuple exact. Alias assignment and
eligibility occur only after `nodeRepl.write` returns. Any timeout,
interruption, missing/truncated output, rejection, or uncertain completion
spends this cell and permits no detachment or later action.

This cell permits no tabs list, browser/controller reconnect or selection,
new tab, alternate tab, second get, second navigation, reload, close,
`markHandoff`, page serialization, screenshot, clipboard, keyboard, form
mutation, or metadata output.

## Fresh Cloudflare prestart read cell

After exact V3 PASS and before clipboard clear, proxy start, preparation, or
owner launch, run this exact cell once with fixed outer deadline `240000 ms`.
It serially proves fresh DNS, rate-rule, Tunnel/connector, Access-application,
and final token-row state. Each page transition has one fixed `20000 ms`
visible-locator readiness wait. Private hrefs, account/zone identifiers,
titles, page text, and DOM content are never output.

```javascript
await (async () => {
  const counters = {
    navigationAttempted: 0,
    navigationFulfilled: 0,
    clickAttempted: 0,
    clickFulfilled: 0,
    readinessAttempted: 0,
    readinessFulfilled: 0,
    writeAttempted: 0,
  };
  let result = "PRECONDITION_FAIL";
  let errorClass = "NONE";
  let declarationsValid = false;
  let preconditionValid = false;
  let accountBindingExact = false;
  let dnsTargetCount = -1;
  let dnsFilterComplete = false;
  let rateDataRowCount = -1;
  let rateTargetDescriptionCount = -1;
  let rateTargetHostCount = -1;
  let rateCompletenessProven = false;
  let tunnelTargetNameCount = -1;
  let tunnelTargetHostCount = -1;
  let tunnelFiltersComplete = false;
  let accessTargetHostCount = -1;
  let accessTargetNameCount = -1;
  let accessFiltersComplete = false;
  let tokenTitleExact = false;
  let tokenCreateControlCount = -1;
  let tokenNameCount = -1;
  let tokenRowCount = -1;
  let tokenFilterComplete = false;
  const safeErrorClass = (error) => {
    const name = typeof error?.name === "string" ? error.name : "";
    return /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(name) ? name : "CloudflarePrestartReadError";
  };
  const navigate = async (url) => {
    counters.navigationAttempted++;
    await secureConsoleOwnedTaskTabV3.goto(url);
    counters.navigationFulfilled++;
  };
  const clickOne = async (locator) => {
    if (await locator.count() !== 1) throw new Error("ClickTargetCountError");
    counters.clickAttempted++;
    await locator.click();
    counters.clickFulfilled++;
  };
  const readyOne = async (locator) => {
    if (await locator.count() !== 1) throw new Error("ReadinessTargetCountError");
    counters.readinessAttempted++;
    await locator.waitFor({ state: "visible", timeoutMs: 20000 });
    counters.readinessFulfilled++;
  };
  const filteredZero = async (filter, query, targetLocators) => {
    if (await filter.count() !== 1) throw new Error("FilterCountError");
    const resultsRoot = secureConsoleOwnedTaskTabV3.playwright.locator("main");
    if (await resultsRoot.count() !== 1) throw new Error("FilterResultsRootCountError");
    await filter.fill("");
    const emptyMarker = resultsRoot.getByText(/^(?:no results|no .* found)$/i);
    const baseline = await resultsRoot.evaluate((root) => {
      const visible = (element) => {
        const style = getComputedStyle(element);
        const box = element.getBoundingClientRect();
        return style.visibility !== "hidden" && style.display !== "none" && box.width > 0 && box.height > 0;
      };
      const emptyCount = [...root.querySelectorAll("*")].filter((element) =>
        visible(element) && /^(?:no results|no .* found)$/i.test((element.textContent || "").trim()),
      ).length;
      const dataRowCount = root.querySelectorAll("table tbody tr").length;
      const enabledNextCount = [...root.querySelectorAll("button,a,[role='button']")].filter((item) =>
        /^next(?: page)?$/i.test((item.getAttribute("aria-label") || item.textContent || "").trim()) &&
        !item.hasAttribute("disabled") && item.getAttribute("aria-disabled") !== "true",
      ).length;
      return { emptyCount, dataRowCount, enabledNextCount };
    });
    const baselineCompleteEmpty = baseline.emptyCount === 1 && baseline.dataRowCount === 0 && baseline.enabledNextCount === 0;
    if (!baselineCompleteEmpty && baseline.emptyCount !== 0) throw new Error("FilterBaselineAmbiguousError");
    await filter.fill(query);
    await readyOne(emptyMarker);
    const current = await filter.evaluate((element, expected) => element.value === expected, query);
    if (!current) throw new Error("FilterValueFreshnessError");
    const completion = await resultsRoot.evaluate((root) => {
      const enabledNextCount = [...root.querySelectorAll("button,a,[role='button']")].filter((item) =>
        /^next(?: page)?$/i.test((item.getAttribute("aria-label") || item.textContent || "").trim()) &&
        !item.hasAttribute("disabled") && item.getAttribute("aria-disabled") !== "true",
      ).length;
      return { busyCount: root.querySelectorAll('[aria-busy="true"]').length, enabledNextCount };
    });
    if (completion.busyCount !== 0 || completion.enabledNextCount !== 0) throw new Error("FilteredResultsIncompleteError");
    const counts = [];
    for (const target of targetLocators) counts.push(await target.count());
    if (counts.some((count) => count !== 0)) throw new Error("FilteredTargetPresentError");
    return counts;
  };
  try {
    declarationsValid =
      typeof secureConsoleOwnedTaskTabV3 === "object" &&
      typeof secureConsoleOwnedTaskTabV3Eligible === "boolean" &&
      typeof secureConsoleOwnedTaskTabV3State === "string" &&
      typeof secureConsoleOwnedTaskTabV3PreCreateDetachConsumed === "boolean" &&
      typeof secureConsoleOwnedTaskTabV3PostNativeDetachConsumed === "boolean" &&
      typeof secureConsoleCloudflareReadsV3Consumed === "boolean";
    preconditionValid =
      declarationsValid &&
      secureConsoleOwnedTaskTabV3 !== null &&
      secureConsoleOwnedTaskTabV3Eligible === true &&
      secureConsoleOwnedTaskTabV3State === "TOKEN_PAGE_READY_ELIGIBLE" &&
      secureConsoleOwnedTaskTabV3PreCreateDetachConsumed === false &&
      secureConsoleOwnedTaskTabV3PostNativeDetachConsumed === false &&
      secureConsoleCloudflareReadsV3Consumed === false;
    if (!preconditionValid) throw new Error("CloudflareReadPreconditionError");

    await navigate("https://dash.cloudflare.com");
    const zoneAnchor = secureConsoleOwnedTaskTabV3.playwright.locator("a").filter({ hasText: "mysw.me" });
    await readyOne(zoneAnchor);
    const zoneHref = await zoneAnchor.getAttribute("href");
    if (typeof zoneHref !== "string") throw new Error("ZoneHrefMissingError");
    const zoneUrl = new URL(zoneHref, "https://dash.cloudflare.com");
    const zonePathMatch = /^\/([0-9a-f]{32})\/mysw\.me\/?$/.exec(zoneUrl.pathname);
    if (zoneUrl.protocol !== "https:" || zoneUrl.hostname !== "dash.cloudflare.com" || zonePathMatch === null) {
      throw new Error("ZoneHrefShapeError");
    }
    const accountSegment = zonePathMatch[1];
    await navigate(zoneUrl.href);
    await readyOne(secureConsoleOwnedTaskTabV3.playwright.getByText("mysw.me", { exact: true }));

    const dnsButton = secureConsoleOwnedTaskTabV3.playwright.getByRole("button", { name: "DNS", exact: true });
    await clickOne(dnsButton);
    const dnsRecordsLink = secureConsoleOwnedTaskTabV3.playwright.getByRole("link", { name: /DNS Records/i });
    await readyOne(dnsRecordsLink);
    await clickOne(dnsRecordsLink);
    await readyOne(secureConsoleOwnedTaskTabV3.playwright.getByText(/Add record/i));
    [dnsTargetCount] = await filteredZero(
      secureConsoleOwnedTaskTabV3.playwright.getByRole("textbox", { name: /search dns records/i }),
      "ai-api-omniroute.mysw.me",
      [secureConsoleOwnedTaskTabV3.playwright.getByRole("row").filter({ hasText: "ai-api-omniroute.mysw.me" })],
    );
    dnsFilterComplete = true;

    const securityButton = secureConsoleOwnedTaskTabV3.playwright.getByRole("button", { name: "Security", exact: true });
    await clickOne(securityButton);
    const securityRulesLink = secureConsoleOwnedTaskTabV3.playwright.getByRole("link", { name: /security rules/i });
    await readyOne(securityRulesLink);
    await clickOne(securityRulesLink);
    const rateButton = secureConsoleOwnedTaskTabV3.playwright.getByRole("button", { name: /rate limiting/i });
    await readyOne(rateButton);
    const ratePanelId = await rateButton.getAttribute("aria-controls");
    if (typeof ratePanelId !== "string" || !/^[A-Za-z][A-Za-z0-9_-]{0,127}$/.test(ratePanelId)) {
      throw new Error("RatePanelBindingError");
    }
    await clickOne(rateButton);
    const ratePanel = secureConsoleOwnedTaskTabV3.playwright.locator(`#${ratePanelId}`);
    await readyOne(ratePanel);
    const rateTable = ratePanel.locator("table");
    await readyOne(rateTable);
    if (await rateTable.count() !== 1) throw new Error("RateTableCountError");
    const rateProof = await rateTable.evaluate((table, panelId) => {
      const rows = [...table.querySelectorAll("tbody tr")];
      const text = table.innerText || "";
      const scope = document.getElementById(panelId);
      const panelBound = scope !== null && scope.querySelectorAll("table").length === 1 && scope.querySelector("table") === table;
      if (!panelBound) return { dataRowCount: -1, targetDescriptionCount: -1, targetHostCount: -1, enabledNextCount: -1, panelBound: false };
      const nextControls = [...scope.querySelectorAll("button,a,[role='button']")].filter((item) =>
        /^next(?: page)?$/i.test((item.getAttribute("aria-label") || item.textContent || "").trim()),
      );
      const enabledNextCount = nextControls.filter((item) =>
        !item.hasAttribute("disabled") && item.getAttribute("aria-disabled") !== "true",
      ).length;
      return {
        dataRowCount: rows.length,
        targetDescriptionCount: (text.match(/OmniRoute team API 20 per 10s/g) || []).length,
        targetHostCount: (text.match(/ai-api-omniroute\.mysw\.me/g) || []).length,
        enabledNextCount,
        panelBound,
      };
    }, ratePanelId);
    rateDataRowCount = rateProof.dataRowCount;
    rateTargetDescriptionCount = rateProof.targetDescriptionCount;
    rateTargetHostCount = rateProof.targetHostCount;
    rateCompletenessProven = rateProof.panelBound === true && rateProof.enabledNextCount === 0;
    if (rateDataRowCount !== 1 || rateTargetDescriptionCount !== 0 || rateTargetHostCount !== 0 || !rateCompletenessProven) {
      throw new Error("RateRuleStateError");
    }

    const zeroTrustAnchor = secureConsoleOwnedTaskTabV3.playwright.locator("a").filter({ hasText: "Zero Trust" });
    await readyOne(zeroTrustAnchor);
    const zeroTrustHref = await zeroTrustAnchor.getAttribute("href");
    if (typeof zeroTrustHref !== "string") throw new Error("ZeroTrustHrefMissingError");
    const zeroTrustUrl = new URL(zeroTrustHref, "https://dash.cloudflare.com");
    const zeroTrustPathMatch = /^\/([0-9a-f]{32})(?:\/home)?\/?$/.exec(zeroTrustUrl.pathname);
    if (zeroTrustUrl.protocol !== "https:" || zeroTrustUrl.hostname !== "one.dash.cloudflare.com" ||
        zeroTrustPathMatch === null || zeroTrustPathMatch[1] !== accountSegment) {
      throw new Error("ZeroTrustHrefShapeError");
    }
    await navigate(zeroTrustUrl.href);
    const postNavigationUrl = new URL(await secureConsoleOwnedTaskTabV3.url());
    const postPathMatch = /^\/([0-9a-f]{32})(?:\/home)?\/?$/.exec(postNavigationUrl.pathname);
    const accountPageMarkers = secureConsoleOwnedTaskTabV3.playwright.locator(`a[href^="/${accountSegment}/"]`);
    accountBindingExact = postNavigationUrl.protocol === "https:" &&
      postNavigationUrl.hostname === "one.dash.cloudflare.com" &&
      postPathMatch !== null && postPathMatch[1] === accountSegment &&
      await accountPageMarkers.count() > 0;
    if (!accountBindingExact) throw new Error("ZeroTrustAccountBindingError");
    const networksButton = secureConsoleOwnedTaskTabV3.playwright.getByRole("button", { name: "Networks", exact: true });
    await readyOne(networksButton);
    await clickOne(networksButton);
    const tunnelsLink = secureConsoleOwnedTaskTabV3.playwright.getByRole("link", { name: /tunnels/i });
    await readyOne(tunnelsLink);
    await clickOne(tunnelsLink);
    await readyOne(secureConsoleOwnedTaskTabV3.playwright.getByText(/create.*tunnel/i));
    const tunnelFilter = secureConsoleOwnedTaskTabV3.playwright.getByRole("textbox", { name: /search tunnels/i });
    [tunnelTargetNameCount] = await filteredZero(tunnelFilter, "omniroute-team-tunnel", [
      secureConsoleOwnedTaskTabV3.playwright.getByRole("row").filter({ hasText: "omniroute-team-tunnel" }),
    ]);
    [tunnelTargetHostCount] = await filteredZero(tunnelFilter, "ai-api-omniroute.mysw.me", [
      secureConsoleOwnedTaskTabV3.playwright.getByRole("row").filter({ hasText: "ai-api-omniroute.mysw.me" }),
    ]);
    tunnelFiltersComplete = true;

    const accessButton = secureConsoleOwnedTaskTabV3.playwright.getByRole("button", { name: "Access", exact: true });
    await readyOne(accessButton);
    await clickOne(accessButton);
    const applicationsLink = secureConsoleOwnedTaskTabV3.playwright.getByRole("link", { name: /applications/i });
    await readyOne(applicationsLink);
    await clickOne(applicationsLink);
    await readyOne(secureConsoleOwnedTaskTabV3.playwright.getByText(/add an application|add application/i));
    const accessFilter = secureConsoleOwnedTaskTabV3.playwright.getByRole("textbox", { name: /search applications/i });
    [accessTargetHostCount] = await filteredZero(accessFilter, "ai-api-omniroute.mysw.me", [
      secureConsoleOwnedTaskTabV3.playwright.getByRole("row").filter({ hasText: "ai-api-omniroute.mysw.me" }),
    ]);
    [accessTargetNameCount] = await filteredZero(accessFilter, "OmniRoute team API", [
      secureConsoleOwnedTaskTabV3.playwright.getByRole("row").filter({ hasText: "OmniRoute team API" }),
    ]);
    accessFiltersComplete = true;

    await navigate("https://dash.cloudflare.com/profile/api-tokens");
    const tokenFilter = secureConsoleOwnedTaskTabV3.playwright.getByRole("textbox", { name: /search api tokens/i });
    [tokenRowCount] = await filteredZero(tokenFilter, "OmniRoute secure console R5 20260901", [
      secureConsoleOwnedTaskTabV3.playwright.getByRole("row").filter({ hasText: "OmniRoute secure console R5 20260901" }),
    ]);
    tokenFilterComplete = true;
    tokenTitleExact = await secureConsoleOwnedTaskTabV3.title() === "API Tokens | Cloudflare";
    tokenCreateControlCount =
      await secureConsoleOwnedTaskTabV3.playwright.getByRole("button", { name: "Create Token", exact: true }).count() +
      await secureConsoleOwnedTaskTabV3.playwright.getByRole("link", { name: "Create Token", exact: true }).count();
    tokenNameCount = await secureConsoleOwnedTaskTabV3.playwright.getByText("OmniRoute secure console R5 20260901", { exact: true }).count();
    if (!tokenTitleExact || tokenCreateControlCount !== 1 || tokenNameCount !== 0 || tokenRowCount !== 0 ||
        !dnsFilterComplete || !rateCompletenessProven || !tunnelFiltersComplete || !accessFiltersComplete || !tokenFilterComplete) {
      throw new Error("FinalTokenPageStateError");
    }
    if (counters.navigationAttempted !== 4 || counters.navigationFulfilled !== 4 ||
        counters.clickAttempted !== 9 || counters.clickFulfilled !== 9 ||
        counters.readinessAttempted !== 21 || counters.readinessFulfilled !== 21) {
      throw new Error("BrowserCounterError");
    }
    result = "EXACT_V3_CLOUDFLARE_PRESTART_READS_PASS";
  } catch (error) {
    errorClass = safeErrorClass(error);
  }
  counters.writeAttempted++;
  nodeRepl.write({
    result,
    declarationsValid,
    preconditionValid,
    accountBindingExact,
    navigationAttempted: counters.navigationAttempted,
    navigationFulfilled: counters.navigationFulfilled,
    clickAttempted: counters.clickAttempted,
    clickFulfilled: counters.clickFulfilled,
    readinessAttempted: counters.readinessAttempted,
    readinessFulfilled: counters.readinessFulfilled,
    dnsTargetCount,
    dnsFilterComplete,
    rateDataRowCount,
    rateTargetDescriptionCount,
    rateTargetHostCount,
    rateCompletenessProven,
    tunnelTargetNameCount,
    tunnelTargetHostCount,
    tunnelFiltersComplete,
    accessTargetHostCount,
    accessTargetNameCount,
    accessFiltersComplete,
    tokenTitleExact,
    tokenCreateControlCount,
    tokenNameCount,
    tokenRowCount,
    tokenFilterComplete,
    writeAttempted: counters.writeAttempted,
    errorClass,
  });
  secureConsoleCloudflareReadsV3Consumed = true;
  secureConsoleOwnedTaskTabV3State = result === "EXACT_V3_CLOUDFLARE_PRESTART_READS_PASS"
    ? "CLOUDFLARE_PRESTART_READS_PASS"
    : "CLOUDFLARE_PRESTART_READS_FAILED";
})();
```

Exact PASS requires declarations/precondition and private account binding true;
navigation `4/4`; clicks `9/9`, each preceded by count one; readiness `21/21`;
DNS target `0` with exact filter complete; rate unique-table data rows `1`,
target description/host `0/0`, and no enabled next page; Tunnel name/host
`0/0` with both filters complete; Access host/name `0/0` with both filters
complete; final token title true, Create count `1`, token name/row `0/0`, and
exact filter complete; write attempted `1`;
`errorClass=NONE`; complete untruncated output; completed tool status; and the
later private consumed/state tuple exact. The cell sets consumed/state only
after `nodeRepl.write` returns. Any discrepancy spends the replacement and
routes, after proven full completion only, to the pre-Create detach cell.

No browser action may occur between this PASS and the inherited form sequence
except the serial read-only/form-preparation operations already authorized by
the inherited contract, substituting only `secureConsoleOwnedTaskTabV3` for
the spent V2 alias.

## Mutually exclusive V3 detachment cells

On any proven pre-Create failure after V3 adoption, execute this exact fixed
`10000 ms`-deadline, zero-browser-call cell once. It does not claim the tab was
untouched or closed.

```javascript
let preCreateDetachAttemptedV3 = 0;
let preCreateDetachFulfilledV3 = 0;
const preCreateDetachDeclarationsV3 =
  typeof secureConsoleOwnedTaskTabV3 === "object" &&
  typeof secureConsoleOwnedTaskTabV3Eligible === "boolean" &&
  typeof secureConsoleOwnedTaskTabV3State === "string" &&
  typeof secureConsoleOwnedTaskTabV3PreCreateDetachConsumed === "boolean" &&
  typeof secureConsoleOwnedTaskTabV3PostNativeDetachConsumed === "boolean" &&
  typeof secureConsoleCloudflareReadsV3Consumed === "boolean";
const preCreateDetachPreconditionV3 =
  preCreateDetachDeclarationsV3 &&
  secureConsoleOwnedTaskTabV3 !== null &&
  secureConsoleOwnedTaskTabV3Eligible === true &&
  ["TOKEN_PAGE_READY_ELIGIBLE", "CLOUDFLARE_PRESTART_READS_PASS", "CLOUDFLARE_PRESTART_READS_FAILED"].includes(secureConsoleOwnedTaskTabV3State) &&
  secureConsoleOwnedTaskTabV3PreCreateDetachConsumed === false &&
  secureConsoleOwnedTaskTabV3PostNativeDetachConsumed === false;
let preCreateDetachResultV3 = "PRECONDITION_FAIL";
if (preCreateDetachPreconditionV3) {
  preCreateDetachAttemptedV3++;
  secureConsoleOwnedTaskTabV3Eligible = false;
  secureConsoleOwnedTaskTabV3 = null;
  secureConsoleOwnedTaskTabV3State = "RETAINED_TAB_PRECREATE_FAILURE_BINDING_DETACHED";
  secureConsoleOwnedTaskTabV3PreCreateDetachConsumed = true;
  preCreateDetachFulfilledV3++;
  preCreateDetachResultV3 = "EXACT_V3_PRECREATE_BINDING_DETACH_PASS";
}
nodeRepl.write({
  result: preCreateDetachResultV3,
  declarationsValid: preCreateDetachDeclarationsV3,
  preconditionValid: preCreateDetachPreconditionV3,
  detachAttempted: preCreateDetachAttemptedV3,
  detachFulfilled: preCreateDetachFulfilledV3,
  preCreateConsumed: preCreateDetachDeclarationsV3 ? secureConsoleOwnedTaskTabV3PreCreateDetachConsumed : null,
  postNativeConsumed: preCreateDetachDeclarationsV3 ? secureConsoleOwnedTaskTabV3PostNativeDetachConsumed : null,
  browserCalls: 0,
  bindingEligible: preCreateDetachDeclarationsV3 ? secureConsoleOwnedTaskTabV3Eligible : null,
  bindingNull: preCreateDetachDeclarationsV3 ? secureConsoleOwnedTaskTabV3 === null : false,
  bindingState: preCreateDetachDeclarationsV3 ? secureConsoleOwnedTaskTabV3State : "DECLARATION_INVALID",
});
```

After the user reports completing the inherited native generated-page close,
execute this exact fixed `10000 ms`-deadline, zero-browser-call cell once.

```javascript
let postNativeDetachAttemptedV3 = 0;
let postNativeDetachFulfilledV3 = 0;
const postNativeDetachDeclarationsV3 =
  typeof secureConsoleOwnedTaskTabV3 === "object" &&
  typeof secureConsoleOwnedTaskTabV3Eligible === "boolean" &&
  typeof secureConsoleOwnedTaskTabV3State === "string" &&
  typeof secureConsoleOwnedTaskTabV3PreCreateDetachConsumed === "boolean" &&
  typeof secureConsoleOwnedTaskTabV3PostNativeDetachConsumed === "boolean" &&
  typeof secureConsoleCloudflareReadsV3Consumed === "boolean";
const postNativeDetachPreconditionV3 =
  postNativeDetachDeclarationsV3 &&
  secureConsoleOwnedTaskTabV3 !== null &&
  secureConsoleOwnedTaskTabV3Eligible === true &&
  secureConsoleOwnedTaskTabV3State === "CLOUDFLARE_PRESTART_READS_PASS" &&
  secureConsoleCloudflareReadsV3Consumed === true &&
  secureConsoleOwnedTaskTabV3PreCreateDetachConsumed === false &&
  secureConsoleOwnedTaskTabV3PostNativeDetachConsumed === false;
let postNativeDetachResultV3 = "PRECONDITION_FAIL";
if (postNativeDetachPreconditionV3) {
  postNativeDetachAttemptedV3++;
  secureConsoleOwnedTaskTabV3Eligible = false;
  secureConsoleOwnedTaskTabV3 = null;
  secureConsoleOwnedTaskTabV3State = "USER_NATIVE_CLOSE_REPORTED_BINDING_DETACHED";
  secureConsoleOwnedTaskTabV3PostNativeDetachConsumed = true;
  postNativeDetachFulfilledV3++;
  postNativeDetachResultV3 = "EXACT_V3_POST_NATIVE_CLOSE_BINDING_DETACH_PASS";
}
nodeRepl.write({
  result: postNativeDetachResultV3,
  declarationsValid: postNativeDetachDeclarationsV3,
  preconditionValid: postNativeDetachPreconditionV3,
  detachAttempted: postNativeDetachAttemptedV3,
  detachFulfilled: postNativeDetachFulfilledV3,
  preCreateConsumed: postNativeDetachDeclarationsV3 ? secureConsoleOwnedTaskTabV3PreCreateDetachConsumed : null,
  postNativeConsumed: postNativeDetachDeclarationsV3 ? secureConsoleOwnedTaskTabV3PostNativeDetachConsumed : null,
  browserCalls: 0,
  bindingEligible: postNativeDetachDeclarationsV3 ? secureConsoleOwnedTaskTabV3Eligible : null,
  bindingNull: postNativeDetachDeclarationsV3 ? secureConsoleOwnedTaskTabV3 === null : false,
  bindingState: postNativeDetachDeclarationsV3 ? secureConsoleOwnedTaskTabV3State : "DECLARATION_INVALID",
});
```

Each detach PASS requires declarations/precondition true, detach `1/1`, its
mutually exclusive consumed tuple, browser calls `0`, binding null,
eligibility false, exact fixed state, complete untruncated output, and completed
tool status. Precondition failure, repeat/opposite invocation, output
uncertainty, or timeout spends the disposition. Neither cell proves tab close.
No get, list, reconnect, new, navigation, reload, close, `markHandoff`, page
read, screenshot, clipboard, keyboard, lookup, retry, or fallback is permitted.

## Ordering, confirmations, revocation, and cleanup

The order is fixed:

1. validate exact artifact/action-time pins and predecessor Node tuple;
2. run V3 adoption/token-readiness once;
3. run fresh Cloudflare prestart reads once;
4. only after both PASS, execute the inherited clipboard clear/empty proof;
5. execute the unchanged private-proxy wrapper once, preparation once, retained
   owner launch once, safe readiness proof, and form preparation;
6. pause for the mandatory combined final Create plus user-native semantic Copy
   plus user-native masked Paste confirmation;
7. after the user's native generated-page close report, run only the V3
   post-native detach cell; and
8. preserve the separate exact-row deletion confirmation, universal revocation
   hold, invalid-token proof, retained-owner final disposition, proxy cleanup,
   local cleanup, and redacted evidence terminals unchanged.

After final Create, no agent/browser inspection of the generated-token page or
clipboard is permitted. The user alone performs the one semantic Copy, one
native masked Paste, native generated-page close, and Enter. The later exact
row deletion remains a separate mandatory confirmation. Standing authority
cannot bypass either checkpoint.

Any failed, malformed, interrupted, timed-out, missing, truncated, or uncertain
consuming action spends this fresh gate. No retry, second get, second readiness
cell, alternate selector/path, browser/controller reacquisition, fallback,
manual integration, handoff, permission expansion, cleanup reuse, or verdict
relaxation is permitted. All secret, token, account/zone/rule identifiers,
hrefs, page content, DOM, screenshots, clipboard bytes, headers, response
bodies, and exception messages remain excluded from output and artifacts.

## Static review gate

Independent Sol High review must pin this file's exact commit, bytes, and
SHA-256; verify every table pin against direct bytes; parse every JavaScript
fence without execution and every inherited PowerShell fence without
execution; prove the V1/V2 declaration tuple, sole V3 get/navigation/readiness
cardinality, post-write assignment ordering, bounded fresh Cloudflare reads,
safe output, mutually exclusive detach lifecycle, unchanged inherited fences,
mandatory confirmations, revocation/cleanup, and no-retry boundaries; and
return exact PASS. Any FAIL, NOT PROVEN, ambiguity, drift, or non-PASS blocks
execution.
