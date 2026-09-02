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

V45 confirms that the returned value is a genuine cross-realm array:
`Array.isArray` passed while realm-local prototype identity differed. That
difference is non-causal because V44 deliberately used `Array.isArray` and did
not require realm-local array-prototype identity.

V45 rules out every other structural and value rejection in V44 except V44's
requirement that the optional `url` property be present and Cloudflare-qualified.
The fresh `cua.getState()` independently proved that the sole offered tab was
the selected Cloudflare API Tokens tab, while the browser API contract declares
`url?: string`. Therefore the narrow evidenced incompatibility is V44 treating
an API-optional listing URL as mandatory. No broader listing relaxation is
supported.

## Security and provider boundary

- V45 was diagnostic-only and could not claim a tab, navigate, read page content, fill, click, create a token, copy a secret, or change Cloudflare.
- No provider-persistent change occurred.
- No secret value was read, printed, logged, or committed.
- Terminal cleanup proved V45 consumed, setup/agent/Chrome/tab bindings null, eligibility false, and state `V45_DIAGNOSTIC_CAPTURED_INELIGIBLE`.
- The CUA realm was reset immediately after that cleanup proof.
- V45 is permanently spent and must never be retried, continued, or reinterpreted.

## Replacement boundary

V46 must change only the incompatible requirement that each candidate listing
record contain `url`. If `url` is present it must remain V37-safe and exactly
Cloudflare-qualified; if absent, the sole/rank-zero/user-confirmed selection
must be verified after claim by the unchanged Cloudflare navigation and page
signatures. V46 must retain `Array.isArray`, every passed structural/content
invariant, and all V44 semantic page-signature, completeness, no-residue,
no-retry, secret, confirmation, and cleanup constraints. V46 may not be
executed until an independent Sol High PASS review, a
non-self-referential classification, and a post-commit coordinator tuple are
complete.
