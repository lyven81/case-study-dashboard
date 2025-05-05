import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

# ----- Sample training logic -----
# Simulated dataset for demonstration purposes
# In production, replace this with your real trained model

# Generate sample data
np.random.seed(0)
X = np.random.rand(500, 4)
y = (X[:, 0] * 2 + X[:, 1] * 1.5 + X[:, 2] + X[:, 3] * 0.5 > 2.2).astype(int)

# Fit logistic regression model
model = LogisticRegression()
model.fit(X, y)

# ----- Streamlit App -----
st.set_page_config(page_title="Student Depression Risk Predictor", layout="centered")
st.title("🎓 Student Depression Risk Predictor")
st.write("Use this tool to estimate the risk of depression in students based on lifestyle and stress factors.")

st.header("🔍 Input Student Factors")

academic_pressure = st.slider("Academic Pressure (1 = Low, 10 = High)", 1, 10, 5)
financial_stress = st.slider("Financial Stress (1 = Low, 10 = High)", 1, 10, 5)
study_hours = st.slider("Study/Work Hours per Day", 0, 16, 8)
diet_score = st.slider("Dietary Habits (1 = Poor, 10 = Healthy)", 1, 10, 5)

# Reverse diet score to match "poor diet = higher risk"
poor_diet_score = 11 - diet_score

# Make prediction
input_data = np.array([[academic_pressure / 10, financial_stress / 10, study_hours / 16, poor_diet_score / 10]])
prediction_proba = model.predict_proba(input_data)[0][1] * 100

st.subheader("📊 Predicted Risk")
st.write(f"Estimated probability of depression: **{prediction_proba:.2f}%**")

# Risk level
if prediction_proba > 85:
    st.error("🚨 High Risk – Immediate support recommended.")
elif prediction_proba > 60:
    st.warning("⚠️ Moderate Risk – Monitor and consider support.")
else:
    st.success("✅ Low Risk – Continue general wellness monitoring.")

# Explanation
st.markdown("---")
st.markdown("**Explanation:** This model estimates the likelihood that a student may be facing depression based on key stress and lifestyle indicators. While not a diagnosis tool, it provides early warning signs for prioritizing support.")

st.caption("Model trained using logistic regression. Sample data is for demonstration only.")
