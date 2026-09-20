# Run status

## Current state

- Repository content: committed and ready
- Local virtual environment: not created in this workflow
- Tests: not executed in this workflow
- `random_baseline.py`: not executed in this workflow
- `convergence.py`: not executed in this workflow
- Numerical results: not generated or claimed
- Deployment: none

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

Do not report numerical findings until the five artifacts have been visibly verified and archived.
