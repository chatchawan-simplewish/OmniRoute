# OmniRoute V34 fresh-session attachment and account-home reacquisition — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only commit
`13b5816a82a8b00082590f373f17e63958c574c4` and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v34-fresh-session-attachment-account-home-reacquisition-brief.md`.
Its direct parent is the V33 action-time runtime/controller drift incident
commit `60358392f188fe3706c36aa518c9947a21e8ba7b`.

I independently reviewed the two committed cells, exact current runtime/API
pins, two-call consumption and predecessor semantics, complete-documentation
boundary, external profile/window/tab confirmation, selected-only adoption,
page signature and untrusted data validation, prohibited surfaces, cleanup and
residue behavior, counters, secret exclusions, and both mandatory later
confirmation boundaries.

I performed no Node, Chrome, browser-binding, provider, clipboard, credential,
network, DNS, routing, process, Prox-01, or VM action and did not evaluate either
V34 cell. The only workspace write is this assigned review artifact.

## Final verdict

**FAIL** — one IMPORTANT finding remains unresolved. V34 must not be executed.

`authorizes_live_execution=false`

## Direct-byte and Git evidence

- Reviewed commit: `13b5816a82a8b00082590f373f17e63958c574c4`.
- Direct parent: `60358392f188fe3706c36aa518c9947a21e8ba7b`.
- The reviewed commit adds exactly the assigned V34 brief path.
- Brief: `19681` bytes, SHA-256
  `EBA52AB5EA70E62D0A63121A25105932936D4B16A04AABABB5DFDB65A239C261`,
  Git blob `7f11aedc2e77b68a5ed51454279c47f73c6f1c40`.
- Call 1: `5119` normalized UTF-8 LF bytes, SHA-256
  `8700F59244DFC95F26A1A364A64621D1A8CA2C4C917BA4D2D5CD5FCCDAE9B253`.
- Call 2: `7864` normalized UTF-8 LF bytes, SHA-256
  `D3995596D42A01191DEBE046E05A6074B8FA690CF072C8DEA793D79663AE2B9D`.
- The brief is UTF-8 without BOM and LF-only, contains exactly two JavaScript
  fences, and `git diff-tree --check` reports no whitespace error.
- Source-level static inspection found no syntax contradiction. No Node parse
  or execution command was run.
- Before review creation, the index held zero paths and the inherited exact
  twelve-path dirty product baseline was present and unstaged.

## Exact predecessor and runtime/API evidence

The parent incident proves V33 was never sent to Node and never consumed. Its
old API-document pin disappeared after the installed package moved to
`26.831.20005`, the persistent V5/V32 bindings were absent, and every V33
declaration remained undefined. V33 is permanently action-time ineligible and
cannot be retried, substituted, or used as a predecessor binding.

The current installed files reproduce independently:

- `browser-client.mjs`: `149771` bytes, SHA-256
  `A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`;
- `api.json`: `58480` bytes, SHA-256
  `A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.

The exact module has one exported `setupBrowserRuntime` entry point. The exact
API document declares `Browsers.get(id: string)`,
`Browser.documentation()`, `Tabs.selected()`, `Tab.goto(url)`, `Tab.url()`,
`Tab.title()`, `PlaywrightAPI.locator(selector)`, and
`PlaywrightLocator.evaluate(callback, arg?, options?)` with the shapes used by
the contract. The brief does not call `title()`.

## Finding

### V34-001 — IMPORTANT — final-output rejection can retain bindings on an externally non-PASS call

Call 1 sets `secureConsoleV34AttachmentState="V34_ATTACHMENT_PASS"`, leaves the
runtime/controller globals live, exits its guarded `try/catch`, and only then
performs the fixed terminal `nodeRepl.write` at lines 189-203. Call 2 similarly
stores the selected handle as eligible and retains every controller binding at
lines 397-401, then performs its fixed terminal write outside the guarded block
at lines 411-438.

Both external PASS definitions require complete fixed terminal output and
completed tool status. A synchronous throw or awaited rejection from either
final write is therefore an uncertain/non-PASS consuming call. The current
code has no cleanup path for that boundary:

- after Call 1, attachmentExact/state and the agent/browser/setup bindings can
  remain PASS/live even though Call 2 is forbidden; and
- after Call 2, the exact selected-tab handle can remain globally retained and
  eligible with the controller bindings live even though lines 447-448 promise
  that anything other than Call-2 PASS clears every V34 controller/owner
  binding.

This is not merely missing evidence: it directly contradicts the declared
cleanup/residue state and leaves persistent authority-bearing globals after an
uncertain one-shot result that cannot be retried or continued.

