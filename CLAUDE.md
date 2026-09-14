# CLAUDE.md — standing instructions for this repo

## What this project is
An open-source Claude skill that builds ATS-optimized resumes, plus a full DevOps toolchain around it. Two audiences: job seekers using the skill, and recruiters/hiring managers looking at the repo as evidence of engineering practice.

## Layout
- `skill/` — the Claude skill. `SKILL.md` is the process; `references/*.md` hold the detail. Keep SKILL.md under 500 lines.
- `docs/` — mirrors of `skill/references/*.md` plus ADRs. Edit under `skill/`, then run `make sync-docs`. A test enforces that they match.
- `scripts/score_resume.py` — the 100-point rubric in Python. Reference implementation.
- `web/index.html` — the same rubric in JavaScript, single file, no backend, no dependencies.
- `tests/` — pytest. `examples/sample_resume.md` is a golden file; its score must stay ≥ 85.
- `k8s/`, `terraform/`, `Dockerfile`, `.github/workflows/` — the DevOps layer.

## Rules that must not be broken
1. **Never weaken the truth rule.** Nothing in `skill/` may encourage fabricating employers, dates, titles, certifications, team settings, or metrics. Real hands-on work goes in a Key Projects section; it never gets placed under an employer where it didn't happen.
2. **Scorer parity.** `scripts/score_resume.py` and `web/index.html` must produce identical numbers for the same input. Change one, change the other.
3. **Docs mirror.** After editing `skill/references/*.md`, run `make sync-docs` or the test suite fails.
4. **No runtime dependencies by default** in `web/` — one HTML file whose rule-based features work with no external service. Two agreed exceptions (`docs/brief.md`, `docs/adr-003-optional-ai.md`): a Google Fonts stylesheet with a full system fallback stack, and the optional, user-initiated AI Boost module (a pinned on-device runtime script, or direct calls to a provider using the visitor's own key). No server, no project-owned keys, no analytics or trackers, no secrets anywhere in the repo.
5. **Sample data stays illustrative.** Numbers in `examples/` are made-up demo values and must be described as such; never present them as a real person's record.

## Working style in this repo
- Before committing, run `make test` and `make build`.
- Use conventional commit prefixes: `feat:`, `fix:`, `docs:`, `ci:`, `build:`, `infra:`, `sec:`, `test:`.
- One logical change per commit; explain *why* in the body when it isn't obvious.
- When adding a playbook or region, update both `skill/references/` and `docs/`, and add a line to `CHANGELOG.md`.
- Prefer editing existing files over adding new ones.
