# OmniRoute V37 fresh-session unique task-tab reacquisition — execution classification

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Classification

V37 is **STATIC PASS / CONDITIONALLY ELIGIBLE**. This file does not consume the
one-shot gate and is deliberately non-self-referential: it contains no claim
about its own commit, bytes, digest, blob, or containing HEAD. The sole
coordinator may execute the committed cell only after this classification is
committed directly on the independent PASS review and a separate post-commit
tuple proves every action-time pin.

## Immutable reviewed package

- Corrected brief commit:
  `9c4c167a4d49975b63a32ef5542ff73a82587042`
- Corrected brief path:
  `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v37-fresh-session-unique-task-tab-reacquisition-brief.md`
- Corrected brief bytes: `25327`
- Corrected brief SHA-256:
  `192417C7D078DA47CD5139A9BDEEEB0C43B276145195740AB985ECC60AA9B763`
- Corrected brief blob: `c6dffdd6d1351e770fc2fecd4a58b93d0e9deb15`
- Executable cells: `1`
- Executable normalized UTF-8 bytes: `15826`
- Executable SHA-256:
  `696C9D97AA0B5FB4510561DB0CB8D180643CB5FC43643717291D9D93FC8C8EBE`
- Executable syntax: `PASS`
- Pure fixtures: `V37_PURE_FIXTURES_PASS`
- Independent PASS review commit:
  `b77582306916b66df5a09a351e2e609a286c84d0`
- Independent PASS review path:
  `.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-v37-fresh-session-unique-task-tab-reacquisition-sol-review.md`
- Independent PASS review bytes: `10972`
- Independent PASS review SHA-256:
  `8DBDEB0120B057143A211E59F086CA6B135736EECDEC453CBAADB2E621F585EF`
- Independent PASS review blob: `1e5b239dde3a6c449acaa2eb62cfec2a30f56849`
- Review verdict: `PASS`
- Open findings: Critical `0`, HIGH `0`, IMPORTANT `0`, Minor `0`
- Closed findings: none; the first V37 review passed with all severities zero.

## Consumed predecessor boundary

V36 is consumed/failed cleanly after fresh attachment and one fulfilled
`openTabs()`; its trusted rank-zero predicate stopped before claim, navigation,
wait, URL read, or snapshot. Its sanitized incident is commit
`921326efd05daa44d946811080ca5209d79f503f`. V36 is permanently ineligible:
never retry, continue, reinterpret, or reuse it. Every earlier consumed gate
remains spent, and V4 remains static evidence only.

## Exact bounded semantics

V37 is one fresh-realm cell and one consuming gate. It consumes before import,
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
URL values. Every cached URL is privately parsed; a target must be exact HTTPS
`dash.cloudflare.com` without port, username, or password and have a path
rooted at `/<32-lowercase-hex>/mysw.me`. Exactly one target is required.

Only the unique target's cached primitive ID is passed once to `claimTab()`. The
claimed tab ID must exactly equal that cached value. The cell then requires the
exact account-home URL and same semantic signature used by reviewed
predecessors: HTTPS Cloudflare host, 32-lowercase-hex account-home path, exactly
one same-account `mysw.me` zone href, anchor count greater than zero, and zero
busy/progress elements.

The only success result is
`EXACT_V37_UNIQUE_TASK_TAB_ACCOUNT_HOME_REACQUISITION_PASS`. Every reviewed
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
  parent is exactly `b77582306916b66df5a09a351e2e609a286c84d0`; the commit
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
- The persistent Node realm is reset once for V37. A state-only post-reset
  query proves every named V35, V36, and V37 setup, agent, browser, tab, eligibility,
  consume, and state declaration absent.
- Exact extraction from the committed corrected brief yields one cell at
  `15826` normalized UTF-8 bytes and the pinned SHA-256; syntax validation
  passes without execution.

## Terminal interpretation

Exact PASS retains only the reviewed V37 browser and claimed account-home tab
bindings for the next separately specified and independently reviewed action.
V37 makes no Cloudflare provider-persistent change and grants no authority for
token creation, secret transmission, proxy/tunnel/DNS/routing mutation, VM
power action, or deletion.

Every failure is terminal for V37. Record only sanitized fixed-schema evidence,
clear eligibility, reset the Node realm, and leave provider state unchanged. A
replacement requires a new reviewed contract.

The mandatory final Create/native Copy/native masked Paste confirmation remains
unreached and cannot be preapproved. The later separate exact-row deletion
confirmation remains unreached and separately mandatory. Standing unattended
authority does not waive either confirmation, secret handling, one-shot
semantics, independent review, cleanup, or higher-priority tool safety.

