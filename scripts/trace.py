"""Run-trace writer for Inv-6.

Appends events as JSONL to a configurable trace file. Each event is a
single JSON object with a timestamp, a `kind`, and event-specific
fields. The verification mode reads earlier traces as auxiliary
evidence (V5 — agent-claim verification).
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import uuid
from pathlib import Path
from typing import Any

_VALID_KINDS = {
    "propose_conjecture",
    "design_test",
    "execute_test",
    "adjudicate",
    "update_corroboration",
    "revise_conjecture",
    "reject_ad_hoc",
    "stop",
    "abstain",
    "final",
}


def append_event(trace_path: Path, kind: str, **fields: Any) -> str:
    """Append a JSON event to `trace_path` (JSONL). Returns the event id."""
    if kind not in _VALID_KINDS:
        raise ValueError(f"unknown kind: {kind!r}; valid: {sorted(_VALID_KINDS)}")

    event_id = uuid.uuid4().hex[:12]
    payload = {
        "ts": time.time_ns(),
        "id": event_id,
        "kind": kind,
        **fields,
    }
    trace_path.parent.mkdir(parents=True, exist_ok=True)
    with trace_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")
    return event_id


def read_trace(trace_path: Path) -> list[dict]:
    if not trace_path.exists():
        return []
    return [json.loads(line) for line in trace_path.read_text("utf-8").splitlines()
            if line.strip()]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="popperian.trace")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_app = sub.add_parser("append", help="append an event")
    p_app.add_argument("--path", type=Path, required=True)
    p_app.add_argument("--kind", required=True, choices=sorted(_VALID_KINDS))
    p_app.add_argument("--field", action="append", default=[],
                       help="repeatable key=value; value parsed as JSON if possible")

    p_read = sub.add_parser("read", help="dump trace as JSON array")
    p_read.add_argument("--path", type=Path, required=True)

    args = parser.parse_args(argv)

    if args.cmd == "append":
        fields: dict[str, Any] = {}
        for kv in args.field:
            if "=" not in kv:
                raise SystemExit(f"--field expects key=value: {kv!r}")
            k, v = kv.split("=", 1)
            try:
                fields[k] = json.loads(v)
            except json.JSONDecodeError:
                fields[k] = v
        eid = append_event(args.path, args.kind, **fields)
        print(json.dumps({"event_id": eid}))
        return 0

    if args.cmd == "read":
        events = read_trace(args.path)
        print(json.dumps(events, indent=2))
        return 0

    return 2


if __name__ == "__main__":
    sys.exit(main())
