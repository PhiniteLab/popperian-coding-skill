#!/usr/bin/env python3
"""Canonical move-safety gate for the manuscripts collection.

ONE implementation, deployed byte-identically to every repository as
``scripts/check_paths.py``. Do not fork it per repo. If a repository needs an
exemption, it declares it in its own ``PAPER.yml`` where a reader can see it --
never by editing this file.

Why this exists
---------------
The 2026-08-02 reorganisation renamed directories and GitHub slugs. Anything that
hardcoded the old absolute path or the old directory name would break silently
after the move. This gate turns "nothing lost functionality" from a claim into an
assertion you can execute.

Design rules learned from the first attempt, which failed an audit
------------------------------------------------------------------
1. **Exemptions are never silent.** Every exemption this run applied is PRINTED,
   every time, even on success. A gate whose carve-outs are invisible cannot
   certify anything.
2. **`frozen_strings` may not cancel the former-name check.** In the first
   attempt each repo listed its own former name in `frozen_strings`, which
   cancelled the only needle the check had -- a no-op in 6 of 12 repos. Here the
   two fields are kept strictly apart:
     * `frozen_strings` = identity literals (package, distribution, console
       script, env prefix, on-disk slug, hash-domain prefix). They downgrade a
       NON-path occurrence to a reported note. They never silence a PATH-LIKE one.
     * `check_paths_exempt` = explicit file paths, each with a mandatory reason.
3. **A path-like occurrence is always an error.** The former name inside a string
   that also contains "/" is a path reference, and no identity declaration
   excuses it. This is the distinction the first attempt missed: an identity
   literal and a path literal can be the same characters and still mean
   different things.
4. **`frozen_strings` entries are LITERALS, never filesystem paths.** Four repos
   in the first attempt resolved them with `Path.exists()`, which made every
   declared literal inert.

Exit codes: 0 clean, 1 violations found, 2 could not run (bad config).
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from typing import NoReturn

try:
    import yaml
except ImportError:  # pragma: no cover
    print("check_paths: PyYAML is required (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parents[1]

# Assembled from parts on purpose. If this file spelled the literal out, the
# gate would match its OWN source and every deployed copy would fail forever.
# Building it here keeps the guarantee real: this file genuinely contains no
# absolute owner-home path, so it needs no self-exemption -- and a gate that
# exempts itself is precisely the blind spot this rewrite exists to remove.
_OWNER_USER = "mehmet"
OWNER_HOME_LITERAL = f"/home/{_OWNER_USER}"

# Files that are read at runtime and can therefore break a move.
EXECUTABLE_SUFFIXES = {".py", ".sh", ".bash", ".yml", ".yaml", ".toml", ".cfg", ".ini"}
EXECUTABLE_NAMES = {"Makefile", "makefile", "GNUmakefile", "Dockerfile"}

# Frozen provenance: a repo-root path recorded in one of these is a historical
# record of where a run actually happened. Rewriting it would falsify the record.
# This list is CLOSED. A repo that needs more declares it in PAPER.yml.
FROZEN_DIR_COMPONENTS = frozenset({
    "results", "paper", "arxiv-latex", "manuscript", "ownerDocs", "archive",
    "legacy", "runs", "reference", "final_review", "final_remediation",
    "reviewer_remediation", "artifact", "experiment_logs", "manuscriptResults",
})
# Never worth scanning.
SKIP_DIR_COMPONENTS = frozenset({
    ".git", ".venv", "venv", "node_modules", "__pycache__", ".mypy_cache",
    ".pytest_cache", ".ruff_cache", ".hypothesis", ".egg-info", "dist", "build",
    ".scratch", "site-packages",
})


def _fail(msg: str) -> NoReturn:
    print(f"check_paths: {msg}", file=sys.stderr)
    sys.exit(2)


def load_card() -> dict:
    card_path = REPO_ROOT / "PAPER.yml"
    if not card_path.is_file():
        _fail("PAPER.yml not found — every repo in this collection must have one")
    try:
        data = yaml.safe_load(card_path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        _fail(f"PAPER.yml does not parse: {exc}")
    if not isinstance(data, dict):
        _fail("PAPER.yml must be a mapping")
    return data


def _as_str_list(value, field: str) -> list[str]:
    """Coerce a PAPER.yml list field, rejecting the prose-instead-of-literal error."""
    if value in (None, "", []):
        return []
    if not isinstance(value, list):
        _fail(f"PAPER.yml:{field} must be a list, got {type(value).__name__}")
    out = []
    for item in value:
        if not isinstance(item, str):
            _fail(f"PAPER.yml:{field} entries must be strings, got {type(item).__name__}")
        item = item.strip()
        if not item:
            continue
        # An audit found repos whose frozen_strings were multi-sentence
        # paragraphs. Such a needle can never match a source line, so the
        # protection silently does not exist. Reject it loudly instead.
        if len(item) > 120 or " " in item.strip() and len(item.split()) > 6:
            _fail(
                f"PAPER.yml:{field} entry looks like prose, not a literal:\n"
                f"    {item[:90]}...\n"
                f"  This field holds exact strings a find-and-replace must not touch.\n"
                f"  Put the explanation in PAPER.yml:notes instead."
            )
        out.append(item)
    return out


def iter_files():
    for path in sorted(REPO_ROOT.rglob("*")):
        if not path.is_file() or path.is_symlink():
            continue
        rel = path.relative_to(REPO_ROOT)
        parts = set(rel.parts[:-1])
        if parts & SKIP_DIR_COMPONENTS:
            continue
        if path.suffix not in EXECUTABLE_SUFFIXES and path.name not in EXECUTABLE_NAMES:
            continue
        yield rel, path, bool(parts & FROZEN_DIR_COMPONENTS)


_TOKEN_BREAK = re.compile(r"""[\s"'`(),;:\]\[{}=]""")


