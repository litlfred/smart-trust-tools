# Test-plan case track-3-ph4h-meow (test/plans/who-itb-agreement.test-plan.json).
# No test runs these Scenarios yet: a tester runs the WHO-ITB beside the
# library and records a report against the plan (bean OI-33 blocks CI).
# Written from the plan's assertions.
@case:track-3-ph4h-meow @manual
Feature: WHO-ITB Track 3, HCERT PH4H: the library agrees with the test bed
  ITB test case tc-ph4h-qr-001: QR to a MeOW medication overview bundle.
  Test data: WHO-ITB test-data/Track3_MeOW_2026.jpg.

  Background:
    Given the HC1 text read from the Track 3 QR image
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
  Scenario: The medication overview claim is what the ITB hands to its StructureMap
    When the library returns the PH4H medication overview claim
    Then it equals, byte for byte, the content the ITB passes to the MedicationOverviewMinToMedicationOverviewBundle StructureMap
