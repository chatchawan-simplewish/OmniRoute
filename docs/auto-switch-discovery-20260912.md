# Fresh read-only discovery contract

Owner: task `01a09361-8143-73d3-adb7-15043355276b`, source branch `codex/omniroute-auto-switch-20260912`.
Status: PREPARED; independent Sol High review required before execution.

## Target and exclusion

VM1205 at `192.168.1.68`, recorded moved to prox-04. Use the existing `belladmin` SSH identity `C:/Users/chatc/.ssh/codex-prox01-vms-ed25519`, BatchMode, IdentitiesOnly, StrictHostKeyChecking=yes and bounded ConnectTimeout. Do not add/change known_hosts. A known-host mismatch stops this discovery.

Current app task inventory shows all other named OmniRoute tasks notLoaded. The current task claims only this new read-only VM1205 metadata-discovery lane; it does not transfer or mutate any old rollout worktree, credential lane, client, VM1201 or Bell-PC workload. Before any future mutation a fresh live-resource ownership transfer/exclusion must be established. No previous D/B/V gate or launcher is used.

## Permitted operation

Run `scripts/auto-switch-discovery-20260912.py` on the VM through `sudo -n python3 -`, supplied on stdin. It selects exactly one running container publishing port 20128, reads Docker metadata in memory, selects the exact /app/data named volume and opens storage.sqlite using SQLite URI mode=ro and query_only=ON. Output contains only container/image/volume/network identifiers, health, environment-presence booleans, routing table names and API-key count. No API-key row values or metadata are selected. All command stderr and arbitrary exception text remain suppressed. No inference, provider calls, environment values, logs, settings values, DB writes, service restart, credential changes, or client changes.

This step determines the running container and metadata, not host migration acceptance or inference-key validity. No mutation or inference may follow solely from a successful discovery. A subsequent reviewed scope must pin host identity, deployed source markers and runtime bindings before activation.

## Fail-closed boundary and rollback

Stop on SSH mismatch, unavailable sudo, zero/multiple matching containers, missing/ambiguous volume or DB, timeout, schema errors or unexpected output. There is no state mutation to roll back. This is a new read-only diagnostic, not a consuming one-shot gate. Further reads may be separately reviewed if new scope is needed; never invoke an old gate as fallback.

## Evidence

Sanitized stdout and exit status are retained in this task's tool record and summarized in `docs/auto-switch-20260912-plan.md`. Review covers exact script bytes and this contract. No secret values enter the review or evidence.

## Exact invocation

PowerShell in the source worktree, one block (review records script and contract SHA-256 before execution):

```powershell
Get-Content -Raw -LiteralPath 'scripts/auto-switch-discovery-20260912.py' | & 'C:\WINDOWS\System32\OpenSSH\ssh.exe' -F none -T -i 'C:\Users\chatc\.ssh\codex-prox01-vms-ed25519' -o IdentitiesOnly=yes -o BatchMode=yes -o StrictHostKeyChecking=yes -o UserKnownHostsFile=C:/Users/chatc/.ssh/known_hosts -o GlobalKnownHostsFile=none -o HostKeyAlias=192.168.1.68 -o ConnectTimeout=10 -o ConnectionAttempts=1 -o ServerAliveInterval=10 -o ServerAliveCountMax=2 belladmin@192.168.1.68 'sudo -n python3 -'
```

The SSH executable resolves to the exact Windows OpenSSH path above; identity and known_hosts presence were verified. A failure does not authorize changing any trust record. Script-level subprocess timeouts are 20 seconds. Prior code review P1 for key-row output is fixed by emitting only key count. The offline self-check asserts credential fixture exclusion and rejects multiple target containers.
