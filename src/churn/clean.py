import pandas as pd


def clean_customers(df: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned copy of the raw customers table."""
    df = df.copy()
    df["signup_date"] = pd.to_datetime(df["signup_date"])
    df["plan_id"] = df["plan_id"].str.strip().str.lower()
    df["contract"] = df["contract"].str.strip().str.lower()
    df = df.drop_duplicates(subset="customer_id", keep="first")
    # negative charges are billing errors; zero is a legitimate free plan
    df = df[df["monthly_charges"] >= 0].copy()
    df["usage_hours"] = df["usage_hours"].fillna(df["usage_hours"].median())
    return df.reset_index(drop=True)
