# OmniRoute V43 fresh-realm token-page readiness package fix2 — Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Verdict

**PASS**

V43-002 and V43-003 are fully closed. The fix2 fixture now exercises the
previously absent listing, declaration-freshness, dirty-default, URL-rejection,
counter, and final-output-state cases. The V43 executable is byte-identical to
the fix1 executable whose V43-001 cleanup correction and inherited V41/V42/V4
security semantics were already reviewed. No unresolved Critical, HIGH,
IMPORTANT, or Minor finding remains in this static package review.

This PASS is a package-quality verdict only. It does not authorize live
execution, consume V43, satisfy action-time pins, or replace either mandatory
external confirmation.

## Reviewed lineage and exact package

- Fix1 package: `9ebc089bb35f1e86cc50e3353917b9c9f7a92050`.
- Fix1 FAIL review:
  `e921e44c8430528ab2dc1ff1cc3db2a3d17a21cb`.
- Reviewed fix2 commit:
  `58b64d3cc97a62668e9ff420a12dfce2fd148426`.
- The reviewed fix2 is directly parented by the fix1 FAIL review and changes
  exactly the assigned V43 brief and pure fixture. The executable is unchanged
  from fix1.
- Brief: `6881` bytes; SHA-256
  `E2BFD7C00A77A282BA1BB30FA0C0F9DD5F3FC05A593234D6A759C8429A4132C1`;
  blob `a900ae26269863ae5083a7465d726b4f599f2bae`.
- Executable: `39193` bytes; SHA-256
  `13E56326548D660B111DDC63857BFD33250A548F7D094FA4131EEBB694D24B01`;
  blob `a1d4f0cb1351fa4c11714c56e008958dabd6ca55`.
- Pure fixture: `45511` bytes; SHA-256
  `4BAE1CE107930217EF5E171D6FD9704AC6D4EE87C9D6FAE365C57CC88FD496A5`;
  blob `56b59b2242168f0395a89f3cd6d204b43c1ac1ae`.
- Each package file has exactly one final LF. The fix2 diff passes
  `git diff-tree --check`.
- The executable and fixture each pass a fresh syntax-only check. Per the
  explicit review rule, I did not rerun the already-passing inert fixture
  because direct-byte inspection raised no concrete execution doubt.
- The index was empty before review work, and the exact existing 12-path
  product dirty baseline was preserved.

Review activity was limited to direct committed bytes, commit ancestry and
scope, hashes/blobs, syntax-only checks, the prior review, and the fixture's
assertion matrix. No CUA, Chrome, runtime setup, `openTabs`, `claimTab`,
provider, credential, DNS, VM, network, or live-gate action was performed.

## Prior finding closure

### V43-001 — HIGH — remains CLOSED

The executable remains exactly the fix1 executable. Its raw documentation
output error and attachment evidence are confined to the enclosing async scope,
cleared before every terminal return or rethrow, and not inspected or logged.
Success and both output-failure paths clear the evidence/error holders and all
broad runtime/controller references. The sole permitted success residue remains
the V43 task-tab continuation binding and its required top-level state flags.

### V43-002 — IMPORTANT — CLOSED

The fixture now completes the missing trust-boundary and freshness matrices:

- Listing validation includes non-array and over-maximum envelopes; array
  symbol, unexpected-name, hole, accessor, and non-enumerable-slot rejection;
  rank-zero own-symbol, class, primitive, accessor, non-enumerable-field,
  unexpected-key, and missing-URL rejection; and null-prototype acceptance.
- Required and optional field validation covers empty, over-limit, control
  character, and non-string values. URL validation separately covers parse
  failure, HTTP, explicit port, username, password, wrong origin, and exact
  HTTPS Cloudflare success.
- Local- and foreign-realm valid listings succeed. A hostile later record is
  not inspected, descriptor-only projection retains the bounded primitive
  `id`/origin result, rejected full-cell listings make zero claims, and all
  listing getter counters remain zero.
- Predecessor contamination now includes consumed, owned-tab, eligibility,
  state, setup, agent, Chrome, and V42-read categories. Dirty-default mutations
  cover the overall consumed flag, every remaining top-level V43 default,
  `PostNativeDetachConsumed`, and all attachment-phase null/false/uncreated
  defaults. Every such case stops before setup/listing with fixed cleanup.
