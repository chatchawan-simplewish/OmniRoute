# V63 exact residual metadata inspection contract and implementation plan

**Goal:** Inspect the smallest read-only ownership/cleanup-eligibility evidence
for the exact V62 directory, after independent Sol High PASS, without cleanup.
**Architecture:** One exact-root metadata check, root owner SID read, and one
nonrecursive child-metadata enumeration; pure output sanitizer; no file bytes.
**Tech stack:** Pinned bundled PowerShell 7.6.5, Windows filesystem metadata,
repository-only evidence and exact-path Git commits.

## Global constraints and authority

Coordinator request: create a fresh independently reviewed residual inspection
contract for the exact V62 directory, inspecting only the smallest metadata/content
evidence needed to determine ownership and cleanup eligibility; no cleanup,
process action, proxy/receiver/credential/Cloudflare/VM action. Preserve V60/V61/V62
closures and 12 product dirty baseline. Execute read-only inspection after PASS.

Sole owner: `/root/v60_receiver_gate_owner`, Sol High. Sole owned checkout:
`C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-agent-routing-source`.
Base: `ee6042702b51b9319aa5ccf26e51bb0ecff747fd`.
No other agent may consume V63; reviewer is independent read-only Sol High.
All prior gates remain permanently closed, with no old cleanup/launch function
loaded or executed. This contract is not receiver or cleanup authority.

## Exact target and smallest-evidence decision

Only target:
`C:\Users\chatc\AppData\Local\Temp\omniroute-secure-console-9df5f87e00bc4a36b3133b32f4e095ba`.
V62's reviewed execution record at `9e89116deddd366d6e8158ae22cf3cd58723efa3`
established only that pathname and a directory/non-reparse metadata snapshot:
creation UTC `2026-09-03T14:41:21.7482409Z`, last-write UTC
`2026-09-03T14:52:31.0363608Z`.
V63 requires fresh exact path/type/non-reparse/timestamp matches before any ACL
read or child enumeration. No wildcard parent inventory or target rediscovery.

Root owner SID is sufficient to identify the observed filesystem security owner;
it cannot prove who created the directory or which execution owns it. Immediate
child metadata can identify shape, unknown entries, and visible blockers without
opening any log or script. Content reading is therefore not needed in V63.
This intentionally narrows the optional metadata/content permission to metadata.
Script hashes/contents, child ACLs, process inspection, and log parsing are omitted.
They would not alone prove safe cleanup, and content is not known secret-free.

The cleanup-eligibility determination remains **NOT PROVEN; leave untouched**
unless separately authorized future evidence establishes all missing conditions.
This is a bounded inspection outcome, not a promise to prove positive eligibility.
Filesystem ownership, creator/process ownership, script identity, physical-object
continuity, and deletion authorization must never be conflated.

## Reviewed executable and test

Package directory: `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/`.

| File | Responsibility | SHA-256 |
| --- | --- | --- |
| `inspect-v63-residual.ps1` | sole one-shot inspection | `2C3D30AF89DD4B5C44F9299E869B88D5A046606DB885D7E304E916A26C764F98` |
| `test-v63-summary.ps1` | pure synthetic sanitizer tests only | `689BAC7B5DB8341C762A8B46349DEE178914487A5290FF0C5ED60D9831E46B81` |

Runtime:
`C:\Users\chatc\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\powershell\pwsh.exe`;
301368 bytes; FileVersion `7.6.5.500`; SHA-256
`362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139`;
Authenticode Valid; signer exactly
`CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US`.
Script checks its current `$PSHOME` runtime path and all those pins before target
access. Execute through that exact shell with `login=false`, no profile.

Pure interface: `Get-V63ChildSummary([string] Root, [object[]] Children)` consumes
synthetic or enumerated directory-entry metadata and produces counts plus safe
metadata for these exact allowlisted filenames only:

- `omniroute-secure-console-owner.ps1` -> fixed label `OWNER_SCRIPT`;
- `omniroute-r5-exact.ps1` -> fixed label `R5_SCRIPT`;
- `omniroute-secure-console-safe.log` -> fixed label `SAFE_LOG`.

These labels describe expected roles only, not proven content. Unknown names are
suppressed and counted; known entries with wrong full path, directory type, or
reparse attributes are counted as unsafe and omitted from detailed output.
Accepted entries emit only fixed label, byte length, creation and last-write UTC.
No filename, error message, or arbitrary property is emitted from unknown input.

