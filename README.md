# S4 x T3 Dirac Spectral Action: A Toy Probe

> **Honest status:** This is a computational toy model for investigating whether certain arithmetic radius ratios are favored by a simplified spectral-count objective. It does **not** prove that \(\mathbb{Q}(\sqrt{2},\sqrt{3},\sqrt{5})\) emerges from geometry.

## What this project is

A reproducible test rig for checking a mathematical hunch quickly—minutes of computation instead of months of hand-waving.

The code explores a simplified Dirac spectrum on a three-torus \(T^3\) with variable radii

\[
R=(R_1,R_2,R_3),
\]

and counts modes below a cutoff:

\[
N(R)=\#\{\mu: \mu^2<\Lambda^2\}.
\]

It compares radius configurations at fixed volume, including a candidate related to

\[
\mathbb{Q}(\sqrt{2},\sqrt{3},\sqrt{5}).
\]

## What this project is not

- Not a proof that the field \(\mathbb{Q}(\sqrt{2},\sqrt{3},\sqrt{5})\) emerges.
- Not a complete spectral-action calculation.
- Not a validated physical model.
- Not a real-world engineering, medical, financial, or prediction tool.
- Not evidence for a Theory of Everything.

The current objective is deliberately limited and simplified. The candidate field was considered from the outset, so treating a favorable result as a discovery would be circular.

## Why it may still be useful

This repository provides a small, reproducible way to test whether the idea survives basic numerical scrutiny. A negative result is useful: it can rule out an attractive but unsupported conjecture before substantial effort is spent on it. A positive result would only motivate better-controlled research; it would not establish the conjecture.

## Current limitations

1. **Simplified objective** — the code minimizes a mode count rather than the full spectral action \(\operatorname{Tr} f(D^2/\Lambda^2)\).
2. **Finite numerical search** — results depend on grid resolution and search bounds.
3. **Cutoff dependence** — both the lattice cutoff and \(\Lambda\) require convergence studies.
4. **Possible degeneracies and boundary effects** — a low count need not represent meaningful geometry.
5. **Circular candidate selection** — the arithmetic field was not predicted independently of the experiment.
6. **No empirical connection** — the model currently makes no tested prediction about the physical world.

## Files

- `dirac_t3.py` — simplified T³ Dirac eigenvalue and state-count routines
- `minimize.py` — fixed-volume grid search over radius ratios
- `plot_search.py` — heatmap of the grid search
- `requirements.txt` — Python dependencies
- `.gitignore` — local environment and generated-file exclusions

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python minimize.py
python plot_search.py
```

The plotting script writes `spectral_search.png`, which is intentionally ignored by Git.

## What would make the test stronger?

A more serious follow-up should:

1. Replace the count with a justified spectral-action objective,
   \(\operatorname{Tr} f(D^2/\Lambda^2)\).
2. Test convergence as the lattice cutoff tends to infinity.
3. Repeat the search over many \(\Lambda\), twist parameters, and volume normalizations.
4. Compare against thousands of random fixed-volume radius triples, not only \((1,1,1)\).
5. Use independent optimization methods and report uncertainty or tie structure.
6. Test whether the special field was selected by the model rather than inserted as a candidate.
7. State a mathematical or physical prediction that could in principle be independently checked.

## Interpretation

If the minimum is near \((1,1,1)\), this simple objective does not favor the proposed structured ratio.

If a structured ratio repeatedly appears, that is only a numerical clue. It could reflect discretization, symmetry, cutoff artifacts, or the choice of objective. It should be treated as a hypothesis for further analysis—not as proof of emergence.

## Reproducibility and security

Keep unpublished work private if appropriate. Do not commit credentials, tokens, or environment files. Record the Python version, dependency versions, search bounds, cutoff values, and random seeds for any reported result.

## License and collaboration

This is an exploratory research prototype. Contributions that add convergence checks, null models, analytic comparisons, or corrections to the assumptions are especially welcome.
