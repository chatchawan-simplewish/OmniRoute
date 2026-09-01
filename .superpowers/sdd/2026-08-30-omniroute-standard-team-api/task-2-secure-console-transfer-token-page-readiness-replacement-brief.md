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
`task-2-secure-console-transfer-token-page-readiness-replacement-fix2-sol-review.md`,
`task-2-secure-console-transfer-token-page-readiness-replacement-fix3-sol-review.md`,
and `task-2-secure-console-transfer-token-page-readiness-replacement-fix3-execution-classification.md`.
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

`git diff --cached --quiet` must succeed. After the six exclusions, exact
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
Fix1 brief `cbb2209a375b8f17b8745513f7e43bde3f0b377a` is `42057` bytes SHA-256
`A901FAB22A750DB64ACBE38148EB67A961BCE5C600700C3FA33EF129B93474C4`;
fix1 FAIL review `bfc203bfe1ad49086c11f53b413d1cc8971b18c6` is `9773` bytes SHA-256
`E16F0448A0A414875ED4C50E55963A01F8CAA7A4EEBAE6C8906F548679256965`.
Fix2 brief `d56e2bb9443aebfae301ff0f883266dfa7946890` is `53932` bytes SHA-256
`4041BB6B6B9A4AB0735BB7A1AA41953112BEE37CCDE0083EA4284AFEA9230666`;
fix2 FAIL review `080f9bec66a3b8f94b93e59e0c5e5463d9695401` is `7249` bytes SHA-256
`2233C0A1F71343FC253F2851EFAC46526EA841C2E6A625B5EA55399ED3BCCB71`.
The fix3 brief commit must have `080f9bec...` as direct parent, its fix3 review
must have the fix3 brief as direct parent, and the fix3 execution
classification must have that review as direct parent. Classification pins
only already-existing incident/brief/review objects above, the committed fix2
brief and review direct bytes, the exact expected classification path, and the
projection digest; it must not claim its own commit, byte length, or hash.

After classification is committed, the root owner records a separate
action-time coordinator evidence tuple containing the classification commit,
its direct parent, exact path, direct byte length, direct SHA-256, current HEAD,
and projection digest. It is valid only when HEAD equals that classification
commit, its parent equals the reviewed fix3-review commit, and all direct bytes
reproduce. The tuple is not committed and does not pin its own identity. It
must exist and revalidate immediately before browser use. Missing, non-direct,
merged, substituted, self-referential, or unpinned ancestry blocks execution.

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
| adopt and token readiness | `10987` | `9000B5CBB1770DF58C307D1D3FED66844B0A6A2A239ED100D144C6C9DEBCAEA7` |
| fresh Cloudflare prestart reads | `19737` | `C9299E0BE4FFFB211B052C1F0E71D8DBEAFA89422EFA5BFC0BB88C380F65EE73` |
| pre-Create detach | `2196` | `467F98589FD335AC6393B8BFEF64D7A3101EBE27C5BAA74E37A7FABA68AC5F60` |
| post-native detach | `2201` | `55B407F463C351B64174800617E8B3F64B3CE98D60BAA1BEAEF1E6D3312B10A5` |

## V3 retained-tab adoption and token-page readiness

The sole owner runs this exact cell once in the same persistent Node session
with one fixed outer tool deadline of `60000 ms`. It validates the exact V1 and
spent-V2 declarations, calls `secureConsoleChromeV1.tabs.get()` exactly once
for the retained ID, performs exactly one navigation to
`https://dash.cloudflare.com/profile/api-tokens`, then performs exactly one
fixed `20000 ms` locator readiness wait for the fresh page's bound paginator,
then one exact page-local token-name fill and one bounded result-transition
wait before title/control/name/row checks.

