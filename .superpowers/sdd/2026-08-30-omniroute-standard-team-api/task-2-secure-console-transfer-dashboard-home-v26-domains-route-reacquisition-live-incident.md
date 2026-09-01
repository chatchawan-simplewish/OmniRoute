# OmniRoute V26 guarded Domains-route reacquisition live incident

## Verdict

**FAIL-CLEAN — `PRECONDITION_FAIL`. V26 is permanently consumed.**

The sole reviewed call created one exact owned tab, navigated to the fixed
dashboard host, and completed the first URL read. The new pre-click account
binding required the account-home path immediately after `goto`; that route had
not settled yet, so execution stopped before the anchor wait/snapshot and
before any Domains or provider action.

The exact tab closed `1 / 1`, residue converged, no handle remains, and state is
`V26_ROUTE_FAILED_CLEAN`. There is no retry, continuation, reinterpretation,
fallback, manual integration, or alternate browser path under V26.

## Authority and action-time evidence

- Fixed brief commit: `f766cd1120f18974211e6126158d76353f790f91`
- Executable: `17364` normalized UTF-8 bytes at SHA-256
  `3474ADDB44DE34170452F3B9545393478B16820BEC5781CF0B19E2B5E40D7A3B`
- Independent Sol High PASS review:
  `8729ffcfe81bdca80449f320ac3f6af341bf71dc`
- Non-self-referential classification:
  `0d237d34d0040a4f20851436c86ebceabb75c996`
- Pre-call tuple: chain `92`; exclusions `94`; projection `10661` records at
  SHA-256
  `C4C85893769D133224AC7404B628C8B0D4B0EBBFF471620B158E652E152B4EBD`;
  empty index; exact 12-path dirty baseline.

Every documented action-time local, runtime, evidence-worktree, residue,
VM1205, DNS, and persistent-Node pin passed before the sole call.

## Exact safe result

- declarations/predecessor/controller/handle/tab shape: true;
- new, home navigation, and first URL: each `1 / 1`;
- home snapshot, Domains count/visibility/click, Domains URL, zone
  wait/count/href/navigation, final URL, and marker wait/count: each `0`;
- home snapshot validated/signature: false/false;
- exact close: `1 / 1`;
- cleanup/residue/retained handle: `EXACT_TAB_CLOSED` / true / false;
- eligible: false; route consumed: true; reads consumed: false;
- both detach flags: false; error class: `Error`;
- output: exactly one completed fixed-value write.

No URL, href, account/zone ID, DOM, HTML, screenshot, provider response,
credential, token, secret, or clipboard value was emitted. No click, fill,
press, submit, Create, edit, delete, DNS, rate-rule, Tunnel, Access, API-token,
permission, VM, routing, listener, process, reconnect, or tab-discovery action
occurred.

Any replacement must be a new independently reviewed contract. It may move the
pre-click account-home parse only after an explicit post-anchor-settle URL read,
while preserving the same-account binding and every inherited safety boundary.
The final Create/native Copy/native masked Paste confirmation and later exact-row
deletion confirmation remain unreached and mandatory.
