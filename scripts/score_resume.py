#!/usr/bin/env python3
"""Heuristic resume scorer implementing the 100-point rubric in docs/ats-scoring.md.

Usage:
    python scripts/score_resume.py --resume examples/sample_resume.md --jd examples/sample_jd.md
    python scripts/score_resume.py --resume r.md --jd jd.md --json
    python scripts/score_resume.py --resume r.md --jd jd.md --min-score 70   # exit 1 if below

The web/ scorer mirrors this logic in JavaScript so both produce the same numbers.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path

FLUFF_VERBS = [
    "responsible for", "helped with", "helped", "worked on", "involved in",
    "assisted with", "assisted", "participated in", "tasked with",
]
BANNED_CLICHES = [
    "spearheaded", "leveraged", "leverage", "synergy", "seamlessly", "seamless",
    "passionate", "results-driven", "proven track record", "dynamic", "cutting-edge",
    "go-getter", "think outside the box", "detail-oriented", "team player",
]
STANDARD_HEADERS = ["summary", "skills", "work experience", "experience",
                    "certifications", "education", "projects", "key projects"]
GENERIC = set("""lead senior junior technical management manager engineer analyst developer
responsibilities requirements experience preferred required plus strong looking hands-on
environments clients client large support operations processes reviews coordination""".split())
STOPWORDS = set("""a an and are as at be by for from has have in is it its of on or that the to
with will you your we our this these those their they them experience years year strong
good knowledge ability able work working team teams role roles skills skill required
preferred plus including etc across using use used within must should can may""".split())


@dataclass
class Score:
    keyword_coverage: float = 0
    keyword_placement: float = 0
    title_alignment: float = 0
    parse_safety: float = 10
    quantification: float = 0
    bullet_quality: float = 10
    scope_progression: float = 0
    length_layout: float = 5
    humanization: float = 5
    hygiene: float = 5
    details: dict = field(default_factory=dict)

    @property
    def total(self) -> float:
        return round(sum([
            self.keyword_coverage, self.keyword_placement, self.title_alignment,
            self.parse_safety, self.quantification, self.bullet_quality,
            self.scope_progression, self.length_layout, self.humanization, self.hygiene,
        ]), 1)


def extract_keywords(jd: str, limit: int = 20) -> list[str]:
    """Pull candidate must-have phrases from a JD: capitalised tokens, acronyms, bigrams."""
    text = re.sub(r"[^\w\s\-+/#.]", " ", jd)
    words = text.split()
    counts: dict[str, int] = {}

    def bump(k: str, weight: int = 1) -> None:
        k = k.strip(".,").lower()
        if len(k) < 2 or k in STOPWORDS or k in GENERIC:
            return
        counts[k] = counts.get(k, 0) + weight

    for w in words:
        tool_like = (re.fullmatch(r"[A-Z]{2,}[0-9/-]*", w)                 # ITIL, DB2, CA-7
                     or re.fullmatch(r"[A-Z][a-z]+[A-Z][A-Za-z]+", w)       # ServiceNow, PowerShell
                     or re.search(r"[0-9+#/-]", w) and w[:1].isalpha())      # z/OS, C++, Control-M
        if tool_like:
            bump(w, 3)
        elif re.fullmatch(r"[A-Z][a-z]{2,}", w):
            bump(w, 1)
    for a, b in zip(words, words[1:]):
        if (a.lower() not in STOPWORDS and b.lower() not in STOPWORDS
                and a[:1].isalpha() and b[-1:].isalnum() and a[-1:].isalnum()):
            bump(f"{a} {b}")
    ranked = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return [k for k, _ in ranked[:limit]]


def bullets_of(resume: str) -> list[str]:
    return [ln.strip().lstrip("•-*–· ").strip() for ln in resume.splitlines()
            if re.match(r"^\s*[•\-*–·]\s+\S", ln)]


def score(resume: str, jd: str, keywords: list[str] | None = None,
          pages: int | None = None, target_pages: int = 2) -> Score:
    s = Score()
    r_low = resume.lower()
    kws = [k.lower() for k in (keywords or extract_keywords(jd))]
    if not kws:
        kws = []

    # 1. Keyword coverage (25)
    present = [k for k in kws if k in r_low]
    s.keyword_coverage = round(25 * len(present) / len(kws), 1) if kws else 0
    s.details["keywords"] = kws
    s.details["keywords_missing"] = [k for k in kws if k not in present]

    # 2. Keyword placement (10) — top third of the document
    lines = [ln for ln in resume.splitlines() if ln.strip()]
    top = "\n".join(lines[: max(1, len(lines) // 3)]).lower()
    top_hits = [k for k in present if k in top]
    ratio = len(top_hits) / len(present) if present else 0
    s.keyword_placement = 10 if ratio >= .8 else 6 if ratio >= .6 else 3 if ratio >= .4 else 0

    # 3. Title alignment (5) — first non-empty JD line treated as the title
    title = next((ln.strip() for ln in jd.splitlines() if ln.strip()), "").lower()
    title = re.sub(r"^(job title|title|role)\s*[:\-]\s*", "", title)
    head = "\n".join(lines[:4]).lower()
    if title and title in head:
        s.title_alignment = 5
    elif title and title in r_low:
        s.title_alignment = 3
    s.details["jd_title"] = title

    # 4. Parse safety (10) — markdown/plain-text heuristics
    if re.search(r"^\s*\|.*\|\s*$", resume, re.M):  # markdown table rows
        s.parse_safety -= 3
    found_headers = [h for h in STANDARD_HEADERS if re.search(rf"^\s*#*\s*{h}\s*$", r_low, re.M)]
    if len(found_headers) < 3:
        s.parse_safety -= 2
    if re.search(r"!\[|<img|\.png|\.jpg", r_low):
        s.parse_safety -= 2
    s.parse_safety = max(0, s.parse_safety)

    # 5. Quantification (15)
    bl = bullets_of(resume)
    numbered = [b for b in bl if re.search(r"\d", b)]
    s.quantification = round(15 * len(numbered) / len(bl), 1) if bl else 0
    s.details["bullets_total"] = len(bl)
    s.details["bullets_without_numbers"] = [b for b in bl if not re.search(r"\d", b)]

    # 6. Bullet quality (10)
    penalties = 0
    fluff_hits = []
    for b in bl:
        bl_low = b.lower()
        for f in FLUFF_VERBS:
            if re.search(rf"\b{re.escape(f)}\b", bl_low):
                penalties += 1
                fluff_hits.append(f)
                break
        if len(b) > 220:
            penalties += 1
        if re.search(r"\b(was|were|is|are|been)\s+\w+ed\b", bl_low):
            penalties += 1
    first_words = [b.split()[0].lower() for b in bl if b.split()]
    penalties += sum(1 for a, b in zip(first_words, first_words[1:]) if a == b)
    s.bullet_quality = max(0, 10 - penalties)
    s.details["fluff_hits"] = sorted(set(fluff_hits))

    # 7. Scope & progression (10) — count scope signals near the top
    scope_pat = r"\b(\d+\+?\s*(people|person|engineers?|members?|users?|servers?|clients?|tickets?|incidents?|apps?|applications?|systems?|regions?|sites?|stores?|accounts?)|\$\s?\d|\d+\s?(k|m|lakh|crore|%))"
    scope_hits = len(re.findall(scope_pat, r_low))
    s.scope_progression = 10 if scope_hits >= 6 else 6 if scope_hits >= 3 else 3 if scope_hits >= 1 else 0
    s.details["scope_signals"] = scope_hits

    # 8. Length & layout (5)
    if pages is not None:
        s.length_layout = 5 if pages == target_pages else 0
    else:
        # ~55 non-empty lines per page in a dense resume
        est = max(1, round(len(lines) / 55))
        s.length_layout = 5 if est == target_pages else 2 if abs(est - target_pages) == 1 else 0
        s.details["estimated_pages"] = est

    # 9. Humanization (5)
    cliche_hits = [c for c in BANNED_CLICHES if re.search(rf"\b{re.escape(c)}\b", r_low)]
    s.humanization = max(0, 5 - len(cliche_hits))
    s.details["cliche_hits"] = cliche_hits

    # 10. Hygiene (5) — date-format consistency + double spaces
    date_styles = set()
    if re.search(r"\b\d{2}/\d{4}\b", resume): date_styles.add("mm/yyyy")
    if re.search(r"\b[A-Z][a-z]{2,8}\.? \d{4}\b", resume): date_styles.add("Mon yyyy")
    if re.search(r"\b\d{4}-\d{2}\b", resume): date_styles.add("yyyy-mm")
    issues = max(0, len(date_styles) - 1) + len(re.findall(r"\S  +\S", resume))
    s.hygiene = max(0, 5 - issues)
    s.details["date_styles"] = sorted(date_styles)
    return s


def report(s: Score) -> str:
    def f(v): return f"{v:g}"
    out = [
        f"## ATS & recruiter match: {s.total:g} / 100",
        f"Keyword coverage {f(s.keyword_coverage)}/25 · Placement {f(s.keyword_placement)}/10 · "
        f"Title {f(s.title_alignment)}/5 · Parse safety {f(s.parse_safety)}/10",
        f"Quantification {f(s.quantification)}/15 · Bullet quality {f(s.bullet_quality)}/10 · "
        f"Scope & progression {f(s.scope_progression)}/10",
        f"Length & layout {f(s.length_layout)}/5 · Humanization {f(s.humanization)}/5 · Hygiene {f(s.hygiene)}/5",
        "",
    ]
    if s.details.get("keywords_missing"):
        out.append("Missing keywords: " + ", ".join(s.details["keywords_missing"]))
    if s.details.get("bullets_without_numbers"):
        out.append(f"Bullets without numbers: {len(s.details['bullets_without_numbers'])}")
    if s.details.get("fluff_hits"):
        out.append("Fluff verbs: " + ", ".join(s.details["fluff_hits"]))
    if s.details.get("cliche_hits"):
        out.append("Clichés: " + ", ".join(s.details["cliche_hits"]))
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--resume", required=True, type=Path)
    ap.add_argument("--jd", required=True, type=Path)
    ap.add_argument("--pages", type=int, help="actual page count if known")
    ap.add_argument("--target-pages", type=int, default=2)
    ap.add_argument("--min-score", type=float, help="exit 1 if total is below this")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    s = score(a.resume.read_text(), a.jd.read_text(), pages=a.pages, target_pages=a.target_pages)
    if a.json:
        d = asdict(s); d["total"] = s.total
        print(json.dumps(d, indent=2))
    else:
        print(report(s))
    if a.min_score is not None and s.total < a.min_score:
        print(f"\nFAIL: {s.total} < {a.min_score}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
