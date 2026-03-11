import numpy as np

def create_features(df):

    print("\nCreating Features...")

    df["Shipping_Days"] = (df["Ship_Date"] - df["Order_Date"]).dt.days

    df["Order_Year"] = df["Order_Date"].dt.year

    df["Order_Month"] = df["Order_Date"].dt.month

    df["Sales_Level"] = np.where(df["Sales"] > 500, "High", "Low")

    print("Feature Engineering Completed")

    return df