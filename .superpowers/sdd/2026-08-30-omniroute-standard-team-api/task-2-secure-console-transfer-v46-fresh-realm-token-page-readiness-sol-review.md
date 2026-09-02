---
status: clean
depth: deep
files_reviewed: 5
findings:
  critical: 0
  high: 0
  important: 0
  minor: 0
  total: 0
---

# OmniRoute V46 fresh-realm token-page readiness — Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Verdict

**PASS**

The V46 candidate is a narrow, evidence-supported replacement for the consumed
V44 gate. It preserves V44's structural, page-signature, completeness,
one-shot, no-residue, secret, confirmation, and cleanup boundaries while making
only the causal listing change established by the corrected V45 result: the
rank-zero record may omit its API-optional `url`; a present URL is still
strictly safe and Cloudflare-qualified. The same validated record object is
passed to `claimTab()`. No unresolved Critical, HIGH, IMPORTANT, or Minor
finding remains.

This is a static package-quality verdict only. It does not authorize or consume
V46, perform a Chrome/provider operation, satisfy action-time checks, replace
the required non-self-referential classification, or consume any external
confirmation.

## Reviewed lineage and direct bytes

- Corrected V45 result: commit
  `2bf5bfacb79da89fd83003048e442c1fd6e8ffeb`, blob
  `ed996f52975a15b48afc2805b1440ecf936a358d`.
- V44 semantic comparator: fixed candidate commit
  `3fed766dd6aadef89167c490f0ca232ffd041def`, executable blob
  `1a085198bbf6a7a4bbd898290e70fac2d6645d21`.
- V44 consumed-failure incident: commit
  `f5b11d7f76deaa48e648bab712318408603da43c`.
- Reviewed V46 candidate:
  `a6bfbc5ad673f49bb3b69d26026b096d1d18cbbd`; its direct parent is the
  corrected V45 result commit above, and it adds exactly the V46 brief,
  executable, and pure fixture.
- Brief: `7134` bytes; SHA-256
  `2A71A3175F5A02C7E6D8600BF3D9D564D89216D3DD04C2C575CD09F95D7B717D`;
  blob `ba3ad197e755e42dc40a009187663e1bcbfaf108`.
- Executable: `40894` bytes; SHA-256
  `55C8833CF0E405022B747298CE71E7ED6DCF4A301A6C429026A598004444050E`;
  blob `a78786b81de965f44f746215c46113222e69b282`.
- Pure fixture: `48886` bytes; SHA-256
  `87C80E600C62ABDD2D0B552B0B23D4A3D5A187EEB4222545311D8369C4BD127D`;
  blob `c367cdff70eaaeeeed06c786d3073c3e94307fbe`.
- All three committed V46 files are LF-only. Their worktree bytes matched the
  candidate before fixture execution.
- The installed browser module at the exact pinned path is `149771` bytes /
  SHA-256
  `A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`.
