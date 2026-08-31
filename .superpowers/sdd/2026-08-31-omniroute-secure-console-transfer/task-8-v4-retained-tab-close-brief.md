# Task 8 v4 retained-tab direct-close brief

Status: static candidate. `authorizes_live_execution=false`.

This is a new cleanup-only one-shot contract, not a retry or continuation of
the consumed v4 clipboard preflight. It may dispose only the exact existing
`loopbackPreflightV4RetainedTab` binding. It authorizes no discovery,
reacquisition, alternate handle, or other live action.

## Pinned evidence

- v4 live report commit `7e37591a9f206ae4965fe2beb08636dd59644973`:
  `2947` bytes, SHA-256
  `A830D0E5981A9693D09C82590B9EE51FAE57E18DE7F888ACCB5D27D7951994DE`;
- independent classification commit
  `de62c60a9e1bbb3d6f31a73450a0d07c0ffce2b6`: `6280` bytes, SHA-256
  `668B08707F31C17A8EC5ECDA936837A29BAC2C2A6418132F695A095B5FF2B4EF`;
- installed `browser-client.mjs`: `149210` bytes, SHA-256
  `C52BA09202F0E82CAA6F6D2A6463A8635C1B1316567975D9B91C1A05FB5AF501`;
- installed `docs/api.json`: `58477` bytes, SHA-256
  `4BFEB97E958025DB37D52AEA11B75BC70BCA417B4995B0F711C0F07F3DDCCB08`;
- project-root `AGENTS.md`: `6051` bytes, SHA-256
  `AD0EA394F694C7795870C2B66D745EDC1FCA8997E7D7041A21E5659B0C349DDC`.

The installed API evidence declares
`Tab.close(): Promise<void>; // Close this tab.`

The pinned live evidence proves that the v4 listener close fulfilled and
`serverListening=false`; select-all, copy, and browser close were never
attempted; and the exact tab was retained in the non-null persistent binding.
The unrelated old v3 listener/server/process remains `NOT PROVEN` and outside
this contract.

## Authority and action-time preconditions

The sole owner may consume this fresh gate only after an independently pinned
Sol High direct-byte review returns exact PASS and action-time checks prove:

1. the brief, review, report, classification, installed API/module, and
   project-root standing-authority bytes and hashes match their pins;
2. the Git index is empty and the exact 12-path dirty source baseline is
   unchanged;
3. the same persistent Node session is selected; the cell itself performs the
   only strict non-null/callable retained-binding check, without a separate
   browser discovery or inspection call;
4. the fresh `loopbackPreflightV4RetainedTabCloseEligible` binding has never
   been declared; and
5. no earlier Task 8 invocation or uncertain Task 8 tool result exists.

Standing authority in project-root `AGENTS.md` permits sole-owner consumption
after independent PASS and action-time pin verification without another chat
approval. Missing or mismatched preconditions stop before the cell. Once the
cell is invoked, success, failure, rejection, timeout, malformed/missing
output, or tool uncertainty spends this gate permanently. There is no retry,
fallback, continuation, or replacement call under this authority.

## Exact one-cell direct close

Run this exact JavaScript cell once in the persistent session that owns the
retained binding. It consumes fresh eligibility before its only possible
browser call. It emits one bounded redacted object and no tab handle, ID,
title, URL, content, metadata, exception message, or stack.

```javascript
let loopbackPreflightV4RetainedTabCloseEligible = true;
await (async () => {
  const output = {
    result: "RETAINED_TAB_CLOSE_NOT_PROVEN",
    errorClass: "NONE",
    closeAttempted: 0,
    closeFulfilled: 0,
    retainedBindingPresent: false
  };
  const safeErrorClass = (error) => {
    const name = typeof error?.name === "string" ? error.name : "";
    return /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(name) ? name : "ERROR";
  };
  const consumedEligibility = loopbackPreflightV4RetainedTabCloseEligible === true;
  loopbackPreflightV4RetainedTabCloseEligible = false;
  const bindingDeclared = typeof loopbackPreflightV4RetainedTab !== "undefined";
  const bindingNonNull = bindingDeclared && loopbackPreflightV4RetainedTab !== null;
  output.retainedBindingPresent = bindingNonNull;
  try {
    if (!consumedEligibility || !bindingNonNull || typeof loopbackPreflightV4RetainedTab.close !== "function") {
      output.result = "RETAINED_TAB_BINDING_INVALID";
      return;
    }
    output.closeAttempted++;
    await loopbackPreflightV4RetainedTab.close();
    output.closeFulfilled++;
    loopbackPreflightV4RetainedTab = null;
    output.retainedBindingPresent = false;
    output.result = "EXACT_RETAINED_TAB_CLOSED";
  } catch (error) {
    output.errorClass = safeErrorClass(error);
    output.result = "RETAINED_TAB_CLOSE_NOT_PROVEN";
    output.retainedBindingPresent = bindingDeclared && loopbackPreflightV4RetainedTab !== null;
  } finally {
    nodeRepl.write(output);
  }
})();
```

## Exact result and fail-closed interpretation

PASS requires one terminal object with exactly:

```text
result=EXACT_RETAINED_TAB_CLOSED
errorClass=NONE
closeAttempted=1
closeFulfilled=1
retainedBindingPresent=false
```

Only fulfilled `close()` permits setting the retained binding to null. A
rejected or uncertain close retains the exact binding. Any missing, extra,
malformed, rejected, timed-out, or tool-transport-uncertain output is
`NOT PROVEN`; no closure or null binding may be inferred from an attempt.

The one cell contains exactly one directly awaited
`loopbackPreflightV4RetainedTab.close()` and one `nodeRepl.write`. It contains
zero `tabs.list`, `tabs.get`, `tabs.new`, discovery, reacquisition, navigation,
keyboard, clipboard, listener, server, process, child, retry, fallback,
credential, permission, deletion, provider, Cloudflare, VM, proxy, key, token,
OmniRoute, or routing actions. It never touches the proven-closed v4 listener
or the unrelated unproven old v3 listener/process.

## Static review and reporting boundary

Independent review must verify strict UTF-8/LF bytes, JavaScript syntax without
evaluation, exact close/write/eligibility/null-assignment cardinality and
ordering, prohibited-action absence, installed `Tab.close` API evidence, empty
index, exact 12-path baseline, and exact diff scope.

A later live report may record only pins, timestamps, the five redacted result
fields, gate consumption, and prohibited-action counters. It must not emit tab
or browser metadata and must set `authorizes_live_execution=false`. This brief
does not authorize live execution; independent PASS and action-time pins remain
mandatory.
