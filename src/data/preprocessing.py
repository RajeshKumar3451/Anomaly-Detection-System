import pandas as pd
import os

def preprocess():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    file_path = os.path.join(BASE_DIR, "data", "synthetic_data.csv")

    df = pd.read_csv(file_path)

    # Feature Engineering
    df["typing_variance"] = df["typing_speed"].rolling(5).std().fillna(0)
    df["click_diff"] = df["click_rate"].diff().fillna(0)

    X = df.drop("label", axis=1)
    y = df["label"]

    return X, y