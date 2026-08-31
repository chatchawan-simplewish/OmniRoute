# Task 2 direct clipboard preflight v2 independent Sol High review

## Verdict

**FAIL / NOT AUTHORIZED.**

The candidate is a materially simpler additive path and its normal success path
is serial, directly awaited, credential-free, and narrowly scoped. It is not
review-clean because an error returned by a browser-client promise is collapsed
to an ordinary exact `ABORT` object even when that error can represent transport
uncertainty or a partially applied browser mutation. The brief then requires a
later clipboard mutation. It also cannot account for a tab created before a
failed `tabs.new()` response, does not explicitly emit the required result via
the Node REPL output API, and does not place Call 3 cleanup in `finally`.

No browser, clipboard, PowerShell block, credential, network, or live-resource
action was executed during this static review.

## Direct-byte inputs

- Candidate commit: `33e722df03ca340c13e98537e03c226d0cb80041`
- Candidate parent: `16e88439331e9459f177122ddef4db5a00861143`
- Reviewed file: `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-direct-clipboard-preflight-v2-live-brief.md`
- Verified SHA-256: `D0202CE1601E02A178E47E5C78E7CEA662ACBBE362305BC102CED18FC31141B4`
- Verified size: `8766` bytes
- Encoding shape: no BOM, zero CR bytes, one trailing LF, no NUL bytes
- Commit scope: exactly the one candidate file
- Comparison inputs: the terminal bridge review at `16e884393` and
  `docs/superpowers/plans/2026-08-31-omniroute-secure-console-transfer.md`
- Existing unrelated modified and untracked implementation files were not
  changed or staged.

## Static checks

| Dimension | Result |
| --- | --- |
| Strict Call 1 / Call 2 / Call 3 order | **PASS in the written contract.** Call 3 is conditioned on receipt of a Call 2 object, and no concurrent host action is specified. |
| Browser success-path settlement | **PASS.** `tabs.new`, `goto`, semantic `click`, one `Control+A`, one `Control+C`, and exact-tab `close` are each directly awaited. `finally` begins only after the active JavaScript promise settles. |
| Timer/race/helper exclusion | **PASS.** The exact cell contains no `Promise.race`, timer, process, bridge, helper, background task, retry, or fallback. |
| Chrome skill/API surface | **PASS for the named normal path.** It reuses the existing `chrome` binding, controls Chrome only through the Node REPL browser client, uses a fresh tab and semantic label locator, and performs no snapshot, screenshot, extraction, coordinates, browser clipboard API, or network URL. |
| Fresh challenge | **PASS.** One runtime `node:crypto.randomBytes(16)` value produces exactly 128 random bits rendered as 32 uppercase hex characters. The fixed HTML interpolation is safe for that alphabet. |
| Copy action counts | **PASS for fulfilled calls.** The source contains exactly one semantic focus, one `Control+A`, and one `Control+C`; counters increment only after the corresponding await fulfills. |
| Exact-tab disposition | **FAIL.** Normal success closes the exact retained handle once, but a rejected `tabs.new()` leaves the binding null even if the remote tab creation partially applied, and the returned object falsely derives `exactTabClosed=true` from local nullness. |
| Tool uncertainty | **FAIL.** Only an outer Node-tool failure is classified as uncertain. Browser-client transport rejection is caught as ordinary `ABORT`, after which `finally` and Call 3 are allowed even though remote mutation settlement is not established. |
| Node cell executability/output | **REVISE.** The JavaScript parses and the new names do not conflict with the known `chrome` binding on a first execution. The persistent REPL guidance says to reassign rather than redeclare, so no second execution is permitted. More importantly, the exact cell ends in a bare object expression instead of the required `nodeRepl.write(...)`; the contract cannot depend on an implicit display result to obtain its one exact object. |
| PowerShell 7 command surface | **PASS for syntax and parameters.** Both blocks parse with zero PowerShell parser errors on PowerShell `7.6.4`; local `Set-Clipboard -Value` accepts empty strings and `Get-Clipboard -Raw` is present. Each block must run as its own PowerShell 7 host call because it uses `exit`. |
| Shape-only clipboard handling | **PASS on the ordinary path.** Clipboard text is held only for case-sensitive equality and length, and is never emitted, serialized, or hashed. |
| Clipboard cleanup | **FAIL.** Call 3 performs clear/read only after the comparison read succeeds; any terminating comparison-read or intermediate clipboard error skips the remaining clear/empty-check because there is no `finally`. This contradicts the secure-transfer plan's all-state cleanup requirement. |
| Counters and PASS conditions | **PASS on the ordinary path.** The six browser counters and Call 1/3 labels are consistent, and PASS requires exact `1` values, equality, exact-tab closure, and final empty clipboard. Error paths remain unsound for the findings below. |
| Proof boundary | **PASS.** A successful observation would prove only the fresh data-URL semantic-copy to local current-Windows-clipboard path. It would not prove credential safety, Cloudflare behavior, AnyDesk settings, later owner transport, or any routing action. |
| Authority scope | **PASS in prose.** The current user statement is sufficient only for one non-secret clipboard preflight after an independent PASS. It does not authorize a credential, token, permission, deletion, evidence-worktree mutation, Cloudflare, OmniRoute, VM1205, proxy/proof/R5, Rulesets, or routing action. |

