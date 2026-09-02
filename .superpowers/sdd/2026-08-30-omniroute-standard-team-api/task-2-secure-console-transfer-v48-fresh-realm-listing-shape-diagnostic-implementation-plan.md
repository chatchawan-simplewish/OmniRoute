# OmniRoute V48 Listing-Shape Diagnostic Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build, independently approve, classify, and consume exactly once a sanitized read-only diagnostic that identifies V47's rejecting trusted-listing predicate without exposing tab data or performing a provider action.

**Architecture:** Reuse the pinned V47 CUA runtime boundary and the proven V45 descriptor-only inspection pattern. Keep the live executable self-contained, exercise its pure inspector against hostile fixtures offline, then pass the exact committed bytes through independent Sol High review and a non-self-referential classification before any live send.

**Tech Stack:** JavaScript ES modules, Node.js `vm`, PowerShell, Git, persistent CUA JavaScript realm.

## Global Constraints

- V47 is consumed and failed; never retry, continue, reinterpret, relax, or reuse it.
- V48 is diagnostic-only, single-use, no-retry, permanently ineligible for tab adoption, and owned solely by the Sol High consuming task.
- Inspect only cached own-property descriptors; never invoke untrusted iterators, getters, setters, callback enumerators, or direct indexed reads.
- Never emit tab identifiers, titles, URLs, group values, page data, exception text, provider data, clipboard data, or secrets.
- Perform no claim, navigation, wait, page read, DOM action, clipboard action, provider mutation, DNS action, VM action, network request, or background process.
- Preserve the exact 12-path dirty product baseline and stage every artifact by exact path only; never use `git add .`.
- Do not execute live until independent Sol High PASS, non-self-referential classification, post-commit tuple, action-time pins, fresh realm, declaration audit, and fresh external task-tab confirmation all pass.
- Another Codex task may control different tabs in the same profile/window only while its tab and live-resource lane are disjoint; overlap on the same tab or Cloudflare object is a fail-closed stop.

---

### Task 1: Implement the descriptor-only diagnostic and hostile fixtures

**Files:**
- Create: `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v48-fresh-realm-listing-shape-diagnostic-executable.js`
- Create: `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v48-pure-fixtures.mjs`

**Interfaces:**
- Consumes: the exact V47 pinned runtime/module/docs constants and documented tab key classification.
- Produces: one self-contained CUA cell with only `secureConsoleV48Consumed`, `secureConsoleV48State`, and `secureConsoleV48Result` retained at top level; one fixture script whose only success output is `V48_PURE_FIXTURES_PASS`.

- [ ] **Step 1: Extract the smallest reusable inspector boundary**

Copy only the cached-standard-built-in and descriptor-inspection logic from the committed V45 diagnostic. Keep its strict historical all-values predicate, but report every V47 array and rank-zero record predicate independently. Define one pure function with this exact interface:

```js
const inspectOpenTabsV48 = (value) => ({
  arrayIsArray: false,
  arrayOwnSymbolCountZero: false,
  lengthDescriptorPresent: false,
  lengthDescriptorData: false,
  lengthDescriptorNonEnumerable: false,
  lengthDescriptorNoAccessor: false,
  boundedLength: false,
  offeredCount: -1,
  arrayOwnNamesExact: false,
  allIndexDescriptorsDataEnumerable: false,
  allIndexValuesNonNullObjects: false,
  descriptorIndexCountMatchesLength: false,
  rankZeroNonNullObject: false,
  rankZeroOrdinaryPrototype: false,
  rankZeroPrototypeDepthBounded: false,
  rankZeroOwnSymbolCountZero: false,
  rankZeroKnownKeysOnly: false,
  rankZeroRequiredIdentityPresent: false,
  rankZeroUnexpectedKeyCount: -1,
  rankZeroDescriptorsSafe: false,
  rankZeroRequiredValuesSafeStrings: false,
  rankZeroOptionalValuesStringOrUndefined: false,
  rankZeroAllValuesV47Safe: false,
  urlFieldPresent: false,
  urlFieldSafeString: false,
  urlParseSucceeded: false,
  urlHttps: false,
  urlCloudflareHostExact: false,
  urlApiTokensPathExact: false,
  documentedKeyChecks: Object.create(null),
});
```

`documentedKeyChecks` must contain a fixed property for every exact V47 documented key. Each property contains only `{ present, data, enumerable, noAccessor, required, valueTypeAllowed }` booleans. Do not place a key value or field value in the result.

- [ ] **Step 2: Write hostile fixtures before the live wrapper**

Use Node's standard `assert/strict` and `vm`; add no dependency. Cover these exact cases:

```js
const cases = [
  'ordinary documented record',
  'optional field undefined',
  'array accessor index',
  'array own symbol',
  'sparse array',
  'record extra key',
  'record accessor field',
  'record own symbol',
  'record non-ordinary prototype',
  'malformed length descriptor/value',
  'malformed URL',
  'throwing proxy/object',
];
```

Assert that every case returns only fixed keys, `offeredCount` and unexpected-key count are bounded or `-1`, optional `undefined` is distinguished from the strict historical predicate, no getter counter increments, and no raw fixture value appears in serialized output.

- [ ] **Step 3: Add the one-shot live wrapper**

The wrapper must set `secureConsoleV48Consumed = true` before setup, validate the pinned runtime/docs exactly, name the session once, call `openTabs()` once, call `inspectOpenTabsV48()` once, clear all local bindings in `finally`, and return one fixed object. Initialize and retain only:

