# Live gateway topology refresh — 20260913 042546 Asia/Bangkok

Read-only SSH checks on VM1205 (`192.168.1.68`) used the frozen strict-host-key helper SHA256 `7776a680ade8940ece3a47dc5feb154e0ef27209a07897674d309ea6f7822279`. Both commands exited 0. Only selected Docker metadata and Caddy upstream dials were emitted; no environment values, configuration bodies, credentials, requests to providers, or mutations occurred.

## Current pins

- Container `omniroute`: `7b20ca195e3c9e875d0a1ce98832ca469c2a114886335b8466b1467b3ed139bc`; running, healthy, user `node`.
- Image: `sha256:60ab56311d1c9873416dc53683148d314465370312547b8ce87c442ce084c6a5`.
- Sole mount: writable volume `omniroute-data-mcp-audit-20260910-r3` at `/app/data`.
- Published listener: container `20128/tcp` to host `0.0.0.0:20128`.
- Restart policy: `unless-stopped`, MaximumRetryCount 0.
- `bridge`: network `c9c8417dcac64d172174f60caa53c0dccd8474937ffa739e0ed41ae4fd107a73`, IP `172.17.0.2`, no explicit aliases.
- `omniroute-internal`: network `baf515e5b9c139e2233df62323a46b50ddc97b99f4c3d427b3ae9b460df9de1c`, IP `172.18.0.4`, no explicit aliases.
- Running `team-api-proxy`: `b979b42dc79015ed70139a7494e2d0b0f47e783752801a2633e6043d967e1203`. Read-only `caddy adapt --config /etc/caddy/Caddyfile` exposes exactly one upstream dial: `omniroute:20128`.

## Implication for final rollout

A replacement with only the same host port does not prove public API continuity: the team proxy consumes the old Docker name. The final reviewed transaction must explicitly bind that DNS identity to the replacement and prove it through the existing proxy, while preserving an exact rollback to the old container. Do not assume stopping the old container removes its DNS identity, assign a competing alias, or mutate the proxy configuration without a reviewed plan.

The minimum candidate design is an exact network-attachment transfer: after stopping the old container at the exclusive snapshot boundary, detach its `omniroute-internal` endpoint, attach the replacement with alias `omniroute`, and verify the proxy resolves/routes to the replacement. Rollback stops and detaches the replacement before reattaching the old container with its recorded network/IP and restarting it. This is an unexecuted design requiring independent review and a focused isolated Docker DNS/rollback rehearsal; no network attachment is changed by this evidence collection. Preserve the old image, volume, container name and proxy bytes.

Q4 remains separately unavailable at its Cloudflare Tunnel. Local BELL-PC2 has no detected cloudflared service/process, and the `BELL-PC` DNS lookup produced no A record. This does not prove Bell-PC is offline or authorize a guessed remote target.

## Public transport compatibility follow-up

The historical team API plan names `https://ai.mysw.me/v1`. A fresh read-only adaptation of the same pinned running team proxy returned exactly these path/method matchers: `GET /v1/models`, `POST /v1/chat/completions`, and `POST /v1/responses`. No `/v1/agent-routes/events` matcher is present. No public HTTP or provider request was made in this follow-up.

Do not bind the durable-ACK client to this public endpoint merely because TLS was documented: the existing allowlist does not establish ACK transport. It would require a separately reviewed narrow proxy-route addition and end-to-end proof. The agreed LAN HTTP endpoint remains unchanged; the VM105 owner is assessing the existing SSH path for its isolated transport. This finding does not authorize either proxy changes or new TLS infrastructure.
