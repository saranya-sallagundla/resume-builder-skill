"""The skill must stay loadable: frontmatter present, references resolvable, size bounded."""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_skill import validate  # noqa: E402

SKILL = ROOT / "skill"


def test_skill_validates():
    assert validate() == []


def test_description_is_pushy_enough():
    fm = re.match(r"^---\n(.*?)\n---", (SKILL / "SKILL.md").read_text(), re.S).group(1)
    desc = re.search(r"^description:\s*(.+)$", fm, re.M).group(1)
    for trigger in ["resume", "job description", "JD", "review"]:
        assert trigger.lower() in desc.lower(), f"description should mention '{trigger}'"


def test_every_reference_is_pointed_to():
    text = (SKILL / "SKILL.md").read_text()
    for ref in (SKILL / "references").glob("*.md"):
        assert f"references/{ref.name}" in text, f"{ref.name} exists but SKILL.md never points to it"


def test_truth_rule_present():
    text = (SKILL / "SKILL.md").read_text().lower()
    assert "never misattribute" in text
    assert "fabricat" in text


def test_evals_well_formed():
    data = json.loads((SKILL / "evals" / "evals.json").read_text())
    assert data["skill_name"] == "resume-builder"
    assert len(data["evals"]) >= 5
    for e in data["evals"]:
        assert e["prompt"] and e["expected_output"]


def test_docs_mirror_references():
    for ref in (SKILL / "references").glob("*.md"):
        mirror = ROOT / "docs" / ref.name
        assert mirror.exists(), f"docs/{ref.name} missing — run `make sync-docs`"
        assert mirror.read_text() == ref.read_text(), f"docs/{ref.name} out of sync — run `make sync-docs`"
