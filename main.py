"""Run the full data quality pipeline: ingest → ETL → monitor."""
import sys

from ingestion.fetch_data import fetch_dummy_data
from etl.transform_load import load_data_to_db
from monitoring.monitor import run_monitoring


def main():
    """Execute ingestion, load to DB, and run anomaly monitoring."""
    try:
        fetch_dummy_data()
        load_data_to_db()
        run_monitoring()
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
