import pandas as pd
from config.db_config import get_engine

def load_data_to_db():
    df = pd.read_csv('data/raw/transactions.csv')
    df.fillna(0, inplace=True)

    engine = get_engine()
    df.to_sql('transactions', engine, if_exists='replace', index=False)
    print("✅ Data loaded into database.")