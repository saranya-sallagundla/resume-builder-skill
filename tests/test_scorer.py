"""Rubric scorer behaves per docs/ats-scoring.md and guards against regressions."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from score_resume import score, extract_keywords, bullets_of  # noqa: E402

JD = (ROOT / "examples" / "sample_jd.md").read_text()
GOOD = (ROOT / "examples" / "sample_resume.md").read_text()
WEAK = """# Someone
Objective: seeking a challenging role

## Experience
- Responsible for mainframe support
- Helped with batch jobs
- Worked on incidents
- Passionate team player with proven track record
"""


def test_extract_keywords_finds_tools():
    kws = extract_keywords(JD)
    joined = " ".join(kws)
    for k in ["aws", "kubernetes", "pagerduty", "rca"]:
        assert k in joined


def test_good_resume_scores_high():
    assert score(GOOD, JD).total >= 80


def test_weak_resume_scores_low():
    s = score(WEAK, JD)
    assert s.total < 40
    assert s.quantification == 0
    assert s.humanization <= 3
    assert "responsible for" in s.details["fluff_hits"]


def test_score_is_deterministic():
    assert score(GOOD, JD).total == score(GOOD, JD).total


def test_page_count_override():
    assert score(GOOD, JD, pages=2).length_layout == 5
    assert score(GOOD, JD, pages=3).length_layout == 0


def test_bullets_parse():
    assert len(bullets_of(GOOD)) >= 10


def test_regression_gate():
    """CI fails if the sample resume ever drops below this floor after a rubric change."""
    assert score(GOOD, JD).total >= 85
