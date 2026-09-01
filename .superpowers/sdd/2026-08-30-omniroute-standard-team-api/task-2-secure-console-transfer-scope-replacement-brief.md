# Task 2 secure-console retained-scope replacement brief

Status: **PROPOSED — not executable until independent Sol High PASS review**

## Purpose

Replace the spent launch-scope gate documented in
`task-2-secure-console-transfer-launch-scope-incident.md`. This is one new
no-retry gate, not a retry of the prior gate. It changes only the coordinator's
PowerShell invocation scope so preparation and launch variables remain in the
same retained parent process.

## Inherited fixed contract

The replacement inherits without relaxation every boundary, fixed value,
counter, timeout, hash, user-native action, mandatory action-time confirmation,
revocation hold, cleanup rule, and terminal condition from:

- live brief commit `7af3ab75ec87d81d75811ff8f2e9b4fa9d0c3e3b`;
- independent PASS review commit
  `ce47c2eacb5a5cbf055c3fc814137e46c1855e40`;
- retained-Chrome recovery brief/review/classification commits
  `70b6b1087748b0612b195f4b1d7e1a78d13bafb7`,
  `f2defb1e8ebf015ac48e7e82fc18e8c83b530746`, and
  `788d38a5db1fd598631fee4f8db764d3719f9186`;
- launch-scope incident commit
  `029cf42275d2d61b6f69f38b7d94a1478702f135`;
- first replacement FAIL review commit
  `d77851c13ee8a0f2f54a214a9175aad1f4ee9285`.

The fixed Cloudflare token remains:

- name `OmniRoute secure console R5 20260901`;
- zone `mysw.me`;
- exactly `Zone WAF Edit` and `Zone Read`;
- no account/token-management, DNS, Tunnel, Access, or other permission.

Scope remains only one private-proxy start plus deterministic Rulesets R5
correction. No Tunnel, DNS/public hostname, Access application, public rollout,
OmniRoute rollout key, model request, alternate bridge, retry, fallback,
second start, second POST, dashboard Rulesets mutation, PATCH/edit, or verdict
relaxation is authorized.

## Fresh action-time checks

Before the replacement consumes any live start:

1. revalidate all original byte/hash, worktree, Windows identity/policy, VM,
   Cloudflare, token-row, public-DNS, and OmniRoute-key prerequisites;
2. consume the separate retained-tab adoption subgate below and continue only
   from its exact PASS terminal using `secureConsoleOwnedTaskTabV2`;
3. perform exactly one new credential-free clipboard clear and exactly one
   shape-only read, requiring empty `TRUE`; this replacement-specific count does
   not reuse or reinterpret the spent gate's clear/read;
4. prove `team-api-proxy` absent, network members `2`, listener `20130` absent,
   and no exact prepared temp directory or owner process from the incident;
5. stop before live action on any discrepancy.

## Separate retained-tab adoption subgate

This subgate resolves finding 1 from the first replacement review. It is a
separate, first, one-shot browser-binding adoption step. It occurs before the
replacement-specific clipboard clear, private-proxy start, preparation, owner
launch, Cloudflare mutation, or credential action.

It uses the previously proven same-session `secureConsoleChromeV1` and the
currently retained but not yet owned `secureConsoleTaskTabV1`. It performs
exactly one `secureConsoleChromeV1.tabs.get()` for the exact retained tab ID.
Because the retrieval is performed by that exact proven Chrome controller and
the returned safe ID must equal the supplied ID, this establishes controller
ownership without a tab list or metadata emission. It then performs exactly
one fixed-title read and one exact targeted locator count to bind the current
OmniRoute API-key page state. It emits only fixed counters, booleans, a safe
error class, and a fixed terminal.

The sole owner executes this exact JavaScript fence once in the same persistent
Node session:

```javascript
let secureConsoleOwnedTaskTabV2 = null;
await (async () => {
  const counters = {
    getAttempted: 0,
    getFulfilled: 0,
    titleAttempted: 0,
    titleFulfilled: 0,
    markerAttempted: 0,
    markerFulfilled: 0,
    writeAttempted: 0,
    writeFulfilled: 0,
  };
  let result = "PRECONDITION_FAIL";
  let errorClass = "NONE";
  let declarationShape = false;
  let controllerOwnership = false;
  let tabShape = false;
  let targetState = false;
  const safeErrorClass = (error) => {
    const name = typeof error?.name === "string" ? error.name : "";
    return /^[A-Za-z][A-Za-z0-9_.-]{0,63}$/.test(name) ? name : "RetainedTabAdoptionError";
  };
  try {
    declarationShape =
      typeof secureConsoleAgentV1 === "object" && secureConsoleAgentV1 !== null &&
      typeof secureConsoleChromeV1 === "object" && secureConsoleChromeV1 !== null &&
      typeof secureConsoleChromeV1.tabs?.get === "function" &&
      typeof secureConsoleTaskTabV1 === "object" && secureConsoleTaskTabV1 !== null &&
      typeof secureConsoleTaskTabV1.id === "string" &&
      /^[A-Za-z0-9_-]{1,64}$/.test(secureConsoleTaskTabV1.id);
    if (!declarationShape) throw new Error("RetainedBindingShapeError");

    const retainedId = secureConsoleTaskTabV1.id;
    counters.getAttempted++;
    const adopted = await secureConsoleChromeV1.tabs.get(retainedId);
    counters.getFulfilled++;
    controllerOwnership =
      typeof adopted === "object" && adopted !== null &&
      typeof adopted.id === "string" && adopted.id === retainedId;
    tabShape =
      controllerOwnership &&
      typeof adopted.goto === "function" &&
      typeof adopted.title === "function" &&
      typeof adopted.markHandoff === "function" &&
      typeof adopted.playwright?.getByRole === "function";
    if (!tabShape) throw new Error("RetainedTabOwnershipError");

    counters.titleAttempted++;
    const title = await adopted.title();
    counters.titleFulfilled++;
    counters.markerAttempted++;
    const markerCount = await adopted.playwright.getByRole("textbox", {
      name: "Search by name or token...",
      exact: true,
    }).count();
    counters.markerFulfilled++;
    targetState =
      title === "OmniRoute — AI Gateway for Multi-Provider LLMs" &&
      markerCount === 1;
    if (!targetState) throw new Error("RetainedTabTargetStateError");

    secureConsoleOwnedTaskTabV2 = adopted;
    result = "EXACT_RETAINED_TASK_TAB_ADOPTION_PASS";
  } catch (error) {
    secureConsoleOwnedTaskTabV2 = null;
    errorClass = safeErrorClass(error);
  }
  counters.writeAttempted++;
  nodeRepl.write({
    result,
    declarationShape,
    controllerOwnership,
    tabShape,
    targetState,
    getAttempted: counters.getAttempted,
    getFulfilled: counters.getFulfilled,
    titleAttempted: counters.titleAttempted,
    titleFulfilled: counters.titleFulfilled,
    markerAttempted: counters.markerAttempted,
    markerFulfilled: counters.markerFulfilled,
    writeAttempted: counters.writeAttempted,
    writeFulfilled: counters.writeFulfilled + 1,
    errorClass,
  });
  counters.writeFulfilled++;
})();
```

Exact PASS requires result
`EXACT_RETAINED_TASK_TAB_ADOPTION_PASS`, all four booleans `true`, counters
`1/1` for get/title/marker/write, and `errorClass=NONE`. Any invocation,
rejection, missing output, counter mismatch, or other terminal spends this
replacement before later action. No retry, fallback, second get, list,
selected-tab lookup, reconnect, new tab, close, navigation, page serialization,
URL read/output, screenshot, clipboard action, keyboard action, or mutation is
permitted in this subgate.

After PASS, only `secureConsoleOwnedTaskTabV2` may be used for the inherited
serial read-only Cloudflare preconditions, form preparation, `markHandoff`, and
the already reviewed user-native sequence. The agent performs no browser call
after final Create. The user's inherited native generated-page close is the
binding's terminal disposition; no later agent close, get, list, reacquisition,
or metadata read is permitted.

## Corrected retained-parent orchestration

Use one persistent bundled-pwsh parent. Extract and hash-check the unchanged
credential-free proxy wrapper, preparation fence, owner fence, R5 fence, launch
fence, and final cleanup fence exactly as pinned by the inherited brief.

Execute the unchanged `8380`-byte proxy wrapper exactly once. It must return
`PROXY_START_AND_PROOF=PASS`.

Then execute the following new orchestration fence exactly once in that same
parent. It extracts the unchanged preparation fence and dot-sources it into the
current scope. Dot-sourcing is the only correction; the preparation code bytes
are unchanged.

