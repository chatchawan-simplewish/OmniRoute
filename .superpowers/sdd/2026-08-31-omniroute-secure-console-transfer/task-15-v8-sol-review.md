# Task 15 v8 keyboard clipboard — independent Sol High static review

Review timestamp: `20260901 011641` (Asia/Bangkok)  
Brief commit: `bb37efde0705001e892344fe7c6437a4c66f9a14`  
Base / Task 14 PASS classification: `d17f557cd3981ec306b6d39c74b8823dcfe880f3`  
Scope: direct-byte and non-evaluating static review only. No contract cell, clipboard, browser, tab, listener, server, child comparison, credential, or routing action was performed.  
`authorizes_live_execution=false`

## Verdict

- Specification verdict: **PASS**.
- Security/quality verdict: **PASS**.
- Findings: **none**.
- This static PASS authorizes no live execution. The fresh one-shot gate remains separately consumable only by the sole Sol High owner after every action-time pin matches.

## Three-call state machine

### Call 1 — Windows clipboard baseline

- The PowerShell block performs exactly one clear and one raw read, in order, with independent attempted/fulfilled counters (`task-15-v8-keyboard-clipboard-brief.md:101-115`).
- It derives only a boolean empty result, clears the local value in `finally`, emits no clipboard content, and requires exact `1/1`, empty true, error `NONE`, and exit 0 (`:116-133`).
- Any other outcome stops before Call 2.

### Call 2 — local keyboard copy and exact-tab close

- Fresh v8 expected-challenge, Call 3 eligibility, and retained-tab bindings are declared once and are distinct from all v7 state (`task-15-v8-keyboard-clipboard-brief.md:146-150`).
- Existing `residualV5Chrome` is validated, session naming is attempted once, and session uncertainty becomes true before the await and false only after fulfillment (`:173-182`).
- The fresh challenge is lexical, exact uppercase shape, and length 50. It is safely embedded in one labelled readonly input in one percent-encoded `data:text/html` URL held only in Call 2 memory (`:183-188`).
- One tab is created and retained immediately after fulfillment. The exact tab is then used for one local `goto`, one exact `getByLabel("OmniRoute V8 Challenge", { exact:true })`, one awaited click, one awaited `Control+A`, one awaited `Control+C`, and one awaited exact-tab close (`:189-247`).
- Click and both press calls each use `timeoutMs:5000`; exactly three such action options exist. The orchestrator Call 2 operation is explicitly required to use `timeout_ms=30000`, and control timeout is terminal (`:135-144`, `:275-281`).
- Every browser/locator action is strictly serial. `browserCallUnsettled` is set immediately before each operation and cleared only after fulfillment; catch folds it, session uncertainty, and uncertain tab state monotonically into `browserUncertain` (`:189-258`).
- The persistent challenge and Call 3 eligibility are set only after all sixteen counters equal one, exact tab close is fulfilled, and all uncertainty is false (`:248-251`). On failure, challenge stays lexical, eligibility stays false, and an opened exact tab binding remains retained unless exact close fulfilled (`:255-289`). No cleanup action follows uncertainty.
- Success output is redacted: it contains only safe result/error class, shape/length, counters, tab-state booleans, and uncertainty booleans. It does not include challenge, HTML, data URL, tab metadata, or content.

### Call 3 — bounded Windows clipboard comparison and cleanup

- Eligibility is consumed before import/spawn. Invalid binding, import failure, spawn failure, child failure, timeout, signal, stderr, parse/schema failure, comparison failure, or cleanup failure is terminal and cannot restore eligibility (`task-15-v8-keyboard-clipboard-brief.md:299-320`, `:361-413`).
- The challenge is passed only as one stdin line to the exact pinned bundled `pwsh`; it is not an argument, environment variable, disk, network, or output value (`:321-367`).
- The child performs one handoff read, one Windows clipboard comparison read, one final clear, and one final empty read. Its `finally` executes the cleanup path once, nulls local values, and emits only the fixed 13-line redacted schema (`:321-360`).
- Parent validation requires child start/exit `1/1`, exit 0, no child error/signal/stderr, exact ordered bounded stdout, equality, observed shape/length, both error labels `NONE`, final clear/read `1/1`, and empty true (`:375-413`).
- The persistent v8 challenge is retained on every failure and nulled only after the fully validated exact-success tuple (`:391-400`). No second child or later browser/clipboard mutation is permitted.

