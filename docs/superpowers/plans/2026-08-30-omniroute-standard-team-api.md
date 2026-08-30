# OmniRoute Standard Team API Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish `https://ai.mysw.me/v1` as a standard OpenAI-compatible, individually keyed team entry point while keeping VM1205 administration and paid providers private.

**Architecture:** A remotely managed Cloudflare Tunnel joins the existing `omniroute-internal` Docker network and targets a dedicated Caddy container. Caddy exposes exactly three method/path pairs and forwards them to the existing OmniRoute container; OmniRoute authenticates separate team keys and restricts them to named local/free connections.

**Tech Stack:** Cloudflare Tunnel, `cloudflare/cloudflared:2026.8.2` resolved to an immutable runtime digest, `caddy@sha256:5f5c8640aae01df9654968d946d8f1a56c497f1dd5c5cda4cf95ab7c14d58648`, Docker, PowerShell 7, OmniRoute API Manager.

## Global Constraints

- This plan does not authorize live Cloudflare, VM1205, API-key, firewall, rate-limit, or endpoint changes.
- Public base URL is exactly `https://ai.mysw.me/v1`.
- Public methods are exactly `GET /v1/models`, `POST /v1/chat/completions`, and `POST /v1/responses`.
- Every other public method/path returns proxy `404` without reaching OmniRoute.
- Use one independently revocable OmniRoute key per teammate or harness; never share the Hermes Agent key.
- Team keys allow only the named VM1201 Q6, Bell-PC Q4, and OpenRouter Free connections.
- Team keys must not include paid subscription, paid OpenRouter, `manage`, provider-quota-bypass, or chaos scopes.
- Maximum public request body is exactly 8 MiB (`max_size 8MiB`).
- Never print, log, commit, or place credentials in command arguments. Prompt and response bodies are not retained as evidence.
- No router port-forward, VM1205 host-published proxy port, OmniRoute restart, Bell proxy change, or local-model change.
- Preserve the paused Task 3 worktree changes and use exact-path staging only.
- A failed gate leaves the public hostname disabled or removed.

---

## File Structure

No OmniRoute application code changes are required.

- Create: `C:\ChatGPT Projects\SW-Selfhosted-Network\artifacts\omniroute-live-integration\team-api-proxy.Caddyfile` — exact public method/path allowlist and upstream proxy.
- Create: `C:\ChatGPT Projects\SW-Selfhosted-Network\artifacts\omniroute-live-integration\verify-team-api.ps1` — static, unauthenticated, authenticated, and SSE verification without secret output.
- Create during execution: `C:\ChatGPT Projects\SW-Selfhosted-Network\artifacts\omniroute-live-integration\evidence\team-api-verification.json` — status-only acceptance evidence.
- Create on VM1205: `/opt/omniroute-team-api/Caddyfile` — root-owned deployed copy.
- Create on VM1205: `/opt/omniroute-team-api/cloudflared-token` — root-owned mode `600`; never copy it into evidence.

### Task 1: Build and validate the offline proxy contract

**Files:**
- Create: `C:\ChatGPT Projects\SW-Selfhosted-Network\artifacts\omniroute-live-integration\team-api-proxy.Caddyfile`
- Create: `C:\ChatGPT Projects\SW-Selfhosted-Network\artifacts\omniroute-live-integration\verify-team-api.ps1`

**Interfaces:**
- Consumes: approved design commit `6877ac4161af46a03517453c8a33da55c87ecfd6`.
- Produces: a Caddy configuration listening on internal port `20130` and a verifier whose live inputs are `-BaseUrl`, `-Model`, and environment variable `OMNIROUTE_TEAM_API_KEY`.

- [ ] **Step 1: Write the static verifier before the Caddyfile**

Create `verify-team-api.ps1` with this complete content:

