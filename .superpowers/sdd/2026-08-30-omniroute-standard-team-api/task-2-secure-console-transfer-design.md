# Task 2 secure-console credential transfer design

Status: proposed replacement contract; review only; no live execution authorized

## Decision

Use one fixed, visible PowerShell 7 owner process with masked console input. The
Cloudflare token must never pass through an agent tool, browser inspection,
clipboard-reading command, file, command line, environment inherited by another
process, report, or Git artifact.

This is a separately reviewed secure-input channel. It does not claim that a
local canary proves Cloudflare copy-control semantics, and it permanently
retires the rejected Chrome-native data-page canary.

Alternatives rejected:

- Treating any generic browser clipboard canary as proof of the later
  Cloudflare copy control is rejected. A corrected non-secret transport
  preflight may run only with the bounded conclusion defined below.
- Creating the token through an existing API credential adds a second secret
  and a new authority path that is not part of the approved plan.

## Bounded AnyDesk clipboard preflight

The user reports that AnyDesk clipboard synchronization is now disabled and
has explicitly requested one new clipboard test. After this design receives a
fresh Sol High PASS, one corrected non-secret preflight may test only the
current Chrome-to-Windows clipboard transport:

1. One fixed PowerShell process clears the Windows clipboard, performs one
   shape-only baseline read proving empty, generates a fresh random 128-bit
   challenge, and emits the non-secret challenge plus `OWNER_READY=PASS`.
2. One local browser page contains that fresh challenge in one readonly input.
   The exact input is focused once, followed by one `Control+A` and one
   `Control+C`. No static expected value is permitted.
3. The process accepts exactly one control line: `COPY_DONE` or `ABORT`.
   `ABORT`, EOF, or timeout performs zero comparison reads and enters cleanup.
4. On `COPY_DONE`, the process performs one comparison read, compares internally
   without echoing clipboard content, clears the clipboard, performs one
   shape-only post-clear read, deletes only its exact-hash script, and exits.
5. Counters are executable: one transfer attempt; at most three clipboard reads
   (baseline, comparison, post-clear); two cleanup writes; one process; one
   page; zero retries; zero browser clipboard API calls.

A PASS proves only that this fresh challenge crossed the observed local
Chrome/AnyDesk/Windows path at that time. It does not prove Cloudflare copy-button
semantics and does not authorize token creation. The later credential still
uses the separately reviewed masked console-input channel below.

## Authority boundaries

- This design and its review are credential-free and may proceed unattended.
- A fresh independent Sol High PASS is required before any process, browser,
  Cloudflare, VM1205, proxy, Rulesets, Tunnel, DNS, key, model, or request action.
- At execution time, obtain one explicit confirmation naming token creation and
  masked credential submission. That confirmation does not authorize deletion,
  permission expansion, retry, fallback, or a second token.
- Any revocation, support transmission, permission change, or deletion requires
  its own action-time confirmation.
- The one-shot gate and its evidence review remain in the sole Sol High owner
  task and must not be delegated.

## Fixed process and channel

1. Revalidate the clean evidence worktree at
   `80adaa7d5d63d1d2c7bfa63b236c6bee93b3b1d8`, all immutable review hashes,
   exact target-resource absence, and zero new target-token rows.
2. Create one credential-free UTF-8/LF/no-BOM temporary `.ps1` under a validated
   temporary directory. Record its exact path, SHA-256, size, and expected PID
   contract before token creation.
3. Start exactly one visible PowerShell 7 process from that script. Retain its
   process handle and PID. It emits only fixed labels including
   `OWNER_READY=PASS`, `OWNER_PID=<pid>`, and `SECRET_PROMPT_READY=PASS`.
4. The process calls `Read-Host -AsSecureString` exactly once. Input is masked;
   the process never echoes, measures publicly, hashes, logs, or returns the
   submitted value. Agent tools must not send the input.
