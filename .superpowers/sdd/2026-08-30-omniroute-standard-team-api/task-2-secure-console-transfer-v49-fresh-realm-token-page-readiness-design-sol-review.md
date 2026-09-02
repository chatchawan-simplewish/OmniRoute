# OmniRoute V49 fresh-realm token-page readiness design Sol High review

Date: 2026-09-03 (Asia/Bangkok)
Reviewer: Codex, independent `gpt-5.6-sol` High security review
Exact design commit: `7cfccd88831ea47027d74212539c6a23f72e572e`
Exact parent/evidence commit: `c8f0adab7d6bcc8773d603ef9d114d6c8936079e`

## Verdict

`FAIL`

`authorizes_live_execution=false`

Two IMPORTANT findings remain. The design is not yet an exact mechanical
V47-to-V49 reissue and does not accurately disposition a recorded V48 cleanup
protocol deviation. No implementation, classification, tuple, CUA, browser,
provider, VM, DNS, secret, or live-gate action is authorized by this review.

## Exact-byte and scope evidence

The V49 design was read directly from commit
`7cfccd88831ea47027d74212539c6a23f72e572e`. It is 9368 bytes, SHA-256
`D18CCB59CE700CA188B4B0955F6BC4EC327E4549E8E40904BDBF662DD1069B7C`,
Git blob `c8015f6b8fe08826534648139300f199cacf92b6`. The design commit has exactly
one changed path and direct parent
`c8f0adab7d6bcc8773d603ef9d114d6c8936079e`, the V48 live-result evidence
commit.

Review inputs read from committed bytes included:

- project-root `AGENTS.md`;
- the V47 brief, 41533-byte executable, and 50343-byte pure fixture;
- the final corrected V48 design, executable, fixture, fix-1 PASS review,
  classification, and live result;
- the V4 replacement, V44, and V46 inherited contracts; and
- the current sequential handoff and exact-path ownership constraints.

No existing suite was rerun. This is a design-only review, and the blocking
questions are proven directly by contradictions in committed text and source.
No CUA, Chrome, provider, network, DNS, VM, secret, clipboard, or authority
gate was accessed.

## Findings

### V49-001 — IMPORTANT — Present `undefined` optional fields broaden V47

The V49 design says every optional documented field may be
"absent/undefined" or a safe string (design line 73). That is not the final V47
trusted-listing predicate the design promises to preserve unchanged.

V47 enumerates every present key and rejects it unless its descriptor value is
a non-empty bounded control-free **string** (V47 executable lines 196-203).
Therefore an optional key may be absent, but if it is present with value
`undefined`, V47 rejects the entire listing. The corrected V48 diagnostic also
kept these as distinct facts: `rankZeroOptionalValuesStringOrUndefined` was a
diagnostic comparison field, while `rankZeroAllValuesV47Safe` represented the
strict historical V47 acceptance predicate. The live V48 result happened to
report both true; it did not authorize broadening V47 for a later fresh listing.

As written, an implementer following the design could claim a record that V47
would have rejected, violating the smallest-mechanical-delta, exact-predicate,
and claim-only-after-full-validation requirements.

Required correction: state exactly that each optional documented key may be
absent, but every **present** optional value must be a bounded non-empty
control-free string. Explicitly forbid present `undefined` in the acceptance
predicate, preserve the strict V47 all-values check, and require a fixture that
proves a present-`undefined` optional key fails before claim while an absent
optional key may pass.

### V49-002 — IMPORTANT — V48's recorded cleanup-proof deviation is not dispositioned

The V49 predecessor section says V48 "completed its read-only listing-shape
diagnostic" and then restates that V48 must never be continued. The committed
V48 live result contains a material qualification that the V49 design omits:
the first permitted state-only cleanup expression failed locally with a
`ReferenceError`, and a second corrected state-only expression was then run
(V48 live result lines 73-78).

That sequence did not call a browser or mutate the provider, and the initial
fixed diagnostic output remains sanitized semantic evidence. It nevertheless
departed from the reviewed V48 design's requirement for **one** state-only
cleanup proof (V48 design line 145) after V48's classification had stated that
any failure, uncertainty, or cleanup doubt spends the gate and forbids
continuation (classification lines 53-55). Describing V48 only as completed
silently normalizes the second query and leaves ambiguous which portion of the
incident V49 is allowed to rely on.

