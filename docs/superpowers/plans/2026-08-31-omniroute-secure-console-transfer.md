# OmniRoute Secure-Console Transfer Implementation Plan

> **For agentic workers:** Keep the one-shot credential gate in the sole Sol
> High owner task. Review-only or document work may use isolated workers, but a
> worker must never receive credentials or consume a live gate.

**Goal:** Replace the rejected clipboard bridge with one bounded non-secret
transport preflight and one review-clean secure-console credential channel,
while preserving the existing one-shot Task 2 proof/R5 authority boundaries.

**Architecture:** A credential-free process may test a fresh challenge once.
After it exits, one visible PowerShell 7 owner uses a same-process monotonic
masked-input loop, clears the current clipboard, verifies the fresh token, and
owns it through the existing proof. Only the immutable synchronous R5 child may
receive the two reviewed private environment values. Pre-accept failures clean
and exit; post-accept outcomes enter a bounded revocation-required hold before
final cleanup.

**Tech stack:** PowerShell 7, Windows Console, Cloudflare API, existing
OmniRoute verifier/R5 artifacts, exact-path Git evidence.

## Global constraints

- Preserve the rejected Chrome-native canary and prior incident evidence; never
  execute, retry, reinterpret, or overwrite them.
- No live action follows from a document commit or review PASS. Preflight,
  token creation/submission, and revocation each require their own exact
  action-time gate.
- Within either live gate: no retry, fallback, replacement process, second
  token, alternate bridge, session handoff, page serialization, or verdict
  relaxation.
- Keep the credential gate and all consuming counters in one Sol High owner.
  Do not delegate R5 or any no-retry gate.
- Preserve unrelated dirty files. Stage only explicit paths and use
  command-scoped Git identity.
- Every evidence state sets `authorizes_live_execution=false`.

---

### Task 1: Commit the F1-F7 revision only

**Files:**
- Modify: `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-design.md`
- Modify: `docs/superpowers/plans/2026-08-31-omniroute-secure-console-transfer.md`

**Inputs:**
- Reviewed design commit `fc386f30eb673be5509b0550f670bad4ad29fdc6`
- FAIL review commit `5d8ea953ce9bfdde88fc9fbeb99db1c43b6d41be`
- Incident review SHA-256
  `A2558F9FBEC57A7FED2D0CA2DF2B3C9864716E23C0E07CC8F4DFD5851BEB93C4`
- Rejected-canary review SHA-256
  `1A03BA9DCD03AD5482DB550A63FEFB710A08E0A72270EE8A327494A2AE518A3C`
- Existing exact R5 bytes: `10,890` bytes, SHA-256
  `DB75253CD851075C1D612A54EC4B02C8016C034C8BC192A3DB9D02DB9890AD41`

- [ ] **Step 1: Verify direct bytes and content gates**

For both files require nonzero size/hash, strict UTF-8, no BOM, LF-only, one
trailing LF, no placeholder token, and no credential pattern. Check that the
design explicitly covers F1 through F7: R5 inheritance, clipboard history/sync,
monotonic input, two-phase revocation, preflight ownership matrix, plaintext
reference limits, and two-subobject evidence.

- [ ] **Step 2: Stage exactly two ignored paths and commit**

```powershell
git add -f -- '.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-design.md'
git add -f -- 'docs/superpowers/plans/2026-08-31-omniroute-secure-console-transfer.md'
git diff --cached --check
git diff --cached --name-only
git -c user.name='Codex' -c user.email='codex@openai.com' commit -m 'docs: close secure transfer review findings'
```

Expected cached names are exactly those two paths. The commit parent is exactly
`5d8ea953ce9bfdde88fc9fbeb99db1c43b6d41be`. Do not stage or modify the
unrelated implementation baseline.

- [ ] **Step 3: Stop without evidence mutation**

Task 1 creates no evidence object, process, browser page, clipboard action,
token, VM1205 request, proxy, R5 child, or Cloudflare action.

### Task 2: Obtain fresh independent direct-byte review

**Single authoritative file appended by reviewer only:**
- `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-sol-review.md`

- [ ] Give the independent Sol High reviewer the authoritative review paths,
  revised commit/hash, and seven required verdict areas F1-F7.
- [ ] Append one clearly titled `Fix round <n> scoped re-review` section to the
  authoritative review above. Never create or maintain a second current verdict
  file for this design.
- [ ] Require direct committed-byte equality, strict encoding, exact two-path
  scope/parent, no placeholder, no secret, and contradiction review.
- [ ] Require `PASS` with no HIGH concern before preparing a live brief. `FAIL /
  REVISE` stops; it authorizes neither a partial execution nor another gate.

