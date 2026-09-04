# V62 exact-target residual identification and disposition contract

State: DRAFT_PENDING_INDEPENDENT_SOL_HIGH_REVIEW. No execution yet.

## Authority and sole ownership

The coordinator explicitly authorized a new V62 read-only exact-target
identification/disposition contract for the single count-only prepared-temp
candidate, independently reviewed before one non-destructive identification.
Sole writer and gate owner: `/root/v60_receiver_gate_owner` (Sol High).
Owned checkout:
`C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-agent-routing-source`.
Base: `893563137ea4f866b00c793831208b139f0404b3`.
V60 and V61 remain permanently closed. No prior gate, cleanup helper, scope
replacement, receiver or launch code is imported, executed, or reauthorized.

The V61 stop report at `750d4d8d22e33ecea96bff674524a44371370087`
records exactly one count-only match. This is historical context, not current
identity or permission to open any residual. V62 does not infer that today's
match is physically the same object as the V61 match.

## Exact target discovery boundary

The target is initially UNKNOWN. No candidate opening, metadata inspection,
content inspection, copying, persistent retention, or cleanup precedes the
binding below. Candidate path strings exist ephemerally only for validation.

1. Confirm bundled PowerShell runtime identity and pinned Windows temp parent.
   Inspect only parent and its explicitly named ancestors for directory type
   and absence of reparse points.
2. Exactly once, enumerate matching immediate directory entry paths under
   `C:\Users\chatc\AppData\Local\Temp`, using only filter
   `omniroute-secure-console-*` and `TopDirectoryOnly`. Do not recurse, read
   candidate contents, output candidate arrays, or rank/select a newest item.
3. The pure validator requires exactly one entry, a fully qualified unchanged
   canonical path, an exact direct parent match (ordinal-ignore-case), and a
   case-sensitive leaf matching `^omniroute-secure-console-[0-9a-f]{32}$`.
   An invalid or ambiguous entry closes V62; do not output its name or path.
4. Only after that exact-path binding, perform one literal `Get-Item` for the
   target's own metadata. Require directory, non-reparse, and ordinal-exact
   full path. Emit only validated path, directory/reparse flags, UTC creation
   and last-write timestamps, and fixed NOT_PROVEN/NOT_INSPECTED fields.
5. Do not enumerate immediate children. Never read residual file bytes, hash
   residual files, read ACLs, enumerate processes, or associate an owner.

This proves a pathname and metadata snapshot only. It does not obtain a stable
file ID or open a retained handle. Concurrent replacement cannot be excluded;
physical identity, ownership, credential status, process association, contents,
and cleanup eligibility all remain NOT PROVEN. No content is opened through
the target even if a metadata race occurs. Future action must freshly bind the
exact object under a separate independently reviewed contract.

## Executable and validation pins

All package files are in `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/`.

| File | SHA-256 |
| --- | --- |
| `identify-v62-residual.ps1` | `EBD7B38BBDAA4EA9AC8F2CF5F4E5A2ECD37EA74121DC6F535FCFDE608A3D333B` |
| `test-v62-target.ps1` | `EEA0A048F151C4F0094F881A42649705CA7209919B5865B96B57A98741229C0A` |

Runtime absolute path:
`C:\Users\chatc\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\powershell\pwsh.exe`.
Length 301368; FileVersion `7.6.5.500`; SHA-256
`362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139`;
Authenticode Valid; signer exactly
`CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US`.
The script verifies its own `$PSHOME` runtime path and these current pins before
directory inventory. The trusted local tool shell also uses this explicit
runtime with `login=false` and no profile. Any mismatch closes V62, no fallback.

The validator test extracts only the named function AST, parses the entire
source without executing it, and runs nine literal synthetic-path cases. It
does not dot-source the executable body or enumerate any live directory.
Test-first RED: stub rejected the valid direct path with
`V62_TARGET_VALIDATION_NOT_IMPLEMENTED` (exit 1).
GREEN: `V62_PURE_TARGET_TEST=PASS CASES=9 LIVE_INVENTORY=0` (exit 0).

## Independent review and action-time pins

Before execution, a separate Sol High reviewer must inspect exact committed
contract, script, and test bytes and return explicit PASS with zero unresolved
findings. Reviewer is read-only and performs no live residual discovery.
The sole owner records that verdict verbatim in a separate review artifact.
Review PASS is necessary, not proof the target exists or that runtime pins match.

Immediately before invocation, the owner must prove the checkout absolute path,
base ancestry, empty index, executable and test hashes above, and preservation
of all 12 product hashes from `task-2-secure-console-transfer-v61-product-baseline.json`.
Only the three V62 candidate files and separate V62 review/execution/disposition
records may differ from the base in committed history. Preserve the same 12
dirty status entries; no product edits or broad staging. Record a durable
`V62_STATE=SPENT_IDENTIFICATION_ATTEMPT_RESERVED` in the V62 execution record
before the one invocation; an interrupted/uncertain invocation stays spent.
Such documentation commits do not permit executable/contract drift after PASS.

One invocation only, by the sole owner using the pinned shell, working directory
above, `login=false`, and at most 30000ms tool wait:

```powershell
& '.\.superpowers\sdd\2026-08-30-omniroute-standard-team-api\identify-v62-residual.ps1'
```

No second inventory, rerun, recovery command, fallback, verdict relaxation,
candidate-name guessing, or manual integration. A tool exception, timeout,
truncated/uncertain receipt, runtime mismatch, path ambiguity, disappearance,
unexpected name, count other than one, or reparse point closes V62. Record fixed
failure status only; do not print exception details or unvalidated paths.
Never rerun to obtain a more informative error. A returned asynchronous session
may be read for completion only, never fed another command or used to retry.

## Disposition and evidence

Success means `V62_CLOSED_IDENTIFIED_PATH_ONLY`, not cleanup or receiver readiness.
Retain only the validated path and allowed metadata in the owned worktree's V62
execution report. Failure means `V62_CLOSED_STOP_UNCERTAIN`; target not retained.
The command deliberately suppresses detailed exceptions. If it fails, diagnosis
requires new authority, not inspecting shell errors or enumerating again.
Both outcomes spend V62 permanently. No rollback is needed: target is untouched.

No residual rename, move, deletion, write, retention copy, file stream, recursive
scan, receiver/proxy start, clipboard action, credential inspection/transmission,
Cloudflare/browser action, SSH/VM action, or provider mutation is authorized.
Only owned-worktree contract/script/test/review/evidence writes and exact-path
commits are allowed; the named coordinator handoff may receive a concise status
append if needed. No other shared project-root edit; no push or archive.

Next after either outcome is a report to the coordinator. Any ownership/content
inspection or disposition beyond leaving the object untouched needs a fresh
exact-target reviewed contract. Any future receiver launch needs a separate new
replacement contract and never reopens V60, V61, or V62.
