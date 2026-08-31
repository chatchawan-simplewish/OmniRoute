# Task 2 secure-console credential transfer design

Status: revised replacement contract; review only; no live execution authorized

## Decision and hard boundary

Use one fixed, visible PowerShell 7 owner process with masked console input. The
Cloudflare token must never pass through an agent tool, browser inspection,
file, command line, report, Git artifact, or any process except the fixed owner
and the one exact-hash synchronous R5 child permitted below.

The native Cloudflare Copy control is retained only because a practical
no-clipboard transfer from the generated-token page is not established. This
fallback is blocked unless read-only, OS-version-specific evidence proves both
Windows clipboard history and Windows OS/device clipboard sync disabled before
token creation. An ambiguous, missing, policy-overridden, or enabled state is a
pre-accept FAIL; it permits no token creation. Clearing the current clipboard
does not erase or prove erasure of clipboard history.

The rejected Chrome-native data-page canary remains retired as credential
evidence. A corrected non-secret preflight has only the bounded conclusion
defined below. This design and every later record set
`authorizes_live_execution=false`.

## Authority boundaries

- This design and its review are credential-free and may proceed unattended.
- A fresh independent Sol High PASS is required before any process, browser,
  clipboard, Cloudflare, VM1205, proxy, Rulesets, Tunnel, DNS, key, model,
  request, or evidence action.
- Preflight execution requires its own exact reviewed brief and authority.
- Token creation plus one masked submission requires one later explicit
  action-time confirmation naming both actions. It does not authorize
  revocation, deletion, retry, permission expansion, or another token.
- Exact-row revocation requires a separate action-time confirmation after the
  token is accepted. It may authorize only one exact-row revocation, one
  exact-token invalidity check, and one refreshed exact-row count.
- The one-shot gate and every consuming action remain in one Sol High owner
  task. No delegation, owner replacement, session handoff, inferred authority,
  retry, fallback, alternate bridge, or verdict relaxation is permitted.

## Corrected non-secret transport preflight

The preflight script and live brief must pin all of these values before it may
run:

1. Generate a fresh 128-bit non-secret challenge at runtime with
   `[Security.Cryptography.RandomNumberGenerator]::Fill()`; static or reused
   bytes are forbidden. Encode it only after generation.
2. Encode the exact credential-free script as strict UTF-8, no BOM, LF-only,
   one trailing LF. Place it under a newly created validated directory below
   `[IO.Path]::GetFullPath([IO.Path]::GetTempPath())`. Record exact root, path,
   size, SHA-256, and deletion guard. The resolved script path must be a direct
   child of the recorded root, use the reviewed filename, and match the
   reviewed hash immediately before deletion.
3. Retain the exact spawned process handle and expected PID. The script emits
   `OWNER_PID=<pid>` and `OWNER_READY=PASS`; reported PID must equal the retained
   handle PID before the page opens.
4. The same process clears the current Windows clipboard with terminating
   error behavior, performs one shape-only empty-baseline read, and then emits
   the fresh non-secret challenge. One local page holds that challenge in one
   readonly input. Focus once, then issue one `Control+A` and one `Control+C`.
   No browser clipboard API call, coordinate action, screenshot, DOM snapshot,
   or page-content extraction is allowed.
5. Accept exactly one control line and apply this state matrix:

| Terminal state | Comparison reads | Required classification |
| --- | ---: | --- |
| `COPY_DONE` | exactly `1` | internal exact compare; PASS only on equality |
| `ABORT` | `0` | `PREFLIGHT=ABORTED` |
| EOF | `0` | `PREFLIGHT=EOF` |
| monotonic timeout | `0` | `PREFLIGHT=TIMEOUT` |

6. Every state enters one common `finally`: clear the current OS clipboard
   once, perform one shape-only post-clear empty check, close only the exact
   page, verify the deletion guard and delete only the exact-hash script, emit
   cleanup labels, and exit. The coordinator then uses the retained handle to
   prove exit and proves exact-script absence. It never kills an unverified PID.

Preflight maxima are: processes `1`; pages `1`; transfer attempts `1`;
baseline/comparison/post-clear reads `1 / 0..1 / 1`; cleanup writes `2` total
(baseline clear and final clear); comparison reads by state `1 / 0 / 0 / 0`;
browser clipboard API calls `0`; retries `0`. The preflight process must exit
before any credential-owner process starts.

