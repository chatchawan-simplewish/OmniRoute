# Task 17 v9 loopback keyboard — independent Sol High static review

Review timestamp: `20260901 015729` (Asia/Bangkok)  
Brief commit: `4a5c6e83a1fd7e44556fd1352698b3854f6a5ca9`  
Base / Task 16 PASS classification: `a9632463a94371d2556fe8f7b4de928461c4eab2`  
Scope: direct-byte and non-evaluating static review only. No contract cell, clipboard, browser, tab, listener, server, child comparison, credential, or routing action was performed.  
`authorizes_live_execution=false`

## Verdict

- Specification verdict: **PASS**.
- Security/quality verdict: **PASS**.
- Findings: **none**.
- This static PASS authorizes no live execution. The fresh one-shot gate remains separately consumable only by the sole Sol High owner after every action-time pin matches.

## Call 1 — Windows clipboard baseline

- The PowerShell block performs exactly one clear followed by one raw read with separate attempted/fulfilled counters (`task-17-v9-loopback-keyboard-brief.md:99-127`).
- It emits only counters, empty boolean, and safe error class; the local value is nulled in `finally`.
- Exact `1/1`, empty true, error `NONE`, and exit 0 are required. Every other outcome stops before Call 2 (`:127-132`).

## Call 2 — loopback server, keyboard copy, and exact cleanup

### Fresh state and server boundary

- V9 declares fresh expected-challenge, Call 3 eligibility, and retained-tab bindings once; it reuses only the existing connected `residualV5Chrome` (`task-17-v9-loopback-keyboard-brief.md:139-143`, `:183-192`).
- Challenge and request path each use independent 128-bit random values. The challenge is exact uppercase shape/length 50; the path is exact lowercase 32-hex suffix (`:193-200`).
- One `http.Server` binds with `{host:"127.0.0.1", port:0, exclusive:true}` and then proves the resolved address is exact IPv4 loopback with a positive ephemeral port (`:249-281`). No fixed port or external interface exists.
- HTML contains a fixed labelled readonly input and an embedded `data:,` favicon. Challenge/path/HTML/URL remain lexical and are never emitted.

### Exact routing and sticky lifecycle uncertainty

- The main route accepts only exact `GET` plus the random path, increments request/response counters separately, serves fixed no-store HTML, and allows it exactly once (`task-17-v9-loopback-keyboard-brief.md:213-228`). A duplicate is sticky uncertainty and receives 409.
- Optional favicon accepts only exact `GET /favicon.ico`, at most once, with separate request/response counters and 204/no-store (`:229-243`). Its exact success tuple is either all four counters zero or all four one (`:402-404`).
- Every other method/path increments unexpected-request count, makes server uncertainty sticky, and receives 404 (`:244-248`).
- Request abort/error, response error/premature close, client error, server error, invalid address/lifecycle, and teardown error all use the monotonic `markServerUncertain` transition (`:179-182`, `:201-212`, `:249-280`, `:301-316`, `:350-385`). No later close success clears prior uncertainty.
- Exact success requires one main request and fulfilled response, optional favicon exact tuple, unexpected requests zero, and server uncertainty false (`:386-431`).

### Browser sequence and retained-tab semantics

- Browser actions are serial: one session name, one tab new, one loopback goto, one exact-label lookup, click, `Control+A`, `Control+C`, and exact-tab close (`task-17-v9-loopback-keyboard-brief.md:282-349`).
- Click and both press actions each use `timeoutMs:5000`; exactly three such options exist. The sole Call 2 control operation is explicitly required to use `timeout_ms=60000` (`:81-86`, `:319-337`).
- `browserCallUnsettled` is set before each browser/locator operation and cleared only after fulfillment. Catch folds session, current-call, and uncertain tab state monotonically into browser uncertainty (`:282-353`).
- Server uncertainty is checked before every user-input/close phase. Any browser or server failure stops forward browser mutation.
- Once tab creation fulfills, the exact binding is retained unless exact close fulfills; no cleanup close follows browser uncertainty (`:288-353`, `:433-436`).

### Forced connection teardown and listener proof

- Installed Node `v24.19.0` directly reports both `http.Server.prototype.closeIdleConnections` and `closeAllConnections` as functions.
- In `finally`, when listening, the contract calls `closeIdleConnections()` once, then `closeAllConnections()` once, then directly awaits one callback-based `server.close()` (`task-17-v9-loopback-keyboard-brief.md:354-382`). There is no intervening await, timer, race, retry, or background helper.
- Each teardown operation has attempted/fulfilled counters; any throw or callback error is sticky uncertainty. After callback fulfillment, listener state must be false and server state exact `CLOSED` (`:373-407`).
- If a server exists but the normal close branch cannot run, the contract marks close state uncertain rather than inferring cleanup (`:383-385`).
- Exact Call 2 success requires all required counter pairs `1/1`, optional favicon tuple exact, tab closed/binding null, server closed/listening false, every uncertainty false, and result/error exact (`:386-431`). Only then is the lexical challenge published immediately before enabling Call 3 (`:408-414`).