```powershell
[CmdletBinding()]
param(
    [switch]$StaticOnly,
    [string]$BaseUrl = "",
    [string]$Model = ""
)

$ErrorActionPreference = "Stop"
$caddyPath = Join-Path $PSScriptRoot "team-api-proxy.Caddyfile"

function Assert-True([bool]$Condition, [string]$Message) {
    if (-not $Condition) { throw $Message }
}

function Get-Status([string]$Method, [string]$Uri, [hashtable]$Headers = @{}, [string]$Body = "") {
    try {
        $params = @{ Method = $Method; Uri = $Uri; Headers = $Headers; SkipHttpErrorCheck = $true }
        if ($Body) { $params.ContentType = "application/json"; $params.Body = $Body }
        return [int](Invoke-WebRequest @params).StatusCode
    } catch {
        if ($_.Exception.Response.StatusCode) { return [int]$_.Exception.Response.StatusCode }
        throw
    }
}

Assert-True (Test-Path -LiteralPath $caddyPath) "Caddyfile missing"
$caddy = Get-Content -Raw -LiteralPath $caddyPath
foreach ($required in @(
    "method GET", "path /v1/models", "method POST",
    "path /v1/chat/completions", "path /v1/responses",
    "max_size 8MiB", "respond 404", "omniroute:20128"
)) {
    Assert-True ($caddy.Contains($required)) "Caddyfile missing: $required"
}
Assert-True (-not $caddy.Contains("log {")) "Caddy access logging must remain disabled"
if ($StaticOnly) { Write-Output "STATIC_PROXY_CONTRACT=PASS"; exit 0 }

Assert-True $BaseUrl "BaseUrl is required for live checks"
$BaseUrl = $BaseUrl.TrimEnd("/")
$unauth = Get-Status GET "$BaseUrl/models"
Assert-True ($unauth -eq 401) "Unauthenticated models expected 401, got $unauth"
foreach ($path in @("/", "/dashboard", "/api/settings")) {
    $status = Get-Status GET ($BaseUrl.Substring(0, $BaseUrl.Length - 3) + $path)
    Assert-True ($status -eq 404) "Denied path $path expected 404, got $status"
}
$wrongMethod = Get-Status POST "$BaseUrl/models" @{} "{}"
Assert-True ($wrongMethod -eq 404) "POST /v1/models expected 404, got $wrongMethod"

$key = [Environment]::GetEnvironmentVariable("OMNIROUTE_TEAM_API_KEY")
Assert-True (-not [string]::IsNullOrWhiteSpace($key)) "OMNIROUTE_TEAM_API_KEY is required"
Assert-True $Model "Model is required for authenticated checks"
$headers = @{ Authorization = "Bearer $key" }
$modelsStatus = Get-Status GET "$BaseUrl/models" $headers
Assert-True ($modelsStatus -eq 200) "Authenticated models expected 200, got $modelsStatus"

$body = @{ model = $Model; messages = @(@{ role = "user"; content = "Reply exactly TEAM_API_OK" }); max_tokens = 16; stream = $false } | ConvertTo-Json -Depth 6 -Compress
$response = Invoke-RestMethod -Method Post -Uri "$BaseUrl/chat/completions" -Headers $headers -ContentType "application/json" -Body $body
$answer = [string]$response.choices[0].message.content
Assert-True ($answer.Trim() -eq "TEAM_API_OK") "Unexpected bounded response"

$client = [System.Net.Http.HttpClient]::new()
$request = [System.Net.Http.HttpRequestMessage]::new([System.Net.Http.HttpMethod]::Post, "$BaseUrl/chat/completions")
$request.Headers.Authorization = [System.Net.Http.Headers.AuthenticationHeaderValue]::new("Bearer", $key)
$streamBody = @{ model = $Model; messages = @(@{ role = "user"; content = "Reply exactly STREAM_OK" }); max_tokens = 16; stream = $true } | ConvertTo-Json -Depth 6 -Compress
$request.Content = [System.Net.Http.StringContent]::new($streamBody, [Text.Encoding]::UTF8, "application/json")
$watch = [Diagnostics.Stopwatch]::StartNew()
$streamResponse = $client.SendAsync($request, [System.Net.Http.HttpCompletionOption]::ResponseHeadersRead).GetAwaiter().GetResult()
Assert-True ($streamResponse.IsSuccessStatusCode) "Streaming request failed"
$reader = [IO.StreamReader]::new($streamResponse.Content.ReadAsStream())
$sawData = $false
$sawDone = $false
while (-not $reader.EndOfStream -and $watch.Elapsed.TotalSeconds -lt 180) {
    $line = $reader.ReadLine()
    if ($line.StartsWith("data:")) { $sawData = $true }
    if ($line -eq "data: [DONE]") { $sawDone = $true; break }
}
$reader.Dispose(); $request.Dispose(); $client.Dispose()
Assert-True $sawData "No SSE data event received"
Assert-True $sawDone "No SSE completion marker received"
Write-Output "LIVE_TEAM_API=PASS"
```

- [ ] **Step 2: Run the verifier and confirm the intended RED result**

Run in PowerShell 7:

