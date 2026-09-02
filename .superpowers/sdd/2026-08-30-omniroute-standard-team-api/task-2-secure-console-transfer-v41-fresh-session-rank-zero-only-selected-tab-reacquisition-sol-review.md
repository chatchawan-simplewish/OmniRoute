# OmniRoute V41 fresh-session rank-zero-only selected-tab reacquisition — Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Verdict

**PASS**

The committed V41 package is internally consistent with its narrow purpose and
the inherited V4 safety contract. I found no unresolved defect at any review
severity. This static PASS does not authorize Chrome access, consumption of the
one-shot gate, provider mutation, secret handling, or either mandatory external
confirmation.

## Reviewed scope and provenance

- Reviewed commit: `6ad4cba47092c5f9eb85b4c55b461bfe60e46e16`.
- Direct parent: `f12b20cbf9c21afc37602ffd8d41dce2eaa4fc44`.
- The reviewed commit adds exactly the V41 brief and V41 pure fixture assigned
  for this review.
- Brief blob: `924f981c6a25e4a8e3d661b054e58607da4f43fa`.
- Brief direct bytes: `19711`; SHA-256
  `B64167FDA2E71964970CA4435B33D63FB6DD0ACCE893F268F74A8A86A13127B4`.
- Fixture blob: `eb80b999eb3b05ef95ec42f7d3d5b73fdaf36feb`.
- Fixture direct bytes: `10898`; SHA-256
  `6CECEAAD6C30EC47C231AA84C828B4BAE351AF81C5EC8A09B51CF5B9FA2CD1DC`.
- The extracted LF-normalized executable is `16543` bytes with SHA-256
  `FA852FF0448AF784BCDDB3800192E539C295829C219DB1B3C7CA4C02152E8DF5`.
- Both committed files have one final LF. `git diff-tree --check` is clean.
- The index was empty before review work. The pre-existing 12-path product dirty
  baseline was not staged, edited, or otherwise touched.

Review access was limited to committed V41 package bytes and scoped Git/static
checks. I did not invoke Chrome, `setupBrowserRuntime`, `openTabs`, `claimTab`, a
provider, credentials, DNS, VM resources, or any live gate.

## Verification evidence

The committed pure fixture was run once with:

`node .superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v41-pure-fixtures.mjs`

It exited `0` and returned `V41_PURE_FIXTURES_PASS`, including:

- `syntax="PASS"` and `moduleShape=true`;
- `foreignRealmAccepted=true`;
- `rankZeroOnly=true` and `laterRecordUninspected=true`;
- `fullCellSuccess=true` and `fixedFailure=true`; and
- `getterCalls=0`.

The fixture exercises the marked helper and an inert transformed full cell. It
does not perform real runtime setup or browser actions. Its matrix covers local
and foreign-realm arrays, array symbols, unexpected names, holes, index
accessors, rank-zero record accessors, missing/extra/optional/control-character
fields, null-prototype records, hostile later records, successful retained
bindings, and fixed terminal-safe failure behavior.

## Security and semantic assessment

### One-shot and predecessor boundary

- `secureConsoleV41Consumed` is observed while fresh and set to `true` before
  the dynamic import. Thus import, setup, or any later failure spends the gate.
- The declaration precondition rejects an already-consumed V41 realm and uses
  undefined predecessor sentinels for V35 attachment/adoption and V36-V40, plus
  the V38-V40 owned-tab sentinels. Because each predecessor cell declares its
  sentinels as one top-level declaration unit, these checks fail closed on a
  predecessor-bearing realm.
- The brief explicitly states that V3, V4-live, V34 Call 2, and V35-V40 remain
  consumed/static and may not be retried, continued, reinterpreted, or
  inherited. No retry loop, reconnect path, fallback selector, manual override,
  tab close, or alternate claim path exists in the executable.

### Cross-realm listing envelope and rank-zero trust

- `Array.isArray` supplies the cross-realm array test; the contract does not
  depend on local `Array.prototype` identity or iteration.
- The helper reads a bounded own `length` data descriptor, rejects symbols,
  requires exactly `length + 1` own names, constructs the exact numeric-name
  set, and reads each numeric slot only through its own descriptor. Holes,
  accessors, non-enumerable slots, unexpected names, and out-of-range lengths
  stop before claim.
