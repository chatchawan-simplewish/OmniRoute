# OmniRoute V24 dashboard-home route-shape diagnostic — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only commit
`b5a3bbb34813da373e5d26c28d9337d6cacede06` and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-dashboard-home-v24-route-shape-diagnostic-brief.md`.
Its direct parent is the consumed V23 prestart incident commit
`e9b4f0b7cd6eefb2c65ad63dd7898346c29ddb21`.

I independently reviewed direct committed bytes, syntax, the exact V23
consumed/failed-clean predecessor, the new one-shot state, one-call
cardinalities, fixed route-shape projection, output leakage, acceptance of zero
candidates, exact-handle cleanup/residue truth, secret/provider exclusions,
no-retry semantics, and both mandatory manual confirmation boundaries.

I performed no Chrome, Node browser binding, provider, clipboard, credential,
process, network, DNS, routing, Prox-01, or VM action and did not evaluate the
V24 cell. The only workspace write is this assigned review artifact.

## Final verdict

**FAIL** — one unresolved IMPORTANT finding. The exact-key/range validator
allows the `-1` sentinel for all route/action counts, but completeness checks
only five of the sixteen integer fields for nonnegative values. A malformed
snapshot with unknown `-1` candidate counts can therefore be accepted as a
complete PASS even though the diagnostic intends to accept actual zero counts,
not unknown sentinels.

`authorizes_live_execution=false`

## Direct-byte, syntax, and Git evidence

- Reviewed commit: `b5a3bbb34813da373e5d26c28d9337d6cacede06`.
- Direct parent: `e9b4f0b7cd6eefb2c65ad63dd7898346c29ddb21`.
- The reviewed commit adds exactly the assigned V24 brief path.
- V24 brief: `13900` bytes, SHA-256
  `667D450CA1859714D9B0B6D693AA07B0F10FBCB3A65469E90F208001637F9878`,
  Git blob `3d3dd6a3156124c55b884fa8cec151f8a4e3de19`.
- Executable payload: `11340` bytes, SHA-256
  `988AD0CD0966AB15C26A4119EE3697AFD678F87693DD6454F1D2282D2238004E`.
- Encoding is UTF-8 without BOM and LF-only with zero CR bytes. There is one
  `javascript` fence and no extra blank line at EOF.
- Non-evaluating top-level-awaited JavaScript parse: **PASS**. The outer IIFE
  is awaited exactly once.
- `git diff-tree --check` reports no whitespace error.
- Index before review creation: zero paths. The exact inherited twelve-path
  dirty baseline was present and remained unstaged.

## Consumed V23 incident boundary

The direct-parent incident is a one-path commit containing
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-prestart-reads-v23-live-incident.md`.
Its committed/local pins reproduce as `2956` bytes, SHA-256
`3732D7C7531CA66FC84191489B32ECE6847F9E9B32F9CEF6DFD1CA305E559E83`,
and blob `6fdff384082f204e0f7a50992c2b36a88b32f7b7`.

The incident binds V23 prestart brief
`e3c9aff865ec6d9200b02325050908b40ab9f90b`, PASS review
`1fb949d6aa5306e39d0d211ce4fae8787da3775a`, and classification
`50a3ce4b3a445f2bc8d8ba4cb00260ef631ced9b`. It proves:

- the V23 readiness gate remained consumed PASS;
- the V23 prestart-read gate was consumed exactly once;
- only its first dashboard-home navigation fulfilled;
- the first exact `mysw.me` anchor count failed before any click, wait, or fill;
- exact-handle close fulfilled;
- the V23 binding became null/ineligible in exact state
  `CLOUDFLARE_PRESTART_READS_FAILED_CLEAN_V23`;
- residue converged and no provider-persistent or secret action occurred.

V24 requires that exact persistent tuple, both detach flags false, and V21/V22
readiness declarations absent. It neither invokes nor reuses the V23 gate or
handle. This is a fresh-tab diagnostic for the obsolete home-route assumption,
not a retry or continuation.

## One-shot, target, and cardinality checks

The V24 consumed flag is set synchronously before the first await. Exact
predecessor validation precedes the sole chained assignment of the new result
into local and durable V24 bindings. The created handle is retained durably
before every later await, ownership is exact, and shape requires `goto`, `url`,
`close`, and locator support.

Static executable call-site counts are exact:

- one `tabs.new`;
- one fixed `goto("https://dash.cloudflare.com")`;
- one URL read;
- one first-visible-anchor wait with `20000 ms` timeout;
- one synchronous body evaluator;
- one exact local-handle close;
- one terminal write; and
- zero click, fill, press, submit, selected/list/get, reconnect, alternate tab,
  clipboard, screenshot, Create/edit/delete, retry, fallback,
  `MutationObserver`, page timer, or page Promise call site.