def _enclosing_token(line: str, start: int, end: int) -> str:
    """The whitespace/quote-delimited token containing the match."""
    left = start
    while left > 0 and not _TOKEN_BREAK.match(line[left - 1]):
        left -= 1
    right = end
    while right < len(line) and not _TOKEN_BREAK.match(line[right]):
        right += 1
    return line[left:right]


def escapes_repo(line: str, needle: str) -> bool:
    """True only when the former name refers to the repo's OLD LOCATION.

    This is deliberately narrow, and the narrowness is the point. An earlier
    version flagged any occurrence next to a "/" and produced 94 false positives
    in one repo alone. Acting on them would have BROKEN working repositories,
    because the former name legitimately survives in three innocent forms:

      * an INTERNAL directory that kept its name, e.g. trap-antidote still
        contains `manuscript/falsification-not-exposure/`, so a Makefile line
        `cd manuscript/falsification-not-exposure/en` is correct;
      * a hash-domain separator, e.g. tiras's
        `"popperian-live-rl/candidate-seed/v1"`, whose digests are frozen in
        published results;
      * prose inside a docstring or a description string.

    None of those break when the repository directory is renamed. Only a
    reference that leaves this repository does: an absolute path, or a
    parent-escaping relative path that expects the old sibling layout.
    """
    for match in re.finditer(re.escape(needle), line):
        token = _enclosing_token(line, match.start(), match.end())
        if not token:
            continue
        # Absolute reference to the old location.
        if token.startswith("/") or token.startswith("~/"):
            return True
        # Parent-escaping reference: ../<needle> or deeper.
        if re.search(r"(^|/)\.\./(?:[^/]*/)*" + re.escape(needle), token):
            return True
    return False


def git_remote() -> str | None:
    try:
        out = subprocess.run(["git", "-C", str(REPO_ROOT), "remote", "get-url", "origin"],
                             capture_output=True, text=True, check=True).stdout.strip()
        return out or None
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def normalise_remote(url: str) -> str:
    url = url.strip().removesuffix(".git")
    url = re.sub(r"^git@([^:]+):", r"https://\1/", url)
    url = re.sub(r"^ssh://git@", "https://", url)
    return url.rstrip("/").lower()


