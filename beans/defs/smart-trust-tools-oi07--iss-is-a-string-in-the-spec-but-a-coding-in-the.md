---
# smart-trust-tools-oi07
title: 'OI-07: iss is a string in the spec but a Coding in the logical model'
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

The CWTPayload logical model types claim 1 as Coding. HCERT 3.2.4 and RFC 8392 type it as a string.

## Reported

Reported 2026-10-24 to WHO as point 4 of WorldHealthOrganization/smart-trust#138 (https://github.com/WorldHealthOrganization/smart-trust/issues/138).

## Requirements affected

- req:stt-cwt-005

## Sources

- library/who-smart-trust-hcert-spec/sections/s010-3-2-4-issuer
- library/who-smart-trust-cwt-payload-model

## Status 2026-11-01

A fix for point 4 of smart-trust#138 is drafted in WorldHealthOrganization/smart-trust#139 (open, commit 04bb7a8). It is WHO's to review and merge; smart-trust main 48e8800 still has the old text.

## Done when

- [ ] the upstream source is corrected, or the requirement no longer depends on it