The post-navigation check accepts only HTTPS `dash.cloudflare.com`. The body
snapshot maps hrefs to local path strings only when they remain HTTPS and on
that exact host. No path or identifier is emitted.

## V24-001 — IMPORTANT: unknown `-1` candidate counts can satisfy snapshot completeness

`emptySnapshot()` correctly uses `-1` to distinguish an unobserved integer
field from an observed zero. The cross-realm `trustedSnapshot()` validator,
however, permits every integer in the full range `-1..1000000`.

After validation, `snapshotComplete` requires only:

- exact host true;
- total anchors greater than zero;
- visible anchors greater than zero; and
- `mainCount`, `navigationCount`, and `busyCount` nonnegative.

It does **not** require nonnegative values for these eleven candidate fields:

- `exactZoneTextAnchorCount`;
- `containsZoneTextAnchorCount`;
- `exactZoneHrefCount`;
- `nestedZoneHrefCount`;
- `accountRootHrefCount`;
- `accountHomeHrefCount`;
- `accountDomainsHrefCount`;
- `websitesActionCount`;
- `domainsActionCount`;
- `overviewActionCount`; and
- `accountActionCount`.

The route booleans intentionally may all be false, and actual candidate counts
intentionally may all be zero. Those are useful diagnostic outcomes. But `-1`
means the candidate was not measured; it is not equivalent to a measured zero.
Because the validator is explicitly the boundary for an untrusted cross-realm
result, the callback's expected use of DOM `.length` does not justify allowing
the sentinel to pass the completeness predicate. An exact-key plain object can
carry `-1` for all eleven fields and still produce
`EXACT_V24_DASHBOARD_ROUTE_SHAPE_DIAGNOSTIC_PASS`, state
`V24_DIAGNOSTIC_PASS_CLEAN`, and a nominal complete snapshot.

That false PASS can misdirect the separately reviewed replacement that is
supposed to consume these counts. It does not expose a secret or directly
mutate the provider, so the finding is IMPORTANT rather than HIGH.

### Required correction

Before setting `snapshotComplete`, require every member of `integerKeys` to be
nonnegative after trusted projection, while retaining the existing upper
bound. This continues to accept zero for every route/action candidate and
rejects only the unknown sentinel. Re-review the corrected exact bytes; do not
execute this reviewed V24 gate.

## Closed checks outside V24-001

### Fixed-key projection and no leakage

The synchronous callback returns five route/host booleans and sixteen integer
counts under a fixed exact-key schema. `plainRecord` implements the pinned
cross-realm direct-null-or-prototype-parent-null rule. Boolean types and safe
integer range are checked before a fresh local projection is stored. No
untrusted key is spread or emitted.

The evaluator retains raw hrefs, resolved paths, anchor/action text, and DOM
nodes only inside page scope. Terminal output contains a fixed result, fixed
state/cleanup strings, sanitized error class, booleans, bounded integers,
counters, and the validated projected record. It emits no URL, path,
account/zone ID, text, href, title, attribute, DOM, HTML, screenshot, provider
response, credential, token, secret, or clipboard value.

V24-001 concerns completeness acceptance, not raw leakage: even the incorrectly
accepted sentinel remains a fixed numeric value.

### Cleanup and residue truth

The fresh handle is chained into the durable V24 binding before later awaits.
If it is captured and close-capable, every body disposition attempts exactly
one close on that exact local handle. A fulfilled close clears the durable
binding only afterward and records PASS-clean or failed-clean according to the
body result. A rejected close retains the exact handle, forces non-PASS, and
reports unconverged residue.

Precreation failure reports no tab created. Rejected/uncertain creation,
fulfilled-without-handle, or malformed-without-close paths do not claim clean;
they preserve the durable value and report residue unproven. There is no
selected/list/get/reconnect fallback or alternative cleanup handle.

### Secrets, provider mutation, and confirmations

Executable scans find no Bearer value, JWT-like value, forty-plus-character
hex secret, credential read, clipboard call, or screenshot. The only browser
effects are a fresh tab, fixed public navigation, read-only wait/snapshot, and
exact-tab close. There is no click, fill, press, submit, Create, edit, delete,
DNS/provider write, VM, routing, listener, or process action.

Any PASS or non-PASS spends V24. No retry, fallback, continuation,
reinterpretation, manual integration, verdict relaxation, or tab discovery is
permitted. The mandatory final Create/native Copy/native masked Paste
confirmation and later separate exact-row deletion confirmation remain
unreached and mandatory.

## Finding counts and limits

- Critical: `0`.
- HIGH: `0`.
- IMPORTANT: `1` unresolved (`V24-001`).
- Minor: `0`.

This static review does not authorize execution. No classification or
post-commit tuple may override V24-001.

## Final verdict

**FAIL**

Unresolved findings: Critical `0`, HIGH `0`, IMPORTANT `1`, Minor `0`.

`authorizes_live_execution=false`
