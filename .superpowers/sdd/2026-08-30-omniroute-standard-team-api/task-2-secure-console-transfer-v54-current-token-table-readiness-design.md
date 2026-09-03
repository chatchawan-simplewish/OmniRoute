# V54 current token-table readiness replacement design

`authorizes_live_execution=false`

## Problem and replacement

V53 was consumed once and failed cleanly because the current Cloudflare User
API Tokens page no longer exposes the reviewed `Search API Tokens`,
`aria-controls`, results-root, or pagination signature. No token or persistent
provider state was created. V53 is permanently spent.

V54 is a new one-shot gate. It preserves V53's attachment, ownership,
fresh-realm, counter, output, cleanup, and no-retry contract and changes only
the downstream token-page readiness signature to match the bounded current UI
observed after V53 cleanup. This design grants no live authority.

## Current-page readiness signature

After exact navigation to `https://dash.cloudflare.com/profile/api-tokens`, V54
must prove all of the following before retaining a task-tab binding:

- exactly one visible `#user-api-tokens-search` text input exists and its value
  is initially empty;
- exactly one visible `Create Token` button or link exists; it is counted and
  never clicked;
- exactly one API-token table exists whose header text contains the ordered
  labels `Token name`, `Permissions`, `Resources`, `Last used`, `Expires`, and
  `Status`;
- the unfiltered table is not busy, contains at least one and at most 1000 body
  rows, and contains zero exact target-name matches;
- filling the exact target name `OmniRoute secure console R5 20260901` is the
  only page mutation;
- the resulting URL has exact HTTPS Cloudflare host and API-token path, no
  fragment, and exactly one query parameter named `search` whose decoded value
  equals the target name;
- the same table becomes non-busy and contains exactly one body row whose
  normalized text is exactly `No results found for your search`;
- the filtered table contains zero exact target-name matches and zero Actions
  controls; and
- all binding, navigation, URL, wait, initial-read, fill, filtered-read,
  Create-read, name-read, and row-read counters match their exact reviewed
  attempted/fulfilled values.

The target-name filter is reversible UI state and may remain applied on PASS;
the separately reviewed creation gate can still use the unique Create control.

## Retained V53 constraints

- One literal direct cell, ASCII, no source read/eval/wrapper/split execution,
  and no dynamic candidate import.
- Candidate size must remain within the already proven `25000`-byte transport
  ceiling; `node --check` and a candidate-length inert direct-cell proof remain
  mandatory.
- Consumed before import or validation; no retry, fallback, correction,
  reconnect, alternate selection, or manual continuation.
- The pinned source projection, browser-client module, documentation, exact
  12-path dirty baseline, empty index, evidence worktree, DNS absence, Windows
  residue, and VM1205 safe-state checks remain unchanged.
- The direct fresh-realm audit must prove all fixed V35-V51 predecessor names
  and all seven V53 persistent declaration names undefined before V54 is sent.
- The ordinary-array descriptor validation, unique exact-URL selection,
  claimed-ID equality, account-home URL and DOM signature, success-only
  persistent binding, fixed sanitized output, and complete failure/output-
  failure cleanup remain unchanged.
- On any false, stale, unavailable, thrown, or uncertain condition, clear every
  candidate/runtime/browser/tab binding, emit sanitized evidence only, and
  stop with V54 permanently spent.

## Prohibited effects

V54 authorizes no token creation, Create click, Copy, clipboard, secret or
credential access, storage/cookie access, DNS, routing, VM, permission, provider
mutation, tab creation/close, alternate browser/profile, or external
communication. Final token creation and secret transfer remain separate and
subject to action-time confirmation required by the browser-control policy.

## Evidence sequence

1. Independent `gpt-5.6-sol` High design/security review must report PASS with
   zero Critical, HIGH, IMPORTANT, and Minor findings and
   `authorizes_live_execution=false`.
2. Implement the smallest direct candidate and one pure fixture. The fixture
   must cover the unchanged V53 trust-boundary matrix plus current-table
   success, old-signature absence, duplicate/missing/wrong search input,
   duplicate/missing/wrong Create control, malformed/duplicate/busy/empty/
   oversized tables, pre-existing target, wrong query state, wrong terminal
   row, target/action residue, exact counters, hostile throws, output failure,
   and contamination by every audited predecessor declaration.
3. Commit a direct-byte review package and obtain independent `gpt-5.6-sol`
   High implementation/security PASS with zero findings.
4. Commit a non-self-referential execution classification and revalidate every
   action-time pin before the single V54 send.

Any failed or uncertain check stops before live execution.
