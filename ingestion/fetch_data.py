import pandas as pd
import numpy as np
import random

def fetch_dummy_data():

    np.random.seed(42)
    num_rows = 500

    user_ids = np.random.randint(1, 100, size=num_rows)
    amounts = np.random.normal(loc=200, scale=50, size=num_rows).round(2)

    for _ in range(10):
        idx = random.randint(0, num_rows - 1)
        amounts[idx] = random.choice([1000, 1500, 2000, 5, 10])

    start_date = pd.to_datetime("2024-01-01")
    timestamps = [start_date + pd.Timedelta(days = int(x)) for x in np.random.randint(0, 60, size=num_rows)]

    df = pd.DataFrame({
        'user_id': user_ids,
        'amount': amounts,
        'timestamp': timestamps
    })

    df.to_csv('data/raw/transactions.csv', index=False)
    print("✅ Data fetched and saved to raw folder.")