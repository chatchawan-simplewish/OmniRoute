# Task 2 secure-console transfer live brief — independent Sol High review

## Verdict

**FAIL — 3 HIGH and 2 IMPORTANT findings.** The target, permissions, redaction,
one-use clipboard transfer, masked-input primitive, R5 source pin, and most
counter/cleanup structure are well bounded. However, the executable owner does
not guarantee the mandatory post-accept revocation hold on every path, and its
credential-bearing R5 child can block indefinitely before revocation. These are
load-bearing credential-residual failures and prohibit a static PASS.

This is a direct-byte static review only. No embedded block was evaluated or
invoked, and no browser, clipboard, token, credential, Cloudflare, VM, proxy,
process, registry, evidence, or routing action was performed.

`authorizes_live_execution=false`

## Reviewed evidence and integrity

- Brief commit: `5026b28140ad2431c1a5b77903845d174e4ed606`;
  direct parent: policy classification commit
  `183e3c82e00bc0e247be1c03f3648b639e3532bb`.
- The brief commit adds exactly
  `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-live-brief.md`.
- Brief: `47893` bytes, SHA-256
  `5C413FE3D6757166F4CCC9C5E969488126E06BC67261ACF37E51B0570891476E`.
- Direct-byte package: `49567` bytes, SHA-256
  `2AC3D7F7E8A5215033F7956A42C9F3003C8985756A9C3E063D7901582D0889C5`.
- Source pins checked: design `4cd480bcdd85f6d5bdee5645b0f16e6a870177e3`,
  design review `d22c0250558ac92b9b4fdc0606e2e1003899698f`, V10
  classification `3f871b2d583ea1b04673ecbe7ca3e2362a9bbead`, and
  policy classification `183e3c82e00bc0e247be1c03f3648b639e3532bb`.
- Before this artifact was created, the Git index was empty and the unrelated
  worktree baseline remained exactly 12 status entries.
- The brief is strict UTF-8, no BOM, LF-only, with exactly one trailing LF.
- The extracted owner is exactly `16234` bytes / SHA-256
  `3EFA4F6287361EEC64BE04B0FF379368384C66684065759D68B1156A589D1C94`.
- The extracted deterministic R5 script is exactly `10890` bytes / SHA-256
  `DB75253CD851075C1D612A54EC4B02C8016C034C8BC192A3DB9D02DB9890AD41`.
- Both extracted scripts parse with zero PowerShell parser errors. Parsing was
  non-evaluating; no fixture, process, network, clipboard, or live action ran.

## Findings

### HIGH 1 — Post-accept failures can bypass the mandatory revocation hold

**Evidence:** `task-2-secure-console-transfer-live-brief.md:549-554`,
`:660-726`, and `:737-806`.

The owner sets `$maskedAccepted = $true` as soon as a nonempty masked value has
reached the process. It then performs clipboard cleanup and converts the
`SecureString` through BSTR to the managed token **before** control reaches the
revocation block. If `Clear-CurrentClipboardOnce`, `SecureStringToBSTR`,
`PtrToStringBSTR`, the whitespace check, or any other uncaught statement in
that interval throws, control jumps to the outer catch and then directly to the
outer finally. The catch emits an active-token incident label, but it never
enters the 600-second `REVOCATION_REQUIRED` hold and never offers the separately
authorized exact-row deletion path.

This contradicts the reviewed design requirement that once the value reaches
the owner, **every** success or failure enters the same-process revocation hold.
The row may remain active while the only retained value is cleared and the
owner exits. The same bypass applies to any later unexpected exception that
escapes the narrower verification/R5 catches before the revocation block.

**Required fix:** restructure the owner so that all work after
`$maskedAccepted = $true` is inside a post-accept guarded phase whose `finally`
or single common continuation always enters the bounded revocation hold before
plaintext/reference cleanup. Operational errors must set a fixed safe status,
not escape around the hold. If conversion failed and no usable token exists,
the hold must still permit separately confirmed exact-row deletion while
classifying exact-token HTTP `401` as NOT PROVEN. Only after grant/deny/timeout
disposition may the outer cleanup clear the retained references and exit.

### HIGH 2 — The credential-bearing R5 child has no bounded lifetime

**Evidence:** brief `:593-657`; especially blocking `ReadToEnd()` at `:615-616`
and parameterless `WaitForExit()` at `:617` and `:641`. The pinned R5 source
contains nine `Invoke-RestMethod` commands and zero `-TimeoutSec` arguments.

