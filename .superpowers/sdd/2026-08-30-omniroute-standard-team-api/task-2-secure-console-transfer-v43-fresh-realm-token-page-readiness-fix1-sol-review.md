# OmniRoute V43 fresh-realm token-page readiness package fix1 — Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Verdict

**FAIL**

Fix1 fully closes V43-001: the raw documentation-output error and attachment
evidence now live only in a short-lived enclosing scope and are cleared before
every terminal return or rethrow. The executable's inherited V41/V42/V4
security semantics remain intact. V43-002 and V43-003 are only partially
closed, however: the fixture still labels partial trust-boundary and
failure-vector coverage as complete. The package remains ineligible for live
execution.

## Reviewed lineage and exact package

- Initial candidate:
  `c54732144b4df28372b2c907251864b2a48aabc0`.
- Initial FAIL review:
  `9a03f94c66fdfa7c8e137dff8e6aeed89adad5c1`.
- Reviewed fix commit:
  `9ebc089bb35f1e86cc50e3353917b9c9f7a92050`.
- The fix is directly parented by the FAIL review and modifies exactly the
  assigned V43 brief, executable, and pure fixture.
- Brief: `6881` bytes; SHA-256
  `CD40F8C65DD428BA3C0F14DB3ED978557D3E8010F7DA58F18B64A0E1FFB90A35`;
  blob `76c16e8608a2c18f5204e382b68f31af27622d44`.
- Executable: `39193` bytes; SHA-256
  `13E56326548D660B111DDC63857BFD33250A548F7D094FA4131EEBB694D24B01`;
  blob `a1d4f0cb1351fa4c11714c56e008958dabd6ca55`.
- Pure fixture: `40500` bytes; SHA-256
  `DCDAD2355DFF7C715E360D20A42F55D50082C1EF614A70C98A4ECE92F8C36145`;
  blob `606676a9df53353565b477c60967ca46f2cce5ff`.
- All three package files have one final LF, and the fix commit passes
  `git diff-tree --check`.
- The index was empty before review work. The exact existing 12-path product
  dirty baseline was not modified or staged.

Review activity was limited to direct committed package bytes, the assigned
prior review, scoped Git/static checks, and the inert fixture. No CUA, Chrome,
real runtime, provider, credential, DNS, VM, network, or live-gate action was
performed.

## Independently observed fixture terminal

I ran the committed fix1 fixture once. It exited `0` and emitted exactly:

`{"result":"V43_PURE_FIXTURES_PASS","briefBytes":6881,"briefSha256":"CD40F8C65DD428BA3C0F14DB3ED978557D3E8010F7DA58F18B64A0E1FFB90A35","executableBytes":39193,"executableSha256":"13E56326548D660B111DDC63857BFD33250A548F7D094FA4131EEBB694D24B01","syntax":"PASS","declarationFree":true,"listingMatrix":true,"exactOutputKeys":true,"fullCellSuccess":true,"fixedFailureCleanup":true,"hostileThrownValues":true,"terminalOutputCleanup":true,"completeCounterVectors":true,"getterCalls":0,"listingGetterCalls":0,"outputGetterCalls":0}`

The byte/hash and syntax fields are correct. The boolean completeness labels
are evaluated against the fixture's assertions below rather than accepted at
face value.

## Prior finding closure

### V43-001 — HIGH — CLOSED

Fix1 encloses both phases in one outer async scope. Only the final V43 task-tab
binding and its continuation state/consumption flags remain top-level. The
attachment evidence, deferred documentation-output error, setup function,
agent, Chrome controller, and attachment tab are locals in the outer scope.

For documentation-output failure, the code copies the error reference into a
short-lived local, clears the deferred-error and attachment-evidence holders,
and then rethrows the local without reading a property, logging it, or making a
second write. Ordinary final-output success clears both holders immediately
after the write. Final-output failure clears both tab phases, all broad runtime
handles, and both holders before rethrow. Exiting/rejecting the outer IIFE then
destroys the remaining local references.

The fixture now observes `evidenceNull=true` and `outputErrorNull=true` on
success, documentation-output failure, and final-output failure. Both output
failure paths use an object with a throwing `name` getter, preserve thrown
identity, perform no second write, and leave `outputGetterCalls=0`. This closes
the raw-value and persistent-evidence residue defect.

### V43-002 — IMPORTANT — PARTIALLY CLOSED, STILL UNRESOLVED

Fix1 adds direct brief bytes/SHA-256 to the fixture terminal, pins the executable
hash in the brief, checks exact top-level and attachment key sets, checks the
nested snapshot key set and primitive/range shape, and extracts the marked
listing helper. It also adds local and foreign-realm success; empty, hole,
rank-zero wrong-origin/missing-URL/unexpected-key; array-symbol/unexpected-name;
index accessor; rank-zero ID accessor; hostile later-record getter; and
null-prototype acceptance cases. Later-record and accessor getter counts stay
zero.

That is meaningful coverage, but it is not the full listing trust-boundary
matrix claimed by `listingMatrix=true`. Distinct predicates remain untested,
including:

