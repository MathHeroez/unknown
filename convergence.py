"""Run cutoff/grid/Lambda convergence checks for the toy objective.

This is a diagnostic only. A stable numerical optimum would not establish
that the arithmetic field emerges; it would only show that the result is less
sensitive to these finite-search parameters.
"""

from __future__ import annotations

import argparse
import csv
import time
from pathlib import Path

import numpy as np

from dirac_t3 import count_states


def normalize(radii: tuple[float, float, float]) -> np.ndarray:
    values = np.asarray(radii, dtype=float)
    return values / np.prod(values) ** (1.0 / 3.0)


def find_optimal(cutoff: int, Lambda: float, grid: int = 25):
    """Find the lowest-count radius triple on a unit-volume grid."""
    best_n = None
    best_r = None
    values = np.linspace(0.5, 2.5, grid)

    for r1 in values:
        for r2 in values:
            r3 = 1.0 / (r1 * r2)
            if not 0.5 <= r3 <= 2.5:
                continue
            radii = (float(r1), float(r2), float(r3))
            n_states = count_states(radii, Lambda=Lambda, cutoff=cutoff)
            if best_n is None or n_states < best_n:
                best_n = n_states
                best_r = radii

    if best_r is None:
        raise RuntimeError("No valid unit-volume grid points were found")
    return best_r, best_n


def candidate_radii() -> np.ndarray:
    return normalize((np.sqrt(2.0), np.sqrt(3.0), np.sqrt(5.0)))


def distance_to_candidate(radii) -> float:
    """Compare sorted normalized ratios, ignoring coordinate ordering."""
    return float(np.linalg.norm(np.sort(normalize(tuple(radii))) - np.sort(candidate_radii())))


def run_matrix(cutoffs, grids, lambdas):
    rows = []
    for cutoff in cutoffs:
        for grid in grids:
            for Lambda in lambdas:
                started = time.perf_counter()
                best_r, best_n = find_optimal(cutoff, Lambda, grid)
                isotropic = (1.0, 1.0, 1.0)
                row = {
                    "cutoff": cutoff,
                    "grid": grid,
                    "Lambda": Lambda,
                    "R1_opt": best_r[0],
                    "R2_opt": best_r[1],
                    "R3_opt": best_r[2],
                    "N_opt": best_n,
                    "candidate_distance": distance_to_candidate(best_r),
                    "N_iso": count_states(isotropic, Lambda=Lambda, cutoff=cutoff),
                    "runtime_s": time.perf_counter() - started,
                }
                rows.append(row)
                print(
                    f"{cutoff}, {grid}, {Lambda:g}, "
                    f"{tuple(round(x, 3) for x in best_r)}, {best_n}, "
                    f"cand_dist={row['candidate_distance']:.3f}, "
                    f"N_iso={row['N_iso']}, {row['runtime_s']:.1f}s"
                )
    return rows


def write_csv(rows, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0])
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("results/convergence.csv"))
    parser.add_argument("--cutoffs", type=int, nargs="+", default=[5, 10, 15, 20, 30])
    parser.add_argument("--grids", type=int, nargs="+", default=[25, 50])
    parser.add_argument("--lambdas", type=float, nargs="+", default=[8, 12, 16])
    args = parser.parse_args()

    print("cutoff, grid, Lambda, R_opt, N_opt, candidate_dist, N_iso, runtime_s")
    rows = run_matrix(args.cutoffs, args.grids, args.lambdas)
    write_csv(rows, args.output)
    print(f"Saved convergence matrix to {args.output}")


if __name__ == "__main__":
    main()
