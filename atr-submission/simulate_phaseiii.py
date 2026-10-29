#!/usr/bin/env python3
"""Reproduce the Phase III multi-seed simulation from notebook cell 25.

This script writes to a separate output directory by default; it does not
overwrite the committed input CSVs. The simulation is synthetic and does not
execute or evaluate a deployed language-model agent.
"""
import argparse
import hashlib
import json
import math
import random
from pathlib import Path

import pandas as pd


RATES = [0.0, 0.1, 0.2, 0.3]
SEEDS = range(2026, 2056)
TRIALS = 100
STAGES = 4


def run_workflow(error_rate: float, propagation: bool, trials: int, seed: int):
    rng = random.Random(seed)
    rows = []
    for trial in range(trials):
        previous_error = False
        stage_errors = 0
        for _stage in range(STAGES):
            probability = error_rate
            if propagation and previous_error:
                probability = min(1.0, error_rate + 0.30)
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


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--outdir",
        default="atr-submission/results/phase_iii_reproduced",
        help="Separate output directory; committed prediction CSVs are not overwritten.",
    )
    args = parser.parse_args()
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    all_rows = []
    for seed in SEEDS:
        for rate in RATES:
            for propagation in [False, True]:
                all_rows.extend(run_workflow(rate, propagation, TRIALS, seed))

    raw = pd.DataFrame(all_rows)
    raw_path = outdir / "multi_seed_results.csv"
    raw.to_csv(raw_path, index=False)

    summary = raw.groupby(["error_rate", "model"], as_index=False).agg(
        mean_stage_errors=("stage_errors", "mean"),
        std_stage_errors=("stage_errors", "std"),
        failure_rate=("workflow_failed", "mean"),
    )
    summary["ci95_half_width"] = (
        1.96 * summary["std_stage_errors"] / math.sqrt(3000)
    )
    summary_path = outdir / "multi_seed_summary.csv"
    summary.to_csv(summary_path, index=False)

    manifest = {
        "status": "PASS" if len(raw) == 24000 else "CHECK_REQUIRED",
        "source": "ATR_PHASE_III_CODE_completed_Prompts_10_11.ipynb, cell 25",
        "description": "Synthetic four-stage simulation; not deployed-agent trace data.",
        "seed_range_inclusive": [2026, 2055],
        "trials_per_seed_rate_condition": TRIALS,
        "stages": STAGES,
        "error_rates": RATES,
        "rows": int(len(raw)),
        "unique_seeds": int(raw["seed"].nunique()),
        "rows_per_rate_model": {
            f"{rate}:{model}": int(len(group))
            for (rate, model), group in raw.groupby(["error_rate", "model"])
        },
        "outputs": {
            raw_path.name: {"sha256": sha256_file(raw_path), "bytes": raw_path.stat().st_size},
            summary_path.name: {"sha256": sha256_file(summary_path), "bytes": summary_path.stat().st_size},
        },
    }
    manifest_path = outdir / "reproduction_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print("SIMULATION REPRODUCTION")
    print(f"Rows: {len(raw)}")
    print(f"Unique seeds: {raw['seed'].nunique()}")
    print(summary.to_string(index=False))
    print(f"Raw output: {raw_path.resolve()}")
    print(f"Summary: {summary_path.resolve()}")
    print(f"Manifest: {manifest_path.resolve()}")
    if len(raw) != 24000:
        raise SystemExit("ERROR: expected 24,000 rows")


if __name__ == "__main__":
    main()
