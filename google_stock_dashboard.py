import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set title and subheader
st.set_page_config(layout="centered")
st.title("📈 When to Buy and Sell Google Stock")
st.subheader("How Data Reveals Hidden Patterns in Price and Volume")

# Load data
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/lyven81/case-study-dashboard/main/google%20stock%20dataset.csv"
    df = pd.read_csv(url)
    df['Month'] = pd.to_datetime(df['Month'], errors='coerce')
    return df.dropna(subset=['Month'])

df = load_data()

# Extract month number and name
df['Month_Num'] = df['Month'].dt.month
df['Year'] = df['Month'].dt.year

# Sidebar for user interaction
st.sidebar.header("Filter Options")
selected_years = st.sidebar.multiselect("Select Year(s):", sorted(df['Year'].unique()), default=sorted(df['Year'].unique()))
filtered_df = df[df['Year'].isin(selected_years)]

# Show raw data
if st.checkbox("Show Raw Data"):
    st.write(filtered_df)

# Moving average chart
st.markdown("### 📉 6-Month Moving Average of Closing Price")
filtered_df['6M_MA'] = filtered_df['Close'].rolling(window=6).mean()
fig1, ax1 = plt.subplots()
ax1.plot(filtered_df['Month'], filtered_df['Close'], label='Monthly Close')
ax1.plot(filtered_df['Month'], filtered_df['6M_MA'], linestyle='--', label='6-Month MA')
ax1.set_ylabel("Price ($)")
ax1.set_xlabel("Date")
ax1.set_title("Google Stock Closing Price with 6-Month Moving Average")
ax1.legend()
st.pyplot(fig1)

# Monthly percent change
st.markdown("### 📊 Monthly % Change")
filtered_df['% Change'] = filtered_df['Close'].pct_change() * 100
fig2, ax2 = plt.subplots()
ax2.plot(filtered_df['Month'], filtered_df['% Change'], color='green')
ax2.axhline(0, linestyle='--', color='gray')
ax2.set_ylabel("% Change")
ax2.set_title("Monthly % Change in Price")
st.pyplot(fig2)

# Volume over time
st.markdown("### 📦 Trading Volume Over Time")
fig3, ax3 = plt.subplots()
ax3.plot(filtered_df['Month'], filtered_df['Volume'], color='orange')
ax3.set_ylabel("Volume (Millions)")
ax3.set_title("Trading Volume")
st.pyplot(fig3)

# Seasonal closing price chart
st.markdown("### 📆 Average Closing Price by Month")
monthly_avg = df.groupby(df['Month'].dt.month)['Close'].mean().reset_index()
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_avg['Month'] = monthly_avg['Month'].apply(lambda x: month_names[x-1])
fig4, ax4 = plt.subplots()
ax4.bar(monthly_avg['Month'], monthly_avg['Close'], color='skyblue')
ax4.set_ylabel("Average Price ($)")
ax4.set_title("Average Monthly Closing Price")
st.pyplot(fig4)

# Earnings vs non-earnings months
st.markdown("### 🧾 Earnings Month Impact")
earnings_months = [1, 4, 7, 10]
df['Volatility'] = df['Close'].pct_change().abs() * 100
df['Earnings_Month'] = df['Month_Num'].apply(lambda x: 'Earnings' if x in earnings_months else 'Non-Earnings')
volatility_summary = df.groupby('Earnings_Month')['Volatility'].mean().reset_index()
volume_summary = df.groupby('Earnings_Month')['Volume'].mean().reset_index()

col1, col2 = st.columns(2)
with col1:
    st.metric("Avg Volatility - Earnings Months", f"{volatility_summary[volatility_summary['Earnings_Month']=='Earnings']['Volatility'].values[0]:.2f}%")
with col2:
    st.metric("Avg Volatility - Non-Earnings Months", f"{volatility_summary[volatility_summary['Earnings_Month']=='Non-Earnings']['Volatility'].values[0]:.2f}%")

# Buy/Sell Recommendation
st.markdown("### 💡 Buy/Sell Recommendation")
st.markdown("""
**📥 Buy in August–September**  
- Historically lower prices and low volume.
- Example: August return average is –3.67%.

**📤 Sell in February–June or October–November**  
- Historically stronger returns.
- Example: October and November average over +4% returns.
""")

# Final Tip
st.info("Use moving averages and volume spikes to plan your next move. Historical patterns can guide better timing.")
