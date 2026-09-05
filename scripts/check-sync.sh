#!/usr/bin/env bash
# check-sync.sh — validate that skill metadata stays in sync across the repo.
#
# Checks:
#   1. skills.sh.json groupings reference exactly the skill directories in skills/
#   2. every SKILL.md frontmatter name matches its directory and has a description
#   3. every evals/evals.json skill_name matches its directory
#   4. README.md mentions every skill name
#   5. plugin.json exists with a valid Agent Plugins manifest
#   6. .claude-plugin/plugin.json exists and agrees with plugin.json (Claude Code)
#   7. .claude-plugin/marketplace.json lists the plugin at the repo root
#
# Usage: ./scripts/check-sync.sh   (exit 0 = all good, 1 = problems found)
#
# If the `claude` CLI is on PATH, both Claude Code manifests are additionally
# validated with `claude plugin validate --strict`.

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

# Portable skill references and invocation metadata.
for d in dirs:
    base = os.path.join(skills_dir, d)
    ui_path = os.path.join(base, "agents", "openai.yaml")
    if not os.path.isfile(ui_path):
        problems.append(f"{d}: agents/openai.yaml missing")
    else:
        ui = open(ui_path).read()
        if f"${d}" not in ui:
            problems.append(f"{d}: default prompt does not invoke this skill")
    for directory, _, files in os.walk(base):
        for filename in files:
            if not filename.endswith(".md"):
                continue
            path = os.path.join(directory, filename)
            body = open(path).read()
            for name in re.findall(r"\$([a-z][a-z0-9]*(?:-[a-z0-9]+)*)", body):
                if name not in dirs and name not in {"schema", "type", "value", "description", "extensions"}:
                    problems.append(f"{d}: unresolved skill invocation ${name} in {filename}")
            for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", body):
                if re.match(r"(?:[a-z]+:|#|/)", link):
                    continue
                target = link.split("#")[0]
                if target and not os.path.exists(os.path.join(directory, target)):
                    problems.append(f"{d}: broken local reference {link} in {filename}")
    eval_path = os.path.join(base, "evals", "evals.json")
    if os.path.isfile(eval_path):
        cases = json.load(open(eval_path)).get("evals", [])
        ids = [case.get("id") for case in cases]
        if len(ids) != len(set(ids)) or not cases:
            problems.append(f"{d}: empty evaluations or duplicate IDs")
        if any(not case.get("prompt") or not case.get("assertions") for case in cases):
            problems.append(f"{d}: evaluations need prompts and assertions")

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

# 6. Claude Code plugin manifest agrees with the portable manifest
cc_path = os.path.join(root, ".claude-plugin", "plugin.json")
try:
    cc = json.load(open(cc_path))
except FileNotFoundError:
    cc = None
    problems.append(".claude-plugin/plugin.json missing (Claude Code will not load this repo as a plugin)")
except json.JSONDecodeError as e:
    cc = None
    problems.append(f".claude-plugin/plugin.json is not valid JSON: {e}")

if cc is not None:
    if cc.get("name") != "dengskills":
        problems.append(".claude-plugin/plugin.json name is not 'dengskills'")
    if not re.fullmatch(r"[a-z][a-z0-9]*(-[a-z0-9]+)*", cc.get("name", "")):
        problems.append(".claude-plugin/plugin.json name is not kebab-case")
    if not re.fullmatch(r"\d+\.\d+\.\d+(-[0-9A-Za-z.-]+)?", cc.get("version", "")):
        problems.append(".claude-plugin/plugin.json version is not semver MAJOR.MINOR.PATCH")
    if "$schema" in cc:
        problems.append(".claude-plugin/plugin.json must not carry the Agent Plugins $schema")
    for field in ("version", "homepage", "repository", "license"):
        if plugin.get(field) != cc.get(field):
            problems.append(f"plugin.json and .claude-plugin/plugin.json disagree on {field}")
    if not cc.get("description"):
        problems.append(".claude-plugin/plugin.json description missing")

# 7. Claude Code marketplace manifest points at the repo root
mk_path = os.path.join(root, ".claude-plugin", "marketplace.json")
try:
    mk = json.load(open(mk_path))
except FileNotFoundError:
    mk = None
    problems.append(".claude-plugin/marketplace.json missing (repo is not self-installable)")
except json.JSONDecodeError as e:
    mk = None
    problems.append(f".claude-plugin/marketplace.json is not valid JSON: {e}")

if mk is not None and cc is not None:
    entries = mk.get("plugins", [])
    entry = next((p for p in entries if p.get("name") == cc.get("name")), None)
    if entry is None:
        problems.append(f"marketplace.json has no entry named {cc.get('name')}")
    elif entry.get("source") not in ("./", "."):
        problems.append("marketplace.json entry source must be './' (the repo is the plugin)")
    mk_version = (mk.get("metadata") or {}).get("version")
    if mk_version != cc.get("version"):
        problems.append("marketplace.json metadata.version does not match the plugin version")

for p in problems:
    print(p)
sys.exit(1 if problems else 0)
PYEOF
check "${PY_FAIL:-0}" "skill metadata is in sync (groupings, frontmatter, evals, README, both manifests)"

if [ "${1:-}" != "--metadata-only" ] && command -v claude > /dev/null 2>&1; then
  claude plugin validate "$REPO_ROOT" --strict > /dev/null 2>&1
  check "$?" "claude plugin validate --strict (.claude-plugin/plugin.json)"
  claude plugin validate "$REPO_ROOT/.claude-plugin/marketplace.json" --strict > /dev/null 2>&1
  check "$?" "claude plugin validate --strict (.claude-plugin/marketplace.json)"
else
  echo "SKIP Claude runtime validation (metadata-only or CLI unavailable)"
fi

exit $FAIL
