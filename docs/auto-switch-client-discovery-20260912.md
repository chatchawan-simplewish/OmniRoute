# Read-only client readiness discovery

Owner: current task `01a09361-8143-73d3-adb7-15043355276b`; no prior client/gate ownership transfer is assumed. This new read-only lane does not stop, start, configure or call inference on either client. Historical targets are discovery candidates only, confirmed by strict existing SSH trust. Unknown/offline/drift stops later activation and is not repaired by this contract.

Script `scripts/auto-switch-client-discovery-20260912.py` emits only fixed role, numeric UID, known repository existence, validated 40-hex Git HEAD, tracked-clean boolean, and allowlisted service-state strings. It never reads configuration, credentials, process command lines, logs, state databases or untracked filenames. Both Git commands use `--no-optional-locks`, preventing optional index refresh writes. Git status is captured in memory and converted to a boolean. No imports from client code, installation, writes or provider calls.

Exact PowerShell invocations from this coordinator worktree, after independent Sol High script/contract hash verification:

```powershell
Get-Content -Raw -LiteralPath 'scripts/auto-switch-client-discovery-20260912.py' | & 'C:\WINDOWS\System32\OpenSSH\ssh.exe' -F none -T -i 'C:\Users\chatc\.ssh\codex-prox01-vms-ed25519' -o IdentitiesOnly=yes -o BatchMode=yes -o StrictHostKeyChecking=yes -o UserKnownHostsFile=C:/Users/chatc/.ssh/known_hosts -o GlobalKnownHostsFile=none -o HostKeyAlias=192.168.1.141 -o ConnectTimeout=10 -o ConnectionAttempts=1 -o ServerAliveInterval=10 -o ServerAliveCountMax=2 hermes@192.168.1.141 'python3 - hermes'
Get-Content -Raw -LiteralPath 'scripts/auto-switch-client-discovery-20260912.py' | & 'C:\WINDOWS\System32\OpenSSH\ssh.exe' -F none -T -i 'C:\Users\chatc\.ssh\codex-prox01-vms-ed25519' -o IdentitiesOnly=yes -o BatchMode=yes -o StrictHostKeyChecking=yes -o UserKnownHostsFile=C:/Users/chatc/.ssh/known_hosts -o GlobalKnownHostsFile=none -o HostKeyAlias=192.168.1.139 -o ConnectTimeout=10 -o ConnectionAttempts=1 -o ServerAliveInterval=10 -o ServerAliveCountMax=2 dsh@192.168.1.139 'python3 - deepseek'
```

No known-host modification, user fallback, sudo, proxy, agent forwarding or alternative target. Per-child timeout 10 seconds. Failed SSH or missing repository/service yields NOT PROVEN and no mutation. Each target can be read independently; no rollback is necessary because the script is read-only. Evidence: sanitized stdout/exit codes in task tool record and result summary in the plan.
