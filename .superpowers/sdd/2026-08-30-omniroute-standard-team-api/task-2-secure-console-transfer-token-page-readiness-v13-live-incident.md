# V13 live incident: isolated prototype-identity validation failure

## Status

- Gate: `V13 validation-stage diagnostic`
- Result: `PRECONDITION_FAIL`
- Consumption: consumed exactly once; never retry, continue, reinterpret, or reuse V13
- Residue: the exact V13-created tab was closed; no retained tab or owned process remained
- Provider impact: no provider action, form fill, click, clipboard read/write, secret read/write, or configuration mutation occurred

## Reviewed evidence chain

- V12 clean incident commit: `5b56ce93f6439d4b2cbc7d232fe07d76e230d4a6`
- V13 brief commit: `777b6e34e0efa82ba6497b45b26fecf6baf602d2`
- V13 brief: `25451` bytes, SHA-256 `8D0E8E6CB0129D2D6D1D5B4D0AB772E6D4C67F0DA81D0B5C57A1109432845679`, blob `827d849bc8b6c41ce55f4037faf3fb98e73f8e40`
- V13 executable: `20104` bytes, SHA-256 `FCB3EFCC7E066237EEBBD6D1A0688D086E4E7273868CAA94DD211012E21946D7`
- Independent Sol High PASS review commit: `6cf01b2d4cf605cddb5e8d2f651d1a188925c904`
- V13 execution classification commit: `7f5dda47df8b6094ec053ef02f59f5152bf6fdf5`
- Post-commit coordinator tuple: `43` exact exclusions; projection `10661` records, SHA-256 `C4C85893769D133224AC7404B628C8B0D4B0EBBFF471620B158E652E152B4EBD`; index `0`; exact dirty baseline `12`

## Action-time pins

Immediately before consumption, every documented local, runtime,
evidence-worktree, residue, VM1205, listener, network-membership, Caddy, DNS,
and persistent-Node predecessor pin passed. The projection remained `10661`
records at SHA-256
`C4C85893769D133224AC7404B628C8B0D4B0EBBFF471620B158E652E152B4EBD`
with `43` exact exclusions, empty index, and the exact 12-path dirty baseline.

## Exact result

- Declaration and predecessor checks: passed
- Controller ownership, created-tab handle capture, and fixed navigation target: passed
- Navigation, URL, bounded visible wait, and visible count: each attempted `1`, fulfilled `1`
- Visible placeholder count: `1`
- Page evaluator returned: `true`
- Result object non-null: `true`
- Result key count: `60`
- Exact keys: `true`
- Boolean types: `true`
- Integer types: `true`
- Integer ranges: `true`
- Found tuples: `true`
- Missing tuples: `true`
- Count sentinels: `true`
- Exact `Object.prototype` identity: `false`
- Diagnostic fulfillment: attempted `1`, fulfilled `0`
- Structural projection: untouched sentinel values because strict acceptance failed before copying
- Cleanup: attempted `1`, fulfilled `1`, `CREATED_TAB_CLOSED`
- Failure-residue convergence: `true`
- Retained exact handle: `false`
- Persistent state: V13 consumed `true`; V13 retained tab `null`; V4 remained `null`, ineligible, and in state `V9_OWNED_TAB_READINESS_FAILED_CLEAN`

## Bounded interpretation

The evaluator returned a complete, exact-keyed, correctly typed, in-range, and
internally consistent 60-field result. The sole failed validation predicate was
strict identity with the local realm's `Object.prototype`. This does not prove
the actual alternate prototype. A null prototype is a plausible safe bridge
serialization shape, but must be tested explicitly rather than inferred.

## Replacement boundary

A replacement may add one explicit `Object.getPrototypeOf(result) === null`
boolean and define plain-record acceptance as exact local `Object.prototype` or
exact `null` only. Every key/type/range/tuple/sentinel check, the unchanged page
evaluator, safe output boundary, visible selector, bounded wait, and exact-tab
cleanup remain mandatory. The replacement must be a fresh one-shot contract
with independent Sol High PASS review, non-self-referential classification,
post-commit tuple, fresh action-time pins, and no retry path.
