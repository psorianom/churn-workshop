import pandas as pd

from churn.features import tenure_bucket, tenure_months


def test_tenure_months():
    signup = pd.Series(pd.to_datetime(["2023-01-15", "2023-12-01"]))
    assert list(tenure_months(signup)) == [12, 1]


def test_tenure_bucket_boundaries():
    assert tenure_bucket(5) == "0-5"
    assert tenure_bucket(6) == "6-11"
    assert tenure_bucket(11) == "6-11"
    assert tenure_bucket(12) == "12-23"
    assert tenure_bucket(23) == "12-23"
    assert tenure_bucket(24) == "24+"
