#!/usr/bin/env python3
"""Report which Founder OS stage gates are open or closed.

Reads the `founder/` workspace in the current project and checks, for each of
the six stages in the stage map, whether the artifacts and evidence that close
its gate are present. This is deliberately heuristic: it inspects which
artifact files exist and looks for the gate-signal line every skill is asked to
write ("Gate: PASS ..." / "Gate: OPEN ..."). It never fabricates progress.

Usage:
    python gate_check.py [--workspace PATH] [--json]

If --workspace is omitted, it looks for ./founder, then ../founder.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# Each stage: the artifact files that should exist before its gate can close,
# and a human summary of the gate condition (from references/stage-map.md).
STAGES: list[dict] = [
    {
        "id": 0,
        "name": "Discover",
        "artifacts": ["00-idea-shortlist.md", "01-community-map.md"],
        "gate": "≥1 gap scoring high with a named community of ≥500 reachable people.",
    },
    {
        "id": 1,
        "name": "Validate",
        "artifacts": ["02-validation-report.md", "evidence-ledger.csv"],
        "gate": "≥3 people paid/committed money OR ≥5 using a manual version weekly.",
    },
    {
        "id": 2,
        "name": "MVP",
        "artifacts": ["05-mvp-spec.md", "11-first-customers.md"],
        "gate": "10 paying customers, each used it ≥3 times, ≥40% 'very disappointed'.",
    },
    {
        "id": 3,
        "name": "First Customers → Repeatable Sale",
        "artifacts": ["12-marketing-plan.md", "19-unit-economics.md", "06-pmf-report.md"],
        "gate": "One channel ≥10 new customers/month, CAC payback <6mo, MRR ≥$8-10k.",
    },
    {
        "id": 4,
        "name": "Processize",
        "artifacts": ["17-process-inventory.md", "18-delegation-plan.md"],
        "gate": "Founder ≤5h/week of ops for two weeks, MRR ≥$25-30k.",
    },
    {
        "id": 5,
        "name": "Grow Sustainably to $1M ARR",
        "artifacts": ["20-financial-model.xlsx", "25-growth-plan.md"],
        "gate": "$83k MRR for 3 months, gross margin ≥60%, NRR ≥100%.",
    },
]

# Skills write a final line like "Gate: PASS — because ..." or "Gate: OPEN — ...".
GATE_LINE = re.compile(r"^\s*Gate:\s*(PASS|CLOSED|OPEN|FAIL)\b", re.IGNORECASE | re.MULTILINE)


@dataclass
class StageStatus:
    id: int
    name: str
    gate: str
    present: list[str] = field(default_factory=list)
    missing: list[str] = field(default_factory=list)
    gate_signal: str | None = None  # "PASS" / "OPEN" / None

    @property
    def closed(self) -> bool:
        # A gate is considered closed only when every expected artifact exists
        # AND at least one of them declares a passing gate line.
        return not self.missing and self.gate_signal in {"PASS", "CLOSED"}


def find_workspace(explicit: str | None) -> Path | None:
    if explicit:
        p = Path(explicit)
        return p if p.is_dir() else None
    for candidate in (Path("founder"), Path("../founder")):
        if candidate.is_dir():
            return candidate.resolve()
    return None


def scan_stage(ws: Path, stage: dict) -> StageStatus:
    st = StageStatus(id=stage["id"], name=stage["name"], gate=stage["gate"])
    for artifact in stage["artifacts"]:
        path = ws / artifact
        if path.exists():
            st.present.append(artifact)
            if path.suffix == ".md":
                match = GATE_LINE.search(path.read_text(encoding="utf-8", errors="replace"))
                if match:
                    signal = match.group(1).upper()
                    # PASS/CLOSED beats OPEN/FAIL if any artifact reports it.
                    if signal in {"PASS", "CLOSED"} or st.gate_signal is None:
                        st.gate_signal = signal
        else:
            st.missing.append(artifact)
    return st


def render_text(statuses: list[StageStatus], ws: Path) -> str:
    lines = [f"Founder OS gate check — workspace: {ws}", ""]
    current_stage = None
    for st in statuses:
        mark = "✅ CLOSED" if st.closed else "🔓 OPEN"
        lines.append(f"Stage {st.id} — {st.name}: {mark}")
        lines.append(f"    gate: {st.gate}")
        if st.present:
            lines.append(f"    have: {', '.join(st.present)}")
        if st.missing:
            lines.append(f"    need: {', '.join(st.missing)}")
        if st.present and st.gate_signal is None:
            lines.append("    note: artifacts exist but none declares a 'Gate: PASS' line yet.")
        lines.append("")
        if not st.closed and current_stage is None:
            current_stage = st.id
    if current_stage is None:
        lines.append("All tracked gates report closed. Next: sustain the $1M run-rate.")
    else:
        lines.append(f"➡️  You are working in Stage {current_stage}. Do not run later-stage skills while this gate is open.")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Report Founder OS stage-gate status.")
    parser.add_argument("--workspace", help="Path to the founder/ workspace directory.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    args = parser.parse_args(argv)

    ws = find_workspace(args.workspace)
    if ws is None:
        msg = (
            "No founder/ workspace found. Run a Stage 0 skill (find-business-idea) "
            "to create it, or pass --workspace PATH."
        )
        if args.json:
            print(json.dumps({"error": msg}))
        else:
            print(msg)
        return 1

    statuses = [scan_stage(ws, stage) for stage in STAGES]

    if args.json:
        print(json.dumps(
            {
                "workspace": str(ws),
                "stages": [
                    {
                        "id": s.id,
                        "name": s.name,
                        "closed": s.closed,
                        "present": s.present,
                        "missing": s.missing,
                        "gate_signal": s.gate_signal,
                        "gate": s.gate,
                    }
                    for s in statuses
                ],
            },
            indent=2,
        ))
    else:
        print(render_text(statuses, ws))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
