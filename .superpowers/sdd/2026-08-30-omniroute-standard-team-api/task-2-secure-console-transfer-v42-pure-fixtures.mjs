import assert from "node:assert/strict";
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const directory = path.dirname(fileURLToPath(import.meta.url));
const briefPath = path.join(
  directory,
  "task-2-secure-console-transfer-v42-v41-binding-token-page-readiness-brief.md",
);
const brief = fs.readFileSync(briefPath, "utf8");
const cells = [...brief.matchAll(/~~~javascript\r?\n([\s\S]*?)\r?\n~~~/g)];
assert.equal(cells.length, 1);
const cell = cells[0][1].replace(/\r\n/g, "\n");
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;
new AsyncFunction(cell);

const occurrences = (needle) => cell.split(needle).length - 1;
assert.equal(occurrences("secureConsoleV42Consumed = true;"), 1);
assert.equal(occurrences(
  'adopted.goto("https://dash.cloudflare.com/profile/api-tokens")',
), 1);
assert.equal(occurrences(
  'await tokenFilter.fill("OmniRoute secure console R5 20260901")',
), 1);
assert.equal(occurrences('name: "Create Token", exact: true'), 2);
assert.equal(occurrences("secureConsoleOwnedTaskTabV41 = null;"), 3);
assert.equal(cell.includes("catch (error)"), false);
assert.match(cell, /  } catch \{\n    errorClass = "Error";\n  }/);
for (const forbidden of [
  ".click(", ".clipboard", ".selected(", ".list(", ".get(",
  ".claimTab(", ".openTabs(", ".close(", ".markHandoff(",
  ".markDeliverable(", "provider.", "credential",
]) {
  assert.equal(cell.includes(forbidden), false, forbidden);
}

const makeFixture = (failNavigation) => {
  const writes = [];
  let filterValue = "";
  let resultsEvaluateCalls = 0;
  const queryEcho = {
    async waitFor(options) {
      assert.deepEqual(options, { state: "visible", timeoutMs: 20000 });
    },
    async count() {
      return 1;
    },
  };
  const emptyStatus = {
    async waitFor(options) {
      assert.deepEqual(options, { state: "visible", timeoutMs: 20000 });
    },
    async count() {
      return 1;
    },
  };
  const paginator = {
    async count() {
      return 1;
    },
    async waitFor(options) {
      assert.deepEqual(options, { state: "visible", timeoutMs: 20000 });
    },
  };
  const resultsRoot = {
    async count() {
      return 1;
    },
    locator(selector) {
      if (selector === '[aria-label="Pagination"]') return paginator;
      assert.equal(selector, "table tbody");
      return {
        getByText(text, options) {
          assert.equal(text, "OmniRoute secure console R5 20260901");
          assert.deepEqual(options, { exact: true });
          return { async count() { return 0; } };
        },
      };
    },
    async evaluate() {
      resultsEvaluateCalls++;
      return resultsEvaluateCalls === 1
        ? { terminalZero: true, completeNonempty: false }
        : true;
    },
    getByText(text, options) {
      assert.equal(text, "OmniRoute secure console R5 20260901");
      assert.deepEqual(options, { exact: true });
      return queryEcho;
    },
    getByRole(role) {
      if (role === "status") {
        return {
          filter(options) {
            assert.ok(options.hasText instanceof RegExp);
            return emptyStatus;
          },
        };
      }
      assert.equal(role, "row");
      return {
        filter(options) {
          assert.deepEqual(options, {
            hasText: "OmniRoute secure console R5 20260901",
          });
          return { async count() { return 0; } };
        },
      };
    },
  };
  const tokenFilter = {
    async count() {
      return 1;
    },
    async getAttribute(name) {
      assert.equal(name, "aria-controls");
      return "token-results";
    },
    async evaluate() {
      return filterValue === "" ||
        filterValue === "OmniRoute secure console R5 20260901";
    },
    async fill(value) {
      assert.equal(value, "OmniRoute secure console R5 20260901");
      filterValue = value;
    },
  };
  const tab = {
    id: "task-tab",
    async goto(url) {
      assert.equal(url, "https://dash.cloudflare.com/profile/api-tokens");
      if (failNavigation) throw { name: "SecretLikeValue" };
    },
    async url() {
      return "https://dash.cloudflare.com/profile/api-tokens";
    },
    playwright: {
      getByRole(role, options) {
        if (role === "textbox") {
          assert.ok(options.name instanceof RegExp);
          return tokenFilter;
        }
        assert.ok(role === "button" || role === "link");
        assert.deepEqual(options, { name: "Create Token", exact: true });
        return { async count() { return role === "button" ? 1 : 0; } };
      },
      getByText() {
        throw new Error("top-level getByText must not be used");
      },
      locator(selector) {
        assert.equal(selector, "#token-results");
        return resultsRoot;
      },
    },
  };
  return { writes, tab };
};

const run = async (failNavigation) => {
  const fixture = makeFixture(failNavigation);
  globalThis.__v42Fixture = fixture;
  const prelude = `
let secureConsoleV41Consumed = true;
let secureConsoleV41State = "V41_ACCOUNT_HOME_READY_ELIGIBLE";
let secureConsoleOwnedTaskTabV41 = globalThis.__v42Fixture.tab;
let secureConsoleOwnedTaskTabV41Eligible = true;
let secureConsoleSetupBrowserRuntimeV41 = () => {};
let secureConsoleAgentV41 = {};
let secureConsoleChromeV41 = {};
const nodeRepl = {
  async write(value) {
    globalThis.__v42Fixture.writes.push(value);
  },
};
`;
  try {
    await new AsyncFunction(prelude + cell)();
  } finally {
    delete globalThis.__v42Fixture;
  }
  assert.equal(fixture.writes.length, 1);
  return fixture.writes[0];
};

const success = await run(false);
assert.equal(
  success.result,
  "EXACT_V42_TOKEN_PAGE_SEMANTIC_READINESS_PASS",
);
assert.equal(success.declarationShape, true);
assert.equal(success.predecessorStateExact, true);
assert.equal(success.tokenSemanticSignature, true);
assert.equal(success.continuationBindingsRetained, true);
assert.equal(success.failureCleanupComplete, false);
assert.equal(success.bindingEligible, true);
assert.equal(success.bindingNull, false);
assert.equal(success.predecessorBindingNull, true);
assert.equal(success.predecessorState, "V41_TRANSFERRED_TO_V42");
assert.equal(success.errorClass, "NONE");
assert.equal(success.consumed, true);
assert.equal(success.readinessAttempted, 3);
assert.equal(success.readinessFulfilled, 3);

const failure = await run(true);
assert.equal(
  failure.result,
  "V42_TOKEN_PAGE_SEMANTIC_READINESS_FAILED_STOP",
);
assert.equal(failure.errorClass, "Error");
assert.equal(failure.consumed, true);
assert.equal(failure.bindingEligible, false);
assert.equal(failure.bindingNull, true);
assert.equal(failure.predecessorBindingNull, true);
assert.equal(failure.failureCleanupComplete, true);
assert.equal(failure.predecessorState, "V41_DOWNSTREAM_FAILURE_DETACHED");

console.log(JSON.stringify({
  result: "V42_PURE_FIXTURES_PASS",
  briefBytes: Buffer.byteLength(brief),
  briefSha256: crypto.createHash("sha256").update(brief).digest("hex").toUpperCase(),
  executableBytes: Buffer.byteLength(cell),
  executableSha256: crypto.createHash("sha256").update(cell).digest("hex").toUpperCase(),
  syntax: "PASS",
  fullCellSuccess: true,
  fixedFailureCleanup: true,
}));
