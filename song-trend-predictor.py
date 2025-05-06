# file: song_trend_dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Title ---
st.title("🎵 What Makes a Song Trend?")
st.markdown("A Content Creator’s Guide Backed by 20,000 Tracks")

# --- Overview Section ---
st.header("Overview")
st.write("""
This dashboard explores how traits like **loudness**, **danceability**, and **explicit lyrics** influence song virality.
It helps content creators choose songs that are more likely to gain traction on short-form platforms like TikTok.
""")

# --- Mock Dataset ---
# Replace with real data if available
data = {
    'Trait': ['Loudness', 'Danceability', 'Explicit', 'Energy', 'Speechiness', 'Instrumentalness'],
    'Impact_on_Popularity': [0.285, 0.237, 0.198, -0.03, -0.05, -0.08]
}
df = pd.DataFrame(data)

# --- Visualization: Feature Importance ---
st.subheader("🔍 Which Traits Drive Popularity?")
fig = px.bar(df, x='Trait', y='Impact_on_Popularity', color='Trait',
             color_discrete_sequence=px.colors.qualitative.Set1,
             labels={'Impact_on_Popularity': 'Estimated Impact (%)'},
             title='Top and Bottom Traits Affecting Song Virality')
st.plotly_chart(fig, use_container_width=True)

# --- Interpretation ---
st.markdown("""
**Key Takeaways:**
- **Loudness, danceability, and explicit lyrics** have the strongest positive impact.
- Traits like **instrumentalness**, **speechiness**, and **excessive energy** may reduce virality.
- Combining high-impact traits is more effective than relying on a single feature.
""")

# --- Prediction Section ---
st.subheader("🎯 Estimate Your Song’s Potential")
st.write("Adjust the sliders to simulate a song's trait levels and estimate its popularity potential.")

# Inputs
loudness = st.slider("Loudness", 0.0, 1.0, 0.5)
danceability = st.slider("Danceability", 0.0, 1.0, 0.5)
explicit = st.slider("Explicit Content Level", 0.0, 1.0, 0.5)

# Simple prediction formula (mock logic)
predicted_popularity = (loudness * 0.285 + danceability * 0.237 + explicit * 0.198) * 100
predicted_popularity = round(predicted_popularity, 2)

# Display result
st.metric(label="🎧 Predicted Virality Score", value=f"{predicted_popularity}%", delta=None)
st.caption("Note: This estimate is illustrative and assumes traits are scaled between 0 and 1.")

# --- Footer ---
st.markdown("---")
st.caption("© 2025 Lee Yih Ven | Built with Streamlit")

