import pandas as pd


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Applying transformations on Dataframe. """
    df = df.rename(columns={"id": "student_id", "name": "student_name"})
    return df
