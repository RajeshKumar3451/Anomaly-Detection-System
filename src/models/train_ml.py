from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib
import os

from src.data.preprocessing import preprocess

X, y = preprocess()

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", IsolationForest(contamination=0.1, random_state=42))
])

pipeline.fit(X)
os.makedirs("models", exist_ok=True)

joblib.dump(pipeline, "models/pipeline.pkl")
print("✅ Pipeline trained and saved successfully!")