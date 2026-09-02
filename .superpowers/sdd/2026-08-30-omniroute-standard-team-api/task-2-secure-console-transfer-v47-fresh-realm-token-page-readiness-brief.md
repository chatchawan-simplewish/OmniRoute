# V47 fresh-realm token-page readiness replacement

Status: candidate only; live execution is forbidden until a separate independent
Sol High PASS review, non-self-referential classification, and post-commit
coordinator tuple are complete.

## Purpose and predecessor

V46 was consumed exactly once and ended
`V46_TOKEN_PAGE_SEMANTIC_READINESS_FAILED_STOP`. Its attachment/reacquisition
stage passed, but the token-page stage failed after exact navigation and before
the first readiness wait. Search fill, Create read, row read, secret handling,
and provider mutation were never attempted. The exact failed pre-readiness
predicate is intentionally **NOT PROVEN**.

V46 incident evidence is commit
`0b7944703a1b0219b3c37707a9ff8030c25d9028`. V46 is permanently spent and
must never be retried, continued, reused, or reinterpreted.

The reviewed V46 executable was 40,894 bytes with SHA-256
`55C8833CF0E405022B747298CE71E7ED6DCF4A301A6C429026A598004444050E`.
V47 preserves that contract and makes one functional change: immediately after
constructing the existing token-search locator, it performs one bounded
`waitFor({ state: "visible", timeoutMs: 20000 })` before evaluating the locator
count or any dependent token-page structure.

This is an asynchronous-readiness repair, not a claim about V46's hidden error.
If the search control or any dependent structure is absent or drifted, V47
still fails closed.

## Exact candidate files

- Executable:
  `task-2-secure-console-transfer-v47-fresh-realm-token-page-readiness-executable.js`
- Executable length: `41045` bytes.
- Executable SHA-256:
  `359CC0E55C1C1944F8C4EDC00FAFD695C54988EFDD4FAAF5A3727BB80AF51A3E`
- Pure fixture:
  `task-2-secure-console-transfer-v47-pure-fixtures.mjs`
- Pure fixture length: `49287` bytes.
- Pure fixture SHA-256:
  `330EF84E5A2CBBAE246584A8D9FB3405F7E632D69E52B04261EFC372D8BA8798`

Any byte or hash drift invalidates review and execution eligibility.

## One-shot declarations and ownership

V47 uses only its fresh V47 declarations. Before execution a fixed direct
`typeof` audit must prove all V35-V47 predecessor and candidate declarations
absent in the fresh realm. The exact executable may be sent only once.

The attachment stage performs exactly one runtime import, setup, Chrome
connection, complete documentation read and terminal write, session name,
`openTabs`, claim of the exact rank-zero returned record, account-home
navigation, bounded wait, URL read, and semantic snapshot.

The trusted listing contract remains exact:

- an array with no symbols, own canonical index descriptors, and safe bounded
  length;
- rank zero only, with a plain record, no symbols, allowed own keys only, and
  own enumerable data descriptors only;
- mandatory bounded non-control `id`;
- optional `url`; if present it must parse to exact HTTPS host
  `dash.cloudflare.com` with no port, username, or password; and
- the exact validated returned record, not an ID reconstruction, is supplied
  to `claimTab` once.

Account-home readiness preserves exact HTTPS host, 32-lowercase-hex account
home path, exactly one `mysw.me` zone link, positive anchor count, and zero busy
indicators. Only the owned tab is transferred downstream on exact PASS.

## Token-page semantic readiness

The downstream stage performs one exact navigation to
`https://dash.cloudflare.com/profile/api-tokens`, one exact URL read, then:

1. constructs the unique textbox locator named `search api tokens`;
2. records one readiness attempt and waits at most 20 seconds for it to become
   visible;
3. records fulfillment, then requires count exactly one;
4. validates its bounded `aria-controls` ID and unique controlled result root;
5. requires one paginator and waits visibly for it;
6. proves the initial filter is empty and the baseline paginator/row/status
   state is complete;
7. fills the fixed non-secret search text
   `OmniRoute secure console R5 20260901` once;
8. waits for the exact query echo and exact empty status;
9. proves exact filter value, terminal `0-0 of 0`, zero rows, both navigation
   buttons disabled, no busy state, exactly one Create Token control, and zero
   exact token-name and matching-row occurrences.

The exact downstream readiness counters are now four attempts and four
fulfillments on PASS: search-control visibility, paginator visibility, query
echo, and empty status. All other V46 counters and completeness requirements
remain unchanged.

Create is counted but never clicked. V47 contains no Copy, clipboard,
credential, token-secret, storage, cookie, DNS, routing, VM mutation, provider
mutation, tab creation/close, reconnect, retry, fallback, override, verdict
relaxation, or manual-continuation path.

## Failure, output, and cleanup

Any failure, exception, timeout, drift, unexpected output, or cleanup doubt
spends V47 and stops. Operational catches are unbound and emit only fixed
booleans, bounded counts, exact counters, fixed state/result strings, and the
literal error class `Error`; thrown values, raw listings, IDs, URLs, account
segments, DOM text, credentials, and secrets are never serialized.

Every ordinary failure clears the V47 owned tab, eligibility, attachment tab,
all broad setup/agent/Chrome aliases, and records exact failed state. Terminal
output failure repeats cleanup and rethrows without inspecting or logging the
thrown value and without a second write.

After any failed or uncertain live result, run only one fixed state-only cleanup
proof, reset the realm, record sanitized evidence, and stop. No V47 retry or
continuation is permitted.

## Review and action-time prerequisites

Before classification, an independent `gpt-5.6-sol` High reviewer must verify
the exact candidate bytes, one-delta claim, pure fixtures, fixed outputs,
one-shot completeness, no-residue behavior, secret boundary, and every
preserved V4/V44/V46 semantic and confirmation constraint. Only zero Critical,
HIGH, IMPORTANT, and Minor findings is PASS.

After PASS, commit a non-self-referential classification on the review parent
and record a separate coordinator tuple proving exact chain/exclusions, clean
index, exact 12-path dirty product baseline, and unchanged outside projection.

Immediately before live use, revalidate candidate/runtime/documentation pins,
clean evidence worktree, DNS absence, zero local residue, VM1205 safe
checkpoint, sole ownership, and exact current-task identity. Then reset the CUA
realm, obtain a fresh exact external Chrome-profile/window/tab confirmation,
initialize only with `await cua.getState();`, and run the fixed declaration
audit before sending the exact V47 executable once.

## Mandatory later confirmations

The final Create/native Copy/native masked Paste confirmation remains external,
mandatory, action-time, and unreached. The later exact-row deletion confirmation
also remains separate, mandatory, and unreached. Standing unattended authority
does not waive either confirmation.
