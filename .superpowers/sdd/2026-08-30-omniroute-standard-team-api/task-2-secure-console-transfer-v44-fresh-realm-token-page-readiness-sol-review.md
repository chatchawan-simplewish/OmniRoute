---
status: issues_found
depth: deep
files_reviewed: 3
findings:
  critical: 0
  high: 0
  important: 1
  minor: 0
  total: 1
---

# OmniRoute V44 fresh-realm token-page readiness package — Sol High review

Date: `2026-09-02` (`Asia/Bangkok`)

`authorizes_live_execution=false`

## Verdict

**FAIL**

The V44 executable preserves the independently reviewed V43 behavior and adds
the intended new gate identity, installed runtime path, and explicit V43
predecessor-declaration rejection. The inert fixture passes its implemented
matrix. The package nevertheless fails its own immutable-output contract: the
brief requires the fixture terminal to print the directly computed fixture
byte/hash tuple, but the fixture neither reads nor hashes itself and its terminal
omits both fields. V44 must not be classified or consumed from this package.

This is a static package-quality review only. It authorizes no CUA, Chrome,
provider, live-resource, VM, secret, confirmation, or authority-gate action.

## Reviewed lineage and exact package

- Candidate commit: `03124f13fedd4474eef57dc13f678b7fed7999bd`.
- Direct parent and V43 runtime-path drift incident commit:
  `f41691acb307954a28c131e12658fd1857e33838`.
- The candidate adds exactly the assigned V44 brief, executable, and fixture.
- Brief: `6165` bytes; SHA-256
  `96E790BD29EDB388399366B8AA064B7A65383235FAF1B0D05CE93E1D576D794D`;
  blob `9cbd2292a3ff668d2c466a7c5a8b0c78d350c78a`.
- Executable: `39687` bytes; SHA-256
  `75F4700B6519A1EA519FE509053735B85E1690A25D5C302B566293A86BF82F67`;
  blob `1a085198bbf6a7a4bbd898290e70fac2d6645d21`.
- Pure fixture: `45955` bytes; SHA-256
  `E63752DD544605D64DDB43F79CDF60D24B9E413F9E8F7C75499B2EA7BB16EA40`;
  blob `bf1177df84b1ea8e0c33b1b3bdddaa0c370f8161`.
- Each candidate file has exactly one final LF and no CRLF. The candidate diff
  passes `git diff --check`.
- The installed browser module at the newly pinned `26.831.21537` path is
  `149771` bytes / SHA-256
  `A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`.
- The installed API documentation at the newly pinned `26.831.21537` path is
  `58480` bytes / SHA-256
  `A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.
- Both former `26.831.20005` paths are absent, matching the committed V43 drift
  incident. The new module was not imported and the documentation was not
  invoked during review.
- The prior V43 PASS review at
  `a3603b212749d4b3a2195dadfb8d7c126ee70b47` and classification at
  `5bec70c591e7ab020b3605f8442942faf0fe16f1` were treated only as static
  predecessor evidence.
- The index was empty before review work. The exact pre-existing 12-path dirty
  product baseline was not edited or staged.

## Exact semantic delta from V43

A direct-byte normalization proves the V44 executable is exactly the reviewed
V43 executable with only:

1. every V43 gate/result/local identifier renamed to V44;
2. Chrome runtime `26.831.20005` changed to `26.831.21537`; and
3. seven V43 top-level predecessor declarations added to the absence predicate:
   owned tab, eligibility, state, both detach flags, Cloudflare-read consumed,
   and overall consumed.

After applying only those transformations, the expected and actual executable
are byte-identical at `39687` bytes.

The V44 fixture is likewise exactly the V43 fixture with the corresponding V44
renames, runtime/executable-hash pin changes, seven individual V43 declaration-
contamination cases, and the terminal `v43PredecessorsAbsent: true` claim. After
those transformations, expected and actual fixture bytes are identical at
`45955` bytes. Each added contamination case stops before setup and `openTabs`,
leaves V44 consumed/ineligible, and requires fixed cleanup.

## Static and inert checks

- Executable and fixture syntax checks passed.
- The inert fixture exited `0` with `V44_PURE_FIXTURES_PASS` and zero listing,
  thrown-value, and output getter calls.
- The one-shot flag is set before predecessor validation and dynamic import.
- The executable retains one import, one `openTabs`, one rank-zero cached-ID
  `claimTab`, one account-home navigation, one token-page navigation, one fixed
  non-secret filter fill, and read-only token-page semantic checks.
- Create is counted but never clicked. No Copy, Paste, clipboard, credential,
  cookie/storage, provider mutation, retry, fallback, reconnect, new/close-tab,
  or manual-integration action is present.
- Success retains only the V44 continuation tab and required state flags.
  Ordinary, documentation-output, and final-output failures clear both phase
  bindings, broad runtime/controller aliases, evidence, and raw-error holders.
- Hostile thrown values are rethrown by identity only on terminal-output paths;
  they are not inspected, logged, serialized, or retained.

## Finding

### V44-001 — IMPORTANT — Required fixture byte/hash tuple is absent from the fixture terminal

The brief says the fixture **must** print directly computed byte/hash tuples for
the executable, fixture, and brief. The committed fixture reads only the brief
and executable. Its final object reports only `briefBytes`, `briefSha256`,
`executableBytes`, and `executableSha256`; there is no fixture path/read, no
direct fixture hash calculation, and no `fixtureBytes` or `fixtureSha256` field.
The observed passing terminal confirms the omission.

This breaks the immutable candidate-package and later non-self-referential
classification contract. A classifier could repeat the separately supplied
fixture digest, but it cannot cite the fixture's promised direct terminal proof.
The discrepancy is especially material for a one-shot gate because package-byte
identity must be settled before any live action.

Required correction:

1. Read the fixture's own committed file bytes in the inert fixture and compute
   its length and SHA-256 directly.
2. Add `fixtureBytes` and `fixtureSha256` to the terminal object and assert their
   expected values without weakening the existing checks.
3. Update the brief's exact fixture tuple and terminal contract if the correction
   changes fixture bytes, then commit a new immutable candidate and obtain a new
   independent review. Do not amend, reinterpret, or consume this failed V44
   package.

## Severity counts

| Severity | Count |
| --- | ---: |
| Critical | 0 |
| HIGH | 0 |
| IMPORTANT | 1 |
| Minor | 0 |

## Authorization statement

`authorizes_live_execution=false`

This FAIL review authorizes no V44 classification, live browser send, provider
action, secret operation, authority-gate consumption, retry, fallback, or
confirmation consumption. A corrected immutable replacement requires a fresh
independent review and all later classification, tuple, action-time pin,
no-residue, and external-confirmation boundaries.
