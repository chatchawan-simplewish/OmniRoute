# Task 2 secure-console token-page readiness V4 replacement brief

Status: **PROPOSED — not executable until independent Sol High PASS review and execution-authority classification**

`authorizes_live_execution=false`

## Purpose and exact predecessor state

This is one new no-retry V4 replacement for the V3 gate and disposition spent
at incident commit `172da50d2b841398c6e4c1d55942e3f6a75d38eb`. It is not a
retry, continuation, repair, or reuse of V3. The V3 execution-authority
classification is `5b221c05d3181a23eb754e3a99aebd1954686f80`, the direct
parent of that incident.

The only reusable live objects are the same-session `secureConsoleChromeV1`
controller, `secureConsoleAgentV1`, and exact retained
`secureConsoleTaskTabV1.id`. Before V4, the exact persistent Node tuple must be:

- spent V2 binding null, eligibility false, state
  `RETAINED_UNTOUCHED_PRECREATE_FAILURE`, pre-Create consumed true, and
  post-native consumed false;
- spent V3 binding null, eligibility false, state
  `V3_ADOPTION_OR_READINESS_FAILED`, pre-Create consumed false, post-native
  consumed false, and Cloudflare reads consumed false; and
- the completed V3 pre-Create disposition declarations remain present with
  precondition false, attempted/fulfilled `0/0`, and result
  `PRECONDITION_FAIL`.

The durable V3 incident proves that the false/zero pre-Create tuple was already
invoked and spent; it is not an unused disposition. The current browser page is
`NOT_PROVEN`. No page, tab, title, URL, DOM, screenshot, or metadata inspection
is permitted before the V4 cell.

## Inherited contract without relaxation

Except for the new V4 binding, semantic-readiness, prestart-read, and detach
cells, inherit every target, fixed value, permission, counter, timeout, secret
boundary, confirmation, revocation hold, cleanup rule, and terminal from:

- live brief commit `7af3ab75ec87d81d75811ff8f2e9b4fa9d0c3e3b`;
- scope-replacement brief/PASS/classification commits
  `20cfaf30e57901b90126af973588bbb65601e7b2`,
  `1f1ec923e9cd3bab16315ab077c525be67525d07`, and
  `c23aec59d87f55b6fc2a24ed0f85b5061767a3ab`;
- corrected V3 brief commit `e562b17e5c5ad9ab8360766693d8df3d7cf2bd35`;
- V3 Sol High PASS review commit
  `139c0b971d120647c319d3b5b5672aca67f94db9`; and
- redacted V3 incident commit
  `172da50d2b841398c6e4c1d55942e3f6a75d38eb`.

The fresh local, VM1205, public-DNS, and OmniRoute checks inherited by V3 remain
accepted only while the incident zero-action boundary, exact same Node session,
empty Git index, and unrelated dirty baseline remain unchanged. Any drift stops
before browser use.

The exact token remains `OmniRoute secure console R5 20260901`, zone `mysw.me`,
and only `Zone WAF Edit` plus `Zone Read`. No DNS, Tunnel, Access, account,
token-management, or other permission is added. No public rollout, Tunnel,
DNS/public-hostname, Access application, OmniRoute key/model request, alternate
bridge, retry, fallback, handoff, second start, or verdict relaxation is
authorized.

## Reproducible source-projection gate

Immediately before browser use, recompute the working projection from the
repository root. The only excluded paths, compared as ordinal `/`-separated
strings, are `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/` plus
exactly:

- `task-2-secure-console-transfer-token-page-readiness-v4-replacement-brief.md`;
- `task-2-secure-console-transfer-token-page-readiness-v4-replacement-sol-review.md`; and
- `task-2-secure-console-transfer-token-page-readiness-v4-replacement-execution-classification.md`.

No directory, glob, prefix, suffix, historical artifact, or other path is
excluded. Reject control characters. Enumerate tracked paths with `git ls-files`
and nonignored untracked files with `git ls-files --others --exclude-standard`.
For each nonexcluded path emit ASCII
`K<TAB>PATH<TAB>LENGTH<TAB>SHA256<LF>`: `K` is `T` for a present tracked file,
`D` with length `-1` and hash `-` for a missing tracked file, or `U` for an
untracked file. Length and uppercase SHA-256 cover exact working bytes. Sort
complete lines ordinally, concatenate without BOM or transformation, and hash
those bytes. Required digest:
`A792CFD81D9ED03C341EAD7AC3A631435308FE59A7B286DE7308E14C13E74B57` over
`10661` records.

`git diff --cached --quiet` must succeed. After the three exclusions, exact
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

## Direct provenance and future classification

