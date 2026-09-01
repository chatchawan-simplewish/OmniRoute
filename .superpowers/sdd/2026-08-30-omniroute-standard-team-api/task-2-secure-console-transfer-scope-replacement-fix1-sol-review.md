# Task 2 secure-console scope replacement fix 1 — Sol High review

Review date: 2026-09-01 (Asia/Bangkok)  
Review mode: independent Sol High, direct-byte/static only  
Reviewed fix commit: `5e940aa91c905ce432736596ae3aa9f572f6e3eb`  
Prior FAIL review: `d77851c13ee8a0f2f54a214a9175aad1f4ee9285`

## Verdict

**FAIL / NOT PROVEN — two HIGH findings.**

Fix 1 materially improves both areas. The new `tabs.get` adoption cell is syntactically valid, uses the exact retained Chrome controller, and proves the returned tab's ID plus fixed title/marker without metadata emission. The prose failure matrix also states the correct monotonic retained-handle principles.

The contract is not yet executable. The browser subgate has no fixed outer deadline, predicts rather than records its write-fulfilled counter, leaves failure-path binding disposition incomplete, and grants a later uncounted `markHandoff` that is not inherited from the pinned live brief. Separately, the owner cleanup matrix is not wired into any exact executable fence: the two unchanged PowerShell wrappers contain none of its counters, try/catch routing, waits, termination, exit proof, or residual terminals. An owner can start before uncertainty while the contract supplies only prose for the load-bearing cleanup sequence.

No execution, browser action, process action, cleanup, credential action, Cloudflare action, VM action, or routing mutation is authorized by this review.

## Integrity and parser evidence

- Fix brief: `16317` bytes, SHA-256 `945414DE520843E1E7B95F172CCDD7736D7A41E537DB6F2590692F25D395CBEC`.
- `HEAD` is the pinned fix commit; its parent is the prior FAIL review commit.
- The fix commit changes exactly the existing scope-replacement brief.
- Git index is empty; unrelated dirty baseline remains exactly `12`.
- The brief is UTF-8 without BOM, LF-only, and ends with the expected trailing LF.
- Exactly one JavaScript fence was parsed without evaluation using Node module syntax checking: `3087` bytes, SHA-256 `2BEAE5B5F25A699ECFAE07660F6297FCE217F91F7BEF3429132EA28E6B7B3EF1`, exit `0`, empty stdout/stderr.
- Both PowerShell fences were parsed without evaluation by the PowerShell language parser with zero errors:
  - preparation wrapper: `2017` bytes, SHA-256 `D438EFF617AA6983419D610A67FAC3DD01B4434E66300659A9A7821F1CE8C5D9`;
  - launch wrapper: `952` bytes, SHA-256 `2FAE9BCF4324FA0A96A9FA82BA920C769899D95D11C7F3EBCBB3521E4E7A2D7A`.

The installed Chrome-control API declares `Tabs.get(id: string): Promise<Tab>`, `Tab.id: string`, `Tab.title(): Promise<undefined | string>`, `Tab.markHandoff(): Promise<void>`, `getByRole(...)`, and locator `count(): Promise<number>`. The adoption cell's direct method signatures are compatible. The installed skill was used only as a static lifecycle/API reference; no browser call was made.

## Prior HIGH 1 — controller provenance

### What fix 1 closes

The prior review correctly rejected a bare assertion that `secureConsoleTaskTabV1` was an owned tab. Fix 1 now treats that object only as the source of a constrained candidate ID and performs one exact controller adoption:

1. declaration/shape checks require the retained `secureConsoleAgentV1`, proven `secureConsoleChromeV1`, callable `tabs.get`, candidate object, and a bounded safe ID string;
2. the candidate ID is supplied once to `secureConsoleChromeV1.tabs.get`;
3. the returned tab's safe ID must equal the supplied ID;
4. the returned object must have the expected tab methods;
5. exactly one fixed title read and one exact-role textbox count must match the fixed OmniRoute API-key page state; and
6. only then is the returned object assigned to the new unique `secureConsoleOwnedTaskTabV2` binding.

Static executable cardinality is exact for the core adoption step:

| Operation | Count |
| --- | ---: |
| `tabs.get` | 1 |
| `tabs.list` / `tabs.new` | 0 / 0 |
| title read | 1 |
| locator count | 1 |
| `nodeRepl.write` | 1 |
| navigation / close / handoff in the cell | 0 / 0 / 0 |
| serialization / screenshot | 0 / 0 |
| clipboard / keyboard | 0 / 0 |

