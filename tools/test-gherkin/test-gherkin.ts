import { toolFactory } from "@litlfred/cat-harness-tools/schemas/tools/tool-folders.js";
import { defineTool } from "@litlfred/cat-harness-tools/schemas/tools/tool.js";

// Temporary: a local stand-in for cat-harness `check:test-gherkin`, until it lands in a pinned cat-harness.
export default toolFactory((t) =>
  defineTool({
    id: "test-gherkin",
    title: "Every test has a Gherkin Scenario",
    description:
      "Check test/features/*.feature against the suites: every Rust #[test], Kotlin @Test and TypeScript conformance run(...) has a Scenario tagged @test:<path>::<test>, every such tag names a test, WHO-ITB Scenarios carry @itb:<suite>/<testcase>, and every test-plan case names its feature file. Temporary, until cat-harness check:test-gherkin is pinned.",
    install: { none: true },
    invoke: { shell: "python3 tools/test-gherkin/check_test_gherkin.py" },
    io: {
      inputs: [
        { name: "list", schema: t("Flag"), required: false, arg: { flag: "--list" }, description: "Print each test's @test: tag and check nothing." },
      ],
      outputs: [],
    },
    satisfies: ["hcert-conformance-testing"],
    selection: {
      when: "A test or a feature file is added, renamed or removed, or CI checks they agree.",
      limits: "Checks the tags, not that the steps match the test's assertions: a reviewer reads that.",
      cost: "Under a second.",
    },
    requires: { runtime: ["python3"], network: false },
  }),
);
