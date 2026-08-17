# Research Inputs and Work Units

## Purpose

This area stores owner-provided research inputs and scoped research work units. A work unit
may be a manuscript, project, technical report, method-development effort, course design, or
other bounded research activity.

## Scope and Boundaries

### Owns

- Owner-authored notes, deep-research outputs, prompt outputs, and idea records.
- One resumable root per scoped work unit.
- Work-unit state, evidence ledger, and editable draft when the active workflow requires it.

### Does Not Own

- Repository-wide literature metadata.
- Executable experiment definitions or generated run artefacts.
- Current repository status or settled decisions.
- Global pipeline rules copied from an external toolchain.

## Inputs and Outputs

| Direction | Item | Source or Consumer | Contract |
|---|---|---|---|
| Input | Owner research input | Owner | Read-only unless the owner explicitly requests revision |
| Input | Workflow goal | Owner or approved workflow | Preserved verbatim in the work-unit state |
| Output | Scoped work unit | Manuscript, project, or report workflow | One slug, one bounded objective |
| Output | Draft and evidence ledger | Owner and reviewers | Traceable to sources and run evidence |

## Structure and Key Elements

```text
myResearch/
  inputs/                    # owner inputs; create files as IN-001-<slug>.md
  <work-slug>/
    RUN.yaml                 # workflow state and work type
    evidence/
      LEDGER.md              # evidence chain
    draft/                   # editable work product
```

Suggested owner-input identity block:

```markdown
# <Input Title>

- **ID:** IN-001
- **Date:** YYYY-MM-DD
- **Type:** owner note | research output | call analysis | other
- **Status:** raw | reviewed | incorporated
- **Related work:** <work-slug> | none
```

## Interfaces and Flow

Owner inputs may inform literature review, method development, work-unit drafts, and
scientific decisions. Work units consume repository-wide literature from
`ownerDocs/myLiterature/` and evidence from `artifacts/`; they do not duplicate either.

## Configuration, Data, and State

- `one slug = one scoped research work unit`.
- `RUN.yaml` is the only work-unit state file when an external workflow uses it.
- `work_type` should identify the unit, for example `manuscript`, `project`,
  `technical_report`, or `course_design`.
- Owner-input files use stable `IN-` IDs and descriptive filenames.

## Validation and Failure Handling

| Concern | Validation | Failure Handling |
|---|---|---|
| Two objectives share one work root | Work-unit scope audit | Split into separate slugs |
| Owner input is edited silently | Ownership audit | Restore original and create a derived note elsewhere |
| Draft cites untracked evidence | Evidence-link audit | Mark unsupported until linked |
| State is duplicated outside `RUN.yaml` | State audit | Retain one canonical state record |

## Maintenance and Related Documentation

Update this README only when the work-unit contract changes. Current work belongs in
`ownerDocs/STATUS.md`; literature belongs in `ownerDocs/myLiterature/`; scientific outcomes
belong in `ownerDocs/myProgression/`.
