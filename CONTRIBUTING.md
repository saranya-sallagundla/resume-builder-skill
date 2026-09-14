# Contributing

## Most-wanted contributions
1. **Playbooks** for roles or markets not yet covered (open a "New playbook or market" issue first).
2. **Rubric evidence** — real before/after scores, ATS behaviour, recruiter feedback (use the "Rubric change" issue).
3. **Scorer parity** — `scripts/score_resume.py` and `web/index.html` must produce identical numbers; fixes to either need the other updated.

## Ground rules
- **Originality pledge.** By opening a PR you confirm the content is your own work (or public-domain / openly licensed with attribution) and you license it under MIT. Questions, scripts and checklists copied from other sites, books or question banks are closed.
- **Data sources.** Salary bands and market figures come only from official or openly published sources, cited with a URL and date, and never from scraping sites that forbid it. CI rejects data rows without a source and date.
- **No third-party marks.** Do not add company names, logos or brand assets that are not ours.
- Nothing in `skill/` may encourage fabricating employers, dates, titles, certifications, team settings or metrics. PRs that weaken the truth rule are closed.
- `skill/references/*.md` and `docs/*.md` are mirrors; edit under `skill/`, then `make sync-docs`.
- Keep `skill/SKILL.md` under 500 lines — push detail into `references/`.
- Every PR must keep the sample-resume regression gate green (`make score` ≥ 85).

## Local setup
```bash
pip install -r requirements-dev.txt
pre-commit install
make test && make build
```
