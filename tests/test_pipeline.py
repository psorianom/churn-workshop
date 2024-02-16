from churn.pipeline import train_and_evaluate


def test_pipeline_runs_and_returns_metrics():
    metrics = train_and_evaluate()
    assert {"auc", "accuracy"} <= set(metrics)


def test_auc_is_in_valid_range():
    metrics = train_and_evaluate()
    assert 0.5 < metrics["auc"] <= 1.0


def test_training_is_deterministic():
    first = train_and_evaluate()
    second = train_and_evaluate()
    assert first["auc"] == second["auc"]
