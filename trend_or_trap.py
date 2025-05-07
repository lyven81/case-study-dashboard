import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Trend or Trap Detector", layout="wide")

# Title
st.title("📊 Trend or Trap Detector")
st.subheader("Spot Golden Cross and Death Cross signals in Google Stock")

# Load data
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/lyven81/case-study-dashboard/main/trap_or_trend.csv"
    df = pd.read_csv(url, parse_dates=['Month'])
    df = df.dropna(subset=['Close'])  # Ensure clean Close prices
    df['20MA'] = df['Close'].rolling(window=20).mean()
    df['200MA'] = df['Close'].rolling(window=200).mean()
    return df

df = load_data()
df['Year'] = df['Month'].dt.year

# Year selector
years = sorted(df['Year'].dropna().unique())
selected_year = st.selectbox("Jump to Year:", years)
filtered_df = df[df['Year'] == selected_year]

# Toggle moving averages
show_20ma = st.checkbox("Overlay 20-day Moving Average", value=True)
show_200ma = st.checkbox("Overlay 200-day Moving Average", value=True)

# Detect crosses
df['Cross_Type'] = None
for i in range(1, len(df)):
    prev_20 = df.loc[i-1, '20MA']
    prev_200 = df.loc[i-1, '200MA']
    curr_20 = df.loc[i, '20MA']
    curr_200 = df.loc[i, '200MA']
    
    if pd.notna(prev_20) and pd.notna(prev_200):
        if prev_20 < prev_200 and curr_20 >= curr_200:
            df.loc[i, 'Cross_Type'] = 'Golden Cross'
        elif prev_20 > prev_200 and curr_20 <= curr_200:
            df.loc[i, 'Cross_Type'] = 'Death Cross'

# Filter crosses in selected year
crosses = df[df['Cross_Type'].notna() & (df['Year'] == selected_year)]

# Plot
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=filtered_df['Month'],
    y=filtered_df['Close'],
    mode='lines',
    name='Close Price',
    line=dict(color='gray')
))

if show_20ma:
    fig.add_trace(go.Scatter(
        x=filtered_df['Month'],
        y=filtered_df['20MA'],
        mode='lines',
        name='20-Day MA',
        line=dict(color='blue')
    ))

if show_200ma:
    fig.add_trace(go.Scatter(
        x=filtered_df['Month'],
        y=filtered_df['200MA'],
        mode='lines',
        name='200-Day MA',
        line=dict(color='orange')
    ))

for i, row in crosses.iterrows():
    color = 'green' if row['Cross_Type'] == 'Golden Cross' else 'red'
    symbol = '🔼' if row['Cross_Type'] == 'Golden Cross' else '🔽'
    fig.add_trace(go.Scatter(
        x=[row['Month']],
        y=[row['Close']],
        mode='markers+text',
        name=row['Cross_Type'],
        text=[symbol],
        textposition='top center',
        marker=dict(size=10, color=color)
    ))

fig.update_layout(
    title=f"Google Stock Trend Detection - {selected_year}",
    xaxis_title="Date",
    yaxis_title="Stock Price",
    height=600,
    legend=dict(orientation="h")
)

st.plotly_chart(fig, use_container_width=True)

# Alerts
st.markdown("### 🔍 Smart Signal Summary")
if not crosses.empty:
    for i, row in crosses.iterrows():
        symbol = "🟢" if row['Cross_Type'] == "Golden Cross" else "🔴"
        st.markdown(f"{symbol} **{row['Cross_Type']} detected in {row['Month'].strftime('%B %Y')}** — price was ${row['Close']:.2f}")
else:
    st.info("No crossover signals detected in the selected year.")

st.markdown("---")
st.markdown("📘 _This tool highlights key turning points in Google's stock trends by identifying when short-term and long-term moving averages cross each other._")