- non-array input and length above the bounded maximum;
- a rank-zero record with its own symbol;
- non-plain/class and primitive rank-zero values;
- non-enumerable rank-zero fields and non-enumerable numeric array slots;
- empty, over-limit, control-character, and non-string required/optional
  fields; and
- invalid URL parse, HTTP scheme, explicit port, username, and password cases.

The broadened freshness matrix is also incomplete. It samples consumed,
owned-tab, Chrome, eligibility, and V42-read predecessor categories, but not
state, setup, or agent sentinels. It mutates five final V43 defaults but omits
`secureConsoleOwnedTaskTabV43PostNativeDetachConsumed` and does not mutate the
attachment-phase null/false/uncreated defaults. A regression in any omitted
predicate can therefore coexist with `declarationFree=true` and
`listingMatrix=true`.

Required correction:

1. Add data-driven cases for every distinct branch of the marked listing
   helper, including every item above, and require zero claim on every rejected
   full-cell listing.
2. Add predecessor contamination representatives for state, setup, and agent,
   and dirty-default cases for every outer and attachment-phase V43 default.
3. Keep the current direct brief/executable hash, snapshot schema, and
   later-record/getter-zero assertions.
4. Emit `listingMatrix=true` and `declarationFree=true` only after the complete
   matrices execute.

### V43-003 — IMPORTANT — PARTIALLY CLOSED, STILL UNRESOLVED

Fix1 now asserts the full success attachment counter vector, expands attachment
failures to thrown and fulfilled-invalid module/agent/Chrome/docs/listing/
controller/tab outcomes, covers account URL/signature mismatches, and adds a
large token-page mismatch/throw matrix plus explicit counter-corruption cases.
It also asserts documentation-output and final-output write cardinality,
rethrow identity, cleanup holders, and their available counter objects.

Two distinct attempted/fulfilled vectors remain absent:

- account-home `adopted.url()` rejection (`urlAttempted=1`,
  `urlFulfilled=0`); and
- token-page `adopted.url()` rejection (`urlAttempted=1`,
  `urlFulfilled=0`).

The existing `accountUrl` and `tokenUrl` cases return an invalid string after
fulfillment, so they exercise `urlFulfilled=1`, not the rejection vectors. The
snapshot counter-corruption source case is not a substitute for these URL
method failures.

The final-output failure observation includes exact `state` and
`attachmentState` fields, but the fixture never asserts them. It can therefore
report `terminalOutputCleanup=true` if either fixed terminal state regresses,
as long as the selected null/eligible/holder checks still pass. The fixture does
assert both exact states for documentation-output failure, which should be
mirrored for final-output failure.

Required correction:

1. Add account-URL-throw and token-URL-throw cases and assert their complete
   attachment/readiness vectors, fixed errors, consumed/ineligible state, and
   full cleanup.
2. Assert final-output `state === "V43_FINAL_OUTPUT_FAILED_STOP"` and
   `attachmentState ===
   "V43Attachment_DOWNSTREAM_OUTPUT_FAILURE_DETACHED"`, along with the already
   observed consumed/null/ineligible state and full counters.
3. Retain the current documentation-output vector/state, final write
   cardinality, counter-corruption, rethrow-identity, and hostile-getter checks.
4. Emit `completeCounterVectors=true` and `terminalOutputCleanup=true` only
   after those assertions execute.

## Preserved semantic and safety boundaries

- V43 consumes before predecessor validation and before import/browser work.
  V41 remains spent and V42 superseded; no retry or fallback was introduced.
- The exact runtime/docs flow, one `openTabs`, cached rank-zero claim,
  account-home navigation/signature, token-page navigation/signature, fixed
  page-local fill, and read-only Create count are unchanged.
- Success retains only the eligible V43 tab and required top-level continuation
  flags. Broad runtime/controller, attachment, evidence, error, offered-list,
  account, URL, and DOM temporaries do not survive the enclosing IIFE.
- Ordinary and output failures clear both tab phases and broad handles and
  remain consumed/ineligible. Operational catches stay unbound and emit only
  fixed `Error`; terminal catches rethrow without inspecting/logging.
- No click, Create, provider mutation, clipboard, credential, secret store,
  DNS, routing, VM, listener, proxy, new/close tab, reconnect, selected/list/get
  fallback, or manual integration action was added.
- The exact external Chrome profile/window/task-tab confirmation and later
  Create/native Copy/native masked Paste and separate row-deletion
  confirmations remain mandatory, external, and unreached.

## Severity counts

| Severity | Count | Unresolved findings |
| --- | ---: | --- |
| Critical | 0 | None |
| HIGH | 0 | None |
| IMPORTANT | 2 | V43-002 and V43-003 |
| Minor | 0 | None |

## Authorization statement

`authorizes_live_execution=false`

This FAIL review authorizes no live V43 send, browser/provider action, gate
consumption, retry, fallback, secret operation, or confirmation consumption. A
corrected immutable package requires a fresh independent Sol High review and
all later classification, tuple, action-time pin, and external-confirmation
boundaries.
