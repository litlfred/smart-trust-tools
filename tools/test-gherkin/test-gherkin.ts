import { toolFactory } from "@litlfred/cat-harness-tools/schemas/tools/tool-folders.js";
import { defineTool } from "@litlfred/cat-harness-tools/schemas/tools/tool.js";

export default toolFactory((t) =>
  defineTool({
    id: "test-gherkin",
    title: "Every test has a Gherkin Scenario",
    description:
      "Run the harness's check:test-gherkin over this repository: every Rust #[test], Kotlin @Test and TypeScript conformance run(...) is named by exactly one Scenario in test/features/ (@test:<file>::<scope>::<name>), every tag names a test, and every WHO-ITB Scenario's @itb:<suite>/<testcase> names a case of the WHO-ITB suites at the commit references/who-itb cites.",
    install: { none: true },
    invoke: { shell: "tools/test-gherkin/check_test_gherkin.sh" },
    io: {
      inputs: [
        { name: "itb", schema: t("RepoPath"), required: false, arg: { flag: "--itb" }, description: "A WHO-ITB checkout already on disk, instead of fetching the cited commit's test suites." },
      ],
      outputs: [],
    },
    satisfies: ["hcert-conformance-testing"],
    selection: {
      when: "A test or a feature file is added, renamed or removed, or CI checks they agree.",
      limits: "Checks the tags, not that the steps match the test's assertions: a reviewer reads that. Without --itb it fetches the WHO-ITB test suites, so it needs the network.",
      cost: "Seconds.",
    },
    requires: { runtime: ["bun", "git", "python3"], network: true },
  }),
);
