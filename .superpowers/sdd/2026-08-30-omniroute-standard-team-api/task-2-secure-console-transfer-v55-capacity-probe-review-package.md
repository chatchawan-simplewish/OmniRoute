# V55 27,200-byte capacity probe review package

`authorizes_live_execution=false`

## Purpose

The final reviewed V55 executable is 26,597 ASCII bytes. Prior direct-cell
capacity evidence covers only 25,351 bytes. This package proposes one inert,
disposable-realm capacity probe before classification.

## Exact probe

- Path: `task-2-secure-console-transfer-v55-27200-byte-capacity-probe.js`
- Bytes: `27200`
- SHA-256: `6D4E928C1CB249893F97154372C1F60E1708B0909F7558CF1F56D35DB17818A1`
- Encoding surface: ASCII only; `node --check` PASS.
- Behavior: evaluate one literal ASCII string and call only
  `nodeRepl.write({result:"V55_CAPACITY_PASS",payloadBytes:27200})`.
- It imports nothing, acquires no browser, reads no tab, and performs no UI,
  provider, credential, secret, clipboard, storage, DNS, VM, or network action.

## Execution contract

After independent Sol High PASS, reset the CUA realm and initialize it with the
required first `await cua.getState();` call. Send the exact committed probe once.
Accept capacity only if the terminal result is exactly
`V55_CAPACITY_PASS` with `payloadBytes=27200`. Any failure or uncertainty stops.
Reset the disposable realm immediately after the result. The proof establishes
input capacity only; it does not prove exact V55 candidate-byte fidelity or
authorize V55 live execution.
