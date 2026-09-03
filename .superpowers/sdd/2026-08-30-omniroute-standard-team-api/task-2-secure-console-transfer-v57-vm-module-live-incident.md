# OmniRoute V57 VM-module live incident

## Outcome

- Timestamp: `20260903 212333` Asia/Bangkok.
- Result: `V57_TOKEN_PAGE_SEMANTIC_READINESS_FAILED_STOP`.
- V57 was consumed exactly once and is permanently spent.
- No API token was created, no secret was exposed or transmitted, and no provider configuration changed.

## Preconditions

- Same-realm VM capability: `V57_VM_CAPABILITY_PASS` for `createContext`, `SourceTextModule`, and `SyntheticModule`.
- Direct fresh-realm audit: `V57_DIRECT_AUDIT_PASS`; 140 predecessor bindings absent and `secureConsoleV57Module` absent.
- Loader bytes: `2553`; SHA-256 `23477C4DC06262AD25CE28D270B767A804DF55A7598D379EB74A560F55AC06D7`.
- Executable bytes: `27336`; SHA-256 `48DD581AE424042D42002AA8D32D017B7156A65CEE729A983BFB878200051A38`.
- Browser profile: `Codex-Chrome-Bell-PC2`; exact user tab was Cloudflare `https://dash.cloudflare.com/profile/api-tokens`.

## Failure and cleanup

- Cross-realm account-home reacquisition passed and claimed exactly one eligible Cloudflare tab.
- Token-page navigation and both readiness waits passed.
- The first locator read was attempted but did not fulfill; no filter fill, create-control read, token-row read, or token creation action occurred.
- Returned cleanup evidence reported `failureCleanupComplete: true`, `bindingNull: true`, `predecessorBindingNull: true`, and predecessor state `V57Attachment_DOWNSTREAM_FAILURE_DETACHED`.
- The exported state-only observation confirmed the V57 tab binding was null, eligibility false, state `V57_TOKEN_PAGE_SEMANTIC_READINESS_FAILED`, and V57 consumed true. The observation's predicate was incorrectly stricter: it expected three downstream-consumption flags to be true even though the failure occurred before those operations. The observed false flags are consistent with the returned counters and no downstream operation.
- The CUA realm was reset after that single observation. V57 will not be retried or reused.

## Follow-up diagnosis

- A fresh read-only AX snapshot showed the token page fully loaded with one enabled `#user-api-tokens-search` text input, one token table, one `Create Token` button, and existing rows.
- A direct-realm locator read of the same input succeeded and returned an empty enabled text input.
- The safe replacement should use short direct CUA/AX or direct-realm Playwright reads instead of another disk-loaded VM candidate for routine page inspection. Token creation remains a separate action-time-confirmed gate.
