# OmniRoute Standard Team API Design

**Status:** Approved design; live implementation is not yet authorized
**Date:** 2026-08-30
**Public base URL:** `https://ai.mysw.me/v1`

## Goal

Let approved team AI harnesses use OmniRoute through the standard OpenAI
`base_url` plus bearer `api_key` interface. Keep OmniRoute administration,
provider credentials, paid routes, and the VM1205 origin off the public
Internet.

## Non-goals

- Do not expose the OmniRoute dashboard or administrative APIs.
- Do not require Cloudflare Access headers or a device client.
- Do not share the existing Hermes Agent key.
- Do not enable team use of paid subscriptions or paid OpenRouter routes
  without separate owner authorization.
- Do not change the Bell-PC Cloudflare proxy or VM1201 local-model service.

## Architecture

```text
Team harness
  |  HTTPS + Authorization: Bearer <individual OmniRoute key>
  v
Cloudflare: ai.mysw.me
  |  Tunnel; coarse WAF/rate-limit protection
  v
VM1205 team API proxy
  |  exact method/path allowlist; no public host port
  v
OmniRoute:20128
  |  key authentication and approved route policy
  v
local/free providers only
```

Cloudflare Tunnel publishes the hostname without making VM1205's origin port
publicly routable. Because generic OpenAI clients already use `Authorization`
for the OmniRoute bearer key, this hostname deliberately does not require a
Cloudflare Access service token.

References:

- https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/
- https://developers.cloudflare.com/waf/rate-limiting-rules/

## Public API contract

The public proxy permits only these method/path pairs:

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/v1/models` | OpenAI-compatible model discovery |
| `POST` | `/v1/chat/completions` | Hermes and OpenAI-compatible chat clients |
| `POST` | `/v1/responses` | Responses-compatible agent clients |

All other paths and methods return a proxy-generated `404` without reaching
OmniRoute. This includes `/`, `/dashboard`, `/api/*`, provider-specific routes,
key-management routes, documentation, health pages, WebSocket routes, and
unversioned aliases.

The proxy forwards the caller's `Authorization`, `Content-Type`, `Accept`, and
streaming response headers unchanged. It does not log or copy bearer values.
Browser CORS is not enabled initially; server-side harnesses do not require it.

## Authentication and authorization

- Create one named OmniRoute API key per teammate or harness.
- Never distribute the Hermes Agent key or a provider credential.
- Keys are inference-only and independently revocable.
- Initial team routing is limited to approved local and free providers.
- Paid subscription and paid OpenRouter routes remain owner-only until a
  separate quota and spending policy is approved.
- A missing, invalid, or revoked key must return `401` from OmniRoute.

## Abuse and resource controls

- Cloudflare applies a coarse source-IP request-rate rule to this hostname.
  Its purpose is abuse containment, not local-slot scheduling.
- The proxy accepts at most 8 MiB per request, enough for the approved large
  text contexts while bounding accidental uploads.
- OmniRoute remains responsible for queueing, provider health, retries, and
  routing decisions.
- Rate limits must not buffer or truncate SSE responses.

No fixed production rate is chosen in this design. The implementation begins
with a bounded test rule, observes legitimate harness traffic, and requires a
separate owner decision before enforcing a permanent threshold.

## Logging

Retain metadata needed to investigate queueing and routing:

- timestamp and request ID;
- named API-key identity, never the bearer value;
- requested model or route alias;
- queue wait, selected provider, attempts, and fallback result;
- status, latency, and token counts when available.

Never log API keys, Cloudflare credentials, provider credentials, prompts,
responses, tool payloads, or authorization headers. Cloudflare and proxy access
logs must follow the same rule.

## Failure handling

- Cloudflare or tunnel failure returns an external gateway error; it must not
  reveal an alternate origin address.
- Invalid authentication stops at OmniRoute with `401`; it does not retry a
  provider.
- Rejected paths stop at the public proxy and never reach OmniRoute.
- Exhausted local/free capacity follows the separately approved OmniRoute
  routing policy; team keys do not gain paid access as an emergency fallback.
- The internal dashboard and Bell-PC proxy remain available even if the team
  hostname is disabled.

## Verification gate

Live implementation is accepted only when all checks pass:

1. The VM1205 OmniRoute port is not opened on the router or public interface.
2. External `GET /v1/models` without a key returns `401`.
3. A dedicated test key lists models successfully.
4. One bounded non-streaming request returns the expected sentinel response.
5. One bounded SSE request streams events to completion without buffering.
6. `/`, `/dashboard`, `/api/*`, and a wrong method return proxy `404` responses.
7. Revoking the test key makes its next request return `401`.
8. Request evidence shows no paid provider was selected.
9. Logs contain the required metadata and no prohibited content.
10. LAN dashboard access, Hermes access, and Bell-PC `1/1 active` status still
    pass after the change.

Any failed check leaves team access disabled. No partial public exposure is an
acceptable result.

## Rollback

1. Disable or remove the `ai.mysw.me` Tunnel public hostname.
2. Revoke every team API key created for the rollout.
3. Stop and remove only the stateless team API proxy.
4. Confirm the public hostname no longer reaches VM1205.
5. Reconfirm internal OmniRoute, Hermes, and Bell-PC operation.

Rollback does not modify OmniRoute data, provider credentials, the existing
Bell-PC proxy, or local model services.

## Authority boundary

This document authorizes design and planning only. Live Cloudflare DNS/Tunnel,
VM1205 proxy, API-key, firewall, rate-limit, and endpoint changes require a
separate explicit implementation authorization.