## Ordered one-shot operation

1. Validate runtime and exact temp-parent binding. Check explicitly named ancestor
   directories (`C:\`, Users, chatc, AppData, Local, Temp) are not reparse points.
2. One literal `Get-Item` for the exact target; require matching V62 timestamps,
   directory/non-reparse flags, and ordinal-exact pathname.
3. One `Get-Acl -LiteralPath` for the root only; derive only its owner SID.
   Read the executing Windows identity SID only to output an equality boolean.
   Never emit other ACL entries, account names, groups, tokens, or environment.
4. One `Get-ChildItem -LiteralPath target -Force`, no recursion. Sanitize metadata
   with the pure helper. Do not open any child or follow any child reparse point.
5. Emit one compact JSON result with root owner SID, owner-match boolean,
   sanitized child metadata, and explicit NOT_READ/NOT_PROVEN limits. Unknown
   entries do not permit inspection or retries; they are counted as blockers.
6. Permanently close V63 and record only that returned evidence. Any exception
   emits only a fixed state, fixed stage label, no-retry flag, and unproven cleanup
   disposition; never emit raw exception details or candidate content.

No stable file ID/retained handle is obtained. Timestamp equality is not proof of
physical identity, and concurrent metadata replacement cannot be ruled out.
The output is a best-effort pathname-based snapshot only, not sufficient for any
deletion or subsequent opening. No file bytes are read even if a metadata race
occurs. Do not strengthen identity/ownership claims from a successful exit.

## Review, reservation, and action-time source pins

- [x] Write pure sanitizer test; observe RED against the unimplemented summary
  (`V63_SUMMARY_NOT_IMPLEMENTED`, exit 1), then implement minimal sanitizer.
- [x] Run pure tests: `V63_PURE_METADATA_TEST=PASS CASES=6 LIVE_TARGET_ACCESS=0`.
  Cases exercise known metadata, unknown-name suppression, outside-root paths,
  reparse files, directories, and empty input. The test extracts only the function
  AST and never executes the live body or accesses the residual.
- [ ] Commit this contract, executable, and test. Separate Sol High reviewer
  inspects exact committed bytes and returns PASS with no unresolved findings.
  Reviewer runs no live inventory or target access and no repeat passing suite
  without naming a specific doubt. Record verdict verbatim in a separate file.
- [ ] Before the sole invocation, create and commit an execution record marked
  `V63_STATE=SPENT_INSPECTION_ATTEMPT_RESERVED`; interruptions remain spent.
- [ ] Revalidate exact checkout/HEAD, base ancestry, empty index, reviewed package
  hashes, and only the three V63 candidate files plus separate V63 review and
  execution records changed since base. Preserve the exact 12 dirty status entries
  and all hashes in `task-2-secure-console-transfer-v61-product-baseline.json`.
- [ ] Invoke exactly once using the pinned runtime and owned working directory:

```powershell
& '.\.superpowers\sdd\2026-08-30-omniroute-standard-team-api\inspect-v63-residual.ps1'
```

At most 30000ms tool wait; a returned running session may be read only for its
completion, never sent another command. No second inventory, rerun, fallback,
target change, timestamp relaxation, old-gate reuse, or exception-driven probing.
Any failed pin, disappearance, metadata drift, uncertainty, timeout or incomplete
receipt closes V63 without attempting a different inspection.

- [ ] Retain complete sanitized receipt and explicit limitations, commit exact
  evidence paths, obtain independent Sol High evidence/disposition review, and
  report to the coordinator in at most five lines.

## Disposition boundary

Both `V63_CLOSED_METADATA_INSPECTED` and `V63_CLOSED_STOP_UNCERTAIN` permanently
spend V63. Neither grants cleanup eligibility or further authority. Leave the
exact residual untouched. No rename/move/delete, contents/hash/stream access,
retention copy, process enumeration/control, receiver/proxy start, clipboard,
credential inspection/transmission, browser/Cloudflare, SSH/VM/provider action,
runtime change, push, archive, or unrelated filesystem scan is allowed.
Only owned-worktree V63 source/test/review/evidence writes and exact-path commits
are permitted. Do not modify product files or any shared project-root file.
Further inspection or cleanup requires a fresh independently reviewed exact-target
contract; V60/V61/V62 remain closed throughout and afterward.
