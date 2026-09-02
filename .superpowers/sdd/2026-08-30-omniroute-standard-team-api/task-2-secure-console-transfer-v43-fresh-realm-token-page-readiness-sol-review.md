# OmniRoute V43 fresh-realm token-page readiness executable package — Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Verdict

**FAIL**

The V43 executable preserves the intended attachment, account-home, and
token-page operational sequence, and its committed inert fixture reaches the
claimed PASS terminal. The package nevertheless violates the approved
no-residue/privacy design by retaining terminal and attachment objects in
top-level lexical bindings, and its fixture materially overstates required
listing, byte-pin, failure-stage, and counter coverage. V43 must not be consumed
from this package.

## Reviewed lineage and exact package

- Design PASS review:
  `dc4ffa4c9b7eba182c3e3cc82b1bf975de878e6b`.
- Candidate package commit:
  `c54732144b4df28372b2c907251864b2a48aabc0`.
- The candidate is directly parented by the design PASS and adds exactly the
  assigned brief, executable, and pure fixture.
- Brief: `6827` bytes; SHA-256
  `3128B7BC77E70848819C5A2AF10FC41C44748EF72D4813504367AC9305BA831A`;
  blob `0acf285ce1fc0915090653135ada1953755a4c99`.
- Executable: `36818` bytes; SHA-256
  `02259382E069888EB0F175B89234C12F4EE79AE6A14B22428125AC8BC3709677`;
  blob `f03f272c1b080c9480ea14ee53a928e337c305d5`.
- Pure fixture: `24031` bytes; SHA-256
  `2C31175974D904CF979BD22157CAB3911F83078D783622C9B4A2050E8A64F760`;
  blob `accb602fa2407506b7bfdad59a9329836037b585`.
- All three committed files have one final LF. The package commit passes
  `git diff-tree --check`.
- The index was empty before review work. The exact pre-existing 12-path product
  dirty baseline was not edited or staged.

I read the three committed package files directly and used only scoped static,
Git, and inert-fixture checks. I did not invoke CUA, Chrome, the real runtime,
`openTabs`, `claimTab`, a provider, credentials, DNS, VM resources, or any live
gate.

## Fixture terminal observed

I reran the committed inert fixture once because the completeness claims were a
concrete review question. It exited `0` and emitted exactly:

`{"result":"V43_PURE_FIXTURES_PASS","executableBytes":36818,"executableSha256":"02259382E069888EB0F175B89234C12F4EE79AE6A14B22428125AC8BC3709677","syntax":"PASS","declarationFree":true,"exactOutputKeys":true,"fullCellSuccess":true,"fixedFailureCleanup":true,"hostileThrownValues":true,"terminalOutputCleanup":true,"completeCounterVectors":true,"getterCalls":0}`

That terminal proves the cases the fixture actually executes; it does not prove
the omitted design cases described below.

## Preserved and correctly implemented boundaries

- V43 is marked consumed before the large V35-V42 predecessor-absence predicate
  and before import/browser activity. V41 remains consumed/non-retriable and
  V42 is explicitly superseded with no executable fallback path.
- Static cardinality is one import, one setup, one Chrome acquisition, one docs
  read/write, one session name, one `openTabs`, one rank-zero `claimTab`, one
  account-home navigation/wait/URL/snapshot, one token-page navigation/URL, one
  fixed local filter fill, and one final evidence write.
- The V41 listing helper uses cross-realm `Array.isArray`, own name/symbol and
  data-descriptor checks, bounded count and string fields, exact HTTPS
  `dash.cloudflare.com`, cached primitive ID projection, and only reads the
  rank-zero descriptor value.
- The claimed controller ID must equal the projected ID. The account-home URL
  must contain the exact lower-hex account segment and the fixed-schema page
  signature requires exact host/path, exactly one exact `mysw.me` zone anchor,
  positive bounded anchor count, and zero busy markers.
- The V42/V4 token-page flow retains the sole search textbox, bounded controlled
  result root, paginator, complete initial state, empty initial filter, fixed
  non-secret fill, exact echo and empty status, terminal zero rows/pagination,
  exactly one semantic Create control, and zero exact-name/matching-row counts.
- Create is never clicked. No provider mutation, clipboard, credential, secret
  store, DNS, routing, VM, listener, proxy, new-tab, close-tab, reconnect,
  selected/list/get fallback, retry, or manual integration site exists.
- Operational catches are unbound and report fixed `Error`. Success clears the
  live setup/agent/Chrome handles and transfers the sole tab from the attachment
  binding into the eligible V43 binding. Ordinary and final-output failure clear
  both live tab bindings and broad runtime/controller handles.
- The brief preserves the exact external selected-profile/window/task-tab
  confirmation immediately before the sole `openTabs` call. It also preserves
  the later, separate Create/native Copy/native masked Paste and exact-row
  deletion confirmations as unreached and nondelegable.

## Findings

### V43-001 — HIGH — Documentation-output failure retains the raw thrown value, and attachment evidence remains as top-level residue

