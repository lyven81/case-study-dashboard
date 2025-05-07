import streamlit as st
import pandas as pd

# Title
st.title("📈 Buy or Sell Advisor for Google Stock")
st.subheader("Personalized tips based on month, earnings cycle, and current price")

# Load dataset
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/lyven81/case-study-dashboard/main/google%20stock%20dataset.csv"
    df = pd.read_csv(url)
    df['Month'] = pd.to_datetime(df['Month'], errors='coerce')
    df = df.dropna(subset=['Month', 'Close'])  # Drop rows with missing values
    df['Month_Num'] = df['Month'].dt.month
    df['Year'] = df['Month'].dt.year
    return df

df = load_data()

# Inputs
month_name_map = {
    1: 'January', 2: 'February', 3: 'March', 4: 'April',
    5: 'May', 6: 'June', 7: 'July', 8: 'August',
    9: 'September', 10: 'October', 11: 'November', 12: 'December'
}
earnings_months = [1, 4, 7, 10]  # Jan, Apr, Jul, Oct

st.markdown("### Select Your Investment Scenario")
selected_month = st.selectbox("Which month are you considering?", list(month_name_map.values()))
current_price = st.slider("What's the current stock price?", min_value=80, max_value=160, value=120, step=1)
is_earnings = st.toggle("Is it an earnings month?", value=(list(month_name_map.values()).index(selected_month) + 1) in earnings_months)

selected_month_num = list(month_name_map.keys())[list(month_name_map.values()).index(selected_month)]

# Historical monthly average
monthly_avg = df.groupby('Month_Num')['Close'].mean().reset_index()
avg_price = monthly_avg.loc[monthly_avg['Month_Num'] == selected_month_num, 'Close'].values[0]

# Strategy engine
st.markdown("### 💡 Smart Assistant Suggestion")

def get_advice(month_num, curr_price, earnings):
    tip = ""
    emoji = ""

    if earnings:
        tip = "Earnings months often show volatility. Make sure to watch for pre-earnings price jumps or drops."
        emoji = "🔴"
    elif month_num in [2, 3, 5, 6, 11]:
        tip = "This month tends to perform well. If prices are up, it might be a good time to sell."
        emoji = "🟡"
    elif month_num in [8, 9]:
        tip = "These months usually see dips. You could find good buying opportunities here."
        emoji = "🟢"
    else:
        if curr_price < avg_price:
            tip = "The stock price is below its monthly average. Might be worth buying in."
            emoji = "🟢"
        else:
            tip = "The price is above average—consider waiting for a better entry point."
            emoji = "🟡"
    
    return f"{emoji} **{tip}**"

st.markdown(get_advice(selected_month_num, current_price, is_earnings))

# Footer
st.markdown("---")
st.markdown("📊 Based on trends observed in Google's monthly stock performance from 2015 to 2023.")
