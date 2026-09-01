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
| adopt and token readiness | `6237` | `2D44E317D0854190CD9BED930697CCED4CD180D9CE48D3B91EB6BF437BADCA07` |
| fresh Cloudflare prestart reads | `9907` | `498A7DC10EC693E649CF3B053EC7F1BAE18D0307419339487356458D415D83BB` |
| pre-Create detach | `2196` | `467F98589FD335AC6393B8BFEF64D7A3101EBE27C5BAA74E37A7FABA68AC5F60` |
| post-native detach | `2201` | `55B407F463C351B64174800617E8B3F64B3CE98D60BAA1BEAEF1E6D3312B10A5` |

## V3 retained-tab adoption and token-page readiness

The sole owner runs this exact cell once in the same persistent Node session
with one fixed outer tool deadline of `60000 ms`. It validates the exact V1 and
spent-V2 declarations, calls `secureConsoleChromeV1.tabs.get()` exactly once
for the retained ID, performs exactly one navigation to
`https://dash.cloudflare.com/profile/api-tokens`, then performs exactly one
fixed `20000 ms` locator readiness wait before title/control/name/row checks.

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
      typeof adopted.title === "function" &&
      typeof adopted.playwright?.getByRole === "function" &&
      typeof adopted.playwright?.getByText === "function";
    if (!tabShape) throw new Error("RetainedTabOwnershipError");

    counters.navigationAttempted++;
    await adopted.goto("https://dash.cloudflare.com/profile/api-tokens");
    counters.navigationFulfilled++;
    const readinessMarker = adopted.playwright.getByText("Create Token", { exact: true }).first();
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
    if (!titleExact || createControlCount !== 1 || tokenNameCount !== 0 || matchingRowCount !== 0) {
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

Exact PASS requires the fixed PASS terminal; all five booleans true; exact
title true; Create count `1`; token-name/row `0/0`; get, navigation, readiness,
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
  let dnsTargetCount = -1;
  let rateDataRowCount = -1;
  let rateTargetDescriptionCount = -1;
  let rateTargetHostCount = -1;
  let tunnelTargetNameCount = -1;
  let tunnelTargetHostCount = -1;
  let accessTargetHostCount = -1;
  let accessTargetNameCount = -1;
  let tokenTitleExact = false;
  let tokenCreateControlCount = -1;
  let tokenNameCount = -1;
  let tokenRowCount = -1;
  const safeErrorClass = (error) => {
    const name = typeof error?.name === "string" ? error.name : "";
    return /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(name) ? name : "CloudflarePrestartReadError";
  };
  const navigate = async (url) => {
    counters.navigationAttempted++;
    await secureConsoleOwnedTaskTabV3.goto(url);
    counters.navigationFulfilled++;
  };
  const click = async (locator) => {
    counters.clickAttempted++;
    await locator.click();
    counters.clickFulfilled++;
  };
  const ready = async (locator) => {
    counters.readinessAttempted++;
    await locator.waitFor({ state: "visible", timeoutMs: 20000 });
    counters.readinessFulfilled++;
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
    await ready(zoneAnchor.first());
    if (await zoneAnchor.count() !== 1) throw new Error("ZoneAnchorCountError");
    const zoneHref = await zoneAnchor.getAttribute("href");
    const zoneUrl = new URL(zoneHref, "https://dash.cloudflare.com");
    if (zoneUrl.protocol !== "https:" || zoneUrl.hostname !== "dash.cloudflare.com" || !/\/mysw\.me\/?$/.test(zoneUrl.pathname)) {
      throw new Error("ZoneHrefShapeError");
    }
    await navigate(zoneUrl.href);
    await ready(secureConsoleOwnedTaskTabV3.playwright.getByText("mysw.me", { exact: true }).first());

    const dnsButton = secureConsoleOwnedTaskTabV3.playwright.getByRole("button", { name: "DNS", exact: true });
    await click(dnsButton);
    const dnsRecordsLink = secureConsoleOwnedTaskTabV3.playwright.getByRole("link", { name: /DNS Records/i });
    await ready(dnsRecordsLink.first());
    await click(dnsRecordsLink.first());
    await ready(secureConsoleOwnedTaskTabV3.playwright.getByText(/Add record/i).first());
    dnsTargetCount = await secureConsoleOwnedTaskTabV3.playwright.getByText("ai-api-omniroute.mysw.me", { exact: true }).count();
    if (dnsTargetCount !== 0) throw new Error("TargetDnsRecordPresentError");

    const securityButton = secureConsoleOwnedTaskTabV3.playwright.getByRole("button", { name: "Security", exact: true });
    await click(securityButton);
    const securityRulesLink = secureConsoleOwnedTaskTabV3.playwright.getByRole("link", { name: /security rules/i });
    await ready(securityRulesLink.first());
    await click(securityRulesLink.first());
    const rateButton = secureConsoleOwnedTaskTabV3.playwright.getByRole("button", { name: /rate limiting/i });
    await ready(rateButton.first());
    await click(rateButton.first());
    await ready(secureConsoleOwnedTaskTabV3.playwright.getByText(/rate limiting rules/i).first());
    const rateProof = await rateButton.first().evaluate((element) => {
      let box = element;
      for (let index = 0; index < 4; index++) box = box.parentElement;
      const rows = [...box.querySelectorAll("tr")];
      const text = box.innerText || "";
      return {
        dataRowCount: Math.max(0, rows.length - 1),
        targetDescriptionCount: (text.match(/OmniRoute team API 20 per 10s/g) || []).length,
        targetHostCount: (text.match(/ai-api-omniroute\.mysw\.me/g) || []).length,
      };
    });
    rateDataRowCount = rateProof.dataRowCount;
    rateTargetDescriptionCount = rateProof.targetDescriptionCount;
    rateTargetHostCount = rateProof.targetHostCount;
    if (rateDataRowCount !== 1 || rateTargetDescriptionCount !== 0 || rateTargetHostCount !== 0) {
      throw new Error("RateRuleStateError");
    }

    const zeroTrustAnchor = secureConsoleOwnedTaskTabV3.playwright.locator("a").filter({ hasText: "Zero Trust" });
    await ready(zeroTrustAnchor.first());
    if (await zeroTrustAnchor.count() !== 1) throw new Error("ZeroTrustAnchorCountError");
    const zeroTrustHref = await zeroTrustAnchor.getAttribute("href");
    const zeroTrustUrl = new URL(zeroTrustHref, "https://dash.cloudflare.com");
    if (zeroTrustUrl.protocol !== "https:" || !/(^|\.)dash\.cloudflare\.com$/.test(zeroTrustUrl.hostname)) {
      throw new Error("ZeroTrustHrefShapeError");
    }
    await navigate(zeroTrustUrl.href);
    const networksButton = secureConsoleOwnedTaskTabV3.playwright.getByRole("button", { name: "Networks", exact: true });
    await ready(networksButton);
    await click(networksButton);
    const tunnelsLink = secureConsoleOwnedTaskTabV3.playwright.getByRole("link", { name: /tunnels/i });
    await ready(tunnelsLink.first());
    await click(tunnelsLink.first());
    await ready(secureConsoleOwnedTaskTabV3.playwright.getByText(/create.*tunnel/i).first());
    tunnelTargetNameCount = await secureConsoleOwnedTaskTabV3.playwright.getByText("omniroute-team-tunnel", { exact: true }).count();
    tunnelTargetHostCount = await secureConsoleOwnedTaskTabV3.playwright.getByText(/ai-api-omniroute\.mysw\.me/).count();
    if (tunnelTargetNameCount !== 0 || tunnelTargetHostCount !== 0) throw new Error("TunnelOrConnectorPresentError");

    const accessButton = secureConsoleOwnedTaskTabV3.playwright.getByRole("button", { name: "Access", exact: true });
    await ready(accessButton);
    await click(accessButton);
    const applicationsLink = secureConsoleOwnedTaskTabV3.playwright.getByRole("link", { name: /applications/i });
    await ready(applicationsLink.first());
    await click(applicationsLink.first());
    await ready(secureConsoleOwnedTaskTabV3.playwright.getByText(/add an application|add application/i).first());
    accessTargetHostCount = await secureConsoleOwnedTaskTabV3.playwright.getByText(/ai-api-omniroute\.mysw\.me/).count();
    accessTargetNameCount = await secureConsoleOwnedTaskTabV3.playwright.getByText(/OmniRoute team API/i).count();
    if (accessTargetHostCount !== 0 || accessTargetNameCount !== 0) throw new Error("AccessApplicationPresentError");

    await navigate("https://dash.cloudflare.com/profile/api-tokens");
    await ready(secureConsoleOwnedTaskTabV3.playwright.getByText("Create Token", { exact: true }).first());
    tokenTitleExact = await secureConsoleOwnedTaskTabV3.title() === "API Tokens | Cloudflare";
    tokenCreateControlCount =
      await secureConsoleOwnedTaskTabV3.playwright.getByRole("button", { name: "Create Token", exact: true }).count() +
      await secureConsoleOwnedTaskTabV3.playwright.getByRole("link", { name: "Create Token", exact: true }).count();
    tokenNameCount = await secureConsoleOwnedTaskTabV3.playwright.getByText("OmniRoute secure console R5 20260901", { exact: true }).count();
    tokenRowCount = await secureConsoleOwnedTaskTabV3.playwright.getByRole("row").filter({ hasText: "OmniRoute secure console R5 20260901" }).count();
    if (!tokenTitleExact || tokenCreateControlCount !== 1 || tokenNameCount !== 0 || tokenRowCount !== 0) {
      throw new Error("FinalTokenPageStateError");
    }
    if (counters.navigationAttempted !== 4 || counters.navigationFulfilled !== 4 ||
        counters.clickAttempted !== 9 || counters.clickFulfilled !== 9 ||
        counters.readinessAttempted !== 15 || counters.readinessFulfilled !== 15) {
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
    navigationAttempted: counters.navigationAttempted,
    navigationFulfilled: counters.navigationFulfilled,
    clickAttempted: counters.clickAttempted,
    clickFulfilled: counters.clickFulfilled,
    readinessAttempted: counters.readinessAttempted,
    readinessFulfilled: counters.readinessFulfilled,
    dnsTargetCount,
    rateDataRowCount,
    rateTargetDescriptionCount,
    rateTargetHostCount,
    tunnelTargetNameCount,
    tunnelTargetHostCount,
    accessTargetHostCount,
    accessTargetNameCount,
    tokenTitleExact,
    tokenCreateControlCount,
    tokenNameCount,
    tokenRowCount,
    writeAttempted: counters.writeAttempted,
    errorClass,
  });
  secureConsoleCloudflareReadsV3Consumed = true;
  secureConsoleOwnedTaskTabV3State = result === "EXACT_V3_CLOUDFLARE_PRESTART_READS_PASS"
    ? "CLOUDFLARE_PRESTART_READS_PASS"
    : "CLOUDFLARE_PRESTART_READS_FAILED";
})();
```

Exact PASS requires declarations/precondition true; navigation `4/4`; clicks
`9/9`; readiness `15/15`; DNS target `0`; rate data rows `1` with target
description/host `0/0`; Tunnel name/host `0/0`; Access host/name `0/0`; final
token title true, Create count `1`, token name/row `0/0`; write attempted `1`;
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
