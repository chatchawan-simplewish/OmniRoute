# OmniRoute V39 cross-realm task-tab reacquisition — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only package commit
`f697a8770b6456324c05b088545c1380a4b9f495`, its direct parent
`4a71518e3189e813a9de6f36b4570d768a6aede0`, and the two paths added by that
commit:

- `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v39-fresh-session-cross-realm-task-tab-reacquisition-brief.md`;
- `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v39-pure-fixtures.mjs`.

I reviewed the exact package, the consumed V38 diagnostic report needed to
establish the predecessor state, the retained V37 account-home semantics, and
the V4 constraints that V39 keeps binding for later separately reviewed work. I
ran only the committed V39 pure fixture and scoped static/read-only checks.

I did not call Chrome, `setupBrowserRuntime`, browser get, `openTabs`,
`claimTab`, navigation, provider, credential, clipboard, DNS, routing, listener,
proxy, process-start, Prox-01, VM, or any other live resource. V39 was not
consumed. The only workspace write is this assigned review artifact.

## Final verdict

**PASS** — zero unresolved Critical, HIGH, IMPORTANT, or Minor findings.

This review is evidence only. It does not authorize live execution. V39 remains
`authorizes_live_execution=false` pending its non-self-referential execution
classification, separate post-commit tuple, every action-time pin, and the
required external confirmations.

## Exact commit, bytes, and offline evidence

- Reviewed commit: `f697a8770b6456324c05b088545c1380a4b9f495`.
- Direct parent: `4a71518e3189e813a9de6f36b4570d768a6aede0`.
- The reviewed commit adds exactly the two assigned V39 paths and no other
  path. `git diff --check` is clean.
- Brief: `21821` bytes, SHA-256
  `A317EFC5F3435212D8E223E2AF46C6CC043CD4129918A0889FF20213CDD16648`,
  Git blob `4753fbace65642c725e4d91e3717f99797ff9f04`.
- Fixture: `10435` bytes, SHA-256
  `FA5C0750EAF74E01491B31695EE53C26441F207F49823C83CEBDAD00E8C918E2`,
  Git blob `2ead83330183502708d46c45e2524bd57ad11db1`.
- The brief is UTF-8 without BOM and LF-only, contains exactly one JavaScript
  fence, and ends with a final LF.
- The fixture extracted the sole LF-normalized executable at `16848` bytes,
  SHA-256
  `B4129373982168BE96B70E528FB1029977050A6E9630D2FF7B940B033BEF9CF4`,
  and compiled it as an `AsyncFunction` without running the real cell.
- Running the exact committed fixture returned:

```json
{"result":"V39_PURE_FIXTURES_PASS","briefBytes":21821,"briefSha256":"A317EFC5F3435212D8E223E2AF46C6CC043CD4129918A0889FF20213CDD16648","executableBytes":16848,"executableSha256":"B4129373982168BE96B70E528FB1029977050A6E9630D2FF7B940B033BEF9CF4","syntax":"PASS","moduleShape":true,"foreignRealmAccepted":true,"uniqueCandidateEnforced":true,"fullCellSuccess":true,"fixedFailure":true,"getterCalls":0}
```

- The fixture imports the pinned module only to inspect its namespace and never
  calls its setup export. Every transformed full-cell run substitutes inert
  setup/browser/documentation/listing/claim/tab/terminal stubs for the sole
  import expression.
- Before review creation, the index was empty and the inherited exact
  twelve-path product dirty baseline was present and unstaged.

## Runtime, documentation, and predecessor boundary

The installed reviewed pair still reproduces the package boundary:

- `browser-client.mjs`: `149771` bytes, SHA-256
  `A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`;
- `api.json`: `58480` bytes, SHA-256
  `A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.

The module namespace exposes function-valued `setupBrowserRuntime` and no
invented `BROWSER_CLIENT_ID`. The reviewed API supports browser get, complete
documentation, session naming, `openTabs`, `claimTab(string)`, fixed
navigation, one-argument wait, URL read, locator, and read-only evaluate exactly
as used.

The fixed V38 live report proves V38 consumed once in a fresh realm, captured
`Array.isArray=true`, local prototype identity false, bounded count `9`, and
true for every other reviewed array, index, record, key, descriptor, optional
value, and string-safety predicate. It performed zero claim, navigation, URL,
or snapshot action; cleared every binding; became permanently ineligible; and
reset the realm. V38 and all earlier named gates remain spent and are not
inherited by V39.

V39 therefore starts from a newly reset declaration-free realm. Its first
executed control flow records freshness and sets `secureConsoleV39Consumed=true`
before import, attachment, documentation, enumeration, or claim. Success,
failure, timeout, or transport uncertainty spends V39 permanently.

## Cross-realm listing and projection

The only intended V37 shape relaxation is removal of identity with the local
realm's `Array.prototype`. The listing must still pass `Array.isArray`, have no
symbols, and have an own non-enumerable data `length` descriptor whose cached
value is a safe integer in `1..1000`.

The fresh own-name list must contain exactly `length` plus every numeric name
`0..length-1`. Each index is obtained through one own descriptor and must be an
enumerable data descriptor. There is no untrusted array iteration, direct index
read, `offered.length` read, or inherited-value dependency.

Each cached index value must satisfy the established cross-realm plain-record
shape and zero-symbol rule. Its own string names must come only from the fixed
six-key API allowlist and include `id`. Every own key receives one own
descriptor read and must be enumerable data containing a nonempty,
control-free string bounded to `512`, `4096` for title, or `16384` for URL.
Only cached primitive `id` and URL values enter fresh local projection records;
the original array and records are never read after projection.

The committed fixtures prove ordinary and exact foreign-realm acceptance;
null-prototype records; symbol, unexpected-name, hole, index-accessor,
record-accessor, unexpected-key, optional-undefined, and control-bearing
rejection; and zero getter calls. Removing local prototype identity introduces
no iterator or inherited-property read.

## Unique task selection and claim continuity

Every cached non-null URL is parsed privately. A candidate requires normalized
HTTPS host exactly `dash.cloudflare.com`, empty non-default port and
credentials, and pathname matching exactly a 32-lowercase-hex account segment,
`mysw.me`, and only an optional slash-delimited descendant. Prefix collisions,
sibling zones, wrong accounts/origins, credentials, non-default ports, and
malformed URLs do not match. No parsed component or URL is emitted.

The complete bounded local projection is filtered before any authority action.
The returned candidate is non-null only when bounded local `targetCount` is
exactly one. Zero or multiple matches stop before claim. The candidate contains
only the cached primitive ID; the one authority-bearing call is exactly
`claimTab(candidate.id)`.

The claimed controller must return that exact cached ID, within the same
control-free bound, and expose the required fixed Tab method surface before
navigation. No candidate record, URL, listing object, rank-zero assumption,
selected/list/get fallback, or alternate claim is retained or re-read.

## Account-home signature, evidence, and retained success

After exact claim, V39 performs one fixed navigation to
`https://dash.cloudflare.com/`, one `20000` ms wait, and one final URL read. The
URL must match exact HTTPS `dash.cloudflare.com`, a 32-lowercase-hex account
segment, and `/home` with only an optional trailing slash. The account segment
is used only inside the same read-only semantic check and is never emitted.

