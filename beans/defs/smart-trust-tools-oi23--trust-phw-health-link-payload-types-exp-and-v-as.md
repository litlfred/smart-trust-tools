---
# smart-trust-tools-oi23
title: 'OI-23: trust-phw Health Link payload types exp and v as strings and requires type'
status: todo
type: bug
priority: normal
tags:
    - open-issue
    - upstream
created_at: 2026-10-20T00:00:00Z
updated_at: 2026-11-01T10:00:00Z
---

HealthLinkPayload types exp and v as string where SMART Health Links and IHE VHL use numbers, and VerifiableHealthLinkPayload makes type 1..1, a field neither SHL nor IHE has.

## Resolution

Raised as WorldHealthOrganization/smart-trust-phw#17: exp integer64, v integer, VHL type 0..1 (absent inside an HCERT).

## Requirements affected

- req:stt-vhl-001

## Sources

- library/who-smart-trust-phw-health-link-payload
- external-schemas/hl7-smart-health-links
- library/ihe-iti-vhl-iti-yy3/sections/s010-2-3-yy3-4-1-3-expected-actions

## Status 2026-11-01

No change upstream: smart-trust-phw main is still 73b3c64 (2026-10-23), so #17 is not fixed.

## Done when

- [ ] the upstream source is corrected, or the requirement no longer depends on it