```powershell
& "C:\ChatGPT Projects\SW-Selfhosted-Network\artifacts\omniroute-live-integration\verify-team-api.ps1" -StaticOnly
```

Expected: FAIL with `Caddyfile missing`.

- [ ] **Step 3: Write the minimal Caddy configuration**

Create `team-api-proxy.Caddyfile`:

```caddyfile
{
    admin off
    auto_https off
}

:20130 {
    route {
        @models {
            method GET
            path /v1/models
        }
        @chat {
            method POST
            path /v1/chat/completions
        }
        @responses {
            method POST
            path /v1/responses
        }

        request_body @chat {
            max_size 8MiB
        }
        request_body @responses {
            max_size 8MiB
        }

        handle @models {
            reverse_proxy http://omniroute:20128 {
                flush_interval -1
                header_up -Cookie
                header_up -CF-Access-Client-Id
                header_up -CF-Access-Client-Secret
            }
        }
        handle @chat {
            reverse_proxy http://omniroute:20128 {
                flush_interval -1
                header_up -Cookie
                header_up -CF-Access-Client-Id
                header_up -CF-Access-Client-Secret
            }
        }
        handle @responses {
            reverse_proxy http://omniroute:20128 {
                flush_interval -1
                header_up -Cookie
                header_up -CF-Access-Client-Id
                header_up -CF-Access-Client-Secret
            }
        }
        handle {
            respond 404
        }
    }
}
```

- [ ] **Step 4: Run static and Caddy syntax checks**

```powershell
& "C:\ChatGPT Projects\SW-Selfhosted-Network\artifacts\omniroute-live-integration\verify-team-api.ps1" -StaticOnly
docker run --rm --mount "type=bind,src=C:\ChatGPT Projects\SW-Selfhosted-Network\artifacts\omniroute-live-integration\team-api-proxy.Caddyfile,dst=/etc/caddy/Caddyfile,readonly" caddy@sha256:5f5c8640aae01df9654968d946d8f1a56c497f1dd5c5cda4cf95ab7c14d58648 caddy validate --config /etc/caddy/Caddyfile
```

Expected: `STATIC_PROXY_CONTRACT=PASS` and `Valid configuration`.

- [ ] **Step 5: Commit only the two offline artifacts in the coordinator repository**

```powershell
git -C "C:\ChatGPT Projects\SW-Selfhosted-Network" add -- "artifacts/omniroute-live-integration/team-api-proxy.Caddyfile" "artifacts/omniroute-live-integration/verify-team-api.ps1"
git -C "C:\ChatGPT Projects\SW-Selfhosted-Network" diff --cached --check
git -C "C:\ChatGPT Projects\SW-Selfhosted-Network" -c user.name="Codex" -c user.email="codex@openai.com" commit -m "ops: add OmniRoute team API proxy contract" -- "artifacts/omniroute-live-integration/team-api-proxy.Caddyfile" "artifacts/omniroute-live-integration/verify-team-api.ps1"
```

Expected: exactly those two paths in the commit.

### Task 2: Deploy and prove the private VM1205 proxy

**Files:**
- Consume: `artifacts/omniroute-live-integration/team-api-proxy.Caddyfile`
- Create on VM1205: `/opt/omniroute-team-api/Caddyfile`

**Interfaces:**
- Consumes: Docker network `omniroute-internal` and upstream `omniroute:20128`.
- Produces: internal-only `http://team-api-proxy:20130`; no host-published port.

- [ ] **Step 1: Obtain the separate live-implementation authority gate**

The approval must explicitly name: VM1205 directory/config creation, the new Caddy container, the Cloudflare Tunnel token and container, the `ai.mysw.me` hostname, the bounded rate rule, a rollout API key, and bounded verification. Stop without this approval.

- [ ] **Step 2: Revalidate the non-destructive baseline**

```powershell
ssh.exe -i "C:\Users\chatc\.ssh\codex-prox01-vms-ed25519" -o BatchMode=yes belladmin@192.168.1.68 "sudo docker inspect -f '{{.Name}}={{.State.Status}}' omniroute bell-cloudflare-proxy; sudo docker network inspect omniroute-internal --format '{{len .Containers}}'; sudo ss -lnt"
```

Expected: both existing containers running, network member count `2`, and no host listener for `20130`.

- [ ] **Step 3: Transfer and validate the root-owned configuration**

Use SSH stdin so no secret or configuration is placed in a command argument:

