#!/usr/bin/env python3
"""Check that every test has a Gherkin Scenario, and every Scenario a test.

TEMPORARY: a local stand-in for cat-harness `check:test-gherkin`, which had
not landed when this was written (2026-11-06). When it lands in a pinned
cat-harness, replace this Tool with it and delete this folder.

The owner's rule (2026-11-06): a test should always have a Gherkin. The
`.feature` files in test/features/ are the specification, one per test-plan
case; the tests are the binding. Each Scenario names the test(s) that run it
in a tag:

    @test:<path>::<test>

where <test> is the Rust function name, the Kotlin backtick name, or the
TypeScript `run(...)` name, each whitespace run written as `_` (a Gherkin
tag ends at whitespace). A Scenario that is a WHO-ITB GITB test case (plan
who-itb-agreement) is tagged instead

    @itb:<suite id>/<testcase id>

as the suite at the commit references/who-itb cites names them. A Scenario
no test runs yet is tagged `@manual`, and says why in a comment.

Fails when:
  - a test has no Scenario tagged with it;
  - a `@test:` tag names no test;
  - a Scenario has none of a `@test:` tag, an `@itb:` tag or `@manual`;
  - an `@itb:` tag is not <suite id>/<testcase id>;
  - a test-plan case's `feature` names no file, or a feature file is named
    by no case.

Usage:
    python3 tools/test-gherkin/check_test_gherkin.py [--list]

--list prints every test's tag, one per line, and checks nothing.
"""

import glob
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
FEATURES = ROOT / "test" / "features"
PLANS = ROOT / "test" / "plans"

RUST = ("tools/hcert-rust/**/*.rs", re.compile(r"#\[test\]\s*(?:#\[[^\]]*\]\s*)*fn\s+([A-Za-z0-9_]+)"))
KOTLIN = ("tools/hcert-kotlin/**/*.kt", re.compile(r"@Test\s+(?:@\w+(?:\([^)]*\))?\s+)*fun\s+(?:`([^`]+)`|(\w+))"))
TS = ("tools/conformance-ts/*.ts", re.compile(r"\brun\(\s*[\"`]([^\"`]*)[\"`]"))
TAG = re.compile(r"@test:(\S+)")
ITB = re.compile(r"@itb:(\S*)")
ITB_ID = re.compile(r"[a-z0-9][a-z0-9-]*/[a-z0-9][a-z0-9-]*")


def norm(name):
    return re.sub(r"\s+", "_", name.strip())


def tests():
    """{tag: (path, name)} for every test in the suites."""
    out = {}
    for pattern, rx in (RUST, KOTLIN, TS):
        for f in sorted(glob.glob(str(ROOT / pattern), recursive=True)):
            rel = pathlib.Path(f).relative_to(ROOT).as_posix()
            if "/build/" in rel or "/target/" in rel:
                continue
            for m in rx.finditer(pathlib.Path(f).read_text()):
                name = next(g for g in m.groups() if g)
                tag = "%s::%s" % (rel, norm(name))
                if tag in out:
                    sys.exit("two tests normalise to the same tag: %s" % tag)
                out[tag] = (rel, name)
    return out


def scenarios(path):
    """(line, title, tags) per Scenario / Scenario Outline; feature-level tags are inherited."""
    pending, feature_tags, out = [], [], []
    for i, line in enumerate(path.read_text().splitlines(), 1):
        s = line.strip()
        if s.startswith("@"):
            pending += s.split("#")[0].split() if " #" in s else s.split()
        elif re.match(r"(Feature|Rule):", s):
            if s.startswith("Feature:"):
                feature_tags = pending
            pending = []
        elif re.match(r"(Scenario|Scenario Outline|Example|Scenario Template):", s):
            out.append((i, s, feature_tags + pending))
            pending = []
        elif s and not s.startswith("#"):
            pass
    return out


def main():
    all_tests = tests()
    if "--list" in sys.argv:
        for t in all_tests:
            print("@test:" + t)
        return
    problems, covered = [], set()
    files = sorted(FEATURES.glob("**/*.feature"))
    for f in files:
        rel = f.relative_to(ROOT).as_posix()
        for line, title, tags in scenarios(f):
            refs = [m.group(1) for t in tags for m in [TAG.match(t)] if m]
            itbs = [m.group(1) for t in tags for m in [ITB.match(t)] if m]
            for i in itbs:
                if not ITB_ID.fullmatch(i):
                    problems.append("%s:%d: @itb:%s is not <suite id>/<testcase id>" % (rel, line, i))
            if not refs and not itbs and "@manual" not in tags:
                problems.append("%s:%d: %s has no @test: or @itb: tag and is not @manual" % (rel, line, title))
            for r in refs:
                if r not in all_tests:
                    problems.append("%s:%d: @test:%s names no test" % (rel, line, r))
                covered.add(r)
    for t in all_tests:
        if t not in covered:
            problems.append("%s has no Scenario tagged @test:%s" % (all_tests[t][0], t))
    named = set()
    for p in sorted(PLANS.glob("*.test-plan.json")):
        for case in json.loads(p.read_text())["testCases"]:
            feat = case.get("feature")
            if not feat:
                problems.append("%s: case %s has no feature" % (p.name, case["id"]))
            elif not (ROOT / feat).is_file():
                problems.append("%s: case %s's feature %s is not a file" % (p.name, case["id"], feat))
            else:
                named.add(feat)
    for f in files:
        rel = f.relative_to(ROOT).as_posix()
        if rel not in named:
            problems.append("%s is the feature of no test-plan case" % rel)
    if problems:
        print("\n".join(problems))
        sys.exit("%d problem(s): every test needs a Gherkin Scenario (test/features/)" % len(problems))
    print("%d tests, each with a Scenario, in %d feature files" % (len(all_tests), len(files)))


if __name__ == "__main__":
    main()
