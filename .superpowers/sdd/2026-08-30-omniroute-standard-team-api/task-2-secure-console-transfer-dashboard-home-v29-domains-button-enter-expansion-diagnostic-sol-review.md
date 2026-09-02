# OmniRoute V29 Domains-button Enter expansion diagnostic — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only commit
`526c479c0f85f00b6f178d3df2987e1d00d9109e` and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-dashboard-home-v29-domains-button-enter-expansion-diagnostic-brief.md`.
Its direct parent is V28 PASS-clean evidence commit
`61f5233ee997ed5ea9f0e6b0561a375453301e94`.

I independently reviewed direct committed bytes, syntax, one-shot consumption,
exact predecessor state, the unique visible/enabled/collapsed button gate, the
single Enter activation, navigation ambiguity, bounded asynchronous read-only
settle, fixed-key/type/completeness validation, output non-leakage,
exact-handle cleanup, no-retry semantics, and the mandatory later confirmation
boundaries.

I performed no Chrome, browser binding, provider, clipboard, credential,
network, DNS, routing, process, Prox-01, or VM action and did not evaluate the
V29 cell. The only workspace write is this assigned review artifact.

## Final verdict

**FAIL** — one unresolved HIGH finding. V29 does not prove that the native
Domains button is outside browser-default form submission semantics before the
sole Enter press, so the claimed expansion-only/no-provider-mutation boundary
is not established.

`authorizes_live_execution=false`

## Direct-byte, syntax, and Git evidence

- Reviewed commit: `526c479c0f85f00b6f178d3df2987e1d00d9109e`.
- Direct parent: `61f5233ee997ed5ea9f0e6b0561a375453301e94`.
- The reviewed commit adds exactly the assigned V29 brief path.
- Brief: `25581` bytes, SHA-256
  `53779221E8C022CC89F5311B8370E301035F87E533FBF1CFEFF981ADA9BDA323`,
  Git blob `f60e80ced03fcc70278e25cc426a1f63faa1575b`.
- Normalized executable: `21487` UTF-8 LF bytes, SHA-256
  `149E43F8F9B66EA3033EC82219466B9250561CFA82D5048FDE487413D8B097A9`.
- Encoding is UTF-8 without BOM and LF-only. Non-evaluating Acorn module parse
  with top-level await: **PASS**.
- Three V29 persistent declarations are present exactly once.
- `git diff-tree --check` reports no whitespace error.
- Before review creation, the index held zero paths and the exact inherited
  twelve-path dirty baseline was present and unstaged.

## V29-001 — HIGH: Enter can invoke unbounded form-submit semantics

V28 proves a unique visible native `BUTTON`, no href or native element-level
`click()` method, an existing `aria-controls` target, enabled/hit-testable/tab-
reachable shape, and clean diagnostic closure. It does not report the button's
HTML type or form owner.

V29's fresh pre-snapshot revalidates tag, visibility, enabled/inert/hit-test
state, hidden controlled target, not-expanded state, and tab stop. It never
reads or validates either `button.type` or `button.form`. The subsequent dynamic
press locator is constrained only to a visible button with exact Domains text.
Static inspection finds zero form-owner, form-attribute, button-type, or
default-submit-impossible predicate.

For a native button, pressing Enter performs activation. A button with submit
semantics and a form owner may therefore invoke browser-default form submission
in addition to or instead of the intended controlled-panel expansion. That can
navigate, send a request, or trigger a same-URL application/provider mutation.
The post-snapshot cannot rule this out: it observes only route/expansion/panel/
anchor booleans and counts, and explicitly allows PASS after the bounded window
even when `settleConditionMet` is false. A same-account-home response or a
same-URL side effect can still satisfy post completeness.

This contradicts the brief's claimed no-submit/no-provider-mutation boundary
and makes the sole irreversible one-shot activation broader than the evidence
supports. Because an unintended submission can cause provider-persistent side
effects that fixed output cannot detect or roll back, this is HIGH.

### Required correction

Before Enter, add fixed-key validated evidence that browser-default submission
is impossible for the exact activation target, for example exact
`button.form === null` or a narrowly reviewed equivalent that proves non-submit
button semantics. Bind the press locator/action-time target to that same safe
shape rather than relying only on tag/text/visibility. Emit only fixed booleans,
never form identity or attribute values. Re-pin and independently re-review the
new committed bytes before any V29 call.

## Closed checks outside V29-001

### One-shot and predecessor exactness

V29 marks its gate consumed before the first await. Its predecessor requires
V23 failed-clean/null/ineligible state, V24 declarations absent, V25 consumed
PASS-clean, V26 and V27 consumed failed-clean with downstream reads unused,
all six V23/V26/V27 detach flags boolean and false, and V28 consumed
`V28_DIAGNOSTIC_PASS_CLEAN` with no retained handle. All three V29 declarations
must be fresh. No consumed predecessor is invoked, reset, continued,
reinterpreted, or retried.

The V28 evidence commit independently records the reviewed/classified V28
tuple, exact `1 / 1` cleanup, no retained handle, fixed structural result, and
no activation or provider mutation. It specifically proves the unique native
button/control-target facts V29 consumes; it does not contain the missing
form/type fact identified in V29-001.

### Unique visible control and single Enter accounting

The pre-snapshot fixed-key validation requires exact Cloudflare account-home,
one total and one visible exact-text Domains button, native button tag, no href
or native click method, enabled/non-inert/hit-testable/pointer-enabled/tab-stop
shape, existing hidden controlled target, not-expanded state, and zero busy
marker. A separate dynamic locator count must also equal one before activation.

There is exactly one `.press()` call site with literal `"Enter"` and a 5000 ms
bound. Counters bracket the single await. There are zero click, fill, second-key,
direct Domains navigation, tab discovery/reacquisition, retry, or fallback call
sites. V29-001 concerns the missing default-submit exclusion, not key count.

### Bounded asynchronous read-only settle

The post evaluator is read-only and bounded twice: internal elapsed time 5000
ms with 100 ms sampling, and outer evaluator timeout 7000 ms. It stops early
only for an account-Domains route, expanded state, visible controlled target,
or controlled anchors. Otherwise it returns one final fixed record at the
internal deadline. It performs no click, key, fill, DOM write, listener,
provider call, fetch, or navigation.

The post route is bound to the original 32-hex account segment and completeness
accepts exactly one of original account-home or same-account Domains, positive
sample/all-anchor/visible-anchor counts, and zero busy markers. Arbitrary host
or path drift fails validation/completeness.

### Fixed-key validation and output safety

The pre record has exact equality over 18 boolean and 3 integer keys; the post
record has exact equality over 11 boolean and 12 integer keys. The pinned
cross-realm rule accepts only a direct null prototype or a prototype whose
parent is null. Every boolean is explicitly typed and every integer must be a
safe value in `0..1000000`; only fixed keys are copied into new trusted local
objects.

Terminal output contains only fixed result/state/cleanup strings, sanitized
error class, booleans, bounded counts, counters, consumed state, and the two
validated fixed-key snapshots. No free-form exception, tag, role, ID,
`aria-controls` value, href, URL, path, account/zone identifier, text, DOM,
HTML, attribute value, screenshot, provider response, credential, token,
secret, or clipboard value is emitted.

### Exact-handle cleanup and no retry

The sole created handle is chained into local and durable V29 bindings before
every later await. Every outcome, including diagnostic PASS, must close that
exact handle. The durable binding clears only after close fulfillment. Close
rejection retains the exact handle, forces non-PASS, and reports unconverged
residue. Rejected/uncertain creation and malformed/no-handle outcomes cannot be
reported clean; only genuine precreation failure is clean.

There is no discovery, reacquisition, continuation, reinterpretation, manual
integration, retry, fallback, second activation, or verdict relaxation. The
mandatory final Create/native Copy/native masked Paste confirmation and later
separate exact-row deletion confirmation remain explicit, unreached, and
mandatory.

## Static cardinalities

- declarations: `3`;
- `tabs.new`: `1`; fixed `goto`: `1`; URL reads: `2`;
- waits: `1`; evaluators: `2`; Enter press: `1`;
- exact-handle close: `1`; terminal write: `1`;
- click/fill: `0 / 0`; selected/list/get discovery: `0`; clipboard/fetch: `0`.

## Finding counts and limits

- Critical: `0`.
- HIGH: `1` unresolved (`V29-001`).
- IMPORTANT: `0`.
- Minor: `0`.

This static review does not authorize live execution. No classification or
post-commit tuple may override `V29-001`.

## Final verdict

**FAIL**

Unresolved findings: Critical `0`, HIGH `1`, IMPORTANT `0`, Minor `0`.

`authorizes_live_execution=false`