No ID, title, marker value, URL, object, page content, tab metadata, or exception message enters the terminal. The dynamic error name is constrained to a short safe identifier and otherwise replaced with the fixed fallback class. A target mismatch nulls the owned binding and stops before later action.

This closes the original unproven-controller-ownership defect itself. It does not close the full authority/lifecycle finding below.

## Finding 1 — HIGH: adoption timing, terminal truthfulness, and lifecycle remain incomplete

### A. No fixed control deadline

The new one-shot cell has no exact outer tool-control deadline. Neither `tabs.get`, `title`, nor locator `count` accepts a contract-specified per-call deadline in the cell, and the brief gives no bounded outer timeout. The statement that a timeout spends the gate does not define when the timeout occurs. A hung browser/transport call can therefore outlive the intended one-shot boundary under an environment-dependent default.

**Correction:** pin one exact numeric outer control timeout for the sole JavaScript invocation, require complete untruncated forwarding of the one terminal, and state that expiry/interruption spends the subgate with no later browser or Task 2 action. Do not add timers, `Promise.race`, retry, or fallback inside the cell.

### B. `writeFulfilled` is forecast, not observed

The terminal reports:

```javascript
writeFulfilled: counters.writeFulfilled + 1
```

before calling code increments `counters.writeFulfilled`. This is not a truthful fulfilled counter at object construction time. Receipt of the tool output can independently prove that the write was delivered, but the field named `writeFulfilled` is still predicted rather than recorded. On a write that emits and then throws or on transport uncertainty, the fixed object may claim fulfillment while cell completion is not proven.

**Correction:** use a transport contract that does not mislabel a projected value as an observed counter. For example, emit `writeAttempted=1` and make complete receipt of the sole terminal the fulfillment proof, or use an explicit post-write eligibility variable that becomes true only after `nodeRepl.write` returns and require both exact terminal receipt and the completed cell state before later use. Missing/uncertain output must not leave an eligible binding.

### C. Binding disposition is incomplete on uncertain and pre-Create failure paths

The cell assigns `secureConsoleOwnedTaskTabV2 = adopted` before its terminal write. If the write or tool transport is missing/uncertain, the new owned alias may remain non-null even though the gate is spent. The prose forbids continuation but does not define a fixed residual state or detachment rule for that alias.

After exact adoption PASS, any later fresh-precondition, proxy, preparation, launch, or readiness failure before final Create likewise leaves the adopted binding/tab without a stated terminal disposition. The only disposition described is the user's native generated-page close after final Create. That success-path action does not cover pre-Create failure, and the brief does not null the binding after the native close.

**Correction:** define a monotonic private eligibility flag and explicit binding state for every terminal:

- initialize eligibility false;
- on subgate failure, null the new alias and leave the pre-existing candidate tab untouched;
- make later browser use conditional on both exact forwarded PASS and exact completed eligibility;
- if output or completion is uncertain, classify the new alias and tab residual state fixed/NOT PROVEN and forbid use without a separate reviewed disposition;
- define the exact pre-Create failure disposition (retained/untouched with a separate cleanup contract, or one explicit user-native close plus binding detach); and
- after the inherited native generated-page close, detach/null the JS alias without any further page/tab inspection, or explicitly classify the closed-object binding residual.

No second `get`, list, reacquisition, alternate handle, or agent close may be introduced as an implicit recovery.

### D. `markHandoff` is new uncounted authority

After PASS the brief authorizes `markHandoff`, but the pinned live brief contains no `markHandoff` operation or cardinality. The adoption cell only shape-checks the method. The later prose grants an unspecified number/timing of handoff calls without a deadline, counter, redacted terminal, or failure disposition. Calling this “inherited” does not make it part of the inherited byte-level contract.

**Correction:** remove `markHandoff` if it is unnecessary. If retention across a turn is genuinely required, specify exactly one directly awaited call at an exact pre-Create point with a fixed control deadline, attempted/fulfilled evidence, and fail-closed disposition, and explain why it does not broaden provider or credential authority. It must remain zero after final Create and on every failed adoption.

Until all four corrections are exact, the prior browser-authority HIGH is only partially resolved.

## Prior HIGH 2 — retained-owner cleanup

### What fix 1 closes conceptually

The new prose matrix states the correct security rules:

- start attempted precedes launch;
- start fulfilled/handle retained follow exact launch return and handle/PID/clock guard;
- no file/root deletion while a retained owner may still run;
- retained handles route through the inherited remaining-budget wait and sole kill/exit-proof path;
- start-uncertain/no-handle state forbids process enumeration/reacquisition and destructive cleanup;
- failed exit proof retains artifacts and stops; and
- file/root cleanup follows only proven exit.

