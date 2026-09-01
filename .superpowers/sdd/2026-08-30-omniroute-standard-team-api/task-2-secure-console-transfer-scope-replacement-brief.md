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
  `d77851c13ee8a0f2f54a214a9175aad1f4ee9285`;
- fix-round FAIL review commit
  `c6e6674cf508c2df11f3da15394007df030a7353`;
- second-fix FAIL review commit
  `318e6de4c99cca9cb56ae99a77393718dbe83c1a`.

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
Node session with one fixed outer tool-control deadline of `30000 ms`. No
internal timer or race is added. Complete, untruncated receipt of its sole
terminal plus completed tool status are both required; timeout, interruption,
missing/truncated output, or uncertain completion spends the subgate.

```javascript
let secureConsoleOwnedTaskTabV2 = null;
let secureConsoleOwnedTaskTabV2Eligible = false;
let secureConsoleOwnedTaskTabV2State = "UNADOPTED";
let secureConsoleOwnedTaskTabV2PreCreateDetachConsumed = false;
let secureConsoleOwnedTaskTabV2PostNativeDetachConsumed = false;
await (async () => {
  const counters = {
    getAttempted: 0,
    getFulfilled: 0,
    titleAttempted: 0,
    titleFulfilled: 0,
    markerAttempted: 0,
    markerFulfilled: 0,
    writeAttempted: 0,
  };
  let result = "PRECONDITION_FAIL";
  let errorClass = "NONE";
  let declarationShape = false;
  let controllerOwnership = false;
  let tabShape = false;
  let targetState = false;
  let adopted = null;
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
    adopted = await secureConsoleChromeV1.tabs.get(retainedId);
    counters.getFulfilled++;
    controllerOwnership =
      typeof adopted === "object" && adopted !== null &&
      typeof adopted.id === "string" && adopted.id === retainedId;
    tabShape =
      controllerOwnership &&
      typeof adopted.goto === "function" &&
      typeof adopted.title === "function" &&
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

    result = "EXACT_RETAINED_TASK_TAB_ADOPTION_PASS";
  } catch (error) {
    secureConsoleOwnedTaskTabV2 = null;
    secureConsoleOwnedTaskTabV2Eligible = false;
    secureConsoleOwnedTaskTabV2State = "ADOPTION_FAILED_CANDIDATE_UNTOUCHED";
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
    errorClass,
  });
  if (result === "EXACT_RETAINED_TASK_TAB_ADOPTION_PASS") {
    secureConsoleOwnedTaskTabV2 = adopted;
    secureConsoleOwnedTaskTabV2Eligible = true;
    secureConsoleOwnedTaskTabV2State = "ADOPTED_ELIGIBLE";
    secureConsoleOwnedTaskTabV2PreCreateDetachConsumed = false;
    secureConsoleOwnedTaskTabV2PostNativeDetachConsumed = false;
  }
})();
```

Exact PASS requires result
`EXACT_RETAINED_TASK_TAB_ADOPTION_PASS`, all four booleans `true`, counters
`1/1` for get/title/marker, `writeAttempted=1`, `errorClass=NONE`, complete
untruncated terminal receipt, completed tool status, and the later private
eligibility check exact `true`. Any invocation,
rejection, missing output, counter mismatch, or other terminal spends this
replacement before later action. No retry, fallback, second get, list,
selected-tab lookup, reconnect, new tab, close, navigation, page serialization,
URL read/output, screenshot, clipboard action, keyboard action, or mutation is
permitted in this subgate. A write or transport uncertainty cannot become
eligible: the alias and eligibility are assigned only after `nodeRepl.write`
returns. If output or completion is uncertain, the binding state is
`NOT_PROVEN`; no later action or detachment cell is permitted without a new
reviewed disposition.

After PASS, only `secureConsoleOwnedTaskTabV2` may be used for the inherited
serial read-only Cloudflare preconditions, form preparation, and the already
reviewed user-native sequence. `markHandoff` is not authorized by this
replacement. The agent performs no browser call after final Create.

On any exact proven pre-Create failure after adoption, execute the following
fixed `10000 ms`-deadline, no-browser detachment cell once. It leaves the
candidate tab retained and untouched while removing the new authority alias:

