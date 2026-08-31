# OmniRoute keyboard clipboard preflight v8 live report

`authorizes_live_execution=false`

## Pins

- Brief commit: `bb37efde0705001e892344fe7c6437a4c66f9a14`
- Brief bytes: `23152`
- Brief SHA-256: `075DE9C7BFCE48088D1E75C401CCBB455EBBA9786889044A19E6D9C749637508`
- Independent review commit: `bb5b43127a500183aebcf0f0bd3b796a96acba66`
- Review bytes: `7768`
- Review SHA-256: `357E0D8EE6390B73B7E67740AB5C6C4E196D33669479AEFBC38302A941172BC9`
- Action-time validation: committed brief/review and bundled PowerShell pins matched; review was `PASS`; standing unattended authority was present; Git index was empty; exact 12-path dirty source baseline was preserved.

## Call 1

- Timestamp (Asia/Bangkok): `20260901 011943`
- Baseline clear attempted/fulfilled: `1 / 1`
- Baseline empty-read attempted/fulfilled: `1 / 1`
- Baseline empty: `TRUE`
- Error: `NONE`

## Call 2

- Timestamp (Asia/Bangkok): `20260901 011951`
- `result=BROWSER_UNCERTAIN`
- `errorClass=Error`
- Challenge shape/length: `true / 50`
- Session-name attempted/fulfilled: `1 / 1`
- Browser-open attempted/fulfilled: `1 / 1`
- Data-URL navigation attempted/fulfilled: `1 / 0`
- Locator, click, select, copy attempted/fulfilled: all `0 / 0`
- Browser-close attempted/fulfilled: `0 / 0`
- Tab state: `NAVIGATION_UNCERTAIN`
- Exact tab closed: `false`
- Retained exact tab binding: `true`
- Browser call unsettled/uncertain: `true / true`
- Session-name uncertainty: `false`

## Call 3 and disposition

- Call 3 invocation count: `0`
- Child process invocation count: `0`
- v8 gate: `CONSUMED`
- Retry/fallback/continuation: `0`
- Copy action attempted: `0`
- Windows clipboard baseline empty: `PROVEN`
- Browser tab disposition: `NOT PROVEN / RETAINED EXACT BINDING`
- End-to-end bridge: `NOT PROVEN`
- Candidate verdict: `CONTRACT-ADHERENT FAIL / NOT PROVEN`
- Credential/key/token/routing actions: `0`

No URL, challenge, tab metadata, or clipboard content was emitted. No
server/listener action existed. Old listener/process residuals remain untouched
and `NOT PROVEN`. Independent post-action classification is required.
