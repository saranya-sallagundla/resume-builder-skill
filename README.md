# resume-builder-skill

An open-source Claude skill that turns a job description plus your raw material into a shortlist-ready, ATS-optimized resume — scored on a fixed 100-point rubric, built from candidate-type playbooks, and bound by one rule: **claim your real work boldly, never misattribute where it happened.**

[![ci](https://github.com/saranya-sallagundla/resume-builder-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/saranya-sallagundla/resume-builder-skill/actions/workflows/ci.yml)
[![docker](https://github.com/saranya-sallagundla/resume-builder-skill/actions/workflows/docker.yml/badge.svg)](https://github.com/saranya-sallagundla/resume-builder-skill/actions/workflows/docker.yml)
[![k8s-test](https://github.com/saranya-sallagundla/resume-builder-skill/actions/workflows/k8s-test.yml/badge.svg)](https://github.com/saranya-sallagundla/resume-builder-skill/actions/workflows/k8s-test.yml)
[![pages](https://github.com/saranya-sallagundla/resume-builder-skill/actions/workflows/pages.yml/badge.svg)](https://saranya-sallagundla.github.io/resume-builder-skill/)
[![codeql](https://github.com/saranya-sallagundla/resume-builder-skill/actions/workflows/codeql.yml/badge.svg)](https://github.com/saranya-sallagundla/resume-builder-skill/security/code-scanning)
![License: MIT](https://img.shields.io/badge/license-MIT-black)

**Live tool:** <https://saranya-sallagundla.github.io/resume-builder-skill/> — paste any JD to get an instant resume **Blueprint**, **Score & X-Ray** a resume against it, run the **6-Second Scan** to see what a recruiter's fast read actually catches, or **Match** one resume against up to three JDs at once. Runs entirely in the browser; nothing is uploaded.

<!-- Replace with a 10-second GIF: paste → Score it → breakdown appears -->
![demo](docs/demo.gif)

## The problem

Most resumes lose before a human reads them: keyword-matching ATS filters, then a recruiter who spends six seconds on the top third of page one. Advice about this is scattered, contradictory, and usually pushes people toward either bland templates or outright invention. This project encodes what actually gets a resume shortlisted — and keeps it truthful, so it also survives the interview it wins.

## What's in the box

| Piece | What it does |
|---|---|
| [`skill/`](skill/) | The Claude skill. Detects candidate type (fresher / domain switcher / experienced / leadership / non-tech), runs a keyword gap analysis, asks at most five questions, drafts, **verifies page count and parsing**, then scores. |
| [`docs/resume-standards.md`](docs/resume-standards.md) | The complete formatting, ATS, bullet, metric and humanization standard — useful even without Claude. |
| [`docs/ats-scoring.md`](docs/ats-scoring.md) | The 100-point rubric. Same numbers every run, so versions are comparable. |
| [`docs/playbooks.md`](docs/playbooks.md) | Per-candidate-type templates, transferable-skills mapping, red-flag handling. |
| [`docs/regional-conventions.md`](docs/regional-conventions.md) | India, US, UK, EU, Gulf, AU/NZ, Singapore, Canada norms. |
| [`scripts/score_resume.py`](scripts/score_resume.py) | Heuristic implementation of the rubric; used as a CI regression gate. |
| [`web/`](web/) | The same rubric as a single-file browser app — JD → resume blueprint, scorer with an X-Ray view, a 6-second recruiter-scan simulator, and a multi-JD match matrix — deployed to GitHub Pages and packaged as a container. |

## Install the skill

1. Download `resume-builder.skill` from the [latest release](https://github.com/saranya-sallagundla/resume-builder-skill/releases).
2. In Claude.ai, open Settings → Skills → Upload, or drop the file into a chat and choose **Save skill**.
3. Say: *"Here's a JD and my resume — tailor it."* The skill shows the gap analysis first, then builds.

## Score a resume from the command line

```bash
python scripts/score_resume.py --resume my_resume.md --jd the_jd.md
```

```text
## ATS & recruiter match: 94.8 / 100
Keyword coverage 23.8/25 · Placement 6/10 · Title 5/5 · Parse safety 10/10
Quantification 15/15 · Bullet quality 10/10 · Scope & progression 10/10
Length & layout 5/5 · Humanization 5/5 · Hygiene 5/5
```

## The truth rule

Hands-on work you actually did — built, deployed, broke, fixed — earns confident bullets, even if no employer paid you for it. It goes in a **Key Projects** section written exactly like work experience. It never goes under an employer's name where it didn't happen, and the skill will decline to put it there and explain why in two sentences: misattributed experience collapses in interviews and fails background checks. Confidence comes from framing, not fiction.

## How it's built (the DevOps part)

Every push runs a pipeline; every pipeline is free on a public repo.

```text
PR opened ──► ci: markdownlint · yamllint · pytest · skill validation · score regression gate (≥ 85)
          ──► docker: build → Trivy scan (fails on HIGH/CRITICAL) → push to GHCR on merge
          ──► k8s-test: kind cluster → apply manifests → rollout → curl smoke test
          ──► terraform: plan commented on PR; apply on merge (branch protection, labels, topics)
          ──► codeql: Python + JavaScript static analysis
merge     ──► pages: deploy web/ to GitHub Pages
tag v*    ──► package: build .skill → changelog → GitHub Release with artifact
weekly    ──► dependabot: actions, pip, docker, terraform
```

Local equivalents: `make test`, `make score`, `make build`, `make run`, `make k8s-local`.

## Contributing

Playbooks for more roles and markets are the most useful contribution — see [CONTRIBUTING.md](CONTRIBUTING.md). Issues labelled `good first issue` are scoped for a first PR.

## License

MIT.
