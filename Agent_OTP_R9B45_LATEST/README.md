# Agent OTP / Synapse R9B.4.5 — Latest Public-Safe Package

Latest packaged checkpoint: **R9B.4.5 review-evidence precision / replay binding**

## Current gate state

- `R9B45_REVIEW_EVIDENCE_PRECISION_STATIC_CANDIDATE`
- `FRESH_WINDOWS_EVALUATION_REQUIRED`
- `HUMAN_VERDICT_PENDING`
- `R9C_BLOCKED`
- security ceiling: `MEASURED_NOT_AUTHENTICATED / UNBOUND / NOT_AUTHORIZED / NONE`

## Package

`synapse_boot_auth_r9b45_review_precision_replay_evidence_20261008_PUBLIC_SAFE.zip`

Public-safe ZIP SHA-256:

`a48d5df8234a9fb9a6c296b09d0cf7c985dcca43e3d91b0e6880131a149b75d4`

Original local sealed R9B.4.5 ZIP SHA-256:

`f183a27b883f48e10be52f0584685143c2a5a8c562a8d34506c309fa516ec96d`

The public-safe derivative differs only by redacting one stale local temporary preparation path from historical R6 test evidence and regenerating affected manifests. No protocol/source semantics were changed.

## Candidate manifests

- original candidate manifest: `1f52a417b2b82e6457c8d005ea2ddfc5a8c47e54e7917123107118e293507dc4`
- public-safe candidate manifest: `6fb8cdacf9f1f17fcbd25e0eb4ba5f4d1e51209e8981e87e690e53bfaa4d6cd0`

## Review baseline

CodeDiff v2.6 reviewed baseline:

`hardening/v2.6 @ 41369e4a94ee9ab85c48ba117319658248e59ece`

Full Validation: **#153 / #154 SUCCESS**.

CodeDiff remains review/sensor infrastructure, not approval authority.