```javascript
let preCreateDetachAttemptedV2 = 0;
let preCreateDetachFulfilledV2 = 0;
const preCreateDetachDeclarationsV2 =
  typeof secureConsoleOwnedTaskTabV2 === "object" &&
  typeof secureConsoleOwnedTaskTabV2Eligible === "boolean" &&
  typeof secureConsoleOwnedTaskTabV2State === "string" &&
  typeof secureConsoleOwnedTaskTabV2PreCreateDetachConsumed === "boolean" &&
  typeof secureConsoleOwnedTaskTabV2PostNativeDetachConsumed === "boolean";
const preCreateDetachPreconditionV2 =
  preCreateDetachDeclarationsV2 &&
  secureConsoleOwnedTaskTabV2 !== null &&
  secureConsoleOwnedTaskTabV2Eligible === true &&
  secureConsoleOwnedTaskTabV2State === "ADOPTED_ELIGIBLE" &&
  secureConsoleOwnedTaskTabV2PreCreateDetachConsumed === false &&
  secureConsoleOwnedTaskTabV2PostNativeDetachConsumed === false;
let preCreateDetachResultV2 = "PRECONDITION_FAIL";
if (preCreateDetachPreconditionV2) {
  preCreateDetachAttemptedV2++;
  secureConsoleOwnedTaskTabV2Eligible = false;
  secureConsoleOwnedTaskTabV2 = null;
  secureConsoleOwnedTaskTabV2State = "RETAINED_UNTOUCHED_PRECREATE_FAILURE";
  secureConsoleOwnedTaskTabV2PreCreateDetachConsumed = true;
  preCreateDetachFulfilledV2++;
  preCreateDetachResultV2 = "EXACT_PRECREATE_BINDING_DETACH_PASS";
}
nodeRepl.write({
  result: preCreateDetachResultV2,
  declarationsValid: preCreateDetachDeclarationsV2,
  preconditionValid: preCreateDetachPreconditionV2,
  detachAttempted: preCreateDetachAttemptedV2,
  detachFulfilled: preCreateDetachFulfilledV2,
  preCreateConsumed: preCreateDetachDeclarationsV2 ? secureConsoleOwnedTaskTabV2PreCreateDetachConsumed : null,
  postNativeConsumed: preCreateDetachDeclarationsV2 ? secureConsoleOwnedTaskTabV2PostNativeDetachConsumed : null,
  browserCalls: 0,
  bindingEligible: preCreateDetachDeclarationsV2 ? secureConsoleOwnedTaskTabV2Eligible : null,
  bindingNull: preCreateDetachDeclarationsV2 ? secureConsoleOwnedTaskTabV2 === null : false,
  bindingState: preCreateDetachDeclarationsV2 ? secureConsoleOwnedTaskTabV2State : "DECLARATION_INVALID",
});
```

After the user reports completing the inherited native generated-page close,
execute this fixed `10000 ms`-deadline, no-browser detachment cell once without
any page/tab inspection:

```javascript
let postNativeDetachAttemptedV2 = 0;
let postNativeDetachFulfilledV2 = 0;
const postNativeDetachDeclarationsV2 =
  typeof secureConsoleOwnedTaskTabV2 === "object" &&
  typeof secureConsoleOwnedTaskTabV2Eligible === "boolean" &&
  typeof secureConsoleOwnedTaskTabV2State === "string" &&
  typeof secureConsoleOwnedTaskTabV2PreCreateDetachConsumed === "boolean" &&
  typeof secureConsoleOwnedTaskTabV2PostNativeDetachConsumed === "boolean";
const postNativeDetachPreconditionV2 =
  postNativeDetachDeclarationsV2 &&
  secureConsoleOwnedTaskTabV2 !== null &&
  secureConsoleOwnedTaskTabV2Eligible === true &&
  secureConsoleOwnedTaskTabV2State === "ADOPTED_ELIGIBLE" &&
  secureConsoleOwnedTaskTabV2PreCreateDetachConsumed === false &&
  secureConsoleOwnedTaskTabV2PostNativeDetachConsumed === false;
let postNativeDetachResultV2 = "PRECONDITION_FAIL";
if (postNativeDetachPreconditionV2) {
  postNativeDetachAttemptedV2++;
  secureConsoleOwnedTaskTabV2Eligible = false;
  secureConsoleOwnedTaskTabV2 = null;
  secureConsoleOwnedTaskTabV2State = "USER_NATIVE_CLOSE_REPORTED_BINDING_DETACHED";
  secureConsoleOwnedTaskTabV2PostNativeDetachConsumed = true;
  postNativeDetachFulfilledV2++;
  postNativeDetachResultV2 = "EXACT_POST_NATIVE_CLOSE_BINDING_DETACH_PASS";
}
nodeRepl.write({
  result: postNativeDetachResultV2,
  declarationsValid: postNativeDetachDeclarationsV2,
  preconditionValid: postNativeDetachPreconditionV2,
  detachAttempted: postNativeDetachAttemptedV2,
  detachFulfilled: postNativeDetachFulfilledV2,
  preCreateConsumed: postNativeDetachDeclarationsV2 ? secureConsoleOwnedTaskTabV2PreCreateDetachConsumed : null,
  postNativeConsumed: postNativeDetachDeclarationsV2 ? secureConsoleOwnedTaskTabV2PostNativeDetachConsumed : null,
  browserCalls: 0,
  bindingEligible: postNativeDetachDeclarationsV2 ? secureConsoleOwnedTaskTabV2Eligible : null,
  bindingNull: postNativeDetachDeclarationsV2 ? secureConsoleOwnedTaskTabV2 === null : false,
  bindingState: postNativeDetachDeclarationsV2 ? secureConsoleOwnedTaskTabV2State : "DECLARATION_INVALID",
});
```

