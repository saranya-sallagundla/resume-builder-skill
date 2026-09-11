# Tonight's runbook — zero installs, browser only

Nothing goes on the laptop. Everything runs in GitHub's browser tools: the web UI, **Codespaces** (a Linux VM in a tab, 60 free hours/month), and Actions. When you return the laptop you lose nothing; sign in from any device and continue.

Time: 60–90 min for phases 1–3, then your resume.

Before you start: confirm your company's acceptable-use policy allows personal GitHub in the browser. Don't sync company files into this repo.

## 1. Create the repo (3 min)

1. github.com → **New repository** → name `resume-builder-skill` → Public → do **not** add README/license → Create.
2. Copy your username; you'll need it in step 3.

## 2. Open a Codespace (3 min)

On the empty repo page: **Code → Codespaces → Create codespace on main**. A VS Code window opens in the browser with a terminal. Wait for it to finish setting up (a minute).

## 3. Get the project files in (5 min)

In the Codespace: drag `resume-builder-skill.zip` from your Downloads onto the file explorer panel (left side). Then in the terminal:

```bash
unzip -q resume-builder-skill.zip && cp -r repo/. . && rm -rf repo resume-builder-skill.zip
grep -rl saranya-sallagundla . | xargs sed -i "s/saranya-sallagundla/$GITHUB_USER/g"
```

(`$GITHUB_USER` is set automatically in Codespaces.)

The repo now contains `.devcontainer/` — **rebuild once** so Docker, kind, kubectl and Terraform get installed inside the VM: press `F1` → *Codespaces: Rebuild Container*. Takes 2–3 minutes.

## 4. Local sanity check — inside the Codespace (5 min)

```bash
make test        # 13 tests pass
make score       # sample resume ≈ 94 / 100
make build       # dist/resume-builder.skill
make docker      # builds the image — Docker runs in the Codespace, not on your laptop
```

Optional but satisfying: `make run`, then click the port-8080 popup — your scorer is running in a container.

## 5. Commit in phases and push (15 min)

Git is pre-authenticated in Codespaces. Commit in this order so the history tells a story:

```bash
git add LICENSE .gitignore README.md CONTRIBUTING.md CHANGELOG.md .devcontainer
git commit -m "docs: project charter, license, contribution rules and dev container"

git add skill docs
git commit -m "feat(skill): resume-builder skill with playbooks, rubric, regional conventions"

git add scripts examples tests requirements-dev.txt Makefile
git commit -m "feat(scorer): heuristic 100-point scorer with golden-file regression tests"

git add .github/workflows/ci.yml .markdownlint-cli2.jsonc .pre-commit-config.yaml .github/CODEOWNERS .github/PULL_REQUEST_TEMPLATE.md .github/ISSUE_TEMPLATE
git commit -m "ci: lint, test, skill validation and score regression gate"
git push -u origin main
```

Open the **Actions** tab in another browser tab: `ci` should go green in ~1 minute. If markdownlint flags something cosmetic, fix it or add the rule ID to `.markdownlint-cli2.jsonc`.

Continue, each as its own commit:

```bash
git add web .github/workflows/pages.yml && git commit -m "feat(web): browser scorer, deployed to GitHub Pages"
git add Dockerfile .dockerignore .github/workflows/docker.yml && git commit -m "build: nginx image with Trivy scan, published to GHCR"
git add k8s .github/workflows/k8s-test.yml && git commit -m "feat(k8s): manifests validated on a kind cluster in CI"
git add terraform .github/workflows/terraform.yml && git commit -m "infra: manage repo settings with Terraform"
git add .github/workflows/codeql.yml .github/dependabot.yml docs/adr-001-scorer-parity.md && git commit -m "sec: CodeQL analysis and Dependabot updates"
git add SETUP_TONIGHT.md && git commit -m "docs: browser-only setup runbook"
git push
```

## 6. Switch on the free features — web UI (10 min)

Repo **Settings**:

1. **Pages** → Build and deployment → Source: *GitHub Actions*. Then Actions tab → `pages` → *Run workflow*. Live at `https://<username>.github.io/resume-builder-skill/`.
2. **Actions → General** → Workflow permissions: *Read and write permissions*.
3. **Code security** → enable Dependabot alerts + security updates, secret scanning.
4. **General** → tick Discussions.
5. **Branches** → Add rule for `main` → require status checks `ci / test`, `ci / lint`.

First release (in the Codespace terminal):

```bash
git tag v0.1.0 && git push --tags
```

The `package` workflow attaches `resume-builder.skill` to a GitHub Release.

Create 3–5 issues with label `good first issue` from the **Issues** tab (templates are ready): "Playbook: Product Manager (US)", "Regional conventions: Japan", "Add demo GIF to README", "Scorer: better passive-voice detection".

## 7. Your resume (20 min)

1. Download `resume-builder.skill` from the Release page → in Claude.ai drop it into a chat → **Save skill**.
2. Paste a real JD + your current resume: *"Tailor my resume to this JD."*
3. Expect: gap analysis → ≤ 5 questions → verified .docx → rubric score → defend notes → upskilling list → LinkedIn mirror.
4. Paste the final text into your live scorer page; screenshot before and after. That pair (anonymized) becomes the README hero.

## 8. Stop the Codespace

Codespaces auto-stop after 30 idle minutes, but to protect your free hours: **Code → Codespaces → ⋯ → Stop codespace** when done. Delete it entirely any time — everything is in git.

## Later this week (optional, still zero-install)

- **Kubernetes for real**: in the Codespace, `make k8s-local` — kind cluster, kustomize apply, rollout, all inside the VM.
- **Terraform**: create a fine-grained PAT (this repo only; Administration: write, Issues: write) → repo **Settings → Secrets → Actions** → `TF_GITHUB_TOKEN`. The `terraform` workflow then plans on PRs and applies on merge. Or run `terraform plan` in the Codespace with `GITHUB_TOKEN` exported.
- **Branches + PRs**: from now on, `git checkout -b feat/...` → push → open PR → watch checks → merge. The protection rule and PR template start earning their keep.
- **Demo GIF**: record the scorer page with any browser-based recorder (e.g. the Loom or Screenity extensions, or Windows' built-in `Win+G` game bar if allowed), save as `docs/demo.gif`.

## Interview lines each badge earns

| Badge | Sentence you can defend |
|---|---|
| ci | "Every PR runs lint, tests and a score regression gate; a rubric change that lowers the golden sample fails the build." |
| docker | "Multi-stage image, non-root nginx, Trivy scan on every build, published to GHCR." |
| k8s-test | "CI spins up a kind cluster, applies kustomize manifests with probes and resource limits, smoke-tests through the Service." |
| terraform | "Branch protection, labels and topics are declared in Terraform; plans post to the PR, apply on merge." |
| codeql | "Static analysis on Python and JavaScript weekly and per PR; Dependabot pins actions, pip, docker and terraform." |
| devcontainer | "The whole toolchain is defined in a dev container — any contributor gets an identical environment in one click." |