### Task 3: Prepare and review the corrected non-secret preflight

**Files:**
- Create: `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-anydesk-clipboard-preflight-live-brief.md`
- Create after execution: `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-anydesk-clipboard-preflight-live-report.md`

- [ ] **Step 1: Pin exact script ownership**

The brief must embed the complete credential-free script and pin strict
UTF-8/LF bytes, size, SHA-256, validated temp root/direct-child path, exact
deletion guard, retained handle/expected PID, reported-PID equality, and
external handle-based exit/absence proof.

- [ ] **Step 2: Pin the four-state matrix and counters**

Generate the fresh 128-bit challenge at runtime with the .NET CSPRNG. Pin one
empty baseline, one page, one focus, one `Control+A`, one `Control+C`, and one
control line. Require comparison-read counts for `COPY_DONE / ABORT / EOF /
timeout` exactly `1 / 0 / 0 / 0`. All states use one `finally` to clear and
empty-check the OS clipboard, close only the exact page, guard-delete the exact
script, emit labels, and exit. Counters remain separate from the later
credential owner.

- [ ] **Step 3: Parse and fixture-test without live transport**

Parse exact PowerShell bytes and run credential-free fixtures for all four
terminal states. Fixtures use no browser/clipboard/Cloudflare/VM1205 action and
prove state routing, comparison counters, common cleanup labels, process exit,
and exact-script absence. Any mismatch revises the brief before review; it does
not consume the live preflight.

- [ ] **Step 4: Obtain independent brief approval, then separate execution authority**

After approval, request authority naming exactly one non-secret preflight.
Execute once, stop on the first mismatch, and independently classify it. Even
a PASS proves only the observed local transport and authorizes no token action.

### Task 4: Prepare the exact credential-owner live brief

**Files:**
- Create: `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-live-brief.md`
- Create after execution: `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-live-report.md`

- [ ] **Step 1: Pin exact owner script and one process**

Embed the complete credential-free script. Pin strict UTF-8/LF/no-BOM bytes,
size, SHA-256, validated temporary root/direct-child path, deletion guard,
retained process handle/PID, fixed labels, numeric input deadline, numeric
revocation-hold deadline, and external exit/absence proof. The preflight
process must already be absent.

- [ ] **Step 2: Implement the single same-process input loop**

Use only `[Diagnostics.Stopwatch]`, `[Console]::KeyAvailable`, and
`[Console]::ReadKey($true)` for the reviewed masked loop. Handle printable
characters, Enter, Backspace, Escape, Ctrl+C, EOF-equivalent console failure,
and timeout. Append directly to `SecureString`; emit no value or length; start
no job, thread, supervisor, or child; offer no second prompt. Every path reaches
one outer `finally`.

- [ ] **Step 3: Pin clipboard prerequisites and cleanup**

Before creation, require read-only effective-state proof for the exact Windows
build that clipboard history and OS/device sync are disabled. Ambiguity or an
enabled state stops before creation. After masked submission, the owner performs
one cleanup-only current-clipboard clear and one shape-only empty check; close
the exact token page before any agent browser call. State explicitly that a
current clear does not erase clipboard history.

- [ ] **Step 4: Pin authorized credential holders and child environments**

The owner is holder `1`. The only permitted second holder is the synchronous
exact-hash R5 `pwsh.exe` child. Its only private environment entries are
`CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ZONE_ID`, added through its
`ProcessStartInfo.Environment` immediately before start. All other child
launches remove both names. Retain the R5 handle/PID, wait synchronously without
yield/interruption, clear the start-info entries after start, and prove child
exit. No parent process-environment secret is permitted.

- [ ] **Step 5: Enumerate plaintext-bearing references**

Name `$key`, its managed `ConsoleKeyInfo.KeyChar`, `$keyChar`, every other
derived character variable, and every additional input-host/console buffer in
the final implementation, plus the unmanaged BSTR, shortest-lived managed token
string, Authorization header string/collection, zone-ID string, the two R5
environment entries, and all R5-local environment/header/response/result
references. Each key object lives only for its current iteration; clear its
named reference and derived character references in a per-iteration `finally`
immediately after handling and again in the full script's one outer `finally`.
Minimize all other lifetimes, call `ZeroFreeBSTR`, dispose `SecureString`, clear
every named reference, and prove child/owner exit. The exact live-brief review
must reject any unenumerated input-host buffer. Evidence may claim only
references cleared and owning processes exited, never managed-memory byte
zeroization.

- [ ] **Step 6: Pin acceptance and two cleanup phases**

