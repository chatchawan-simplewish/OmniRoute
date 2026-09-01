# OmniRoute V17 explicit evaluator-timeout readiness replacement brief

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Purpose and consumed-gate boundary

V16 was consumed once and failed clean at incident commit
`eab7c64`: its terminal evaluator was attempted but did not fulfill, every
later query/Create/name/row read was skipped, the exact created tab closed once,
residue converged, and no provider mutation or secret action occurred. V16 is
permanently spent and is never retried, continued, reinterpreted, or invoked by
V17.

The installed pinned browser API exposes locator
`evaluate(pageFunction, arg?, options?)` with optional
`PlaywrightEvaluateOptions.timeoutMs`, defined as the maximum time for setup
and script execution. V16 allowed its page-local loop `20000 ms` but omitted
that transport option. The observed attempted/not-fulfilled stage is consistent
with the transport rejecting before the longer page-local deadline. V17 makes
only the minimum corrective change: the same evaluator receives
`{ timeoutMs: 25000 }`, leaving a `5000 ms` settlement margin. The outer
one-shot Node deadline remains `60000 ms`.

## Exact inherited boundary

V17 preserves every reviewed V16 semantic and security constraint:

- fixed public navigation target only:
  `https://dash.cloudflare.com/profile/api-tokens`;
- fixed non-secret filter value only:
  `OmniRoute secure console R5 20260901`;
- one fresh owned tab, one navigation, one filter fill, and no title read, tabs
  list, reconnect, alternate-tab selection, screenshot, clipboard operation,
  keyboard operation, Create/edit/delete click, provider mutation, retry, or
  fallback;
- exact V15-through-V4 consumed/null/ineligible predecessor chain plus the exact
  consumed-failed-clean V16 null/ineligible/no-detach/no-read tuple;
- the same exact pre-fill baseline, private section fingerprint, causal
  transition, `2000 ms` minimum elapsed interval, `1000 ms` scoped
  mutation/fingerprint quiet interval, three allowlisted terminal row shapes,
  exact visible query echo, single actionable `Create Token`, and zero exact
  token-name/matching-row results;
- fixed-key cross-realm trusted projections only, with no untrusted spread and
  no raw page text, row text, fingerprint, DOM, HTML, URL, title, attribute,
  screenshot, token, secret, or clipboard output;
- exact PASS retains only the exact V17-created handle for a separately
  committed and independently reviewed prestart read;
- every non-PASS consumes V17; an exact created handle closes once, close
  uncertainty retains it ineligible, and missing/rejected/malformed/uncertain
  results never claim clean residue; and
- the mandatory final Create/native Copy/native masked Paste confirmation and
  later separate exact-row deletion confirmation remain mandatory.

## Rejected alternatives

- Repeated controller-side evaluate calls are rejected because they add browser
  actions and weaken the single bounded terminal observation model.
- Shortening the page-local deadline or relaxing the causal/quiet proof is
  rejected because it could convert an incomplete filter transition into PASS.
- Reusing V16 is prohibited because V16 is consumed.

## One-shot V17 executable

The sole Sol High owner may run this exact cell once in the same persistent
Node session only after an independent Sol High PASS review, a
non-self-referential classification, a separate post-commit coordinator tuple,
and every fresh action-time pin pass. No review or classification alone
authorizes execution.

