# OmniRoute V44 fresh-realm token-page readiness — implementation review brief

Status: proposed replacement package for independent review.

`authorizes_live_execution=false`

## Replacement boundary

V43 was never executed. Its action-time check stopped after the tool-required
`cua.getState()` and a state-only declaration audit because the pinned Chrome
runtime path no longer existed. No browser client was imported, no tab was
claimed or navigated, no provider read or write occurred, and the CUA realm was
reset. The incident is committed at `f41691acb` in
`task-2-secure-console-transfer-v43-runtime-path-drift-incident.md`.

V43 is unconsumed but superseded, static, and permanently ineligible. It must
never be executed, retried, reinterpreted, continued, or used as fallback.

V44 is the smallest replacement: it changes the gate identity and result labels,
pins the installed `26.831.21537` runtime path, and rejects every V43 predecessor
declaration. All V43 semantic, security, completeness, no-residue, no-retry,
secret, confirmation, counter, output, and cleanup constraints remain unchanged.

## Immutable candidate package

- Executable:
  `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v44-fresh-realm-token-page-readiness-executable.js`
- Executable length: `39687` bytes.
- Executable SHA-256:
  `75F4700B6519A1EA519FE509053735B85E1690A25D5C302B566293A86BF82F67`
- Pure fixture:
  `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v44-pure-fixtures.mjs`
- Pure fixture length: `46332` bytes.
- Pure fixture SHA-256:
  `C9CA54C48A846B83C7D31F72EE609C40088A8B669C6A6AE90B4643AF1762F799`
- Browser client module:
  `C:\Users\chatc\.codex\plugins\cache\openai-bundled\chrome\26.831.21537\scripts\browser-client.mjs`
- Browser client length: `149771` bytes.
- Browser client SHA-256:
  `A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`
- Browser client API documentation:
  `C:\Users\chatc\.codex\plugins\cache\openai-bundled\chrome\26.831.21537\docs\api.json`
- API documentation length: `58480` bytes.
- API documentation SHA-256:
  `A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`

The fixture must report `V44_PURE_FIXTURES_PASS` and must print the directly
computed executable, fixture, and brief byte/hash tuple. Review and later
classification must pin those direct bytes without self-reference.

## Exact operation contract

V44 is a one-shot, no-retry readiness gate. The complete committed executable is
the only permitted live cell. It declares only new V44 bindings and marks the
overall V44 gate consumed before validation or dynamic import.

Before import, it proves exact fresh V44 defaults and absence of every named
V35-V43 consumed, controller, owned-tab, eligibility, state, detach, runtime,
agent, and Cloudflare-read declaration. Any declaration contamination stops
before setup, import, tab listing, claim, navigation, read, or write.

The browser module and API documentation must exist at the exact pinned paths
with the exact pinned lengths and SHA-256 hashes. There is one import, one
`openTabs()`, one `claimTab()`, one Cloudflare account navigation, one API-token
page navigation, one row-read attempt, and one non-provider field fill. There
is no click, Create, token copy, clipboard read, secret read, storage/cookie read,
or provider mutation.

The trusted listing must be complete, non-truncated, duplicate-free, and contain
only the user-offered Chrome profile/window. The rank-zero selected tab must be
the unique intended Cloudflare API Tokens task tab and must satisfy every V43
page signature. Any ambiguity, mismatch, interstitial, login state, challenge,
or incomplete listing fails closed.

Success retains only the V44 owned task-tab binding and its exact eligibility
state. Failure clears all V44 phase bindings and broad runtime/controller aliases,
detaches any claim made by V44, and reports only redacted structural evidence,
counters, and cleanup status. It must not print, log, commit, or retain secrets.

## Fixture coverage

The pure fixture checks executable syntax; exact single-call topology; forbidden
provider/clipboard/storage actions; trusted-list completeness; rank-zero and
unique-intended-tab semantics; page signatures; all validation, import, listing,
claim, navigation, read, and fill failure branches; V35-V43 declaration
contamination; one-shot counters; exact result schema; and success/failure
cleanup with no residue.

## Action-time boundary

No live execution is authorized by this brief. First require:

1. an exact-path candidate commit;
2. an independent `gpt-5.6-sol` High PASS review committed separately;
3. a non-self-referential classification committed on the review parent; and
4. a post-commit coordinator tuple proving the chain, exclusions, clean index,
   exact 12-path dirty product baseline, and unchanged outside projection.

Immediately before any live attempt, revalidate the candidate bytes and hashes,
runtime/documentation pins, clean evidence worktree, DNS absence, zero local
residue, VM1205 safe checkpoint, and sole ownership. Then reset the CUA realm.
After that reset, obtain a fresh exact external confirmation that Chrome Profile
`Codex-Chrome-Bell-PC2`, the intended window, and intended Cloudflare task tab
are selected and that no other Chrome profile/window is offered to the extension.
An earlier confirmation cannot be reused.

The first call in that fresh realm must be exactly `await cua.getState();`.
It must prove the sole offered Chrome profile and rank-zero intended API Tokens
tab. A following state-only audit must prove every V35-V44 declaration absent.
Only then may the exact committed V44 cell be sent once.

Any failure, uncertainty, exception, timeout, drift, unexpected output, or cleanup
doubt spends V44 and stops. There is no retry, fallback, manual continuation,
override, verdict relaxation, or reuse.

The mandatory final Create/native Copy/native masked Paste confirmation and the
later separate exact-row deletion confirmation remain external, mandatory, and
unreached.

`authorizes_live_execution=false`
