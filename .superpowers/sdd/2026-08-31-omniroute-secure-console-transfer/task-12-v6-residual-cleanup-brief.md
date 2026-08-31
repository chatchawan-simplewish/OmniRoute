# Task 12 v6 residual cleanup brief

Status: fresh static cleanup candidate. `authorizes_live_execution=false`.

This is a new cleanup-only one-shot contract after the consumed v6 preflight's
sole child start failed with `ENOENT`. It is not a v6 retry, continuation,
comparison attempt, fallback, or transport verdict override. The exact v6 tab
is already proven closed. This contract only clears/proves the current
clipboard empty, then conditionally nulls the retained non-secret challenge
binding after verifying its redacted state.

## Pinned evidence and future report

- current base / Task 11 classification commit:
  `05499000fc62476607ff3e41f269ea45c3a79c2d`;
- corrected Task 11 brief: `18717` bytes, SHA-256
  `3D5670C7E5E5C3D58205D168311E4732A605325CF9A082C1AD84EEE862B1CFFB`;
- Task 11 live report commit
  `2e8dfc13890ed41a738b579e36ce470b4e9fa7c0`: `2249` bytes,
  SHA-256
  `30FE3DCC71A212DF124168127284D559ED2358D14AF992D59AA575BF7F4EB35D`;
- Task 11 classification: `4802` bytes, SHA-256
  `F95C749388D383F160ACA64A5EC2986110D698818A0B8450ABB05F7582C675D5`;
- project-root `AGENTS.md`: `6051` bytes, SHA-256
  `AD0EA394F694C7795870C2B66D745EDC1FCA8997E7D7041A21E5659B0C349DDC`.

The evidence proves native write fulfilled, the exact v6 tab closed, Call 3
eligibility was consumed, child exit/comparison/final clear did not fulfill,
and the exact-shaped non-secret challenge binding remained retained. Final
clipboard state is `NOT PROVEN` before this cleanup.

A future result must be written only to
`.superpowers/sdd/2026-08-31-omniroute-secure-console-transfer/task-12-v6-residual-cleanup-live-report.md`
and independently classified. It must remain redacted and set
`authorizes_live_execution=false`.

## Authority and exact boundary

Standing unattended authority may permit the sole Sol High owner to consume
this fresh cleanup gate only after independent direct-byte PASS and action-time
verification of exact brief/review/evidence/authority pins, empty Git index,
unchanged exact 12-path dirty source baseline, the same persistent Node
session, and zero intervening clipboard or binding action.

There are exactly two serial calls. Call 2 is forbidden unless Call 1 returns
its exact success tuple. Any invocation, mismatch, rejection, missing or
malformed output, or tool uncertainty spends this cleanup gate and stops. No
retry, fallback, second clear/read, second binding check/null, browser call,
tab action, child process, navigation, server/listener/process inspection or
action, credential, provider, Cloudflare, VM, proxy, key, token, OmniRoute, or
routing action is permitted.

## Call 1 — clear once and prove current clipboard empty once

Run this exact PowerShell 7 block once. It emits no clipboard content.

```powershell
$ErrorActionPreference = 'Stop'
$clearAttempted = 0
$clearFulfilled = 0
$emptyReadAttempted = 0
$emptyReadFulfilled = 0
$clipboardEmpty = $false
$errorClass = 'NONE'
try {
    $clearAttempted++
    Set-Clipboard -Value ''
    $clearFulfilled++
    $emptyReadAttempted++
    $currentClipboard = [string](Get-Clipboard -Raw)
    $emptyReadFulfilled++
    $clipboardEmpty = $currentClipboard.Length -eq 0
} catch {
    $name = $_.Exception.GetType().Name
    $errorClass = if ($name -cmatch '^[A-Za-z][A-Za-z0-9_.-]{0,63}$') { $name } else { 'ERROR' }
} finally {
    $currentClipboard = $null
}
'V6_RESIDUAL_CLIPBOARD_CLEAR_ATTEMPTED=' + $clearAttempted
'V6_RESIDUAL_CLIPBOARD_CLEAR_FULFILLED=' + $clearFulfilled
'V6_RESIDUAL_CLIPBOARD_EMPTY_READ_ATTEMPTED=' + $emptyReadAttempted
'V6_RESIDUAL_CLIPBOARD_EMPTY_READ_FULFILLED=' + $emptyReadFulfilled
'V6_RESIDUAL_CLIPBOARD_EMPTY=' + $clipboardEmpty.ToString().ToUpperInvariant()
'V6_RESIDUAL_CLIPBOARD_ERROR=' + $errorClass
if ($clearAttempted -eq 1 -and $clearFulfilled -eq 1 -and $emptyReadAttempted -eq 1 -and $emptyReadFulfilled -eq 1 -and $clipboardEmpty -and $errorClass -eq 'NONE') { exit 0 }
exit 2
```

