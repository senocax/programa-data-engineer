# Import main libraries
import sqlite3
import pandas as pd
import logging.config
from os import path
from get_usa_medals import get_usa_medals

# Define path db and tablename
_DBPATH = "db/olympics.db"
_table = "medals"

# ----- Config logging ------
log_file_path = path.join(
    path.dirname(
        path.abspath('log_file_config.conf')),
    'log_file_config.conf')
logging.config.fileConfig(log_file_path)
logger_main = logging.getLogger("database")
# -----End Config logging ------

# Connect to database 
with sqlite3.connect(_DBPATH) as conn:
    # Create cursor
    cursor = conn.cursor()

    # Create table medales
    query_table = f"""CREATE TABLE IF NOT EXISTS {_table} (
            Year INTEGER,
            City TEXT,
            Sport TEXT,
            Discipline TEXT,
            NOC TEXT,
            Event TEXT,
            'Event gender' TEXT,
            Medal TEXT
            )"""

    # Execute SQL query
    cursor.execute(query_table)
    conn.commit()

    # Get and Save subset dataframe into table medals
    US_Gold = get_usa_medals()
    US_Gold.to_sql(_table, con=conn, if_exists='replace', index=False)

    # Validate data has been loaded correctly
    logger_main.info(pd.read_sql(f'select * from {_table}', conn)
)

