# V65 current-state/provenance cleanup-eligibility contract and plan

**Goal:** Make a bounded, independently reviewed read-only eligibility decision
for the exact residual/log; establish sufficient evidence or explicitly reject
cleanup eligibility. No cleanup or mutation follows either outcome.
**Architecture:** Current exact metadata and filesystem-owner checks plus a
pinned documentary provenance check, followed by a fail-closed pure decision.
**Tech stack:** Pinned PowerShell 7.6.5, filesystem metadata, immutable Git evidence.

## Authority, owner, and prior closures

Coordinator authorizes fresh independently reviewed read-only current-state and
provenance checks sufficient to establish or reject cleanup eligibility for the
exact V62 residual/log. No cleaning or mutation; no process/proxy/receiver/token/
Cloudflare/VM action beyond bounded read-only checks explicitly reviewed.
Sole writer and gate owner: `/root/v60_receiver_gate_owner`, Sol High.
Owned checkout:
`C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-agent-routing-source`.
Base `86dbe9b975469b5ab477a4cc42db8690d8a0a02a`.
V60/V61/V62/V63/V64 remain permanently closed. No old executable gate is reused.
Only new V65 documentation, script, test, and evidence files may change.

## Eligibility policy and bounded conclusion

Current filesystem ownership is not operational ownership. A log containing
expected statuses is not an authenticated record that the named lifecycle ended.
Before positive cleanup eligibility could be accepted, evidence would need to
bind the exact target to its authorized preparation/owner lifecycle and establish
its safe disposition. The existing independently reviewed records explicitly
do not provide that binding: V62 pathname only, V63 filesystem metadata, V64
unauthenticated historical status claims with PID redacted.

A repository-only drafting check found no occurrence of the exact root suffix in
the pre-V62 evidence snapshot at `893563137ea4f866b00c793831208b139f0404b3`.
This is a scoped absence, not proof that no record exists anywhere. V65 repeats
that immutable-snapshot check in its reserved run. No task-history database,
uncommitted private logs, other checkout, arbitrary filesystem, or browser is
searched. No out-of-scope evidence absence is asserted.

If current shape and owners match but that origin binding remains unestablished,
the correct V65 decision is **REJECT_MISSING_AUTHORITATIVE_ORIGIN_BINDING**.
This is an explicit rejection of cleanup eligibility under this evidence policy,
not a claim that the file is malicious, contains a credential, or has a live owner.
A future independently reviewed retention/disposition plan may handle unknown
origin differently; V65 cannot silently adopt that materially different policy.

Positive eligibility is not fabricated from a matching owner or quiet-looking
log. If the scoped search unexpectedly finds a reference, stop with
`STOP_NEW_PROVENANCE_REQUIRES_REVIEW` instead of opening or interpreting it under
this contract. That reference alone is not a verified lifecycle binding either.
Missing provenance is sufficient to reject the current cleanup request; therefore
no PID derivation, log reread, process lookup, handle probe, credential/provider
check, or broader search is necessary or authorized in V65.

## Exact live scope and pins

Directory:
`C:\Users\chatc\AppData\Local\Temp\omniroute-secure-console-9df5f87e00bc4a36b3133b32f4e095ba`.
Only child permitted in the expected snapshot:
`omniroute-secure-console-safe.log` (literal direct child of that exact directory).
Directory creation UTC `2026-09-03T14:41:21.7482409Z`, last-write UTC
`2026-09-03T14:52:31.0363608Z`.
File length 476, creation UTC `2026-09-03T14:42:30.2964752Z`, last-write UTC
`2026-09-03T14:52:31.0440727Z`.
Expected current-user SID from V63:
`S-1-5-21-2948832038-1864667924-1544628304-1001`.
No alternate path, timestamp relaxation, reparse traversal, content open, or hash.

Runtime:
`C:\Users\chatc\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\powershell\pwsh.exe`;
301368 bytes, FileVersion `7.6.5.500`, SHA-256
`362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139`,
Authenticode Valid, exact signer
`CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US`.
Script checks actual `$PSHOME` and these runtime pins before live target access.

New package in `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/`:

| File | SHA-256 |
| --- | --- |
| `check-v65-eligibility.ps1` | `75EA024355D1C528ED52C013FD89596A235E2A5DF1E16D7B7ED883606DBDC335` |
| `test-v65-eligibility.ps1` | `C386340ABD5A12DCFA3D0649A859EBECFCF93230621D60F1E0C24D657662883F` |