- The loop validates only the array envelope for later indices. It does not
  read, destructure, iterate, stringify, filter, emit, or inspect the `.value`
  of any descriptor after index zero. Only
  `indexDescriptors[0].value` becomes a record candidate. The hostile-later
  fixture proves that a throwing later-record getter is never invoked.
- The rank-zero record must be a cross-realm-compatible plain or null-prototype
  record, contain no symbols, use only the fixed documented key set, and expose
  required `id` and `url` through enumerable own data descriptors. Every
  present field must be a bounded, nonempty, control-free primitive string.
- URL parsing requires exact HTTPS `dash.cloudflare.com`, empty explicit port,
  and empty username/password. The projected candidate retains only the cached
  primitive ID, bounded count, and boolean origin result; no raw record or
  metadata survives. `claimTab` receives only the cached projected ID.
- Exactly one `openTabs()` call precedes exactly one possible `claimTab()` call.
  Selection of rank zero remains expressly dependent on the documented
  last-opened/focused ordering and the owner's exact selected-tab and
  no-other-profile/window confirmation. Static review does not establish that
  action-time fact.

### Post-claim semantic proof and completeness

- The claimed controller must return the same cached primitive ID and expose
  the required `goto`, `url`, `waitForTimeout`, and `locator` methods before
  navigation.
- Navigation is fixed to `https://dash.cloudflare.com/`. The post-navigation
  URL must be the exact account-home form with one 32-character lowercase-hex
  account segment.
- The in-page snapshot derives only fixed booleans and bounded counts. The
  semantic signature requires exact Cloudflare HTTPS origin, the same account
  home path, exactly one exact `/<account>/mysw.me` zone anchor, a positive
  anchor count, and zero busy/progress indicators.
- The returned snapshot passes a fixed-schema plain-record gate before use.
  No raw DOM, URL, account segment, candidate metadata, credential, or secret is
  emitted.
- Attempted/fulfilled counters cover import, setup, connection, documentation,
  documentation output, naming, listing, claim, navigation, wait, URL, snapshot,
  and final output. Success requires exact cardinality `1` for every substantive
  stage; the single final write attempt is separately recorded. There is no
  hidden second attempt or alternate stage.

### Failure privacy, cleanup, and residue

- The operational catch is unbound and emits only fixed `errorClass="Error"`;
  it never examines, names, serializes, or reports the thrown value.
- On any ordinary failure, the owned tab and eligibility are cleared, the
  V41 state becomes failed, and setup/agent/browser bindings are nulled. The
  consumed flag deliberately remains true.
- On success, only the setup function, agent, browser, and adopted controller
  bindings needed for the separately gated continuation are retained; no raw
  listing or candidate record is retained.
- If the final output transport throws, the terminal catch clears all retained
  live bindings, sets the fixed final-output-failed state, and rethrows without
  a retry. This preserves transport uncertainty and no-residue semantics.

### Confirmation and action-time boundary

- The brief carries forward all V4 page-signature, completeness, no-residue,
  no-retry, secret, confirmation, and cleanup constraints.
- A live owner would still have to revalidate the committed package hashes,
  runtime/docs and worktree pins, empty index, exact 12-path dirty baseline,
  stable listing projection, ownership/residue/DNS/VM pins, exact Chrome
  selection, and a fresh declaration-free V35-V41 realm immediately before any
  consumption.
- The final Create/native Copy/native masked Paste confirmation remains an
  external, nondelegable gate. The later exact-row deletion confirmation is a
  separate external, nondelegable gate. Neither is pre-approved or satisfied by
  this review.

## Findings

| Severity | Count | Unresolved findings |
| --- | ---: | --- |
| Critical | 0 | None |
| HIGH | 0 | None |
| IMPORTANT | 0 | None |
| Minor | 0 | None |

## Authorization statement

`authorizes_live_execution=false`

This PASS classifies only the committed static V41 package. Live execution
remains blocked pending the required non-self-referential classification,
post-commit tuple, all action-time pins, and the owner's exact external
selection confirmation. The later secret-bearing and deletion actions remain
behind their two distinct mandatory confirmations.