```javascript
let secureConsoleOwnedTaskTabV17 = null;
let secureConsoleOwnedTaskTabV17Eligible = false;
let secureConsoleOwnedTaskTabV17State = "UNCREATED";
let secureConsoleOwnedTaskTabV17PreCreateDetachConsumed = false;
let secureConsoleOwnedTaskTabV17PostNativeDetachConsumed = false;
let secureConsoleCloudflareReadsV17Consumed = false;
let secureConsoleV17ReadinessConsumed = false;
await (async () => {
  const gateWasFresh = secureConsoleV17ReadinessConsumed === false;
  secureConsoleV17ReadinessConsumed = true;
  const counters = {
    newAttempted: 0, newFulfilled: 0,
    navigationAttempted: 0, navigationFulfilled: 0,
    urlAttempted: 0, urlFulfilled: 0,
    waitAttempted: 0, waitFulfilled: 0,
    countAttempted: 0, countFulfilled: 0,
    scopeAttempted: 0, scopeFulfilled: 0,
    baselineAttempted: 0, baselineFulfilled: 0,
    fillAttempted: 0, fillFulfilled: 0,
    terminalAttempted: 0, terminalFulfilled: 0,
    queryAttempted: 0, queryFulfilled: 0,
    createAttempted: 0, createFulfilled: 0,
    nameAttempted: 0, nameFulfilled: 0,
    rowAttempted: 0, rowFulfilled: 0,
    closeAttempted: 0, closeFulfilled: 0,
    writeAttempted: 0,
  };
  const emptyBaseline = () => ({
    inputConnected: false, inputVisible: false, inputValueEmpty: false,
    sectionFound: false, sectionDepth: -1,
    pageTableCount: -1, pageGridCount: -1, pagePaginationCount: -1,
    pageBusyCount: -1, sectionTableCount: -1, sectionSearchCount: -1,
    sectionStatusCount: -1, sectionEmptyStatusCount: -1,
    sectionTbodyCount: -1, sectionRowCount: -1,
    sectionVisibleRowCount: -1, sectionBusyCount: -1,
    sectionCreateActionableCount: -1,
  });
  const emptyTerminal = () => ({
    terminalObserved: false,
    transitionObserved: false, minimumElapsedSatisfied: false,
    quietWindowSatisfied: false,
    inputConnected: false, inputVisible: false, inputValueExact: false,
    queryInputExactCount: -1, sectionFound: false, sectionDepth: -1,
    pageTableCount: -1, pageGridCount: -1, pagePaginationCount: -1,
    pageBusyCount: -1, sectionTableCount: -1, sectionSearchCount: -1,
    sectionStatusCount: -1, sectionEmptyStatusCount: -1,
    sectionTbodyCount: -1, sectionRowCount: -1,
    sectionVisibleRowCount: -1, sectionVisibleCandidateRowCount: -1,
    sectionEmptyRowCount: -1, sectionBusyCount: -1,
    matchingRowCount: -1,
  });
  const safeErrorClass = (error) => {
    const name = typeof error?.name === "string" ? error.name : "Error";
    return /^[A-Za-z][A-Za-z0-9_]{0,63}$/.test(name) ? name : "Error";
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
  const trustedProjection = (value, booleanKeys, integerKeys, wideIntegerKeys = []) => {
    const expectedKeys = [...booleanKeys, ...integerKeys, ...wideIntegerKeys];
    if (!exactKeys(value, expectedKeys)) return null;
    const projected = {};
    for (const key of booleanKeys) {
      const item = value[key];
      if (typeof item !== "boolean") return null;
      projected[key] = item;
    }
    for (const key of integerKeys) {
      const item = value[key];
      if (!Number.isSafeInteger(item) || item < -1 || item > 1000000) return null;
      projected[key] = item;
    }
    for (const key of wideIntegerKeys) {
      const item = value[key];
      if (!Number.isSafeInteger(item) || item < 0 || item > 0xffffffff) return null;
      projected[key] = item;
    }
    return projected;
  };
  let result = "PRECONDITION_FAIL";
  let declarationShape = false;
  let predecessorStateExact = false;
  let controllerOwnership = false;
  let tabShape = false;
  let createdHandleCaptured = false;
  let navigationTargetExact = false;
  let placeholderSearchCount = -1;
  let baselineValidated = false;
  let baselineSemanticExact = false;
  let baselineFingerprint = -1;
  let terminalValidated = false;
  let terminalSemanticExact = false;
  let tokenQueryEchoCount = -1;
  let createControlCount = -1;
  let tokenNameCount = -1;
  let matchingRowCount = -1;
  let filterComplete = false;
  let tokenSemanticSignature = false;
  let baseline = emptyBaseline();
  let terminal = emptyTerminal();
  let cleanupState = "NO_TAB_CREATED";
  let residueConverged = true;
  let errorClass = "NONE";
  let tab = null;
  try {
    declarationShape =
      typeof secureConsoleChromeV5 === "object" &&
      secureConsoleChromeV5 !== null &&
      typeof secureConsoleChromeV5.tabs?.new === "function" &&
      typeof secureConsoleV16ReadinessConsumed === "boolean" &&
      typeof secureConsoleV15StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV14StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV13StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV12StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV11StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV10StructuralDiagnosticConsumed === "boolean" &&
      typeof secureConsoleV9ReadinessConsumed === "boolean" &&
      typeof secureConsoleV17ReadinessConsumed === "boolean";
    if (!declarationShape) throw new Error("ReadinessDeclarationShapeError");
    predecessorStateExact =
      gateWasFresh === true &&
      secureConsoleV16ReadinessConsumed === true &&
      secureConsoleOwnedTaskTabV16 === null &&
      secureConsoleOwnedTaskTabV16Eligible === false &&
      secureConsoleOwnedTaskTabV16State === "V16_READINESS_FAILED_CLEAN" &&
      secureConsoleOwnedTaskTabV16PreCreateDetachConsumed === false &&
      secureConsoleOwnedTaskTabV16PostNativeDetachConsumed === false &&
      secureConsoleCloudflareReadsV16Consumed === false &&
      secureConsoleV15StructuralDiagnosticConsumed === true &&
      secureConsoleV15RetainedTab === null &&
      secureConsoleV14StructuralDiagnosticConsumed === true &&
      secureConsoleV14RetainedTab === null &&
      secureConsoleV13StructuralDiagnosticConsumed === true &&
      secureConsoleV13RetainedTab === null &&
      secureConsoleV12StructuralDiagnosticConsumed === true &&
      secureConsoleV12RetainedTab === null &&
      secureConsoleV11StructuralDiagnosticConsumed === true &&
      secureConsoleV11RetainedTab === null &&
      secureConsoleV10StructuralDiagnosticConsumed === true &&
      secureConsoleV10RetainedTab === null &&
      secureConsoleV9ReadinessConsumed === true &&
      secureConsoleV9RetainedTab === null &&
      secureConsoleV4AdoptionConsumed === true &&
      secureConsoleOwnedTaskTabV4 === null &&
      secureConsoleOwnedTaskTabV4Eligible === false &&
      secureConsoleOwnedTaskTabV4State === "V9_OWNED_TAB_READINESS_FAILED_CLEAN" &&
      secureConsoleOwnedTaskTabV4PreCreateDetachConsumed === false &&
      secureConsoleOwnedTaskTabV4PostNativeDetachConsumed === false &&
      secureConsoleCloudflareReadsV4Consumed === false &&
      secureConsoleOwnedTaskTabV17 === null &&
      secureConsoleOwnedTaskTabV17Eligible === false &&
      secureConsoleOwnedTaskTabV17State === "UNCREATED" &&
      secureConsoleOwnedTaskTabV17PreCreateDetachConsumed === false &&
      secureConsoleOwnedTaskTabV17PostNativeDetachConsumed === false &&
      secureConsoleCloudflareReadsV17Consumed === false;
    if (!predecessorStateExact) throw new Error("ReadinessPredecessorStateError");

    counters.newAttempted++;
    secureConsoleOwnedTaskTabV17 = tab = await secureConsoleChromeV5.tabs.new();
    counters.newFulfilled++;
    createdHandleCaptured = typeof tab === "object" && tab !== null;
    if (!createdHandleCaptured) throw new Error("ReadinessCreatedHandleError");
    controllerOwnership = secureConsoleOwnedTaskTabV17 === tab;
    tabShape =
      controllerOwnership &&
      typeof tab.goto === "function" &&
      typeof tab.url === "function" &&
      typeof tab.close === "function" &&
      typeof tab.playwright?.locator === "function" &&
      typeof tab.playwright?.getByRole === "function";
    if (!tabShape) throw new Error("ReadinessTabShapeError");

    counters.navigationAttempted++;
    await tab.goto("https://dash.cloudflare.com/profile/api-tokens");
    counters.navigationFulfilled++;
    counters.urlAttempted++;
    const tokenUrl = new URL(await tab.url());
    counters.urlFulfilled++;
    navigationTargetExact = tokenUrl.href === "https://dash.cloudflare.com/profile/api-tokens";
    if (!navigationTargetExact) throw new Error("ReadinessNavigationTargetError");

    const tokenFilter = tab.playwright.locator('input[placeholder*="search" i]:visible');
    if (typeof tokenFilter?.waitFor !== "function" ||
        typeof tokenFilter?.count !== "function" ||
        typeof tokenFilter?.evaluate !== "function" ||
        typeof tokenFilter?.fill !== "function" ||
        typeof tokenFilter?.locator !== "function") {
      throw new Error("ReadinessFilterShapeError");
    }
    counters.waitAttempted++;
    await tokenFilter.waitFor({ state: "visible", timeoutMs: 10000 });
    counters.waitFulfilled++;
    counters.countAttempted++;
    placeholderSearchCount = await tokenFilter.count();
    counters.countFulfilled++;
    if (placeholderSearchCount !== 1) throw new Error("ReadinessFilterCountError");
    const tokenSection = tokenFilter.locator("xpath=ancestor::section[1]");
    if (typeof tokenSection?.count !== "function" ||
        typeof tokenSection?.locator !== "function" ||
        typeof tokenSection?.getByText !== "function" ||
        typeof tokenSection?.getByRole !== "function") {
      throw new Error("ReadinessSectionShapeError");
    }
    counters.scopeAttempted++;
    const tokenSectionCount = await tokenSection.count();
    counters.scopeFulfilled++;
    if (tokenSectionCount !== 1) throw new Error("ReadinessSectionCountError");

    counters.baselineAttempted++;
    const untrustedBaseline = await tokenFilter.evaluate((input) => {
      const normalize = (value) => (value || "").replace(/\s+/g, " ").trim().toLowerCase();
      const statusText = new Set(["no api tokens found", "no tokens found", "no results"]);
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
      const fingerprintSource = [
        ...rows.map((row) => `${row.getClientRects().length > 0 ? 1 : 0}:${normalize(row.textContent)}`),
        ...statuses.map((item) => `s:${item.getClientRects().length > 0 ? 1 : 0}:${normalize(item.textContent)}`),
      ].join("\u001f");
      let sectionFingerprint = 2166136261;
      for (let index = 0; index < fingerprintSource.length; index++) {
        sectionFingerprint ^= fingerprintSource.charCodeAt(index);
        sectionFingerprint = Math.imul(sectionFingerprint, 16777619) >>> 0;
      }
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
        sectionEmptyStatusCount: statuses.filter((item) => statusText.has(normalize(item.textContent))).length,
        sectionTbodyCount: section === null ? -1 : section.querySelectorAll("tbody").length,
        sectionRowCount: section === null ? -1 : rows.length,
        sectionVisibleRowCount: section === null ? -1 : rows.filter((row) => row.getClientRects().length > 0).length,
        sectionBusyCount: section === null ? -1 : section.querySelectorAll('[aria-busy="true"], [role="progressbar"]').length,
        sectionCreateActionableCount: section === null ? -1 : actions.filter((item) => {
          const text = normalize(item.textContent);
          return text === "create token" || text === "create api token" || text === "create";
        }).length,
        sectionFingerprint,
      };
    });
    counters.baselineFulfilled++;
    const baselineBooleanKeys = [
      "inputConnected", "inputVisible", "inputValueEmpty", "sectionFound",
    ];
    const baselineIntegerKeys = [
      "sectionDepth", "pageTableCount", "pageGridCount", "pagePaginationCount",
      "pageBusyCount", "sectionTableCount", "sectionSearchCount",
      "sectionStatusCount", "sectionEmptyStatusCount", "sectionTbodyCount",
      "sectionRowCount", "sectionVisibleRowCount", "sectionBusyCount",
      "sectionCreateActionableCount",
    ];
    const baselineExpectedKeys = [...baselineBooleanKeys, ...baselineIntegerKeys];
    const trustedBaseline = trustedProjection(
      untrustedBaseline,
      baselineBooleanKeys,
      baselineIntegerKeys,
      ["sectionFingerprint"],
    );
    baselineValidated = trustedBaseline !== null;
    if (!baselineValidated) throw new Error("ReadinessBaselineValidationError");
    baselineFingerprint = trustedBaseline.sectionFingerprint;
    baseline = Object.fromEntries(
      baselineExpectedKeys.map((key) => [key, trustedBaseline[key]]),
    );
    baselineSemanticExact =
      baseline.inputConnected === true &&
      baseline.inputVisible === true &&
      baseline.inputValueEmpty === true &&
      baseline.sectionFound === true &&
      baseline.sectionDepth === 3 &&
      baseline.pageTableCount === 2 &&
      baseline.pageGridCount === 0 &&
      baseline.pagePaginationCount === 0 &&
      baseline.pageBusyCount === 0 &&
      baseline.sectionTableCount === 1 &&
      baseline.sectionSearchCount === 1 &&
      baseline.sectionStatusCount === 0 &&
      baseline.sectionEmptyStatusCount === 0 &&
      baseline.sectionTbodyCount === 1 &&
      baseline.sectionRowCount === 5 &&
      baseline.sectionVisibleRowCount === 5 &&
      baseline.sectionBusyCount === 0 &&
      baseline.sectionCreateActionableCount === 0;
    if (!baselineSemanticExact) throw new Error("ReadinessBaselineSemanticError");

    counters.fillAttempted++;
    await tokenFilter.fill("OmniRoute secure console R5 20260901");
    counters.fillFulfilled++;

    counters.terminalAttempted++;
    const untrustedTerminal = await tokenFilter.evaluate(async (input, prefillFingerprint) => {
      const target = "omniroute secure console r5 20260901";
      const normalize = (value) => (value || "").replace(/\s+/g, " ").trim().toLowerCase();
      const statusText = new Set(["no api tokens found", "no tokens found", "no results"]);
      const snapshot = () => {
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
        const rows = section === null ? [] : [...section.querySelectorAll("tbody tr")];
        const statuses = section === null ? [] : [...section.querySelectorAll('[role="status"]')];
        const visibleRows = rows.filter((row) => row.getClientRects().length > 0);
        const emptyRows = rows.filter((row) => statusText.has(normalize(row.textContent)));
        const visibleCandidateRows = visibleRows.filter((row) => !statusText.has(normalize(row.textContent)));
        const fingerprintSource = [
          ...rows.map((row) => `${row.getClientRects().length > 0 ? 1 : 0}:${normalize(row.textContent)}`),
          ...statuses.map((item) => `s:${item.getClientRects().length > 0 ? 1 : 0}:${normalize(item.textContent)}`),
        ].join("\u001f");
        let fingerprint = 2166136261;
        for (let index = 0; index < fingerprintSource.length; index++) {
          fingerprint ^= fingerprintSource.charCodeAt(index);
          fingerprint = Math.imul(fingerprint, 16777619) >>> 0;
        }
        return { section, fingerprint, value: {
          terminalObserved: false, transitionObserved: false,
          minimumElapsedSatisfied: false, quietWindowSatisfied: false,
          inputConnected: input.isConnected === true,
          inputVisible: input.getClientRects().length === 1,
          inputValueExact: normalize(input.value) === target,
          queryInputExactCount: section === null ? -1 : [...section.querySelectorAll('input[placeholder*="search" i]')].filter((item) => normalize(item.value) === target).length,
          sectionFound: section !== null,
          sectionDepth,
          pageTableCount: document.querySelectorAll("table").length,
          pageGridCount: document.querySelectorAll('[role="grid"]').length,
          pagePaginationCount: document.querySelectorAll('[aria-label="Pagination"], [aria-label="Next page"], [aria-label="Previous page"]').length,
          pageBusyCount: document.querySelectorAll('[aria-busy="true"], [role="progressbar"]').length,
          sectionTableCount: section === null ? -1 : section.querySelectorAll("table").length,
          sectionSearchCount: section === null ? -1 : section.querySelectorAll('input[placeholder*="search" i]').length,
          sectionStatusCount: statuses.length,
          sectionEmptyStatusCount: statuses.filter((item) => statusText.has(normalize(item.textContent))).length,
          sectionTbodyCount: section === null ? -1 : section.querySelectorAll("tbody").length,
          sectionRowCount: section === null ? -1 : rows.length,
          sectionVisibleRowCount: section === null ? -1 : visibleRows.length,
          sectionVisibleCandidateRowCount: section === null ? -1 : visibleCandidateRows.length,
          sectionEmptyRowCount: section === null ? -1 : emptyRows.length,
          sectionBusyCount: section === null ? -1 : section.querySelectorAll('[aria-busy="true"], [role="progressbar"]').length,
          matchingRowCount: section === null ? -1 : rows.filter((row) => normalize(row.textContent).includes(target)).length,
        } };
      };
      const terminalShape = (value) => {
        const rowShape =
          value.sectionRowCount === 0 ||
          (value.sectionRowCount === 5 && value.sectionVisibleRowCount === 0) ||
          (value.sectionRowCount === 1 && value.sectionEmptyRowCount === 1 &&
            value.sectionVisibleCandidateRowCount === 0);
        return value.inputConnected === true &&
          value.inputVisible === true &&
          value.inputValueExact === true &&
          value.queryInputExactCount === 1 &&
          value.sectionFound === true &&
          value.sectionDepth === 3 &&
          value.pageTableCount === 2 &&
          value.pageGridCount === 0 &&
          value.pagePaginationCount === 0 &&
          value.pageBusyCount === 0 &&
          value.sectionTableCount === 1 &&
          value.sectionSearchCount === 1 &&
          value.sectionStatusCount === value.sectionEmptyStatusCount &&
          value.sectionStatusCount >= 0 && value.sectionStatusCount <= 1 &&
          value.sectionTbodyCount === 1 &&
          value.sectionVisibleCandidateRowCount === 0 &&
          value.sectionEmptyRowCount >= 0 && value.sectionEmptyRowCount <= 1 &&
          value.sectionBusyCount === 0 &&
          value.matchingRowCount === 0 &&
          rowShape;
      };
      const startedAt = performance.now();
      const deadline = startedAt + 20000;
      let observed = snapshot();
      let observedSection = observed.section;
      let lastFingerprint = observed.fingerprint;
      let lastFingerprintChangeAt = startedAt;
      let lastMutationAt = startedAt;
      let transitionObserved = observed.fingerprint !== prefillFingerprint;
      const observer = new MutationObserver(() => {
        lastMutationAt = performance.now();
      });
      const observeSection = (section) => {
        observer.disconnect();
        if (section !== null) {
          observer.observe(section, {
            attributes: true, childList: true, characterData: true, subtree: true,
          });
        }
      };
      observeSection(observedSection);
      try {
        while (true) {
          const now = performance.now();
          const minimumElapsedSatisfied = now - startedAt >= 2000;
          const quietWindowSatisfied =
            now - Math.max(lastFingerprintChangeAt, lastMutationAt) >= 1000;
          if (transitionObserved && terminalShape(observed.value) &&
              minimumElapsedSatisfied && quietWindowSatisfied) break;
          if (now >= deadline) break;
          await new Promise((resolve) => setTimeout(resolve, 100));
          const next = snapshot();
          const sampledAt = performance.now();
          if (next.fingerprint !== lastFingerprint) {
            lastFingerprint = next.fingerprint;
            lastFingerprintChangeAt = sampledAt;
          }
          if (next.section !== observedSection) {
            observedSection = next.section;
            lastMutationAt = sampledAt;
            observeSection(observedSection);
          }
          observed = next;
          transitionObserved ||= observed.fingerprint !== prefillFingerprint;
        }
        const finishedAt = performance.now();
        const minimumElapsedSatisfied = finishedAt - startedAt >= 2000;
        const quietWindowSatisfied =
          finishedAt - Math.max(lastFingerprintChangeAt, lastMutationAt) >= 1000;
        return {
          ...observed.value,
          terminalObserved:
            transitionObserved && terminalShape(observed.value) &&
            minimumElapsedSatisfied && quietWindowSatisfied,
          transitionObserved,
          minimumElapsedSatisfied,
          quietWindowSatisfied,
        };
      } finally {
        observer.disconnect();
      }
    }, baselineFingerprint, { timeoutMs: 25000 });
    counters.terminalFulfilled++;
    const terminalBooleanKeys = [
      "terminalObserved", "transitionObserved", "minimumElapsedSatisfied",
      "quietWindowSatisfied", "inputConnected", "inputVisible",
      "inputValueExact", "sectionFound",
    ];
    const terminalIntegerKeys = [
      "queryInputExactCount", "sectionDepth", "pageTableCount", "pageGridCount",
      "pagePaginationCount", "pageBusyCount", "sectionTableCount",
      "sectionSearchCount", "sectionStatusCount", "sectionEmptyStatusCount",
      "sectionTbodyCount", "sectionRowCount", "sectionVisibleRowCount",
      "sectionVisibleCandidateRowCount", "sectionEmptyRowCount",
      "sectionBusyCount", "matchingRowCount",
    ];
    const trustedTerminal = trustedProjection(
      untrustedTerminal,
      terminalBooleanKeys,
      terminalIntegerKeys,
    );
    terminalValidated = trustedTerminal !== null;
    if (!terminalValidated) throw new Error("ReadinessTerminalValidationError");
    terminal = trustedTerminal;
    const terminalRowShapeExact =
      terminal.sectionRowCount === 0 ||
      (terminal.sectionRowCount === 5 && terminal.sectionVisibleRowCount === 0) ||
      (terminal.sectionRowCount === 1 && terminal.sectionEmptyRowCount === 1 &&
        terminal.sectionVisibleCandidateRowCount === 0);
    terminalSemanticExact =
      terminal.terminalObserved === true &&
      terminal.transitionObserved === true &&
      terminal.minimumElapsedSatisfied === true &&
      terminal.quietWindowSatisfied === true &&
      terminal.inputConnected === true &&
      terminal.inputVisible === true &&
      terminal.inputValueExact === true &&
      terminal.queryInputExactCount === 1 &&
      terminal.sectionFound === true &&
      terminal.sectionDepth === 3 &&
      terminal.pageTableCount === 2 &&
      terminal.pageGridCount === 0 &&
      terminal.pagePaginationCount === 0 &&
      terminal.pageBusyCount === 0 &&
      terminal.sectionTableCount === 1 &&
      terminal.sectionSearchCount === 1 &&
      terminal.sectionStatusCount === terminal.sectionEmptyStatusCount &&
      terminal.sectionStatusCount >= 0 && terminal.sectionStatusCount <= 1 &&
      terminal.sectionTbodyCount === 1 &&
      terminal.sectionVisibleCandidateRowCount === 0 &&
      terminal.sectionEmptyRowCount >= 0 && terminal.sectionEmptyRowCount <= 1 &&
      terminal.sectionBusyCount === 0 &&
      terminal.matchingRowCount === 0 &&
      terminalRowShapeExact;
    if (!terminalSemanticExact) throw new Error("ReadinessTerminalSemanticError");

    const tokenQueryEcho = tokenSection.getByText("OmniRoute secure console R5 20260901", { exact: true });
    if (typeof tokenQueryEcho?.waitFor !== "function" ||
        typeof tokenQueryEcho?.count !== "function") {
      throw new Error("ReadinessQueryEchoShapeError");
    }
    counters.queryAttempted++;
    await tokenQueryEcho.waitFor({ state: "visible", timeoutMs: 10000 });
    tokenQueryEchoCount = await tokenQueryEcho.count();
    counters.queryFulfilled++;
    counters.createAttempted++;
    createControlCount =
      await tab.playwright.getByRole("button", { name: "Create Token", exact: true }).count() +
      await tab.playwright.getByRole("link", { name: "Create Token", exact: true }).count();
    counters.createFulfilled++;
    counters.nameAttempted++;
    tokenNameCount = await tokenSection.locator("table tbody").getByText("OmniRoute secure console R5 20260901", { exact: true }).count();
    counters.nameFulfilled++;
    counters.rowAttempted++;
    matchingRowCount = await tokenSection.getByRole("row").filter({ hasText: "OmniRoute secure console R5 20260901" }).count();
    counters.rowFulfilled++;
    filterComplete =
      baseline.inputValueEmpty === true &&
      terminal.inputValueExact === true &&
      terminal.queryInputExactCount === 1 &&
      terminal.transitionObserved === true &&
      terminal.minimumElapsedSatisfied === true &&
      terminal.quietWindowSatisfied === true &&
      tokenQueryEchoCount === 1 &&
      terminal.terminalObserved === true;
    tokenSemanticSignature =
      navigationTargetExact === true &&
      baselineSemanticExact === true &&
      terminalSemanticExact === true &&
      createControlCount === 1 &&
      tokenQueryEchoCount === 1 &&
      tokenNameCount === 0 &&
      matchingRowCount === 0 &&
      terminal.matchingRowCount === 0 &&
      filterComplete === true;
    if (!tokenSemanticSignature) throw new Error("AuthenticatedTokenPageSemanticStateError");
    result = "V17_TOKEN_PAGE_SEMANTIC_READINESS_BODY_COMPLETE";
  } catch (error) {
    errorClass = safeErrorClass(error);
  }

  if (result === "V17_TOKEN_PAGE_SEMANTIC_READINESS_BODY_COMPLETE") {
    secureConsoleOwnedTaskTabV17 = tab;
    secureConsoleOwnedTaskTabV17Eligible = true;
    secureConsoleOwnedTaskTabV17State = "TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE_V17";
    cleanupState = "SUCCESS_TAB_RETAINED";
    residueConverged = true;
    result = "EXACT_V17_TOKEN_PAGE_SEMANTIC_READINESS_PASS";
  } else if (counters.newAttempted === 1 && counters.newFulfilled === 0) {
    cleanupState = "NEW_REJECTED_RESIDUE_UNPROVEN";
    residueConverged = false;
    secureConsoleOwnedTaskTabV17State = "V17_READINESS_FAILED_RESIDUE_UNPROVEN";
  } else if (counters.newFulfilled === 1 && createdHandleCaptured === false) {
    cleanupState = "NEW_FULFILLED_WITHOUT_HANDLE_RESIDUE_UNPROVEN";
    residueConverged = false;
    secureConsoleOwnedTaskTabV17State = "V17_READINESS_FAILED_RESIDUE_UNPROVEN";
  } else if (tab !== null && tab !== undefined) {
    if (typeof tab.close !== "function") {
      cleanupState = "MALFORMED_EXACT_HANDLE_RETAINED";
      residueConverged = false;
      secureConsoleOwnedTaskTabV17 = tab;
      secureConsoleOwnedTaskTabV17Eligible = false;
      secureConsoleOwnedTaskTabV17State = "V17_READINESS_FAILED_TAB_RETAINED";
    } else {
      try {
        counters.closeAttempted++;
        await tab.close();
        counters.closeFulfilled++;
        tab = null;
        secureConsoleOwnedTaskTabV17 = null;
        secureConsoleOwnedTaskTabV17Eligible = false;
        secureConsoleOwnedTaskTabV17State = "V17_READINESS_FAILED_CLEAN";
        cleanupState = "CREATED_TAB_CLOSED";
        residueConverged = true;
      } catch (cleanupError) {
        cleanupState = "CLOSE_FAILED_EXACT_HANDLE_RETAINED";
        residueConverged = false;
        secureConsoleOwnedTaskTabV17 = tab;
        secureConsoleOwnedTaskTabV17Eligible = false;
        secureConsoleOwnedTaskTabV17State = "V17_READINESS_FAILED_TAB_RETAINED";
      }
    }
  } else {
    cleanupState = "NO_TAB_CREATED";
    residueConverged = true;
    secureConsoleOwnedTaskTabV17State = "V17_READINESS_FAILED_CLEAN";
  }

  counters.writeAttempted++;
  nodeRepl.write({
    result,
    declarationShape,
    predecessorStateExact,
    controllerOwnership,
    tabShape,
    createdHandleCaptured,
    navigationTargetExact,
    placeholderSearchCount,
    baselineValidated,
    baselineSemanticExact,
    terminalValidated,
    terminalSemanticExact,
    tokenQueryEchoCount,
    createControlCount,
    tokenNameCount,
    matchingRowCount,
    filterComplete,
    tokenSemanticSignature,
    baseline,
    terminal,
    cleanupState,
    residueConverged,
    retainedExactHandle: secureConsoleOwnedTaskTabV17 !== null,
    eligible: secureConsoleOwnedTaskTabV17Eligible,
    stateExact:
      secureConsoleOwnedTaskTabV17State === "TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE_V17",
    ...counters,
    errorClass,
    consumed: secureConsoleV17ReadinessConsumed,
    v16BindingNull: secureConsoleOwnedTaskTabV16 === null,
    v16BindingIneligible: secureConsoleOwnedTaskTabV16Eligible === false,
    v16BindingStateExact:
      secureConsoleOwnedTaskTabV16State === "V16_READINESS_FAILED_CLEAN",
    v4BindingNull: secureConsoleOwnedTaskTabV4 === null,
    v4BindingIneligible: secureConsoleOwnedTaskTabV4Eligible === false,
    v4BindingStateExact:
      secureConsoleOwnedTaskTabV4State === "V9_OWNED_TAB_READINESS_FAILED_CLEAN",
  });
})();
```

