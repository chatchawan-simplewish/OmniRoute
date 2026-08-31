# Task 7 loopback clipboard preflight v4 live report

## Authority and pins

- Standing unattended authority: project-root `AGENTS.md`.
- Brief commit: `04a75e8b61cfaaed73dc130687e9450a5b2d99c3`
- Brief bytes / SHA-256: `23134` / `3868288D89C6F0B84F81CE13A1385A44A8876B01800421FD91E58526C22F7CF8`
- Independent review commit: `aaa69494ecbde08634c78172eb05a37879174ec0`
- Review bytes / SHA-256: `9899` / `40023ADB8814692ACF2E751CFAECBC67689B76AC844150C3BDA185C22C4DA6C2`
- Action-time pins, review PASS, standing authority, empty index, and exact 12-path baseline: PASS.
- The fresh v4 one-shot authority is consumed and cannot be retried or continued.

## Call 1 — exact baseline PASS

The exact PowerShell 7 block ran once and returned exit `0`:

```text
PREFLIGHT_V4_BASELINE_CLEAR_ATTEMPTED=1
PREFLIGHT_V4_BASELINE_CLEAR_FULFILLED=1
PREFLIGHT_V4_BASELINE_READ_ATTEMPTED=1
PREFLIGHT_V4_BASELINE_READ_FULFILLED=1
PREFLIGHT_V4_BASELINE_EMPTY=TRUE
PREFLIGHT_V4_BASELINE_ERROR=NONE
```

## Call 2 — settled fail-closed result

The exact committed Call 2 cell was invoked once with the reviewed
`timeout_ms=120000` allowance. It returned within that allowance:

```text
result=SERVER_OR_PRECONDITION_UNCERTAIN
errorClass=Error
challengeShape=true
challengeLength=50
serverStart=1/1
serverRequest=2/1
serverResponse=1/1
serverClose=1/1
browserOpen=1/1
browserGoto=1/1
browserFocus=1/1
browserSelectAll=0/0
browserCopy=0/0
browserClose=0/0
tabState=FOCUSED
exactTabClosed=false
retainedTabBinding=true
serverState=CLOSED_AFTER_UNCERTAINTY
serverListening=false
serverUncertain=true
```

Evidence-bound disposition:

- the fresh loopback listener started and the main response fulfilled;
- the browser caused a second loopback request, violating the exact-one-request contract;
- sticky server uncertainty correctly stopped the sequence after field focus;
- select-all and copy were never attempted, so the contract made no clipboard write after the proven-empty baseline;
- the exact tab was intentionally retained after uncertainty and remains bound as `loopbackPreflightV4RetainedTab`;
- server close fulfilled and `serverListening=false`, proving the v4 listener is not retained; its earlier request-count uncertainty is not rehabilitated;
- no timeout, retry, fallback, alternate tab, later browser action, old-listener action, credential, or routing action occurred.

## Call 3 and stop boundary

- Call 3 attempts: `0`;
- child attempts: `0`;
- comparison/final-clear/final-empty-read attempts: `0`;
- retry/fallback attempts: `0`;
- later browser or clipboard actions: `0`.

Clipboard transport remains `NOT PROVEN`. The v4 tab residual is `NOT PROVEN`
until separately disposed; the v4 listener absence is proven by fulfilled close
and `serverListening=false`. The unrelated lost v3 listener/process residual
remains `NOT PROVEN`. Independent Sol High classification is required before a
new direct-binding tab-close contract is prepared.