**Required fix:** make each final fixed-output call an explicit awaited
terminal boundary. On any JavaScript-visible rejection, clear the corresponding
attachment/controller/owner bindings, force the fixed failed state and
ineligibility, and rethrow or otherwise stop without a second output attempt.
For output truncation or transport uncertainty that cannot be observed inside
JavaScript, state honestly that bindings may remain and require disposal of the
entire fresh Node realm before any successor; do not claim universal clearing.
Preserve single-write/no-retry semantics and do not close the externally owned
selected tab.

## Minor API conformance note

### V34-002 — Minor — undocumented second argument to `waitForTimeout`

The exact current API declares
`waitForTimeout(timeoutMs: number): Promise<void>`, and the pinned runtime
implementation accepts only that integer. Call 2 passes an additional
`{ state: "networkidle" }` argument at lines 325-328. JavaScript ignores the
extra argument, so the actual behavior is a fixed 20-second delay, not a
network-idle wait.

This does not defeat the subsequent exact URL and page-signature checks, and
the prose claims only bounded settlement, so it is not execution-blocking.
Remove the unused argument in the fix to keep the cell exactly within the
documented current API.

## Correctly preserved security boundaries

- Call 1 consumes `secureConsoleV34AttachmentConsumed` before dynamic import,
  runtime setup, Chrome attachment, or documentation. Its import path, setup,
  `browsers.get("chrome")`, and complete-documentation read each occur once.
- Documentation must be a bounded nonempty string and is written directly in
  one attempt before attachmentExact can become true. Documentation-write
  failure inside the guarded block clears the attachment bindings.
- Call 2 consumes adoption before its predecessor check or selected-tab call.
  AttachmentExact and the exact PASS state are required before one
  `tabs.selected()` call. There is no listing, get-by-ID, new tab, alternate
  browser, reconnect, second selection, fallback, or retry.
- The owner-supplied profile/window/tab choice remains an explicit external
  confirmation before each call. No code reads profile, window, extension,
  cookie, storage, password, or session metadata.
- The selected handle must be a bounded control-free ID-bearing object with the
  exact methods needed. Its ID is never emitted. On ordinary non-PASS paths the
  owner binding is null/ineligible and controller globals are cleared. The
  selected external tab is never created or closed.
- Account-home navigation is fixed to the Cloudflare root. The private returned
  URL must exactly match HTTPS, exact host, a 32-hex account segment, and the
  account-home path before any snapshot.
- The page-local snapshot is title-free, synchronous, read-only, and exact-key
  projected. Host/path booleans are typed, counts are safe integers in
  `0..1000000`, the unique zone href is privately restricted to exact HTTPS
  Cloudflare origin with empty port/credentials and original account/zone
  pathname, and no raw href/account/page data is emitted.
- Semantic PASS requires exact account-home host/path, exactly one zone href,
  positive anchors, and zero busy markers. Exceptions emit only a sanitized
  class name.
- There is no screenshot, DOM serialization, clipboard, click, press, fill,
  Create, edit, delete, provider mutation, process start, VM action,
  proxy/routing change, or credential action.
- The final Create/native Copy/native masked Paste confirmation and separate
  exact-row deletion confirmation remain explicit, mandatory, and unreached.

## Static method and counter cardinality

Call 1 contains exactly:

- dynamic import `1`; setup call `1`; `browsers.get("chrome")` `1`;
- documentation read `1`; documentation write `1`; fixed terminal write `1`;
- five attempted/fulfilled pairs, each with one increment site per member;
- tab/profile/browser listing, selected/get/new tab, navigation, screenshot,
  clipboard, and provider action: `0`.

Call 2 contains exactly:

- `tabs.selected()` `1`; fixed `goto` `1`; wait `1`; URL read `1`;
- locator evaluation `1`; fixed terminal write `1`;
- five attempted/fulfilled pairs, each with one increment site per member;
- browser/tab listing, tab get/new/close, title, click/press/fill, screenshot,
  clipboard, fetch, and provider action: `0`.

Each cell declares one `writeAttempted` counter and increments it once. These
cardinalities are correct but do not close `V34-001`.

## Finding counts and limits

- Critical: `0`.
- HIGH: `0`.
- IMPORTANT: `1` (`V34-001`).
- Minor: `1` (`V34-002`).

## Final verdict

**FAIL**

Unresolved findings: Critical `0`, HIGH `0`, IMPORTANT `1`, Minor `1`.

`authorizes_live_execution=false`
