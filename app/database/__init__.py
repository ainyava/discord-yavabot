from .connection import get_connection
from .setup_tables import setup_tables

import logging

connection = get_connection()
logging.info("setting up database tables")
setup_tables(connection=connection)

__all__ = [
    "connection",
]
