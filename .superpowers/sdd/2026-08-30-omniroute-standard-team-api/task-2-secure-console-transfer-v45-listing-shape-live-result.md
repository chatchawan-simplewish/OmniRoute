# OmniRoute V45 listing-shape live result

## Reviewed package and action-time state

- Candidate commit: `9d6f95763`
- Sol High PASS review commit: `268ca707ec1b5d29ef71ad59f7ef822cd67341ef`
- Non-self-referential classification commit: `4a813c5b616b329c8fc53d23e057a2510d1111e3`
- Executable bytes: `21169`
- Executable SHA-256: `D4469DA4ECA7BF2667894A7780C6F022D02827548BE873B716EA2D778B0AE81F`
- The fresh-realm direct binding audit passed for all 80 prohibited/predeclared names.
- The user supplied the exact fresh-session Chrome profile/window/tab confirmation immediately before execution.

## One-shot result

V45 was consumed exactly once and returned
`EXACT_V45_FIXED_LISTING_SHAPE_DIAGNOSTIC_CAPTURED`.

- Import, setup, Chrome connection, full documentation validation/write, session naming, and `openTabs()` each completed exactly once.
- `offeredCount` was exactly `1`.
- `Array.isArray(offered)` was `true`.
- `Object.getPrototypeOf(offered) === Array.prototype` was `false`.
- Every remaining checked array property passed: no symbols; safe bounded data `length`; exact own-name count; expected names only; and complete enumerable data index descriptors.
- Every record check passed: plain record; no symbols; allowed keys with `id`; complete enumerable data descriptors; safe IDs; safe or absent URLs; optional values string or undefined; and all values V37-safe.
- Claim, navigation, URL, snapshot, and provider writes remained exactly zero.
- The fixed terminal output completed with `errorClass: NONE`.

## Root cause

V44's listing validation rejected the sole offered tab only because it required
the array object's prototype to equal the current REPL realm's
`Array.prototype`. The browser runtime returned a genuine cross-realm array:
`Array.isArray` and every bounded structural/content check passed, while the
realm-local prototype identity check did not.

This is sufficient evidence for the narrow replacement: accept a genuine
cross-realm array without weakening any length, descriptor, key, value, ID,
URL, page-signature, completeness, no-residue, secret, confirmation, or cleanup
constraint.

## Security and provider boundary

- V45 was diagnostic-only and could not claim a tab, navigate, read page content, fill, click, create a token, copy a secret, or change Cloudflare.
- No provider-persistent change occurred.
- No secret value was read, printed, logged, or committed.
- Terminal cleanup proved V45 consumed, setup/agent/Chrome/tab bindings null, eligibility false, and state `V45_DIAGNOSTIC_CAPTURED_INELIGIBLE`.
- The CUA realm was reset immediately after that cleanup proof.
- V45 is permanently spent and must never be retried, continued, or reinterpreted.

## Replacement boundary

V46 must change only the incompatible realm-local array-prototype equality
requirement. It must retain `Array.isArray` plus every passed structural and
content invariant and all V44 semantic page-signature, completeness,
no-residue, no-retry, secret, confirmation, and cleanup constraints. V46 may
not be executed until an independent Sol High PASS review, a
non-self-referential classification, and a post-commit coordinator tuple are
complete.
