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

st.title("💎 Beyond the Buzzwords: Keyword Q&A")
st.markdown("Explore what really drives jewelry ad performance through 10 fun and interactive questions! 💬")

qna = [
    {
        "question": "Q1. Which keywords are safe bets for always-on jewelry ads?",
        "answer": "✅ <b>Minimalistic Jewelry</b> and <b>Multi-strand Necklaces</b>—they deliver consistent results with no major drop-offs."
    },
    {
        "question": "Q2. Which keyword had a 625% jump in engagement?",
        "answer": "🔥 <b>Colorful Jewelry</b>—a rising star! Its massive growth signals it’s time to feature it in upcoming campaigns."
    },
    {
        "question": "Q3. What’s the deal with Baroque Jewelry?",
        "answer": "🚧 It looked great at first but fizzled out fast. High visibility, low clicks. Time to pause or rethink the strategy."
    },
    {
        "question": "Q4. When should you promote Vintage and Artisan Jewelry?",
        "answer": "📅 <b>Weekdays</b>! These classic styles appeal more to weekday shoppers, especially those browsing during lunch breaks."
    },
    {
        "question": "Q5. What styles should dominate weekend promotions?",
        "answer": "🎉 <b>Boho</b> and <b>Layered Jewelry</b>—relaxed and fun styles that resonate more on Friday to Sunday."
    },
    {
        "question": "Q6. Which keywords are gaining momentum you shouldn’t ignore?",
        "answer": "📈 <b>Everyday Jewelry</b> (+320%), <b>Bold Jewelry</b> (+250%), plus surges in <b>Fashion Brooches</b> and <b>Ear Cuffs</b>."
    },
    {
        "question": "Q7. Which ad platform delivered the highest ROAS?",
        "answer": "💰 <b>Facebook Ads</b>—especially for <b>Fall Jewelry</b> (ROAS 34.88) and <b>Body Jewelry</b> (ROAS 32.20)."
    },
    {
        "question": "Q8. Which styles shine best on DV360?",
        "answer": "🖼️ <b>Animal Jewelry</b>, <b>Cocktail Rings</b>, and <b>Festival Jewelry</b>—bold and great for visual display ads."
    },
    {
        "question": "Q9. What kind of keywords perform better on Google Ads?",
        "answer": "🔍 <b>Modern Jewelry</b> and <b>Crystal Jewelry</b>—they match buyer intent and work well with product search ads."
    },
    {
        "question": "Q10. What's one smart tip to stretch every ad dollar?",
        "answer": "🎯 Focus spend on <b>reliable performers</b>, <b>emerging trends</b>, and <b>high-ROAS combos</b> instead of spreading too thin."
    },
]

for item in qna:
    with st.expander(f"{item['question']}"):
        st.markdown(f"<div class='big-answer'>{item['answer']}</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("📊 <span style='font-size:16px;'>Based on findings from a multi-platform jewelry keyword performance analysis.</span>", unsafe_allow_html=True)
