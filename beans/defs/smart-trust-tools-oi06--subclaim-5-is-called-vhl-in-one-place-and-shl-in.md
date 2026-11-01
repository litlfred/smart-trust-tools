---
# smart-trust-tools-oi06
title: 'OI-06: Subclaim 5 is called VHL in one place and SHL in another'
status: completed
type: bug
priority: normal
tags:
    - open-issue
    - upstream
created_at: 2026-10-20T00:00:00Z
updated_at: 2026-11-01T10:00:00Z
---

QR Code Generation 2.1 and the HCert logical model describe subclaim 5 as the URI of a Verifiable Health Link. HCERT Specification 3.2.7.1.5, which is the authoritative list, describes it as Smart Health Link (SHL) and links the SMART Health Links spec. The two define different URI schemes and payloads.

## Resolution

Raised as WorldHealthOrganization/smart-trust#130: 3.2.7.1.5 becomes Verifiable Health Link (IHE ITI VHL, SHL payload format), and the HCert model types key 5 as the trust-phw VerifiableHealthLinkPayload, carried as a CBOR map. The library follows that (STT-VHL-002).

## Requirements affected

- req:stt-pay-009
- req:stt-sel-001
- req:stt-vhl-002

## Sources

- library/who-smart-trust-qr-code-generation/sections/s003-2-step-1-select-the-payload-type
- library/who-smart-trust-hcert-spec/sections/s013-3-2-7-health-certificate-claim
- library/who-smart-trust-hcert-model

## Status 2026-11-01

Fixed upstream: WorldHealthOrganization/smart-trust#130 merged on 2026-10-26 (main 4a5ac54). HCERT Specification 3.2.7.1.5 is now "Verifiable Health Link (VHL)", and claim key 5 holds the VHL payload as a CBOR map, as STT-VHL-002 already assumes.

## Done when

- [x] the upstream source is corrected, or the requirement no longer depends on it
