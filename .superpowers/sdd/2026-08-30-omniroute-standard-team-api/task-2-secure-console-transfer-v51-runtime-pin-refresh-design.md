# V51 runtime-pin refresh replacement design

## Status and authority

V50 is a consumed historical one-shot and is permanently ineligible. It may
not be retried, continued, reused, reinterpreted, relaxed, or made eligible by
this document. V51 is a new replacement gate, consumed before validation or
import. This design is offline only: it neither authorizes nor reserves any
live action or authority.

The only proposed delta from final V50 is current runtime/documentation
provenance. All V50 record-selection, no-retry, privacy, cleanup,
confirmation, and no-mutation semantics are retained verbatim.

## Direct static compatibility and current pins

The compatibility evidence is a direct offline read of only these current
files, under the installed `26.901.20858` Chrome bundle:

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `C:\\Users\\chatc\\.codex\\plugins\\cache\\openai-bundled\\chrome\\26.901.20858\\scripts\\browser-client.mjs` | 150611 | `B9B9BC2319D5EE6AA0B1E481D63BB2130D28102FC7C9080803AB5552185D9037` |
| `C:\\Users\\chatc\\.codex\\plugins\\cache\\openai-bundled\\chrome\\26.901.20858\\docs\\api.json` | 59294 | `FC7966FFBC9010252AD3EA745E061068BEC3919EFFF860A87E6013A38A7E277F` |

The current documentation declares `BrowserUser.openTabs():
Promise<Array<BrowserUserTabInfo>>` and `BrowserUser.claimTab(tab: string |
BrowserUserTabInfo): Promise<Tab>`. The current runtime implements `openTabs`
by returning the backend `tabs` array and implements `claimTab` by accepting a
nonempty string or an object with string `id`, then sending that `id`. This is
interface-compatible with V50's complete descriptor-safe validation of the
returned record array and its single `claimTab` call using the exact returned
record. No runtime behavior, browser state, or backend result was invoked or
observed.

These pins are design evidence only. They must be recomputed from these exact
paths immediately before any later candidate import; any mismatch, missing
file, version/path substitution, or interface uncertainty stops V51 before a
send and does not authorize fallback or a second attempt.

## Retained V50 selection and downstream contract

V51 retains the V50 bounded ordinary-array contract unchanged: no symbols;
exact data `length` descriptor `1..1000`; exact contiguous index names; and
enumerable data descriptors. Every record is fully validated before selection:
non-null ordinary plain record at bounded prototype depth, only the documented
`id`, `lastOpened`, `providerTabId`, `tabGroup`, `title`, and optional `url`
keys; required enumerable data `id`; and bounded non-empty control-free string
for every present documented value. Accessors, present `undefined`, unknown
keys, symbols, malformed descriptors, and hostile structure fail before claim.

An absent `url` is a nonmatch. A present safe unrelated URL (including `http:`,
an internal scheme, or an explicit port) remains a nonmatch without parsing or
target-origin tests. Exactly one returned record whose already-validated URL is
literal-equal to `https://dash.cloudflare.com/profile/api-tokens` is selected
and claimed exactly once. Zero or multiple matches fail closed. No rank,
identifier reconstruction, guessed reference, normalization, alternate URL,
or raw listing output is allowed.

After that selection V51 retains V50/V49/V4 unchanged: one pinned import,
setup, Chrome connection, complete documentation read/write, session name,
`openTabs`, and exact-record claim; the exact account-home and `mysw.me`
zone-link signature; exact token-page navigation; bounded search/root/paginator
bindings; the fixed non-secret filter `OmniRoute secure console R5 20260901`;
its exact empty-terminal semantics; count-only, never-clicked Create; and all
reviewed counters and completeness predicates.

## Non-mutation, privacy, cleanup, and confirmations

V51 permits no CUA/browser/provider/network/VM/DNS/clipboard/credential/secret
action while this design is drafted or reviewed. A later candidate continues to
prohibit Copy, clipboard, token or credential access, storage, cookies, tab
creation/close, reconnect, retry, fallback, override, alternate path, verdict
relaxation, manual continuation, and every mutation. Create remains counted
only, never clicked.

The V35-V50 predecessor declarations, including all seven V50 globals, must be
absent in a fresh realm and pass a separate direct declaration audit immediately
before any V51 send. Only fixed literals, booleans, bounded counts, exact
counters, and fixed-schema results may be emitted. Raw listings, descriptors,
records, identifiers, titles, URLs, account segments, DOM text, thrown values,
credentials, tokens, and secrets are never emitted or retained.

PASS retains only the V51 owned token-page binding and minimal reviewed state,
eligibility, consumption, and later detach/read flags; all broad aliases clear.
Any failure or uncertainty spends V51, clears both V51 bindings and every broad
alias, emits at most one fixed sanitized terminal result, permits at most one
fixed state-only cleanup proof, then immediately resets the realm. A proof
failure cannot be corrected or queried again. The final Create/native
Copy/native masked Paste confirmation and the later separate exact-row deletion
confirmation remain external, mandatory, and unreached.

## Required independent sequence

1. Commit a smallest V51 executable and pure fixture mechanically preserving
   every retained V50 semantic, with only the V51 names, predecessor guards,
   and these runtime/doc provenance pins changed. Verify syntax, zero/one/many
   exact matches, unrelated safe URLs, hostile records, privacy, counters,
   PASS retention, and one-proof-only cleanup offline.
2. Produce a direct-byte package and obtain a fresh independent
   `gpt-5.6-sol` High review with zero unresolved Critical, HIGH, IMPORTANT, or
   Minor findings. This review is non-authorizing and must not use CUA, browser,
   provider, network, VM, DNS, clipboard, credentials, or secrets.
3. Commit a later non-self-referential V51 execution classification of only the
   prior committed evidence. It must state `authorizes_live_execution=false`.
4. The coordinator then produces a separate post-commit tuple: direct-parent
   chain, all candidate/review/classification hashes and blobs, empty index,
   exact unchanged 12-path dirty product baseline, unchanged outside
   projection, and current runtime/doc pin reproduction.
5. Only the sole Sol High gate owner may make the action-time decision after
   fresh realm reset, first call exactly `await cua.getState();`, direct
   declaration audit, clean evidence state, fixed exclusions, public-DNS
   absence, zero local residue, VM1205 safe checkpoint, sole token-object lane,
   and a new exact external confirmation of Chrome Profile `Codex-Chrome-Bell-PC2`,
   intended window, API Tokens tab, and no conflicting controller. Any missing,
   stale, false, or uncertain condition stops before a V51 send.

This V51 design grants no live authority. It neither changes provider state nor
waives any mandatory external or higher-priority safety confirmation.
