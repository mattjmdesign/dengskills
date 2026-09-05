#!/usr/bin/env bash
# check-sync.sh — validate that skill metadata stays in sync across the repo.
#
# Thin wrapper around scripts/validate-repo.py (the source of truth for
# deterministic checks) plus optional `claude plugin validate --strict`
# when the Claude Code CLI is on PATH.
#
# Usage: ./scripts/check-sync.sh [--metadata-only]   (exit 0 = all good, 1 = problems found)

set -u
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
FAIL=0

check() {
  local ok="$1" msg="$2"
  if [ "$ok" = "0" ]; then
    echo "OK   $msg"
  else
    echo "FAIL $msg"
    FAIL=1
  fi
}

python3 "$REPO_ROOT/scripts/validate-repo.py" || PY_FAIL=1
check "${PY_FAIL:-0}" "repository validation (groupings, frontmatter, evals, triggers, README, all manifests)"

if [ "${1:-}" != "--metadata-only" ] && command -v claude > /dev/null 2>&1; then
  claude plugin validate "$REPO_ROOT" --strict > /dev/null 2>&1
  check "$?" "claude plugin validate --strict (.claude-plugin/plugin.json)"
  claude plugin validate "$REPO_ROOT/.claude-plugin/marketplace.json" --strict > /dev/null 2>&1
  check "$?" "claude plugin validate --strict (.claude-plugin/marketplace.json)"
else
  echo "SKIP Claude runtime validation (metadata-only or CLI unavailable)"
fi

exit $FAIL
