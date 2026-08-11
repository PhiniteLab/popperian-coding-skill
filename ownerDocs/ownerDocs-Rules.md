# ownerDocs — area map and reading order

**Read this file first.** It states what each area of this workspace contains, who owns
it, and what an agent may do with it. The structure is standard across every repository;
the content is specific to this one.

## Precedence

The global operating contract (`~/.claude/CLAUDE.md`) is loaded on every turn in every
repository and is the live authority on language, model routing, delegation, git and
cross-model execution; where anything in this workspace conflicts with it, **the global
contract wins**. `myManuscriptRules/` is binding for manuscript work and outranks every
general convention here. A repository's own `CLAUDE.md` governs that repository's specifics.
This workspace supplies the DOMAIN and the STATE, not the operating rules.

## Reading order for an agent entering this repository

1. `00-REPO-CONTEXT.md` — what this repository is, the claim under development, where the
   real state lives, and how to run it. One page; read it before touching anything.
2. `STATUS.md` — where the work stands today: in progress, last verified state, next
   actions, what is awaiting the owner.
3. `myGeneralFiles/instructions.md` — the owner's role definition: who the owner is, what
   the working partnership is, and the standard of work expected.
4. `myGeneralFiles/rules.md` — how to work and how to answer: the operating rules that
   govern responses, process and delivery.
5. `myManuscriptRules/` — **binding** for any manuscript work in this repository. The
   English `academic-writing-skill.md` is the operative version; the `.tr.md` beside it is
   the owner's source, not the version an agent obeys.
6. `DECISIONS.md` when you are about to revisit a choice — a decision recorded there has
   already been argued, and re-opening it needs new evidence, not a fresh opinion.
7. This map, then the area you were asked about.

## Areas

| Area | Owner | What it holds | Agent's permission |
|---|---|---|---|
| `00-REPO-CONTEXT.md` | owner | what this repository is, the claim, constraints, where the truth lives | read as ground truth; propose corrections, never edit silently |
| `STATUS.md` | owner | the present tense: in progress, last verified state, next, awaiting-owner, parked | may PROPOSE an end-of-session update; the owner decides whether it lands |
| `DECISIONS.md` | owner | one append-only entry per settled decision, with what was rejected and why | may DRAFT an entry for a decision settled in session; never rewrite a settled one |
| `myGeneralFiles/` | owner | `instructions.md` (role, identity, standard) and `rules.md` (how to work, how to answer) | read as ground truth; never edit |
| `myResearch/` | owner | the owner's own research inputs: deep-research reports, prompt outputs, and the LLM-written versions of methods the owner developed. Article runs open one `<slug>/` root per idea | read; write only inside a run root the owner opened |
| `myLiterature/` | owner drops PDFs, agent maintains the manifest | the corpus as PDFs under `pdfs/` (gitignored) plus `MANIFEST.yaml`, which is tracked and is what makes the corpus re-downloadable; `usedBy` records which runs draw on each source | maintain the manifest; never delete a PDF |
| `myLiterature/review/` | agent writes, owner evaluates | syntheses of that corpus — repository-wide, or per-run in `review/<slug>/` | write; keep every claim traceable to a manifest entry |
| `myManuscriptRules/` | owner | the binding academic-writing ruleset | obey; never edit |
| `myMethods/` | agent writes, owner evaluates | every method attempted and the one being developed, in numbered order — **the highest number is the current method**; `evidence/` holds the scripts that verified them | write with the owner's approval; never renumber history |
| `myProgression/` | agent appends at closure | the cumulative ledger: claim → test → outcome → revised belief → cost. Dead ends and refutations are first-class entries | append only; never rewrite an entry |
| `CLAUDE-REVIEW/` | Claude | Claude's adversarial reviews, one `REVIEW-<N>/` per round with its own `evidence/` | write; use earlier rounds as the comparison baseline |
| `CODEX-REVIEW/` | Codex | Codex's independent reviews, same round shape | **READ-ONLY for Claude, always, in every repository** |

## Standing rules

- **Prior reviews are the baseline, not archive.** `CLAUDE-REVIEW/` and `CODEX-REVIEW/`
  exist so a new round can be compared against what was already found. Read the previous
  round before opening a new one; a finding that was already refuted is not a new finding.
- **The current method is the last one.** In `myMethods/`, the highest-numbered
  specification supersedes the ones below it. Never present an earlier version as current.
- **Numbered files carry their reading order.** A `NN-` prefix means the file order is the
  intended order.
- **The owner fills the owner columns.** Where the table says *owner*, an agent reads and
  never writes — including when the area is empty. An empty folder is a placeholder, not
  an invitation.
