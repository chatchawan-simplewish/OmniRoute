# OmniRoute V33 zone-route outer-locator signature fix round 1 — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only corrected brief commit
`57ce295eabcfef389854ca5915b63ed622c56262` and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-zone-route-v33-outer-locator-signature-brief.md`.
Its direct parent is the initial independent Sol High FAIL review commit
`cbe78d95ead42f9585b1d13430f604e95f093ee3`.

I independently reviewed the corrected committed bytes against findings
`V33-001` through `V33-004`, the exact V32 failed-clean predecessor, full
one-shot lifecycle, exact method and counter cardinality, route and locator
semantics, untrusted count handling, fixed output, exact-handle cleanup,
no-residue/no-retry rules, secret exclusions, and both mandatory later
confirmation boundaries.

I performed no Node, Chrome, browser-binding, provider, clipboard, credential,
network, DNS, routing, process, Prox-01, or VM action and did not evaluate the
V33 cell. The only workspace write is this assigned review artifact.

## Final verdict

**PASS** — `V33-001`, `V33-002`, `V33-003`, and `V33-004` are closed, with no
unresolved Critical, HIGH, IMPORTANT, or Minor finding.

`authorizes_live_execution=false`

## Direct-byte and Git evidence

- Reviewed commit: `57ce295eabcfef389854ca5915b63ed622c56262`.
- Direct parent: `cbe78d95ead42f9585b1d13430f604e95f093ee3`.
- The reviewed commit modifies exactly the assigned V33 brief path.
- Corrected brief: `26762` bytes, SHA-256
  `CC2F04EDAD35736145107FD53072F5319C45CBABEEE28BA348340721D2878370`,
  Git blob `3243ca05c602d7d490feca0254143f804425a917`.
- Normalized executable: `22033` UTF-8 LF bytes, SHA-256
  `C24E1B555186A35703F4395CDDE7AF628360F59D33570D68ED646162BC329DC0`.
- The corrected brief is UTF-8 without BOM and LF-only. The exact executable
  bytes match the supplied pin. Source-level static inspection found no syntax
  contradiction; no Node parse or execution command was run.
- `git diff-tree --check` reports no whitespace error.
- Before review creation, the index held zero paths and the inherited exact
  twelve-path dirty product baseline was present and unstaged.

## V33-001 closure — fresh exact-route bracket and honest evidence ceiling

**Resolved.** The pre-probe settled URL now requires exact `https:` protocol,
exact `dash.cloudflare.com` hostname, empty port, empty username/password, and
the original 32-hex account plus `mysw.me` zone prefix before any outer count.

After all eleven counts, a new `postUrlAttempted/postUrlFulfilled` pair brackets
one fresh `tab.url()` read. That returned URL is privately parsed and must pass
the same protocol, hostname, empty port, empty credentials, and original
account/zone-prefix checks. `routeContinuous` additionally requires exact raw
URL equality with the validated pre-probe settled URL. Any failure remains at
fixed `postStage=POST_URL`, prevents aggregate post-snapshot fulfillment, and
cannot reach the PASS result.

The terminal post-route booleans are now derived from the fresh post-probe
parsed URL rather than the stale pre-probe object. Both `postUrlValidated` and
`routeContinuous` are fixed terminal booleans and mandatory completeness
conditions; `routeContinuous` is also an exact-key trusted post-snapshot field.

The brief no longer claims an atomic page-state snapshot. It explicitly limits
a PASS to endpoint-bracketed exact-URL continuity and sequential outer counts.
This closes the stale-route misattribution while preserving the design's honest
non-atomic ceiling. The raw URLs and account segment remain private and are not
written.

## V33-002 closure — raw candidate semantics and no destination inference

**Resolved.** All three href-derived values, trusted-record keys, and counter
pairs are renamed as raw candidate evidence:

- `rawApiTokensHrefCandidateCount`;
- `rawRelativeProfileApiTokensHrefCandidateCount`; and
- `rawRelativeAccountApiTokensHrefCandidateCount`.

The design section identifies them as raw href-attribute candidate shapes and
describes the profile/account forms as literal relative forms. The evidence
interpretation explicitly states that they are not same-origin pathname
validation and must never be used as destination proof. A positive candidate
can support only a separately reviewed successor that privately reads and
validates one exact destination before navigation. This removes the false
semantic equivalence with V32's normalized same-host path counts without adding
or emitting raw href data.

## V33-003 closure — immediate count validation at the originating stage

**Resolved.** `requireSafeCount` accepts only safe integers in `0..1000000` and
throws a fixed local error otherwise. Each of the eleven outer count results is
checked immediately after its fulfillment counter and before `postStage`
advances or the next probe begins. An unsafe return therefore stops at its
originating fixed stage. The final exact-key `trustedRecord` repeats the same
type/range checks as defense in depth before terminal projection.

No raw or unsafe count can reach terminal output. A count-method rejection
leaves its fulfillment counter at zero; an unsafe fulfilled return leaves that
counter at one but retains the originating stage and prevents every later
probe, aggregate fulfillment, and PASS.

## V33-004 closure — clean committed file ending

**Resolved.** The corrected commit removes the extra blank line at EOF, and
`git diff-tree --check` is clean.

## Exact predecessor, one-shot, cleanup, and security boundaries

V32 remains consumed exactly once at incident commit
`7563e19717d5bf6a8b7ba09f4290167cdf554e53`, with state
`V32_DIAGNOSTIC_FAILED_CLEAN`, close `1 / 1`, converged residue, and no retained
handle. It proves only the unique private observed-href navigation through the
settled zone prefix; it proves no API-token/profile/manage-account signature.

V33 consumes its fresh gate before its first precondition. The exact predecessor
tuple still requires the complete V23 through V32 spent/static state, V24
declarations absent, V31 PASS-clean, V32 failed-clean, no retained predecessor
handle, and all three V33 declarations fresh. No prior gate is reset, continued,
retried, reinterpreted, or relaxed.

The sole new-tab handle is assigned to both durable and local bindings before
later awaits. Every created-handle outcome attempts close on that exact handle.
The durable binding clears only after close fulfillment. Close rejection keeps
the exact handle, forces non-PASS, and reports unconverged residue. Rejected or
uncertain creation and malformed/no-handle outcomes cannot claim clean residue
after a creation attempt.

Terminal output remains fixed to status strings, booleans, bounded trusted
counts, counters, and a sanitized error class. It emits no href, URL, path,
account/zone identifier, page text, DOM, HTML, attribute value, screenshot,
provider response, credential, token, secret, clipboard value, or free-form
exception message.

There is no click, press, fill, Create, Copy, Paste, fetch, clipboard access,
provider mutation, tab listing/discovery/reacquisition, reconnect, retry,
fallback, manual integration, or verdict relaxation. The mandatory final
Create/native Copy/native masked Paste confirmation and later separate exact-row
deletion confirmation remain explicit, unreached, and mandatory.

## Static method and counter cardinality

Static source sites reproduce as:

- V33 persistent declarations: `3`;
- `tabs.new`: `1`; `goto`: `2`; URL reads: `3`;
- bounded network-idle waits: `2`; page evaluator: `1`;
- outer locator counts: `11`; immediate safe-count calls: `11`;
- exact-handle close: `1`; terminal write: `1`;
- click / press / fill: `0 / 0 / 0`;
- tab list / get / selected discovery: `0 / 0 / 0`;
- fetch / clipboard: `0 / 0`.

All twenty-two declared attempted/fulfilled pairs have exactly one increment
site for each member: new, home navigation/wait/URL, pre-snapshot, zone
navigation/wait/URL, post URL, aggregate post-snapshot, eleven individual
counts, and close. `writeAttempted` has one declaration and one increment.

PASS_CLEAN additionally requires the fixed PASS result, every validation and
completeness boolean true, exact route continuity, `postStage=COMPLETE`, every
declared non-cleanup pair `1 / 1`, close `1 / 1`, `EXACT_TAB_CLOSED`, converged
residue, no retained handle, `V33_DIAGNOSTIC_PASS_CLEAN`, consumed true, and
error class `NONE`.

## Finding counts and limits

- Critical: `0`.
- HIGH: `0` (`V33-001` closed).
- IMPORTANT: `0` (`V33-002` and `V33-003` closed).
- Minor: `0` (`V33-004` closed).

This static PASS does not itself authorize live execution. The brief's separate
non-self-referential classification and fresh action-time pins remain required.

## Final verdict

**PASS**

Unresolved findings: Critical `0`, HIGH `0`, IMPORTANT `0`, Minor `0`.

`authorizes_live_execution=false`
