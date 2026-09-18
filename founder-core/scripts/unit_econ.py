#!/usr/bin/env python3
"""Compute Founder OS unit economics from a customers CSV.

Uses the exact formulas in references/metrics-glossary.md so every skill agrees.

Input CSV columns (header row required):
    customer_id, channel, arpa, monthly_churn, gross_margin, cac
      - arpa:          monthly revenue per account (currency)
      - monthly_churn: fraction 0-1 (e.g. 0.03 for 3%)
      - gross_margin:  fraction 0-1 (e.g. 0.7 for 70%)
      - cac:           fully loaded acquisition cost for that customer

Usage:
    python unit_econ.py customers.csv [--json]

Outputs per-channel and blended ARPA, gross margin, lifetime, LTV, CAC,
payback (months), and LTV:CAC, plus the three guardrail checks.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import defaultdict

PAYBACK_GUARDRAIL = 6.0   # months
LTV_CAC_GUARDRAIL = 3.0
MARGIN_GUARDRAIL = 0.60


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def compute_group(rows: list[dict]) -> dict:
    arpa = _mean([r["arpa"] for r in rows])
    churn = _mean([r["monthly_churn"] for r in rows])
    margin = _mean([r["gross_margin"] for r in rows])
    cac = _mean([r["cac"] for r in rows])

    lifetime = (1.0 / churn) if churn > 0 else float("inf")
    ltv = arpa * margin * lifetime if lifetime != float("inf") else float("inf")
    monthly_gross_per_cust = arpa * margin
    payback = (cac / monthly_gross_per_cust) if monthly_gross_per_cust > 0 else float("inf")
    ltv_cac = (ltv / cac) if cac > 0 and ltv != float("inf") else float("inf")

    return {
        "customers": len(rows),
        "arpa": round(arpa, 2),
        "gross_margin": round(margin, 4),
        "monthly_churn": round(churn, 4),
        "lifetime_months": None if lifetime == float("inf") else round(lifetime, 1),
        "ltv": None if ltv == float("inf") else round(ltv, 2),
        "cac": round(cac, 2),
        "payback_months": None if payback == float("inf") else round(payback, 1),
        "ltv_cac": None if ltv_cac == float("inf") else round(ltv_cac, 2),
        "guardrails": {
            "payback_ok": payback <= PAYBACK_GUARDRAIL,
            "ltv_cac_ok": ltv_cac >= LTV_CAC_GUARDRAIL,
            "margin_ok": margin >= MARGIN_GUARDRAIL,
        },
    }


def load(path: str) -> list[dict]:
    rows = []
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for i, raw in enumerate(reader, start=2):
            try:
                rows.append({
                    "customer_id": raw.get("customer_id", f"row{i}"),
                    "channel": (raw.get("channel") or "unknown").strip(),
                    "arpa": float(raw["arpa"]),
                    "monthly_churn": float(raw["monthly_churn"]),
                    "gross_margin": float(raw["gross_margin"]),
                    "cac": float(raw["cac"]),
                })
            except (KeyError, ValueError) as exc:
                print(f"Skipping row {i}: {exc}", file=sys.stderr)
    return rows


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Compute Founder OS unit economics.")
    parser.add_argument("csv", help="Path to customers CSV.")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    rows = load(args.csv)
    if not rows:
        print("No valid rows found.", file=sys.stderr)
        return 1

    by_channel: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_channel[r["channel"]].append(r)

    result = {
        "blended": compute_group(rows),
        "by_channel": {ch: compute_group(rs) for ch, rs in sorted(by_channel.items())},
    }

    if args.json:
        print(json.dumps(result, indent=2))
        return 0

    def show(label: str, g: dict) -> None:
        print(f"\n{label} (n={g['customers']})")
        print(f"  ARPA ${g['arpa']}  margin {g['gross_margin']:.0%}  churn {g['monthly_churn']:.1%}")
        print(f"  lifetime {g['lifetime_months']} mo  LTV ${g['ltv']}  CAC ${g['cac']}")
        print(f"  payback {g['payback_months']} mo  LTV:CAC {g['ltv_cac']}")
        gr = g["guardrails"]
        flags = [
            f"payback≤6 {'✅' if gr['payback_ok'] else '❌'}",
            f"LTV:CAC≥3 {'✅' if gr['ltv_cac_ok'] else '❌'}",
            f"margin≥60% {'✅' if gr['margin_ok'] else '❌'}",
        ]
        print("  guardrails: " + "  ".join(flags))

    show("BLENDED", result["blended"])
    for ch, g in result["by_channel"].items():
        show(f"CHANNEL: {ch}", g)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
