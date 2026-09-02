# OmniRoute V28 Domains-action shape diagnostic fix 1 — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only commit
`cf062d27fac8d7912cfea32ea32414302f482172` and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-dashboard-home-v28-domains-action-shape-diagnostic-brief.md`.
Its direct parent is initial FAIL review commit
`20e7795247f575cc87fcedca131feb83f8a892bb`.

I independently reviewed the direct committed bytes, syntax, closure of
IMPORTANT `V28-001`, the complete V23/V26/V27 predecessor and three-attempt
architecture stop, diagnostic-only projection, output non-leakage, zero
activation, exact-handle cleanup, cardinality, no-mutation/no-retry semantics,
secret exclusions, and both mandatory manual confirmation boundaries.

I performed no Chrome, browser binding, provider, clipboard, credential,
network, DNS, routing, process, Prox-01, or VM action and did not evaluate the
V28 cell. The only workspace write is this assigned review artifact.

## Final verdict

**PASS** — `V28-001` is fully closed and there are no unresolved Critical,
HIGH, or IMPORTANT findings.

`authorizes_live_execution=false`

## Direct-byte, syntax, and Git evidence

- Reviewed commit: `cf062d27fac8d7912cfea32ea32414302f482172`.
- Direct parent: `20e7795247f575cc87fcedca131feb83f8a892bb`.
- The reviewed commit modifies exactly the assigned V28 brief path.
- Brief: `20642` bytes, SHA-256
  `313994D8C9C69E5DDE511E0641D3FF5D969C5D1A82188C467A1D311E8BC029AD`,
  Git blob `c3be9488cb3097d46bd8d572d2f0facaa2059016`.
- Normalized executable: `17125` UTF-8 bytes, SHA-256
  `AD92BA14844D1F015720EC68DE0F794A2F85F1CD09D775C940616B2101E4DFAD`.
- Encoding is UTF-8 without BOM and LF-only. Non-evaluating Acorn module parse
  with top-level await: **PASS**.
- Three V28 persistent declarations are present exactly once.
- `git diff-tree --check` reports no whitespace error.
- Before review creation, the index held zero paths and the exact inherited
  twelve-path dirty baseline was present and unstaged.

## V28-001 closure — exact detach-state predecessor

The corrected declaration predicate now explicitly type-checks all six
persistent detach fields as booleans:

- V23 pre-create and post-native detach consumed;
- V26 pre-create and post-native detach consumed; and
- V27 pre-create and post-native detach consumed.

The predecessor predicate separately requires every one of those six fields to
equal `false`. Static counts reproduce exactly six detach `typeof` checks and
six detach false-value checks, with each named field appearing in both sets.

This restores the exact V23/V26/V27 incident history: no intervening native
detach or handoff state can satisfy V28's three-attempt diagnostic boundary.
The correction is fail-closed and occurs before the sole new-tab attempt. The
commit diff changes no diagnostic evaluator, output, activation, cleanup, or
call-cardinality behavior. `V28-001` is fully closed.

## Rechecked inherited contract

### Exact predecessor and architecture stop

V28 is consumed before its first await and requires V23 readiness/prestart
reads consumed with null/ineligible failed-clean tab state, all V24 diagnostic
declarations absent, V25 consumed PASS-clean with no retained tab, V26 consumed
failed-clean/ineligible with reads unused, and V27 consumed failed-clean/
ineligible with reads unused. The new six false detach checks complete that
state. All three V28 declarations must be fresh.

V28 makes no fourth activation guess. It reproduces only the proven fixed-home
navigation, host-only initial URL check, one bounded first-visible-anchor wait,
settled account-home URL check, and one synchronous read-only body snapshot.
It always proceeds to exact-tab cleanup.

### Fixed-key diagnostic completeness and account-local checks

The snapshot retains exact equality over 26 boolean and 17 integer keys. The
pinned cross-realm rule accepts only a direct null prototype or a prototype
whose parent is null. Every boolean is explicitly typed; every integer is safe,
nonnegative, and bounded to `1000000`. Only those fixed keys enter a new trusted
controller-local projection.

The structural booleans cover tag, role, href presence and same-host/
same-original-account Domains route, native-click presence, disabled/ARIA/
inert shape, rectangle/viewport/center hit, pointer events, target/download,
ARIA-controls, data-href, and tab-stop shape. The inherited semantic signature
also proves exact account-home route, complete anchor/route/action/structure
counts, one Domains action, one visible Domains action, and no busy marker.

The settled account segment is passed inward only for fixed equality and is not
returned. Raw tag, role, href, ID, URL, path, account/zone identifier, text,
DOM, HTML, style, and attribute values remain local.

### Output, activation, and mutation boundary

Terminal output contains only fixed result/state/cleanup strings, sanitized
error class, booleans, bounded counts, counters, consumed state, and the
validated fixed-key snapshot. No raw untrusted key or value, identifier,
content, provider response, credential, token, secret, clipboard value, or
screenshot is emitted.

Static call sites reproduce exactly: `tabs.new` 1, fixed `goto` 1, URL reads 2,
wait 1, evaluator 1, exact-handle close 1, and terminal write 1. Click/fill/
press are `0 / 0 / 0`; selected/list/get discovery, clipboard, and fetch are
also zero. There is no native click invocation, submit, keyboard event,
listener, Create/edit/delete, DNS/rate/Tunnel/Access/API-token/permission,
provider-persistent, process, routing, VM, reconnect, retry, fallback, or
alternate-tab action.

### Exact-handle cleanup and no retry

The sole new-tab result is chained into local and durable V28 bindings before
every later await. Every outcome, including diagnostic PASS, must close that
exact handle. The durable binding clears only after close fulfillment. Close
rejection retains the exact handle, forces non-PASS, and reports unconverged
residue. Rejected/uncertain creation and malformed/no-handle outcomes cannot be
reported clean; only genuine precreation failure is clean.

There is no discovery, reacquisition, continuation, reinterpretation, manual
integration, retry, fallback, alternate activation, or verdict relaxation.
The final Create/native Copy/native masked Paste confirmation and later
separate exact-row deletion confirmation remain explicit, unreached, and
mandatory.

## Finding counts and limits

- Critical: `0`.
- HIGH: `0`.
- IMPORTANT: `0` (`V28-001` closed).
- Minor: `0`.

This static PASS does not authorize live execution. A later non-self-referential
classification and fresh action-time pins remain required by the brief.

## Final verdict

**PASS**

Unresolved findings: Critical `0`, HIGH `0`, IMPORTANT `0`, Minor `0`.

`authorizes_live_execution=false`
