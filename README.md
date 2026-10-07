# Extra — Agent OTP / Synapse public package checkpoint

Latest public-safe full package: **R9B.2 pre-provisioned pinned registry measurement**  
Checkpoint date: **2026-10-07**

## Current status

`R9B1_LOCAL_MEASUREMENT_PASS`
→ `REGISTRY_SELF_ENROLLMENT_GAP_FOUND`
→ `R9B2_PREPROVISIONED_PINNED_REGISTRY_READY`

Security ceiling remains:

- `MEASURED_NOT_AUTHENTICATED`
- `stable_node_id = UNBOUND`
- `authorization_status = NOT_AUTHORIZED`
- `authority_effect = NONE`
- `G1 = CLOSED`
- `F2 = CLOSED`

R9B.2 separates registry provisioning from measurement and requires an **exact SHA-256 pin** for the pre-provisioned
verifier registry. It is still a rehearsal/measurement layer, not a protected installation credential.

## Package layout

- `packages/synapse_boot_auth_r9b2_preprovisioned_registry_measurement_20261007/`
  - complete extracted public-safe package
  - candidate source
  - handoff packets
  - review/evidence layer
  - tests/lints/CodeDiff artifacts
  - manifest
- `releases/synapse_boot_auth_r9b2_preprovisioned_registry_measurement_20261007_PUBLIC_SAFE.zip`
  - downloadable public-safe full ZIP

## Integrity

Original local package SHA-256:

`8272f9e7d1788719da7054a9cc6ba83f23bec613ef572092ae8cb8a258b18d13`

Public-safe ZIP SHA-256:

`516fa450f48dd3162832b68f31c3b36df026267cea68dabaf1d906f09b873e2b`

The SHA values differ intentionally. Before publishing to this **public** repository, historical accumulated
patch/log evidence containing a local workspace literal was redacted to `<LOCAL_WORKSPACE>`. Functional source was
not altered by this publication redaction.

Redacted historical occurrences: **5**

CodeDiff privacy feedback for this publication:

`PR-with-codediff-finder@ffac2e1309f565ff0fb139c42b6405013dd17497`

## Trust note

CodeDiff remains a degraded SHADOW sensor in this package (`trusted_for_gate=false`). It is a risk/evidence sensor,
not an approval authority.
