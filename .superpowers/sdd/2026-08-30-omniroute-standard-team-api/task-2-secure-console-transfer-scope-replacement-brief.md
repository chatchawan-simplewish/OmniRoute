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
  `029cf42275d2d61b6f69f38b7d94a1478702f135`.

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
2. use only the retained `secureConsoleTaskTabV1`; do not reconnect, reacquire,
   list tabs, serialize unrelated page data, or change Chrome profile;
3. perform exactly one new credential-free clipboard clear and exactly one
   shape-only read, requiring empty `TRUE`; this replacement-specific count does
   not reuse or reinterpret the spent gate's clear/read;
4. prove `team-api-proxy` absent, network members `2`, listener `20130` absent,
   and no exact prepared temp directory or owner process from the incident;
5. stop before live action on any discrepancy.

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

Before masked acceptance, remove only the exact new proxy after fixed-attribute
guards, prove proxy absent/network members `2`/listener absent, and remove only
the exact direct-child hash-pinned temp files and now-empty root. After masked
acceptance, use only the inherited owner's bounded revocation-required path and
cleanup. If final Create occurred without a usable retained token, separately
confirm exact-row deletion; exact-token HTTP `401` remains `NOT PROVEN`.

Success remains only the inherited exact terminal tuple ending
`OWNER_RESULT=EXACT_CORRECTION_PASS_TOKEN_REVOKED` plus external owner exit,
script/safe-log/temp cleanup, refreshed Cloudflare token counts `0/0`, invalid
HTTP `401`, and independently reviewed redacted evidence.

## Review gate

Independent Sol High review must pin this brief's exact commit, byte count, and
SHA-256; validate both fences parse; confirm dot-sourcing is the sole semantic
change; confirm no old-gate retry or expanded authority; and return exact
`PASS` before execution. Any `FAIL`, `NOT PROVEN`, ambiguity, or drift blocks
execution.