## API and runtime evidence

- Installed browser API is `58477` bytes / SHA-256 `4BFEB97E958025DB37D52AEA11B75BC70BCA417B4995B0F711C0F07F3DDCCB08`.
- Direct declarations confirm `nameSession(name:string):Promise<void>`, `Tabs.new():Promise<Tab>`, `Tab.goto(url:string):Promise<void>`, `PlaywrightPage.getByLabel(...,{exact?})`, `PlaywrightLocator.click(LocatorClickOptions)`, `PlaywrightLocator.press(value,{timeoutMs?})`, and `Tab.close():Promise<void>`. `LocatorClickOptions` includes `timeoutMs?:number`.
- Pinned bundled `pwsh` exists and matches `301368` bytes / SHA-256 `DB6DD81183FE57D22E03B911EC9A30A2FD7C40542E97743615355A6FB44F458F` / file version `7.6.4.500`.
- Exact bundled `pwsh` parser returned zero errors and zero stderr for Call 1 and the embedded child without evaluating them. Both JavaScript cells passed `node --check --input-type=module`.
- The previously reviewed exact bundled-runtime compatibility proof remains applicable; no concrete doubt justified rerunning that passing inert probe.

## Cardinality, redaction, and prohibited actions

- Static executable cardinality: one `residualV5Chrome.nameSession`, one `tabs.new`, one exact-tab `goto`, one exact-label lookup, one `field.click`, one `Control+A`, one `Control+C`, one exact-tab close, and one `spawnSync`.
- Exactly one local data URL is constructed in executable code. It contains only the fresh non-secret challenge and fixed HTML, is consumed solely by the exact tab, and is never emitted.
- No server/listener/connect, external HTTP(S) URL, tab-native clipboard API, CUA, reconnect, tab enumeration/get, retry, fallback, alternate tab, credential, key, token, provider, Cloudflare, VM, proxy, OmniRoute mutation, or routing action exists.
- Old v3/v5 listener/process residuals remain untouched and `NOT PROVEN`. No v7 state is reused other than pinned evidence establishing cleanup.

## Pins and repository boundary

- Reviewed HEAD equals `bb37efde0705001e892344fe7c6437a4c66f9a14`; the commit adds only the 423-line v8 brief.
- Before creating this requested scratch report, Git index count was `0` and the unchanged dirty baseline count was exactly `12`.
- Brief bytes are UTF-8 without BOM, LF-only (`423` LF bytes, zero CR bytes), with no replacement character.
- Pinned evidence matches: corrected Task 13 brief `20581` / `9B84E07C0F6B5B3CBAEB0BD8A67B9D81139921F49011B113BC80D46D7285FDC9`; Task 13 classification `5509` / `269A8F2A27F3662C69DBF0CC85E977D1DE91E7EA043C250F21833AB530EA8BA9`; Task 14 classification `4145` / `52B50688C8A20CA26B5F995813D9A7DBAF74FAA56CD45C875566F9AD09A020F0`; project authority `6051` / `AD0EA394F694C7795870C2B66D745EDC1FCA8997E7D7041A21E5659B0C349DDC`.
- Standing authority is correctly narrow: exact brief/review/evidence/runtime/API/authority bytes, empty index, exact 12-path baseline, same connected non-null browser binding, zero intervening live action, and never-declared v8 bindings are mandatory. Any failure, uncertainty, or invocation spends the gate and permits no retry, fallback, continuation, or verdict relaxation.

## Disposition

Static review is complete and **PASS**. Any live preflight remains a separate one-shot authority consumption and its redacted result requires independent post-action classification. `authorizes_live_execution=false`.
