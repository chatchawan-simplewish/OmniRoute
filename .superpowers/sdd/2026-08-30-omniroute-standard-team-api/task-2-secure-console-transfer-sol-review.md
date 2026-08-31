# Task 2 secure-console transfer independent Sol High review

Reviewed at: `2026-08-31` (`Asia/Bangkok`)

Reviewer role: fresh independent Sol High, direct-byte, contract-only review. No
browser, process, VM1205, Cloudflare, OmniRoute, proxy, Rulesets, Tunnel, DNS,
credential, token, clipboard, or consuming-gate action was performed. The only
write is this review artifact.

## Executive verdict

**FAIL / REVISE BEFORE EXECUTION / NOT AUTHORIZED.**

The replacement is directionally correct: it retires the rejected canary as
credential evidence, uses a fresh non-secret challenge with an empty baseline,
bounds the preflight conclusion, separates the credential channel, preserves
one-shot/no-retry language, and requires action-time authority. It is not yet
review-clean because four HIGH contradictions make the proposed gate either
non-executable or less secure than stated:

1. the unchanged R5 child must inherit the token, while the new design forbids
   the token from reaching any child process or inherited environment;
2. the native Copy/Paste path leaves the plaintext token in the Windows
   clipboard and potentially clipboard history, but cleanup forbids and omits
   credential-stage clipboard cleanup;
3. `Read-Host -AsSecureString` is blocking and the contract provides no
   executable same-process bounded timeout; and
4. a post-capture failure enters `finally` and destroys the token before the
   separately authorized revocation and mandatory invalid-token `401` proof can
   use the exact token.

No live brief may be prepared as approved, and no process, browser, token,
Cloudflare, VM1205, proxy, proof, R5, Rulesets, or evidence mutation is
pre-approved by this review.

## Direct-byte inputs

| Input | Independent result |
| --- | --- |
| Authoritative commit | `fc386f30eb673be5509b0550f670bad4ad29fdc6` |
| Parent | exactly `c924f79c9ec31deb00c1ef5437fd663cf0e05d4f` |
| Commit scope | exactly the replacement design and implementation plan |
| Design | `8,678` bytes; SHA-256 `CC9640D121DBC86AE6B38051F94922EE140B3DA45D1CD99E78111C09C6129396`; blob `905d1f4e37acf559097dd309f8930405a5161283` |
| Plan | `9,515` bytes; SHA-256 `AC358FB9ADC20668E020CF103981AF9730B2FA139CD8E1E60C0FC156CCA9C4D5`; blob `16e8fca9fa007aa63dbf0ab3e2aa943ee8531d2a` |
| Encoding | both strict UTF-8, no BOM, LF-only, one trailing LF |
| Working/direct equality | both working files hash to their exact committed blobs |
| Incident review | SHA-256 `A2558F9FBEC57A7FED2D0CA2DF2B3C9864716E23C0E07CC8F4DFD5851BEB93C4` |
| Rejected-canary review | SHA-256 `1A03BA9DCD03AD5482DB550A63FEFB710A08E0A72270EE8A327494A2AE518A3C` |
| Supplied review diff | direct read; it contains exactly the two-file commit described above |

Line references below use `design` for
`task-2-secure-console-transfer-design.md`, `plan` for
`2026-08-31-omniroute-secure-console-transfer.md`, `canary review` for
`task-2-chrome-native-canary-contract-sol-review.md`, and `R5 review` for
`task-2-rulesets-api-incident-sol-review.md`.

## Required-dimension results

| Dimension | Result |
| --- | --- |
| Fresh-challenge stale-baseline correction | **PASS in principle.** `design:31-44` clears and reads an empty baseline, generates a fresh 128-bit challenge, permits one copy, and gives executable maximum read/write counters. This eliminates the static stale-clipboard false PASS identified at `canary review:26-39`. |
| COPY_DONE / ABORT / EOF / timeout cleanup and ownership | **REVISE.** `design:37-44` names the states but does not pin a common state matrix, exact script path/root/hash ownership, retained process handle, reported/expected PID equality, page closure, cleanup labels, or handle-based exit proof for every state. `plan:91-95` adds a `finally` requirement but not the missing ownership proof. |
| Bounded conclusion | **PASS.** `design:46-49` says a PASS proves only the observed local Chrome/AnyDesk/Windows transport and neither proves Cloudflare semantics nor authorizes token creation. |
| Separate masked credential channel | **PASS in concept / FAIL as executable contract.** `design:7-14,64-89` separates the channel and bars agent submission, but the R5 inheritance and timeout contradictions below prevent faithful implementation. |
| Fresh single-token binding | **PASS in concept, subject to exact live-brief evidence.** `design:95-108` requires pre-zero row count, a unique reviewed name, one Create, retained-PID equality, active verification, no pre-existing source, and one post-ready submission. The live brief must pin how the final Create and exact row are evidenced without serializing the token page. |
| One fixed owner through 19 labels / R5 | **FAIL.** The owner remains fixed, but unchanged R5 necessarily receives the credential in a child environment, contrary to the new prohibition. |
| Deterministic cleanup | **FAIL.** Clipboard/current-history state, managed plaintext copies, and post-capture revocation sequencing are not safely closed. |
| Action-time and no-retry gates | **PARTIAL PASS.** Creation/submission authority and zero retry/fallback remain explicit at `design:51-62,110-121` and `plan:11-19`; the separate revocation authority has no executable success/failure sequence that preserves the exact token until invalidity proof. |
| Additive evidence | **REVISE.** `design:138-151` preserves prior fields and redaction, but does not define a complete additive preflight record and limits `authorizes_live_execution=false` to a design-review case that the plan never writes. |

