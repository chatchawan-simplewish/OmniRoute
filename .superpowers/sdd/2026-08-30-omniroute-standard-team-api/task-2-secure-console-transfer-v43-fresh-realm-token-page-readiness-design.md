# OmniRoute V43 fresh-realm token-page readiness — design brief

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Trigger and boundary

V41 was consumed once and passed, but its retained CUA lexical binding is no
longer present. V41 must not be retried or reinterpreted. V42 remains
unexecuted and cannot satisfy its exact same-realm predecessor precondition.
V42 is therefore superseded and static: it must never be executed,
reinterpreted, or used as fallback, including if V43 fails.

V43 is the smallest replacement: one newly reviewed, fresh-realm, one-shot
gate that composes V41's reviewed attachment semantics with V42's reviewed
token-page readiness semantics. It does not reuse any V41 or V42 live binding,
and it creates new V43-only declarations. No browser or provider action is
authorized by this design brief.

## Exact design

The single V43 cell must:

1. declare every V43 binding once, prove its exact declared null/false/
   uncreated defaults, and mark V43 consumed before evaluating the remainder of
   the declaration-shape precondition or performing import, setup, enumeration,
   claim, navigation, or page work; the remainder must prove the relevant
   V35-V42 consumption, owned-tab, eligibility, state, setup, agent, and Chrome
   sentinels are `undefined` in the new realm;
2. import the pinned Computer Use runtime once, call setup once with no
   options, acquire Chrome once, read the complete API documentation once and
   write it once, set the exact reviewed session name once, and call
   `openTabs` once;
3. preserve V41's complete cross-realm array, descriptor, no-symbol, rank-zero
   record, bounded-string, exact HTTPS `dash.cloudflare.com`, and later-record
   noninspection contract; rank-zero selection is justified only by the pinned
   documented last-opened/focused ordering and a fresh external owner
   confirmation that the intended Cloudflare task tab is selected and no other
   Chrome profile/window competes at action time;
4. claim only the rank-zero tab once, prove exact controller identity, perform
   exactly one account-home navigation and one account-home URL/signature read
   with exact account-home path, exactly one `mysw.me` zone anchor, positive
   bounded anchor count, and zero busy markers;
5. perform exactly one subsequent navigation to
   `https://dash.cloudflare.com/profile/api-tokens`, one URL read, and V42's
   unchanged inherited V4 token-page signature and completeness reads;
6. fill only the sole semantic search textbox with the fixed non-secret query,
   prove the exact filtered terminal state, count the exact semantic Create
   Token control read-only, and never click Create;
7. on success retain only one controller-owned V43 task-tab binding and its
   eligibility/state/consumption flags; clear the setup function, agent,
   Chrome controller, offered listing, and every temporary or predecessor
   binding, and prove sole-binding/no-residue before reporting PASS; and
8. on any mismatch, exception, timeout, or terminal-output failure, clear all
   V43 bindings and eligibility, emit only fixed secret-safe evidence, stop
   consumed, and provide no retry, fallback, reconnect, alternate navigation,
   selected/list/get fallback, new-tab, close-tab, or manual integration path.

The cell must have exact operation counters and an explicit complete counter
vector for success and every fixed failure stage. The unbound catch may emit
only literal `Error`. Terminal-output failure must repeat complete cleanup,
rethrow without inspecting or logging the thrown value, and make no second
write.

The exact fixed-schema output may contain only bounded booleans, exact operation
counters, fixed state/result/error literals, and approved bounded counts. It
must never contain an offered listing, record metadata, tab ID, raw URL,
account segment, DOM-derived text, credential, secret, or thrown value.

## Pure fixture requirements

The inert fixture must extract the sole LF-normalized V43 executable and prove:

- syntax and exact brief/executable bytes and SHA-256;
- complete success state, exact counter vector, sole retained V43 tab binding,
  absence of broad runtime/controller residue, and the exact output key set;
- rejection before claim for malformed array/descriptor/symbol/rank-zero
  inputs, including proof that later offered-record values are never read;
- rejection before import/action for contaminated V35-V42 predecessor
  declarations and nonfresh V43 defaults, with exact partial counters and full
  cleanup;
- bounded cleanup and complete counter vectors for import, setup,
  documentation, enumeration, claim, account-home navigation/signature,
  token-page navigation/signature/filter, and terminal-output failures; and
- both a thrown plain data-name token and a thrown object whose `name` getter
  throws, proving fixed output, absence of the token, zero getter calls, exact
  counters, consumed/ineligible state, full cleanup, and exact output keys; and
- zero real browser, provider, clipboard, credential, DNS, routing, VM,
  listener, proxy, owner, or network action.

## Preserved constraints

The runtime module pin remains `149771` bytes / SHA-256
`A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`.
The API docs pin remains `58480` bytes / SHA-256
`A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.

The stable projection remains `10661` records / SHA-256
`C4C85893769D133224AC7404B628C8B0D4B0EBBFF471620B158E652E152B4EBD`.
The exact 12-path product baseline, clean evidence worktree, zero residue,
absent public DNS, VM1205 safe checkpoint, archived prior owner, and sole-owner
constraints remain mandatory action-time pins.

The action-time realm must be newly reset and declaration-free for every named
V35-V43 sentinel before the single send. Immediately before the single
`openTabs` call, the owner must freshly and externally confirm exactly:

`Chrome Profile Codex-Chrome-Bell-PC2, intended window, and intended Cloudflare task tab are selected; no other Chrome profile/window is offered to the extension.`

That confirmation cannot be inferred, automated, delegated, or satisfied by a
design/review artifact. Any selection, ordering, declaration, or realm drift or
uncertainty stops V43 consumed before claim, without listing fallback,
selected-tab fallback, get fallback, new-tab, reconnect, or manual fallback.

No secret may be printed, committed, logged, or placed in evidence. The final
Create/native Copy/native masked Paste confirmation and the later separate
exact-row deletion confirmation remain mandatory, external, and cannot be
pre-approved, automated, delegated, or waived.

## Review and execution boundary

Implementation may begin only after independent Sol High PASS review of this
design. The executable/fixture package then requires its own immutable commit,
independent Sol High PASS review, non-self-referential classification, and
separate post-commit coordinator tuple. Only after every action-time pin passes
may the sole Sol High owner consume V43 once.

`authorizes_live_execution=false`
