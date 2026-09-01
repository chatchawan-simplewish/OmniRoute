# Task 2 token-page readiness replacement — fix-round-3 Sol High review

## Verdict

**FAIL** — the fix-round-2 HIGH is fully corrected, but one remaining HIGH
freshness gap and one IMPORTANT provenance error block exact PASS.

`authorizes_live_execution=false`.

This is a static review only. It authorizes no browser, clipboard, credential,
Cloudflare, VM, SSH, process, routing, or other live action.

## Reviewed source and integrity

- Fix-round-3 brief commit: `3654c4219e5b87407ec571005a72d95238c65a2e`.
- Direct parent/fix2 FAIL review commit:
  `080f9bec66a3b8f94b93e59e0c5e5463d9695401`.
- Exact brief: `task-2-secure-console-transfer-token-page-readiness-replacement-brief.md`.
- Direct bytes: `52584`.
- SHA-256: `2284BD06896785F675B1D1F1A5AFFE062377923366954CE4497E19592A661C97`.
- The four JavaScript fences are pinned at:
  - `10987` / `9000B5CBB1770DF58C307D1D3FED66844B0A6A2A239ED100D144C6C9DEBCAEA7`;
  - `19737` / `C9299E0BE4FFFB211B052C1F0E71D8DBEAFA89422EFA5BFC0BB88C380F65EE73`;
  - `2196` / `467F98589FD335AC6393B8BFEF64D7A3101EBE27C5BAA74E37A7FABA68AC5F60`;
  - `2201` / `55B407F463C351B64174800617E8B3F64B3CE98D60BAA1BEAEF1E6D3312B10A5`.
- All four fences passed non-evaluating `node --check` with empty
  stdout/stderr. The inherited PowerShell pins remain unchanged from their
  already reviewed parse-valid direct bytes.
- Required source projection:
  `C4C9807FD5667E872BCBCFFD60FBF2AA71AEBC788AC744EFCD93FF18457C8E0F`;
  index `0`; exact filtered status baseline `12`.

## Prior finding disposition

### Fix2 HIGH — page-resident observer/timer/Promise/expando state: corrected

The corrected fences contain no `MutationObserver`, `setTimeout`, page-resident
Promise, expando assignment, asynchronous evaluate callback, concurrent wait,
or later cleanup call. Every locator evaluation is a synchronous read-only
snapshot. Fresh-read queries are separated by fresh exact navigation where a
filter would otherwise be reused, then use serial fill, native locator
`waitFor`, and synchronous terminal snapshots. No browser-side work or retained
state can outlive a pass, throw, rejection, or outer timeout.

### Earlier HIGH/IMPORTANT findings

- Account/zone/root-or-home/post-navigation binding, count-one click locators,
  unique rate panel/table, exact result regions, paginator/row/busy terminals,
  and the fresh-read helper's empty/nonempty baselines remain scoped and
  fail-closed.
- Page-local fills remain explicitly authorized but provider-persistent form
  mutations remain forbidden. V3 fill `1/1` and fresh-read fills `12/12` are
  counted immediately around the awaited calls. Navigation `6/6`, click
  `13/13`, and readiness `33/33` match the source.
- The source projection, closed artifact allowlist, exact dirty baseline, and
  separate post-commit coordinator tuple retain the non-self-referential design.
  The current-commit pinning sentence contains a distinct error described in
  IMPORTANT finding 2.

## Findings

### HIGH 1 — the initial token baseline is not proven to be unfiltered

The first V3 token cell treats a fresh navigation's `0-0 of 0` terminal as
authoritative global absence (brief lines 262-290), but it never proves the
search textbox is empty before taking that baseline. `Tab.goto(url)` promises
only to open the URL; it does not prove that application state, browser-restored
form state, or a dashboard-preserved search value is empty.

If the token page opens with a retained nonempty search value whose result is
already `0-0 of 0`, `tokenBaseline.terminalZero` becomes true even though the
full token dataset may be nonempty. The cell then fills the target token name,
but the exact empty-status locator can already be visible and its native wait
can return immediately. The later textbox-value and terminal snapshots prove
only the current visible filter state, not that the earlier baseline was global.
All counters and booleans can therefore PASS while an existing same-name token
is outside the initially retained filter, permitting a duplicate final Create.

The fresh-read helper does not have this gap: it performs an awaited `fill("")`
before every baseline. The initial V3 cell must establish the same invariant.

#### Required correction

Before reading `tokenBaseline`, synchronously read the bound filter's current
value and require it to be exactly empty, exposing only a redacted boolean in
the terminal; or authorize/count one exact empty clear before the baseline and
adjust the exact fill tuple accordingly. Only an empty-filter terminal may be
classified as global zero. Preserve native waits, synchronous snapshots, exact
region/paginator/row/busy proof, and no background state.

### IMPORTANT 2 — the fix3 classification is instructed to pin fix2, not fix3, direct bytes

Lines 108-113 correctly require a fix3 brief → fix3 review → fix3 execution
classification direct-parent chain, but then state that the classification pins
“the committed fix2 brief and review direct bytes.” Those fix2 objects are
already historical objects listed above. The current fix3 brief and its future
PASS review are the load-bearing reviewed contract and are not required by this
sentence to be directly pinned inside the classification.

The later coordinator tuple pins the classification and its parent, but that
does not repair the classification's missing explicit fix3 brief/review byte
pins. This is not self-referential, but it leaves the current contract's exact
direct-byte identity incomplete.

#### Required correction

Replace “committed fix2 brief and review direct bytes” with “committed fix3
brief and fix3 review direct bytes.” Require the classification to record their
full commits, exact paths, byte lengths, and SHA-256 values while continuing to
omit its own unknown commit/blob identity. Keep the separate coordinator tuple
for the resulting classification commit and bytes.

## Preserved controls

- V1/V2/V3 one-shot lifecycle, post-write eligibility, consumed state, and the
  mutually exclusive zero-browser detach cells remain exact.
- All browser operations are serial and bounded by native locator/outer
  deadlines; errors are redacted and uncertainty spends the gate.
- Mandatory final Create/native Copy/native masked Paste and later exact-row
  deletion confirmations, universal revocation, invalid-token proof,
  owner/proxy/local cleanup, secret boundary, and no-retry/no-fallback/no-handoff
  controls remain unchanged.

Those controls do not compensate for the false global-zero baseline or missing
current fix3 byte pins.

## Finding count

- Blocking: 0
- HIGH: 1
- IMPORTANT: 1
- Static verdict: **FAIL**
- `authorizes_live_execution=false`