## Exact reserved read-only sequence

1. Validate runtime. Set process-local `GIT_NO_REPLACE_OBJECTS=1`, then one quiet
   fixed-string Git search for the exact root suffix in only the pinned pre-V62
   evidence-directory tree. Exit 1 means scoped absence, exit 0 means reference
   detected, other exit codes fail closed. Suppress native stderr and all matches.
2. Validate resolved Temp parent and explicitly named ancestors (`C:\`, Users,
   chatc, AppData, Local, Temp) are directories without reparse attributes.
3. One literal metadata read for the exact directory and one for the exact log;
   require ordinal-exact paths, directory/file types, no reparse flags, and the
   historical timestamps/length above. Any drift closes V65 immediately.
4. One nonrecursive `Get-ChildItem -LiteralPath` for the directory. Determine only
   whether there is exactly one regular non-reparse child at the exact log path.
   Do not output unknown names, recurse, or open any child content.
5. Read the root and log ACLs once each, deriving only owner SIDs internally.
   Compare each to the expected current-user SID; emit only booleans. No ACL
   entries, account names, SID values, process metadata, or environment values
   appear in output. These owner reads do not establish access-control provenance.
6. Apply `Get-V65Eligibility(ShapeMatches,RootOwnerMatches,LogOwnerMatches,
   OriginReferenceAbsent)`: wrong shape -> `REJECT_CURRENT_SHAPE`; either owner
   mismatch -> `REJECT_FILESYSTEM_OWNER_MISMATCH`; absent origin ->
   `REJECT_MISSING_AUTHORITATIVE_ORIGIN_BINDING`; otherwise stop for new review.
7. Emit fixed decision/status fields only, including search scope, no content
   reread/process checks, unestablished lifecycle binding, and leave-untouched
   disposition. No positive cleanup authority is emitted. Permanently close V65.

These pathname-based checks are snapshots, not a retained physical-object handle
or proof against concurrent replacement. No current process/provider state is
queried or inferred. Any exception emits only a fixed stage, no-retry marker,
rejected eligibility and leave-untouched disposition; raw errors are suppressed.

## Test, review, reservation, and execution

- [x] Test-first RED: placeholder incorrectly classified the missing-origin case;
  test failed with `V65_MISSING_ORIGIN_ACCEPTED` before implementation.
- [x] GREEN: five pure cases cover missing origin, shape drift, root/file owner
  mismatch, and newly detected unreviewed provenance. Parser checks the complete
  source; test extracts only the pure function and performs no target access.
- [ ] Commit contract/script/test and obtain independent read-only Sol High PASS
  on exact bytes, zero unresolved findings. Reviewer does not access live target,
  look up a PID, or rerun passing tests without a concrete doubt.
- [ ] Record review verbatim and commit an execution reservation:
  `V65_STATE=SPENT_ELIGIBILITY_ATTEMPT_RESERVED` before target access.
- [ ] Immediately revalidate exact checkout/HEAD, base ancestry, empty index,
  reviewed contract/script/test hashes, only these three candidates plus V65
  review/execution records changed from base, original 12 dirty status entries,
  and all hashes in `task-2-secure-console-transfer-v61-product-baseline.json`.
- [ ] Invoke once in the owned worktree using the exact pinned shell, no profile,
  `login=false`, at most 30000ms tool wait:

```powershell
& '.\.superpowers\sdd\2026-08-30-omniroute-standard-team-api\check-v65-eligibility.ps1'
```

No rerun, second listing, fallback, raw error inspection, source/target change, or
relaxed verdict. A returned running session may only be read for completion.
Failed pins, timeout, uncertainty or interruption permanently spend V65.
- [ ] Retain sanitized receipt and explicit scope/limits, commit exact evidence,
  obtain independent Sol High evidence/disposition review, recheck baseline and
  report the concrete eligibility decision to the coordinator.

## Final boundary

Both completed decision and uncertain stop reject cleanup eligibility under V65.
Leave the directory/log untouched. No cleanup, mutation, rename/move/delete,
permission change, file-content/hash read, process enumeration/control, proxy/
receiver start, token/clipboard action, browser/Cloudflare, SSH/VM/provider action,
archive, push, shared-root edit, or product edit. Only owned-worktree V65 artifacts
and exact-path commits change. V60-V64 remain closed. Further action requires a
fresh reviewed contract; no manual confirmation is added for these read-only checks.
