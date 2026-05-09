# 🧠 Behavioral Anomaly Detection System 🚀

### ML + Deep Learning + Real-Time API + Dashboard + Docker

---

## 🔥 Overview

This project builds an **end-to-end Behavioral Anomaly Detection System** that analyzes user interaction patterns (typing speed, mouse movement, click behavior, session dynamics) to detect **fraudulent or bot-like activity in real time**.

It combines **Machine Learning, Deep Learning, and MLOps practices** to simulate a real-world fraud detection system.

---

## 🎯 Problem Statement

Traditional authentication methods (passwords, OTPs) fail to detect:

* Bot activity
* Account takeovers
* Behavioral anomalies

👉 This system introduces **behavioral biometrics** to continuously validate user authenticity.

---

## 💡 Solution

We model user interaction behavior and detect anomalies using:

* 🤖 **Isolation Forest (ML)** → Detect rare abnormal patterns
* 🧠 **Autoencoder (DL)** → Reconstruction-based anomaly detection
* ⚡ **FastAPI** → Real-time prediction service
* 📊 **Streamlit Dashboard** → Interactive visualization
* 🐳 **Docker** → Production-ready deployment

---

## 🏗️ Architecture

```
User Behavior Data 
        ↓
Feature Engineering (Behavioral + Temporal)
        ↓
ML/DL Models (Isolation Forest + Autoencoder)
        ↓
FastAPI (Real-Time Inference)
        ↓
Streamlit Dashboard (Visualization)
```

---

## 📊 Key Insights (EDA)

* Behavioral features strongly differentiate normal vs anomalous users

* Anomalies show:

  * Higher typing speed
  * Higher mouse velocity
  * Increased click frequency
  * Shorter session durations

* Statistical tests confirm **significant differences (p < 0.05)**

* PCA reveals **clear clustering of anomalies**

* Risk scoring aligns with anomalous behavior

---

## ⚙️ Tech Stack

| Layer         | Tools                           |
| ------------- | ------------------------------- |
| Data          | Pandas, NumPy                   |
| ML            | Scikit-learn (Isolation Forest) |
| DL            | PyTorch (Autoencoder)           |
| API           | FastAPI                         |
| Dashboard     | Streamlit                       |
| Visualization | Matplotlib, Seaborn             |
| Deployment    | Docker                          |
| EDA           | Statistical Testing, PCA        |

---

## 🚀 Features

* ✅ Real-time anomaly detection
* ✅ Behavioral feature engineering
* ✅ Deep learning-based anomaly scoring
* ✅ Risk scoring system
* ✅ Interactive dashboard
* ✅ Dockerized deployment
* ✅ Production-style architecture

---

## 📸 Demo (Add Screenshots Here)

* 📊 Dashboard UI
* 📈 PCA Visualization
* 🚨 Risk Score Distribution
* ⚡ FastAPI `/docs` endpoint

---

## 🔍 Explainability

Used **SHAP (SHapley Additive exPlanations)** to interpret model predictions and identify key behavioral features contributing to anomalies.

---

## 📉 Deep Learning Insights

Autoencoder detects anomalies using **reconstruction error**:

* Normal behavior → Low error
* Anomalous behavior → High error

---

## 🧪 How to Run

### 1️⃣ Clone Repo

```
git clone https://github.com/your-username/behavioral-anomaly-detection.git
cd behavioral-anomaly-detection
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run API

```
uvicorn api.main:app --reload
```

### 4️⃣ Run Dashboard

```
streamlit run dashboard/app.py
```

---

## 🐳 Docker Deployment

```
docker build -t anomaly-app -f docker/Dockerfile .
docker run -p 8000:8000 anomaly-app
```

---

## 📡 API Example

**POST /predict**

```
{
  "typing_speed": 220,
  "mouse_speed": 120,
  "click_rate": 6,
  "session_time": 300
}
```

---

## 📈 Results

* Successfully identifies anomalous sessions
* Demonstrates strong separation between normal and fraudulent behavior
* Supports real-time risk scoring

---

## 💼 Resume Highlights

* Built an end-to-end behavioral anomaly detection system using ML and Deep Learning
* Engineered behavioral and temporal features from interaction data
* Developed real-time API using FastAPI and deployed with Docker
* Designed interactive dashboard for anomaly visualization
* Applied statistical analysis and SHAP explainability

---

## 🔮 Future Improvements

* Real-time streaming (Kafka)
* Cloud deployment (AWS / Render)
* Graph-based anomaly detection
* Advanced sequence models (LSTM, Transformers)

---

## 👨‍💻 Author

**Rajesh Kumar**

---

## ⭐ If you found this useful, give it a star!
