"""Anomaly detection using scikit-learn Isolation Forest."""
import pandas as pd
from sklearn.ensemble import IsolationForest

from config.db_config import get_engine


def detect_anomalies():
    """
    Load transactions from the database and flag anomalies in the amount column.
    Uses Isolation Forest (unsupervised). Returns DataFrame with an 'anomaly' column
    (1 = normal, -1 = anomaly).
    """
    engine = get_engine()
    df = pd.read_sql("SELECT * FROM transactions", engine)

    model = IsolationForest(contamination=0.25, random_state=42)
    df["anomaly"] = model.fit_predict(df[["amount"]])

    print(df[["user_id", "amount", "anomaly"]])
    return df