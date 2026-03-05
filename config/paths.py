"""Project root and standard paths. All paths are relative to the project root."""
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
RAW_CSV_PATH = RAW_DATA_DIR / "transactions.csv"
DB_PATH = PROJECT_ROOT / "data" / "quality.db"
OUTPUT_DIR = PROJECT_ROOT / "output"
