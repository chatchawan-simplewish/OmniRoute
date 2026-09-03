# V51 runtime-pin refresh brief

## Status and authority

V49 was consumed once, failed closed before claim, and is permanently
ineligible. Its sanitized live result is committed at `d1c70a8a0`. V49 may not
be retried, continued, reused, reinterpreted, or relaxed.

V51 is a new one-shot replacement. This design does not authorize live
execution. Live execution requires committed candidates, independent Sol High
PASS review, a later non-self-referential execution classification, a separate
post-commit coordinator tuple, and fresh action-time pins.

## Evidence and narrow decision

V51 pins only the installed `26.901.20858` bundle, reproduced offline before
candidate import: `scripts/browser-client.mjs` is 150611 bytes, SHA-256
`B9B9BC2319D5EE6AA0B1E481D63BB2130D28102FC7C9080803AB5552185D9037`; and
`docs/api.json` is 59294 bytes, SHA-256
`FC7966FFBC9010252AD3EA745E061068BEC3919EFFF860A87E6013A38A7E277F`.
Missing, substituted, or mismatched pins stop V51 before import with no retry.

V49 completed import, setup, Chrome connection, documentation validation,
session naming, and exactly one `openTabs` call. It stopped with
`listingValidated=false`, sanitized `offeredCount=-1`, and zero claim or later
actions. The exact rejecting property is **NOT PROVEN** because V49 prohibited
raw-listing output.

The owner has confirmed that other tasks may use other tabs in the same Chrome
profile, while no other task controls the intended Cloudflare API Tokens tab or
Cloudflare token object. Therefore recency rank is not a stable ownership
predicate. V51 removes only the rank-zero assumption and selects exactly one
fully validated record whose URL is exactly:

`https://dash.cloudflare.com/profile/api-tokens`

It does not diagnose, reinterpret, or retry V49.

## Trusted listing and candidate selection

V51 preserves the bounded ordinary-array contract: no symbols, an exact data
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

## Preserved V49 and V4 semantics

After unique candidate selection, V51 mechanically preserves V49's reviewed
flow and all inherited V4 semantic signatures:

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

Create is counted but never clicked. V51 contains no Copy, clipboard, secret,
credential, storage, cookie, DNS, routing, VM mutation, provider mutation, tab
creation/close, reconnect, retry, fallback, override, verdict relaxation, or
manual-continuation path.

## Fresh-realm and predecessor guards

V51 is consumed before validation or import. Its fresh-realm guard requires all
established persistent V35-V49 declarations absent, including all seven V49
globals:

- `secureConsoleOwnedTaskTabV49`
- `secureConsoleOwnedTaskTabV49Eligible`
- `secureConsoleOwnedTaskTabV49State`
- `secureConsoleOwnedTaskTabV49PreCreateDetachConsumed`
- `secureConsoleOwnedTaskTabV49PostNativeDetachConsumed`
- `secureConsoleCloudflareReadsV49Consumed`
- `secureConsoleV49Consumed`

A separate direct declaration audit must prove the same set absent immediately
before the live send.

## Output, cleanup, and privacy

Only fixed literals, booleans, bounded counts, exact counters, and fixed-schema
results may be emitted. Raw listings, descriptors, records, identifiers,
titles, URLs, account segments, DOM text, thrown values, credentials, tokens,
and secrets are never emitted or retained.

Exact PASS retains only the owned V51 token-page binding plus minimal
eligibility, state, consumption, and later reviewed detach/read flags. All broad
runtime, browser, documentation, listing, record, URL, and snapshot aliases are
cleared.

Any failure or uncertainty spends V51, clears both V51 tab bindings and every
broad alias, emits at most one fixed sanitized terminal result, and stops
ineligible. Only one fixed state-only cleanup proof is allowed, followed
immediately by realm reset. If the proof fails, there is no corrected or second
query. V51 can never be retried, continued, reused, reinterpreted, or relaxed.

## Review and live prerequisites

Before live execution, all of the following must pass:

- smallest executable and pure fixture derived mechanically from final V50;
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