A PASS proves only that the fresh non-secret challenge crossed the observed
local Chrome/AnyDesk/Windows path at that time. It neither proves Cloudflare
copy-control semantics nor authorizes token creation.

## Fixed credential owner and temporary script

Before creation, revalidate the clean evidence worktree at
`80adaa7d5d63d1d2c7bfa63b236c6bee93b3b1d8`, all immutable contract hashes,
the exact target-resource absence facts, exact target-token name and row counts
`0 / 0`, preflight-process exit, and exact preflight-script absence.

The credential live brief must contain the complete credential-free owner
script and pin its exact UTF-8/LF/no-BOM bytes, one trailing LF, size, SHA-256,
validated temporary root, direct-child path, and deletion guard. Retain the
spawn handle and expected PID. The script emits only fixed labels, including
`OWNER_READY=PASS`, `OWNER_PID=<pid>`, and `SECRET_PROMPT_READY=PASS`; the
reported PID must equal the retained handle PID before creation is enabled.

Credential processes are counted separately from preflight: preflight process
`0..1` and later credential-owner process exactly `1`. They never overlap.

## Executable bounded masked-input primitive

`Read-Host` is forbidden. The owner script must implement exactly one
same-process prompt using a monotonic `[Diagnostics.Stopwatch]` deadline and
`[Console]::KeyAvailable` / `[Console]::ReadKey($true)`. The exact live brief
pins the numeric timeout. Its input core is structurally equivalent to this
single-threaded primitive and may differ only in reviewed label/error plumbing:

```powershell
$secret = [Security.SecureString]::new()
$clock = [Diagnostics.Stopwatch]::StartNew()
$accepted = $false
$cancelled = $false
$key = $null
$keyChar = $null
$ctrl = $null
while ($clock.Elapsed -lt $secretDeadline) {
    if (-not [Console]::KeyAvailable) {
        [Threading.Thread]::Sleep(25)
        continue
    }
    try {
        $key = [Console]::ReadKey($true)
        $keyChar = $key.KeyChar
        $ctrl = ($key.Modifiers -band [ConsoleModifiers]::Control) -ne 0
        if ($key.Key -eq [ConsoleKey]::Escape -or
            ($ctrl -and $key.Key -eq [ConsoleKey]::C)) {
            $cancelled = $true
            break
        }
        if ($key.Key -eq [ConsoleKey]::Enter) {
            $accepted = $secret.Length -gt 0
            break
        }
        if ($key.Key -eq [ConsoleKey]::Backspace) {
            if ($secret.Length -gt 0) { $secret.RemoveAt($secret.Length - 1) }
            continue
        }
        if (-not [char]::IsControl($keyChar)) {
            $secret.AppendChar($keyChar)
        }
    } finally {
        $keyChar = $null
        $key = $null
        $ctrl = $null
    }
}
$clock.Stop()
if ($cancelled) { throw 'MASKED_INPUT_CANCELLED' }
if (-not $accepted) { throw 'MASKED_INPUT_EMPTY_OR_TIMEOUT' }
$secret.MakeReadOnly()
```

The loop handles printable characters, Enter, Backspace, Escape, and Ctrl+C.
It emits neither input nor length, starts no job/thread/child, and has no second
prompt. Timeout is proven before live execution with no credential, no HTTP
request, no clipboard action, no R5 child, and the same final cleanup labels.
All exits from the full script converge on its one outer `finally`.

## Clipboard fallback and page closure

Immediately before creation, the reviewed brief must perform read-only proof,
using a mechanism validated for the exact Windows build, that clipboard history
is disabled and OS/device clipboard sync is disabled. It records only setting
names, effective disabled results, proof method, timestamp, and OS build; no
clipboard content. User assertion alone is insufficient.

After action-time confirmation, the user completes exactly one final Create,
activates only the page's native Copy control, switches to the visible owner,
pastes once into the masked prompt, and submits once. No agent browser call,
snapshot, screenshot, DOM/page-content read, browser clipboard API call, or
keystroke injection is permitted after final Create.

After the masked value is accepted, the same owner process performs exactly one
cleanup-only current-clipboard clear and exactly one shape-only empty check,
then the exact token-bearing page is closed before any agent browser call.
These actions are not transfer evidence and do not claim to erase history.

Credential-stage clipboard counters are: user native Copy `1`; user masked
Paste `1`; owner cleanup-only OS writes `1`; owner cleanup-only shape reads `1`;
agent clipboard reads/writes `0 / 0`; browser clipboard API reads/writes `0 / 0`.
If either disabled-setting proof or post-submit current-clipboard cleanup fails,
the gate stops before verification/proxy/R5 and enters post-accept revocation.

