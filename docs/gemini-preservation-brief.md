# Task 2: Preserve deployed Gemini behavior in the routing candidate

Exclusive writer remains the original runtime implementer in `.worktrees/omniroute-auto-switch-runtime-20260912`. Start only after coordinator dispatch. Do not edit any other worktree; other agents are active. No live service, database, provider, credential, SSH or browser changes.

Port still-missing Gemini behavior from `.worktrees/gemini-model-source`, exact custom range `5458026c2..f5dd779088d2129a53dedea0fa75ba788316a0c0`, commits `94a363eb6`, `0b7ad106c`, `f5dd77908`. Source baseline `820ead300` lacks all these custom production changes. Preserve current baseline improvements and the completed routing port; do not replace newer files wholesale.

Required behavior:

- Enabled `data-mode-id` menu items only; strict unique label parsing including Flash-Lite.
- Three-second account-menu hydration discovery.
- Exact requested-mode selection and selected-state verification; terminal model error produces existing sanitized 400 handling.
- Provider model discovery uses account-menu results, filters stale imported rows, and fails with sanitized 502.
- Registry uses 3.1 Pro, 3.6 Flash, 3.6 Thinking; dynamic discovery may import enabled Flash-Lite. No live row deletion or account rotation.

The source delta has ten files and focused Gemini tests. Reuse/port those focused tests, establish failing coverage before the fix, run only affected tests and scoped lint. Do not run a broad suite/build in this task. Current lockfile already pins Playwright1.62.1 with matching nested core1.62.1: do not add dependencies, repin or downgrade it. Chromium installation and isolated launch belong to later image acceptance.

Write `docs/auto-switch-gemini-preservation-report-20260912.md` in your own worktree with baseline/tip, exact paths, exact commands and counts, and no live acceptance claim. Exact-path commit with command-scoped identity. Return <=5 concise lines. Coordinator will independently review this delta separately.
