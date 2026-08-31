# Task 2 direct clipboard preflight v2 live report

Observed at: `2026-08-31 15:24:04` (`Asia/Bangkok`)

## Pinned authority and bytes

- Candidate brief commit: `c2e2ac2bdd1ffa9437773e97cbc2fe49afba62af`
- Candidate brief SHA-256: `A4693C150C9A4DD137D71BE3DE1C7A4BE297F5822A219C5D95F1E2CDD3612D57`
- Candidate brief size: `11317` bytes
- Independent PASS review commit: `936a17ebcc2cc1cf725446e453629dce755b46cd`
- Authority consumed: one user-approved non-secret clipboard preflight
- Retry count: `0`

## Redacted observations

```text
PREFLIGHT_V2_BASELINE_CLEAR_CALLS=1
PREFLIGHT_V2_BASELINE_READ_CALLS=1
PREFLIGHT_V2_BASELINE_EMPTY=TRUE
PREFLIGHT_V2_CHALLENGE_SHAPE=^OMNI-PREFLIGHT-[0-9A-F]{32}$
PREFLIGHT_V2_CHALLENGE_LENGTH=47
PREFLIGHT_V2_BROWSER_RESULT=BROWSER_UNCERTAIN
PREFLIGHT_V2_BROWSER_ERROR_CLASS=Error
PREFLIGHT_V2_TAB_STATE=OPEN_MUTATION_UNCERTAIN
PREFLIGHT_V2_COUNTER_OPEN=1
PREFLIGHT_V2_COUNTER_GOTO=0
PREFLIGHT_V2_COUNTER_FOCUS=0
PREFLIGHT_V2_COUNTER_SELECT_ALL=0
PREFLIGHT_V2_COUNTER_COPY=0
PREFLIGHT_V2_COUNTER_CLOSE=0
PREFLIGHT_V2_EXACT_TAB_CLOSED=FALSE
PREFLIGHT_V2_RETAINED_TAB_HANDLE=TRUE
PREFLIGHT_V2_CALL3=FORBIDDEN_NOT_RUN
PREFLIGHT_V2_COMPARISON_READS=0
PREFLIGHT_V2_FINAL_CLEAR_CALLS=0
PREFLIGHT_V2_FINAL_EMPTY_READS=0
PREFLIGHT_V2_CURRENT_CLIPBOARD_FINAL_STATE=NOT_PROVEN
PREFLIGHT_V2_RESULT=NOT_PROVEN_BROWSER_UNCERTAIN
PREFLIGHT_V2_RETRY_COUNT=0
```

The fresh challenge value and clipboard content are omitted. The baseline was
cleared and observed empty before the browser call. The fulfilled tab-create
call returned one exact handle. The subsequent `goto` promise rejected before
its fulfilled counter could increment, so the reviewed contract classified
remote browser state as uncertain and prohibited every later browser or
clipboard mutation. No focus, selection, copy, tab close, comparison read,
final clear, empty read, fallback, or retry occurred.

## Security boundary

- Overall verdict: **NOT PROVEN / FAIL CLOSED**.
- The non-secret preflight gate is consumed and may not be retried.
- The exact retained tab handle remains in the persistent Node REPL binding
  `directPreflightV2RetainedTab`; its actual remote open/navigation state and
  closure are not proven.
- The final current-clipboard state is not re-read. The copy counter is `0`,
  but no cleanup claim is inferred from that fact.
- No credential, token, authorization header, private identifier, Cloudflare,
  OmniRoute, VM1205, proxy/proof/R5, Rulesets, permission, deletion, evidence
  worktree, revocation, or other live-resource action occurred.
- `authorizes_live_execution=false`
