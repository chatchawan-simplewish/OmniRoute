# V14 live incident: cross-realm plain-record prototype boundary

## Status

- Gate: `V14 null-prototype structural diagnostic`
- Result: `PRECONDITION_FAIL`
- Consumption: consumed exactly once; never retry, continue, reinterpret, or reuse V14
- Residue: exact V14-created tab closed; no retained tab or owned process remained
- Provider impact: no provider action, form fill, click, clipboard read/write, secret read/write, or configuration mutation occurred

## Reviewed chain and action-time state

- V13 incident commit: `e95bdc321432588dc23b73866ae006f7fe23746b`
- V14 brief commit: `a56432d640b906eaa844d5a04721d79d4bb67d9e`
- V14 brief: `26365` bytes, SHA-256 `A25B6F3481AF32516F1E46960D03FE27C3822A3C547258DE380FFFDD892A4E10`, blob `572f1d3b2979815706351e1d1d502d27e918ab05`
- V14 executable: `20682` bytes, SHA-256 `6EAE11B3ACFF75C73B167B50EE3E48B861BAC5F2CCADDA5FC7FEC7C031987EF6`
- Independent Sol High PASS review commit: `3bab0827f9523cab7573dd0ace1f4c9fa17d5a8c`
- V14 classification commit: `46376b94e60c67f09bca38fa3921f8f4f61ec652`
- Coordinator tuple: `47` exact exclusions; projection `10661` records at SHA-256 `C4C85893769D133224AC7404B628C8B0D4B0EBBFF471620B158E652E152B4EBD`; index `0`; exact dirty baseline `12`

Every documented local, runtime, evidence-worktree, residue, VM1205, listener,
network-membership, Caddy, DNS, and persistent-Node predecessor pin passed
immediately before consumption.

## Exact result

- Declaration, predecessor, controller, handle, navigation, wait, and unique-visible-input checks: passed
- Evaluator returned: `true`
- Non-null object and exact 60 keys: `true`
- All boolean/integer type, range, tuple, and sentinel checks: `true`
- Local `Object.prototype` identity: `false`
- Null prototype identity: `false`
- Aggregate two-prototype predicate: `false`
- Diagnostic attempted/fulfilled: `1 / 0`
- Cleanup attempted/fulfilled: `1 / 1`, `CREATED_TAB_CLOSED`
- Failure residue converged: `true`; retained exact handle: `false`
- V14 consumed: `true`; V14 retained tab: `null`; V4 remained null, ineligible, and in state `V9_OWNED_TAB_READINESS_FAILED_CLEAN`

## Pinned bridge evidence

The pinned installed bridge
`scripts/browser-client.mjs` remains `149210` bytes at SHA-256
`C52BA09202F0E82CAA6F6D2A6463A8635C1B1316567975D9B91C1A05FB5AF501`.
Its exported `isPlainObject` implementation is an exact `135`-byte fragment at
SHA-256 `CE3E29DA20DBE7CEA1C14DB761B4CB45AC14328DB37722E98BF013669ADBC295`.
It accepts a non-null object when its direct prototype is null or when that
prototype's prototype is null. This is the bridge's explicit cross-realm plain-
object rule; it does not rely on identity with the controller realm's
`Object.prototype`.

## Replacement boundary

A replacement may use exactly the pinned bridge plain-object predicate:
non-null object and either direct prototype null or direct prototype's prototype
null. It may add only a safe parent-prototype-null boolean. The page evaluator,
exact 60 keys, every type/range/tuple/sentinel check, safe output, visible
selector, bounded wait, exact-tab cleanup, and no-mutation boundary remain
unchanged. It must be a fresh one-shot contract with independent Sol High PASS
review, non-self-referential classification, post-commit tuple, fresh pins, and
no retry path.
