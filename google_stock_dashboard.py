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

st.title("📈 When to Buy and Sell Google Stock: Q&A Edition")
st.markdown("Simple, data-driven insights—minus the jargon. Let’s explore!")

qna = [
    {
        "question": "Q1. What’s the best time of year to buy Google stock?",
        "answer": "📉 August and September. Historically, prices dip during these months—great for bargain hunters!"
    },
    {
        "question": "Q2. When should I think about selling?",
        "answer": "📈 February to June and again in October–November—these months show strong average returns."
    },
    {
        "question": "Q3. Why are earnings months (Jan, Apr, Jul, Oct) important?",
        "answer": "⚠️ They come with higher price swings. Be prepared for volatility, both up and down!"
    },
    {
        "question": "Q4. What month has the strongest closing price?",
        "answer": "🏆 June. It leads with an average closing price above $800!"
    },
    {
        "question": "Q5. What month typically performs the worst?",
        "answer": "😬 August. It has the lowest average return and trading volume. Approach with caution!"
    },
    {
        "question": "Q6. How do prices behave around earnings announcements?",
        "answer": "💥 They dip more than usual, offering potential short-term buy opportunities if you're watching closely."
    },
    {
        "question": "Q7. What does a spike in trading volume usually indicate?",
        "answer": "🔍 It often signals changing investor sentiment—price moves may soon follow!"
    },
    {
        "question": "Q8. What was special about Google stock after 2019?",
        "answer": "🚀 Prices jumped by 65%, but volatility doubled. It became a faster-moving market."
    },
    {
        "question": "Q9. What’s the easiest tool to spot long-term trends?",
        "answer": "📏 The 6-month moving average—it helps smooth out noise and show real direction."
    },
    {
        "question": "Q10. Any simple strategy for beginners?",
        "answer": "✅ Buy in Aug–Sep and sell into Feb–Jun strength. Use history as your compass!"
    }
]

# Render the questions and answers using expanders
for item in qna:
    with st.expander(f"{item['question']}"):
        st.markdown(f"<div class='big-answer'>{item['answer']}</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("📊 <span style='font-size:16px;'>Based on Google's stock trends from 2015 to 2023.</span>", unsafe_allow_html=True)
