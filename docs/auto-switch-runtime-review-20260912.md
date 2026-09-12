# Runtime source acceptance

Independent Sol High review of routing port `c70211160bae5237be4dfd7c8bb9e2894d757492` found one P1: the Codex app-server execution path bypassed the submitted-attempt hook. A post-send error could therefore look like zero attempts and allow another upstream dispatch. The other requested controller, authorization, persistence, quota, output and tool-acknowledgement gates passed review. No broad test suite was rerun by the reviewer.

Original implementer fix `2ab36c708de4cf72c2b3d92b523f08d44f9f9558` rejects first-class `codex-app-server` and every named Codex transport before agent-route dispatch. Default Codex HTTP remains eligible, and ordinary non-agent routes are unaffected. The focused regression passed 1/1 with zero dispatches; the integration file passed 9/9. Separate independent Sol High review accepted the fix by direct source inspection without rerunning passing checks.

Independent Sol High review also accepted Gemini preservation delta `2ab36c7..dc53bcfed67b3bbea7d2fbf82468342e573dadb3`: strict enabled account-menu discovery, unique requested-mode selection, Flash-Lite parsing, selected-state verification, three-second hydration, sanitized 400/502 failures and stale-row filtering. The newer API/auth structure and image-retirement guard remain preserved. All 28 focused tests and scoped lint passed; reviewer did not repeat them.

This accepts the candidate source, not live deployment. Image acceptance, intended inference credentials, provider qualification, live bindings and current-client reconciliation/rollout remain outstanding.
