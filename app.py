import streamlit as st
import pandas as pd
import numpy as np
import pickle

# 1. Load the exported machine learning assets
try:
    model = pickle.load(open('heart_model.pkl', 'rb'))
    scaler = pickle.load(open('scaler.pkl', 'rb'))
except FileNotFoundError:
    st.error("Error: Core model or scaler files are missing from the directory setup.")

# 2. Configure a clean, humanized web page layout
st.set_page_config(page_title="CardioCheck AI", page_icon="❤️", layout="centered")

st.title("❤️ CardioCheck AI: Patient Risk Assessment Platform")
st.write("Enter the patient's objective clinical measurements below to evaluate heart disease probability.")

st.markdown("---")
st.subheader("📋 Patient Clinical Metrics")

# 3. Collect UI Input fields mapping perfectly to our 13 training features
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Patient Age (Years)", min_value=1, max_value=120, value=54)
    sex = st.selectbox("Biological Sex", options=[1, 0], format_func=lambda x: "Male" if x == 1 else "Female")
    cp = st.selectbox("Chest Pain Experience Type", options=[0, 1, 2, 3], 
                      format_func=lambda x: {0: "Typical Angina", 1: "Atypical Angina", 2: "Non-Anginal Pain", 3: "Asymptomatic"}[x])
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=50, max_value=250, value=130)
    chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, value=240)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

with col2:
    restecg = st.selectbox("Resting ECG Baseline Results", options=[0, 1, 2],
                           format_func=lambda x: {0: "Normal", 1: "ST-T Wave Abnormality", 2: "Left Ventricular Hypertrophy"}[x])
    thalach = st.number_input("Maximum Heart Rate Achieved (bpm)", min_value=60, max_value=220, value=150)
    exang = st.selectbox("Exercise-Induced Angina (Chest Pain from Exertion)", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    oldpeak = st.number_input("ST Depression Induced by Exercise (oldpeak)", min_value=0.0, max_value=6.0, value=1.0, step=0.1)
    slope = st.selectbox("Slope of Peak Exercise ST Segment", options=[0, 1, 2],
                         format_func=lambda x: {0: "Upsloping", 1: "Flat", 2: "Downsloping"}[x])
    ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy", options=[0, 1, 2, 3])
    thal = st.selectbox("Thalassemia Status", options=[1, 2, 3],
                        format_func=lambda x: {1: "Normal", 2: "Fixed Defect", 3: "Reversible Defect"}[x])

st.markdown("---")

# 4. Predict and format the output when user clicks button
if st.button("Generate Diagnostic Risk Profile", use_container_width=True):
    # Construct input feature array matching the precise format expected by scikit-learn
    patient_features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    
    # Scale features identically to training setup to guarantee statistical validity
    scaled_features = scaler.transform(patient_features)
    
    # Process prediction metrics
    prediction = model.predict(scaled_features)
    risk_probability = model.predict_proba(scaled_features)[0][1] * 100
    
    # Display human-centric results based on predictive threshold
    st.subheader("📊 Diagnostic Assessment Outcome")
    if prediction[0] == 1:
        st.error(f"⚠️ **High Risk Profile Identified:** The predictive model calculates a **{risk_probability:.1f}%** probability of underlying cardiovascular disease. Clinical triage prioritization is strongly advised.")
    else:
        st.success(f"✅ **Low Risk Profile Identified:** The model calculates a **{risk_probability:.1f}%** probability of active cardiovascular issues. Standby routine preventive monitoring.")