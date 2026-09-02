# OmniRoute V49 fresh-realm token-page readiness fix-1 Sol High review

Date: 2026-09-03 (Asia/Bangkok)
Reviewer: Codex, independent `gpt-5.6-sol` High implementation/security review
Fix-1 review-package commit: `41c5c4803762f135450a6db769683c8ab49a10db`
Exact fix commit: `7a506bcd21e87882236879072d7ba92125f122fd`
Fix parent / prior FAIL review: `ac7a04d9dbdfd5d0b698ed81c892f801deccbcb1`

## Verdict

`PASS`

`authorizes_live_execution=false`

V49-001 and V49-002 are closed. Regression review of the exact corrected
brief, executable, implementation plan, pure fixture, and fix package found no
unresolved Critical, HIGH, IMPORTANT, or Minor finding. This review permits
only the later classification step; it does not authorize a CUA or live send.

## Exact-byte and ancestry evidence

The fix commit is the direct child of the prior FAIL review and changes exactly
the V49 brief, executable, implementation plan, and pure fixture. The fix-1
package is its direct child and changes exactly one package path. The four fixed
candidate blobs remain unchanged at the package commit.

| Artifact | Bytes | SHA-256 | Git blob |
| --- | ---: | --- | --- |
| V49 design | 10510 | `0D481DB643A01051784C25D4CC831A4A138AA6782FE7AA37CDC639D119152537` | `a656719c528d1fcd20ccea301cb94e4628b16ace` |
| V49 design fix-1 PASS review | 7229 | `1E4AB13FD0E0996379749EFC47BC0CE855476635A9BE36D1BF0D59760CA6E808` | `caa289fce7db814dd604b885201f9eab8994d272` |
| Corrected implementation plan | 3642 | `D43C9B370C66A7669126494186E8E2A0007F16BABD3CA7D7E1528EEA6DF2F753` | `7dc10a62b7e5e224328ff239530b8aeb2ce126a1` |
| Corrected brief | 5575 | `6A163D6C508DD0A47EDAE8E125F8E3BF013C5C6EE8A303EEC5066C8E44E9AEB7` | `f9f5fac1a2c767344f5f07e77c79f6e1cf66ad6a` |
| Corrected executable | 42193 | `D60CC7898F509013D19DFF1E7254065F5C2FF531386211A348CDF392F3D59988` | `126b81d3f9ace97ca0afdae514a3c4f3305b3b6c` |
| Corrected pure fixture | 52056 | `31A060E86A08432C56676B2D1A2A1C3107CD9076A16399C9BDF28A77E9B92585` | `80a0c3de005e1e8730257c3421edfe25daaf2975` |
| Fix-1 review package | 6449 | `0309321ADCE91B3FFA36CA590E41BC558B02F98529D6AAA1B53552B2B591B085` | `60d9730be6be1ca2b62f3f00ae2e0acb0873849a` |

The original review package remains blob
`a7b86ea1efff2160f3443d2be11324b6407709fb`; the prior FAIL review remains
blob `58e9d586c9cf9566ae9e37d8ae49df1e4e1182fc`. The final V47
brief/executable/fixture blobs remain
`91c4954fac980da63586cc8a8856d5c59bea83d5`,
`087c3ec28c414abc66dd5db0a58405fb635061f4`, and
`6efab96fadc7e1b4613b1db7a3db38a120af6d86`. The final corrected V48
design/executable/fixture/PASS-review/classification/live-result blobs remain
`232abfed08475b9fec17a5c21a6299db3fbc6720`,
`544cadd03fc4049d7a4cda6074f62c8aa40190cc`,
`b0017298e1826dd6c8946f08094167b6ca8268f7`,
`4f27bcc737210215c9b33d245b3cf98ee5b33521`,
`e1d274df38b3b1e775fc4c17497bd2842542e71a`, and
`7ee54b84afd6a407074fa678dfa5fe7831cc58d1`.

