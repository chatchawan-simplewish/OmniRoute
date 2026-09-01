# OmniRoute V10 structural diagnostic — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only commit
`39dcae3a99728680dd473d58d097c83212b34ad1` and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-token-page-readiness-v10-structural-diagnostic-brief.md`.
Its direct parent is immutable V9 clean incident commit
`0c5acc372e9d1f88b362adde8e61192067988a32`.

I reviewed predecessor exactness, bounded diagnostic candidates and outputs,
call cardinality, durable exact-handle retention, exact-close acceptance,
failure residue, no-retry/no-provider-mutation boundaries, secrets, and
preserved downstream confirmations.

I performed no Chrome, browser, provider, clipboard, credential, process,
network, routing, Prox-01, or VM action and did not execute the V10 cell. The
only workspace write is this assigned review artifact. No baseline source path
was modified or staged.

## Final verdict

**FAIL** — one unresolved **HIGH** malformed-result/output-boundary finding
blocks PASS.

## Git and direct-byte pins

- V10 commit: `39dcae3a99728680dd473d58d097c83212b34ad1`.
- Direct parent: `0c5acc372e9d1f88b362adde8e61192067988a32`.
- The V10 commit adds exactly the V10 brief path; reviewed HEAD equaled that
  commit before this review commit.
- Index before review: zero paths. Exact inherited dirty baseline: twelve
  source records, preserved and not staged.
- V10 brief: `19532` bytes, SHA-256
  `1384C8A511D0920A3A7073033A2793CB8AD45616DC193CC009ABE9F927679672`,
  Git blob `80866c24dfb8effc257c39a2e2a3f4611c536a3b`.
- Encoding is strict UTF-8 without BOM, LF-only, zero CR bytes, and exactly one
  trailing LF. `git diff --check` from the V9 incident parent to V10 passes.

## Executable fence and syntax

The brief contains exactly one `javascript` fence. Including its mandatory
final LF, the executable reproduces:

- bytes: `15369`;
- SHA-256:
  `8A9B782AB7FCD3D0A2953D11AD6D6CEFD38EAD25697CD45F29A6869AF669A78B`;
- top-level-awaited asynchronous JavaScript syntax: **PASS**.

The syntax check parsed an async wrapper without evaluating the V10 cell or
loading a live resource. The outer IIFE is awaited exactly once and has no
fire-and-forget `void` form.

## Finding

### HIGH — fulfilled diagnostic output is unvalidated before PASS and spread emission

The page evaluator's literal source intends to return exactly 60 fixed fields,
and the 60 names match `emptyStructure` with no missing, extra, or duplicate
name. Its reviewed normal expressions reduce raw page text, href, attributes,
and DOM state to booleans or integer counts/depths.

However, after the controller boundary the returned value is trusted directly:

```javascript
structure = await tokenFilter.evaluate((input) => {
  // DOM traversal and raw local comparisons
  return { /* intended fixed fields */ };
});
counters.diagnosticFulfilled++;
result = "V10_STRUCTURAL_DIAGNOSTIC_BODY_COMPLETE";
```

There is no check that `structure` is a non-null plain object, that it has the
exact 60-key allowlist, that each named boolean is actually boolean, or that
each count/depth is a finite integer in its permitted range. Static counts are
zero for `Object.keys`, `Number.isInteger`, and any non-null structure check.

The terminal then emits the controller-returned value without projection:

```javascript
nodeRepl.write({
  // fixed local fields
  ...structure,
  // cleanup fields
});
```

Consequences:

- a fulfilled `null`, partial object, or wrong-type value still increments
  `diagnosticFulfilled` and can become
  `EXACT_V10_STRUCTURAL_DIAGNOSTIC_PASS` after close;
- a fulfilled object with unexpected enumerable properties is emitted, so the
  booleans/integer-only output allowlist is not enforced at the controller
  boundary; and
- a malformed string is object-spread into character-valued properties,
  directly demonstrating that non-boolean/non-integer output can escape while
  the diagnostic body is treated complete.

This violates both the explicit malformed-value fail-closed rule and the
output confidentiality boundary. Because V10 is meant to support the next
one-shot readiness contract, false diagnostic completeness or raw unexpected
output is HIGH.

Required correction: receive the evaluator result into an untrusted temporary,
validate exact own-key equality and prototype/shape, validate every boolean and
every finite integer count/depth (including permitted sentinel/range rules),
and only then project the exact allowlisted fields into a locally constructed
safe `structure`. A mismatch must throw before `diagnosticFulfilled` and body
completion. Never spread the unvalidated controller-returned object into the
terminal output. Recompute and repin executable bytes/hash after correction.

## Rechecked passing constraints

Subject to the blocking finding above:

- the predecessor exactly requires consumed V9, null V9 retained handle,
  consumed V4 adoption, null/ineligible V4 binding in
  `V9_OWNED_TAB_READINESS_FAILED_CLEAN`, and all V4 detach/read gates still
  false, matching the immutable V9 incident;
- direct executable call cardinality is exactly one each for `tabs.new`, fixed
  `goto`, page-local locator `evaluate`, exact-handle `close`, and terminal
  `nodeRepl.write`;
- fill, click, press, clipboard, selected, list, get, connect/reconnect, retry,
  fallback, alternate-tab, screenshot, and detach call cardinality is zero;
- one chained fulfillment assignment retains the returned handle in local and
  durable V10 state before every later await;
- exact PASS is possible only after the exact close settles, the local and V10
  bindings are cleared, cleanup is `CREATED_TAB_CLOSED`, and residue is
  converged; close rejection and malformed handle fulfillment retain the
  returned value, while creation rejection remains residue-unproven;
- the consumed flag is set before the first creation attempt and no retry,
  fallback, reconnect, alternate tab, manual selector, detach, or cleanup
  improvisation exists;
- the intended diagnostic candidate set is structurally complete against the
  brief: unique placeholder connection/visibility/empty value; page
  table/grid/pagination/busy counts; nearest any/single/two-table and
  section/region/group ancestor depths and descendant metrics; status/empty,
  tbody/row/busy and Create-actionable counts; exact normalized Create text;
  actionable Create text; ARIA labels; same-origin exact/Create-like paths;
  and bounded data markers;
- all raw text, href, URL, role, attribute, and DOM values used by the literal
  evaluator remain local in its normal return path; only comparisons,
  booleans, counts, and bounded depths are deliberately returned;
- the only URL is the fixed public token page and only an equality boolean is
  deliberately emitted; no raw tab ID or URL is output;
- no Bearer value, JWT form, or 40-hex secret occurs in executable code; and
- there is no provider-persistent Create/edit/delete or page fill action. The
  exact token name, no-generated-secret rule, V4 detach ordering, final
  Create/native Copy/native masked Paste confirmation, later separate exact-row
  deletion confirmation, revocation hold, invalid-token proof, retained-owner
  disposition, and cleanup requirements remain preserved.

## Findings by severity

- Critical: none.
- HIGH: `1` unresolved — malformed evaluator output is neither rejected nor
  safely projected before diagnostic PASS/output.
- IMPORTANT: none.
- Minor: none.

## Residual limits

- This review proves only committed static bytes. It does not prove current
  browser, controller, provider, credential, process, VM, DNS, routing, or
  persistent-REPL state.
- V10 must not be classified or consumed from this FAIL review. A corrected
  contract requires a fresh independent Sol High review.
- Static review grants no execution authority.

## Final verdict

**FAIL**

Unresolved findings: Critical `0`, HIGH `1`, IMPORTANT `0`, Minor `0`.

`authorizes_live_execution=false`
