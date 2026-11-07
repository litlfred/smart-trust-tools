---
# smart-trust-tools-oi03
title: 'OI-03: EKU certificate type for non-DCC payloads is undefined'
status: todo
type: bug
parent: smart-trust-tools-oiep
priority: normal
tags:
    - open-issue
    - upstream
created_at: 2026-10-20T00:00:00Z
updated_at: 2026-11-01T10:00:00Z
---

Appendix A.2 defines EKU OIDs for test, vaccinations and recovery, and QR Code Generation 11 step 7 says to check the EKU "against the certificate type". There is no mapping from subclaims 3, 4, 5, -6 or -7 to a certificate type. DVC (-6) is presumably "vaccinations". VHL (5) has no obvious type.

## Resolution

Add a subclaim-to-certificate-type table, or use the GDHCN Key Usage value set.

## Reported

Reported 2026-10-24 to WHO as point 1 of WorldHealthOrganization/smart-trust#138 (https://github.com/WorldHealthOrganization/smart-trust/issues/138).

## Requirements affected

- req:stt-ver-004

## Sources

- library/who-smart-trust-qr-code-generation/sections/s012-11-verifying-the-same-steps-upwards
- library/who-smart-trust-hcert-spec/sections/s028-a-2-extended-key-usage-identifiers

## Status 2026-11-01

No change upstream: smart-trust main 48e8800 (2026-10-30) still has the text, and open PR #139 does not cover this point of #138.

## Done when

- [ ] the upstream source is corrected, or the requirement no longer depends on it
