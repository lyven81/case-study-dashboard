import streamlit as st

# Page configuration
st.set_page_config(page_title="Margin vs Volume", layout="centered")
st.title("📈 Margin or Volume: Which Drives Sales Growth More Effectively?")
st.markdown("This interactive dashboard uses a regression model to estimate how price and quantity impact total revenue.")

# Regression equation
# Total Revenue = 299.28 × Quantity + 2.80 × Price − 840.48

st.header("📊 Input Price and Quantity")
price = st.number_input("Unit Price", min_value=0.0, value=100.0, step=1.0)
quantity = st.number_input("Quantity Sold", min_value=0, value=10, step=1)

# Optional: compare to actual revenue
actual_revenue = st.number_input("Actual Revenue (optional)", min_value=0.0, value=0.0, step=1.0)

# Calculate predicted revenue
predicted_revenue = 299.28 * quantity + 2.80 * price - 840.48
st.metric(label="Predicted Total Revenue", value=f"${predicted_revenue:,.2f}")

# Show difference if actual revenue is entered
if actual_revenue > 0:
    difference = actual_revenue - predicted_revenue
    if abs(difference) < 1:
        st.success("✅ Your actual revenue closely matches the predicted value.")
    elif difference > 0:
        st.info(f"📈 Your actual revenue is **${difference:,.2f}** higher than predicted.")
    else:
        st.warning(f"📉 Your actual revenue is **${abs(difference):,.2f}** lower than predicted.")

# Insights section
st.markdown("---")
st.subheader("💡 Insights")
st.markdown("""
- Increasing **quantity sold** has a stronger, more stable impact on total revenue.
- **Price changes** lead to larger swings in revenue but may not scale as predictably.
- Consider using **volume-based strategies** (e.g., bundling, upselling) while applying **targeted pricing** to premium products.
""")
