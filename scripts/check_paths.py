#!/usr/bin/env python3
"""Path-safety gate for this repository (collection repository standard, section E).

Fails (exit 1) on:
  (a) any '/home/mehmet' literal in an executable file
      (.py .sh .bash Makefile .yml .yaml .toml .cfg .ini)
  (b) any occurrence of this repo's FORMER directory name
      ('popperian-coding-skill') in an executable file
  (c) any CITATION.cff URL that disagrees with 'git remote get-url origin'
      (this repo has no pyproject.toml, so there is no [project.urls] table
      to check)

Exits 0 with a summary line when clean.

Deliberate exceptions (documented, not silenced):

  * PAPER.yml is EXEMPT from the former-directory-name scan (b). PAPER.yml
    is the collection standard's mandated, canonical record of the rename
    (its `former_names` / `former_github_slugs` keys are REQUIRED to
    contain 'popperian-coding-skill' / 'PhiniteLab/popperian-coding-skill'
    verbatim). Flagging it would fail the repo for doing exactly what the
    standard requires. PAPER.yml still gets the '/home/mehmet' literal
    check (a) — there is no legitimate reason for that path to appear
    there.

  * SKILL.md's `name: popperian-coding` and README.md's install path
    `~/.claude/skills/popperian-coding/` are the skill's frozen registered
    identity (see PAPER.yml:frozen_strings) and do not trip this scan
    regardless: the former-directory-name string is 'popperian-coding-skill'
    (with the '-skill' suffix), a strict superstring of 'popperian-coding'
    that neither of those frozen strings contains. No exclusion needed.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

FORMER_DIR_NAME = "popperian-coding-skill"
FORBIDDEN_LITERAL = "/home/mehmet"

SCAN_EXTENSIONS = {".py", ".sh", ".bash", ".yml", ".yaml", ".toml", ".cfg", ".ini"}
SCAN_LITERAL_NAMES = {"Makefile"}

# Frozen-provenance directories: never modified by tooling, never scanned.
# (Most of these do not exist in this small repo; listed for parity with
# the collection-wide standard so this script is copy-paste reusable.)
EXCLUDED_DIRS = {
    "results",
    "paper",
    "arxiv-latex",
    "manuscript",
    "ownerDocs",
    "archive",
    "legacy",
    "runs",
    "reference",
    "artifact",
    ".git",
    ".venv",
    "node_modules",
}
# Compound relative paths (dir/subdir form) excluded as frozen provenance.
EXCLUDED_PATH_PREFIXES = {
    Path("docs/record/legacy"),
    Path("final_review"),
    Path("final_remediation"),
    Path("reviewer_remediation"),
}

# Files exempt from the former-directory-name scan only (rule b), with the
# reason recorded above in the module docstring.
FORMER_NAME_EXEMPT_FILES = {"PAPER.yml"}

# This script itself is exempt from BOTH content scans (a) and (b): it must
# name the forbidden literal and the former directory name verbatim, in its
# own docstring and in the FORMER_DIR_NAME / FORBIDDEN_LITERAL constants
# above, in order to define what those checks look for. A checker that
# forbids its own definition is a quine problem, not a real violation —
# scanning this file for the strings it exists to detect would always
# self-fail. Every other file in the repo is still fully scanned.
SELF_EXEMPT_FILES = {"scripts/check_paths.py"}


def is_excluded(path: Path) -> bool:
    rel = path.relative_to(REPO_ROOT)
    parts = rel.parts
    if any(part in EXCLUDED_DIRS for part in parts):
        return True
    for prefix in EXCLUDED_PATH_PREFIXES:
        if rel == prefix or prefix in rel.parents:
            return True
    return False


def iter_scanned_files() -> list[Path]:
    files: list[Path] = []
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file():
            continue
        if is_excluded(path):
            continue
        rel_posix = path.relative_to(REPO_ROOT).as_posix()
        if rel_posix in SELF_EXEMPT_FILES:
            continue
        if path.name in SCAN_LITERAL_NAMES or path.suffix in SCAN_EXTENSIONS:
            files.append(path)
    return sorted(files)


def check_literal_and_former_name(files: list[Path]) -> list[str]:
    failures: list[str] = []
    for path in files:
        rel = path.relative_to(REPO_ROOT)
        try:
            text = path.read_text(encoding="utf-8", errors="strict")
        except (UnicodeDecodeError, OSError) as exc:
            failures.append(f"{rel}: could not read as UTF-8 text ({exc})")
            continue

        for lineno, line in enumerate(text.splitlines(), start=1):
            if FORBIDDEN_LITERAL in line:
                failures.append(
                    f"{rel}:{lineno}: contains forbidden literal "
                    f"'{FORBIDDEN_LITERAL}'"
                )
            if rel.name not in FORMER_NAME_EXEMPT_FILES and FORMER_DIR_NAME in line:
                failures.append(
                    f"{rel}:{lineno}: contains former directory name "
                    f"'{FORMER_DIR_NAME}'"
                )
    return failures


def get_origin_url() -> str | None:
    try:
        out = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    url = out.stdout.strip()
    return url[:-4] if url.endswith(".git") else url


def check_citation_cff_url(origin: str | None) -> list[str]:
    failures: list[str] = []
    cff_path = REPO_ROOT / "CITATION.cff"
    if not cff_path.exists():
        return failures
    if origin is None:
        failures.append(
            "CITATION.cff: cannot verify repository-code URL — "
            "'git remote get-url origin' failed"
        )
        return failures

    try:
        import yaml  # type: ignore[import-untyped]
    except ImportError:
        failures.append(
            "CITATION.cff: PyYAML is not installed, cannot parse the file "
            "to check its URL fields (install pyyaml to run this check)"
        )
        return failures

    data = yaml.safe_load(cff_path.read_text(encoding="utf-8"))
    for key in ("repository-code", "url"):
        value = data.get(key)
        if value is None:
            continue
        normalized = value[:-4] if value.endswith(".git") else value
        if normalized.rstrip("/") != origin.rstrip("/"):
            failures.append(
                f"CITATION.cff: '{key}' is '{value}' but "
                f"'git remote get-url origin' is '{origin}'"
            )
    return failures


def check_pyproject_urls(origin: str | None) -> list[str]:
    failures: list[str] = []
    pyproject_path = REPO_ROOT / "pyproject.toml"
    if not pyproject_path.exists():
        return failures  # no Python package in this repo

    if origin is None:
        failures.append(
            "pyproject.toml: cannot verify [project.urls] — "
            "'git remote get-url origin' failed"
        )
        return failures

    try:
        import tomllib
    except ImportError:  # pragma: no cover - Python < 3.11 fallback
        try:
            import tomli as tomllib  # type: ignore[no-redef]
        except ImportError:
            failures.append(
                "pyproject.toml: no TOML parser available "
                "(tomllib/tomli) to check [project.urls]"
            )
            return failures

    data = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))
    urls = data.get("project", {}).get("urls", {})
    for key, value in urls.items():
        normalized = value[:-4] if value.endswith(".git") else value
        if origin.rstrip("/") not in normalized.rstrip("/"):
            failures.append(
                f"pyproject.toml [project.urls] '{key}' is '{value}' but "
                f"'git remote get-url origin' is '{origin}'"
            )
    return failures


def main() -> int:
    files = iter_scanned_files()
    origin = get_origin_url()

    failures: list[str] = []
    failures.extend(check_literal_and_former_name(files))
    failures.extend(check_citation_cff_url(origin))
    failures.extend(check_pyproject_urls(origin))

    if failures:
        print(f"check_paths: FAILED ({len(failures)} issue(s))", file=sys.stderr)
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)
        return 1

    print(
        f"check_paths: OK — {len(files)} file(s) scanned, "
        f"origin={origin!r}, 0 issues"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
