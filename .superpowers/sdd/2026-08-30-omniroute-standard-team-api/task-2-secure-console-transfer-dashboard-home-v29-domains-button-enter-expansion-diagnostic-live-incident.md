# V29 Domains-button Enter diagnostic live incident

## Verdict

`FAILED_CLEAN_BEFORE_PRESS` — V29 was consumed exactly once and returned
`PRECONDITION_FAIL`. It is permanently spent and must never be retried,
continued, reinterpreted, or used as authority for another action.

No Enter, click, fill, direct navigation, provider write, secret action, or
provider-persistent change occurred. The exact created tab closed and no
retained handle remains.

## Reviewed execution tuple

- Fixed brief: `7c14ed6077fb77bd1668cabc399ddfabf0ad562b`.
- Independent Sol High PASS review:
  `a947ab77ba90610c5f4aadf0bff3c100a7b77291`.
- Non-self-referential classification:
  `4cd005ffcb499e0a8111d8c326a875f982cc0c0e`.
- Executable: `22060` normalized LF bytes, SHA-256
  `9B23FCF320AC1711365F4A61B9A7D005798707A1748EDFDD0591869E95892D8F`.
- Action-time coordinator tuple: chain/exclusions/records `106/108/10661`;
  projection
  `C4C85893769D133224AC7404B628C8B0D4B0EBBFF471620B158E652E152B4EBD`;
  index `0`; exact dirty baseline `12`.
- Runtime, evidence worktree, temporary/process residue, VM1205, public DNS,
  and persistent predecessor/V29-absence pins all matched the reviewed
  contract before the sole call.

## Fixed pre-snapshot evidence

- Host and exact account-home path: true.
- Unique/visible Domains button: true/true; counts `1/1`.
- Native button, href absent, native element click absent: true/true/true.
- Enabled, non-inert, form owner absent: true/true/true.
- Positive rectangle, within viewport, center hit self/descendant, pointer
  events enabled, keyboard tab stop: all true.
- `aria-controls` present and target present: true/true.
- `aria-expanded=true`: false.
- Controlled target geometrically visible: **true**.
- Busy count: `0`.

The reviewed V29 precondition required the controlled target to be hidden.
That single predicate was false, so `preShapeExact=false` and the gate stopped
before constructing or counting the press locator.

## Counters and cleanup

- New tab, navigation, initial URL, settled wait/URL, and pre-snapshot:
  attempts/fulfilments all `1/1`.
- Locator count, target-safety evaluation, Enter press, and post-snapshot:
  attempts/fulfilments all `0/0`.
- Close `1/1`; terminal write attempted `1`.
- Cleanup `EXACT_TAB_CLOSED`; residue converged true; retained handle false;
  state `V29_DIAGNOSTIC_FAILED_CLEAN`; consumed true; sanitized error class
  `Error`.

## Replacement boundary

Any successor must be a fresh separately committed, independently Sol High
reviewed, classified, and action-time-pinned one-shot contract. It may treat
geometric visibility of the existing controlled container as disproven as a
collapsed-state proxy, while retaining the exact unique-button, enabled,
non-inert, hit-test, tab-stop, `aria-expanded=false`, and dual
`button.form === null` safety gates. This incident itself authorizes no press
or other browser/provider action.