## Freshness and binding

Use one new unique token name fixed in the reviewed live brief. Acceptance
requires all of the following without serializing the page or value:

- refreshed exact target-token name count `0` and exact row count `0` before
  the one final Create;
- exactly one final Create action and exactly one resulting target row;
- fixed owner PID equal to the retained process PID;
- exactly one masked submission after `SECRET_PROMPT_READY=PASS`;
- same-process active-token verification with the exact reviewed response
  shape and status;
- no pre-existing credential source, token environment value, or token file.

The token becomes **accepted** only after all acceptance checks pass. Before
acceptance, any failure uses immediate full cleanup and process exit. If the
row was created but the value reached the owner, treat it as post-accept for
revocation safety even if active verification failed.

## Credential holders, R5, and plaintext lifetime

Authorized credential holders are exactly:

1. the fixed owner process; and
2. only while running, the fresh synchronous `pwsh.exe -NoLogo -NoProfile
   -NonInteractive -File <exact-path>` R5 child whose LF-only UTF-8 source is
   exactly `10,890` bytes and SHA-256
   `DB75253CD851075C1D612A54EC4B02C8016C034C8BC192A3DB9D02DB9890AD41`.

The R5 child's private environment entries are exactly
`CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ZONE_ID`. They are supplied through the
reviewed `ProcessStartInfo.Environment` immediately before `Start()`, never in
arguments or the parent's process environment. Every other child starts with
both names removed. No child may start concurrently with R5, R5 runs
synchronously without yield or interruption, the exact reviewed R5 script must
not spawn another child, and the retained R5 handle/PID must exit before owner
cleanup continues. R5 child count is at most `1`.

The live brief must enumerate and name every plaintext-bearing location:

- `$key`, the managed `ConsoleKeyInfo` value returned by `ReadKey($true)`, and
  its plaintext-bearing `KeyChar` member;
- `$keyChar` and every other managed character variable derived from
  `ConsoleKeyInfo.KeyChar` by the final implementation;
- every additional input-host or console buffer introduced by the exact live
  implementation, with its lifetime and cleanup limit;
- the unmanaged BSTR returned from `SecureStringToBSTR`;
- the shortest-lived managed token string returned by `PtrToStringBSTR`;
- the managed Authorization header value and header collection;
- any managed zone-ID string needed by the reviewed endpoint;
- the two R5 `ProcessStartInfo.Environment` entries above;
- any R5 child-local environment, header, response, and result references
  already present in the immutable exact-hash script.

Each `$key` object and derived character reference must live only for its
current loop iteration. Clear `$keyChar`, `$key`, and `$ctrl` in the
per-iteration `finally` immediately after handling, including `break` and
`continue`, and clear all three named references again in the full script's one
outer `finally`. The inner lifetime guard does not create a second terminal
cleanup path. The exact live-brief review must inventory any further
input-host buffer before approval.

Convert only immediately before the first authorized same-process request.
Keep no duplicate token variable. In the one outer `finally`, call
`ZeroFreeBSTR` once for a nonzero BSTR, dispose the `SecureString`, remove the
two environment entries from `ProcessStartInfo`, clear every named managed
reference/header/result, and prove R5-child and owner exit. Evidence may claim
only **named references cleared and owning processes exited**. It must not
claim managed-memory byte zeroization.

All other child processes, including credential-free proof/SSH helpers, must be
launched with both private environment names absent. No process or session
handoff is allowed.

## Two-phase cleanup and revocation hold

### Phase A: pre-accept failure

Before the value reaches the owner, EOF, cancel, timeout, empty input, PID
mismatch, browser ambiguity, or missing label immediately enters the one outer
`finally`: dispose/clear references, guard-delete only the exact owner script,
prove owner exit and script absence, record FAIL / NOT PROVEN, and stop. If a
row exists but no exact token reached the owner, request separate exact-row
revocation authority; invalid-token HTTP `401` remains NOT PROVEN.

### Phase B: post-accept success or failure

Once the exact token reaches the owner, every success or failure enters
`REVOCATION_REQUIRED` in that same process. No further proxy, proof, R5, POST,
DELETE, verification, browser, or child action is allowed except a previously
started synchronous R5 completing and the separately authorized revocation
sequence. The live brief pins one monotonic hold deadline and emits only:

