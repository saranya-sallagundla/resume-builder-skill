"""web/index.html is the whole product, so CI checks the parts that break silently.

The interview skill bank is embedded as strict JSON between markers precisely so this test can
read it without running any JavaScript. Keep it that way: no comments, no trailing commas, no
single quotes inside the marked block.
"""
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = (ROOT / "web" / "index.html").read_text(encoding="utf-8")

DOMAINS = {"cloud", "swe", "data", "itsm", "pm", "biz", "soft"}
# a "tool" is something a team could choose not to use, so it can be argued against;
# a "practice" can only be done well or badly. The question templates branch on this.
KINDS = {"tool", "practice"}


def bank() -> dict:
    m = re.search(r"/\*BANK-START\*/(.*?)/\*BANK-END\*/", PAGE, re.S)
    assert m, "skill bank markers missing from web/index.html"
    return json.loads(m.group(1))


def test_bank_is_valid_json_and_big_enough():
    data = bank()
    assert data["version"] >= 1
    assert len(data["skills"]) >= 80, "skill bank v1 is meant to cover ~80 skills across domains"


def test_bank_reviewed_date_is_sane():
    reviewed = date.fromisoformat(bank()["reviewed"])
    assert reviewed <= date.today(), "reviewed date is in the future"


def test_every_skill_is_complete():
    for s in bank()["skills"]:
        where = s.get("n", "<unnamed>")
        assert s.get("n"), "a skill has no name"
        assert s["d"] in DOMAINS, f"{where}: unknown domain {s['d']!r}"
        assert s["k"] in KINDS, f"{where}: unknown kind {s.get('k')!r}"
        assert isinstance(s["a"], list), f"{where}: aliases must be a list"
        # the probe and the strong-answer note are what keep generated questions specific
        assert len(s["p"]) > 15, f"{where}: probe is too thin to generate a real question"
        assert len(s["s"]) > 25, f"{where}: strong-answer note is too thin to be useful"
        assert not s["p"].endswith("."), f"{where}: probe is a phrase, not a sentence"


def test_aliases_are_lowercase_and_unambiguous():
    seen: Counter = Counter()
    for s in bank()["skills"]:
        for a in s["a"]:
            assert a == a.lower(), f"{s['n']}: alias {a!r} must be lowercase — matching lowercases the text"
            seen[a] += 1
        assert s["n"].lower() not in s["a"], f"{s['n']}: name repeated in aliases, it is matched already"
    dupes = [a for a, c in seen.items() if c > 1]
    assert not dupes, f"aliases shared by two skills would double-count: {dupes}"


def test_every_domain_is_represented():
    got = {s["d"] for s in bank()["skills"]}
    assert got == DOMAINS, f"missing coverage for {DOMAINS - got}"


def test_no_duplicate_element_ids():
    ids = re.findall(r'\sid="([^"]+)"', PAGE)
    dupes = [i for i, c in Counter(ids).items() if c > 1]
    assert not dupes, f"duplicate element ids break getElementById: {dupes}"


def test_every_room_in_the_staircase_resolves():
    """A staircase link either opens a real view or the honest 'coming' page — never nothing."""
    hrefs = set(re.findall(r'href="#/([^"]*)"', PAGE))
    views = set(re.findall(r'id="view-([a-z]+)"', PAGE))
    for href in hrefs:
        if not href or href.startswith("soon/"):
            continue
        assert href in views, f"#/{href} is linked but there is no view-{href} section"
