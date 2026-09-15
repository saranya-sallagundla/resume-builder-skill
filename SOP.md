# SOP: Build and publish the resume-builder project using Claude Code on the web

**Audience:** someone who has never used GitHub, Docker, or a terminal.
**Constraint honoured:** nothing is installed on your laptop. Everything runs in a browser tab.
**Total time:** about 2 hours, and you can stop after any Part and resume later.

---

## Part 0 — Read this first (5 min)

### 0.1 What you are building

Three things at once:

1. **A Claude skill** — a file you install into Claude.ai that makes Claude build ATS-optimized resumes properly.
2. **A public GitHub project** — the same skill, published with documentation, so it counts as portfolio work.
3. **A DevOps pipeline around it** — automated checks that run every time you change the project. This is the part that turns "I wrote some documents" into "I engineered and shipped something."

### 0.2 Why nothing gets installed

**Claude Code on the web** (at `claude.ai/code`) runs on Anthropic's cloud computers, not yours. It clones your GitHub project into a temporary virtual machine, does the work you ask for in plain English, and pushes the result back to GitHub. You only ever open a browser tab. When you return the laptop, you lose nothing — the project lives in your GitHub account.

Requirement: Claude Code on the web needs a paid Claude plan (Pro, Max, Team, or Enterprise). You said you have Claude Code access, so you're covered.

### 0.3 Words you'll see, in plain English

| Word | What it actually means |
|---|---|
| **Repository (repo)** | A project folder that lives on GitHub. |
| **Commit** | A save point with a note describing what changed. |
| **Push** | Upload your save points to GitHub. |
| **Branch** | A parallel copy of the project where you try something without breaking the main copy. |
| **Pull request (PR)** | A request to merge a branch into the main copy, with automated checks attached. |
| **GitHub Actions / workflow / pipeline** | A robot that runs your checks automatically whenever you change something. |
| **CI** | "Continuous integration" — the name for that robot habit. |
| **Docker / image / container** | A way to package an app with everything it needs so it runs identically anywhere. |
| **Kubernetes (k8s)** | The system big companies use to run lots of containers. `kind` is a throwaway mini-Kubernetes used only for testing. |
| **Terraform** | Describing settings in a file instead of clicking buttons, so the settings are version-controlled. |
| **GitHub Pages** | Free website hosting for files in your repo. |
| **Badge** | The little green "passing" image in a README that proves your checks run. |
| **Session** | One conversation with Claude Code, working on one task. |

### 0.4 How to use this SOP with Claude Code

Anything in a grey box labelled **PROMPT** is text you copy and paste into the Claude Code message box, then press Enter. You don't type commands yourself — you describe the goal and Claude Code runs the commands in its cloud VM.

If Claude Code asks you a question, answer in plain English. If it proposes a plan, read it and reply `yes, proceed` or tell it what to change.

**Golden rule:** if anything goes wrong at any step, paste the exact error text into Claude Code and add: `this failed, please diagnose and fix it, then explain what was wrong in simple terms.` That is the intended way to use it.

---

## Part 1 — Accounts and one policy check (10 min)

### Step 1.1 — Check your company policy

Before anything else, confirm your company's acceptable-use policy allows using a personal GitHub account and personal Claude account from the work laptop in a browser. Most allow browser-based personal use; some don't.

Also: **nothing from your employer goes into this project.** No company code, no client names, no internal documents, no work email. When you later test the skill on your own resume, keep employer names generic if your resume contains client-confidential detail, and do not commit your resume into the public repo.

### Step 1.2 — Create a GitHub account

1. Go to `github.com` → **Sign up**.
2. Use a personal email, not your work email. Recruiters will see this account — pick a professional username (`saranya-<something>`, not `cooldude99`).
3. Verify the email.
4. Optional but worth 2 minutes: add a profile photo, a one-line bio, and your city. Recruiters click through.

### Step 1.3 — Confirm your Claude plan

Go to `claude.ai` and sign in. Claude Code on the web needs Pro, Max, Team, or Enterprise.

---

## Part 2 — Create the empty repository (5 min)

### Step 2.1

1. Go to `github.com/new`.
2. **Repository name:** `resume-builder-skill`
3. **Description:** `An open-source Claude skill that builds ATS-optimized resumes — with a 100-point scoring rubric, candidate-type playbooks, and a strict no-fabrication rule.`
4. Select **Public**. (Private repos can't use free GitHub Pages, and recruiters can't see them.)
5. Tick **Add a README file**. (You need at least one file so the repo isn't empty; we'll overwrite it.)
6. **Add .gitignore:** None. **License:** None. (Both are in the zip already.)
7. Click **Create repository**.

