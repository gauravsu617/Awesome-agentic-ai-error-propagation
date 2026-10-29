#!/usr/bin/env python3
"""Validate and summarize simulated workflow results for Phase IV.
Usage:
  python evaluate_phaseiv.py --input predictions/multi_seed_results.csv --outdir results/phase_iv
Dependencies: pandas, numpy, matplotlib
"""
import argparse
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

REQUIRED = {"error_rate", "model", "stage_errors", "workflow_failed"}

def wilson_interval(p, n, z=1.96):
    if n <= 0:
        return (float("nan"), float("nan"))
    den = 1 + z*z/n
    center = (p + z*z/(2*n)) / den
    half = z * np.sqrt(p*(1-p)/n + z*z/(4*n*n)) / den
    return center-half, center+half

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--outdir", default="results/phase_iv")
    args = ap.parse_args()
    df = pd.read_csv(args.input)
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    if df[list(REQUIRED - {"workflow_failed"})].isna().any().any():
        raise ValueError("Missing values in required numeric/group fields")
    df["error_rate"] = pd.to_numeric(df["error_rate"], errors="raise")
    df["stage_errors"] = pd.to_numeric(df["stage_errors"], errors="raise")
    if not df["error_rate"].between(0, 1).all():
        raise ValueError("error_rate must be in [0, 1]")
    if (df["stage_errors"] < 0).any():
        raise ValueError("stage_errors cannot be negative")
    if df["workflow_failed"].dtype != bool:
        df["workflow_failed"] = df["workflow_failed"].astype(str).str.strip().str.lower().map(
            {"true": True, "false": False, "1": True, "0": False})
    if df["workflow_failed"].isna().any():
        raise ValueError("workflow_failed contains unrecognized boolean values")
    if not (df["workflow_failed"] == (df["stage_errors"] > 0)).all():
        raise ValueError("workflow_failed must equal (stage_errors > 0); inspect metric definition")
    keys = [c for c in ["trial", "error_rate", "model", "seed"] if c in df.columns]
    if keys and df.duplicated(keys).any():
        raise ValueError(f"Duplicate trial keys detected: {int(df.duplicated(keys).sum())}")

    rows = []
    for (rate, model), g in df.groupby(["error_rate", "model"], sort=True):
        n = len(g)
        p = float(g["workflow_failed"].mean())
        lo, hi = wilson_interval(p, n)
        rows.append({
            "error_rate": rate, "model": model, "n": n,
            "mean_stage_errors": g["stage_errors"].mean(),
            "std_stage_errors": g["stage_errors"].std(ddof=1),
            "failure_rate": p, "failure_ci95_low": lo, "failure_ci95_high": hi
        })
    summary = pd.DataFrame(rows)
    out = Path(args.outdir)
    out.mkdir(parents=True, exist_ok=True)
    summary.to_csv(out / "phaseiv_results.csv", index=False)

    means = summary.pivot(index="error_rate", columns="model", values="mean_stage_errors")
    fails = summary.pivot(index="error_rate", columns="model", values="failure_rate")
    if {"independent", "propagation"}.issubset(means.columns) and {"independent", "propagation"}.issubset(fails.columns):
        comparison = pd.DataFrame({
            "error_rate": means.index,
            "independent_mean_stage_errors": means["independent"],
            "propagation_mean_stage_errors": means["propagation"],
            "stage_error_difference_prop_minus_ind": means["propagation"] - means["independent"],
            "independent_failure_rate": fails["independent"],
            "propagation_failure_rate": fails["propagation"],
            "failure_rate_difference_prop_minus_ind": fails["propagation"] - fails["independent"],
        })

        # Use matched trials for uncertainty on the stage-error difference.
        # This is valid only when the input contains a usable pairing key.
        if {"seed", "trial", "error_rate"}.issubset(df.columns):
            paired = df.pivot(index=["seed", "trial", "error_rate"],
                              columns="model", values="stage_errors")
            if {"independent", "propagation"}.issubset(paired.columns):
                paired["difference_prop_minus_ind"] = (
                    paired["propagation"] - paired["independent"]
                )
                paired_summary = paired.groupby(level="error_rate")["difference_prop_minus_ind"].agg(
                    paired_n="count", paired_mean_difference="mean", paired_sd="std"
                )
                paired_summary["paired_se"] = (
                    paired_summary["paired_sd"] / np.sqrt(paired_summary["paired_n"])
                )
                paired_summary["paired_ci95_low"] = (
                    paired_summary["paired_mean_difference"] - 1.96 * paired_summary["paired_se"]
                )
                paired_summary["paired_ci95_high"] = (
                    paired_summary["paired_mean_difference"] + 1.96 * paired_summary["paired_se"]
                )
                paired_summary = paired_summary.drop(columns=["paired_sd"])
                comparison = comparison.merge(
                    paired_summary.reset_index(), on="error_rate", how="left"
                )

        comparison.to_csv(out / "phaseiv_comparison.csv", index=False)

    for metric, ylabel, title, filename in [
        ("mean_stage_errors", "Mean stage errors per workflow", "Stage-error accumulation", "phaseiv_stage_errors.png"),
        ("failure_rate", "Workflow failure rate", "Any-stage-error failure rate", "phaseiv_failure_rate.png"),
    ]:
        plt.figure(figsize=(7, 4.5))
        for model in summary["model"].unique():
            d = summary[summary["model"] == model]
            plt.plot(d["error_rate"], d[metric], marker="o", label=model)
        plt.xlabel("Base per-stage error probability")
        plt.ylabel(ylabel)
        plt.title(title)
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()
        plt.savefig(out / filename, dpi=200)
        plt.close()
    print(f"PASS: validated {len(df)} rows from {args.input}")
    print(summary.to_string(index=False))
    print(f"Outputs written to {out.resolve()}")

if __name__ == "__main__":
    main()
