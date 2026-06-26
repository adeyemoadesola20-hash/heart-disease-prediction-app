# ❤️ End-to-End Heart Disease Prediction Platform

An intelligent, data-driven Machine Learning web application that predicts the probability of underlying cardiovascular disease based on standard clinical patient metrics.

## 🎯 Project Overview
* **Objective:** Act as an automated medical pre-screening layer to flag high-risk individuals for clinical triage prioritization.
* **Key Focus:** Optimized specifically for **High Recall (91%)** to ensure patient safety by minimizing critical False Negatives.
* **Core Algorithm:** Random Forest Classifier Ensemble Layer.
* **Data Source:** UCI Heart Disease Dataset (Structured clinical data).

## 📊 Performance Metrics
* **Overall Model Accuracy:** 78.69%
* **Disease Present Recall:** 91.00%
* **ROC-AUC Score:** 0.8766

## 📁 Repository Structure
* `app.py`: Interactive user interface configuration built with Streamlit.
* `requirements.txt`: System library installation mapping for cloud execution.
* `heart_model.pkl`: Serialized, pre-trained Random Forest model weights.
* `scaler.pkl`: Fitted StandardScaler configuration to handle inputs safely.

## 🛠️ How to Run Locally
1. Clone this repository to your system.
2. Open your terminal inside the folder and run: `pip install -r requirements.txt`
3. Launch the web dashboard with: `streamlit run app.py`
