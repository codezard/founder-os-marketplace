#!/usr/bin/env python3
"""Build cohort retention curves from a customer activity CSV.

Used by the pmf-measure skill to answer the one question that matters: does the
retention curve flatten? A flattening curve (a stable floor of returning
customers) is the leading indicator of product-market fit.

Input CSV (header row required):
    customer_id, signup_date, active_date
      - one row per (customer, day-they-were-active)
      - dates as YYYY-MM-DD
      - signup_date repeats on each of a customer's rows

Usage:
    python retention.py activity.csv [--period week|month] [--json]

Prints, for each signup cohort, the % of customers still active in period
0,1,2,... after signup.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import defaultdict
from datetime import date


def parse_date(s: str) -> date:
    return date.fromisoformat(s.strip())


def period_index(signup: date, active: date, period: str) -> int:
    days = (active - signup).days
    if days < 0:
        return -1
    return days // (7 if period == "week" else 30)


def load(path: str):
    signup_of: dict[str, date] = {}
    active_periods: dict[str, set] = defaultdict(set)
    rows = []
    with open(path, newline="", encoding="utf-8") as fh:
        for i, raw in enumerate(csv.DictReader(fh), start=2):
            try:
                cid = raw["customer_id"].strip()
                signup = parse_date(raw["signup_date"])
                active = parse_date(raw["active_date"])
            except (KeyError, ValueError) as exc:
                print(f"Skipping row {i}: {exc}", file=sys.stderr)
                continue
            signup_of[cid] = signup
            rows.append((cid, signup, active))
    return signup_of, rows


def build_curves(path: str, period: str) -> dict:
    signup_of, rows = load(path)
    # cohort key = signup period bucket relative to earliest signup
    if not signup_of:
        return {"cohorts": {}, "overall": []}

    # Group customers into cohorts by their signup period (calendar bucketed).
    earliest = min(signup_of.values())
    cohort_of: dict[str, int] = {
        cid: period_index(earliest, s, period) for cid, s in signup_of.items()
    }
    cohort_members: dict[int, set] = defaultdict(set)
    for cid, c in cohort_of.items():
        cohort_members[c].add(cid)

    # active[cohort][period_since_signup] = set of customer_ids active then
    active: dict[int, dict[int, set]] = defaultdict(lambda: defaultdict(set))
    for cid, signup, act in rows:
        p = period_index(signup, act, period)
        if p >= 0:
            active[cohort_of[cid]][p].add(cid)

    cohorts = {}
    max_p = 0
    for c, members in sorted(cohort_members.items()):
        n = len(members)
        curve = []
        p = 0
        while True:
            retained = len(active[c].get(p, set()) & members)
            if p > 0 and retained == 0 and p > max((active[c].keys()), default=0):
                break
            curve.append(round(retained / n, 3) if n else 0.0)
            if p >= max((active[c].keys()), default=0):
                break
            p += 1
        max_p = max(max_p, len(curve))
        cohorts[f"cohort_{c}"] = {"customers": n, "retention": curve}

    return {"period": period, "cohorts": cohorts}


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Cohort retention curves for PMF.")
    parser.add_argument("csv")
    parser.add_argument("--period", choices=["week", "month"], default="week")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    result = build_curves(args.csv, args.period)
    if not result["cohorts"]:
        print("No cohorts found — check the CSV.", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(result, indent=2))
        return 0

    print(f"Retention by {args.period} (period 0 = signup {args.period}):\n")
    for name, data in result["cohorts"].items():
        curve = data["retention"]
        pretty = "  ".join(f"{v:.0%}" for v in curve)
        print(f"{name} (n={data['customers']}): {pretty}")
    print("\nLook for the curve to FLATTEN (a stable floor > 0). A curve that "
          "decays to 0 means no retention — do not declare PMF.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
