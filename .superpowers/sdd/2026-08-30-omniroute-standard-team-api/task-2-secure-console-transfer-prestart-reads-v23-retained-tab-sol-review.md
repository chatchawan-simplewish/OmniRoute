# OmniRoute V23 retained-tab prestart reads — independent Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Scope and authority

This review covers only commit
`e3c9aff865ec6d9200b02325050908b40ab9f90b` and exact path
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-prestart-reads-v23-retained-tab-brief.md`.
Its direct parent is V23 live PASS report commit
`029ebf916c4c9e7017e72e4f1eefe1c447ea00ad`.

I independently reviewed direct committed bytes, syntax, exact retained-handle
ownership, the one-shot and interrupted-state boundary, inherited V4
credential-free DNS/rate/Tunnel/Access reads, the V23 direct token-inventory
replacement, navigation/click/readiness/fill cardinalities, synchronous
cross-realm output, exact-handle failure cleanup, provider/secret exclusions,
and both mandatory manual confirmation boundaries.

I performed no Chrome, Node browser binding, provider, clipboard, credential,
process, network, DNS, routing, Prox-01, or VM action and did not evaluate the
reviewed cell. The only workspace write is this assigned review artifact.

## Final verdict

**PASS** — zero unresolved Critical, HIGH, or IMPORTANT findings. The contract
spends its own read gate and makes the exact V23 handle ineligible before its
first executed await, preserves the reviewed credential-free inventory reads,
and retains or closes only that exact handle according to a fail-closed state
machine.

`authorizes_live_execution=false`

## Direct-byte, syntax, and Git evidence

- Reviewed commit: `e3c9aff865ec6d9200b02325050908b40ab9f90b`.
- Direct parent: `029ebf916c4c9e7017e72e4f1eefe1c447ea00ad`.
- The reviewed commit adds exactly the assigned prestart-read brief path.
- Brief: `32272` bytes, SHA-256
  `F0A7D75B94B25240F61B727F89C202D1D35A4BAD42BFC27B0C1615228D030CD0`,
  Git blob `c968c743c73cf70411aa5d87142fa411b15afcb2`.
- Executable payload: `28122` bytes, SHA-256
  `9724EE66F0AB5C1F185AF255CF053AF4CB4EF127BF29509CEFA8523A232A654D`.
- Encoding is UTF-8 without BOM and LF-only with zero CR bytes. There is one
  `javascript` fence and no extra blank line at EOF.
- Non-evaluating top-level-awaited JavaScript parse: **PASS**. The outer IIFE
  is awaited exactly once.
- `git diff-tree --check` reports no whitespace error.
- Index before review creation: zero paths. The exact inherited twelve-path
  dirty baseline was present and remained unstaged.

## V23 live PASS predecessor

The direct-parent report is the sole one-path commit of
`.superpowers/sdd/2026-08-30-omniroute-standard-team-api/task-2-secure-console-transfer-token-page-readiness-v23-live-pass.md`.
Its committed/local bytes reproduce as `2365` bytes, SHA-256
`26DFEE63EFB1016A677DD211928ABB1C396C659CFD65012E9D043493681FCAD1`,
and blob `30a591517ca2d5472c6503d6b7c4126edd2d2869`.

That immutable report binds:

- brief `5f9e79f5a5f9a68404d7b6df86a895e6b8b479ec`;
- independent PASS review
  `0f35a07dccb57efdb16d737173923357afd51f34`;
- classification `c3a2b226986c81d753f7d6417d9fe65267f86575`;
- exact V23 readiness result
  `EXACT_V23_TOKEN_PAGE_SEMANTIC_READINESS_PASS`;
- V23 readiness consumed, exact handle retained, eligibility true, state
  `TOKEN_PAGE_SEMANTIC_READY_ELIGIBLE_V23`, error `NONE`, and no close attempt.

The prestart executable accepts only that exact persistent tuple: the V23
readiness gate must be consumed; the handle must be non-null and eligible; both
detach flags must remain false; state must be the exact readiness-PASS state;
and this prestart-read flag must be fresh before the executable synchronously
sets it consumed.

## One-shot and interrupted-state safety

The first executable statements snapshot freshness and set
`secureConsoleCloudflareReadsV23Consumed = true`. After synchronous declaration
and predecessor validation, the exact durable V23 handle is captured locally,
then the durable eligibility is set false and state becomes
`CLOUDFLARE_PRESTART_READS_RUNNING_V23`. All three transitions occur before the
first executed await (`navigate` to the dashboard).

There is no asynchronous boundary between successful predecessor validation,
local exact-handle capture, ineligibility, and the running state. Consequently:

- an interruption at any later await leaves the gate spent and the durable
  handle ineligible/running;
- the same gate cannot be retried, continued, or reinterpreted;
- no selected/list/get/new/reconnect path can reacquire another tab; and
- only a normally completed exact PASS re-enables that same handle.

On an ordinary caught failure after capture, cleanup first preserves
ineligibility and records a closing state, then attempts exactly one close on
the local handle only when it still equals the durable binding. A fulfilled
close clears the durable binding only afterward. A rejected close retains the
same exact handle ineligible and reports unconverged residue. If exact identity
or close shape cannot be proven, the handle is not guessed or cleared; the
state reports residue unproven. No branch claims clean residue prematurely.

## Credential-free target safety and completeness

### Zone/account binding

The first fixed navigation reaches only `https://dash.cloudflare.com`. The
unique visible `mysw.me` anchor must expose an HTTPS `dash.cloudflare.com` href
whose path contains exactly one 32-hex zone/account segment and exact zone
name. The Zero Trust href must be HTTPS `one.dash.cloudflare.com`, repeat the
same 32-hex segment, and land on a page whose URL and account-relative anchor
markers reproduce that same segment. IDs and hrefs remain local and are never
emitted.