## Findings and required corrections

### F1 — HIGH: inner browser transport uncertainty can race later cleanup

At `brief:89-114`, every rejected browser-client promise is caught and converted
to an exact `ABORT` or `RETAINED_TAB` object. At `brief:135-138`, receipt of any
exact object authorizes Call 3. That is not equivalent to proving the remote
browser mutation settled: a transport failure or timeout can reject the local
promise after the command was accepted, while its remote side effect is absent,
partial, complete, or still resolving. In particular, a copy command can race
the later Windows clipboard clear, recreating the class of race that terminally
rejected the bridge path.

Minimum correction: distinguish ordinary semantic failure from browser-client
transport/timeout uncertainty using a documented, reviewable signal. Any
uncertain browser result must return a dedicated terminal classification and
forbid every later browser or clipboard mutation. Do not infer remote settlement
solely from local promise rejection.

### F2 — HIGH: failed `tabs.new()` can hide an opened tab

At `brief:84,89`, `directPreflightTab` is assigned only after `tabs.new()`
fulfills. If creation partially applies but its response rejects or is lost,
the catch observes null; `finally` performs no close; and `brief:121` reports
`exactTabClosed=true`. This is the same load-bearing open-result ambiguity that
the terminal bridge review required to be handled conservatively.

Minimum correction: never equate a null local binding after an uncertain open
with proof of no tab or exact closure. Classify the tab state as uncertain,
forbid Call 3, and ensure the verdict/report cannot claim closure or zero
residual tab without an authoritative exact-handle result.

### F3 — IMPORTANT: the exact result object is not explicitly emitted

At `brief:116-122`, the cell ends with a bare object expression. The available
Node REPL contract says to use `nodeRepl.write(value)` for output. The brief
requires one exact returned object as the authorization edge for Call 3, so it
must not rely on implicit expression display behavior.

Minimum correction: emit exactly the bounded result object with one explicit
`nodeRepl.write(...)` after `finally`; emit no other content. Keep all names
single-use or scope them so the persistent REPL cannot hit a redeclaration on
the only authorized execution.

### F4 — IMPORTANT: Call 3 does not guarantee its promised final clear

At `brief:150-155`, the comparison read precedes the clear and the clear precedes
the empty-check, with no `try/finally`. A terminating `Get-Clipboard` or
`Set-Clipboard` error skips remaining cleanup and contradicts `brief:135-136`
and the plan's requirement that all terminal states converge on one clear and
empty-check attempt.

Minimum correction: put the one comparison attempt in `try` and the single
clear plus empty-check attempt in `finally`, preserve one-shot counters, never
emit observed text, and require successful cleanup for PASS. A cleanup error
must remain FAIL / NOT PROVEN without retry.

## Authority boundary

The exact candidate is **FAIL / NOT AUTHORIZED**. This review authorizes no
preflight execution and no browser, clipboard, PowerShell, credential, token,
Cloudflare, OmniRoute, VM1205, proxy/proof/R5, Rulesets, evidence mutation,
revocation, permission change, deletion, or other live action. A corrected
direct-byte candidate requires a fresh independent review. Even a future PASS
would authorize only the one already user-approved non-secret preflight and
would not authorize credential or routing work.
