let secureConsoleOwnedTaskTabV50 = null;
let secureConsoleOwnedTaskTabV50Eligible = false;
let secureConsoleOwnedTaskTabV50State = "UNADOPTED";
let secureConsoleOwnedTaskTabV50PreCreateDetachConsumed = false;
let secureConsoleOwnedTaskTabV50PostNativeDetachConsumed = false;
let secureConsoleCloudflareReadsV50Consumed = false;
let secureConsoleV50Consumed = false;
await (async () => {
  let secureConsoleV50AttachmentEvidence = null;
  let secureConsoleV50TerminalOutputFailure = null;
  let secureConsoleSetupBrowserRuntimeV50Attachment = null;
  let secureConsoleAgentV50Attachment = null;
  let secureConsoleChromeV50Attachment = null;
  let secureConsoleOwnedTaskTabV50Attachment = null;
  let secureConsoleOwnedTaskTabV50AttachmentEligible = false;
  let secureConsoleV50AttachmentState = "UNCREATED";
  await (async () => {
    const gateWasFresh = secureConsoleV50Consumed === false;
    secureConsoleV50Consumed = true;
    const predecessorDeclarationsAbsent =
      typeof secureConsoleAgentV35 === "undefined" &&
      typeof secureConsoleAgentV36 === "undefined" &&
      typeof secureConsoleAgentV37 === "undefined" &&
      typeof secureConsoleAgentV38 === "undefined" &&
      typeof secureConsoleAgentV39 === "undefined" &&
      typeof secureConsoleAgentV40 === "undefined" &&
      typeof secureConsoleAgentV41 === "undefined" &&
      typeof secureConsoleChromeV35 === "undefined" &&
      typeof secureConsoleChromeV36 === "undefined" &&
      typeof secureConsoleChromeV37 === "undefined" &&
      typeof secureConsoleChromeV38 === "undefined" &&
      typeof secureConsoleChromeV39 === "undefined" &&
      typeof secureConsoleChromeV40 === "undefined" &&
      typeof secureConsoleChromeV41 === "undefined" &&
      typeof secureConsoleCloudflareReadsV42Consumed === "undefined" &&
      typeof secureConsoleOwnedTaskTabV35 === "undefined" &&
      typeof secureConsoleOwnedTaskTabV35Eligible === "undefined" &&
      typeof secureConsoleOwnedTaskTabV35State === "undefined" &&
      typeof secureConsoleOwnedTaskTabV36 === "undefined" &&
      typeof secureConsoleOwnedTaskTabV36Eligible === "undefined" &&
      typeof secureConsoleOwnedTaskTabV37 === "undefined" &&
      typeof secureConsoleOwnedTaskTabV37Eligible === "undefined" &&
      typeof secureConsoleOwnedTaskTabV38 === "undefined" &&
      typeof secureConsoleOwnedTaskTabV38Eligible === "undefined" &&
      typeof secureConsoleOwnedTaskTabV39 === "undefined" &&
      typeof secureConsoleOwnedTaskTabV39Eligible === "undefined" &&
      typeof secureConsoleOwnedTaskTabV40 === "undefined" &&
      typeof secureConsoleOwnedTaskTabV40Eligible === "undefined" &&
      typeof secureConsoleOwnedTaskTabV41 === "undefined" &&
      typeof secureConsoleOwnedTaskTabV41Eligible === "undefined" &&
      typeof secureConsoleOwnedTaskTabV42 === "undefined" &&
      typeof secureConsoleOwnedTaskTabV42Eligible === "undefined" &&
      typeof secureConsoleOwnedTaskTabV42PostNativeDetachConsumed === "undefined" &&
      typeof secureConsoleOwnedTaskTabV42PreCreateDetachConsumed === "undefined" &&
      typeof secureConsoleOwnedTaskTabV42State === "undefined" &&
      typeof secureConsoleSetupBrowserRuntimeV35 === "undefined" &&
      typeof secureConsoleSetupBrowserRuntimeV36 === "undefined" &&
      typeof secureConsoleSetupBrowserRuntimeV37 === "undefined" &&
      typeof secureConsoleSetupBrowserRuntimeV38 === "undefined" &&
      typeof secureConsoleSetupBrowserRuntimeV39 === "undefined" &&
      typeof secureConsoleSetupBrowserRuntimeV40 === "undefined" &&
      typeof secureConsoleSetupBrowserRuntimeV41 === "undefined" &&
      typeof secureConsoleV35AdoptionConsumed === "undefined" &&
      typeof secureConsoleV35AttachmentConsumed === "undefined" &&
      typeof secureConsoleV35AttachmentExact === "undefined" &&
      typeof secureConsoleV35AttachmentState === "undefined" &&
      typeof secureConsoleV36Consumed === "undefined" &&
      typeof secureConsoleV36State === "undefined" &&
      typeof secureConsoleV37Consumed === "undefined" &&
      typeof secureConsoleV37State === "undefined" &&
      typeof secureConsoleV38Consumed === "undefined" &&
      typeof secureConsoleV38State === "undefined" &&
      typeof secureConsoleV39Consumed === "undefined" &&
      typeof secureConsoleV39State === "undefined" &&
      typeof secureConsoleV40Consumed === "undefined" &&
      typeof secureConsoleV40State === "undefined" &&
      typeof secureConsoleV41Consumed === "undefined" &&
      typeof secureConsoleV41State === "undefined" &&
      typeof secureConsoleV42Consumed === "undefined" &&
      typeof secureConsoleOwnedTaskTabV43 === "undefined" &&
      typeof secureConsoleOwnedTaskTabV43Eligible === "undefined" &&
      typeof secureConsoleOwnedTaskTabV43State === "undefined" &&
      typeof secureConsoleOwnedTaskTabV43PreCreateDetachConsumed === "undefined" &&
      typeof secureConsoleOwnedTaskTabV43PostNativeDetachConsumed === "undefined" &&
      typeof secureConsoleCloudflareReadsV43Consumed === "undefined" &&
      typeof secureConsoleV43Consumed === "undefined" &&
      typeof secureConsoleOwnedTaskTabV44 === "undefined" &&
      typeof secureConsoleOwnedTaskTabV44Eligible === "undefined" &&
      typeof secureConsoleOwnedTaskTabV44State === "undefined" &&
      typeof secureConsoleOwnedTaskTabV44PreCreateDetachConsumed === "undefined" &&
      typeof secureConsoleOwnedTaskTabV44PostNativeDetachConsumed === "undefined" &&
      typeof secureConsoleCloudflareReadsV44Consumed === "undefined" &&
      typeof secureConsoleV44Consumed === "undefined" &&
      typeof secureConsoleSetupBrowserRuntimeV45 === "undefined" &&
      typeof secureConsoleAgentV45 === "undefined" &&
      typeof secureConsoleChromeV45 === "undefined" &&
      typeof secureConsoleOwnedTaskTabV45 === "undefined" &&
      typeof secureConsoleOwnedTaskTabV45Eligible === "undefined" &&
      typeof secureConsoleV45Consumed === "undefined" &&
      typeof secureConsoleV45State === "undefined" &&
      typeof secureConsoleOwnedTaskTabV46 === "undefined" &&
      typeof secureConsoleOwnedTaskTabV46Eligible === "undefined" &&
      typeof secureConsoleOwnedTaskTabV46State === "undefined" &&
      typeof secureConsoleOwnedTaskTabV46PreCreateDetachConsumed === "undefined" &&
      typeof secureConsoleOwnedTaskTabV46PostNativeDetachConsumed === "undefined" &&
      typeof secureConsoleCloudflareReadsV46Consumed === "undefined" &&
      typeof secureConsoleV46Consumed === "undefined" &&
      typeof secureConsoleOwnedTaskTabV47 === "undefined" &&
      typeof secureConsoleOwnedTaskTabV47Eligible === "undefined" &&
      typeof secureConsoleOwnedTaskTabV47State === "undefined" &&
      typeof secureConsoleOwnedTaskTabV47PreCreateDetachConsumed === "undefined" &&
      typeof secureConsoleOwnedTaskTabV47PostNativeDetachConsumed === "undefined" &&
      typeof secureConsoleCloudflareReadsV47Consumed === "undefined" &&
      typeof secureConsoleV47Consumed === "undefined" &&
      typeof secureConsoleV48Consumed === "undefined" &&
      typeof secureConsoleV48State === "undefined" &&
      typeof secureConsoleV48Result === "undefined" &&
      typeof secureConsoleOwnedTaskTabV49 === "undefined" &&
      typeof secureConsoleOwnedTaskTabV49Eligible === "undefined" &&
      typeof secureConsoleOwnedTaskTabV49State === "undefined" &&
      typeof secureConsoleOwnedTaskTabV49PreCreateDetachConsumed === "undefined" &&
      typeof secureConsoleOwnedTaskTabV49PostNativeDetachConsumed === "undefined" &&
      typeof secureConsoleCloudflareReadsV49Consumed === "undefined" &&
      typeof secureConsoleV49Consumed === "undefined";
    const counters = {
      importAttempted: 0, importFulfilled: 0,
      setupAttempted: 0, setupFulfilled: 0,
      connectAttempted: 0, connectFulfilled: 0,
      documentationAttempted: 0, documentationFulfilled: 0,
      documentationWriteAttempted: 0, documentationWriteFulfilled: 0,
      nameAttempted: 0, nameFulfilled: 0,
      openTabsAttempted: 0, openTabsFulfilled: 0,
      claimAttempted: 0, claimFulfilled: 0,
      navigationAttempted: 0, navigationFulfilled: 0,
      waitAttempted: 0, waitFulfilled: 0,
      urlAttempted: 0, urlFulfilled: 0,
      snapshotAttempted: 0, snapshotFulfilled: 0,
      writeAttempted: 0,
    };
    let result = "V50Attachment_FRESH_CROSS_REALM_TASK_REACQUISITION_FAILED_STOP";
    let declarationShape = false;
    let moduleShape = false;
    let agentShape = false;
    let connectedShape = false;
    let documentationValidated = false;
    let documentationLength = -1;
    let sessionNamed = false;
    let offeredCount = -1;
    let listingValidated = false;
    let uniqueUrlSelected = false;
    let candidateValidated = false;
    let candidateUrlPresent = false;
    let candidateUrlExact = false;
    let controllerOwnership = false;
    let tabShape = false;
    let homeUrlValidated = false;
    let snapshotValidated = false;
    let semanticComplete = false;
    let continuationBindingsRetained = false;
    let failureCleanupComplete = false;
    let snapshot = null;
    let adopted = null;
    let errorClass = "NONE";
    // BEGIN_V50Attachment_PURE_TRUSTED_LISTING
    const plainRecord = (value) => {
      if (typeof value !== "object" || value === null) return false;
      const prototype = Object.getPrototypeOf(value);
      return prototype === null ||
        (prototype !== null && Object.getPrototypeOf(prototype) === null);
    };
    const trustedListing = (value) => {
      if (!Array.isArray(value) ||
          Object.getOwnPropertySymbols(value).length !== 0) return null;
      const lengthDescriptor = Object.getOwnPropertyDescriptor(value, "length");
      if (!lengthDescriptor ||
          !Object.prototype.hasOwnProperty.call(lengthDescriptor, "value") ||
          lengthDescriptor.enumerable !== false ||
          !Number.isSafeInteger(lengthDescriptor.value) ||
          lengthDescriptor.value < 1 || lengthDescriptor.value > 1000) return null;
      const length = lengthDescriptor.value;
      const arrayNames = Object.getOwnPropertyNames(value);
      if (arrayNames.length !== length + 1 ||
          !arrayNames.includes("length")) return null;
      const expectedNames = new Set(["length"]);
      for (let index = 0; index < length; index++) {
        expectedNames.add(String(index));
      }
      if (arrayNames.some((name) => !expectedNames.has(name))) return null;
      const indexDescriptors = [];
      for (let index = 0; index < length; index++) {
        const descriptor =
          Object.getOwnPropertyDescriptor(value, String(index));
        if (!descriptor ||
            !Object.prototype.hasOwnProperty.call(descriptor, "value") ||
            descriptor.enumerable !== true) return null;
        indexDescriptors.push(descriptor);
      }
      if (indexDescriptors.length !== length) return null;
      const allowed = new Set([
        "id", "lastOpened", "providerTabId", "tabGroup", "title", "url",
      ]);
      let selected = null;
      for (const indexDescriptor of indexDescriptors) {
        const record = indexDescriptor.value;
        if (!plainRecord(record) ||
            Object.getOwnPropertySymbols(record).length !== 0) return null;
        const keys = Object.getOwnPropertyNames(record);
        if (!keys.includes("id") || keys.some((key) => !allowed.has(key))) {
          return null;
        }
        let validatedId = null;
        let validatedUrl = null;
        for (const key of keys) {
          const descriptor = Object.getOwnPropertyDescriptor(record, key);
          if (!descriptor ||
              !Object.prototype.hasOwnProperty.call(descriptor, "value") ||
              descriptor.enumerable !== true) return null;
          const limit = key === "url" ? 16384 : key === "title" ? 4096 : 512;
          if (typeof descriptor.value !== "string" ||
              descriptor.value.length === 0 ||
              descriptor.value.length > limit ||
              /[\u0000-\u001f\u007f]/.test(descriptor.value)) return null;
          if (key === "id") validatedId = descriptor.value;
          if (key === "url") validatedUrl = descriptor.value;
        }
        if (validatedId === null) return null;
        if (validatedUrl ===
            "https://dash.cloudflare.com/profile/api-tokens") {
          if (selected !== null) return null;
          selected = { tab: record, id: validatedId };
        }
      }
      if (selected === null) return null;
      return {
        tab: selected.tab,
        id: selected.id,
        count: length,
        urlPresent: true,
        urlExact: true,
      };
    };
    // END_V50Attachment_PURE_TRUSTED_LISTING
    const trustedSnapshot = (value) => {
      if (!plainRecord(value)) return null;
      const expected = [
        "accountHomePath", "allAnchorCount", "busyCount",
        "exactZoneHrefCount", "hostExact",
      ];
      const keys = Object.keys(value).sort();
      if (keys.length !== expected.length ||
          keys.some((key, index) => key !== expected[index])) return null;
      if (typeof value.hostExact !== "boolean" ||
          typeof value.accountHomePath !== "boolean") return null;
      for (const key of ["exactZoneHrefCount", "allAnchorCount", "busyCount"]) {
        if (!Number.isSafeInteger(value[key]) || value[key] < 0 ||
            value[key] > 1000000) return null;
      }
      return {
        hostExact: value.hostExact,
        accountHomePath: value.accountHomePath,
        exactZoneHrefCount: value.exactZoneHrefCount,
        allAnchorCount: value.allAnchorCount,
        busyCount: value.busyCount,
      };
    };
    try {
      declarationShape =
        gateWasFresh === true &&
        predecessorDeclarationsAbsent === true &&
        secureConsoleOwnedTaskTabV50 === null &&
        secureConsoleOwnedTaskTabV50Eligible === false &&
        secureConsoleOwnedTaskTabV50State === "UNADOPTED" &&
        secureConsoleOwnedTaskTabV50PreCreateDetachConsumed === false &&
        secureConsoleOwnedTaskTabV50PostNativeDetachConsumed === false &&
        secureConsoleCloudflareReadsV50Consumed === false &&
        typeof secureConsoleV35AttachmentConsumed === "undefined" &&
        typeof secureConsoleV35AdoptionConsumed === "undefined" &&
        typeof secureConsoleV36Consumed === "undefined" &&
        typeof secureConsoleV37Consumed === "undefined" &&
        typeof secureConsoleV38Consumed === "undefined" &&
        typeof secureConsoleOwnedTaskTabV38 === "undefined" &&
        typeof secureConsoleV39Consumed === "undefined" &&
        typeof secureConsoleOwnedTaskTabV39 === "undefined" &&
        typeof secureConsoleV40Consumed === "undefined" &&
        typeof secureConsoleOwnedTaskTabV40 === "undefined" &&
        secureConsoleSetupBrowserRuntimeV50Attachment === null &&
        secureConsoleAgentV50Attachment === null && secureConsoleChromeV50Attachment === null &&
        secureConsoleOwnedTaskTabV50Attachment === null &&
        secureConsoleOwnedTaskTabV50AttachmentEligible === false &&
        secureConsoleV50AttachmentState === "UNCREATED";
      if (!declarationShape) throw new Error("FreshRealmDeclarationError");
      secureConsoleV50AttachmentState = "V50Attachment_CONSUMING";

      counters.importAttempted++;
      const imported = await import(
        "file:///C:/Users/chatc/.codex/plugins/cache/openai-bundled/chrome/26.831.21537/scripts/browser-client.mjs"
      );
      counters.importFulfilled++;
      moduleShape = typeof imported === "object" && imported !== null &&
        typeof imported.setupBrowserRuntime === "function";
      if (!moduleShape) throw new Error("FreshRuntimeModuleShapeError");
      secureConsoleSetupBrowserRuntimeV50Attachment = imported.setupBrowserRuntime;

      counters.setupAttempted++;
      secureConsoleAgentV50Attachment = await secureConsoleSetupBrowserRuntimeV50Attachment();
      counters.setupFulfilled++;
      agentShape = typeof secureConsoleAgentV50Attachment === "object" &&
        secureConsoleAgentV50Attachment !== null &&
        typeof secureConsoleAgentV50Attachment.browsers?.get === "function";
      if (!agentShape) throw new Error("FreshRuntimeAgentShapeError");

      counters.connectAttempted++;
      secureConsoleChromeV50Attachment =
        await secureConsoleAgentV50Attachment.browsers.get("chrome");
      counters.connectFulfilled++;
      connectedShape = typeof secureConsoleChromeV50Attachment === "object" &&
        secureConsoleChromeV50Attachment !== null &&
        typeof secureConsoleChromeV50Attachment.documentation === "function" &&
        typeof secureConsoleChromeV50Attachment.nameSession === "function" &&
        typeof secureConsoleChromeV50Attachment.user?.openTabs === "function" &&
        typeof secureConsoleChromeV50Attachment.user?.claimTab === "function";
      if (!connectedShape) throw new Error("FreshChromeShapeError");

      counters.documentationAttempted++;
      const documentation = await secureConsoleChromeV50Attachment.documentation();
      counters.documentationFulfilled++;
      documentationValidated =
        typeof documentation === "string" &&
        documentation.length >= 40000 && documentation.length <= 50000 &&
        documentation.includes("openTabs(): Promise<Array<BrowserUserTabInfo>>") &&
        documentation.includes(
          "claimTab(tab: string | BrowserUserTabInfo): Promise<Tab>",
        ) &&
        documentation.includes("id: string") &&
        documentation.includes("lastOpened?: string") &&
        documentation.includes("providerTabId?: string") &&
        documentation.includes("tabGroup?: string") &&
        documentation.includes("title?: string") &&
        documentation.includes("url?: string");
      documentationLength = documentationValidated ? documentation.length : -1;
      if (!documentationValidated) {
        throw new Error("CompleteDocumentationValidationError");
      }
      counters.documentationWriteAttempted++;
      try {
        await nodeRepl.write(documentation);
        counters.documentationWriteFulfilled++;
      } catch (terminalError) {
        secureConsoleV50TerminalOutputFailure = terminalError;
        throw new Error("V50DocumentationOutputError");
      }

      counters.nameAttempted++;
      await secureConsoleChromeV50Attachment.nameSession("🔐 OmniRoute secure console");
      counters.nameFulfilled++;
      sessionNamed = true;

      counters.openTabsAttempted++;
      const offered = await secureConsoleChromeV50Attachment.user.openTabs();
      counters.openTabsFulfilled++;
      const candidate = trustedListing(offered);
      listingValidated = candidate !== null;
      offeredCount = listingValidated ? candidate.count : -1;
      uniqueUrlSelected = listingValidated;
      candidateValidated = listingValidated;
      candidateUrlPresent = listingValidated && candidate.urlPresent;
      candidateUrlExact = listingValidated && candidate.urlExact;
      if (!candidateValidated) throw new Error("UniqueUrlTaskTabShapeError");

      counters.claimAttempted++;
      adopted = await secureConsoleChromeV50Attachment.user.claimTab(candidate.tab);
      counters.claimFulfilled++;
      controllerOwnership = typeof adopted === "object" && adopted !== null &&
        typeof adopted.id === "string" && adopted.id === candidate.id &&
        adopted.id.length > 0 && adopted.id.length <= 512 &&
        !/[\u0000-\u001f\u007f]/.test(adopted.id);
      tabShape = controllerOwnership && typeof adopted.goto === "function" &&
        typeof adopted.url === "function" &&
        typeof adopted.playwright?.waitForTimeout === "function" &&
        typeof adopted.playwright?.locator === "function";
      if (!tabShape) throw new Error("ClaimedTabOwnershipError");

      counters.navigationAttempted++;
      await adopted.goto("https://dash.cloudflare.com/");
      counters.navigationFulfilled++;
      counters.waitAttempted++;
      await adopted.playwright.waitForTimeout(20000);
      counters.waitFulfilled++;
      counters.urlAttempted++;
      const homeUrl = await adopted.url();
      counters.urlFulfilled++;
      const homeMatch =
        /^https:\/\/dash\.cloudflare\.com\/([0-9a-f]{32})\/home\/?$/.exec(
          homeUrl,
        );
      homeUrlValidated = homeMatch !== null;
      if (!homeUrlValidated) throw new Error("AccountHomeUrlError");
      const accountSegment = homeMatch[1];

      counters.snapshotAttempted++;
      const untrusted = await adopted.playwright.locator("body").evaluate(
        (body, segment) => {
          const anchors = [...body.querySelectorAll("a[href]")];
          const exactZoneHrefCount = anchors.filter((item) => {
            try {
              const url = new URL(item.getAttribute("href") || "", location.href);
              return url.protocol === "https:" &&
                url.hostname === "dash.cloudflare.com" &&
                url.port === "" && url.username === "" && url.password === "" &&
                new RegExp("^/" + segment + "/mysw\\.me/?$").test(url.pathname);
            } catch {
              return false;
            }
          }).length;
          return {
            hostExact: location.protocol === "https:" &&
              location.hostname === "dash.cloudflare.com" &&
              location.port === "",
            accountHomePath:
              new RegExp("^/" + segment + "/home/?$").test(location.pathname),
            exactZoneHrefCount,
            allAnchorCount: anchors.length,
            busyCount: body.querySelectorAll(
              '[aria-busy="true"], [role="progressbar"]',
            ).length,
          };
        },
        accountSegment,
      );
      counters.snapshotFulfilled++;
      snapshot = trustedSnapshot(untrusted);
      snapshotValidated = snapshot !== null;
      semanticComplete = snapshotValidated && snapshot.hostExact === true &&
        snapshot.accountHomePath === true && snapshot.exactZoneHrefCount === 1 &&
        snapshot.allAnchorCount > 0 && snapshot.busyCount === 0;
      if (!semanticComplete) {
        throw new Error("AccountHomeSemanticSignatureError");
      }

      const exactCounters =
        counters.importAttempted === 1 && counters.importFulfilled === 1 &&
        counters.setupAttempted === 1 && counters.setupFulfilled === 1 &&
        counters.connectAttempted === 1 && counters.connectFulfilled === 1 &&
        counters.documentationAttempted === 1 &&
        counters.documentationFulfilled === 1 &&
        counters.documentationWriteAttempted === 1 &&
        counters.documentationWriteFulfilled === 1 &&
        counters.nameAttempted === 1 && counters.nameFulfilled === 1 &&
        counters.openTabsAttempted === 1 && counters.openTabsFulfilled === 1 &&
        counters.claimAttempted === 1 && counters.claimFulfilled === 1 &&
        counters.navigationAttempted === 1 &&
        counters.navigationFulfilled === 1 && counters.waitAttempted === 1 &&
        counters.waitFulfilled === 1 && counters.urlAttempted === 1 &&
        counters.urlFulfilled === 1 && counters.snapshotAttempted === 1 &&
        counters.snapshotFulfilled === 1;
      if (!exactCounters) throw new Error("V50AttachmentCompletenessError");
      result = "EXACT_V50Attachment_CROSS_REALM_TASK_TAB_ACCOUNT_HOME_REACQUISITION_PASS";
    } catch {
      errorClass = "Error";
    }

    if (result ===
        "EXACT_V50Attachment_CROSS_REALM_TASK_TAB_ACCOUNT_HOME_REACQUISITION_PASS") {
      secureConsoleOwnedTaskTabV50Attachment = adopted;
      secureConsoleOwnedTaskTabV50AttachmentEligible = true;
      secureConsoleV50AttachmentState = "V50Attachment_ACCOUNT_HOME_READY_ELIGIBLE";
      continuationBindingsRetained =
        typeof secureConsoleSetupBrowserRuntimeV50Attachment === "function" &&
        secureConsoleAgentV50Attachment !== null && secureConsoleChromeV50Attachment !== null &&
        secureConsoleOwnedTaskTabV50Attachment !== null;
    } else {
      secureConsoleOwnedTaskTabV50Attachment = null;
      secureConsoleOwnedTaskTabV50AttachmentEligible = false;
      secureConsoleV50AttachmentState = "V50Attachment_REACQUISITION_OR_READINESS_FAILED";
      secureConsoleChromeV50Attachment = null;
      secureConsoleAgentV50Attachment = null;
      secureConsoleSetupBrowserRuntimeV50Attachment = null;
      failureCleanupComplete =
        secureConsoleSetupBrowserRuntimeV50Attachment === null &&
        secureConsoleAgentV50Attachment === null && secureConsoleChromeV50Attachment === null &&
        secureConsoleOwnedTaskTabV50Attachment === null &&
        secureConsoleOwnedTaskTabV50AttachmentEligible === false;
    }
    secureConsoleV50AttachmentEvidence = {
        result,
        declarationShape,
        moduleShape,
        agentShape,
        connectedShape,
        documentationValidated,
        documentationLength,
        sessionNamed,
        offeredCount,
        listingValidated,
        uniqueUrlSelected,
        candidateValidated,
        candidateUrlPresent,
        candidateUrlExact,
        controllerOwnership,
        tabShape,
        homeUrlValidated,
        snapshotValidated,
        semanticComplete,
        continuationBindingsRetained,
        failureCleanupComplete,
        snapshot,
        ...counters,
        errorClass,
        consumed: secureConsoleV50Consumed,
        bindingEligible: secureConsoleOwnedTaskTabV50AttachmentEligible,
        bindingNull: secureConsoleOwnedTaskTabV50Attachment === null,
        state: secureConsoleV50AttachmentState,
    };
  })();
  if (secureConsoleV50TerminalOutputFailure !== null) {
    const terminalOutputFailure = secureConsoleV50TerminalOutputFailure;
    secureConsoleV50TerminalOutputFailure = null;
    secureConsoleV50AttachmentEvidence = null;
    throw terminalOutputFailure;
  }
  await (async () => {
    const gateWasFresh = secureConsoleV50Consumed === true;
    const counters = {
      bindingAttempted: 0,
      bindingFulfilled: 0,
      navigationAttempted: 0,
      navigationFulfilled: 0,
      urlAttempted: 0,
      urlFulfilled: 0,
      readinessAttempted: 0,
      readinessFulfilled: 0,
      fillAttempted: 0,
      fillFulfilled: 0,
      createReadAttempted: 0,
      createReadFulfilled: 0,
      nameReadAttempted: 0,
      nameReadFulfilled: 0,
      rowReadAttempted: 0,
      rowReadFulfilled: 0,
      writeAttempted: 0,
    };
    let result = "V50_TOKEN_PAGE_SEMANTIC_READINESS_FAILED_STOP";
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
    let continuationBindingsRetained = false;
    let predecessorRuntimeCleared = false;
    let failureCleanupComplete = false;
    let adopted = null;
    try {
      declarationShape =
        gateWasFresh === true &&
        typeof secureConsoleV50Consumed === "boolean" &&
        typeof secureConsoleV50AttachmentState === "string" &&
        typeof secureConsoleOwnedTaskTabV50Attachment === "object" &&
        typeof secureConsoleOwnedTaskTabV50AttachmentEligible === "boolean" &&
        typeof secureConsoleSetupBrowserRuntimeV50Attachment === "function" &&
        typeof secureConsoleAgentV50Attachment === "object" &&
        secureConsoleAgentV50Attachment !== null &&
        typeof secureConsoleChromeV50Attachment === "object" &&
        secureConsoleChromeV50Attachment !== null &&
        secureConsoleOwnedTaskTabV50 === null &&
        secureConsoleOwnedTaskTabV50Eligible === false &&
        secureConsoleOwnedTaskTabV50State === "UNADOPTED" &&
        secureConsoleOwnedTaskTabV50PreCreateDetachConsumed === false &&
        secureConsoleOwnedTaskTabV50PostNativeDetachConsumed === false &&
        secureConsoleCloudflareReadsV50Consumed === false;
      if (!declarationShape) throw new Error("V50DeclarationShapeError");
      predecessorStateExact =
        secureConsoleV50Consumed === true &&
        secureConsoleV50AttachmentState === "V50Attachment_ACCOUNT_HOME_READY_ELIGIBLE" &&
        secureConsoleOwnedTaskTabV50Attachment !== null &&
        secureConsoleOwnedTaskTabV50AttachmentEligible === true;
      if (!predecessorStateExact) throw new Error("V50AttachmentPredecessorStateError");

      counters.bindingAttempted++;
      adopted = secureConsoleOwnedTaskTabV50Attachment;
      counters.bindingFulfilled++;
      controllerOwnership =
        typeof adopted === "object" && adopted !== null &&
        typeof adopted.id === "string" &&
        adopted.id.length > 0 && adopted.id.length <= 512 &&
        !/[\u0000-\u001f\u007f]/.test(adopted.id);
      tabShape =
        controllerOwnership &&
        typeof adopted.goto === "function" &&
        typeof adopted.url === "function" &&
        typeof adopted.playwright?.getByRole === "function" &&
        typeof adopted.playwright?.getByText === "function" &&
        typeof adopted.playwright?.locator === "function";
      if (!tabShape) throw new Error("V50AttachmentTabOwnershipError");

      counters.navigationAttempted++;
      await adopted.goto("https://dash.cloudflare.com/profile/api-tokens");
      counters.navigationFulfilled++;
      counters.urlAttempted++;
      const tokenUrl = new URL(await adopted.url());
      counters.urlFulfilled++;
      navigationTargetExact =
        tokenUrl.href === "https://dash.cloudflare.com/profile/api-tokens";
      if (!navigationTargetExact) throw new Error("TokenNavigationTargetError");

      const tokenFilter =
        adopted.playwright.getByRole("textbox", { name: /search api tokens/i });
      counters.readinessAttempted++;
      await tokenFilter.waitFor({ state: "visible", timeoutMs: 20000 });
      counters.readinessFulfilled++;
      if (await tokenFilter.count() !== 1) {
        throw new Error("TokenFilterCountError");
      }
      const tokenRegionId = await tokenFilter.getAttribute("aria-controls");
      if (typeof tokenRegionId !== "string" ||
          !/^[A-Za-z][A-Za-z0-9_-]{0,127}$/.test(tokenRegionId)) {
        throw new Error("TokenRegionBindingError");
      }
      const tokenResultsRoot = adopted.playwright.locator(`#${tokenRegionId}`);
      if (await tokenResultsRoot.count() !== 1) {
        throw new Error("TokenResultsRootCountError");
      }
      const tokenPaginator =
        tokenResultsRoot.locator('[aria-label="Pagination"]');
      if (await tokenPaginator.count() !== 1) {
        throw new Error("TokenPaginatorCountError");
      }
      counters.readinessAttempted++;
      await tokenPaginator.waitFor({ state: "visible", timeoutMs: 20000 });
      counters.readinessFulfilled++;
      tokenInitialFilterEmpty =
        await tokenFilter.evaluate((input) => input.value === "");
      if (!tokenInitialFilterEmpty) {
        throw new Error("TokenInitialFilterStateError");
      }
      const tokenBaseline = await tokenResultsRoot.evaluate((root) => {
        const pager = root.querySelector('[aria-label="Pagination"]');
        const match = /^(\d+)\s*[-–]\s*(\d+)\s+of\s+(\d+)$/.exec(
          (pager?.textContent || "").replace(/\s+/g, " ").trim(),
        );
        const rows = root.querySelectorAll("table tbody tr").length;
        const busy = root.matches('[aria-busy="true"]') ||
          root.querySelector('[aria-busy="true"]') !== null;
        const statuses = [...root.querySelectorAll('[role="status"]')].filter(
          (item) => /^(?:no api tokens found|no tokens found)$/i.test(
            (item.textContent || "").trim(),
          ),
        );
        const buttons = pager === null ? [] : [...pager.querySelectorAll("button")];
        const next = buttons.filter(
          (item) => item.getAttribute("aria-label") === "Next page",
        );
        const previous = buttons.filter(
          (item) => item.getAttribute("aria-label") === "Previous page",
        );
        const disabled = (item) =>
          item.hasAttribute("disabled") ||
          item.getAttribute("aria-disabled") === "true";
        if (busy || match === null || next.length !== 1 ||
            previous.length !== 1) {
          return { terminalZero: false, completeNonempty: false };
        }
        const start = Number(match[1]);
        const end = Number(match[2]);
        const total = Number(match[3]);
        return {
          terminalZero:
            start === 0 && end === 0 && total === 0 && rows === 0 &&
            statuses.length === 1 && disabled(next[0]) &&
            disabled(previous[0]),
          completeNonempty:
            start === 1 && end === rows && total >= rows && rows > 0 &&
            statuses.length === 0 && disabled(previous[0]) &&
            disabled(next[0]) === (end >= total),
        };
      });
      if (!tokenBaseline.terminalZero && !tokenBaseline.completeNonempty) {
        throw new Error("TokenBaselineIncompleteError");
      }

      counters.fillAttempted++;
      await tokenFilter.fill("OmniRoute secure console R5 20260901");
      counters.fillFulfilled++;
      const tokenQueryEcho = tokenResultsRoot.getByText(
        "OmniRoute secure console R5 20260901",
        { exact: true },
      );
      counters.readinessAttempted++;
      await tokenQueryEcho.waitFor({ state: "visible", timeoutMs: 20000 });
      counters.readinessFulfilled++;
      tokenQueryEchoCount = await tokenQueryEcho.count();
      if (tokenQueryEchoCount !== 1) {
        throw new Error("TokenQueryEchoCountError");
      }
      const tokenEmptyStatus = tokenResultsRoot.getByRole("status").filter({
        hasText: /^(?:no api tokens found|no tokens found)$/i,
      });
      counters.readinessAttempted++;
      await tokenEmptyStatus.waitFor({ state: "visible", timeoutMs: 20000 });
      counters.readinessFulfilled++;
      if (await tokenEmptyStatus.count() !== 1) {
        throw new Error("TokenEmptyStatusCountError");
      }
      const tokenValueExact = await tokenFilter.evaluate(
        (input) => input.value === "OmniRoute secure console R5 20260901",
      );
      const tokenTerminal = await tokenResultsRoot.evaluate((root) => {
        const pager = root.querySelector('[aria-label="Pagination"]');
        const match = /^(\d+)\s*[-–]\s*(\d+)\s+of\s+(\d+)$/.exec(
          (pager?.textContent || "").replace(/\s+/g, " ").trim(),
        );
        const rows = root.querySelectorAll("table tbody tr").length;
        const statuses = [...root.querySelectorAll('[role="status"]')].filter(
          (item) => /^(?:no api tokens found|no tokens found)$/i.test(
            (item.textContent || "").trim(),
          ),
        );
        const buttons = pager === null ? [] : [...pager.querySelectorAll("button")];
        const next = buttons.filter(
          (item) => item.getAttribute("aria-label") === "Next page",
        );
        const previous = buttons.filter(
          (item) => item.getAttribute("aria-label") === "Previous page",
        );
        const disabled = (item) =>
          item.hasAttribute("disabled") ||
          item.getAttribute("aria-disabled") === "true";
        const busy = root.matches('[aria-busy="true"]') ||
          root.querySelector('[aria-busy="true"]') !== null;
        return !busy && match !== null &&
          Number(match[1]) === 0 && Number(match[2]) === 0 &&
          Number(match[3]) === 0 && rows === 0 && statuses.length === 1 &&
          next.length === 1 && previous.length === 1 &&
          disabled(next[0]) && disabled(previous[0]);
      });

      counters.createReadAttempted++;
      createControlCount =
        await adopted.playwright.getByRole(
          "button", { name: "Create Token", exact: true },
        ).count() +
        await adopted.playwright.getByRole(
          "link", { name: "Create Token", exact: true },
        ).count();
      counters.createReadFulfilled++;
      counters.nameReadAttempted++;
      tokenNameCount = await tokenResultsRoot.locator("table tbody").getByText(
        "OmniRoute secure console R5 20260901",
        { exact: true },
      ).count();
      counters.nameReadFulfilled++;
      counters.rowReadAttempted++;
      matchingRowCount = await tokenResultsRoot.getByRole("row").filter({
        hasText: "OmniRoute secure console R5 20260901",
      }).count();
      counters.rowReadFulfilled++;
      tokenFilterComplete =
        tokenInitialFilterEmpty && tokenQueryEchoCount === 1 &&
        tokenValueExact && tokenTerminal &&
        (tokenBaseline.terminalZero || tokenBaseline.completeNonempty);
      tokenSemanticSignature =
        navigationTargetExact && createControlCount === 1 &&
        tokenNameCount === 0 && matchingRowCount === 0 &&
        tokenFilterComplete;
      const exactCounters =
        counters.bindingAttempted === 1 && counters.bindingFulfilled === 1 &&
        counters.navigationAttempted === 1 &&
        counters.navigationFulfilled === 1 &&
        counters.urlAttempted === 1 && counters.urlFulfilled === 1 &&
        counters.readinessAttempted === 4 &&
        counters.readinessFulfilled === 4 &&
        counters.fillAttempted === 1 && counters.fillFulfilled === 1 &&
        counters.createReadAttempted === 1 &&
        counters.createReadFulfilled === 1 &&
        counters.nameReadAttempted === 1 &&
        counters.nameReadFulfilled === 1 &&
        counters.rowReadAttempted === 1 &&
        counters.rowReadFulfilled === 1;
      if (!tokenSemanticSignature || !exactCounters) {
        throw new Error("AuthenticatedTokenPageSemanticStateError");
      }
      result = "EXACT_V50_TOKEN_PAGE_SEMANTIC_READINESS_PASS";
    } catch {
      errorClass = "Error";
    }

    if (result === "EXACT_V50_TOKEN_PAGE_SEMANTIC_READINESS_PASS") {
      secureConsoleOwnedTaskTabV50 = adopted;
      secureConsoleOwnedTaskTabV50Eligible = true;
      secureConsoleOwnedTaskTabV50Attachment = null;
      secureConsoleOwnedTaskTabV50AttachmentEligible = false;
      secureConsoleV50AttachmentState = "V50Attachment_TRANSFERRED_TO_V50";
      secureConsoleChromeV50Attachment = null;
      secureConsoleAgentV50Attachment = null;
      secureConsoleSetupBrowserRuntimeV50Attachment = null;
      predecessorRuntimeCleared =
        secureConsoleChromeV50Attachment === null &&
        secureConsoleAgentV50Attachment === null &&
        secureConsoleSetupBrowserRuntimeV50Attachment === null;
      continuationBindingsRetained =
        secureConsoleOwnedTaskTabV50 !== null &&
        secureConsoleOwnedTaskTabV50Eligible === true &&
        secureConsoleOwnedTaskTabV50Attachment === null &&
        secureConsoleOwnedTaskTabV50AttachmentEligible === false &&
        predecessorRuntimeCleared === true;
      if (continuationBindingsRetained) {
        secureConsoleOwnedTaskTabV50State =
          "TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE";
      } else {
        result = "V50_TOKEN_PAGE_SEMANTIC_READINESS_FAILED_STOP";
        errorClass = "Error";
        secureConsoleOwnedTaskTabV50 = null;
        secureConsoleOwnedTaskTabV50Eligible = false;
        secureConsoleOwnedTaskTabV50State =
          "V50_TOKEN_PAGE_SEMANTIC_READINESS_FAILED";
        secureConsoleV50AttachmentState = "V50Attachment_DOWNSTREAM_FAILURE_DETACHED";
        failureCleanupComplete =
          secureConsoleOwnedTaskTabV50 === null &&
          secureConsoleOwnedTaskTabV50Eligible === false &&
          secureConsoleOwnedTaskTabV50Attachment === null &&
          secureConsoleOwnedTaskTabV50AttachmentEligible === false &&
          predecessorRuntimeCleared === true;
      }
    } else {
      secureConsoleOwnedTaskTabV50 = null;
      secureConsoleOwnedTaskTabV50Eligible = false;
      secureConsoleOwnedTaskTabV50State =
        "V50_TOKEN_PAGE_SEMANTIC_READINESS_FAILED";
      secureConsoleOwnedTaskTabV50Attachment = null;
      secureConsoleOwnedTaskTabV50AttachmentEligible = false;
      secureConsoleV50AttachmentState = "V50Attachment_DOWNSTREAM_FAILURE_DETACHED";
      secureConsoleChromeV50Attachment = null;
      secureConsoleAgentV50Attachment = null;
      secureConsoleSetupBrowserRuntimeV50Attachment = null;
      predecessorRuntimeCleared =
        secureConsoleChromeV50Attachment === null &&
        secureConsoleAgentV50Attachment === null &&
        secureConsoleSetupBrowserRuntimeV50Attachment === null;
      failureCleanupComplete =
        secureConsoleOwnedTaskTabV50 === null &&
        secureConsoleOwnedTaskTabV50Eligible === false &&
        secureConsoleOwnedTaskTabV50Attachment === null &&
        secureConsoleOwnedTaskTabV50AttachmentEligible === false &&
        predecessorRuntimeCleared === true;
    }

    counters.writeAttempted++;
    try {
      await nodeRepl.write({
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
        continuationBindingsRetained,
        predecessorRuntimeCleared,
        failureCleanupComplete,
        attachment: secureConsoleV50AttachmentEvidence,
        ...counters,
        errorClass,
        consumed: secureConsoleV50Consumed,
        bindingEligible: secureConsoleOwnedTaskTabV50Eligible,
        bindingNull: secureConsoleOwnedTaskTabV50 === null,
        state: secureConsoleOwnedTaskTabV50State,
        predecessorBindingNull: secureConsoleOwnedTaskTabV50Attachment === null,
        predecessorState: secureConsoleV50AttachmentState,
      });
      secureConsoleV50AttachmentEvidence = null;
      secureConsoleV50TerminalOutputFailure = null;
    } catch (terminalError) {
      secureConsoleOwnedTaskTabV50 = null;
      secureConsoleOwnedTaskTabV50Eligible = false;
      secureConsoleOwnedTaskTabV50State = "V50_FINAL_OUTPUT_FAILED_STOP";
      secureConsoleOwnedTaskTabV50Attachment = null;
      secureConsoleOwnedTaskTabV50AttachmentEligible = false;
      secureConsoleV50AttachmentState = "V50Attachment_DOWNSTREAM_OUTPUT_FAILURE_DETACHED";
      secureConsoleChromeV50Attachment = null;
      secureConsoleAgentV50Attachment = null;
      secureConsoleSetupBrowserRuntimeV50Attachment = null;
      secureConsoleV50AttachmentEvidence = null;
      secureConsoleV50TerminalOutputFailure = null;
      throw terminalError;
    }
  })();
})();
