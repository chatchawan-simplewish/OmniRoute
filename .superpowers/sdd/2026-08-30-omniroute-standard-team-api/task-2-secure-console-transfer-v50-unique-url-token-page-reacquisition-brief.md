# V50 unique-URL token-page reacquisition executable brief

## Authority and disposition

This candidate implements the corrected V50 design at commit
`22ed4ee1ce6e5263aa7b285330797de7951f0cdf` and its zero-finding Sol High
design review at commit `be427102721e31d86a95d2a0309e46bea3dbb71a`.
It does not authorize live execution.

V49 was consumed once, failed closed before claim, and is permanently
ineligible. It may not be retried, continued, reused, reinterpreted, or
relaxed. Its exact historical rejecting property remains **NOT PROVEN**.

## Exact source and candidate pins

- Final V49 source executable length: `42193` bytes.
- Final V49 source executable SHA-256:
  `D60CC7898F509013D19DFF1E7254065F5C2FF531386211A348CDF392F3D59988`
- Final V49 source fixture length: `52056` bytes.
- Final V49 source fixture SHA-256:
  `31A060E86A08432C56676B2D1A2A1C3107CD9076A16399C9BDF28A77E9B92585`
- Executable length: `42583` bytes.
- Executable SHA-256:
  `081E4AAD064E7F164E9A597396E4710158D11C85D2B448134D4722DC928E5433`
- Pure fixture length: `52118` bytes.
- Pure fixture SHA-256:
  `51A79ED3196769768C34000F6BF29C8B0C82503AF1BE3D381C3B837DC78C1FFD`

The four candidate paths are:

- `task-2-secure-console-transfer-v50-unique-url-token-page-reacquisition-brief.md`
- `task-2-secure-console-transfer-v50-unique-url-token-page-reacquisition-implementation-plan.md`
- `task-2-secure-console-transfer-v50-unique-url-token-page-reacquisition-executable.js`
- `task-2-secure-console-transfer-v50-unique-url-token-page-reacquisition-pure-fixtures.mjs`

All paths are under
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/`.

## Exact implementation delta

The executable is the final reviewed V49 executable mechanically renamed to
V50, with only these semantic additions:

- the fresh-realm predecessor guard extends through all seven persistent V49
  declarations;
- the bounded offered array is validated in full before selection or claim;
- every record must be an ordinary plain record with no symbols, only the six
  documented keys, a required enumerable data `id`, and enumerable data
  descriptors for every present field;
- every present field must be a bounded, non-empty, control-free string;
  absent `url` is a nonmatch, while present `undefined`, accessors, symbols,
  hostile structures, and unknown keys fail before claim;
- present URL strings are not parsed; safe unrelated `http:`, internal-scheme,
  explicit-port, and otherwise nonmatching strings remain valid nonmatches;
- exactly one record must have a URL literally equal to
  `https://dash.cloudflare.com/profile/api-tokens`; zero or duplicate exact
  matches fail closed; and
- only that exact returned record is passed once to `claimTab`, with no ID
  reconstruction, rank assumption, guessed reference, or alternate target.

The fixture is derived from the final V49 fixture and covers exact selection at
a nonzero rank, cross-realm input, absent URL, unrelated safe strings, `http:`,
internal-scheme, explicit-port, zero match, duplicate match, hostile arrays and
records, accessors, symbols, unknown keys, present `undefined`, every V49
predecessor declaration, exact counters, fixed output privacy, PASS retention,
failure cleanup, terminal-output cleanup, and one-proof-only cleanup.

## Preserved V49 and V4 behavior

V50 is consumed before validation or import. It performs at most one pinned
import, setup, Chrome connection, complete documentation read and write,
session name, `openTabs`, exact-record claim, each reviewed navigation, each
reviewed URL read, and each reviewed semantic snapshot.

After selection, the V49 flow remains unchanged: account-home navigation and
signature, exact token-page navigation, one visible search control with a
bounded `aria-controls`, one controlled results root, one visible paginator,
complete baseline, fixed non-secret filter `OmniRoute secure console R5
20260901`, exact echo, terminal `0-0 of 0`, zero rows, one empty status,
disabled pagination, zero busy state, exactly one Create Token control, and
zero exact token-name or matching-row occurrences. All attachment and
downstream counters and completeness predicates remain exact.

Create is counted but never clicked. There is no Copy, clipboard, token-secret,
credential, storage, cookie, DNS, routing, VM mutation, provider mutation, tab
creation or close, reconnect, retry, fallback, override, alternate path,
verdict relaxation, or manual continuation.

## Output, retention, and cleanup

Only fixed literals, booleans, bounded counts, exact counters, and fixed-schema
results may be emitted. Raw listings, descriptors, records, identifiers,
titles, URLs, account segments, DOM text, thrown values, credentials, tokens,
and secrets are never emitted or retained.

Exact PASS retains only the owned V50 token-page binding and minimal reviewed
flags. All broad runtime, browser, documentation, listing, record, URL, and
snapshot aliases are cleared. Any failure or uncertainty spends V50, clears
both bindings and every broad alias, emits at most one fixed sanitized terminal
result, and stops ineligible. One fixed state-only cleanup proof is allowed,
followed immediately by realm reset; proof failure cannot lead to a corrected
or second query.

## Review and live prerequisites

These candidates require a committed direct-byte review package, independent
Sol High implementation review with zero Critical, HIGH, IMPORTANT, or Minor
findings, a later non-self-referential execution classification, and a separate
coordinator tuple before any live send.

Action time still requires exact candidate/runtime/documentation pins, clean
evidence state, exact 12-path product baseline, stable outside projection,
public DNS absence, zero local residue, VM1205 safe checkpoint, sole token-
object lane, current task identity, fresh realm, a complete direct declaration
audit, and new external profile/window/tab/non-conflict confirmation.

The final Create/native Copy/native masked Paste confirmation remains separate,
external, mandatory, and unreached. The later exact-row deletion confirmation
also remains separate, mandatory, and unreached.