```js
let secureConsoleV48Consumed = false;
let secureConsoleV48State = 'not-started';
let secureConsoleV48Result = null;
```

The success state is `diagnostic-captured-ineligible`; the failure state is `failed-ineligible`. The outer catch may emit only `errorClass: 'Error'`. Every forbidden-operation counter remains exactly zero.

- [ ] **Step 4: Run syntax and fixture checks**

Run in PowerShell as one block:

```powershell
$dir = '.superpowers/sdd/2026-08-30-omniroute-standard-team-api'
$exe = Join-Path $dir 'task-2-secure-console-transfer-v48-fresh-realm-listing-shape-diagnostic-executable.js'
$fixture = Join-Path $dir 'task-2-secure-console-transfer-v48-pure-fixtures.mjs'
node --check $exe
if ($LASTEXITCODE -ne 0) { throw 'V48 executable syntax failed' }
node $fixture
if ($LASTEXITCODE -ne 0) { throw 'V48 pure fixtures failed' }
```

Expected output ends with exactly `V48_PURE_FIXTURES_PASS` and contains no tab/provider values.

- [ ] **Step 5: Self-review and commit exact paths**

Check no placeholders, dynamic output keys, raw-value logging, retries, fallback, or forbidden calls exist. Stage only the two exact paths and commit command-scoped as `Codex <codex@local>`:

```powershell
git add -f -- $exe $fixture
git -c user.name=Codex -c user.email=codex@local commit -m 'test(omniroute): add V48 listing diagnostic'
```

Verify the commit contains exactly two paths, the index is empty, and the exact 12-path dirty product baseline remains.

### Task 2: Produce immutable review evidence and obtain independent Sol High PASS

**Files:**
- Create: `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v48-fresh-realm-listing-shape-diagnostic-review-package.md`
- Create by independent reviewer: `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v48-fresh-realm-listing-shape-diagnostic-sol-review.md`

**Interfaces:**
- Consumes: exact committed design, plan, executable, and fixture bytes from Task 1.
- Produces: hashes, blob IDs, test evidence, and independent verdict for precisely those bytes.

- [ ] **Step 1: Build the review package**

Record commit/parent, exact paths, Git blobs, byte counts, SHA-256, extracted-cell count, declaration names, fixed result keys, forbidden-token scan, syntax result, fixture result, index count, 12-path baseline, runtime/docs pins, and evidence-worktree pin. Do not include runtime tab data or secrets.

- [ ] **Step 2: Commit only the review package**

```powershell
git add -f -- '.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v48-fresh-realm-listing-shape-diagnostic-review-package.md'
git -c user.name=Codex -c user.email=codex@local commit -m 'docs(omniroute): package V48 review evidence'
```

- [ ] **Step 3: Request independent Sol High review**

Give the reviewer only the design, plan, review package, exact commits/hashes, and files under review. Require direct-byte review and a fixed verdict of `PASS` or `FAIL`; any unresolved Critical, HIGH, or IMPORTANT finding is `FAIL`. The reviewer must not execute CUA or provider actions.

- [ ] **Step 4: Commit the independent review alone**

The reviewer stages only its exact review path and commits with its command-scoped identity. Confirm the parent is the review-package commit, the index is empty, and the 12-path baseline remains.

### Task 3: Classify and consume V48 once

**Files:**
- Create: `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v48-fresh-realm-listing-shape-diagnostic-execution-classification.md`
- Create after execution: `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v48-listing-shape-diagnostic-live-result.md`

**Interfaces:**
- Consumes: exact Sol High PASS review commit and Task 1 bytes.
- Produces: non-self-referential eligibility classification, post-commit tuple, and one sanitized terminal diagnostic result.

- [ ] **Step 1: Write and commit the execution classification**

Classify only already committed evidence. State V48 is eligible for one diagnostic send only, permanently ineligible for adoption, and spent on any output/uncertainty. Its parent must be the exact Sol High PASS review commit. Commit only this path.

- [ ] **Step 2: Build the post-commit coordinator tuple**

After the classification commit, prove exact HEAD/parent/path/blob/bytes/SHA-256 for every V48 artifact, empty index, exact 12-path dirty baseline, stable projection `10661` records with SHA-256 `C4C85893769D133224AC7404B628C8B0D4B0EBBFF471620B158E652E152B4EBD`, clean evidence worktree `80adaa7d5d63d1d2c7bfa63b236c6bee93b3b1d8`, pinned runtime/docs, DNS absence, Windows no-residue, and VM1205 safe state.

- [ ] **Step 3: Reset and obtain the fresh external confirmation**

Reset the persistent CUA realm. The first new-realm call must be exactly `await cua.getState();`. Require a new exact confirmation that `Codex-Chrome-Bell-PC2`, the intended window, and intended Cloudflare API Tokens tab are selected. Stop if the same tab or Cloudflare object is being controlled elsewhere.

- [ ] **Step 4: Audit declarations and send once**

Run the fixed `typeof` audit for every historical and V48 top-level declaration. If and only if every declaration is `undefined`, send the exact reviewed executable once. Never retry or continue it.

- [ ] **Step 5: Prove cleanup and reset**

Run one fixed state-only query proving consumed, terminal ineligible state, cleared retained result/bindings as specified, and all forbidden-operation counters zero. Reset the realm immediately.

- [ ] **Step 6: Record and commit the sanitized result**

Write only the fixed diagnostic fields, cleanup proof, and no-residue evidence. Commit that one exact path and preserve the empty index plus 12-path dirty product baseline. If V48 fails or is uncertain, record it as spent and design a new reviewed V49 contract; never retry V48.
