# OmniRoute V32 observed zone-route API-signature — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only commit
`8cbecc10e723accd69417f31efbf1dd4ece03c88` and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-zone-route-v32-api-signature-brief.md`.
Its direct parent is the V31 consumed PASS-clean report commit
`cfb34f1b1ae5dc2efe7d3f664cd539a88607a14c`.

I independently reviewed direct committed bytes, V31 predecessor evidence,
fresh route evidence, both direct navigations and settled-URL checks,
fixed-key output, one-shot consumption, exact-handle cleanup, no-retry and
no-provider-mutation constraints, secret exclusions, and the inherited V4
manual-confirmation boundaries.

I performed no Node, Chrome, browser binding, provider, clipboard, credential,
network, DNS, routing, process, Prox-01, or VM action and did not evaluate the
V32 cell. The only workspace write is this assigned review artifact.

## Final verdict

**FAIL** — one unresolved **HIGH** finding.

`authorizes_live_execution=false`

## Direct-byte and Git evidence

- Reviewed commit: `8cbecc10e723accd69417f31efbf1dd4ece03c88`.
- Direct parent: `cfb34f1b1ae5dc2efe7d3f664cd539a88607a14c`.
- The reviewed commit changes exactly the assigned V32 brief path.
- Brief: `19922` bytes, SHA-256
  `E317A793E2140450B77036775931B023B9C2B631D374DF1888D9D539AC4AF0D6`,
  Git blob `b324f56af9014a87265c0febcce0f6dce2e305f5`.
- Normalized executable: `16588` UTF-8 LF bytes, SHA-256
  `5ECC9E2D8F8F83C5CDA749ED3A12BC91C601D4333B12F92BFF06CB20BF325D35`.
- The exact executable bytes match the supplied syntax-PASS pin; static source
  inspection found no syntax contradiction. Per the explicit boundary, no
  Node parse command was run.
- `git diff-tree --check` reports no whitespace error.
- Before review creation, the index held zero paths and the exact inherited
  twelve-path dirty baseline was present and unstaged.

The V31 report reproduces as `3834` bytes, SHA-256
`F73D45DDACB2C9A2FF3CF6A98027ED726AD166210BC08D86889828E2E31C4778`,
and blob `6336bbeb3dfc6f1b1952dd37e9c04f407e8280bc`.

## V32-001 — HIGH — navigation is synthesized rather than bound to the fresh observed href

The pre-snapshot counts anchors whose parsed protocol, host, and pathname match
the account-local `mysw.me` zone path, then returns only
`exactZoneHrefCount`. It discards the matched href. After requiring that count
to equal one, controller code independently constructs:

`"https://dash.cloudflare.com/" + accountSegment + "/mysw.me"`

and passes that synthesized string to the second `goto`.

This does not prove that the navigation destination equals the sole fresh href
observed in the page. The anchor predicate does not constrain `search` or
`hash`, so the unique observed href may carry either component while V32
silently drops both. More fundamentally, a count is evidence that a qualifying
route exists, not the route value from which this one-shot navigation was
derived. The implementation therefore contradicts its explicit direct-evidence,
fresh-exact-href, no-inferred-route boundary and may spend V32 on a different
destination from the sole observed link.

Required correction: retain the sole observed absolute href in an untrusted
controller-local binding, validate it completely against the original account
segment and the allowed exact route shape (including an explicit search/hash
policy), and navigate that validated observed value. Never include the raw href
in terminal output. Alternatively, prove that the observed href has empty
search/hash and prove byte-for-byte equality with the synthesized canonical
destination before `zoneNavigationAttempted` is incremented. The fix must
remain one-shot and receive a fresh independent review; this V32 gate is not
authorized for execution.

## Closed security and one-shot checks

Subject to V32-001, the remaining reviewed boundaries are internally coherent:

- V32 consumes its fresh gate before the first await and requires the exact V23
  through V31 predecessor tuple, including V24 absence, V25 PASS-clean,
  V26/V27 failed-clean, V28 PASS-clean, V29/V30 failed-clean, and V31
  PASS-clean with null retained handles and unused downstream read gates.
- The fresh tab handle is chained into durable and local bindings before every
  later await. Creation rejection/uncertainty and malformed handle outcomes do
  not claim clean residue. Close rejection retains the exact handle and forces
  non-PASS; durable ownership clears only after close fulfillment.
- Static action sites are one `tabs.new`, two `goto`, two fulfilled URL reads,
  two bounded network-idle waits, two synchronous evaluators, one exact-handle
  close, and one terminal write. There is no click, press, fill, submit,
  selected/list/get discovery, retry, fallback, reconnect, or provider-persistent
  mutation.
- Home and settled-zone URL checks bind protocol, exact Cloudflare host,
  controller-local 32-hex account segment, and the account-local `mysw.me`
  zone prefix. Page-derived raw URLs, hrefs, paths, identifiers, attributes,
  text, DOM, HTML, and free-form errors are not emitted.
- Both page snapshots pass exact-key cross-realm validation. Only booleans and
  safe integers in `0..1000000` enter new trusted records; terminal output is
  fixed-key and uses a sanitized error class.
- The inherited provider-safety boundary remains read-only. No API token,
  credential, secret, clipboard value, Create/edit/delete, DNS, rate-rule,
  Tunnel, Access, permission, VM, routing, listener, or process action occurs.
- The mandatory final Create/native Copy/native masked Paste confirmation and
  the later separate exact-row deletion confirmation remain explicit,
  unreached, and mandatory.

## Finding counts and limits

- Critical: `0`.
- HIGH: `1` (`V32-001`, unresolved).
- IMPORTANT: `0`.
- Minor: `0`.

This review is static and fail-closed. It authorizes no live action, no V32
consumption, no retry, and no successor execution.

## Final verdict

**FAIL**

Unresolved findings: Critical `0`, HIGH `1`, IMPORTANT `0`, Minor `0`.

`authorizes_live_execution=false`