The executable declares `secureConsoleV43TerminalOutputFailure` and
`secureConsoleV43AttachmentEvidence` as top-level lexical bindings. If the
documentation write fails, the bound catch assigns the original thrown object
to `secureConsoleV43TerminalOutputFailure`, converts the operational result to a
fixed failure, performs live-handle cleanup, and then rethrows the globally
retained value. The binding is never reset to null. After rejection, the fresh
realm therefore still retains the raw arbitrary thrown object—the precise
secret/privacy/no-residue condition the approved design forbids.

Independently, `secureConsoleV43AttachmentEvidence` is assigned a nested result
object after the attachment phase and is never cleared after successful final
output, ordinary failure output, documentation-output rejection, or final-
output rejection. Its fields are intended to be fixed-schema, but the approved
success contract permits only the one V43 tab binding and required
eligibility/state/consumption flags to remain; it does not permit a persistent
attachment-evidence object. The fixture's observation hooks do not inspect
either global, so `terminalOutputCleanup=true` and `fullCellSuccess=true` can be
reported while this residue survives.

Required correction:

1. Keep both attachment evidence and any deferred documentation-write error in
   locals within one enclosing async scope, or explicitly clear the top-level
   bindings on every terminal path before return/rethrow.
2. For documentation-write failure, preserve identity only in a short-lived
   local, complete cleanup, clear any global reference, and then rethrow without
   property access, logging, serialization, or a second write.
3. After successful final evidence write, clear the attachment evidence holder
   while retaining only the final eligible V43 tab and declared continuation
   flags. On ordinary/final-output failure, clear it together with both tab and
   broad runtime bindings.
4. Extend the fixture observation to require both evidence/error holders null
   on success, normal failure, documentation-output failure, and final-output
   failure, including hostile thrown objects with zero getter calls.

### V43-002 — IMPORTANT — The fixture omits the required listing trust-boundary and exact package-byte matrix

The approved design requires malformed array, descriptor, symbol, rank-zero,
and hostile-later-record cases that stop before claim and prove later offered
record values are never read. The committed fixture runs one valid foreign-
realm listing with a benign later record, but it never invokes the marked
listing helper against malformed arrays, holes, index accessors, symbols,
unexpected names, malformed/accessor rank-zero records, wrong origins, or a
later record with a throwing getter. Thus `declarationFree=true` and the valid
success case do not establish the required listing rejection/nonobservation
matrix.

The design also requires exact brief **and** executable bytes/SHA-256. The
fixture reads and hashes only the executable. It never reads the brief and its
terminal contains no brief bytes or brief SHA-256. It further checks only the
top-level and attachment key sets, not the nested snapshot key set.

Required correction:

1. Extract the marked listing helper from the exact executable and add the full
   local/foreign-realm accept/reject matrix, including a hostile later record
   whose getter count must remain zero and proof of zero claim on rejection.
2. Read the exact committed brief, report/assert its byte length and SHA-256,
   and retain the executable byte/hash/syntax pins.
3. Assert the exact nested snapshot key set and primitive/range schema in
   addition to the existing top-level and attachment key sets.
4. Expand contaminated predecessor and nonfresh V43 tests beyond one V41
   consumed sentinel and one consumed-default edit so the declared sentinel and
   default categories are actually represented.

### V43-003 — IMPORTANT — `completeCounterVectors=true` overstates the executed failure and counter coverage

The success case does not assert the complete attachment counter vector; it
asserts selected external stub-call totals and only deep-compares the token-page
counter vector. In particular, the inert import is replaced by a fixture
property and `fixture.importCalls` is asserted as zero, while the attachment
output's import-attempted/fulfilled counters are not checked in success.

The attachment failure loop covers thrown import/setup/connect/docs/session/
listing/claim/navigation/wait and an invalid account snapshot, but omits shape
and fulfilled-invalid outcomes, account URL failure, documentation-write
counter proof, controller/tab-shape failure, and other fixed stop sites. The
token failure loop covers only navigation throw, the first textbox-count
signature failure, and fill throw; it does not cover URL, controlled-root,
paginator/readiness, baseline, echo/status, terminal-state,
Create/name/row-read, or final semantic-counter failures.

Finally, the documentation-output and final-output tests assert write-call
cardinality and selected cleanup booleans but do not assert their complete
attachment/token counter vectors or all fixed terminal states. The emitted
`completeCounterVectors=true` therefore makes a stronger claim than the fixture
proves.

Required correction:

1. Assert the full attachment and token counter vectors for success.
2. Add fixture cases for every fixed failure site or use a data-driven matrix
   that proves the distinct attempted/fulfilled vector for each stage,
   including returned-invalid shape/signature outcomes as well as throws.
3. For documentation-output and final-output failures, assert the complete
   counter vectors, exact consumed/ineligible states, all binding cleanup,
   single failed write/no later write, and thrown-value identity/noninspection.
4. Emit `completeCounterVectors=true` only after all those assertions run.

## Severity counts

| Severity | Count |
| --- | ---: |
| Critical | 0 |
| HIGH | 1 |
| IMPORTANT | 2 |
| Minor | 0 |

## Authorization statement

`authorizes_live_execution=false`

This FAIL review authorizes no live V43 send, browser/provider action, secret
operation, gate consumption, retry, fallback, or confirmation consumption. A
corrected immutable package requires a fresh independent review and all later
classification, tuple, action-time pin, and external-confirmation boundaries.
