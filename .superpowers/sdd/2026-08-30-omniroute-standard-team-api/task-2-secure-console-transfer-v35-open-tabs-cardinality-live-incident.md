# OmniRoute V35 open-tabs cardinality — live incident

Date: `2026-09-02` (`Asia/Bangkok`)

## Terminal classification

V35 Call 1 is **consumed / PASS**. V35 Call 2 is **consumed / failed
cleanly**. V35 is permanently ineligible. Never retry, continue, reinterpret,
or reuse either V35 cell.

The failure occurred at the reviewed exact-one private candidate gate after the
single permitted `openTabs()` call. The runtime returned eight shape-valid
top-level tab records. The cell therefore stopped before any `claimTab()`,
navigation, wait, URL read, or page evaluation.

## Immutable package and action-time state

- Corrected brief commit:
  `3504b9e87eacd1c8de6801df7256bd502ce7d37f`
- Independent PASS review commit:
  `41d220ccdd66cb403868e4be06144b681a6589fa`
- Execution-classification commit:
  `394f3aa0bb7efcda2329a4ad3cc658f2f1c6494f`
- Call-1 bytes/SHA-256:
  `5456` / `4F6F4A3F35D6BBCC3EFC5CA6A4B335788D14F38191C88B0D51D63539DA11A2F4`
- Call-2 bytes/SHA-256:
  `9904` / `6A387C46AA9A226649BA705F503037DCA0813678DDAEAD860060964069C0116F`
- Post-classification tuple before execution: HEAD
  `394f3aa0bb7efcda2329a4ad3cc658f2f1c6494f`, parent
  `41d220ccdd66cb403868e4be06144b681a6589fa`, one classification path,
  chain paths `134`, exclusions `136`, projection records `10661`, projection
  SHA-256
  `C4C85893769D133224AC7404B628C8B0D4B0EBBFF471620B158E652E152B4EBD`,
  empty index, exact 12-path dirty baseline.
- Runtime module and API-documentation pins matched.
- Evidence worktree was clean at
  `80adaa7d5d63d1d2c7bfa63b236c6bee93b3b1d8`.
- Windows temporary/process residue was zero.
- VM1205 matched the complete safe checkpoint.
- Public A/CNAME counts were zero through `1.1.1.1` and `8.8.8.8`.
- The owner's exact Chrome profile/window/task-tab selection confirmation was
  present and unchanged.

## Sanitized fixed-schema evidence

Call 1 returned exact result `EXACT_V35_FRESH_CHROME_ATTACHMENT_PASS` with
declaration, module, agent, connection, and documentation validation true;
documentation length `42596`; every import/setup/connect/documentation/write
attempt and fulfillment count `1`; consumed and attachmentExact true; state
`V35_ATTACHMENT_PASS`; error class `NONE`.

Call 2 returned:

```text
result=PRECONDITION_FAIL
declarationShape=true
predecessorExact=true
candidateCount=8
candidateValidated=false
controllerOwnership=false
tabShape=false
homeUrlValidated=false
snapshotValidated=false
semanticComplete=false
snapshot=null
openTabsAttempted=1
openTabsFulfilled=1
claimAttempted=0
claimFulfilled=0
navigationAttempted=0
navigationFulfilled=0
waitAttempted=0
waitFulfilled=0
urlAttempted=0
urlFulfilled=0
snapshotAttempted=0
snapshotFulfilled=0
writeAttempted=1
errorClass=Error
consumed=true
bindingEligible=false
bindingNull=true
bindingState=V35_REACQUISITION_OR_READINESS_FAILED
```

No tab ID, provider-tab ID, title, URL, group, account ID, zone ID, href,
secret, credential, token, or raw exception was emitted.

## Root cause and boundary

The reviewed V35 candidate projector treated every current, shape-valid
`BrowserUserTabInfo` record as a candidate and required the total to equal one.
The owner's confirmation restricted the offered Chrome profile and window; it
did not assert that the window contained only one open tab. Eight valid records
therefore caused the intended fail-closed cardinality stop. This is a contract
selection defect, not evidence of a provider or controller mutation.

The terminal cleanup predicate proved adoption consumed, retained tab null,
eligibility false, failure state exact, and setup/agent/browser bindings null.
The Node realm was then reset. No tab was claimed, created, closed, or
navigated; no provider-persistent change was made.

A replacement must be newly specified and independently reviewed. It must
preserve fresh-session attachment, exactly one `openTabs()` and one
`claimTab()`, private exact-record validation, no metadata emission, no retry,
the same account-home semantic signature, terminal cleanup, and all existing
secret and mandatory-confirmation boundaries. It must identify the externally
selected intended tab from the documented ordered listing without assuming
that the browser window contains only one tab.
