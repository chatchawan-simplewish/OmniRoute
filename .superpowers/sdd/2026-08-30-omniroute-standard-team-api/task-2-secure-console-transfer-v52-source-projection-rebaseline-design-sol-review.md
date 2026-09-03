# OmniRoute V52 source-projection rebaseline design Sol High review

Date: 2026-09-03 (Asia/Bangkok)
Reviewer: Codex, independent `gpt-5.6-sol` High design/security review
Exact design commit: `b3fb1b2ce53b0ae0e14e7eef4c8feca0adce2eb1`
Direct parent / final V51 classification: `246c7f9e435ed86df3f10a402b55bd2fd62ddfc9`

## Verdict

`PASS`

`implementation_may_proceed=true`

`authorizes_live_execution=false`

The V52 design is a new consumed-before-validation-or-import, no-retry
replacement for classified historical V51. Its only semantic delta is the
owner-authorized fixed-exclusion source-projection rebaseline to `10619`
records with SHA-256
`89D36435A31AE04E560A27D53D8A0953F19E837DF60837FADCF3DC174C0B9477`,
plus the necessary V52 naming and V51 predecessor guards. No unresolved
Critical, HIGH, IMPORTANT, or Minor finding remains.

## Exact review boundary and provenance

The design was read directly from commit
`b3fb1b2ce53b0ae0e14e7eef4c8feca0adce2eb1`. It is `8170` bytes, SHA-256
`8C8FD45A6EA5789BECF3700F7C47AA2E426316487BACF7114E3C97ED611B7F6A`,
and Git blob `b4d0071a989c779caee8a5466400489c383e760a`. That commit is the direct
child of final V51 classification commit
`246c7f9e435ed86df3f10a402b55bd2fd62ddfc9` and adds exactly the V52
design path. Its author and committer are both `Codex <codex@local>`.

The review compared V52 with the final V51 design, V51 zero-finding design
PASS, corrected candidate lineage, zero-finding fix-1 implementation PASS,
and final non-self-referential V51 classification. V52 does not amend, revive,
reuse, reinterpret, relax, continue, or retry V51.

No CUA, browser, provider, network, VM, DNS, clipboard, credential, secret, or
live action was performed. The index was empty, and the exact inherited
12-path dirty product baseline was neither changed nor staged.

## Current runtime and documentation pins

Direct local byte/hash checks reproduced both declared current pins:

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `C:\\Users\\chatc\\.codex\\plugins\\cache\\openai-bundled\\chrome\\26.901.20858\\scripts\\browser-client.mjs` | 150611 | `B9B9BC2319D5EE6AA0B1E481D63BB2130D28102FC7C9080803AB5552185D9037` |
| `C:\\Users\\chatc\\.codex\\plugins\\cache\\openai-bundled\\chrome\\26.901.20858\\docs\\api.json` | 59294 | `FC7966FFBC9010252AD3EA745E061068BEC3919EFFF860A87E6013A38A7E277F` |

Static inspection confirms the current documentation still declares
`openTabs(): Promise<Array<BrowserUserTabInfo>>` and
`claimTab(tab: string | BrowserUserTabInfo): Promise<Tab>`, with required
string `id` and only the five documented optional fields. The runtime still
returns the transport `tabs` array and accepts the exact returned record by
extracting its string `id`. V52 correctly requires both pins and compatibility
to be reproduced again immediately before candidate import; drift, absence,
substitution, or uncertainty stops before a send.

## Replacement and inherited-security review

- V51 is explicitly immutable, classified historical evidence. V52 is a new,
  separately consumed gate; a validation, import, send, failure, or uncertainty
  spends it without retry, fallback, continuation, or authority reuse.
- The complete bounded ordinary-array contract survives: exact data length
  `1..1000`, contiguous enumerable data indexes, no symbols, and descriptor-safe
  validation of every plain record before selection. Accessors, holes, malformed
  descriptors, unknown keys, present `undefined`, unsafe strings, and hostile
  records fail before claim.
- URL membership remains literal equality with
  `https://dash.cloudflare.com/profile/api-tokens`. Absent URLs and safe
  unrelated HTTP, internal-scheme, explicit-port, or other URLs are nonmatches;
  zero or multiple exact matches fail closed. Rank, normalization, identifier
  reconstruction, guessed references, alternate URLs, and raw listings remain
  prohibited.
- The predecessor boundary advances through V51. The fresh-realm and separate
  direct-declaration audit must prove every V35-V51 declaration absent,
  including all seven exact V51 persistent globals: owned tab, eligibility,
  state, pre-Create detach, post-native detach, Cloudflare-read, and consumed.
- The V51/V50/V49/V4 downstream contract survives unchanged: one pinned
  import, setup, Chrome connection, complete documentation read/write, session
  name, one `openTabs`, one exact-record claim, exact account-home and `mysw.me`
  zone-link signature, exact token-page navigation, bounded bindings, fixed
  non-secret filter, exact empty terminal, count-only never-clicked Create, all
  reviewed counters/completeness predicates, and downstream readiness `4/4`.
- Output remains fixed-schema and sanitized. Raw listings, descriptors,
  records, identifiers, titles, URLs, account segments, DOM text, thrown values,
  credentials, tokens, and secrets are neither emitted nor retained.
- PASS retains only the V52 owned token-page binding and minimal reviewed
  flags while clearing broad aliases. Failure or uncertainty spends V52,
  clears both V52 bindings and broad aliases, permits at most one fixed
  state-only cleanup proof, and then requires immediate realm reset. Cleanup
  proof failure cannot be corrected, queried, or retried.
- Copy, clipboard, credential/token access, storage/cookies, tab creation or
  close, reconnect, retry, fallback, override, alternate path, verdict
  relaxation, manual continuation, and every mutation remain prohibited.
  Final Create/native Copy/native masked Paste confirmation and later separate
  exact-row deletion confirmation remain external, mandatory, and unreached.

## Evidence sequence and authorization boundary

The V52 sequence is complete and fail-closed: commit the smallest candidate
quartet; commit its direct-byte package; obtain an independent zero-finding Sol
High implementation/security review; commit a later non-self-referential
classification of only prior evidence; then record a separate post-commit tuple
covering direct ancestry, all bytes/hashes/blobs, the exact 12-path baseline,
and the V52 projection reproduction. Candidate fixtures must exercise the
full selection, predecessor, counter, privacy, retention, and one-proof-only
cleanup boundary.

Only the sole Sol High owner may later decide action-time eligibility after
freshly proving the authorized `10619`-record projection and exact digest,
empty index, clean evidence state, current pins, public-DNS absence, zero local
residue, VM1205 safe checkpoint, fresh realm/reset and declaration audit, sole
token-object lane, and fresh exact external profile/window/tab/non-conflict
confirmation. Any stale, false, unavailable, missing, or uncertain condition
stops before a send.

This PASS authorizes only offline V52 candidate implementation under the
reviewed design. It does not authorize live execution or consume V52.

## Severity counts

- Critical: 0
- HIGH: 0
- IMPORTANT: 0
- Minor: 0

## Concern

None.
