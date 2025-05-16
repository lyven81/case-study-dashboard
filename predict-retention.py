import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Page config
st.set_page_config(page_title="🗺️ Churn Simulation Explorer", layout="centered")

# Title and intro
st.title("🗺️ Churn Simulation Explorer")
st.markdown("Simulate how customer retention changes with different location and behavior scenarios.")

# Inputs
location_context = st.radio("Choose Location Context", ["Rural", "Suburban", "Urban"], horizontal=True)
simulation_model = st.selectbox("Select Simulation Model", ["Current", "Semi-Rural", "Behavioral Shift"])

# Simulated retention rates
weeks = np.arange(1, 13)
base_rates = {
    "Rural": 0.94 - 0.002 * weeks,
    "Suburban": 0.89 - 0.003 * weeks,
    "Urban": 0.82 - 0.0045 * weeks
}

# Apply simulation logic
if simulation_model == "Current":
    simulated_rates = base_rates[location_context]
elif simulation_model == "Semi-Rural":
    simulated_rates = {
        "Urban": 0.85 - 0.003 * weeks,
        "Suburban": 0.91 - 0.0025 * weeks,
        "Rural": 0.95 - 0.0015 * weeks
    }[location_context]
elif simulation_model == "Behavioral Shift":
    simulated_rates = {
        "Urban": 0.88 - 0.002 * weeks,
        "Suburban": 0.90 - 0.002 * weeks,
        "Rural": 0.92 - 0.002 * weeks
    }[location_context]

# Plot chart
fig, ax = plt.subplots()
ax.plot(weeks, simulated_rates, marker='o', color='orange')
ax.set_ylim(0.7, 1.0)
ax.set_xticks(weeks)
ax.set_xlabel("Week")
ax.set_ylabel("Retention Rate")
ax.set_title("Projected Retention Trend")

st.pyplot(fig)

# Strategic advice
st.markdown("### 📌 Strategic Insight")
if location_context == "Urban" and simulation_model == "Current":
    st.success("🌆 Urban churn rises 8.5%—consider targeted offers.")
elif location_context == "Rural" and simulation_model == "Behavioral Shift":
    st.success("🏡 Semi-rural performs nearly as well as rural.")
elif location_context == "Suburban" and simulation_model == "Semi-Rural":
    st.info("🌳 Suburban shift yields stable retention with minor gains.")
else:
    st.info("📈 Scenario tested. Adjust dials above to explore more strategic paths.")

# Footer
st.markdown("---")
st.markdown("📊 <span style='font-size:16px;'>This dashboard simulates retention impact under various location and behavior models.</span>", unsafe_allow_html=True)