- The installed `docs/api.json` at the exact pinned path is `58480` bytes /
  SHA-256
  `A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.
- The index was empty before review work. The exact pre-existing 12-path dirty
  product baseline was neither edited nor staged.

## V45 evidence and exact V44-to-V46 semantic delta

The corrected V45 result is sufficient for the replacement boundary. Its
single consumed diagnostic observed one offered record, passed `Array.isArray`,
and passed every V44 descriptor, record, key, ID, safe-value, completeness, and
optional-value predicate. Cross-realm prototype inequality was explicitly
non-causal because V44 used `Array.isArray`. Claim, navigation, URL, snapshot,
and provider-write counters remained zero. The only V44 rejection not ruled out
was its mandatory treatment of documented `url?: string`.

A direct blob diff against the fixed V44 executable establishes that V46:

- changes V44 identity/result/state names to fresh V46 names;
- adds the complete V44 and V45 predecessor-declaration guards;
- removes only `validatedUrl === null` from the listing rejection;
- retains parsing plus exact HTTPS `dash.cloudflare.com`, empty-port,
  empty-username, and empty-password checks whenever URL is present;
- adds fixed `candidateUrlPresent` evidence;
- returns the cached rank-zero record and passes that exact object to
  `claimTab()` instead of passing only its ID; and
- otherwise preserves the V44 account-home navigation/signature, token-page
  navigation/signature, fixed filter fill, counters, output, transfer, and
  cleanup logic.

No broader listing or page-readiness relaxation is present.

## Freshness, listing trust, and exact-object claim

- V46 sets `secureConsoleV46Consumed = true` before predecessor validation or
  dynamic import. A nonfresh/default-dirty/contaminated realm stops before
  import, setup, documentation, naming, `openTabs`, claim, or navigation.
- Mechanical comparison against V45's established 73-name V35-V44 set plus
  its seven V45-owned declarations proves: expected `80`, actual unique `80`,
  missing `0`, extra `0`. The ten repeated later guard references are deliberate
  state checks, not missing or duplicate members of the initial set.
- The listing uses cross-realm-safe `Array.isArray`, symbol/name checks, a
  bounded own data `length`, exact index-name completeness, cached enumerable
  data descriptors, a plain/null-prototype rank-zero record, documented keys
  only, and bounded control-free strings. It invokes no offered-array iterator,
  getter, setter, direct indexed property read, or later-record value access.
- An absent URL succeeds with fixed `candidateUrlPresent=false` and
  `candidateUrlCloudflare=false`. A present malformed, non-HTTPS,
  non-Cloudflare, explicit-port, username, or password URL fails before claim.
- `candidate.tab` is exactly the cached descriptor value. The fixture proves
  `claimTab` receives that object by identity, including the absent-URL success
  path. The claimed controller must return the same bounded safe ID before any
  navigation.
- Selection ambiguity remains externally fail-closed: action time requires a
  fresh exact profile/window/tab confirmation and fresh `getState` proof of the
  sole offered Chrome profile with the intended rank-zero API Tokens tab.
  Post-claim account-home URL/zone-link semantics and API Tokens page semantics
  independently bind the claimed controller to the intended Cloudflare task.

## Completeness, security, and cleanup

- The executable contains exactly one import, `openTabs`, `claimTab`, account
  navigation, token-page navigation, and fixed non-secret filter fill. Both
  phase counter vectors must be exact before success.
- The account-home signature requires an exact 32-hex account-home URL, exact
  Cloudflare origin, exactly one expected zone link, a nonempty anchor set, and
  no busy/progress state. The token-page signature requires exact canonical
  URL, page region/root/paginator structure, settled filtering, exactly one
  Create control, and zero exact token-name/row matches.
- Create is counted but never clicked. The source contains no click, Copy,
  clipboard, local/session storage, cookie, token-secret, credential, provider
  mutation, tab-create/close, reconnect, retry, fallback, or manual-continuation
  path. Only fixed booleans, bounded counts, fixed states/counters, and a bounded
  trusted snapshot are retained or emitted; thrown values are neither inspected
  nor serialized.
- Success retains only the V46 owned tab binding and exact eligible state while
  clearing broad runtime/controller aliases. Every ordinary failure clears both
  V46 tab bindings and all broad aliases; documentation-output and final-output
  failures repeat cleanup, null evidence/output-error holders, and rethrow the
  original terminal value by identity. The fixture verifies these branches and
  all getter counters remain zero.
- V44 and V45 remain consumed, static, permanently ineligible, and unavailable
  as retry, continuation, reinterpretation, or fallback.
- No browser setup, Chrome connection, enumeration, claim, navigation, provider
  read/write, credential/secret operation, DNS/network/VM action, confirmation,
  or authority-gate consumption occurred during this review.

## Fixture terminal observed

The committed inert fixture exited `0` after `node --check` and emitted:

`{"result":"V46_PURE_FIXTURES_PASS","briefBytes":7134,"briefSha256":"2A71A3175F5A02C7E6D8600BF3D9D564D89216D3DD04C2C575CD09F95D7B717D","executableBytes":40894,"executableSha256":"55C8833CF0E405022B747298CE71E7ED6DCF4A301A6C429026A598004444050E","fixtureBytes":48886,"fixtureSha256":"87C80E600C62ABDD2D0B552B0B23D4A3D5A187EEB4222545311D8369C4BD127D","syntax":"PASS","declarationFree":true,"v45PredecessorsAbsent":true,"listingMatrix":true,"exactOutputKeys":true,"fullCellSuccess":true,"fixedFailureCleanup":true,"hostileThrownValues":true,"terminalOutputCleanup":true,"completeCounterVectors":true,"getterCalls":0,"listingGetterCalls":0,"outputGetterCalls":0}`

The fixture imports only Node built-ins. Before evaluating the full cell it
replaces the sole browser-module import with an inert fixture binding; it does
not import or invoke the browser runtime, connect to Chrome, enumerate or claim
a real tab, navigate, inspect a provider page, or mutate provider state.

## Severity counts

| Severity | Count | Unresolved findings |
| --- | ---: | --- |
| Critical | 0 | None |
| HIGH | 0 | None |
| IMPORTANT | 0 | None |
| Minor | 0 | None |

## Authorization statement

`authorizes_live_execution=false`

V46 remains non-executable until a separate non-self-referential classification
and post-commit coordinator tuple are complete and all action-time hashes,
fresh-realm declaration audit, DNS/no-residue/VM/ownership checks, and exact
external Chrome selection confirmation pass. Any V46 failure or uncertainty
spends the gate with no retry. The final Create/native Copy/native masked Paste
confirmation and the later separate exact-row deletion confirmation remain
external, mandatory, and unreached.
