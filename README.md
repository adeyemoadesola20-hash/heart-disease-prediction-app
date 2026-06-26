CardioCheck AI: Interactive Cardiac Risk Predictor

CardioCheck AI is an interactive, production-grade clinical web application designed to bridge the gap between machine learning models and real-world clinical utility. Built as an AnalystLab Africa Capstone project, the platform exposes a machine learning model trained on the famous UCI Cleveland Heart Disease dataset, allowing clinicians to input 13 distinct patient metrics and receive visual risk assessments in real-time.

🚀 Live Demo

Experience the interactive web application live on Hugging Face Spaces:

👉 CardioCheck AI Live Space

🛠️ Tech Stack & Architecture

Machine Learning Core: Scikit-Learn (heart_model.pkl), serialized scaling pipeline (scaler.pkl)

Data Engineering: Pandas, NumPy

Interactive UI Framework: Streamlit (Python)

Deployment Platform: Hugging Face Spaces (Cloud-hosted)

🎯 Key Engineering & Testing Milestones

This project went far beyond basic model deployment. During the validation phase, rigorous test cases were designed to audit safety, consistency, and fairness.

1. UI-to-Backend Pipeline Validation

Objective: Ensure the web form safely parses $13$ human-friendly inputs, converts categorical variables into numerical matrices, scales the array using the identical training scaler ($z = \frac{x - \mu}{\sigma}$), and generates a runtime assessment without dropping features.

Reference Output: Verbatim: Screenshot 2026-06-26 165605.png confirms clean end-to-end data processing on initialization.

2. Label Inversion Resolution

Insight: During initial testing, a class label mismatch was detected where the model output mathematically flipped the diagnostic state (e.g., classifying a severe profile as "low-risk").

Fix: Successfully implemented UI-layer correction logic ($\text{risk\_percentage} = 100 - \text{calculated\_probability}$) to realign display elements with raw clinical truth without modifying the frozen model weights.

3. Baseline Consistency & Safety Testing

Objective: Prove model stability over similar demographic cohorts to prevent diagnostic drift.

Results:

A healthy 30-year-old female baseline profile was tested: Verbatim: Screenshot 2026-06-26 170638.png yielded a low-risk score of $23.0\%$ (Green alert).

An ultra-healthy 25-year-old female baseline profile was tested: Verbatim: Screenshot 2026-06-26 171554_2.png yielded the exact same stable score of $23.0\%$ (Green alert).

A healthy 35-year-old male baseline profile: Verbatim: Screenshot 2026-06-26 181435_2.png successfully registered a low-risk baseline score of $20.0\%$ (Green alert).

4. Boundary Stress Testing (Extreme Risk)

Objective: Verify the application's ability to trigger immediate red warnings under severe multi-symptom stress.

Results: Configuring a 67-year-old male with asymptotic chest pain, flat ST segment slope, $3$ blocked vessels, and high blood pressure ($160\text{ mm Hg}$) successfully pushed the calculated risk to $61.0\%$ (Red alert).

Reference Output: Verbatim: Screenshot 2026-06-26 171144.png.

🕵️‍♂️ Advanced Audit Finding: Algorithmic Bias Detection

A major highlight of this capstone project was uncovering and documenting a demographic bias within the pre-trained UCI Cleveland ML model.

[Clinical Patient Profile: Age 65, Female, Severe Symptoms]
    ├── True Medical Risk: HIGH (Asymptomatic Chest Pain, Flat ST, High Oldpeak, Blocked Vessels)
    ├── Model Probability Output: 47.0% 
    └── Application Diagnostic Alert State: GREEN (Low Risk Profile Identified)


The Analytical Breakdown

When testing an extremely high-risk female profile (Age 65, asymptomatic chest pain, flat ST segment, $2$ blocked vessels, high cholesterol), the application registered an elevated score of $47.0\%$, remaining just under the $50\%$ decision threshold and incorrectly triggering a Green/Low Risk card (Verbatim: Screenshot 2026-06-26 181256_2.png).

Why did this happen?

Dataset Skew: The training dataset (UCI Cleveland) contains roughly twice as many male records as female records.

Feature Over-weighting: The machine learning algorithm optimized its mathematical paths by over-weighting biological sex as a diagnostic shortcut, requiring a female profile to exhibit almost absolute failure across all parameters to cross the $50\%$ threshold.

This discovery highlights the vital role of medical data auditing, demonstrating why raw accuracy metrics must be paired with demographic equity audits before models are deployed to clinical settings.

💻 Running the App Locally

To clone the repository and run the CardioCheck AI workspace locally, follow these steps:

Prerequisites

Make sure you have Python $3.9$ or higher installed on your computer.

Step 1: Clone the Repository

git clone https://github.com/SholayD/heart-disease-prediction.git
cd heart-disease-prediction


Step 2: Install Dependencies

Create a virtual environment (optional but recommended) and install the required modules:

pip install -r requirements.txt


Step 3: Launch the UI

Start the Streamlit application server:

streamlit run app.py


Your local web browser will automatically open to http://localhost:8501.

📜 License & Acknowledgments

License: This project is licensed under the MIT License - see the LICENSE file for details.

Data Source: UCI Machine Learning Repository - Cleveland Heart Disease Dataset.

Project Context: Developed as a Capstone Engineering Milestone under the AnalystLab Africa initiative.
