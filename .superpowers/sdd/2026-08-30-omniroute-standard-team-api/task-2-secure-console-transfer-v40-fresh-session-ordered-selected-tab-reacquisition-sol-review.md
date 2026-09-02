# OmniRoute V40 ordered selected-tab reacquisition — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only package commit
`24ccef20d7157c324bf7c84435b93a7889b33b1c`, its direct parent
`27b2f2ee5ce168452a595e932964e09bd07709e7`, and the two paths added by that
commit:

- `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v40-fresh-session-ordered-selected-tab-reacquisition-brief.md`;
- `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v40-pure-fixtures.mjs`.

I reviewed the exact package, the consumed V39 incident needed to establish
the predecessor state, the previously reviewed ordered-selection design, and
the V4 constraints V40 keeps binding. I ran only the committed V40 pure fixture
and scoped static/read-only checks.

I did not call real `setupBrowserRuntime`, Chrome, browser get, `openTabs`,
`claimTab`, navigation, provider, credential, clipboard, DNS, routing, listener,
proxy, process-start, Prox-01, VM, or any other live resource. V40 was not
consumed. The only workspace write is this assigned review artifact.

## Final verdict

**FAIL** — one Minor finding remains unresolved. The governing V40 rule allows
PASS only when Critical, HIGH, IMPORTANT, and Minor counts are all zero.

`authorizes_live_execution=false`

## Exact commit, bytes, and offline evidence

- Reviewed commit: `24ccef20d7157c324bf7c84435b93a7889b33b1c`.
- Direct parent: `27b2f2ee5ce168452a595e932964e09bd07709e7`.
- The reviewed commit adds exactly the two assigned V40 paths and no other
  path.
- Brief: `20253` bytes, SHA-256
  `2D31D525C15AF34F7EB996D70DB09043907C2F5DE5701F73ED261D2EB6818407`,
  Git blob `0e4ac5093a4ccc1e2451ad0c86763f04630f5c2a`.
- Fixture: `10507` bytes, SHA-256
  `D932EC2BE4E6ED85F6C94F10395E62AF1B7483FF218695E2E860EB4853A41C79`,
  Git blob `bba393e3aef8ea8410fe384bc95cd02aa4b445f1`.
- The brief is UTF-8 without BOM and LF-only and contains exactly one
  JavaScript fence.
- The fixture extracted the sole LF-normalized executable at `16531` bytes,
  SHA-256
  `A72DF6E3491521EA01A07CEFD3933768FC1DBEE62520E4C3FE0AA710AC37E868`,
  and compiled it as an `AsyncFunction` without running the real cell.
- Running the exact committed fixture returned:

```json
{"result":"V40_PURE_FIXTURES_PASS","briefBytes":20253,"briefSha256":"2D31D525C15AF34F7EB996D70DB09043907C2F5DE5701F73ED261D2EB6818407","executableBytes":16531,"executableSha256":"A72DF6E3491521EA01A07CEFD3933768FC1DBEE62520E4C3FE0AA710AC37E868","syntax":"PASS","moduleShape":true,"foreignRealmAccepted":true,"orderedRankZeroEnforced":true,"fullCellSuccess":true,"fixedFailure":true,"getterCalls":0}
```

- The fixture imports the pinned module only to inspect its namespace. It does
  not call its setup export. Its transformed full-cell runs use only inert
  setup/browser/documentation/listing/claim/tab/terminal stubs.
- Before review creation, the index was empty and the inherited exact
  twelve-path product dirty baseline was present and unstaged.

## Finding

### V40-001 — Minor — committed brief has an extra blank line at EOF

The committed brief ends with two consecutive LF bytes after
`` `authorizes_live_execution=false` ``, rather than exactly one final LF.
Consequently the package commit fails the repository whitespace check:

```text
.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v40-fresh-session-ordered-selected-tab-reacquisition-brief.md:469: new blank line at EOF.
```

This does not alter the extracted JavaScript cell or its security semantics,
so the severity is Minor. It is nevertheless unresolved, and this brief
explicitly requires the independent review to report Minor `0` before PASS.

**Required fix:** remove only the extra blank line so the brief ends with one
LF immediately after the final `` `authorizes_live_execution=false` `` line,
commit the corrected brief directly on this FAIL review, rerun the committed
fixture to establish the new brief byte/hash tuple, and obtain a fresh
independent review. Do not execute V40 while correcting it.

## Correctly preserved predecessor and one-shot boundary

The fixed V39 incident proves V39 consumed once after complete fresh
attachment, documentation, session naming, and a structurally valid
foreign-realm listing with bounded `offeredCount=10`. Its zone-path filter
returned zero candidates, so claim, navigation, wait, URL, and snapshot counts
all remained zero. It cleared every binding, became permanently ineligible,
and reset the realm. V39 and all earlier named gates remain spent and cannot be
retried, continued, reinterpreted, or inherited.

V40 begins from a newly reset declaration-free realm. Its first control flow
records freshness and sets `secureConsoleV40Consumed=true` before import,
attachment, documentation, naming, enumeration, or claim. Success, failure,
timeout, or transport uncertainty spends V40 permanently. No retry, second
enumeration/claim, alternate selection, fallback, reconnect, or continuation is
present or authorized.

## Foreign-realm descriptor trust and rank-zero selection

The listing must pass `Array.isArray`, have zero own symbols, and expose an own
non-enumerable data `length` descriptor whose cached value is a safe integer in
`1..1000`. Its fresh own-name set must be exactly `length` plus every numeric
name `0..length-1`, and every numeric index must be an enumerable own data
descriptor.

