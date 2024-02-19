import pandas as pd


def _normalize(series: pd.Series) -> pd.Series:
    return series.str.strip().str.lower()


def clean_customers(df: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned copy of the raw customers table."""
    df = df.copy()
    df["signup_date"] = pd.to_datetime(df["signup_date"])
    df["plan_id"] = _normalize(df["plan_id"])
    df["contract"] = _normalize(df["contract"])
    df = df.drop_duplicates(subset="customer_id", keep="first")
    valid = df["monthly_charges"] > 0
    df = df[valid].copy()
    df["usage_hours"] = df["usage_hours"].fillna(df["usage_hours"].median())
    return df.reset_index(drop=True)
