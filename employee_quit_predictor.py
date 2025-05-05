import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

# --- Page Setup ---
st.set_page_config(page_title="Employee Quit Predictor", layout="centered")
st.title("🔍 Who’s Likely to Quit?")
st.markdown("Predict employee resignation risk using logistic regression based on demographic and work-related factors.")

# --- Input Widgets ---
st.header("Enter Employee Details")

gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 20, 60, 30)
tenure = st.slider("Years with Company", 0, 20, 2)
experience = st.slider("Years of Domain Experience", 0, 15, 2)
education = st.selectbox("Education Level", ["PhD", "Master's", "Bachelor's"])
pay_tier = st.selectbox("Salary Tier", ["Tier 1 (High)", "Tier 2 (Mid)", "Tier 3 (Low)"])
bench_status = st.selectbox("Is the employee benched?", ["Yes", "No"])
city = st.selectbox("Work Location", ["New Delhi", "Mumbai", "Pune"])

# --- Feature Engineering ---
input_data = pd.DataFrame({
    "gender": [1 if gender == "Female" else 0],
    "age": [age],
    "tenure": [tenure],
    "experience": [experience],
    "education_master": [1 if education == "Master's" else 0],
    "education_phd": [1 if education == "PhD" else 0],
    "pay_tier_2": [1 if pay_tier == "Tier 2 (Mid)" else 0],
    "pay_tier_3": [1 if pay_tier == "Tier 3 (Low)" else 0],
    "benched": [1 if bench_status == "Yes" else 0],
    "city_mumbai": [1 if city == "Mumbai" else 0],
    "city_pune": [1 if city == "Pune" else 0]
})

# --- Dummy Model (Replace with your trained model later) ---
# These coefficients are placeholder values based on case study findings.
model = LogisticRegression()
model.coef_ = np.array([[0.5, -0.3, -0.2, -0.4, 0.3, -0.5, 0.4, 0.6, 0.3, -0.2, 0.1]])
model.intercept_ = np.array([-1.2])
model.classes_ = np.array([0, 1])  # 0 = Stay, 1 = Quit

# --- Prediction ---
if st.button("Predict Resignation Risk"):
    prob = model.predict_proba(input_data)[0][1]
    st.metric("Predicted Quit Probability", f"{prob*100:.2f}%")

    if prob > 0.7:
        st.warning("⚠️ High risk of resignation. Consider taking retention action.")
    elif prob > 0.5:
        st.info("🟠 Moderate risk. Monitor and engage proactively.")
    else:
        st.success("🟢 Low risk of resignation.")