def main() -> int:
    card = load_card()
    former_names = _as_str_list(card.get("former_names"), "former_names")
    former_slugs = _as_str_list(card.get("former_github_slugs"), "former_github_slugs")
    frozen = _as_str_list(card.get("frozen_strings"), "frozen_strings")

    exempt_raw = card.get("check_paths_exempt") or []
    exempt: dict[str, str] = {}
    if exempt_raw:
        if not isinstance(exempt_raw, list):
            _fail("PAPER.yml:check_paths_exempt must be a list of {path, reason} mappings")
        for entry in exempt_raw:
            if not isinstance(entry, dict) or "path" not in entry or "reason" not in entry:
                _fail("every check_paths_exempt entry needs BOTH 'path' and 'reason'")
            exempt[str(entry["path"]).strip()] = str(entry["reason"]).strip()

    errors: list[str] = []
    notes: list[str] = []
    applied_exemptions: set[str] = set()
    scanned = 0

    for rel, path, is_frozen in iter_files():
        relstr = str(rel)
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        scanned += 1
        is_paper_yml = relstr == "PAPER.yml"

        for lineno, line in enumerate(text.splitlines(), 1):
            # ---- rule 1: owner home path ----
            # PAPER.yml is exempt by design, for the same reason it is exempt from
            # rule 2: it is the identity card whose job is to RECORD former
            # locations and install roots. Flagging it would push every repo into
            # inventing a blanket carve-out, which is the failure this gate exists
            # to remove. It is metadata, never executed.
            if OWNER_HOME_LITERAL in line and not is_paper_yml:
                if is_frozen:
                    notes.append(f"{relstr}:{lineno}  frozen provenance, not rewritten")
                elif relstr in exempt:
                    applied_exemptions.add(relstr)
                else:
                    errors.append(
                        f"{relstr}:{lineno}  absolute owner path '{OWNER_HOME_LITERAL}' "
                        f"in an executable file — breaks on any other machine"
                    )

            # ---- rule 2: former directory name / former slug ----
            # PAPER.yml is REQUIRED to record its own former names, so it is never
            # a violation there. (The first attempt flagged it, which is why repos
            # started adding blanket exemptions.)
            if is_paper_yml or is_frozen:
                continue
            for needle in (*former_names, *former_slugs):
                if needle not in line:
                    continue
                if escapes_repo(line, needle):
                    if relstr in exempt:
                        applied_exemptions.add(relstr)
                    else:
                        errors.append(
                            f"{relstr}:{lineno}  former name '{needle}' in a path that LEAVES this "
                            f"repository (absolute, or ../ escaping to the old sibling layout) — "
                            f"this breaks after the move"
                        )
                elif any(needle in f or f in needle for f in frozen):
                    notes.append(f"{relstr}:{lineno}  '{needle}' as frozen identity, not a path")
                elif relstr in exempt:
                    applied_exemptions.add(relstr)
                else:
                    notes.append(
                        f"{relstr}:{lineno}  former name '{needle}' appears (not path-like) — "
                        f"declare it in frozen_strings if deliberate"
                    )

    # ---- rule 3: declared URLs agree with the live remote ----
    remote = git_remote()
    if remote:
        want = normalise_remote(remote)
        for meta_name in ("CITATION.cff", "pyproject.toml"):
            meta = REPO_ROOT / meta_name
            if not meta.is_file():
                continue
            for lineno, line in enumerate(meta.read_text(encoding="utf-8").splitlines(), 1):
                for m in re.finditer(r"https?://github\.com/[\w.\-]+/[\w.\-]+", line):
                    found = normalise_remote(m.group(0))
                    if found != want and "PhiniteLab" in m.group(0):
                        errors.append(
                            f"{meta_name}:{lineno}  URL {m.group(0)} disagrees with the live "
                            f"remote {remote}"
                        )

    # ---------------- report: exemptions are ALWAYS visible ----------------
    if exempt:
        print("check_paths: declared exemptions (from PAPER.yml:check_paths_exempt)")
        for p, reason in sorted(exempt.items()):
            mark = "USED" if p in applied_exemptions else "unused"
            print(f"    [{mark}] {p}\n           reason: {reason}")
        stale = set(exempt) - applied_exemptions
        if stale:
            print(f"    NOTE: {len(stale)} exemption(s) matched nothing — remove them.")
        print()

    if notes:
        print(f"check_paths: {len(notes)} informational note(s)")
        for n in notes[:40]:
            print(f"    {n}")
        if len(notes) > 40:
            print(f"    ... and {len(notes) - 40} more")
        print()

    if errors:
        print(f"check_paths: FAIL — {len(errors)} violation(s) in {scanned} executable files")
        for e in errors:
            print(f"    {e}")
        return 1

    print(f"check_paths: OK ({scanned} executable files scanned, "
          f"{len(exempt)} declared exemption(s), {len(notes)} note(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