The V3 incident path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-token-page-readiness-v3-title-incident.md`
at commit `172da50d2b841398c6e4c1d55942e3f6a75d38eb` is `5104` bytes,
SHA-256 `E57C82BA099832C4FFD2EB096CE7439288F8688E75C19D1A0F29AA1BA6FD1CFD`,
and has classification commit `5b221c05d3181a23eb754e3a99aebd1954686f80`
as direct parent. The future committed V4 brief must have that incident as
direct parent; its independent V4 Sol High review must have the V4 brief as
direct parent; and the V4 execution classification must have that review as
direct parent.

The classification records full commits, exact paths, direct byte lengths, and
SHA-256 values for the committed V3 incident, committed V4 brief, and committed
V4 review, plus the expected classification path and projection digest. It must
not claim its own commit, byte length, hash, blob identity, or current HEAD.
After the classification is committed, the root coordinator records a separate,
non-committed action-time tuple containing the classification commit, direct
parent, exact path, direct bytes, direct SHA-256, current HEAD, and projection.
It is valid only when HEAD equals the classification commit, its parent equals
the reviewed V4 review, and every direct byte pin reproduces.

## Exact executable pins

The consumed V2 and V3 JavaScript fences are historical state evidence only and
must never execute again:

| Historical fence | Bytes | SHA-256 |
| --- | ---: | --- |
| V2 adoption | `3608` | `73BD7B0DF858FA29C2C182CC535FBB4695732011898CF8718724CAD35259FD1D` |
| V2 pre-Create detach | `2030` | `E457BC6BDF47A70A12BEEEC5ACE859A4CF7FEEC0B6B782C8A3EBAE7081887A20` |
| V2 post-native detach | `2066` | `0A3554F25F598C98D60F35853019D4F0741AEE6EF68F4105A951D657E1CC2A1D` |
| V3 adoption/readiness | `11761` | `3DD84179EED98D1FAE77BD48A62AE1B3C28EB30630931038E52B38BAD24F6DC9` |
| V3 prestart reads | `19737` | `C9299E0BE4FFFB211B052C1F0E71D8DBEAFA89422EFA5BFC0BB88C380F65EE73` |
| V3 pre-Create detach | `2196` | `467F98589FD335AC6393B8BFEF64D7A3101EBE27C5BAA74E37A7FABA68AC5F60` |
| V3 post-native detach | `2201` | `55B407F463C351B64174800617E8B3F64B3CE98D60BAA1BEAEF1E6D3312B10A5` |

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

The four new JavaScript fence pins cover direct LF-only UTF-8 bytes including
the final LF:

| New V4 fence | Bytes | SHA-256 |
| --- | ---: | --- |
| adopt and semantic readiness | `13251` | `2D3F9C743D29B0AA5AB7A92BA3F1123F332DB664107FFA80DDBF9AB209A6D200` |
| fresh Cloudflare prestart reads | `20437` | `FAB457F36F3AEA9EFF89716DD28C30751B2F7607683E31CCCBA4D7F9C4A6AEBB` |
| pre-Create detach | `2309` | `60692947118FCD2CA765B8C7C850490B79B9ED3C0D3942D14CB5F429F924746D` |
| post-native detach | `2305` | `5ABC144ABA9866294EC4A7746906E3D3132ADAE993B93969C426295085FE102D` |

## V4 retained-tab adoption and semantic token-page readiness

The sole Sol High owner runs this exact cell once in the same persistent Node
session with fixed outer deadline `60000 ms`. It performs exactly one retained
ID `tabs.get`, one navigation to
`https://dash.cloudflare.com/profile/api-tokens`, and no title read. It requires
the exact post-navigation URL plus a unique token-search input, its unique
`aria-controls` result region, one exact Create Token semantic control, exact
paginator totals/rows/no-busy terminal, and one exact query echo after the sole
page-local token-name fill. No title text is accepted, rejected, read, or
output.

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
    getAttempted: 0,
    getFulfilled: 0,
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
      typeof secureConsoleOwnedTaskTabV2PostNativeDetachConsumed === "boolean" &&
      typeof secureConsoleOwnedTaskTabV3 === "object" &&
      typeof secureConsoleOwnedTaskTabV3Eligible === "boolean" &&
      typeof secureConsoleOwnedTaskTabV3State === "string" &&
      typeof secureConsoleOwnedTaskTabV3PreCreateDetachConsumed === "boolean" &&
      typeof secureConsoleOwnedTaskTabV3PostNativeDetachConsumed === "boolean" &&
      typeof secureConsoleCloudflareReadsV3Consumed === "boolean" &&
      typeof preCreateDetachAttemptedV3 === "number" &&
      typeof preCreateDetachFulfilledV3 === "number" &&
      typeof preCreateDetachDeclarationsV3 === "boolean" &&
      typeof preCreateDetachPreconditionV3 === "boolean" &&
      typeof preCreateDetachResultV3 === "string";
    if (!declarationShape) throw new Error("RetainedDeclarationShapeError");
    predecessorStateExact =
      secureConsoleOwnedTaskTabV2 === null &&
      secureConsoleOwnedTaskTabV2Eligible === false &&
      secureConsoleOwnedTaskTabV2State === "RETAINED_UNTOUCHED_PRECREATE_FAILURE" &&
      secureConsoleOwnedTaskTabV2PreCreateDetachConsumed === true &&
      secureConsoleOwnedTaskTabV2PostNativeDetachConsumed === false &&
      secureConsoleOwnedTaskTabV3 === null &&
      secureConsoleOwnedTaskTabV3Eligible === false &&
      secureConsoleOwnedTaskTabV3State === "V3_ADOPTION_OR_READINESS_FAILED" &&
      secureConsoleOwnedTaskTabV3PreCreateDetachConsumed === false &&
      secureConsoleOwnedTaskTabV3PostNativeDetachConsumed === false &&
      secureConsoleCloudflareReadsV3Consumed === false &&
      preCreateDetachDeclarationsV3 === true &&
      preCreateDetachPreconditionV3 === false &&
      preCreateDetachAttemptedV3 === 0 &&
      preCreateDetachFulfilledV3 === 0 &&
      preCreateDetachResultV3 === "PRECONDITION_FAIL";
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
      typeof adopted.playwright?.getByRole === "function" &&
      typeof adopted.playwright?.getByText === "function";
    if (!tabShape) throw new Error("RetainedTabOwnershipError");

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
    result = "EXACT_V4_TOKEN_PAGE_SEMANTIC_READINESS_PASS";
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
    navigationTargetExact,
    createControlCount,
    tokenNameCount,
    matchingRowCount,
    tokenInitialFilterEmpty,
    tokenQueryEchoCount,
    tokenFilterComplete,
    tokenSemanticSignature,
    getAttempted: counters.getAttempted,
    getFulfilled: counters.getFulfilled,
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
  });
  secureConsoleV4AdoptionConsumed = true;
  if (result === "EXACT_V4_TOKEN_PAGE_SEMANTIC_READINESS_PASS") {
    secureConsoleOwnedTaskTabV4 = adopted;
    secureConsoleOwnedTaskTabV4Eligible = true;
    secureConsoleOwnedTaskTabV4State = "TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE";
  } else {
    secureConsoleOwnedTaskTabV4 = null;
    secureConsoleOwnedTaskTabV4Eligible = false;
    secureConsoleOwnedTaskTabV4State = "V4_ADOPTION_OR_READINESS_FAILED";
  }
})();
```

Exact PASS requires the fixed PASS terminal; declaration, predecessor,
ownership, tab-shape, navigation-target, initial-filter, filter-complete, and
semantic-signature booleans true; Create/query-echo counts `1/1`; token
name/row `0/0`; get, navigation, URL, Create, name, and row counters `1/1`;
readiness `3/3`; page-local fill `1/1`; write attempted `1`;
`errorClass=NONE`; complete output; completed tool status; and the later private
V4 consumed/binding tuple exact.

A completed non-PASS internally leaves the V4 binding null, ineligible, state
`V4_ADOPTION_OR_READINESS_FAILED`, and consumed true. No detach cell is then
required or permitted. A missing, truncated, rejected, timed-out, or uncertain
invocation spends V4 externally and permits no later action. The cell performs
no tabs list, reconnect, new tab, reacquisition, title read, screenshot,
`markHandoff`, clipboard, keyboard, Create/edit/delete, provider-persistent
mutation, retry, or fallback.

## Fresh Cloudflare prestart read cell

After exact V4 semantic-readiness PASS and before clipboard clear, proxy start,
preparation, or owner launch, run this exact cell once with fixed outer deadline
240000 ms. It preserves the reviewed DNS, rate-rule, Tunnel/connector,
Access-application, and token-row completeness proofs. The final token page uses
the same title-free semantic signature.

All operations remain serial and bounded. Every filter binds through one
validated ria-controls region. Evaluate callbacks are synchronous snapshots
only; there is no observer, timer, page-resident Promise, expando, async evaluate
callback, concurrent wait, or post-failure cleanup.

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
  let tokenNavigationExact = false;
  let tokenQueryEchoCount = -1;
  let tokenSemanticSignature = false;
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
    await secureConsoleOwnedTaskTabV4.goto(url);
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
    const resultsRoot = secureConsoleOwnedTaskTabV4.playwright.locator(`#${regionId}`);
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
      typeof secureConsoleOwnedTaskTabV4 === "object" &&
      typeof secureConsoleOwnedTaskTabV4Eligible === "boolean" &&
      typeof secureConsoleOwnedTaskTabV4State === "string" &&
      typeof secureConsoleOwnedTaskTabV4PreCreateDetachConsumed === "boolean" &&
      typeof secureConsoleOwnedTaskTabV4PostNativeDetachConsumed === "boolean" &&
      typeof secureConsoleCloudflareReadsV4Consumed === "boolean" &&
      typeof secureConsoleV4AdoptionConsumed === "boolean";
    preconditionValid =
      declarationsValid &&
      secureConsoleOwnedTaskTabV4 !== null &&
      secureConsoleOwnedTaskTabV4Eligible === true &&
      secureConsoleOwnedTaskTabV4State === "TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE" &&
      secureConsoleOwnedTaskTabV4PreCreateDetachConsumed === false &&
      secureConsoleOwnedTaskTabV4PostNativeDetachConsumed === false &&
      secureConsoleCloudflareReadsV4Consumed === false &&
      secureConsoleV4AdoptionConsumed === true;
    if (!preconditionValid) throw new Error("CloudflareReadPreconditionError");

    await navigate("https://dash.cloudflare.com");
    const zoneAnchor = secureConsoleOwnedTaskTabV4.playwright.locator("a").filter({ hasText: "mysw.me" });
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
    await readyOne(secureConsoleOwnedTaskTabV4.playwright.getByText("mysw.me", { exact: true }));

    const dnsButton = secureConsoleOwnedTaskTabV4.playwright.getByRole("button", { name: "DNS", exact: true });
    await clickOne(dnsButton);
    const dnsRecordsLink = secureConsoleOwnedTaskTabV4.playwright.getByRole("link", { name: /DNS Records/i });
    await readyOne(dnsRecordsLink);
    await clickOne(dnsRecordsLink);
    await readyOne(secureConsoleOwnedTaskTabV4.playwright.getByText(/Add record/i));
    [dnsTargetCount] = await filteredZero(
      secureConsoleOwnedTaskTabV4.playwright.getByRole("textbox", { name: /search dns records/i }),
      "ai-api-omniroute.mysw.me",
      ["ai-api-omniroute.mysw.me"],
      ["No DNS records found", "No records found"],
    );
    dnsFilterComplete = true;

    const securityButton = secureConsoleOwnedTaskTabV4.playwright.getByRole("button", { name: "Security", exact: true });
    await clickOne(securityButton);
    const securityRulesLink = secureConsoleOwnedTaskTabV4.playwright.getByRole("link", { name: /security rules/i });
    await readyOne(securityRulesLink);
    await clickOne(securityRulesLink);
    const rateButton = secureConsoleOwnedTaskTabV4.playwright.getByRole("button", { name: /rate limiting/i });
    await readyOne(rateButton);
    const ratePanelId = await rateButton.getAttribute("aria-controls");
    if (typeof ratePanelId !== "string" || !/^[A-Za-z][A-Za-z0-9_-]{0,127}$/.test(ratePanelId)) {
      throw new Error("RatePanelBindingError");
    }
    await clickOne(rateButton);
    const ratePanel = secureConsoleOwnedTaskTabV4.playwright.locator(`#${ratePanelId}`);
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

    const zeroTrustAnchor = secureConsoleOwnedTaskTabV4.playwright.locator("a").filter({ hasText: "Zero Trust" });
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
    const postNavigationUrl = new URL(await secureConsoleOwnedTaskTabV4.url());
    const postPathMatch = /^\/([0-9a-f]{32})(?:\/home)?\/?$/.exec(postNavigationUrl.pathname);
    const accountPageMarkers = secureConsoleOwnedTaskTabV4.playwright.locator(`a[href^="/${accountSegment}/"]`);
    accountBindingExact = postNavigationUrl.protocol === "https:" &&
      postNavigationUrl.hostname === "one.dash.cloudflare.com" &&
      postPathMatch !== null && postPathMatch[1] === accountSegment &&
      await accountPageMarkers.count() > 0;
    if (!accountBindingExact) throw new Error("ZeroTrustAccountBindingError");
    const networksButton = secureConsoleOwnedTaskTabV4.playwright.getByRole("button", { name: "Networks", exact: true });
    await readyOne(networksButton);
    await clickOne(networksButton);
    const tunnelsLink = secureConsoleOwnedTaskTabV4.playwright.getByRole("link", { name: /tunnels/i });
    await readyOne(tunnelsLink);
    await clickOne(tunnelsLink);
    await readyOne(secureConsoleOwnedTaskTabV4.playwright.getByText(/create.*tunnel/i));
    const tunnelFilter = secureConsoleOwnedTaskTabV4.playwright.getByRole("textbox", { name: /search tunnels/i });
    [tunnelTargetNameCount] = await filteredZero(tunnelFilter, "omniroute-team-tunnel", ["omniroute-team-tunnel"], ["No tunnels found"]);
    await navigate(zeroTrustUrl.href);
    const tunnelHostUrl = new URL(await secureConsoleOwnedTaskTabV4.url());
    const tunnelHostPath = /^\/([0-9a-f]{32})(?:\/home)?\/?$/.exec(tunnelHostUrl.pathname);
    if (tunnelHostUrl.hostname !== "one.dash.cloudflare.com" || tunnelHostPath === null || tunnelHostPath[1] !== accountSegment) throw new Error("TunnelHostAccountBindingError");
    const networksButtonForHost = secureConsoleOwnedTaskTabV4.playwright.getByRole("button", { name: "Networks", exact: true });
    await readyOne(networksButtonForHost);
    await clickOne(networksButtonForHost);
    const tunnelsLinkForHost = secureConsoleOwnedTaskTabV4.playwright.getByRole("link", { name: /tunnels/i });
    await readyOne(tunnelsLinkForHost);
    await clickOne(tunnelsLinkForHost);
    await readyOne(secureConsoleOwnedTaskTabV4.playwright.getByText(/create.*tunnel/i));
    const tunnelHostFilter = secureConsoleOwnedTaskTabV4.playwright.getByRole("textbox", { name: /search tunnels/i });
    [tunnelTargetHostCount] = await filteredZero(tunnelHostFilter, "ai-api-omniroute.mysw.me", ["ai-api-omniroute.mysw.me"], ["No tunnels found"]);
    tunnelFiltersComplete = true;

    const accessButton = secureConsoleOwnedTaskTabV4.playwright.getByRole("button", { name: "Access", exact: true });
    await readyOne(accessButton);
    await clickOne(accessButton);
    const applicationsLink = secureConsoleOwnedTaskTabV4.playwright.getByRole("link", { name: /applications/i });
    await readyOne(applicationsLink);
    await clickOne(applicationsLink);
    await readyOne(secureConsoleOwnedTaskTabV4.playwright.getByText(/add an application|add application/i));
    const accessFilter = secureConsoleOwnedTaskTabV4.playwright.getByRole("textbox", { name: /search applications/i });
    [accessTargetHostCount] = await filteredZero(accessFilter, "ai-api-omniroute.mysw.me", ["ai-api-omniroute.mysw.me"], ["No applications found"]);
    await navigate(zeroTrustUrl.href);
    const accessNameUrl = new URL(await secureConsoleOwnedTaskTabV4.url());
    const accessNamePath = /^\/([0-9a-f]{32})(?:\/home)?\/?$/.exec(accessNameUrl.pathname);
    if (accessNameUrl.hostname !== "one.dash.cloudflare.com" || accessNamePath === null || accessNamePath[1] !== accountSegment) throw new Error("AccessNameAccountBindingError");
    const accessButtonForName = secureConsoleOwnedTaskTabV4.playwright.getByRole("button", { name: "Access", exact: true });
    await readyOne(accessButtonForName);
    await clickOne(accessButtonForName);
    const applicationsLinkForName = secureConsoleOwnedTaskTabV4.playwright.getByRole("link", { name: /applications/i });
    await readyOne(applicationsLinkForName);
    await clickOne(applicationsLinkForName);
    await readyOne(secureConsoleOwnedTaskTabV4.playwright.getByText(/add an application|add application/i));
    const accessNameFilter = secureConsoleOwnedTaskTabV4.playwright.getByRole("textbox", { name: /search applications/i });
    [accessTargetNameCount] = await filteredZero(accessNameFilter, "OmniRoute team API", ["OmniRoute team API"], ["No applications found"]);
    accessFiltersComplete = true;

    await navigate("https://dash.cloudflare.com/profile/api-tokens");
    const tokenUrl = new URL(await secureConsoleOwnedTaskTabV4.url());
    tokenNavigationExact = tokenUrl.href === "https://dash.cloudflare.com/profile/api-tokens";
    if (!tokenNavigationExact) throw new Error("FinalTokenNavigationError");
    const tokenFilter = secureConsoleOwnedTaskTabV4.playwright.getByRole("textbox", { name: /search api tokens/i });
    [tokenRowCount] = await filteredZero(tokenFilter, "OmniRoute secure console R5 20260901", ["OmniRoute secure console R5 20260901"], ["No API tokens found", "No tokens found"]);
    const tokenRegionId = await tokenFilter.getAttribute("aria-controls");
    if (typeof tokenRegionId !== "string" || !/^[A-Za-z][A-Za-z0-9_-]{0,127}$/.test(tokenRegionId)) throw new Error("FinalTokenRegionBindingError");
    const tokenResultRegion = secureConsoleOwnedTaskTabV4.playwright.locator(`#${tokenRegionId}`);
    if (await tokenResultRegion.count() !== 1) throw new Error("FinalTokenRegionCountError");
    const tokenQueryEcho = tokenResultRegion.getByText("OmniRoute secure console R5 20260901", { exact: true });
    await readyOne(tokenQueryEcho);
    tokenQueryEchoCount = await tokenQueryEcho.count();
    tokenCreateControlCount =
      await secureConsoleOwnedTaskTabV4.playwright.getByRole("button", { name: "Create Token", exact: true }).count() +
      await secureConsoleOwnedTaskTabV4.playwright.getByRole("link", { name: "Create Token", exact: true }).count();
    tokenNameCount = await tokenResultRegion.locator("table tbody").getByText("OmniRoute secure console R5 20260901", { exact: true }).count();
    tokenFilterComplete = tokenQueryEchoCount === 1 && tokenRowCount === 0;
    tokenSemanticSignature = tokenNavigationExact && tokenCreateControlCount === 1 && tokenNameCount === 0 && tokenFilterComplete;
    if (!tokenSemanticSignature || !dnsFilterComplete || !rateCompletenessProven || !tunnelFiltersComplete || !accessFiltersComplete) {
      throw new Error("FinalTokenPageStateError");
    }
    if (counters.navigationAttempted !== 6 || counters.navigationFulfilled !== 6 ||
        counters.clickAttempted !== 13 || counters.clickFulfilled !== 13 ||
        counters.readinessAttempted !== 34 || counters.readinessFulfilled !== 34 ||
        counters.fillAttempted !== 12 || counters.fillFulfilled !== 12) {
      throw new Error("BrowserCounterError");
    }
    result = "EXACT_V4_CLOUDFLARE_PRESTART_READS_PASS";
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
    tokenNavigationExact,
    tokenQueryEchoCount,
    tokenSemanticSignature,
    tokenCreateControlCount,
    tokenNameCount,
    tokenRowCount,
    tokenFilterComplete,
    writeAttempted: counters.writeAttempted,
    errorClass,
  });
  secureConsoleCloudflareReadsV4Consumed = true;
  secureConsoleOwnedTaskTabV4State = result === "EXACT_V4_CLOUDFLARE_PRESTART_READS_PASS"
    ? "CLOUDFLARE_PRESTART_READS_PASS"
    : "CLOUDFLARE_PRESTART_READS_FAILED";
})();
```

Exact PASS requires declarations/precondition and private account binding true;
navigation `6/6`; clicks `13/13`, each preceded by count one; native readiness
`34/34`; page-local fills `12/12` (six clear/query pairs only); DNS target `0`;
rate unique-table rows `1`, target description/host `0/0`, exact paginator and
no busy state; Tunnel name/host `0/0`; Access host/name `0/0`; final token exact
navigation true, Create/query-echo `1/1`, token name/row `0/0`, semantic
signature true, and exact filter completion; write attempted `1`;
`errorClass=NONE`; complete output; completed tool status; and the later private
consumed/state tuple exact.

The twelve fills remain confined to six page-local search inputs. No Create,
edit, delete, provider-persistent, or other form mutation is authorized. The
cell sets consumed/state only after `nodeRepl.write` returns. Any discrepancy
spends the prestart cell and, after proven full completion only, routes to the
single V4 pre-Create detach cell.

## Mutually exclusive V4 detachment cells

V4 adoption/readiness failure is already fail-closed: its cell leaves the
binding null and ineligible, so neither detach cell may be invoked. Only a
proven pre-Create failure after successful V4 adoption with a live eligible
binding uses this exact `10000 ms`, zero-browser-call cell once:

```javascript
let preCreateDetachAttemptedV4 = 0;
let preCreateDetachFulfilledV4 = 0;
const preCreateDetachDeclarationsV4 =
  typeof secureConsoleOwnedTaskTabV4 === "object" &&
  typeof secureConsoleOwnedTaskTabV4Eligible === "boolean" &&
  typeof secureConsoleOwnedTaskTabV4State === "string" &&
  typeof secureConsoleOwnedTaskTabV4PreCreateDetachConsumed === "boolean" &&
  typeof secureConsoleOwnedTaskTabV4PostNativeDetachConsumed === "boolean" &&
  typeof secureConsoleCloudflareReadsV4Consumed === "boolean" &&
  typeof secureConsoleV4AdoptionConsumed === "boolean";
