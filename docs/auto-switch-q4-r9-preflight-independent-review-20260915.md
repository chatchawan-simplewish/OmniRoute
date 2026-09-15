# Q4 R9 descriptor preflight independent review

Verdict: **BLOCK — DO NOT AUTHORIZE THE PREFLIGHT**

Reviewed commit: `24b8b065c05261c024ec383b6927d1c6918282f0`

Scope was limited to root `AGENTS.md`, the current R9 v2 contract/source and source-review classification, and exactly the eight files added by the reviewed commit. No live resource was contacted, no SSH command was run, and no consuming or rendering mode was executed.

## Exact additive package

| File | SHA-256 |
| --- | --- |
| `docs/auto-switch-q4-r9-preflight-contract-20260915.md` | `1cad8456ca809124f4542b5320e03787fba335396db27e5a24cf8196ebf0986b` |
| `scripts/auto-switch-q4-r9-collector-template-20260915.py` | `16b36c7e94d2ed9c70bbc80cde08ea277e4942c1454baafed2465b1f4416ebfe` |
| `scripts/auto-switch-q4-r9-command-template-20260915.json` | `11e1b0c50b222bcdd99b0545aff3ea315b614b9419ae7e1c2fa09f3b03e93a93` |
| `scripts/auto-switch-q4-r9-preflight-20260915-test.py` | `f09e4904c6f59e4b10a0b18528e192a0e91fd772de50612c2fc363009ffa4da6` |
| `scripts/auto-switch-q4-r9-preflight-20260915.py` | `7e3e96e0e4179b2ef41dbab37a906ae088a24739bd419714dac0328d2525f917` |
| `scripts/auto-switch-q4-r9-preflight-bootstrap-20260915.py` | `02713bc45a3fd636530de715f580478ee57220a0b4a6aff144daa629dc12fa7a` |
| `scripts/auto-switch-q4-r9-request-template-20260915.json` | `7827305e1efedd20893712e7545f7ab4f787d4df63aa3f5cc9cece4f8df3d133` |
| `scripts/auto-switch-q4-r9-runtime-template-20260915.py` | `0b84615a63ea78ba48957b7e4133e2f42312bed142c98ae711ac04e10e4dcf36` |

## Current R9 v2 framework baseline

The current classification in `docs/auto-switch-q4-r9-20260915-independent-rereview-4.md` is source PASS only, explicitly not execution authority. Its four recorded hashes still match the current committed bytes:

| File | SHA-256 |
| --- | --- |
| `docs/auto-switch-q4-r9-20260915-contract.md` | `7afad77dae2a21330f0f8d59afd587e8d110b8ad2716b6e77215a4585b57dc33` |
| `scripts/auto-switch-q4-r9-20260915.py` | `71c7226818bf4b52b5b7ce4611fceb8b371bf2b6b41f958a2d3df3929ecf793c` |
| `scripts/auto-switch-q4-r9-20260915-helper.py` | `0395ce2c3f3a6b7ad1287facb3c4fded4ff52ec131d3c758bf32ee0fadf4a020` |
| `scripts/auto-switch-q4-r9-20260915-test.py` | `7cd2c059c8c076f4332a0d48114bad647f3d6125695fb20c9b782784a019450c` |

The renderer produces the exact R9 v2 action, runtime, credential, source-manifest, and operation-hash shapes required by the launcher/helper. That schema compatibility does not close the execution-proof defects below.

## Blocking findings

1. **The approved host-key bytes are not the bytes SSH is guaranteed to use.** `review_payload()` and `validate_approval()` hash the current `known_hosts` pathname, but `ssh_command()` later gives that mutable pathname to a separate `ssh.exe` process. No retained descriptor, lock, opened-object identity, or post-use equality check bridges those operations. A replacement after approval validation but before SSH opens the file can change the accepted host key while the approval still passes. This contradicts the contract's strict pinned-`known_hosts` boundary and prevents authorization of the one contact (`preflight` lines 108-114 and 121-147).

2. **The later-action evidence does not prove the pinned candidate endpoint or connection.** The runtime verifies a Docker container ID/name/image, while the collector independently contacts the caller-supplied private IPv4; neither program derives or compares that endpoint with the inspected container's network identity. The collector also never sends `X-OmniRoute-Connection` and never observes a selected-connection identifier. It copies `candidate_id` and `connection_id` from the approved action into evidence. Therefore another private OmniRoute endpoint, or another LM Studio connection serving the same model, can satisfy the HTTP/model/provider checks while evidence claims the pinned candidate and connection. This fails the R9 contract's candidate/connection binding (`runtime template` lines 30-38 and 56-70; `collector template` lines 53-83).

3. **A contacted or uncertain preflight is reported on stdout as `NOT_EXECUTED`.** `run_preflight()` correctly reserves the receipt first and leaves canonical local `UNKNOWN` on any timeout, overflow, nonzero status, malformed response, or write-path exception. However the top-level catch emits `status=NOT_EXECUTED` for every exception, including after SSH was launched or the remote observation may have completed. That conflicting classification can invite a forbidden retry and violates the contract's transport-uncertainty semantics (`preflight` lines 232-258 and 334-339).

## Preserved properties

- The local receipt is opened with `O_EXCL` before the single transport call. An existing receipt prevents another call; the source contains no retry or fallback.
- The fixed SSH command uses one connection attempt, batch mode, an absolute identity path, strict host-key checking, a fixed host/user, and a fixed `sudo -n /usr/bin/python3 -I` read-only bootstrap. Finding 1 prevents the stronger exact-host-key claim.
- The retained bootstrap is supplied once after approval validation and is not reopened by `run_preflight()`. The remote shim executes those retained bytes from stdin.
- The POSIX bootstrap opens the fixed root-owned parent and basename credential with `O_DIRECTORY`/`O_NOFOLLOW`, uses `fstat`, emits descriptor metadata only, and checks both distinct R9 leaves absent without creating or changing a remote object.
- No credential content or credential hash is read, emitted, logged, or placed in argv/environment by the preflight. Receipt and rendered action contain descriptor metadata only.
- The consuming R9 helper independently reopens the approved parent/credential objects, compares exact descriptor identity, and refuses existing state or terminal leaves before its exclusive UNKNOWN/SPENT reservation. Historic R8 is not referenced or reopened.

## Checks and disposition

- Confirmed the reviewed commit is HEAD on `codex/omniroute-q4-r9-20260915`, the worktree was clean before this review artifact, and the commit added exactly the eight hashed files above.
- Performed direct static review of all eight committed files and the current R9 v2 contract, launcher, helper, test classification, and byte hashes.
- Focused test not run: its single test covers the synthetic happy path, retained-bootstrap no-reopen, local receipt exclusivity, rendering, schema compatibility, and secret-hash rejection, but it does not exercise or resolve any blocking finding above.
- Do not issue a preflight approval, make the SSH contact, render an action from this package, or relax the current source-only execution block. Replace the package, add one focused regression check for each repaired boundary, and obtain a fresh independent Sol High review.
