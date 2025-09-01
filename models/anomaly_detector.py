import pandas as pd
from sklearn.ensemble import IsolationForest
from config.db_config import get_engine

def detect_anomalies():
    engine = get_engine()
    df = pd.read_sql('SELECT * FROM transactions', engine)

    model = IsolationForest(contamination=0.25, random_state=42)
    df['anomaly'] = model.fit_predict(df[['amount']])

    print(df[['user_id', 'amount', 'anomaly']])
    return df


# IsolationForest is a smart tool to help spot outliers or potential problems in your data!