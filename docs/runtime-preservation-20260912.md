# Current runtime preservation prerequisites

Source port baseline `820ead300f0c03e17a87fbaa7e22e81d72faeeeb` contains the accepted MCP audit fix but does not by itself reconstruct current live r3.

Before candidate build, reconcile the Gemini custom source range `5458026c2..f5dd779088d2129a53dedea0fa75ba788316a0c0` in `.worktrees/gemini-model-source`: commits `94a363eb6`, `0b7ad106c`, `f5dd77908`. Ten files, 186 insertions and 9 deletions: model-menu parsing/hydration, requested-mode selection, model discovery route and focused Gemini tests. Port only still-missing behavior; preserve later baseline improvements. Do not delete the hidden Flash-Lite row or alter signed-in account credentials.

Current image also contains the isolated Playwright runtime layout from `.worktrees/web-provider-repair/scripts/web-provider-repair/Dockerfile`: Playwright 1.62.1, matching nested playwright-core, Chromium installation and node-owned browser cache. The current base's dependency layout must be inspected before deciding whether this older repair remains necessary; do not blindly downgrade new dependencies. Candidate must prove a network-isolated browser launch plus the existing native SQLite/audit check.

The live r3 base and data volume remain untouched. A full rebuilt candidate must retain these source/runtime behaviors and pass scoped review. A compiled byte overlay is not assumed safe for the multi-file routing controller; build from reconciled source instead.

This is a preservation checklist, not build/deployment execution authority. Runtime-port worker remains the sole source writer until it returns its commit; the coordinator does not edit that worktree concurrently.

# Image acceptance note

The current candidate Dockerfile already supplies a `runner-web` stage, copies the full builder Playwright package (including its nested matching core), installs Chromium and hands browser-cache ownership to `node`. Prefer that existing stage over adding another browser installer. Later isolated image acceptance must verify resolved package versions and a network-disabled headless launch as the runtime user. Merely inspecting the lockfile or Dockerfile is not a passing browser smoke.
