import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dashboard title
st.title("🌍 Can Money Buy Happiness?")
st.subheader("Explore how GDP and personal freedom affect national happiness.")

# Sidebar inputs
st.sidebar.header("Input Parameters")
gdp = st.sidebar.slider("GDP per Capita (normalized scale)", 0.0, 2.5, 1.0, step=0.01)
freedom = st.sidebar.slider("Freedom to Make Life Choices", 0.0, 1.0, 0.5, step=0.01)

# Regression formula from your case study
happiness_score = 1.89 * gdp + 2.41 * freedom

# Display prediction result
st.metric(label="Predicted Happiness Score", value=round(happiness_score, 2))

# Explanation text
st.markdown("""
**Interpretation:**  
This estimated score reflects how financial stability and personal autonomy influence well-being at a national level.  
The model explains about 71% of variation in global happiness scores.

> ✅ *Try adjusting GDP and freedom to see how they change the happiness score.*
""")

# Optional sample chart
chart_data = pd.DataFrame({
    "GDP per Capita": np.linspace(0.1, 2.5, 50),
    "Freedom": [freedom]*50,
})
chart_data["Predicted Happiness"] = 1.89 * chart_data["GDP per Capita"] + 2.41 * chart_data["Freedom"]

st.line_chart(chart_data.rename(columns={"GDP per Capita": "index"}).set_index("index"))
