import unittest
from src.simulation import run_workflow, STAGES

class TestSimulation(unittest.TestCase):
    def test_output_shape_and_bounds(self):
        rows = run_workflow(0.2, False, 12, 2026)
        self.assertEqual(len(rows), 12)
        self.assertTrue(all(0 <= r["stage_errors"] <= len(STAGES) for r in rows))

    def test_zero_rate(self):
        for condition in (False, True):
            rows = run_workflow(0.0, condition, 100, 2026)
            self.assertTrue(all(r["stage_errors"] == 0 for r in rows))

    def test_full_rate(self):
        rows = run_workflow(1.0, True, 10, 2026)
        self.assertTrue(all(r["stage_errors"] == 4 for r in rows))

    def test_repeatability(self):
        self.assertEqual(run_workflow(0.2, True, 20, 2026),
                         run_workflow(0.2, True, 20, 2026))

    def test_failure_flag(self):
        rows = run_workflow(0.3, True, 50, 2026)
        self.assertTrue(all(r["workflow_failed"] == (r["stage_errors"] > 0) for r in rows))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            run_workflow(-0.1, False, 10, 1)
        with self.assertRaises(ValueError):
            run_workflow(0.2, False, 0, 1)

if __name__ == "__main__":
    unittest.main()