The installed pinned browser module remains 149771 bytes with SHA-256
`A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`;
the paired `docs/api.json` remains 58480 bytes with SHA-256
`A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.
These observations are review evidence only and must be revalidated at action
time.

No CUA, browser, provider, network, VM, DNS, clipboard, secret, or live-gate
action was performed. The already-passing fixture was not rerun because the
exact fix diff, direct candidate bytes, and independent normalized comparison
resolved both prior findings without a remaining runtime doubt.

## Prior-finding closure

### V49-001 — CLOSED

The executable now adds exactly one `typeof ... === "undefined"` guard for each
of V47's seven persistent top-level declarations, followed by the three V48
diagnostic declarations. The fixture adds exactly one inert contamination
prelude for each of those ten names. Every contaminated path remains consumed,
ineligible, and detached and proves zero import/setup/documentation/name/
`openTabs`/claim/navigation attempts before the fixed failure result.

The predecessor boundary is therefore complete through V48. The external
action-time declaration audit through V49 remains mandatory defense in depth
and is not replaced by these internal checks.

### V49-002 — CLOSED

The fixture now contains a separate inert coordinator-cleanup model with two
scenarios: fixed-proof success and fixed-proof failure. Each asserts exactly one
proof attempt, zero corrected-query attempts, exactly one reset, and exact
order `proof` then `reset`. Its aggregate fixed terminal reports two scenarios,
two proof attempts, zero corrections, two resets, and
`oneProofOnlyCleanup=true`.

The model performs no browser or provider action and does not place an external
cleanup query inside the V49 executable. It closes the V48-incident regression
requirement while preserving coordinator ownership: a failed proof cannot be
corrected or retried and is followed by immediate realm reset.

## Normalized-delta verification

An independent direct-line normalization reproduced both package claims:

- after mapping V49 names/literals to V47, removing exactly the seven V47 and
  three V48 predecessor guard lines, and restoring the V46 terminal
  conjunction, the executable equals the final V47 executable exactly;
- after the same version mapping, removing exactly ten contamination cases,
  the absent-optional and present-`undefined` assertions, the inert cleanup
  model and its five terminal fields, and restoring the V46 predecessor label,
  the fixture equals the final V47 fixture exactly.

The executable therefore has no browser/provider behavior delta beyond the ten
required declaration guards. The fixture-only additions are bounded to the two
closed findings and do not broaden live semantics.

## Regression and security review

| Area | Verdict | Verified boundary |
| --- | --- | --- |
| One-shot and no retry | PASS | V49 is consumed before validation/import. One import, setup, Chrome connection, documentation read/write, session name, `openTabs`, exact-record claim, each navigation/URL read/snapshot, and fixed fill remain the maximum. No retry, reconnect, fallback, alternate route, override, relaxation, or continuation exists. |
| Trusted listing | PASS | Array/name/length/index descriptors, ordinary rank-zero record, symbols, allowed keys, safe ID, strict present-value strings, absent optional acceptance, present `undefined` rejection, and complete optional URL-origin checks remain exact. Later ranks are not inspected as records. |
| Claim ordering | PASS | The exact cached rank-zero object is passed once to `claimTab` only after every listing predicate passes; no ID reconstruction or pre-validation claim/navigation/page operation exists. |
| Account home | PASS | Fixed navigation, one bounded wait, one URL read, exact HTTPS host plus lowercase 32-hex `/home`, one `mysw.me` zone link, positive anchors, and zero busy state remain mandatory. |
| Token page | PASS | Exact URL, unique visible search/root/paginator, complete empty-or-nonempty baseline, fixed filter, exact echo and empty status, terminal `0-0 of 0`, zero rows, disabled controls, no busy state, Create count one, and name/row counts zero remain mandatory. |
| Completeness | PASS | Attachment counters remain exact one/one and downstream readiness remains exactly four attempts/four fulfillments. Failure-stage and counter-mismatch vectors remain unchanged. |
| Cleanup and residue | PASS | PASS retains only the owned V49 task-tab binding plus minimal flags. Failure and terminal-output failure detach both bindings, clear runtime/evidence aliases, avoid a second terminal write, and leave consumed/ineligible state; post-failure cleanup is one proof then reset only. |
| Hostile inputs | PASS | Listing accessors are rejected through descriptor inspection, later-rank values are not dereferenced as records, thrown values are caught unbound, and output/throw getters remain uninvoked. |
| Output and secrets | PASS | Output remains fixed-schema booleans/bounded counts/counters plus sanitized attachment evidence. No raw listing, descriptor, record, identifier, title, URL, account segment, DOM text, thrown value, credential, token, clipboard, or secret is emitted or retained. |
| Prohibited mutation | PASS | Create is counted but never clicked. There is no Copy, clipboard, credential, storage/cookie, DNS, route, VM, provider mutation, or tab create/close path. |
| Predecessor disposition | PASS | V47 and V48 remain spent, ineligible, non-authorizing, and unavailable for retry, continuation, reuse, reinterpretation, or relaxation. V47's historical cause remains NOT PROVEN; V48's second cleanup query remains a disclosed non-authorizing deviation and no precedent. |
| Confirmations | PASS | New exact profile/window/tab/non-conflict confirmation is still required before the send. Final Create/native Copy/native masked Paste and later exact-row deletion confirmations remain separate, external, mandatory, and unreached. |

## Remaining authorization boundary

This PASS does not authorize live execution. A later non-self-referential
classification whose parent is exactly this review commit, followed by a
separate coordinator tuple, is required. Action time must still revalidate the
candidate/runtime/documentation pins, clean evidence worktree, public DNS
absence, zero local residue, VM1205 safe checkpoint, exact 12-path dirty
baseline, stable projection, sole live-resource lane, current task identity,
fresh CUA realm, fixed complete declaration audit, and new exact external
Chrome Profile `Codex-Chrome-Bell-PC2` window/tab/non-conflict confirmation.
Any mismatch stops fail-closed and does not permit reuse of V49.

## Severity counts

- Critical: 0
- HIGH: 0
- IMPORTANT: 0
- Minor: 0
