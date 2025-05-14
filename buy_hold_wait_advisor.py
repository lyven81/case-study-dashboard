
import streamlit as st

# Page setup
st.set_page_config(page_title="📊 Buy-Hold-Wait Advisor", layout="centered")

# Styling
st.markdown("""
    <style>
        .result-box {
            background-color: #f9f9f9;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            font-size: 20px;
            margin-top: 20px;
            box-shadow: 0px 0px 8px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("📊 Buy-Hold-Wait Advisor")
st.markdown("Simulate stock decision-making with a smart assistant using trend, price, and market phase.")

# User Inputs
current_price = st.number_input("Enter Current Stock Price ($)", min_value=1.0, max_value=5000.0, value=300.0, step=1.0)
market_phase = st.radio("Select Market Phase", ["Uptrend", "Volatile", "Plateau"])
week_index = st.slider("Select Week Index (1–52)", min_value=1, max_value=52, value=26)

# Simulated prediction model
# Coefficients are arbitrary for demonstration
base_price = 250
open_price = 280
volume = 1000000
trend_score = week_index

# Simulate impact by phase
if market_phase == "Uptrend":
    predicted_value = base_price + 0.3 * open_price + 1.2 * trend_score + 0.00001 * volume
elif market_phase == "Volatile":
    predicted_value = base_price + 0.25 * open_price + 0.6 * trend_score + 0.000005 * volume
else:  # Plateau
    predicted_value = base_price + 0.2 * open_price + 0.3 * trend_score + 0.000002 * volume

# Decision logic
price_gap = current_price - predicted_value

if price_gap < -10:
    st.markdown(f"<div class='result-box' style='color:green;'>🟢 Buy – undervalued!<br/>Fair Value Estimate: ${predicted_value:.2f}</div>", unsafe_allow_html=True)
elif -10 <= price_gap <= 10:
    st.markdown(f"<div class='result-box' style='color:orange;'>🟡 Hold – fairly priced.<br/>Fair Value Estimate: ${predicted_value:.2f}</div>", unsafe_allow_html=True)
else:
    st.markdown(f"<div class='result-box' style='color:red;'>🔴 Wait – currently overpriced.<br/>Fair Value Estimate: ${predicted_value:.2f}</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("📈 <span style='font-size:16px;'>Powered by a simulated regression model using open price, time index, volume, and market cycle.</span>", unsafe_allow_html=True)
