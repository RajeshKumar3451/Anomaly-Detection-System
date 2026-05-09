import streamlit as st
import pandas as pd
import numpy as np
import requests
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="AnomalyGuard AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    .main {
        background-color: #0E1117;
        color: white;
    }

    .metric-card {
        background: linear-gradient(135deg, #1f2937, #111827);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 0px 15px rgba(0,255,255,0.1);
    }

    .risk-high {
        color: #ff4b4b;
        font-weight: bold;
    }

    .risk-medium {
        color: orange;
        font-weight: bold;
    }

    .risk-low {
        color: #00ff88;
        font-weight: bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.title("🛡️ AnomalyGuard AI")
st.caption("Behavioral Fraud Intelligence Platform")

st.sidebar.title("⚙️ Session Simulator")

API_URL = "https://anomalyguard-ai.onrender.com/predict"

typing_speed = st.sidebar.slider("Typing Speed", 0, 400, 220)
mouse_speed = st.sidebar.slider("Mouse Speed", 0, 300, 110)
click_rate = st.sidebar.slider("Click Rate", 0, 20, 6)
session_time = st.sidebar.slider("Session Time", 0, 1000, 350)


payload = {
    "typing_speed": typing_speed,
    "mouse_speed": mouse_speed,
    "click_rate": click_rate,
    "session_time": session_time
}

response = requests.post(API_URL, json=payload)

result = response.json()

prediction = result["prediction"]
anomaly_score = result["anomaly_score"]
risk_level = result["risk_level"]
risk_score = result["risk_score"]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Prediction",
        prediction
    )

with col2:
    st.metric(
        "Risk Level",
        risk_level
    )

with col3:
    st.metric(
        "Risk Score",
        risk_score
    )

with col4:
    st.metric(
        "Anomaly Score",
        round(anomaly_score, 4)
    )

st.subheader("🎯 Fraud Risk Meter")

fig_gauge = go.Figure(go.Indicator(
    mode="gauge+number",
    value=risk_score,
    title={'text': "Risk Score"},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "red"},
        'steps': [
            {'range': [0, 35], 'color': "green"},
            {'range': [35, 70], 'color': "orange"},
            {'range': [70, 100], 'color': "red"}
        ],
    }
))

st.plotly_chart(fig_gauge, use_container_width=True)

st.subheader("📊 Behavioral Analytics")

behavior_df = pd.DataFrame({
    "Feature": [
        "Typing Speed",
        "Mouse Speed",
        "Click Rate",
        "Session Time"
    ],
    "Value": [
        typing_speed,
        mouse_speed,
        click_rate,
        session_time
    ]
})

fig_bar = px.bar(
    behavior_df,
    x="Feature",
    y="Value",
    color="Value",
    title="User Behavioral Signals"
)

st.plotly_chart(fig_bar, use_container_width=True)

st.subheader("📈 Session Activity Timeline")

np.random.seed(42)

time_data = pd.DataFrame({
    "Time": range(1, 51),
    "Risk": np.random.normal(risk_score, 8, 50)
})

fig_line = px.line(
    time_data,
    x="Time",
    y="Risk",
    title="Behavioral Risk Over Session"
)

st.plotly_chart(fig_line, use_container_width=True)

st.subheader("🚨 Threat Intelligence")

if risk_level == "High":
    st.error("Potential fraudulent behavior detected")

elif risk_level == "Medium":
    st.warning("Suspicious behavioral pattern detected")

else:
    st.success("Behavior appears authentic")

st.subheader("🧠 Session Intelligence")

session_table = pd.DataFrame({
    "Metric": [
        "Typing Speed",
        "Mouse Speed",
        "Click Rate",
        "Session Time",
        "Prediction",
        "Risk Level"
    ],
    "Value": [
        typing_speed,
        mouse_speed,
        click_rate,
        session_time,
        prediction,
        risk_level
    ]
})

st.dataframe(session_table, use_container_width=True)

st.markdown("---")
st.caption(
    "AnomalyGuard AI • Real-Time Behavioral Fraud Detection"
)
