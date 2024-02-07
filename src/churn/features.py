import pandas as pd

AS_OF = pd.Timestamp("2024-01-01")


def tenure_months(signup_date: pd.Series) -> pd.Series:
    """Whole calendar months between signup and the reference date."""
    return (AS_OF.year - signup_date.dt.year) * 12 + (AS_OF.month - signup_date.dt.month)


def tenure_bucket(months: int) -> str:
    if months < 6:
        return "0-5"
    if months < 12:
        return "6-11"
    if months < 24:
        return "12-23"
    return "24+"


def add_tenure_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["tenure_months"] = tenure_months(df["signup_date"])
    df["tenure_bucket"] = df["tenure_months"].map(tenure_bucket)
    return df