const preCreateDetachPreconditionV4 =
  preCreateDetachDeclarationsV4 &&
  secureConsoleV4AdoptionConsumed === true &&
  secureConsoleOwnedTaskTabV4 !== null &&
  secureConsoleOwnedTaskTabV4Eligible === true &&
  ["TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE", "CLOUDFLARE_PRESTART_READS_PASS", "CLOUDFLARE_PRESTART_READS_FAILED"].includes(secureConsoleOwnedTaskTabV4State) &&
  secureConsoleOwnedTaskTabV4PreCreateDetachConsumed === false &&
  secureConsoleOwnedTaskTabV4PostNativeDetachConsumed === false;
let preCreateDetachResultV4 = "PRECONDITION_FAIL";
if (preCreateDetachPreconditionV4) {
  preCreateDetachAttemptedV4++;
  secureConsoleOwnedTaskTabV4Eligible = false;
  secureConsoleOwnedTaskTabV4 = null;
  secureConsoleOwnedTaskTabV4State = "RETAINED_TAB_PRECREATE_FAILURE_BINDING_DETACHED";
  secureConsoleOwnedTaskTabV4PreCreateDetachConsumed = true;
  preCreateDetachFulfilledV4++;
  preCreateDetachResultV4 = "EXACT_V4_PRECREATE_BINDING_DETACH_PASS";
}
nodeRepl.write({
  result: preCreateDetachResultV4,
  declarationsValid: preCreateDetachDeclarationsV4,
  preconditionValid: preCreateDetachPreconditionV4,
  detachAttempted: preCreateDetachAttemptedV4,
  detachFulfilled: preCreateDetachFulfilledV4,
  preCreateConsumed: preCreateDetachDeclarationsV4 ? secureConsoleOwnedTaskTabV4PreCreateDetachConsumed : null,
  postNativeConsumed: preCreateDetachDeclarationsV4 ? secureConsoleOwnedTaskTabV4PostNativeDetachConsumed : null,
  browserCalls: 0,
  bindingEligible: preCreateDetachDeclarationsV4 ? secureConsoleOwnedTaskTabV4Eligible : null,
  bindingNull: preCreateDetachDeclarationsV4 ? secureConsoleOwnedTaskTabV4 === null : false,
  bindingState: preCreateDetachDeclarationsV4 ? secureConsoleOwnedTaskTabV4State : "DECLARATION_INVALID",
});
```

After the user reports the inherited native generated-page close, run this
mutually exclusive `10000 ms`, zero-browser-call cell once:

```javascript
let postNativeDetachAttemptedV4 = 0;
let postNativeDetachFulfilledV4 = 0;
const postNativeDetachDeclarationsV4 =
  typeof secureConsoleOwnedTaskTabV4 === "object" &&
  typeof secureConsoleOwnedTaskTabV4Eligible === "boolean" &&
  typeof secureConsoleOwnedTaskTabV4State === "string" &&
  typeof secureConsoleOwnedTaskTabV4PreCreateDetachConsumed === "boolean" &&
  typeof secureConsoleOwnedTaskTabV4PostNativeDetachConsumed === "boolean" &&
  typeof secureConsoleCloudflareReadsV4Consumed === "boolean" &&
  typeof secureConsoleV4AdoptionConsumed === "boolean";