```powershell
Get-Content -Raw "C:\ChatGPT Projects\SW-Selfhosted-Network\artifacts\omniroute-live-integration\team-api-proxy.Caddyfile" | ssh.exe -i "C:\Users\chatc\.ssh\codex-prox01-vms-ed25519" belladmin@192.168.1.68 "sudo install -d -m 700 -o root -g root /opt/omniroute-team-api; sudo install -m 644 -o root -g root /dev/stdin /opt/omniroute-team-api/Caddyfile"
ssh.exe -i "C:\Users\chatc\.ssh\codex-prox01-vms-ed25519" belladmin@192.168.1.68 "sudo docker run --rm --network omniroute-internal --mount type=bind,src=/opt/omniroute-team-api/Caddyfile,dst=/etc/caddy/Caddyfile,readonly caddy@sha256:5f5c8640aae01df9654968d946d8f1a56c497f1dd5c5cda4cf95ab7c14d58648 caddy validate --config /etc/caddy/Caddyfile"
```

Expected: mode `700` directory, root-owned configuration, and valid Caddy syntax.

- [ ] **Step 4: Start the hardened proxy without publishing a host port**

```powershell
ssh.exe -i "C:\Users\chatc\.ssh\codex-prox01-vms-ed25519" belladmin@192.168.1.68 "sudo docker run -d --name team-api-proxy --restart unless-stopped --network omniroute-internal --read-only --cap-drop ALL --cap-add NET_BIND_SERVICE --security-opt no-new-privileges:true --memory 128m --cpus 0.5 --tmpfs /data:rw,noexec,nosuid,size=16m --tmpfs /config:rw,noexec,nosuid,size=16m --mount type=bind,src=/opt/omniroute-team-api/Caddyfile,dst=/etc/caddy/Caddyfile,readonly caddy@sha256:5f5c8640aae01df9654968d946d8f1a56c497f1dd5c5cda4cf95ab7c14d58648 caddy run --config /etc/caddy/Caddyfile"
```

Expected: `team-api-proxy` running with an empty `HostConfig.PortBindings` object.

- [ ] **Step 5: Prove the internal allowlist before any public hostname exists**

From the `omniroute` container, request only status codes from `team-api-proxy`:

```powershell
ssh.exe -i "C:\Users\chatc\.ssh\codex-prox01-vms-ed25519" belladmin@192.168.1.68 "sudo docker exec omniroute node -e \"for (const [m,p] of [['GET','/v1/models'],['GET','/dashboard'],['POST','/v1/models']]) fetch('http://team-api-proxy:20130'+p,{method:m}).then(r=>console.log(m,p,r.status))\""
```

Expected: `GET /v1/models 401`, `GET /dashboard 404`, and `POST /v1/models 404`.

### Task 3: Create the bounded Cloudflare edge and Tunnel

**Files:**
- Create on VM1205: `/opt/omniroute-team-api/cloudflared-token`
- Create evidence: status-only tunnel name, connector ID, image digest, and hostname; no token.

**Interfaces:**
- Consumes: `http://team-api-proxy:20130` on `omniroute-internal`.
- Produces: `https://ai.mysw.me` routed only through Cloudflare Tunnel.

- [ ] **Step 1: Check for overlapping Access applications and rate-rule scope**

In Cloudflare, verify no Access application or wildcard covers `ai.mysw.me`. Check the zone plan before creating a rate rule:

- Pro or higher: match `http.host eq "ai.mysw.me" and starts_with(http.request.uri.path, "/v1/")`.
- Free: Host matching is unavailable. Proceed with path-only `starts_with(http.request.uri.path, "/v1/")` only after proving no other hostname in the zone uses `/v1/`; otherwise stop and request a separate proxy-rate-limit design.

Use IP as the counting characteristic, `20` requests per `10` seconds, Block for `10` seconds. Create this rule before the public hostname.

- [ ] **Step 2: Create a remotely managed Tunnel and public hostname**

Create Tunnel `vm1205-omniroute-team-api`. Set its public hostname to `ai.mysw.me` and service to `http://team-api-proxy:20130`. Do not create an Access application for this hostname.

- [ ] **Step 3: Resolve and record the immutable cloudflared image digest**

```powershell
$cloudflaredImage = (ssh.exe -i "C:\Users\chatc\.ssh\codex-prox01-vms-ed25519" belladmin@192.168.1.68 "sudo docker pull cloudflare/cloudflared:2026.8.2 >/dev/null; sudo docker image inspect cloudflare/cloudflared:2026.8.2 --format '{{index .RepoDigests 0}}'").Trim()
if ($cloudflaredImage -notmatch '^cloudflare/cloudflared@sha256:[0-9a-f]{64}$') { throw "Unexpected cloudflared digest" }
$env:CLOUDFLARED_IMAGE_REF = $cloudflaredImage
```

