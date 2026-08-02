# scaffold-skill

> On disagreement between this README and [`PAPER.yml`](PAPER.yml), `PAPER.yml` wins.

| bucket | arXiv | role | former names | former GitHub slug |
|---|---|---|---|---|
| published | [2606.06454](https://arxiv.org/abs/2606.06454) | studied-artifact | popperian-coding-skill | PhiniteLab/popperian-coding-skill |

This repository is named **scaffold-skill**. The Claude Agent Skill it contains
keeps its own registered identity, **`popperian-coding`** (see `SKILL.md`'s
`name:` field) — that identity is frozen because a byte-identical copy of the
skill is vendored into the companion evaluation repository, and it is the name
under which the companion paper studies and reports on the skill. The two
names are deliberately different: **repo = scaffold-skill, skill = popperian-coding.**

A Claude **coding skill** that switches a code agent from *verification*
("does my answer look right?") to *falsification* ("what severe test would break
my answer if it were wrong?").

It applies to four coding modes — code review, code generation, task
verification, and test construction — and enforces six invariants: an explicit
conjecture inventory, mandatory severity scores, oracle independence, an
MDL-based ad-hoc-rescue blocker, abstention as a first-class outcome, and a
versioned run trace. Outputs are labelled `corroborated(κ=…)`, `partial`,
`refuted`, or `abstain` — never "verified", "done", or "LGTM".

## What is in this repository

| Path | Purpose |
|------|---------|
| `SKILL.md` | Skill entry point: frontmatter, the six invariants, output-label discipline, and the mode router. |
| `modes/` | The four mode protocols: `generation.md`, `review.md`, `verification.md`, `test_construction.md`. |
| `scripts/` | Helper tools called from the modes: `severity.py` (test-severity estimate), `mdl.py` (ad-hoc-rescue detector), `trace.py` (run-trace appender). |
| `catalogs/` | Bug-class catalogue, domain checklists, and mutation operators used by the planner steps. |
| `LICENSE` | MIT. |

## How it works

Every output decomposes into named atomic claims (C1, C2, …). Each claim is
attacked by a severity-scored *severe test* run against a tool oracle — a test
runner, mutation runner, sandbox, or SAST — never the same model instance that
produced the answer. A claim is reported as surviving only after passing its
severe tests; a revision that merely swallows a failing input is blocked by a
minimum-description-length check (`scripts/mdl.py`). When the specification is
ambiguous, the acceptance criteria are missing, or no oracle exists, the skill
returns a first-class `abstain(reason=…, blocking_question=…)` instead of a
best-effort guess.

## Using it with Claude

This is a [Claude Agent Skill](https://docs.claude.com/en/docs/claude-code/skills).
Place the directory under your skills location — named after the **skill's**
registered identity (`SKILL.md`'s `name: popperian-coding`), not after this
**repository's** name — for example `~/.claude/skills/popperian-coding/`, so
that `SKILL.md` and its `modes/`, `scripts/`, and `catalogs/` sit together.
The install directory name must match `SKILL.md`'s `name:` field exactly; it
is unrelated to the fact that this repository itself is called
`scaffold-skill`. The agent enters the appropriate mode through the
`mode_router` patterns declared in `SKILL.md`.

## Companion paper

This skill is the **object of study** in a controlled, pre-registered evaluation:

> **Scaffold, Not Vocabulary? A Controlled, Two-Tier, Pre-Registered Study of a
> Popperian Code-Generation Skill.** Mehmet İşcan, PythaLab / Yıldız Technical
> University, Istanbul, Turkey.

The paper reports a **calibrated negative result**. Under HumanEval+
execution-oracle evaluation, on Claude Sonnet 4.6 (via the Claude Code agentic
serving path) and Qwen2.5-Coder-0.5B (local Ollama), the full skill showed *no
separable execution-correctness benefit* over a labels-only scaffold of the same
structure: the measurable best-of-eight gains tracked scaffold *structure* rather
than the incremental Popperian procedural content, and a same-model self-judge
did not beat random selection among its own samples. The result bounds a specific
engineering claim about this skill family under the tested conditions; it is not
an evaluation of Popperian methodology in general. We release the skill so that
the result can be reproduced and the controlled-evaluation protocol
(placebo + labels-only + execution oracle + halo sentinel) re-used.

Preprint: [arXiv:2606.06454](https://arxiv.org/abs/2606.06454).

## License

MIT — see [`LICENSE`](LICENSE).
