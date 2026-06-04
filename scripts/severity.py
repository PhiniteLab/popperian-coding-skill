"""Severity estimation and corroboration update.

Two responsibilities:

1. `estimate` — approximate the severity of a candidate test against a
   conjecture. Uses a BALD-proxy: |P(fail | ¬H) - P(fail | H)|, where
   the probabilities are produced by an LLM "twin-step" query whose
   prompts are provided by the caller (we just do the arithmetic +
   diversity adjustment here, to keep this script free of API deps).

2. `update` — update a corroboration state given a new test outcome.
   Implements the additive surrogate from the design spec (C1-C2):
       Δ = +(1 - κ) · σ        if passed
       Δ = -λ · σ              if failed (H-blame dominant)
       Δ = -λ · σ · b_H        if failed (shared blame)
       Δ = 0                   if inconclusive
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

# ---------------------------------------------------------------------
# Verisimilitude / corroboration anchors — Popper 1963 ADDENDA §3 p. 387.
#
# Popper defines verisimilitude Vs in the extended [-1, +1] space where
# Vs(tautology) = 0  and  Vs(contradiction) = -1.  This code operates in
# the [0, 1] κ-space, so both tautology and contradiction collapse to 0 —
# the κ-space loses the sign distinction that makes Vs expressive.
# Use KAPPA_CONTRADICTION only as a sentinel / floor; consult the
# verisimilitude module for the [-1, +1] Vs metric when sign matters.
# ---------------------------------------------------------------------

KAPPA_TAUTOLOGY: float = 0.0      # vacuous claim: no error, no information
KAPPA_CONTRADICTION: float = 0.0  # in [0,1] κ-space; in [-1,+1] Vs-space → -1.0
KAPPA_MAX: float = 1.0
KAPPA_MIN: float = 0.0
KAPPA_DEFAULT_STAR: float = 0.85  # threshold κ* per docs/DESIGN.md §3

# ---------------------------------------------------------------------
# severity estimation
# ---------------------------------------------------------------------

@dataclass(frozen=True)
class SeverityInputs:
    p_fail_given_h_false: float       # caller-supplied; from LLM-twin step
    p_fail_given_h_true: float
    diversity_penalty: float = 0.0    # cosine sim against history; β·max(sim)
    cost_penalty: float = 0.0         # γ·(cost / budget)
    background_facts: tuple[str, ...] = ()   # b in Popper's S(e,h,b)
    p_e_given_b: float | None = None         # P(e|b); None → BALD-proxy fallback


def estimate_severity(inp: SeverityInputs) -> float:
    """BALD-proxy severity, clipped to [0, 1].

    σ ≈ |P(fail | ¬H) - P(fail | H)| - β·diversity - γ·cost
    """
    base = abs(inp.p_fail_given_h_false - inp.p_fail_given_h_true)
    sigma = base - inp.diversity_penalty - inp.cost_penalty
    return max(0.0, min(1.0, sigma))


def estimate_severity_popperian(inp: SeverityInputs) -> float:
    """Popperian severity S(e, h, b) as defined in Popper 1963, ADDENDA §2
    (Conjectures and Refutations, pp. 388-390).

    Formula::

        S(e, h, b) = (P(e|hb) - P(e|b)) / (P(e|hb) + P(e|b))

    where:
        P(e|hb)  — probability of evidence e given hypothesis H and background
                   knowledge b.  Supplied as ``inp.p_fail_given_h_true``
                   (re-interpreted as P(e|hb); the LLM twin-step conditions on
                   background implicitly).
        P(e|b)   — probability of evidence e given background knowledge b
                   *alone* (theory H plays no role).  Supplied explicitly via
                   ``inp.p_e_given_b`` when available.

    Range: [-1, 1].  Negative values indicate evidence that goes *against*
    hypothesis H (the standard BALD-proxy, clipped to [0,1], cannot represent
    this case).

    Fallback: if ``inp.p_e_given_b is None``, the formula cannot be evaluated
    and the function returns the existing BALD-proxy result (``estimate_severity``)
    instead, so callers that do not yet supply P(e|b) are unaffected.

    Background knowledge ``inp.background_facts`` is recorded in the dataclass
    for tracing / audit purposes; only the *count* of facts influences nothing
    here — the caller is responsible for conditioning P(e|b) on those facts.

    References
    ----------
    Popper, K. R. (1963). *Conjectures and Refutations*. Routledge.
    ADDENDA §2, pp. 388-390.
    """
    if inp.p_e_given_b is None:
        return estimate_severity(inp)

    p_ehb = inp.p_fail_given_h_true   # P(e | hb)
    p_eb = inp.p_e_given_b            # P(e | b)

    for name, val in (("p_fail_given_h_true", p_ehb), ("p_e_given_b", p_eb)):
        if math.isnan(val) or val < 0.0 or val > 1.0:
            raise ValueError(
                f"estimate_severity_popperian: {name}={val!r} is not a valid "
                "probability in [0, 1]."
            )

    denominator = p_ehb + p_eb
    if denominator == 0.0:
        # Both zero: evidence is impossible under any assumption → severity 0
        return 0.0

    raw = (p_ehb - p_eb) / denominator
    return max(-1.0, min(1.0, raw))


# ---------------------------------------------------------------------
# corroboration update
# ---------------------------------------------------------------------

Status = Literal["passed", "failed", "inconclusive", "error"]


@dataclass(frozen=True)
class CorroborationState:
    score: float = 0.0
    severe_tests_passed: int = 0
    severe_tests_failed: int = 0
    inconclusive_count: int = 0
    rescue_rejections: int = 0
    history: tuple[dict, ...] = field(default_factory=tuple)


def update(
    state: CorroborationState,
    severity: float,
    status: Status,
    h_blame: float = 1.0,
    lambda_fail: float = 2.0,
    severity_floor: float = 0.20,
    prior_probability: float | None = None,
) -> CorroborationState:
    """Apply C1-C2 update.

    Parameters
    ----------
    prior_probability:
        Optional prior probability of the conjecture being tested.  Must be
        strictly in (0, 1).  When supplied, the pass-case delta is scaled by a
        "boldness" factor derived from Popper (Conjectures and Refutations p. 59):
        a passing test on a low-prior (bold) conjecture is more informative than
        a passing test on a high-prior (safe) one.

        boldness      = -log2(prior_probability)       # bits of improbability
        boldness_norm = min(1.0, boldness / 10.0)      # cap at 10 bits → 1.0
        delta         = (1 - κ) · σ · (1 + boldness_norm)
        delta         = min(delta, 1 - κ)              # cannot exceed headroom

        When None (default), behavior is identical to the original formula
        (boldness factor = 1.0 effectively).
    """
    if prior_probability is not None and (
        math.isnan(prior_probability)
        or prior_probability <= 0.0
        or prior_probability >= 1.0
    ):
        raise ValueError(
            f"prior_probability must be strictly in (0, 1), got {prior_probability!r}"
        )

    if severity < severity_floor:
        # below floor → does not contribute, only logged
        return CorroborationState(
            score=state.score,
            severe_tests_passed=state.severe_tests_passed,
            severe_tests_failed=state.severe_tests_failed,
            inconclusive_count=state.inconclusive_count,
            rescue_rejections=state.rescue_rejections,
            history=state.history + ({
                "severity": severity,
                "status": status,
                "note": "below_floor",
            },),
        )

    if status == "passed":
        if prior_probability is not None:
            boldness = -math.log2(prior_probability)
            boldness_norm = min(1.0, boldness / 10.0)
            headroom = 1.0 - state.score
            delta = min(headroom * severity * (1.0 + boldness_norm), headroom)
        else:
            delta = (1.0 - state.score) * severity
        return CorroborationState(
            score=_clip(state.score + delta),
            severe_tests_passed=state.severe_tests_passed + 1,
            severe_tests_failed=state.severe_tests_failed,
            inconclusive_count=state.inconclusive_count,
            rescue_rejections=state.rescue_rejections,
            history=state.history + ({"severity": severity,
                                       "status": status, "delta": delta},),
        )

    if status == "failed":
        delta = -lambda_fail * severity * h_blame
        return CorroborationState(
            score=_clip(state.score + delta),
            severe_tests_passed=state.severe_tests_passed,
            severe_tests_failed=state.severe_tests_failed + 1,
            inconclusive_count=state.inconclusive_count,
            rescue_rejections=state.rescue_rejections,
            history=state.history + ({"severity": severity,
                                       "status": status, "delta": delta,
                                       "h_blame": h_blame},),
        )

    if status == "inconclusive":
        return CorroborationState(
            score=state.score,
            severe_tests_passed=state.severe_tests_passed,
            severe_tests_failed=state.severe_tests_failed,
            inconclusive_count=state.inconclusive_count + 1,
            rescue_rejections=state.rescue_rejections,
            history=state.history + ({"severity": severity,
                                       "status": status, "delta": 0.0},),
        )

    # error
    return state


def _clip(x: float) -> float:
    return max(0.0, min(1.0, x))


def is_contradiction(state: CorroborationState) -> bool:
    """Heuristic: return True if the history contains a high-confidence direct refutation.

    A history entry is treated as an epistemic contradiction when ALL of:
    - status == "failed"
    - severity >= 0.85  (very severe test)
    - h_blame >= 1.0    (full blame on the hypothesis H)

    This is a heuristic, not a theorem.  In Popper's verisimilitude framework
    (Conjectures and Refutations ADDENDA §3 p. 387), a genuine contradiction
    carries Vs = -1 in the [-1, +1] space; in the [0, 1] κ-space that
    collapses to KAPPA_CONTRADICTION = 0.0.  Use this helper as a guard to
    signal when a conjecture should be abandoned, not as a formal proof of
    inconsistency.

    Parameters
    ----------
    state:
        Current corroboration state whose history is inspected.

    Returns
    -------
    bool
        True if at least one history entry meets the contradiction threshold.
    """
    for entry in state.history:
        if (
            entry.get("status") == "failed"
            and entry.get("severity", 0.0) >= 0.85
            and entry.get("h_blame", 1.0) >= 1.0
        ):
            return True
    return False


# ---------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------

def _load_state(path: Path | None) -> CorroborationState:
    if path is None or not path.exists():
        return CorroborationState()
    data = json.loads(path.read_text(encoding="utf-8"))
    return CorroborationState(
        score=data.get("score", 0.0),
        severe_tests_passed=data.get("severe_tests_passed", 0),
        severe_tests_failed=data.get("severe_tests_failed", 0),
        inconclusive_count=data.get("inconclusive_count", 0),
        rescue_rejections=data.get("rescue_rejections", 0),
        history=tuple(data.get("history", ())),
    )


def _dump_state(state: CorroborationState, path: Path) -> None:
    path.write_text(json.dumps({
        "score": state.score,
        "severe_tests_passed": state.severe_tests_passed,
        "severe_tests_failed": state.severe_tests_failed,
        "inconclusive_count": state.inconclusive_count,
        "rescue_rejections": state.rescue_rejections,
        "history": list(state.history),
    }, indent=2), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="popperian.severity")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_est = sub.add_parser("estimate", help="estimate σ for a candidate test")
    p_est.add_argument("--p-fail-given-h-false", type=float, required=True)
    p_est.add_argument("--p-fail-given-h-true", type=float, required=True)
    p_est.add_argument("--diversity-penalty", type=float, default=0.0)
    p_est.add_argument("--cost-penalty", type=float, default=0.0)

    p_pop = sub.add_parser(
        "popper_estimate",
        help="Popperian severity S(e,h,b) per Popper 1963 ADDENDA §2",
    )
    p_pop.add_argument("--p-e-given-hb", type=float, required=True,
                       help="P(e|hb): probability of evidence given H and background")
    p_pop.add_argument("--p-e-given-b", type=float, required=True,
                       help="P(e|b): probability of evidence given background only")
    p_pop.add_argument("--background-facts", type=str, default="",
                       help="Comma-separated background fact strings (count recorded)")

    p_up = sub.add_parser("update", help="apply one update to a state file")
    p_up.add_argument("--state", type=Path, required=True)
    p_up.add_argument("--severity", type=float, required=True)
    p_up.add_argument("--status", choices=["passed", "failed",
                                            "inconclusive", "error"],
                      required=True)
    p_up.add_argument("--h-blame", type=float, default=1.0)
    p_up.add_argument("--lambda-fail", type=float, default=2.0)
    p_up.add_argument("--severity-floor", type=float, default=0.20)

    args = parser.parse_args(argv)

    if args.cmd == "popper_estimate":
        raw_facts = args.background_facts
        facts: tuple[str, ...] = (
            tuple(f.strip() for f in raw_facts.split(",") if f.strip())
            if raw_facts else ()
        )
        sigma = estimate_severity_popperian(SeverityInputs(
            p_fail_given_h_false=0.0,   # not used by Popperian path
            p_fail_given_h_true=args.p_e_given_hb,
            p_e_given_b=args.p_e_given_b,
            background_facts=facts,
        ))
        print(json.dumps({
            "severity_popperian": sigma,
            "p_e_given_hb": args.p_e_given_hb,
            "p_e_given_b": args.p_e_given_b,
            "background_facts_count": len(facts),
        }, indent=2))
        return 0

    if args.cmd == "estimate":
        sigma = estimate_severity(SeverityInputs(
            p_fail_given_h_false=args.p_fail_given_h_false,
            p_fail_given_h_true=args.p_fail_given_h_true,
            diversity_penalty=args.diversity_penalty,
            cost_penalty=args.cost_penalty,
        ))
        print(json.dumps({"severity": sigma}, indent=2))
        return 0

    if args.cmd == "update":
        state = _load_state(args.state)
        new_state = update(
            state=state,
            severity=args.severity,
            status=args.status,
            h_blame=args.h_blame,
            lambda_fail=args.lambda_fail,
            severity_floor=args.severity_floor,
        )
        _dump_state(new_state, args.state)
        print(json.dumps({
            "score": new_state.score,
            "severe_tests_passed": new_state.severe_tests_passed,
            "severe_tests_failed": new_state.severe_tests_failed,
            "inconclusive_count": new_state.inconclusive_count,
        }, indent=2))
        return 0

    return 2


if __name__ == "__main__":
    sys.exit(main())
