# V10 live incident: clean precondition failure

## Status

- Gate: `V10 structural diagnostic`
- Result: `PRECONDITION_FAIL`
- Consumption: consumed exactly once; never retry, continue, reinterpret, or reuse V10
- Residue: the exact V10-created tab was closed; no retained tab or owned process remained
- Provider impact: no provider action, form fill, click, clipboard read/write, secret read/write, or configuration mutation occurred

## Reviewed evidence chain

- Original brief commit: `39dcae3a99728680dd473d58d097c83212b34ad1`
- Initial Sol High FAIL review commit: `36ffea1d17f42e0b2ef4d050bca60763b071c3f7`
- Fix commit: `8cf9eac8e03dfd83d52bb4be3fb63f5dc6341f5d`
- Fix executable: `17840` bytes, SHA-256 `502EC63F8B1871830C82992BCC3836D9B2EBBA83D849BEAF0271EF6171C4309F`
- Fix brief: `22351` bytes, SHA-256 `2274EFB9CFA7303C77598D889FA14B4E35201EE89700DC1BD1F4127227165F2C`, blob `94c551ade3b2aa99d138d3962ce5ffa2fbecb3a7`
- Sol High PASS review commit: `4fb6f95e9d29573828558162c99ef50e460e1ca4`
- Execution classification commit: `fb9beccbcdea25e490639f8f98bcc416c3a896a1`
- Post-commit coordinator tuple: `31` exact exclusions; projected retained diff `10661` bytes, SHA-256 `C4C85893769D133224AC7404B628C8B0D4B0EBBFF471620B158E652E152B4EBD`; index `0`; exact dirty baseline `12`

## Action-time pins

Immediately before consumption, every documented local, runtime, evidence-worktree, residue, VM1205, listener, network-membership, Caddy, DNS, and persistent-Node predecessor pin passed. The exact dirty baseline remained `12`, the index remained empty, the projected retained diff remained `10661` bytes with SHA-256 `C4C85893769D133224AC7404B628C8B0D4B0EBBFF471620B158E652E152B4EBD`, and no temp or owner-process residue existed.

## Exact result

- Declaration and predecessor checks: passed
- Controller ownership, created-tab handle capture, and fixed navigation target: passed
- Navigation: attempted `1`, fulfilled `1`
- Placeholder lookup count: attempted `1`, fulfilled `1`, observed `0`
- Structural evaluator: attempted `0`, fulfilled `0`
- All structural output fields: untouched sentinel values (`false` or `-1`)
- Cleanup: attempted `1`, fulfilled `1`, `CREATED_TAB_CLOSED`
- Failure-residue convergence: `true`
- Retained exact handle: `false`
- Error class: `Error`
- Persistent state: V10 consumed `true`; V10 retained tab `null`; V4 remained `null`, ineligible, and in state `V9_OWNED_TAB_READINESS_FAILED_CLEAN`

## Bounded interpretation

The fixed navigation completed, but the exact placeholder locator count was `0` when checked immediately afterward. Because the evaluator never ran, this incident does not establish the page structure, authentication state, or Create-control shape. Compared with V8 and V9, which observed the same placeholder once, the narrow supported inference is a page-local readiness race. No broader conclusion is authorized.

## Replacement boundary

A replacement may add one bounded visibility wait for the same placeholder before counting it, then run the unchanged read-only structural diagnostic and exact-tab cleanup. It must be a fresh one-shot contract with new persistent variable names, independent Sol High PASS review, a non-self-referential classification, a post-commit coordinator tuple, fresh action-time pins, and no retry path.
