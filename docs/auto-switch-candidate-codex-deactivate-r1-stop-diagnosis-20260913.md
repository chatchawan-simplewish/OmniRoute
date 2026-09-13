# Candidate Codex deactivation R1 local STOP diagnosis — 2026-09-13

## Evidence and conclusion

- The single reviewed invocation passed all action-time pins and the local self-check, then exited `2`. Its immutable receipt is `docs/auto-switch-candidate-codex-deactivate-r1-result-20260913.json`, SHA-256 `e85e339b88c36da8c2fdf41b569f96ecec1895a75041d3cb122ce9e93a33dd80`: outer status `UNKNOWN`, stage `transport`, `remote=null`, `candidate_stopped=null`.
- Frozen launcher SHA-256 is `5a5b80f62a04255addd0e2ac9598de48efe0cc12500e80a899b576cfb4f6be8d`; independent PASS review SHA-256 is `3c48dbecfeb50b016d0d72c54f4c70a14ae716316da3eff449ecaf109f72028a`; reviewed-pins SHA-256 is `e82ea453ad33857c90809bc086e0a780cff39c00290418ece4fac5e242760002`.
- `execute()` leaves the default `transport` receipt when the bounded SSH child raises, when any stderr is present, or when stdout cannot be parsed and validated. It does not retain the child return code, output byte counts/hashes, or a pre/post-dispatch marker. Therefore the receipt cannot distinguish failure before SSH dispatch from SSH/remote execution followed by missing, malformed, contradictory, or stderr-bearing output. The actual candidate, target connection, PATCH dispatch, and readback state all remain **UNKNOWN**.

## Local source checks

The frozen rendered program generated with a non-secret fixture token is 22,500 bytes with SHA-256 `b4343128ea1e7dc39a3ba061eeee1f466a1b1943c912f1157f4856b9adc4ab49`. It parses as Python, contains the expected `json`, `os`, `pathlib`, `re`, `sqlite3`, `stat`, `subprocess`, `threading`, `time`, and `urllib.parse` imports, contains exactly one native child validator definition and call before projection, and excludes the fixture token. The focused test verifies the rendered validator's wrong-ID, rc0/wrong-status, and contradictory post-dispatch rejections, but it does not execute the full emitted Docker/HTTP path. No deterministic source defect explains the spent outcome from retained evidence.

## Minimum fresh reconciliation

Before any replacement mutation, use a separately reviewed read-only reconciliation that revalidates the exact candidate name/ID/image/volume/running/healthy/network-none isolation with repeated formatted Docker inspection, then performs at most one candidate-local authenticated GET of the exact Codex row `8f92f200-d280-47b3-b380-2d94be0a4b75`. Retain only fixed child return-code/status categories, bounded stdout/stderr byte counts and hashes, exact public IDs, and the sanitized `isActive` boolean. Keep the token in memory/stdin, emit no response body or credential fields, and perform no PATCH, restart, stop, cleanup, SQLite access, provider request, or retry. Independent review and a fresh explicit sole-owner dispatch remain required.