- `REVOCATION_REQUIRED=PASS`;
- the non-secret exact reviewed row name;
- `REVOCATION_AUTHORITY=WAITING|GRANTED|DENIED|TIMEOUT`.

On separate exact-row authority, perform one revocation action, use the retained
exact token for exactly one invalid-token verification requiring HTTP `401`,
refresh and require exact name/row counts `0 / 0`, then enter final cleanup. Row
absence never substitutes for the exact-token `401`.

Denial or hold timeout performs no inferred revocation and no retry. It records
`CREDENTIAL_INCIDENT=ACTIVE_TOKEN_REVOCATION_NOT_PROVEN`, blocks every later
Task 2 action, and explicitly reports that the named row may remain active and
requires owner action. At the bounded local-residency deadline the process
clears its references and exits through the common final cleanup; this is
FAIL / NOT PROVEN, not successful disposition. A later user-performed row
removal may establish row count `0`, but invalid-token `401` remains NOT PROVEN
unless the exact retained token was used in the authorized sequence.

Final cleanup always includes the BSTR/reference rules above, guarded
exact-script deletion, R5-child exit proof if started, owner exit proof, and
exact-script absence. It performs the single allowed current-clipboard clear
and empty check only if masked input ended before that pair was attempted. If
the pair was attempted and failed, it is not retried; cleanup records the
credential incident and unresolved clipboard state.

## Structural counters

- Preflight processes/pages/attempts: at most `1 / 1 / 1`
- Credential-owner processes: exactly `1` when the credential gate starts
- Authorized credential holders: owner `1`; R5 child `0..1`; all others `0`
- Masked prompts/submissions: exactly `1 / 0..1`
- Agent-visible secret values and token-page inspection calls: `0 / 0`
- Credential native Copy/masked Paste: at most `1 / 1`
- Credential owner cleanup clipboard writes/shape reads: at most `1 / 1`
- Agent and browser-API credential clipboard reads/writes: `0 / 0`
- Token creations / active verifications: at most `1 / 1`
- Revocation actions / invalid-token checks / refreshed row checks: at most
  `1 / 1 / 1`, only under separate authority
- Proxy starts/proofs/restarts: at most `1 / 1 / 0`
- R5 children/Rulesets POSTs/attributable DELETEs: at most `1 / 1 / 1`
- Retries/fallbacks/alternate bridges/session handoffs: `0`

## Later additive evidence contract

Task 1 changes only this design and its implementation plan. It makes no
evidence mutation.

One later exact-path evidence commit may add only
`secure_console_transfer_v1`, with `schema_version=1`, alongside all existing
incident fields. It has separate `transport_preflight` and `credential_gate`
subobjects. Each subobject includes only:

- reviewed contract, brief, and script SHA-256 and byte size;
- bounded start/end timestamps;
- expected/observed retained PIDs and exit proof;
- exact counters, result, and cleanup labels;
- exact-page close, clipboard current-state cleanup, exact-script deletion,
  and external absence proof results;
- `authorizes_live_execution=false`.

`credential_gate` additionally records disabled clipboard-history/sync proof
results, acceptance status, R5 child exit, revocation authority/result,
exact-token invalidity status, and refreshed name/row counts. It contains no
secret, header, private identifier, page serialization, clipboard content,
keystroke, prompt, response body, or managed string.

The initial permitted evidence parent is exactly
`80adaa7d5d63d1d2c7bfa63b236c6bee93b3b1d8`, and the path is exactly
`artifacts/omniroute-live-integration/evidence/team-api-verification.json` in
the offline evidence worktree. If any independently approved evidence commit
intervenes, the later live brief must replace that parent with the exact
reviewed current commit before execution; drift stops the gate.

Require one-path scope, command-scoped Git identity, strict UTF-8 without BOM,
LF-only, one trailing LF, valid JSON, redaction scans, direct committed-byte
review, exact parent, and working/committed equality. Preserve every prior
incident fact, including overall FAIL, acceptance NOT PROVEN, private
transcript exposure, capture failure, and invalid-token HTTP `401` NOT PROVEN.
Only a new exact-token post-revocation HTTP `401` may change that one status;
row absence or cleanup cannot.

## Acceptance

This design becomes review-clean only after a fresh independent Sol High
direct-byte review finds no HIGH concern and confirms all seven correction
areas. A PASS authorizes preparation and independent review of exact live
briefs only. It authorizes no preflight, token creation, masked submission,
revocation, Cloudflare/VM1205 action, proxy/R5 consumption, or evidence change.
