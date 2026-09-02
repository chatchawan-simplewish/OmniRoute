# OmniRoute V32 observed-zone route API-signature live incident

Date: 2026-09-02 (Asia/Bangkok)

## Terminal classification

V32 was consumed exactly once and returned `PRECONDITION_FAIL`. The reviewed
flow opened one exact tab, loaded the account home, privately captured and
validated the unique same-account `mysw.me` zone href, navigated directly to
that exact observed href, completed the bounded zone wait, and validated the
settled Cloudflare zone-route URL. The first post-navigation page-signature
evaluation then rejected with sanitized error class `Error` before returning
any snapshot.

The exact created tab closed `1/1`; cleanup is `EXACT_TAB_CLOSED`, residue
converged, and no exact handle was retained. State is
`V32_DIAGNOSTIC_FAILED_CLEAN` and `secureConsoleZoneV32Consumed` is true. V32
is permanently spent. It must never be retried, continued, reinterpreted, or
used as authority for provider mutation.

## Pinned execution identity

- Corrected V32 brief: `a55dd20a0b92e26f38b5af0baadfe6864812fd7f`;
  `21625` bytes; SHA-256
  `60BA0BC5A3A2F65F90CBECDEDD320810F7998AE7D20F8E5C4EAC6BA4474FBEEF`;
  blob `3c281118274fc45dbaa5da429a0eae1a6430554f`.
- Executable: `18215` normalized LF bytes; SHA-256
  `8DFA8749AD040359239805E0F6D02E9DFC70BEE792FB2FBAB3A94B7EA204F870`.
- Independent Sol High PASS review:
  `942b27d28e3a6a1b2da9cdb71e83b2470092cfdc`.
- Non-self-referential classification:
  `3a3712ba4b19e4742e5399da4232ab1655978327`.
- Action-time coordinator tuple: chain/exclusions/records `119/121/10661`;
  projection SHA-256
  `C4C85893769D133224AC7404B628C8B0D4B0EBBFF471620B158E652E152B4EBD`;
  empty index; exact 12-path dirty product baseline.
- Reviewed runtime hashes, clean evidence worktree at
  `80adaa7d5d63d1d2c7bfa63b236c6bee93b3b1d8`, zero temporary/process
  residue, VM1205 safe checkpoint, and absent public DNS all revalidated.
- Persistent controller `secureConsoleChromeV5` was present; V31 predecessor
  state was exactly consumed/clean/no-retained-handle; every V32 declaration
  was absent before execution.

One local orchestration prestart stopped on unavailable `TextEncoder` before
the reviewed executable was sent to Node. It did not consume V32 or touch the
browser. The replacement .NET UTF-8/SHA-256 preflight passed immediately
before the sole consuming call.

## Fixed pre-navigation evidence

- Declaration shape, exact V31 predecessor, controller ownership, created
  handle, tab shape, account-home URL, and pre-snapshot validation: all true.
- Exact Cloudflare host and account-home path: true/true.
- Exact same-account zone-href count: `1`; all-anchor count: `112`; busy count:
  `0`.
- The sole observed href was privately parsed and validated for HTTPS, exact
  Cloudflare host, empty port and credentials, bounded/control-free text, and
  exact `/<account>/mysw.me` pathname. No raw href or account identifier was
  emitted or retained in this artifact.

## Fixed navigation and failure evidence

- New tab, home navigation, home wait, home URL read, and pre-snapshot:
  `1/1` each.
- Zone navigation, zone wait, and settled URL read: `1/1` each.
- Observed-zone URL validation and settled-zone URL validation: true/true.
- Post-snapshot evaluation: `1/0`; validation false; completeness false;
  snapshot null; sanitized error class `Error`.
- Close: `1/1`; terminal write attempted `1`; cleanup
  `EXACT_TAB_CLOSED`; residue converged true; retained exact handle false.

## Successor boundary

V32 proves that direct navigation to the unique observed same-account zone
href completes and settles on the expected Cloudflare zone-route prefix. It
does not prove any API-token, profile, or manage-account signature because the
post-navigation evaluator returned no data. No Create, native Copy, masked
Paste, token creation, provider configuration, or other provider-persistent
action occurred.

Any successor must be a new one-shot contract with new declarations and an
independent Sol High PASS review. It may use the proven private observed-href
navigation pattern, but it must isolate the post-navigation evaluation failure
with fixed, sanitized, completeness-checked output; preserve exact cleanup,
no-residue, no-secret, and no-retry semantics; and remain diagnostic-only.
The mandatory final Create/native Copy/native masked Paste confirmation and
the later separate exact-row deletion confirmation remain untouched.
