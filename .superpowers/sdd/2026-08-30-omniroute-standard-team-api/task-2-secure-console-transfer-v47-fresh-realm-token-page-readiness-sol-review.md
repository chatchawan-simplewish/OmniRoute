---
status: issues_found
depth: deep
files_reviewed: 7
findings:
  critical: 0
  high: 0
  important: 2
  minor: 1
  total: 3
---

# OmniRoute V47 fresh-realm token-page readiness — Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Verdict

**FAIL**

The new bounded search-control visibility wait is correctly placed and its
success/failure counter vectors are internally consistent. The V47 package is
nevertheless ineligible for classification or live use. Its executable omits
all seven V46 top-level declarations from the in-cell predecessor guard, while
the fixture has no V46 contamination case and still labels its guard evidence
as V45-only. Separately, the fixture asserts the predecessor V46 executable
hash rather than the pinned V47 executable hash, so it can report PASS without
proving the current executable pin. The executable and fixture also introduce
blank lines at EOF. PASS requires zero findings at every severity.

This is a static package-quality review only. It authorizes no CUA, Chrome,
provider, live-resource, VM, secret, confirmation, or authority-gate action.

## Reviewed lineage and direct bytes

- Authoritative V47 candidate:
  `ea7830005a32b71e26ffa63a9a6d61cf3ddcd71c`.
- Direct parent and V46 consumed-failure incident:
  `0b7944703a1b0219b3c37707a9ff8030c25d9028`.
- The candidate adds exactly the V47 brief, executable, and pure fixture.
- Brief: `6940` bytes; SHA-256
  `F8676FA9CA1B0B09828EE22A5379D62D72C1884E7EE56E2F9CCF854673F9F710`;
  blob `6ca469aa45d0ab2831b6dd3a2991f6d9391a3530`.
- Executable: `41045` bytes; SHA-256
  `359CC0E55C1C1944F8C4EDC00FAFD695C54988EFDD4FAAF5A3727BB80AF51A3E`;
  blob `7c75f92396163a4c351efdaa3086adc0704eefb3`.
- Pure fixture: `49287` bytes; SHA-256
  `330EF84E5A2CBBAE246584A8D9FB3405F7E632D69E52B04261EFC372D8BA8798`;
  blob `3eb827102cc8fe18581abbcfb42afe61b51f159e`.
- All three working-tree files exactly matched the candidate blobs when
  inspected. The executable and fixture passed syntax-only `node --check`.
  Per the assignment, the already-passing fixture was not executed.
- Reviewed V46 package executable:
  `a6bfbc5ad673f49bb3b69d26026b096d1d18cbbd`, `40894` bytes, SHA-256
  `55C8833CF0E405022B747298CE71E7ED6DCF4A301A6C429026A598004444050E`.
- Reviewed V46 Sol High PASS:
  `250a8c9b15bebd0335ff89c929306981eaf7fc53`.
- Reviewed V46 non-self-referential classification:
  `e9a179c507f09756630b575632f6e6a5ad8e6a0d`.
- Reviewed V46 live result at the incident parent: attachment PASS, exact token
  navigation PASS, failure before the first readiness wait, no filter fill or
  Create/name/row read, exact ordinary cleanup, realm reset, no secret, and no
  provider-persistent change. The exact failed pre-readiness predicate remains
  **NOT PROVEN**.
- Installed browser module remains `149771` bytes / SHA-256
  `A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`.
