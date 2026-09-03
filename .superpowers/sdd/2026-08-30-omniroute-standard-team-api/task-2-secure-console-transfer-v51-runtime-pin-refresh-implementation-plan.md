# V51 runtime-pin refresh implementation plan

## Inputs and boundary

- V51 design commit: `06c792a0b0c9aa6bb59684431a7a5a8f48068948`
- Independent V51 design PASS: `86001a8e8fdc8f5fe50394f8cf152f0d0217c1c9`
- Candidate lineage: `adf131f77340a14bd1f602b9d49ea8de34ba8f2b`
- Direct-byte package: `f5a82e99f8fbb3824453b0238b4af816081c81a4`
- Source executable: final committed V50 executable
- Source fixture: final committed V50 pure fixture
- New predecessor boundary: all seven persistent V50 declarations

This is offline candidate construction only. It performs no CUA, browser,
provider, network, DNS, VM, clipboard, credential, secret, or live-gate action.

## Task 1 — Derive exactly four candidates

Create or replace only:

- `task-2-secure-console-transfer-v51-runtime-pin-refresh-brief.md`
- `task-2-secure-console-transfer-v51-runtime-pin-refresh-implementation-plan.md`
- `task-2-secure-console-transfer-v51-runtime-pin-refresh-executable.js`
- `task-2-secure-console-transfer-v51-runtime-pin-refresh-pure-fixtures.mjs`

Mechanically rename final V50 ownership, state, result, and marker literals to
V51. Preserve all downstream browser, account-home, token-page, counter,
output, privacy, retention, failure-cleanup, terminal-output, and one-proof-only
semantics.

## Task 2 — Implement the sole semantic delta

Extend the fresh-realm guard through the seven V50 globals. Validate the exact
bounded ordinary array and every record before claim. Require safe data
descriptors and strings, treat absent URL and safe unrelated strings as
nonmatches, reject hostile or malformed records, and select only when exactly
one safe URL string equals
`https://dash.cloudflare.com/profile/api-tokens`.

Claim that exact returned record once. Zero or multiple matches stop before
claim. Do not parse unrelated URLs, use rank, guess or reconstruct a tab ID, or
add any alternate target or continuation path.

## Task 3 — Prove the candidate

Run:

1. Node syntax validation of the V51 executable;
2. the V51 pure fixture, requiring `V51_PURE_FIXTURES_PASS`;
3. a direct normalized executable comparison to final V50 after removing only
   only the seven V50 predecessor guards, V51 ownership literals, and refreshed
   runtime/documentation provenance;
4. source scans for exact operation counts and prohibited behavior; and
5. Git status/index checks proving the 12 product paths are unchanged and only
   the four V51 candidate paths enter the index.

Fixtures must cover exact, unrelated, absent, `http:`, internal-scheme,
explicit-port, zero, duplicate, hostile, predecessor, counter, privacy, PASS
retention, failure cleanup, terminal-output cleanup, and one-proof-only cases.

## Task 4 — Commit and stop before review

Stage with `git add -f` and the four exact candidate paths only, then commit
those four paths together. Do not create a report, review package, execution
classification, or live evidence artifact in this implementation step.

After commit, hand the immutable candidate bytes to an independent Sol High
reviewer. A later direct-byte package, zero-finding review, classification,
coordinator tuple, action-time pins, fresh declaration audit, and required
external confirmations remain mandatory before any live action.
