import streamlit as st
from optimizer import recommend_cards

st.set_page_config(page_title="Credit Card Optimizer", layout="centered")

st.title("💳 Credit Card Optimizer")
st.markdown("#### Find the best card based on your monthly spending in different categories.")

# Collect user input
st.sidebar.header("Enter Your Monthly Spend (₹)")
grocery_spend = st.sidebar.number_input("Grocery", min_value=0, value=3000)
travel_spend = st.sidebar.number_input("Travel", min_value=0, value=2000)
fuel_spend = st.sidebar.number_input("Fuel", min_value=0, value=1000)
dining_spend = st.sidebar.number_input("Dining", min_value=0, value=1500)
top_n = st.sidebar.slider("Number of Top Cards to Show", 1, 10, 3)

# When the user clicks the button
if st.button("🔍 Recommend Best Cards"):
    # Prepare the spend dictionary
    spend_dict = {
        "grocery": grocery_spend,
        "travel": travel_spend,
        "fuel": fuel_spend,
        "dining": dining_spend
    }

    try:
        recommendations, total_savings = recommend_cards(spend_dict, top_n=top_n)

        if recommendations:
            st.success(f"🎯 Potential annual savings: ₹{total_savings}")

            st.markdown("### 💡 Top Recommended Cards")
            st.table(recommendations)
        else:
            st.warning("No suitable cards found. Try adjusting your spends.")

    except Exception as e:
        st.error(f"Something went wrong: {e}")
