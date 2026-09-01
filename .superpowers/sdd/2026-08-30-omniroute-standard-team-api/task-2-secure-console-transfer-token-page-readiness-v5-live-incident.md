# Task 2 V5 live incident

Date: 2026-09-01 (Asia/Bangkok)

## Static chain

- V5 brief commit: `8aaa90a22720d7f59928939959fc3ebf82bb39e7`
- independent Sol High PASS review commit:
  `50e0bfb350e294d089b6b9674628edb7ec63b5f1`
- non-self-referential classification commit:
  `bbf67701b165940eed49e771ab29a258cd012c37`

## Consumed live result

V5 Call 1 was executed exactly once in the sole owner task and returned the
exact attachment PASS. Its counters were one attempted and one fulfilled
Chrome attachment, one attempted and one fulfilled complete-documentation
read, and no attachment error.

V5 Call 2 was then executed exactly once in the same persistent JavaScript
session. It returned `PRECONDITION_FAIL` with:

- selected-tab call attempted once and fulfilled once;
- controller ownership false and tab shape false;
- navigation, URL, semantic readiness, fill, Create, token-name, and row calls
  all zero;
- error class `Error`;
- consumed true;
- V4 binding ineligible, null, and state
  `V5_REACQUISITION_OR_READINESS_FAILED`.

No opaque browser identifier or secret value is retained in this evidence.

## Fail-closed disposition

V5 is consumed and failed. It must never be retried, continued, reinterpreted,
or used to authorize downstream V4 execution. V4 prestart was not executed.
Because V5 Call 2 created no tab, neither V4 detach cell is permitted or
needed for this failure.

No navigation, provider action, Create/edit/delete, clipboard action, secret
capture, proxy start, listener start, retained owner start, routing change,
credential change, VM mutation, or Cloudflare-persistent change occurred.

Only a new, independently reviewed replacement contract may use the surviving
fresh-session Chrome controller. That replacement must treat this exact V5
terminal state as its predecessor, remain one-shot/no-retry, preserve the V4
semantic page signature and completeness rules, and fail closed with a null
ineligible V4 binding.
