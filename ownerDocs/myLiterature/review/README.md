# Literature Reviews

## Purpose

This area stores traceable syntheses of the literature corpus. Reviews compare method
families, assumptions, models, protocols, guarantee levels, limitations, and open problems;
they are not chronological lists of paper summaries.

## Scope and Boundaries

### Owns

- Repository-wide literature syntheses.
- Work-specific review folders keyed by work slug.
- Source-supported comparison matrices and research-gap analyses.

### Does Not Own

- Unmanifested sources.
- Manuscript sections copied from a review.
- Method specifications or experimental results.
- Claims supported only by title or abstract when full-text evidence is required.

## Inputs and Outputs

| Direction | Item | Source or Consumer | Contract |
|---|---|---|---|
| Input | Manifested source | `../MANIFEST.yaml` | Referenced by stable `L-` ID |
| Input | Verified source content | Corpus reviewer | Verification state remains explicit |
| Output | Synthesis | Methods, projects, manuscripts | Every factual claim traces to source IDs |
| Output | Research gap | Owner and method workflow | Conditions and limitations are explicit |

## Structure and Key Elements

- Repository-wide syntheses live directly in this folder.
- Work-specific syntheses live in `review/<work-slug>/`.
- Numbered prefixes may be used when a fixed reading order is required.
- Superseded reviews remain available as the comparison baseline.

## Interfaces and Flow

A review consumes only manifested sources and produces a synthesis that can inform method
specifications, hypotheses, project objectives, and manuscript framing. It never converts a
low-verification source into a high-confidence claim.

## Configuration, Data, and State

This area has no runtime configuration. Source identity and verification state are read from
`../MANIFEST.yaml`. Review files use repository-relative links and stable source IDs.

## Validation and Failure Handling

| Concern | Validation | Failure Handling |
|---|---|---|
| Review cites unknown `L-` ID | Source-reference check | Mark claim unsupported |
| Literature is listed paper by paper | Synthesis-quality review | Restructure by method family or assumption set |
| Verification level is omitted | Evidence audit | Add the exact status |
| Superseded review is deleted | History audit | Restore from Git and add a new review instead |

## Maintenance and Related Documentation

Update a review when the corpus or interpretation changes. Do not rewrite scientific history
silently; preserve earlier syntheses when they are needed as review baselines.
