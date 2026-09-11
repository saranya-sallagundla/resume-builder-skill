# Contributing

## Most-wanted contributions
1. **Playbooks** for roles or markets not yet covered (open a "New playbook or market" issue first).
2. **Rubric evidence** — real before/after scores, ATS behaviour, recruiter feedback (use the "Rubric change" issue).
3. **Scorer parity** — `scripts/score_resume.py` and `web/index.html` must produce identical numbers; fixes to either need the other updated.

## Ground rules
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
