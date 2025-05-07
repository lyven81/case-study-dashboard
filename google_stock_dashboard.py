import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("When to Buy and Sell Google Stock")
st.subheader("Data Reveals Hidden Patterns in Price and Volume")

# Load your cleaned dataset
@st.cache_data
def load_data():
    # Replace with your actual data source or upload CSV to GitHub
    url = "https://raw.githubusercontent.com/lyven81/case-study-dashboard/main/google%20stock%20dataset.csv"
    return pd.read_csv(url, parse_dates=['Month'])

# Fix datetime conversion
df['Month'] = pd.to_datetime(df['Month'], errors='coerce')

# Now extract the numeric month
df['Month_Num'] = df['Month'].dt.month

df = load_data()

# Show raw data toggle
if st.checkbox("Show raw data"):
    st.write(df)

# Moving average analysis
st.markdown("### 6-Month Moving Average vs Monthly Closing Price")
df['6M_MA'] = df['Close'].rolling(window=6).mean()

fig, ax = plt.subplots()
ax.plot(df['Month'], df['Close'], label='Monthly Close')
ax.plot(df['Month'], df['6M_MA'], label='6-Month MA', linestyle='--')
ax.set_xlabel('Date')
ax.set_ylabel('Price ($)')
ax.set_title('Google Stock Price and 6-Month Moving Average')
ax.legend()
st.pyplot(fig)

# Percent change by month
st.markdown("### Monthly Percent Change")
df['% Change'] = df['Close'].pct_change() * 100
fig2, ax2 = plt.subplots()
ax2.plot(df['Month'], df['% Change'], color='green')
ax2.axhline(0, linestyle='--', color='gray')
ax2.set_title('Monthly % Price Change')
ax2.set_ylabel('% Change')
st.pyplot(fig2)

# Volume trends
st.markdown("### Trading Volume Over Time")
fig3, ax3 = plt.subplots()
ax3.plot(df['Month'], df['Volume'], color='orange')
ax3.set_title("Google Stock Trading Volume")
ax3.set_ylabel("Volume (Millions)")
st.pyplot(fig3)

# Seasonal insight
st.markdown("### Average Closing Price by Month")
df['Month_Num'] = df['Month'].dt.month
monthly_avg = df.groupby('Month_Num')['Close'].mean().reset_index()
month_map = {
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
}
monthly_avg['Month'] = monthly_avg['Month_Num'].map(month_map)

fig4, ax4 = plt.subplots()
ax4.bar(monthly_avg['Month'], monthly_avg['Close'], color='skyblue')
ax4.set_title('Average Monthly Closing Price')
ax4.set_ylabel('Average Price ($)')
st.pyplot(fig4)

# Final takeaway
st.markdown("---")
st.markdown("📌 **Investor Tip:**")
st.markdown("- August–September often present buying opportunities.")
st.markdown("- February–June and October–November are usually good selling windows.")
st.markdown("- Watch for volume spikes ahead of price changes.")

