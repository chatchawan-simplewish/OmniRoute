# Task 2 direct-preflight retained-tab disposition brief

Status: static candidate; **NOT AUTHORIZED** until an independent Sol High
direct-byte review passes and the user gives exact action-time approval to
close this one retained non-secret preflight tab.

## Fixed inputs

- Live report commit: `e7c597509ee4a06a9e368769636dc254cd2d4fc4`
- Independent classification commit:
  `cf5813b94f0ae281cbe73e134f5a7e79b8eee87b`
- Live result: `NOT_PROVEN_BROWSER_UNCERTAIN`
- Exact persistent Node REPL binding: `directPreflightV2RetainedTab`
- Recorded state: `OPEN_MUTATION_UNCERTAIN`
- Fulfilled browser counters: `open/goto/focus/selectAll/copy/close =
  1/0/0/0/0/0`

The binding was assigned from the fulfilled `chrome.tabs.new()` result before
the rejected `goto`. It has not been queried, reacquired, closed, or otherwise
used since the one-shot attempt stopped.

## Authority boundary

This is a new, separately authorized disposition action, not a retry of the
preflight. It permits exactly one `close()` call on the retained binding and
one explicit result emission. It permits no tab discovery, `tabs.get`, list,
snapshot, screenshot, URL/title/content extraction, navigation, reload,
coordinate action, keyboard action, clipboard action, retry, fallback,
credential, token, Cloudflare, OmniRoute, VM1205, proxy/proof/R5, Rulesets,
permission, deletion, evidence-worktree, revocation, or other live-resource
action.

## Exact one-call disposition

Run this exact cell once in the existing persistent Node REPL only after the
required review PASS and exact user approval. It reassigns the already-declared
retained binding and declares no replacement tab handle.

```javascript
await (async () => {
  let directPreflightV2DispositionResult = "CLOSE_UNCERTAIN";
  let directPreflightV2DispositionErrorClass = "NONE";
  let directPreflightV2DispositionCloseCalls = 0;
  let directPreflightV2DispositionCloseFulfilled = 0;
  if (directPreflightV2RetainedTab === null) {
    directPreflightV2DispositionResult = "PRECONDITION_BINDING_NULL";
  } else {
    directPreflightV2DispositionCloseCalls++;
    try {
      await directPreflightV2RetainedTab.close();
      directPreflightV2DispositionCloseFulfilled++;
      directPreflightV2RetainedTab = null;
      directPreflightV2DispositionResult = "EXACT_RETAINED_TAB_CLOSED";
    } catch (directPreflightV2DispositionError) {
      directPreflightV2DispositionErrorClass = typeof directPreflightV2DispositionError?.name === "string" ? directPreflightV2DispositionError.name : "ERROR";
      directPreflightV2DispositionResult = "CLOSE_UNCERTAIN";
    }
  }
  nodeRepl.write({
    result: directPreflightV2DispositionResult,
    errorClass: directPreflightV2DispositionErrorClass,
    closeCalls: directPreflightV2DispositionCloseCalls,
    closeFulfilled: directPreflightV2DispositionCloseFulfilled,
    retainedBindingNull: directPreflightV2RetainedTab === null
  });
})();
```

## Verdict

Disposition PASS requires exactly:

- `result=EXACT_RETAINED_TAB_CLOSED`;
- `errorClass=NONE`;
- `closeCalls=1`, `closeFulfilled=1`;
- `retainedBindingNull=true`.

`PRECONDITION_BINDING_NULL`, any tool-transport uncertainty, any rejected
`close`, missing/malformed output, or any counter mismatch is `NOT PROVEN`.
There is no second close, reacquisition, lookup, fallback, or retry. The result
authorizes no replacement preflight or later live action and is recorded with
`authorizes_live_execution=false`.
