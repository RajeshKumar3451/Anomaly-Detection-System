import numpy as np
import pandas as pd

np.random.seed(42)

def generate_data(n_normal=5000, n_anomaly=500):
    
    normal = pd.DataFrame({
        "typing_speed": np.random.normal(200, 20, n_normal),
        "mouse_speed": np.random.normal(100, 15, n_normal),
        "click_rate": np.random.normal(5, 1, n_normal),
        "session_time": np.random.normal(300, 50, n_normal)
    })
    normal["label"] = 0

    anomaly = pd.DataFrame({
        "typing_speed": np.random.normal(400, 60, n_anomaly),
        "mouse_speed": np.random.normal(300, 60, n_anomaly),
        "click_rate": np.random.normal(15, 4, n_anomaly),
        "session_time": np.random.normal(50, 20, n_anomaly)
    })
    anomaly["label"] = 1

    df = pd.concat([normal, anomaly])
    df.to_csv("data/synthetic_data.csv", index=False)

if __name__ == "__main__":
    generate_data()