# OmniRoute V27 settled-home Domains-route reacquisition — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only commit
`2c84d6a23e321b1ffc9851358f90cc46b6eef899` and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-dashboard-home-v27-settled-domains-route-reacquisition-brief.md`.
Its direct parent is initial V27 commit
`557888b3e69893e2255f1a66520aeb9cb0dacb28`, whose direct parent is consumed
V26 failed-clean incident commit
`04bc5e467caa057ab44ea49935a6b66c8e87a1b2`.

I independently reviewed direct committed bytes, syntax, the V26 timing
diagnosis and V27 settle correction, exact V23/V25/V26/V24 predecessor state,
same-account route binding, inherited V25 semantic completeness, fixed call
bounds and output, exact-handle retention/cleanup, secret/provider exclusions,
no-retry semantics, and both mandatory manual confirmation boundaries.

I performed no Chrome, browser binding, provider, clipboard, credential,
network, DNS, routing, process, Prox-01, or VM action and did not evaluate the
V27 cell. The only workspace write is this assigned review artifact.

## Final verdict

**PASS** — no unresolved Critical, HIGH, or IMPORTANT finding.

`authorizes_live_execution=false`

## Direct-byte, syntax, and Git evidence

- Reviewed commit: `2c84d6a23e321b1ffc9851358f90cc46b6eef899`.
- Direct parent: `557888b3e69893e2255f1a66520aeb9cb0dacb28`.
- The reviewed commit modifies exactly the assigned V27 brief, correcting only
  the incident commit pin from an invalid hash to the exact committed hash.
- Brief: `22748` bytes, SHA-256
  `85DEB41D561B79D63939A38FD2A9E0509F4AF52108870C38D4FC9EE344C2F423`,
  Git blob `08fba2f841a9fc4a5bae0909c5ca487e93f809eb`.
- Normalized executable: `18432` UTF-8 bytes, SHA-256
  `8C929CC532186B34B3B3FAF67E370ACCFEC5EE825E652BED90F6F70E355440B2`.
- Encoding is UTF-8 without BOM and LF-only. Non-evaluating Acorn module parse
  with top-level await: **PASS**.
- Seven V27 persistent declarations are present exactly once.
- Before review creation, the index held zero paths and the exact inherited
  twelve-path dirty baseline was present and unstaged.

## V26 root cause and V27 settle correction

The V26 incident records an exact consumed failed-clean result: new tab,
fixed-home navigation, and first URL read each completed `1 / 1`; the immediate
account-home path check failed before the visible-anchor wait, snapshot, click,
or any provider action. Exact close completed `1 / 1`, residue converged, no
handle remained, and state became `V26_ROUTE_FAILED_CLEAN`.

V27 preserves the fixed navigation and first URL read but deliberately restricts
that immediate check to exact HTTPS Cloudflare host. It then waits once, for at
most 20 seconds, on the existing dynamic first-visible-`a[href]` condition that
preceded V25's proven home snapshot. Only after that wait fulfills does a
distinct second URL read parse exact `/([0-9a-f]{32})/home/?` and retain the
account segment. The sequence is statically exact: navigation, initial host URL
check, visible-anchor wait, settled URL read/account bind, snapshot, then click.

The second path check is still before the snapshot and sole click. Therefore a
prematurely fulfilled condition or an unsettled/wrong route fails closed without
clicking. The subsequent snapshot independently requires the exact account-home
shape and no busy marker. This is a condition-based bounded settle, not a sleep,
retry, polling loop, fallback, or relaxed verdict.

## Predecessor and one-shot boundary

The V27 gate is marked consumed before the first await. Its exact predecessor
requires:

- V23 readiness and prestart reads consumed, V23 tab null/ineligible, exact
  `CLOUDFLARE_PRESTART_READS_FAILED_CLEAN_V23`, and both detach flags false;
- all V24 diagnostic declarations absent;
- V25 diagnostic consumed PASS-clean with no retained tab;
- V26 route consumed failed-clean, no retained tab, ineligible, both V26 detach
  flags false, and V26 downstream reads unconsumed; and
- all seven V27 declarations in their fresh states.

No V23, V25, or V26 gate is invoked, reset, retried, reinterpreted, continued,
or reused. Any V27 non-PASS permanently spends V27.

## Same-account and semantic completeness

The controller-local account segment comes only from the settled pre-click home
URL. After the guarded Domains click, the current URL must be exact
`/[same account]/home/domains`. The exact visible `mysw.me` anchor href and the
final zone URL must each independently be exact `https://dash.cloudflare.com`
routes carrying that same original segment. No post-click route can redefine
the account authority.

