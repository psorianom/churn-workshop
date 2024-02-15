from churn.clean import clean_customers
from churn.data import load_customers, load_plans
from churn.evaluate import evaluate
from churn.features import build_features
from churn.model import make_matrix, split_and_scale, train_model


def train_and_evaluate() -> dict:
    raw = load_customers()
    customers = clean_customers(raw)
    features = build_features(customers, load_plans())
    X, y = make_matrix(features)
    X_train, X_test, y_train, y_test = split_and_scale(X, y)
    model = train_model(X_train, y_train)
    metrics = evaluate(model, X_test, y_test)
    metrics.update(
        {
            "rows_raw": len(raw),
            "rows_clean": len(customers),
            "rows_features": len(features),
            "churn_rate": float(y.mean()),
        }
    )
    return metrics


def main() -> None:
    m = train_and_evaluate()
    print(f"AUC: {m['auc']:.3f}")


if __name__ == "__main__":
    main()
