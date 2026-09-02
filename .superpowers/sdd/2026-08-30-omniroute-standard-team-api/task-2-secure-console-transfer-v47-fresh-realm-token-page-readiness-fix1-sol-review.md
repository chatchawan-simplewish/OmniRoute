---
status: clean
depth: deep
files_reviewed: 8
findings:
  critical: 0
  high: 0
  important: 0
  minor: 0
  total: 0
---

# OmniRoute V47 fresh-realm token-page readiness fix1 — Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Verdict

**PASS**

V47-001, V47-002, and V47-003 are closed. The executable now rejects the
complete established 87-name V35-V46 predecessor set before import. The fixture
tests every V46 top-level contaminant, derives and verifies the current V47
executable tuple, emits the accurate V46 predecessor field, and retains exact
failure cleanup. All candidate files have exactly one final LF. The complete
V47 gate otherwise preserves the reviewed V46 security contract and adds only
the bounded search-control visibility wait with corresponding four-event
readiness counters. No unresolved Critical, HIGH, IMPORTANT, or Minor finding
remains.

This PASS is a static package-quality verdict only. It does not authorize or
consume V47, perform a browser/provider/VM operation, satisfy action-time
checks, replace classification, or consume an external confirmation.

## Reviewed lineage and direct package

- V46 consumed-failure incident and sanitized live result:
  `0b7944703a1b0219b3c37707a9ff8030c25d9028`.
- Initial V47 candidate:
  `ea7830005a32b71e26ffa63a9a6d61cf3ddcd71c`.
- Independent FAIL review:
  `678bbbcede8a11b0a379511eda7cf42db22755e5` with V47-001 through
  V47-003.
- Reviewed fix1 candidate:
  `5b34ce5b4dd4409e8e21569615138181ddc7c2c5`. It is directly parented
  by the FAIL review and changes exactly the V47 brief, executable, and pure
  fixture.
- Brief: `7446` bytes; SHA-256
  `E404CD3FA2F0DA28209CCB21FD53087BCAC59C0434649FAA2F72013A94FDFF83`;
  blob `91c4954fac980da63586cc8a8856d5c59bea83d5`.
- Executable: `41533` bytes; SHA-256
  `5B44CE8AADCA857C24BCCC6C93F566856AE93711065B8BA4577590703DAA708D`;
  blob `087c3ec28c414abc66dd5db0a58405fb635061f4`.
- Pure fixture: `50343` bytes; SHA-256
  `90771E3BB4423B986A8AAF5CD6F4BD6F208B176639D1BBCBF6BEB466F24815A3`;
  blob `6efab96fadc7e1b4613b1db7a3db38a120af6d86`.
- All three working-tree files exactly matched the candidate blobs. Each has
  zero CR bytes and exactly one final LF. The candidate diff passes
  `git diff-tree --check`.
- Reviewed V46 comparator executable:
  `a6bfbc5ad673f49bb3b69d26026b096d1d18cbbd`, `40894` bytes,
  SHA-256
  `55C8833CF0E405022B747298CE71E7ED6DCF4A301A6C429026A598004444050E`.
- Reviewed V46 Sol High PASS:
  `250a8c9b15bebd0335ff89c929306981eaf7fc53`.
- Reviewed V46 non-self-referential classification:
  `e9a179c507f09756630b575632f6e6a5ad8e6a0d`.
- Installed browser module remains `149771` bytes / SHA-256
  `A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`.