V27 otherwise preserves the V25/V26 fixed-key body snapshot unchanged: five
explicit booleans and sixteen nonnegative safe integers bounded to
`0..1000000`, accepted only through the pinned cross-realm plain-record rule,
exact sorted key equality, type checks, and trusted fixed-key projection.

Acceptance requires the exact account-home route, other current-path shapes
false, positive total and visible anchors, zero exact/containing zone text,
zero exact/nested zone href, exactly one normalized Domains action, and zero
busy marker. The separate exact-text visible Domains locator must count one and
be visible before its sole click. The exact-text visible zone anchor waits
boundedly and must count one before href read; the final visible exact zone
marker also waits boundedly and must count one.

## Cardinality, output, and mutation boundary

Static call sites reproduce exactly:

- V27 declarations `7`;
- `tabs.new` `1`, fixed/validated `goto` `2`, URL reads `4`;
- waits `3` total, including exactly one first-visible-anchor settle wait;
- body evaluator `1`, Domains click `1`, failure-only close `1`, terminal write
  `1`; and
- fill `0`, press `0`, selected/list/get discovery `0`, clipboard `0`, and
  network fetch `0`.

The sole click is the reviewed read-only Domains navigation guarded by exact
total and visible cardinality. There is no Create, edit, delete, submit,
DNS/rate/Tunnel/Access/API-token/permission, provider-persistent, listener,
process, routing, VM, retry, fallback, reconnect, or alternate-tab action.

Raw home/settled/Domains/final URLs, zone href, account segment, page paths,
anchor/action text, DOM, HTML, attributes, and untrusted snapshot remain local.
Terminal output contains only fixed result/state/cleanup strings, sanitized
error class, booleans, bounded counts, counters, and consumed/detach flags. No
identifier, URL, href, provider response, credential, token, secret, clipboard
value, screenshot, or raw untrusted record is emitted.

## Success retention and failure cleanup

The sole new-tab result is chained into the local and durable V27 bindings
before every later await. Exact PASS retains only that handle, marks exact
`ZONE_ROUTE_READY_ELIGIBLE_V27`, and leaves the downstream read and both detach
gates unused.

Every non-PASS makes the handle ineligible. A close-capable exact handle is
closed once and the durable binding clears only after fulfilled close. Close
rejection retains that exact handle and reports unconverged residue. Rejected,
uncertain, malformed, or no-handle creation cannot be reported clean; only a
genuine precreation failure is clean. There is no discovery, reacquisition,
retry, fallback, continuation, reinterpretation, manual integration, or verdict
relaxation.

The mandatory final Create/native Copy/native masked Paste confirmation and the
later separate exact-row deletion confirmation remain explicit, unreached, and
mandatory.

## Finding counts and limits

- Critical: `0`.
- HIGH: `0`.
- IMPORTANT: `0`.
- Minor: `0`.

This static PASS does not authorize live execution. A later non-self-referential
classification and fresh action-time pins remain required by the brief.

## Final verdict

**PASS**

Unresolved findings: Critical `0`, HIGH `0`, IMPORTANT `0`, Minor `0`.

`authorizes_live_execution=false`
