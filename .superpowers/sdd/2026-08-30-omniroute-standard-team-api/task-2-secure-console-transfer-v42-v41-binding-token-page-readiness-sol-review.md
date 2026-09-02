# OmniRoute V42 V41-binding token-page readiness — Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Verdict

**FAIL**

The committed V42 package has one unresolved HIGH finding and one unresolved
IMPORTANT finding. The success path does not implement the brief's sole-binding
transfer boundary, and the pure fixture cannot detect that defect or prove the
required terminal-output cleanup and complete counter matrix. V42 must not be
executed live from this package.

## Reviewed scope and provenance

- Reviewed commit: `bbb3a152791d6a9187195b2874e0c16baa2f5337`.
- Direct parent: `35c2a633424c0ed2851a31b849452a9784781e36`.
- The reviewed commit adds exactly the assigned V42 brief and V42 pure fixture.
- Brief blob: `02203ca58676e33310b756b924ae8c220f4289be`.
- Brief direct bytes: `18296`; SHA-256
  `D55F68C71EC3BC533212079F06F34992E9860889E6B6F2DA3B875CA89B3332AB`.
- Fixture blob: `9f2081e1cce0fbf50e61bc568f8bbcc0ba3b8f5d`.
- Fixture direct bytes: `7230`; SHA-256
  `0AB091CA7B1572FC95D69ACBB6E0C57DFF9A01049FCE1A551826A05542FB370D`.
- The sole LF-normalized executable cell is `14374` bytes with SHA-256
  `924DDE82A8921E1F05A9CB1DD6CB81FDCA297E7113EFA7D22EF149CB42CAEE0D`.
- Both package files have one final LF and the commit passes
  `git diff-tree --check`.
- The index was empty before review work. The exact pre-existing 12-path product
  dirty baseline was neither edited nor staged.

Review access was limited to the committed V42 package bytes and scoped
read-only Git/static checks. I did not invoke CUA, Chrome,
`setupBrowserRuntime`, a provider, credentials, DNS, VM resources, or any live
gate.

## Verification evidence

I ran the committed pure fixture once:

`node .superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v42-pure-fixtures.mjs`

It exited `0` and reported `V42_PURE_FIXTURES_PASS`, brief and executable hashes
matching the direct-byte extraction, `syntax="PASS"`, `fullCellSuccess=true`,
and `fixedFailureCleanup=true`. That passing result is narrower than the review
contract and does not resolve the findings below.

Scoped source-site checks confirm exactly one V42 consume assignment, one fixed
navigation call, one fixed fill, and one final write attempt. They also confirm
that each V41 runtime binding is nulled only twice: once in the ordinary failure
branch and once in the final-output failure branch, never in the success branch.

## Requirements assessment

### Correct and bounded aspects

- V42 marks itself consumed before predecessor validation or any tab action.
  V41 must already be consumed, eligible, account-home-ready, and present in the
  same realm; V42 does not import, reconnect, list, select, claim, close, or
  create another tab.
- The controller shape is checked before use. There is exactly one fixed
  navigation to `https://dash.cloudflare.com/profile/api-tokens` and one URL
  read whose normalized `href` must equal that exact URL.
- The page work is limited to a local search-filter fill and semantic reads. No
  Create control is clicked and no provider-persistent mutation, credential,
  clipboard, proxy, DNS, or VM action exists in the cell.
- The page signature expresses the inherited V4 checks: one named textbox, a
  bounded `aria-controls` ID, one bound result root and paginator, complete
  baseline state, empty initial filter, one exact query fill and echo, terminal
  zero pagination, no rows or busy state, one semantic Create control, and zero
  exact-name and matching-row counts. Readiness is exactly `3/3` and the success
  predicate requires the declared per-stage exact counters.
- The operational catch is unbound and reports only fixed
  `errorClass="Error"`; it does not inspect or serialize a thrown value.