## Exact PASS and failure semantics

PASS requires `EXACT_V17_TOKEN_PAGE_SEMANTIC_READINESS_PASS`; every
declaration, predecessor, ownership, tab-shape, navigation, baseline,
causal-transition, minimum-elapsed, quiet-window, terminal, visible-query,
Create, name, row, cleanup, and fixed-output condition true; exact counter
cardinalities; retained exact V17 handle; V17 eligibility true; V17 consumed
true; exact failed-clean V16 tuple; and unchanged exact V4 tuple.

Any other result spends V17 permanently. It permits no retry, continuation,
fallback, provider action, manual integration, or verdict relaxation.

## Review and action-time gate

The independent Sol High reviewer must verify direct incident ancestry; exact
V16 predecessor binding semantics; the one added locator evaluator
`timeoutMs: 25000`; nested `20000 < 25000 < 60000` deadlines; unchanged
causal/stability/query-echo predicates; cross-realm fixed-key projection;
single-call cardinalities; exact success retention; every failure cleanup
branch; no secret sink; no provider mutation; and all inherited manual
confirmations.

Immediately before the sole call, revalidate exact committed brief/executable
bytes, independent review, classification and post-commit tuple, source
projection, empty index, exact 12-path dirty baseline, installed browser
runtime hashes, clean evidence worktree, zero temporary/process residue,
VM1205 safe state, public DNS absence, exact persistent V16-through-V4
bindings, and every V17 declaration still absent.

`authorizes_live_execution=false`

