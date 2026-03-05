"""Database connection configuration."""
from sqlalchemy import create_engine

from config.paths import DB_PATH


def get_engine():
    """Return a SQLAlchemy engine for the project SQLite database."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return create_engine(f"sqlite:///{DB_PATH}", echo=False)
