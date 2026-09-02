# OmniRoute V36 fresh-session ordered selected-tab reacquisition — execution classification

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Classification

V36 is **STATIC PASS / CONDITIONALLY ELIGIBLE**. This file does not consume the
one-shot gate and is deliberately non-self-referential: it contains no claim
about its own commit, bytes, digest, blob, or containing HEAD. The sole
coordinator may execute the committed cell only after this classification is
committed directly on the independent PASS review and a separate post-commit
tuple proves every action-time pin.

## Immutable reviewed package

- Corrected brief commit:
  `8905b23e81df28eb283614d96cba0ba1fa5c9957`
- Corrected brief path:
  `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v36-fresh-session-ordered-selected-tab-reacquisition-brief.md`
- Corrected brief bytes: `25410`
- Corrected brief SHA-256:
  `73F88B050EEA1604ECC771B0CB9866C8B2FE5844D70D04597775D842A675EFDE`
- Corrected brief blob: `cad341e6d719b8004bf0d196c3487c9da7a1a165`
- Executable cells: `1`
- Executable normalized UTF-8 bytes: `15000`
- Executable SHA-256:
  `5395EAC07AEC15AB63BC78AA9DB1E89AE909DC00EE74991F6CEDF0BCB32834B0`
- Executable syntax: `PASS`
- Pure fixtures: `V36_FIX2_PURE_FIXTURES_PASS`
- Independent PASS review commit:
  `f070cae4b86b19d96c60ccc918f8be1d9ffa9c27`
- Independent PASS review path:
  `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v36-fresh-session-ordered-selected-tab-reacquisition-fix2-sol-review.md`
- Independent PASS review bytes: `10274`
- Independent PASS review SHA-256:
  `C2F4811902505F5840C99934E3B3835A90BCE46B9E8958E69355549D4C28B2A2`
- Independent PASS review blob: `c924026c62ac6ba72d9ab96041bf66fc602187f3`
- Review verdict: `PASS`
- Open findings: Critical `0`, HIGH `0`, IMPORTANT `0`, Minor `0`
- Closed findings: `V36-001`, `V36-002`, `V36-003`

The original review commit
`36460bd2f7ead55d945a8b86b3d81d88b718f1fe` and fix-1 review commit
`a0f15ddde6432d5c586bf64902a75ed6eb2d7b78` remain static FAIL evidence only.
They authorize no execution. The corrected brief and fix-2 PASS review above
are the only V36 executable package.

## Consumed predecessor boundary

V35 Call 1 is consumed/PASS. V35 Call 2 is consumed/failed cleanly after one
`openTabs()` returned eight shape-valid records; it stopped before claim,
navigation, wait, URL read, or snapshot. Its sanitized incident is commit
`1d9adba04a8d432865b2b28e1e4eb06a5945169a`. V35 is permanently ineligible:
never retry, continue, reinterpret, or reuse either cell. Every earlier
consumed gate remains spent, and V4 remains static evidence only.

## Exact bounded semantics

V36 is one fresh-realm cell and one consuming gate. It consumes before import,
setup, attachment, documentation, session naming, enumeration, or claim. It
may perform exactly one import, runtime setup, Chrome get, complete
documentation read/write, session-name call, `openTabs()`, `claimTab()`,
navigation to `https://dash.cloudflare.com/`, 20000 ms wait, URL read, and body
snapshot. It creates no tab, closes no tab, and has no retry, fallback,
alternate browser/profile/window, selected-tab fallback, second enumeration,
second claim, loop over targets, or manual integration.

The listing projector requires a bounded nonempty ordinary Array with the exact
standard prototype, no own symbols, one cached non-enumerable data length, and
exactly the own enumerable numeric data descriptors `0..length-1`. It never
invokes an iterator or reads an indexed property. Every descriptor-cached record
must be a stable plain record with no symbols or accessors, only the current
allowed field names, mandatory bounded control-free ID, and bounded
control-free string values. The projector retains only cached primitive ID and
URL values. The documented rank-zero record is selected only under the owner's
external intended-tab selection pin, and its cached URL must parse as exact
HTTPS `dash.cloudflare.com` without port, username, or password.

Only the cached primitive rank-zero ID is passed once to `claimTab()`. The
claimed tab ID must exactly equal that cached value. The cell then requires the
exact account-home URL and same semantic signature used by reviewed
predecessors: HTTPS Cloudflare host, 32-lowercase-hex account-home path, exactly
one same-account `mysw.me` zone href, anchor count greater than zero, and zero
busy/progress elements.

