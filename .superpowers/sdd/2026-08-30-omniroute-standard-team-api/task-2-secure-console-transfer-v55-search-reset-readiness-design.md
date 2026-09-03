# V55 search-reset readiness replacement design

`authorizes_live_execution=false`

## Replacement and narrow delta

V54 was sent once, failed cleanly, and is permanently spent. It may not be
retried, continued, reused, reinterpreted, relaxed, or used as fallback. V55
is a new consumed-before-import one-shot replacement. This design is offline
only and authorizes no live action.

The V54 incident proves the current search field can be nonempty on arrival.
Fresh read-only diagnosis further proves that `fill("")` alone is insufficient:
the field can become empty while the URL and table still show the prior search
and `No results found for your search`. V55 changes only readiness by requiring
a bounded reset convergence before the existing unfiltered baseline check.

## Reset convergence contract

After exact API Tokens navigation, V55 requires exactly one visible
`#user-api-tokens-search` input and exactly one current token table. It shall:

1. read the input value; if nonempty, perform exactly one `fill("")`; if empty,
   perform no fill;
2. after a fill, wait for the exact base URL
   `https://dash.cloudflare.com/profile/api-tokens` with no query or fragment;
3. wait until the exact sentinel `No results found for your search` is hidden
   or detached from that same table; and
4. only then read the empty input and evaluate the existing non-busy,
   1..1000-row, ordered-header, zero-target unfiltered baseline.

Every reset read, fill, URL wait/read, and sentinel wait/read has exact
attempted/fulfilled counters. A duplicate/missing/unsafe input or table,
wrong/reset-stale URL, visible sentinel, counter mismatch, throw, or uncertainty
fails before the target-name filter, Create read, or retained binding. Fixtures
must cover initially empty and stale-filter success; field-only clear with stale
URL/table; sentinel residue; wrong base URL; duplicate/missing controls;
counter vectors; cleanup/output failure; and the existing current-table matrix.

## Literal transport and retained boundaries

The V55 source and candidate remain ASCII. The session name must use
`String.fromCodePoint(0x1F510)+" OmniRoute secure console"`; no literal emoji
or Unicode escape is permitted in the candidate. The direct-cell send contract
must preserve the committed UTF-8 bytes exactly: action-time transport proof
uses an inert literal payload at least candidate length, records byte count and
fixed PASS, resets the disposable realm, and any byte discrepancy stops before
the one V55 send.

V55 retains V54's source projection and runtime/documentation pins; complete
ordinary-array descriptor validation; exact URL selection and claim; account
signature; current table, target filter, and Create-never-clicked contract;
fixed sanitized output; success-only binding; one-proof cleanup; no retry,
fallback, mutation, clipboard, credential, secret, storage, provider, DNS, VM,
tab, or external communication action. The fresh audit covers all fixed 125
V35-V53 predecessor declarations. Failure clears every binding and spends V55.

## Evidence and later gate

Implementation must provide candidate-derived pure fixtures for all retained
and reset cases, syntax/ASCII/byte-ceiling proof, and an independent Sol High
zero-finding review. A later non-self-referential classification, fresh pins,
exact external browser confirmation, and byte-preserving transport proof remain
mandatory before any send. Final Create/copy/paste and row deletion remain
separate external confirmations.
