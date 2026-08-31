# Task 14 v7 retained-binding cleanup brief

Status: fresh static cleanup candidate. `authorizes_live_execution=false`.

This is a new cleanup-only one-shot contract after the consumed v7 native
clipboard preflight retained its non-secret expected-challenge binding. It is
not a v7 retry, continuation, comparison attempt, fallback, transport test, or
verdict override. The independently classified evidence already proves the
exact v7 tab closed, Call 3 eligibility consumed, the comparison failed, and
the final Windows clipboard empty. This contract performs only a conditional
in-memory null assignment to the retained non-secret challenge binding.

## Pinned evidence and future report

- current base / Task 13 classification commit:
  `c2312314afd2e0fa46095e751917315d799ae285`;
- corrected Task 13 brief commit:
  `a2b887bb4fad01343b5d2957a27363ee877c7c72`;
- Task 13 live report commit
  `0028d20fcfa19b17241bc5cb882f7daae418973c`: `2706` bytes,
  SHA-256
  `A5FE7A2A9033AE5693AF8582F5A74A6631A1E06BB90587ECF449EA6AD45ECA01`;
- Task 13 independent classification: `5509` bytes, SHA-256
  `269A8F2A27F3662C69DBF0CC85E977D1DE91E7EA043C250F21833AB530EA8BA9`;
- prior Task 12 cleanup pattern commit:
  `15bdf746ffdc4f524f867c147e44233f76b36f5c`;
- project-root `AGENTS.md`: `6051` bytes, SHA-256
  `AD0EA394F694C7795870C2B66D745EDC1FCA8997E7D7041A21E5659B0C349DDC`.

The pinned Task 13 classification explicitly proves final Windows clipboard
empty, the v7 expected-challenge binding retained and present, and v7 Call 3
eligibility consumed. That proof is an external action-time prerequisite; this
contract neither reads nor changes the clipboard. Any classification byte,
meaning, or pin mismatch stops before the sole call.

A future result must be written only to
`.superpowers/sdd/2026-08-31-omniroute-secure-console-transfer/task-14-v7-retained-binding-cleanup-live-report.md`
and independently classified. It must remain redacted and set
`authorizes_live_execution=false`.

## Authority and exact boundary

Standing unattended authority may permit the sole Sol High owner to consume
this fresh cleanup gate only after independent direct-byte PASS and action-time
verification of the exact brief, review, Task 13 report/classification, and
project authority pins; the classification's final-clipboard-empty proof; an
empty Git index; the unchanged exact 12-path dirty source baseline; the same
persistent Node session that owns the v7 bindings; and zero intervening binding
action.

There is exactly one JavaScript call. Its fresh cleanup eligibility is consumed
before any binding check. Any invocation, mismatch, rejection, missing or
malformed output, or tool uncertainty spends this cleanup gate and stops. No
retry, fallback, second check, second assignment, clipboard call, browser call,
tab action, child process, navigation, server/listener/process inspection or
action, credential, provider, Cloudflare, VM, proxy, key, token, OmniRoute, or
routing action is permitted.

## Sole call — verify retained state, then null once

Run this exact JavaScript cell once in the persistent session that owns the v7
bindings. It first consumes fresh cleanup eligibility. It then checks that the
expected challenge is declared, non-null, a 50-character exact
`OMNI-PREFLIGHT-V7-` plus 32 uppercase-hex non-secret value, and that Call 3
eligibility is declared and exactly false/consumed. Only the exact precondition
branch attempts one null assignment.

```javascript
let nativeClipboardPreflightV7ResidualCleanupEligible = true;
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
  const eligible = nativeClipboardPreflightV7ResidualCleanupEligible === true;
  nativeClipboardPreflightV7ResidualCleanupEligible = false;
  output.cleanupEligibilityConsumed = eligible;
  output.bindingCheckAttempted++;
  output.challengeDeclared = typeof nativeClipboardPreflightV7ExpectedChallenge !== "undefined";
  output.call3EligibilityDeclared = typeof nativeClipboardPreflightV7Call3Eligible !== "undefined";
  output.challengeInitiallyNonNull = output.challengeDeclared && nativeClipboardPreflightV7ExpectedChallenge !== null;
  output.challengeShapeMatched = output.challengeInitiallyNonNull && typeof nativeClipboardPreflightV7ExpectedChallenge === "string" && /^OMNI-PREFLIGHT-V7-[0-9A-F]{32}$/.test(nativeClipboardPreflightV7ExpectedChallenge);
  output.challengeLength = output.challengeShapeMatched ? nativeClipboardPreflightV7ExpectedChallenge.length : -1;
  output.call3EligibilityConsumed = output.call3EligibilityDeclared && nativeClipboardPreflightV7Call3Eligible === false;
  output.bindingCheckFulfilled++;
  const exactPreconditions = eligible && output.challengeDeclared && output.challengeInitiallyNonNull && output.challengeShapeMatched && output.challengeLength === 50 && output.call3EligibilityDeclared && output.call3EligibilityConsumed && output.bindingCheckAttempted === 1 && output.bindingCheckFulfilled === 1;
  if (exactPreconditions) {
    output.nullAttempted++;
    try {
      nativeClipboardPreflightV7ExpectedChallenge = null;
      output.nullFulfilled++;
      output.challengeBindingNull = nativeClipboardPreflightV7ExpectedChallenge === null;
      output.result = output.nullAttempted === 1 && output.nullFulfilled === 1 && output.challengeBindingNull ? "EXACT_RETAINED_CHALLENGE_CLEARED" : "NULL_RESULT_NOT_PROVEN";
    } catch (error) {
      output.errorClass = safeErrorClass(error);
      output.result = "NULL_ASSIGNMENT_NOT_PROVEN";
    }
  }
  nodeRepl.write(output);
})();
```

Exact PASS requires result `EXACT_RETAINED_CHALLENGE_CLEARED`, error `NONE`,
cleanup eligibility true/consumed, binding check `1 / 1`, challenge
declared/non-null/shape true, length 50, Call 3 eligibility declared and
consumed true, null `1 / 1`, and final binding null true. PASS also requires
the action-time direct-byte proof that the pinned Task 13 classification still
proves final Windows clipboard empty.

If any precondition mismatches, null attempted/fulfilled remain `0 / 0`, the
challenge binding is not assigned, result remains
`PRECONDITION_MISMATCH_NOT_PROVEN`, and the contract stops. The fresh cleanup
eligibility remains consumed. Assignment error or any missing, malformed,
rejected, or tool-uncertain output is FAIL / NOT PROVEN and permits no second
attempt.

## Static, redaction, and residual boundary

Independent review must verify strict UTF-8/LF bytes, non-evaluating JavaScript
syntax, exactly one JavaScript cell/call, one consumed cleanup eligibility
transition before checks, one binding-check path, one success-gated null
assignment, one redacted `nodeRepl.write`, mismatch-before-assignment ordering,
and zero prohibited action. It must separately verify the pinned Task 13
classification bytes and its final-Windows-clipboard-empty conclusion.

Output contains only safe result/error classes, booleans, length, and counters;
it never emits the challenge value or any clipboard content. The old v3/v5
listener/server/process residuals remain untouched and `NOT PROVEN` after every
outcome. This brief authorizes no live execution; independent PASS and exact
action-time pins remain mandatory.
