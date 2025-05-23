import streamlit as st
import matplotlib.pyplot as plt

# --- Page Configuration ---
st.set_page_config(page_title="Smart Growth Strategy Planner", layout="centered")

# --- Custom Style ---
st.markdown("""
    <style>
        .result-box {
            background-color: #f9f9f9;
            border-radius: 10px;
            padding: 20px;
            font-size: 18px;
            margin-top: 20px;
            text-align: center;
            box-shadow: 0px 0px 5px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("💼 Smart Growth Strategy Planner")
st.markdown("Explore how increasing headcount or improving productivity affects revenue.")

# --- Inputs ---
headcount_increase = st.slider("Increase in Headcount (%)", 0, 30, 0)
productivity_increase = st.slider("Increase in Productivity per Employee (%)", 0, 30, 0)
include_cost = st.toggle("Include Operational Cost Impact")
view_mode = st.radio("View Results As", ["Total Revenue", "Revenue per Employee"])

# --- Constants ---
base_headcount = 100
base_revenue_per_employee = 100000
base_cost_per_employee = 60000

# --- Calculations ---
# Strategy 1: Hire more people
rev_hiring = (base_headcount * (1 + headcount_increase / 100)) * base_revenue_per_employee
cost_hiring = (base_headcount * (1 + headcount_increase / 100)) * base_cost_per_employee

# Strategy 2: Improve productivity
rev_productivity = base_headcount * (base_revenue_per_employee * (1 + productivity_increase / 100))
cost_productivity = base_headcount * base_cost_per_employee

# Strategy 3: Combine both
rev_combined = (base_headcount * (1 + headcount_increase / 100)) * (base_revenue_per_employee * (1 + productivity_increase / 100))
cost_combined = (base_headcount * (1 + headcount_increase / 100)) * base_cost_per_employee

# Adjust for view mode
if view_mode == "Revenue per Employee":
    rev_hiring /= (base_headcount * (1 + headcount_increase / 100))
    rev_productivity /= base_headcount
    rev_combined /= (base_headcount * (1 + headcount_increase / 100))

# Adjust for cost if toggled
if include_cost:
    rev_hiring -= cost_hiring
    rev_productivity -= cost_productivity
    rev_combined -= cost_combined

# --- Chart ---
fig, ax = plt.subplots()
labels = ["Hiring", "Productivity", "Combined"]
revenues = [rev_hiring, rev_productivity, rev_combined]
colors = ["#007BFF", "#28a745", "#fd7e14"]
ax.bar(labels, revenues, color=colors)
ax.set_ylabel("Revenue ($)")
ax.set_title("Revenue Impact Comparison")
st.pyplot(fig)

# --- Recommendation ---
if productivity_increase > headcount_increase and productivity_increase >= 10:
    recommendation = "📈 Productivity boost alone leads to higher gains at lower cost."
elif headcount_increase > 0 and productivity_increase == 0:
    recommendation = "⚠️ Hiring alone increases cost with limited revenue gain."
elif headcount_increase > 0 and productivity_increase > 0:
    recommendation = "✅ Combining both strategies shows synergistic revenue growth."
else:
    recommendation = "ℹ️ Try adjusting sliders to simulate different growth strategies."

st.markdown(f"<div class='result-box'>{recommendation}</div>", unsafe_allow_html=True)
