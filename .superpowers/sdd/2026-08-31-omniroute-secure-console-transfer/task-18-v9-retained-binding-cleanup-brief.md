# Task 18 v9 retained-binding cleanup brief

Status: fresh static cleanup candidate. `authorizes_live_execution=false`.

This is a new cleanup-only one-shot contract after the consumed v9 loopback
keyboard preflight retained its non-secret expected-challenge binding. It is
not a v9 retry, continuation, comparison attempt, fallback, transport test, or
verdict override. The independently classified evidence already proves the v9
tab and loopback server closed, Call 3 consumed, the comparison failed, and the
final Windows clipboard empty. This contract performs only a conditional
in-memory null assignment to the retained challenge binding.

## Pinned evidence and future artifacts

- current base / Task 17 classification commit:
  `b12a12b26286a7014f9dcb4f7203ac488d816a15`;
- Task 17 v9 brief commit
  `4a5c6e83a1fd7e44556fd1352698b3854f6a5ca9`: `31149` bytes,
  SHA-256
  `2F39D6128A09EFE8D8C3CAEC1587ABAA469539D88CACD1C521BC0CB0F15C1FBD`;
- Task 17 independent review commit
  `5c6c92d5c106c59b9782261225f9513b41da41e8`: `9577` bytes,
  SHA-256
  `B4D137117BDF2593F60741AFD434C8434E18202A3C205E0F4715E90A29B86F24`;
- Task 17 live report commit
  `a3bf5ea34605fad3ab20d32c49c24f297666d2fb`: `2166` bytes,
  SHA-256
  `DCABAD77FEC48915C9C2EE8BF13074C182B9E4304D42AA6958D045611F1396EC`;
- Task 17 independent classification: `6543` bytes, SHA-256
  `548B0C2BCD85C4D03E7305173A538969AAA228BA1B7C08DC5AB8813BBB51D4C3`;
- proven binding-only cleanup pattern: Task 14 v7 brief commit
  `adfa836f0934f30a3f2d0a4ffcb98cb271340804`.

The pinned classification proves the non-secret v9 expected-challenge binding
retained and present, the v9 gate consumed, the final Windows clipboard empty,
and the exact v9 tab and server closed. The pinned reviewed v9 brief defines
the retained value's exact shape as
`^OMNI-PREFLIGHT-V9-[0-9A-F]{32}$`, length 50. These are external action-time
prerequisites; this cleanup neither reads nor changes browser, clipboard,
server, listener, process, or routing state.

The only future report path is
`.superpowers/sdd/2026-08-31-omniroute-secure-console-transfer/task-18-v9-retained-binding-cleanup-live-report.md`.
The only future classification path is
`.superpowers/sdd/2026-08-31-omniroute-secure-console-transfer/task-18-v9-retained-binding-cleanup-classification.md`.
Both must remain redacted and set `authorizes_live_execution=false`.

## Authority and exact boundary

Standing unattended authority applies only after independent direct-byte PASS
and action-time verification of the exact brief/review/report/classification
and project-authority pins, the classification's retained-binding and final-
clipboard-empty conclusions, empty Git index, unchanged exact 12-path dirty
source baseline, the same persistent Node session that owns the v9 binding,
zero intervening binding action, and the fresh
`loopbackKeyboardPreflightV9RetainedBindingCleanupEligible` binding never
declared.

There is exactly one Node REPL cell. Its fresh cleanup eligibility is consumed
before any binding check. Invocation, precondition mismatch, assignment error,
rejection, missing or malformed output, timeout, or tool uncertainty spends
the cleanup gate and stops. No retry, fallback, second check, second assignment,
browser/tab/server/listener/process/clipboard inspection or mutation, child,
credential, key, token, OmniRoute, or routing action is permitted.

## Sole cell — verify retained shape, then null once

Run this exact cell once in the persistent Node session that owns the v9
binding. It never emits the retained value. Only exact consumed eligibility,
string type, reviewed shape, length 50, and one fulfilled check permit the sole
null assignment.

```javascript
let loopbackKeyboardPreflightV9RetainedBindingCleanupEligible = true;
await (async () => {
  const output = {
    result: "PRECONDITION_MISMATCH_NOT_PROVEN",
    cleanupEligibilityConsumed: false,
    bindingCheckAttempted: 0,
    bindingCheckFulfilled: 0,
    challengeIsString: false,
    challengeShapeMatched: false,
    challengeLengthMatched: false,
    nullAttempted: 0,
    nullFulfilled: 0,
    challengeBindingNull: false
  };
  const eligible = loopbackKeyboardPreflightV9RetainedBindingCleanupEligible === true;
  loopbackKeyboardPreflightV9RetainedBindingCleanupEligible = false;
  output.cleanupEligibilityConsumed = eligible;
  output.bindingCheckAttempted++;
  output.challengeIsString = typeof loopbackKeyboardPreflightV9ExpectedChallenge === "string";
  output.challengeShapeMatched = output.challengeIsString && /^OMNI-PREFLIGHT-V9-[0-9A-F]{32}$/.test(loopbackKeyboardPreflightV9ExpectedChallenge);
  output.challengeLengthMatched = output.challengeIsString && loopbackKeyboardPreflightV9ExpectedChallenge.length === 50;
  output.bindingCheckFulfilled++;
  const exactPreconditions = eligible && output.challengeIsString && output.challengeShapeMatched && output.challengeLengthMatched && output.bindingCheckAttempted === 1 && output.bindingCheckFulfilled === 1;
  if (exactPreconditions) {
    output.nullAttempted++;
    try {
      loopbackKeyboardPreflightV9ExpectedChallenge = null;
      output.nullFulfilled++;
      output.challengeBindingNull = loopbackKeyboardPreflightV9ExpectedChallenge === null;
      output.result = output.nullAttempted === 1 && output.nullFulfilled === 1 && output.challengeBindingNull ? "EXACT_RETAINED_CHALLENGE_CLEARED" : "NULL_RESULT_NOT_PROVEN";
    } catch {
      output.result = "NULL_ASSIGNMENT_NOT_PROVEN";
    }
  }
  nodeRepl.write(output);
})();
```

Exact PASS requires result `EXACT_RETAINED_CHALLENGE_CLEARED`, cleanup
eligibility consumed true, binding check `1 / 1`, string/shape/length booleans
all true, null `1 / 1`, and challenge binding null true.

Any precondition mismatch leaves null attempted/fulfilled `0 / 0`, performs no
assignment to `loopbackKeyboardPreflightV9ExpectedChallenge`, retains the
default `PRECONDITION_MISMATCH_NOT_PROVEN` result, and stops. Cleanup eligibility
remains consumed. Assignment error or any uncertain output is FAIL / NOT
PROVEN and permits no second attempt.

## Static, redaction, and residual boundary

Independent review must verify strict UTF-8/LF bytes, non-evaluating JavaScript
syntax, exactly one Node REPL cell, one cleanup-eligibility transition before
checks, one exact shape and length check, one success-gated null assignment,
one redacted `nodeRepl.write`, mismatch-before-assignment ordering, and zero
prohibited action. Output contains only the safe result, counters, and
booleans; it never emits the challenge or any clipboard/browser/server data.

The v9 transport remains failed/not proven. Older listener/process residuals
remain untouched and `NOT PROVEN`. This brief authorizes no live execution;
independent PASS and exact action-time pins remain mandatory.
