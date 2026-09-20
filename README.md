# S4 x T3 Dirac Spectral Action

## Objective

This project tests a simple geometric hypothesis: whether the field
K = Q(sqrt(2), sqrt(3), sqrt(5))
can emerge from minimizing a low-energy spectral count on a 3-torus.

The model studies the Dirac operator on T^3 with variable radii:

R = (R1, R2, R3)

and compares how many eigenmodes fall below a cutoff scale Lambda.

The central quantity is:

N(R) = #{mu < Lambda}

where the eigenvalues are modeled by

mu = 2*pi*sqrt( sum_i ((n_i + eps_i)/R_i)^2 )

with twisted boundary conditions encoded by eps = (1/2, 1/2, 1/2).

## Scientific motivation

The idea is to test whether a special geometric ratio is preferred by the low-energy spectrum. If the minimizing radius configuration is close to the values suggested by the field
K = Q(sqrt(2), sqrt(3), sqrt(5)),
then the geometry may be encoding the same arithmetic data.

This is a numerical exploratory test rather than a formal theorem.

## Repository contents

- `dirac_t3.py` — Dirac eigenvalue and counting routines
- `minimize.py` — brute-force search over radius ratios with fixed volume
- `plot_search.py` — optional surface/heatmap visualization of the search landscape
- `README.md` — project summary and usage notes
- `.gitignore` — local environment and cache exclusions
- `requirements.txt` — dependency list

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python minimize.py
python plot_search.py
```

## Interpretation of results

- If the best numerical minimum is close to the isotropic point `(1,1,1)`, then the spectral count does not prefer the special field-based geometry.
- If the numerical minimum is close to a structured ratio such as
  sqrt(3/2) and sqrt(5/2),
  then the field-based candidate is favored by the optimization.
- The comparison is meaningful only when the total torus volume is held fixed during the search.

## Security and reproducibility

- Keep the repository private if the work is unpublished or exploratory.
- Do not commit tokens or secrets.
- Use a GitHub fine-grained PAT or SSH for pushing.
- Protect the `main` branch with PR review and required status checks.
