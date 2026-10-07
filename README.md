# Extra — Agent OTP / Synapse R9B.2 Full Package

Current consolidated version: **R9B.2 pre-provisioned pinned registry measurement**  
Checkpoint: **2026-10-07**

## Status

`R9B1_LOCAL_MEASUREMENT_PASS` → `R9B2_PREPROVISIONED_PINNED_REGISTRY_READY`

Security ceiling remains:

- `MEASURED_NOT_AUTHENTICATED`
- `stable_node_id = UNBOUND`
- `authorization_status = NOT_AUTHORIZED`
- `authority_effect = NONE`
- `G1 = CLOSED`
- `F2 = CLOSED`

## Full source package

The current self-contained source package is stored under [`Agent_OTP_R9B2_FULL_BUNDLE/`](Agent_OTP_R9B2_FULL_BUNDLE/) as a verified multipart text bundle. Run `python Agent_OTP_R9B2_FULL_BUNDLE/extract_full_package.py` to reconstruct `Agent_OTP_R9B2_FULL/`.
It contains the components required by the latest R9B.2 flow:

- R6 Named Pipe verifier/capture boundary
- R9A.3 native handle-bound mediator evidence
- R9A.3.1 portable matrix runner
- R9B.1 dedicated mediator Named Pipe measurement
- R9B.2 pre-provisioned verifier registry + exact SHA-256 pin
- evaluators, tests, privacy/masking helpers, semantic lint and YM handoff packets
- closeout/result/lineage and regenerated package manifest

## Integrity references

Original local R9B.2 package SHA-256: `8272f9e7d1788719da7054a9cc6ba83f23bec613ef572092ae8cb8a258b18d13`

Public-safe archival ZIP SHA-256: `516fa450f48dd3162832b68f31c3b36df026267cea68dabaf1d906f09b873e2b`

The public-safe artifact differs only because historical local-workspace literals in accumulated old patch/log evidence were redacted before public publication. The consolidated current source package here omits those historical patch archives entirely.

Publication privacy feedback: `PR-with-codediff-finder@ffac2e1309f565ff0fb139c42b6405013dd17497`

## Trust note

CodeDiff remains a degraded SHADOW sensor (`trusted_for_gate=false`). It is not an approval authority. R9B.2 is still measurement/rehearsal; protected installation credential work has not been activated.
