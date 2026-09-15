# Security policy

Vriddhih is a static site with no server, no accounts and no stored user data. Its attack surface is the browser code, the content and data files, and the build pipeline.

## Reporting a vulnerability

Please do not open a public issue for security problems. Use GitHub's private vulnerability reporting on this repository ("Security" tab → "Report a vulnerability"). You will get an acknowledgement within seven days.

## In scope

- Cross-site scripting or injection through pasted text, share links or data files
- Leaking of an AI provider key from browser storage, URLs or logs
- Prompt-injection paths that make model output trigger an action
- Supply-chain issues in GitHub Actions, the container image or pinned runtime scripts
- Incorrect Content-Security-Policy or missing input caps

## Out of scope

- Behaviour of third-party AI providers or hosting platforms
- Issues that require a compromised device or browser
- Accuracy of scores, questions or salary ranges (open a normal issue for these)

## No bounty

This is a free volunteer project. Reports are credited in the changelog if you wish.
