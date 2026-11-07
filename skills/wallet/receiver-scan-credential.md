---
name: receiver-scan-credential
description: >
  The health worker at a receiving system scans the QR a holder shows (an
  HCERT, or the HCERT carrying a VHL) and, for a passcode-protected VHL,
  enters the passcode the holder says. Input is the QR as shown; output is
  the HC1 text (and passcode) handed to the receiving system, which verifies
  it. Performed by a person; never judges authenticity.
input: schemas/skills/receiver-scan-credential/input.schema.json
output: schemas/skills/receiver-scan-credential/output.schema.json
---

# Scan a health credential

**Performed by a person**: the health worker operating a receiving system
(a CHW app, a clinic EHR, a point-of-care viewer). Role
`receiving-health-worker`. What happens to the scan is the system's:
`hcert-verify` (or its unverified triage read) and `vhl-receive`.

## Input and output

The contract is [`input.schema.json`](../../schemas/skills/receiver-scan-credential/input.schema.json)
and [`output.schema.json`](../../schemas/skills/receiver-scan-credential/output.schema.json).

- **In:** the `shown` QR, its `medium` (paper or a screen), and, for a VHL,
  the `passcode` the holder says.
- **Out:** the `hc1` text read, one per QR, and the `passcode` when one was
  entered.

## What the health worker does

1. Scan each QR once, with the receiving system's camera.
2. For a VHL, type the passcode the holder says; never ask to see it written.
3. Hand over to the system, which verifies. The health worker does not
   decide whether a credential is genuine: the system's result says so.

## Success criteria

- Each QR's text reaches the receiving system unchanged, starting `HC1:`.
- A QR that will not scan is reported as such, and the records are treated
  like paper.
