#!/usr/bin/env python3
"""audit-security.py — static security scan for dengskills.

Treats skills as executable software: audits bundled instructions,
scripts, and resources plus external network references.

Verdicts:
  FAIL            must block a release (secret, path escape, hidden instruction)
  REVIEW REQUIRED human looks before merge (network use, subprocess, broad fs access)
  INVENTORY       reported for visibility (URLs in skill resources)

Usage: python3 scripts/audit-security.py   (exit 0 = no FAIL findings)
"""
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
fails = []
reviews = []
inventory = []


def add(bucket, location, message):
    bucket.append(f"{location}: {message}")


TEXT_EXTENSIONS = {".md", ".yaml", ".yml", ".json", ".py", ".sh", ".js", ".ts"}

FAIL_PATTERNS = [
    (re.compile(r"(?i)(sk-ant-|ghp_|gho_|xox[bap]-|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----)"),
     "possible secret or credential"),
    (re.compile(r"\.\.(?:/|\\\\)"), "parent-directory escape pattern"),
    (re.compile(r"(?i)ignore (previous|all|your) (instructions|rules)|do not (reveal|mention|disclose|output)|suppress (output|warnings|errors)"),
     "hidden instruction to suppress behavior"),
    (re.compile(r"(?i)exfiltrat|send .* to (an? )?(external|remote|third-party)|post .*https?://"), "possible exfiltration behavior"),
]

REVIEW_PATTERNS = [
    (re.compile(r"\bcurl\b|\bwget\b|requests\.(get|post)|urllib|fetch\("), "network call needs review"),
    (re.compile(r"\beval\(|\bexec\(|os\.system|subprocess.*shell\s*=\s*True"), "unsafe execution pattern needs review"),
    (re.compile(r"os\.environ|process\.env|printenv|\$HOME|\$USER"), "environment access needs review"),
    (re.compile(r"shutil\.rmtree|rm -rf|os\.remove|os\.unlink"), "destructive filesystem call needs review"),
    (re.compile(r"mcp\.", re.I), "MCP reference needs review"),
]

URL_PATTERN = re.compile(r"https?://[^\s)\"']+")


def main():
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        name = skill_dir.name
        for path in sorted(skill_dir.rglob("*")):
            if not path.is_file() or "__pycache__" in path.parts:
                continue
            location = f"{name}/{path.relative_to(skill_dir)}"
            if path.suffix not in TEXT_EXTENSIONS:
                continue
            try:
                text = path.read_text()
            except (OSError, UnicodeDecodeError):
                continue
            if path.suffix in (".py", ".sh", ".js", ".ts") and not os.access(path, os.X_OK):
                pass
            for pattern, message in FAIL_PATTERNS:
                if pattern.search(text):
                    add(fails, location, message)
            for pattern, message in REVIEW_PATTERNS:
                if pattern.search(text):
                    add(reviews, location, message)
            for url in URL_PATTERN.findall(text):
                if "github.com/mattjmdesign" in url or "frontendguide.dev" in url:
                    continue
                add(inventory, location, f"external URL: {url}")

    # Symlinks must not escape the plugin root (Agent Plugins path containment).
    for path in SKILLS_DIR.rglob("*"):
        if path.is_symlink() and ROOT not in path.resolve().parents:
            add(fails, str(path.relative_to(ROOT)), "symlink escapes plugin root")
    for manifest in (ROOT / ".codex-plugin" / "plugin.json", ROOT / ".claude-plugin" / "plugin.json"):
        if manifest.is_file() and manifest.is_symlink() and ROOT not in manifest.resolve().parents:
            add(fails, str(manifest.relative_to(ROOT)), "symlink escapes plugin root")

    # Executables outside scripts/ get flagged for review.
    for path in SKILLS_DIR.rglob("*"):
        if path.is_file() and os.access(path, os.X_OK):
            if "scripts" not in path.relative_to(SKILLS_DIR).parts:
                add(reviews, str(path.relative_to(SKILLS_DIR)), "executable outside scripts/")

    print(f"FAIL findings: {len(fails)}")
    for item in fails:
        print(f"  FAIL {item}")
    print(f"REVIEW findings: {len(reviews)}")
    for item in reviews:
        print(f"  REVIEW {item}")
    print(f"URL inventory: {len(inventory)}")
    for item in sorted(set(inventory)):
        print(f"  URL {item}")
    return 1 if fails else 0


sys.exit(main())
