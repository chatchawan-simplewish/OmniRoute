# OmniRoute V26 Domains-route reacquisition — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only commit
`f54ffbe95d5ea0abe8b70b7b9306d24446c0eac1` and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-dashboard-home-v26-domains-route-reacquisition-brief.md`.
Its direct parent is V25 live report commit
`01a5977398cf5d653e1bfe81a76cd6cb32439454`.

I independently reviewed direct committed bytes, syntax, exact V23/V25/V24
predecessor state, inherited V25 snapshot validation/completeness, Domains and
zone action cardinalities, home-to-Domains-to-zone account binding, static call
bounds, fixed output/no identifier leakage, success retention, failure cleanup,
secret/provider exclusions, no-retry semantics, and both mandatory manual
confirmation boundaries.

I performed no Chrome, Node browser binding, provider, clipboard, credential,
process, network, DNS, routing, Prox-01, or VM action and did not evaluate the
V26 cell. The only workspace write is this assigned review artifact.

## Final verdict

**FAIL** — one unresolved HIGH finding. V26 validates that the post-click
Domains route, zone href, and final zone route all share one account segment,
but never binds that segment to the account segment in the V25-confirmed home
URL. A unique Domains action that navigates to a different account can therefore
pass and retain an eligible tab in the wrong account.

`authorizes_live_execution=false`

## Direct-byte, syntax, and Git evidence

- Reviewed commit: `f54ffbe95d5ea0abe8b70b7b9306d24446c0eac1`.
- Direct parent: `01a5977398cf5d653e1bfe81a76cd6cb32439454`.
- The reviewed commit adds exactly the assigned V26 brief path.
- Brief: `20492` bytes, SHA-256
  `379C7AB7F8C3A78B944461012AF39C644A3AA89EE1729EC8237F75F33E07D6DA`,
  Git blob `40191801fa7c6fa6f6a4f80ad137764cbd2b43be`.
- Normalized executable payload: `17165` UTF-8 bytes, SHA-256
  `40D81B3906D49F02D752958C54DFEB37F6E7DFEFF9853A42A3B3EA5BE92303FC`.
- Encoding is UTF-8 without BOM and LF-only with zero CR bytes. There is one
  `javascript` fence and no extra blank line at EOF.
- Non-evaluating top-level-awaited JavaScript parse: **PASS**.
- Seven V26 persistent declarations are present exactly once.
- `git diff-tree --check` reports no whitespace error.
- Index before review creation: zero paths. The exact inherited twelve-path
  dirty baseline was present and remained unstaged.

## Predecessor evidence

The direct-parent V25 report is a one-path commit containing
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-dashboard-home-v25-route-shape-diagnostic-live-report.md`.
Its committed/local pins reproduce as `2423` bytes, SHA-256
`D10333193500BCCC4C1464F919547FB5F5C324874C48A107D2AD0C7EFB1CCE90`,
and blob `a0e0a11e319b6438a9c31d43d7287228db1a0d5e`.

That report proves V25 consumed PASS-clean with no retained handle, exact home
host and account-home path, absent direct zone anchor/href, exactly one Domains
action, exact one-call diagnostic cardinalities, and no provider-persistent
action. Its authority chain pins V25 brief
`22e005d7789559b4d2990e79109b0497da367c73`, PASS review
`24a87912ef4fb15a100be5d048b588c222bd6899`, and classification
`1488fa684532a62e1664dddec33ef249a06cd99d`.

V26 requires:

- V23 readiness and prestart-read gates consumed;
- the V23 tab null/ineligible in exact state
  `CLOUDFLARE_PRESTART_READS_FAILED_CLEAN_V23`;
- both V23 detach flags false;
- all three V24 declarations absent;
- V25 diagnostic consumed, retained tab null, and exact state
  `V25_DIAGNOSTIC_PASS_CLEAN`;
- all seven fresh V26 declarations in their unused states.

No V23 or V25 gate is invoked, reset, continued, reinterpreted, or retried.
V24 remains static failed-review evidence only.

## V26-001 — HIGH: post-click account is not bound to the home account

After the fixed home navigation, V26 reads `homeUrl` and checks only protocol
and hostname. The inherited snapshot separately proves that the current path
has the shape `/[32-hex]/home`, but returns only the boolean
`accountHomePath`; it intentionally does not return the account identifier.
The controller never parses or retains the 32-hex account segment from
`homeUrl.pathname`.

After clicking the unique visible Domains action, V26 parses the current path
as `/([32-hex])/home/domains` and defines that newly observed value as
`accountSegment`. It then correctly requires both the visible `mysw.me` href
and the final `/[account]/mysw.me` URL to carry that same post-click segment.
This proves internal consistency only from Domains onward.

There is no comparison between:

- the account segment in the original V25-confirmed account-home URL; and
- the account segment produced by the Domains click.

