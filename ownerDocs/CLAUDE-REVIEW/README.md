# CLAUDE-REVIEW — Claude's adversarial review rounds

One folder per round, created when the round happens:

```
CLAUDE-REVIEW/
  REVIEW-1/
    00-...md … NN-...md      # the round's reports, in reading order
    evidence/                # the scripts that round actually ran
  REVIEW-2/
    ...
```

## Rules

- **A round is a unit.** Its reports and the evidence that backs them stay together; an
  evidence script that lives outside its round cannot be traced to the finding it settled.
- **Earlier rounds are the baseline.** Read them before opening a new one. A finding that a
  previous round already refuted is not a new finding, and repeating it without addressing
  the earlier refutation is a defect in the new round.
- **Executable evidence over assertion.** A finding whose support is a script in
  `evidence/` outranks one whose support is prose. Scripts are kept runnable — they are the
  reason a verdict can be re-checked months later.
- Numbered file prefixes carry the reading order; the highest-numbered file in a round is
  usually its consolidated verdict.

`CODEX-REVIEW/` mirrors this shape for the independent Codex line and is **read-only for
Claude in every repository**.
