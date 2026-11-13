#!/usr/bin/env bash
# Every test has a Gherkin Scenario, and every Scenario names a test: the
# harness's check:test-gherkin (cat-harness-tools), run with what is this
# repository's own.
#
#  - The TypeScript conformance suites run their tests through their own
#    runner, run("STT-… title", …), in plain modules: declared with
#    --js-test-call.
#  - The who-itb-agreement Scenarios bind WHO-ITB GITB test cases by
#    @itb:<suite>/<testcase>. Those resolve against the WHO-ITB test suites
#    at the commit references/who-itb cites, fetched here to a temporary
#    directory and never copied into the repository (WHO-ITB has no licence).
#    --itb <dir> uses a checkout already on disk instead.
#
# Usage: tools/test-gherkin/check_test_gherkin.sh [--itb DIR] [-- extra check:test-gherkin args]
set -euo pipefail
root="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$root"
itb=""
if [[ "${1:-}" == "--itb" ]]; then itb="$2"; shift 2; fi
[[ "${1:-}" == "--" ]] && shift
if [[ -z "$itb" ]]; then
  url="$(python3 -Ic 'import json; print(json.load(open("references/who-itb.json"))["URL"])')"
  sha="${url##*/tree/}"
  repo="${url%%/tree/*}"
  [[ "$sha" =~ ^[0-9a-f]{40}$ ]] || { echo "references/who-itb.json: URL does not name a commit: $url" >&2; exit 2; }
  itb="$(mktemp -d)"
  trap 'rm -rf "$itb"' EXIT
  git -C "$itb" init -q
  git -C "$itb" fetch -q --depth 1 --filter=blob:none "$repo.git" "$sha"
  git -C "$itb" checkout -q FETCH_HEAD -- testsuites
fi
exec bun run cat check:test-gherkin -- \
  --js-test-call tools/conformance-ts/suite.ts=run \
  --js-test-call tools/conformance-ts/cross.ts=run \
  --itb "$itb" "$@"
