#!/usr/bin/env bash
# check-sync.sh — validate that skill metadata stays in sync across the repo.
#
# Checks:
#   1. skills.sh.json groupings reference exactly the skill directories in skills/
#   2. every SKILL.md frontmatter name matches its directory and has a description
#   3. every evals/evals.json skill_name matches its directory
#   4. README.md mentions every skill name
#   5. plugin.json exists with a valid Agent Plugins manifest
#
# Usage: ./scripts/check-sync.sh   (exit 0 = all good, 1 = problems found)

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

python3 - "$REPO_ROOT" << 'PYEOF' || PY_FAIL=1
import json, os, re, sys

root = sys.argv[1]
skills_dir = os.path.join(root, "skills")
dirs = sorted(d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d)))
problems = []

# 1. skills.sh.json groupings
grouping_path = os.path.join(root, "skills.sh.json")
try:
    with open(grouping_path) as f:
        grouping = json.load(f)
    grouped = [s for g in grouping.get("groupings", []) for s in g.get("skills", [])]
    if sorted(grouped) != dirs:
        problems.append(f"skills.sh.json groupings do not match skills/ dirs: grouped={grouped} dirs={dirs}")
except FileNotFoundError:
    problems.append("skills.sh.json missing")

# 2. SKILL.md frontmatter
for d in dirs:
    path = os.path.join(skills_dir, d, "SKILL.md")
    if not os.path.isfile(path):
        problems.append(f"{d}: SKILL.md missing")
        continue
    text = open(path).read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        problems.append(f"{d}: SKILL.md has no frontmatter")
        continue
    fm = m.group(1)
    name_m = re.search(r"^name:\s*(\S+)\s*$", fm, re.M)
    desc_m = re.search(r"^description:\s*(.+)$", fm, re.M)
    if not name_m or name_m.group(1) != d:
        problems.append(f"{d}: frontmatter name does not match directory")
    if not desc_m or not desc_m.group(1).strip():
        problems.append(f"{d}: frontmatter description missing or empty")

# 3. evals skill_name
for d in dirs:
    path = os.path.join(skills_dir, d, "evals", "evals.json")
    if not os.path.isfile(path):
        problems.append(f"{d}: evals/evals.json missing")
        continue
    data = json.load(open(path))
    if data.get("skill_name") != d:
        problems.append(f"{d}: evals skill_name mismatch ({data.get('skill_name')})")

# 4. README mentions every skill name
readme = open(os.path.join(root, "README.md")).read()
for d in dirs:
    if d not in readme:
        problems.append(f"README.md does not mention {d}")

# 5. plugin.json manifest
plugin_path = os.path.join(root, "plugin.json")
try:
    plugin = json.load(open(plugin_path))
    for field in ("$schema", "name", "version"):
        if not plugin.get(field):
            problems.append(f"plugin.json missing {field}")
    if plugin.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        problems.append("plugin.json $schema is not the Agent Plugins 1.0.0 canonical identifier")
    if plugin.get("name") != "dengskills":
        problems.append("plugin.json name is not 'dengskills'")
    if plugin.get("homepage") and "frontendguide.dev" not in plugin.get("homepage", ""):
        problems.append("plugin.json homepage does not point at frontendguide.dev")
    if sorted(d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))) != dirs:
        pass
except FileNotFoundError:
    problems.append("plugin.json missing")

for p in problems:
    print(p)
sys.exit(1 if problems else 0)
PYEOF
check "${PY_FAIL:-0}" "skill metadata is in sync (groupings, frontmatter, evals, README, plugin.json)"

exit $FAIL
