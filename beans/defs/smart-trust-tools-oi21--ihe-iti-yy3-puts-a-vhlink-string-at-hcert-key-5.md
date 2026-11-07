---
# smart-trust-tools-oi21
title: 'OI-21: IHE ITI-YY3 puts a vhlink:/ string at HCERT key 5; ITI-YY4 reads an object'
status: todo
type: bug
priority: normal
tags:
    - open-issue
    - upstream
created_at: 2026-10-20T00:00:00Z
updated_at: 2026-11-01T10:00:00Z
---

ITI-YY3 step 5 base64url-encodes the minified payload JSON, prefixes it with vhlink:/ and puts that text at claim -260 key 5. ITI-YY4 step 8 and its example read key 5 as a decoded object. Text-in-CBOR also costs about a third of the QR: on the ITI-YY3 example the string form is ~609 HC1 characters against ~422 for a CBOR map.

## Resolution

Patch prepared for the IHE editors (upstream/ihe-iti-vhl/): for the HCERT carrier key 5 is the payload as a CBOR map; vhlink:/ stays the text form for URI carriers; receivers also accept the string. smart-trust#130 makes the same change on the WHO side.

## Requirements affected

- req:stt-vhl-002

## Sources

- library/ihe-iti-vhl-iti-yy3/sections/s010-2-3-yy3-4-1-3-expected-actions
- library/ihe-iti-vhl-iti-yy4
- library/who-smart-trust-hcert-model

## Status 2026-11-01

The WHO side is fixed: smart-trust#130 merged on 2026-10-26 (main 4a5ac54), so the HCERT model types key 5 as a CBOR map. The IHE side is not: IHE/ITI.VHL main is still 4820147 (2026-06-14), and ITI-YY3 step 5 still prefixes vhlink:/. Stays open for IHE.

## Done when

- [ ] the upstream source is corrected, or the requirement no longer depends on it
