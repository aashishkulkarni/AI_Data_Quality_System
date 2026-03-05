"""Load raw data into the database with basic cleaning."""
import pandas as pd

from config.db_config import get_engine
from config.paths import RAW_CSV_PATH


def load_data_to_db():
    """Read raw transactions CSV, fill nulls, and load into the database."""
    if not RAW_CSV_PATH.exists():
        raise FileNotFoundError(
            f"Raw data not found at {RAW_CSV_PATH}. Run the pipeline from project root "
            "so ingestion runs first, or ensure data/raw/transactions.csv exists."
        )
    df = pd.read_csv(RAW_CSV_PATH)
    df.fillna(0, inplace=True)

    engine = get_engine()
    df.to_sql("transactions", engine, if_exists="replace", index=False)
    print("✅ Data loaded into database.")