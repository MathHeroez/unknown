# S4 x T3 Dirac Spectral Action: A Toy Probe

> **Private research status:** This repository is a private exploratory research probe into the spectral geometry of \(S^4 \times T^3\). It tests whether a simplified Dirac-spectrum objective on a variable-radius \(T^3\) can favor arithmetic structure associated with \(K=\mathbb{Q}(\sqrt2,\sqrt3,\sqrt5)\). The project is intentionally limited to a finite computational sanity check intended to falsify or support the idea before deeper mathematical work. It is not a proof, completed physical model, or claim of emergence.

## Purpose

The code studies a simplified Dirac spectrum on a three-torus with variable radii `R = (R1, R2, R3)`. It counts modes below a scale `Lambda` and compares fixed-volume radius triples. The field-inspired candidate is treated as a hypothesis to test, not as a discovery.

This repository is deliberately a **falsification instrument**. A negative result is useful: it can stop an unsupported idea before months of deeper work are spent on it. A positive result is only a reason to design a stronger experiment.

## Diagnostics

- `random_baseline.py` compares the candidate with reproducible random unit-volume triples.
- `convergence.py` checks sensitivity to lattice cutoff, grid resolution, and `Lambda`.
- `minimize.py` performs the basic fixed-volume grid search.
- `plot_search.py` visualizes the search landscape.
- `dirac_t3.py` contains the simplified eigenvalue and state-count routines.

Run privately with:

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python random_baseline.py
python convergence.py
```

Generated outputs are written under `results/` and are ignored by Git. Record the environment and parameters after each run:

```bash
python --version
pip freeze > results/freeze.txt
echo "$RANDOM_SEED"
```

Also preserve the command-line arguments, random seed, proposal distribution, cutoff, grid size, and `Lambda` values.

## Interpretation rules

- A favorable percentile in one random baseline is not evidence of emergence; repeat with multiple seeds and proposal distributions.
- A stable optimum across finite cutoffs and grid sizes only reduces concern about one numerical artifact.
- A drifting optimum means the current objective or search is not reliable.
- The arithmetic candidate must be evaluated after a field-blind optimization, not inserted into the optimizer.
- Passing these tests would justify a better experiment, not a proof or completed physical theory.

## Remaining requirements

1. Replace the raw mode count with a justified spectral action `Tr f(D^2 / Lambda^2)`.
2. Establish convergence under the relevant limits.
3. Test multiple smooth functions `f` and spin-structure twists.
4. Use independent null models and field-blind optimization.
5. Define a mathematical or physical prediction that could be checked independently.

Keep this repository private until the diagnostics are independently reproducible and the stated checks have been addressed.
