# ADR-003: AI is optional, user-initiated, and never the project's

**Status:** accepted · **Date:** 2026-09-13 · **Supersedes:** ADR-002's "no AI calls"

## Context

Coaching features — fluent bullet rewrites, questions for brand-new skills, cover-letter drafts — are better with a language model. ADR-002 ruled out AI because the maintainer's only Claude access is employer-provided and because the site promises that nothing is uploaded. Both facts still hold. Two free routes exist that respect them:

- **Mode B — bring your own free key.** Several providers offer free, rate-limited API tiers. A visitor can use their own key; the maintainer can test with a personal account.
- **Mode A — on-device.** Small open models run in the browser through WebGPU. Nothing leaves the device. It needs a capable device and a one-time model download.

## Decision

1. Every feature works without AI. Rule-based output is the default and is always shown first.
2. AI Boost is an explicit, per-visitor opt-in. Mode B ships first; Mode A follows within one week and becomes the preferred option where the device supports it.
3. The project never holds a key, runs a server, or proxies requests. In Mode B the visitor's key lives only in their browser storage; the browser calls the provider directly; a notice states what is sent and links the provider's terms. A one-click control forgets the key.
4. Guardrails apply to every model call: pasted text is passed as data inside delimiters with fixed instructions; output is validated against a schema and rendered as text; output never triggers an action; a PII-strip option removes emails, phone numbers and addresses before sending.
5. AI never produces the numbers in a user's resume. It may propose shape and wording; figures remain the user's, and generated examples stay labelled.

## Consequences

- ADR-002's "client-side only, no server" stays in force; only its blanket "no AI" is lifted.
- CLAUDE.md rule 4 gains a second agreed exception: the AI Boost module (a pinned on-device runtime script, or direct calls to a visitor-chosen provider).
- Mode A cannot be fully verified until a WebGPU-capable laptop is available; it ships with a device check and a graceful fallback, and a small model for smoke testing.
- Free tiers change. The provider list and limits are documented in the Privacy page and reviewed with the monthly staleness check.
