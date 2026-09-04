# OmniRoute V59 replacement secure-console token contract

## Purpose

Create one replacement Cloudflare user token only when the current direct
console state proves this exact contract is safe to consume. V57 is spent and
V58 was read-only readiness evidence; neither is reusable.

## Fixed scope

- Account: `digital@simplewish.me`.
- Zone: exactly `mysw.me`.
- Token name: exactly `OmniRoute secure console R5 20260901`.
- Permissions: exactly `Zone WAF: Edit` and `Zone: Read`.
- Excluded: every account permission, DNS, Tunnel, token management, other
  zone, additional permission, rule mutation, VM/process action, and secret
  inspection or persistence.

## One-shot sequence

1. Revalidate the sole source worktree, expected product dirty baseline, exact
   Chrome profile, one claimed Cloudflare tab, signed-in account, API Tokens
   URL, and no conflicting token-object owner.
2. Read the token table and prove the matching-row count for the fixed V59 name
   is zero. Any other result is `FAIL_STOP_NO_RETRY`.
3. Prepare the form with only the fixed name, zone, and two permissions. Stop
   before `Create Token`.
4. Immediately before final Create, refresh the table and form state. The
   matching-row count must remain zero and every fixed field must still match.
5. Before confirmation or Create, prove the retained credential-owner PID and
   its exact `OWNER_READY=PASS` and `SECRET_PROMPT_READY=PASS` markers. Any
   absence, stale state, or mismatch prevents token creation.
6. Obtain the mandatory action-time user confirmation for the complete Create,
   Copy, and Paste sequence, then perform exactly one Create action. The user
   alone performs one native Copy and one masked Paste into only that visible
   retained credential-owner prompt. The agent never reads, types, serializes,
   captures, logs, or commits the token value.
7. If any action is failed, interrupted, ambiguous, malformed, or uncertain,
   mark the gate spent and stop. There is no retry, fallback, second token,
   scope expansion, provider mutation, or secret transfer.

## Post-create boundary

Only the separately reviewed
`task-2-secure-console-transfer-scope-replacement-brief.md` may govern
post-create routing, deployment, verification, evidence, and cleanup; V59
grants none of those actions by itself. Exact-row revocation is a separate
destructive action and requires a new, explicit action-time confirmation naming
this V59 token row.
