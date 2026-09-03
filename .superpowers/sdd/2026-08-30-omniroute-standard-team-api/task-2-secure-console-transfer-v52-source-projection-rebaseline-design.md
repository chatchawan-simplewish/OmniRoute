# V52 source-projection rebaseline replacement design

`authorizes_live_execution=false`

## Status, replacement, and fixed baseline

V51 is a classified historical one-shot. It must never be retried, continued,
reused, reinterpreted, relaxed, or made eligible through V52. V52 is a new,
separately consumed-before-validation-or-import replacement. This design is
offline documentation only and neither reserves nor authorizes live execution.

The owner newly authorizes exactly one changed baseline: the fixed-exclusion
source projection is **10619 records**, SHA-256
`89D36435A31AE04E560A27D53D8A0953F19E837DF60837FADCF3DC174C0B9477`.
The V52 coordinator must reproduce that exact count and digest immediately at
action time; any difference, missing evidence, or uncertainty stops before a
V52 send, without fallback or retry.

All V51/V50 record-selection, predecessor, downstream, counter, privacy,
retention, cleanup, no-mutation, external-confirmation, and no-retry semantics
are retained verbatim. The only V52 delta is this owner-authorized source-
projection rebaseline and V52 naming/predecessor guards.

## Immutable V51 evidence and runtime provenance

V51 remains immutable evidence, classified at
`246c7f9e435ed86df3f10a402b55bd2fd62ddfc9`, directly descending from the
zero-finding V51 fix-1 Sol PASS `554ba72983b459a61baf8796bd34bf0d51e8bac3`.
V52 neither amends nor relies on V51 as reusable execution authority.

The current installed `26.901.20858` pins remain mandatory and unchanged:

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `C:\\Users\\chatc\\.codex\\plugins\\cache\\openai-bundled\\chrome\\26.901.20858\\scripts\\browser-client.mjs` | 150611 | `B9B9BC2319D5EE6AA0B1E481D63BB2130D28102FC7C9080803AB5552185D9037` |
| `C:\\Users\\chatc\\.codex\\plugins\\cache\\openai-bundled\\chrome\\26.901.20858\\docs\\api.json` | 59294 | `FC7966FFBC9010252AD3EA745E061068BEC3919EFFF860A87E6013A38A7E277F` |

V52 preserves V51's directly reviewed `openTabs()` array and exact returned-
record `claimTab` compatibility. These pins and their exact paths must be
recomputed immediately before any candidate import; drift, substitution,
absence, or interface uncertainty fails closed before a send.

## Retained record-selection and downstream contract

V52 mechanically retains V51's bounded ordinary-array contract: no symbols;
exact data `length` descriptor `1..1000`; exact contiguous enumerable data
indexes; and full, descriptor-safe validation of every plain record before
selection. Only documented keys (`id`, `lastOpened`, `providerTabId`,
`tabGroup`, `title`, optional `url`) are permitted; required `id` and every
present value are bounded non-empty control-free strings. Accessors, present
`undefined`, unknown keys, malformed descriptors, hostile records, and unsafe
strings fail before claim.

An absent URL is a nonmatch. A safe unrelated URL, including `http:`, an
internal scheme, or explicit port, is a nonmatch without target parsing.
Exactly one already-validated record with literal URL
`https://dash.cloudflare.com/profile/api-tokens` may be claimed once. Zero or
multiple matches fail closed. No rank, normalization, identifier
reconstruction, guessed reference, alternate URL, or raw-listing output is
permitted.

After selection V52 retains V51/V50/V49/V4 unchanged: one pinned import,
setup, Chrome connection, complete documentation read/write, session name,
`openTabs`, exact-record claim, account-home and `mysw.me` zone-link signature,
exact token-page navigation, bounded search/root/paginator bindings, fixed
non-secret filter `OmniRoute secure console R5 20260901`, exact empty-terminal
semantics, count-only never-clicked Create, and every reviewed counter,
completeness predicate, and downstream readiness `4/4` PASS condition.

## Fresh realm, privacy, retention, cleanup, and prohibited surfaces