## Findings and minimum corrections

### F1 — HIGH: unchanged R5 requires the forbidden child-process credential handoff

`design:7-10` says the token must never enter an environment inherited by
another process. `design:87-89` says the owner must not relay the token to
another process while continuing the unchanged deterministic R5 child.
`plan:109-118` likewise pins the existing exact-hash R5 artifact.

That cannot satisfy the authoritative R5 execution contract. `R5
review:405-423` requires a fresh non-interactive `pwsh.exe` child and explicitly
states that the child inherits the two private Cloudflare environment values.
The existing live-owner brief also requires that exact child at
`task-2-labeled-proof-live-brief.md:23-32`.

Minimum correction: choose and independently review exactly one consistent
model before writing the live brief:

- narrowly permit the exact-hash, synchronous R5 child to inherit only the two
  required private values, count that child as an authorized credential holder,
  prevent all other child inheritance, and prove its exit; or
- replace R5 with a new same-process implementation and obtain a new direct-byte
  contract/hash review.

The first option is the minimum change because it preserves the existing R5
bytes. Neither option may be silently inferred from the current text.

### F2 — HIGH: the credential remains in Windows clipboard/history and cleanup forbids clearing it

The user must activate native Copy and paste into the masked prompt
(`design:78-82`; `plan:140-146`). The design therefore places the plaintext
token in the Windows clipboard even though it never becomes agent-visible.
`design:90-93` clears process variables and the script but does not clear the
clipboard. Worse, `design:129-132` requires credential-stage clipboard
reads/writes by the agent or fixed process to remain `0 / 0`. The earlier
approved owner contract required clipboard clearing after revocation
(`task-2-labeled-proof-live-brief.md:32`), so the replacement weakens that
cleanup.

Setting the current clipboard to empty also does not by itself prove removal
from Windows clipboard history or cloud/device clipboard sync. The report that
AnyDesk synchronization is disabled (`design:26-29`) does not establish those
Windows states.

Minimum correction:

1. before token creation, prove Windows clipboard history and OS/device sync are
   disabled, or obtain separate destructive-data authority for an exact reviewed
   history-clear operation; otherwise use a no-clipboard manual-entry channel;
2. immediately after masked submission, make the same owner process perform one
   cleanup-only clipboard clear and one post-clear empty check without emitting
   content;
3. change the credential-stage counters to allow and classify those cleanup-only
   actions while retaining zero agent clipboard reads; and
4. keep all agent browser calls blocked until the current clipboard and any
   approved history surface are proven clean and the token page is closed.

### F3 — HIGH: `Read-Host -AsSecureString` and a bounded same-process timeout are not an executable pair

`design:72-77` mandates exactly one `Read-Host -AsSecureString` call in exactly
one fixed process. `design:110-117` simultaneously requires a reviewed bounded
timeout whose expiry reaches `finally` without a second process or prompt.
`plan:112-120` repeats both requirements and asks for an ABORT/timeout fixture.

`Read-Host` is a blocking host call; this contract defines no same-process
mechanism that interrupts it at the deadline. A timer that merely fires cannot
release the blocking read. Common job/child-process workarounds would violate
the one-process and sole-credential-owner constraints.

Minimum correction: pin one executable bounded masked-input primitive in the
design before live-brief work. The narrow same-process option is a reviewed
monotonic-deadline `[Console]::KeyAvailable` / `ReadKey($true)` loop that appends
characters directly to a `SecureString`, handles Enter/Backspace/cancel, emits
no value or length, and converges on the same `finally`. If `Read-Host` is kept,
the design must explicitly permit and secure the exact supervisory mechanism
that can cancel it, then re-count process/credential ownership. The live brief
must prove timeout without using any real credential.

### F4 — HIGH: failure cleanup destroys the exact token before separately authorized revocation proof

`design:112-117` sends every failure to `finally`, which clears the token/header
state and exits. Only afterward, `design:118-119` says to request separate
action-time authority for exact-row revocation. If the token reached the fixed
process, this ordering makes the mandatory post-revocation invalid-token HTTP
`401` proof impossible because the exact token no longer exists. The incident
review explicitly preserves that requirement at
`task-2-labeled-capture-incident-sol-review.md:147-158`.

