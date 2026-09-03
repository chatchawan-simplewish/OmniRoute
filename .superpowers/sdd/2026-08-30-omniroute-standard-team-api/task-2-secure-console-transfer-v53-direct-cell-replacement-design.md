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

## Smallest viable execution surface and measurable transport proof

V53 must be one literal, directly submitted JavaScript cell. It must not read
source from disk, call `eval`, construct code from strings, dynamically import
the candidate itself, use `vm`, use a wrapper, or split execution across cells.
Only the pinned browser-client module import remains dynamic.

The committed executable must be ASCII and no more than **16,000 UTF-8 bytes**.
Before implementation review, a disposable freshly reset browser-control realm
must accept and execute one inert literal cell whose actual tool `code` payload
is at least the candidate's exact byte length. The inert cell may contain only
an ASCII block comment plus one fixed `nodeRepl.write` marker; it must not import,
attach, enumerate, claim, navigate, inspect a page, create a binding, or perform
any provider action. Record the tested payload byte count and PASS marker in the
direct-byte review package, then reset that disposable realm. Candidate syntax
must also pass `node --check`. Failure or uncertainty blocks classification and
live use; it does not consume V53.

Compression is mechanical only: shorten local identifiers, share pure local
helpers, remove comments/whitespace, and consolidate duplicate sanitized-output
assembly. V53 must retain runtime enforcement for every V52 trust boundary:
consumed-before-import; fresh declarations; pinned import/API shapes; complete
documentation signature; bounded ordinary-array and descriptor validation of
every offered record; unique exact-URL selection; claimed-ID equality; tab API
shape; account-home URL and DOM signature; token-page URL, filter binding,
pagination completeness, exact query echo, terminal-zero result, Create count,
name count, row count, exact operation counters; success-only persistent binding;
failure and output-failure cleanup; and fixed sanitized output. The external
tuple and direct audit supplement these checks and never replace runtime
enforcement.

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
   failure, one-proof-only cleanup, absence of prohibited calls, every exact
   operation-counter and completeness vector, and contamination by each of the
   fixed 118 V35-V51 predecessor declarations. Every predecessor-contamination
   case must fail before import, attachment, or browser effects. Every
   operation-counter or completeness mismatch must fail at the earliest
   checkpoint after its relevant attempted effect, permit no subsequent effect,
   and preserve exact attempted/fulfilled vectors for every permitted stage.
   All such failures leave V53 consumed, ineligible, cleaned, and sanitized.
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
