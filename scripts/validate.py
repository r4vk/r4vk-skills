#!/usr/bin/env python3
"""Check the marketplace. With --base REF also require a version bump for changed plugins."""
import argparse, json, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
errors = []


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)


ap = argparse.ArgumentParser()
ap.add_argument("--base")
base = ap.parse_args().base
if base and git("cat-file", "-e", f"{base}^{{commit}}").returncode:
    sys.exit(f"base commit not found: {base}")

entries = load(ROOT / ".claude-plugin" / "marketplace.json")["plugins"]
listed = {e["name"] for e in entries}
present = {p.name for p in (ROOT / "plugins").iterdir() if p.is_dir()}
if listed != present or len(listed) != len(entries):
    errors.append(f"marketplace entries {sorted(listed)} != plugin folders {sorted(present)}")

for e in entries:
    name = e["name"]
    folder = ROOT / "plugins" / name
    if e["source"] != f"./plugins/{name}":
        errors.append(f"{name}: wrong source")
    if "version" in e:
        errors.append(f"{name}: keep version only in plugin.json")
    if not (folder / ".claude-plugin" / "plugin.json").is_file():
        errors.append(f"{name}: no plugin.json")
        continue
    manifest = load(folder / ".claude-plugin" / "plugin.json")
    version = manifest.get("version", "")
    if manifest.get("name") != name:
        errors.append(f"{name}: name differs in plugin.json")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append(f"{name}: bad version {version!r}")
    skills = list(folder.glob("skills/*/SKILL.md"))
    if not skills:
        errors.append(f"{name}: no skill")
    for skill in skills:
        text = skill.read_text(encoding="utf-8")
        m = re.match(r"---\nname: ([a-z0-9-]+)\ndescription: (.+)\n---\n", text)
        if not m or m.group(1) != skill.parent.name:
            errors.append(f"{skill}: bad frontmatter")
        elif len(m.group(2)) > 1024 or re.search(r"[<>]", m.group(2)):
            errors.append(f"{skill}: description too long or has angle brackets")
        if len(text.splitlines()) >= 500:
            errors.append(f"{skill}: 500 lines or more")
    if base and git("diff", "--quiet", base, "--", f"plugins/{name}").returncode:
        old = git("show", f"{base}:plugins/{name}/.claude-plugin/plugin.json")
        if old.returncode == 0:
            before = json.loads(old.stdout)["version"]
            if tuple(map(int, version.split("."))) <= tuple(map(int, before.split("."))):
                errors.append(f"{name}: files changed, raise version above {before}")

print("\n".join(errors) if errors else "marketplace OK")
sys.exit(1 if errors else 0)
