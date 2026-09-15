# Q4 R9 descriptor preflight independent rereview

Verdict: **BLOCK — DO NOT AUTHORIZE THE PREFLIGHT**

Fix commit reviewed: `cebda6c1f6a9827043a2b4516d721b9e6d56cb0b`

Prior BLOCK review: `c5ffc920a2e98ff481c3d86c85d1c0d2f717353b`

Scope was limited to the exact six-file fix diff and all eight current additive package files. Current OmniRoute source was read only to verify the request/log identifier contract. No live resource was contacted and no SSH, rendering, or consuming mode was executed.

## Current additive package

| File | SHA-256 |
| --- | --- |
| `docs/auto-switch-q4-r9-preflight-contract-20260915.md` | `b3b22069db48b094040d2280bb2f24cf285e9c3ad1bd62b263bae2bd3adc6601` |
| `scripts/auto-switch-q4-r9-collector-template-20260915.py` | `a9618a5520216aea3ab686ead7607aacd6ccedb9bf5c21dbd0605a94179190af` |
| `scripts/auto-switch-q4-r9-command-template-20260915.json` | `be89ae6ec7711169f683ee95f5d1dfe25f1f96e180ba572986d13fe605dcf10b` |
| `scripts/auto-switch-q4-r9-preflight-20260915-test.py` | `33cfe57f9f4942c743b4e7b72a5fd030163e142ba035ccd542156e64fbffca0d` |
| `scripts/auto-switch-q4-r9-preflight-20260915.py` | `3720fd8ca44c2f4309c0b0bb036310838c25426def71ed909ab59ced07cffd07` |
| `scripts/auto-switch-q4-r9-preflight-bootstrap-20260915.py` | `02713bc45a3fd636530de715f580478ee57220a0b4a6aff144daa629dc12fa7a` |
| `scripts/auto-switch-q4-r9-request-template-20260915.json` | `7827305e1efedd20893712e7545f7ab4f787d4df63aa3f5cc9cece4f8df3d133` |
| `scripts/auto-switch-q4-r9-runtime-template-20260915.py` | `bea23833c5732d716e5807b590a948a285381b6fc22e771aace473da02be102d` |

## Blocking finding

1. **The collector queries `call_logs` with an identifier that OmniRoute does not persist as `call_logs.id`.** The collector takes response header `x-omniroute-request-id` as `observed_log_id` and queries `call_logs WHERE id=?` (`collector` lines 45-59 and 94-101). Current non-streaming OmniRoute builds that response header from independently generated `skillRequestId` (`open-sse/handlers/chatCore.ts` lines 860 and 4587-4595), while attempt logging persists `call_logs.id=pendingRequestId` (`open-sse/handlers/chatCore.ts` lines 778-785 and `open-sse/handlers/chatCore/attemptLogging.ts` lines 234-242). Those identifiers are not the same contract. The synthetic test inserts a row whose ID is manually made equal to the response header and therefore cannot detect the production mismatch (`preflight test` lines 123-135). A real successful generation cannot establish the selected connection through this query and would leave the consuming gate UNKNOWN/SPENT after contact. Use a request-carried identifier that OmniRoute actually persists, or bind the observed connection through a directly returned server field/header, then test that exact production identifier flow.

## Prior finding closure

1. **Retained `known_hosts`: CLOSED.** Approval validation retains the reviewed bytes. `retained_known_hosts()` writes them to a fresh temporary leaf, opens a Windows handle with read sharing only, verifies the held bytes, keeps the handle open while SSH uses that exact path, rechecks descriptor/path identity and bytes after return, and treats replacement, mutation, or cleanup failure as uncertainty (`preflight` lines 112-118, 125-153, and 238-315). The focused Windows test proved `os.replace` is denied while the transport callback runs and that the temporary leaf is removed afterward.

2. **Candidate endpoint observation: SOURCE CLOSED, runtime-platform proof still deferred.** The runtime now reads the endpoint IPv4 from the exact candidate inspect object on pinned network name `omniroute-internal`, requires it to equal the reviewed endpoint, and repeats that comparison through start/health/stop inspection (`runtime` lines 32-56 and 59-89). The current test covers matching and mismatching synthetic inspect values. Stopped-container address retention and the complete start/stop sequence remain for the mandatory later root-POSIX/Docker exact-action test; they are not proved by this Windows unit check.

3. **Transport uncertainty classification: CLOSED.** Receipt creation remains exclusive and precedes preparation/contact. `PREFLIGHT_SPENT` is set immediately after reservation, the receipt retains canonical local `UNKNOWN` on every exception, and the top-level failure envelope reports `UNKNOWN` with `preflight_spent=true` whenever reservation occurred or the fixed receipt exists. `NOT_EXECUTED` is limited to the no-receipt/no-contact boundary (`preflight` lines 295-335 and 389-416).

## Preserved properties and compatibility

- The preflight remains one-contact, read-only, POSIX descriptor metadata only, with no retry/fallback and no remote mutation or leaf reservation.
- No credential content or credential hash is read, emitted, logged, or placed in argv/environment. Descriptor identity, size, mode, owner, and mtime remain the only credential evidence.
- Retained bootstrap bytes are not reopened by `run_preflight`; absent R9 leaves are directly observed and are independently revalidated by the consuming helper before its exclusive UNKNOWN/SPENT reservation.
- The renderer still produces canonical action/runtime/credential/source-manifest shapes and exact operation hashes accepted by the current R9 v2 launcher/helper. Historic R8 remains untouched.

## Checks and disposition

- Inspected the exact `c5ffc920..cebda6c1` diff, all eight current additive files, and the current OmniRoute response-header/call-log persistence source.
- Ran `python -B scripts/auto-switch-q4-r9-preflight-20260915-test.py -v` offline: one test passed. It validates the host-key lock, UNKNOWN receipt/envelope, synthetic endpoint comparison, synthetic SQLite selection, rendering, and R9 v2 schema compatibility; it does not cover the production identifier mismatch above.
- Do not issue a preflight approval, make the SSH contact, or render an action. Replace the request/log correlation, add one focused production-contract regression check, and obtain another fresh independent rereview.