- Ordinary failure clears both tab bindings and eligibility flags, marks V41
  detached, and clears the V41 Chrome, agent, and setup bindings. Final-output
  failure performs the same live-binding cleanup, marks a fixed terminal state,
  and rethrows without retry.
- The cell contains no retry, fallback, reconnect, alternate navigation,
  controller close, or continuation path. A failed or uncertain invocation
  remains consumed.
- The brief preserves the later Create/native Copy/native masked Paste and
  separate exact-row deletion confirmations as distinct mandatory external
  gates. Neither is reached or authorized here.

## Findings

### V42-001 — HIGH — Success retains broad V41 runtime/browser bindings contrary to the sole-binding contract

The brief says success “retains only the V42 binding,” and the assigned review
criterion requires a sole binding on success. The success branch assigns the
tab to `secureConsoleOwnedTaskTabV42`, clears only the V41 tab variable and
eligibility flag, and changes the V41 state. It does **not** clear:

- `secureConsoleChromeV41`;
- `secureConsoleAgentV41`; or
- `secureConsoleSetupBrowserRuntimeV41`.

Those bindings are explicitly required to be non-null on entry and include the
broad Chrome/session authority inherited from V41. They remain live after a
reported V42 success even though the package claims only the narrow V42 tab
binding survives. `continuationBindingsRetained` also omits these three
conditions, so the result can report a successful sole transfer while stale
V41 authority remains reachable. This violates the no-residue and least-
authority boundary and makes the output materially stronger than the actual
state.

Required correction:

1. In the V42 success branch, after the V42 tab is retained and the V41 tab is
   detached, set `secureConsoleChromeV41`, `secureConsoleAgentV41`, and
   `secureConsoleSetupBrowserRuntimeV41` to `null`.
2. Extend the success completeness predicate (or a separate fixed boolean) to
   require all three V41 runtime bindings to be null, in addition to the V41 tab
   and eligibility checks.
3. Keep the sole V42 tab binding eligible only if every one of those checks is
   true; otherwise fail closed and perform the existing full cleanup.

### V42-002 — IMPORTANT — The fixture does not prove the sole-binding, terminal-output, or exact-counter contract

The fixture's success assertion trusts the cell's
`continuationBindingsRetained` boolean. That boolean does not cover the three
stale V41 runtime bindings identified in V42-001, and the fixture cannot inspect
the cell's lexical predecessor bindings after execution. Consequently the
fixture reports `fullCellSuccess=true` while missing the success-residue defect.

The fixture also has only a normal success scenario and a navigation-failure
scenario. It never makes `nodeRepl.write` fail, so it does not exercise or
observe the required final-output cleanup. Finally, it asserts only the
`readinessAttempted` and `readinessFulfilled` values from the success counter
set; it does not assert exact binding, navigation, URL, fill, Create-read,
name-read, row-read, or final-write cardinality, nor the partial counter state
on failure.

Required correction:

1. Make the fixed success result prove that the V42 tab is the sole surviving
   live binding, including null V41 setup/agent/Chrome bindings, and assert that
   proof in the fixture.
2. Add an inert final-output-failure case whose `nodeRepl.write` throws. Use a
   safe transformed-cell observation hook or equivalent to assert V41 and V42
   tab null/ineligible state, all V41 runtime bindings null, fixed terminal V42
   and V41 states, and consumed V42. The test must not inspect the thrown value
   beyond identity/control needed by the inert harness.
3. Assert the complete exact success counter vector and the expected bounded
   partial vector for both ordinary and output failure scenarios, including one
   and only one final write attempt.

## Severity counts

| Severity | Count |
| --- | ---: |
| Critical | 0 |
| HIGH | 1 |
| IMPORTANT | 1 |
| Minor | 0 |

## Authorization statement

`authorizes_live_execution=false`

This FAIL review authorizes no live execution, continuation, retry, provider
action, secret operation, or confirmation consumption. A corrected package
requires a new independent review and new action-time classification/pins.
