# ADR-001: Two scorers, one rubric

**Status:** accepted · **Date:** 2026-09-10

## Context

The rubric needs to run both in CI (Python, as a regression gate) and in a browser (no backend, no API cost) for the public demo.

## Decision

Implement the rubric twice — `scripts/score_resume.py` and `web/index.html` — from the same specification in `docs/ats-scoring.md`. Both are heuristic; neither calls an LLM. The Python version is the reference; the test suite pins its behaviour and the sample resume acts as a golden file.

## Consequences

- Zero runtime cost and no secrets anywhere in the project.
- Drift between the two is a real risk; CONTRIBUTING requires paired changes, and a future eval could diff both outputs on the sample set.
- Heuristic keyword extraction will miss some phrases an LLM would catch; the Claude skill compensates when it runs, the web demo does not.
