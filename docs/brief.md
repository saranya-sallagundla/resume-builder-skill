# Vriddhih — product brief

**Version:** 4 · **Date:** 2026-09-14 · **Status:** approved by owner · **Supersedes:** brief v3

*Vriddhih* (Sanskrit: वृद्धिः, "growth, rising") is a free website that walks a person up every step from *I want a new job* to *I am doing well in it* — résumé, interview, offer, exit, joining, and growth — for any profession, in the browser, with nothing uploaded.

## Why

Writing a résumé, preparing for interviews, negotiating an offer, resigning cleanly and starting well are the most consequential things most working people do, and most people do them alone or depend on someone else. Version 1 of this project graded a résumé. Vriddhih coaches the whole journey, and keeps being useful after the offer letter.

## Who it is for

- Anyone who works, in any domain — software, data, cloud, QA, product, design, sales, marketing, finance, HR, operations, healthcare administration, mainframe, and more. Domain packs supply the specifics; the engine is domain-agnostic.
- At every level: fresher, career switcher, experienced, leadership, non-tech.
- Recruiters and hiring managers evaluating this repository as evidence of engineering practice.

## Non-negotiables

1. **Website only.** No installable app, no install prompts, no app-store builds.
2. **No server, no accounts, no cost.** GitHub Pages hosting; GitHub Actions on the free public-repo tier; no paid services; no keys or secrets owned by the project.
3. **Nothing is uploaded by default.** Rule-based features run in the browser. Saved data lives in the visitor's browser, with export and delete.
4. **AI is optional, never default, never ours.** See `adr-003-optional-ai.md`. Mode B (visitor's own free key) ships first; Mode A (on-device model) within one week after.
5. **Truth rule.** Generated example content is labelled *example* and disclaimed; it is never presented as the user's own facts.
6. **Scorer parity and docs mirror.** `scripts/score_resume.py` and `web/index.html` agree; `skill/references/` and `docs/` match; fixture score stays ≥ 85.
7. **Zero-risk posture.** Original content only, open or cited data only, no scraping, no third-party marks or logos, disclaimer and privacy pages, security policy, contributor originality pledge. No stock photography — every backdrop is drawn procedurally.

## Risk and guardrails

### Owner protection

- MIT licence plus a plain-language **Disclaimer** page (`docs/legal/disclaimer.md`): as-is, not legal, financial, tax or employment advice; examples are illustrative; salary figures are estimates from cited public sources; AI output may be wrong.
- **Privacy** page (`docs/legal/privacy.md`): no accounts, analytics, cookies or server; what the optional AI modes send and to whom; how to delete everything.
- **Content policy:** every question, script and checklist is written for this project. Salary data comes only from public or official sources, cited with a date, or from the visitor's own input. No scraping of sites that forbid it.
- **No third-party marks.** Design language may be inspired by others; the site never names or shows another company's brand.
- **Non-commercial.** No ads, payments or affiliate links.
- **Contributor pledge** in `CONTRIBUTING.md`; **security policy** in `SECURITY.md`.

### Against spam and bad data

| Surface | Guardrail |
|---|---|
| Content and data files | Change only by pull request; CODEOWNERS review; branch protection; CI schema validation (types, sane ranges, required source and date, no disallowed URLs, no profanity) |
| Pasted text | 30k-character cap, debounce, HTML always escaped, strict Content-Security-Policy, no `innerHTML` from untrusted strings |
| Share links | Numbers only, range-checked on read; no free text rendered from the URL |
| AI Boost inputs | Pasted text passed as data inside delimiters with fixed instructions; output validated against a schema and rendered as text; output never triggers an action; optional PII-strip before sending |
| AI Boost keys | Browser storage only; never in URLs, logs or the repo; one-click forget |
| Repository | Dependabot, CodeQL, secret scanning, Trivy; "limit interactions" if issue spam appears |
| Hosting | Static GitHub Pages; nothing can run up a bill |

## Design direction — "Sky &amp; Paper"

Approved preview: the Sky &amp; Paper board (hero and six rooms). Three moves define every screen:

1. **One big line with one italic word.** Bricolage Grotesque 800 headline; a single Instrument Serif italic word in coral carries the emotion.
2. **A torn-paper anchor.** One or two generated torn-paper shapes (cobalt, mustard, coral, ink) frame the composition. Generated with jittered polygons and a displacement filter; never an image asset.
3. **Paper cards are the interface.** Cream cards with a coloured top bar, slight rotation, soft shadow. No dashboards, no mac windows, no skeuomorphic props.

- **Backdrop:** procedural clouds (SVG fractal noise thresholded to alpha) over an analogous sky gradient; each stage shifts the sky one step around the wheel (blue, peach, mint, warm, lavender, sky-mint) so rooms feel different with identical components. Paper grain at 7%.
- **Navigation:** a **staircase** across the bottom of the front door — six stops: Target, Résumé, Apply, Interview, Offer &amp; Exit, Join &amp; Grow. On phones it folds into a stepper. The nav is the name.
- **Palette (triadic on analogous sky, 60·30·10):** sky peach `#FFD3BF` → lavender `#E8DDFF` → sky `#CFE3FF` and paper `#FFFBF2` (60%); cobalt `#2B4CFF` working colour (30%); coral `#FF6A57` CTA and italic word (10%); mustard `#F5C542` for paper and highlighter only; ink `#141621`. Semantic mint `#1FA57A`, amber `#E0A100`, rose `#D64550` appear only inside results.
- **Type:** Bricolage Grotesque (display), Instrument Serif italic (accent), Onest (body), Geist Mono (labels, numbers), Caveat only for the single handwritten journal line. Scale ×1.618; headline line-height 1.04–1.12; body 1.5; captions 40–60 characters. Google Fonts with system fallbacks.
- **Golden ratio:** frames and hero split on 618/382/236 guides; window-free layouts still snap headline column, cards and numbers to those lines. Figma's caution applies: where φ and readability disagree, the reader wins.
- **Both themes** designed; motion honours `prefers-reduced-motion`; visible keyboard focus; no horizontal scroll at 375px.
- **Copy voice:** human, specific, never "empower your career journey". Front-door caption: *Your desk for the résumé, the interview, and the big move.*
- The palette sheet and type specimens live in `docs/`, never on the site.

## The journey and its rooms

| Stage | Room concept | What lives there |
|---|---|---|
| **Target** | The compass | Role Compass, JD red-flag check, skill-gap plan, "where are you today?" starter |
| **Résumé** | *Fix it line by line* — the sheet with paper cards beside it; the score in display type | Build, Score, X-Ray, fixes, Placement Map, Coach, Three Readers, Compare, length rule, master + variants, truth ledger, export |
| **Apply** | *Every application, and its next move* — cards riding a cobalt ribbon through the stages | Tracker, follow-up clock, reflection, cover letter, LinkedIn, referral script, calendar export |
| **Interview** | *Fifty questions, written for your level* — a giant 50, a fanned deck, one cobalt drill card | 50 Questions, Drill, Story Bank, Voice Mock, 60-second pitch, company briefing sheet, round playbooks, reverse questions, interview-day checklist, Ask Calculator, take-home view |
| **Offer &amp; Exit** | *Compare, decide, leave well* — two paper columns and a three-date timeline | Offer comparator, counter-offer helper and email, resignation letter, notice calculator, exit checklist, handover doc |
| **Join &amp; Grow** | *One sentence a week. Your next résumé, written* — a handwritten line becoming a typeset bullet | Pre-joining checklist, 30-60-90, week-one questions, Brag Doc, review prep, promotion case, skill radar, raise script, 90-day check-ins |

## Features — complete list

### Target

- **Role Compass.** Paste 3–5 JDs → the common skill core, your coverage, the role family you're closest to, and the three skills that unlock the most roles.
- **JD red-flag check.** Flags vague compensation, "rockstar/ninja", unpaid trials, overloaded scope, unrealistic experience asks.
- **Skill-gap plan.** Missing JD skills → a short plan with free, cited resources.
- **Where are you today?** First-visit picker that jumps to the right step.

### Résumé

- **Build from JD.** A complete illustrative résumé for the role and level; every invented figure tagged *example*; banner: copy the shape, never the numbers.
- **Score.** Ten dimensions, 100 points; the score is the loudest element on the page with an italic verdict.
- **X-Ray.** Highlighter: yellow = JD keyword found, blue = best empty slot; wavy underline = weak bullet; clichés struck.
- **Fixes, not flags.** Each issue says where the keyword belongs with an example sentence; the metric type that fits a numberless bullet with an example rewrite; strong-verb swaps; the exact headline for a title mismatch.
- **Keyword Placement Map.** Section × keyword grid with the best empty slot marked.
- **Coach.** Click a bullet → diagnosis, metric fit, rewrite pattern, example rewrite, and the Interview Defense question it triggers.
- **Three Readers.** ATS bot, HR screener (6 seconds), hiring manager (2 minutes) as three paper cards: verdict, three notes, "what gets you the call".
- **Compare.** One résumé vs up to three JDs; Version Compare with per-dimension deltas.
- **Length rule.** Any page count accepted; ≤ 2 pages → 5, 3 → 2, 4+ → 0; real page-size preview; Letter/A4 toggle.
- **Master résumé + variants.** One master, per-JD variants saved locally; **Tailor diff** shows exactly which bullets to reorder or rewrite for a new JD.
- **Truth ledger.** Every number can carry a private source note ("Jira dashboard, Q3"); the ledger feeds Interview Defense.
- **Extractor fix.** Stops promoting generic verbs and vague nouns; prefers tools, platforms, certifications, multi-word phrases. Ships with Python parity, tests and a refreshed fixture score.
- **Export.** Copy as Markdown; print to PDF with a page-accurate stylesheet.

### Apply

- **Tracker.** Cards move Saved → Applied → Screen → Tech → Final → Offer along the ribbon; each carries its match score and its next move; a count of what's in play.
- **Follow-up clock.** Thank-you within 24 h, nudge at day 7, close-out at day 21 — scripts for each.
- **Post-interview reflection.** Two-minute card after each round; wobbles feed Drill; patterns surface ("you lose at HR rounds").
- **Cover letter** from your bullets and the JD. **LinkedIn headline and About** from the résumé.
- **Referral request script** for a contact at the company.
- **Calendar export (.ics)** for follow-ups, interviews and notice dates — no notification server needed.

### Interview

- **50 Questions.** Skills mapped from the JD (weighted) and résumé (evidenced), classed Core / Gap / Differentiator / Claim. Experience band 0–2, 2–5, 5–10, 10+ detected and editable. Fixed recipe: 15 core at three depths, 8 claim probes, 8 scenarios from JD responsibilities, 7 gap questions with an honest answer route, 6 STAR, 6 role and HR. Each card shows category, why they'll ask (the JD line or bullet), what a strong answer includes, and a self-rating. Filter by round; export or print.
- **Staying current.** The JD drives generation for any new tool; the skill bank carries `lastReviewed` and a monthly Action flags entries older than six months; AI Boost covers unknown skills; community questions arrive through issue forms and are schema-checked.
- **Drill.** Flat-colour flashcards; Blank / Shaky / Confident; shaky first; keyboard shortcuts; gentle progress ("31 of 50 confident", "practised 4 days this week") — no badges or leaderboards.
- **STAR Story Bank.** One bullet → one story skeleton → the questions it answers.
- **Voice Mock.** Browser speech recognition transcribes a spoken answer; counts fillers, pace, whether a number was stated, and the four STAR beats. Nothing leaves the device.
- **60-second pitch.** "Tell me about yourself" from the résumé: headline → two proof points → why this role → the ask. Timed, editable.
- **Company briefing sheet.** Paste their About / values / a news paragraph → their language, your matching stories, three questions to ask them.
- **Round playbooks.** Recruiter, Technical, Manager, Client, HR — what each tests, what to prepare, how to open.
- **Reverse questions.** Questions to ask them, built from JD gaps and red flags, sorted by round.
- **Interview-day checklist.** Per round and format (remote, onsite, panel).
- **Ask Calculator.** Inputs: role family, years, country and city tier, current package, notice, competing offers, in-demand JD skills held, certifications. Data: `salary-bands.json` (role × band × region → P25/P50/P75/P90, source and date); US bands refreshed monthly from official BLS data by a scheduled Action (no key); other regions curated by PR; visitor may enter their own figure. Output: **Safe**, **Sweet spot**, **Stretch** — number, plain-English odds, script, signals that move you up or down. Source and date printed on the result.
- **Take-home view.** Approximate in-hand per month (India CTC → fixed → in-hand) or net (US), clearly marked approximate.

### Offer &amp; Exit

- **Offer comparator.** Two or three offers normalised to total compensation: fixed, variable, bonus, ESOP vesting, PF, remote; winner outlined; year-1 vs steady-state view.
- **Counter-offer helper** (stay vs go) and a **counter-offer email** draft.
- **Resignation letter** with tone options.
- **Notice calculator.** Resign date → last working day (weekends, holidays) → join date; leave encashment; buyout maths; shown as a three-date timeline.
- **Exit checklist by country.** Relieving and experience letters, Form 16 / W-2, PF/UAN transfer, gratuity, insurance continuation, asset return.
- **Handover document** generated from your project list.

### Join &amp; Grow

- **Pre-joining checklist.** Background-verification documents, bank and ID, day-one prep.
- **30-60-90 plan** built from the JD that got you hired.
- **Week-one questions.** Who owns what, on-call, definition of done, how decisions get made.
- **Brag Doc.** One plain sentence a week → a résumé bullet and a review talking point, auto-drafted; weeks-logged bars.
- **Review prep and promotion case.** Journal → talking points → ladder mapping.
- **Skill radar.** Your skills vs the JDs you target, refreshed as you log.
- **Yearly raise script** from the radar and market bands.
- **90-day check-ins.** Day 30 / 60 / 90 reflection prompts, exportable to calendar.

### Cross-cutting

- **Region lens:** India, US, UK, EU, Gulf conventions applied to every tip.
- **Domain packs:** software, data, cloud, QA, product, design, sales, marketing, finance, HR, operations, healthcare administration, mainframe; more by PR.
- **AI Boost (optional):** Mode B — visitor's own free key (Google AI Studio, Groq, OpenRouter free models); Mode A — on-device model via WebGPU. Never default; never the project's keys; PII-strip before sending.
- **My Data:** everything in browser storage; export/import JSON with optional passphrase encryption (WebCrypto); one-click delete.
- **Share link:** score numbers only in the URL. **Before/after card:** an anonymised score card for sharing or the README.
- **Accessibility:** keyboard-first Drill, visible focus, reduced motion, 375px layouts, contrast checked in both themes.
- **Disclaimer and Privacy** linked from every page.

## Delivery plan

One pull request per part; CI green; merge; verify live. Each UI part is preceded by an approved preview.

| Part | Delivers | Owner's hands-on |
|---|---|---|
| 0 | Brief v4, ADR-003, disclaimer, privacy, SECURITY.md, contributor pledge, CLAUDE.md | Branch, PR, merge |
| 1 | Sky &amp; Paper shell: fonts, tokens, procedural backdrops, torn-paper generator, staircase nav, front door with feature cards, Disclaimer and Privacy pages | Approve on phone, merge |
| 2 | Résumé room: Build, Score, X-Ray, fixes, Placement Map, Coach, Three Readers, Compare, length rule, extractor fix, export — JS and Python, tests, docs | `make test`, `make score`, merge |
| 3 | Interview room: 50 Questions with bands, skill bank v1 (≈ 80 skills across domains), Drill, Story Bank, 60-second pitch, reverse questions, round playbooks, interview-day checklist | Review bank copy, merge |
| 4 | AI Boost Mode B, PII-strip, CSP, schema validation for content files | Test with a personal free key, merge |
| 5 | Ask Calculator, take-home view, salary-bands v1, BLS refresh Action, skill-bank staleness Action | Run both Actions once, merge |
| 6 | AI Boost Mode A (on-device), device check | Test when a laptop is available |
| 7 | Voice Mock, company briefing sheet, master + variants, Tailor diff, truth ledger | Play HR, merge |
| 8 | Offer &amp; Exit room: comparator, counter-offer, resignation letter, notice calculator, exit checklist, handover | Try the notice calculator, merge |
| 9 | Apply room: tracker, follow-up clock, reflection, cover letter, LinkedIn, referral script, .ics export | Track one real application, merge |
| 10 | Join &amp; Grow room: checklists, 30-60-90, Brag Doc, review prep, promotion case, radar, raise script, check-ins | Log one week, merge |
| 11 | Target room: Role Compass, red-flag check, skill-gap plan, starter picker; My Data export/import with encryption | Merge |
| 12 | Lighthouse and a11y CI, README hero and before/after card, `v1.0.0` release, starter issues | Tag, install the skill |

## Acceptance

- All CI checks green on `main`; fixture score ≥ 85; content and data schemas validated.
- Lighthouse performance and accessibility ≥ 90; both themes legible; no console errors; 375px without horizontal scroll.
- Every generated example visibly labelled; every salary figure shows source and date; Disclaimer and Privacy linked from every page.
- No key, secret, tracker or paid service anywhere; the owner's cost is zero.

## Decisions log

- **2026-09-13 — Name:** Vriddhih. Exact spelling free on GitHub and every checked TLD; the plain word is used by others. Always write it with the final *h*; never "Vriddhi" alone; prefer `vriddhih.app` or `.in` if a domain is bought.
- **2026-09-13 — Scope:** the whole journey, all domains and levels; the daily-use hook is the Brag Doc.
- **2026-09-13 — AI:** optional only; Mode B first, Mode A a week later; no Mode C; no project keys.
- **2026-09-13 — Form:** website only; zero cost; non-commercial forever.
- **2026-09-14 — Design:** Sky &amp; Paper approved (hero and six rooms). Rooms are not props or windows; they reuse the hero's three moves. The Apple-style direction from brief v3 is withdrawn.
- **2026-09-14 — Part 1 shipped; dark mode flagged.** Sky & Paper shell live. Owner: dark-mode colours are "the worst" — revisit at the end of the build (not now, not blocking Part 2). Tracked here so it isn't forgotten.
- **2026-09-14 — Research additions:** 60-second pitch, company briefing sheet, interview-day checklist, post-interview reflection, follow-up clock, take-home view, gentle streaks (from Dribbble and Figma Community patterns). Owner-approved suggestions added: master + variants with Tailor diff, truth ledger, referral script, counter-offer email, .ics export, 90-day check-ins, starter picker, before/after card, Letter/A4 toggle.
- **Process:** one PR per part; the owner runs every git and GitHub step; preview approved before each UI part; CI green before merge.