Expected: an official `cloudflare/cloudflared@sha256:...` digest. Use that exact digest in every subsequent container command; do not run the mutable tag.

- [ ] **Step 4: Transfer the Tunnel token without displaying it**

Place the token in local process environment `CLOUDFLARED_TUNNEL_TOKEN`, then run this as one PowerShell block. Never echo the variable:

```powershell
if ([string]::IsNullOrWhiteSpace($env:CLOUDFLARED_TUNNEL_TOKEN)) { throw "Tunnel token missing" }
$env:CLOUDFLARED_TUNNEL_TOKEN | ssh.exe -i "C:\Users\chatc\.ssh\codex-prox01-vms-ed25519" belladmin@192.168.1.68 "sudo install -m 600 -o root -g root /dev/stdin /opt/omniroute-team-api/cloudflared-token"
Remove-Item Env:CLOUDFLARED_TUNNEL_TOKEN
```

Expected: remote mode `600`, owner `root:root`; no token in terminal output or shell history.

- [ ] **Step 5: Start cloudflared with the token file**

Use the immutable reference captured in Step 3:

```powershell
$cloudflaredImage = $env:CLOUDFLARED_IMAGE_REF
if ($cloudflaredImage -notmatch '^cloudflare/cloudflared@sha256:[0-9a-f]{64}$') { throw "cloudflared image reference missing" }
ssh.exe -i "C:\Users\chatc\.ssh\codex-prox01-vms-ed25519" belladmin@192.168.1.68 "sudo docker run -d --name omniroute-team-tunnel --restart unless-stopped --network omniroute-internal --read-only --cap-drop ALL --security-opt no-new-privileges:true --memory 128m --cpus 0.5 --mount type=bind,src=/opt/omniroute-team-api/cloudflared-token,dst=/run/secrets/tunnel-token,readonly $cloudflaredImage tunnel --no-autoupdate run --token-file /run/secrets/tunnel-token"
Remove-Item Env:CLOUDFLARED_IMAGE_REF
```

Expected: connector Healthy in Cloudflare and no host-published port.

- [ ] **Step 6: Verify the public deny-first surface before creating a key**

```powershell
& "C:\ChatGPT Projects\SW-Selfhosted-Network\artifacts\omniroute-live-integration\verify-team-api.ps1" -BaseUrl "https://ai.mysw.me/v1"
```

Expected: the script reaches the intentional `OMNIROUTE_TEAM_API_KEY is required` stop only after unauthenticated `401` and denied-path `404` checks pass.

### Task 4: Create and verify a restricted rollout key

**Files:**
- Update live OmniRoute API Manager only.
- Write status-only evidence to `artifacts/omniroute-live-integration/evidence/team-api-verification.json`.

**Interfaces:**
- Consumes: public endpoint and named connections `VM1201 Qwen3.8-27B Q6`, `Bell-PC Qwen3.8-27B Q4`, and `OpenRouter Free`.
- Produces: temporary key `team-rollout-test`, later revoked; permanent keys are created individually only for named team members or harnesses.

- [ ] **Step 1: Create the temporary key in the LAN dashboard**

First confirm all three named connections exist and are healthy; stop if any is missing rather than substituting a paid connection.

Configure exactly:

- Name: `team-rollout-test`.
- Manage, provider-quota bypass, and chaos access: disabled.
- No-log: enabled.
- Allowed connections: only `VM1201 Qwen3.8-27B Q6`, `Bell-PC Qwen3.8-27B Q4`, and `OpenRouter Free`.
- Allowed endpoints: only `/api/v1/models`, `/api/v1/chat/completions`, and `/api/v1/responses`.
- Custom key rate: `20` requests per `10` seconds.
- Paid connections and paid quota pools: not selected.

Copy the key once into local process environment `OMNIROUTE_TEAM_API_KEY`; do not display or save it.

- [ ] **Step 2: Run the two bounded acceptance requests**

Use the already confirmed Bell model ID:

```powershell
& "C:\ChatGPT Projects\SW-Selfhosted-Network\artifacts\omniroute-live-integration\verify-team-api.ps1" -BaseUrl "https://ai.mysw.me/v1" -Model "lmstudio/qwen3.8-27b-unsloth-ud-q4ks"
```

