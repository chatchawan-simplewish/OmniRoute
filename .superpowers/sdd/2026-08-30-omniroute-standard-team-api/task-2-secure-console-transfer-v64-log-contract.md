# V64 exact safe-log read-only inspection contract and plan

**Goal:** One bounded read of the exact V63 safe-log file after independent Sol
High PASS; retain only fixed/redacted historical status fields, never raw text.
**Architecture:** Exact-path metadata pins, one read-only no-follow native handle,
one 476-byte read, an all-or-nothing finite status parser, and sanitized evidence.
**Tech stack:** Pinned PowerShell 7.6.5, in-memory compiled C# Win32 interop,
repository-only synthetic tests and exact-path evidence commits.

## Authority and closures

Coordinator request authorizes a fresh independently reviewed read-only contract
to inspect only the exact V63 safe-log path/content. Output is limited to fixed or
redacted status fields. No token/secret value, cleanup, process, proxy/receiver,
Cloudflare, or VM action. Preserve V60-V63 closures and the 12 product baseline.
After PASS execute once, record evidence, report no more than five lines.

Sole owner: `/root/v60_receiver_gate_owner`, Sol High. Owned checkout:
`C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-agent-routing-source`.
Base: `0d83bee6f2499d8850e7b05b1646294931540d19`.
V60/V61/V62/V63 remain permanently closed. No old gate code is loaded or executed.
Historical source contributes only a finite vocabulary, never execution authority.

## Exact target and metadata pins

Only file:
`C:\Users\chatc\AppData\Local\Temp\omniroute-secure-console-9df5f87e00bc4a36b3133b32f4e095ba\omniroute-secure-console-safe.log`.
No directory inventory, sibling read, target search, alternate stream, or fallback.

V63 record `0d7ff86700911ace8cb81f55f34fb71f47fd9b89` supplied:

- parent root is the exact direct Temp child shown above, creation UTC
  `2026-09-03T14:41:21.7482409Z`, last-write UTC `2026-09-03T14:52:31.0363608Z`;
- file length 476, creation UTC `2026-09-03T14:42:30.2964752Z`, last-write UTC
  `2026-09-03T14:52:31.0440727Z`, regular non-reparse enumeration metadata;
- root owner matched the current Windows user, but file ownership, historical
  creator/process ownership, physical continuity, and cleanup remained unproven.

V64 freshly checks the exact root/file path, type, non-reparse attributes and
timestamps, plus the explicitly named Temp ancestry, before opening the file.
Those historical metadata matches are not proof of V63-to-V64 physical continuity.

## Exact package pins

All new files reside in `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/`.

| File | SHA-256 |
| --- | --- |
| `inspect-v64-log.ps1` | `F4AE15157FD8B7619D9E4DE3C76633A487158D3550CAF104F5C05BBED9CC1488` |
| `V64ExactReader.cs` | `EDD25482367C87F5904E18327D88A08AAC2A2ACF0ABD3E431596AD3FF4D4B061` |
| `test-v64-inspection.ps1` | `4363E9AE57E61E1AE28332740F1E494646078459AF14CC6498D677537769B569` |
| `v64-reader-fixture.txt` | `AEAAD409DA57DCA05027C2399EB52BC2F264841E33982F7E9513BF4AE10C7EC1` |

Runtime absolute path:
`C:\Users\chatc\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\powershell\pwsh.exe`;
301368 bytes, FileVersion `7.6.5.500`, SHA-256
`362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139`,
Authenticode Valid, signer exactly
`CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US`.
The script checks actual `$PSHOME`, runtime pins, and native-helper source hash
before compiling the helper in memory or accessing the target. No runtime changes.

## One-handle read boundary

`V64ExactReader.ReadExact(path, creationFileTime, lastWriteFileTime)` is called
once for the fixed live pathname; tests call it only for the committed non-secret
476-byte fixture. It opens one existing file with `GENERIC_READ`,
`FILE_SHARE_READ` only, and `FILE_FLAG_OPEN_REPARSE_POINT`. No write/delete access,
creation, truncation, delete-on-close, writable mapping, or retry exists.
An incompatible existing writer causes a fail-closed open error, not process
inspection or termination. The short-lived handle allows other readers only.

