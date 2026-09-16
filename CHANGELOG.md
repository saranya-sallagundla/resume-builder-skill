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

- AI Boost (Mode B): optional, off by default, using the visitor's own free API key. The key lives
  only in their browser, never in a URL and never in this repository, with one-click forget.
  Pasted text is sent as delimited data with fixed instructions to ignore any instruction inside
  it; replies are schema-validated and rendered as plain text; the model is told never to invent
  figures. A "strip contact details" pass (on by default) replaces emails, phone numbers and links.
  A request preview shows exactly what would be sent, with the key redacted, before anything goes.
  Wired into the résumé Coach for bullet rewrites — the rule-based coaching is unchanged and still
  shown first, whether AI is off, misconfigured or failing.
- Content-Security-Policy, the load-bearing part being `connect-src`: the page may only ever talk
  to the AI providers a visitor opts into. A test keeps the allowlist and the provider table in sync.
- "Test connection" on the AI Boost page, distinguishing a rejected key, a retired model name, a
  rate limit, and a provider that refuses browser calls outright.

### Changed

- The Interview stop on the staircase is live; the Ask Calculator moved to the Offer &amp; Exit room.
- Default AI provider is Groq (free and fast). The page makes no claim about which providers a
  given browser can reach: the same "CORS failure" is reported whether an API refuses browsers,
  a network blocks the call, or the provider is rate-limiting, so "Test connection" is the source
  of truth for each visitor and the failure message names all three causes.
- Privacy page now states accurately what the PII strip does and does not remove.

## [0.1.0] — 2026-09-10

- Initial release: skill with five playbooks, 100-point rubric, regional conventions, examples, evals.
- Python scorer with CI regression gate; browser scorer on GitHub Pages.
- Docker image (Trivy-scanned, GHCR), Kubernetes manifests validated on kind, Terraform-managed repo settings, CodeQL, Dependabot.
