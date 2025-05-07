import streamlit as st

st.set_page_config(layout="wide")

# Custom CSS styling
st.markdown("""
    <style>
        .big-font {
            font-size:22px !important;
        }
        .stRadio > div {
            flex-direction: row;
        }
        .question-block {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 8px rgba(0,0,0,0.05);
            margin-bottom: 30px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Google Stock Insights: Q&A Edition")
st.markdown("Get bite-sized, interactive answers based on Google stock trends from 2015 to 2023.")

questions = [
    "📈 Which month tends to have the highest average closing price?",
    "📉 When do prices usually dip, offering potential buy opportunities?",
    "📊 Is October a good month to sell?",
    "🔍 What’s special about April in terms of stock movement?",
    "💸 Do earnings months show more price spikes?",
    "📆 How does February usually perform?",
    "📉 When is a 'trap' most likely—price goes up then sharply drops?",
    "📈 When do we usually see the start of an uptrend?",
    "🧠 Are there months with both high volume and price swings?",
    "🎯 What's the best tip for someone eyeing Google stock seasonally?"
]

answers = [
    "November usually closes with the highest average price. It’s historically a strong month.",
    "August and September often see dips—smart investors keep watch for rebounds here!",
    "Yes! October often performs well, making it a potential exit point for gains.",
    "April is an earnings month—volatility is common. Watch for pre-earnings spikes.",
    "Yes. Earnings months (Jan, Apr, Jul, Oct) often bring sharp movement—great for active traders!",
    "February is historically strong. Prices are stable and often rising post-January dips.",
    "August has seen sudden spikes followed by drops. It’s a month to tread carefully.",
    "March and October sometimes show early signs of price recovery and upward trends.",
    "April and October stand out for high trading volume and bigger swings—momentum traders take note!",
    "Look for dips in late summer (Aug–Sep) and sell before year-end highs (Nov–Dec)."
]

for i in range(len(questions)):
    st.markdown(
        f"<div class='question-block'><p class='big-font'><strong>{questions[i]}</strong></p><p class='big-font'>{answers[i]}</p></div>",
        unsafe_allow_html=True
    )
