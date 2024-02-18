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


def add_plan_features(df: pd.DataFrame, plans: pd.DataFrame) -> pd.DataFrame:
    """Attach the list price of each customer's plan."""
    return df.merge(plans[["plan_id", "list_price"]], on="plan_id", how="left")


def add_region_features(df: pd.DataFrame) -> pd.DataFrame:
    """Average monthly charges of each customer's region."""
    df = df.copy()
    df["region_avg_charges"] = (
        df.groupby("region")["monthly_charges"].transform("mean").fillna(0)
    )
    return df


def build_features(customers: pd.DataFrame, plans: pd.DataFrame) -> pd.DataFrame:
    df = add_tenure_features(customers)
    df = add_plan_features(df, plans)
    df = add_region_features(df)
    return df
