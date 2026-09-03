#!/usr/bin/env bash
# bump-version.sh — set the pack version in all three manifests at once.
#
# One version, several client manifests that must never disagree:
#   plugin.json                        Agent Plugins manifest (portable)
#   .claude-plugin/plugin.json         Claude Code plugin manifest
#   .claude-plugin/marketplace.json    metadata.version
#
# Adding another client's manifest? Add it to `paths` below so it bumps too.
#
# Usage:
#   ./scripts/bump-version.sh 1.4.0     set an explicit version
#   ./scripts/bump-version.sh minor     bump major | minor | patch
#   ./scripts/bump-version.sh           print the current version and exit

set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

python3 - "$REPO_ROOT" "${1-}" << 'PYEOF'
import json, re, sys

root, arg = sys.argv[1], sys.argv[2]
paths = {
    "root":        f"{root}/plugin.json",
    "claude":      f"{root}/.claude-plugin/plugin.json",
    "marketplace": f"{root}/.claude-plugin/marketplace.json",
}
manifests = {k: json.load(open(p)) for k, p in paths.items()}

def version_of(key):
    m = manifests[key]
    return m["metadata"]["version"] if key == "marketplace" else m["version"]

current = version_of("claude")
disagree = {k: version_of(k) for k in manifests if version_of(k) != current}
if disagree:
    print(f"warning: manifests disagree before bump — claude={current}, {disagree}", file=sys.stderr)

if not arg:
    print(current)
    sys.exit(0)

if arg in ("major", "minor", "patch"):
    major, minor, patch = (int(x) for x in current.split("."))
    if arg == "major":
        major, minor, patch = major + 1, 0, 0
    elif arg == "minor":
        minor, patch = minor + 1, 0
    else:
        patch += 1
    new = f"{major}.{minor}.{patch}"
elif re.fullmatch(r"\d+\.\d+\.\d+(-[0-9A-Za-z.-]+)?", arg):
    new = arg
else:
    print(f"error: '{arg}' is not a semver version or one of major|minor|patch", file=sys.stderr)
    sys.exit(1)

for key, m in manifests.items():
    if key == "marketplace":
        m["metadata"]["version"] = new
    else:
        m["version"] = new
    with open(paths[key], "w") as f:
        json.dump(m, f, indent=2)
        f.write("\n")

print(f"{current} -> {new}")
print("\nNext:")
print("  1. add the release to CHANGELOG.md")
print("  2. ./scripts/check-sync.sh")
print("  3. git commit -am \"Release v{v}\" && git tag v{v} && git push --follow-tags".format(v=new))
print("\nOptional, for Claude Code consumers:")
print("  claude plugin tag . --push            # also tags dengskills--v%s" % new)
PYEOF