Every cached index value must pass the established cross-realm plain-record,
zero-symbol, fixed-six-key allowlist, mandatory ID, enumerable data descriptor,
nonempty bounded string, and control-free checks. Projection retains only
fresh local primitive ID and URL values. No untrusted iterator, ordinary array
length, direct index, direct record field, or post-projection record read is
used.

The pinned API documentation states that `openTabs()` lists top-level tabs
across offered browser windows ordered by `lastOpened` descending, and defines
`lastOpened` as the last open/focus timestamp. V40 therefore uses only the
fully validated local rank-zero projection. Its authority depends on the
action-time exact owner confirmation that the intended task tab is selected
and no other Chrome profile/window is offered, together with the no-competing-
owner pin. That confirmation must remain immediate and unchanged through the
sole `openTabs` call; no rank-zero result independently proves user intent.

The rank-zero URL must be nonempty and parse to normalized HTTPS host exactly
`dash.cloudflare.com`, with empty non-default port and credentials. A later
Cloudflare record cannot replace a non-Cloudflare rank-zero record. The fixture
proves local and foreign-realm acceptance, later-record non-influence,
zero/multiple later Cloudflare records, symbol/name/hole/accessor/value
rejection, and zero getter calls.

## Claim, account-home signature, and evidence privacy

Only the once-cached primitive rank-zero ID reaches the sole
`claimTab(candidate.id)` call. Claimed ownership must return that exact cached
ID and the required Tab surface before any page action.

After exact claim, the cell performs one fixed navigation to
`https://dash.cloudflare.com/`, one `20000` ms wait, one final URL read, and one
body-locator evaluation. The URL must be exact HTTPS Cloudflare account home
with a 32-lowercase-hex account segment. The read-only semantic signature must
then prove exact same host/path, exactly one same-account `mysw.me` zone href,
positive anchor count, and zero busy/progress markers.

The page result is projected to exactly two booleans and three safe
nonnegative counts bounded by `1000000`. Only that fixed five-field snapshot,
booleans, bounded counts/sentinels, exact counters, and literal result/state/
error strings can reach terminal evidence. No ID, URL, title, provider ID,
group, timestamp, account segment, href, descriptor, prototype, raw listing,
raw page value, raw thrown value, credential, token, or secret is emitted.

## Thrown-value privacy, success retention, and cleanup

The outer handler is an unbound `catch` assigning only literal
`errorClass="Error"`; it never binds, reads, stringifies, coerces, or
prototype-tests a thrown value. The committed hostile fixtures confirm that a
token-like `name` and a throwing `name` getter do not enter output and cause
zero getter calls.

Exact success retains the reviewed setup function, agent, browser, and claimed
account-home tab bindings in this fresh realm, marks eligibility true, and sets
the exact ready state for a later separately reviewed same-realm step. It
authorizes no provider mutation or secret action.

Ordinary failure clears tab eligibility and every setup/agent/browser/tab
binding, sets fixed failure state, and proves failure cleanup before terminal
output. Terminal-output failure repeats all cleanup, sets the fixed stop state,
and rethrows without a second write. Any missing output, visible throw, timeout,
or transport uncertainty requires immediate realm disposal and a new reviewed
contract; no tab close or recovery action is allowed.

## Static source-site and counter completeness

The sole cell contains exactly one source site for dynamic import, setup,
browser get, documentation read and write, session name, `openTabs`,
`claimTab(candidate.id)`, fixed goto, one-argument wait, URL read, locator
evaluation, and terminal object write.

Import, setup, connect, documentation, documentation-write, name, open-tabs,
claim, navigation, wait, URL, and snapshot attempted/fulfilled counters each
have exactly one increment site per member. Every success-side pair is required
at exactly `1/1` before the fixed PASS result.

The cell contains zero retained-tab get, selected/list fallback, reconnect,
second enumeration/claim, new/close tab, screenshot, click/press/fill, fetch,
provider, clipboard, credential, DNS, routing, listener, proxy, process, or VM
action sites.

## V4, action-time, and mandatory confirmation boundary

All V4 page-signature, completeness, no-residue, no-retry, secret,
confirmation, and cleanup constraints remain binding and unreached. V40 does
not execute V4, prestart reads, Create, native copy/paste, provider mutation, or
deletion.

Before any live send, the sole owner must still prove the exact package/review/
classification ancestry and hashes/blobs; separate post-commit tuple; stable
`10661`-record projection; empty index; exact twelve-path product baseline;
runtime/docs pins; clean evidence worktree; zero residue; absent public DNS;
unchanged VM1205 safe checkpoint; archived prior owner; no competing owner;
the exact immediate Chrome profile/window/intended-tab selection confirmation;
and a newly reset declaration-free V35-V40 realm.

The final Create/native Copy/native masked Paste confirmation and the later
separate exact-row deletion confirmation remain mandatory external gates.
Neither can be pre-approved, automated, delegated, inferred from this review,
or waived.

## Finding counts and limits

- Critical: `0`.
- HIGH: `0`.
- IMPORTANT: `0`.
- Minor: `1` (`V40-001`).

No live or consuming action was authorized or performed.

## Final verdict

**FAIL**

Unresolved findings: Critical `0`, HIGH `0`, IMPORTANT `0`, Minor `1`.

`authorizes_live_execution=false`
