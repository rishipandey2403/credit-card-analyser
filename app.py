# app.py

import streamlit as st
from optimizer import recommend_cards

st.set_page_config(page_title="💳 Credit Card Optimizer", layout="centered")

st.title("💳 Credit Card Optimizer AI Agent")
st.markdown("#### Enter your average monthly spending:")

# Define spend categories dynamically (can be extended)
spend_categories = ["Grocery", "Travel", "Fuel", "Dining"]

spend_dict = {}
for category in spend_categories:
    spend = st.number_input(f"{category} (₹)", min_value=0, value=1000, step=100)
    spend_dict[category] = spend

if st.button("🔍 Find Best Cards"):
    recommendations = recommend_cards(spend_dict)

    st.subheader("🎯 Top Credit Card Recommendations")
    st.dataframe(recommendations.reset_index(drop=True), use_container_width=True)
