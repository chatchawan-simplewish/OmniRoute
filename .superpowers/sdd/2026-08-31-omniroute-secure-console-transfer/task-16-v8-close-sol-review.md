# Task 16 v8 retained-tab direct close — independent Sol High static review

Review timestamp: `20260901 013157` (Asia/Bangkok)  
Brief commit: `bc05245f94d8a914c70bfb04a0413d06920a1f0f`  
Base / Task 15 classification: `1b25304d3cdc38e24bf0f542f98207eebde5ab30`  
Scope: direct-byte and non-evaluating static review only. No browser, tab, clipboard, child, listener, server, process, credential, or routing action was performed.  
`authorizes_live_execution=false`

## Verdict

- Specification verdict: **PASS**.
- Security/quality verdict: **PASS**.
- Findings: **none**.
- This static PASS authorizes no live execution. The fresh one-shot cleanup gate remains separately consumable only by the sole Sol High owner after every action-time pin matches.

## Exact binding and pinned state

- The contract names only `keyboardClipboardPreflightV8RetainedTab`, exactly matching the retained binding established in Task 15.
- Pinned Task 15 live report matches `2095` bytes / SHA-256 `0D5B822B05DB73AE7C62A588AC1D4C44C5E7047AFE6858587649BEB753BC975E`.
- Pinned Task 15 classification matches `5312` bytes / SHA-256 `9EE8DAEA43FDDF2ADF51ED624912408CF754CC1E5C9410E0E3A75AD3C4C74833`.
- That evidence proves tab creation fulfilled, navigation remained uncertain, tab close was never attempted, and the exact tab binding remained non-null. It also proves locator/click/select/copy and Call 3/child were never attempted.
- The challenge remained lexical and was never published to the persistent expected-challenge binding. Windows clipboard empty is pinned to the Task 15 report boundary; this contract neither inspects nor refreshes either state.

## One-cell state machine

- Fresh `keyboardClipboardPreflightV8RetainedTabCloseEligible` is declared once. Its value is captured and immediately set false before any retained-binding inspection (`task-16-v8-retained-tab-close-brief.md:87-110`).
- The cell safely checks declaration via `typeof`, then exact-binding non-null state, then callable `close`, with one attempted/fulfilled binding-check path (`:110-115`).
- A mismatch returns `RETAINED_TAB_BINDING_INVALID` before any close or binding assignment (`:116-120`). The cleanup eligibility remains consumed.
- The only browser action is one directly awaited `keyboardClipboardPreflightV8RetainedTab.close()` (`:121-123`).
- The exact retained binding is set null only after the close promise fulfills and the fulfilled counter increments (`:123-126`).
- A rejected close enters the catch, emits only a safe error class/result, and recomputes retained-binding presence without assigning the binding (`:127-130`). Thus rejection retains the exact binding and cannot be misclassified as closed.
- A single `finally` emits the one terminal redacted object (`:131-134`). Exact PASS requires eligibility true/consumed, binding check `1/1`, declared/non-null/callable true, close `1/1`, error `NONE`, exact result, and retained binding false (`:137-147`).
- Invocation, failure, rejection, timeout, missing/malformed output, or tool uncertainty spends the gate. No second close or later cleanup is permitted.

## API, syntax, cardinality, and redaction

- Installed API is `58477` bytes / SHA-256 `4BFEB97E958025DB37D52AEA11B75BC70BCA417B4995B0F711C0F07F3DDCCB08` and directly declares `Tab.close(): Promise<void>`.
- Installed browser module is `149210` bytes / SHA-256 `C52BA09202F0E82CAA6F6D2A6463A8635C1B1316567975D9B91C1A05FB5AF501`.
- The sole JavaScript cell passed `node --check --input-type=module`; it was not evaluated.
- Executable-cell cardinality is exactly one eligibility-to-false transition, one directly awaited exact-binding close, one success-only binding-to-null assignment, and one `nodeRepl.write(output)`.
- Executable-code inspection found zero `tabs.list`, `tabs.get`, `tabs.new`, discovery/reacquisition, navigation/goto, URL/content/metadata inspection, keyboard, clipboard, child/spawn, server/listener/connect, process inspection/action, retry, fallback, credential, permission, deletion, provider, Cloudflare, VM, proxy, key, token, OmniRoute, or routing action.
- Output is limited to safe result/error class, booleans, and counters. It exposes no tab handle/ID/title/URL, page content/metadata, challenge, clipboard value, exception message/stack, credential, key, token, or routing data.
- Old listener/process residuals remain untouched and `NOT PROVEN`.

## Repository and authority boundary

- Reviewed HEAD equals `bc05245f94d8a914c70bfb04a0413d06920a1f0f`; the commit adds only the 153-line Task 16 brief.
- Before creating this requested scratch report, Git index count was `0` and the unchanged dirty baseline count was exactly `12`.
- Brief is `7721` bytes / SHA-256 `F12B63ED0DD3FFB02D12FB6BBEDB205A7467AD67592CFF7816AADF90FFCF8D29`, UTF-8 without BOM, LF-only (`153` LF bytes, zero CR bytes), with no replacement character.
- Project authority bytes remain `6051` / SHA-256 `AD0EA394F694C7795870C2B66D745EDC1FCA8997E7D7041A21E5659B0C349DDC`.
- Standing authority is correctly narrow: exact brief/review/report/classification/API/module/authority pins, empty index, exact 12-path baseline, same persistent Node session, zero intervening tab/binding action, and never-declared fresh close eligibility are mandatory. No discovery call is allowed. Any outcome spends the gate; no retry, fallback, continuation, alternate handle, or verdict relaxation exists.

## Disposition

Static review is complete and **PASS**. Any live direct-close remains a separate one-shot authority consumption and its redacted result requires independent post-action classification. `authorizes_live_execution=false`.
