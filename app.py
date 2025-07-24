
import streamlit as st
from card_optimizer import recommend_cards

st.title("💳 Credit Card Optimizer Agent")
st.markdown("Get the best card for your monthly spending!")

st.subheader("📊 Enter your estimated monthly spending:")

categories = ["Groceries", "Dining", "Travel", "Shopping", "Others"]
spend_dict = {}

for cat in categories:
    spend_dict[cat] = st.number_input(f"{cat} (₹)", min_value=0, value=0, step=100)

if st.button("🔍 Optimize"):
    recommendations, total_savings = recommend_cards(spend_dict)

    st.subheader("✅ Recommendations:")
    for rec in recommendations:
        st.markdown(f"- **{rec['category']}**: Use **{rec['recommended_card']}** → Save ₹{rec['estimated_saving']}")

    st.subheader("💰 Total Estimated Monthly Savings:")
    st.success(f"₹{sum(total_savings.values())}")
