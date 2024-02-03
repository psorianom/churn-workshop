from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def load_customers() -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / "customers.csv")


def load_plans() -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / "plans.csv")