The only success result is
`EXACT_V36_ORDERED_SELECTED_TAB_ACCOUNT_HOME_REACQUISITION_PASS`. Every reviewed
shape, completeness, semantic, counter, consume, binding, state, and null-error
field must be exact. The final evidence schema may contain only fixed strings,
booleans, bounded counts, the trusted fixed snapshot, and sanitized error
class. It must emit no tab ID, provider-tab ID, title, URL, group, timestamp,
account ID, zone ID, href, secret, token, credential, listing, record, raw
exception, or final raw documentation.

On any failure the retained tab is null, eligibility false, terminal failure
state exact, and setup/agent/browser bindings cleared. A claim made before a
later failure is released only by required realm disposal; no tab is closed.
Any non-exact result, exception, timeout, partial output, or uncertainty is a
consumed terminal failure. Never retry, continue, relax, reinterpret, or use a
substitute target.

## Action-time pins

Immediately before extracting or sending the executable, every item below must
be true. Any mismatch stops before consumption.

- Current HEAD is the separate post-classification coordinator HEAD; its direct
  parent is exactly `f070cae4b86b19d96c60ccc918f8be1d9ffa9c27`; the commit
  adds exactly this classification path.
- The separate coordinator tuple proves this file's actual path, bytes,
  uppercase SHA-256, blob, HEAD, parent, one changed path, chain-path count,
  exclusion count, projection record count/digest, empty index, and exact
  12-path dirty baseline.
- The projection has exactly `10661` records and SHA-256
  `C4C85893769D133224AC7404B628C8B0D4B0EBBFF471620B158E652E152B4EBD`
  under the two fixed exclusions plus every unique chain path.
- Browser-client module is exactly
  `C:\Users\chatc\.codex\plugins\cache\openai-bundled\chrome\26.831.20005\scripts\browser-client.mjs`,
  bytes `149771`, SHA-256
  `A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`.
- API documentation is exactly
  `C:\Users\chatc\.codex\plugins\cache\openai-bundled\chrome\26.831.20005\docs\api.json`,
  bytes `58480`, SHA-256
  `A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.
- Static API and implementation pins still prove `browsers.get(id)`, complete
  `Browser.documentation()`, `Browser.nameSession(name)`, `Browser.user`,
  `openTabs()` ordered by `lastOpened` descending, `claimTab(string)`, `Tab.id`,
  `Tab.goto`, `Tab.url`, `waitForTimeout`, locator evaluation, and the exact
  current `BrowserUserTabInfo` field set.
- Evidence worktree
  `C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-team-api-offline`
  is clean at `80adaa7d5d63d1d2c7bfa63b236c6bee93b3b1d8`.
- Windows temporary/process residue is zero. Public A/CNAME counts for
  `ai-api-omniroute.mysw.me` are zero through `1.1.1.1` and `8.8.8.8`.
- VM1205 matches the complete safe checkpoint: `omniroute` and
  `bell-cloudflare-proxy` running; `team-api-proxy` and
  `omniroute-team-tunnel` absent; `omniroute-internal` members `2`; retained
  directory `root:root:700`; retained file `root:root:644`; retained SHA-256
  `a31c2010bb47767e25a826cebcd2469cb51d8af5c5ae089e46d2051edd69d9bb`;
  listener `20130` absent.
- The owner's exact current external confirmation remains applicable:
  `Chrome Profile Codex-Chrome-Bell-PC2, intended window, and intended task tab are selected; no other Chrome profile/window is offered to the extension.`
- No competing task, process, browser controller, extension offering, or live
  authority owner exists.
- The persistent Node realm is reset once for V36. A state-only post-reset
  query proves every named V35 and V36 setup, agent, browser, tab, eligibility,
  consume, and state declaration absent.
- Exact extraction from the committed corrected brief yields one cell at
  `15000` normalized UTF-8 bytes and the pinned SHA-256; syntax validation
  passes without execution.

## Terminal interpretation

Exact PASS retains only the reviewed V36 browser and claimed account-home tab
bindings for the next separately specified and independently reviewed action.
V36 makes no Cloudflare provider-persistent change and grants no authority for
token creation, secret transmission, proxy/tunnel/DNS/routing mutation, VM
power action, or deletion.

Every failure is terminal for V36. Record only sanitized fixed-schema evidence,
clear eligibility, reset the Node realm, and leave provider state unchanged. A
replacement requires a new reviewed contract.

The mandatory final Create/native Copy/native masked Paste confirmation remains
unreached and cannot be preapproved. The later separate exact-row deletion
confirmation remains unreached and separately mandatory. Standing unattended
authority does not waive either confirmation, secret handling, one-shot
semantics, independent review, cleanup, or higher-priority tool safety.
