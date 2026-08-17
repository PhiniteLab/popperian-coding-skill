# Methods

## Purpose

This area preserves every material method version, its validation plan, and the explicit
registry that identifies the current method. It records scientific design evolution without
storing executable validation code.

## Scope and Boundaries

### Owns

- Method specifications.
- Method-specific assumptions, notation, interfaces, and failure conditions.
- Validation plans that define decisive tests and acceptance criteria.
- A registry with exactly one current method.

### Does Not Own

- Executable tests, experiment protocols, or verification scripts.
- Generated evidence or metrics.
- Present-tense work status.
- Implementation code.

## Inputs and Outputs

| Direction | Item | Source or Consumer | Contract |
|---|---|---|---|
| Input | Literature and owner constraints | Literature and context | Assumptions and gaps remain explicit |
| Input | Prior failures and decisions | Progression and decisions | New method addresses known failure modes |
| Output | Method specification | Implementation and experiments | Complete, dimensionally consistent, falsifiable |
| Output | Validation plan | Tests and experiment protocols | Measurable success and failure criteria |

## Structure and Key Elements

Naming convention:

```text
M-001-<name>-specification.md
M-001-<name>-validation.md
M-002-<name>-specification.md
M-002-<name>-validation.md
```

Method registry:

| ID | Status | Specification | Validation Plan | Implementation | Evidence |
|---|---|---|---|---|---|
| <!-- M-XXX --> | <!-- proposed/current/etc. --> | <!-- file --> | <!-- file --> | <!-- path or pending --> | <!-- path or pending --> |

Allowed status values:

```text
proposed
under_validation
current
superseded
rejected
```

## Interfaces and Flow

Literature, context, decisions, and progression inform a method specification. The
specification guides implementation under `src/`; the validation plan is executed through
`tests/scientific/` and `experiments/`; produced evidence remains under `artifacts/` and is
linked through `REPO-INFO/TRACEABILITY.md`.

## Configuration, Data, and State

- Exactly one method may be `current`.
- Method IDs are stable and never reused.
- Earlier method files remain unchanged.
- A new registry row declares which method is superseded; history is not rewritten.
- Runtime values belong in `configs/`, not in method specifications unless they define a
  scientific invariant or declared experimental constant.

## Validation and Failure Handling

| Concern | Validation | Failure Handling |
|---|---|---|
| More than one current method | Registry validation | Fail until authority is resolved |
| Current method lacks validation plan | Completeness audit | Treat as proposed, not current |
| Method references missing evidence | Path validation | Mark evidence pending or invalid |
| Executable script is stored here | Boundary audit | Move to tests, experiments, or scripts/audits |
| Superseded file is rewritten | History audit | Restore and create a new method version |

## Maintenance and Related Documentation

Update the registry only when method status or canonical pointers change. Append new method
files; do not renumber or delete history. Record belief changes in `myProgression/` and
settled selection decisions in `DECISIONS.md`.
