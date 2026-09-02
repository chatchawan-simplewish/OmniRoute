# OmniRoute V35 fresh-session open-tabs claim and account-home reacquisition — execution classification

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Classification

V35 is **STATIC PASS / CONDITIONALLY ELIGIBLE**. This classification does not
itself consume either one-shot cell and does not waive any action-time pin. The
sole coordinator may execute Call 1 only after this file is committed directly
on the independent PASS review and a separate post-commit coordinator tuple
proves every required pin. Call 2 remains separately ineligible until Call 1
returns the exact complete PASS result and its own action-time pins revalidate.

The classification is deliberately non-self-referential: it contains no claim
about its own commit, byte length, digest, blob, or the HEAD that will contain
it. Those values belong only in the separately calculated post-commit tuple.

## Immutable reviewed package

- Corrected brief commit:
  `3504b9e87eacd1c8de6801df7256bd502ce7d37f`
- Corrected brief path:
  `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v35-fresh-session-open-tabs-claim-reacquisition-brief.md`
- Corrected brief bytes: `22491`
- Corrected brief SHA-256:
  `EF482474FF8A0E13637B92366DD911E157B989488628BAB33E465538D5DE71E9`
- Corrected brief blob: `e0aaf1dd69c76f4cb9e6aa66f8f72632a6181b83`
- Call-1 bytes: `5456`
- Call-1 SHA-256:
  `4F6F4A3F35D6BBCC3EFC5CA6A4B335788D14F38191C88B0D51D63539DA11A2F4`
- Call-2 bytes: `9904`
- Call-2 SHA-256:
  `6A387C46AA9A226649BA705F503037DCA0813678DDAEAD860060964069C0116F`
- Independent PASS review commit:
  `41d220ccdd66cb403868e4be06144b681a6589fa`
- Independent PASS review path:
  `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v35-fresh-session-open-tabs-claim-reacquisition-fix1-sol-review.md`
- Independent PASS review bytes: `9838`
- Independent PASS review SHA-256:
  `41A958F525ED69B75584627ED317F96040EF526C09D7430E1CF61CF5DBB16F91`
- Independent PASS review blob: `115b586c25a0161af7538dabcc5274be1dc44c23`
- Review verdict: `PASS`
- Open findings: Critical `0`, HIGH `0`, IMPORTANT `0`, Minor `0`
- Closed findings: `V35-001`, `V35-002`

The earlier V35 review commit
`ebbe03b537d2ef8f373052b0831d5a862d13bf12` is retained as static FAIL
evidence only. It does not authorize execution. The corrected brief and the
fix-1 PASS review above are the only V35 executable package.

## Predecessor and consumed-gate boundary

V34 Call 1 is consumed and passed. V34 Call 2 is consumed and failed cleanly
because the current runtime returned no selected-tab ID, leaving controller
ownership false before navigation. V34 is permanently ineligible: never retry,
continue, reinterpret, or reuse either V34 cell. The fixed incident is commit
`0d6de7be7aea903bff24c82fb81db5ef25239f30` at
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v34-selected-tab-ownership-shape-live-incident.md`.

V3 and every other previously consumed gate remain spent under their recorded
terminal interpretations. V4 remains static evidence only. V35 is a new
replacement with independent cells and must not inherit any predecessor's
persistent Node or Chrome bindings.

## Exact bounded semantics

Call 1 is the only fresh Chrome attachment cell. It consumes before import or
attachment. In a freshly reset Node realm it proves all named V34 and V35
declarations absent, imports the exact pinned browser client module, obtains
the exact pinned browser, and captures complete runtime documentation. Its only
terminal success is `EXACT_V35_FRESH_CHROME_ATTACHMENT_PASS` with every exact
shape, completeness, consume, count, state, and null-error field required by
the committed cell. Any other output, exception, timeout, or uncertainty is a
consumed failure. No retry, fallback, second attachment, alternate browser, or
manual binding is permitted.

Call 2 is a separate one-shot cell. It consumes before any precondition or tab
operation. It requires the exact Call-1 PASS state, exact controller ownership,
and the reviewed plain-record snapshot gate. It performs exactly one
`openTabs()` call and privately validates the returned records. Candidate
projection is closed to current documented fields only: `id`, `lastOpened`,
`providerTabId`, `tabGroup`, `title`, and `url`. It rejects symbols, accessors,
non-enumerable fields, unexpected fields, non-plain records, invalid values,
and any candidate count other than exactly one. The candidate ID is validated
from one descriptor read and cached; it is never emitted or re-read.

Only after exactly one private candidate exists may Call 2 perform exactly one
`claimTab()` using the cached candidate ID. The claimed tab ID must exactly
match the cached ID and remain private. The cell then performs exactly one
navigation to `https://dash.cloudflare.com/`, exactly one 20000 ms wait,
exactly one URL read, and exactly one account-home semantic snapshot. Success
requires the exact `https://dash.cloudflare.com/<32-lowercase-hex>/home` URL,
host `dash.cloudflare.com`, account-home path, exactly one same-account
`mysw.me` zone href, at least one anchor, and zero busy elements. The only
terminal success is
`EXACT_V35_OPEN_TABS_CLAIM_ACCOUNT_HOME_REACQUISITION_PASS` with every reviewed
boolean, counter, state, candidate-count, and null-error field exact.

