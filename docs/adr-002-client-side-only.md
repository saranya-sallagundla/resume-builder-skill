# ADR-002: The web tool stays client-side, with no AI calls

**Status:** partly superseded by `adr-003-optional-ai.md` (the "no AI" part; "no server" stays) · **Date:** 2026-09-13

## Context

Version 2 adds coaching features — sample resumes, bullet rewrites, reviewer personas — that an LLM could produce well. Three facts argue against calling one from the web page:

- The page is public and static. Any shared key would leak; a per-visitor key excludes most job seekers, who do not have one.
- The maintainer's Claude access is employer-provided and must not be used for a personal project, so an AI mode could not even be tested honestly today.
- The project's promise is "nothing is uploaded". Sending a resume to any API breaks it.

## Decision

All generation and feedback in `web/index.html` is rule-based and runs in the browser. Suggestions come from the JD's extracted keywords, the resume's detected structure, verb and metric pattern tables, and the standards in `docs/`. Generated content is labelled as example content.

The Claude skill in `skill/` remains the AI path: it runs inside a user's own Claude account, where the user controls the data.

## Consequences

- Suggestions are consistent and explainable, but less fluent than an LLM's. The copy library must be written with care.
- The scorer and the coach share one keyword extractor, so extractor improvements need parity in Python and a refreshed golden score.
- A "bring your own key" AI mode may be added later as an explicit opt-in, stored only in the visitor's browser, once it can be tested with a personal key. It must never become the default.
