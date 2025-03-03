# This is to extract and read data from pandas_practice database
import pandas as pd
import sqlalchemy
from config import DB_CONFIG

def extract_data(query : str) -> pd.DataFrame :
    """Extract data from mysql database. """
    engine = sqlalchemy.create_engine(
        f"{DB_CONFIG['DB_TYPE']}+mysqlconnector://{DB_CONFIG['DB_USER']}:{DB_CONFIG['DB_PASS']}@{DB_CONFIG['DB_HOST']}:{DB_CONFIG['DB_PORT']}/{DB_CONFIG['DB_NAME']}"
    )
    df = pd.read_sql(query, engine)
    return df
