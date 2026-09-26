"""Behavior checks for the reusable preparation corpus gate."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from research.validate_preparation import validate_cases


def prepared_cases():
    cases = []
    for index in range(100):
        kind = "random" if index < 50 else "edge" if index < 60 else "hand"
        case = {"source": {"value": index}, "kind": kind}
        if kind == "random":
            case["seed"] = 1234
        cases.append(case)
    return cases


class PreparationGateChecks(unittest.TestCase):
    def test_accepts_distinct_random_and_edge_cases(self):
        validate_cases(prepared_cases())

    def test_rejects_incomplete_corpora(self):
        changes = (
            lambda cases: cases.pop(),
            lambda cases: cases[99].update(source=cases[0]["source"]),
            lambda cases: cases[0].update(kind="hand"),
            lambda cases: cases[50].update(kind="hand"),
            lambda cases: cases[0].pop("seed"),
        )
        for change in changes:
            with self.subTest(change=change):
                cases = prepared_cases()
                change(cases)
                with self.assertRaises(ValueError):
                    validate_cases(cases)

    def test_command_exits_nonzero_for_short_corpus(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cases.json"
            command = [sys.executable, str(Path(__file__).with_name("validate_preparation.py")), str(path)]
            path.write_text(json.dumps(prepared_cases()))
            self.assertEqual(subprocess.run(command, capture_output=True).returncode, 0)
            path.write_text(json.dumps(prepared_cases()[:-1]))
            self.assertNotEqual(subprocess.run(command, capture_output=True).returncode, 0)


if __name__ == "__main__":
    unittest.main()
