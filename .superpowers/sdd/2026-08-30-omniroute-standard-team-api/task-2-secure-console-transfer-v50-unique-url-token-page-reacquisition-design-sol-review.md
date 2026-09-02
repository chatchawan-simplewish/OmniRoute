# OmniRoute V50 unique-URL token-page reacquisition design Sol High review

Date: 2026-09-03 (Asia/Bangkok)
Reviewer: Codex, independent `gpt-5.6-sol` High security review
Exact design commit: `658ca83801279f65ca52b183cb01006473565ec4`
Direct parent / V49 live-result commit: `d1c70a8a0547f23a441e7cf031a53b9198de4b37`

## Verdict

`FAIL`

`implementation_may_proceed=false`

`authorizes_live_execution=false`

The proposed unique-target selection is directionally safe, but the design
does not implement its claimed single semantic change. It makes a documented
optional URL mandatory and applies target-origin restrictions to every
unrelated tab. In the explicitly allowed shared-profile topology, a legitimate
unrelated tab can therefore spend V50 before the unique exact token-page record
is considered.

## Exact review boundary

The design was read directly from commit
`658ca83801279f65ca52b183cb01006473565ec4`. It is 6676 bytes, SHA-256
`735F0B1504B27022CD00D9E04FA7BEB9372F0E1341C4FE954FFD61D74C24F661`,
Git blob `20777176ba6cdf1fc035e39bc511559b05ea7921`. The commit changes exactly
that one design path and directly follows the committed V49 live result.

The review rechecked project-root `AGENTS.md` (blob
`cc76b1d408fcf11f4d4ce015f85f6266cb680a42`), the final V49
design/brief/executable/fixture/PASS-review/live-result blobs
`a656719c528d1fcd20ccea301cb94e4628b16ace`,
`f9f5fac1a2c767344f5f07e77c79f6e1cf66ad6a`,
`126b81d3f9ace97ca0afdae514a3c4f3305b3b6c`,
`80a0c3de005e1e8730257c3421edfe25daaf2975`,
`0a56a2ff571bd30bdcefbfdced3df2c61e809689`, and
`cfc5a51837c1813a37b98edae77300c9f1515ac0`; the V48 live evidence
blob `7ee54b84afd6a407074fa678dfa5fe7831cc58d1`; and the V4 replacement
brief plus zero-finding static review.

No CUA, browser, provider, network, VM, DNS, clipboard, credential, secret, or
live-gate action was performed. The index was empty and the exact pre-existing
12-path dirty product baseline was not changed or staged.

## Finding

### V50-001 — IMPORTANT — unrelated tabs are subjected to target-only URL requirements

The narrow-decision section says V50 removes only V49's rank-zero assumption
and chooses exactly one fully validated record whose URL is the exact API
Tokens URL. The selection section instead requires every offered record to
have both `id` and `url`, and requires every URL to be HTTPS with no username,
password, or explicit port before distinguishing the exact match.

That is a material extra semantic change:

- the installed API surface documents `url?: string`, and V49 deliberately
  accepts an absent URL as a valid structural branch;
- the design explicitly permits other tasks to use other tabs in the same
  Chrome profile;
- an unrelated valid tab may consequently have no URL metadata, an `http:`,
  `chrome:`, or other non-HTTPS URL, or a legitimate explicit port; and
- none of those unrelated records can be the exact target, yet any one of them
  makes the entire proposed V50 listing fail and permanently spends the
  one-shot gate before claim.

This is especially important because V49's raw rejecting property remains NOT
PROVEN and V48 inspected record semantics only at rank zero. There is no direct
evidence that every later-rank unrelated record satisfies the new mandatory-
URL/HTTPS/no-port predicate. The design therefore risks repeating a clean but
non-diagnostic listing rejection while claiming to solve shared-profile rank
instability.

Required correction: preserve the strict array and safe-record/data-descriptor
validation, but keep `url` optional for nonmatching records. A missing URL is a
nonmatch. For each present URL, first require the bounded non-empty control-free
data string; then define candidate membership by exact equality to
`https://dash.cloudflare.com/profile/api-tokens` (or an equivalently explicit
canonical predicate that cannot broaden the target). Unrelated safely read URL
values must be allowed to be nonmatching without inheriting the target's HTTPS,
host, path, query, fragment, or port requirements. Malformed/accessor/hostile
record structure may still fail closed. Require fixtures for an exact target
alongside URL-absent, `http:`, internal-scheme, and ported unrelated tabs, plus
zero and duplicate exact-target cases.

## Passing areas retained after correction

- V49 and V48 are accurately treated as consumed, permanently ineligible,
  non-authorizing, and unavailable for retry, continuation, reuse,
  reinterpretation, or relaxation. V49's rejecting property remains NOT
  PROVEN rather than inferred from V48.
- V50 is a new consumed-first one-shot gate. Zero or multiple exact target
  records fail closed; only the exact returned object may be claimed once after
  complete cached validation, with no ID reconstruction or raw identifier/URL
  output.
- The design preserves the reviewed account-home signature and V4 token-page
  semantics: exact navigation, unique search/root/paginator binding, complete
  baseline, fixed query, exact echo and empty terminal, disabled controls,
  zero rows/busy/name matches, one Create control, and exact counters.
- PASS retention is limited to the V50 owned token-page binding and minimal
  flags. Failure clears both bindings and broad aliases; terminal output is
  sanitized; only one state-only cleanup proof precedes immediate reset, with
  no corrected second query.
- Create remains count-only. No Copy, clipboard, secret, credential, storage,
  cookie, DNS, routing, VM/provider mutation, tab creation/close, reconnect,
  retry, fallback, override, alternate path, verdict relaxation, or manual
  continuation is authorized.
- The complete V35-V49 predecessor guard and matching action-time direct
  declaration audit remain required.
- Final Create/native Copy/native masked Paste and later exact-row deletion
  confirmations remain separate, external, mandatory, and unreached.

## Authorization and next step

Implementation may not proceed from this FAIL. A corrected design requires a
new independent zero-finding Sol High review before implementation. Even a
future design PASS will not authorize live execution: committed candidates,
their direct-byte review package and independent implementation PASS, a later
non-self-referential classification, separate coordinator tuple, action-time
pins, fresh realm, declaration audit, sole token-object lane, and a new exact
external profile/window/tab/non-conflict confirmation remain mandatory.

## Severity counts

- Critical: 0
- HIGH: 0
- IMPORTANT: 1
- Minor: 0
