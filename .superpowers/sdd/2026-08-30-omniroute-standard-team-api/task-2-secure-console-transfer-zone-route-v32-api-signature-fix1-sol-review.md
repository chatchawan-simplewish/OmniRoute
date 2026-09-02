# OmniRoute V32 observed zone-route API-signature fix round 1 — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only fixed brief commit
`a55dd20a0b92e26f38b5af0baadfe6864812fd7f` and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-zone-route-v32-api-signature-brief.md`.
Its direct parent is the initial Sol High FAIL review commit
`337f5a6d07d884056df277da99ca03ee8efd4cc1`.

I independently reviewed the fixed direct committed bytes against the initial
V32 brief, unresolved finding `V32-001`, V31 predecessor report, full one-shot
and exact-handle lifecycle, fixed output, provider/secret exclusions, and the
inherited V4 manual-confirmation boundaries.

I performed no Node, Chrome, browser binding, provider, clipboard, credential,
network, DNS, routing, process, Prox-01, or VM action and did not evaluate the
V32 cell. The only workspace write is this assigned review artifact.

## Final verdict

**PASS** — `V32-001` is closed, with no unresolved Critical, HIGH, or
IMPORTANT finding.

`authorizes_live_execution=false`

## Direct-byte and Git evidence

- Reviewed commit: `a55dd20a0b92e26f38b5af0baadfe6864812fd7f`.
- Direct parent: `337f5a6d07d884056df277da99ca03ee8efd4cc1`.
- The reviewed commit modifies exactly the assigned V32 brief path.
- Fixed brief: `21625` bytes, SHA-256
  `60BA0BC5A3A2F65F90CBECDEDD320810F7998AE7D20F8E5C4EAC6BA4474FBEEF`,
  Git blob `3c281118274fc45dbaa5da429a0eae1a6430554f`.
- Normalized executable: `18215` UTF-8 LF bytes, SHA-256
  `8DFA8749AD040359239805E0F6D02E9DFC70BEE792FB2FBAB3A94B7EA204F870`.
- The brief is UTF-8 without BOM and LF-only. The exact executable bytes match
  the supplied syntax-PASS pin; static source inspection found no syntax
  contradiction. Per the explicit boundary, no Node parse command was run.
- `git diff-tree --check` reports no whitespace error.
- Before review creation, the index held zero paths and the exact inherited
  twelve-path dirty baseline was present and unstaged.

The unchanged V31 report evidence remains pinned at commit
`cfb34f1b1ae5dc2efe7d3f664cd539a88607a14c`, `3834` bytes, SHA-256
`F73D45DDACB2C9A2FF3CF6A98027ED726AD166210BC08D86889828E2E31C4778`,
and blob `6336bbeb3dfc6f1b1952dd37e9c04f407e8280bc`.

## V32-001 closure — observed exact href is now the navigation authority

**Resolved.** The pre-snapshot now builds `exactZoneAnchors`, requires exactly
one candidate, and privately returns that exact element's raw `href` alongside
the fixed pre-snapshot fields. Controller code accepts the untrusted result only
when it is a cross-realm plain record with exact expected keys; the observed
href must be a nonempty string of at most 2048 characters and contain no ASCII
control character.

Before the zone-navigation counter advances, the private href is parsed against
the freshly validated account-home URL and must have:

- exact `https:` protocol;
- exact `dash.cloudflare.com` hostname;
- empty explicit port;
- empty username and password; and
- exact original-account `/mysw.me` pathname, with only the reviewed optional
  trailing slash.

The second `goto` receives `observedZoneUrl.href` directly. The URL parser
preserves any observed query and fragment in that absolute href, so there is no
independently synthesized route and no query/fragment loss. No await or other
page interaction occurs between validation and the attempted navigation.

The raw observed href and parsed URL remain controller-local. Before terminal
output, the pre-snapshot is rebuilt through a new fixed-key trusted projection
that excludes `observedZoneHref`; the terminal object also contains neither the
raw href nor `observedZoneUrl.href`. Failure output remains limited to the
sanitized error class and fixed status fields.

These properties close the initial finding's direct-evidence, fresh-href,
complete-validation, destination-equality, and non-emission requirements.

## Full inherited security and one-shot review

- V32 consumes its fresh gate before the first await. The exact predecessor
  tuple still requires V23 failed-clean/null/ineligible, V24 absent, V25
  PASS-clean, V26/V27 failed-clean with unused downstream reads, V28 PASS-clean,
  V29/V30 failed-clean, and V31 consumed PASS-clean with no retained handle.
- The sole new-tab handle is chained into both durable and local bindings before
  any later await. Rejected/uncertain creation and malformed-handle outcomes do
  not claim clean residue. Close rejection retains the exact handle, forces
  non-PASS, and reports unconverged residue. Ownership clears only after exact
  close fulfillment.
- The home navigation remains fixed. The first URL read binds the exact
  Cloudflare host and 32-hex account-home segment. The second read validates the
  settled same-account zone prefix before the post snapshot can proceed.
- Both page snapshots use exact-key cross-realm validation. Every terminal
  boolean is explicitly typed, every counter is a safe integer in
  `0..1000000`, and only fresh trusted fixed-key records are emitted.
- Terminal evidence contains no href, URL, path, account ID, zone identifier,
  raw key, text, DOM, HTML, attribute, screenshot, provider response,
  credential, token, secret, clipboard value, or free-form exception message.
- There is no Create/edit/delete, API-token, DNS, rate-rule, Tunnel, Access,
  permission, routing, listener, process, UI activation, provider-persistent
  mutation, tab discovery/reacquisition, retry, fallback, manual integration,
  or verdict relaxation.
- The mandatory final Create/native Copy/native masked Paste confirmation and
  the later separate exact-row deletion confirmation remain explicit,
  unreached, and mandatory.

## Static and runtime cardinality contract

Static source sites reproduce as:

- V32 declarations: `3`;
- `tabs.new`: `1`; `goto`: `2`; fulfilled URL reads: `2`;
- bounded network-idle waits: `2`; synchronous evaluators: `2`;
- exact-handle close: `1`; terminal write: `1`;
- observed validated href used as the second destination: `1`;
- click/fill/press: `0 / 0 / 0`;
- selected/list/get discovery: `0 / 0 / 0`;
- fetch/clipboard: `0 / 0`;
- raw observed href or parsed href in terminal object: `0`.

PASS_CLEAN additionally requires all declared non-cleanup attempt/fulfillment
pairs `1 / 1`, every validation/completeness boolean true including
`observedZoneUrlValidated`, close `1 / 1`, `EXACT_TAB_CLOSED`, converged
residue, no retained handle, `V32_DIAGNOSTIC_PASS_CLEAN`, consumed true, and
sanitized error class `NONE`.

## Finding counts and limits

- Critical: `0`.
- HIGH: `0` (`V32-001` closed).
- IMPORTANT: `0`.
- Minor: `0`.

This static PASS does not authorize live execution. The brief's separate
non-self-referential classification and fresh action-time pins remain required.

## Final verdict

**PASS**

Unresolved findings: Critical `0`, HIGH `0`, IMPORTANT `0`, Minor `0`.

`authorizes_live_execution=false`
