#!/usr/bin/env python3
"""validate-repo.py — deterministic repository validation for dengskills.

Checks (exit 0 = all good, 1 = problems found):
  1. skills.sh.json groupings reference exactly the skill directories in skills/
  2. every SKILL.md frontmatter name matches its directory and has a description
  3. every evals/evals.json skill_name matches its directory
  4. README.md mentions every skill name
  5. plugin.json exists with a valid Agent Plugins manifest
  6. .claude-plugin/plugin.json exists and agrees with plugin.json (Claude Code)
  7. .claude-plugin/marketplace.json lists the plugin at the repo root
  8. .codex-plugin/plugin.json exists and agrees with plugin.json (Codex)
  9. every skills/<name>/evals/triggers.json exists with a valid routing suite

Usage: python3 scripts/validate-repo.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
problems = []


def fail(message):
    problems.append(message)


def main():
    dirs = sorted(p.name for p in SKILLS_DIR.iterdir() if p.is_dir())

    # 1. skills.sh.json groupings
    try:
        grouping = json.loads((ROOT / "skills.sh.json").read_text())
        grouped = [s for g in grouping.get("groupings", []) for s in g.get("skills", [])]
        if sorted(grouped) != dirs:
            fail(f"skills.sh.json groupings do not match skills/ dirs: grouped={grouped} dirs={dirs}")
    except FileNotFoundError:
        fail("skills.sh.json missing")
    except json.JSONDecodeError as error:
        fail(f"skills.sh.json is not valid JSON: {error}")

    # 2. SKILL.md frontmatter
    for name in dirs:
        path = SKILLS_DIR / name / "SKILL.md"
        if not path.is_file():
            fail(f"{name}: SKILL.md missing")
            continue
        text = path.read_text()
        match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not match:
            fail(f"{name}: SKILL.md has no frontmatter")
            continue
        frontmatter = match.group(1)
        name_match = re.search(r"^name:\s*(\S+)\s*$", frontmatter, re.M)
        desc_match = re.search(r"^description:\s*(.+)$", frontmatter, re.M)
        if not name_match or name_match.group(1) != name:
            fail(f"{name}: frontmatter name does not match directory")
        if not desc_match or not desc_match.group(1).strip():
            fail(f"{name}: frontmatter description missing or empty")

    # 3. evals skill_name
    for name in dirs:
        path = SKILLS_DIR / name / "evals" / "evals.json"
        if not path.is_file():
            fail(f"{name}: evals/evals.json missing")
            continue
        try:
            data = json.loads(path.read_text())
        except json.JSONDecodeError as error:
            fail(f"{name}: evals/evals.json is not valid JSON: {error}")
            continue
        if data.get("skill_name") != name:
            fail(f"{name}: evals skill_name mismatch ({data.get('skill_name')})")

    # Portable skill references and invocation metadata.
    for name in dirs:
        base = SKILLS_DIR / name
        ui_path = base / "agents" / "openai.yaml"
        if not ui_path.is_file():
            fail(f"{name}: agents/openai.yaml missing")
        elif f"${name}" not in ui_path.read_text():
            fail(f"{name}: default prompt does not invoke this skill")
        for directory, _, files in __import__("os").walk(base):
            for filename in files:
                if not filename.endswith(".md"):
                    continue
                path = Path(directory) / filename
                body = path.read_text()
                for ref in re.findall(r"\$([a-z][a-z0-9]*(?:-[a-z0-9]+)*)", body):
                    if ref not in dirs and ref not in {"schema", "type", "value", "description", "extensions"}:
                        fail(f"{name}: unresolved skill invocation ${ref} in {filename}")
                for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", body):
                    if re.match(r"(?:[a-z]+:|#|/)", link):
                        continue
                    target = link.split("#")[0]
                    if target and not (Path(directory) / target).exists():
                        fail(f"{name}: broken local reference {link} in {filename}")
        eval_path = base / "evals" / "evals.json"
        if eval_path.is_file():
            cases = json.loads(eval_path.read_text()).get("evals", [])
            ids = [case.get("id") for case in cases]
            if len(ids) != len(set(ids)) or not cases:
                fail(f"{name}: empty evaluations or duplicate IDs")
            if any(not case.get("prompt") or not case.get("assertions") for case in cases):
                fail(f"{name}: evaluations need prompts and assertions")

    # 4. README mentions every skill name
    readme = (ROOT / "README.md").read_text()
    for name in dirs:
        if name not in readme:
            fail(f"README.md does not mention {name}")

    # 5. plugin.json manifest
    try:
        plugin = json.loads((ROOT / "plugin.json").read_text())
        for field in ("$schema", "name", "version"):
            if not plugin.get(field):
                fail(f"plugin.json missing {field}")
        if plugin.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
            fail("plugin.json $schema is not the Agent Plugins 1.0.0 canonical identifier")
        if plugin.get("name") != "dengskills":
            fail("plugin.json name is not 'dengskills'")
        if plugin.get("homepage") and "frontendguide.dev" not in plugin.get("homepage", ""):
            fail("plugin.json homepage does not point at frontendguide.dev")
    except FileNotFoundError:
        plugin = {}
        fail("plugin.json missing")
    except json.JSONDecodeError as error:
        plugin = {}
        fail(f"plugin.json is not valid JSON: {error}")

    # 6. Claude Code plugin manifest agrees with the portable manifest
    cc_path = ROOT / ".claude-plugin" / "plugin.json"
    try:
        cc = json.loads(cc_path.read_text())
    except FileNotFoundError:
        cc = None
        fail(".claude-plugin/plugin.json missing (Claude Code will not load this repo as a plugin)")
    except json.JSONDecodeError as error:
        cc = None
        fail(f".claude-plugin/plugin.json is not valid JSON: {error}")

    if cc is not None:
        if cc.get("name") != "dengskills":
            fail(".claude-plugin/plugin.json name is not 'dengskills'")
        if not re.fullmatch(r"[a-z][a-z0-9]*(-[a-z0-9]+)*", cc.get("name", "")):
            fail(".claude-plugin/plugin.json name is not kebab-case")
        if not re.fullmatch(r"\d+\.\d+\.\d+(-[0-9A-Za-z.-]+)?", cc.get("version", "")):
            fail(".claude-plugin/plugin.json version is not semver MAJOR.MINOR.PATCH")
        if "$schema" in cc:
            fail(".claude-plugin/plugin.json must not carry the Agent Plugins $schema")
        for field in ("version", "homepage", "repository", "license"):
            if plugin.get(field) != cc.get(field):
                fail(f"plugin.json and .claude-plugin/plugin.json disagree on {field}")
        if not cc.get("description"):
            fail(".claude-plugin/plugin.json description missing")

    # 7. Claude Code marketplace manifest points at the repo root
    mk_path = ROOT / ".claude-plugin" / "marketplace.json"
    try:
        mk = json.loads(mk_path.read_text())
    except FileNotFoundError:
        mk = None
        fail(".claude-plugin/marketplace.json missing (repo is not self-installable)")
    except json.JSONDecodeError as error:
        mk = None
        fail(f".claude-plugin/marketplace.json is not valid JSON: {error}")

    if mk is not None and cc is not None:
        entries = mk.get("plugins", [])
        entry = next((p for p in entries if p.get("name") == cc.get("name")), None)
        if entry is None:
            fail(f"marketplace.json has no entry named {cc.get('name')}")
        elif entry.get("source") not in ("./", "."):
            fail("marketplace.json entry source must be './' (the repo is the plugin)")
        mk_version = (mk.get("metadata") or {}).get("version")
        if mk_version != cc.get("version"):
            fail("marketplace.json metadata.version does not match the plugin version")

    # 8. Codex plugin manifest agrees with the portable manifest
    cx_path = ROOT / ".codex-plugin" / "plugin.json"
    try:
        cx = json.loads(cx_path.read_text())
    except FileNotFoundError:
        cx = None
        fail(".codex-plugin/plugin.json missing (Codex has no native plugin manifest)")
    except json.JSONDecodeError as error:
        cx = None
        fail(f".codex-plugin/plugin.json is not valid JSON: {error}")

    if cx is not None:
        if cx.get("name") != "dengskills":
            fail(".codex-plugin/plugin.json name is not 'dengskills'")
        if not re.fullmatch(r"[a-z][a-z0-9]*(-[a-z0-9]+)*", cx.get("name", "")):
            fail(".codex-plugin/plugin.json name is not kebab-case")
        if not re.fullmatch(r"\d+\.\d+\.\d+(-[0-9A-Za-z.-]+)?", cx.get("version", "")):
            fail(".codex-plugin/plugin.json version is not semver MAJOR.MINOR.PATCH")
        if "$schema" in cx:
            fail(".codex-plugin/plugin.json must not carry the Agent Plugins $schema")
        for field in ("version", "homepage", "repository", "license"):
            if plugin.get(field) != cx.get(field):
                fail(f"plugin.json and .codex-plugin/plugin.json disagree on {field}")
        if cx.get("skills") != "./skills/":
            fail('.codex-plugin/plugin.json skills pointer is not "./skills/"')
        if not (cx.get("interface") or {}).get("displayName"):
            fail(".codex-plugin/plugin.json interface.displayName missing")

    # 9. routing suites exist and are structurally valid (data only; no model runs)
    for name in dirs:
        path = SKILLS_DIR / name / "evals" / "triggers.json"
        if not path.is_file():
            fail(f"{name}: evals/triggers.json missing")
            continue
        try:
            data = json.loads(path.read_text())
        except json.JSONDecodeError as error:
            fail(f"{name}: evals/triggers.json is not valid JSON: {error}")
            continue
        if data.get("skill_name") != name:
            fail(f"{name}: triggers skill_name mismatch ({data.get('skill_name')})")
        cases = data.get("cases", [])
        ids = [case.get("id") for case in cases]
        if len(cases) < 10 or len(ids) != len(set(ids)):
            fail(f"{name}: triggers need at least 10 uniquely-identified cases")
        for case in cases:
            if not case.get("query"):
                fail(f"{name}: trigger case {case.get('id')} needs a query")
            if "should_trigger" not in case:
                fail(f"{name}: trigger case {case.get('id')} needs should_trigger")
            if not case.get("should_trigger") and not case.get("expected_skill"):
                fail(f"{name}: negative trigger case {case.get('id')} needs expected_skill")
            if case.get("expected_skill") and case["expected_skill"] not in dirs:
                fail(f"{name}: trigger case {case.get('id')} names unknown skill {case['expected_skill']}")

    for problem in problems:
        print(problem)
    return 1 if problems else 0


sys.exit(main())
