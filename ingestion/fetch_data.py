"""Generate or fetch raw transaction data for the pipeline."""
import random

import numpy as np
import pandas as pd

from config.paths import RAW_CSV_PATH, RAW_DATA_DIR


def fetch_dummy_data():
    """Generate synthetic transaction data with some outliers and save to CSV."""
    np.random.seed(42)
    num_rows = 500

    user_ids = np.random.randint(1, 100, size=num_rows)
    amounts = np.random.normal(loc=200, scale=50, size=num_rows).round(2)

    for _ in range(10):
        idx = random.randint(0, num_rows - 1)
        amounts[idx] = random.choice([1000, 1500, 2000, 5, 10])

    start_date = pd.to_datetime("2024-01-01")
    timestamps = [
        start_date + pd.Timedelta(days=int(x))
        for x in np.random.randint(0, 60, size=num_rows)
    ]

    df = pd.DataFrame({
        "user_id": user_ids,
        "amount": amounts,
        "timestamp": timestamps,
    })

    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(RAW_CSV_PATH, index=False)
    print("✅ Data fetched and saved to raw folder.")