const postNativeDetachPreconditionV4 =
  postNativeDetachDeclarationsV4 &&
  secureConsoleV4AdoptionConsumed === true &&
  secureConsoleOwnedTaskTabV4 !== null &&
  secureConsoleOwnedTaskTabV4Eligible === true &&
  secureConsoleOwnedTaskTabV4State === "CLOUDFLARE_PRESTART_READS_PASS" &&
  secureConsoleCloudflareReadsV4Consumed === true &&
  secureConsoleOwnedTaskTabV4PreCreateDetachConsumed === false &&
  secureConsoleOwnedTaskTabV4PostNativeDetachConsumed === false;
let postNativeDetachResultV4 = "PRECONDITION_FAIL";
if (postNativeDetachPreconditionV4) {
  postNativeDetachAttemptedV4++;
  secureConsoleOwnedTaskTabV4Eligible = false;
  secureConsoleOwnedTaskTabV4 = null;
  secureConsoleOwnedTaskTabV4State = "USER_NATIVE_CLOSE_REPORTED_BINDING_DETACHED";
  secureConsoleOwnedTaskTabV4PostNativeDetachConsumed = true;
  postNativeDetachFulfilledV4++;
  postNativeDetachResultV4 = "EXACT_V4_POST_NATIVE_CLOSE_BINDING_DETACH_PASS";
}
nodeRepl.write({
  result: postNativeDetachResultV4,
  declarationsValid: postNativeDetachDeclarationsV4,
  preconditionValid: postNativeDetachPreconditionV4,
  detachAttempted: postNativeDetachAttemptedV4,
  detachFulfilled: postNativeDetachFulfilledV4,
  preCreateConsumed: postNativeDetachDeclarationsV4 ? secureConsoleOwnedTaskTabV4PreCreateDetachConsumed : null,
  postNativeConsumed: postNativeDetachDeclarationsV4 ? secureConsoleOwnedTaskTabV4PostNativeDetachConsumed : null,
  browserCalls: 0,
  bindingEligible: postNativeDetachDeclarationsV4 ? secureConsoleOwnedTaskTabV4Eligible : null,
  bindingNull: postNativeDetachDeclarationsV4 ? secureConsoleOwnedTaskTabV4 === null : false,
  bindingState: postNativeDetachDeclarationsV4 ? secureConsoleOwnedTaskTabV4State : "DECLARATION_INVALID",
});
```

Each detach PASS requires declarations/precondition true, detach `1/1`, its
mutually exclusive consumed tuple, browser calls `0`, binding null, eligibility
false, exact state, complete output, and completed status. Invocation on an
adoption/readiness failure is forbidden because no live V4 binding exists.
Precondition failure, repeat/opposite invocation, uncertainty, or timeout spends
that disposition. Neither cell proves tab close. No get, list, reconnect, new,
navigation, reload, close, `markHandoff`, page read, screenshot, clipboard,
keyboard, retry, or fallback is permitted.

## Ordering, confirmations, revocation, and cleanup

The order is fixed:

1. validate exact artifacts, post-commit coordinator tuple, action-time pins,
   and predecessor Node tuple;
2. run V4 adoption/semantic readiness once;
3. on any adoption/readiness non-PASS or uncertainty, stop with the internal
   null/ineligible failure state and do not invoke a detach cell;
4. only after exact V4 PASS, run fresh Cloudflare prestart reads once;
5. on a proven pre-Create failure after live V4 adoption, run only the V4
   pre-Create detach cell and stop;
6. only after both V4 cells PASS, execute inherited clipboard clear/empty proof,
   private-proxy wrapper, preparation, retained owner launch, safe readiness,
   and form preparation in their reviewed order;
7. pause for the mandatory combined final Create, user-native semantic Copy,
   and user-native masked Paste confirmation;
8. after the user's native generated-page close report, run only the V4
   post-native detach cell; and
9. preserve the separate exact-row deletion confirmation, universal revocation
   hold, invalid-token proof, retained-owner final disposition, proxy cleanup,
   local cleanup, and redacted evidence terminals unchanged.

After final Create, no agent/browser inspection of the generated-token page or
clipboard is permitted. The user alone performs the one semantic Copy, one
native masked Paste, native generated-page close, and Enter. The later exact-row
deletion remains a separate mandatory confirmation. Standing authority cannot
bypass either checkpoint.

Any failed, malformed, interrupted, timed-out, missing, truncated, or uncertain
consuming action spends its fresh gate. No retry, second get, second readiness
cell, alternate selector/path, list, reconnect, new tab, controller/tab
reacquisition, fallback, manual integration, handoff, permission expansion,
cleanup reuse, or verdict relaxation is permitted. All secret, token,
account/zone/rule identifiers, hrefs, page content, DOM, screenshots, clipboard
bytes, headers, response bodies, and exception messages remain excluded from
output and artifacts.

## Static review gate

Independent Sol High review must pin this file's exact commit, bytes, and
SHA-256; verify direct ancestry and projection; reproduce every JavaScript and
PowerShell byte/hash pin; parse all fences without execution; prove the exact
V1/V2/V3 predecessor tuple, sole V4 get/navigation, title-free semantic
signature, internal adoption-failure disposal, fresh DNS/rate/Tunnel/Access/
token completeness, exact counters, mutually exclusive detach lifecycle,
mandatory confirmations, revocation/cleanup, safe output, and no-retry
boundaries; and return exact PASS. Any FAIL, NOT PROVEN, ambiguity, drift, or
non-PASS blocks execution.
