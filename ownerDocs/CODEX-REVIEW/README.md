# Codex Reviews

## Purpose

This area stores independent Codex review rounds against the same repository target. Its
value is independence from the Claude implementation and review line.

## Scope and Boundaries

### Owns

- Codex-produced review rounds and their evidence.
- Independent findings, verdicts, risks, and required actions.

### Does Not Own

- Claude-authored corrections or reinterpretations.
- Reusable repository tests or method specifications.
- Present repository status.

## Inputs and Outputs

| Direction | Item | Source or Consumer | Contract |
|---|---|---|---|
| Input | Explicit review target | Owner or approved cross-model workflow | Same target state as comparison review |
| Input | Executed evidence | Codex or repository artefacts | Verification status stated |
| Output | Independent verdict | Owner and Claude review line | Preserved without Claude editing |
| Output | Contradictions and risks | Owner | Compared through evidence, not silent amendment |

## Structure and Key Elements

```text
CODEX-REVIEW/
  REVIEW-001/
    README.md
    evidence/                 # only when round-specific evidence exists
```

The round README follows the same headings as a Claude round: Scope, Target State, Previous
Baseline, Findings, Evidence, Verdict, Unresolved Risks, and Required Actions.

## Interfaces and Flow

Claude may read, cite, compare, and answer a Codex verdict in `CLAUDE-REVIEW/`. Claude never
writes, edits, reorganises, or corrects a file in this area.

## Configuration, Data, and State

This area is read-only for Claude in every repository. Round numbering is sequential and
independent of Claude round numbering.

## Validation and Failure Handling

| Concern | Validation | Failure Handling |
|---|---|---|
| Claude-authored modification detected | Ownership audit | Restore independent content |
| Review target differs from comparison target | Target-state audit | Declare non-comparability |
| Verdict lacks evidence | Evidence audit | Mark as unverified opinion |
| Closed round is rewritten | History audit | Restore and open a new round |

## Maintenance and Related Documentation

Only the independent Codex workflow writes here. Accepted changes are implemented and
recorded in their canonical repository locations rather than by editing the review.
