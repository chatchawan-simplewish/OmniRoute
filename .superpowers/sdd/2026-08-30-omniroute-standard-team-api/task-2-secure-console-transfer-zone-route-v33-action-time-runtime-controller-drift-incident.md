# OmniRoute V33 action-time runtime/controller drift incident

Date: `2026-09-02` (`Asia/Bangkok`)

## Terminal prestart classification

V33 was **not executed and not consumed**. Its reviewed executable was never
sent to the persistent Node tool. The action-time gate stopped before that call
because two required runtime/predecessor pins were false:

1. the pinned `26.825.51511` installed API document was absent; and
2. the persistent `secureConsoleChromeV5` controller and V32 predecessor
   declarations were absent from the current Node realm.

A fixed non-browser state query confirmed every V33 declaration remains
undefined. No Chrome method, browser tab method, provider action, VM mutation,
process start, credential action, clipboard action, or network action occurred.

The V33 static package is permanently action-time ineligible. It must not be
retried, executed, continued, reinterpreted, or relaxed. A new independently
reviewed fresh-session attachment/reacquisition replacement is required.

## Pinned V33 static package

- Corrected V33 brief: `57ce295eabcfef389854ca5915b63ed622c56262`.
- Independent Sol High PASS review:
  `bb24912c5b49d5910b4967828404bca326edf964`.
- Non-self-referential classification:
  `5c37b684471521bbde8ccb1b56b80c0e34e35118`.
- Post-classification tuple: chain paths `124`; exclusions `126`; records
  `10661`; projection SHA-256
  `C4C85893769D133224AC7404B628C8B0D4B0EBBFF471620B158E652E152B4EBD`;
  empty index; exact 12-path dirty product baseline.

Those static facts remain valid evidence. They do not override the failed
action-time runtime/controller pins.

## Exact runtime drift evidence

The two executable runtime inputs retained from the original fresh-session
package still match:

- `chrome/26.825.51511/skills/control-chrome/SKILL.md`: present, `12813`
  bytes, SHA-256
  `3359692CE61D149B01EE21812A9F9E7381B060A35C28FDA8493057CBE90C0C3A`.
- `chrome/26.825.51511/scripts/browser-client.mjs`: present, `149210`
  bytes, SHA-256
  `C52BA09202F0E82CAA6F6D2A6463A8635C1B1316567975D9B91C1A05FB5AF501`.

The pinned
`browser/26.825.51511/docs/api.json` is absent. No file under the current plugin
cache matches its former `58477`-byte SHA-256
`4BFEB97E958025DB37D52AEA11B75BC70BCA417B4995B0F711C0F07F3DDCCB08`.

The current installed browser and Chrome packages instead expose identical
`26.831.20005` runtime inputs:

- `docs/api.json`: `58480` bytes, SHA-256
  `A7C8D53096EA2563CF939D5F7A37DFC2AE0701E891510566930868D04CE0F5DF`.
- `scripts/browser-client.mjs`: `149771` bytes, SHA-256
  `A50E341988B45C547B02DB74787AA64AFFC64F42B5C605308823EEC853179298`.

This is material runtime-package drift. Substituting the new files into V33
without a new review would violate its exact-byte gate and is forbidden.

## Exact Node-state evidence

The fixed state-only query returned:

- `controllerPresent=false`;
- V32 consumed/retained/state exact checks: false/false/false;
- V33 consumed/retained/state declarations absent: true/true/true.

The query used only `typeof`, equality tests, and one fixed `nodeRepl.write`.
It did not call `browsers.get`, documentation, selected/list/get/new, URL,
locator, navigation, evaluation, close, or any provider/browser method.

## Successor boundary

The smallest aligned successor must be a new fresh-session, one-shot Chrome
attachment/reacquisition replacement pinned to the current installed runtime.
It must independently re-establish a persistent controller before any page
work, preserve the exact profile/window/tab confirmation already supplied by
the owner, and retain every secret, semantic signature, completeness,
no-residue, no-retry, cleanup, and confirmation constraint.

The replacement requires a new committed brief, independent Sol High PASS
review, non-self-referential classification, post-commit coordinator tuple,
and fresh action-time pins. It may not execute V33 or assume any missing
declaration. The final Create/native Copy/native masked Paste confirmation and
later separate exact-row deletion confirmation remain mandatory and unreached.
