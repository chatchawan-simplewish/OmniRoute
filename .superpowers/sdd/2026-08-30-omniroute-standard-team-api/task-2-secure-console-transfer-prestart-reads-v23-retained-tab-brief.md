# OmniRoute V23 retained-tab Cloudflare prestart reads brief

`authorizes_live_execution=false`

## Scope and predecessor

This is a new one-shot, retained-handle, credential-free prestart-read contract.
It is a direct child of V23 live PASS report commit
`029ebf916c4c9e7017e72e4f1eefe1c447ea00ad`. V23 readiness is consumed and
must never be retried. Its exact owned tab is retained, eligible, and in state
`TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE_V23`.

The contract invokes no tab discovery, selected/list/get, reconnect, new tab,
Create, edit, delete, credential, clipboard, VM, DNS, routing, listener, or
process action. It reuses only the exact retained V23 handle. It consumes its
own prestart-read flag and makes the handle ineligible before its first await.
An interrupted or uncertain call therefore cannot be continued or retried.

## Reviewed behavior retained and narrowed

The contract preserves the independently reviewed V4 credential-free Cloudflare
prestart reads for:

- exact `mysw.me` account/zone binding;
- zero target DNS record;
- exactly one unrelated rate-limit row and zero target description/host match;
- zero target Tunnel name and hostname;
- zero target Access application hostname and name; and
- final authenticated token-page Create/name/row absence.

The DNS, Tunnel, and Access searches retain the reviewed clear/query,
aria-controls-bound region, exact paginator, terminal-empty, and zero-row
completeness checks. The rate-rule read retains its unique table, exact
paginator, no-busy, and account-panel binding proof.

The final token page deliberately does not reuse the obsolete filter action. It
repeats V23's direct unfiltered inventory proof: one connected visible empty
search input, exact depth-three section, tables `2/1`, body `1`, five visible
rows, zero grid/pagination/busy/empty marker, five visible non-empty candidates,
one global exact Create control, and zero exact target-name/target-row matches.

All evaluator callbacks are synchronous fixed-key snapshots. Output contains
only fixed result/state/error strings, booleans, bounded counts, and counters;
no account ID, zone ID, href, page text, DOM, response, credential, token,
secret, clipboard value, screenshot, or provider identifier is emitted.

## One-shot executable