Each detachment cell requires declaration/precondition `true`, its mutually
exclusive consumed tuple, detach `1/1`, browser calls `0`, binding null,
eligibility false, exact state, complete fixed terminal, and completed tool
status. A precondition failure, second/opposite cell, repeated invocation,
timeout, missing/truncated output, or uncertain completion spends that
disposition without retry or fallback; if mutation may have occurred, alias
state is `NOT_PROVEN` and the other cell is forbidden. Neither cell proves tab
closure. The pre-Create terminal explicitly
classifies the tab retained/untouched; the post-native-close terminal records
only the user's reported native action and JS alias detachment. No second get,
list, reacquisition, alternate handle, agent close, or metadata read is
permitted.

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

The retained parent next executes this complete guarded launch wrapper exactly
once. It extracts the unchanged `655`-byte launch fence and unchanged
`2779`-byte final fence, pins both, and dot-sources the launch once. It also
preloads the exact failure-disposition fence below before any start-capable
operation. No exception text is emitted.

```powershell
$scopeOwnerStartAttempted = 0
$scopeOwnerStartFulfilled = 0
$scopeOwnerHandleRetained = $false
$scopeOwnerWaitAttempted = 0
$scopeOwnerWaitFulfilled = 0
$scopeOwnerFileCleanup = 0
$scopeOwnerRootCleanup = 0
$scopeProxyCleanup = 0
$scopeProxyChildStartAttempted = 0
$scopeProxyChildStartFulfilled = 0
$scopeProxyChildWaitAttempted = 0
$scopeProxyChildWaitFulfilled = 0
$scopeProxyChildTerminationAttempted = 0
$scopeProxyChildTerminationFulfilled = 0
$scopeProxyChildExitProofAttempted = 0
$scopeProxyChildExitProofFulfilled = 0
$scopeProxyChildDrainAttempted = 0
$scopeProxyChildDrainFulfilled = 0
$scopeProxyChildDisposeAttempted = 0
$scopeProxyChildDisposeFulfilled = 0
$scopeProxyChildResidual = 'NONE'
$scopeProxyCleanupProcess = $null
$scopeProxyCleanupOutTask = $null
$scopeProxyCleanupErrTask = $null
$scopeOwnerResidual = 'NONE'
$ownerTerminationAttempted = 0
$ownerTerminationFulfilled = 0
$ownerExitProofAttempted = 0
$ownerExitProofFulfilled = 0
$owner = $null
$expectedOwnerPid = $null
$ownerClock = $null

function Invoke-ExactScopeProxyCleanup {
    $remote = @'
set -eu
id="$(sudo docker inspect -f '{{.Id}}' team-api-proxy)"
printf '%s' "$id" | grep -Eq '^[0-9a-f]{64}$'
test "$(sudo docker inspect -f '{{.State.Status}}' team-api-proxy)" = running
test "$(sudo docker inspect -f '{{.Image}}' team-api-proxy)" = sha256:5f5c8640aae01df9654968d946d8f1a56c497f1dd5c5cda4cf95ab7c14d58648
test "$(sudo docker inspect -f '{{json .HostConfig.PortBindings}}' team-api-proxy)" = '{}'
test "$(sudo docker network inspect omniroute-internal --format '{{len .Containers}}')" = 3
! sudo ss -lntH | grep -Eq '(^|:)20130([[:space:]]|$)'
sudo docker rm -f team-api-proxy >/dev/null
test -z "$(sudo docker ps -aq -f name='^/team-api-proxy$')"
test "$(sudo docker network inspect omniroute-internal --format '{{len .Containers}}')" = 2
! sudo ss -lntH | grep -Eq '(^|:)20130([[:space:]]|$)'
printf 'EXACT_PROXY_CLEANUP=PASS\n'
'@
    $startInfo = [Diagnostics.ProcessStartInfo]::new()
    $startInfo.FileName = 'C:\Windows\System32\OpenSSH\ssh.exe'
    $startInfo.UseShellExecute = $false
    $startInfo.RedirectStandardOutput = $true
    $startInfo.RedirectStandardError = $true
    foreach ($arg in @('-i','C:\Users\chatc\.ssh\codex-prox01-vms-ed25519','-o','BatchMode=yes','-o','ConnectTimeout=10','-o','ServerAliveInterval=5','-o','ServerAliveCountMax=3','belladmin@192.168.1.68',$remote)) {
        $null = $startInfo.ArgumentList.Add($arg)
    }
    $script:scopeProxyCleanupProcess = [Diagnostics.Process]::new()
    $script:scopeProxyCleanupProcess.StartInfo = $startInfo
    $script:scopeProxyChildStartAttempted++
    try { $started = $script:scopeProxyCleanupProcess.Start() }
    catch {
        $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_START_UNCERTAIN'
        throw 'SCOPE_PROXY_CLEANUP_START_UNCERTAIN'
    }
    if (-not $started) {
        $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_START_FAILED'
        $script:scopeProxyChildDisposeAttempted++
        try { $script:scopeProxyCleanupProcess.Dispose() }
        catch {
            $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_START_FAILED_DISPOSE_NOT_PROVEN'
            throw 'SCOPE_PROXY_CLEANUP_START_FAILED_DISPOSE_NOT_PROVEN'
        }
        $script:scopeProxyChildDisposeFulfilled++
        $script:scopeProxyCleanupProcess = $null
        throw 'SCOPE_PROXY_CLEANUP_START_FAILED'
    }
    $script:scopeProxyChildStartFulfilled++
    try {
        $script:scopeProxyCleanupOutTask = $script:scopeProxyCleanupProcess.StandardOutput.ReadToEndAsync()
        $script:scopeProxyCleanupErrTask = $script:scopeProxyCleanupProcess.StandardError.ReadToEndAsync()
    }
    catch {
        $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_STREAM_TASK_START_NOT_PROVEN'
        throw 'SCOPE_PROXY_CLEANUP_STREAM_TASK_START_NOT_PROVEN'
    }
    $script:scopeProxyChildWaitAttempted++
    try { $scopeProxyChildExited = $script:scopeProxyCleanupProcess.WaitForExit(60000) }
    catch {
        $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_WAIT_NOT_PROVEN'
        throw 'SCOPE_PROXY_CLEANUP_WAIT_NOT_PROVEN'
    }
    $scopeProxyChildTimedOut = $false
    if (-not $scopeProxyChildExited) {
        $script:scopeProxyChildTerminationAttempted++
        try {
            $script:scopeProxyCleanupProcess.Kill()
            $script:scopeProxyChildTerminationFulfilled++
        }
        catch {
            $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_TERMINATION_NOT_PROVEN'
            throw 'SCOPE_PROXY_CLEANUP_TERMINATION_NOT_PROVEN'
        }
        $script:scopeProxyChildExitProofAttempted++
        try { $scopeProxyChildExitProven = $script:scopeProxyCleanupProcess.WaitForExit(10000) }
        catch {
            $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_EXIT_PROOF_NOT_PROVEN'
            throw 'SCOPE_PROXY_CLEANUP_EXIT_PROOF_NOT_PROVEN'
        }
        if (-not $scopeProxyChildExitProven) {
            $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_EXIT_NOT_PROVEN'
            throw 'SCOPE_PROXY_CLEANUP_TIMEOUT_EXIT_NOT_PROVEN'
        }
        $script:scopeProxyChildExitProofFulfilled++
        $scopeProxyChildTimedOut = $true
    }
    else { $script:scopeProxyChildWaitFulfilled++ }
    $script:scopeProxyChildDrainAttempted++
    try { $scopeProxyChildDrained = [Threading.Tasks.Task]::WaitAll(@($script:scopeProxyCleanupOutTask,$script:scopeProxyCleanupErrTask),5000) }
    catch {
        $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_DRAIN_WAIT_NOT_PROVEN'
        throw 'SCOPE_PROXY_CLEANUP_DRAIN_WAIT_NOT_PROVEN'
    }
    if (-not $scopeProxyChildDrained) {
        $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_DRAIN_TIMEOUT'
        throw 'SCOPE_PROXY_CLEANUP_DRAIN_TIMEOUT'
    }
    try {
        $scopeProxyChildStdout = $script:scopeProxyCleanupOutTask.Result
        $scopeProxyChildStderr = $script:scopeProxyCleanupErrTask.Result
        $scopeProxyChildExitCode = $script:scopeProxyCleanupProcess.ExitCode
    }
    catch {
        $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_DRAIN_RESULT_NOT_PROVEN'
        throw 'SCOPE_PROXY_CLEANUP_DRAIN_RESULT_NOT_PROVEN'
    }
    $script:scopeProxyChildDrainFulfilled++
    if ($scopeProxyChildTimedOut) {
        $scopeProxyChildTerminalResidual = 'PROXY_CLEANUP_CHILD_TIMEOUT_EXIT_PROVEN'
    }
    elseif ($scopeProxyChildExitCode -ne 0 -or $scopeProxyChildStdout.Trim() -ne 'EXACT_PROXY_CLEANUP=PASS' -or -not [string]::IsNullOrWhiteSpace($scopeProxyChildStderr)) {
        $scopeProxyChildTerminalResidual = 'PROXY_CLEANUP_CHILD_TERMINAL_NOT_PROVEN'
    }
    else { $scopeProxyChildTerminalResidual = 'NONE' }
    $script:scopeProxyChildResidual = $scopeProxyChildTerminalResidual
    $script:scopeProxyChildDisposeAttempted++
    try { $script:scopeProxyCleanupProcess.Dispose() }
    catch {
        if ($scopeProxyChildTerminalResidual -eq 'NONE') {
            $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_DISPOSE_NOT_PROVEN_AFTER_PASS'
        }
        elseif ($scopeProxyChildTimedOut) {
            $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_DISPOSE_NOT_PROVEN_AFTER_TIMEOUT_EXIT'
        }
        else {
            $script:scopeProxyChildResidual = 'PROXY_CLEANUP_CHILD_DISPOSE_NOT_PROVEN_AFTER_TERMINAL_FAILURE'
        }
        throw 'SCOPE_PROXY_CLEANUP_DISPOSE_NOT_PROVEN'
    }
    $script:scopeProxyChildDisposeFulfilled++
    $script:scopeProxyCleanupProcess = $null
    $script:scopeProxyCleanupOutTask = $null
    $script:scopeProxyCleanupErrTask = $null
    if ($scopeProxyChildTerminalResidual -eq 'PROXY_CLEANUP_CHILD_TIMEOUT_EXIT_PROVEN') {
        throw 'SCOPE_PROXY_CLEANUP_TIMEOUT_EXIT_PROVEN'
    }
    if ($scopeProxyChildTerminalResidual -ne 'NONE') { throw 'SCOPE_PROXY_CLEANUP_NOT_PROVEN' }
}

function Remove-ExactScopePreparedFiles {
    $tempRoot = [IO.Path]::GetFullPath([IO.Path]::GetTempPath()).TrimEnd('\')
    $root = [IO.Path]::GetFullPath($transferRoot)
    if ([IO.Path]::GetDirectoryName($root).TrimEnd('\') -cne $tempRoot) { throw 'SCOPE_TEMP_ROOT_GUARD_FAILED' }
    foreach ($path in @($ownerScriptPath,$r5ScriptPath,$safeLogPath)) {
        if ([IO.Path]::GetDirectoryName([IO.Path]::GetFullPath($path)) -cne $root) { throw 'SCOPE_TEMP_CHILD_GUARD_FAILED' }
    }
    if (Test-Path -LiteralPath $safeLogPath) { throw 'SCOPE_SAFE_LOG_UNEXPECTED' }
    if (@(Get-ChildItem -LiteralPath $root -Force).Count -ne 2) { throw 'SCOPE_PREPARED_FILE_COUNT_DRIFT' }
    if ((Get-FileHash -Algorithm SHA256 -LiteralPath $ownerScriptPath).Hash -cne '347FCD60A41DF780CE4A94E4FC14C87E5059112068C689EF73636ABC5B0F0B6C' -or
        (Get-FileHash -Algorithm SHA256 -LiteralPath $r5ScriptPath).Hash -cne 'DB75253CD851075C1D612A54EC4B02C8016C034C8BC192A3DB9D02DB9890AD41') {
        throw 'SCOPE_PREPARED_HASH_DRIFT'
    }
    Remove-Item -LiteralPath $ownerScriptPath -Force
    Remove-Item -LiteralPath $r5ScriptPath -Force
    if (@(Get-ChildItem -LiteralPath $root -Force).Count -ne 0) { throw 'SCOPE_TEMP_NOT_EMPTY' }
    Remove-Item -LiteralPath $root -Force
}

try {
    $launchTailForScope = $briefRawForScope.Substring($briefRawForScope.IndexOf('## Launch and transfer sequence'))
    $launchMatchForScope = [regex]::Match($launchTailForScope, '(?ms)^```powershell\n(?<code>.*?)^```$')
    if (-not $launchMatchForScope.Success) { throw 'LAUNCH_SCOPE_EXTRACTION_FAILED' }
    $launchBytesForScope = [Text.UTF8Encoding]::new($false).GetBytes($launchMatchForScope.Groups['code'].Value)
    $launchHashForScope = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($launchBytesForScope))
    if ($launchBytesForScope.Length -ne 655 -or $launchHashForScope -cne '995185FA04790564F4CDCA967E87CAB82EB97731D8458EF85CEF942D4606A293') { throw 'LAUNCH_SCOPE_BYTE_PIN_FAILED' }

    $finalMatchesForScope = [regex]::Matches($launchTailForScope, '(?ms)^```powershell\n(?<code>.*?)^```$')
    if ($finalMatchesForScope.Count -ne 2) { throw 'FINAL_SCOPE_EXTRACTION_COUNT_FAILED' }
    $ownerFinalCodeForScope = $finalMatchesForScope[1].Groups['code'].Value
    $ownerFinalBytesForScope = [Text.UTF8Encoding]::new($false).GetBytes($ownerFinalCodeForScope)
    $ownerFinalHashForScope = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($ownerFinalBytesForScope))
    if ($ownerFinalBytesForScope.Length -ne 2779 -or $ownerFinalHashForScope -cne '9316DE2F7C84A89947E57C8563E9381E97D7C52F0DFFE56CA7E4DE616DD8F637') { throw 'FINAL_SCOPE_BYTE_PIN_FAILED' }

    $replacementPathForScope = '.superpowers\sdd\2026-08-30-omniroute-standard-team-api\task-2-secure-console-transfer-scope-replacement-brief.md'
    $replacementRawForScope = [IO.File]::ReadAllText((Resolve-Path -LiteralPath $replacementPathForScope),[Text.UTF8Encoding]::new($false,$true))
    $dispositionTailForScope = $replacementRawForScope.Substring($replacementRawForScope.IndexOf('### Exact post-launch pre-accept failure disposition'))
    $dispositionMatchForScope = [regex]::Match($dispositionTailForScope, '(?ms)^```powershell\n(?<code>.*?)^```$')
    if (-not $dispositionMatchForScope.Success) { throw 'DISPOSITION_SCOPE_EXTRACTION_FAILED' }
    $ownerPreacceptDispositionCodeForScope = $dispositionMatchForScope.Groups['code'].Value
    $dispositionBytesForScope = [Text.UTF8Encoding]::new($false).GetBytes($ownerPreacceptDispositionCodeForScope)
    $dispositionHashForScope = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($dispositionBytesForScope))
    if ($dispositionBytesForScope.Length -ne 3308 -or $dispositionHashForScope -cne 'B8087F2CB77A695C1B6DD145DDD3D39D48F8AABEBBA00863BEA0610C8BE6518E') { throw 'DISPOSITION_SCOPE_BYTE_PIN_FAILED' }

    $scopeOwnerStartAttempted++
    . ([scriptblock]::Create($launchMatchForScope.Groups['code'].Value))
    if ($null -eq $owner -or $owner.Id -ne $expectedOwnerPid -or $null -eq $ownerClock) { throw 'LAUNCH_SCOPE_HANDLE_MISSING' }
    $scopeOwnerStartFulfilled++
    $scopeOwnerHandleRetained = $true
    [Console]::Out.WriteLine(('EXACT_RETAINED_SCOPE_OWNER_LAUNCHED=PASS START={0}/{1} HANDLE={2}' -f $scopeOwnerStartAttempted,$scopeOwnerStartFulfilled,$scopeOwnerHandleRetained.ToString().ToUpperInvariant()))
}
catch {
    if ($scopeOwnerStartAttempted -eq 0) {
        try {
            Remove-ExactScopePreparedFiles
            $scopeOwnerFileCleanup = 1
            $scopeOwnerRootCleanup = 1
            Invoke-ExactScopeProxyCleanup
            $scopeProxyCleanup = 1
            $scopeOwnerResidual = 'PRESTART_CLEANUP_PASS'
        }
        catch { $scopeOwnerResidual = 'PRESTART_CLEANUP_NOT_PROVEN' }
        [Console]::Out.WriteLine(('EXACT_RETAINED_SCOPE_OWNER_LAUNCH=FAIL START={0}/{1} HANDLE=FALSE FILE_CLEANUP={2} ROOT_CLEANUP={3} PROXY_CLEANUP={4} RESIDUAL={5} PROXY_CHILD_START={6}/{7} WAIT={8}/{9} TERMINATION={10}/{11} EXIT_PROOF={12}/{13} DRAIN={14}/{15} DISPOSE={16}/{17} CHILD_RESIDUAL={18}' -f $scopeOwnerStartAttempted,$scopeOwnerStartFulfilled,$scopeOwnerFileCleanup,$scopeOwnerRootCleanup,$scopeProxyCleanup,$scopeOwnerResidual,$scopeProxyChildStartAttempted,$scopeProxyChildStartFulfilled,$scopeProxyChildWaitAttempted,$scopeProxyChildWaitFulfilled,$scopeProxyChildTerminationAttempted,$scopeProxyChildTerminationFulfilled,$scopeProxyChildExitProofAttempted,$scopeProxyChildExitProofFulfilled,$scopeProxyChildDrainAttempted,$scopeProxyChildDrainFulfilled,$scopeProxyChildDisposeAttempted,$scopeProxyChildDisposeFulfilled,$scopeProxyChildResidual))
        throw 'RETAINED_SCOPE_PRESTART_FAILURE_NO_RETRY'
    }
    if ($owner -is [Diagnostics.Process] -and $null -ne $ownerClock) {
        $scopeOwnerHandleRetained = $true
        if ($null -eq $expectedOwnerPid) { $expectedOwnerPid = $owner.Id }
        . ([scriptblock]::Create($ownerPreacceptDispositionCodeForScope))
        throw 'RETAINED_SCOPE_POSTSTART_FAILURE_DISPOSED_NO_RETRY'
    }
    $scopeOwnerResidual = 'START_UNCERTAIN_NO_HANDLE'
    [Console]::Out.WriteLine(('EXACT_RETAINED_SCOPE_OWNER_LAUNCH=FAIL START={0}/{1} HANDLE=FALSE WAIT=0/0 TERMINATION=0/0 EXIT_PROOF=0/0 FILE_CLEANUP=0 ROOT_CLEANUP=0 PROXY_CLEANUP=0 RESIDUAL={2} PROXY_CHILD_START=0/0 WAIT=0/0 TERMINATION=0/0 EXIT_PROOF=0/0 DRAIN=0/0 DISPOSE=0/0 CHILD_RESIDUAL=NONE' -f $scopeOwnerStartAttempted,$scopeOwnerStartFulfilled,$scopeOwnerResidual))
    throw 'RETAINED_SCOPE_START_UNCERTAIN_NO_HANDLE_NO_RETRY'
}
```

