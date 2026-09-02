# OmniRoute V49 fresh-realm token-page readiness design fix-1 Sol High review

Date: 2026-09-03 (Asia/Bangkok)
Reviewer: Codex, independent `gpt-5.6-sol` High security review
Exact corrected design commit: `6fd3669ce2dfa0763e2a1a137f86d65b4edf0ff9`
Direct parent / prior FAIL review: `ded48d8a4dd412aa3e6a524dd36fbae63b1dc7b7`

## Verdict

`PASS`

`authorizes_live_execution=false`

Both prior IMPORTANT findings, V49-001 and V49-002, are closed. Regression
review found no unresolved Critical, HIGH, IMPORTANT, or Minor finding in the
corrected design. This is design approval only: no executable, fixture, review
package, execution classification, post-commit tuple, or action-time gate has
yet been approved by this artifact.

## Exact-byte and ancestry evidence

The corrected V49 design was read directly from commit
`6fd3669ce2dfa0763e2a1a137f86d65b4edf0ff9`. It is 10510 bytes, SHA-256
`0D481DB643A01051784C25D4CC831A4A138AA6782FE7AA37CDC639D119152537`,
Git blob `a656719c528d1fcd20ccea301cb94e4628b16ace`. The fix commit has exactly one
path, the V49 design, and its direct parent is the prior FAIL review commit.

The required predecessor inputs were read from committed bytes and are
unchanged across the fix commit:

| Input | Git blob |
| --- | --- |
| V47 brief | `91c4954fac980da63586cc8a8856d5c59bea83d5` |
| V47 executable | `087c3ec28c414abc66dd5db0a58405fb635061f4` |
| V47 pure fixture | `6efab96fadc7e1b4613b1db7a3db38a120af6d86` |
| Corrected V48 design | `232abfed08475b9fec17a5c21a6299db3fbc6720` |
| Corrected V48 executable | `544cadd03fc4049d7a4cda6074f62c8aa40190cc` |
| Corrected V48 pure fixture | `b0017298e1826dd6c8946f08094167b6ca8268f7` |
| V48 fix-1 PASS review | `4f27bcc737210215c9b33d245b3cf98ee5b33521` |
| V48 classification | `e1d274df38b3b1e775fc4c17497bd2842542e71a` |
| V48 live result | `7ee54b84afd6a407074fa678dfa5fe7831cc58d1` |

Project-root `AGENTS.md`, the prior V49 FAIL review, and the inherited V4/V44/V46
semantic and confirmation constraints were also rechecked. No suite was rerun:
this is a design-only fix review and the exact text plus unchanged predecessor
bytes resolve the two concrete findings without an executable test doubt. No
CUA, browser, provider, network, VM, DNS, secret, clipboard, or live-gate action
was performed.

## Finding closure

### V49-001 — CLOSED

The trusted-listing text now matches the strict V47 predicate:

- an optional documented key may be absent;
- every present optional key must contain a bounded, non-empty, control-free
  string; and
- a present optional key with `undefined` is explicitly rejected.

The verification contract now requires both an absent-optional-key fixture that
may pass and a present-`undefined` fixture that must fail before claim. This
preserves V47's strict all-values predicate and prevents any broader claim
eligibility from being inferred from V48's diagnostic-only comparison field.

### V49-002 — CLOSED

The predecessor section now records the V48 incident without normalization:

- the first fixed sanitized diagnostic payload preceded cleanup and is the
  only listing-shape input used by V49;
- the first permitted cleanup proof failed locally with `ReferenceError`;
- the second corrected query is explicitly classified as a deviation and
  transparent, non-authorizing incident evidence;
- the second query is not precedent for retry, correction, or continuation;
  and
- V49 relies only on the first sanitized payload plus the eventual confirmed
  realm reset, while V48 remains consumed and permanently unusable.

The V49 cleanup contract additionally states that if its sole fixed cleanup
proof fails, no corrected or second query is allowed: reset immediately and
record uncertainty. Fixture coverage must prove that one-proof-only behavior.

## Regression review of previously passing areas

| Area | Verdict | Verified boundary |
| --- | --- | --- |
| Smallest fresh-session reissue | PASS | Implementation is constrained to mechanical V47-to-V49 declaration/literal/fixture renaming plus the complete V35-V48 declaration guard. No new browser API or behavior is authorized. |
| V47/V48 disposition | PASS | Both predecessors are consumed, non-reusable, non-authorizing, and cannot be retried, continued, relaxed, reinterpreted, or used as fallback. V47's historical cause remains NOT PROVEN. |
| Trusted listing | PASS | Exact array, descriptor, rank-zero, ordinary-record, symbol, documented-key, strict present-value, safe ID, optional URL, full Cloudflare-origin, and exact-record claim predicates are preserved. Later ranks are not inspected as records. |
| Claim ordering | PASS | Claim occurs exactly once only after every cached listing predicate passes; the exact returned rank-zero record is used and ID reconstruction is forbidden. |
| Account-home semantics | PASS | Fixed navigation, bounded wait, one URL read, exact HTTPS host and lowercase 32-hex home path, one `mysw.me` link, positive anchors, and zero busy indicators remain mandatory. |
| Token-page semantics | PASS | Exact URL, unique visible search control/root/paginator, complete baseline, fixed non-secret fill, four readiness waits, exact empty terminal, Create count one, and name/row count zero remain mandatory. |
| Completeness | PASS | Every inherited V47 attachment and downstream counter keeps its exact reviewed value; Create is counted but never clicked. |
| Failure/no residue | PASS | Consumed-first, fixed/unbound error handling, terminal-output cleanup/rethrow, complete failure detachment, one cleanup proof, immediate reset, and no correction/retry are explicit. PASS retains only the owned task-tab binding and minimal flags. |
| Output/secrets | PASS | Raw listing, descriptor, prototype, record, ID, URL, DOM, provider metadata, thrown value, clipboard, credential, and secret data are excluded from output and evidence. |
| Prohibited actions | PASS | No Copy, clipboard, Create click, credential read, storage/cookie read, DNS/routing/VM/provider mutation, tab creation/close, reconnect, fallback, override, alternate path, or manual continuation is permitted. |
| Review and action gates | PASS | Exact executable/fixture, direct-byte package, zero-finding Sol High review, later non-self-referential classification, separate tuple, action-time pins, fresh realm, declaration audit, exact external tab confirmation, and no conflicting controller remain mandatory. |
| Later confirmations | PASS | Final Create/native Copy/native masked Paste and later exact-row deletion remain external, separate, action-time, mandatory, and unreached. |

## Remaining authorization boundary

This PASS permits the next design-to-implementation step only. Before any live
send, the future exact executable and fixture must independently satisfy and
pin this design, receive a fresh zero-finding Sol High review, then receive a
non-self-referential classification and separate post-commit coordinator tuple.
All runtime/documentation, worktree, projection, DNS, residue, VM1205, ownership,
task-identity, fresh-realm, declaration-audit, selected-tab, and conflict checks
must pass again at action time. Any mismatch stops fail-closed.

## Severity counts

- Critical: 0
- HIGH: 0
- IMPORTANT: 0
- Minor: 0
