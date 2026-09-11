.PHONY: test lint score build sync-docs docker run k8s-local clean

PY ?= python3
JD ?= examples/sample_jd.md
RESUME ?= examples/sample_resume.md

test:            ## run unit tests
	$(PY) -m pytest -q

lint:            ## markdown + yaml lint (needs npx / yamllint)
	npx --yes markdownlint-cli2 "skill/**/*.md" "docs/**/*.md" README.md
	yamllint -d relaxed .github k8s

score:           ## score RESUME against JD (make score RESUME=me.md JD=jd.md)
	$(PY) scripts/score_resume.py --resume $(RESUME) --jd $(JD)

build:           ## validate + package the .skill file into dist/
	$(PY) scripts/build_skill.py

sync-docs:       ## copy skill references into docs/ so both stay identical
	cp skill/references/*.md docs/

docker:          ## build the scorer image
	docker build -t resume-scorer:local .

run: docker      ## run the scorer at http://localhost:8080
	docker run --rm -p 8080:8080 resume-scorer:local

k8s-local:       ## deploy to a local kind cluster
	kind create cluster --name dev || true
	docker build -t resume-scorer:ci . && kind load docker-image resume-scorer:ci --name dev
	kubectl apply -k k8s/ && kubectl set image deployment/resume-scorer web=resume-scorer:ci
	kubectl rollout status deployment/resume-scorer

clean:
	rm -rf dist site .pytest_cache
