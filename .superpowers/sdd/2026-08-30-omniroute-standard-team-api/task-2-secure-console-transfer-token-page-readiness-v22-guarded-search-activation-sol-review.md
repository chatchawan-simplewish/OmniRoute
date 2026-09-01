# OmniRoute V22 guarded explicit search activation — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only commit
`be0f466e28df313e7aeab153481e92b52745de24` and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-token-page-readiness-v22-guarded-search-activation-brief.md`.
Its direct parent is the V21 Sol High FAIL review commit
`b48d557bc8a48eee13ed60dfa7c0b8917a18b748`.

I independently checked direct committed bytes, syntax, the consumed V20
incident and absent/unconsumed V21 boundary, exact pre-Enter input ownership,
value/type/form/section checks, native associated-submitter semantics,
same-URL and AJAX/provider-mutation risk, one-Enter cardinality, immediate URL
recheck, inherited V4/V15 page signatures and completeness, exact predecessor
state, fixed output, cleanup/no-residue/no-retry behavior, secret exclusions,
and both mandatory manual confirmation boundaries.

I performed no Chrome, Node browser binding, provider, clipboard, credential,
process, network, DNS, routing, Prox-01, or VM action and did not evaluate the
V22 cell. The only workspace write is this assigned review artifact.

## Final verdict

**FAIL** — one unresolved HIGH remains. V22 closes the browser-native implicit
form-submission portion of V21-001, but does not prove that the dispatched Enter
event cannot invoke an application keyboard handler that performs a same-URL
AJAX/provider mutation. The postpress URL equality check cannot detect or undo
that effect.

`authorizes_live_execution=false`

## Direct-byte, syntax, and Git evidence

- Reviewed commit: `be0f466e28df313e7aeab153481e92b52745de24`.
- Direct parent: `b48d557bc8a48eee13ed60dfa7c0b8917a18b748`.
- The reviewed commit adds exactly the assigned V22 brief path.
- V22 brief: `41295` bytes, SHA-256
  `45C6296E2182CA327FA329B27D48C297D5FFEFC1B6B65C5EADA916E38E5F2579`,
  Git blob `23ffba7d031778c05552c0f18781c73f55bfb506`.
- The executable payload is `35755` bytes at SHA-256
  `D1F292548EFA3BFBF16DABBFDF096F4961CBE10916D12873E5421118D4DE6C70`.
- Encoding is UTF-8 without BOM and LF-only with zero CR bytes. There is one
  `javascript` fence and no extra blank line at EOF.
- Non-evaluating top-level-awaited JavaScript parse: **PASS**. The outer IIFE
  is awaited exactly once.
- `git diff-tree --check` reports no whitespace error.
- Index before review creation: zero paths. The exact inherited twelve-path
  dirty baseline was present and remained unstaged.

## Predecessor evidence and one-shot boundary

The immutable V20 incident pins reproduce exactly: commit
`237ca08aa206deac4c642bdd7dd69c5c673e6739`, `3499` bytes, SHA-256
`55A896088D25DE02D75DE9071F5FE76459CD5750C721F9CA94EE56CD764EE28F`,
and blob `6252e4265da78228612d96e4106fba4e35e28c62`. It proves the inherited
baseline and five candidate rows, then failed cleanly at the candidate-set
hidden wait after the exact fill/value proof. Its exact tab closed; it is
consumed/null/ineligible/failed-clean with no read or detach consumed.

The V21 brief and FAIL review pins also reproduce exactly:

- V21 brief commit `f7d705c7c67d46c8db4ee46f693fa7cd542dd784`:
  `37654` bytes, SHA-256
  `942C9130BD1060541F88FE17305CDAB2427FF9F6BA4E7701D4C0FC39D8629EDE`,
  blob `af21e3347226e40bd2ccd4e515695f32e2c79f2d`;
- V21 review commit `b48d557bc8a48eee13ed60dfa7c0b8917a18b748`:
  `11248` bytes, SHA-256
  `952BBA8F9C4ADAA72FF71F6D42393CEB18BB73CB515E17E4781A35269CF4491A`,
  blob `ada9fdf5bf1be7cb3a3741dce1b5454a8c4ed3bf`.

V22 sets its consumed flag before any await. Its declaration and predecessor
checks require V20 through V16 consumed/null/ineligible/exact failed-clean,
both detach flags false, and provider-read flags false; V15 through V9 consumed
with retained handles null; and the exact consumed/null/ineligible/no-detach/
no-read V4 state. Every V21 persistent declaration is required to be
`undefined`, correctly preserving the fact that V21 was never evaluated.
No predecessor is invoked, reset, continued, reinterpreted, or retried.

## V21-001 closure analysis

### Browser-native form/default-action portion — closed

Immediately before Enter, the same exact visible placeholder-search locator is
evaluated synchronously. Strict locator evaluation plus the earlier exact count
and its fixed-key trusted projection establish that the input is connected,
visible, exact-valued, and the sole exact-valued search input in the same
nearest depth-three section. The guard also requires the reflected input type
to be `search` or `text`.

Most importantly, it requires `input.form === null`. The DOM `form` property
accounts for both an ancestor form and an external association through a
`form` attribute. Therefore the exact input has no associated form and cannot
participate in browser-native implicit form submission or activate an
associated default submitter. The emitted
`associatedFormSubmitterCount === 0` is derived rather than independently
enumerated, but it is semantically sound for this native boundary because a
null form owner means there is no associated form in which to enumerate a
submitter.

The same read also requires section depth three, exact-valued search-input
count one, and zero section descendants matching the defined Create-like
button/link action set. Those checks close the native implicit/default-form
scenario identified in the narrow required correction.

### V22-001 — HIGH: Enter's application-handler effect remains unbounded

The executable next dispatches a real Enter key event with
`tokenFilter.press("Enter", { timeoutMs: 5000 })`. Proving `input.form === null`
prevents the browser's native implicit form-submission algorithm; it does not
constrain JavaScript event listeners on the input, its ancestors, `document`,
or `window`. Such a listener can respond to `keydown`, `keypress`, or `keyup`
and issue an AJAX/fetch mutation, invoke another control, or initiate a
same-document action before `press()` settles.

The section Create scan does not prove handler behavior. It only text-matches
`button`, `a`, `[role=button]`, and `[role=link]` descendants for three fixed
labels. It neither inspects registered keyboard handlers nor establishes a
fixed controller mapping from Enter to a read-only search operation. Input
type `search` or `text` likewise does not constrain application listeners.

The immediate `tab.url()` equality check is detection after the event, not a
prevention boundary. It rules out a completed cross-URL navigation visible at
that read, but still cannot exclude:

- a same-URL submission or reload;
- a history-preserving or same-document action;
- an AJAX/fetch provider mutation with no URL change; or
- a mutation that finishes before the URL read or continues asynchronously
  after it.

Closing the owned tab on a later rejection cannot reverse a provider mutation.
The executable therefore does not enforce its prose claim that Enter is not
authority to submit, create, edit, delete, or mutate provider-persistent state.
Because this is a one-shot security boundary and the possible external side
effect is not recoverable by exact-handle cleanup, the unresolved gap is HIGH.

#### Required correction

Do not dispatch Enter unless immutable/pinned application evidence establishes
that the exact control's Enter path is read-only search activation and cannot
call a provider-persistent endpoint. Otherwise use a separately reviewed
readiness mechanism that does not dispatch a keyboard event with unbounded
application-handler semantics. Retain the form-null and immediate URL checks;
neither alone is proof against same-URL AJAX effects.

## Closed static checks outside V22-001

### Page signature, V4/V15 completeness, and terminal proof

The inherited baseline remains fixed to the authenticated token page: exact
public URL, one visible connected empty search input in the nearest depth-three
section, two page tables, one section table/body, five visible rows, no grid,
pagination, busy marker, status/empty marker, or section Create-like action.
Before fill it still proves query/empty-marker/visible-candidate counts
`0/0/5`.

The fixed non-secret fill remains exact. If Enter were independently proven
safe, the inherited dynamic candidate locator is still section-scoped to
`tbody tr`, excludes the two exact V4 empty-marker texts, and requires visible
rows. Its lazy first-row hidden wait followed by the synchronous terminal
snapshot requires exact query echo/count, depth/table/body structure, zero
grid/pagination/busy/candidate/matching rows, one exact visible V4 empty
marker, and one of the three accepted row variants. The later checks require
one global actionable exact `Create Token` and zero exact target-name/role-row/
evaluator matches. These preserve the inherited V4/V15 semantic page signature
and completeness boundary.

### Cross-realm validation and fixed safe output

All three page evaluators are synchronous and read-only. There is no async
evaluator, page Promise, `MutationObserver`, page timer, expando, polling loop,
or page-resident state. Baseline, prepress, and terminal values pass the pinned
cross-realm plain-record rule, exact-key schemas, explicit boolean types,
bounded safe-integer checks, and fixed-key local projection before use.

Terminal output contains only fixed result/cleanup strings, sanitized error
class, booleans, bounded integers, counters, and already validated trusted
records. It does not emit raw URL, text, ID, title, attribute, DOM, HTML,
screenshot, key name, token, credential, secret, or clipboard content.

### Call cardinality, retention, and cleanup

Static call-site counts are:

- one each: `tabs.new`, fixed `goto`, fill, exact Enter press, exact-handle
  close, and terminal write;
- two URL reads: initial navigation confirmation and immediate post-Enter
  equality check;
- two waits: initial visible input and candidate-set hidden;
- three synchronous evaluator calls; and
- zero click, selected/list/get, connect/reconnect, detach, screenshot,
  clipboard, Create/edit/delete, retry, or fallback call site.

The created handle is chained into the local and durable V22 bindings before
every later await. Exact PASS retains only that handle and marks it eligible.
Rejected or uncertain creation reports residue unproven; malformed/close-failed
handles are retained ineligible; a settled successful close clears the binding
only afterward; and precreation failure is clean. These branches correctly
preserve tab-residue truth, but cannot undo V22-001's possible external effect.

### Secrets and mandatory confirmations

Executable scans find no Bearer value, JWT form, long hexadecimal secret,
credential read, or clipboard operation. The mandatory final Create/native
Copy/native masked Paste confirmation and the later separate exact-row deletion
confirmation remain explicit, unreached, and mandatory. There is no VM, DNS,
routing, listener, process, or explicit provider-persistent call site.

## Finding counts and residual limits

- Critical: `0`.
- HIGH: `1` unresolved (`V22-001`).
- IMPORTANT: `0`.
- Minor: `0`.

This review proves only the committed static contract and does not authorize
execution. No classification or post-commit tuple can override V22-001.

## Final verdict

**FAIL**

Unresolved findings: Critical `0`, HIGH `1`, IMPORTANT `0`, Minor `0`.

`authorizes_live_execution=false`
