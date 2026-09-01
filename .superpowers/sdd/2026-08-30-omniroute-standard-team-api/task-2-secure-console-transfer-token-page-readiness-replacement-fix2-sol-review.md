# Task 2 token-page readiness replacement — fix-round-2 Sol High review

## Verdict

**FAIL** — the three fix-round-1 findings are corrected at their stated
boundaries, but one new HIGH browser-lifecycle finding prevents a safe static
PASS. `authorizes_live_execution=false`.

This is a static review only. It authorizes no browser, clipboard, credential,
Cloudflare, VM, SSH, process, routing, or other live action.

## Reviewed source and integrity

- Fix-round-2 brief commit: `d56e2bb9443aebfae301ff0f883266dfa7946890`.
- Direct parent/fix1 FAIL review commit:
  `bfc203bfe1ad49086c11f53b413d1cc8971b18c6`.
- Exact brief: `task-2-secure-console-transfer-token-page-readiness-replacement-brief.md`.
- Direct bytes: `53932`.
- SHA-256: `4041BB6B6B9A4AB0735BB7A1AA41953112BEE37CCDE0083EA4284AFEA9230666`.
- The four JavaScript fences are pinned at:
  - `11813` / `B508877FBBA9546C8C7655FDFF989D13CE982C9F0B4CE027C64A521D707A6765`;
  - `20834` / `A61097CDB9902C1CB3F59D5F455F7CC84305CF0E3AC33656CFCDD76523A403EE`;
  - `2196` / `467F98589FD335AC6393B8BFEF64D7A3101EBE27C5BAA74E37A7FABA68AC5F60`;
  - `2201` / `55B407F463C351B64174800617E8B3F64B3CE98D60BAA1BEAEF1E6D3312B10A5`.
- All four fences passed non-evaluating `node --check` with empty
  stdout/stderr. The inherited PowerShell pins remain unchanged from their
  already reviewed parse-valid direct bytes.
- The required working projection remains
  `C4C9807FD5667E872BCBCFFD60FBF2AA71AEBC788AC744EFCD93FF18457C8E0F`,
  with the supplied independent reproduction covering `10653` records, index
  `0`, and exact filtered baseline `12`.

## Prior finding disposition

### Prior HIGH — stale/unbound filtered-result false PASS: corrected at predicate level

The corrected cells bind every filter by validated `aria-controls` to one exact
result region. They require an exact paginator, row counts, busy-free state,
exact empty status, and terminal next/previous controls. Reused filters first
establish a newly mutated clear baseline before arming the query transition;
the query then requires another region mutation to an exact `0-0 of 0` terminal.
The token, DNS, Tunnel, Access, and unique rate-panel/table proofs are scoped and
no longer rely on a broad `main` scan. Exact account/root-or-home and
post-navigation binding remain intact.

This closes the prior stale-marker logic only if the transition mechanism is a
valid, fully disposed browser operation. It is not; the new HIGH finding below
concerns that mechanism's implementation and failure lifecycle.

### Prior IMPORTANT — self-referential classification pin: corrected

The classification now pins only already-existing objects, its expected path,
and the projection. A separate uncommitted action-time coordinator tuple pins
the resulting classification commit, parent, path, direct bytes/hash, HEAD, and
projection after the commit exists (brief lines 92-117). No artifact is required
to contain its own unknown commit or blob hash.

### Prior IMPORTANT — forbidden/uncounted search fills: corrected

The brief now distinguishes exact nonpersistent page-local search fills from
forbidden provider-persistent Create/edit mutations. The V3 cell reports and
requires fill `1/1`; the fresh-read cell reports and requires the six exact
clear/query pairs as fill `12/12`. Counters increment immediately before and
after the awaited `fill` calls.

## Finding

### HIGH — the read-only evaluate API is used to install page-resident background state that survives failure

The installed Chrome API version `26.825.51511` documents
`PlaywrightLocator.evaluate` as JavaScript evaluation in a **read-only scope**.
The new transition design instead uses it to create and persist mutable state on
live DOM elements:

- The V3 token cell assigns `root.__secureConsoleTokenTransitionV3`, containing
  a `MutationObserver`, timer, Promise, resolver/rejecter, and input/DOM
  references (brief lines 285-308), then expects a later separate evaluate call
  to recover and delete that state (lines 312-320).
- The reusable helper similarly assigns
  `root.__secureConsoleFilterTransitionV3`, installs an observer and 20-second
  timer, and expects another evaluate call to await/delete it (lines 491-531).
  Cross-evaluate expando persistence is not part of the installed API contract.
- If an arm evaluate fulfills and the subsequent `fill` rejects or becomes
  uncertain, the cell's outer catch can emit its failure terminal while the
  page observer/timer remains active. The timer later rejects a Promise that no
  later call is permitted to await.
- If the transition timer itself rejects, `finish()` throws at `await
  state.promise`; the following `delete` is skipped. The expando and rejected
  Promise remain attached. An outer tool timeout has the same unproven residual
  boundary.
- The helper's cleanup of an `old` state occurs only on a later `arm` call. A
  failed or uncertain consuming action forbids that later browser call, so it
  is not a valid cleanup path.

This violates both the documented read-only evaluate semantics and the strict
serial fail-closed rule: after a rejected/uncertain browser promise, background
page work and retained state can continue even though no later browser mutation
or cleanup call is authorized. It also makes successful actionability depend on
undocumented persistence of JavaScript expando objects between locator-evaluate
invocations. The output counters do not report observer, timer, Promise, arm,
dispose, or residual state.

#### Required correction

Remove all page-resident observers, timers, Promises, expando assignments, and
cross-evaluate state. Use only documented direct serial awaited browser calls
and read-only evaluate snapshots. Establish freshness through an exact UI state
that is query-bound by the page itself—for example, a uniquely scoped result
status/total that echoes or otherwise proves the current query generation—or
return to a fresh, fully proven baseline/navigation before each query so a
newly visible exact terminal cannot be stale. Keep exact region, paginator,
row, busy, account, fill, and redacted counter proofs. Do not use a timer,
Promise race/concurrency, retry, fallback, or post-rejection cleanup action. Any
rejected or uncertain browser promise must end the cell with no surviving
browser-side work or state.

## Preserved controls

- Source projection, index/baseline, closed artifact allowlist, direct ancestry,
  and post-commit coordinator evidence are otherwise explicit and fail-closed.
- Account, zone, host, root-or-home path, post-navigation, unique locator,
  unique rate-table, and pagination predicates are scoped and redacted.
- V1/V2/V3 one-shot lifecycle, post-write eligibility, consumed state, and
  mutually exclusive zero-browser detach cells remain intact.
- Mandatory final Create/native Copy/native masked Paste and later exact-row
  deletion confirmations, universal revocation, invalid-token proof,
  owner/proxy/local cleanup, secret boundary, and no-retry/no-fallback/no-handoff
  controls remain unchanged.

Those controls do not neutralize the background browser-state residual.

## Finding count

- Blocking: 0
- HIGH: 1
- IMPORTANT: 0
- Static verdict: **FAIL**
- `authorizes_live_execution=false`
