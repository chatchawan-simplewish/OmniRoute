# V46 token-page readiness live result

Date: 2026-09-02 (Asia/Bangkok)

## Verdict

`V46_TOKEN_PAGE_SEMANTIC_READINESS_FAILED_STOP`

V46 was consumed exactly once and is permanently spent. It must never be
retried, continued, reused, or reinterpreted.

## Sanitized evidence

The fresh-realm attachment stage passed:

- result `EXACT_V46Attachment_CROSS_REALM_TASK_TAB_ACCOUNT_HOME_REACQUISITION_PASS`;
- sole offered candidate count `1`;
- candidate URL present and Cloudflare-qualified;
- controller ownership and tab shape passed;
- account-home URL and semantic snapshot passed;
- snapshot counters were bounded: one exact zone link, `112` anchors, and zero
  busy indicators; and
- every attachment operation counter matched its exact reviewed value.

The downstream token-page stage failed cleanly:

- declaration, predecessor state, controller ownership, tab shape, and exact
  token-page navigation passed;
- binding, navigation, and URL counters each attempted and fulfilled once;
- failure occurred before the first readiness wait;
- search fill, Create-control read, token-name read, and matching-row read were
  never attempted;
- result state was `V46_TOKEN_PAGE_SEMANTIC_READINESS_FAILED`;
- the V46 tab binding was null and ineligible;
- predecessor runtime/controller bindings were cleared; and
- ordinary failure cleanup reported complete.

The reviewed catch intentionally emitted only the fixed `Error` class. The
exact failing predicate among the pre-readiness token-page structural checks is
therefore **NOT PROVEN** and must not be inferred.

## Provider and secret boundary

- No Create control was clicked.
- No API token was created.
- No secret was read, copied, pasted, printed, logged, or committed.
- No provider-persistent change occurred.
- The filter value was not changed by V46.
- The mandatory final Create/native Copy/native masked Paste confirmation and
  the later separate exact-row deletion confirmation remain unreached.

## Cleanup proof

One state-only cleanup query proved:

- consumed true;
- retained tab binding null;
- eligibility false;
- exact failed state true;
- pre-Create detach unconsumed;
- post-native detach unconsumed; and
- Cloudflare reads unconsumed.

The CUA realm was reset immediately after that proof.

## Continuation boundary

Stop after committing this sanitized incident. Any further live attempt
requires a new, independently reviewed replacement contract with a new gate.
V46 cannot supply evidence or authority for that replacement.
