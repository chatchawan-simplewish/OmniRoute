# OmniRoute V36 ordered candidate — live incident

Date: `2026-09-02` (`Asia/Bangkok`)

## Terminal classification

V36 is **consumed / failed cleanly** and permanently ineligible. Never retry,
continue, reinterpret, relax, or reuse the V36 cell.

The sole `openTabs()` call fulfilled, but the trusted-listing/rank-zero
Cloudflare predicate returned no candidate. The cell stopped before any
`claimTab()`, navigation, wait, URL read, or page snapshot. No tab ID,
provider-tab ID, title, URL, group, timestamp, account ID, zone ID, href,
secret, token, credential, raw listing, or raw exception was emitted.

## Immutable package and pins

- Corrected brief commit:
  `8905b23e81df28eb283614d96cba0ba1fa5c9957`
- Independent PASS review commit:
  `f070cae4b86b19d96c60ccc918f8be1d9ffa9c27`
- Execution-classification commit:
  `35ec51937a06f69f70089e6b15ecc5052109a067`
- Executable bytes/SHA-256:
  `15000` / `5395EAC07AEC15AB63BC78AA9DB1E89AE909DC00EE74991F6CEDF0BCB32834B0`
- Post-classification tuple: HEAD
  `35ec51937a06f69f70089e6b15ecc5052109a067`, parent
  `f070cae4b86b19d96c60ccc918f8be1d9ffa9c27`, exactly one classification
  path, chain paths `140`, exclusions `142`, projection records `10661`,
  projection SHA-256
  `C4C85893769D133224AC7404B628C8B0D4B0EBBFF471620B158E652E152B4EBD`,
  empty index, exact 12-path dirty baseline.
- Runtime module/docs/API pins matched.
- Evidence worktree was clean at
  `80adaa7d5d63d1d2c7bfa63b236c6bee93b3b1d8`.
- Windows temporary/process residue was zero.
- VM1205 matched the full safe checkpoint.
- Public A/CNAME counts were zero through `1.1.1.1` and `8.8.8.8`.
- The owner's exact Chrome profile/window/task-tab confirmation was present.
- The Node realm was freshly reset and every named V35/V36 declaration was
  absent before the exact executable was extracted and sent once.

## Sanitized fixed-schema evidence

```text
result=V36_FRESH_ORDERED_REACQUISITION_FAILED_STOP
declarationShape=true
moduleShape=true
agentShape=true
connectedShape=true
documentationValidated=true
documentationLength=42596
sessionNamed=true
offeredCount=-1
listingValidated=false
rankZeroSelected=false
candidateUrlCloudflare=false
controllerOwnership=false
tabShape=false
homeUrlValidated=false
snapshotValidated=false
semanticComplete=false
snapshot=null
importAttempted=1
importFulfilled=1
setupAttempted=1
setupFulfilled=1
connectAttempted=1
connectFulfilled=1
documentationAttempted=1
documentationFulfilled=1
documentationWriteAttempted=1
documentationWriteFulfilled=1
nameAttempted=1
nameFulfilled=1
openTabsAttempted=1
openTabsFulfilled=1
claimAttempted=0
claimFulfilled=0
navigationAttempted=0
navigationFulfilled=0
waitAttempted=0
waitFulfilled=0
urlAttempted=0
urlFulfilled=0
snapshotAttempted=0
snapshotFulfilled=0
writeAttempted=1
errorClass=Error
consumed=true
bindingEligible=false
bindingNull=true
state=V36_REACQUISITION_OR_READINESS_FAILED
```

The terminal cleanup predicate separately proved consumed true, retained tab
null, eligibility false, terminal state exact, and setup/agent/browser bindings
null. The Node realm was then reset.

## Cause and no-residue boundary

The precise rejecting predicate is **NOT PROVEN** because the reviewed output
intentionally collapses all private listing failures and emits neither listing
shape nor URL metadata. The pinned runtime statically remaps returned arrays
through a standard array `map`, while V35 had previously validated eight record
shapes; this makes a non-Cloudflare rank-zero record a plausible inference, but
it is not direct evidence and must not be promoted to fact. Shape or ordering
drift remains possible.

No tab was claimed, created, closed, or navigated. No provider-persistent
change, secret operation, proxy/tunnel/DNS/routing mutation, VM process, or
listener was started. Session naming is the only completed browser-session
side effect and is non-provider-persistent.

A replacement requires a new committed contract and independent Sol High PASS
review. It must preserve structural no-iterator listing validation, descriptor-
cached bounded evidence, cached primitive-ID claim, one enumeration, one claim,
no metadata emission, same account-home signature, no retry, terminal cleanup,
and every secret/confirmation boundary. It must not depend on rank zero being
the Cloudflare task tab; instead it may privately filter the structurally
validated records to one exact Cloudflare task candidate and require uniqueness
before the sole claim.
