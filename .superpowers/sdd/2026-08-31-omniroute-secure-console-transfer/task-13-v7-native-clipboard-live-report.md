# OmniRoute native clipboard bridge preflight v7 live report

`authorizes_live_execution=false`

## Pins

- Corrected brief commit: `a2b887bb4fad01343b5d2957a27363ee877c7c72`
- Brief bytes: `20581`
- Brief SHA-256: `9B84E07C0F6B5B3CBAEB0BD8A67B9D81139921F49011B113BC80D46D7285FDC9`
- Independent PASS review commit: `21ff7730e43352d5d1f6dbac782e64ed6067b230`
- Review bytes: `5522`
- Review SHA-256: `FC35706902F5E4EC12DA67573E86B74167CAC2772EADD49566C55252A1B6D13F`
- Bundled PowerShell: `301368` bytes, SHA-256 `DB6DD81183FE57D22E03B911EC9A30A2FD7C40542E97743615355A6FB44F458F`, version `7.6.4.500`
- Action-time validation: committed brief/review and executable pins matched; review was `PASS`; standing unattended authority was present; Git index was empty; exact 12-path dirty source baseline was preserved.

## Call 1

- Timestamp (Asia/Bangkok): `20260901 003527`
- Baseline clear attempted/fulfilled: `1 / 1`
- Baseline empty-read attempted/fulfilled: `1 / 1`
- Baseline empty: `TRUE`
- Error: `NONE`

## Call 2

- Timestamp (Asia/Bangkok): `20260901 003536`
- `result=NATIVE_WRITE_SETTLED_TAB_CLOSED`
- `errorClass=NONE`
- Challenge shape/length: `true / 50`
- Session-name, browser-open, native-write, browser-close attempted/fulfilled: all `1 / 1`
- Tab state/exact closed: `CLOSED / true`
- Retained tab binding: `false`
- Browser/session-name uncertainty: `false / false`

## Call 3

- Timestamp (Asia/Bangkok): `20260901 003546`
- `result=HANDOFF_OR_COMPARISON_UNCERTAIN_RETAINED_BINDING`
- `errorClass=NONE`
- Child start attempted/exit fulfilled: `1 / 1`
- Child exit code: `2`
- Stdout schema valid: `true`
- Handoff/comparison reads: `1 / 1`
- Comparison match: `FALSE`
- Observed shape/length: `FALSE / 0`
- Comparison error: `NONE`
- Final clear attempted/fulfilled: `1 / 1`
- Final empty-read attempted/fulfilled: `1 / 1`
- Final empty: `TRUE`
- Cleanup error: `NONE`
- PowerShell result: `FAIL`
- Challenge binding retained: `true`

## Disposition

- v7 gate: `CONSUMED`
- Retry/fallback/continuation: `0`
- Browser tab: `CLOSED PROVEN`
- Browser-session native clipboard write: `FULFILLED PROVEN`
- Windows clipboard observed challenge: `FALSE PROVEN`
- End-to-end bridge: `FAIL / NOT PROVEN`
- Final Windows clipboard empty: `PROVEN`
- Retained non-secret challenge binding: `PRESENT`
- Candidate verdict: `CONTRACT-ADHERENT FAIL`
- Credential/key/token/routing actions: `0`

The evidence demonstrates that the native browser-session clipboard write did
not populate the Windows clipboard visible to the child. No clipboard content
or challenge value was emitted. Old listener/process residuals remain untouched
and `NOT PROVEN`. Independent post-action classification is required.