## Call 3 — exact child comparison and final empty proof

- Eligibility is consumed before import/spawn; failure cannot restore it (`task-17-v9-loopback-keyboard-brief.md:445-466`).
- The challenge reaches only one synchronous bundled-`pwsh` child through stdin; shell is false, environment is restricted, deadline is 30000 ms, kill signal and buffer are bounded (`:467-520`).
- The child performs one stdin read, one clipboard comparison read, one final clear, and one final empty read. Cleanup executes once in `finally`, local values are nulled, and only the fixed 13-line redacted schema is emitted (`:467-506`).
- Parent validation requires start/exit fulfilled, exit 0, no child error/signal/stderr, exact ordered bounded stdout, exact equality/shape/length, both error labels `NONE`, clear/read `1/1`, and empty true (`:521-558`).
- Persistent challenge is retained on every failure and nulled only after fully validated exact success; no second child or later mutation is allowed (`:537-558`).

## Runtime, API, syntax, and cardinality

- Bundled Node pin matches: version `v24.19.0`, file version `24.19.0`, `92825416` bytes, SHA-256 `3602F2BB1A10F2CBAB4C36886218A33C1AB3DB87290E73B033C46C77147D0237`. Direct host evidence confirms both teardown methods are functions.
- Bundled PowerShell pin matches: `301368` bytes, file version `7.6.4.500`, SHA-256 `DB6DD81183FE57D22E03B911EC9A30A2FD7C40542E97743615355A6FB44F458F`.
- Browser API matches `58477` bytes / SHA-256 `4BFEB97E958025DB37D52AEA11B75BC70BCA417B4995B0F711C0F07F3DDCCB08` and directly declares the reviewed `nameSession`, `Tabs.new`, `Tab.goto`, `getByLabel`, `click`, `press(timeoutMs?)`, and `Tab.close` interfaces.
- Exact bundled `pwsh` parser reports zero errors and zero stderr for Call 1 and the embedded child without evaluating them. Both JavaScript cells pass bundled Node `--check --input-type=module`.
- Executable cardinality is one `createServer`, listen, nameSession, tabs.new, loopback goto, exact-label lookup, click, `Control+A`, `Control+C`, exact-tab close, closeIdleConnections, closeAllConnections, callback server.close, and spawnSync. Teardown call order is statically verified. Exactly three `timeoutMs:5000`, one Call 2 `timeout_ms=60000` requirement, and one child `timeout:30000` exist.

## Redaction, prohibited actions, and repository boundary

- Output contains no challenge, clipboard value, HTML, URL, port, request path, tab handle/ID/title/URL, content/metadata, exception message/stack, credential, key, or token.
- No external HTTP(S) target, data-page navigation, tab-native clipboard API, CUA, reconnect, enumeration/list/get, retry/fallback, credential, key, token, provider, Cloudflare, VM, proxy, OmniRoute mutation, or routing action exists.
- Old v3/v5 listener/process residuals remain untouched and `NOT PROVEN`.
- Reviewed HEAD equals `4a5c6e83a1fd7e44556fd1352698b3854f6a5ca9`; the commit adds only the 563-line v9 brief. Before creating this scratch report, Git index count was `0` and the unchanged dirty baseline was exactly `12` paths.
- Brief is UTF-8 without BOM, LF-only (`563` LF bytes, zero CR bytes), with no replacement character.
- Pinned source evidence matches: Task 16 classification `4254` / `4394B488F07B4AEA28B29ADCE9A1B42051B15A3D2BA7CCC18F89E22B995A2775`; v5 pattern `26264` / `C5C6C9A699253AB1D3C2D5D50C0E68D1B3F03C09A5865B82DE3B6021F42E9476`; v8 pattern `23152` / `075DE9C7BFCE48088D1E75C401CCBB455EBBA9786889044A19E6D9C749637508`; v7 child pattern `20581` / `9B84E07C0F6B5B3CBAEB0BD8A67B9D81139921F49011B113BC80D46D7285FDC9`; project authority `6051` / `AD0EA394F694C7795870C2B66D745EDC1FCA8997E7D7041A21E5659B0C349DDC`.
- Standing authority is correctly narrow: exact brief/review/evidence/API/module/runtime/authority pins, empty index, exact baseline, same browser binding, zero intervening live action, and never-declared v9 bindings are required. Invocation or uncertainty spends the gate; no retry, continuation, alternate tab, later cleanup, or verdict relaxation exists.

## Disposition

Static review is complete and **PASS**. Any live preflight remains a separate one-shot authority consumption and its redacted result requires independent post-action classification. `authorizes_live_execution=false`.