### DNS, Tunnel, and Access filters

The five reviewed `filteredZero` executions cover:

- DNS hostname `ai-api-omniroute.mysw.me`;
- Tunnel name `omniroute-team-tunnel`;
- Tunnel hostname `ai-api-omniroute.mysw.me`;
- Access application hostname `ai-api-omniroute.mysw.me`; and
- Access application name `OmniRoute team API`.

Each exact visible filter must count one and bind a unique sanitized
`aria-controls` result root. Before query, that root must have a unique visible
paginator and prove either an exact complete non-empty inventory or exact
disabled `0–0 of 0` terminal state with no busy marker. Each fixed query is
then entered by a page-local fill, the exact empty status must become uniquely
visible, query echo must be exact, the paginator must prove `0–0 of 0`, and
all target row counts must be zero. The helper's evaluator object has exactly
the two fixed boolean fields created by the reviewed callback; only strict
`true` comparisons influence acceptance and no object or page value is
emitted.

These fills are credential-free inventory filters. They do not submit a form,
click a mutation control, or carry a secret. The DNS, Tunnel, and Access menu
clicks are exact-count-one navigation/expansion targets followed by reviewed
readiness markers.

### Rate-limit table

The rate button is uniquely visible and its sanitized `aria-controls` binds
one exact panel, paginator, and table. One synchronous fixed-key evaluator
proves the table is the panel's sole table, the paginator text exactly reports
`1–1 of 1`, both pager buttons are unique and disabled, the panel is not busy,
there is exactly one unrelated row, and the target description and hostname
occur zero times.

The evaluator returns only five statically named booleans/counts derived from
row lengths and regex occurrence lengths. Acceptance collapses them to exact
`1/0/0` and strict boolean equality; terminal output manually enumerates only
those count/boolean fields. No table text or provider identifier escapes.

### V23 direct token inventory

The final token-page navigation is exact and intentionally performs no token
filter fill or activation. The V23 replacement repeats the independently
reviewed direct unfiltered inventory proof:

- one connected, visible, exactly empty search input in the nearest
  depth-three section;
- page/section tables `2/1`, one table body, five physical rows, and all five
  visible;
- zero grid, pagination, page/section busy state, status/empty status, and
  section Create-like action;
- zero exact V4 empty marker and five visible non-empty candidate rows;
- one global actionable exact `Create Token`; and
- zero exact target-name and target-row matches.

The evaluator result must pass the pinned cross-realm plain-record predicate,
exact-key equality, explicit boolean types, and bounded safe-integer validation
before a new local fixed-key projection is accepted. This preserves V23's
complete five-row unfiltered target-absence proof without reusing the obsolete
query/keypress path.

## Exact call cardinality

Static helper expansion and the terminal counter assertions agree:

- navigations: `6/6` — dashboard, zone, Zero Trust home, repeated Tunnel home,
  repeated Access home, and final token page;
- menu clicks: `13/13`, all through one helper that requires target count one
  before clicking;
- native readiness: `32/32` — twenty-two direct ready targets, five paginator
  readiness calls inside the five filter invocations, and five terminal-empty
  waits;
- page-local fills: `10/10` — one clear and one fixed query for each of five
  inventory filters;
- direct call sites: one `goto` helper body, one `click` helper body, two
  `waitFor` sites, two `fill` sites, four synchronous evaluator sites, four URL
  reads, one exact-handle close, and one terminal write; and
- zero tabs.new, selected/list/get, reconnect, Create/edit/delete, submit,
  clipboard, screenshot, retry, fallback, `MutationObserver`, page timer, or
  page Promise call site.

Every success counter is checked for exact attempted/fulfilled equality before
PASS. Partial navigation, click, readiness, or fill rejects acceptance.

## Fixed safe output and secret boundary

All page evaluator callbacks are synchronous and return only statically named
booleans or counts. Intermediary filter state is consumed only through strict
boolean comparisons. Rate and token fields are projected into separately named
local count/boolean variables; the token object additionally passes the full
cross-realm exact-key/type/range validator. Terminal output has a static key
list and contains only fixed result/state/cleanup strings, a sanitized error
class, booleans, counts, counters, and residue state. No object spread or raw
evaluator result is emitted.

Executable scans find no Bearer value, JWT-like value, forty-plus-character
hex secret, credential read, clipboard call, screenshot, provider response,
or secret-storage access. Local account/zone segments and hrefs are validated
but not written. All explicit page interactions are credential-free reads or
navigation; there is no Create, edit, delete, DNS/provider write, VM, routing,
listener, or process action.

## Mandatory confirmation boundaries

Exact PASS authorizes only a later separately committed and independently
reviewed credential-free clipboard-clear/proxy/preparation/owner/form path. It
does not authorize final Create, native Copy, or native masked Paste. Their
combined manual confirmation remains mandatory. The later separate exact-row
deletion confirmation also remains unreached and mandatory.

## Finding counts and limits

- Critical: `0`.
- HIGH: `0`.
- IMPORTANT: `0`.
- Minor: `0`.

This review proves only the committed static contract. It does not prove the
current retained browser handle, provider UI, action-time hashes, VM state, or
live inventory and does not authorize execution. Those pins and the separate
classification remain mandatory before the sole call.

## Final verdict

**PASS**

Unresolved findings: Critical `0`, HIGH `0`, IMPORTANT `0`, Minor `0`.

`authorizes_live_execution=false`