After the token and Zone ID are placed in the child environment, the owner
calls synchronous `ReadToEnd()` on both streams and then unbounded
`WaitForExit()`. No child deadline, timed wait, cancellation, or retained-handle
termination path exists. The fallback wait in `finally` is also unbounded. A
network stall, child deadlock, or pipe/process anomaly can therefore retain the
token in the owner and child environments indefinitely, prevent entry into the
600-second revocation hold, prevent BSTR/SecureString cleanup, and leave the
one-shot gate permanently uncertain.

The two 600-second stopwatches do not bound this interval: the secret-input
clock ends before the R5 start, while the revocation clock starts only after the
child returns.

**Required fix:** give R5 a reviewed fixed wall-clock deadline. Avoid blocking
`ReadToEnd()` before the deadline; use bounded/asynchronous stream capture and a
timed wait. On expiry, act only on the retained exact child handle, perform one
reviewed termination attempt if authorized, prove bounded exit, clear both
private environment entries, classify R5 uncertain, and continue directly to
the mandatory revocation hold. Alternatively revise and repin the deterministic
R5 source with fixed HTTP deadlines, but an outer process deadline is still
needed for non-HTTP hangs. All timeout/termination counters and residual-state
outcomes must be fixed and redacted.

### HIGH 3 — The revocation confirmation trigger excludes valid post-accept failure paths

**Evidence:** authority rule at brief `:99-101` and launch rule at `:839-845`
say the separate deletion confirmation occurs **after R5 reaches a terminal**.
Yet the owner correctly routes active-token verification failure and exact-zone
lookup failure to `REVOCATION_REQUIRED` without starting R5 (`:556-591`,
`:660-726`). Clipboard/BSTR failures should also route there after HIGH 1 is
fixed.

On these paths there is no R5 terminal, so the prose supplies no valid trigger
for the mandatory exact-row deletion authority even though an active token row
may exist. This conflicts with the post-accept rule that every outcome requires
revocation and can force an avoidable timeout/active-credential incident.

**Required fix:** make the checkpoint trigger the owner's exact safe tuple
`REVOCATION_REQUIRED=PASS`, the fixed row name, and
`REVOCATION_AUTHORITY=WAITING` for **every** post-accept outcome, whether R5 was
never started, failed, timed out, or passed. The separately confirmed mutation
must remain exactly one deletion of the fixed matching row plus refreshed exact
name/row counts `0 / 0`; only then may the user signal `G`. No R5 terminal may
be a prerequisite for revocation authority.

### IMPORTANT 1 — “Exact-hash R5 child” is not bound to the executable at spawn time

**Evidence:** the brief pins the bundled `pwsh.exe` bytes/hash/version, but the
owner only assigns its path at `:408`. Immediately before the child start at
`:593-610`, it neither checks file length/hash/version nor proves the resolved
path is the pinned executable. Static AST/cardinality inspection finds zero
`Get-FileHash` checks against `$pwshPath` in the owner.

An earlier credential-free action-time check does not bind bytes at the later
post-accept process start. Executable drift between those points would give the
token and Zone ID to an unpinned process, violating the two-holder boundary.

**Required fix:** immediately before constructing/starting the sole R5 child,
re-resolve and require the exact path, `301368` bytes, SHA-256
`DB6DD81183FE57D22E03B911EC9A30A2FD7C40542E97743615355A6FB44F458F`,
and file version `7.6.4.500`. Failure must remain post-accept, start zero
children, and enter the revocation hold from HIGH 1.

### IMPORTANT 2 — Other retained child/process waits are also unbounded

**Evidence:** credential-free `Invoke-ExactSsh` reads both streams and uses
parameterless `WaitForExit()` at `:185-205`; `ConnectTimeout=10` bounds only SSH
connection establishment, not an already connected remote start/proof/rollback
command. The retained parent later waits on the credential owner with another
parameterless `WaitForExit()` at `:851`.

An SSH remote command can hang after connection, leaving the fresh proxy start
or proof uncertain and preventing the exact rollback decision. An unexpected
owner wedge can likewise block external exit/script-absence proof forever.
These paths are incompatible with fixed one-shot observation boundaries.

**Required fix:** assign reviewed fixed deadlines to every spawned retained
process and define exact timeout disposition. For SSH, use both transport
liveness settings and a retained-handle wall clock; timeout must report
start/proof/rollback uncertainty without retry. For the credential owner, the
outer deadline must exceed the sum of the reviewed prompt, R5, revocation, and
request budgets, then use only the retained verified handle for any separately
authorized termination and classify token/revocation state conservatively.

