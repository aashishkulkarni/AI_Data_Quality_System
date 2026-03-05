# AI Data Quality System

A Python pipeline that ingests transaction-style data, loads it into a database, and uses ML (Isolation Forest) to detect anomalies for data quality monitoring.

## Features

- **Ingestion:** Generate or load raw transaction data (user_id, amount, timestamp).
- **ETL:** Clean and load data into SQLite via SQLAlchemy.
- **Monitoring:** Unsupervised anomaly detection with scikit-learn Isolation Forest; reports written to `output/`.

## Getting Started

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aashishkulkarni/AI_Data_Quality_System.git
   cd AI_Data_Quality_System
   ```
2. Create a virtual environment (recommended) and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

### Usage

1. From the project root, run the pipeline:
   ```bash
   python main.py
   ```
2. Review the anomaly report in the `output/` directory.

## Project Structure

```
AI_Data_Quality_System/
├── config/
│   └── db_config.py      # Database connection (SQLite)
├── data/
│   └── raw/              # Raw input data (e.g. transactions.csv)
├── etl/
│   └── transform_load.py # Load and clean data into DB
├── ingestion/
│   └── fetch_data.py     # Fetch/generate raw data
├── models/
│   └── anomaly_detector.py  # Isolation Forest anomaly detection
├── monitoring/
│   └── monitor.py        # Run monitoring and write reports
├── output/               # Generated reports (anomaly summary)
├── main.py
├── requirements.txt
└── README.md
```