```powershell
$briefRawForScope = [IO.File]::ReadAllText((Resolve-Path -LiteralPath '.superpowers\sdd\2026-08-30-omniroute-standard-team-api\task-2-secure-console-transfer-live-brief.md'), [Text.UTF8Encoding]::new($false, $true))
$prepTailForScope = $briefRawForScope.Substring($briefRawForScope.IndexOf('## Credential-free script preparation'))
$prepMatchForScope = [regex]::Match($prepTailForScope, '(?ms)^```powershell\n(?<code>.*?)^```$')
if (-not $prepMatchForScope.Success) { throw 'PREP_SCOPE_EXTRACTION_FAILED' }
$prepBytesForScope = [Text.UTF8Encoding]::new($false).GetBytes($prepMatchForScope.Groups['code'].Value)
$prepHashForScope = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($prepBytesForScope))
if ($prepBytesForScope.Length -ne 3983 -or $prepHashForScope -cne '784E91D71AB0B07A65C6FDA429CC4A86C3E6107C76E258BC608F75DA893C1D4A') { throw 'PREP_SCOPE_BYTE_PIN_FAILED' }
. ([scriptblock]::Create($prepMatchForScope.Groups['code'].Value))
if ([string]::IsNullOrWhiteSpace($transferRoot) -or [string]::IsNullOrWhiteSpace($ownerScriptPath) -or [string]::IsNullOrWhiteSpace($r5ScriptPath) -or [string]::IsNullOrWhiteSpace($safeLogPath)) { throw 'PREP_SCOPE_VARIABLES_MISSING' }
if ([IO.Path]::GetDirectoryName([IO.Path]::GetFullPath($ownerScriptPath)) -cne [IO.Path]::GetFullPath($transferRoot) -or [IO.Path]::GetDirectoryName([IO.Path]::GetFullPath($r5ScriptPath)) -cne [IO.Path]::GetFullPath($transferRoot) -or [IO.Path]::GetDirectoryName([IO.Path]::GetFullPath($safeLogPath)) -cne [IO.Path]::GetFullPath($transferRoot)) { throw 'PREP_SCOPE_CHILD_GUARD_FAILED' }
if ((Get-FileHash -Algorithm SHA256 -LiteralPath $ownerScriptPath).Hash -cne '347FCD60A41DF780CE4A94E4FC14C87E5059112068C689EF73636ABC5B0F0B6C' -or (Get-FileHash -Algorithm SHA256 -LiteralPath $r5ScriptPath).Hash -cne 'DB75253CD851075C1D612A54EC4B02C8016C034C8BC192A3DB9D02DB9890AD41' -or (Test-Path -LiteralPath $safeLogPath)) { throw 'PREP_SCOPE_WRITTEN_STATE_FAILED' }
[Console]::Out.WriteLine('EXACT_RETAINED_SCOPE_PREPARATION=PASS')
```

Extract the unchanged `655`-byte launch fence, require SHA-256
`995185FA04790564F4CDCA967E87CAB82EB97731D8458EF85CEF942D4606A293`,
and dot-source it once into the same parent:

```powershell
$launchTailForScope = $briefRawForScope.Substring($briefRawForScope.IndexOf('## Launch and transfer sequence'))
$launchMatchForScope = [regex]::Match($launchTailForScope, '(?ms)^```powershell\n(?<code>.*?)^```$')
if (-not $launchMatchForScope.Success) { throw 'LAUNCH_SCOPE_EXTRACTION_FAILED' }
$launchBytesForScope = [Text.UTF8Encoding]::new($false).GetBytes($launchMatchForScope.Groups['code'].Value)
$launchHashForScope = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($launchBytesForScope))
if ($launchBytesForScope.Length -ne 655 -or $launchHashForScope -cne '995185FA04790564F4CDCA967E87CAB82EB97731D8458EF85CEF942D4606A293') { throw 'LAUNCH_SCOPE_BYTE_PIN_FAILED' }
. ([scriptblock]::Create($launchMatchForScope.Groups['code'].Value))
if ($null -eq $owner -or $owner.Id -ne $expectedOwnerPid -or $null -eq $ownerClock) { throw 'LAUNCH_SCOPE_HANDLE_MISSING' }
[Console]::Out.WriteLine('EXACT_RETAINED_SCOPE_OWNER_LAUNCHED=PASS')
```

No `&` child-scope invocation is permitted for either fence. No variable
recovery by process enumeration, PID/name lookup, temp-directory scan, newest
file selection, or alternate path is permitted.

## Coordination and confirmations

