import os
import logging
import joblib
import pandas as pd

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Behavioral Anomaly Detection API",
    version="1.0.0"
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PIPELINE_PATH = os.path.join(BASE_DIR, "models", "pipeline.pkl")

if not os.path.exists(PIPELINE_PATH):
    raise RuntimeError(f"Pipeline not found at {PIPELINE_PATH}")

if os.path.getsize(PIPELINE_PATH) == 0:
    raise RuntimeError("Pipeline file is empty or corrupted")

try:
    pipeline = joblib.load(PIPELINE_PATH)
    logger.info("Pipeline loaded successfully")

except Exception as e:
    logger.error(f"Error loading pipeline: {e}")
    raise RuntimeError("Failed to load pipeline")

class UserInput(BaseModel):
    typing_speed: float
    mouse_speed: float
    click_rate: float
    session_time: float

@app.get("/")
def home():
    return {
        "status": "API Running",
        "service": "Behavioral Anomaly Detection"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

THRESHOLD_LOW = -0.05
THRESHOLD_HIGH = -0.15

def map_risk(score: float):


    if score < THRESHOLD_HIGH:
        risk_level = "High"

    elif score < THRESHOLD_LOW:
        risk_level = "Medium"

    else:
        risk_level = "Low"

    # Convert anomaly score → risk score (0-100) More negative = higher risk
    risk_score = int(min(max(abs(score) * 400, 0), 100))

    return risk_level, risk_score

@app.post("/predict")
def predict(data: UserInput):

    try:
        df = pd.DataFrame([{
            "typing_speed": data.typing_speed,
            "mouse_speed": data.mouse_speed,
            "click_rate": data.click_rate,
            "session_time": data.session_time,

            
            "typing_variance": 0.0,
            "click_diff": 0.0
        }])

        pred = pipeline.predict(df)[0]

        score = pipeline.decision_function(df)[0]

        
        prediction = "Anomaly" if pred == -1 else "Normal"

        
        risk_level, risk_score = map_risk(score)

       
        return {
            "prediction": prediction,
            "anomaly_score": round(float(score), 4),
            "risk_level": risk_level,
            "risk_score": risk_score
        }

    except Exception as e:

        logger.error(f"Prediction error: {e}")

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )