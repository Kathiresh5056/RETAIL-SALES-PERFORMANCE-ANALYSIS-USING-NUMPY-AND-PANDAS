import pandas as pd

def load_data(path):
    df = pd.read_csv(path, encoding="latin1")
    
    print("\nDataset Loaded Successfully")
    print("Shape:", df.shape)

    return df