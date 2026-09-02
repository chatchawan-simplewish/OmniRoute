# OmniRoute V43 fresh-realm token-page readiness — design brief

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Trigger and boundary

V41 was consumed once and passed, but its retained CUA lexical binding is no
longer present. V41 must not be retried or reinterpreted. V42 remains
unexecuted and cannot satisfy its exact same-realm predecessor precondition.

V43 is the smallest replacement: one newly reviewed, fresh-realm, one-shot
gate that composes V41's reviewed attachment semantics with V42's reviewed
token-page readiness semantics. It does not reuse any V41 or V42 live binding,
and it creates new V43-only declarations. No browser or provider action is
authorized by this design brief.

## Exact design

The single V43 cell must:

1. declare every V43 binding once and mark V43 consumed before import, setup,
   enumeration, claim, navigation, or page work;
2. import the pinned Computer Use runtime once, call setup once with no
   options, acquire Chrome once, read the complete API documentation once and
   write it once, set the exact reviewed session name once, and call
   `openTabs` once;
3. preserve V41's complete cross-realm array, descriptor, no-symbol, rank-zero
   record, bounded-string, exact HTTPS `dash.cloudflare.com`, and later-record
   noninspection contract;
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
only literal `Error`. Terminal-output failure must repeat complete cleanup.

## Pure fixture requirements

The inert fixture must extract the sole LF-normalized V43 executable and prove:

- syntax and exact brief/executable bytes and SHA-256;
- complete success state, exact counter vector, sole retained V43 tab binding,
  and absence of broad runtime/controller residue;
- rejection before claim for malformed array/descriptor/symbol/rank-zero
  inputs, including proof that later offered-record values are never read;
- bounded cleanup and complete counter vectors for import, setup,
  documentation, enumeration, claim, account-home navigation/signature,
  token-page navigation/signature/filter, and terminal-output failures; and
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
