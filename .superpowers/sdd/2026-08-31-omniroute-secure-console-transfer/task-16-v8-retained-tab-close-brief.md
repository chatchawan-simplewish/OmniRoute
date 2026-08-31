# Task 16 v8 retained-tab direct-close brief

Status: fresh static cleanup candidate. `authorizes_live_execution=false`.

This is a new cleanup-only one-shot contract, not a retry or continuation of
the consumed v8 keyboard clipboard preflight. It may dispose only the exact
existing `keyboardClipboardPreflightV8RetainedTab` binding. It authorizes no
discovery, reacquisition, alternate handle, navigation continuation, clipboard
action, or transport verdict change.

## Pinned evidence and future report

- current base / Task 15 classification commit:
  `1b25304d3cdc38e24bf0f542f98207eebde5ab30`;
- Task 15 live report commit
  `4a6d4c08a8ad8c77c7fcbe1ccf17f481b259c290`: `2095` bytes,
  SHA-256
  `0D5B822B05DB73AE7C62A588AC1D4C44C5E7047AFE6858587649BEB753BC975E`;
- Task 15 independent classification: `5312` bytes, SHA-256
  `9EE8DAEA43FDDF2ADF51ED624912408CF754CC1E5C9410E0E3A75AD3C4C74833`;
- successful Task 8 direct-binding pattern commit
  `7cbb93be68786c20c48f92650bacf8baf9f39585`;
- installed browser API: `58477` bytes / SHA-256
  `4BFEB97E958025DB37D52AEA11B75BC70BCA417B4995B0F711C0F07F3DDCCB08`;
- installed browser module: `149210` bytes / SHA-256
  `C52BA09202F0E82CAA6F6D2A6463A8635C1B1316567975D9B91C1A05FB5AF501`;
- project-root `AGENTS.md`: `6051` bytes / SHA-256
  `AD0EA394F694C7795870C2B66D745EDC1FCA8997E7D7041A21E5659B0C349DDC`.

The installed API evidence must continue to declare exactly
`close(): Promise<void>; // Close this tab.`

The pinned Task 15 evidence proves tab creation fulfilled, navigation remained
uncertain, and the exact tab was retained in the non-null persistent
`keyboardClipboardPreflightV8RetainedTab` binding. Locator, click, selection,
copy, tab close, Call 3, and child were never attempted. The challenge remained
lexical and was never published to the persistent expected-challenge binding.
Windows clipboard empty is proven at the Task 15 report boundary. This cleanup
does not inspect or refresh either clipboard or challenge state.

A future result must be written only to
`.superpowers/sdd/2026-08-31-omniroute-secure-console-transfer/task-16-v8-retained-tab-close-live-report.md`
and independently classified. It may record only pins, timestamp, gate
consumption, the redacted terminal fields below, and prohibited-action counts.
It must set `authorizes_live_execution=false`.

## Authority and action-time preconditions

Standing unattended authority may permit the sole Sol High owner to consume
this fresh cleanup gate only after independent direct-byte PASS and action-time
checks prove the exact brief/review/report/classification/API/module/authority
pins, empty Git index, unchanged exact 12-path dirty source baseline, the same
persistent Node session, zero intervening tab or binding action, and the fresh
`keyboardClipboardPreflightV8RetainedTabCloseEligible` binding never declared.

The cell itself performs the only binding declaration/non-null/callable check.
No separate browser inspection or discovery call is permitted. Missing or
mismatched action-time preconditions stop before the cell. Once invoked,
success, failure, rejection, timeout, missing/malformed output, or tool
uncertainty spends this gate permanently. There is no retry, fallback,
continuation, replacement call, or later cleanup under this authority.

## Exact one-cell direct close

Run this exact JavaScript cell once in the persistent session that owns the v8
retained binding. It consumes fresh eligibility before any binding check. It
then validates only that the exact binding is declared, non-null, and exposes a
callable `close`. Only that exact branch directly awaits one `Tab.close`; only
fulfilled close permits nulling the binding.