Exact Call 1 success requires exit 0, clear `1 / 1`, empty read `1 / 1`, empty
true, and error `NONE`. Anything else forbids Call 2.

## Call 2 — verify retained state, then null once

Run this exact JavaScript cell once in the persistent session that owns the v6
bindings. Fresh cleanup eligibility is consumed before inspection. It checks
that the challenge binding is declared, non-null, a 50-character exact
`OMNI-PREFLIGHT-V6-` plus 32 uppercase-hex non-secret value, and that Call 3
eligibility is declared and exactly false/consumed. Only the exact precondition
branch attempts one null assignment.

```javascript
let nativeClipboardPreflightV6ResidualCleanupEligible = true;
await (async () => {
  const safeErrorClass = (error) => {
    const name = typeof error?.name === "string" ? error.name : "";
    return /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(name) ? name : "ERROR";
  };
  const output = {
    result: "PRECONDITION_MISMATCH_NOT_PROVEN",
    errorClass: "NONE",
    cleanupEligibilityConsumed: false,
    bindingCheckAttempted: 0,
    bindingCheckFulfilled: 0,
    challengeDeclared: false,
    challengeInitiallyNonNull: false,
    challengeShapeMatched: false,
    challengeLength: -1,
    call3EligibilityDeclared: false,
    call3EligibilityConsumed: false,
    nullAttempted: 0,
    nullFulfilled: 0,
    challengeBindingNull: false
  };
  const eligible = nativeClipboardPreflightV6ResidualCleanupEligible === true;
  nativeClipboardPreflightV6ResidualCleanupEligible = false;
  output.cleanupEligibilityConsumed = eligible;
  output.bindingCheckAttempted++;
  output.challengeDeclared = typeof nativeClipboardPreflightV6ExpectedChallenge !== "undefined";
  output.call3EligibilityDeclared = typeof nativeClipboardPreflightV6Call3Eligible !== "undefined";
  output.challengeInitiallyNonNull = output.challengeDeclared && nativeClipboardPreflightV6ExpectedChallenge !== null;
  output.challengeShapeMatched = output.challengeInitiallyNonNull && typeof nativeClipboardPreflightV6ExpectedChallenge === "string" && /^OMNI-PREFLIGHT-V6-[0-9A-F]{32}$/.test(nativeClipboardPreflightV6ExpectedChallenge);
  output.challengeLength = output.challengeShapeMatched ? nativeClipboardPreflightV6ExpectedChallenge.length : -1;
  output.call3EligibilityConsumed = output.call3EligibilityDeclared && nativeClipboardPreflightV6Call3Eligible === false;
  output.bindingCheckFulfilled++;
  const exactPreconditions = eligible && output.challengeDeclared && output.challengeInitiallyNonNull && output.challengeShapeMatched && output.challengeLength === 50 && output.call3EligibilityDeclared && output.call3EligibilityConsumed && output.bindingCheckAttempted === 1 && output.bindingCheckFulfilled === 1;
  if (exactPreconditions) {
    output.nullAttempted++;
    try {
      nativeClipboardPreflightV6ExpectedChallenge = null;
      output.nullFulfilled++;
      output.challengeBindingNull = nativeClipboardPreflightV6ExpectedChallenge === null;
      output.result = output.nullAttempted === 1 && output.nullFulfilled === 1 && output.challengeBindingNull ? "EXACT_RETAINED_CHALLENGE_CLEARED" : "NULL_RESULT_NOT_PROVEN";
    } catch (error) {
      output.errorClass = safeErrorClass(error);
      output.result = "NULL_ASSIGNMENT_NOT_PROVEN";
    }
  }
  nodeRepl.write(output);
})();
```

Exact Call 2 PASS requires result `EXACT_RETAINED_CHALLENGE_CLEARED`, error
`NONE`, cleanup eligibility true/consumed, binding check `1 / 1`, challenge
declared/non-null/shape true, length 50, Call 3 eligibility declared and
consumed true, null `1 / 1`, and final binding null true.

If any precondition mismatches, null attempted/fulfilled remain `0 / 0`, the
binding is not assigned, result remains `PRECONDITION_MISMATCH_NOT_PROVEN`, and
the contract stops. Assignment error or any missing/malformed/rejected/tool-
uncertain output is FAIL / NOT PROVEN and permits no second attempt.

## Static, redaction, and residual boundary

Independent review must verify strict UTF-8/LF bytes, PowerShell parsing,
non-evaluating JavaScript syntax, exactly one clear/read, one consumed cleanup
eligibility transition, one binding-check path, one success-gated null
assignment, one redacted `nodeRepl.write`, mismatch-before-assignment ordering,
and zero prohibited action.

Output contains only safe result/error classes, booleans, length, and counters;
it never emits clipboard content or challenge value. The old v3/v5
listener/server/process residuals remain untouched and `NOT PROVEN` after every
outcome. This brief authorizes no live execution; independent PASS and exact
action-time pins remain mandatory.
