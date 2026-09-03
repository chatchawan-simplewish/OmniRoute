# OmniRoute V55 search-reset readiness design Sol High review

Date: 2026-09-03 (Asia/Bangkok)
Reviewer: Codex, independent `gpt-5.6-sol` High design/security review
Reviewed design commit: `2c857a4863ba46479d8f9827a0aa05b90af32bec`
Direct parent / final V54 incident diagnosis: `0e56bad8f6ff8e85ad3542c37390f7789c109a6d`
Initial V54 incident commit: `f5cd6ff22633cab7810745c343a99ac8e58dfb2c`

## Verdict

`FAIL`

`implementation_may_proceed=false`

`authorizes_live_execution=false`

The proposed replacement is appropriately narrow and avoids the exact V54
session-name escape failure, but three security-significant contract gaps and
two important specification conflicts must be corrected before implementation.

## Direct committed-byte evidence

Commit `2c857a486` is the direct child of the final incident diagnosis and adds
exactly the V55 design path. Direct Git-object reads produced:

| Artifact | Git blob | Bytes | SHA-256 | ASCII |
| --- | --- | ---: | --- | --- |
| V55 design | `36de772520c8b487da5775c134215a82938d9864` | 3490 | `05B9E5EFC037A5133170892ACC426136FBE36629DAF3CD6155DB777D0866292F` | yes |
| Initial V54 incident | `6a5c341f1c5f1a22768ed1e9eea72a7d0fc382b0` | 2934 | `5B4739A2E872389543B7A208C3DD8275A2FDCB2EFE41DAF2EF9BEAD129346FB9` | yes |
| Final V54 incident diagnosis | `6c72ce8a6fc235179383a475596665afc7331150` | 3515 | `EC69D20B3184B6C665E969B9F05B0E7DDB054E6B89B15BB3BAEAF9D7B399E165` | yes |
| V54 final Sol PASS | `916577c10d0bda59dcc6f468aaf912ce77b90a37` | 4771 | `F3AA0019D8F8FD4B448B91FBC571B503B53704666E1BB13604912D2193190F85` | yes |
| V54 classification | `aa4829b6df3b66c7c09a8675ceee119c2e5b3c8d` | 5615 | `056BE33B477DC72A849E9219525AF377E7D8F8627A76AB9642FE7E45943F143F` | yes |

No CUA, browser, provider, network, DNS, VM, clipboard, credential, secret, or
live action was performed. The review used committed artifacts and the current
project-root `AGENTS.md` only.

## Findings

### V55-HIGH-001 — HIGH — Initially empty input can skip convergence and retain a stale table

The URL and sentinel convergence steps are conditional on performing
`fill("")`. When the input is initially empty, the design performs no fill and
therefore does not require the exact base-URL wait/read or the no-results
sentinel hidden/detached wait/read before evaluating the inherited baseline.

The final V54 diagnosis directly proves that input emptiness can precede URL and
table convergence. In the dangerous state, an empty input and one non-busy
sentinel row can satisfy the inherited 1..1000-row, ordered-header, zero-target
baseline even though the table is still filtered. That permits false readiness
and can hide an existing target token from a later creation gate.

Required fix: make base-URL convergence and sentinel absence mandatory on both
branches. Only the clear itself is conditional: initial nonempty means exactly
one clear; initial empty means zero clears. Both branches must then prove exact
base URL, sentinel absent/hidden, final input empty, and the full unfiltered
baseline before target filtering or retention.

### V55-HIGH-002 — HIGH — V54 declarations are omitted from the fresh-realm audit

The design retains only the 125 fixed V35-V53 predecessor declarations. V54 was
actually sent and declared seven distinct persistent V54 bindings before it
failed. A V55 audit that stops at V53 can therefore accept a realm contaminated
by V54 state, including a retained runtime/tab/controller binding, contrary to
the fresh-realm and no-retry boundary.

Required fix: audit the inherited 125 names plus all seven persistent V54 names,
for 132 unique predecessor declarations. Fixtures must contaminate each name and
prove failure before import, attachment, browser effects, or page mutation.

### V55-HIGH-003 — HIGH — The inert payload proves capacity, not exact candidate-byte delivery

The design says exact candidate-byte preservation is proven by sending an inert
literal payload at least as long as the candidate. Such a payload proves only
that the transport accepts a cell of sufficient size. It does not submit or
compare the candidate bytes and cannot detect candidate-specific escaping or
transformation. V54 is direct evidence of this distinction: its larger inert
capacity proof passed, yet the actual reviewed `\\ud83d\\udd10` sequence was
transmitted as U+0017.

The V55 requirement that source and candidate be ASCII and construct the session
name with `String.fromCodePoint(0x1F510)` is sound and directly removes that
known escape. It does not make an unrelated capacity payload an exact-byte
proof.

Required fix: describe the inert probe only as a capacity check. Separately
define an exact transport-fidelity mechanism that compares the actual candidate
payload bytes with the committed blob/hash before execution, or a reviewed
equivalent that prevents any transformed candidate from reaching import or
browser effects. The implementation fixture must also assert ASCII source and
candidate, the exact `String.fromCodePoint(0x1F510)` construction, and absence of
literal emoji and all Unicode escapes.

### V55-IMP-001 — IMPORTANT — Exact branch and failure counter vectors are unspecified

The design requires exact counters but gives no numeric vectors for initially
empty versus initially nonempty input, nor for failures at URL wait/read,
sentinel wait/read, final input read, or baseline read. It is also ambiguous
whether the initially empty branch performs a second/final input read. An
implementation and fixture could choose matching but unintended counts and
still call them exact.

Required fix: enumerate the attempted/fulfilled vector for every reset-stage
counter on both success branches, and state earliest-stop vectors for each false,
throw, timeout, and malformed-read boundary. Keep target-filter, Create, and
retained-binding counters at zero for every reset failure.

### V55-IMP-002 — IMPORTANT — Manual browser confirmation contradicts current project policy

The final evidence paragraph makes an `exact external browser confirmation`
mandatory before the V55 send. Current root `AGENTS.md` requires the task to
self-verify browser, profile, window, tab ID, URL, provider object, and exclusive
control from current tool state for routine read-only or reversible work. It
explicitly says not to add owner-confirmation gates to programmatically
verifiable steps; owner input is required only for higher-priority policy,
critical irreversible action, or unresolved exclusive-control ambiguity.

Required fix: replace the external-confirmation requirement with exact action-
time tool-state self-verification and a fail-closed pause only if exclusivity is
ambiguous or a higher-priority rule requires confirmation. Preserve the separate
mandatory confirmations for final Create/copy/paste and row deletion.

## Retained properties without findings

V55 correctly marks V54 spent and forbids retry, continuation, fallback, or
verdict relaxation. Conditional `fill("")` is the smallest reversible page-state
mutation needed to clear a stale search, and all token creation, secret access,
clipboard, storage, persistent provider, DNS, VM, and tab mutation remains
prohibited. Failure cleanup, sanitized output, success-only binding, V54 pins,
and later independent review/classification gates are retained in principle.

## Severity counts

- Critical: 0
- HIGH: 3
- IMPORTANT: 2
- Minor: 0
