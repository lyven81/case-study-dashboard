
import streamlit as st

# --- App Configuration ---
st.set_page_config(page_title="Gold Fair Value Check", layout="centered")

# --- Custom Styling ---
st.markdown("""
    <style>
        .result-box {
            background-color: #f9f9f9;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            font-size: 20px;
            margin-top: 20px;
            box-shadow: 0px 0px 5px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("💰 Is Gold Fairly Priced?")
st.markdown("Simulate and see whether gold is undervalued, overvalued, or just right based on modeled trends.")

# --- Inputs ---
current_price = st.number_input("Enter Current Gold Price ($)", min_value=100.0, max_value=25000.0, value=1950.0, step=1.0)
market_condition = st.radio("Select Market Condition", ["Normal", "Crisis"])
time_index = st.slider("Select Time Index (Week Number)", min_value=1, max_value=104, value=52)

# --- Fair Value Estimation Logic (simulated model) ---
base_price = 1800 + 2.5 * time_index  # trend line
if market_condition == "Crisis":
    fair_value = base_price - 75  # simulated dip under crisis
else:
    fair_value = base_price

# --- Price Gap Evaluation ---
price_gap = current_price - fair_value

# --- Output ---
if price_gap < -30:
    st.markdown(f"<div class='result-box' style='color:green;'>🟢 Undervalued – Potential buying opportunity!<br />Fair Value: ${fair_value:.2f}</div>", unsafe_allow_html=True)
elif -30 <= price_gap <= 30:
    st.markdown(f"<div class='result-box' style='color:orange;'>🟡 Fairly priced – Hold.<br />Fair Value: ${fair_value:.2f}</div>", unsafe_allow_html=True)
else:
    st.markdown(f"<div class='result-box' style='color:red;'>🔴 Overpriced – Consider waiting.<br />Fair Value: ${fair_value:.2f}</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.markdown("📊 <span style='font-size:16px;'>This dashboard simulates price valuation based on trend and market stress effects.</span>", unsafe_allow_html=True)
