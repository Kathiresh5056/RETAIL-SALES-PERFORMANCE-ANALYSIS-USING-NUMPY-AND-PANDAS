import pandas as pd

def clean_data(df):

    df = df.drop_duplicates()

    df["Order_Date"] = pd.to_datetime(df["Order_Date"], dayfirst=True, errors="coerce")
    df["Ship_Date"] = pd.to_datetime(df["Ship_Date"], dayfirst=True, errors="coerce")

    df = df.ffill()

    print("Cleaning Completed")

    return df