# OmniRoute V23 retained-tab prestart reads — live incident

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Consumed gate

- Brief commit:
  `e3c9aff865ec6d9200b02325050908b40ab9f90b`.
- Independent Sol High PASS review commit:
  `1fb949d6aa5306e39d0d211ce4fae8787da3775a`.
- Classification commit:
  `50a3ce4b3a445f2bc8d8ba4cb00260ef631ced9b`.
- Executable: `28122` UTF-8 bytes, SHA-256
  `9724EE66F0AB5C1F185AF255CF053AF4CB4EF127BF29509CEFA8523A232A654D`.
- Sole call result: `PRECONDITION_FAIL`.
- `prestart_consumed=true`; no retry, reuse, continuation, reinterpretation,
  fallback, or verdict relaxation is permitted.

## Non-consuming preparation correction

The first local extraction wrapper verified the exact payload bytes and hash
but stopped before the Node/browser tool call because it incorrectly compared
the UTF-8 byte count `28122` to the JavaScript UTF-16 character count
`28118`. The reviewed paginator regular expressions contain non-ASCII dash
characters. A fixed-output persistent-state check then proved the prestart flag
was still false, the exact V23 handle remained retained/eligible, and its state
was unchanged. No gate or browser code was evaluated by that wrapper attempt.

The corrected wrapper retained the exact byte/hash proof, required the exact
character count `28118`, and made the sole Node/browser call.

## Sanitized live terminal

- declarations and precondition: true/true;
- navigation: `1/1`;
- click, readiness, and fill: `0/0`, `0/0`, and `0/0`;
- every DNS/rate/Tunnel/Access/token result remained at its fixed initial
  false or `-1` value;
- exact-handle close: `1/1`;
- retained handle false; eligible false;
- state: `CLOUDFLARE_PRESTART_READS_FAILED_CLEAN_V23`;
- cleanup: `FAILURE_EXACT_TAB_CLOSED`;
- residue converged true; consumed true; write attempted `1`;
- sanitized error class: `Error`.

The deterministic failing boundary is the first
`readyOne(zoneAnchor)` call after the fulfilled dashboard-home navigation.
Its internal exact locator count check failed before incrementing the readiness
counter, so the `a` locator filtered by `mysw.me` did not count exactly one.
No anchor text, href, account identifier, DOM, or page content was emitted.

## Side-effect boundary

The gate performed one navigation and read-only locator counting only. It made
zero click, fill, Create, edit, delete, credential, clipboard, secret, VM, DNS,
routing, listener, process, or provider-persistent mutation. The exact tab
closed and no browser handle remains.

A replacement must start from a new reviewed fresh-tab contract and may use
the incident only as static evidence that the dashboard-home exact zone-anchor
assumption is obsolete. It must not retry or continue this gate.

The mandatory combined final Create/native Copy/native masked Paste
confirmation and later separate exact-row deletion confirmation remain
unreached and mandatory.

`authorizes_live_execution=false`
