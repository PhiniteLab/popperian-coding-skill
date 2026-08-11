# ownerDocs — owner documentation workspace

The owner's working area. **Structure** is standard across every repo (materialized
from the `owner-docs-scaffold` template); **content** is repo-specific and owner-owned.

| Area | Who writes | Content |
|---|---|---|
| `ownerDocs-Rules.md` | owner | the area map an agent reads first — what each folder holds |
| `00-REPO-CONTEXT.md` | owner | one page orienting an agent: what this repo is, the claim, where the truth lives |
| `STATUS.md` | owner (Claude may propose) | the present tense — what is in progress, last verified state, next actions |
| `DECISIONS.md` | owner (Claude may draft) | why the repo is the way it is; one entry per settled decision, with what was rejected |
| `myGeneralFiles/` | owner | identity, role, standing working rules (`instructions.md`, `rules.md`) |
| `myResearch/` | owner | raw research inputs: deep-research reports, prompt outputs, idea dumps |
| `myLiterature/` | owner drops PDFs · Claude maintains `MANIFEST.yaml` | corpus PDFs under `pdfs/` (gitignored) + the tracked `MANIFEST.yaml` |
| `myLiterature/review/` | Claude writes, owner evaluates | consolidated literature reviews |
| `myManuscriptRules/` | owner (binding) | academic-writing ruleset — binds all manuscript work |
| `myMethods/` | Claude writes, owner evaluates | method specs, implementation & validation plans; `evidence/` holds their verification scripts |
| `myProgression/` | Claude appends at closure | cumulative scientific-progression ledger |
| `CLAUDE-REVIEW/` | Claude | adversarial reviews, specs, verification scripts |
| `CODEX-REVIEW/` | Codex | independent reviews — **READ-ONLY for Claude** |

Empty folders are placeholders, not obligations.

**Three files answer three different questions, and keeping them apart is what stops each
from rotting into the others:** `00-REPO-CONTEXT.md` = what this repository IS (changes
rarely) · `STATUS.md` = where it stands TODAY (overwritten often, kept to one screen) ·
`DECISIONS.md` = WHY it is this way (append-only, never rewritten). Results go to
`myProgression/`, specifications to `myMethods/` — neither belongs in these three.

## Conventions

- **Review rounds.** `CLAUDE-REVIEW/` and `CODEX-REVIEW/` grow one `REVIEW-<N>/` folder per
  round, each with its own `evidence/` for the scripts that round actually ran
  (`CLAUDE-REVIEW/REVIEW-2/evidence/r2_gate_rank_probe.py`). Rounds are created when a round
  happens — the template ships the two parents empty rather than pre-creating a round nobody
  asked for.
- **Numbered files.** Owner-curated areas order by a `NN-` prefix
  (`myMethods/03-...-specification.md`, `myLiterature/review/00-priority-monitor-register.md`)
  so the reading order is the file order.
- **PDFs are gitignored, the manifest is not.** `**/myLiterature/pdfs/*.pdf` keeps the corpus
  out of git; `myLiterature/MANIFEST.yaml` stays tracked so the corpus is re-downloadable
  from it. The path is fixed by the article ruleset (`RUN.yaml → pdfManifest`).
- **The article pipeline writes INTO this workspace, it does not own it.** A research run
  (`article-research-pipeline`) opens its run root at `myResearch/<slug>/` and its shared
  literature at `myLiterature/` — this shape is their precondition.
