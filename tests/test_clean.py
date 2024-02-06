import pandas as pd

from churn.clean import clean_customers
from churn.data import load_customers


def test_duplicate_ids_removed():
    cleaned = clean_customers(load_customers())
    assert cleaned["customer_id"].is_unique


def test_negative_charges_dropped():
    cleaned = clean_customers(load_customers())
    assert (cleaned["monthly_charges"] >= 0).all()


def test_dates_are_parsed():
    cleaned = clean_customers(load_customers())
    assert pd.api.types.is_datetime64_any_dtype(cleaned["signup_date"])


def test_free_plan_customers_kept():
    raw = load_customers()
    cleaned = clean_customers(raw)
    free_ids = raw.loc[raw["plan_id"].str.strip().str.lower() == "free", "customer_id"].unique()
    assert len(free_ids) > 0
    assert set(free_ids) <= set(cleaned["customer_id"])