- Installed `docs/api.json` remains `58480` bytes / SHA-256
  `A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.
- The index was empty before review work. The exact pre-existing 12-path dirty
  product baseline was neither edited nor staged.

## Confirmed narrow wait behavior

A direct full blob diff from the reviewed V46 executable proves that, apart
from version/result/state renames and terminal whitespace, the only added
runtime operation is:

`await tokenFilter.waitFor({ state: "visible", timeoutMs: 20000 });`

It occurs immediately after constructing the existing search textbox locator,
before its count, attribute, controlled-root, or paginator checks. The pinned
runtime implements `Locator.waitFor({ state, timeoutMs })`, and the new timeout
is bounded at 20 seconds. V47 increments `readinessAttempted` immediately before
the await and `readinessFulfilled` immediately after it. PASS therefore requires
exactly four readiness attempts and four fulfillments: the new textbox wait,
the preserved paginator wait, query-echo wait, and empty-status wait.

The fixture adds a `tokenFilterWait` failure and correctly shifts every later
failure vector and the successful vector from three to four. It retains fixed
top-level and attachment schemas, hostile thrown-value checks, zero getter-call
expectations, and ordinary/documentation/final-output cleanup checks.

## Preserved boundaries outside the findings

- V47 marks its consumed flag before predecessor validation or import. The
  attachment and downstream operation topology otherwise preserves the
  independently reviewed V46 path: one import, setup, Chrome connection,
  documentation read/write, session name, `openTabs`, exact-object claim,
  account navigation/wait/URL/snapshot, token navigation/URL, fixed non-secret
  fill, and bounded page reads.
- Trusted listing inspection remains descriptor-only, cross-realm safe,
  bounded, and nonobservant of later-record values. Optional URL absence stays
  accepted; any present URL remains exact HTTPS `dash.cloudflare.com` with no
  port, username, or password. The cached rank-zero record object is supplied
  to the sole `claimTab` call.
- Account-home and token-page signatures, fixed outputs, completeness counters,
  success transfer, ordinary failure cleanup, documentation-output cleanup,
  final-output cleanup, and rethrow-by-identity semantics are otherwise the
  V46-reviewed logic.
- Source topology contains exactly one dynamic import, `openTabs`, `claimTab`,
  account navigation, token-page navigation, new textbox wait, and fixed filter
  fill. There is no `.click`, clipboard, local/session storage, or cookie path.
- No Create, Copy, Paste, credential, token-secret, DNS, routing, VM, provider
  mutation, tab-create/close, reconnect, retry, fallback, override, verdict
  relaxation, or manual-continuation path was introduced.
- V46 remains consumed and permanently spent. V4/V44/V46 semantic,
  completeness, no-residue, no-retry, secret, counter, output, and confirmation
  constraints remain binding. The final Create/native Copy/native masked Paste
  confirmation and separate exact-row deletion confirmation remain external,
  mandatory, action-time, and unreached.
- No browser setup, Chrome connection, tab enumeration/claim/navigation,
  provider read/write, secret operation, DNS/network/VM action, confirmation,
  or gate consumption occurred during this review.

## Findings

### V47-001 — IMPORTANT — In-cell freshness guard and fixture omit every V46 predecessor declaration

The V47 executable's `predecessorDeclarationsAbsent` predicate is byte-for-byte
the V46 predecessor set and ends at `secureConsoleV45State`. A mechanical union
of V46's established 80-name V35-V45 set with V46's seven top-level bindings
requires 87 unique names. V47 contains only the prior 80, with these seven
missing:

- `secureConsoleOwnedTaskTabV46`;
- `secureConsoleOwnedTaskTabV46Eligible`;
- `secureConsoleOwnedTaskTabV46State`;
- `secureConsoleOwnedTaskTabV46PreCreateDetachConsumed`;
- `secureConsoleOwnedTaskTabV46PostNativeDetachConsumed`;
- `secureConsoleCloudflareReadsV46Consumed`; and
- `secureConsoleV46Consumed`.

Thus a realm containing, for example, only `secureConsoleV46Consumed` can pass
the in-cell predecessor predicate and proceed to import/setup/listing even
though the candidate requires a fresh post-V46 realm. The separate action-time
audit is mandatory but does not make this reusable one-shot cell fail closed if
that preflight is skipped, stale, or incorrectly relayed. This also contradicts
the claimed preservation of V46's predecessor-contamination defense.

The fixture reproduces the gap: its contamination matrix ends at V45 and has
no V46 case. Its terminal still reports `v45PredecessorsAbsent: true`, so its
PASS evidence neither tests nor claims the required V46 boundary.

Required correction:

1. Add all seven V46 top-level bindings to the executable's initial direct
   `typeof ... === "undefined"` predecessor predicate before import.
2. Add inert V46 contamination cases proving each security-distinct category
   consumes V47 but stops before import/setup/documentation/naming/`openTabs`
   and leaves exact cleanup.
3. Rename the fixed fixture terminal field to accurately cover the V46
   predecessor boundary, recompute package pins, commit a new immutable
   candidate, and obtain fresh independent review.

### V47-002 — IMPORTANT — Fixture self-consistency assertion pins V46, not the V47 executable

At fixture line 21, the sole executable-hash assertion checks
`55C8833...`, the reviewed V46 predecessor hash. The V47 brief necessarily
contains that value in its predecessor section, so the assertion succeeds even
if the brief's V47 executable hash is absent, wrong, or stale. The fixture never
asserts the actual V47 executable SHA-256
`359CC0E55C1C1944F8C4EDC00FAFD695C54988EFDD4FAAF5A3727BB80AF51A3E`.

The terminal computes and emits the V47 executable tuple, but its PASS status
does not establish that the brief pins that tuple. This weakens the immutable
package proof used by later classification for a no-retry gate.

Required correction:

1. Assert that the brief contains the directly computed V47 executable hash
   (and length, if retaining the existing exact-tuple convention).
2. If the predecessor V46 hash is also intentionally checked, keep it as a
   separately named predecessor assertion rather than substituting it for the
   current executable pin.
3. Recompute the changed fixture/brief tuple and obtain fresh independent
   review of the new commit.

### V47-003 — MINOR — Executable and fixture add blank lines at EOF

`git diff-tree --check` reports new blank lines beginning at executable line
883 and fixture line 1265. This does not alter runtime behavior, but the V47
contract requires zero Minor findings for PASS and every byte change forces new
immutable hashes. Trim both files to one final LF when preparing the fix.

## Severity counts

| Severity | Count |
| --- | ---: |
| Critical | 0 |
| HIGH | 0 |
| IMPORTANT | 2 |
| Minor | 1 |

## Authorization statement

`authorizes_live_execution=false`

This FAIL review authorizes no V47 classification, live browser send,
provider/secret action, VM action, gate consumption, retry, fallback, or
confirmation consumption. A corrected immutable candidate requires a fresh
independent Sol High review, followed only after PASS by a separate
non-self-referential classification, post-commit coordinator tuple, all
action-time pins and fresh-realm audits, and every external confirmation.
