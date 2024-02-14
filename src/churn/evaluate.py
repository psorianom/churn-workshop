from sklearn.metrics import accuracy_score, roc_auc_score


def evaluate(model, X_test, y_test) -> dict:
    preds = model.predict(X_test)
    return {
        "auc": roc_auc_score(y_test, model.predict_proba(X_test)[:, 1]),
        "accuracy": accuracy_score(y_test, preds),
    }