### Exact post-launch pre-accept failure disposition

This fence is pre-extracted and pinned before launch. On every later readiness
or coordination failure before final Create for which the exact owner handle is
retained, dot-source it exactly once in the same parent. It uses only the one
inherited final remaining-budget wait/termination/exit-proof block and then the
guarded proxy cleanup function above.

```powershell
$scopeOwnerWaitAttempted++
try {
    . ([scriptblock]::Create($ownerFinalCodeForScope))
    $scopeOwnerWaitFulfilled++
    if ((Test-Path -LiteralPath $ownerScriptPath -PathType Leaf) -or (Test-Path -LiteralPath $r5ScriptPath -PathType Leaf) -or (Test-Path -LiteralPath $safeLogPath -PathType Leaf)) { throw 'SCOPE_OWNER_FILES_REMAIN' }
    $scopeOwnerFileCleanup = 1
    if (Test-Path -LiteralPath $transferRoot) { throw 'SCOPE_OWNER_ROOT_REMAINS' }
    $scopeOwnerRootCleanup = 1
    Invoke-ExactScopeProxyCleanup
    $scopeProxyCleanup = 1
    $scopeOwnerResidual = 'NONE'
    [Console]::Out.WriteLine(('EXACT_PREACCEPT_OWNER_DISPOSITION=PASS START={0}/{1} HANDLE={2} WAIT={3}/{4} TERMINATION={5}/{6} EXIT_PROOF={7}/{8} FILE_CLEANUP={9} ROOT_CLEANUP={10} PROXY_CLEANUP={11} RESIDUAL={12} PROXY_CHILD_START={13}/{14} WAIT={15}/{16} TERMINATION={17}/{18} EXIT_PROOF={19}/{20} DRAIN={21}/{22} DISPOSE={23}/{24} CHILD_RESIDUAL={25}' -f $scopeOwnerStartAttempted,$scopeOwnerStartFulfilled,$scopeOwnerHandleRetained.ToString().ToUpperInvariant(),$scopeOwnerWaitAttempted,$scopeOwnerWaitFulfilled,$ownerTerminationAttempted,$ownerTerminationFulfilled,$ownerExitProofAttempted,$ownerExitProofFulfilled,$scopeOwnerFileCleanup,$scopeOwnerRootCleanup,$scopeProxyCleanup,$scopeOwnerResidual,$scopeProxyChildStartAttempted,$scopeProxyChildStartFulfilled,$scopeProxyChildWaitAttempted,$scopeProxyChildWaitFulfilled,$scopeProxyChildTerminationAttempted,$scopeProxyChildTerminationFulfilled,$scopeProxyChildExitProofAttempted,$scopeProxyChildExitProofFulfilled,$scopeProxyChildDrainAttempted,$scopeProxyChildDrainFulfilled,$scopeProxyChildDisposeAttempted,$scopeProxyChildDisposeFulfilled,$scopeProxyChildResidual))
}
catch {
    if ($null -ne $owner) {
        try {
            if (-not $owner.HasExited) { $scopeOwnerResidual = 'EXACT_OWNER_EXIT_NOT_PROVEN' }
            else { $scopeOwnerResidual = 'POSTEXIT_CLEANUP_NOT_PROVEN' }
        }
        catch { $scopeOwnerResidual = 'EXACT_OWNER_STATE_NOT_PROVEN' }
    }
    elseif ($scopeOwnerResidual -eq 'NONE') { $scopeOwnerResidual = 'POSTEXIT_CLEANUP_NOT_PROVEN' }
    [Console]::Out.WriteLine(('EXACT_PREACCEPT_OWNER_DISPOSITION=FAIL START={0}/{1} HANDLE={2} WAIT={3}/{4} TERMINATION={5}/{6} EXIT_PROOF={7}/{8} FILE_CLEANUP={9} ROOT_CLEANUP={10} PROXY_CLEANUP={11} RESIDUAL={12} PROXY_CHILD_START={13}/{14} WAIT={15}/{16} TERMINATION={17}/{18} EXIT_PROOF={19}/{20} DRAIN={21}/{22} DISPOSE={23}/{24} CHILD_RESIDUAL={25}' -f $scopeOwnerStartAttempted,$scopeOwnerStartFulfilled,$scopeOwnerHandleRetained.ToString().ToUpperInvariant(),$scopeOwnerWaitAttempted,$scopeOwnerWaitFulfilled,$ownerTerminationAttempted,$ownerTerminationFulfilled,$ownerExitProofAttempted,$ownerExitProofFulfilled,$scopeOwnerFileCleanup,$scopeOwnerRootCleanup,$scopeProxyCleanup,$scopeOwnerResidual,$scopeProxyChildStartAttempted,$scopeProxyChildStartFulfilled,$scopeProxyChildWaitAttempted,$scopeProxyChildWaitFulfilled,$scopeProxyChildTerminationAttempted,$scopeProxyChildTerminationFulfilled,$scopeProxyChildExitProofAttempted,$scopeProxyChildExitProofFulfilled,$scopeProxyChildDrainAttempted,$scopeProxyChildDrainFulfilled,$scopeProxyChildDisposeAttempted,$scopeProxyChildDisposeFulfilled,$scopeProxyChildResidual))
    throw 'RETAINED_SCOPE_PREACCEPT_DISPOSITION_NOT_PROVEN_NO_RETRY'
}
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

The guarded proxy-cleanup SSH child separately records start, wait,
termination, exit-proof, stream-drain, and dispose attempted/fulfilled counters,
retains its exact process plus output/error tasks until proven drain and safe
disposal, and reports `PROXY_CLEANUP_CHILD_RESIDUAL`. Timeout permits one
exact-handle kill and one checked exit-proof wait only. Every proven exit,
including timeout/kill, receives the single bounded drain attempt and one safe
dispose attempt. Wait, termination, exit-proof, drain-wait, drain-result, and
disposal exceptions set distinct non-`NONE` residuals before failure.
Start-uncertain, termination-not-proven, exit-not-proven, drain-not-proven, or
dispose-not-proven retains the exact available handle/tasks and stops. A
timeout-exit-proven or terminal-mismatch
path disposes and clears bindings only after drain and disposal are proven,
then fails with its fixed residual. No second wait, kill, drain, dispose,
cleanup invocation, lookup, retry, or fallback is permitted.

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
