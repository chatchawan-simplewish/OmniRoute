# OmniRoute V49 fresh-realm token-page readiness Sol High review

Date: 2026-09-03 (Asia/Bangkok)
Reviewer: Codex, independent `gpt-5.6-sol` High implementation/security review
Review-package commit: `65f430eb45d7f903769f109ab538cd2afabee2f2`
Exact candidate commit: `dbb04a3d3e185f8290cd27977de4dabad62a1eaf`
Candidate parent: `97f5d23b7243df6eb205f7be9393dd65027d703f`

## Verdict

`FAIL`

`authorizes_live_execution=false`

The package is not eligible for classification or live execution. The review
found one HIGH and one IMPORTANT issue: the fresh-realm guard omits every
persistent V47 top-level declaration, and the pure fixture does not implement
the design-required one-proof-only post-failure cleanup test.

## Exact-byte and ancestry evidence

The candidate is the direct parent of the review-package commit. The candidate
changes exactly the brief, executable, and fixture; the package commit changes
only the review package. Their committed candidate blobs are unchanged at the
package commit.

| Artifact | Bytes | SHA-256 | Git blob |
| --- | ---: | --- | --- |
| V49 design | 10510 | `0D481DB643A01051784C25D4CC831A4A138AA6782FE7AA37CDC639D119152537` | `a656719c528d1fcd20ccea301cb94e4628b16ace` |
| V49 design fix-1 PASS review | 7229 | `1E4AB13FD0E0996379749EFC47BC0CE855476635A9BE36D1BF0D59760CA6E808` | `caa289fce7db814dd604b885201f9eab8994d272` |
| V49 implementation plan | 3362 | `985231DBC4EEA655429E82A73BD2E29D9AF59875CDB4D48230DDB7C539C3B19B` | `0180a95531679ff1ac712e507a17b1c5885fb2f8` |
| V49 brief | 5170 | `8154E6145C5ABBB8EE226ED173A91D5A944E048D98787F79298B9B11F1AABA3B` | `bc90089ae3aa073eb81a55b2bca94e3a205e82e1` |
| V49 executable | 41699 | `F279984ABAEDD5087B99956E04763F592022E45E2D3AE974293184F148BD12AE` | `86399ce818fe8e00416b3ec6fa10342cd714721c` |
| V49 pure fixture | 50618 | `8C916F69588C9003CEB4FF2C0B0C28EEA75D4557FAA8A03BFB9B8EA9552F7B7F` | `53bca1099df3fda4fc1b8b843e6517ef3a5436b8` |
| V49 review package | 6766 | `E4052A7D17F60FB680FA7743049C0E68F21EFF0F635911F6B0020EC944928096` | `a7b86ea1efff2160f3443d2be11324b6407709fb` |

The final V47 brief/executable/fixture blobs are respectively
`91c4954fac980da63586cc8a8856d5c59bea83d5`,
`087c3ec28c414abc66dd5db0a58405fb635061f4`, and
`6efab96fadc7e1b4613b1db7a3db38a120af6d86`. The corrected V48
design/executable/fixture/PASS-review/classification/live-result blobs are
respectively `232abfed08475b9fec17a5c21a6299db3fbc6720`,
`544cadd03fc4049d7a4cda6074f62c8aa40190cc`,
`b0017298e1826dd6c8946f08094167b6ca8268f7`,
`4f27bcc737210215c9b33d245b3cf98ee5b33521`,
`e1d274df38b3b1e775fc4c17497bd2842542e71a`, and
`7ee54b84afd6a407074fa678dfa5fe7831cc58d1`.