5. After action-time confirmation, the user physically completes the final
   Cloudflare Create action, uses the page's native Copy control, switches to
   the visible owner terminal, pastes into the masked prompt, and submits once.
   No agent browser call is permitted after the final Create action until the
   token has been cleared or revoked and the token-bearing page is closed.
6. The fixed process converts the `SecureString` to plaintext only inside its
   own scope and only immediately before the reviewed Cloudflare verification
   request. It accepts only an active-token verification response with the
   expected response shape. It emits status labels only.
7. On acceptance, the same fixed process retains sole credential ownership and
   continues the already approved 19-label proxy proof and deterministic R5
   child contract. It must not relay the token to another process or session.
8. In `finally`, zero and free the unmanaged plaintext buffer, dispose the
   secure value, clear all header/token variables, delete only the exact-hash
   temporary script, and verify the fixed process exits. The report records
   labels and counters only.

## Freshness and binding

Before token creation, prove refreshed exact target-token name count `0`. Use a
new unique token name fixed in the reviewed live brief. After the user submits
the secret, require all of the following without displaying the value:

- exactly one final Create action and one exact target-token row;
- the fixed PID equals the retained process PID;
- the verification endpoint reports the submitted token active;
- no pre-existing credential source, environment value, or token file exists;
- exactly one masked submission occurred after `SECRET_PROMPT_READY=PASS`.

These checks bind the accepted credential to the single fresh creation event
without claiming that clipboard state itself is evidence.

## Abort, timeout, and failure

- The secret prompt has one reviewed bounded timeout. EOF, cancellation,
  timeout, empty input, invalid response shape, non-active verification, PID
  mismatch, browser ambiguity, or any missing label is FAIL / NOT PROVEN.
- Failure enters the same `finally` cleanup path. There is no second prompt,
  process, token, paste, verification request, proxy start, proof, R5 child, or
  alternate bridge.
- If a token row was created, stop and request action-time confirmation for one
  exact-row revocation. Do not continue the gate after revocation.
- Preserve every prior FAIL and NOT PROVEN fact. Never reinterpret cleanup as
  acceptance evidence.

## Structural counters

- Fixed PowerShell processes: exactly 1
- Non-secret preflight processes/pages/attempts: at most 1 / at most 1 / at most 1
- Non-secret preflight clipboard reads/writes: at most 3 / at most 2
- Masked secret prompts/submissions: exactly 1 / at most 1
- Agent-visible secret values: 0
- Browser snapshots/screenshots/DOM or page-content reads after creation: 0
- Credential-stage clipboard reads/writes by agent or fixed process: 0 / 0
- Token creations: at most 1
- Token verification requests: at most 1
- Proxy starts/proofs/restarts: at most 1 / at most 1 / 0
- R5 children/Rulesets POSTs/attributable DELETEs: at most 1 / at most 1 / at most 1
- Retries/fallbacks/alternate bridges/session handoffs: 0

## Evidence contract

Add one `secure_console_transfer` object to the existing evidence JSON. It may
contain only the reviewed contract hash, script hash/size, fixed PID, bounded
timestamps, status labels, counters, verification status, cleanup status, and
`authorizes_live_execution=false` for the design-review commit. Preserve every
existing incident field byte-for-byte except a strictly required schema-version
increment and the additive object.

For any later live evidence commit, require exact-path staging, command-scoped
Git identity, direct committed-byte UTF-8/redaction review, exact parent/scope,
and working/committed equality. Never include a credential, authorization
header, account/zone/rule identifier, page serialization, clipboard content,
or user keystroke.

## Acceptance

The design is review-clean only if a fresh independent Sol High reviewer finds
no HIGH concern and explicitly confirms that the secure-console path replaces
the rejected canary without weakening one-shot ownership, freshness, cleanup,
or evidence requirements. A design PASS authorizes preparation of the exact
live brief only; it does not authorize token creation or execution.
