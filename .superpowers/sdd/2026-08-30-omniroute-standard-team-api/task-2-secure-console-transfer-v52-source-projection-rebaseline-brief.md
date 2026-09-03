# V52 source-projection rebaseline brief

## Status and authority

V51 is the immediately preceding consumed gate and is permanently ineligible.
It may not be retried, continued, reused, reinterpreted, relaxed, or made
eligible by V52. V52 is a new replacement gate, consumed before validation or
import. This brief is offline only and grants no live authority.

V52 design provenance is commit `b3fb1b2ce53b0ae0e14e7eef4c8feca0adce2eb1`;
its independent Sol High design PASS is
`06cff4158e1c5b31fe6f2c083e1a2bdd2582e5b8`. This new candidate directly
follows that offline design review; V51 remains immutable evidence only.

## Evidence and narrow decision

V52 pins only the installed `26.901.20858` bundle, reproduced offline before
candidate import: `scripts/browser-client.mjs` is 150611 bytes, SHA-256
`B9B9BC2319D5EE6AA0B1E481D63BB2130D28102FC7C9080803AB5552185D9037`; and
`docs/api.json` is 59294 bytes, SHA-256
`FC7966FFBC9010252AD3EA745E061068BEC3919EFFF860A87E6013A38A7E277F`.
Missing, substituted, or mismatched pins stop V52 before import with no retry.

The sole V52 delta is the owner-authorized fixed-exclusion source projection:
exactly `10619` records with SHA-256
`89D36435A31AE04E560A27D53D8A0953F19E837DF60837FADCF3DC174C0B9477`.
The coordinator must reproduce both constants immediately before any candidate
import; any mismatch, missing evidence, or uncertainty stops before a send.

V52 retains V51's exact one-record URL selection and selects exactly one fully
validated returned record whose URL is:

`https://dash.cloudflare.com/profile/api-tokens`

It does not diagnose, reinterpret, or retry V51.

## Trusted listing and candidate selection

V52 preserves the bounded ordinary-array contract: no symbols, an exact data
`length` descriptor, integer length `1..1000`, exact contiguous index names,
and enumerable data descriptors for every index.

Every offered record is validated before selection:

- non-null ordinary plain record with bounded prototype depth and no symbols;
- own keys limited to `id`, `lastOpened`, `providerTabId`, `tabGroup`, `title`,
  and `url`;
- `id` must be a present enumerable data property; `url` remains optional and,
  when absent, makes that record a nonmatch;
- every present documented value must be a bounded, non-empty, control-free
  string; present `undefined`, accessors, and unknown keys fail before claim;
- each present URL is used only as its already validated safe string; unrelated
  `http:`, internal-scheme, ported, or otherwise nonmatching safe values are
  permitted and are not parsed or subjected to target-origin predicates;
- exactly one record must have URL string equality with
  `https://dash.cloudflare.com/profile/api-tokens`.

Zero or multiple exact matches fail closed. Only that exact returned record is
claimed, exactly once. No tab id is guessed, reconstructed, or emitted.

## Preserved V51, V49, and V4 semantics

After unique candidate selection, V52 mechanically preserves V51's reviewed
flow and all inherited V49/V4 semantic signatures:

1. one pinned runtime import, setup, Chrome connection, complete documentation
   read/write, session name, `openTabs`, and exact-record claim;
2. one navigation to Cloudflare account home, exact account-home URL shape,
   exact `mysw.me` zone-link count `1`, positive anchor count, and zero busy
   indicators;
3. one navigation to the exact API Tokens URL;
4. one visible `search api tokens` textbox with a bounded valid
   `aria-controls`, one controlled results root, one visible paginator, and a
   complete empty or nonempty baseline;
5. one fixed non-secret filter value
   `OmniRoute secure console R5 20260901`, one exact query echo, terminal
   `0-0 of 0`, zero rows, one empty status, disabled paginator controls, and
   zero busy state;
6. exactly one Create Token control and zero exact token-name or matching-row
   occurrences; and
7. exact counters and completeness predicates for every permitted action.

Create is counted but never clicked. V52 contains no Copy, clipboard, secret,
credential, storage, cookie, DNS, routing, VM mutation, provider mutation, tab
creation/close, reconnect, retry, fallback, override, verdict relaxation, or
manual-continuation path.

## Fresh-realm and predecessor guards

V52 is consumed before validation or import. Its fresh-realm guard retains all
historic V35-V49 declarations and adds all seven V51 globals:

- `secureConsoleOwnedTaskTabV51`
- `secureConsoleOwnedTaskTabV51Eligible`
- `secureConsoleOwnedTaskTabV51State`
- `secureConsoleOwnedTaskTabV51PreCreateDetachConsumed`
- `secureConsoleOwnedTaskTabV51PostNativeDetachConsumed`
- `secureConsoleCloudflareReadsV51Consumed`
- `secureConsoleV51Consumed`

A separate direct declaration audit must prove the same set absent immediately
before the live send.

## Output, cleanup, and privacy

Only fixed literals, booleans, bounded counts, exact counters, and fixed-schema
results may be emitted. Raw listings, descriptors, records, identifiers,
titles, URLs, account segments, DOM text, thrown values, credentials, tokens,
and secrets are never emitted or retained.

Exact PASS retains only the owned V52 token-page binding plus minimal
eligibility, state, consumption, and later reviewed detach/read flags. All broad
runtime, browser, documentation, listing, record, URL, and snapshot aliases are
cleared.

Any failure or uncertainty spends V52, clears both V52 tab bindings and every
broad alias, emits at most one fixed sanitized terminal result, and stops
ineligible. Only one fixed state-only cleanup proof is allowed, followed
immediately by realm reset. If the proof fails, there is no corrected or second
query. V52 can never be retried, continued, reused, reinterpreted, or relaxed.

## Review and live prerequisites

Before live execution, all of the following must pass:

- smallest executable and pure fixture derived mechanically from final V51;
- syntax and fixtures covering zero, one, and multiple exact URL matches;
  unrelated safe tabs with absent URL, `http:`, internal-scheme, and explicit-
  port URL values; hostile records; optional-key rejection; counter
  completeness; privacy; PASS retention; and one-proof-only cleanup;
- direct-byte review package and independent `gpt-5.6-sol` High review with
  zero unresolved Critical, HIGH, IMPORTANT, or Minor findings;
- later non-self-referential execution classification and separate coordinator
  tuple proving chain, hashes, empty index, exact 12-path dirty baseline, and
  unchanged outside projection;
- fresh runtime/documentation hashes, clean evidence worktree, public DNS
  absence, zero local residue, VM1205 safe checkpoint, sole token-object lane,
  current task identity, fresh realm, direct declaration audit, and new external
  profile/window/tab/non-conflict confirmation.

The final Create/native Copy/native masked Paste confirmation remains mandatory
at action time. The later exact-row deletion confirmation remains separate and
mandatory. Standing unattended authority does not waive either confirmation or
any higher-priority browser safety boundary.
