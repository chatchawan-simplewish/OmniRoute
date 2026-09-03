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
2. on both branches, wait/read the exact base URL
   `https://dash.cloudflare.com/profile/api-tokens` with no query or fragment;
3. on both branches, wait/read until the exact sentinel `No results found for
   your search` is hidden or detached from that same table; and
4. on both branches, read the input again and require empty before evaluating
   the existing non-busy,
   1..1000-row, ordered-header, zero-target unfiltered baseline.

The initially-empty success vector is `initialRead 1/1`, `resetFill 0/0`,
`resetUrlWait 1/1`, `resetUrlRead 1/1`, `resetSentinelWait 1/1`,
`resetSentinelRead 1/1`, `finalRead 1/1`, and `baselineRead 1/1`; the stale
nonempty success vector differs only by `resetFill 1/1`. Each boundary
increments attempted before its effect and fulfilled only after success. For a
false completed read, that boundary is `1/1`; for throw, timeout, or malformed
URL/result it is `1/0`. Each such earliest stop retains only its reviewed
attempted/fulfilled prefix, makes every later reset counter `0/0`, and makes
every target filter/Create/name/row counter `0/0`. The inherited local
`bindingAttempted/bindingFulfilled` counter is already `1/1` before API Tokens
navigation and therefore remains `1/1` on both success vectors and every
reached reset earliest-stop vector; its persistent success-only binding remains
null and ineligible on every reset failure. Fixtures enumerate both success
vectors and every earliest-stop vector with those local and persistent states.
A duplicate/missing/unsafe input or table,
wrong/reset-stale URL, visible sentinel, counter mismatch, throw, or uncertainty
fails before the target-name filter, Create read, or retained binding. Fixtures
must cover initially empty and stale-filter success; field-only clear with stale
URL/table; sentinel residue; wrong base URL; duplicate/missing controls;
counter vectors; cleanup/output failure; and the existing current-table matrix.

## Literal transport and retained boundaries

The V55 source and candidate remain ASCII. The session name must use
`String.fromCodePoint(0x1F510)+" OmniRoute secure console"`; no literal emoji
or Unicode escape is permitted in the candidate. The inert literal payload is
capacity-only: it proves acceptance at least as large as the candidate and is
then reset. Separately, the coordinator compares actual literal-cell payload
UTF-8 bytes and SHA-256 with the committed candidate blob before execution;
transform, mismatch, absence, or uncertainty stops before import or browser
effect. Fixtures assert ASCII source/candidate, the exact construction, and no
literal emoji or Unicode escape.

V55 retains V54's source projection and runtime/documentation pins; complete
ordinary-array descriptor validation; exact URL selection and claim; account
signature; current table, target filter, and Create-never-clicked contract;
fixed sanitized output; success-only binding; one-proof cleanup; no retry,
fallback, mutation, clipboard, credential, secret, storage, provider, DNS, VM,
tab, or external communication action. The fresh audit covers `132`
predecessor declarations: the inherited `125` V35-V53 names plus
`secureConsoleOwnedTaskTabV54`, `secureConsoleOwnedTaskTabV54Eligible`,
`secureConsoleOwnedTaskTabV54State`,
`secureConsoleOwnedTaskTabV54PreCreateDetachConsumed`,
`secureConsoleOwnedTaskTabV54PostNativeDetachConsumed`,
`secureConsoleCloudflareReadsV54Consumed`, and `secureConsoleV54Consumed`.
Each fixture contamination fails before import, attachment, browser effect, or
page mutation. Failure clears every binding and spends V55.

## Evidence and later gate

Implementation must provide candidate-derived pure fixtures for all retained
and reset cases, syntax/ASCII/byte-ceiling proof, and an independent Sol High
zero-finding review. A later non-self-referential classification, fresh pins,
exact action-time tool-state self-verification of browser/profile/window/tab
ID/URL/provider object and exclusive control, and byte-fidelity comparison
remain mandatory before any send. Ambiguity or a higher-priority rule pauses
fail-closed. Final Create/copy/paste and row deletion remain separate external
confirmations.
