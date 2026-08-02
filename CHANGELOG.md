# Changelog

All notable changes to this repository are recorded here.

## Unreleased

### Changed

- Repository renamed and relocated: was `popperian-coding-skill` at
  `PhiniteLab/popperian-coding-skill`, now `scaffold-skill` at
  `PhiniteLab/scaffold-skill`. The skill contained in this repository keeps
  its own registered identity, `popperian-coding` (`SKILL.md`'s `name:`
  field, byte-identical to the vendored copy in the `exec-refute` companion
  repository) — only the repository and GitHub slug changed, not the skill.
- Adopted the collection repository standard: `PAPER.yml` identity card,
  `CITATION.cff`, README status block, `Makefile` interoperability verbs,
  `scripts/check_paths.py` path-safety gate, `ownerDocs/` workspace
  skeleton, `.editorconfig`, `.gitignore`, and a name-agnostic CI workflow.

## 0.1.0 — 2026-06-04

- Initial release: the `popperian-coding` Claude Agent Skill —
  falsification-over-verification coding scaffold with four modes
  (`review`, `generation`, `verification`, `test_construction`), six
  invariants, and the `severity.py` / `mdl.py` / `trace.py` helper scripts.
