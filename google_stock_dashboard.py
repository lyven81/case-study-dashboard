from pathlib import Path

streamlit_code = """
import streamlit as st

st.set_page_config(page_title="📈 Google Stock Q&A", layout="centered")

st.title("📊 Smart Q&A: When to Buy or Sell Google Stock")
st.markdown("Explore what the data reveals in a fun and interactive way—even if you're not a market expert.")

st.markdown(\"\"\"
<style>
    .big-font {
        font-size: 18px !important;
    }
</style>
\"\"\", unsafe_allow_html=True)

def display_answer(button_label, answer_text):
    if st.button(button_label):
        st.markdown(f'<div class="big-font">{answer_text}</div>', unsafe_allow_html=True)

display_answer("1️⃣ What’s a 'Golden Cross,' and should I get excited?",
    "🟢 <b>Yes, it’s a good sign!</b><br>When Google’s short-term moving average rises above the long-term average, it’s called a <b>Golden Cross</b>—often signaling an upcoming uptrend."
)

display_answer("2️⃣ Why is August not my stock market bestie?",
    "🔻 <b>Because August is historically weak.</b><br>With an average return of –3.67% and the lowest trading volume, August tends to disappoint. Better wait for a rebound."
)

display_answer("3️⃣ Is it true February is a good time to sell?",
    "📈 <b>Yes!</b><br>February has one of the strongest historical returns. If you’re holding Google stock, it might be a sweet spot to cash in."
)

display_answer("4️⃣ What do earnings seasons do to stock prices?",
    "🎯 <b>They shake things up.</b><br>In January, April, July, and October, volatility spikes to 6.68%. Prices often dip around earnings—sometimes a great chance to buy."
)

display_answer("5️⃣ Can volume tell me anything useful?",
    "🔍 <b>Absolutely.</b><br>Volume spikes often happen before big price moves. When trading volume jumps, it could signal rising interest—get ready."
)

display_answer("6️⃣ Did things really change after 2019?",
    "🚀 <b>Big time!</b><br>Google’s average closing price jumped 65%, and trading volume doubled. More action, more risk—and more opportunities."
)

display_answer("7️⃣ How can I spot a market trap?",
    "⚠️ <b>Watch for the 'Death Cross'.</b><br>That’s when short-term trends fall below long-term ones. Combine it with falling volume—it might signal a downturn."
)

display_answer("8️⃣ What’s the best quarter to invest in Google?",
    "🌟 <b>Q1 shines the brightest.</b><br>January to March has the highest average return. Historically, it’s the best time to hold."
)

display_answer("9️⃣ Is it better to time entry by month?",
    "📅 <b>It helps!</b><br>Buying in August–September and selling in February–June often pays off. Past patterns show clear seasonal trends."
)

display_answer("🔟 I don’t do stats—can I still use this?",
    "🧠 <b>Yes!</b><br>We simplified the data so anyone can use it. Just follow the patterns: watch earnings months, buy the dips, sell into strength."
)

st.markdown("---")
st.caption("📘 Insights based on historical stock trends for Google (2015–2023).")
"""

Path("/mnt/data/stock_qna_dashboard.py").write_text(streamlit_code)
"/mnt/data/stock_qna_dashboard.py"

