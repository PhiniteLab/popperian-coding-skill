# myLiterature — the repository-wide literature pool

**Shared across every article run in this repository.** A second `<slug>` does not get a
second corpus; it reuses this one and records its use in the manifest. Nothing here is
run-specific except the per-slug reading-note folder.

```
myLiterature/
  MANIFEST.yaml         # TRACKED — one entry per PDF: bibliographic record, DOI, usedBy: [slug…]
  pdfs/
    *.pdf               # GITIGNORED — the corpus itself, never committed
  review/
    <slug>/             # work-specific reading notes for one run
    *.md                # repository-wide syntheses (priority monitors, source matrices)
```

Paths and file names follow the article ruleset (`PIPELINE.md` § 9 item 4; `RUN.yaml`
declares `pdfManifest: ownerDocs/myLiterature/MANIFEST.yaml`). They are a contract, not a
preference — a run that cannot find `MANIFEST.yaml` at that exact path cannot resolve its
own corpus.

## The manifest is the contract

`pdfs/*.pdf` is excluded by `**/myLiterature/pdfs/*.pdf` in the repository's `.gitignore`,
so the PDFs never enter git. `MANIFEST.yaml` **does**, and it is therefore the only record
that survives a fresh clone. A PDF with no entry is invisible to every later step: it
cannot be cited, cannot be re-downloaded, and will not appear in any review.

Each entry carries the file name, the title as printed on page 1, the venue and year, the
DOI or arXiv id, the role that source plays in this repository's argument, and `usedBy` —
the run slugs that draw on it. `usedBy` is what makes the pool cumulative: a second article
that needs the same paper appends its slug instead of re-downloading it.

## Reviews

`review/` holds the syntheses an agent writes and the owner evaluates. Every claim in a
review traces back to a manifest entry — a review sentence with no traceable source is a
defect, not a shortcut. Per-run reading notes live in `review/<slug>/`; repository-wide
syntheses sit directly in `review/`.