```javascript
let keyboardClipboardPreflightV8RetainedTabCloseEligible = true;
await (async () => {
  const output = {
    result: "RETAINED_TAB_CLOSE_NOT_PROVEN",
    errorClass: "NONE",
    cleanupEligibilityConsumed: false,
    bindingCheckAttempted: 0,
    bindingCheckFulfilled: 0,
    bindingDeclared: false,
    bindingInitiallyNonNull: false,
    closeCallable: false,
    closeAttempted: 0,
    closeFulfilled: 0,
    retainedBindingPresent: false
  };
  const safeErrorClass = (error) => {
    const name = typeof error?.name === "string" ? error.name : "";
    return /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(name) ? name : "ERROR";
  };
  const consumedEligibility = keyboardClipboardPreflightV8RetainedTabCloseEligible === true;
  keyboardClipboardPreflightV8RetainedTabCloseEligible = false;
  output.cleanupEligibilityConsumed = consumedEligibility;
  output.bindingCheckAttempted++;
  output.bindingDeclared = typeof keyboardClipboardPreflightV8RetainedTab !== "undefined";
  output.bindingInitiallyNonNull = output.bindingDeclared && keyboardClipboardPreflightV8RetainedTab !== null;
  output.closeCallable = output.bindingInitiallyNonNull && typeof keyboardClipboardPreflightV8RetainedTab.close === "function";
  output.retainedBindingPresent = output.bindingInitiallyNonNull;
  output.bindingCheckFulfilled++;
  try {
    if (!consumedEligibility || !output.bindingDeclared || !output.bindingInitiallyNonNull || !output.closeCallable || output.bindingCheckAttempted !== 1 || output.bindingCheckFulfilled !== 1) {
      output.result = "RETAINED_TAB_BINDING_INVALID";
      return;
    }
    output.closeAttempted++;
    await keyboardClipboardPreflightV8RetainedTab.close();
    output.closeFulfilled++;
    keyboardClipboardPreflightV8RetainedTab = null;
    output.retainedBindingPresent = false;
    output.result = "EXACT_RETAINED_TAB_CLOSED";
  } catch (error) {
    output.errorClass = safeErrorClass(error);
    output.result = "RETAINED_TAB_CLOSE_NOT_PROVEN";
    output.retainedBindingPresent = output.bindingDeclared && keyboardClipboardPreflightV8RetainedTab !== null;
  } finally {
    nodeRepl.write(output);
  }
})();
```

Exact PASS requires one terminal object with result
`EXACT_RETAINED_TAB_CLOSED`, error `NONE`, cleanup eligibility consumed true,
binding check `1 / 1`, declared/non-null/callable true, close `1 / 1`, and
retained binding present false.

Only fulfilled `close()` permits setting the exact retained binding to null. A
precondition mismatch performs no close and no binding assignment. A rejected
or uncertain close retains the exact binding. Any missing, extra, malformed,
rejected, timed-out, or tool-transport-uncertain output is FAIL / `NOT PROVEN`;
no closure or null binding may be inferred from an attempt, and no second call
is permitted.

## Prohibited action, redaction, and static boundary

The executable cell contains exactly one directly awaited
`keyboardClipboardPreflightV8RetainedTab.close()`, one success-only
`keyboardClipboardPreflightV8RetainedTab = null`, one consumed eligibility
transition before checks, and one redacted `nodeRepl.write`.

It contains zero `tabs.list`, `tabs.get`, `tabs.new`, discovery, reacquisition,
navigation, URL/content/metadata inspection, keyboard, clipboard, child,
server, listener, process, retry, fallback, credential, permission, deletion,
provider, Cloudflare, VM, proxy, key, token, OmniRoute, or routing action. It
emits no tab handle, ID, title, URL, content, metadata, challenge, clipboard
value, exception message, stack, credential, key, token, or routing data. Old
listener/process residuals remain untouched and `NOT PROVEN`.

Independent review must verify strict UTF-8/LF bytes, non-evaluating JavaScript
syntax, exact eligibility/check/close/null/write cardinality and ordering,
redaction, prohibited-action absence, installed `Tab.close` API evidence,
empty index, exact 12-path baseline, and exact diff scope. This brief
authorizes no live execution; independent PASS and action-time pins remain
mandatory.
