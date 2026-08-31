# Task 19 v10 copy-button preflight live report

`authorizes_live_execution=false`

## Pins and action-time state

- Reviewed brief commit: `780b70c0432f7842be0858cb4faafd273cb8985e`
- Independent review commit: `599f32ce3518578b243c9bcebb232057da1f6f93`
- Brief bytes/SHA-256: `31745` /
  `6DF92C3128DD3B83D5DE1029DF97D14648776A13CF02F7AD896BBEF0B860BAA9`
- Review bytes/SHA-256: `12234` /
  `533C66B36B5DF701A4A06DF2B9DEABE00760E896CB6618B605E79A69AE7187CA`
- Project authority SHA-256:
  `AD0EA394F694C7795870C2B66D745EDC1FCA8997E7D7041A21E5659B0C349DDC`
- Git index count: `0`
- Preserved dirty source baseline count: `12`

## Call 1

- Exit: `0`
- Baseline clear attempted/fulfilled: `1 / 1`
- Baseline read attempted/fulfilled: `1 / 1`
- Baseline empty: `TRUE`
- Error: `NONE`

## Call 2

- `result=COPY_BUTTON_SETTLED_TAB_AND_SERVER_CLOSED`
- `errorClass=NONE`
- Challenge shape/length matched: `true / 51`
- Every required attempted/fulfilled counter: `1 / 1`
- Optional favicon request/response counters: all `0`
- Unexpected request count: `0`
- Tab state: `CLOSED`
- Exact tab closed: `true`
- Retained tab binding: `false`
- Server state/listening: `CLOSED / false`
- All uncertainty states: `false`

## Call 3

- `result=EXACT_MATCH_AND_FINAL_EMPTY`
- `errorClass=NONE`
- Child start attempted/exit fulfilled: `1 / 1`
- Child exit code: `0`
- Stdout schema valid: `true`
- Handoff/comparison reads: `1 / 1`
- Comparison match: `TRUE`
- Observed shape/length: `TRUE / 51`
- Comparison error: `NONE`
- Final clear attempted/fulfilled: `1 / 1`
- Final read attempted/fulfilled: `1 / 1`
- Final empty: `TRUE`
- Cleanup error: `NONE`
- PowerShell result: `PASS`
- Challenge binding retained: `false`

## Candidate disposition

- Candidate verdict: `PASS`
- Independent post-action classification: `PENDING`
- Retry/fallback/continuation: `0`
- Exact tab: `CLOSED PROVEN`
- Loopback server/listener: `CLOSED PROVEN`
- Windows clipboard final state: `EMPTY PROVEN`
- Direct `Tab.clipboard` actions: `0`
- Keyboard actions: `0`
- Screenshots: `0`
- DOM/page-content serialization: `0`
- Credential/key/token/routing actions: `0`

This candidate proves only the local DOM Clipboard-API copy-button path. It
does not prove that any Cloudflare credential control uses the same mechanism,
and it provides no credential or routing authority. The report exposes no
challenge value and contains only redacted labels, counters, booleans, lengths,
and pins. It does not authorize further live execution.
