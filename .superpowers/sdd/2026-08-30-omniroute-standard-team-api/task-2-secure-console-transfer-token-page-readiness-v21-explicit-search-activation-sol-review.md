# OmniRoute V21 explicit search activation — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only commit
`f7d705c7c67d46c8db4ee46f693fa7cd542dd784` and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-token-page-readiness-v21-explicit-search-activation-brief.md`.
Its direct parent is consumed-failed-clean V20 incident commit
`237ca08aa206deac4c642bdd7dd69c5c673e6739`.

I independently checked direct committed bytes, syntax, the V20 incident,
unique input/value ownership, exact one-Enter cardinality, immediate URL
recheck, default-submit/Create risk, inherited candidate settlement and
terminal snapshot, exact V20-through-V16 and V4 predecessor state, V4/V15
completeness, fixed output, cleanup/no-residue/no-retry behavior, secrets,
provider-persistent exclusions, and both mandatory confirmation boundaries.

I performed no Chrome, Node browser-binding, provider, clipboard, credential,
process, network, DNS, routing, Prox-01, or VM action and did not evaluate the
V21 cell. The only workspace write is this assigned review artifact.

## Final verdict

**FAIL** — one unresolved HIGH finding permits Enter to trigger an unproven
implicit/default form action before any post-action check. The contract does
not establish its stated no-Create/no-provider-persistent boundary.

`authorizes_live_execution=false`

## Direct-byte, syntax, and Git evidence

- Reviewed commit: `f7d705c7c67d46c8db4ee46f693fa7cd542dd784`.
- Direct parent: `237ca08aa206deac4c642bdd7dd69c5c673e6739`.
- The reviewed commit adds exactly the assigned V21 brief path.
- V21 brief: `37654` bytes, SHA-256
  `942C9130BD1060541F88FE17305CDAB2427FF9F6BA4E7701D4C0FC39D8629EDE`,
  Git blob `af21e3347226e40bd2ccd4e515695f32e2c79f2d`.
- The executable payload ending at `})();` is `33365` bytes at SHA-256
  `06FFB1C36111CAAD6B349B5366C7CA62855F7268F7B2CC3EEC73952B509B2D35`.
- Encoding is UTF-8 without BOM and LF-only with zero CR bytes. There is one
  `javascript` fence.
- Non-evaluating top-level-awaited JavaScript parse: **PASS**. The outer IIFE
  is awaited exactly once.
- Index before review creation: zero paths. The exact inherited twelve-path
  dirty baseline was present and remained unstaged.

## V20 incident and intended replacement boundary

The direct-parent V20 incident reproduces its supplied pins: `3499` bytes,
SHA-256
`55A896088D25DE02D75DE9071F5FE76459CD5750C721F9CA94EE56CD764EE28F`,
Git blob `6252e4265da78228612d96e4106fba4e35e28c62`.

It proves the inherited exact baseline, prefill target/marker/candidate counts
`0/0/5`, one fixed fill, and synchronous postfill exact input value/count one.
The dynamic candidate-set hidden wait then did not fulfill; terminal evaluation
and later reads were skipped. Exact close fulfilled, residue converged, V20 is
consumed/null/ineligible/failed-clean, and no provider or secret action
occurred.

The incident leaves open whether Enter is required to activate this particular
search control. V21 preserves V20 and adds one exact bounded
`tokenFilter.press("Enter", { timeoutMs: 5000 })`, followed by a URL read,
candidate settle wait, and terminal snapshot. That is a narrow hypothesis, but
the added mutating action lacks a mandatory default-action safety proof.

## Finding

### V21-001 — HIGH: Enter can implicitly submit a form or activate a default submitter before the URL check

The prepress proof establishes that the target is one connected, visible
placeholder-search input in the expected section and that its value is exact.
It does **not** inspect or require any of the following:

- `input.form === null`, which covers both an ancestor form and an externally
  associated form via the `form` attribute;
- absence of an enabled default/implicit submit control in an associated form;
- absence of a submit-capable control whose default action Enter can activate;
- input type/search activation semantics; or
- any fixed-key controller proof that Enter's only permitted effect is the
  page-local search activation.

The baseline's `sectionCreateActionableCount === 0` does not close this gap. It
only text-matches button/link-like descendants of the section for `create`,
`create token`, or `create api token`. It neither detects a generic/hidden
submitter nor covers a form-associated submitter elsewhere. The contract later
expects one global actionable `Create Token`, demonstrating that an actionable
Create control exists outside the prefill section scan.

Pressing Enter while a form-associated input is focused can cause browser
implicit submission/default-button activation. A page key handler can likewise
perform an action before `press()` settles. By the time V21 executes
`await tab.url()`, the side effect may already have happened.

The exact URL comparison is a detection check, not prevention or rollback. It
cannot exclude:

- a same-URL form submission or reload;
- a same-document or history-preserving action;
- an AJAX/fetch provider mutation that leaves the URL unchanged; or
- a default submitter action that completes before the URL is reread.

Closing the exact tab after mismatch or rejection does not undo a provider
mutation. Therefore V21's prose claim that Enter is not authority to submit,
create, edit, delete, or mutate provider state is not enforced by the
executable. This violates the one-shot fail-closed boundary and is HIGH.

#### Required correction

Before any Enter press, add a synchronous fixed-key cross-realm projection
from the exact input that at minimum proves:

1. the input is still connected, visible, unique, and exact-valued;
2. `input.form === null` (no ancestor or externally associated form);
3. no form/default submitter can be activated by implicit submission; and
4. the exact search section still contains no Create-like action.

If `input.form` is non-null or the default-action boundary cannot be proven,
the replacement must fail before pressing Enter and use a separately reviewed
non-submit activation mechanism. Any replacement must retain the immediate
post-action URL check, but must not treat URL equality as proof that no default
submission or provider mutation occurred.

## Closed/static checks outside V21-001

### Exact predecessor and one-shot state

V21 sets its consumed flag before validation. It requires V20, V19, V18, V17,
and V16 each consumed, retained binding null, eligibility false, exact
failed-clean state, both detach flags false, and Cloudflare-read flag false. It
also requires V15 through V9 consumed with retained handles null and exact V4
consumed/null/ineligible/failed-clean/no-detach/no-read state. Fresh V21
declarations must be null, ineligible, uncreated, and unused.

No predecessor is called, reset, continued, reinterpreted, reacquired, or
retried. The predecessor chain itself is fail-closed.

### Input ownership, Enter cardinality, and URL read

The one visible search-input locator is shape-checked, waited visible, and
required to count one. Baseline proves it connected, visible, and empty in the
unique nearest depth-three section. After the one fixed fill, the exact
four-field fixed-key query projection proves the same locator connected,
visible, exact-valued, and unique by value within that section.

There is exactly one `press` call site, with exact key `Enter` and bounded
`5000 ms` timeout. The next statements increment the URL counter, await one URL
read, compare the full href to the fixed public token-page URL, and throw on
mismatch. There is no second press, alternate key, click, or fallback.

These checks prove target ownership/cardinality and postpress URL equality;
they do not remedy V21-001's pre-action default-submit gap.

### Candidate settle, terminal snapshot, and V4 completeness

The inherited candidate locator remains scoped to section `tbody tr`, excludes
the two exact V4 empty-marker texts with `hasNotText`, and requires
`visible: true`. Prefill count remains exactly five. The lazy `.first()` hidden
wait therefore completes only when no currently visible non-empty candidate
row remains.

After settle, the unchanged synchronous terminal snapshot still requires
exact query input value/count, the V15 depth/table/search/body structure, zero
grid/pagination/busy state, one exact visible V4 empty marker, zero visible
candidate and matching rows, and one of the three exact row variants. The
later checks still require one actionable global `Create Token` and zero exact
target-name/role-row/evaluator matches.

### Synchronous fixed-key output

The three evaluator callbacks (baseline, postfill query, terminal) remain
synchronous and read-only. There is zero asynchronous evaluator,
`MutationObserver`, page timer, page `Promise`, expando, polling loop, or
cross-evaluate page state.

Baseline, query, and terminal results still pass the pinned cross-realm
plain-record rule, exact-key schemas, and same-read boolean/integer projection.
Output remains fixed result/cleanup strings, sanitized error class, booleans,
bounded integers, trusted records, local counters, and fixed-equality
predecessor fields. No raw page text, URL, ID, title, attribute, DOM, HTML,
screenshot, token, credential, secret, or clipboard content is emitted.

### Call cardinality and cleanup

Static call-site counts are:

- one each: `tabs.new`, fixed `goto`, fill, Enter press, candidate `.first()`,
  exact-handle close, and terminal write;
- two URL reads: initial navigation confirmation and immediate post-Enter
  equality check;
- two waits: initial visible input and candidate-set hidden;
- three synchronous evaluator calls and eight locator counts; and
- zero click, selected/list/get, connect/reconnect, detach, screenshot,
  clipboard, Create/edit/delete, retry, or fallback call site.

The one created handle is chained into local and durable bindings before every
later await. Success retains only that exact handle. Every non-PASS branch
otherwise preserves the inherited fail-closed cleanup: rejected/no-handle
creation reports residue unproven; malformed objects are retained ineligible;
exact close clears only after settlement; close rejection retains the exact
handle; and precreation failure is clean. This cleanup cannot reverse the
possible external effect in V21-001.

### Secrets and confirmations

Executable scans find zero Bearer value, JWT form, or 40-plus-hex secret. The
mandatory final Create/native Copy/native masked Paste confirmation and later
separate exact-row deletion confirmation remain explicit and unreached. No
credential, clipboard, VM, DNS, routing, listener, or process action exists.

## Finding counts and residual limits

- Critical: `0`.
- HIGH: `1` unresolved (`V21-001`).
- IMPORTANT: `0`.
- Minor: the committed Markdown contains one extra blank line at EOF;
  `git diff-tree --check` reports it at line 778. It is outside the executable
  and does not affect the HIGH verdict.

This review proves only the committed static contract and does not authorize
execution. No classification or post-commit tuple can override V21-001.

## Final verdict

**FAIL**

Unresolved findings: Critical `0`, HIGH `1`, IMPORTANT `0`, Minor `1`.

`authorizes_live_execution=false`
