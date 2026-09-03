# V51 runtime-pin refresh implementation plan

## Inputs and boundary

- Corrected design commit:
  `22ed4ee1ce6e5263aa7b285330797de7951f0cdf`
- Independent design PASS review commit:
  `be427102721e31d86a95d2a0309e46bea3dbb71a`
- Source executable: final committed V50 executable
- Source fixture: final committed V50 pure fixture
- New predecessor boundary: all seven persistent V50 declarations

This is offline candidate construction only. It performs no CUA, browser,
provider, network, DNS, VM, clipboard, credential, secret, or live-gate action.

## Task 1 — Derive exactly four candidates

Create or replace only:

- `task-2-secure-console-transfer-v51-unique-url-token-page-reacquisition-brief.md`
- `task-2-secure-console-transfer-v51-unique-url-token-page-reacquisition-implementation-plan.md`
- `task-2-secure-console-transfer-v51-unique-url-token-page-reacquisition-executable.js`
- `task-2-secure-console-transfer-v51-unique-url-token-page-reacquisition-pure-fixtures.mjs`

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
   the reviewed selection block, seven V49 guards, and renamed evidence fields;
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