Expected: `LIVE_TEAM_API=PASS`; exactly one non-streaming and one streaming bounded request.

- [ ] **Step 3: Prove routing and logging boundaries**

In OmniRoute request metadata, verify both requests identify `team-rollout-test`, selected the Bell-PC LM Studio connection, recorded queue wait, attempts, fallback result, status, latency, and token metadata, and did not select any paid connection. Inspect only field names and metadata; do not open prompt or response bodies.

- [ ] **Step 4: Revoke the rollout key and prove immediate denial**

Delete `team-rollout-test`, retain its value only long enough for one final status check, then clear it:

```powershell
$headers = @{ Authorization = "Bearer $env:OMNIROUTE_TEAM_API_KEY" }
$status = try { [int](Invoke-WebRequest -Uri "https://ai.mysw.me/v1/models" -Headers $headers -SkipHttpErrorCheck).StatusCode } catch { [int]$_.Exception.Response.StatusCode }
if ($status -ne 401) { throw "Revoked key expected 401, got $status" }
Remove-Item Env:OMNIROUTE_TEAM_API_KEY
"REVOKED_KEY=PASS"
```

Expected: `REVOKED_KEY=PASS` and no reusable rollout credential remains.

### Task 5: Regression audit, evidence, and handoff

**Files:**
- Create: `C:\ChatGPT Projects\SW-Selfhosted-Network\artifacts\omniroute-live-integration\evidence\team-api-verification.json`

**Interfaces:**
- Consumes: results from Tasks 1-4.
- Produces: final PASS/FAIL evidence and exact rollback commands.

- [ ] **Step 1: Recheck internal services without inference**

Verify LAN dashboard HTTP `200`, `omniroute` running, `bell-cloudflare-proxy` running, `team-api-proxy` running, `omniroute-team-tunnel` running, Bell-PC `connected`, and Bell model `1/1 active`.

- [ ] **Step 2: Prove the origin is not publicly bound**

```powershell
ssh.exe -i "C:\Users\chatc\.ssh\codex-prox01-vms-ed25519" belladmin@192.168.1.68 "sudo docker inspect -f '{{.Name}} PORTS={{json .HostConfig.PortBindings}} READONLY={{.HostConfig.ReadonlyRootfs}}' team-api-proxy omniroute-team-tunnel; sudo ss -lnt"
```

Expected: no proxy/tunnel host port binding and no new public listener.

- [ ] **Step 3: Write redacted evidence**

Write JSON containing timestamps, commit hashes, public status codes, container image digests, hardening flags, Cloudflare connector health, key revocation result, queue wait, attempts, fallback result, selected provider name, and regression outcomes. Exclude prompts, responses, request/response bodies, API keys, Tunnel tokens, provider keys, Authorization headers, and Cloudflare account identifiers.

- [ ] **Step 4: Run the final Sol High security/completion review**

The reviewer checks the direct-byte Caddyfile, verifier, evidence JSON, live container inspection, Cloudflare hostname/rate rule, route allowlist, key restrictions, revocation proof, and regression results. Any HIGH concern or failed gate means FAIL and triggers rollback.

- [ ] **Step 5: Keep rollback copy-paste ready**

If any gate fails, first disable/remove the `ai.mysw.me` public hostname and revoke team keys in Cloudflare/OmniRoute, then run:

```powershell
ssh.exe -i "C:\Users\chatc\.ssh\codex-prox01-vms-ed25519" belladmin@192.168.1.68 "sudo docker stop omniroute-team-tunnel team-api-proxy; sudo docker rm omniroute-team-tunnel team-api-proxy"
```

Do not remove `/opt/omniroute-team-api` until evidence review confirms no credential is needed for incident analysis. Bell-PC proxy and OmniRoute remain untouched.

- [ ] **Step 6: Commit only redacted coordinator artifacts**

```powershell
git -C "C:\ChatGPT Projects\SW-Selfhosted-Network" add -- "artifacts/omniroute-live-integration/evidence/team-api-verification.json"
git -C "C:\ChatGPT Projects\SW-Selfhosted-Network" diff --cached --check
git -C "C:\ChatGPT Projects\SW-Selfhosted-Network" -c user.name="Codex" -c user.email="codex@openai.com" commit -m "evidence: verify OmniRoute team API exposure" -- "artifacts/omniroute-live-integration/evidence/team-api-verification.json"
```

Expected: only the redacted evidence path committed.