```javascript
await (async () => {
  const gateWasFresh = secureConsoleCloudflareReadsV23Consumed === false;
  secureConsoleCloudflareReadsV23Consumed = true;
  const counters = {
    navigationAttempted: 0,
    navigationFulfilled: 0,
    clickAttempted: 0,
    clickFulfilled: 0,
    readinessAttempted: 0,
    readinessFulfilled: 0,
    fillAttempted: 0,
    fillFulfilled: 0,
    closeAttempted: 0,
    closeFulfilled: 0,
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
  let tokenSemanticSignature = false;
  let tokenCreateControlCount = -1;
  let tokenNameCount = -1;
  let tokenRowCount = -1;
  let tokenEmptyMarkerCount = -1;
  let tokenVisibleCandidateRowCount = -1;
  let tokenInventoryComplete = false;
  let cleanupState = "NOT_STARTED";
  let residueConverged = true;
  let tab = null;
  const safeErrorClass = (error) => {
    const name = typeof error?.name === "string" ? error.name : "";
    return /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(name) ? name : "CloudflarePrestartReadError";
  };
  const plainRecord = (value) => {
    if (typeof value !== "object" || value === null) return false;
    const prototype = Object.getPrototypeOf(value);
    return prototype === null ||
      (prototype !== null && Object.getPrototypeOf(prototype) === null);
  };
  const exactKeys = (value, expected) => {
    if (!plainRecord(value)) return false;
    const actual = Object.keys(value).sort();
    const wanted = [...expected].sort();
    return actual.length === wanted.length &&
      actual.every((key, index) => key === wanted[index]);
  };
  const trustedProjection = (value, booleanKeys, integerKeys) => {
    if (!exactKeys(value, [...booleanKeys, ...integerKeys])) return null;
    const projected = {};
    for (const key of booleanKeys) {
      if (typeof value[key] !== "boolean") return null;
      projected[key] = value[key];
    }
    for (const key of integerKeys) {
      if (!Number.isSafeInteger(value[key]) || value[key] < -1 || value[key] > 1000000) {
        return null;
      }
      projected[key] = value[key];
    }
    return projected;
  };
  const navigate = async (url) => {
    counters.navigationAttempted++;
    await secureConsoleOwnedTaskTabV23.goto(url);
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
    const resultsRoot = secureConsoleOwnedTaskTabV23.playwright.locator(`#${regionId}`);
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
      typeof secureConsoleOwnedTaskTabV23 === "object" &&
      typeof secureConsoleOwnedTaskTabV23Eligible === "boolean" &&
      typeof secureConsoleOwnedTaskTabV23State === "string" &&
      typeof secureConsoleOwnedTaskTabV23PreCreateDetachConsumed === "boolean" &&
      typeof secureConsoleOwnedTaskTabV23PostNativeDetachConsumed === "boolean" &&
      typeof secureConsoleCloudflareReadsV23Consumed === "boolean" &&
      typeof secureConsoleV23ReadinessConsumed === "boolean";
    preconditionValid =
      declarationsValid &&
      gateWasFresh === true &&
      secureConsoleV23ReadinessConsumed === true &&
      secureConsoleOwnedTaskTabV23 !== null &&
      secureConsoleOwnedTaskTabV23Eligible === true &&
      secureConsoleOwnedTaskTabV23State === "TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE_V23" &&
      secureConsoleOwnedTaskTabV23PreCreateDetachConsumed === false &&
      secureConsoleOwnedTaskTabV23PostNativeDetachConsumed === false &&
      secureConsoleCloudflareReadsV23Consumed === true;
    if (!preconditionValid) throw new Error("CloudflareReadPreconditionError");
    tab = secureConsoleOwnedTaskTabV23;
    secureConsoleOwnedTaskTabV23Eligible = false;
    secureConsoleOwnedTaskTabV23State = "CLOUDFLARE_PRESTART_READS_RUNNING_V23";

    await navigate("https://dash.cloudflare.com");
    const zoneAnchor = secureConsoleOwnedTaskTabV23.playwright.locator("a").filter({ hasText: "mysw.me" });
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
    await readyOne(secureConsoleOwnedTaskTabV23.playwright.getByText("mysw.me", { exact: true }));

    const dnsButton = secureConsoleOwnedTaskTabV23.playwright.getByRole("button", { name: "DNS", exact: true });
    await clickOne(dnsButton);
    const dnsRecordsLink = secureConsoleOwnedTaskTabV23.playwright.getByRole("link", { name: /DNS Records/i });
    await readyOne(dnsRecordsLink);
    await clickOne(dnsRecordsLink);
    await readyOne(secureConsoleOwnedTaskTabV23.playwright.getByText(/Add record/i));
    [dnsTargetCount] = await filteredZero(
      secureConsoleOwnedTaskTabV23.playwright.getByRole("textbox", { name: /search dns records/i }),
      "ai-api-omniroute.mysw.me",
      ["ai-api-omniroute.mysw.me"],
      ["No DNS records found", "No records found"],
    );
    dnsFilterComplete = true;

    const securityButton = secureConsoleOwnedTaskTabV23.playwright.getByRole("button", { name: "Security", exact: true });
    await clickOne(securityButton);
    const securityRulesLink = secureConsoleOwnedTaskTabV23.playwright.getByRole("link", { name: /security rules/i });
    await readyOne(securityRulesLink);
    await clickOne(securityRulesLink);
    const rateButton = secureConsoleOwnedTaskTabV23.playwright.getByRole("button", { name: /rate limiting/i });
    await readyOne(rateButton);
    const ratePanelId = await rateButton.getAttribute("aria-controls");
    if (typeof ratePanelId !== "string" || !/^[A-Za-z][A-Za-z0-9_-]{0,127}$/.test(ratePanelId)) {
      throw new Error("RatePanelBindingError");
    }
    await clickOne(rateButton);
    const ratePanel = secureConsoleOwnedTaskTabV23.playwright.locator(`#${ratePanelId}`);
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

    const zeroTrustAnchor = secureConsoleOwnedTaskTabV23.playwright.locator("a").filter({ hasText: "Zero Trust" });
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
    const postNavigationUrl = new URL(await secureConsoleOwnedTaskTabV23.url());
    const postPathMatch = /^\/([0-9a-f]{32})(?:\/home)?\/?$/.exec(postNavigationUrl.pathname);
    const accountPageMarkers = secureConsoleOwnedTaskTabV23.playwright.locator(`a[href^="/${accountSegment}/"]`);
    accountBindingExact = postNavigationUrl.protocol === "https:" &&
      postNavigationUrl.hostname === "one.dash.cloudflare.com" &&
      postPathMatch !== null && postPathMatch[1] === accountSegment &&
      await accountPageMarkers.count() > 0;
    if (!accountBindingExact) throw new Error("ZeroTrustAccountBindingError");
    const networksButton = secureConsoleOwnedTaskTabV23.playwright.getByRole("button", { name: "Networks", exact: true });
    await readyOne(networksButton);
    await clickOne(networksButton);
    const tunnelsLink = secureConsoleOwnedTaskTabV23.playwright.getByRole("link", { name: /tunnels/i });
    await readyOne(tunnelsLink);
    await clickOne(tunnelsLink);
    await readyOne(secureConsoleOwnedTaskTabV23.playwright.getByText(/create.*tunnel/i));
    const tunnelFilter = secureConsoleOwnedTaskTabV23.playwright.getByRole("textbox", { name: /search tunnels/i });
    [tunnelTargetNameCount] = await filteredZero(tunnelFilter, "omniroute-team-tunnel", ["omniroute-team-tunnel"], ["No tunnels found"]);
    await navigate(zeroTrustUrl.href);
    const tunnelHostUrl = new URL(await secureConsoleOwnedTaskTabV23.url());
    const tunnelHostPath = /^\/([0-9a-f]{32})(?:\/home)?\/?$/.exec(tunnelHostUrl.pathname);
    if (tunnelHostUrl.hostname !== "one.dash.cloudflare.com" || tunnelHostPath === null || tunnelHostPath[1] !== accountSegment) throw new Error("TunnelHostAccountBindingError");
    const networksButtonForHost = secureConsoleOwnedTaskTabV23.playwright.getByRole("button", { name: "Networks", exact: true });
    await readyOne(networksButtonForHost);
    await clickOne(networksButtonForHost);
    const tunnelsLinkForHost = secureConsoleOwnedTaskTabV23.playwright.getByRole("link", { name: /tunnels/i });
    await readyOne(tunnelsLinkForHost);
    await clickOne(tunnelsLinkForHost);
    await readyOne(secureConsoleOwnedTaskTabV23.playwright.getByText(/create.*tunnel/i));
    const tunnelHostFilter = secureConsoleOwnedTaskTabV23.playwright.getByRole("textbox", { name: /search tunnels/i });
    [tunnelTargetHostCount] = await filteredZero(tunnelHostFilter, "ai-api-omniroute.mysw.me", ["ai-api-omniroute.mysw.me"], ["No tunnels found"]);
    tunnelFiltersComplete = true;

    const accessButton = secureConsoleOwnedTaskTabV23.playwright.getByRole("button", { name: "Access", exact: true });
    await readyOne(accessButton);
    await clickOne(accessButton);
    const applicationsLink = secureConsoleOwnedTaskTabV23.playwright.getByRole("link", { name: /applications/i });
    await readyOne(applicationsLink);
    await clickOne(applicationsLink);
    await readyOne(secureConsoleOwnedTaskTabV23.playwright.getByText(/add an application|add application/i));
    const accessFilter = secureConsoleOwnedTaskTabV23.playwright.getByRole("textbox", { name: /search applications/i });
    [accessTargetHostCount] = await filteredZero(accessFilter, "ai-api-omniroute.mysw.me", ["ai-api-omniroute.mysw.me"], ["No applications found"]);
    await navigate(zeroTrustUrl.href);
    const accessNameUrl = new URL(await secureConsoleOwnedTaskTabV23.url());
    const accessNamePath = /^\/([0-9a-f]{32})(?:\/home)?\/?$/.exec(accessNameUrl.pathname);
    if (accessNameUrl.hostname !== "one.dash.cloudflare.com" || accessNamePath === null || accessNamePath[1] !== accountSegment) throw new Error("AccessNameAccountBindingError");
    const accessButtonForName = secureConsoleOwnedTaskTabV23.playwright.getByRole("button", { name: "Access", exact: true });
    await readyOne(accessButtonForName);
    await clickOne(accessButtonForName);
    const applicationsLinkForName = secureConsoleOwnedTaskTabV23.playwright.getByRole("link", { name: /applications/i });
    await readyOne(applicationsLinkForName);
    await clickOne(applicationsLinkForName);
    await readyOne(secureConsoleOwnedTaskTabV23.playwright.getByText(/add an application|add application/i));
    const accessNameFilter = secureConsoleOwnedTaskTabV23.playwright.getByRole("textbox", { name: /search applications/i });
    [accessTargetNameCount] = await filteredZero(accessNameFilter, "OmniRoute team API", ["OmniRoute team API"], ["No applications found"]);
    accessFiltersComplete = true;

    await navigate("https://dash.cloudflare.com/profile/api-tokens");
    const tokenUrl = new URL(await tab.url());
    tokenNavigationExact = tokenUrl.href === "https://dash.cloudflare.com/profile/api-tokens";
    if (!tokenNavigationExact) throw new Error("FinalTokenNavigationError");
    const tokenFilter = tab.playwright.locator('input[placeholder*="search" i]:visible');
    await readyOne(tokenFilter);
    if (await tokenFilter.count() !== 1) throw new Error("FinalTokenFilterCountError");
    const untrustedTokenInventory = await tokenFilter.evaluate((input) => {
      const normalize = (value) => (value || "").replace(/\s+/g, " ").trim().toLowerCase();
      const actionSelector = 'button, a, [role="button"], [role="link"]';
      let depth = 1;
      let node = input.parentElement;
      let section = null;
      let sectionDepth = -1;
      while (node !== null && node !== document.body && depth <= 32) {
        if (section === null &&
            (node.tagName === "SECTION" || ["region", "group"].includes(node.getAttribute("role")))) {
          section = node;
          sectionDepth = depth;
        }
        node = node.parentElement;
        depth++;
      }
      const statuses = section === null ? [] : [...section.querySelectorAll('[role="status"]')];
      const rows = section === null ? [] : [...section.querySelectorAll("tbody tr")];
      const actions = section === null ? [] : [...section.querySelectorAll(actionSelector)];
      return {
        inputConnected: input.isConnected === true,
        inputVisible: input.getClientRects().length === 1,
        inputValueEmpty: input.value === "",
        sectionFound: section !== null,
        sectionDepth,
        pageTableCount: document.querySelectorAll("table").length,
        pageGridCount: document.querySelectorAll('[role="grid"]').length,
        pagePaginationCount: document.querySelectorAll('[aria-label="Pagination"], [aria-label="Next page"], [aria-label="Previous page"]').length,
        pageBusyCount: document.querySelectorAll('[aria-busy="true"], [role="progressbar"]').length,
        sectionTableCount: section === null ? -1 : section.querySelectorAll("table").length,
        sectionSearchCount: section === null ? -1 : section.querySelectorAll('input[placeholder*="search" i]').length,
        sectionStatusCount: statuses.length,
        sectionEmptyStatusCount: statuses.filter((item) => ["no api tokens found", "no tokens found", "no results"].includes(normalize(item.textContent))).length,
        sectionTbodyCount: section === null ? -1 : section.querySelectorAll("tbody").length,
        sectionRowCount: section === null ? -1 : rows.length,
        sectionVisibleRowCount: section === null ? -1 : rows.filter((row) => row.getClientRects().length > 0).length,
        sectionBusyCount: section === null ? -1 : section.querySelectorAll('[aria-busy="true"], [role="progressbar"]').length,
        sectionCreateActionableCount: section === null ? -1 : actions.filter((item) => {
          const text = normalize(item.textContent);
          return text === "create token" || text === "create api token" || text === "create";
        }).length,
      };
    });
    const tokenInventory = trustedProjection(
      untrustedTokenInventory,
      ["inputConnected", "inputVisible", "inputValueEmpty", "sectionFound"],
      [
        "sectionDepth", "pageTableCount", "pageGridCount", "pagePaginationCount",
        "pageBusyCount", "sectionTableCount", "sectionSearchCount",
        "sectionStatusCount", "sectionEmptyStatusCount", "sectionTbodyCount",
        "sectionRowCount", "sectionVisibleRowCount", "sectionBusyCount",
        "sectionCreateActionableCount",
      ],
    );
    if (tokenInventory === null) throw new Error("FinalTokenInventoryValidationError");
    const tokenSection = tokenFilter.locator("xpath=ancestor::section[1]");
    if (await tokenSection.count() !== 1) throw new Error("FinalTokenSectionCountError");
    const tokenEmptyStatus = tokenSection.getByRole("status").filter({
      hasText: /^(?:No API Tokens Found|No Tokens Found)$/i,
    });
    const tokenEmptyRow = tokenSection.getByRole("row").filter({
      hasText: /^(?:No API Tokens Found|No Tokens Found)$/i,
    });
    if (typeof tokenEmptyStatus?.or !== "function") {
      throw new Error("FinalTokenMarkerShapeError");
    }
    tokenEmptyMarkerCount = await tokenEmptyStatus.or(tokenEmptyRow).count();
    tokenVisibleCandidateRowCount = await tokenSection.locator("tbody tr").filter({
      hasNotText: /^(?:No API Tokens Found|No Tokens Found)$/i,
      visible: true,
    }).count();
    tokenCreateControlCount =
      await tab.playwright.getByRole("button", { name: "Create Token", exact: true }).count() +
      await tab.playwright.getByRole("link", { name: "Create Token", exact: true }).count();
    tokenNameCount = await tokenSection.locator("table tbody").getByText(
      "OmniRoute secure console R5 20260901",
      { exact: true },
    ).count();
    tokenRowCount = await tokenSection.getByRole("row").filter({
      hasText: "OmniRoute secure console R5 20260901",
    }).count();
    tokenInventoryComplete =
      tokenInventory.inputConnected === true &&
      tokenInventory.inputVisible === true &&
      tokenInventory.inputValueEmpty === true &&
      tokenInventory.sectionFound === true &&
      tokenInventory.sectionDepth === 3 &&
      tokenInventory.pageTableCount === 2 &&
      tokenInventory.pageGridCount === 0 &&
      tokenInventory.pagePaginationCount === 0 &&
      tokenInventory.pageBusyCount === 0 &&
      tokenInventory.sectionTableCount === 1 &&
      tokenInventory.sectionSearchCount === 1 &&
      tokenInventory.sectionStatusCount === 0 &&
      tokenInventory.sectionEmptyStatusCount === 0 &&
      tokenInventory.sectionTbodyCount === 1 &&
      tokenInventory.sectionRowCount === 5 &&
      tokenInventory.sectionVisibleRowCount === 5 &&
      tokenInventory.sectionBusyCount === 0 &&
      tokenInventory.sectionCreateActionableCount === 0 &&
      tokenEmptyMarkerCount === 0 &&
      tokenVisibleCandidateRowCount === 5;
    tokenSemanticSignature =
      tokenNavigationExact === true &&
      tokenInventoryComplete === true &&
      tokenCreateControlCount === 1 &&
      tokenNameCount === 0 &&
      tokenRowCount === 0;
    if (!tokenSemanticSignature || !dnsFilterComplete || !rateCompletenessProven ||
        !tunnelFiltersComplete || !accessFiltersComplete) {
      throw new Error("FinalTokenPageStateError");
    }
    if (counters.navigationAttempted !== 6 || counters.navigationFulfilled !== 6 ||
        counters.clickAttempted !== 13 || counters.clickFulfilled !== 13 ||
        counters.readinessAttempted !== 32 || counters.readinessFulfilled !== 32 ||
        counters.fillAttempted !== 10 || counters.fillFulfilled !== 10) {
      throw new Error("BrowserCounterError");
    }
    result = "EXACT_V23_CLOUDFLARE_PRESTART_READS_PASS";
  } catch (error) {
    errorClass = safeErrorClass(error);
  }

  if (result === "EXACT_V23_CLOUDFLARE_PRESTART_READS_PASS") {
    secureConsoleOwnedTaskTabV23 = tab;
    secureConsoleOwnedTaskTabV23Eligible = true;
    secureConsoleOwnedTaskTabV23State = "CLOUDFLARE_PRESTART_READS_PASS_V23";
    cleanupState = "SUCCESS_TAB_RETAINED";
    residueConverged = true;
  } else if (tab !== null && tab === secureConsoleOwnedTaskTabV23 &&
      typeof tab.close === "function") {
    secureConsoleOwnedTaskTabV23Eligible = false;
    secureConsoleOwnedTaskTabV23State = "CLOUDFLARE_PRESTART_READS_FAILED_CLOSING_V23";
    counters.closeAttempted++;
    try {
      await tab.close();
      counters.closeFulfilled++;
      secureConsoleOwnedTaskTabV23 = null;
      secureConsoleOwnedTaskTabV23State = "CLOUDFLARE_PRESTART_READS_FAILED_CLEAN_V23";
      cleanupState = "FAILURE_EXACT_TAB_CLOSED";
      residueConverged = true;
    } catch (closeError) {
      if (errorClass === "NONE") errorClass = safeErrorClass(closeError);
      secureConsoleOwnedTaskTabV23 = tab;
      secureConsoleOwnedTaskTabV23State = "CLOUDFLARE_PRESTART_READS_FAILED_TAB_RETAINED_V23";
      cleanupState = "FAILURE_EXACT_TAB_CLOSE_REJECTED";
      residueConverged = false;
    }
  } else {
    secureConsoleOwnedTaskTabV23Eligible = false;
    secureConsoleOwnedTaskTabV23State = "CLOUDFLARE_PRESTART_READS_FAILED_RESIDUE_UNPROVEN_V23";
    cleanupState = "FAILURE_RESIDUE_UNPROVEN";
    residueConverged = false;
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
    closeAttempted: counters.closeAttempted,
    closeFulfilled: counters.closeFulfilled,
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
    tokenSemanticSignature,
    tokenCreateControlCount,
    tokenNameCount,
    tokenRowCount,
    tokenEmptyMarkerCount,
    tokenVisibleCandidateRowCount,
    tokenInventoryComplete,
    retainedExactHandle: secureConsoleOwnedTaskTabV23 !== null,
    eligible: secureConsoleOwnedTaskTabV23Eligible,
    state: secureConsoleOwnedTaskTabV23State,
    cleanupState,
    residueConverged,
    consumed: secureConsoleCloudflareReadsV23Consumed,
    writeAttempted: counters.writeAttempted,
    errorClass,
  });
})();
```

## Exact acceptance and cleanup

PASS requires: declarations/precondition/account binding true; navigation
`6/6`; menu clicks `13/13`, each after exact count one; native readiness
`32/32`; page-local search fills `10/10` on five credential-free inventory
filters only; DNS target `0`; rate rows/target description/target host
`1/0/0` with completeness true; Tunnel name/host `0/0`; Access host/name
`0/0`; final token navigation and direct inventory true; Create count `1`;
target name/row `0/0`; empty marker/candidate rows `0/5`; error
`NONE`; consumed true; exact handle retained/eligible in
`CLOUDFLARE_PRESTART_READS_PASS_V23`; close `0/0`; cleanup
`SUCCESS_TAB_RETAINED`; residue converged true; and completed tool output.

Any failure spends the prestart gate. When the exact retained handle was
captured, the contract makes one bounded exact-handle close attempt and clears
the persistent binding only after fulfilled close. Close rejection retains only
that exact handle ineligible. No retry, fallback, continuation, reinterpretation,
manual integration, verdict relaxation, or alternate browser path is allowed.

Exact PASS authorizes only the separately reviewed credential-free clipboard
clear/proxy/preparation/owner/form path. It does not authorize the final Create,
native Copy, or native masked Paste. Their combined manual confirmation remains
mandatory. The later exact-row deletion confirmation also remains separate and
mandatory.

Independent Sol High review must verify direct bytes/syntax, V23 live PASS
predecessor, exact retained binding, one-shot-before-await state, navigation and
locator target safety, completeness of every inventory read, fixed-key
cross-realm output, call cardinality, failure cleanup, secrets, no provider
mutation, no retry, and both manual confirmation boundaries.

`authorizes_live_execution=false`
