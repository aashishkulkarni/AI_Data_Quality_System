from ingestion.fetch_data import fetch_dummy_data
from etl.transform_load import load_data_to_db
from monitoring.monitor import run_monitoring

if __name__ == "__main__":
    fetch_dummy_data()
    load_data_to_db()
    run_monitoring()