The plan has only the creation/submission authority step (`plan:140-146`) and no
explicit success-or-failure revocation checkpoint before final cleanup. This is
not merely documentary: it can leave either an active token without a retained
proof credential or an indefinitely resident credential while waiting for new
authority.

Minimum correction: define two cleanup phases:

1. before any token is accepted, failures use immediate full cleanup and exit;
2. after the exact token is accepted, success or failure enters a bounded
   `REVOCATION_REQUIRED` hold in the same fixed owner, requests the separate
   exact-row revocation confirmation, permits one revocation action, verifies
   the exact token now returns HTTP `401` and the refreshed row count is `0`, and
   only then performs final zero/free/clipboard/script/process cleanup.

The live brief must specify the timeout/denial outcome without retry or inferred
revocation authority. If exact-token `401` cannot be completed, record it as
`NOT PROVEN`; never substitute row absence or cleanup.

### F5 — IMPORTANT: preflight state ownership and cleanup are still underspecified

The fresh challenge and read/write maxima fix the stale-baseline and counter
problems (`design:31-49`), but `ABORT`, EOF, and timeout merely “enter cleanup.”
Unlike the minimum correction at `canary review:71-81`, the design does not
require the coordinator to retain the exact spawned handle, match its PID to an
owner label, or prove all terminal states release that handle. It also does not
scope `Fixed PowerShell processes: exactly 1` (`design:123-128`) to the credential
gate even though the preflight and credential gate each create a process.

Minimum correction: the preflight brief must pin:

- runtime CSPRNG challenge generation rather than a static value;
- exact script bytes, validated temporary root/path, hash, size, and deletion
  guard;
- retained spawn handle/expected PID and owner-reported PID equality;
- a four-row `COPY_DONE` / `ABORT` / EOF / timeout matrix with comparison-read
  counts `1 / 0 / 0 / 0`;
- one common `finally` that clears and post-checks the OS clipboard, closes only
  the exact page, deletes only the exact-hash script, emits cleanup labels, and
  exits; and
- external handle-based exit and exact-script-absence proof.

State process counters separately: at most one preflight process and exactly one
later credential-owner process. A preflight PASS remains non-transferable to the
Cloudflare copy control.

### F6 — IMPORTANT: deterministic memory-zero claims exceed what the planned PowerShell flow proves

`design:83-93` and `plan:112-120` require conversion of the `SecureString` for
HTTP use, `ZeroFreeBSTR`, variable clearing, and exit. `ZeroFreeBSTR` can wipe
the unmanaged BSTR, but ordinary PowerShell/.NET header construction and the
existing R5 environment contract create managed string/environment copies that
cannot be proven zeroed merely by assigning `$null` or removing variables.

Minimum correction: the exact live brief must enumerate every plaintext-bearing
buffer, managed string, header, environment entry, and permitted child; minimize
their lifetimes; call `ZeroFreeBSTR` in `finally`; clear every named reference;
prove the exact child and owner exit; and bound the evidence statement to
“references cleared and owning processes exited.” Do not claim byte-for-byte
managed-memory zeroization unless a reviewed implementation actually provides
and verifies it.

### F7 — IMPORTANT: additive evidence does not fully specify the two separate gates

`design:138-151` allows one `secure_console_transfer` object and preserves prior
incident fields, which is directionally correct. It does not explicitly require
the rejected-canary review's complete additive preflight fields
(`canary review:77-81`), distinguish preflight result from credential result, or
require `authorizes_live_execution=false` for every later evidence state. It
also mentions a design-review evidence object although Task 1's exact commit
scope excludes the evidence file (`plan:23-77`).

Minimum correction: keep Task 1 evidence-free. For later evidence, add one
versioned object with separate `transport_preflight` and `credential_gate`
subobjects. Pin each contract/brief/script hash and size, bounded timestamps,
exact counters, result, cleanup labels, prior-incident preservation, and
`authorizes_live_execution=false`. Preserve all prior FAIL / NOT PROVEN facts,
including private transcript exposure and invalid-token `401` status, unless a
new exact-token proof directly establishes only that specific later fact.
Require exact parent, exact path-only scope, strict UTF-8/redaction, and
working/committed equality.

## Conditions for a future PASS

A revised committed design may receive PASS only after all HIGH findings and
the IMPORTANT contract gaps above are corrected without weakening the existing
one-shot counters. The next review must direct-byte verify the revised design,
the exact preflight state machine, the exact credential-input/timeout primitive,
the R5 secret-ownership choice, the revocation-before-final-cleanup sequence,
and the additive evidence schema.

Even a later design PASS may authorize only preparation and independent review
of exact live briefs. It must not authorize preflight execution, token creation,
masked submission, revocation, Cloudflare/VM1205 action, proxy/R5 consumption,
or evidence mutation without their separately required action-time gates.
