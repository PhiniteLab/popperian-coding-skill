# scaffold-skill — interoperability verbs (collection repository standard).
# This repository ships a Claude Agent Skill (SKILL.md, modes/, catalogs/) plus
# three standalone helper scripts under scripts/. There is no pyproject.toml,
# no installable Python package, no experiment/paper source, and no test
# suite — so several verbs below are honest no-ops that say why rather than
# faking success. See PAPER.yml and README.md for what this repo actually is.

PYTHON ?= python3

.PHONY: setup test lint type smoke falsify paper check-paths repro check clean

setup:
	@echo "setup: no-op — no pyproject.toml/package in this repo; scripts/ use only the stdlib (argparse, json, gzip, dataclasses)."

test:
	@echo "test: no-op — no tests/ suite in this repo (pytest collects 0 items, exit 5); companion evaluation lives in ../exec-refute."

lint:
	ruff check .

type:
	pyright scripts

smoke:
	$(PYTHON) -m compileall -q scripts
	$(PYTHON) -m scripts.severity --help >/dev/null
	$(PYTHON) -m scripts.mdl --help >/dev/null
	$(PYTHON) -m scripts.trace --help >/dev/null
	@echo "smoke: OK — scripts/ byte-compile and each CLI entrypoint responds to --help."

falsify:
	@echo "falsify: no-op — this repo is the studied artifact (SKILL.md, name: popperian-coding); the falsification harness that evaluates it lives in the companion repo ../exec-refute, not here."

paper:
	@echo "paper: no-op — no LaTeX source for arXiv:2606.06454 exists in this repo (latex_home: null in PAPER.yml); only a compiled PDF with no source lives at ../exec-refute/makale1.pdf."

check-paths:
	$(PYTHON) scripts/check_paths.py

repro:
	@echo "repro: no-op — no experiment/training run to reproduce in this repo; it is skill source + helper scripts, not an experiment harness."

check: lint type test check-paths

clean:
	find . -name '__pycache__' -not -path './.git/*' -exec rm -rf {} +
	rm -rf .ruff_cache .mypy_cache .pytest_cache
