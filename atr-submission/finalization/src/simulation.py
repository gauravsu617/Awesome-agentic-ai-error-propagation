"""Four-stage synthetic error-propagation simulator used by the AITR project."""
import random

STAGES = ("planning", "retrieval", "evidence_extraction", "verification")

def run_workflow(error_rate: float, propagation: bool, trials: int, seed: int,
                 delta: float = 0.30) -> list[dict]:
    """Run trials and return row-level outcomes."""
    if not 0.0 <= error_rate <= 1.0:
        raise ValueError("error_rate must be in [0, 1]")
    if trials < 1:
        raise ValueError("trials must be >= 1")
    if not 0.0 <= delta <= 1.0:
        raise ValueError("delta must be in [0, 1]")
    rng = random.Random(seed)
    rows = []
    for trial in range(trials):
        previous_error = False
        stage_errors = 0
        for stage in STAGES:
            probability = error_rate
            if propagation and previous_error:
                probability = min(1.0, error_rate + delta)
            current_error = rng.random() < probability
            stage_errors += int(current_error)
            previous_error = current_error
        rows.append({
            "trial": trial,
            "error_rate": error_rate,
            "model": "propagation" if propagation else "independent",
            "stage_errors": stage_errors,
            "workflow_failed": stage_errors > 0,
            "seed": seed,
        })
    return rows