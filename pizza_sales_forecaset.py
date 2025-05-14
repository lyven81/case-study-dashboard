import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- Streamlit Page Configuration ---
st.set_page_config(page_title="📈 Next Week Sales Forecaster", layout="centered")

# --- Title & Instructions ---
st.title("📈 Next Week Sales Forecaster")
st.markdown("Plan smarter for your pizza shop! This tool forecasts traffic and sales so you can schedule staff, prep ingredients, and ace delivery.")

# --- Inputs ---
week = st.slider("Select Upcoming Week (1–52)", min_value=1, max_value=52, value=25)
promotion = st.text_input("Enter Key Promotions This Week (optional)", placeholder="e.g., Buy 1 Free 1, 10% off Veggie Pizzas")
holiday_spike = st.toggle("Is this a public holiday or special weekend?")

# --- Simulated Forecast Logic ---
np.random.seed(week)
base_sales = 5500 + np.random.randint(0, 1500)
if holiday_spike:
    base_sales += 1000
lower_bound = base_sales - 500
upper_bound = base_sales + 500

# --- Output: Sales Projection ---
st.markdown("### 📊 Projected Weekly Sales")
st.markdown(f"**Estimated Range:** RM {lower_bound:,} – RM {upper_bound:,}")

# --- Simulate Traffic Heatmap Data ---
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
hours = [f"{h}:00" for h in range(10, 22)]
traffic_data = np.random.poisson(lam=20, size=(len(hours), len(days)))
if holiday_spike:
    traffic_data += np.random.poisson(lam=5, size=(len(hours), len(days)))

traffic_df = pd.DataFrame(data=traffic_data, index=hours, columns=days)

# --- Output: Heatmap ---
st.markdown("### 🔥 Hourly Traffic Heatmap")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(traffic_df, cmap="YlOrRd", linewidths=.5, annot=False, ax=ax)
ax.set_title("Expected In-Store Traffic by Hour", fontsize=14)
st.pyplot(fig)

# --- Footer ---
st.markdown("---")
st.markdown("📦 Use this forecast to align stock, staffing, and delivery hours for maximum efficiency!")
