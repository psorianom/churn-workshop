from churn.data import load_customers, load_plans


def test_customers_have_expected_columns():
    df = load_customers()
    for col in [
        "customer_id",
        "signup_date",
        "plan_id",
        "region",
        "contract",
        "monthly_charges",
        "usage_hours",
        "support_tickets",
        "late_payments",
        "churned",
    ]:
        assert col in df.columns


def test_customers_not_empty():
    assert len(load_customers()) > 1000


def test_plans_loaded():
    assert {"plan_id", "list_price"} <= set(load_plans().columns)
