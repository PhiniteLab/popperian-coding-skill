# myLiterature/review — consolidated literature reviews

**Claude writes here; the owner evaluates.** These are syntheses of the corpus recorded in
`../MANIFEST.yaml`, not summaries of individual papers.

## Shape

- Repository-wide reviews sit directly in this folder, ordered by an `NN-` prefix
  (`00-priority-monitor-register.md`, `01-...`) so the file order is the reading order.
- A review belonging to one article run goes in `review/<slug>/`, matching the run root
  the pipeline opened at `myResearch/<slug>/`.

## Rules

- **Every claim traces to a manifest entry.** A source that is cited here but absent from
  `../MANIFEST.yaml` is a broken review, not a minor omission — the manifest is what makes
  the corpus re-downloadable, so an untracked source is one nobody can check.
- **Synthesize by method family, assumption set, guarantee level and open problem** — never
  as a chronological list of papers. A list is not a review.
- **Never cite a paper that was not read.** A source seen only as a title or abstract is
  recorded as exactly that, with its verification status stated.
- **Do not delete a superseded review.** Add the new one with the next number; the earlier
  round is the baseline a later one is compared against.
