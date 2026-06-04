"""Structural-MDL ad hoc rescue detector.

Implements the test for Inv-4: a revision H' of a refuted H is permitted
only if the structural MDL growth of the proposed change is less than the
encoded length of the refuting input. This is a pragmatic proxy for
Popper's prohibition of ad hoc rescues.

Usage as a CLI (called by the skill via Bash):

    python -m skill.scripts.mdl is_ad_hoc \\
        --before path/to/before_spec.json \\
        --after  path/to/after_spec.json \\
        --refutation path/to/refutation_spec.json \\
        [--tau 8]

Exit code 0 → revision is substantive (proceed).
Exit code 1 → revision is ad hoc (reject).
Stdout: JSON {is_ad_hoc, mdl_delta_bits, refutation_bits, reason}.

The structural spec is a JSON document representing the *shape* of the
conjecture (preconditions, branches, output schema) — NOT the natural
language. Spec authors are responsible for emitting it; SKILL.md
modes specify what to put there.

The MDL proxy is gzip(canonical_json(spec)) * 8. This is rough but
language-agnostic and deterministic. For more rigorous variants,
swap in a domain-specific encoder.
"""

from __future__ import annotations

import argparse
import gzip
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


def canonical_json(obj: Any) -> str:
    """Return a stable, canonical JSON serialization of obj."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def mdl_bits(obj: Any) -> int:
    """Approximate MDL of obj as 8 * len(gzip(canonical_json(obj)))."""
    payload = canonical_json(obj).encode("utf-8")
    compressed = gzip.compress(payload, compresslevel=9)
    return len(compressed) * 8


@dataclass(frozen=True)
class AdHocDecision:
    is_ad_hoc: bool
    mdl_before_bits: int
    mdl_after_bits: int
    mdl_delta_bits: int
    refutation_bits: int
    tau_bits: int
    reason: str

    def to_json(self) -> str:
        return json.dumps(
            {
                "is_ad_hoc": self.is_ad_hoc,
                "mdl_before_bits": self.mdl_before_bits,
                "mdl_after_bits": self.mdl_after_bits,
                "mdl_delta_bits": self.mdl_delta_bits,
                "refutation_bits": self.refutation_bits,
                "tau_bits": self.tau_bits,
                "reason": self.reason,
            },
            indent=2,
        )


def decide(
    before: Any,
    after: Any,
    refutation: Any,
    tau_bits: int = 8,
) -> AdHocDecision:
    """Implements the M1-M3 check from the design spec.

    H' is ad hoc iff:
        bits(H') - bits(H) > bits(refutation_spec) - tau

    i.e., the conjecture grew by more than the information needed to
    encode the refutation, suggesting the refutation was swallowed as
    an exception clause.
    """
    mb = mdl_bits(before)
    ma = mdl_bits(after)
    mr = mdl_bits(refutation)
    delta = ma - mb

    is_ad_hoc = delta > (mr - tau_bits)
    reason = (
        "revision grows MDL by more than refutation encoding ⇒ ad hoc"
        if is_ad_hoc
        else "revision growth within refutation budget ⇒ substantive"
    )
    return AdHocDecision(
        is_ad_hoc=is_ad_hoc,
        mdl_before_bits=mb,
        mdl_after_bits=ma,
        mdl_delta_bits=delta,
        refutation_bits=mr,
        tau_bits=tau_bits,
        reason=reason,
    )


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="popperian.mdl")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_is = sub.add_parser("is_ad_hoc", help="decide whether a revision is ad hoc")
    p_is.add_argument("--before", type=Path, required=True)
    p_is.add_argument("--after", type=Path, required=True)
    p_is.add_argument("--refutation", type=Path, required=True)
    p_is.add_argument("--tau", type=int, default=8, help="MDL tolerance in bits")

    p_bits = sub.add_parser("bits", help="report MDL bits for a structural spec")
    p_bits.add_argument("--spec", type=Path, required=True)

    args = parser.parse_args(argv)

    if args.cmd == "is_ad_hoc":
        d = decide(
            before=_load_json(args.before),
            after=_load_json(args.after),
            refutation=_load_json(args.refutation),
            tau_bits=args.tau,
        )
        print(d.to_json())
        return 1 if d.is_ad_hoc else 0

    if args.cmd == "bits":
        print(mdl_bits(_load_json(args.spec)))
        return 0

    return 2


if __name__ == "__main__":
    sys.exit(main())