Static inspection confirms `homeUrl.pathname` is never parsed and no
home-account-to-`domainsPath[1]` comparison exists. Thus a stale, misrouted, or
otherwise wrong-account Domains action can navigate to a different account;
if that account contains one visible `mysw.me` anchor with a self-consistent
route, every remaining predicate passes. V26 then retains that exact tab as
eligible for downstream Cloudflare reads in the wrong account.

The current gate is read-only and does not itself persist a provider mutation,
but wrong-account eligibility can direct later security-sensitive inventory and
creation work at the wrong tenant boundary. This is HIGH.

### Required correction

Before the click, parse the original `homeUrl.pathname` with exact
`^/([0-9a-f]{32})/home/?$`, retain that segment only in controller-local state,
and require the post-click Domains segment to equal it. Continue requiring the
zone href and final zone URL to equal that original segment. Emit only fixed
equality booleans, never the account identifier. Re-review the corrected exact
bytes before any live call.

## Closed checks outside V26-001

### V25 snapshot semantics and completeness

V26 reproduces V25's complete fixed-key body snapshot:

- five host/path booleans;
- sixteen route/action/structure counts;
- the pinned cross-realm direct-null-or-prototype-parent-null record rule;
- exact key equality, explicit boolean types, and safe integers restricted to
  the measured range `0..1000000`.

The acceptance signature requires exact Cloudflare host, account-home true,
other current-path booleans false, positive total/visible anchors, zero exact or
containing zone-text anchors, zero exact or nested zone hrefs, exactly one
Domains action, and zero busy markers. This preserves V25's semantic and
all-integer completeness boundary while selecting the exact live facts needed
for reacquisition. No unknown `-1` sentinel can enter the trusted snapshot.

The snapshot and subsequent locator jointly prove exactly one total normalized
Domains action and exactly one visible matching action. The zone locator is
exact-text and visible, waits boundedly, and must count exactly one before its
href is read. The final exact-text visible zone marker must also count exactly
one.

### Static call bounds

The supplied static cardinalities reproduce exactly:

- `tabs.new`: `1`;
- fixed `goto`: `2` — dashboard home and the validated zone URL;
- URL reads: `3` — home, post-Domains, and final zone;
- Domains click: `1`;
- exact-handle close: `1` call site, failure-only;
- terminal write: `1`;
- synchronous body evaluator: `1`;
- bounded waits: first visible anchor, visible zone anchor, and visible final
  zone marker; and
- zero fill, press, submit, selected/list/get, reconnect, alternate tab,
  clipboard, screenshot, Create/edit/delete, DNS/rate/Tunnel/Access/token
  action, retry, or fallback call site.

The sole click is guarded by exact total count one, exact visible count one, and
an exact normalized `Domains` label. It is followed immediately by exact HTTPS
host/path validation. V26-001 concerns missing prior-account equality, not click
cardinality.

### Fixed output and no identifier/secret leakage

Raw home/Domains/final URLs, the zone href, account segments, anchor/action
text, DOM nodes, and page paths remain controller/page local. Terminal output
contains only fixed result/state/cleanup strings, sanitized error class,
booleans, bounded counts, counters, and fixed consumed/detach flags. It does not
emit the home snapshot object, account or zone identifier, URL, href, path,
text, DOM, HTML, screenshot, response, credential, token, secret, or clipboard
value.

Executable scans find no Bearer value, JWT-like value, forty-plus-character
hex secret, credential read, clipboard call, or screenshot. There is no
provider-persistent, DNS, permission, Create, edit, delete, VM, routing,
listener, or process action.

### Success retention, failure cleanup, and no retry

The sole new-tab result is chained into local and durable V26 bindings before
every later await. Exact PASS marks and retains only that handle, leaves reads
and both detach flags false, and records `ZONE_ROUTE_READY_ELIGIBLE_V26`.

Any non-PASS makes the handle ineligible. A captured close-capable handle is
closed exactly once; the durable binding clears only after fulfilled close.
Close rejection retains the exact handle and reports unconverged residue.
Rejected/uncertain creation or malformed/no-handle outcomes report residue
unproven rather than clean. Genuine precreation failure is clean. There is no
reacquisition, discovery, alternate handle, retry, fallback, continuation,
reinterpretation, manual integration, or verdict relaxation.

The mandatory final Create/native Copy/native masked Paste confirmation and
later separate exact-row deletion confirmation remain explicit, unreached, and
mandatory.

## Finding counts and limits

- Critical: `0`.
- HIGH: `1` unresolved (`V26-001`).
- IMPORTANT: `0`.
- Minor: `0`.

This static review does not authorize execution. No classification or
post-commit tuple may override V26-001.

## Final verdict

**FAIL**

Unresolved findings: Critical `0`, HIGH `1`, IMPORTANT `0`, Minor `0`.

`authorizes_live_execution=false`
