# Claude Reviews

## Purpose

This area stores Claude's adversarial review rounds and the evidence specific to each round.
Earlier rounds remain the comparison baseline for later reviews.

## Scope and Boundaries

### Owns

- One `REVIEW-<NNN>/` folder per completed or active Claude review round.
- The review scope, findings, evidence, verdict, unresolved risks, and required actions.
- Round-specific probes that are not reusable repository verification assets.

### Does Not Own

- Independent Codex reviews.
- Reusable scientific tests or experiment protocols.
- Method specifications or present repository status.

## Inputs and Outputs

| Direction | Item | Source or Consumer | Contract |
|---|---|---|---|
| Input | Review target and prior baseline | Repository and prior rounds | Target state is explicit |
| Input | Executed evidence | Round evidence or repository artefacts | Verification status stated |
| Output | Review verdict | Owner and implementation workflow | Findings are actionable and evidence-linked |
| Output | Required actions | Status, decisions, methods, or code | File ownership and validation defined |

## Structure and Key Elements

```text
CLAUDE-REVIEW/
  REVIEW-001/
    README.md
    evidence/                 # only when round-specific evidence exists
```

Round README headings:

```text
Scope
Target State
Previous Baseline
Findings
Evidence
Verdict
Unresolved Risks
Required Actions
```

## Interfaces and Flow

A new round reads relevant previous Claude and Codex rounds, inspects the current target,
executes or references evidence, and produces a verdict. Reusable validation assets are
promoted to `tests/`, `experiments/`, or `scripts/audits/` instead of remaining here.

## Configuration, Data, and State

Review rounds are numbered sequentially. A round is immutable after closure except for a
clearly labelled factual correction. The highest number is the latest round, not necessarily
the most authoritative result.

## Validation and Failure Handling

| Concern | Validation | Failure Handling |
|---|---|---|
| Finding repeats a resolved issue | Baseline comparison | Explain new evidence or remove duplication |
| Finding lacks evidence | Evidence audit | Mark as hypothesis or remove definitive verdict |
| Reusable test remains round-local | Asset audit | Promote to canonical verification area |
| Closed round is rewritten | History audit | Restore and open a new round |

## Maintenance and Related Documentation

Create a round only when a review occurs. Update `STATUS.md`, `DECISIONS.md`, methods,
traceability, or source files separately when the review leads to accepted changes.
