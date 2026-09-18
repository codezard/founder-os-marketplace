#!/usr/bin/env python3
"""Paid-ads math: Max CPA, Max CPC, and required test budget.

Used by the paid-ads skill. Ads are gated behind PMF and unit economics; this
script turns the unit economics into the ceilings a campaign must stay under.

Usage:
    python ads_math.py \
        --arpa 120 --gross-margin 0.7 --target-payback 6 \
        --landing-cvr 0.03 --variants 3

Definitions:
    Max CPA = target_payback_months * (arpa * gross_margin)
    Max CPC = Max CPA * landing_page_conversion_rate
    Test budget/variant = 5 * Max CPA  (rule of thumb to reach signal)
"""
from __future__ import annotations

import argparse
import json
import sys

# 5x Max CPA per variant is the common rule of thumb to gather enough
# conversions per variant to distinguish a winner from noise.
TEST_MULTIPLE = 5


def compute(arpa: float, gross_margin: float, target_payback: float,
            landing_cvr: float, variants: int) -> dict:
    monthly_gross = arpa * gross_margin
    max_cpa = target_payback * monthly_gross
    max_cpc = max_cpa * landing_cvr
    budget_per_variant = TEST_MULTIPLE * max_cpa
    return {
        "monthly_gross_profit_per_customer": round(monthly_gross, 2),
        "max_cpa": round(max_cpa, 2),
        "max_cpc": round(max_cpc, 2),
        "test_budget_per_variant": round(budget_per_variant, 2),
        "total_test_budget": round(budget_per_variant * variants, 2),
        "variants": variants,
    }


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Paid-ads CPA/CPC ceilings and test budget.")
    parser.add_argument("--arpa", type=float, required=True, help="Monthly revenue per account.")
    parser.add_argument("--gross-margin", type=float, required=True, help="Fraction 0-1.")
    parser.add_argument("--target-payback", type=float, default=6.0, help="Target payback in months.")
    parser.add_argument("--landing-cvr", type=float, required=True, help="Landing page conversion rate 0-1.")
    parser.add_argument("--variants", type=int, default=3, help="Number of creative variants to test.")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    if not (0 < args.gross_margin <= 1) or not (0 < args.landing_cvr <= 1):
        print("gross-margin and landing-cvr must be fractions between 0 and 1.", file=sys.stderr)
        return 1

    result = compute(args.arpa, args.gross_margin, args.target_payback,
                     args.landing_cvr, args.variants)
    if args.json:
        print(json.dumps(result, indent=2))
        return 0

    print("Paid-ads ceilings (do not exceed):")
    print(f"  Monthly gross profit / customer: ${result['monthly_gross_profit_per_customer']}")
    print(f"  Max CPA: ${result['max_cpa']}")
    print(f"  Max CPC: ${result['max_cpc']}")
    print(f"  Test budget / variant: ${result['test_budget_per_variant']}")
    print(f"  Total test budget ({result['variants']} variants): ${result['total_test_budget']}")
    print("\nPrecondition: PMF ≥ Emerging and landing page converts ≥ 2%. If not, do not run ads.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
