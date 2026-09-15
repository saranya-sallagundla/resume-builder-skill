# Changelog

## [Unreleased]

### Added

- Vriddhih Interview room: fifty questions generated from the job description and your own résumé
  (core skills at three depths, claim probes on your own numbers, scenarios from their
  responsibilities, gap questions with an honest answer route, behavioural and role questions),
  filtered by interview round, with an experience band detected from the résumé and editable.
- Interview skill bank v1 — 91 skills across cloud, software, data, ITSM, project, business and
  soft-skill domains. Embedded in `web/index.html` as strict JSON between `BANK-START`/`BANK-END`
  markers, schema-checked by `tests/test_web_page.py`.
- Drill deck (blank / shaky / confident, shaky first, keyboard shortcuts), STAR Story Bank,
  60-second pitch with a timer and word count, reverse questions built from the JD's own wording,
  round playbooks and a per-format interview-day checklist. Ratings, stories, pitch and checklist
  state stay in the visitor's browser.

### Changed

- The Interview stop on the staircase is live; the Ask Calculator moved to the Offer &amp; Exit room.

## [0.1.0] — 2026-09-10

- Initial release: skill with five playbooks, 100-point rubric, regional conventions, examples, evals.
- Python scorer with CI regression gate; browser scorer on GitHub Pages.
- Docker image (Trivy-scanned, GHCR), Kubernetes manifests validated on kind, Terraform-managed repo settings, CodeQL, Dependabot.
