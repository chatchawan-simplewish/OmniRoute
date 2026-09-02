# OmniRoute V43 fresh-realm token-page readiness design — Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Verdict

**FAIL**

V43 is directionally the smallest viable replacement: one fresh-realm cell can
reacquire the selected tab, prove the account-home signature, and continue to
the token-page readiness signature without reviving either spent V41 or
unusable V42. The committed design is not yet a safe implementation contract,
however. It omits the external selection fact that authorizes rank-zero, does
not require the executable to prove its claimed fresh/predecessor-free realm,
and underspecifies fixed-schema output and thrown-value privacy fixtures.

## Reviewed scope and provenance

- Design commit: `6f700adfa2700d93b82689dbc8721cad266eb19e`.
- Direct parent: `190c4391176a7f4f483be3682cf6524ba2666169`.
- The design commit adds exactly the assigned V43 design path.
- Design blob: `21939c7905d2ae43a33fc867f2f2673d64af5f72`.
- Direct committed bytes: `4919`.
- SHA-256:
  `1D54CEB240D600E25F197A10EF568EDEE87D9849306948F981AFD5C794705A70`.
- The file has exactly one final LF, and the commit passes
  `git diff-tree --check`.
- The index was empty before review work. The exact pre-existing 12-path product
  dirty baseline was neither modified nor staged.

I reviewed only the committed V43 design bytes and scoped Git evidence. I did
not invoke CUA, Chrome, a provider, credentials, DNS, VM resources, or any live
gate.

## Design assessment

### Sound composition choices

- The design correctly treats V41 as consumed and non-retriable and recognizes
  that V42's same-realm predecessor condition cannot be reconstructed after the
  retained lexical binding is gone.
- Combining fresh attachment, account-home proof, and token-page readiness in
  one newly consumed V43 cell avoids an unnecessary intermediate retained-
  binding handoff and is the minimal viable composition at the operation level.
- The proposed cell consumes before import or action and permits exactly one
  import, setup, Chrome acquisition, complete documentation read/write,
  session naming, listing, rank-zero claim, account-home navigation/proof, and
  token-page navigation/proof.
- It carries forward the cross-realm array envelope, own-descriptor validation,
  bounded rank-zero record, exact Cloudflare HTTPS origin, cached-ID claim, and
  later-record noninspection requirements.
- It carries forward the account-home account-path/one-zone-anchor/no-busy
  signature and the unchanged V42/V4 token-page filter, pagination, Create-read,
  zero-name, and zero-row semantics.
- Create remains read-only and the sole fill is a fixed non-secret local page
  filter. No provider-persistent action is part of the design.
- The proposed success boundary clears broad runtime/listing/temporary state and
  retains only one eligible V43 tab. Failure and output failure are one-shot,
  terminal, fixed-error, and cleanup-oriented, with no retry, reconnect,
  selection fallback, new tab, close, or manual integration path.
- Runtime, documentation, repository projection, dirty baseline, residue, DNS,
  VM, and sole-owner pins remain explicit. The later Create/native Copy/native
  masked Paste and separate exact-row deletion confirmations remain external and
  mandatory.

These choices should be preserved in a corrected design.

## Findings

### V43-D001 — HIGH — Rank-zero claim lacks its mandatory exact-selection confirmation boundary

The design requires one rank-zero claim and says it preserves V41's structural
listing contract, but it does not require the fact that made V41's ordered
selection safe: the documented last-opened/focused ordering plus the owner's
exact confirmation that the intended task tab is selected and that no other
Chrome profile/window can displace rank zero. Neither the executable design
steps, pure-fixture requirements, nor action-time pin list names this boundary.

Without that external fact, a structurally valid exact-Cloudflare record at
rank zero can still be the wrong account/tab. The later account-home signature
proves page kind and one `mysw.me` anchor, not that the controller claimed the
owner-intended tab. This is a wrong-target security risk before the later token
workflow.

Required correction:

1. State that rank-zero is justified only by the pinned/documented ordering and
   a fresh external owner confirmation naming the intended selected task tab,
   with no other Chrome profile/window competing at action time.
