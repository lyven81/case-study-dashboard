import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="From Ratings to Revenue", layout="centered")

# Title
st.title("📈 From Ratings to Revenue")
st.subheader("Unlocking Sales Growth on Shopee")

# Intro
st.markdown("""
This interactive dashboard shows how increasing customer ratings can significantly impact sales on Shopee. 
Explore how product performance evolves as ratings increase.
""")

# Simulated data
ratings = list(range(0, 11000, 500))
units_sold = [10, 30, 50, 120, 300, 700, 1200, 2400, 8000, 15000, 23000, 25000, 26000, 27000, 28000, 28500, 29000, 29500, 30000, 30500, 31000, 31500]

data = pd.DataFrame({
    'Customer Ratings': ratings[:len(units_sold)],
    'Units Sold': units_sold
})

# Line chart
st.markdown("### 📊 Units Sold vs. Customer Ratings")
fig, ax = plt.subplots()
ax.plot(data['Customer Ratings'], data['Units Sold'], marker='o', color='green')
ax.set_xlabel("Number of Customer Ratings")
ax.set_ylabel("Units Sold")
ax.set_title("Customer Ratings Influence Sales Volume")
st.pyplot(fig)

# Highlights
st.markdown("### 🔍 Key Insights")
st.markdown("""
- Every new rating adds measurable sales value.
- Big jumps in sales start around **1000 ratings**.
- **30–50 ratings** is the critical point to trigger high sales probability.
""")

# Recommendation Box
st.markdown("### 💡 Recommendations")
st.success("""
- Focus on early ratings collection (30–50 reviews).
- Promote products near 1000 ratings for breakthrough growth.
- Support product quality to sustain momentum.
""")

# Footer
st.caption("Created by Lee Yih Ven | Powered by Streamlit")

