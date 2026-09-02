# V49 fresh-realm token-page readiness implementation plan

## Inputs

- Approved design commit: `6fd3669ce`
- Independent design PASS review commit: `582968408`
- Source executable: final committed V47 executable
- Source fixture: final committed V47 pure fixture
- V48 predecessor declarations: `secureConsoleV48Consumed`,
  `secureConsoleV48State`, and `secureConsoleV48Result`

No CUA, browser, provider, DNS, VM, clipboard, credential, or secret action is
part of this implementation plan.

## Task 1 — Derive the two V49 candidates

Create exactly:

- `task-2-secure-console-transfer-v49-fresh-realm-token-page-readiness-executable.js`
- `task-2-secure-console-transfer-v49-pure-fixtures.mjs`

Mechanically replace V47-owned names and literals with V49. Preserve all
functional V47 browser, listing, account-home, token-page, counter, output,
privacy, binding, and cleanup logic byte-for-byte except for the reviewed deltas
below.

Add the three V48 top-level declarations to the executable predecessor-absence
guard and to the fixture contamination loop. Add one fixture proving a present
optional `undefined` value is rejected before claim and retain an explicit
passing assertion for an absent optional key.

## Task 2 — Prove the declared delta

Run the smallest local checks:

1. Node syntax check for the V49 executable;
2. the V49 pure fixture, requiring exact terminal
   `V49_PURE_FIXTURES_PASS`;
3. a normalized comparison against V47 that maps V49 names/literals back to
   V47 and removes only the three V48 guard/contamination additions plus the two
   optional-key fixture assertions; and
4. source scans proving no retry, reconnect, Create click, Copy, clipboard,
   secret, provider mutation, alternate URL, or manual-continuation path was
   added.

Commit the executable and fixture together by exact path only. Preserve the
empty index after; preserve the exact 12 dirty product paths.

## Task 3 — Create the review package

Create one direct-byte review package containing:

- exact candidate commit and parent;
- candidate byte counts, SHA-256 values, and Git blob IDs;
- syntax and fixture terminals;
- normalized-delta proof;
- fixed runtime and documentation pins;
- exact no-residue and authority boundaries;
- V47/V48 disposition;
- every live-execution prerequisite; and
- `authorizes_live_execution=false`.

Commit the package alone by exact path. Do not create an execution
classification.

## Task 4 — Independent Sol High review

An independent `gpt-5.6-sol` High reviewer reads committed bytes and reviews
the full contract. PASS requires zero Critical, HIGH, IMPORTANT, and Minor
findings. A FAIL receives a focused fix round and a new review artifact; no
classification or live action follows a FAIL.

## Task 5 — Classification and coordinator tuple

Only after exact independent PASS:

1. commit a non-self-referential execution classification alone on the exact
   PASS review parent;
2. record a separate coordinator tuple proving exact chain, exclusions, hashes,
   empty index, exact 12-path dirty baseline, and stable outside projection; and
3. stop before CUA until every action-time precondition and a new external tab
   confirmation are present.

The final Create/native Copy/native masked Paste confirmation and later separate
exact-row deletion confirmation remain mandatory and outside this plan.
