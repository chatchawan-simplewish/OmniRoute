# OmniRoute loopback clipboard preflight v5 live report

`authorizes_live_execution=false`

## Pins

- Brief commit: `f31cbc18b10d132e14909b09acb4047a18248fff`
- Brief bytes: `26264`
- Brief SHA-256: `C5C6C9A699253AB1D3C2D5D50C0E68D1B3F03C09A5865B82DE3B6021F42E9476`
- Independent review commit: `a3de832381cece4d5ecf6f5e3579d9458eaa5830`
- Review bytes: `9969`
- Review SHA-256: `DE3D0B4BB742381B565DD1E90BB00F1448CCA8E31225891D3B920CEBBD212C77`
- Action-time validation: committed brief/review bytes matched; review was `PASS` with zero findings; standing unattended authority was present; Git index was empty; exact 12-path dirty source baseline was preserved.

## Call 1

- Timestamp (Asia/Bangkok): `20260831 224550`
- Exit: `0`
- `PREFLIGHT_V5_BASELINE_CLEAR_ATTEMPTED=1`
- `PREFLIGHT_V5_BASELINE_CLEAR_FULFILLED=1`
- `PREFLIGHT_V5_BASELINE_READ_ATTEMPTED=1`
- `PREFLIGHT_V5_BASELINE_READ_FULFILLED=1`
- `PREFLIGHT_V5_BASELINE_EMPTY=TRUE`
- `PREFLIGHT_V5_BASELINE_ERROR=NONE`

## Call 2

- Timestamp (Asia/Bangkok): `20260831 224819`
- Invocation count: `1`
- Reviewed control timeout: `120000` milliseconds
- Tool outcome: `TIMED_OUT_KERNEL_RESET`
- Terminal redacted result object received: `0`
- Call 2 result: `NOT PROVEN`

Because Call 2 timed out and reset the JavaScript kernel, no browser, request,
server-close, listener, exact-tab, copy, or binding outcome is inferred.

## Call 3 and disposition

- Call 3 invocation count: `0`
- Child process invocation count: `0`
- Final clipboard clear/read count: `0`
- Final clipboard state: `NOT PROVEN`
- Retry/fallback/continuation/replacement call count: `0`
- Credential/key/token/routing action count: `0`
- v5 gate: `CONSUMED`
- Overall candidate verdict: `FAIL / NOT PROVEN`

The old v3 listener/server/process remains unrelated and `NOT PROVEN`.
Independent post-action classification is required.
