# Test-plan case track-1-vhl (test/plans/who-itb-agreement.test-plan.json).
# No test runs these Scenarios yet: a tester runs the WHO-ITB beside the
# library and records a report against the plan (bean OI-33 blocks CI:
# no licence on the track images, no pinned QR reader, the GDHCN DEV trust
# list host unreachable from the build). Written from the plan's assertions.
@case:track-1-vhl @manual
Feature: WHO-ITB Track 1, HCERT VHL: the library agrees with the test bed
  ITB test case tc-vhl-001: QR to a verified LAC IPS bundle. Test data:
  WHO-ITB test-data/Track1_VHL_1234_2026.jpg; the PIN is 1234.

  Background:
    Given the HC1 text read from the Track 1 QR image
    And the gdhcn-helper's results for the same image

  @req:stt-tst-009
  Scenario: The decoded COSE_Sign1 is the helper's, byte for byte
    When the library decodes the HC1 text
    Then its protected header, payload and signature bytes equal the gdhcn-helper's cose._raw

  @req:stt-tst-009
  Scenario: Verification agrees with the helper on the DEV trust list
    Given the GDHCN DEV trust list the ITB uses
    When the library verifies the certificate
    Then it reports the same kid and issuer as the gdhcn-helper
    And it fails where the helper reports valid=false

  @req:stt-tst-009
  Scenario: The VHL link is read, authorised and fetched as the ITB does
    When the library reads the VHL link from the HCERT
    Then its url, flags and key are the ones the ITB extracts
    And with the PIN 1234 it fetches the ITI-YY5 manifest
    And it decrypts the IPS bundle the ITB retrieves
