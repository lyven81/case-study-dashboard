
import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="📈 Growth Tracker", layout="centered")

# --- Title ---
st.title("📈 Growth Tracker: Is It Time to Buy or Hold?")
st.markdown("Simulate different market scenarios and get instant guidance on Microsoft stock trends!")

# --- Inputs ---
st.markdown("### Set Your Scenario")

open_price = st.slider("Current Open Price ($)", min_value=100, max_value=400, value=250, step=1)

market_condition = st.selectbox("Market Condition", ["Normal", "COVID-like", "Crisis"])

in_growth_phase = st.toggle("Is it a Growth Phase?", value=True)

# --- Logic for Predicted Close Price ---
# These coefficients are hypothetical for demo purposes.
base_close = open_price * 1.02

if market_condition == "Normal":
    adjustment = 1.00
elif market_condition == "COVID-like":
    adjustment = 0.95
else:  # Crisis
    adjustment = 0.90

if in_growth_phase:
    growth_factor = 1.05
else:
    growth_factor = 0.98

predicted_close = round(base_close * adjustment * growth_factor, 2)
historical_avg_close = 260  # Placeholder average

# --- Output ---
st.markdown("### 📊 Prediction Result")

st.metric(label="📉 Predicted Close Price", value=f"${predicted_close}")

# --- Comparison to Historical Average ---
st.markdown("### 📌 Smart Insight")

if predicted_close < historical_avg_close * 0.95:
    st.success("💹 Looks like a buy opportunity! Price is likely undervalued.")
elif predicted_close > historical_avg_close * 1.05:
    st.warning("⚠️ Wait it out—price likely inflated above trend.")
else:
    st.info("📎 Fair value zone. Hold or monitor for better timing.")

# --- Footer ---
st.markdown("---")
st.markdown("📘 Based on historical trends from Microsoft stock between 2000–2023. This simulation is for learning purposes only.")
