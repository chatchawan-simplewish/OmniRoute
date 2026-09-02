# OmniRoute V50 unique-URL token-page reacquisition Sol High implementation review

Date: 2026-09-03 (Asia/Bangkok)
Reviewer: Codex, independent `gpt-5.6-sol` High implementation/security review
Review-package commit: `0fa0ee60e2fe369c4709f5f81d299486e3cd3773`
Candidate commit: `ccdc4f9eebc92a002764a8744527a2cc134488d5`
Candidate parent: `f322e5dd98ef90c860b5aabb1e870ab21ad71bac`

## Verdict

`PASS`

`authorizes_live_execution=false`

Direct-byte review found zero unresolved Critical, HIGH, IMPORTANT, or Minor
findings. The V50 candidate implements the corrected unique-literal-URL
selection contract without weakening V49/V4 one-shot, privacy, cleanup,
counter, retention, or prohibited-action boundaries.

## Exact review boundary and provenance

The candidate commit is the direct child of its implementation handoff and
adds exactly the four declared V50 paths. The review-package commit is the
direct child of the candidate and changes exactly the one package path. The
four candidate blobs are unchanged at the package commit.

| Artifact | Bytes | SHA-256 | Git blob |
| --- | ---: | --- | --- |
| Brief | 6142 | `5355D31F21E97B1C6D74ECA7C4EB2DB21D091FCA2FFE712BE90A9587712B943D` | `a78499f6b3c0f6beada4eb2cd6f300a31da17e5e` |
| Implementation plan | 3184 | `ACD734F9542110A1F4D286CC3363E52967650F33EF21E973236F9BA8E0DF0228` | `76071bbb6c57360ddc5827a5c1019e3a9a4c3fed` |
| Executable | 42583 | `081E4AAD064E7F164E9A597396E4710158D11C85D2B448134D4722DC928E5433` | `f13f4e1326250465bf4f30ed742096097add92ec` |
| Pure fixture | 52118 | `51A79ED3196769768C34000F6BF29C8B0C82503AF1BE3D381C3B837DC78C1FFD` | `e97f1fd138bca94ea82081941e9707aa5e8ebdda` |

The review read the four candidate files directly from the candidate commit,
the corrected V50 design and its zero-finding fix-round design review, the
final V49 design/brief/executable/fixture/fix-round PASS/live result, and the
inherited V4 replacement semantics and static PASS. The corrected V50 design
blob remains `a1afd0ca9aee5910cf131a06882a92b993005681`.

No CUA, browser, Chrome, provider, network, VM, DNS, clipboard, credential,
secret, or live action was performed. The already-passing fixture was not
rerun because direct-byte and normalized-delta review raised no concrete doubt.
The pre-review index was empty, and the exact pre-existing 12-path product
dirty baseline was neither changed nor staged.

## Complete trusted-listing and selection review

The implementation validates the complete offered array before claim:

- `Array.isArray` must pass; own symbols are forbidden; `length` must be an
  exact non-enumerable data descriptor with safe integer value `1..1000`;
  own names must be exactly `length` plus every contiguous canonical index;
  and every index must be an enumerable data descriptor.
- Every indexed value is visited before `trustedListing` returns. Each must be
  a non-null ordinary plain record at the reviewed bounded prototype depth,
  with zero symbols and only `id`, `lastOpened`, `providerTabId`, `tabGroup`,
  `title`, and `url` own keys.
- `id` is required. Every present field, including `url`, must be an enumerable
  data property containing a bounded, non-empty, control-free string. Accessor
  properties, present `undefined`, unknown keys, symbols, malformed descriptors,
  primitive/class records, holes, and hostile later records fail before claim.
- Absent `url` is a safe nonmatch. Present unrelated safe strings, including
  `http:`, internal-scheme, and explicit-port values, are not parsed and remain
  nonmatches.