Nonblocking safe-log inspection must prove the retained PID plus exact
`OWNER_READY=PASS` and `SECRET_PROMPT_READY=PASS` before the Cloudflare form's
final Create is enabled.

The mandatory final-Create/native-Copy/native-masked-Paste confirmation and the
later separate exact-row deletion confirmation remain mandatory exactly as in
the inherited brief. Standing unattended authority cannot bypass either
browser/tool/user action-time confirmation.

After final Create, no agent/browser inspection of the generated-token page or
clipboard is permitted. The user performs exactly one semantic Copy, exactly
one native masked Paste, closes the generated-token page, then presses Enter.
The owner performs all token verification, private Zone-ID derivation, exact R5
child execution, revocation hold, invalid-token proof, and cleanup.

## Failure and cleanup

Any discrepancy spends this replacement gate. No retry, second start, second
preparation, second launch, alternate invocation, or continuation is permitted.

The retained parent records fixed start-state counters and booleans:
`OWNER_START_ATTEMPTED`, `OWNER_START_FULFILLED`, `OWNER_HANDLE_RETAINED`,
`OWNER_WAIT_ATTEMPTED/FULFILLED`, `OWNER_TERMINATION_ATTEMPTED/FULFILLED`,
`OWNER_EXIT_PROOF_ATTEMPTED/FULFILLED`, `OWNER_FILE_CLEANUP`,
`OWNER_ROOT_CLEANUP`, and `OWNER_RESIDUAL`.

The parent increments start attempted immediately before dot-sourcing the exact
launch fence. It increments start fulfilled and sets handle retained only after
the fence returns and the exact `$owner`/PID/clock guard passes.

The monotonic failure matrix is mandatory:

1. Before start attempted, or after a launch failure for which process start is
   proven impossible, guarded cleanup may remove only the exact new proxy and
   exact direct-child hash-pinned prepared files/root.
2. If the exact retained owner handle exists, no safe log, owner/R5 script, or
   temp root may be deleted until that handle has proven exit. Every
   post-launch/pre-accept readiness failure, safe-output uncertainty, or other
   coordinator failure routes directly to the inherited single final
   remaining-budget block. That block alone may wait on the retained handle,
   make at most one exact-handle `Kill()` after the fixed wall deadline, perform
   the one bounded exit proof, inspect the redacted safe log, and delete files
   only after proven exit. The owner itself retains its bounded masked-prompt
   timeout and pre-accept common cleanup.
3. If process start may have occurred but no exact handle is retained, set
   `OWNER_RESIDUAL=START_UNCERTAIN_NO_HANDLE`, classify owner/process and temp
   state `NOT PROVEN`, perform no process lookup, enumeration, PID/name
   reacquisition, kill, safe-log deletion, script deletion, root deletion, or
   later-stage action, and stop.
4. If retained-handle exit cannot be proven after the sole permitted
   termination/exit-proof path, set
   `OWNER_RESIDUAL=EXACT_OWNER_EXIT_NOT_PROVEN`, retain all possibly in-use
   files/root, perform no lookup/reacquisition or later-stage action, and stop.
5. Only after owner exit is proven may the inherited direct-child guards and
   exact safe-log/script/root cleanup run. Then guarded proxy cleanup proves
   proxy absent, network members `2`, and listener `20130` absent.

All matrix evidence is fixed counters/booleans/status labels only; exception
text, process metadata, IDs, paths, page metadata, and secrets are forbidden.
After masked acceptance, use only the inherited owner's universal bounded
revocation-required path and cleanup. If final Create occurred without a usable
retained token, separately confirm exact-row deletion; exact-token HTTP `401`
remains `NOT PROVEN`.

Success remains only the inherited exact terminal tuple ending
`OWNER_RESULT=EXACT_CORRECTION_PASS_TOKEN_REVOKED` plus external owner exit,
script/safe-log/temp cleanup, refreshed Cloudflare token counts `0/0`, invalid
HTTP `401`, and independently reviewed redacted evidence.

## Review gate

Independent Sol High review must pin this brief's exact commit, byte count, and
SHA-256; validate the JavaScript fence without browser execution and both
PowerShell fences by parser only; confirm the adoption subgate has exact
controller provenance, counts, redaction, lifecycle, and disposition; confirm
dot-sourcing is the sole preparation/launch semantic change; verify the full
post-launch/pre-accept retained-handle cleanup matrix; confirm no old-gate retry
or expanded authority; and return exact `PASS` before execution. Any `FAIL`,
`NOT PROVEN`, ambiguity, or drift blocks execution.
