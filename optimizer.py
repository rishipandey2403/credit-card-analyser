import pandas as pd

def recommend_cards(spend_dict, top_n=3):
    """
    Recommends the top credit cards based on user spend in each category.

    Parameters:
    - spend_dict: Dictionary with spend categories and monthly spend (e.g., {'Grocery': 5000, 'Travel': 2000, ...})
    - top_n: Number of top cards to return

    Returns:
    - Tuple: (List of recommendations, total potential annual savings)
    """

    # Load and clean data
    df = pd.read_csv("cards_data.csv")
    df.columns = df.columns.str.strip()  # Remove leading/trailing spaces
    df = df.fillna(0)  # Replace NaNs with 0

    # Normalize column names for internal use
    required_columns = ["Card Name", "Grocery %", "Travel %", "Fuel %", "Dining %", "Annual Fee"]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    recommendations = []

    for _, row in df.iterrows():
        card_name = row["Card Name"]
        annual_fee = float(row["Annual Fee"])

        # Compute annual rewards
        total_rewards = 0
        for category in ["Grocery", "Travel", "Fuel", "Dining"]:
            col_name = f"{category} %"
            spend = spend_dict.get(category.lower(), 0)
            reward_rate = float(row.get(col_name, 0)) / 100
            total_rewards += spend * reward_rate * 12  # Monthly spend * 12 months

        net_savings = total_rewards - annual_fee

        recommendations.append({
            "Card Name": card_name,
            "Annual Rewards (₹)": round(total_rewards, 2),
            "Annual Fee (₹)": annual_fee,
            "Net Savings (₹)": round(net_savings, 2)
        })

    # Sort by Net Savings descending
    sorted_cards = sorted(recommendations, key=lambda x: x["Net Savings (₹)"], reverse=True)
    top_cards = sorted_cards[:top_n]
    total_savings = round(sum(card["Net Savings (₹)"] for card in top_cards), 2)

    return top_cards, total_savings