- Candidate membership is exactly one literal string equality with
  `https://dash.cloudflare.com/profile/api-tokens`. Zero matches and a second
  exact match return failure before claim. Only the exact returned record is
  retained locally and passed once to `claimTab`; no ID reconstruction, rank
  assumption, guessed reference, normalization, alternate URL, or broad-origin
  predicate exists.

The fixture bytes cover the exact match at nonzero rank beside absent-URL,
HTTP, internal-scheme, explicit-port, and otherwise unrelated safe records;
zero and duplicate exact matches; array/index/record descriptor hostility;
later hostile records after an early target; symbols, unknown keys, class and
primitive records, boundary strings, and present `undefined`. Its identity and
privacy checks prove selection by exact object identity and exclude IDs and the
target URL from serialized evidence.

## V49/V4 regression, guards, counters, and cleanup

After replacing only the V50 trusted-listing block with final V49's block,
removing the seven V49 predecessor guards, mapping the two renamed evidence
fields and one fixed error literal, and renaming V50 literals to V49, the
executable is byte-for-byte identical to the final reviewed V49 executable.
Accordingly the account-home signature and all inherited V4 token-page
semantics remain unchanged.

The fresh-realm predecessor expression contains `104` unique V35-V49 guards:
V35 `10`; each of V36-V47 `7`; V48 `3`; and V49 `7`. The seven V49 guards are
exactly the owned binding, eligibility, state, pre-Create detach flag,
post-native detach flag, Cloudflare-read flag, and consumed flag. The fixture
contains a separate contamination case for each and proves zero import/setup/
documentation/name/`openTabs`/claim/navigation attempts on rejection.

Static operation cardinality remains one pinned import, one setup, one Chrome
connection, one documentation read/write, one session name, one `openTabs`,
one exact-record `claimTab`, two navigations, one bounded account wait, two URL
reads, the inherited bounded semantic reads, and one fixed non-secret fill.
There are zero click, tab-create, tab-close, reconnect, retry, fallback,
override, alternate-route, or manual-continuation paths. Create is counted
exactly once but never clicked. Attachment and downstream completeness
counters remain the exact V49 values; downstream readiness is `4/4` on PASS.

Exact PASS retains only the V50 owned token-page binding plus minimal
eligibility, state, consumed, and later-reviewed detach/read flags. It clears
the attachment binding, setup function, agent, Chrome controller, and broad
listing/record/URL/snapshot aliases. Any failure clears both bindings and all
broad aliases, leaves V50 consumed and ineligible, and emits at most one fixed
sanitized result. Terminal-output failure repeats local cleanup and rethrows
without inspecting the thrown value or writing again.

Output remains limited to fixed literals, booleans, bounded counts, exact
counters, and fixed-schema evidence. No raw listing, descriptor, record, ID,
title, URL, account segment, DOM text, thrown value, credential, token, or
secret is emitted or retained. The fixture preserves the separate coordinator
cleanup model with exactly one state-only proof attempt, zero correction
attempts, and exactly one immediate reset in both proof-success and
proof-failure scenarios.

V49 remains consumed, permanently ineligible, and unavailable for retry,
continuation, reuse, reinterpretation, or relaxation; its exact historical
listing rejection remains **NOT PROVEN**. V50 is consumed before validation or
import and provides no retry, continuation, fallback, override, or mutation.
Final Create/native Copy/native masked Paste confirmation and later exact-row
deletion confirmation remain separate, external, mandatory, and unreached.

## Authorization boundary

This PASS permits only the later non-self-referential execution-classification
step. It does not authorize a live send. Live execution still requires that
classification as this review commit's direct child, a separate coordinator
tuple, exact action-time candidate/runtime/documentation and repository pins,
fresh realm, the complete reviewed direct declaration audit, sole token-object
lane, and a new exact external profile/window/tab/non-conflict confirmation.
Any mismatch stops fail-closed and does not permit reuse of V50.

## Severity counts

- Critical: 0
- HIGH: 0
- IMPORTANT: 0
- Minor: 0

## Concern

None.
