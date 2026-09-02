# OmniRoute V40 ordered selected-tab reacquisition fix round 1 — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only fix-round commit
`b782e09e61e95a73a3932e3b0bd64ab52b488786`, its direct parent and original
FAIL review `13fcd03f8f0f7345e240b9f1453d1a1c62abbfba`, and the unchanged V40
fixture needed to verify the corrected brief.

I reviewed the exact one-path diff, final-byte shape, unchanged executable,
committed fixture result, and every semantic boundary accepted in the original
review. I ran only the committed V40 pure fixture and scoped static/read-only
checks.

I performed no real setup, Chrome, browser enumeration or claim, provider,
credential, clipboard, DNS, routing, VM, or other live action. V40 was not
consumed. The only workspace write is this assigned review artifact.

## Final verdict

**FAIL** — the original EOF finding is closed, but one new Minor scope/format
finding remains. V40 requires all four severity counts to be zero for PASS.

`authorizes_live_execution=false`

## Exact fix evidence

- Reviewed commit: `b782e09e61e95a73a3932e3b0bd64ab52b488786`.
- Direct parent: `13fcd03f8f0f7345e240b9f1453d1a1c62abbfba`.
- The commit modifies exactly the V40 brief path.
- Corrected brief: `20251` bytes, SHA-256
  `AE03C9AE6E0F957DBD8050CE89965946112F3F0B82640A45B3A607534057662C`,
  Git blob `281fddfb84a32410228f98133f4e9761da80c355`.
- The brief now ends in exactly one LF byte, is LF-only without BOM, and the
  corrected commit passes `git diff --check`.
- The sole executable remains byte-identical at `16531` bytes, SHA-256
  `A72DF6E3491521EA01A07CEFD3933768FC1DBEE62520E4C3FE0AA710AC37E868`.
- The unchanged fixture remains `10507` bytes, SHA-256
  `D932EC2BE4E6ED85F6C94F10395E62AF1B7483FF218695E2E860EB4853A41C79`,
  Git blob `bba393e3aef8ea8410fe384bc95cd02aa4b445f1`.
- Running the exact committed fixture returned:

```json
{"result":"V40_PURE_FIXTURES_PASS","briefBytes":20251,"briefSha256":"AE03C9AE6E0F957DBD8050CE89965946112F3F0B82640A45B3A607534057662C","executableBytes":16531,"executableSha256":"A72DF6E3491521EA01A07CEFD3933768FC1DBEE62520E4C3FE0AA710AC37E868","syntax":"PASS","moduleShape":true,"foreignRealmAccepted":true,"orderedRankZeroEnforced":true,"fullCellSuccess":true,"fixedFailure":true,"getterCalls":0}
```

- Before review creation, the index was empty and the inherited exact
  twelve-path product dirty baseline remained present and unstaged.

## Finding closure

### V40-001 — closed

The extra blank line at EOF is gone. The brief ends immediately after the final
`` `authorizes_live_execution=false` `` line with exactly one LF, and the
package whitespace check is clean.

## Finding

### V40-FIX1-001 — Minor — fix removes an unrelated interior blank line

The commit does not contain only the requested EOF normalization. Its exact
diff removes two LF bytes:

1. the extra blank line at EOF, which is the required fix; and
2. the ordinary interior blank line between the top
   `` `authorizes_live_execution=false` `` marker and `## Purpose`.

The second deletion is unrelated to the EOF finding and the commit subject. It
does not change the executable or security semantics, so the severity is
Minor. It nevertheless violates the literal minimal-fix boundary and leaves
the opening metadata/header transition inconsistent with the surrounding
brief format. Because this package allows PASS only with Minor `0`, it remains
blocking.

**Required fix:** restore exactly one blank line between the top authorization
marker and `## Purpose`, while preserving exactly one LF after the final
authorization marker. Commit only that brief correction directly on this FAIL
review, rerun the fixture for the new brief byte/hash tuple, and obtain a fresh
independent review. Do not execute V40 during the correction.

## Unchanged semantic package

Direct executable-byte identity and the passing fixture confirm the fix did
not alter V40 behavior:

- the gate still consumes before import and has no retry, fallback, second
  enumeration/claim, reconnect, alternate selection, or continuation;
- the foreign-realm listing still requires the bounded own length descriptor,
  exact numeric names and data descriptors, fixed record allowlist, required
  cached primitive ID, safe cached URL, and zero getter/direct-value reads;
- the documented descending last-opened/focused order and exact immediate
  owner Chrome profile/window/intended-tab confirmation remain jointly required
  for rank-zero authority;
- rank zero must privately parse to exact normalized HTTPS
  `dash.cloudflare.com` origin before the sole cached-ID claim;
- claimed-ID continuity, fixed account-home navigation, exact URL, one
  same-account `mysw.me` anchor, positive anchors, and zero busy markers remain
  mandatory;
- the outer catch still emits only literal `Error` without inspecting a thrown
  value;
- success retains only the reviewed same-realm setup/agent/browser/claimed-tab
  bindings, while ordinary and terminal-output failure clear all bindings;
- source-site and attempted/fulfilled counter cardinality remains exact; and
- no provider, credential, clipboard, DNS, routing, listener, proxy, VM, Create,
  native copy/paste, or deletion action is added or authorized.

All classification, separate tuple, package/hash, projection, empty-index,
twelve-path baseline, runtime/docs, residue, DNS, VM checkpoint, archived-owner,
sole-owner, exact selection, and fresh-realm action-time pins remain mandatory.
All V4 constraints and the final Create/native Copy/native masked Paste plus
separate exact-row deletion confirmations remain external and unreached.

## Finding counts and limits

- Critical: `0`.
- HIGH: `0`.
- IMPORTANT: `0`.
- Minor: `1` (`V40-FIX1-001`).

No live or consuming action was authorized or performed.

## Final verdict

**FAIL**

Unresolved findings: Critical `0`, HIGH `0`, IMPORTANT `0`, Minor `1`.

`authorizes_live_execution=false`