Before acceptance, failures fully clean, guard-delete, prove owner exit, and
stop. A token that reaches the owner enters post-accept handling even if active
verification fails. Post-accept success/failure enters bounded
`REVOCATION_REQUIRED` in the same owner and permits no action except a started
R5 finishing and the separately authorized revocation sequence.

On revocation authority: one exact-row action, one exact-token invalidity check
requiring HTTP `401`, one refreshed exact-name/row count requiring `0 / 0`, then
final cleanup. On denial/timeout: no inferred action or retry; record active-row
risk and `NOT PROVEN`, block Task 2, clear and exit at the bounded local-residency
deadline, and require explicit later owner disposition. Row absence cannot
substitute for the exact-token `401`.

- [ ] **Step 7: Credential-free parser and timeout/cancel fixtures**

Parse the exact script. Run only credential-free fixtures that inject no value,
make zero HTTP/clipboard/browser/R5 calls, and prove timeout/cancel reach the
same final cleanup with one PID, script deletion, owner exit, and zero residual
child. These fixtures do not prove live console or credential behavior.

- [ ] **Step 8: Obtain fresh Sol High live-brief approval**

The independent reviewer checks exact bytes and every counter/authority edge.
Any concern stops before process, browser, clipboard, or token action.

### Task 5: Consume the credential gate once

**Inputs:** approved live brief, exact evidence HEAD, exact action-time token
creation/submission confirmation, fixed existing 19-label proxy proof, immutable
R5 script.

- [ ] **Step 1: Revalidate all preconditions read-only**

Require exact evidence HEAD, clean evidence worktree, immutable hashes,
preflight process/script absence, target proxy/Tunnel/listener/token absence,
target token name/row counts `0 / 0`, exact OS setting proof, and zero drift.
Any mismatch stops before owner start or token creation.

- [ ] **Step 2: Request creation and submission authority separately**

Name exactly one Cloudflare final Create and one user masked paste into the
retained visible owner PID. Do not combine revocation or any later authority.

- [ ] **Step 3: Execute only the approved creation/submission sequence**

Start exactly one owner. The user uses native Create/Copy/Paste manually. Make
no agent token-page inspection. The owner clears/current-empty-checks the
clipboard, closes the exact page, verifies freshness/row/PID/active status, and
then runs the existing proof/R5 contract at most once. Stop on first mismatch.

- [ ] **Step 4: Enter bounded revocation-required hold**

After the exact token reaches the owner, success and failure both enter the
hold. Request a separate confirmation naming one exact-row revocation, one
exact-token HTTP `401` check, and one refreshed `0 / 0` row check.

- [ ] **Step 5: Resolve or classify the hold**

If granted, perform only the reviewed revocation sequence and final cleanup.
If denied or timed out, perform no revocation or retry; report the exact active
row risk, mark invalidity/acceptance NOT PROVEN, block all later Task 2 action,
and follow the brief's bounded local-reference cleanup/exit disposition. Never
silently imply the token was revoked.

### Task 6: Add one redacted versioned evidence object and review it

**File modified only after the live result:**
- `C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-team-api-offline\artifacts\omniroute-live-integration\evidence\team-api-verification.json`

- [ ] **Step 1: Revalidate exact evidence parent and path**

Expected initial parent is
`80adaa7d5d63d1d2c7bfa63b236c6bee93b3b1d8`. If an approved evidence commit
intervened, stop and obtain a revised live brief pinning its exact commit; do
not infer a parent.

- [ ] **Step 2: Add only `secure_console_transfer_v1`**

Set `schema_version=1`; include separate `transport_preflight` and
`credential_gate` subobjects. For each, record reviewed contract/brief/script
hashes and sizes, bounded timestamps, expected/observed PIDs, counters, result,
cleanup labels, page close, current-clipboard cleanup, exact-script deletion,
external exit/absence proof, and `authorizes_live_execution=false`.

Credential evidence additionally records disabled clipboard-history/sync proof,
acceptance, R5 exit, revocation authority/result, exact-token invalidity, and
refreshed name/row counts. Preserve every prior incident field. Change the
invalid-token `401` status only after one exact retained-token post-revocation
HTTP `401`; never from row absence or cleanup.

- [ ] **Step 3: Verify redaction and commit exactly one path**

Require strict UTF-8/no BOM/LF-only/one trailing LF, valid JSON, no credential,
Authorization header, private ID, clipboard content, keystroke, prompt,
response body, or managed plaintext. Stage only the exact evidence path with
command-scoped identity. Verify cached scope/check, exact parent, committed
bytes, and working/committed equality.

- [ ] **Step 4: Obtain independent evidence review and stop**

The reviewer issues PASS or preserves FAIL / NOT PROVEN. No evidence result
authorizes retry, rollout, Tunnel, DNS, key, model request, or another token.
