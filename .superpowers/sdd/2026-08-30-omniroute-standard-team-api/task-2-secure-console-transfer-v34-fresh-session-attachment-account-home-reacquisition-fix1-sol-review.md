# OmniRoute V34 fresh-session attachment and account-home reacquisition fix round 1 — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only corrected brief commit
`de938a548b036e7b83af4b4168066b0e6cd25066` and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v34-fresh-session-attachment-account-home-reacquisition-brief.md`.
Its direct parent is the initial independent Sol High FAIL review commit
`964eaf4be28cf5fe8936e1ec30a3a8f72425c2eb`.

I independently reviewed the corrected committed bytes against findings
`V34-001` and `V34-002`, then rechecked the exact current runtime/API pins,
two-call consumption and predecessor semantics, complete-documentation output,
external profile/window/tab confirmation, selected-only adoption, page
signature and untrusted validation, prohibited surfaces, cleanup/residue,
counters, secret exclusions, and both mandatory later confirmation boundaries.

I performed no Node, Chrome, browser-binding, provider, clipboard, credential,
network, DNS, routing, process, Prox-01, or VM action and did not evaluate either
V34 cell. The supplied AsyncFunction syntax PASS pins were not rerun because no
concrete syntax doubt remained. The only workspace write is this assigned
review artifact.

## Final verdict

**PASS** — `V34-001` and `V34-002` are closed, with no unresolved Critical,
HIGH, IMPORTANT, or Minor finding.

`authorizes_live_execution=false`

## Direct-byte and Git evidence

- Reviewed commit: `de938a548b036e7b83af4b4168066b0e6cd25066`.
- Direct parent: `964eaf4be28cf5fe8936e1ec30a3a8f72425c2eb`.
- The reviewed commit modifies exactly the assigned V34 brief path.
- Corrected brief: `21185` bytes, SHA-256
  `1D0B29390AE70279E4C462E687F667B9A3384A0052E66F8E2C1FA68904E68D44`,
  Git blob `848ea19d600f15e879f7e48d7b459d88e49231f4`.
- Call 1: `5473` normalized UTF-8 LF bytes, SHA-256
  `E529B443FD20595772A56C7BC6E66B8203604FD168C21195DE31E1A05646D637`.
- Call 2: `8224` normalized UTF-8 LF bytes, SHA-256
  `5934E2C76F37B1F76490FD06B0EF59E12447153F6567DC3BA3590974BBD932EA`.
- The corrected brief is UTF-8 without BOM and LF-only, contains exactly two
  JavaScript fences, and `git diff-tree --check` reports no whitespace error.
- Before review creation, the index held zero paths and the inherited exact
  twelve-path dirty product baseline was present and unstaged.

## V34-001 closure — terminal-output cleanup and honest transport uncertainty

**Resolved.** Both fixed terminal writes are now explicit awaited boundaries
inside dedicated `try/catch` blocks.

For Call 1, a JavaScript-visible terminal-write rejection now:

- forces `secureConsoleV34AttachmentExact=false`;
- sets fixed state `V34_ATTACHMENT_FINAL_OUTPUT_FAILED_STOP`;
- clears the Chrome, agent, and setup bindings; and
- rethrows without attempting another output.

For Call 2, a JavaScript-visible terminal-write rejection now:

- nulls the selected owner binding and marks it ineligible;
- sets fixed state `V34_FINAL_OUTPUT_FAILED_STOP`;
- clears the Chrome, agent, and setup bindings; and
- rethrows without closing the externally owned tab or attempting another
  output.

The complete documentation write is also explicitly awaited. Its failure
remains inside Call 1's primary guarded block, which sanitizes the error,
clears the attachment bindings, and permits the one fixed terminal failure
record. This is classification output, not a retry of the documentation.

The brief no longer overclaims cleanup for failures outside JavaScript's
visibility. It states that transport failure or truncation may leave bindings
and requires disposal of the entire fresh Node realm before any separately
reviewed successor. No retry, continuation, binding reuse, or manual integration
is permitted. These rules close the prior contradiction between external PASS
requirements and persistent binding state.

## V34-002 closure — exact current wait API

**Resolved.** Call 2 now uses exactly
`await adopted.playwright.waitForTimeout(20000)`. The undocumented
`{ state: "networkidle" }` argument is absent, so the source matches the pinned
current API and runtime implementation: one bounded fixed 20-second wait.

## Exact predecessor and runtime/API boundary

The parent V33 drift incident remains exact: V33 was never sent to Node and
never consumed; its old API-document pin and persistent predecessor/controller
bindings were absent; and every V33 declaration remained undefined. V33 is
permanently action-time ineligible and is neither retried nor adapted by V34.

The reviewed current runtime pins remain:

- `browser-client.mjs`: `149771` bytes, SHA-256
  `A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`;
- `api.json`: `58480` bytes, SHA-256
  `A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.

