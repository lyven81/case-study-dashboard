import streamlit as st

# Custom CSS for larger font sizes
st.markdown("""
    <style>
        .big-question {
            font-size: 20px !important;
            font-weight: 600;
        }
        .big-answer {
            font-size: 18px !important;
            font-weight: 400;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Trend or Trap: Learn with Q&A")
st.markdown("Welcome to your interactive Google Stock crash course. Let's see what you've got! 💥")

qna = [
    {
        "question": "Q1. What does it mean when the price crosses above the 200-day average?",
        "answer": "That's a classic <b>Golden Cross</b>! It often signals the start of a potential uptrend—investors take this as a bullish sign. 📈"
    },
    {
        "question": "Q2. What should you watch for when the price drops below the 200-day average?",
        "answer": "That's a <b>Death Cross</b>, a potential warning sign of a downturn. Time to get cautious. 🚨"
    },
    {
        "question": "Q3. Is high trading volume always a good sign?",
        "answer": "Not necessarily. High volume during a price rise suggests strong momentum. But high volume during a drop could signal panic selling. Context matters! 🔍"
    },
    {
        "question": "Q4. Why do earnings months matter?",
        "answer": "Google’s stock shows big swings in <b>January, April, July, and October</b>—earnings season! Expect volatility whether good or bad. ⚖️"
    },
    {
        "question": "Q5. Which month historically offers the best 'buy the dip' opportunity?",
        "answer": "<b>August and September</b> often see lower prices. If you’re bargain hunting, they’re your friends. 🛒"
    },
    {
        "question": "Q6. When might be a good time to sell?",
        "answer": "Historically, <b>February through June</b> and <b>October–November</b> show strong price growth—ideal months to lock in profits. 💰"
    },
    {
        "question": "Q7. What's a healthy price trend?",
        "answer": "When short-term averages (20-day) rise steadily above long-term ones (200-day), it's a sign of consistent momentum—not just a spike. 📈"
    },
    {
        "question": "Q8. How can I tell if it’s just hype?",
        "answer": "If the price jumps up quickly but volume is flat, the trend might be weak or unsustainable. Be skeptical. 🤔"
    },
    {
        "question": "Q9. What’s the danger of ignoring moving averages?",
        "answer": "You might mistake a temporary spike for a real trend or miss warning signs of a downturn. Averages smooth the noise. 🎯"
    },
    {
        "question": "Q10. What’s your one-line advice for timing trades?",
        "answer": "<b>Let the trend confirm the story.</b> Use patterns, volume, and average lines to decide—not just the headline news. 🧠"
    },
]

for item in qna:
    with st.expander(f"{item['question']}"):
        st.markdown(f"<div class='big-answer'>{item['answer']}</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("📊 <span style='font-size:16px;'>Based on Google's stock trends from 2015 to 2023.</span>", unsafe_allow_html=True)
