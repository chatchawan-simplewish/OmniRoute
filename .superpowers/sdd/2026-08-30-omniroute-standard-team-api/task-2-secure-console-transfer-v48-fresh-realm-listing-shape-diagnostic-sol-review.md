# OmniRoute V48 fresh-realm listing-shape diagnostic Sol High review

Date: 2026-09-03 (Asia/Bangkok)
Reviewer: Codex, independent Sol High security review
Review package commit: `b55b7742c5447e59070c203cf81a9d398ea858bb`
Review package parent / exact target: `a9b3332a7b1b7141778758a3d50bc5b12db7abe0`
Exact target parent: `5d7a11bc6b0b78d6a00e2d016350d547e7f4971b`

## Verdict

`FAIL`

`authorizes_live_execution=false`

One IMPORTANT finding remains. The V48 predicate vector is not semantically
isomorphic to the consumed V47 trusted-listing predicate, so a live V48 result
cannot reliably identify the exact V47 rejection class. No V48 live send,
classification as eligible, browser action, provider action, retry, fallback,
or reinterpretation is authorized by this review.

## Exact-byte evidence

The four review targets were read directly from target commit
`a9b3332a7b1b7141778758a3d50bc5b12db7abe0`. Their blobs are unchanged at the
review-package commit.

| Artifact | Bytes | SHA-256 | Git blob |
| --- | ---: | --- | --- |
| Design | 8827 | `199BADF7B69629F0CAE1FCB8F49D2A8F7A3B8F1BD5A4E7FC3EF4FAB0A393CE6A` | `eb9ac9e0d8f89afa5998d0d3b200e6f15736441f` |
| Implementation plan | 11657 | `D3B71A9749B5CF20F663F050C528CFA7299E2F3F652E42DA666D925FE20390E4` | `683591b5d447aa32deb79a997125bd6cfa9bf554` |
| Executable | 17178 | `6686679836226820EFC47DF24C39CD7241CC165403C2B40D208374A1E87C7D05` | `cd68a49f1a0b1e9057b97f098b2b07f9124b4ae3` |
| Pure fixture | 9862 | `553F8B0A7FDF0985C3EB0886DB00206D04BEBE8FC16A20F12E3C49904C8ABA46` | `4743c02559b0026ba046c6adb80031babdb366f1` |

The review package itself is 6823 bytes, SHA-256
`77FB174036854ACB651928C69EB0E6AB39E4CB17D915DD927A4DA59C3137B7FE`,
blob `36f233b3d2ee69ff56d57d711814ca7d77283bf4`. The candidate/target diff for
the four review targets is empty.

The pinned local runtime was read as 149771 bytes with SHA-256
`A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`.
The pinned complete API documentation was read as 58480 bytes with SHA-256
`A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.
No CUA, Chrome, tab, provider, network, DNS, VM, or authority-gate action was
performed. The already-passing fixture suite was not rerun: the blocking issue
is a direct semantic comparison that its current cases do not exercise.

## Finding

### V48-001 — IMPORTANT — The diagnostic adds and omits predicates relative to V47

The design says V48 identifies which existing V47 trusted-listing predicate
rejected the listing and must not invent a new accepted shape. The executable
does not preserve that boundary in two material ways:

1. V47 validates that every array index has an own enumerable data descriptor,
   then applies the non-null/plain-record checks only to the rank-zero value
   (`V47` lines 170-182). V48 additionally emits
   `allIndexValuesNonNullObjects` by requiring *every* indexed value to be a
   non-null object (`V48` lines 181-191). A primitive value at a later rank can
   make this V48 flag false even though that condition did not reject V47.
2. V47's URL predicate requires HTTPS, exact Cloudflare hostname, empty port,
   empty username, and empty password (`V47` lines 217-220). V48 reports only
   HTTPS and hostname from that predicate, omits the port/username/password
   subpredicates, and adds an exact `/profile/api-tokens` pathname flag that V47
   never used at listing validation (`V48` lines 299-303). Consequently an
   explicit port or userinfo can reject V47 without a corresponding V48 flag,
   while an unrelated pathname can produce a false V48 signal even though V47
   would accept it at this boundary.

This blocks required question 4 and makes the design, implementation, and
fixture mutually inconsistent under question 10. It does not create a direct
secret-exposure or provider-mutation path, but it defeats the diagnostic's sole
purpose and could drive an incorrect replacement contract.

Required correction: make the emitted historical-predicate vector correspond
exactly to V47. Remove or explicitly segregate non-V47 contextual predicates;
add fixed booleans for V47's empty port, username, and password checks; and add
fixtures proving a later-rank primitive plus URL port/userinfo/path cases are
classified exactly as V47 classified them. The fix review must re-check all ten
questions against new committed bytes.

## Required review questions

| # | Answer | Evidence and boundary |
| ---: | --- | --- |
| 1 | Yes | V47 is declared consumed and permanently non-reusable; V48 has a distinct consumed/state/result gate and references V47 only as a fresh-realm declaration guard. |
| 2 | Yes | Output keys are fixed; descriptor values, keys, identifiers, title, group, URL, exceptions, and secret-like fixture values are not returned or stringified. |
| 3 | Yes | The open-tabs path uses cached own-property descriptors and reads only returned descriptor data; accessor fixtures prove getters are not invoked and no direct untrusted indexed read is used. Throwing proxy traps escape the pure inspector into the fixed outer catch. |
| 4 | **No** | V48 adds an all-ranks object condition, omits three V47 URL-origin conditions, and adds a pathname condition. It cannot faithfully name the exact V47 rejection class. See V48-001. |
| 5 | Yes | Result keys are statically constructed. Counts and lengths are bounded or `-1`; attempt/fulfilment counters are fixed zero/one values. |
| 6 | Yes, for secrecy | URL parsing occurs only after an own data descriptor and bounded control-free string check; raw URL and parsed bindings are not emitted and are cleared. Historical predicate completeness still fails under question 4. |
| 7 | Yes | Success and failure states are permanently ineligible, forbidden-operation counters remain zero, and browser/listing bindings are nulled in `finally`. Any uncertainty still spends the one-shot gate. |
| 8 | No, for completeness | The fixtures cover the stated getter, symbol, sparse, prototype, malformed, cross-realm, and fixed-failure boundaries without proving live eligibility, but they do not expose V48-001's V47 semantic divergences. |
| 9 | Yes | The runtime path and API surface are fixed; there is one import/setup/connect/docs/name/openTabs path and no retry, fallback, alternate browser, DevTools, claim, navigation, wait, or manual integration. |
| 10 | **No** | Design and plan promise exact V47 rejection diagnosis; executable and fixture implement the divergent predicate vector in V48-001. |

## Confirmed boundaries

- The V47 incident remains fixed at
  `28a77a3fed0816709d390129552fc5d3bed17957`; V47 stays spent and cannot be
  retried, continued, reused, relaxed, or reinterpreted.
- V48 remains diagnostic-only and permanently ineligible for tab adoption on
  every outcome.
- No claim, navigation, wait, page URL read, snapshot, DOM or clipboard action,
  provider mutation, token creation, secret output, DNS action, VM action, or
  background process exists in the reviewed live path.
- The mandatory later classification, post-commit tuple, action-time pins,
  fresh-realm declaration audit, and exact external tab confirmation remain
  mandatory after a future PASS review. The later Create/native Copy/native
  masked Paste and exact-row deletion confirmations remain preserved and
  unreached.

## Severity counts

- Critical: 0
- HIGH: 0
- IMPORTANT: 1
- Minor: 0