The installed pinned browser module was read as 149771 bytes with SHA-256
`A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`.
The paired `docs/api.json` was read as 58480 bytes with SHA-256
`A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.
These are static review observations only and still require action-time
revalidation.

No CUA, browser, provider, network, VM, DNS, clipboard, secret, or live-gate
action was performed. The already-passing fixture was not rerun: direct-byte
inspection found missing test categories, and repeating the existing suite
could not resolve either omission.

## Mechanical delta

Independent line-normalization confirms the package's physical delta claim:

- replacing `V49`/`v49` with `V47`/`v47`, deleting the three V48 guard lines,
  and restoring the V46 terminal conjunction makes the executable exactly the
  final V47 executable;
- performing the same rename, deleting the three V48 contamination cases and
  the two optional-key assertions, and restoring the terminal predecessor label
  makes the fixture exactly the final V47 fixture.

That proof is accurate as a byte comparison but exposes V49-001: the declared
three-line executable delta is not sufficient to implement the approved
V35-V48 predecessor boundary.

## Findings

### V49-001 — HIGH — V47 declarations are absent from the fresh-realm guard and contamination matrix

The final V47 executable creates seven persistent top-level declarations:

- `secureConsoleOwnedTaskTabV47`
- `secureConsoleOwnedTaskTabV47Eligible`
- `secureConsoleOwnedTaskTabV47State`
- `secureConsoleOwnedTaskTabV47PreCreateDetachConsumed`
- `secureConsoleOwnedTaskTabV47PostNativeDetachConsumed`
- `secureConsoleCloudflareReadsV47Consumed`
- `secureConsoleV47Consumed`

The V49 executable's `predecessorDeclarationsAbsent` conjunction checks the
established V35-V46 set and then jumps directly to the three V48 diagnostic
declarations. None of the seven V47 declarations is checked. The fixture's
contamination loop has the same gap: it includes V46 and the three V48 cases,
but no V47 case. Consequently the package's statements that the executable
guards and fixture prove the complete V35-V48 predecessor set are false.

This violates the approved design's explicit V35-V48 fresh-realm requirement
and weakens the spent-gate/no-retry boundary: the candidate cell can proceed to
runtime import in a realm that still contains V47's consumed state or retained
tab declaration. A later external declaration audit is mandatory defense but
does not make the executable's required internal guard or its claimed fixture
coverage complete.

Required fix: add all seven V47 `typeof ... === "undefined"` terms before the
V48 terms; add a contamination case for each persistent V47 declaration; update
the brief, mechanical-delta description, tuples/hashes, and review package; and
produce a new passing fixture terminal before a fresh review.

### V49-002 — IMPORTANT — one-proof-only cleanup is specified but not exercised by the fixture

The approved design requires the pure fixture to cover one-proof-only failure
cleanup, specifically the V48-incident boundary: one fixed state-only cleanup
proof after a failed/uncertain result, no corrected or second query if that
proof fails, then immediate realm reset. The fixture contains no cleanup-proof
operation, proof-attempt counter, proof-failure vector, second-query sentinel,
or reset-order assertion. Its `fixedFailureCleanup=true` terminal summarizes
the executable's internal binding cleanup and terminal-write cleanup only; it
does not prove the separate post-result cleanup procedure.

The executable appropriately contains no external cleanup query, so this
procedure must remain coordinator-owned. Nevertheless, the committed fixture
and package claim coverage required by the design without an inert model that
can prove exactly-one attempt and zero correction attempts. This leaves the
specific failure mode disclosed by V48 untested.

Required fix: add a smallest inert coordinator-cleanup fixture model that
asserts exactly one fixed state-only proof attempt, immediate reset after both
proof success and proof failure, and zero corrected/second queries; expose an
unambiguous terminal boolean/counter set and update the brief/package hashes.

## Regression review of remaining security contract

Subject to the two blocking findings, the direct bytes preserve the other V47
semantics:

- V49 consumption occurs before validation/import, with one import, setup,
  Chrome connection, documentation read/write, name, `openTabs`, exact-record
  claim, account-home navigation/wait/URL/snapshot, token-page navigation/URL,
  and bounded readiness sequence.
- The listing validator uses own data descriptors, never calls accessors,
  inspects only rank zero as a record, rejects every present non-string value
  including `undefined`, accepts an absent optional field, enforces the full
  HTTPS Cloudflare-origin predicate, and passes the exact returned record to
  `claimTab` only after complete validation.
- Account-home requires the exact 32-lowercase-hex `/home` form, one `mysw.me`
  zone link, positive anchors, and no busy indicator. Token-page readiness
  preserves the exact URL, unique search/root/paginator bindings, baseline
  completeness, fixed filter, four bounded readiness attempts/fulfillments,
  exact empty terminal, disabled controls, Create count one, and zero token-name
  and matching-row counts.
- PASS retains only the V49 task-tab binding plus minimal flags and clears
  attachment/runtime aliases. Failure and terminal-output failure detach both
  bindings, clear broad aliases/evidence, avoid thrown-value inspection, and
  perform no second terminal write.
- Output is fixed-schema and excludes raw listing, descriptor, record, ID,
  title, URL, account segment, DOM text, thrown value, clipboard, credential,
  token, or secret data. Create is counted but never clicked; no provider,
  route, DNS, VM, storage, cookie, clipboard, token-secret, tab-create/close,
  retry, reconnect, fallback, override, or manual-continuation path exists.
- V47 and V48 remain consumed, ineligible, non-authorizing, and unavailable for
  retry, continuation, reuse, reinterpretation, or relaxation. V48's corrected
  second cleanup query remains disclosed non-authorizing incident evidence.
- The final Create/native Copy/native masked Paste confirmation and the later
  separate exact-row deletion confirmation remain external, mandatory,
  action-time, and unreached.

## Authorization boundary

No execution classification or coordinator tuple may be produced from this
FAIL. A corrected candidate requires a new exact review package and independent
zero-finding Sol High review. Even after a future PASS, live execution remains
blocked on a non-self-referential classification, separate coordinator tuple,
candidate/runtime/docs pins, clean evidence worktree, public DNS absence, zero
local residue, VM1205 safe checkpoint, exact 12-path baseline, stable projection,
sole lane/current task, fresh CUA realm, complete direct declaration audit, and
new exact external profile/window/tab/non-conflict confirmation.

## Severity counts

- Critical: 0
- HIGH: 1
- IMPORTANT: 1
- Minor: 0