- Installed `docs/api.json` remains `58480` bytes / SHA-256
  `A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.
- The index was empty before review work. The exact pre-existing 12-path dirty
  product baseline was neither edited nor staged.

## Finding closure

### V47-001 closed — complete V46 predecessor defense

A mechanical union of the established 80-name V35-V45 predicate and V46's
seven top-level bindings produces 87 expected unique names. The fix1
executable contains exactly those 87 names: missing `0`, extra `0`.

The seven newly guarded bindings are:

- `secureConsoleOwnedTaskTabV46`;
- `secureConsoleOwnedTaskTabV46Eligible`;
- `secureConsoleOwnedTaskTabV46State`;
- `secureConsoleOwnedTaskTabV46PreCreateDetachConsumed`;
- `secureConsoleOwnedTaskTabV46PostNativeDetachConsumed`;
- `secureConsoleCloudflareReadsV46Consumed`; and
- `secureConsoleV46Consumed`.

The fixture adds one full-cell contaminant for every name. Each branch proves
V47 is consumed but fails declaration validation before import, setup,
documentation, naming, listing, claim, navigation, wait, URL, or snapshot;
setup and `openTabs` calls remain zero; no V47 tab is eligible or retained; the
exact failed state is recorded; and ordinary cleanup is complete. The terminal
field is now accurately named `v46PredecessorsAbsent`.

### V47-002 closed — current executable tuple is derived and enforced

The fixture computes `executableBytes` and `executableSha256` directly from the
V47 executable, then requires both derived values in the brief before any PASS
terminal. It separately retains the reviewed V46 hash assertion as predecessor
lineage evidence rather than substituting it for the current pin. The observed
terminal reports the exact direct V47 value `41533` /
`5B44CE8AADCA857C24BCCC6C93F566856AE93711065B8BA4577590703DAA708D`.

### V47-003 closed — terminal whitespace normalized

The executable and fixture now end with exactly one LF and no preceding blank
line. The brief does likewise. No candidate path produces a `diff-tree
--check` diagnostic.

## One-delta and wait/counter verification

After mechanically normalizing V47 identity back to V46, removing the seven
new V46 predecessor guards, removing the three-line textbox wait, and restoring
the readiness totals from four to three, the fix1 executable is byte-equivalent
to the reviewed V46 executable modulo terminal blank whitespace. This proves
there is no hidden runtime-semantic delta.

The only new runtime operation is exactly:

`await tokenFilter.waitFor({ state: "visible", timeoutMs: 20000 });`

It is placed immediately after the unique search textbox locator is constructed
and before its count, `aria-controls`, controlled-root, or paginator checks.
The installed runtime documents and implements `Locator.waitFor` with
`state`/`timeoutMs`. Attempt is counted before the await, fulfillment only after
it, and any timeout is caught as fixed `Error` evidence with complete cleanup.

PASS requires four exact readiness attempts and fulfillments: search-control
visibility, paginator visibility, query echo, and empty status. The fixture's
new `tokenFilterWait` failure plus all shifted later failure vectors and the
success vector enforce those counts without changing any other operation
counter.

## Fixture terminal observed

The fixture was executed once in this fix review because the newly changed V46
contamination matrix and derived current-executable pin were the concrete prior
defects requiring direct confirmation. Static inspection first proved the
fixture imports only Node built-ins and replaces the sole browser-module import
before evaluating the full cell. It exited `0` with:

`{"result":"V47_PURE_FIXTURES_PASS","briefBytes":7446,"briefSha256":"E404CD3FA2F0DA28209CCB21FD53087BCAC59C0434649FAA2F72013A94FDFF83","executableBytes":41533,"executableSha256":"5B44CE8AADCA857C24BCCC6C93F566856AE93711065B8BA4577590703DAA708D","fixtureBytes":50343,"fixtureSha256":"90771E3BB4423B986A8AAF5CD6F4BD6F208B176639D1BBCBF6BEB466F24815A3","syntax":"PASS","declarationFree":true,"v46PredecessorsAbsent":true,"listingMatrix":true,"exactOutputKeys":true,"fullCellSuccess":true,"fixedFailureCleanup":true,"hostileThrownValues":true,"terminalOutputCleanup":true,"completeCounterVectors":true,"getterCalls":0,"listingGetterCalls":0,"outputGetterCalls":0}`

The run performed no browser-runtime import/setup, Chrome connection, tab
enumeration/claim/navigation, provider read/write, secret operation, or live
resource action.

## Full security-contract re-review

- V47 marks consumed before predecessor validation or import. Nonfresh,
  contaminated, and dirty-default branches stop permanently ineligible with
  fixed output and exact cleanup. No retry, fallback, reconnect, continuation,
  reinterpretation, override, or verdict relaxation exists.
- The attachment topology remains one import, setup, connection, complete
  documentation read/write, session name, `openTabs`, exact rank-zero record
  claim, account navigation/wait/URL/snapshot, and exact counter vector.
- Trusted listing validation remains cross-realm safe, descriptor-only,
  complete, bounded, and free of untrusted getters, setters, iterators, direct
  index reads, or later-record value access. URL absence is allowed; any present
  URL must be exact HTTPS `dash.cloudflare.com` without port or credentials.
- Controller identity, account-home URL, exact zone link, positive anchor
  count, zero busy indicators, canonical token-page URL, controlled root,
  paginator, settled filter, terminal `0-0 of 0`, disabled navigation, exactly
  one Create control, and zero exact token-name/row matches remain mandatory.
- Output remains fixed booleans, bounded counts, fixed counters/states/results,
  and a bounded trusted snapshot. Operational catches are unbound. Hostile
  thrown values and getter-bearing listing/output objects are neither inspected
  nor serialized; all getter counters remain zero.
- Success retains only the eligible V47 owned-tab binding while clearing broad
  runtime/controller aliases. Ordinary failure clears both phase tab bindings
  and all aliases. Documentation-output and final-output failures repeat
  cleanup, null evidence/error holders, and rethrow the original value by
  identity without a second write.
- Create is counted but never clicked. There is no Copy, clipboard, credential,
  token-secret, storage, cookie, DNS, routing, VM, provider mutation, tab
  creation/close, or other persistence path.
- V46 remains spent. All V4/V44/V46 semantic, no-residue, no-retry, secret,
  counter, output, and confirmation constraints remain binding. Fresh
  profile/window/tab confirmation plus fresh `getState` and declaration audit
  remain action-time requirements. The final Create/native Copy/native masked
  Paste confirmation and later separate exact-row deletion confirmation remain
  external, mandatory, and unreached.
- No browser/provider/VM/live-resource action, secret operation, confirmation,
  or authority-gate consumption occurred during this review.

## Severity counts

| Severity | Count | Unresolved findings |
| --- | ---: | --- |
| Critical | 0 | None |
| HIGH | 0 | None |
| IMPORTANT | 0 | None |
| Minor | 0 | None |

## Authorization statement

`authorizes_live_execution=false`

This PASS review authorizes no V47 live send, browser/provider/VM action,
secret operation, authority-gate consumption, or confirmation consumption. A
separate non-self-referential classification, post-commit coordinator tuple,
all action-time pins, fresh realm and exact external Chrome-selection
confirmation, plus both later external confirmations remain mandatory.
