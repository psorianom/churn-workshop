import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# TODO(stakeholder): wants AUC >= 0.85 before Friday. Try adding more features from the customer table.
NUMERIC = ["tenure_months", "monthly_charges", "usage_hours", "support_tickets", "late_payments", "list_price", "region_avg_charges", "tickets_per_year"]
CATEGORICAL = ["contract", "plan_id", "tenure_bucket"]


def make_matrix(features: pd.DataFrame):
    """Return (X, y) for modelling."""
    X = pd.get_dummies(features[NUMERIC + CATEGORICAL], columns=CATEGORICAL)
    y = features["churned"]
    return X, y


def split_and_scale(X: pd.DataFrame, y: pd.Series, test_size: float = 0.2):
    """Split into train and test sets, then scale the numeric columns using the training set only."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
    scaler = StandardScaler()
    X_train, X_test = X_train.copy(), X_test.copy()
    X_train[NUMERIC] = scaler.fit_transform(X_train[NUMERIC])
    X_test[NUMERIC] = scaler.transform(X_test[NUMERIC])
    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> RandomForestClassifier:
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    return model
