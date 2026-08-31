# OmniRoute Secure-Console Transfer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the rejected clipboard canary with one bounded fresh-challenge transport preflight plus a review-clean secure-console credential channel, then use the credential channel once inside the existing Task 2 gate.

**Architecture:** A credential-free fresh-challenge preflight may test the current Chrome/AnyDesk/Windows clipboard path once without claiming Cloudflare equivalence. A separate fixed visible PowerShell 7 process receives one masked user submission with `Read-Host -AsSecureString`, verifies the token, and remains the sole credential owner through the existing 19-label proof and R5 contract; every abort path converges on deterministic cleanup.

**Tech Stack:** PowerShell 7, Cloudflare API, existing OmniRoute verifier/R5 artifacts, Git exact-path evidence.

## Global Constraints

- Preserve the rejected Chrome-native canary as rejected; never execute it.
- No live action before a fresh independent Sol High design PASS.
- Within either gate: no retry, fallback, replacement process, second token, alternate bridge, page serialization, or verdict relaxation.
- A preflight PASS proves only the current non-secret transport and authorizes no token action.
- Preserve the unrelated dirty baseline and stage only named files with command-scoped Git identity.
- Require action-time confirmation for the exact token creation and masked submission, and separate confirmation for revocation, sensitive transmission, permission change, or deletion.
- The one-shot live gate and its evidence review stay in the sole Sol High owner task.

---

### Task 1: Freeze and independently review the replacement design

**Files:**
- Create: `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-design.md`
- Create after review: `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-sol-review.md`

**Interfaces:**
- Consumes: incident review SHA-256 `A2558F9FBEC57A7FED2D0CA2DF2B3C9864716E23C0E07CC8F4DFD5851BEB93C4`, rejected-canary review SHA-256 `1A03BA9DCD03AD5482DB550A63FEFB710A08E0A72270EE8A327494A2AE518A3C`, evidence commit `80adaa7d5d63d1d2c7bfa63b236c6bee93b3b1d8`.
- Produces: immutable design commit/hash and an independent `PASS` or `FAIL / REVISE` review.

- [ ] **Step 1: Verify the design bytes**

Run in PowerShell from the nested OmniRoute repository:

```powershell
$Path = '.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-design.md'
$Bytes = [IO.File]::ReadAllBytes((Resolve-Path $Path))
[pscustomobject]@{
  Bytes = $Bytes.Length
  Sha256 = (Get-FileHash -Algorithm SHA256 $Path).Hash
  CrLf = ([regex]::Matches([Text.Encoding]::UTF8.GetString($Bytes), "`r`n")).Count
  Placeholder = ([regex]::Matches([Text.Encoding]::UTF8.GetString($Bytes), ('(?im)\b(T' + 'BD|T' + 'ODO)\b'))).Count
}
```

Expected: non-zero bytes/hash, `CrLf=0`, `Placeholder=0`.

- [ ] **Step 2: Commit only the design and this plan**

```powershell
git add -f -- '.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-design.md'
git add -- 'docs/superpowers/plans/2026-08-31-omniroute-secure-console-transfer.md'
git diff --cached --check
git diff --cached --name-only
git -c user.name='Codex' -c user.email='codex@openai.com' commit -m 'docs: design secure OmniRoute token transfer'
```

Expected staged names: exactly the two paths above.

- [ ] **Step 3: Obtain a fresh independent Sol High review**

Give the reviewer only the two authoritative review paths, the replacement-design path, exact commit/hash, and the five required verdict dimensions: faithful separate secure-input boundary; fresh single token binding; fixed-process ownership; abort/timeout/cleanup; additive redacted evidence.

Expected: the reviewer writes the review file and returns `PASS` with no HIGH concern, or `FAIL / REVISE` with exact findings. A failure stops Task 2.

- [ ] **Step 4: Commit only the independent review**

```powershell
git add -f -- '.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-sol-review.md'
git diff --cached --check
git diff --cached --name-only
git -c user.name='Codex' -c user.email='codex@openai.com' commit -m 'docs: review secure OmniRoute token transfer'
```

Expected staged name: exactly the review path.

### Task 2: Prepare and run the reviewed non-secret preflight

