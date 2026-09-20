# S4 x T3 Dirac Spectral Action: A Toy Probe

> Honest status: this repository is a small computational probe for a conjectural idea, not a proof and not a physical model. It explores whether a simplified spectral-count objective on a 3-torus favors a special arithmetic radius ratio.

## What this project does

This project studies a simplified Dirac spectrum on a three-torus `T^3` with variable radii `R = (R1, R2, R3)`. The code computes a finite set of eigenvalues and counts how many lie below a cutoff scale `Lambda`:

`N(R) = #{mu : mu^2 < Lambda^2}`

It compares different radius ratios while keeping the total volume fixed. The goal is not to claim a theorem, but to see whether a structured geometry is numerically favored under a simple spectral heuristic.

## What this project is not

- It is not a proof that `Q(sqrt(2), sqrt(3), sqrt(5))` emerges from geometry.
- It is not a complete spectral-action calculation.
- It is not a validated physical model.
- It is not a real-world engineering or prediction tool.
- It is not a theory of everything.

This is intentionally a toy experiment. It exists to answer one narrow question: does the idea survive a quick numerical sanity check?

## Repository contents

- `dirac_t3.py` — simplified Dirac eigenvalue and counting routines
- `minimize.py` — fixed-volume ratio search over a grid of radii
- `random_baseline.py` — reproducible null-model comparison
- `convergence.py` — cutoff, grid-resolution, and Lambda convergence matrix
- `plot_search.py` — heatmap-based visualization of the search landscape
- `requirements.txt` — project dependencies

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python minimize.py
python random_baseline.py
python convergence.py
python plot_search.py
```

The baseline and convergence scripts save generated CSV files under `results/`, which is ignored by Git.

## Convergence test

Run the default matrix with cutoffs `5, 10, 15, 20, 30`, grids `25, 50`, and `Lambda` values `8, 12, 16`:

```bash
python convergence.py
```

The output records the optimal radii, optimal count, distance from the field-inspired candidate, isotropic count, and runtime. A stable optimum across cutoffs and grid sizes is evidence against one specific truncation artifact, not proof of emergence. A drifting optimum means the current result is not reliable.

## Random-baseline interpretation

The baseline is a diagnostic, not a proof. Its result depends on the proposal distribution, bounds, cutoff, and objective. A candidate that does not beat the baseline is weak evidence against the current toy objective. A candidate that does beat it is only evidence that the candidate is favored under this particular null model.

## What would make the experiment stronger?

1. Replace the raw count with a justified spectral action.
2. Run convergence checks over lattice cutoff, grid size, and `Lambda`.
3. Compare against multiple random fixed-volume baselines.
4. Test multiple objective functions and twist choices.
5. Find the optimizer without mentioning the proposed arithmetic field, then compare afterward.
6. Define a mathematical or physical prediction that could be independently checked.

## Reproducibility and security

Keep unpublished work private if appropriate. Do not commit credentials, tokens, or environment files. Record Python and dependency versions, search bounds, cutoff values, proposal distributions, and random seeds for every reported result.