The exact module exposes the reviewed `setupBrowserRuntime` entry point. The
exact API shapes used by V34 remain valid: browser get/documentation,
selected-tab acquisition, tab goto/URL, one-argument wait, locator, and
read-only locator evaluation. Call 2 remains title-free.

## Full inherited security review

- Call 1 consumes the attachment gate before import, setup, connect, or
  documentation. The exact pinned module path, setup call,
  `browsers.get("chrome")`, and complete documentation read/write occur once.
  AttachmentExact requires every shape and attempted/fulfilled pair `1 / 1`.
- Call 2 separately consumes adoption before any precondition or selection. It
  requires exact persistent Call-1 PASS, then calls `tabs.selected()` exactly
  once. There is no list, get-by-ID, new tab, alternate browser, reconnect,
  second selection, fallback, or retry.
- The exact owner-supplied Chrome profile/window/task-tab selection remains a
  mandatory external confirmation before both calls. No code reads profile,
  window, extension, cookie, storage, password, or session metadata.
- The selected object must expose a bounded control-free ID plus only the
  required tab methods. The opaque ID is never emitted. The exact external tab
  is retained only after full semantic PASS and is never created or closed.
- Navigation is fixed to the Cloudflare root. The private returned URL must
  exactly match HTTPS, exact host, one 32-hex account, and account-home path
  before the page snapshot.
- The title-free page-local evaluator is synchronous and read-only. Its result
  must be a cross-realm plain record with exact keys, typed booleans, and safe
  counts in `0..1000000`. The unique zone href is privately restricted to exact
  HTTPS Cloudflare origin, empty port/credentials, and original account/zone
  pathname. Raw href, URL, account, page, selector, and tab-ID data are not
  emitted.
- Semantic PASS requires exact account-home host/path, exactly one zone href,
  positive anchors, and zero busy markers. Errors emit only a sanitized class.
- Ordinary Call-2 failure nulls/disqualifies the owner binding and clears the
  controller globals. JavaScript-visible final-output failure runs the new
  cleanup; unobservable output uncertainty requires whole-realm disposal.
- There is no screenshot, DOM serialization, clipboard, click, press, fill,
  Create, edit, delete, provider mutation, process start, VM mutation,
  proxy/routing change, credential action, retry, fallback, verdict relaxation,
  or manual integration.
- The final Create/native Copy/native masked Paste confirmation and later
  separate exact-row deletion confirmation remain explicit, mandatory, and
  unreached.

## Static method and counter cardinality

Call 1 contains exactly:

- dynamic import `1`; setup `1`; `browsers.get("chrome")` `1`;
- documentation read `1`; awaited documentation write `1`; awaited fixed
  terminal write `1`; terminal cleanup catch `1`;
- five attempted/fulfilled pairs, each with one increment site per member;
- one `writeAttempted` declaration and one increment;
- tab/profile/browser listing, selected/get/new tab, navigation, screenshot,
  clipboard, and provider action: `0`.

Call 2 contains exactly:

- `tabs.selected()` `1`; fixed `goto` `1`; one-argument wait `1`; URL read `1`;
- locator evaluation `1`; awaited fixed terminal write `1`; terminal cleanup
  catch `1`;
- five attempted/fulfilled pairs, each with one increment site per member;
- one `writeAttempted` declaration and one increment;
- browser/tab listing, tab get/new/close, title, click/press/fill, screenshot,
  clipboard, fetch, and provider action: `0`.

## Finding counts and limits

- Critical: `0`.
- HIGH: `0`.
- IMPORTANT: `0` (`V34-001` closed).
- Minor: `0` (`V34-002` closed).

This static PASS does not authorize either live call. The separate
non-self-referential classification, action-time pins, exact external
confirmation, and sole-owner execution remain required.

## Final verdict

**PASS**

Unresolved findings: Critical `0`, HIGH `0`, IMPORTANT `0`, Minor `0`.

`authorizes_live_execution=false`
