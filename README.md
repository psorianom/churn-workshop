# Churn Pipeline

Predicts which subscription customers will churn.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest
python run.py
```

## Pipeline

1. `data.py` loads the raw customer and plan tables from `data/`
2. `clean.py` normalizes text, removes duplicate ids and invalid rows
3. `features.py` builds tenure, plan, region and ticket features
4. `model.py` builds the feature matrix, splits, scales and trains a random forest
5. `evaluate.py` reports AUC and accuracy on the held-out set

## Troubleshooting

- `ModuleNotFoundError: churn`: run commands from the repository root (pytest and `run.py` add `src/` to the path for you).
- Results differ between runs: see the section on reproducibility (coming soon).
