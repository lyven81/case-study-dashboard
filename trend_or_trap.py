
import streamlit as st

st.set_page_config(page_title="Trend or Trap Advisor", layout="centered")
st.title("📊 Trend or Trap? | Google Stock Insight Advisor")
st.markdown("Get quick insights based on typical stock trends, without needing charts or data files!")

# Q1
st.markdown("### 1. Is this daily price swing unusual?")
daily_change = st.slider("Daily % Change", -10, 10, 0)
if abs(daily_change) > 2:
    st.warning("🔺 Yes! That’s unusual. Typical daily swings are –2% to +2%. Investigate further.")
else:
    st.success("✅ Normal fluctuation. Nothing too wild here.")

# Q2
st.markdown("### 2. Is this monthly price swing a red flag?")
monthly_change = st.slider("Monthly % Change", -50, 50, 0)
if abs(monthly_change) > 15:
    st.warning("⚠️ That’s a big swing! Google usually moves 5–10% monthly.")
else:
    st.success("🟢 Within expected range.")

# Q3
st.markdown("### 3. Did the trend signal something?")
cross_event = st.radio("Did the 20-day MA cross the 200-day MA?", ["Yes - Upward", "Yes - Downward", "No Change"])
if cross_event == "Yes - Upward":
    st.success("🌟 Golden Cross spotted! Trend may be turning bullish.")
elif cross_event == "Yes - Downward":
    st.warning("⚠️ Death Cross ahead! Trend might weaken.")
else:
    st.info("🔄 No strong signal detected yet.")

# Q4
st.markdown("### 4. What’s the vibe this month?")
month = st.selectbox("Pick a month", ["January", "April", "May", "August", "October", "December"])
if month in ["January", "December"]:
    st.success("🧊 Calm and steady. Good time to review and plan.")
elif month in ["April", "August"]:
    st.warning("🔥 Watch out! These months tend to bring more volatility.")
else:
    st.info("📊 Balanced month — keep an eye but nothing extreme.")

# Q5
st.markdown("### 5. Has volume been unusually high?")
volume_spike = st.radio("Volume increased > 50% this week?", ["Yes", "No"])
if volume_spike == "Yes":
    st.warning("🔍 High volume! Look for news or earnings buzz.")
else:
    st.success("🔕 Normal trading activity.")

# Q6
st.markdown("### 6. Are we near earnings season?")
earnings_coming = st.toggle("Earnings report coming soon?")
if earnings_coming:
    st.warning("🧨 Expect price swings before and after earnings!")
else:
    st.info("🧘 Calm waters... for now.")

# Q7
st.markdown("### 7. Did we just hit an all-time high?")
all_time = st.radio("Price touched all-time high?", ["Yes", "No"])
if all_time == "Yes":
    st.warning("🚩 Be cautious — some pullbacks tend to follow highs.")
else:
    st.success("✅ Still room to grow or recover.")

# Q8
st.markdown("### 8. Are we in a sideways zone?")
flat_movement = st.slider("Flat trading days in a row", 0, 20, 3)
if flat_movement >= 10:
    st.info("⏸️ Trend paused. Breakout might be near!")
else:
    st.success("📈 Still moving — no stall yet.")

# Q9
st.markdown("### 9. Is it a good time to dollar-cost average?")
is_volatility = st.radio("Market feeling bumpy?", ["Yes", "No"])
if is_volatility == "Yes":
    st.success("📉 Great time to dollar-cost average and smooth out risk.")
else:
    st.info("⏳ Maybe hold and wait for a dip.")

# Q10
st.markdown("### 10. Should I act today?")
today_price_move = st.slider("Today's % Move", -5, 5, 0)
if abs(today_price_move) > 3:
    st.warning("🎯 Big moves today. Best not to rush decisions.")
else:
    st.success("👌 No urgency. Take your time and research.")

st.markdown("---")
st.caption("Based on trend patterns observed from 2015–2023. For educational use only.")
