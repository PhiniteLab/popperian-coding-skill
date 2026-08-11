# myProgression — what was believed, what was tested, what changed

The repository's accumulation area. Two kinds of file:

- **`00-scientific-progression.md`** — the cumulative ledger, one `P-` row per claim:
  claim → test → outcome → revised belief → cost. Every work unit appends its rows at
  closure. **Append only**: an entry is never rewritten, and a refutation is recorded as a
  new row that supersedes the old one rather than as an edit to it.
- **`<slug>-experiment-journal.md`** — the live observation journal an article run keeps
  while experiments are actually running. One per slug; it lives here rather than in the
  run root because the journal outlives the run.

## Why failures are first-class

The ledger is the only place that records what did **not** work. A dead end that is not
written down is re-attempted; a refuted claim that is quietly deleted looks like a claim
that was never made. `FALSIFIED` and `REFUTED` outcomes are the point of the file, not an
embarrassment to be tidied away — several of the strongest results in this workspace exist
because an earlier row recorded exactly how the previous version failed.
