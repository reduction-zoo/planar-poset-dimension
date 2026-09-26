"""Check the fixed source corpus before candidate construction."""

import argparse
import json
from pathlib import Path


def validate_cases(cases):
    if not isinstance(cases, list) or len(cases) < 100:
        raise ValueError("At least 100 cases are required")
    seen = set()
    random_count = edge_count = 0
    for case in cases:
        if not isinstance(case, dict) or "source" not in case:
            raise ValueError("Each case needs a source instance")
        kind = case.get("kind")
        if kind not in {"random", "edge", "hand"}:
            raise ValueError("Each case needs a kind: random, edge, or hand")
        source = json.dumps(case["source"], sort_keys=True, separators=(",", ":"), allow_nan=False)
        if source in seen:
            raise ValueError("Source instances must be distinct")
        seen.add(source)
        if kind == "random":
            if type(case.get("seed")) is not int or case["seed"] < 0:
                raise ValueError("Random cases need a nonnegative integer seed")
            random_count += 1
        elif kind == "edge":
            edge_count += 1
    if random_count < 50 or edge_count < 10:
        raise ValueError("The corpus needs at least 50 seeded-random and 10 edge cases")
    return len(cases), random_count, edge_count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cases", type=Path)
    args = parser.parse_args()
    try:
        total, random_count, edge_count = validate_cases(json.loads(args.cases.read_text()))
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Preparation corpus failed: {exc}\n")
    print(f"Preparation corpus passed: {total} distinct cases, {random_count} random, {edge_count} edge")


if __name__ == "__main__":
    main()