You'll land on your new repo page. The address bar shows `github.com/<your-username>/resume-builder-skill`. Write your username down — you'll need it.

---

## Part 3 — Upload the project files (15 min)

Your laptop can open a zip without installing anything (Windows Explorer and macOS Finder both do it natively).

### Step 3.1 — Extract the zip

1. Download `resume-builder-skill.zip` from the Claude chat.
2. Right-click → **Extract All** (Windows) or double-click (Mac).
3. You get a folder called `repo` containing everything.

### Step 3.2 — Upload the ordinary folders

1. On your repo page, click **Add file** → **Upload files**.
2. Open the extracted `repo` folder in a second window.
3. Select these and drag them into the browser upload area:
   - the folders `skill`, `docs`, `scripts`, `tests`, `examples`, `web`, `k8s`, `terraform`
   - the files `README.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `LICENSE`, `Makefile`, `Dockerfile`, `SOP.md`, `SETUP_TONIGHT.md`, `requirements-dev.txt`
4. In the **Commit changes** box, replace the message with: `feat: resume-builder skill, scorer, web app and deployment manifests`
5. Click **Commit changes**. Wait for the page to reload.

### Step 3.3 — The hidden files (this is the part that trips people up)

Files and folders starting with a dot (`.github`, `.devcontainer`, `.gitignore`, `.dockerignore`, `.markdownlint-cli2.jsonc`, `.pre-commit-config.yaml`) are hidden by your operating system and often refuse to drag correctly. Don't fight it — let Claude Code create them. That's Part 4.

If you're curious, you can first make hidden files visible (Windows: File Explorer → View → tick *Hidden items*; Mac: `Cmd+Shift+.`) and try dragging them too. If they upload, great — Part 4 will simply confirm they're correct instead of creating them.

---

## Part 4 — Connect Claude Code on the web (10 min)

### Step 4.1 — Open it

1. Go to `claude.ai/code`.
2. On Windows/macOS the first screen offers the desktop app. **Click "Continue on web"** at the bottom — that keeps you install-free.

### Step 4.2 — Connect GitHub

1. It will prompt you to connect GitHub. Follow the prompt; GitHub asks you to authorize. Approve it.
2. It may then offer to install the "Claude GitHub App" on your repositories. Installing it enables Claude to auto-fix failing checks on pull requests later — useful, and you can also click **Skip**; sessions reach your repos either way.
3. **Environment:** on Pro and Max an environment named **Default** is created for you. On Team/Enterprise you may see a *Create your first cloud environment* form — leave everything prefilled and click **Create & finish**. Default is fine for this project.

### Step 4.3 — Select your repo and start

1. Below the message box, click the repository selector and choose `resume-builder-skill`.
2. Leave the branch as `main`.
3. Set the mode dropdown to **Plan** for your first task (Claude proposes an approach and waits for your approval before editing). Later you can switch to **Accept edits** to move faster.

### Step 4.4 — First prompt: create the hidden files

Paste this exactly:

> **PROMPT**
>
> This repo is a Claude skill plus its DevOps toolchain. Some dot-prefixed files could not be uploaded through the GitHub web UI, so please create any that are missing. Read `README.md`, `CLAUDE.md` and `Makefile` first to understand the intended setup, then create:
>
> 1. `.gitignore` ignoring: `dist/`, `site/`, `__pycache__/`, `.pytest_cache/`, `*.pyc`, `terraform/.terraform/`, `terraform/*.tfstate*`, `terraform/terraform.tfvars`, `terraform/plan.txt`, `junit.xml`
> 2. `.dockerignore` ignoring: `.git`, `dist`, `tests`, `terraform`, `k8s`, `skill/evals`
> 3. `.markdownlint-cli2.jsonc` with config disabling rules MD013, MD033, MD041, MD024, MD060
> 4. `.github/CODEOWNERS` assigning everything to my GitHub username
> 5. `.github/PULL_REQUEST_TEMPLATE.md` with a checklist: `make test` passes, `make sync-docs` run if references changed, sample-resume score not dropped, no fabricated content in examples
> 6. `.github/ISSUE_TEMPLATE/playbook.yml` and `.github/ISSUE_TEMPLATE/rubric.yml` as GitHub issue forms
> 7. `.github/dependabot.yml` with weekly updates for github-actions, pip, docker, and terraform (terraform directory is `/terraform`)
> 8. `.pre-commit-config.yaml` with trailing-whitespace, end-of-file-fixer, check-yaml, markdownlint, and a local hook running `python3 scripts/build_skill.py`
> 9. `.devcontainer/devcontainer.json` based on the Python 3.12 devcontainer image, with features for docker-in-docker, kubectl, terraform, github-cli and node, installing `requirements-dev.txt` and `kind` in postCreateCommand, and forwarding port 8080
>
> Do not create the workflow files yet — that's the next task. When done, tell me in plain English what each file does.

Review the plan, reply `yes, proceed`, then when it finishes it pushes a branch. Click **Create PR**, then merge it on GitHub (green **Merge pull request** → **Confirm merge**).

### Step 4.5 — Second prompt: verify the project actually works

Start a new session (or continue the same one) and paste:

> **PROMPT**
>
> Install the dev dependencies and verify the project end to end. Specifically:
> 1. `pip install -r requirements-dev.txt`
> 2. Run `pytest -q` — all tests must pass
> 3. Run `python scripts/build_skill.py` — it should validate and produce `dist/resume-builder.skill`
> 4. Run `python scripts/score_resume.py --resume examples/sample_resume.md --jd examples/sample_jd.md` and show me the output
> 5. Check that `scripts/score_resume.py` and `web/index.html` implement the same rubric — list any dimension where they would produce different numbers
>
> Report results in plain English. Fix anything broken, but explain each fix before you make it. Do not change the rubric's point weights.

Expected: tests pass, and the sample resume scores about 94.8 out of 100.

---

## Part 5 — Add the pipelines (20 min)

This is the DevOps content. The workflow files are already in the zip under `.github/workflows/`, but they're hidden files, so they may not have uploaded. Have Claude Code handle it.

### Step 5.1

> **PROMPT**
>
> Set up the CI/CD workflows in `.github/workflows/`. If any already exist, review them instead of recreating them. I need seven workflows:
>
> 1. **ci.yml** — on pull requests and pushes to main. Two jobs: `lint` (markdownlint on skill/docs/README, yamllint on .github and k8s) and `test` (Python 3.12, install requirements-dev.txt, run `python scripts/build_skill.py`, run pytest, then a regression gate: `python scripts/score_resume.py --resume examples/sample_resume.md --jd examples/sample_jd.md --min-score 85`). Write the score into the job summary and upload the .skill file as an artifact.
> 2. **package.yml** — on tags matching `v*`: build the .skill file, generate a changelog from git log since the previous tag, and publish a GitHub Release with the .skill attached.
> 3. **docker.yml** — build the image from the Dockerfile, scan it with Trivy failing on HIGH/CRITICAL, upload the SARIF results to code scanning, and push to GHCR (`ghcr.io/<owner>/resume-scorer`) on merges to main only, not on PRs.
> 4. **k8s-test.yml** — create a `kind` cluster, build the image locally, load it into kind, `kubectl apply -k k8s/`, override the deployment image to the CI build, wait for rollout, then port-forward and curl the service to confirm the page is served. Print diagnostics if it fails.
> 5. **pages.yml** — on merges to main, copy `web/` plus the two example markdown files into a site folder and deploy to GitHub Pages using the official Pages actions.
> 6. **terraform.yml** — on changes under `terraform/`: fmt check, init, validate, plan (commented onto the PR), and apply only on merge to main. Use a secret named `TF_GITHUB_TOKEN`.
> 7. **codeql.yml** — CodeQL analysis for Python and JavaScript on PRs, pushes to main, and weekly.
>
> Set the minimum required `permissions` on each workflow rather than granting broad access. After creating them, validate every YAML file parses correctly. Explain in plain English what each workflow proves about the project.

Merge that PR. Then open the **Actions** tab on GitHub and watch. Green ticks = working.

### Step 5.2 — If something goes red

Completely normal on a first run. Click the failed run, click the failed step, copy the red error text, and paste into Claude Code:

> **PROMPT**
>
> The `<workflow name>` workflow failed with this error. Diagnose the root cause, fix it, and explain what was wrong in simple terms:
>
> ```
> <paste the error here>
> ```

---

## Part 6 — Switch on the free GitHub features (15 min)

All in the GitHub web UI, in your repo's **Settings** tab.

| # | Where | Do this | Why |
|---|---|---|---|
| 1 | Settings → **Pages** | Source: **GitHub Actions** | Publishes your live scorer page |
| 2 | Actions tab → `pages` workflow → **Run workflow** | Run it once | First deploy |
| 3 | Settings → **Actions → General** → Workflow permissions | **Read and write permissions** | Lets workflows publish releases and images |
| 4 | Settings → **Code security** | Enable Dependabot alerts, Dependabot security updates, secret scanning | Security signals recruiters notice |
| 5 | Settings → **General** → Features | Tick **Discussions** | Makes the project look alive |
| 6 | Repo home → **About** (gear icon) | Add topics: `claude-skill`, `resume`, `ats`, `devops`, `github-actions`, `kubernetes`, `terraform`. Add the Pages URL as the website | Discoverability |
| 7 | Settings → **Branches** → Add branch ruleset | Protect `main`; require status checks `ci / test` and `ci / lint` | Proves you work with quality gates |

After step 1–2, your live page is at `https://<your-username>.github.io/resume-builder-skill/`. Open it, paste any JD and resume, click **Score it**. Put that URL in the README (it's already there — just confirm the username is right).

### Step 6.1 — Cut your first release

> **PROMPT**
>
> Create and push an annotated git tag `v0.1.0` with a short release message summarising the initial release. Then tell me where to find the published release.

The `package` workflow builds `resume-builder.skill` and attaches it to the release. That's your download link for the next Part.

### Step 6.2 — Create starter issues

> **PROMPT**
>
> Using the GitHub CLI, create five issues in this repository, each labelled `good first issue`, with a one-paragraph description and clear acceptance criteria: (1) Playbook: Product Manager, US market. (2) Regional conventions: Japan. (3) Scorer: improve passive-voice detection accuracy. (4) Add a demo GIF to the README. (5) Parity test that diffs the Python and JavaScript scorer outputs on the sample set. Also create the labels if they don't exist.

Open issues make a repo look maintained rather than abandoned.

---

## Part 7 — Use the skill on your own resume (20 min)

This is the actual point of everything above.

### Step 7.1 — Install the skill

1. Go to your repo → **Releases** → `v0.1.0` → download `resume-builder.skill`.
2. Open `claude.ai` (normal chat, not the Code tab).
3. Drag the `.skill` file into the chat and choose **Save skill**. (Or Settings → Capabilities/Skills → Upload.)

### Step 7.2 — Run it

Open a fresh chat and paste:

> **PROMPT**
>
> Here is a job description and my current resume. Tailor my resume to this JD.
>
> JOB DESCRIPTION:
> <paste the full JD, job title on the first line>
>
> MY CURRENT RESUME:
> <paste your resume text, or attach the file>

### Step 7.3 — What should happen, in order

1. **Gap analysis** — the JD's must-have keywords, which you have, which are worded wrong, which are genuinely missing, plus red flags.
2. **Up to five questions** — usually asking for numbers: team size, ticket volumes, SLA percentages, cost or time saved. Answer as precisely as you honestly can; "roughly 200 a month" is fine, inventing "247" is not.
3. **A 2-page .docx** — verified for page count and parsing.
4. **A score** with the ten-dimension breakdown.
5. **Defend-your-resume notes** — the five bullets most likely to be probed in an interview.
6. **An upskilling shortlist** — what to learn to close the real gaps.
7. **A LinkedIn headline and About** matching the resume.

### Step 7.4 — Verify independently

Paste the final resume text into your own live scorer page and screenshot the score. Do the same with your *old* resume first if you still have it. That before/after pair is the most persuasive thing you can put in the README — anonymize it (replace employer and client names with "US healthcare payer" etc.) before publishing.

> **PROMPT** (in Claude Code, after saving the screenshots)
>
> I'm adding two screenshots to `docs/`: `score-before.png` and `score-after.png`. Add a short "Results" section near the top of the README that shows them side by side with one sentence of context, making clear the example is anonymized and the numbers are one real before/after run.

---

## Part 8 — Keep it alive (15 min a week)

A repo with one burst of commits and then silence reads worse than a small repo with steady activity. Weekly, pick one item:

- Close one `good first issue` yourself — via a branch and a PR, not a direct push, so the branch protection and PR template do their job.
- Add a playbook for a new role or market.
- Improve the scorer's accuracy and add a test proving it.
- Update `CHANGELOG.md` and tag a new version when something meaningful lands.

**Always use the branch/PR flow from now on:**

> **PROMPT**
>
> Create a branch called `feat/<short-name>`, implement <the change>, run `make test` and `make sync-docs` if references changed, commit with a conventional-commit message, push, and open a pull request explaining the change and its effect on the rubric score.

---

## Part 9 — What you can now say in an interview

Only claim these once the corresponding badge is actually green. Every line below is defensible from the repo.

| Evidence | The sentence |
|---|---|
| `ci` badge | "Every pull request runs markdown and YAML linting, unit tests, skill-structure validation, and a scoring regression gate — a rubric change that lowers the golden-file resume score fails the build." |
| `docker` badge | "The web scorer ships as a multi-stage image running non-root nginx, scanned with Trivy on every build, published to GitHub Container Registry." |
| `k8s-test` badge | "CI provisions a kind cluster, applies kustomize manifests with readiness and liveness probes and resource limits, then smoke-tests through the Service via port-forward." |
| `terraform` badge | "Branch protection, labels and repository topics are declared in Terraform; plans are posted to the pull request and applied on merge." |
| `codeql` badge + Dependabot | "Static analysis runs on Python and JavaScript per-PR and weekly; Dependabot keeps Actions, pip, Docker and Terraform dependencies current." |
| `.devcontainer/` | "The toolchain is defined as a dev container, so any contributor gets an identical environment in one click." |
| `docs/adr-001` | "Design decisions are recorded as ADRs — for example, why the rubric is implemented twice and how parity is enforced." |
| The skill itself | "I encoded recruiter screening criteria into a reusable AI skill with a 100-point rubric, five candidate-type playbooks, and a hard no-fabrication rule; I used it to tailor my own resume and validated the before/after with the same scorer." |

And the sentence for the resume's Key Projects section:

> **resume-builder-skill** — open-source Claude skill for ATS-optimized resume generation. 100-point scoring rubric implemented in Python and JavaScript, five candidate-type playbooks, evaluation suite. CI/CD on GitHub Actions with lint, test and score-regression gates; Docker image Trivy-scanned and published to GHCR; Kubernetes manifests validated on ephemeral kind clusters; repository settings managed with Terraform; CodeQL and Dependabot enabled.

---

## Part 10 — Troubleshooting

| Problem | Fix |
|---|---|
| `claude.ai/code` only shows a GitHub login button | Cloud sessions need a connected GitHub account. Complete the browser connect flow in Part 4.2. |
| Your repo doesn't appear in the picker | A session can use any repo the connected GitHub account can see. Confirm you're signed into the right GitHub account, then reload the page. |
| A workflow fails on its very first run | Expected. Copy the error, paste it into Claude Code with the diagnose-and-fix prompt from Step 5.2. |
| `terraform` workflow fails on a missing token | It stays dormant until you add the secret. Create a fine-grained personal access token scoped to this repo with Administration: write and Issues: write, then add it at Settings → Secrets and variables → Actions as `TF_GITHUB_TOKEN`. |
| Pages URL shows 404 | Settings → Pages → Source must be **GitHub Actions**, then re-run the `pages` workflow. First deploy can take a couple of minutes. |
| GHCR push denied | Settings → Actions → General → Workflow permissions → **Read and write**. |
| Markdownlint fails on something cosmetic | Either fix the file or add the rule ID to `.markdownlint-cli2.jsonc`. Ask Claude Code to decide which is more appropriate. |
| The session closed / tab closed | Cloud sessions keep running after you close the tab. Reopen `claude.ai/code` and pick the session from the sidebar. |
| The skill produced a 1.5-page resume | Tell it: "the document must be exactly 2 full pages with no trailing white space — verify by converting to PDF and counting pages, then adjust and re-verify." That verification step is in the skill; this nudges it to actually run. |
| You want the skill to invent experience | It will decline and explain. That's deliberate — misattributed experience fails background verification and collapses in interviews. Use the Key Projects route it offers instead. |

### If you get stuck anywhere

Paste this into Claude Code:

> **PROMPT**
>
> Read `SOP.md` in this repo. I'm at Part <number>, step <number>. Here's what I did and what happened: <describe it>. Tell me what to do next in simple terms, and do the parts you can do yourself.

---

## Appendix — Quick command reference

You never need to type these; Claude Code runs them. Useful for understanding what's happening, or if you ever get a real machine.

| Command | What it does |
|---|---|
| `make test` | Run the unit tests |
| `make score RESUME=x.md JD=y.md` | Score a resume against a JD |
| `make build` | Validate and package the `.skill` file |
| `make sync-docs` | Copy `skill/references/*` into `docs/` |
| `make docker` | Build the container image |
| `make run` | Serve the scorer at `localhost:8080` |
| `make k8s-local` | Deploy to a local kind cluster |

Official Claude Code docs, if you want to go deeper: `https://code.claude.com/docs/en/web-quickstart`