The fresh-realm/direct-declaration audit immediately before a V52 send must
prove every V35-V51 declaration absent, including these seven V51 predecessor
globals: `secureConsoleOwnedTaskTabV51`,
`secureConsoleOwnedTaskTabV51Eligible`, `secureConsoleOwnedTaskTabV51State`,
`secureConsoleOwnedTaskTabV51PreCreateDetachConsumed`,
`secureConsoleOwnedTaskTabV51PostNativeDetachConsumed`,
`secureConsoleCloudflareReadsV51Consumed`, and `secureConsoleV51Consumed`.

Only fixed literals, booleans, bounded counts, exact counters, and fixed-schema
results may be emitted. Raw listings, descriptors, records, identifiers,
titles, URLs, account segments, DOM text, thrown values, credentials, tokens,
and secrets are never emitted or retained. PASS retains only the V52 owned
token-page binding and minimal reviewed state, eligibility, consumption, and
later detach/read flags; all broad aliases clear. Any failure or uncertainty
spends V52, clears both V52 bindings and broad aliases, emits at most one fixed
sanitized terminal result, permits at most one fixed state-only cleanup proof,
and immediately resets the realm. Cleanup-proof failure cannot be corrected or
queried again.

This design and every review/candidate step performs no CUA, browser, provider,
network, VM, DNS, clipboard, credential, or secret action. The later candidate
also forbids Copy, clipboard, credential/token access, storage/cookies, tab
creation/close, reconnect, retry, fallback, override, alternate path, verdict
relaxation, manual continuation, and every mutation. The final Create/native
Copy/native masked Paste confirmation and separate exact-row deletion
confirmation remain external, mandatory, and unreached.

## Required V52 evidence sequence and action-time gate

1. Commit the smallest V52 candidate quartet: brief, implementation plan,
   executable, and pure fixture. It must mechanically preserve V51, changing
   only V52 names, all seven V51 predecessor guards, and the authorized source
   projection baseline. Pure fixtures must cover zero/one/many exact matches,
   unrelated safe URLs, hostile records, all seven V51-global contaminations,
   counter completeness, privacy, PASS retention, and one-proof-only cleanup.
2. Commit a direct-byte package for that quartet and obtain an independent
   `gpt-5.6-sol` High implementation/security review with zero unresolved
   Critical, HIGH, IMPORTANT, and Minor findings. Both are offline-only and
   state `authorizes_live_execution=false`.
3. Commit a later non-self-referential classification of only prior V52
   evidence, also with `authorizes_live_execution=false`; then the coordinator
   records a separate post-commit tuple with direct ancestry, all bytes/hashes/
   blobs, exact 12-path baseline, and V52 projection reproduction.
4. Only the sole Sol High owner may decide at action time after re-proving the
   exact projection count/digest, empty index, clean evidence worktree, current
   pins, public-DNS absence, zero local residue, VM1205 safe checkpoint, fresh
   realm reset whose first call is exactly `await cua.getState();`, declaration
   audit, sole token-object lane, and fresh exact external confirmation of
   Chrome Profile `Codex-Chrome-Bell-PC2`, intended window, API Tokens tab, and
   no conflicting controller. Any stale, false, unavailable, or uncertain
   condition stops before a send.

## Exact inherited dirty baseline and commit boundary

V52 must preserve these exact unstaged product statuses: `M`
`open-sse/services/codexQuotaFetcher.ts`; `M`
`src/app/api/v1/models/catalog.ts`; `M` `src/lib/localDb.ts`; `M`
`tests/unit/api/models-agent-route-aliases.test.ts`; `M`
`tests/unit/services/agent-route.test.ts`; and `??`
`open-sse/services/agentRoute.ts`, `open-sse/services/agentRouteObjectives.ts`,
`src/app/api/v1/agent-routes/`, `src/lib/db/agentRouteRuns.ts`,
`src/lib/db/migrations/134_agent_route_runs.sql`,
`tests/unit/api/agent-route-events.test.ts`, and
`tests/unit/db/agent-route-runs.test.ts`. The index stays empty. No product
path or project-root `AGENTS.md` may be staged, modified, reverted, or touched.

Commit only this design path with command-scoped `Codex <codex@local>` identity.
Its sole direct parent is `246c7f9e435ed86df3f10a402b55bd2fd62ddfc9`; it must
change exactly this one path. This design grants no live authority.