Output is restricted to the committed fixed schema. It must not emit a tab ID,
provider tab ID, title, URL, group, account ID, zone ID, href, secret, token,
credential, or raw exception. The cell creates no tab and closes no tab. The
externally selected task tab remains user-owned; V35 claims it for controller
use only after the exact private uniqueness proof.

## Call-1 action-time pins

Immediately before Call 1, all of the following must be true. Any mismatch
stops before the cell and does not consume Call 1.

- The current HEAD is the post-commit classification HEAD from the separate
  coordinator tuple; its direct parent is exactly
  `41d220ccdd66cb403868e4be06144b681a6589fa`; and the commit adds exactly this
  classification path.
- The separate tuple proves this file's actual bytes, uppercase SHA-256, blob,
  HEAD, parent, changed path, chain-path count, exclusion count, projection
  record count and digest, empty index, and exact 12-path dirty baseline.
- The source projection contains exactly `10661` records and SHA-256
  `C4C85893769D133224AC7404B628C8B0D4B0EBBFF471620B158E652E152B4EBD`
  under the recorded two fixed exclusions plus every unique chain path.
- The browser-client module is exactly
  `C:\Users\chatc\.codex\plugins\cache\openai-bundled\chrome\26.831.20005\scripts\browser-client.mjs`,
  bytes `149771`, SHA-256
  `A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`.
- The API documentation is exactly
  `C:\Users\chatc\.codex\plugins\cache\openai-bundled\chrome\26.831.20005\docs\api.json`,
  bytes `58480`, SHA-256
  `A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.
- Static API and implementation pins still prove `browsers.get(id)`,
  `Browser.documentation()`, `Browser.user`, `BrowserUser.openTabs()`,
  `BrowserUser.claimTab(tab)`, `Tabs.selected()`, `Tab.id`, `Tab.goto`,
  `Tab.url`, `playwright.waitForTimeout(timeoutMs)`, locator evaluation, and
  the current `BrowserUserTabInfo` field set used by the projector.
- Evidence worktree
  `C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-team-api-offline`
  is clean at `80adaa7d5d63d1d2c7bfa63b236c6bee93b3b1d8`.
- Windows temporary/process residue remains zero, public DNS remains absent,
  and VM1205 retains the recorded safe checkpoint: OmniRoute running; proxy
  and tunnel services absent; internal members `2`; retained directory
  `root:root:700`; retained file `root:root:644`; retained SHA-256
  `a31c2010bb47767e25a826cebcd2469cb51d8af5c5ae089e46d2051edd69d9bb`;
  listener `20130` absent.
- The owner's exact current external confirmation remains applicable:
  `Chrome Profile Codex-Chrome-Bell-PC2, intended window, and intended task tab are selected; no other Chrome profile/window is offered to the extension.`
- The persistent Node realm is reset once for V35. A state-only post-reset query
  proves every named V34 and V35 controller, browser, tab, eligibility, consume,
  and state declaration absent before the executable cell is extracted.
- Exact extraction from the committed corrected brief reproduces Call 1 at
  `5456` bytes and the pinned digest. Syntax validation passes without running
  the cell.

## Call-2 action-time pins

Call 2 remains ineligible unless Call 1 has exact complete PASS output and
retained state. Immediately before Call 2, repeat every non-destructive pin
whose drift could alter execution, including HEAD/parent/path and tuple,
projection, index, dirty baseline, runtime/module/API, evidence worktree,
Windows residue, VM1205, public DNS, and the owner's external Chrome selection
confirmation. In addition:

- Persistent state must show Call 1 consumed exactly once, eligible true,
  controller/browser bindings present, state `V35_ATTACHMENT_PASS`, and no
  V35 Call-2 consumption or retained tab.
- Exact extraction from the committed corrected brief reproduces Call 2 at
  `9904` bytes and the pinned digest. Syntax validation passes without running
  the cell.
- No competing task, process, browser controller, extension offering, or live
  authority owner may exist.

Any action-time mismatch stops before Call 2 and leaves it unconsumed. After
Call 2 begins, any non-exact result, exception, timeout, partial output, or
uncertainty is a consumed failure. Never retry, continue, relax a verdict,
substitute a tab, use selected-tab fallback, enumerate again, claim again,
navigate manually, close a tab, or preserve an uncertain controller.

## Terminal interpretation

Exact Call-2 PASS retains only the reviewed V35 controller and claimed task-tab
bindings for the next separately specified and independently reviewed action.
It makes no Cloudflare provider-persistent change and grants no authority for a
later create, copy, paste, routing, credential, DNS, proxy, tunnel, VM, or
deletion action.

Every Call-2 failure is terminal for V35. Record only fixed-schema sanitized
evidence, clear eligibility, dispose the Node realm, and leave provider state
unchanged. A replacement requires a new reviewed contract.

The mandatory final Create/native Copy/native masked Paste confirmation is not
reached by V35 and remains required. The later separate exact-row deletion
confirmation is also not reached and remains separately required. Standing
unattended authority does not waive either confirmation, secrets handling,
one-shot semantics, independent review, cleanup, or any higher-priority tool
safety boundary.
