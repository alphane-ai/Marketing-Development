#!/usr/bin/env python3
"""
Simple lead scoring helper.

Usage:
  python scripts/lead_score.py --pain 5 --payment 4 --compliance 5 --validation 4 --case 4
"""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pain", type=int, required=True, help="Pain score, 1-5")
    parser.add_argument("--payment", type=int, required=True, help="Payment ability score, 1-5")
    parser.add_argument("--compliance", type=int, required=True, help="Compliance feasibility score, 1-5")
    parser.add_argument("--validation", type=int, required=True, help="7-day validation score, 1-5")
    parser.add_argument("--case", type=int, required=True, help="Case study value score, 1-5")
    args = parser.parse_args()

    scores = [args.pain, args.payment, args.compliance, args.validation, args.case]
    if any(score < 1 or score > 5 for score in scores):
        raise SystemExit("All scores must be between 1 and 5.")

    total = sum(scores)
    if total >= 18:
        decision = "priority"
    elif total >= 15:
        decision = "secondary"
    else:
        decision = "defer"

    print(f"total_score={total}")
    print(f"decision={decision}")


if __name__ == "__main__":
    main()
