# V52 source-projection rebaseline implementation plan

## Inputs and boundary

- V52 design commit: `b3fb1b2ce53b0ae0e14e7eef4c8feca0adce2eb1`
- Independent V52 design PASS: `06cff41585f3118a5fda03c64467ef9a01915ec2`
- Reviewed pre-fix candidate: `fe6b9618cfbf46b55b4a55908b37acd9de6c7fab`
- Pre-fix direct-byte package: `9b956bd4d47fa686474c645bd9e10e7507e6741d`
- Source executable: final committed V51 executable
- Source fixture: final committed V51 pure fixture
- New predecessor boundary: retain all seven V50 declarations and add all seven
  V51 declarations

This is offline candidate construction only. It performs no CUA, browser,
provider, network, DNS, VM, clipboard, credential, secret, or live-gate action.

## Task 1 — Derive exactly four candidates

Create or replace only:

- `task-2-secure-console-transfer-v52-source-projection-rebaseline-brief.md`
- `task-2-secure-console-transfer-v52-source-projection-rebaseline-implementation-plan.md`
- `task-2-secure-console-transfer-v52-source-projection-rebaseline-executable.js`
- `task-2-secure-console-transfer-v52-source-projection-rebaseline-pure-fixtures.mjs`

Mechanically rename final V51 ownership, state, result, and marker literals to
V52; retain V51's seven V50 predecessor guards and add seven V51 predecessor
guards; and bind the fixed-exclusion source
projection to `10619` / `89D36435A31AE04E560A27D53D8A0953F19E837DF60837FADCF3DC174C0B9477`.
Preserve all downstream browser, account-home, token-page, counter,
output, privacy, retention, failure-cleanup, terminal-output, and one-proof-only
semantics.

## Task 2 — Implement the sole semantic delta

Extend the fresh-realm guard through all fourteen V50 and V51 globals. Validate the exact
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

1. Node syntax validation of the V52 executable;
2. the V52 pure fixture, requiring `V52_PURE_FIXTURES_PASS`;
3. a direct normalized executable comparison to final V51 after removing only
   only the seven added V51 predecessor guards, V52 ownership literals, and refreshed
   runtime/documentation provenance;
4. source scans for exact operation counts and prohibited behavior; and
5. Git status/index checks proving the 12 product paths are unchanged and only
   the four V52 candidate paths enter the index.

Fixtures must cover exact, unrelated, absent, `http:`, internal-scheme,
explicit-port, zero, duplicate, hostile, predecessor, counter, privacy, PASS
retention, failure cleanup, terminal-output cleanup, one-proof-only cases, and
the exact V52 source-projection constants.

## Task 4 — Commit and stop before review

Stage with `git add -f` and the four exact candidate paths only, then commit
those four paths together. Do not create a report, review package, execution
classification, or live evidence artifact in this implementation step.

After commit, hand the immutable candidate bytes to an independent Sol High
reviewer. A later direct-byte package, zero-finding review, classification,
coordinator tuple, action-time pins, fresh declaration audit, and required
external confirmations remain mandatory before any live action.
