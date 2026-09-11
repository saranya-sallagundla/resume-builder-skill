#!/usr/bin/env python3
"""Validate the skill and package skill/ into dist/resume-builder.skill (a zip)."""
import re, sys, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill"
DIST = ROOT / "dist"


def validate() -> list[str]:
    errors = []
    md = SKILL / "SKILL.md"
    if not md.exists():
        return ["skill/SKILL.md missing"]
    text = md.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append("SKILL.md has no YAML frontmatter")
    else:
        fm = m.group(1)
        if not re.search(r"^name:\s*\S+", fm, re.M): errors.append("frontmatter: name missing")
        if not re.search(r"^description:\s*\S+", fm, re.M): errors.append("frontmatter: description missing")
    if len(text.splitlines()) > 500:
        errors.append("SKILL.md exceeds 500 lines — move content to references/")
    for ref in re.findall(r"`references/([\w\-]+\.md)`", text):
        if not (SKILL / "references" / ref).exists():
            errors.append(f"referenced file missing: references/{ref}")
    return errors


def package() -> Path:
    DIST.mkdir(exist_ok=True)
    out = DIST / "resume-builder.skill"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(SKILL.rglob("*")):
            if p.is_file() and "evals" not in p.parts:
                z.write(p, Path("resume-builder") / p.relative_to(SKILL))
    return out


if __name__ == "__main__":
    errs = validate()
    if errs:
        print("\n".join(f"ERROR: {e}" for e in errs)); sys.exit(1)
    print(f"packaged: {package()}")