- The fixture continues to compute the brief byte count/hash directly, pins the
  executable hash, validates the exact top-level/attachment/snapshot schemas,
  and gates its `listingMatrix` and `declarationFree` terminal claims after the
  expanded assertions.

These checks cover every security-distinct branch identified by the prior
review. No untrusted listing metadata is emitted, no later-record value or
shape is read, and no rejected listing reaches `claimTab`.

### V43-003 — IMPORTANT — CLOSED

The fixture now adds both missing URL rejection vectors:

- account-home `url()` rejection proves attachment `urlAttempted=1` and
  `urlFulfilled=0`, with all later attachment counters zero;
- token-page `url()` rejection proves readiness `urlAttempted=1` and
  `urlFulfilled=0`, with all later readiness counters zero.

Both cases assert the fixed `Error` class, consumed/ineligible state, exact full
counter objects, fixed output schema, and complete failure cleanup. Fulfilled
but semantically invalid account and token URLs remain separate cases with
`urlFulfilled=1`, so attempted-versus-fulfilled meaning is not conflated.

The final-output-failure case now asserts both exact terminal states:
`V43_FINAL_OUTPUT_FAILED_STOP` and
`V43Attachment_DOWNSTREAM_OUTPUT_FAILURE_DETACHED`. It retains the existing
proof of exact success counters before the failed final write, two total write
attempts with only the documentation output fulfilled, original thrown-value
identity, no second write, both tab bindings null/ineligible, broad runtime and
error/evidence holders null, and zero hostile output getter reads.

The expanded operational matrices continue to cover the success vector,
fulfilled-invalid stages, thrown stages, counter-corruption rejection,
documentation-output failure, and final-output failure. The terminal
`completeCounterVectors` and `terminalOutputCleanup` claims occur only after
these assertions.

## Preserved V43 security and semantic contract

- V43 sets its one-shot consumed flag before predecessor validation and before
  import or browser work. V41 remains spent and must not retry; V42 remains
  unexecuted, superseded, and unavailable as fallback.
- The declaration-free gate, one pinned import, one no-options setup, one
  Chrome acquisition, complete documentation check/write, exact session name,
  one `openTabs`, descriptor-cached rank-zero projection, and one cached-ID
  claim are unchanged.
- The exact external selected-profile/window/task-tab confirmation remains
  immediately before `openTabs`; it cannot be inferred, delegated, automated,
  or reused.
- Account-home navigation, fixed wait, URL validation, bounded exact
  account-home snapshot, and token-page navigation preserve the reviewed
  Cloudflare HTTPS origin, account path, exact `mysw.me` anchor, zero-busy, and
  V42/V4 token-page semantic signatures.
- Page interaction remains limited to fixed local filtering and reads. Create
  is counted but never clicked; there is no provider mutation, secret read,
  clipboard action, retry, fallback, reconnect, new/close-tab action, or manual
  integration path.
- Operational catches remain unbound and emit only literal `Error`. Hostile
  thrown values are neither inspected nor included in output. Output schemas
  expose no offered listing, tab ID, URL, account segment, DOM text, credential,
  secret, or thrown value.
- Success retains only the eligible V43 token-page tab binding. Ordinary,
  documentation-output, and final-output failures clear both phase bindings,
  broad runtime/controller references, and local evidence/error holders while
  leaving the one-shot gate consumed and ineligible.
- Source-site completeness, exact counter cardinality, immutable package tuple,
  runtime/API/docs pins, projected-record baseline, empty-index/dirty-baseline,
  owner/archive/residue, DNS, VM checkpoint, and fresh-realm checks remain
  mandatory action-time conditions.
- The final Create/native Copy/native masked Paste confirmation and the later
  separate exact-row deletion confirmation remain mandatory, external,
  unreached, and non-delegable.

## Severity counts

| Severity | Count | Unresolved findings |
| --- | ---: | --- |
| Critical | 0 | None |
| HIGH | 0 | None |
| IMPORTANT | 0 | None |
| Minor | 0 | None |

## Authorization statement

`authorizes_live_execution=false`

This PASS review authorizes no live V43 send, browser/provider action, gate
consumption, secret operation, or confirmation consumption. The independent
classification, coordinator tuple, all action-time pins, and both later
external confirmations remain required.
