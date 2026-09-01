# Task 2 secure-console scope replacement — fix-round-3 Sol High review

## Verdict

**FAIL** — the two findings carried from fix round 2 are corrected, but one new
**IMPORTANT** cleanup-state finding prevents a safe, unambiguous static PASS.
`authorizes_live_execution=false`.

This is a static review only. It authorizes no browser, clipboard, credential,
Cloudflare, VM, process, routing, or other live action.

## Reviewed source and integrity

- Brief commit: `2f6a6d57cf9e560eedf048dd9469012342e0fd83`.
- Exact brief: `task-2-secure-console-transfer-scope-replacement-brief.md`.
- Direct bytes: `38554`.
- SHA-256: `029EA6598D946934AAFD300C271CE821789DC6BB17B78FDABA23AB92B22AD0E1`.
- All six executable fences matched their supplied direct-byte pins exactly.
- All three JavaScript fences passed non-evaluating `node --check` with empty
  stdout/stderr. All three PowerShell fences parsed with zero parser errors.

## Prior finding disposition

### Prior HIGH — cleanup child handle loss: corrected

The corrected cleanup helper assigns the exact process to the retained script
binding before `Start()` and retains that process plus both asynchronous stream
tasks on start uncertainty, exit-not-proven, and drain-not-proven paths
(brief lines 400-440). Timeout handling performs at most one exact-handle kill
and one bounded exit-proof wait (lines 420-434). No lookup, reacquisition, or
second termination path is introduced.

### Prior IMPORTANT — unguarded detach cells: corrected

Both detach cells now require the exact retained declarations, non-null binding,
eligible state, `ADOPTED_ELIGIBLE` lifecycle state, and mutually exclusive
unconsumed flags before mutation (lines 208-232 and 253-277). Each cell reports
fixed redacted counters and state, and a failed, repeated, or opposite-cell
attempt is explicitly spent without retry (lines 294-305). The cells perform no
browser action and do not claim tab-closure proof.

## Finding

### IMPORTANT — cleanup child output/disposal exceptions can retain state while reporting `PROXY_CLEANUP_CHILD_RESIDUAL=NONE`

The cleanup child does not monotonically classify every terminal uncertainty:

- `[Threading.Tasks.Task]::WaitAll(...)` at lines 437-441 can throw when either
  redirected stream task is faulted, rather than return `false`. The subsequent
  `.Result` reads at line 443 can also throw. Neither operation has a local
  catch that changes `scopeProxyChildResidual`, so the parent fail terminal can
  report a retained process/tasks tuple with child residual still `NONE`.
- On the otherwise-successful path, `Dispose()` at lines 454-460 can throw after
  `DISPOSE_ATTEMPTED` but before fulfilled/nulling and before the residual is set
  to `NONE`. Because the residual begins as `NONE`, this also produces an
  internally contradictory terminal: overall cleanup failed, dispose is `1/0`,
  retained bindings remain, but child residual says `NONE`.
- When the one permitted timeout termination proves exit, lines 428-432 throw
  immediately without the bounded stream drain or a safe disposal attempt. The
  prose promises retention until proven drain and safe disposal (lines 608-614)
  but does not define this `TIMEOUT_EXIT_PROVEN` retained-handle/task disposition
  or authorize a later one-shot disposition. The gate is spent, so the ambiguity
  cannot be repaired by continuation.

The overall catch remains fail-closed and no live child is claimed absent, so
this is not the prior HIGH handle-loss defect. It is nevertheless load-bearing:
the fixed terminal can misstate exact cleanup-child residual state and the
contract is not fully actionable for these reachable exception paths.

### Required correction

After every proven child exit, including the timeout/kill path, perform the one
bounded stream-drain attempt. Catch both the drain wait and result access; set a
distinct monotonic non-`NONE` residual before returning failure and retain the
exact process/tasks. Wrap disposal similarly: increment attempted immediately
before the call, set a distinct disposal-not-proven residual on exception, and
clear retained bindings only after fulfilled disposal. Define the resulting
redacted terminal states and explicitly state that no second wait, kill, drain,
dispose, cleanup invocation, lookup, retry, or fallback is permitted.

## Preserved boundaries

Apart from the finding above, the replacement remains a fresh, one-shot scope
fix; it does not revive the spent predecessor. Adoption, the mutually exclusive
detach transitions, the retained-owner monotonic cleanup matrix, the inherited
mandatory confirmations, universal revocation hold, exact deletion boundary,
secret-redaction rules, and no-retry/no-fallback/no-handoff scope remain intact.

## Finding count

- Blocking: 0
- HIGH: 0
- IMPORTANT: 1
- Static verdict: **FAIL**
- `authorizes_live_execution=false`
