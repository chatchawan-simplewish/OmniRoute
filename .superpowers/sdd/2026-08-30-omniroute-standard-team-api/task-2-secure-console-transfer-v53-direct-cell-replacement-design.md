# V53 compact direct-cell replacement design

`authorizes_live_execution=false`

## Problem and replacement

V52 is reviewed and unspent, but its 43,728-byte executable cannot be loaded
unchanged through the supported browser-control surface: that surface accepts a
literal JavaScript cell, exposes no file-execution API, rejects string-generated
execution, and a dynamic module import would make the required continuation
bindings module-scoped. No V52 browser attachment, claim, navigation, page read,
provider mutation, credential operation, or secret operation occurred.

V53 replaces V52. V52 becomes historical and permanently ineligible for later
use, retry, continuation, reinterpretation, or fallback. V53 is a new one-shot
gate, consumed before its first import or validation. This design is offline
only and grants no live authority.

## Smallest viable execution surface

V53 must be one literal, directly submitted JavaScript cell. It must not read
source from disk, call `eval`, construct code from strings, dynamically import
the candidate itself, use `vm`, use a wrapper, or split execution across cells.
Only the pinned browser-client module import remains dynamic.

The implementation may delete duplicated internal proof scaffolding where the
same fact is already established by the mandatory separate action-time tuple or
fresh direct declaration audit. It may not simplify input validation, exact URL
selection, unique-match requirements, no-retry behavior, secret boundaries,
cleanup, output privacy, or persistent continuation state.

## Retained pins and semantics

- Source projection: exactly `10619` records, SHA-256
  `89D36435A31AE04E560A27D53D8A0953F19E837DF60837FADCF3DC174C0B9477`,
  using the fixed exclusion of the complete phase evidence directory.
- Browser client: `26.901.20858/scripts/browser-client.mjs`, 150611 bytes,
  SHA-256 `B9B9BC2319D5EE6AA0B1E481D63BB2130D28102FC7C9080803AB5552185D9037`.
- Documentation: `26.901.20858/docs/api.json`, 59294 bytes, SHA-256
  `FC7966FFBC9010252AD3EA745E061068BEC3919EFFF860A87E6013A38A7E277F`.
- The exact 12-path dirty product baseline and empty index remain mandatory.
- The fixed direct fresh-realm audit must prove all 118 V35-V51 declarations
  absent before the one V53 cell.
- The listing must be an ordinary bounded complete array. Every record must be
  descriptor-validated before selection. Exactly one record must have literal
  URL `https://dash.cloudflare.com/profile/api-tokens`; zero, duplicate,
  accessor, symbol, unknown-key, unsafe-string, or malformed records fail before
  claim.
- The claimed tab must pass unchanged account-home semantic readiness, then
  unchanged API-token-page readiness. The exact token-name filter remains
  `OmniRoute secure console R5 20260901`; Create is counted but never clicked;
  the matching token name and row counts must both be zero.
- On exact PASS, retain one eligible task-tab binding for the separately
  reviewed creation gate. On any failure or uncertainty, clear all candidate,
  runtime, browser, and tab bindings, emit only fixed sanitized evidence, and
  stop. No retry, reconnect, alternate selection, correction, fallback, or
  manual continuation exists.

## Prohibited effects

V53 authorizes no token creation, Create click, Copy, clipboard, secret or
credential access, storage/cookie access, DNS, routing, VM, provider mutation,
tab creation/close, alternate browser/profile, or external communication. The
final Create/native Copy/native masked Paste confirmation and later exact-row
deletion confirmation remain separate, mandatory, and unreached.

## Required evidence sequence

1. Independent `gpt-5.6-sol` High design review must report PASS with zero
   Critical, HIGH, IMPORTANT, and Minor findings and
   `authorizes_live_execution=false`.
2. Implement the smallest candidate and one pure fixture. The fixture must
   verify syntax, trusted-listing matrices, exact sanitized output keys,
   success retention, failure cleanup, hostile thrown values, terminal-output
   failure, one-proof-only cleanup, and absence of prohibited calls.
3. Commit a direct-byte review package and obtain independent `gpt-5.6-sol`
   High implementation/security PASS with zero findings.
4. Commit a later non-self-referential execution classification, then record a
   separate coordinator tuple proving ancestry, exact bytes/hashes/blobs,
   projection, index, and dirty baseline.
5. Immediately before live use, freshly prove runtime/docs, clean evidence
   worktree, DNS absence, zero Windows residue, VM1205 safe state, sole lane,
   current task identity, external profile/window/tab/non-conflict confirmation,
   fresh realm whose first call is exactly `await cua.getState();`, and the
   118-name direct declaration audit.

Any false, stale, unavailable, or uncertain condition stops before V53 is sent.

