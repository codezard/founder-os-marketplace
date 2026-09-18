#!/usr/bin/env python3
"""Van Westendorp price-sensitivity bands from willingness-to-pay survey data.

Used by the pricing-strategy skill. The Van Westendorp Price Sensitivity Meter
asks four questions and finds the acceptable price range from where the answer
curves cross.

Input CSV (header row required), one respondent per row, prices in currency:
    too_cheap, cheap, expensive, too_expensive
      - too_cheap:     price so low you'd doubt the quality
      - cheap:         price you'd consider a bargain
      - expensive:     price starting to feel expensive (but still consider)
      - too_expensive: price so high you would not buy

Usage:
    python pricing_bands.py wtp.csv [--json]

Reports:
    PMC (Point of Marginal Cheapness), PME (Point of Marginal Expensiveness),
    OPP (Optimal Price Point), IPP (Indifference Price Point), and the
    acceptable range [PMC, PME].
"""
from __future__ import annotations

import argparse
import csv
import json
import sys


def load(path: str) -> list[dict]:
    rows = []
    with open(path, newline="", encoding="utf-8") as fh:
        for i, raw in enumerate(csv.DictReader(fh), start=2):
            try:
                rows.append({
                    "too_cheap": float(raw["too_cheap"]),
                    "cheap": float(raw["cheap"]),
                    "expensive": float(raw["expensive"]),
                    "too_expensive": float(raw["too_expensive"]),
                })
            except (KeyError, ValueError) as exc:
                print(f"Skipping row {i}: {exc}", file=sys.stderr)
    return rows


def cum_share(rows: list[dict], key: str, price: float, descending: bool) -> float:
    """Share of respondents whose threshold is met at `price`.

    descending=True  -> count respondents whose value >= price ("at least this cheap")
    descending=False -> count respondents whose value <= price ("at least this expensive")
    """
    n = len(rows)
    if descending:
        c = sum(1 for r in rows if r[key] >= price)
    else:
        c = sum(1 for r in rows if r[key] <= price)
    return c / n if n else 0.0


def crossing(rows: list[dict], key_a: str, desc_a: bool, key_b: str, desc_b: bool,
             grid: list[float]) -> float:
    """Find the price on the grid where curve A and curve B are closest to crossing."""
    best_price, best_gap = grid[0], float("inf")
    for p in grid:
        a = cum_share(rows, key_a, p, desc_a)
        b = cum_share(rows, key_b, p, desc_b)
        gap = abs(a - b)
        if gap < best_gap:
            best_gap, best_price = gap, p
    return best_price


def compute(rows: list[dict]) -> dict:
    all_prices = [v for r in rows for v in r.values()]
    lo, hi = min(all_prices), max(all_prices)
    steps = 200
    grid = [lo + (hi - lo) * i / steps for i in range(steps + 1)]

    # "not cheap" = 1 - cheap (ascending). Curves per Van Westendorp:
    #   too_cheap: descending (more people say "too cheap" at low prices)
    #   too_expensive: ascending (more say "too expensive" at high prices)
    #   cheap ("not cheap"): ascending
    #   expensive: ascending
    # PMC: too_cheap x expensive ; PME: too_expensive x cheap
    # OPP: too_cheap x too_expensive ; IPP: cheap x expensive
    pmc = crossing(rows, "too_cheap", True, "expensive", False, grid)
    pme = crossing(rows, "too_expensive", False, "cheap", True, grid)
    opp = crossing(rows, "too_cheap", True, "too_expensive", False, grid)
    ipp = crossing(rows, "cheap", True, "expensive", False, grid)

    return {
        "respondents": len(rows),
        "PMC_point_of_marginal_cheapness": round(pmc, 2),
        "PME_point_of_marginal_expensiveness": round(pme, 2),
        "OPP_optimal_price_point": round(opp, 2),
        "IPP_indifference_price_point": round(ipp, 2),
        "acceptable_range": [round(min(pmc, pme), 2), round(max(pmc, pme), 2)],
    }


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Van Westendorp pricing bands.")
    parser.add_argument("csv")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    rows = load(args.csv)
    if len(rows) < 5:
        print("Need at least ~5 respondents for a meaningful reading.", file=sys.stderr)
        if not rows:
            return 1

    result = compute(rows)
    if args.json:
        print(json.dumps(result, indent=2))
        return 0

    print(f"Van Westendorp bands (n={result['respondents']}):")
    print(f"  Acceptable range: {result['acceptable_range'][0]} – {result['acceptable_range'][1]}")
    print(f"  OPP (optimal):    {result['OPP_optimal_price_point']}")
    print(f"  IPP (indiff.):    {result['IPP_indifference_price_point']}")
    print(f"  PMC / PME:        {result['PMC_point_of_marginal_cheapness']} / {result['PME_point_of_marginal_expensiveness']}")
    print("\nAnchor to value, not to these bands alone — see the pricing-strategy skill.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
