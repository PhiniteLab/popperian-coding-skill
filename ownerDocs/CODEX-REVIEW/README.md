# CODEX-REVIEW — the independent Codex review line

Same round shape as `CLAUDE-REVIEW/`:

```
CODEX-REVIEW/
  REVIEW-1/
    00-review-index.md … NN-...md
    evidence/
  REVIEW-2/
    ...
```

## READ-ONLY for Claude, in every repository, always

This area exists to hold a review that Claude did **not** write. Its value is precisely
that it was produced by a different model against the same target — an independent
perspective is the only thing that catches an error the whole Claude line shares. Claude
reads these reports, compares its own findings against them, and cites them; Claude never
writes, edits, reorganises, or "corrects" a file here. A Codex verdict that Claude
disagrees with is answered in `CLAUDE-REVIEW/`, with evidence — not amended in place.
