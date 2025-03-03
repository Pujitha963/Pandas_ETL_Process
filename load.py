import pandas as pd

def save_to_csv(df: pd.DataFrame, filePath: str):
    """Save the transformed dataframe to a csv file."""
    df.to_csv(filePath, index=False)
    print(f"Data saved to file path : {filePath}")