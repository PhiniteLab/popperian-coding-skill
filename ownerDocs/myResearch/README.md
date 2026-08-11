# myResearch — the owner's research inputs, and the article run roots

Two kinds of thing live here, and they do not mix.

## 1. Free-standing owner inputs (flat files)

Deep-research reports, prompt outputs, idea dumps, the LLM-written versions of methods the
owner developed. Numbered by arrival: `deep-research-report-1.md`, `prompt-output-3.md`.
These are **owner-authored ground truth** — an agent reads them and never edits them.

## 2. Article run roots (`<slug>/`)

The S00–S16 article research pipeline opens **one run root per article idea**, and
everything belonging to that work lives inside it:

```
myResearch/<slug>/
  RUN.yaml              # the run state: active step, goal contract, carry-outputs
  evidence/
    LEDGER.md           # the evidence chain — one row per step
    <per-step evidence files>
  draft/                # the manuscript being built
```

Conventions that make a run resumable:

- **One slug = one article = one root.** A second idea gets a second slug, never a branch
  inside an existing root.
- `RUN.yaml → active` names the step the run is on. It is the only place that says so.
- `goal.raw` is the owner's own sentence, copied verbatim and never rewritten.
- The run root is created by the pipeline, not by the scaffold — this workspace only
  guarantees that `myResearch/` exists for it to open into.

The pipeline's ruleset (step files, `RUN.yaml`/`LEDGER.md` templates) is **not** copied
here: it lives outside every repository as a single source of truth, and the run reads it
step by step. See the `article-research-pipeline` skill.
