# Agent OTP R9B.2 Full Bundle

This directory contains the complete current self-contained R9B.2 source package as a deterministic multipart text bundle.

- parts: **7**
- gzip/tar archive SHA-256: `0d89539d18d13fec212548a0b250861fcd35cfc85c7a44de5b57804cbd3a6021`
- extracted manifest SHA-256: `d8e6796a882bb173a956b8062ababfae66c3ccccc1e416e55161dafeceeea7f7`
- extracted file count: **71**

Reconstruct:

```bash
python extract_full_package.py
```

The script verifies both the compressed archive SHA-256 and inner tar SHA-256 before extraction.

Security ceiling: `MEASURED_NOT_AUTHENTICATED / NODE_UNBOUND / G1_F2_CLOSED`.
