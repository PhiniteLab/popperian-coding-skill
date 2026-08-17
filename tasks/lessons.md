# Lessons — this repository only

**This file is a legend, not a form.** There is no placeholder entry below to fill in, and that
is deliberate: every lessons-class file in this stack's history that received zero writes
arrived as a pre-seeded template with empty slots. A form invites being left blank. The first
real entry is the first content.

Entries are APPENDED, never rewritten, and never hand-written. Use the writer, which REFUSES
rather than warns:

```bash
python3 ~/.claude/bin/ledger.py --repo . append --from-json -
python3 ~/.claude/bin/ledger.py --repo . validate
```

The writer is DEPLOYED, not repo-local, so it works in every repository. This file used to name
`scripts/ledger.py`, which exists only inside the agent stack — every other repository could
therefore hold lessons it had no way to write.

## How this file is read back

Writing is half of it. A ledger nobody reads is an archive, not a memory — this stack shipped
one for months with three writers and no reader. Three hooks now read this file:

| When | What you get |
|---|---|
| Session start | the durable `principle` / `constraint` claims, ranked and capped |
| You edit a file a lesson names | that lesson, once per session |
| **A tool call fails** | any lesson whose text matches the failure — never throttled |

After compaction the session-start digest is re-armed on the next prompt. An entry that is
`FALSIFIED`, or that carries `superseded-by:` because a check now enforces it, is not injected:
the file grows, the injection does not.

## Entry shape

```
### L-003 · finding · HOLDS · 2026-08-17
**claim:** one line, under 200 characters — what is true
**evidence:** a repo-relative path that resolves
**interpretation:** what it MEANS, what it changes, what follows
**from:** T-2026-08-17-a
```

| Field | Rule |
|---|---|
| `type` | `defect` · `finding` · `principle` · `decision` · `constraint` — closed set |
| `verdict` | `HOLDS` · `FALSIFIED` · `INCONCLUSIVE` · `OBSERVED` — closed set |
| `claim` | non-empty, ≤ 200 characters |
| `evidence` | **a repo-relative path that actually exists.** The strongest anti-filler rule there is: a vague recollection cannot name a file |
| `interpretation` | **required for `finding` and `principle`**, and must be anchored to a number or an explicit condition. Finding the defect is not the deliverable; reading it is |
| `from` | a `T-…` block id in `tasks/todo.md`; the writer refuses an id that matches no block |

## Why the bar is a script and not a judgement call

Both ends of "how strict should this be" are measured failures in this corpus. The strictest
prose schema in the stack holds ZERO entries after months. The one store with no schema at all
accumulated 19 entries of which 19 were raw JSON transcript fragments — 249 KB of debris that
still looked like a record. So the bar is decidable by a script, and the writer drops the entry
rather than logging a warning nobody reads.

**"No entry" is a valid and expected outcome.** A hook records candidate events and hands them
over on the next prompt; ruling "nothing worth keeping here" in one line is a correct answer, not
a skipped step.
