import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    # Convert price columns to numeric
    for col in ["Open", "High", "Low", "Close", "Volume"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df