2. Add that confirmation to the mandatory action-time pins immediately before
   the single `openTabs` call. It must not be inferred, automated, delegated, or
   satisfied by the design review.
3. Require any selection/order drift or uncertainty to stop V43 consumed before
   claim, with no listing, selected-tab, get, new-tab, or manual fallback.

### V43-D002 — IMPORTANT — “Fresh realm” and predecessor retirement are asserted, not fail-closed executable preconditions

The trigger text calls V43 fresh and says it does not reuse V41/V42 bindings,
but the exact cell requirements only say to declare V43 bindings and consume
V43. They do not require a declaration-shape gate that proves predecessor
sentinels and bindings are absent, nor do the action-time pins require a
declaration-free V35-V43 realm. A cell implemented literally from this design
could therefore run in a contaminated realm and still satisfy the written
contract.

The design also says V42 is unexecuted and cannot satisfy its same-realm
precondition, but does not explicitly retire/supersede it. Leaving V42 as an
apparently unconsumed alternative creates two nominal gate contracts even
though only V43 is valid.

Required correction:

1. Define an exact executable declaration-shape precondition. At minimum it
   must prove V43 was fresh before setting its consumed flag, every V43 binding
   starts at its declared null/false/uncreated value, and the relevant V35-V42
   consumption/owned-tab/runtime sentinels are `undefined` in the new realm.
2. Make the fresh declaration-free V35-V43 state a mandatory action-time pin,
   not a narrative assumption. Consumption must occur before evaluating the
   remainder of the precondition so any mismatch spends V43.
3. Explicitly classify V42 as superseded/static and never executable or
   reinterpret-able after loss of its sole same-realm V41 predecessor. V42 must
   not become a fallback if V43 fails.
4. Add fixture cases for contaminated predecessor declarations and nonfresh V43
   defaults, proving stop-before-import/action with exact partial counters and
   complete cleanup.

### V43-D003 — IMPORTANT — Evidence privacy and hostile thrown-value fixture requirements are incomplete

The design requires fixed secret-safe failure and says no secret may appear in
evidence, but it does not define the fixed success/failure output schema or
explicitly prohibit emission of the offered listing, tab metadata, raw URLs,
account segment, DOM-derived strings, or raw thrown values. Clearing these
temporaries after use does not by itself constrain what may already have been
written as evidence.

The pure-fixture section requires failure-stage cleanup and an unbound catch,
but it does not require hostile thrown-value cases. Syntax/source inspection
alone is weaker than the established privacy proof: a plain data-name token and
an object with a throwing `name` getter should demonstrate that failure output
is fixed and the thrown value is never inspected.

Required correction:

1. Specify an exact fixed-schema output containing only bounded booleans,
   counters, fixed state/result/error literals, and approved bounded counts.
   Explicitly exclude raw listings, record metadata, tab IDs, URLs, account
   segments, DOM text, credentials, secrets, and thrown values.
2. Require the operational catch to remain unbound and output only the literal
   error class. If terminal output itself fails, require cleanup and rethrow
   without inspecting or logging the thrown value and without a second write.
3. Extend the inert fixture matrix with both a thrown plain data-name token and
   a thrown object whose `name` getter throws. Assert fixed output, absence of
   the token, zero getter calls, exact counters, consumed/ineligible state, and
   full binding cleanup.
4. Require the fixture to assert the exact output key set on success and each
   fixed failure path, as well as sole-binding/no-residue state.

## Severity counts

| Severity | Count |
| --- | ---: |
| Critical | 0 |
| HIGH | 1 |
| IMPORTANT | 2 |
| Minor | 0 |

## Authorization statement

`authorizes_live_execution=false`

This FAIL authorizes no V43 implementation execution, live browser action,
provider action, secret handling, or gate consumption. A corrected design must
receive a fresh independent review before the executable/fixture package is
implemented and committed. The eventual package still requires its own
independent Sol High review, non-self-referential classification, post-commit
tuple, and all action-time pins before any one-shot send.
