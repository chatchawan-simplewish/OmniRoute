# Candidate image build path

Read-only strict-known-host SSH discovery on 2026-09-12 confirmed builder `belladmin@192.168.1.147`, hostname `prox01-codex`, Docker server 29.1.3, 123.8 GiB free `/var/tmp` disk and 14.9 GiB available memory. Default Docker Buildx is unavailable. Local Windows has no Docker executable.

Prior successful B1 evidence used a private SHA-named directory under `/var/tmp/omniroute-routing-build`, an explicitly pinned retained Buildx plugin and the Docker default builder. Those scripts and gates remain historical and must not be rerun. A new build must use a fresh private directory, final reviewed source/archive pins, the candidate's existing `runner-web` target, and an independently reviewed launcher. No service restart, volume attachment, provider network call or live image replacement is part of building the candidate.

Acceptance must include full matching Playwright package resolution and a network-disabled Chromium launch as the runtime user. Do not claim that source tests or a successful image build establish provider generation or client readiness.
