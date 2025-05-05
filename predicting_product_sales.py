import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="Predicting Product Sales", layout="centered")

# Title and Introduction
st.title("📈 Predicting Product Sales")
st.markdown("""
This dashboard helps marketing managers estimate product sales based on ad spending across three key channels:

- **Affiliate Marketing**
- **Billboards**
- **Social Media**

Adjust the sliders below to simulate how spending changes impact total product sales.
""")

# Simulated dataset (based on your case study narrative)
np.random.seed(42)
n = 100
affiliate = np.random.uniform(1000, 5000, n)
billboards = np.random.uniform(1000, 5000, n)
social = np.random.uniform(1000, 5000, n)
noise = np.random.normal(0, 500, n)
sales = 3.92 * affiliate + 3.01 * billboards + 2.43 * social + noise

df = pd.DataFrame({
    "Affiliate Marketing": affiliate,
    "Billboards": billboards,
    "Social Media": social,
    "Product Sales": sales
})

# Fit regression model
X = df[["Affiliate Marketing", "Billboards", "Social Media"]]
y = df["Product Sales"]
model = LinearRegression()
model.fit(X, y)

# Sidebar sliders
st.sidebar.header("Adjust Advertising Spend ($)")
affiliate_input = st.sidebar.slider("Affiliate Marketing", 1000, 10000, 3000, step=500)
billboards_input = st.sidebar.slider("Billboards", 1000, 10000, 3000, step=500)
social_input = st.sidebar.slider("Social Media", 1000, 10000, 3000, step=500)

# Predict with new values
new_data = np.array([[affiliate_input, billboards_input, social_input]])
predicted_sales = model.predict(new_data)[0]

st.subheader("🔍 Predicted Product Sales")
st.metric(label="Total Predicted Sales", value=f"{int(predicted_sales):,} units")

# Show model coefficients
st.subheader("📊 Channel Impact (Model Coefficients)")
coef_df = pd.DataFrame({
    "Channel": ["Affiliate Marketing", "Billboards", "Social Media"],
    "Sales per $1 Spent": model.coef_
})
st.dataframe(coef_df, use_container_width=True)

# Visualization
st.subheader("📉 Predicted vs Actual Sales (Sample Data)")
df["Predicted"] = model.predict(X)

fig, ax = plt.subplots()
ax.scatter(df["Product Sales"], df["Predicted"], alpha=0.7)
ax.plot([df["Product Sales"].min(), df["Product Sales"].max()],
        [df["Product Sales"].min(), df["Product Sales"].max()],
        'r--', label="Ideal Fit")
ax.set_xlabel("Actual Sales")
ax.set_ylabel("Predicted Sales")
ax.legend()
st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("🔗 [Return to Portfolio](https://lyven81.github.io/data-analyst-portfolio/index.html)")
