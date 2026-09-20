# S4 x T3 Dirac Spectral Action

Testing whether the field
K = Q(sqrt(2), sqrt(3), sqrt(5))
emerges from minimizing the spectral action.

## Goal

We study the Dirac spectrum on a 3-torus with variable radii:

R = (R1, R2, R3)

and compare the number of low-lying eigenmodes below a cutoff scale Lambda.

The key object is:

N(R) = #{mu < Lambda}

where the eigenvalues are

mu = 2*pi*sqrt( sum_i ((n_i + eps_i)/R_i)^2 )

with twisted boundary conditions encoded by eps = (1/2, 1/2, 1/2).

## Files

- `dirac_t3.py`: Dirac spectrum implementation
- `minimize.py`: numerical search for the lowest-count radius ratio

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python minimize.py
```

## Notes

- The optimizer keeps the total 3D volume fixed while scanning radius ratios.
- This is a numerical exploratory starter, not a full physical derivation.
- The goal is to test whether the geometry tied to the field
  K = Q(sqrt(2), sqrt(3), sqrt(5)) is favored by the low-energy spectral count.

## Security and repo hygiene

- Keep the repository private if this contains unpublished or exploratory work.
- Do not commit tokens, secrets, or local environment files.
- Use a GitHub fine-grained PAT or SSH for pushing.
- Protect the `main` branch with pull-request review and required status checks.
