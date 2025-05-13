
import streamlit as st

# --- App Configuration ---
st.set_page_config(page_title="🎯 Targeted Product Promotion Planner", layout="centered")

# --- Title ---
st.title("🎯 Targeted Product Promotion Planner")
st.markdown("Use gender-based insights to craft smarter, more effective product promotions.")

# --- User Inputs ---
gender = st.radio("Select Target Audience", ["Male", "Female", "Both"])
category = st.selectbox("Choose a Product Category", ["Snacks", "Vegetables", "Dairy", "Frozen Meals", "Bakery", "Beverages"])
budget = st.slider("Set Promotion Budget ($)", min_value=1000, max_value=50000, step=1000, value=10000)

# --- Strategy Engine ---
def get_suggestion(gender, category, budget):
    tone_map = {
        "Snacks": {"Male": "performance", "Female": "indulgent", "Both": "balanced indulgence"},
        "Vegetables": {"Male": "performance", "Female": "healthy", "Both": "well-being"},
        "Dairy": {"Male": "strength", "Female": "wellness", "Both": "daily essentials"},
        "Frozen Meals": {"Male": "quick fuel", "Female": "convenience", "Both": "time-saving"},
        "Bakery": {"Male": "hearty", "Female": "comfort", "Both": "freshly baked goodness"},
        "Beverages": {"Male": "energy", "Female": "refreshment", "Both": "hydration and energy"},
    }

    roi_estimate = {
        "Male": 1.3,
        "Female": 1.5,
        "Both": 1.2
    }

    tone = tone_map.get(category, {}).get(gender, "neutral")
    roi = round(roi_estimate[gender] * (budget / 10000), 2)

    return tone, roi

# --- Generate Results ---
tone, roi = get_suggestion(gender, category, budget)

# --- Output ---
st.markdown("### 📢 Recommendation")
st.markdown(f"**Target Gender:** {gender}")
st.markdown(f"**Category Chosen:** {category}")
st.markdown(f"**Suggested Messaging Tone:** *{tone.title()}*")
st.markdown(f"**Estimated ROI Impact:** 📈 {roi}x return on ${budget:,}")

# --- Footer ---
st.markdown("---")
st.markdown("📊 This planner simulates gender-based promotional strategy using historical trend logic.")
