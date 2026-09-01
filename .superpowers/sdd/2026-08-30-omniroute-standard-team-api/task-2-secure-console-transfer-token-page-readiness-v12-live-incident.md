# V12 live incident: clean evaluator/validation-boundary failure

## Status

- Gate: `V12 visible structural diagnostic`
- Result: `PRECONDITION_FAIL`
- Consumption: consumed exactly once; never retry, continue, reinterpret, or reuse V12
- Residue: the exact V12-created tab was closed; no retained tab or owned process remained
- Provider impact: no provider action, form fill, click, clipboard read/write, secret read/write, or configuration mutation occurred

## Reviewed evidence chain

- V11 clean incident commit: `612aff1c272407983b6b0cadb01a79e8bb948ae4`
- V12 brief commit: `6062100e6d5893980419dd5edc377777806f7032`
- V12 brief: `23426` bytes, SHA-256 `C94D6AEC6680A704DABF9275242D9583ED191AC83955498B1E5F0F80140CE8B2`, blob `cc1a4aebeeaf352c0ed0fc69a2df25d4cb05dd28`
- V12 executable: `18502` bytes, SHA-256 `18C66B1B29B1A547EC381211669589FE8F9BBA2F3682C9F7F50F51BD0A877BA4`
- Independent Sol High PASS review commit: `fd6d8edf2af589b526376cc9eedf5c785446440e`
- V12 execution classification commit: `8bccec831e8cab02a7387bcb9df10e2c4e3ca768`
- Post-commit coordinator tuple: `39` exact exclusions; projection `10661` records, SHA-256 `C4C85893769D133224AC7404B628C8B0D4B0EBBFF471620B158E652E152B4EBD`; index `0`; exact dirty baseline `12`

## Action-time pins

Immediately before consumption, every documented local, runtime,
evidence-worktree, residue, VM1205, listener, network-membership, Caddy, DNS,
and persistent-Node predecessor pin passed. The exact dirty baseline remained
`12`, the index remained empty, and the projection remained `10661` records at
SHA-256 `C4C85893769D133224AC7404B628C8B0D4B0EBBFF471620B158E652E152B4EBD`
with `39` exact exclusions.

## Exact result

- Declaration and predecessor checks: passed
- Controller ownership, created-tab handle capture, and fixed navigation target: passed
- Navigation and URL reads: attempted `1`, fulfilled `1`
- Bounded visible wait: attempted `1`, fulfilled `1`
- Visible placeholder count: attempted `1`, fulfilled `1`, observed `1`
- Structural evaluator/validation: attempted `1`, fulfilled `0`
- All structural output fields: untouched sentinel values (`false` or `-1`)
- Cleanup: attempted `1`, fulfilled `1`, `CREATED_TAB_CLOSED`
- Failure-residue convergence: `true`
- Retained exact handle: `false`
- Error class: `Error`
- Persistent state: V12 consumed `true`; V12 retained tab `null`; V4 remained `null`, ineligible, and in state `V9_OWNED_TAB_READINESS_FAILED_CLEAN`

## Bounded interpretation

The visible selector is a valid uniqueness predicate in this observation: one
visible input was found after the bounded wait. The evaluator was invoked, but
the existing fulfillment counter is incremented only after both the page
evaluation and every controller validation step. Therefore the supported
failure boundary is only: page evaluation rejection or later shape/key/type,
range, tuple, or sentinel validation failure. This incident cannot distinguish
those cases and exposes no raw DOM or page value.

## Replacement boundary

A replacement may retain the same visible selector and unchanged page evaluator
while adding controller-local boolean/integer stage evidence only: whether the
evaluator returned and which exact shape/key/type/range/tuple/sentinel checks
passed. It must never emit untrusted values or keys. It must be a fresh one-shot
contract with new persistent variables, independent Sol High PASS review, a
non-self-referential classification, a post-commit coordinator tuple, fresh
action-time pins, exact-tab cleanup, and no retry path.