**Files:**
- Create: `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-anydesk-clipboard-preflight-live-brief.md`
- Create: `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-anydesk-clipboard-preflight-live-report.md`

**Interfaces:**
- Consumes: Task 1 PASS and the user's report that AnyDesk clipboard synchronization is disabled.
- Produces: one fresh-challenge PASS/FAIL bounded to the observed Chrome/AnyDesk/Windows transport.

- [ ] **Step 1: Write and review the exact preflight brief**

Pin one random 128-bit challenge, one browser page, one fixed process, one baseline read, one copy, one comparison read, one post-clear read, `COPY_DONE|ABORT`, one timeout, exact cleanup, and zero retries. Obtain fresh Sol High direct-byte approval before running it.

- [ ] **Step 2: Execute once and stop on first mismatch**

Run no Cloudflare, credential, proxy, VM1205, Rulesets, Tunnel, DNS, key, model, or request action. Record labels and counters only; close the exact page and delete the exact-hash script in `finally`.

- [ ] **Step 3: Independently classify the result**

Require the review to state that PASS proves only the observed non-secret path and authorizes no token creation. A FAIL is retained without retry and does not block the separately reviewed secure-console design unless the reviewer finds a shared-process defect.

### Task 3: Prepare the exact one-shot credential live brief

**Files:**
- Create: `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-live-brief.md`
- Create: `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-live-report.md`
- Modify only after execution: `C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-team-api-offline\artifacts\omniroute-live-integration\evidence\team-api-verification.json`

**Interfaces:**
- Consumes: Task 1 PASS, existing 19-label proxy contract, existing exact-hash verifier/R5 artifacts.
- Produces: exact temporary-script bytes/hash, fixed labels and counters, timeout/cleanup path, and action-time checklist.

- [ ] **Step 1: Write the exact credential-free PowerShell owner script into the live brief**

The brief must pin one process, one `Read-Host -AsSecureString`, one Cloudflare verification request, the existing proof/R5 commands, and one `finally` path that calls `ZeroFreeBSTR`, disposes the secure value, clears variables, deletes only the exact-hash script, and exits. It must emit labels only and contain no credential placeholder that could be replaced into committed bytes.

- [ ] **Step 2: Run a credential-free parser and cleanup self-check**

Parse the exact script bytes with PowerShell's parser. Run only an `ABORT`/timeout fixture using a non-secret value and a temporary copy of the script. Verify one PID, zero HTTP requests, zero clipboard reads, exact script deletion, and no residual child process.

Expected: parser errors `0`; all cleanup labels `PASS`; live counters `0`.

- [ ] **Step 3: Obtain fresh Sol High live-brief approval**

The same independent role reviews direct bytes and confirms the brief implements the approved design without adding authority. Any concern stops before process or browser action.

### Task 4: Consume the reviewed credential gate once

**Files:**
- Modify: `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-live-report.md`
- Modify: `C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-team-api-offline\artifacts\omniroute-live-integration\evidence\team-api-verification.json`

**Interfaces:**
- Consumes: exact approved live brief, action-time confirmation, fixed evidence HEAD.
- Produces: one PASS evidence commit or one fail-closed incident commit; never both.

- [ ] **Step 1: Revalidate all preconditions read-only**

Require exact evidence HEAD, clean evidence worktree, immutable hashes, target proxy/tunnel/listener absence, exact target-token row count `0`, and zero drift. Any mismatch stops.

- [ ] **Step 2: Request the single action-time credential confirmation**

Name the final Cloudflare token creation and the user's one masked paste into the fixed visible terminal. Do not combine revocation, permission expansion, support transmission, or deletion authority.

- [ ] **Step 3: Execute the approved brief exactly once**

The Sol High owner starts one fixed process, the user performs the final Create/Copy/Paste manually, and the same process verifies and consumes the token through the existing proxy/R5 contract. Stop on the first mismatch.

- [ ] **Step 4: Commit and independently review exact evidence**

Stage only the evidence path with command-scoped identity. Verify direct bytes, redaction, parent, scope, counters, and working/commit equality. The Sol High evidence review issues PASS or preserves FAIL / NOT PROVEN without retry.