The page-local snapshot counts anchors and busy/progress markers and validates
one exact same-account `mysw.me` zone href. Its untrusted return must project to
exactly five fixed fields: two booleans and three safe nonnegative integer
counts bounded by `1000000`. PASS requires exact host and account-home path,
exact zone count `1`, positive anchor count, and busy count `0`.

Only that projected five-field snapshot, fixed booleans, bounded counts,
counters, literal state/result/error strings, and sentinels can reach terminal
evidence. No ID, URL, title, provider ID, group, timestamp, account segment,
href, descriptor, prototype, raw listing, raw page value, raw exception,
credential, token, or secret is emitted.

Exact success retains the reviewed setup function, agent, browser, and claimed
account-home tab bindings in this fresh realm, marks eligibility true, and sets
`V39_ACCOUNT_HOME_READY_ELIGIBLE`. This retention authorizes only a later
separately reviewed same-realm step; it authorizes no provider or credential
action.

## Thrown-value privacy and cleanup

The outer handler is an unbound `catch` assigning only literal
`errorClass="Error"`. It does not bind, read, stringify, coerce, or
prototype-test a thrown value. The committed full-cell fixtures throw both a
plain token-like `name` and an object whose `name` getter itself throws; both
produce fixed failure evidence and zero getter calls.

Ordinary failure clears tab eligibility and all setup/agent/browser/tab
bindings, sets fixed failed state, and proves `failureCleanupComplete=true`
before the terminal write. Terminal-write failure repeats all cleanup, sets
`V39_FINAL_OUTPUT_FAILED_STOP`, and rethrows without a second output or thrown-
value inspection. Any visible throw, missing output, timeout, or transport
uncertainty requires immediate realm disposal and a newly reviewed contract;
no close, retry, recovery, continuation, or fallback is permitted.

## Static source-site and counter completeness

The sole cell contains exactly one source site for each of:

- dynamic import, setup, browser get, documentation read and write, session
  name, `openTabs`, `claimTab(candidate.id)`, fixed goto, one-argument wait, URL
  read, locator evaluation, and terminal object write;
- import, setup, connect, documentation, documentation-write, name, open-tabs,
  claim, navigation, wait, URL, and snapshot attempted/fulfilled increments.

Every success-side attempted/fulfilled pair must be exactly `1/1` before the
fixed PASS result is assigned. The cell has zero retained-tab get, selected or
list fallback, reconnect, second enumeration/claim, new/close tab, screenshot,
click/press/fill, fetch, provider, clipboard, credential, DNS, routing,
listener, proxy, process, or VM action sites.

## V4 and action-time constraints

All V4 page-signature, completeness, no-residue, no-retry, secret,
confirmation, and cleanup constraints remain binding and unreached. V39 does
not execute V4, prestart reads, Create, native copy/paste, provider mutation, or
deletion.

Before a live send, the sole owner must still prove the exact package/review/
classification ancestry and file/executable hashes and blobs; a separate
post-commit tuple; stable `10661`-record projection digest
`C4C85893769D133224AC7404B628C8B0D4B0EBBFF471620B158E652E152B4EBD`;
empty index; exact twelve-path product baseline; runtime/docs pins; clean
evidence worktree; zero Windows residue; absent public DNS; unchanged VM1205
safe checkpoint; archived prior owner; no competing owner; exact owner-selected
Chrome profile/window/task-tab confirmation; and a newly reset realm with every
named V35-V39 declaration absent.

The final Create/native Copy/native masked Paste confirmation and the later
separate exact-row deletion confirmation remain mandatory external gates.
Neither may be pre-approved, automated, delegated, inferred from this PASS, or
waived.

## Finding counts and limits

- Critical: `0`.
- HIGH: `0`.
- IMPORTANT: `0`.
- Minor: `0`.

No live or consuming action was authorized or performed.

## Final verdict

**PASS**

Unresolved findings: Critical `0`, HIGH `0`, IMPORTANT `0`, Minor `0`.

`authorizes_live_execution=false`
