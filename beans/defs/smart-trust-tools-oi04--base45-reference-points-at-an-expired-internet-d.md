---
# smart-trust-tools-oi04
title: 'OI-04: Base45 reference points at an expired Internet-Draft'
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

Both pages cite draft-faltstrom-base45. That draft was published as RFC 9285, which should be the reference.

## Reported

Reported 2026-10-24 to WHO as point 2 of WorldHealthOrganization/smart-trust#138 (https://github.com/WorldHealthOrganization/smart-trust/issues/138).

## Requirements affected

- req:stt-b45-001

## Sources

- library/who-smart-trust-qr-code-generation/sections/s009-8-step-7-encode-as-base45
- library/who-smart-trust-hcert-spec/sections/s018-4-2-2-qr-2d-barcode
- external-schemas/ietf-draft-faltstrom-base45
- external-schemas/ietf-rfc9285

## Status 2026-11-01

A fix for point 2 of smart-trust#138 is drafted in WorldHealthOrganization/smart-trust#139 (open, commit 04bb7a8). It is WHO's to review and merge; smart-trust main 48e8800 still has the old text.

## Done when

- [ ] the upstream source is corrected, or the requirement no longer depends on it
