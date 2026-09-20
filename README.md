# S4 x T3 Dirac Spectral Action: A Toy Probe

> **Private exploratory probe.** This repository is a private exploratory research probe into the spectral geometry of \(S^4 \times T^3\). It tests whether a simplified Dirac-spectrum objective on a variable-radius \(T^3\) can favor arithmetic structure associated with \(K=\mathbb{Q}(\sqrt2,\sqrt3,\sqrt5)\). The project is intentionally limited to a finite computational sanity check intended to falsify or support the idea before deeper mathematical work. It is not a proof, completed physical model, or claim of emergence.

## Purpose

The code studies a simplified Dirac spectrum on a three-torus with variable radii `R = (R1, R2, R3)`. It counts modes below a scale `Lambda` and compares fixed-volume radius triples. The field-inspired candidate is treated as a hypothesis to test, not as a discovery.

This repository is deliberately a **falsification instrument**. A negative result is useful: it can stop an unsupported idea before months of deeper work are spent on it. A positive result is only a reason to design a stronger experiment.

## Diagnostics

- `random_baseline.py` compares the candidate with reproducible random unit-volume triples and writes a histogram of the complete baseline.
- `convergence.py` checks sensitivity to lattice cutoff, grid resolution, and `Lambda` using actual searches without injected noise.
- `minimize.py` performs the basic fixed-volume grid search.
- `plot_search.py` visualizes the search landscape.
- `dirac_t3.py` contains the simplified eigenvalue and state-count routines.
- `tests/test_research.py` checks volume normalization, deterministic sampling, nonnegative counts, ranking, and CSV output.

## Run privately

Run from the repository root:

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt

python -m pytest -v
python random_baseline.py
python convergence.py

python --version > results/python_version.txt
pip freeze > results/freeze.txt
echo "$RANDOM_SEED"
```

The default run produces these five reproducibility artifacts:

```text
results/random_baseline.csv
results/random_baseline.png
results/convergence.csv
results/python_version.txt
results/freeze.txt
```

The scripts use the repository's computational toy-model implementation. Do not replace it with a placeholder ratio-cost or noise-based convergence script.

## Engineering Skills Demonstrated

- Reproducible Python environments and dependency capture
- Parameterized numerical experiments
- Fixed-volume constrained optimization
- Randomized null-model testing
- Cutoff and grid-convergence analysis
- Deterministic seeds and experiment logging
- Unit testing of numerical invariants and output contracts
- Explicit failure criteria and uncertainty-aware reporting

## Archive policy

Generated outputs are ignored by Git by default. For a private audit trail, keep the five artifacts local and archive the complete `results/` directory outside Git. If selected outputs are intentionally published for reproducibility, inspect them first and force-add only the approved files:

```bash
git add -f \
  results/random_baseline.csv \
  results/random_baseline.png \
  results/convergence.csv \
  results/python_version.txt \
  results/freeze.txt

git commit -m "Archive reproducibility outputs"
git push
```

Before publishing, inspect `results/freeze.txt` and all CSV files for sensitive paths, private package indexes, local usernames, or other information that should not be public. Leaving generated outputs untracked is the conservative default for this exploratory research probe.

## Reproducibility log

Preserve the exact command-line arguments, random seed, proposal distribution, cutoff, grid size, and `Lambda` values. Preserve terminal output alongside the generated artifacts when possible. The default random-baseline seed is recorded in the script and printed at runtime.

## Interpretation rules

- A percentile describes performance under one sampling distribution; it is not proof.
- A histogram is a visualization of the sampled baseline; it is not independent evidence.
- Convergence measures sensitivity to finite numerical parameters; it is not validation of the model.
- Tests verify implementation invariants and output contracts; they do not validate the physical model.
- A favorable percentile in one random baseline is not evidence of emergence; repeat with multiple seeds and proposal distributions.
- A stable optimum across finite cutoffs and grid sizes only reduces concern about one numerical artifact.
- A drifting optimum means the current objective or search is not reliable.
- The arithmetic candidate must be evaluated after a field-blind optimization, not inserted into the optimizer.
- Passing these tests would justify a better experiment, not a proof or completed physical theory.

## Portfolio description

> A reproducible research-engineering prototype using a simplified computational toy model to test a spectral-geometry hypothesis through randomized baselines, numerical convergence checks, and explicit failure criteria.

## Remaining requirements

1. Replace the raw mode count with a justified spectral action `Tr f(D^2 / Lambda^2)`.
2. Establish convergence under the relevant limits.
3. Test multiple smooth functions `f` and spin-structure twists.
4. Use independent null models and field-blind optimization.
5. Define a mathematical or physical prediction that could be checked independently.

Keep this repository private until the diagnostics are independently reproducible and the stated checks have been addressed.