## Confirmed contracts without findings

The following portions passed static review but do not offset the findings:

- **Target/scope:** exact zone `mysw.me`, hostname
  `ai-api-omniroute.mysw.me`, fixed description/expression, fixed unique token
  name, specific-zone resource scope, and exactly Zone WAF Edit plus Zone Read.
  Account, token-management, DNS, Tunnel, and other permissions are excluded.
- **Freshness:** refreshed token-name and matching-row counts must both be zero;
  OS/policy, worktree, Chrome-zero-tab, proxy/VM, Cloudflare rule/resource, and
  OmniRoute-key states are freshly pinned before Create.
- **Human gates:** final Create, one native Cloudflare Copy, and one masked
  native Paste require one explicit action-time confirmation; exact-row
  deletion requires a distinct confirmation. Neither static PASS nor standing
  authority can waive those confirmations.
- **Browser/secret boundary:** after final Create, agent DOM/page inspection,
  snapshots, screenshots, evaluation, clipboard API, keyboard injection, CUA,
  and token-page inspection are all zero. No Cloudflare copy equivalence is
  inferred from V10.
- **Masked input:** one same-process monotonic 600-second prompt uses
  `ReadKey($true)`, clears per-iteration key references, emits no value/length,
  and has no second secret prompt.
- **Clipboard cleanup:** executable cardinality is one `Set-Clipboard` and one
  `Get-Clipboard`; the attempt guard prevents retry after either is attempted.
  Cleanup is shape-only and does not claim history erasure.
- **Same-process API:** active-token verification and exact-name `mysw.me` zone
  lookup are serial, each with `TimeoutSec 20`; zone success requires one result,
  total count one, exact case-sensitive name, and one lowercase 32-hex ID that
  is never emitted.
- **R5 source/cardinality:** the exact deterministic R5 bytes parse cleanly,
  contain one POST, and preserve the reviewed attributable rollback boundary.
  The owner allows at most one child and passes the token/Zone ID only through
  child environment entries, not arguments or parent environment.
- **Revocation proof when reached:** one separately authorized exact-row delete,
  refreshed counts `0 / 0`, then one retained-token verify requiring HTTP 401;
  row absence never substitutes for 401.
- **Cleanup/redaction:** BSTR is zero-freed once when nonzero; `SecureString` is
  disposed; named managed/header/response/environment references are cleared;
  exact-hash owner/R5 scripts are guard-deleted; safe output excludes token,
  Zone ID, headers, response bodies, DOM, clipboard bytes, and private IDs.
- **Excluded rollout:** no Tunnel/DNS/public hostname/Access application,
  rollout key, model request, OmniRoute restart, Bell proxy, VM power, provider
  routing, or evidence mutation is included.

## Pre/post-accept path audit

| Path | Static result |
| --- | --- |
| Pre-accept path/byte/env guard failure | Correctly converges on outer cleanup; no token accepted. |
| Masked cancel, empty input, or 600-second timeout | Correctly converges on cleanup with no authenticated request or child. |
| Post-accept clipboard or BSTR/conversion failure | **FAIL:** bypasses revocation hold (HIGH 1). |
| Verify or zone lookup failure | Reaches hold, but confirmation trigger is contradictory because R5 never ran (HIGH 3). |
| R5 start/output/terminal failure | Intended to reach hold after catch, but can hang indefinitely before catch/hold (HIGH 2). |
| Revocation deny or 600-second timeout | Fixed active-token incident, no inferred revocation, then named-reference cleanup; PASS. |
| Revocation grant plus exact HTTP 401 | Correct terminal split between R5 PASS and prior operational failure; PASS. |
| Invalidity request failure/non-401 | Fixed NOT PROVEN disposition and cleanup; PASS. |
| Script/clipboard cleanup failure | Fixed cleanup-failure terminal, no retry; PASS, subject to earlier hold defects. |

## Required disposition

Do not execute or consume this candidate. Revise the brief and owner script,
repin all affected bytes/hashes, and obtain a fresh independent Sol High review.
The fix must guarantee one bounded revocation disposition after every
post-accept path, bind the exact child executable immediately before the sole
spawn, and bound every retained process without introducing retry, fallback,
secret output, broader deletion, or authority expansion. The public rollout
and evidence mutation remain excluded.