Those rules close the conceptual omissions from the first candidate. They are not yet an executable contract.

## Finding 2 — HIGH: the cleanup matrix is prose-only and not connected to the exact launch fence

The two exact PowerShell fences are byte-for-byte unchanged from the failed candidate. Static inspection shows, across both wrappers:

- `OWNER_START` / owner-start state declarations or increments: `0`;
- `try` / `catch` / `finally` around launch: `0 / 0 / 0`;
- retained-handle `WaitForExit`: `0`;
- retained-handle `Kill`: `0`;
- exit-proof branch: `0`; and
- matrix residual/file/root counter output: `0`.

The launch wrapper still directly dot-sources the inherited start and then throws on a missing owner/PID/clock guard. No exact executable code increments start attempted immediately before the start-capable operation, distinguishes “start impossible” from “start may have occurred,” or routes an exception/output uncertainty into the correct matrix branch. No exact failure-cleanup fence is supplied. The owner would have to improvise variable names, counter initialization, catch placement, process-state tests, remaining-budget routing, artifact retention, and terminal output outside reviewed bytes.

This is load-bearing because `Start-Process` can succeed before a later property access, wrapper guard, output transport, or coordinator step fails. Prose alone cannot prove whether a process may exist, whether the exact handle is retained, or which cleanup branch is safe. An ad hoc implementation would either risk deleting files used by a live owner or risk unauthorized process lookup/reacquisition.

**Required correction:** provide exact parseable PowerShell bytes—either replace the launch wrapper with one fully guarded orchestration fence or add one exact failure-disposition fence—and pin its byte count/hash. The executable contract must:

1. initialize every start/wait/termination/exit-proof/file/root/residual counter and state label;
2. increment start attempted immediately before the exact start-capable dot-source call;
3. retain `$owner`, `$expectedOwnerPid`, and `$ownerClock` as soon as available, and set start fulfilled/handle retained only after the exact guard;
4. catch every launch/extraction/guard/output failure without emitting exception text;
5. distinguish exact pre-start/start-impossible, retained-handle, and start-uncertain/no-handle states monotonically;
6. route the retained-handle branch through the already pinned single final remaining-budget block, with no second wait/kill/exit proof;
7. forbid process enumeration, PID/name lookup, reacquisition, tree kill, or destructive temp cleanup in the no-handle/uncertain or exit-unproven branches;
8. permit fixed-hash/direct-child file and root cleanup only after proven owner exit;
9. guard proxy cleanup and prove proxy absent/network members `2`/listener absent;
10. emit one fixed redacted terminal containing truthful counters and residual state; and
11. make rejected, missing, truncated, timed-out, or uncertain terminal output spend the replacement without retry or later action.

The exact code must also define how the normal-success path transfers the same retained counters/handle/clock into nonblocking coordination and the one inherited final block, without redeclaration or a second cleanup path.

## Preserved inherited boundaries

No defect was found in the unchanged scope, credential, confirmation, or revocation rules themselves. Fix 1 continues to preserve:

- the old incident gate as spent and this candidate as a new no-retry gate;
- complete fresh original preconditions plus a new clipboard empty proof;
- one private-proxy start and one deterministic R5 POST maximum;
- exact token name, `mysw.me`, specific-zone scope, and only `Zone WAF Edit` plus `Zone Read`;
- zero account/token-management, DNS, Tunnel, Access, public rollout, OmniRoute rollout key, model, alternate bridge, dashboard Rulesets mutation, PATCH/edit, permission expansion, retry, fallback, second start, second POST, handoff between owners, or verdict relaxation;
- retained PID and exact `OWNER_READY=PASS` / `SECRET_PROMPT_READY=PASS` before final Create;
- separate mandatory action-time confirmation for final Create/native Copy/masked Paste and later exact-row deletion;
- zero agent token-page/credential clipboard inspection after Create;
- same-process token verification and private Zone-ID derivation;
- one exact-hash bounded R5 child;
- universal post-accept revocation hold, invalidity proof, guarded cleanup, and conservative NOT PROVEN states; and
- exact success only on the inherited terminal tuple, proven external owner exit, artifact cleanup, refreshed token counts `0 / 0`, and HTTP `401`.

Standing unattended authority waives neither mandatory user confirmation and cannot retry or relax any spent, uncertain, or failed gate.

## Disposition

The fix is not safe or unambiguous enough for execution. Close both HIGH findings in a new committed revision and obtain another independent Sol High review. Until then, the prior live gate remains spent, this replacement candidate remains blocked, and no browser, process, proxy, credential, Cloudflare, VM, routing, or cleanup action is authorized under it.
