# S4 x T3 Dirac Spectral Action: A Toy Probe

> Honest status: this repository is a small computational probe for a conjectural idea, not a proof and not a physical model. It explores whether a simplified spectral-count objective on a 3-torus favors a special arithmetic radius ratio.

## What this project does

This project studies a simplified Dirac spectrum on a three-torus \(T^3\) with variable radii

\[
R=(R_1,R_2,R_3).
\]

The code computes a finite set of eigenvalues and counts how many of them lie below a cutoff scale \(\Lambda\):

\[
N(R)=\#\{\mu : \mu^2<\Lambda^2\}.
\]

It then compares different radius ratios while keeping the total volume fixed. The goal is not to claim a theorem, but to see whether a structured geometry is numerically favored under a simple spectral heuristic.

## What this project is not

- It is not a proof that \(\mathbb{Q}(\sqrt{2},\sqrt{3},\sqrt{5})\) emerges from geometry.
- It is not a complete spectral-action calculation.
- It is not a validated physical model.
- It is not a real-world engineering or prediction tool.
- It is not a theory of everything.

This is intentionally a toy experiment. It exists to answer one narrow question: does the idea survive a quick numerical sanity check?

## Why it may still be useful

A minimized spectral heuristic can be useful as a hypothesis generator. It is a way to test whether a concept is obviously nonsense or is worth more careful mathematical work. The repository is therefore a quick reproducibility tool and a transparency device: it makes the assumptions visible instead of hiding them behind vague claims.

## Current limitations

1. The objective is a raw state count, not the full spectral action.
2. The search is a finite grid, not a mathematically rigorous global optimization.
3. The cutoff introduces discretization effects and convergence questions.
4. The candidate field may be implicitly baked into the setup instead of predicted independently.
5. No experimental or physical prediction is claimed.
6. No claim of emergence or proof is made.

## Repository contents

- `dirac_t3.py` — simplified Dirac eigenvalue and counting routines
- `minimize.py` — fixed-volume ratio search over a grid of radii
- `plot_search.py` — heatmap-based visualization of the search landscape
- `README.md` — project goals, scope, and caveats
- `.gitignore` — local environment and generated artifact exclusions
- `requirements.txt` — project dependencies

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python minimize.py
python plot_search.py
```

The plotting script saves a PNG image to `spectral_search.png`.

## Interpretation of results

- If the minimum stays near the isotropic point, the simplified objective does not favor a special structured geometry.
- If the minimum is near a structured ratio, that is only a numerical clue. It is not evidence of emergence and requires a more rigorous model.
- This project is intentionally designed to test plausibility, not to establish a conclusion.

## What would make the experiment stronger?

A more serious follow-up would require:

1. Replacing the count with a true spectral action objective.
2. Running convergence checks over cutoff and grid size.
3. Comparing against a large random baseline of fixed-volume radius triples.
4. Testing multiple objective functions and parameter choices.
5. Reporting whether the candidate arithmetic field was independently predicted or simply inserted by hand.
6. Defining a mathematically or physically meaningful prediction that could be checked independently.

## Security and reproducibility

- Keep unpublished work private if appropriate.
- Do not commit credentials, tokens, or environment files.
- Record the Python version and dependency versions used for any numerical result.
- Report search bounds, cutoff values, and assumptions clearly.

## Final framing

This repository is best understood as a small, honest toy probe: a reproducible numerical experiment designed to test whether a conjectural geometric pattern is worth deeper mathematical investigation. It is not a proof, not a validated theory, and not a real-world application.
