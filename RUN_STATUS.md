# Run status

## Current state

- Repository content: committed and ready
- Local virtual environment: not created in this workflow
- Tests: not executed in this workflow
- `random_baseline.py`: not executed in this workflow
- `convergence.py`: not executed in this workflow
- Numerical results: not generated or claimed
- Deployment: none

## Portfolio value

The project is valuable as a research-engineering artifact because it demonstrates:

- hypothesis-to-code translation,
- null-model falsification instead of confirmation,
- numerical convergence checks,
- reproducibility discipline,
- honest reporting of the limits of a toy model.

It is not valuable as a proof claim until the local run produces and verifies actual output artifacts.

## Execution gate

The probe becomes execution-verified only after a local run succeeds and `results/` contains all five files:

- `random_baseline.csv`
- `random_baseline.png`
- `convergence.csv`
- `python_version.txt`
- `freeze.txt`

Until then, the project is portfolio-ready in structure but not execution-verified.

## Local command

```bash
git clone https://github.com/MathHeroez/unknown.git
cd unknown
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pytest -v
python random_baseline.py
python convergence.py
python --version > results/python_version.txt
python -m pip freeze > results/freeze.txt
ls -lh results/
```

## Required reporting standard

After a successful run, report the actual observed values and make no stronger claim than the evidence supports.

Examples:

- "The candidate sits at the 3.2nd percentile under the tested random null model."
- "The optimum was stable across the tested cutoff and grid settings."
- "The result is inconclusive for the physical hypothesis, but the diagnostic pipeline is reproducible."

Do not report numerical findings until the five artifacts have been visibly verified and archived.
