# Task 2 secure-console launch-scope incident

Status: **FAIL / NOT PROVEN — one-shot live gate spent**

## Authority and pins

- Fixed live brief commit: `7af3ab75ec87d81d75811ff8f2e9b4fa9d0c3e3b`.
- Independent PASS review commit: `ce47c2eacb5a5cbf055c3fc814137e46c1855e40`.
- Retained-Chrome recovery classification commit: `788d38a5db1fd598631fee4f8db764d3719f9186`.
- Owner script pin: `22118` bytes, SHA-256
  `347FCD60A41DF780CE4A94E4FC14C87E5059112068C689EF73636ABC5B0F0B6C`.
- R5 script pin: `10890` bytes, SHA-256
  `DB75253CD851075C1D612A54EC4B02C8016C034C8BC192A3DB9D02DB9890AD41`.

No secret, credential value, Cloudflare account/zone/rule/token identifier,
container identifier, or unrelated resource name is recorded here.

## Proven execution

All credential-free action-time checks passed before the live action:

- source index `0`, preserved dirty baseline `12`, source HEAD
  `788d38a5db1fd598631fee4f8db764d3719f9186`;
- evidence worktree clean at
  `80adaa7d5d63d1d2c7bfa63b236c6bee93b3b1d8`;
- both Windows clipboard-policy values remained exact DWORD `0`;
- one credential-free clipboard clear/read completed `1/1`, with empty `TRUE`;
- existing VM services were running, target proxy/Tunnel absent, network member
  count `2`, listener `20130` absent, and retained Caddy hash exact;
- authenticated Cloudflare showed the fixed token row absent, one unrelated
  rate-limit rule, and zero target rate-rule, DNS, Tunnel/connector, and Access
  application matches;
- authenticated OmniRoute exact-name search showed zero `team-rollout-test`
  matches.

The exact credential-free proxy wrapper was extracted at `8380` bytes with
SHA-256 `A7C7F04705344160030C3BF1CA383179616507555F56D2288E3BFD9B46FEF2AC`,
executed once, and returned exact terminal `PROXY_START_AND_PROOF=PASS`. The
reviewed 19-label proof therefore passed once.

The exact preparation block was extracted at `3983` bytes with SHA-256
`784E91D71AB0B07A65C6FDA429CC4A86C3E6107C76E258BC608F75DA893C1D4A`
and executed once. It returned
`EXACT_OWNER_AND_R5_SCRIPTS_PREPARED=PASS`.

## Failure

The coordinator invoked the extracted preparation block with PowerShell child
scope operator `&`. The block-created path variables therefore did not persist
in the retained parent PowerShell session.

The exact launch fence was then extracted at `655` bytes with SHA-256
`995185FA04790564F4CDCA967E87CAB82EB97731D8458EF85CEF942D4606A293` and
invoked once. `Start-Process` rejected the null
`-RedirectStandardOutput` argument before starting a process. Exact observed
error class: parameter validation; exact condition: redirected-output path null
or empty.

This was a coordinator scope error, not an owner-script, R5, Cloudflare, VM, or
credential failure. Nevertheless the one-shot gate is spent. No retry,
fallback, or continuation occurred.

## Negative proof and cleanup

- Owner processes started: `0`.
- Masked prompts/submissions: `0/0`.
- Cloudflare token rows created/deleted: `0/0`.
- Native secret Copy/Paste: `0/0`.
- Agent/browser clipboard secret reads/writes: `0/0`.
- R5 children/POST/DELETE: `0/0/0`.
- Token verification and Zone lookup: `0/0`.
- Cloudflare form/resource mutation: `0`.
- Routing, DNS, Tunnel, Access, OmniRoute key, and model-request mutation: `0`.

Bounded credential-free cleanup then:

1. revalidated the exact new private proxy's fixed image, running state, empty
   host port bindings, network member count `3`, and absent listener `20130`;
2. removed only `team-api-proxy` once and proved it absent, network members `2`,
   and listener `20130` absent — terminal `EXACT_PROXY_CLEANUP=PASS`;
3. found exactly one direct child temp directory containing only the two exact
   hash-pinned scripts and no safe log, removed those two files and the now-empty
   directory — terminal `EXACT_CREDENTIAL_FREE_TEMP_CLEANUP=PASS`.

No credential existed, so no credential incident or revocation obligation was
created.

## Disposition

The live gate at commits `7af3ab75e` / `ce47c2eac` is spent and cannot be
retried. Future execution requires a new independently reviewed one-shot
replacement contract. The replacement must preserve every original security,
scope, no-retry, confirmation, revocation, and cleanup boundary while correcting
only retained-parent PowerShell scoping.