The search input's required `aria-controls` must identify exactly one result
region. Fresh-navigation baseline is complete only with its exact paginator,
row total, busy-free state, and either a complete nonempty page or authoritative
global `0-0 of 0` terminal. From a nonempty baseline, a bounded native locator
wait requires the exact empty status to become visible after the one fill; a
globally empty baseline proves absence before the fill, so an unchanged empty
marker is not load-bearing. Evaluate calls only take synchronous read snapshots.

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
    fillAttempted: 0,
    fillFulfilled: 0,
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
    const tokenRegionId = await tokenFilter.getAttribute("aria-controls");
    if (typeof tokenRegionId !== "string" || !/^[A-Za-z][A-Za-z0-9_-]{0,127}$/.test(tokenRegionId)) throw new Error("TokenRegionBindingError");
    const tokenResultsRoot = adopted.playwright.locator(`#${tokenRegionId}`);
    if (await tokenResultsRoot.count() !== 1) throw new Error("TokenResultsRootCountError");
    const tokenPaginator = tokenResultsRoot.locator('[aria-label="Pagination"]');
    if (await tokenPaginator.count() !== 1) throw new Error("TokenPaginatorCountError");
    counters.readinessAttempted++;
    await tokenPaginator.waitFor({ state: "visible", timeoutMs: 20000 });
    counters.readinessFulfilled++;
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
    tokenFilterComplete = tokenValueExact && tokenTerminal && (tokenBaseline.terminalZero || tokenBaseline.completeNonempty);

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
    tokenNameCount = await tokenResultsRoot.getByText("OmniRoute secure console R5 20260901", { exact: true }).count();
    counters.nameFulfilled++;
    counters.rowAttempted++;
    matchingRowCount = await tokenResultsRoot.getByRole("row").filter({ hasText: "OmniRoute secure console R5 20260901" }).count();
    counters.rowFulfilled++;
    if (!titleExact || createControlCount !== 1 || tokenNameCount !== 0 || matchingRowCount !== 0 || !tokenFilterComplete ||
        counters.readinessAttempted !== 2 || counters.readinessFulfilled !== 2 ||
        counters.fillAttempted !== 1 || counters.fillFulfilled !== 1) {
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
    fillAttempted: counters.fillAttempted,
    fillFulfilled: counters.fillFulfilled,
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
booleans and `tokenFilterComplete` true; Create count `1`; token-name/row `0/0`;
get, navigation, title, Create, name, and row counters all `1/1`; native
locator readiness `2/2`; page-local search fill `1/1`;
write attempted `1`;
`errorClass=NONE`; complete untruncated output; completed tool status; and the
later private V3 alias/eligibility/state tuple exact. Alias assignment and
eligibility occur only after `nodeRepl.write` returns. Any timeout,
interruption, missing/truncated output, rejection, or uncertain completion
spends this cell and permits no detachment or later action.

This cell permits no tabs list, browser/controller reconnect or selection,
new tab, alternate tab, second get, second navigation, reload, close,
`markHandoff`, page serialization, screenshot, clipboard, keyboard,
persistent/provider Create/edit mutation, or metadata output. The single exact
page-local search-filter fill is authorized and makes no provider-persistent
change; no other form fill is authorized.

## Fresh Cloudflare prestart read cell

After exact V3 PASS and before clipboard clear, proxy start, preparation, or
owner launch, run this exact cell once with fixed outer deadline `240000 ms`.
It serially proves fresh DNS, rate-rule, Tunnel/connector, Access-application,
and final token-row state. Each page transition has one fixed `20000 ms`
visible-locator readiness sequence, and every exact empty-status transition is
individually bounded at `20000 ms`. Private hrefs, account/zone identifiers,
titles, page text, and DOM content are never output.

Every search filter must bind by required `aria-controls` to one exact result
region. Every query starts from a fresh navigation to its exact page; its clear
is accepted only after bound-paginator readiness and a completed region
baseline. An authoritative busy-free `0-0 of 0`, zero-row, exact-status,
terminal-paginator baseline proves global absence; otherwise the fresh baseline
must be complete and nonempty before the query fill, after which a bounded
native locator wait requires a newly visible exact empty status. No injected
observer, timer, Promise, expando, concurrent wait, or post-failure cleanup is
used. Rate uses the same exact panel-bound paginator/row/busy terminal.

```javascript
await (async () => {
  const counters = {
    navigationAttempted: 0,
    navigationFulfilled: 0,
    clickAttempted: 0,
    clickFulfilled: 0,
    readinessAttempted: 0,
    readinessFulfilled: 0,
    fillAttempted: 0,
    fillFulfilled: 0,
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
  const filteredZero = async (filter, query, targetTexts, emptyTexts) => {
    if (await filter.count() !== 1) throw new Error("FilterCountError");
    const regionId = await filter.getAttribute("aria-controls");
    if (typeof regionId !== "string" || !/^[A-Za-z][A-Za-z0-9_-]{0,127}$/.test(regionId)) throw new Error("FilterRegionBindingError");
    const resultsRoot = secureConsoleOwnedTaskTabV3.playwright.locator(`#${regionId}`);
    if (await resultsRoot.count() !== 1) throw new Error("FilterRegionCountError");
    await readyOne(resultsRoot.locator('[aria-label="Pagination"]'));
    const readState = async () => resultsRoot.evaluate((root, expectedEmptyTexts) => {
      const pagerList = [...root.querySelectorAll('[aria-label="Pagination"]')];
      if (pagerList.length !== 1) return { terminalZero: false, completeNonempty: false };
      const pager = pagerList[0];
      const match = /^(\d+)\s*[-–]\s*(\d+)\s+of\s+(\d+)$/.exec((pager.textContent || "").replace(/\s+/g, " ").trim());
      const rows = root.querySelectorAll("table tbody tr").length;
      const statuses = [...root.querySelectorAll('[role="status"]')].filter((item) => expectedEmptyTexts.includes((item.textContent || "").trim()));
      const buttons = [...pager.querySelectorAll("button")];
      const next = buttons.filter((item) => item.getAttribute("aria-label") === "Next page");
      const previous = buttons.filter((item) => item.getAttribute("aria-label") === "Previous page");
      const disabled = (item) => item.hasAttribute("disabled") || item.getAttribute("aria-disabled") === "true";
      const busy = root.matches('[aria-busy="true"]') || root.querySelector('[aria-busy="true"]') !== null;
      if (busy || match === null || next.length !== 1 || previous.length !== 1) return { terminalZero: false, completeNonempty: false };
      const start = Number(match[1]), end = Number(match[2]), total = Number(match[3]);
      return {
        terminalZero: start === 0 && end === 0 && total === 0 && rows === 0 && statuses.length === 1 && disabled(next[0]) && disabled(previous[0]),
        completeNonempty: start === 1 && end === rows && total >= rows && rows > 0 && statuses.length === 0 && disabled(previous[0]) && disabled(next[0]) === (end >= total),
      };
    }, emptyTexts);
    counters.fillAttempted++;
    await filter.fill("");
    counters.fillFulfilled++;
    const baseline = await readState();
    if (baseline.terminalZero !== true && baseline.completeNonempty !== true) throw new Error("FilterBaselineIncompleteError");
    counters.fillAttempted++;
    await filter.fill(query);
    counters.fillFulfilled++;
    const exactEmpty = new RegExp(`^(?:${emptyTexts.map((text) => text.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")).join("|")})$`);
    const emptyStatus = resultsRoot.getByRole("status").filter({ hasText: exactEmpty });
    counters.readinessAttempted++;
    await emptyStatus.waitFor({ state: "visible", timeoutMs: 20000 });
    counters.readinessFulfilled++;
    if (await emptyStatus.count() !== 1) throw new Error("FilteredEmptyStatusCountError");
    const queryExact = await filter.evaluate((input, expected) => input.value === expected, query);
    const completion = await readState();
    if (!queryExact || completion.terminalZero !== true) throw new Error("FilteredResultsIncompleteError");
    const counts = [];
    for (const text of targetTexts) counts.push(await resultsRoot.getByRole("row").filter({ hasText: text }).count());
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
      ["ai-api-omniroute.mysw.me"],
      ["No DNS records found", "No records found"],
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
    if (await rateTable.count() !== 1) throw new Error("RateTableCountError");
    const ratePaginator = ratePanel.locator('[aria-label="Pagination"]');
    await readyOne(ratePaginator);
    const rateProof = await rateTable.evaluate((table, panelId) => {
      const rows = [...table.querySelectorAll("tbody tr")];
      const text = table.innerText || "";
      const scope = document.getElementById(panelId);
      const panelBound = scope !== null && scope.querySelectorAll("table").length === 1 && scope.querySelector("table") === table;
      const pagers = panelBound ? [...scope.querySelectorAll('[aria-label="Pagination"]')] : [];
      const pager = pagers.length === 1 ? pagers[0] : null;
      const match = /^(\d+)\s*[-–]\s*(\d+)\s+of\s+(\d+)$/.exec((pager?.textContent || "").replace(/\s+/g, " ").trim());
      const buttons = pager === null ? [] : [...pager.querySelectorAll("button")];
      const next = buttons.filter((item) => item.getAttribute("aria-label") === "Next page");
      const previous = buttons.filter((item) => item.getAttribute("aria-label") === "Previous page");
      const disabled = (item) => item.hasAttribute("disabled") || item.getAttribute("aria-disabled") === "true";
      const busy = scope?.matches('[aria-busy="true"]') || scope?.querySelector('[aria-busy="true"]') !== null;
      const paginationComplete = match !== null && Number(match[1]) === 1 && Number(match[2]) === rows.length && Number(match[3]) === rows.length && next.length === 1 && previous.length === 1 && disabled(next[0]) && disabled(previous[0]) && !busy;
      return {
        dataRowCount: rows.length,
        targetDescriptionCount: (text.match(/OmniRoute team API 20 per 10s/g) || []).length,
        targetHostCount: (text.match(/ai-api-omniroute\.mysw\.me/g) || []).length,
        paginationComplete,
        panelBound,
      };
    }, ratePanelId);
    rateDataRowCount = rateProof.dataRowCount;
    rateTargetDescriptionCount = rateProof.targetDescriptionCount;
    rateTargetHostCount = rateProof.targetHostCount;
    rateCompletenessProven = rateProof.panelBound === true && rateProof.paginationComplete === true;
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
    [tunnelTargetNameCount] = await filteredZero(tunnelFilter, "omniroute-team-tunnel", ["omniroute-team-tunnel"], ["No tunnels found"]);
    await navigate(zeroTrustUrl.href);
    const tunnelHostUrl = new URL(await secureConsoleOwnedTaskTabV3.url());
    const tunnelHostPath = /^\/([0-9a-f]{32})(?:\/home)?\/?$/.exec(tunnelHostUrl.pathname);
    if (tunnelHostUrl.hostname !== "one.dash.cloudflare.com" || tunnelHostPath === null || tunnelHostPath[1] !== accountSegment) throw new Error("TunnelHostAccountBindingError");
    const networksButtonForHost = secureConsoleOwnedTaskTabV3.playwright.getByRole("button", { name: "Networks", exact: true });
    await readyOne(networksButtonForHost);
    await clickOne(networksButtonForHost);
    const tunnelsLinkForHost = secureConsoleOwnedTaskTabV3.playwright.getByRole("link", { name: /tunnels/i });
    await readyOne(tunnelsLinkForHost);
    await clickOne(tunnelsLinkForHost);
    await readyOne(secureConsoleOwnedTaskTabV3.playwright.getByText(/create.*tunnel/i));
    const tunnelHostFilter = secureConsoleOwnedTaskTabV3.playwright.getByRole("textbox", { name: /search tunnels/i });
    [tunnelTargetHostCount] = await filteredZero(tunnelHostFilter, "ai-api-omniroute.mysw.me", ["ai-api-omniroute.mysw.me"], ["No tunnels found"]);
    tunnelFiltersComplete = true;

    const accessButton = secureConsoleOwnedTaskTabV3.playwright.getByRole("button", { name: "Access", exact: true });
    await readyOne(accessButton);
    await clickOne(accessButton);
    const applicationsLink = secureConsoleOwnedTaskTabV3.playwright.getByRole("link", { name: /applications/i });
    await readyOne(applicationsLink);
    await clickOne(applicationsLink);
    await readyOne(secureConsoleOwnedTaskTabV3.playwright.getByText(/add an application|add application/i));
    const accessFilter = secureConsoleOwnedTaskTabV3.playwright.getByRole("textbox", { name: /search applications/i });
    [accessTargetHostCount] = await filteredZero(accessFilter, "ai-api-omniroute.mysw.me", ["ai-api-omniroute.mysw.me"], ["No applications found"]);
    await navigate(zeroTrustUrl.href);
    const accessNameUrl = new URL(await secureConsoleOwnedTaskTabV3.url());
    const accessNamePath = /^\/([0-9a-f]{32})(?:\/home)?\/?$/.exec(accessNameUrl.pathname);
    if (accessNameUrl.hostname !== "one.dash.cloudflare.com" || accessNamePath === null || accessNamePath[1] !== accountSegment) throw new Error("AccessNameAccountBindingError");
    const accessButtonForName = secureConsoleOwnedTaskTabV3.playwright.getByRole("button", { name: "Access", exact: true });
    await readyOne(accessButtonForName);
    await clickOne(accessButtonForName);
    const applicationsLinkForName = secureConsoleOwnedTaskTabV3.playwright.getByRole("link", { name: /applications/i });
    await readyOne(applicationsLinkForName);
    await clickOne(applicationsLinkForName);
    await readyOne(secureConsoleOwnedTaskTabV3.playwright.getByText(/add an application|add application/i));
    const accessNameFilter = secureConsoleOwnedTaskTabV3.playwright.getByRole("textbox", { name: /search applications/i });
    [accessTargetNameCount] = await filteredZero(accessNameFilter, "OmniRoute team API", ["OmniRoute team API"], ["No applications found"]);
    accessFiltersComplete = true;

    await navigate("https://dash.cloudflare.com/profile/api-tokens");
    const tokenFilter = secureConsoleOwnedTaskTabV3.playwright.getByRole("textbox", { name: /search api tokens/i });
    [tokenRowCount] = await filteredZero(tokenFilter, "OmniRoute secure console R5 20260901", ["OmniRoute secure console R5 20260901"], ["No API tokens found", "No tokens found"]);
    tokenFilterComplete = true;
    tokenTitleExact = await secureConsoleOwnedTaskTabV3.title() === "API Tokens | Cloudflare";
    tokenCreateControlCount =
      await secureConsoleOwnedTaskTabV3.playwright.getByRole("button", { name: "Create Token", exact: true }).count() +
      await secureConsoleOwnedTaskTabV3.playwright.getByRole("link", { name: "Create Token", exact: true }).count();
    const tokenRegionId = await tokenFilter.getAttribute("aria-controls");
    if (typeof tokenRegionId !== "string" || !/^[A-Za-z][A-Za-z0-9_-]{0,127}$/.test(tokenRegionId)) throw new Error("FinalTokenRegionBindingError");
    const tokenResultRegion = secureConsoleOwnedTaskTabV3.playwright.locator(`#${tokenRegionId}`);
    if (await tokenResultRegion.count() !== 1) throw new Error("FinalTokenRegionCountError");
    tokenNameCount = await tokenResultRegion.getByText("OmniRoute secure console R5 20260901", { exact: true }).count();
    if (!tokenTitleExact || tokenCreateControlCount !== 1 || tokenNameCount !== 0 || tokenRowCount !== 0 ||
        !dnsFilterComplete || !rateCompletenessProven || !tunnelFiltersComplete || !accessFiltersComplete || !tokenFilterComplete) {
      throw new Error("FinalTokenPageStateError");
    }
    if (counters.navigationAttempted !== 6 || counters.navigationFulfilled !== 6 ||
        counters.clickAttempted !== 13 || counters.clickFulfilled !== 13 ||
        counters.readinessAttempted !== 33 || counters.readinessFulfilled !== 33 ||
        counters.fillAttempted !== 12 || counters.fillFulfilled !== 12) {
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
    fillAttempted: counters.fillAttempted,
    fillFulfilled: counters.fillFulfilled,
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
navigation `6/6`; clicks `13/13`, each preceded by count one; native locator
readiness `33/33`;
page-local search fills `12/12` (six clear/query pairs only);
DNS target `0` with exact filter complete; rate unique-table data rows `1`,
target description/host `0/0`, and exact terminal paginator; Tunnel name/host
`0/0` with both filters complete; Access host/name `0/0` with both filters
complete; final token title true, Create count `1`, token name/row `0/0`, and
exact filter complete; write attempted `1`;
`errorClass=NONE`; complete untruncated output; completed tool status; and the
later private consumed/state tuple exact. The cell sets consumed/state only
after `nodeRepl.write` returns. Any discrepancy spends the replacement and
routes, after proven full completion only, to the pre-Create detach cell.

These twelve fills are the only additional browser mutations in this cell and
are confined to the six bound page-local search inputs. No Create, edit,
delete, provider-persistent, or other form mutation is authorized.

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
