"""Random-baseline test for the fixed-volume spectral-count objective.

This script deliberately does not use the arithmetic candidate during sampling.
It samples 10,000 positive radius triples from a reproducible log-uniform
proposal, normalizes each triple to volume one, and compares the candidate
R = (sqrt(2), sqrt(3), sqrt(5)) only after the baseline has been generated.

Important: the result depends on the sampling distribution. This is a
null-model diagnostic, not a proof of emergence.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np

from dirac_t3 import count_states


DEFAULT_SAMPLES = 10_000
DEFAULT_SEED = 20260920
DEFAULT_LAMBDA = 12.0
DEFAULT_CUTOFF = 15


def normalize_volume(radii: np.ndarray) -> np.ndarray:
    """Normalize positive radius triples so their product is one."""
    radii = np.asarray(radii, dtype=float)
    if radii.shape != (3,) or np.any(radii <= 0):
        raise ValueError("radii must contain exactly three positive values")
    return radii / np.prod(radii) ** (1.0 / 3.0)


def sample_unit_volume_radii(
    samples: int, rng: np.random.Generator, log_bound: float = 1.5
) -> np.ndarray:
    """Draw unit-volume triples from a symmetric log-uniform proposal.

    Two independent log-radii are sampled uniformly from [-log_bound, log_bound].
    The third is chosen so the product is exactly one. The resulting triples are
    then normalized defensively against floating-point roundoff.
    """
    if samples <= 0:
        raise ValueError("samples must be positive")
    if log_bound <= 0:
        raise ValueError("log_bound must be positive")

    log_r1_r2 = rng.uniform(-log_bound, log_bound, size=(samples, 2))
    log_radii = np.column_stack(
        [log_r1_r2, -np.sum(log_r1_r2, axis=1)]
    )
    return np.exp(log_radii)


def candidate_radii() -> np.ndarray:
    """Return the field-inspired candidate, normalized to volume one."""
    return normalize_volume(np.sqrt([2.0, 3.0, 5.0]))


def evaluate(radii: np.ndarray, Lambda: float, cutoff: int) -> np.ndarray:
    """Evaluate N(R) for each row of a radius array."""
    return np.asarray(
        [count_states(tuple(R), Lambda=Lambda, cutoff=cutoff) for R in radii],
        dtype=int,
    )


def summarize(candidate_score: int, baseline_scores: np.ndarray) -> dict[str, float]:
    """Return rank and percentile statistics, where lower scores are better."""
    scores = np.asarray(baseline_scores)
    better_or_equal = int(np.count_nonzero(scores <= candidate_score))
    strictly_better = int(np.count_nonzero(scores < candidate_score))
    rank = strictly_better + 1
    percentile_at_or_worse = 100.0 * better_or_equal / len(scores)
    return {
        "rank": rank,
        "strictly_better": strictly_better,
        "percentile_at_or_worse": percentile_at_or_worse,
        "baseline_min": int(scores.min()),
        "baseline_median": float(np.median(scores)),
        "baseline_max": int(scores.max()),
    }


def write_results(path: Path, radii: np.ndarray, scores: np.ndarray) -> None:
    """Write sampled radii and scores for later inspection."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["r1", "r2", "r3", "N"])
        writer.writerows(
            [float(R[0]), float(R[1]), float(R[2]), int(score)]
            for R, score in zip(radii, scores)
        )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--samples", type=int, default=DEFAULT_SAMPLES)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--lambda-scale", type=float, default=DEFAULT_LAMBDA)
    parser.add_argument("--cutoff", type=int, default=DEFAULT_CUTOFF)
    parser.add_argument("--log-bound", type=float, default=1.5)
    parser.add_argument("--output", type=Path, default=Path("results/random_baseline.csv"))
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    radii = sample_unit_volume_radii(args.samples, rng, args.log_bound)
    scores = evaluate(radii, args.lambda_scale, args.cutoff)

    candidate = candidate_radii()
    candidate_score = count_states(
        tuple(candidate), Lambda=args.lambda_scale, cutoff=args.cutoff
    )
    stats = summarize(candidate_score, scores)

    write_results(args.output, radii, scores)

    print("Random baseline for the simplified spectral-count objective")
    print(f"Samples: {args.samples}; seed: {args.seed}")
    print(f"Lambda: {args.lambda_scale}; lattice cutoff: {args.cutoff}")
    print(f"Sampling log-bound: +/- {args.log_bound}")
    print(f"Candidate R: {tuple(candidate)}")
    print(f"Candidate N: {candidate_score}")
    print(f"Baseline N range: {stats['baseline_min']}..{stats['baseline_max']}")
    print(f"Baseline median N: {stats['baseline_median']:.1f}")
    print(f"Random samples strictly better: {stats['strictly_better']}")
    print(f"Candidate rank (lower N is better): {stats['rank']} / {args.samples + 1}")
    print(
        "Candidate is at or below %.2f%% of random baseline scores"
        % stats["percentile_at_or_worse"]
    )
    print(f"Saved samples to {args.output}")


if __name__ == "__main__":
    main()
