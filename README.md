# Extra — Agent OTP / Synapse Packages

Current latest consolidated package: **R9B.4.5 review-evidence precision / replay binding**  
Checkpoint: **2026-10-08**

## Latest

See [`Agent_OTP_R9B45_LATEST/`](Agent_OTP_R9B45_LATEST/).

Current state:

- `R9B45_REVIEW_EVIDENCE_PRECISION_STATIC_CANDIDATE`
- `FRESH_WINDOWS_EVALUATION_REQUIRED`
- `HUMAN_VERDICT_PENDING`
- `R9C_BLOCKED`

Security ceiling remains:

- `MEASURED_NOT_AUTHENTICATED`
- `stable_node_id = UNBOUND`
- `authorization_status = NOT_AUTHORIZED`
- `authority_effect = NONE`

Latest public-safe ZIP SHA-256:

`a48d5df8234a9fb9a6c296b09d0cf7c985dcca43e3d91b0e6880131a149b75d4`

Original local sealed ZIP SHA-256:

`f183a27b883f48e10be52f0584685143c2a5a8c562a8d34506c309fa516ec96d`

The public-safe derivative changes only a stale local temporary path in historical test evidence and regenerates affected manifests. It does not change protocol/source semantics.

## Historical package

The prior **R9B.2** package remains archived under [`Agent_OTP_R9B2_FULL_BUNDLE/`](Agent_OTP_R9B2_FULL_BUNDLE/).

## Review baseline

CodeDiff v2.6 reviewed baseline:

`hardening/v2.6 @ 41369e4a94ee9ab85c48ba117319658248e59ece`

Harness Full Validation **#153 / #154 SUCCESS**.

CodeDiff is a review/sensor layer, not approval authority.