Required correction: record the two-query cleanup deviation explicitly and
fail closed. State that V48 remains spent; the second query is transparent,
non-authorizing incident evidence and is not precedent for a retry or
continuation. Bound V49's inherited evidence to the first fixed sanitized
diagnostic payload plus the eventual realm reset, explain why that payload is
still acceptable for design input, and require V49's cleanup fixture/procedure
to prove one fixed cleanup proof only with no corrected second query.

## Contract review

| Area | Result | Evidence and limit |
| --- | --- | --- |
| Smallest fresh reissue | **FAIL** | The declared four-part mechanical delta is appropriately narrow, but V49-001 changes listing acceptance and V49-002 leaves predecessor authority ambiguous. |
| V47/V48 no retry | **FAIL** | The design correctly forbids reuse of both gates, but it must explicitly disposition the V48 second cleanup query rather than describing an unqualified completion. |
| Trusted listing | **FAIL** | Array structure, rank-zero-only selection, URL origin, exact-record claim, and claim ordering are preserved; present optional `undefined` is not. |
| Claim ordering | PASS | Claim is permitted once only after all cached listing predicates pass, uses the exact returned rank-zero record, and cannot reconstruct from ID. |
| Account-home semantics | PASS | Exact navigation, bounded wait, one URL read, lowercase 32-hex account path, exact `mysw.me` link count, positive anchors, and zero busy indicators are preserved. |
| Token-page semantics | PASS | Exact target URL, visible unique search control, bounded `aria-controls`, unique root/paginator, complete baseline, fixed fill, four readiness waits, empty terminal, Create count, and zero name/row matches are retained. |
| Completeness | PASS | Exact inherited attachment and downstream counter values are mandatory; Create is read-only and never clicked. |
| Failure and cleanup | PASS with predecessor block | V49 itself specifies consumed-first, fixed failure, terminal-write cleanup/rethrow, failure detach, one cleanup proof, reset, and no retry. V48's prior deviation still requires V49-002's explicit disposition. |
| Output and secrets | PASS | Output excludes thrown values and raw listing, ID, URL, DOM, provider, clipboard, credential, and secret data; only fixed literals and bounded structural evidence are allowed. |
| Later confirmations | PASS | Final Create/native Copy/native masked Paste and later exact-row deletion remain external, separate, action-time, mandatory, and unreached. |
| Review/action gates | PASS | Exact executable/fixture, direct-byte package, zero-finding Sol High PASS, non-self-referential classification, post-commit tuple, action-time pins, fresh realm, declaration audit, external tab confirmation, and conflict absence are all required before any send. |

## Preserved boundaries

- V47 remains consumed and historically failed at listing validation. Its
  cause remains **NOT PROVEN**; no V49 text may retry or reinterpret it.
- V48 remains consumed, diagnostic-only, and permanently ineligible for tab
  adoption or provider mutation. Its sanitized listing payload does not itself
  authorize V49 execution.
- V49 is one-shot and consumed before validation/import. Any failure,
  interruption, timeout, drift, output failure, cleanup doubt, or uncertainty
  spends it without retry, fallback, reconstruction, alternate selector/URL,
  manual continuation, or verdict relaxation.
- The pinned runtime/documentation, clean evidence worktree, public DNS
  absence, zero local residue, VM1205 checkpoint, sole lane ownership, current
  task identity, exact 12-path baseline, projection, fresh realm, declaration
  audit, and new external selected-tab confirmation remain action-time gates.
- V49 may retain only its exact owned token-page binding and minimal reviewed
  flags on PASS. Every broad runtime/listing/descriptor/record/URL/snapshot
  alias must be cleared; failure retains no eligible or tab binding.
- Create is only counted during readiness. The agent may not inspect the
  generated-token page or clipboard after Create; the owner-only native
  sequence and later exact-row deletion confirmation remain unchanged.

## Severity counts

- Critical: 0
- HIGH: 0
- IMPORTANT: 2
- Minor: 0
