# AGENTS.md

## Project
Customer churn pipeline (pandas + scikit-learn).
Source in `src/churn/`, tests in `tests/`, data in `data/`.

## Commands
- Run all tests: `pytest`
- Run one test: `pytest tests/test_clean.py::test_name`
- Run the pipeline: `python run.py`

## Rules
- Work on a branch, never directly on `main`.
- Do not edit or delete existing tests to make them pass. If a test looks wrong, say so and ask.
- Do not change the signatures of public functions in `src/churn/`.
- Do not modify files in `data/`.
- Do not add new dependencies.
- Keep changes small and scoped to the task.
- After changing data-processing code, run `python run.py` and check that the row counts between stages make sense.
