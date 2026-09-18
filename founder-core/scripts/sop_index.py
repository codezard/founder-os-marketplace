#!/usr/bin/env python3
"""Generate an index of SOPs in the founder/ workspace.

Used by the sop-builder skill. Scans founder/sops/*.md, reads each SOP's
frontmatter-ish header fields (Purpose, Owner, Last reviewed) and produces a
single INDEX.md so the founder and any hire can see every documented process
and when it was last reviewed.

Usage:
    python sop_index.py [--sops-dir PATH]

Defaults to ./founder/sops, then ../founder/sops.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FIELDS = ["Purpose", "Owner", "Time budget", "Last reviewed"]


def find_dir(explicit: str | None) -> Path | None:
    if explicit:
        p = Path(explicit)
        return p if p.is_dir() else None
    for candidate in (Path("founder/sops"), Path("../founder/sops")):
        if candidate.is_dir():
            return candidate.resolve()
    return None


def extract_field(text: str, field: str) -> str:
    # Matches lines like "**Purpose:** ..." or "Purpose: ..." near the top.
    pattern = re.compile(rf"^\**{re.escape(field)}\**\s*[:：]\s*(.+)$", re.IGNORECASE | re.MULTILINE)
    m = pattern.search(text)
    return m.group(1).strip().strip("*") if m else "—"


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Build an index of SOPs.")
    parser.add_argument("--sops-dir")
    args = parser.parse_args(argv)

    sops_dir = find_dir(args.sops_dir)
    if sops_dir is None:
        print("No founder/sops directory found. Create SOPs first with sop-builder.", file=sys.stderr)
        return 1

    sops = sorted(p for p in sops_dir.glob("*.md") if p.name.lower() != "index.md")
    if not sops:
        print(f"No SOPs found in {sops_dir}.", file=sys.stderr)
        return 1

    lines = ["# SOP Index", "", f"{len(sops)} documented procedure(s).", "",
             "| Task | Purpose | Owner | Time | Last reviewed |",
             "|---|---|---|---|---|"]
    for sop in sops:
        text = sop.read_text(encoding="utf-8", errors="replace")
        purpose = extract_field(text, "Purpose")
        owner = extract_field(text, "Owner")
        budget = extract_field(text, "Time budget")
        reviewed = extract_field(text, "Last reviewed")
        lines.append(f"| [{sop.stem}]({sop.name}) | {purpose} | {owner} | {budget} | {reviewed} |")

    index_path = sops_dir / "INDEX.md"
    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {index_path} with {len(sops)} SOP(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
