# OmniRoute native clipboard bridge preflight v6 live report

`authorizes_live_execution=false`

## Pins

- Corrected brief commit: `3c6cb31586f1b1a541cf3791be339af364826f80`
- Brief bytes: `18717`
- Brief SHA-256: `3D5670C7E5E5C3D58205D168311E4732A605325CF9A082C1AD84EEE862B1CFFB`
- Independent PASS review commit: `22dbc548dc05eca20f81e256988867120cd69f2b`
- Review bytes: `4983`
- Review SHA-256: `4F21EC9FA6CB25B2E2685D20E38F2078877ECB5199B94D229D0EA2A189EDF868`
- Action-time validation: committed brief/review bytes matched; review was `PASS`; standing unattended authority was present; Git index was empty; exact 12-path dirty source baseline was preserved.

## Call 1

- Timestamp (Asia/Bangkok): `20260831 234416`
- Exit: `0`
- Baseline clear attempted/fulfilled: `1 / 1`
- Baseline empty-read attempted/fulfilled: `1 / 1`
- Baseline empty: `TRUE`
- Error: `NONE`

## Call 2

- Timestamp (Asia/Bangkok): `20260831 234427`
- `result=NATIVE_WRITE_SETTLED_TAB_CLOSED`
- `errorClass=NONE`
- Challenge shape/length: `true / 50`
- Session-name attempted/fulfilled: `1 / 1`
- Browser-open attempted/fulfilled: `1 / 1`
- Native clipboard-write attempted/fulfilled: `1 / 1`
- Browser-close attempted/fulfilled: `1 / 1`
- Tab state/exact closed: `CLOSED / true`
- Retained tab binding: `false`
- Browser/session-name uncertainty: `false / false`

## Call 3

- Timestamp (Asia/Bangkok): `20260831 234438`
- `result=HANDOFF_OR_COMPARISON_UNCERTAIN_RETAINED_BINDING`
- `errorClass=ENOENT`
- Child-start attempted: `1`
- Child-exit fulfilled: `0`
- Child exit code: `null`
- Stdout schema valid: `false`
- Comparison: `null`
- Challenge binding retained: `true`
- Final clipboard clear/read: `0 / 0`
- Final clipboard state: `NOT PROVEN`

## Disposition

- v6 gate: `CONSUMED`
- Retry/fallback/continuation: `0`
- Browser tab: `CLOSED PROVEN`
- Native clipboard write: `FULFILLED PROVEN`
- End-to-end comparison: `NOT PROVEN`
- Final clipboard empty: `NOT PROVEN`
- Candidate verdict: `CONTRACT-ADHERENT FAIL / NOT PROVEN`
- Credential/key/token/routing actions: `0`

The retained challenge is non-secret and was not emitted. The old v3/v5
listener/process residuals remain untouched and `NOT PROVEN`. Independent
post-action classification is required.
