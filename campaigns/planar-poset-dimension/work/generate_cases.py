"""Fix reproducible source formulas before constructing a reduction."""

import json
import random
from pathlib import Path


EDGE_CASES = [
    (0, [], True),
    (0, [[]], False),
    (1, [], True),
    (1, [[1]], True),
    (1, [[-1]], True),
    (1, [[1], [-1]], False),
    (1, [[1, -1]], True),
    (2, [[1], [2]], True),
    (2, [[1], [-1, 2], [-2]], False),
    (2, [[1, 2], [-1, -2]], True),
    (2, [[1], [-1]], False),
    (3, [[1, 2, 3], [-1, -2, -3]], True),
    (3, [[1], [2], [3]], True),
    (3, [[1], [2], [-1, -2]], False),
    (3, [[], [1]], False),
    (3, [[1, 1, 1], [-1, -1, -1]], False),
    (4, [], True),
    (4, [[1, 2], [-1, 2], [1, -2], [-1, -2]], False),
    (3, [[1, -1, 2], [-2, 3]], True),
    (3, [[1], [-1], [2]], False),
]


def random_source(seed):
    rng = random.Random(seed)
    n = rng.randint(1, 6)
    clauses = []
    for _ in range(rng.randint(1, 10)):
        size = rng.randint(1, min(3, n))
        variables = rng.sample(range(1, n + 1), size)
        clauses.append([variable * rng.choice((-1, 1)) for variable in variables])
    return {"num_vars": n, "clauses": clauses}


def build_cases():
    from check import solve_source

    cases = []
    seen = set()

    def add(source, kind, seed=None, expected_satisfiable=None):
        key = json.dumps(source, sort_keys=True, separators=(",", ":"))
        if key in seen:
            return False
        seen.add(key)
        answer = solve_source(source)
        if expected_satisfiable is not None and ("assignment" in answer) != expected_satisfiable:
            raise AssertionError(f"Hand-labelled case disagrees with oracle: {source}")
        case = {"source": source, "kind": kind, "expected": answer}
        if seed is not None:
            case["seed"] = seed
        cases.append(case)
        return True

    for n, clauses, satisfiable in EDGE_CASES:
        add({"num_vars": n, "clauses": clauses}, "edge", expected_satisfiable=satisfiable)
    seed = 0
    while sum(case["kind"] == "random" for case in cases) < 100:
        add(random_source(seed), "random", seed=seed)
        seed += 1
    return cases


if __name__ == "__main__":
    path = Path(__file__).with_name("cases.json")
    cases = build_cases()
    path.write_text(json.dumps(cases, indent=2) + "\n")
    print(f"Wrote {len(cases)} cases to {path}")
