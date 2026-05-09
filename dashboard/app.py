import streamlit as st
import requests

# -----------------------------
# Config
# -----------------------------
st.set_page_config(page_title="Anomaly Detection Dashboard", layout="wide")

API_URL = "http://127.0.0.1:8000/predict"

# -----------------------------
# Title
# -----------------------------
st.title("🛡️ Behavioral Anomaly Detection System")

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("User Behavior Input")

typing_speed = st.sidebar.slider("Typing Speed", 0, 500, 200)
mouse_speed = st.sidebar.slider("Mouse Speed", 0, 300, 100)
click_rate = st.sidebar.slider("Click Rate", 0, 20, 5)
session_time = st.sidebar.slider("Session Time", 0, 600, 300)

analyze = st.sidebar.button("Analyze Session")

# -----------------------------
# Main Layout
# -----------------------------
col1, col2, col3 = st.columns(3)

# -----------------------------
# Run Prediction
# -----------------------------
if analyze:
    payload = {
        "typing_speed": typing_speed,
        "mouse_speed": mouse_speed,
        "click_rate": click_rate,
        "session_time": session_time
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        result = response.json()

        risk_score = result["risk_score"]
        risk_level = result["risk_level"]
        prediction = result["prediction"]
        anomaly_score = result["anomaly_score"]

        # -----------------------------
        # KPI Cards
        # -----------------------------
        with col1:
            st.metric("Prediction", prediction)

        with col2:
            st.metric("Risk Level", risk_level)

        with col3:
            st.metric("Risk Score", f"{risk_score}/100")

        st.markdown("---")

        # -----------------------------
        # Risk Visualization (Gauge Style)
        # -----------------------------
        st.subheader("Risk Visualization")

        if risk_score < 40:
            color = "green"
        elif risk_score < 70:
            color = "orange"
        else:
            color = "red"

        st.markdown(
            f"""
            <div style="background-color:{color};
                        padding:20px;
                        border-radius:10px;
                        text-align:center;
                        color:white;
                        font-size:24px;">
                Risk Score: {risk_score}
            </div>
            """,
            unsafe_allow_html=True
        )

        # -----------------------------
        # Behavior Breakdown
        # -----------------------------
        st.subheader("Behavior Analysis")

        st.write(f"Typing Speed: {typing_speed}")
        st.write(f"Mouse Speed: {mouse_speed}")
        st.write(f"Click Rate: {click_rate}")
        st.write(f"Session Time: {session_time}")

        st.write(f"Anomaly Score: {anomaly_score:.4f}")

        # -----------------------------
        # Insights Section
        # -----------------------------
        st.subheader("Insights")

        if risk_level == "High":
            st.error("⚠️ High anomaly detected. Possible bot or fraud behavior.")
        elif risk_level == "Medium":
            st.warning("⚠️ Suspicious behavior detected. Monitor closely.")
        else:
            st.success("✅ Normal behavior.")

    else:
        st.error("API Error")