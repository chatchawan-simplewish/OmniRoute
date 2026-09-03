# OmniRoute V56 disk-module live incident

## Outcome

V56 was sent exactly once and failed safely before candidate execution. It is
permanently spent and must not be retried, continued, reused, reinterpreted, or
used as a fallback.

## Preconditions

- Classification Sol High PASS: `c5be9d0ed9cb011588e450eec78dd1c47776e5fd`.
- Post-commit tuple: classification commit `809a8efaf2da38ba7a0ecedb32b8907be348fb9b`,
  direct parent `c64d49bc1daf78926ca669ba81c7ed17020a7387`, one changed path.
- Exact source projection, runtime/docs pins, empty index, inherited 12-path
  baseline, clean evidence worktree, DNS absence, zero Windows residue, and
  VM1205 safe checkpoint all passed.
- Fresh CUA realm first call was exactly `await cua.getState();`.
- Direct audit passed: all 132 V35-V54 predecessor declarations absent and
  `secureConsoleV56Module` absent.
- Tool state proved Chrome profile `Codex-Chrome-Bell-PC2`, exactly one API
  Tokens tab at `https://dash.cloudflare.com/profile/api-tokens`, and a
  disjoint tab/provider lane.

## Failure and cleanup

The exact reviewed loader passed its local byte-count, SHA-256, and ASCII
checks, then its sole `import(data:text/javascript;base64,...)` attempt failed
with fixed error class/message surface:

`Unsupported import specifier ... in node_repl. Use a package name ... or a relative/absolute/file:// .js/.mjs path.`

The candidate ESM module was not parsed or evaluated. It performed no runtime
setup, browser connection, tab listing/claim, navigation, search fill, provider
mutation, token action, credential/secret access, clipboard action, DNS action,
or VM action. One fixed cleanup query returned
`V56_LOADER_FAILURE_CLEANUP_PASS` with `moduleNull=true`; the realm was then
reset.

## Replacement finding

A separate disposable-realm capability check, after reset, proved
`node:vm.SourceTextModule` and `SyntheticModule` are available and that an
in-memory source module can execute with one allowlisted bridged dynamic import.
This is diagnostic evidence only. Any replacement requires a new V57 contract,
fixtures, independent review, classification, and fresh action-time checks.