Before any bytes are read, require the normalized final handle path to equal the
exact `\\?\`-prefixed requested path, disk file type, no directory/reparse/offline
attributes, exactly one hard link, 476-byte size, and matching creation/write times.
One `ReadFile` call requests exactly 476 bytes and must return exactly 476.
Recheck handle metadata and final path after the read, including volume/file ID
and attribute equality. Any discrepancy suppresses the entire result.
The handle is disposed on every path. No dynamic path, ID, or OS error is emitted.

These guards bind the handle for this read, not a historical creator or current
process. Filesystem or privileged concurrent changes cannot be converted into
historical provenance by matching timestamps. No cleanup authority follows.

API behavior was checked against primary Microsoft documentation:
[CreateFileW](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew),
[GetFinalPathNameByHandleW](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getfinalpathnamebyhandlew),
[GetFileInformationByHandle](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getfileinformationbyhandle).

## Non-disclosing parser contract

`Get-V64StatusSummary([byte[]] Bytes)` accepts at most 476 bytes, strict UTF-8,
optional leading BOM, printable ASCII status text plus CR/LF, at most 32 lines
and 160 characters per line. It never executes or interprets log text as code.
The source contains the exact finite key/value table, drawn from the historical
owner `Write-Safe` statements in `task-2-secure-console-transfer-live-brief.md`.
Only complete exact table matches can enter output; values are copied from that
static table, not from arbitrary log substrings. Numeric PID input is discarded
and replaced by `OWNER_PID=PRESENT_REDACTED`; the expected token row name is
replaced by `EXPECTED_NAME_REDACTED`. Neither grants process/provider authority.

The bounded vocabulary covers readiness, clipboard counters, verification/lookup
counters, R5 counters/results/residual status, invalidity and script-deletion
counters, error enums, terminal owner result, and revocation-status enums.
Counter strings are explicit finite table entries, not arbitrary numeric captures.
An `OWNER_RESULT` field must be present. Duplicate keys, unknown lines/values,
extra blank lines, malformed UTF-8, controls, oversized input, or missing terminal
result reject the entire parse: `Grammar=REJECTED_REDACTED`, empty fields.
There is no partial status output or raw rejected-text excerpt, hash, encoding
fallback, alternate parser, second read, or manual interpretation of errors.

Accepted output is `V64_CLOSED_STATUS_INSPECTED`, `Grammar=ALLOWLIST_ONLY`, fixed
historical fields, `ReadBound=476_BYTES_ONCE`, `RawOutput=SUPPRESSED`, and fixed
NOT_PROVEN live-state/provenance/cleanup limits. A rejected parse is
`V64_CLOSED_REDACTED_CONTENT_UNCERTAIN` (exit 2); other failures are
`V64_CLOSED_STOP_UNCERTAIN` (exit 1) with a fixed stage only. Never emit an exception
message, native error code, line contents, token, secret, PID value, or log hash.

Raw bytes stay only in the local short-lived process and are cleared in `finally`
before JSON output; native failure buffers are also cleared. Raw managed-string
references are dropped. This is not a claim of forensic memory zeroization.
No transcript, raw evidence copy, debug output, screenshot, or clipboard access.
Even entirely allowlisted text is an unauthenticated historical log claim, not
proof that its claimed actions occurred or that credentials are currently safe.

## Test-first preparation and independent review

- [x] Parser RED: valid known status failed against the placeholder parser.
- [x] Parser GREEN: 11 cases, including safe statuses, PID redaction, injected
  synthetic private markers, duplicate/invalid/missing fields, oversized/blank
  input and malformed UTF-8. No live residual access.
- [x] Native reader RED: stub rejected the known repository fixture.
- [x] Native reader GREEN: exact 476-byte fixture read, timestamp mismatch
  rejection, and rejection while a write-capable fixture handle is held. The
  fixture writer performs no writes and is disposed; no live process action.
- [ ] Commit the five candidate files (contract, script, native source, test,
  fixture) and obtain independent read-only Sol High PASS on exact bytes with
  no unresolved findings. Reviewer does not access target or rerun passing tests
  without a specific doubt. Record verdict verbatim in a separate review file.
- [ ] Commit an execution record marked
  `V64_STATE=SPENT_LOG_INSPECTION_ATTEMPT_RESERVED` before invocation. No target
  access may occur before PASS and this reservation.
- [ ] Immediately revalidate exact checkout/HEAD, base ancestry, empty index,
  all five reviewed candidate hashes, only those files plus separate V64 review
  and execution records changed since base, exact 12 dirty status entries, and
  all 12 hashes in `task-2-secure-console-transfer-v61-product-baseline.json`.
- [ ] Run once in the owned worktree through the pinned shell, `login=false`,
  no profile, at most 30000ms tool wait:

```powershell
& '.\.superpowers\sdd\2026-08-30-omniroute-standard-team-api\inspect-v64-log.ps1'
```

Any failure, drift, sharing conflict, incomplete receipt, interruption or timeout
spends V64 permanently. A returned running session may only be read for completion;
never inject another command or retry. Do not relax a pin or inspect raw errors.
- [ ] Commit only sanitized receipt and limits; obtain independent Sol High
  evidence/disposition review; verify baseline and report no more than five lines.

## Final boundary

All outcomes close V64. Leave the log and directory untouched; no cleanup,
rename/move/delete, permission change, process enumeration/control, receiver/proxy
start, credential use/transmission, browser/Cloudflare, SSH/VM/provider action,
push, archive, root-file edit, or product change. Only the exact file bytes are
read privately; only fixed/redacted status evidence is retained in the owned
worktree. V60-V63 remain closed. Further action needs a fresh reviewed contract.
